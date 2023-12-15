from os import getenv
from subprocess import run

from mkdocs.config.defaults import MkDocsConfig

class CookDocs:
	def __init__(self) -> None:
		self.download()
		if (getenv('CF_PAGES') != None and int(getenv('CF_PAGES')) == 1):
			self.reshim()
		self.run()

	def download(self) -> None:
		goInstallAttempt = run(["go", "install", "github.com/nicholaswilde/cook-docs/cmd/cook-docs@latest"], capture_output=True, check=True, text=True)
		print(goInstallAttempt.stdout, flush=True)
		print(goInstallAttempt.stderr, flush=True)

	def reshim(self) -> None:
		reshim_attempt = run("asdf reshim golang", capture_output=True, shell=True, check=False, text=True)
		print(reshim_attempt.stdout, flush=True)
		print(reshim_attempt.stderr, flush=True)

	def run(self) -> None:
		cookDocsAttempt = run(["cook-docs"], capture_output=True, shell=True, check=True, text=True)
		print(cookDocsAttempt.stdout, flush=True)
		print(cookDocsAttempt.stderr, flush=True)

def on_config(config: MkDocsConfig) -> MkDocsConfig | None:
	CookDocs()
