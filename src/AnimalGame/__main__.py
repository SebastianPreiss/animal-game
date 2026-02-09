import sys


def main() -> None:
    if "--gui" in sys.argv:
        from AnimalGame.ui.gui import run_gui

        run_gui()
    else:
        from AnimalGame.ui.cli import run_cli

        run_cli()


if __name__ == "__main__":
    main()
