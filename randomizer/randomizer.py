from random import randint
from cyckei.plugins import cyp_base


class PluginController(cyp_base.BaseController):
    def __init__(self, sources):
        super().__init__(
            "randomizer",
            "Generates random values, as an example."
        )

        # Create a randomizer object
        self.sources = self.load_sources(sources)
        self.logger.info(f"Created {len(self.sources)} Randomizer(s)")

        # List of names to declare to Cyckei
        self.names = []
        for source in self.sources:
            self.names.append(str(source))

    def load_sources(self, config_sources):
        """
        Searches for available sources, and establishes source objects.

        Returns
        -------
        Dictionary of sources in format "name": SourceObject.
        """

        # Sources don't need to be found for this plugin,
        # so we just initialize two randomizers as examples
        sources = {}
        for source in config_sources:
            object = PluginSource(source["meta"])
            sources[object.name] = object

        return sources


class PluginSource(cyp_base.BaseSource):
    def __init__(self, range):
        super().__init__()
        self.range = range
        self.name = f"Random {range[0]}-{range[1]}"

    def read(self):
        return randint(self.range[0], self.range[1])


if __name__ == "__main__":
    controller = PluginController()
    print(cyp_base.read_all(controller))
