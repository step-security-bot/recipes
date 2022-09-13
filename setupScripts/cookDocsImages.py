import os
import re
import shutil

class CookDocsImages:
	def __init__(self) -> None:
		self.recipeTree(f"{os.getcwd()}/recipes")

	def recipeTree(self, walkDir:str) -> None:
		for root, dirs, files in os.walk(walkDir):
			for filename in files:
				# cook-docs only supports jpg and png https://github.com/nicholaswilde/cook-docs/blob/70a9703a6647cfa857dd8a94c0623149fcd03368/pkg/cook/recipe_info.go#L33
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
			# CF
			# drwxr-xr-x 2 buildbot nogroup    4096 Sep  4 22:48 .
			# GH
			# drwxr-xr-x 2 runner docker    4096 Sep  4 22:48 .
			# 
			# Keep base folder perms of 755
			os.makedirs(imageRoot, 0o755)
			print("Created", imageRoot)
		# Check if image exists
		originalImagePath = os.path.join(root, filename)
		newImagePath = os.path.join(imageRoot, self.standardizeName(filename))
		if not os.path.isfile(newImagePath):
			shutil.move(originalImagePath, newImagePath)
			print("Moved", originalImagePath, "to", newImagePath)