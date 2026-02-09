import tkinter as tk
from typing import Callable, List


class FeedingPopup:
    """Popup mit Food-Buttons, max 2 Reihen, automatisch scrollbar wenn nötig."""

    def __init__(
        self,
        root: tk.Toplevel,
        title: str,
        options: List[str],
        callback: Callable[[str], None],
        max_columns: int = 2,
        button_width: int = 10,
        button_height: int = 2,
        padding: int = 5,
    ):
        self.popup = tk.Toplevel(root)
        self.popup.title(title)
        self.popup.resizable(False, False)

        self.options = options
        rows = (len(options) + max_columns - 1) // max_columns
        width_px = max_columns * (button_width * 10 + padding * 2)
        height_px = int(min(rows, 2) * (button_height * 100 + padding * (rows / 2)))

        self.popup.geometry(f"{width_px}x{height_px}")

        if rows > 2:
            container = tk.Frame(self.popup)
            container.pack(fill="both", expand=True)

            canvas = tk.Canvas(container)
            scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
            self.scrollable_frame = tk.Frame(canvas)

            self.scrollable_frame.bind(
                "<Configure>",
                lambda e: canvas.configure(scrollregion=canvas.bbox("all")),
            )

            canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
            canvas.configure(yscrollcommand=scrollbar.set)

            canvas.pack(side="left", fill="both", expand=True)
            scrollbar.pack(side="right", fill="y")
        else:
            self.scrollable_frame = tk.Frame(self.popup)
            self.scrollable_frame.pack(fill="both", expand=True)

        for idx, option in enumerate(options):
            row = idx // max_columns
            col = idx % max_columns
            btn = tk.Button(
                self.scrollable_frame,
                text=option,
                width=button_width,
                height=button_height,
                command=lambda o=option: callback(o),
            )
            btn.grid(row=row, column=col, padx=padding, pady=padding, sticky="nsew")

        for col in range(max_columns):
            self.scrollable_frame.grid_columnconfigure(col, weight=1)
