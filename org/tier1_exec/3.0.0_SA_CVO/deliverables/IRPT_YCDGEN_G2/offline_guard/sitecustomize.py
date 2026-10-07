"""An outbound-network block for EVERY Python process started with this folder on PYTHONPATH (3.0.0_SA_CVO, 2026-10-07).

WHY. A relayed test command is run verbatim (1.0.0_SA_CTO msg 106241). Its offline suite carries its own network guard;
its two pytest runs carry none. Python imports `sitecustomize` at start-up, so putting this folder on PYTHONPATH blocks
every non-loopback connect and name lookup in all three processes without changing one character of the command.
It answers "did the run reach AWS or a vendor at all": each attempt is appended to the file named by
OFFLINE_GUARD_LOG, one JSON line per attempt, with the process's argv. No line = no attempt.

COST: four function wraps per process. NON-APPLICATION: loopback; file I/O; a process that does not start Python.
"""
import json
import os
import socket
import sys

_LOG = os.environ.get("OFFLINE_GUARD_LOG")
_LOOP = {"127.0.0.1", "::1", "localhost", ""}


class OfflineGuardRefused(RuntimeError):
    pass


def _loopback(host):
    if host is None:
        return True
    h = str(host).strip("[]").lower()
    return h in _LOOP or h.startswith("127.")


def _check(kind, host, port=None):
    if _loopback(host):
        return
    if _LOG:
        try:
            with open(_LOG, "a", encoding="utf-8") as fh:
                fh.write(json.dumps({"kind": kind, "host": str(host), "port": port, "argv": sys.argv[:6]}) + "\n")
        except OSError:
            pass
    raise OfflineGuardRefused("OFFLINE GUARD (3.0.0_SA_CVO): refused %s to %s:%s -- this run is offline" % (kind, host, port))


def _addr(address):
    if isinstance(address, (tuple, list)) and address:
        return address[0], (address[1] if len(address) > 1 else None)
    return address, None


_connect, _connect_ex = socket.socket.connect, socket.socket.connect_ex
_create, _getaddrinfo = socket.create_connection, socket.getaddrinfo


def connect(self, address):
    _check("connect", *_addr(address))
    return _connect(self, address)


def connect_ex(self, address):
    _check("connect_ex", *_addr(address))
    return _connect_ex(self, address)


def create_connection(address, *a, **k):
    _check("create_connection", *_addr(address))
    return _create(address, *a, **k)


def getaddrinfo(host, port, *a, **k):
    _check("getaddrinfo", host, port)
    return _getaddrinfo(host, port, *a, **k)


socket.socket.connect, socket.socket.connect_ex = connect, connect_ex
socket.create_connection, socket.getaddrinfo = create_connection, getaddrinfo
