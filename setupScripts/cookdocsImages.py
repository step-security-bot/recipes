import os
import re
import shutil

class CookDocsImages:
	def __init__(self) -> None:
		self.recipeTree(f"{os.getcwd()}/recipes")

	def recipeTree(self, walkDir:str) -> None:
		print('WORKTODO')
		for root, dirs, files in os.walk(walkDir):
			for filename in files:
				if re.search(r'^((?!icon).)+\.(jpg|png)$', filename, flags=re.IGNORECASE):
					self.moveAsset(root, filename)
	
	def standardizeName(self, filename) -> str:
		# Matching https://github.com/nicholaswilde/cook-docs/blob/main/pkg/document/template.go#L50
		noSpaces = re.sub("\s", "-", filename)
		lowercase = noSpaces.lower()
		return lowercase
	
	def moveAsset(self, root, filename) -> None:
		# Check if assets folder exists
		imageRoot = os.path.join(root, 'assets/images')
		if not os.path.isdir(imageRoot):
			print("Creating", imageRoot)
			os.system(f"ls -la {root}")
		# shutil.move(os.path.join(root, filename), os.path.join(root, 'assets/images', self.standardizeName(filename)))			# drwxr-xr-x 2 buildbot nogroup    4096 Sep  4 22:48 .
			# GH
			# drwxr-xr-x 2 runner docker    4096 Sep  4 22:48 .
			# 
			# Keep base folder perms of 755
			os.makedirs(imageRoot, 0o755)
