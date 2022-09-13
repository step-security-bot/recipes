import os
import subprocess
from .ciSystem import CiSystem
from .cookLang import CookLang
from .cookDocs import CookDocs
from .cookDocsImages import CookDocsImages
from .lessCompiler import LessCompiler
import shutil

class Docs:
	def __init__(self) -> None:
		self.systemType = self.setupEnv()
		self.systemDebug()
		CookLang()
		CookDocs()
		CookDocsImages()
		LessCompiler()
		# self.ciTweaks()
		self.generate()
		self.siteExtraConfig()
	
	def setupEnv(self) -> CiSystem:
		if (os.getenv('CI_SYSTEM_OVERRIDE') != None and int(os.getenv('CI_SYSTEM_OVERRIDE')) >= 0):
			return CiSystem(int(os.getenv('CI_SYSTEM_OVERRIDE')))
		else:
			if (os.getenv('CF_PAGES') != None and int(os.getenv('CF_PAGES')) == 1):
				# Install node packages since CF only installs python packages by default
				subprocess.run(["npm", "ci", "--production=false"], capture_output=True, check=True, text=True)
				return CiSystem.CLOUDFLARE
			elif (os.getenv('GITHUB_ACTIONS') != None and bool(os.getenv('GITHUB_ACTIONS')) == True):
				return CiSystem.GITHUB
	
	def systemDebug(self) -> None:
		print('Detected CI system', self.systemType, flush=True)
		print('CI_SYSTEM_OVERRIDE', os.getenv('CI_SYSTEM_OVERRIDE'), flush=True)
		print('CF_PAGES', os.getenv('CF_PAGES'), flush=True)
		print('GITHUB_ACTIONS', os.getenv('GITHUB_ACTIONS'), flush=True)

	def ciTweaks(self) -> None:
		with open('mkdocs.yml', 'r') as mkdocsConfigFile:
			self.mkdocsConfig = mkdocsConfigFile.read()

		with open('mkdocs.yml', 'w') as mkdocsConfigFile:
			mkdocsConfigFile.write(self.mkdocsConfig)
	
	def generate(self) -> None:
		command =['mkdocs']
		if self.systemType == CiSystem.CLOUDFLARE:
			command.append('build')
		elif self.systemType == CiSystem.GITHUB:
			command.append('gh-deploy')
			command.append('--force')
		
		subprocess.run(command, capture_output=True, check=True, text=True)

	def siteExtraConfig(self) -> None:
		if self.systemType == CiSystem.CLOUDFLARE:
			shutil.move('./_headers', './site/_headers')