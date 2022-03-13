import json
import socket
from uuid import uuid4

import dash


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


def get_callback_context():
    context = dash.callback_context
    ctx = json.dumps(
        {
            "states": context.states,
            "triggered": context.triggered,
            "inputs": context.inputs,
        },
        indent=2,
    )
    return ctx
