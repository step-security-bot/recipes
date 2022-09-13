from ghapi.all import GhApi
import re
import subprocess
from pathlib import Path

class CookLang:
	def __init__(self) -> None:
		self.download(self.getDownloadLink())
		self.unzip()
		self.delzip()

	def getDownloadLink(self) -> str:
		ghAssets = GhApi().repos.get_latest_release('cooklang', 'CookCLI').assets
		for ghAsset in ghAssets:
			if re.search('CookCLI_\d+\.\d+\.\d+_linux_amd64\.zip', ghAsset.name):
				return ghAsset.browser_download_url
	
	def download(self, downloadUrl:str) -> None:
		self.zipFileName = Path(downloadUrl).name
		downloadAttempt = subprocess.run(["wget", "-nv", downloadUrl, "-O", self.zipFileName], capture_output=True, check=True, text=True)
		print(downloadAttempt.stdout, flush=True)
		print(downloadAttempt.stderr, flush=True)
	
	def unzip(self) -> None:
		unzipAttempt = subprocess.run(["unzip", "-o", self.zipFileName], capture_output=True, check=True, text=True)
		print(unzipAttempt.stdout, flush=True)
		print(unzipAttempt.stderr, flush=True)
	
	def delzip(self) -> None:
		delzipAttempt = subprocess.run(["rm", "-v", self.zipFileName], capture_output=True, check=True, text=True)
		print(delzipAttempt.stdout, flush=True)
		print(delzipAttempt.stderr, flush=True)