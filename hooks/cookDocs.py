from mkdocs.config.base import Config
from subprocess import run
from os import getenv

class CookDocs:
	def __init__(self) -> None:
		self.download()
		self.run()

	def download(self) -> None:
		goInstallAttempt = run(["go", "install", "github.com/nicholaswilde/cook-docs/cmd/cook-docs@latest"], capture_output=True, check=True, text=True)
		print(goInstallAttempt.stdout, flush=True)
		print(goInstallAttempt.stderr, flush=True)

	def run(self) -> None:
		if (getenv('GITHUB_ACTIONS') != None and bool(getenv('GITHUB_ACTIONS')) == True):
			gopath = ''
		elif (getenv('CF_PAGES') != None and int(getenv('CF_PAGES')) == 1):
			gopath = '$GOPATH/bin/'

		ls_attempt = run(f"ls -lia $GOBIN", capture_output=True, shell=True, check=True, 	text=True)
		print(ls_attempt.stdout, flush=True)
		print(ls_attempt.stderr, flush=True)

		ls_attempt = run(f"ls -lia $GOPATH/bin", capture_output=True, shell=True, check=True, 	text=True)
		print(ls_attempt.stdout, flush=True)
		print(ls_attempt.stderr, flush=True)

		ls_attempt = run(f"ls -lia $HOME/go/bin", capture_output=True, shell=True, check=True, 	text=True)
		print(ls_attempt.stdout, flush=True)
		print(ls_attempt.stderr, flush=True)

		cookDocsAttempt = run([f"{gopath}cook-docs"], capture_output=True, shell=True, check=True, 	text=True)
		print(cookDocsAttempt.stdout, flush=True)
		print(cookDocsAttempt.stderr, flush=True)

def on_config(config: Config) -> Config:
	CookDocs()