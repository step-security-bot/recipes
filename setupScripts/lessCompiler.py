import subprocess
import os

class LessCompiler:
	def __init__(self) -> None:
		self.runLesscpy()

	def runLesscpy(self) -> None:
		# subprocess.run(["lesscpy", "-t", "-r", f"{os.getcwd()}/recipes/stylesheets"], capture_output=True, check=True)
		print('running:', f"lesscpy -t -r -g -V {os.getcwd()}/recipes/stylesheets/", flush=True)
		lesscpyAttempt = os.system(f"lesscpy -t -r -g -V {os.getcwd()}/recipes/stylesheets/")
		if lesscpyAttempt != 0:
			raise Exception(f"lesscpy exited with code: {lesscpyAttempt}")