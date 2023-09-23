from mkdocs.structure.nav import Navigation, Section, Link
from mkdocs.config.defaults import MkDocsConfig
from mkdocs.structure.files import Files

def on_config(config: MkDocsConfig) -> MkDocsConfig | None:
	pass

def on_nav(nav: Navigation, config: MkDocsConfig, files: Files) -> Navigation | None:
	nav.items.insert(0, Link(title="Main Site", url="https://demosjarco.dev"))

	return nav