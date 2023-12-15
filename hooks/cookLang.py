from hashlib import sha256
from io import DEFAULT_BUFFER_SIZE
from pathlib import Path
from tarfile import open as tarOpen
from urllib.parse import ParseResult, urlparse

from ghapi.all import GhApi
from mkdocs.config.defaults import MkDocsConfig
from requests import get

class CookLang:
	def __init__(self) -> None:
		self.download(self.getDownloadLink())

	def getDownloadLink(self) -> dict[str, ParseResult]:
		url_dict: dict[str, ParseResult] = {}
		found_archive = False
		found_hash = False
		ghAssets = GhApi().repos.get_latest_release('cooklang', 'CookCLI').assets
		for ghAsset in ghAssets:
			if ghAsset.name == 'cook-x86_64-unknown-linux-gnu.tar.gz':
				url_dict["archive"] = urlparse(ghAsset.browser_download_url)
				found_archive = True
			elif ghAsset.name == 'cook-x86_64-unknown-linux-gnu.tar.gz.sha256':
				url_dict["hash"] = urlparse(ghAsset.browser_download_url)
				found_hash = True

			if found_archive and found_hash:
				break

		return url_dict

	def download(self, downloadUrls: dict[str, ParseResult]) -> None:
		archiveDownloadUrl = downloadUrls["archive"]
		archiveFileLocation = Path(Path(archiveDownloadUrl.path).name)
		with get(archiveDownloadUrl.geturl(), stream=True) as downloadAttempt:
			with open(archiveFileLocation, "wb") as archiveFile:
				for chunk in downloadAttempt.iter_content(chunk_size=DEFAULT_BUFFER_SIZE):
					if chunk:
						archiveFile.write(chunk)
		print(f"Downloaded {archiveDownloadUrl.geturl()} to {archiveFileLocation.resolve().relative_to(Path.cwd())}")

		hashDownloadUrl = downloadUrls["hash"]
		hashFileLocation = Path(Path(hashDownloadUrl.path).name)
		with get(hashDownloadUrl.geturl(), stream=True) as downloadAttempt:
			with open(hashFileLocation, "wb") as hashFile:
				for chunk in downloadAttempt.iter_content(chunk_size=DEFAULT_BUFFER_SIZE):
					if chunk:
						hashFile.write(chunk)
		print(f"Downloaded {hashDownloadUrl.geturl()} to {hashFileLocation.resolve().relative_to(Path.cwd())}")

		self.hashVerify(archiveLocation=archiveFileLocation, sha256Location=hashFileLocation)

	def hashVerify(self, archiveLocation: Path, sha256Location: Path) -> None:
		# Read the expected hash from the hash file
		with open(sha256Location, 'r') as hashFile:
			expected_hash = hashFile.read().strip()

		# Compute the SHA256 hash of the archive
		hasher = sha256()
		with open(archiveLocation, 'rb') as archiveFile:
			while chunk := archiveFile.read(DEFAULT_BUFFER_SIZE):
				hasher.update(chunk)
		computed_hash = hasher.hexdigest()

		# Compare the hashes
		if computed_hash == expected_hash:
			print("Hash verified.")
			self.unarchive(archiveLocation)
		else:
			raise ValueError(f"Hash verification failed. Download {computed_hash} vs expected {expected_hash}")

	def unarchive(self, archiveLocation: Path) -> None:
		with tarOpen(archiveLocation, 'r:gz') as tar:
			tar.extractall(path=archiveLocation.parent)
			print(f"Unzipped {len(tar.getnames())} file(s) from {archiveLocation.resolve().relative_to(Path.cwd())} to {archiveLocation.parent.resolve().relative_to(Path.cwd())}")

		self.delArchive(archiveLocation)

	def delArchive(self, archiveLocation: Path) -> None:
		archiveLocation.unlink()
		print(f"Deleted {archiveLocation}")

def on_config(config: MkDocsConfig) -> MkDocsConfig | None:
	CookLang()
