import subprocess

class LessCompiler:
	def __init__(self) -> None:
		self.runLessWatchCompiler()

	def runLessWatchCompiler(self) -> None:
		lessCompilerAttempt = subprocess.run(["npm", "run", "less"], capture_output=True, check=True, text=True)
		print(lessCompilerAttempt.stdout, flush=True)
		print(lessCompilerAttempt.stderr, flush=True)