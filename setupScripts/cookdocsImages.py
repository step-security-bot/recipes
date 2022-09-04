from ast import walk
import os

class CookDocsImages:
	def __init__(self) -> None:
		self.recipeTree(f"{os.getcwd()}/site")

	def recipeTree(self, walkDir:str) -> None:
		for root, dirs, files in os.walk(walkDir):
			for filename in files:
				print('WORKTODO', os.path.join(root, filename))