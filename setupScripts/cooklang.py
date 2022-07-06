from ghapi.all import GhApi
import re
import os
from pathlib import Path

class CookLang:
	def __init__(self) -> None:
		self.download()

	def download(self):
		ghAssets = GhApi().repos.get_latest_release('cooklang', 'CookCLI').assets
		for ghAsset in ghAssets:
			if re.search('CookCLI_\d+\.\d+\.\d+_linux_amd64\.zip', ghAsset.name):
				fileName = Path(ghAsset.browser_download_url).name
				downloadAttempt = os.system(f"wget -nv {ghAsset.browser_download_url} -O {fileName}")
				if downloadAttempt != 0:
					raise Exception(f"wget exited with code: {downloadAttempt}")
				unzipAttempt = os.system(f"unzip -o {fileName}")
				if unzipAttempt != 0:
					raise Exception(f"unzip exited with code: {unzipAttempt}")