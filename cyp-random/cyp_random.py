import logging
from random import randint
from cyckei.plugins import cyp_base

logger = logging.getLogger("cyckei")


class RandomController(cyp_base.PluginController):
    def get_sources(self):
        """
        Searches for available sources, and establishes source objects.

        Returns
        -------
        Dictionary of sources in format "name": SourceObject.
        """

        # Sources don't need to be found for this plugin, so we just initialize
        sources = {}
        sources["Rand1"] = SourceObject(10)
        sources["Rand2"] = SourceObject(20)


class SourceObject(object):
    def __init__(self, port):
        super().__init__()
        self.range = [0, port]
        self.name = f"Random 0-{port}"

    def connect(self):
        return True

    def ping(self):
        return True

    def read(self):
        return randint(self.range[0], self.range[1])


if __name__ == "__main__":
    controller = RandomController()
