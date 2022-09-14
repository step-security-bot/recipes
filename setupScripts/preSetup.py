from .preSetupCf import PreSetupCF
import os

class PreSetup:
	def __init__(self) -> None:
		self.cf = PreSetupCF(self.isSudo())
	
	def isSudo(self) -> bool:
		if not os.environ.get("SUDO_UID") and os.geteuid() != 0:
			return False
		else:
			return True