import tkinter as tk
from pathlib import Path
from tkinter import messagebox
from typing import List

from AnimalGame.game_controller import GameController
from AnimalGame.gameinit import create_animals, load_config
from AnimalGame.gamestructure import FOODOPTIONS, Animal, FeedAble
from AnimalGame.ui.animal_widget import AnimalWidget
from AnimalGame.ui.feeding_popup import FeedingPopup


class AnimalGUI:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("AnimalGame GUI")
        self.root.geometry("800x600")
        self.root.resizable(False, False)

        # Game Setup
        config_path = Path(__file__).resolve().parent.parent / "config.toml"
        animals: List[Animal] = create_animals(load_config(config_path))
        self.controller = GameController(animals)

        # Status-Bar
        self.status = tk.StringVar()
        self.status.set("Welcome to AnimalGame GUI!")
        self.status_label = tk.Label(root, textvariable=self.status, anchor="w")
        self.status_label.pack(fill="x", side="bottom")
        self.wolf_status = tk.StringVar()
        self.wolf_status.set("")
        self.wolf_status_label = tk.Label(
            root, textvariable=self.wolf_status, anchor="w"
        )
        self.wolf_status_label.pack(fill="x", side="bottom")

        # Animal Frame
        self.frame = tk.Frame(root)
        self.frame.pack(expand=True, fill="both")
        self.animal_widgets: List[AnimalWidget] = []
        self.load_animal_widgets()

    def load_animal_widgets(self):
        """Load widgets for all animals and display them in a grid."""
        for widget in self.frame.winfo_children():
            widget.destroy()

        self.animal_widgets.clear()
        for idx, animal in enumerate(self.controller.get_animal_list()):
            widget = AnimalWidget(self.frame, animal, self.show_feed_menu)
            widget.label.grid(row=idx // 4, column=idx % 4, padx=10, pady=10)
            self.animal_widgets.append(widget)

    def show_feed_menu(self, animal: Animal, event):
        """Open a popup to select food."""
        if not isinstance(animal, FeedAble) or not animal.is_alive:
            messagebox.showinfo("Info", f"{animal.name} cannot be fed!")
            return

        def feed_callback(food):
            self.feed_animal(animal, food)
            popup.popup.destroy()

        popup = FeedingPopup(
            self.root,  # type: ignore
            f"Feed {animal.name}",
            FOODOPTIONS,
            feed_callback,
        )

    def feed_animal(self, animal: FeedAble, food: str):
        """Perform feeding action via GameController and update GUI."""
        self.wolf_status.set("")
        event = self.controller.feed_animal(animal, food)
        self.status.set(f"[{event.actor}] {event.action}: {event.result}")

        self.update_animal_widgets()

        for wolf_event in self.controller.wolves_act():
            self.wolf_status.set(
                f"\n[{wolf_event.actor}] {wolf_event.action}: {wolf_event.result}"
            )
            self.update_animal_widgets()

    def update_animal_widgets(self):
        """Update the status of all animal widgets."""
        for widget in self.animal_widgets:
            widget.update_status()


def run_gui():
    root = tk.Tk()
    _ = AnimalGUI(root)
    root.mainloop()
