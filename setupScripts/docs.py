import os
from .cooklang import CookLang
from .cookdocs import CookDocs

class Docs:
	def __init__(self) -> None:
		CookLang()
		CookDocs()
		self.ciTweaks()
		self.generate()
	
	def ciTweaks(self) -> None:
		with open('mkdocs.yml', 'r') as mkdocsConfigFile:
			self.mkdocsConfig = mkdocsConfigFile.read()

		if (os.getenv('GITHUB_ACTIONS') != None and bool(os.getenv('GITHUB_ACTIONS')) == True):
			self.mkdocsConfig.replace('https://recipes.demosjarco.dev', 'https://demosjarco.github.io/recipes')
			self.mkdocsConfig.replace('CF_PAGES', 'GITHUB_ACTIONS')

		with open('mkdocs.yml', 'w') as mkdocsConfigFile:
			mkdocsConfigFile.write(self.mkdocsConfig)
	
	def generate(self) -> None:
		if (os.getenv('GITHUB_ACTIONS') != None and bool(os.getenv('GITHUB_ACTIONS')) == True):
			subcommand = 'gh-deploy'
		elif (os.getenv('CF_PAGES') != None and int(os.getenv('CF_PAGES')) == 1):
			subcommand = 'build'
		
		runDocsAttempt = os.system(f"mkdocs {subcommand}")
		if runDocsAttempt != 0:
			raise Exception(f"mkdocs exited with code: {runDocsAttempt}")