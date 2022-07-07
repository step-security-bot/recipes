from ghapi.all import GhApi
import re
import os
from pathlib import Path

class CookLang:
	def __init__(self) -> None:
		self.download(self.getDownloadLink())
		self.unzip()

	def getDownloadLink(self) -> str:
		ghAssets = GhApi().repos.get_latest_release('cooklang', 'CookCLI').assets
		for ghAsset in ghAssets:
			if re.search('CookCLI_\d+\.\d+\.\d+_linux_amd64\.zip', ghAsset.name):
				return ghAsset.browser_download_url
	
	def download(self, downloadUrl:str) -> None:
		self.zipFileName = Path(downloadUrl).name
		downloadAttempt = os.system(f"wget -nv {downloadUrl} -O {self.zipFileName}")
		if downloadAttempt != 0:
			raise Exception(f"wget exited with code: {downloadAttempt}")
	
	def unzip(self) -> None:
		unzipAttempt = os.system(f"unzip -o {self.zipFileName}")
		if unzipAttempt != 0:
			raise Exception(f"unzip exited with code: {unzipAttempt}")