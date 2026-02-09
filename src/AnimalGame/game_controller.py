from random import choice, random
from typing import List

from .gamestructure import Animal, FeedAble, GameEvent, Player
from .wild.animals import Wolf


class GameController:
    def __init__(self, animals: List[Animal]):
        self.animals = animals
        self.player = Player()
        self.wolves = [a for a in animals if isinstance(a, Wolf)]
        self.feedable = [a for a in animals if isinstance(a, FeedAble)]

    def get_animal_list(self) -> List[Animal]:
        """Return all animals."""
        return self.animals

    def get_alive_feedable(self) -> List[FeedAble]:
        """Return feedable and alive animals."""
        return [a for a in self.feedable if a.is_alive]

    def feed_animal(self, animal: FeedAble, food: str) -> GameEvent:
        """Feed an animal and return the resulting GameEvent."""
        event = self.player.feed(animal, food)
        self.wolves_act()
        return event

    def wolves_act(self) -> List[GameEvent]:
        """Let wolves attack randomly. Returns a list of events."""
        events = []
        for wolf in self.wolves:
            alive_prey = [
                a for a in self.animals if a.is_alive and not isinstance(a, Wolf)
            ]
            if alive_prey and random() < 0.25:
                prey = choice(alive_prey)
                event = wolf.eat(prey)
                events.append(event)
                break
        return events
