import os
from .cooklang import CookLang
from .cookdocs import CookDocs
import ruamel.yaml

class Docs:
	def __init__(self) -> None:
		CookLang()
		CookDocs()
		self.ciTweaks()
		self.generate()
	
	def ciTweaks(self) -> None:
		yaml = ruamel.yaml.YAML()
		with open('mkdocs.yml') as mkdocsConfigFile:
			data = yaml.load(mkdocsConfigFile)

		for elem in data:
			if elem['name'] == 'site_url':
				if (os.getenv('GITHUB_ACTIONS') != None and bool(os.getenv('GITHUB_ACTIONS')) == True):
					elem['value'] = 'https://demosjarco.github.io/recipes'
				elif (os.getenv('CF_PAGES') != None and int(os.getenv('CF_PAGES')) == 1):
					elem['value'] = 'https://recipes.demosjarco.dev'
			elif elem['name'] == 'enabled_if_env':
				if (os.getenv('GITHUB_ACTIONS') != None and bool(os.getenv('GITHUB_ACTIONS')) == True):
					elem['value'] = 'GITHUB_ACTIONS'
				elif (os.getenv('CF_PAGES') != None and int(os.getenv('CF_PAGES')) == 1):
					elem['value'] = 'CF_PAGES'

		with open('mkdocs.yml', 'wb') as mkdocsConfigFile:
			yaml.dump(data, mkdocsConfigFile)
	
	def generate(self) -> None:
		if (os.getenv('GITHUB_ACTIONS') != None and bool(os.getenv('GITHUB_ACTIONS')) == True):
			runDocsAttempt = os.system('mkdocs gh-deploy')
			if runDocsAttempt != 0:
				raise Exception(f"mkdocs exited with code: {runDocsAttempt}")
		elif (os.getenv('CF_PAGES') != None and int(os.getenv('CF_PAGES')) == 1):
			runDocsAttempt = os.system('mkdocs build')
			if runDocsAttempt != 0:
				raise Exception(f"mkdocs exited with code: {runDocsAttempt}")