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
		subprocess.run(["wget", "-nv", downloadUrl, "-O", self.zipFileName], capture_output=True, check=True, text=True)
	
	def unzip(self) -> None:
		subprocess.run(["unzip", "-o", self.zipFileName], capture_output=True, check=True, text=True)
	
	def delzip(self) -> None:
		subprocess.run(["rm", "-v", self.zipFileName], capture_output=True, check=True, text=True)