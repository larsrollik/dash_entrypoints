import argparse
import logging
import socket
import sys

from dash_entrypoints.entrypoint import run_entrypoint


def get_local_ip_address():
    """https://stackoverflow.com/questions/166506/finding-local-ip-addresses-using-pythons-stdlib"""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(("10.255.255.255", 1))
        ip = s.getsockname()[0]
    except Exception:
        ip = "127.0.0.1"
    finally:
        s.close()
    return ip


def make_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-n",
        "--app-name",
        type=str,
        dest="app_name",
        default="App name",
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
        default="dash_entrypoints.views",
        help="Module import statement for module that contains pages, e.g. 'mypackage.page_subpackage' ",
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
