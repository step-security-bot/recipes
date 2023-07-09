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

		print("Before $GOBIN")
		ls_attempt = run(f"ls -lia $GOBIN", capture_output=True, shell=True, check=False, text=True)
		print(ls_attempt.stdout, flush=True)
		print(ls_attempt.stderr, flush=True)
		print("After $GOBIN")

		print("Before $GOPATH/bin")
		ls_attempt2 = run(f"ls -lia $GOPATH/bin", capture_output=True, shell=True, check=False, 	text=True)
		print(ls_attempt2.stdout, flush=True)
		print(ls_attempt2.stderr, flush=True)
		print("After $GOPATH/bin")

		print("Before $HOME/go/bin")
		ls_attempt3 = run(f"ls -lia $HOME/go/bin", capture_output=True, shell=True, check=False, 	text=True)
		print(ls_attempt3.stdout, flush=True)
		print(ls_attempt3.stderr, flush=True)
		print("After $HOME/go/bin")

		cookDocsAttempt = run([f"{gopath}cook-docs"], capture_output=True, shell=True, check=True, 	text=True)
		print(cookDocsAttempt.stdout, flush=True)
		print(cookDocsAttempt.stderr, flush=True)

def on_config(config: Config) -> Config:
	CookDocs()