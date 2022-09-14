import subprocess
import os

class PreSetupCF:
	def __init__(self, isSudo) -> None:
		self.isSudo = isSudo

	def installMkDocsDeps(self) -> None:
		# commands = ["apt", "install", "-y", "libcairo2-dev", "libfreetype6-dev", "libffi-dev", "libjpeg-dev", "libpng-dev", "libz-dev"]
		# if not self.isSudo:
		# 	commands.insert(0, "sudo")
		# aptInstallAttempt = subprocess.run(commands, capture_output=True, check=True, text=True)
		# print(aptInstallAttempt.stdout, flush=True)
		# print(aptInstallAttempt.stderr, flush=True)
		testCommand = f'apt install -y libcairo2-dev libfreetype6-dev libffi-dev libjpeg-dev libpng-dev libz-dev'
		print('RUNNING:', testCommand)
		os.system(testCommand)

	def npmCi(self, production:bool = False) -> None:
		npmCiAttempt = subprocess.run(["npm", "ci", f"--production={production == True and 'true' or 'false'}"], capture_output=True, check=True, text=True)
		print(npmCiAttempt.stdout, flush=True)
		print(npmCiAttempt.stderr, flush=True)