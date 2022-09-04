import os
import re

class CookDocsImages:
	def __init__(self) -> None:
		self.recipeTree(f"{os.getcwd()}/recipes")

	def recipeTree(self, walkDir:str) -> None:
		print('WORKTODO')
		for root, dirs, files in os.walk(walkDir):
			for filename in files:
				if re.search(r'^((?!icon).)+\.(jpg|png)$', filename, flags=re.IGNORECASE):
					print(os.path.join(root, filename))
					# print(filename)