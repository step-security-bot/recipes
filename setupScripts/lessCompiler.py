import subprocess
import os

class LessCompiler:
	def __init__(self) -> None:
		self.runLesscpy()

	def runLesscpy(self) -> None:
		subprocess.run(["npm", "run", "less"], shell=True, check=True)