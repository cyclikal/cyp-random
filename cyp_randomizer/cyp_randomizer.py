import logging
from random import randint
from cyckei.plugins import cyp_base
import os.path

logger = logging.getLogger("cyckei")


class RandomController(cyp_base.PluginController):
    def __init__(self):
        base_path = os.path.join(os.path.dirname(__file__), "..")
        super().__init__("randomizer", base_path)

    def get_sources(self):
        """
        Searches for available sources, and establishes source objects.

        Returns
        -------
        Dictionary of sources in format "name": SourceObject.
        """

        # Sources don't need to be found for this plugin,
        # so we just initialize two randomizers as examples
        sources = {}
        sources["Rand1"] = Randomizer(10)
        sources["Rand2"] = Randomizer(20)

        return sources


class Randomizer(cyp_base.SourceObject):
    def __init__(self, port):
        super().__init__()
        self.range = [0, port]
        self.name = f"Random 0-{port}"

    def read(self):
        return randint(self.range[0], self.range[1])


if __name__ == "__main__":
    controller = RandomController()
    print(cyp_base.read_all(controller))
