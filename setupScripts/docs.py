import os
from .cooklang import CookLang
from .cookdocs import CookDocs

class Docs:
	def __init__(self) -> None:
		CookLang()
		CookDocs()
		self.generate()
	
	def generate(self) -> None:
		if (os.getenv('GITHUB_ACTIONS') != None and bool(os.getenv('GITHUB_ACTIONS')) == True):
			runDocsAttempt = os.system('mkdocs gh-deploy')
			if runDocsAttempt != 0:
				raise Exception(f"mkdocs exited with code: {runDocsAttempt}")
		elif (os.getenv('CF_PAGES') != None and int(os.getenv('CF_PAGES')) == 1):
			runDocsAttempt = os.system('mkdocs build')
			if runDocsAttempt != 0:
				raise Exception(f"mkdocs exited with code: {runDocsAttempt}")