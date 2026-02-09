from AnimalGame.gamestructure import Animal, GameEvent


class Parrot(Animal):
    food_preferences = [
        "seeds",
        "fruit",
        "apple",
        "bread",
        "carrot",
        "lettuce",
    ]

    def __init__(self):
        super().__init__(name="Parrot")

    def feed(self, food: str) -> GameEvent:
        if not self.is_alive:
            return GameEvent(self.name, "feed", "The parrot is dead.")

        if food.lower() not in self.food_preferences:
            return GameEvent(self.name, "feed", "The parrot refuses the food.")

        return GameEvent(self.name, "feed", "The parrot eats happily and squawks!")

    def make_sound(self) -> str:
        return "Squawk!"


class Wolf(Animal):
    def __init__(self):
        super().__init__(name="Wolf")

    def eat(self, prey: Animal) -> GameEvent:
        if not isinstance(prey, Animal):
            raise TypeError("Wolf can only eat animals")

        if not prey.is_alive:
            return GameEvent(self.name, "eat", "The prey is already dead.")

        prey.die()
        return GameEvent(self.name, "eat", f"The wolf devours the {prey.name}!")

    def make_sound(self) -> str:
        return "Grrrr"
