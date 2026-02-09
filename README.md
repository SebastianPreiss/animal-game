# AnimalGame

[![Tests, Build & Package](https://github.com/SebastianPreiss/animal-game/actions/workflows/build.yml/badge.svg)](https://github.com/SebastianPreiss/animal-game/actions/workflows/build.yml)
[![Latest Release](https://img.shields.io/github/v/release/SebastianPreiss/animal-game?label=Latest%20Version&color=blue)](https://github.com/SebastianPreiss/animal-game/releases/latest)
[![Download Wheel](https://img.shields.io/badge/Wheel-download-orange)](https://github.com/SebastianPreiss/animal-game/releases/latest)
[![Docker Image](https://img.shields.io/badge/Docker-GHCR-blue?logo=docker&logoColor=white)](https://github.com/SebastianPreiss/animal-game/pkgs/container/animalgame)

---

A small animal management game in Python that supports both CLI and GUI.
The GUI is for demonstration purposes and shows the abstraction from game logic to visualization.
Feed animals, listen to their sounds, and watch out for wolves!

---

## Project Structure

```
AnimalGame/
├─ src/
│  ├─ farm/               # Farm animals: Cow, Chicken
│  │  ├─ __init__.py
│  │  └─ animals.py
│  ├─ wild/               # Wild animals: Parrot, Wolf
│  │  ├─ __init__.py
│  │  └─ animals.py
│  ├─ ui/                 # CLI and GUI components
│  │  └─ assets/          # PNG images for animals
│  ├─ __init__.py
│  ├─ __main__.py         # Main entry point, contains do_main_loop()
│  ├─ game_controller.py  # Logic
│  ├─ gamestructure.py    # Base classes & interfaces, includes type hints & exception handling
│  ├─ gameinit.py         # Load config.toml & create animals
│  ├─ config.toml         # Game configuration
└─ tests/                 # Pytest tests
```

---

## Installation (Local, Poetry)

1. Clone the repository:

```bash
git clone <repo-url>
cd animal-game
```

2. Install Poetry (if not installed):

```bash
pip install poetry
```

3. Install dependencies:

```bash
poetry install
```

4. Activate the Poetry shell (optional, for easier access):

```bash
poetry shell
```

---

## Configuration (`config.toml`)

Example:

```toml
[farm]
cows = 2
chickens = 3

[wild]
parrots = 1
wolves = 1
```

This defines the number of each animal to instantiate at game start.

---

## CLI Usage

Run the CLI version:

```bash
poetry run python -m AnimalGame.__main__ --cli
```

Example flow:

```
Animals:
1. Cow [alive]
2. Chicken [alive]

Select animal to feed (number or 'q' to quit): 1

Food options:
1. grass
2. grains
...
Select food by number: 1
[Cow] feed: The cow eats happily and says Moo!
```

- Animals are listed with numbers
- Food options are selectable by number
- Wolves act randomly after each feeding
- Type hints are used throughout the classes
- Feeding invalid targets raises `TypeError` which is handled gracefully

---

## GUI Usage

Run the GUI version (optional):

```bash
poetry run python -m AnimalGame.__main__ --gui
```

Features:

- Window size: 800x600
- Animals displayed with PNG images (100x100)
- Right-click on an animal to open a feeding popup
- Food buttons show max 2 rows; scrollbar appears if options exceed space
- Status bar shows actions (feeding, wolf attacks)
- Wolves act randomly

> Note: GUI is mainly for demonstration.

---

## Docker Usage

Pull and run the container directly from GitHub Container Registry:

```bash
docker pull ghcr.io/sebastianpreiss/animal-game/animalgame:latest

```

Run the CLI interactively inside the container:

```bash
docker run -it --rm ghcr.io/sebastianpreiss/animal-game/animalgame:latest

```

---

## Tests

Run Pytest:

```bash
poetry run pytest -v
```

Included tests:

- `test_cow.py`: Feed a cow correctly and test wrong food
- `test_wolf.py`: Wolf eats a cow correctly

---

## Notes

- Each animal has specific food preferences
- Wolves can only attack living animals

---

## Assets

- PNG files located in `src/ui/assets/`
- Recommended size: 100x100 pixels
- Use Git LFS for large files
