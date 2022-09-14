import subprocess
import os

class PreSetupCF:
	def __init__(self, isSudo) -> None:
		self.isSudo = isSudo

	def installMkDocsDeps(self) -> None:
		testCommand1 = f'{self.isSudo == True and "" or "sudo"} apt update'
		print('RUNNING:', testCommand1)
		os.system(testCommand1)
		testCommand2 = f'{self.isSudo == True and "" or "sudo"} apt install -y libcairo2-dev libfreetype6-dev libffi-dev libjpeg-dev libpng-dev libz-dev'
		print('RUNNING:', testCommand2)
		os.system(testCommand2)
	def npmCi(self, production:bool = False) -> None:
		npmCiAttempt = subprocess.run(["npm", "ci", f"--production={production == True and 'true' or 'false'}"], capture_output=True, check=True, text=True)
		print(npmCiAttempt.stdout, flush=True)
		print(npmCiAttempt.stderr, flush=True)