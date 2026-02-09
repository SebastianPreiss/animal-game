from pathlib import Path
from typing import List

from AnimalGame.game_controller import GameController
from AnimalGame.gameinit import create_animals, load_config
from AnimalGame.gamestructure import FOODOPTIONS, Animal, FeedAble


def display_event(event):
    print(f"[{event.actor}] {event.action}: {event.result}")


def do_main_loop(animals: List[Animal]):
    controller = GameController(animals)

    while True:
        print("\nAnimals:")
        for idx, animal in enumerate(controller.get_animal_list()):
            status = "alive" if animal.is_alive else "dead"
            print(f"{idx + 1}. {animal.name} [{status}]")

        alive_feedable = controller.get_alive_feedable()
        if not alive_feedable:
            print("\nAll feedable animals have been fed or are dead!")
            break

        choice = input("Select animal to feed (number or 'q' to quit): ").strip()
        if choice.lower() == "q":
            break

        try:
            animal = controller.get_animal_list()[int(choice) - 1]
            if not isinstance(animal, FeedAble):
                print(f"{animal.name} cannot be fed!")
                continue
            if not animal.is_alive:
                print(f"{animal.name} is dead!")
                continue
        except (ValueError, IndexError):
            print("Invalid selection")
            continue

        print("\nFood options:")
        for i, food in enumerate(FOODOPTIONS, 1):
            print(f"{i}. {food}")

        try:
            food = FOODOPTIONS[int(input("Select food by number: ")) - 1]
        except (ValueError, IndexError):
            print("Invalid selection")
            continue

        event = controller.feed_animal(animal, food)
        display_event(event)

        for event in controller.wolves_act():
            display_event(event)


def run_cli() -> None:
    """
    CLI entry point.
    Loads configuration, initializes the game, and starts the loop.
    """
    config_path = Path(__file__).resolve().parent.parent / "config.toml"

    config = load_config(config_path)
    animals = create_animals(config)

    print("Welcome to AnimalGame")
    do_main_loop(animals)
    print("Game finished.")
