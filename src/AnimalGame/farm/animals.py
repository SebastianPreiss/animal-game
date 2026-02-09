from AnimalGame.gamestructure import Animal, FeedAble, GameEvent


class Cow(Animal, FeedAble):
    food_preferences = [
        "grass",
        "hay",
        "oats",
        "pellets",
    ]

    def __init__(self):
        super().__init__(name="Cow")

    def feed(self, food: str) -> GameEvent:
        if not self.is_alive:
            return GameEvent(self.name, "feed", "The cow is dead and cannot eat.")

        if food.lower() not in self.food_preferences:
            return GameEvent(self.name, "feed", "The cow refuses the food.")

        return GameEvent(self.name, "feed", "The cow eats happily and says Moo!")

    def make_sound(self) -> str:
        return "Moo"


class Chicken(Animal, FeedAble):
    food_preferences = [
        "grains",
        "seeds",
        "insects",
        "worms",
        "corn",
    ]

    def __init__(self):
        super().__init__(name="Chicken")

    def feed(self, food: str) -> GameEvent:
        if not self.is_alive:
            return GameEvent(self.name, "feed", "The chicken is dead and cannot eat.")

        if food.lower() not in self.food_preferences:
            return GameEvent(self.name, "feed", "The chicken pecks suspiciously.")

        return GameEvent(self.name, "feed", "The chicken eats and says Cluck!")

    def make_sound(self) -> str:
        return "Cluck"
