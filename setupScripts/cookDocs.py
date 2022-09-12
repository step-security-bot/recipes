import os

class CookDocs:
	def __init__(self) -> None:
		self.download()
		self.run()

	def download(self) -> None:
		goInstallAttempt = os.system("go install github.com/nicholaswilde/cook-docs/cmd/cook-docs@latest")
		if goInstallAttempt != 0:
			raise Exception(f"go exited with code: {goInstallAttempt}")

	def run(self) -> None:
		if (os.getenv('GITHUB_ACTIONS') != None and bool(os.getenv('GITHUB_ACTIONS')) == True):
			gopath = ''
		elif (os.getenv('CF_PAGES') != None and int(os.getenv('CF_PAGES')) == 1):
			gopath = '$GOPATH/bin/'

		print('running: ', f'{gopath}cook-docs', flush=True)
		cookDocsAttempt = os.system(f"{gopath}cook-docs")
		if cookDocsAttempt != 0:
			raise Exception(f"cook-docs exited with code: {cookDocsAttempt}")