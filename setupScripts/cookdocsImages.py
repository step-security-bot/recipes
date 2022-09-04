from ast import walk
import os

class CookDocsImages:
	def __init__(self) -> None:
		self.recipeTree(f"{os.getcwd()}/site")

	def recipeTree(self, walkDir:str) -> None:
		print('WORKTODO')
		for root, dirs, files in os.walk(walkDir):
			for filename in files:
				print(os.path.join(root, filename))