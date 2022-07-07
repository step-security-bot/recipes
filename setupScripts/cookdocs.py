import os

class CookDocs:
	def __init__(self) -> None:
		self.download()

	def download(self):
		goInstallAttempt = os.system("go install github.com/nicholaswilde/cook-docs/cmd/cook-docs@latest")
		if goInstallAttempt != 0:
			raise Exception(f"go exited with code: {goInstallAttempt}")
		cookDocsAttempt = os.system("$GOPATH/bin/cook-docs")
		if cookDocsAttempt != 0:
			raise Exception(f"cook-docs exited with code: {cookDocsAttempt}")