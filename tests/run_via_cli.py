import sys

from dash_entrypoints import run_cli


if __name__ == "__main__":
    sys.argv += [
        "-n",
        "CLI-TEST",
        # "-f",
        # "/Volumes/Data/code/valiant/secrets/secrets.json",
    ]
    run_cli()
