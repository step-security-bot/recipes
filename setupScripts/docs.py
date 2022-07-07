import os
from .cooklang import CookLang
from .cookdocs import CookDocs

class Docs:
	def __init__(self) -> None:
		# GitHub specific commands only
		print(f"GitHub Actions is: {os.getenv('GITHUB_ACTIONS')}")
		CookLang()
		CookDocs()
		# Cloudflare specific commands only
		if (os.getenv('CF_PAGES') != None and int(os.getenv('CF_PAGES')) == 1):
			self.runMkDocs()
	
	def runMkDocs(self) -> None:
		runDocsAttempt = os.system('mkdocs build')
		if runDocsAttempt != 0:
			raise Exception(f"mkdocs exited with code: {runDocsAttempt}")