import random
from pathlib import Path
from typing import List

from AnimalGame.gameinit import create_animals, load_config
from AnimalGame.gamestructure import Animal, FeedAble, GameEvent, Player
from AnimalGame.wild.animals import Wolf


def display_event(event: GameEvent) -> None:
    """
    Displays a game event to the console.
    This is pure UI logic.
    """
    print(f"[{event.actor}] {event.action}: {event.result}")


def do_main_loop(animals: List[Animal]) -> None:
    player = Player()
    wolves = [a for a in animals if isinstance(a, Wolf)]
    feedable = [a for a in animals if isinstance(a, FeedAble)]

    while True:
        print("\nAnimals:")
        for idx, animal in enumerate(animals):
            status = "alive" if animal.is_alive else "dead"
            print(f"{idx + 1}. {animal.name} [{status}]")

        alive_feedable = [a for a in feedable if a.is_alive]
        if not alive_feedable:
            print("\nAll feedable animals have been fed or are dead!")
            break

        try:
            choice = input("Select animal to feed (number or 'q' to quit): ").strip()
            if choice.lower() == "q":
                break
            idx = int(choice) - 1
            if idx < 0 or idx >= len(animals):
                print("Invalid selection")
                continue
            animal = animals[idx]
            if not isinstance(animal, FeedAble):
                print(f"{animal.name} cannot be fed!")
                continue
            if not animal.is_alive:
                print(f"{animal.name} is dead!")
                continue
        except ValueError:
            print("Please enter a valid number")
            continue

        food = input(f"What do you feed {animal.name}? ").strip()
        event = player.feed(animal, food)
        print(f"[{event.actor}] {event.action}: {event.result}")

        for wolf in wolves:
            alive_prey = [a for a in animals if a.is_alive and not isinstance(a, Wolf)]
            if alive_prey and random.random() < 0.5:
                prey = random.choice(alive_prey)
                event = wolf.eat(prey)
                print(f"[{event.actor}] {event.action}: {event.result}")


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
