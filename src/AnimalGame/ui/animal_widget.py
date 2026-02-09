import tkinter as tk
from pathlib import Path

from PIL import Image, ImageTk

from AnimalGame.gamestructure import Animal

ASSETS_PATH = Path(__file__).parent / "assets"


class AnimalWidget:
    def __init__(self, parent: tk.Frame, animal: Animal, feed_callback):
        self.animal = animal
        self.label = tk.Label(
            parent, text=f"{animal.name} [{self.get_status()}]", compound="top"
        )
        self.label.bind("<Button-3>", lambda e: feed_callback(animal, e))
        self.load_image()

    def load_image(self):
        img_path = ASSETS_PATH / f"{self.animal.name.lower()}.png"
        try:
            img = Image.open(img_path).resize((100, 100))
            photo = ImageTk.PhotoImage(img)
            self.label.img = photo  # type: ignore
            self.label.config(image=photo)
        except FileNotFoundError:
            pass

    def get_status(self):
        return "alive" if self.animal.is_alive else "dead"

    def update_status(self):
        self.label.config(text=f"{self.animal.name} [{self.get_status()}]")
