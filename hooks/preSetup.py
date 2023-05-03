from sys import platform
from distro import id as distroId
# Must import full os or WEXITSTATUS crashes other systems
import os
from subprocess import check_output, DEVNULL, CalledProcessError, run

class GitClone:
	def __init__(self) -> None:
		if self.is_shallow_clone():
			print("Is Shallow")
			self.unshallow()
		else:
			print("Not shallow")

	def is_shallow_clone(self) -> None:
		git_dir = os.path.join(os.getcwd(), ".git")
		shallow_file = os.path.join(git_dir, "shallow")

		if os.path.isfile(shallow_file):
			return True

		try:
			git_config = check_output(["git", "config", "--get", "remote.origin.fetch"], stderr=DEVNULL).decode("utf-8")
			if "--depth=" in git_config:
				return True
		except CalledProcessError:
			pass

		return False

	def unshallow(self) -> None:
		unshallowAttempt = run(["git", "fetch", "--unshallow"], capture_output=True, check=True, text=True)
		print(unshallowAttempt.stdout, flush=True)
		print(unshallowAttempt.stderr, flush=True)

class PackageManager:
	def __init__(self) -> None:
		pass

	def installPackages(self, *packages: str, assumeYes: bool = False) -> None:
		pass

class AptInstall(PackageManager):
	def __init__(self) -> None:
		super().__init__()
		os.system('sudo apt update')

	def installPackages(self, *packages: str, assumeYes: bool = False) -> None:
		super().installPackages(packages, assumeYes=assumeYes)
		aptAttempt = os.system(f'sudo apt install {assumeYes == True and "-y" or ""} {" ".join(packages)}')
		if os.WEXITSTATUS(aptAttempt) >= 100:
			print(f'Error {os.WEXITSTATUS(aptAttempt)}', f'Failed to install {" ".join(packages)}')

class YumInstall(PackageManager):
	def __init__(self) -> None:
		super().__init__()
		os.system('sudo yum check-update')

	def installPackages(self, *packages: str, assumeYes: bool = False) -> None:
		super().installPackages(*packages, assumeYes=assumeYes)
		yumAttempt = os.system(f'sudo yum install {assumeYes == True and "-y" or ""} {" ".join(packages)}')
		print("EXIT CODE:", yumAttempt, os.WEXITSTATUS(yumAttempt))

class ZypperInstall(PackageManager):
	def __init__(self) -> None:
		super().__init__()
		os.system('sudo zypper refresh')

	def installPackages(self, *packages: str, assumeYes: bool = False) -> None:
		super().installPackages(*packages, assumeYes=assumeYes)
		zypperAttempt = os.system(f'sudo zypper install  {assumeYes == True and "-y" or ""} {" ".join(packages)}')
		print("EXIT CODE:", zypperAttempt, os.WEXITSTATUS(zypperAttempt))

def on_startup(command, dirty: bool):
	# Unshallow clone
	GitClone()

	# MkDocs social requirement
	if (os.getenv('ENABLED_SOCIAL') != None and bool(os.getenv('ENABLED_SOCIAL'))):
		if platform == "linux":
			if distroId() == "ubuntu" or distroId() == "debian":
				AptInstall().installPackages('libcairo2-dev', 'libfreetype6-dev', 'libffi-dev', 'libjpeg-dev', 'libpng-dev', 'libz-dev', assumeYes=True)
			elif distroId() == "fedora":
				YumInstall().installPackages('cairo-devel', 'freetype-devel', 'libffi-devel', 'libjpeg-devel', 'libpng-devel', 'zlib-devel', assumeYes=True)
			elif distroId() == "opensuse":
				ZypperInstall().installPackages('cairo-devel', 'freetype-devel', 'libffi-devel', 'libjpeg-devel', 'libpng-devel', 'zlib-devel', assumeYes=True)
