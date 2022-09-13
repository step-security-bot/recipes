import subprocess

class LessCompiler:
	def __init__(self) -> None:
		self.runLessWatchCompiler()

		subprocess.run(["npm", "run", "less"], capture_output=True, check=True, text=True)
	def runLessWatchCompiler(self) -> None:
