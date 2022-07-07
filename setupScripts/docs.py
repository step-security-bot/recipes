import os
from .cooklang import CookLang
from .cookdocs import CookDocs

class Docs:
	def __init__(self) -> None:
		CookLang()
		CookDocs()
		
		if (os.getenv('CF_PAGES') != None and int(os.getenv('CF_PAGES')) == 1):
			# Running in Cloudflare Pages
			self.runMkDocs()
	
	def runMkDocs(self) -> None:
		runDocsAttempt = os.system('mkdocs build')
		if runDocsAttempt != 0:
			raise Exception(f"mkdocs exited with code: {runDocsAttempt}")