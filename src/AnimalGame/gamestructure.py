from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Protocol, runtime_checkable


class GameEntity(ABC):
    pass


@runtime_checkable
class FeedAble(Protocol):
    def feed(self, food: str) -> GameEvent:
        """
        Feed the animal with the given food.
        Returns a GameEvent describing the outcome.
        """
        ...


class Animal(GameEntity, ABC):
    def __init__(self, name: str):
        self.name: str = name
        self.is_alive: bool = True

    @abstractmethod
    def make_sound(self) -> str:
        """
        Returns the sound the animal makes.
        """
        raise NotImplementedError

    def die(self) -> None:
        """
        Marks the animal as dead.
        """
        self.is_alive = False


class Player(GameEntity):
    def feed(self, animal: FeedAble, food: str) -> GameEvent:
        """
        Feeds a FeedAble animal.

        Raises:
            TypeError: if the given object is not FeedAble
        """
        if not isinstance(animal, FeedAble):
            raise TypeError("Target is not feedable")

        return animal.feed(food)


@dataclass
class GameEvent:
    actor: str
    action: str
    result: str
