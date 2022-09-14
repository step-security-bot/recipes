import subprocess

class PreSetupCF:
	def __init__(self, isSudo) -> None:
		self.isSudo = isSudo

	def installMkDocsDeps(self) -> None:
		aptUpdateAttempt = subprocess.run(['sudo', 'apt', 'update'], capture_output=True, check=True, text=True)
		print(aptUpdateAttempt.stdout, flush=True)
		print(aptUpdateAttempt.stderr, flush=True)
		aptInstallAttempt = subprocess.run(['sudo', 'apt', 'install', '-y', 'libcairo2-dev', 'libfreetype6-dev', 'libffi-dev', 'libjpeg-dev', 'libpng-dev', 'libz-dev'], capture_output=True, check=True, text=True)
		print(aptInstallAttempt.stdout, flush=True)
		print(aptInstallAttempt.stderr, flush=True)

	def npmCi(self, production:bool = False) -> None:
		npmCiAttempt = subprocess.run(["npm", "ci", f"--production={production == True and 'true' or 'false'}"], capture_output=True, check=True, text=True)
		print(npmCiAttempt.stdout, flush=True)
		print(npmCiAttempt.stderr, flush=True)