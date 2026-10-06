"""lib/devices.py -- the one reader of the device register org/devices/DEVICES.json (NFRA_CTLPLN FWD-2, C-REGISTRY).

A box is named once, in the register; every script that names devices asks this module instead of listing them.
Fail-closed: an unreadable or empty register raises (CLI: rc 3); it never falls back to a built-in list.

    python lib/devices.py names             # one canonical name per line
    python lib/devices.py resolve <label>   # canonical name for a name or alias (case-insensitive); rc 2 if unknown
    python lib/devices.py queue <label>     # the box's inbound queue name; rc 2 if unknown

OPAL_DEVICE_REGISTER=<path> points every reader at another register file (fixtures and proofs only).
"""
from __future__ import annotations

import json
import os
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
REGISTER = ROOT / "org" / "devices" / "DEVICES.json"


class RegisterError(RuntimeError):
    pass


def register_path() -> pathlib.Path:
    override = os.environ.get("OPAL_DEVICE_REGISTER", "").strip()
    return pathlib.Path(override) if override else REGISTER


def load(path: pathlib.Path | None = None) -> dict:
    p = path or register_path()
    try:
        reg = json.loads(p.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        raise RegisterError("ERROR: device register unreadable at %s (%s)" % (p, exc)) from exc
    if not reg.get("devices"):
        raise RegisterError("ERROR: device register at %s lists no devices" % p)
    return reg


def devices(reg: dict | None = None) -> list:
    return list((reg or load())["devices"])


def names(reg: dict | None = None) -> list:
    return [d["name"] for d in devices(reg)]


def resolve(label: str, reg: dict | None = None) -> str | None:
    """Canonical name for a box name or alias, case-insensitive; None when the register does not hold it."""
    want = (label or "").strip().lower()
    for d in devices(reg):
        if want in [d["name"].lower()] + [a.lower() for a in d.get("aliases", [])]:
            return d["name"]
    return None


def inbound_queue(label: str, reg: dict | None = None) -> str | None:
    name = resolve(label, reg)
    for d in devices(reg):
        if d["name"] == name:
            return d["inbound_queue"]
    return None


def main(argv: list) -> int:
    try:
        if argv[:1] == ["names"] and len(argv) == 1:
            print("\n".join(names()))
            return 0
        if argv[:1] in (["resolve"], ["queue"]) and len(argv) == 2:
            out = resolve(argv[1]) if argv[0] == "resolve" else inbound_queue(argv[1])
            if out is None:
                print("ERROR: %r is not a device in %s (holds: %s)" % (argv[1], register_path(), ", ".join(names())),
                      file=sys.stderr)
                return 2
            print(out)
            return 0
    except RegisterError as exc:
        print(str(exc), file=sys.stderr)
        return 3
    print("usage: python lib/devices.py names | resolve <label> | queue <label>", file=sys.stderr)
    return 64


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
