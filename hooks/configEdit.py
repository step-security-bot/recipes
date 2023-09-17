from mkdocs.config.base import Config
from mkdocs.structure.nav import Navigation, Section, Link
from mkdocs.structure.files import Files

def on_config(config: Config) -> Config:
	pass

def on_nav(nav: Navigation, config: Config, files: Files) -> Navigation | None:
	nav.items.insert(0, Link(title="Main Site", url="https://demosjarco.dev"))

	return nav