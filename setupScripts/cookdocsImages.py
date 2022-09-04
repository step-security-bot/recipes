from ast import walk
import os

class CookDocsImages:
	def __init__(self) -> None:
		self.recipeTree(os.getcwd())

	def recipeTree(self, walkDir:str) -> None:
		print('WORKTODO', os.listdir(walkDir))