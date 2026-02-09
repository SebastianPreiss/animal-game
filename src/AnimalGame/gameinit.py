from pathlib import Path
from typing import List

import tomllib

from AnimalGame.farm.animals import Chicken, Cow
from AnimalGame.gamestructure import Animal
from AnimalGame.wild.animals import Parrot, Wolf


def load_config(path: Path) -> dict:
    """
    Loads the TOML configuration file.
    """
    with path.open("rb") as f:
        return tomllib.load(f)


def create_animals(config: dict) -> List[Animal]:
    """
    Creates all animals defined in the configuration.
    """
    animals: List[Animal] = []

    farm = config.get("farm", {})
    wild = config.get("wild", {})

    for _ in range(farm.get("cows", 0)):
        animals.append(Cow())

    for _ in range(farm.get("chickens", 0)):
        animals.append(Chicken())

    for _ in range(wild.get("parrots", 0)):
        animals.append(Parrot())

    for _ in range(wild.get("wolves", 0)):
        animals.append(Wolf())

    return animals
