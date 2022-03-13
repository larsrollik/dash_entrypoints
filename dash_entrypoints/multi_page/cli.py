import argparse
import logging
import sys

from dash_entrypoints.misc import get_local_ip_address
from dash_entrypoints.multi_page import DEFAULT_APP_NAME
from dash_entrypoints.multi_page import DEFAULT_ASSETS_FOLDER
from dash_entrypoints.multi_page import DEFAULT_VIEWS_MODULE
from dash_entrypoints.multi_page.entrypoint import run_entrypoint


def make_parser():
    """Make arg parser"""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-n",
        "--app-name",
        type=str,
        dest="app_name",
        default=DEFAULT_APP_NAME,
        help="App name",
    )
    parser.add_argument(
        "-ip",
        "--ip-address",
        type=str,
        dest="ip_address",
        default=get_local_ip_address(),
        help="Host name or IP address",
    )
    parser.add_argument(
        "-m",
        "--views-module",
        type=str,
        dest="views_module",
        default=DEFAULT_VIEWS_MODULE,
        help="Module import statement for module that contains pages, e.g. 'mypackage.page_subpackage' ",
    )
    parser.add_argument(
        "-a",
        "--assets-folder",
        type=str,
        dest="assets_folder",
        default=DEFAULT_ASSETS_FOLDER,
        help="Folder with stylesheet, script, image assets",
    )
    parser.add_argument(
        "--port",
        "-p",
        dest="port",
        type=int,
        default=9050,
        help="Port number for server",
    )
    parser.add_argument(
        "--debug",
        "-d",
        dest="debug",
        action="store_true",
        default=False,
        help="Debug mode",
    )
    return parser


def run_cli(*args):
    """Command line interface wrapper"""
    if not args:
        args = sys.argv[1:]

    if len(args) > 0 and not isinstance(args[0], str):
        args = args[0]

    if len(args) > 0 and str(args[0]).endswith(".py"):
        _, args = args[0], args[1:]

    if len(args) <= 1:
        args = args + ["-h"]

    parser = make_parser()
    args_dict = parser.parse_args(args=args).__dict__

    if args_dict.get(
        "debug",
    ):
        print("CLI arguments:", args_dict)

    if "exit_flag" in args_dict.keys():
        return

    # Call module
    run_entrypoint(**args_dict)

    logging.debug("EXITING CLI.")


if __name__ == "__main__":
    run_cli()
