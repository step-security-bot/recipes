import subprocess
import os

class PreSetupCF:
	def __init__(self, isSudo) -> None:
		self.isSudo = isSudo

	def installMkDocsDeps(self) -> None:
		os.system(f'{self.isSudo == True and "" or "sudo"} apt update')
		os.system(f'{self.isSudo == True and "" or "sudo"} apt install -y libcairo2-dev libfreetype6-dev libffi-dev libjpeg-dev libpng-dev libz-dev')
	def npmCi(self, production:bool = False) -> None:
		npmCiAttempt = subprocess.run(["npm", "ci", f"--production={production == True and 'true' or 'false'}"], capture_output=True, check=True, text=True)
		print(npmCiAttempt.stdout, flush=True)
		print(npmCiAttempt.stderr, flush=True)