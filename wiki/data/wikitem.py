from dataclasses import dataclass


@dataclass()
class ParseItem():
    """Parse item"""
    site: str
    frontend_langs: str
    backend_langs: str
    popularity: int
    desc: str = None

    def __post_init__(self):
        self.desc = self.desc or "%s (Frontend:%s|Backend:%s)" % (self.site, self.frontend_langs, self.backend_langs)
