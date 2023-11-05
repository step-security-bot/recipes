from hashlib import sha512
from mkdocs.config.defaults import MkDocsConfig
from pathlib import Path
from io import StringIO
import lesscpy

class LessCompiler:
	@staticmethod
	def get_sha512_hash(content: str) -> str:
		return sha512(content.encode()).hexdigest()

	@staticmethod
	def compileCSS(cssFilePath: Path, lessFilePath: Path) -> None:
		with open(lessFilePath, 'r') as lessFile:
			lessFileText = lessFile.read()

		newCssFileText = lesscpy.compile(StringIO(lessFileText), tabs=True, spaces=False)

		try:
			with open(cssFilePath, 'r', encoding='utf-8') as cssFile:
				oldCssFileText = cssFile.read()
		except FileNotFoundError:
			oldCssFileText = ""

		if LessCompiler.get_sha512_hash(newCssFileText) != LessCompiler.get_sha512_hash(oldCssFileText):
			with open(cssFilePath, 'w') as cssFile:
				cssFile.write(newCssFileText)
			print(f"Compiled {lessFilePath} to {cssFilePath}", flush=True)
		else:
			print(f"No changes detected; skipping compilation for {lessFilePath}", flush=True)

# Run `on_config` because it runs before `get_files`
def on_config(config: MkDocsConfig) -> MkDocsConfig | None:
	for extraCssFilePath in config.extra_css:
		cssFilePath = Path(config.docs_dir).joinpath(Path(extraCssFilePath))
		lessFilePath = cssFilePath.with_suffix('.less')

		if lessFilePath.exists():
			LessCompiler.compileCSS(cssFilePath, lessFilePath)
