import os
from .ciSystem import CiSystem
from .cookLang import CookLang
from .cookDocs import CookDocs
from .cookDocsImages import CookDocsImages
import shutil

class Docs:
	def __init__(self) -> None:
		self.systemType = self.setupEnv()
		print(self.systemType, os.getenv('CI_SYSTEM_OVERRIDE'), os.getenv('CF_PAGES'), os.getenv('GITHUB_ACTIONS'), flush=True)
		CookLang()
		CookDocs()
		CookDocsImages()
		# self.ciTweaks()
		self.generate()
		self.siteExtraConfig()
	
	def setupEnv(self) -> CiSystem:
		if (os.getenv('CI_SYSTEM_OVERRIDE') != None and int(os.getenv('CI_SYSTEM_OVERRIDE')) >= 0):
			return CiSystem(int(os.getenv('CI_SYSTEM_OVERRIDE')))
		else:
			if (os.getenv('CF_PAGES') != None and int(os.getenv('CF_PAGES')) == 1):
				return CiSystem.CLOUDFLARE
			elif (os.getenv('GITHUB_ACTIONS') != None and bool(os.getenv('GITHUB_ACTIONS')) == True):
				return CiSystem.GITHUB

	def ciTweaks(self) -> None:
		with open('mkdocs.yml', 'r') as mkdocsConfigFile:
			self.mkdocsConfig = mkdocsConfigFile.read()

		with open('mkdocs.yml', 'w') as mkdocsConfigFile:
			mkdocsConfigFile.write(self.mkdocsConfig)
	
	def generate(self) -> None:
		if self.systemType == CiSystem.CLOUDFLARE:
			subcommand = 'build'
		elif self.systemType == CiSystem.GITHUB:
			subcommand = 'gh-deploy --force'
		
		print('running: ', f'mkdocs {subcommand}', flush=True)
		runDocsAttempt = os.system(f"mkdocs {subcommand}")
		if runDocsAttempt != 0:
			raise Exception(f"mkdocs exited with code: {runDocsAttempt}")

	def siteExtraConfig(self) -> None:
		if self.systemType == CiSystem.CLOUDFLARE:
			shutil.move('./_headers', './site/_headers')