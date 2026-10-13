"""lib/devices.py -- the one reader of the device register org/devices/DEVICES.json (NFRA_CTLPLN FWD-2, C-REGISTRY).

A box is named once, in the register; every script that names devices asks this module instead of listing them.
Fail-closed: an unreadable or empty register raises (CLI: rc 3); it never falls back to a built-in list.

    python lib/devices.py names             # one canonical name per line
    python lib/devices.py resolve <label>   # canonical name for a name or alias (case-insensitive); rc 2 if unknown
    python lib/devices.py queue <label>     # the box's inbound queue name; rc 2 if unknown
    python lib/devices.py this              # this box, from its own AGENTBUS_DEVICE setting; rc 2 if unset/unknown
    python lib/devices.py placement         # one placement value per line (the project-row `fabric` values)

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


def senders(reg: dict | None = None) -> list:
    """Sender-only tailnet identities (top-level `senders`): accepted as agentbus `from_tailnet`, never a box."""
    return list((reg or load()).get("senders") or [])


def held_tailnet_names(reg: dict | None = None) -> list:
    """Every tailnet name an agentbus consumer accepts: each box's, then each sender-only identity's."""
    reg = reg or load()
    return [d["tailnet_name"] for d in devices(reg) + senders(reg) if d.get("tailnet_name")]


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


def placement_values(reg: dict | None = None) -> tuple:
    """The values a project row's `fabric` may hold, one per box, in register order (NFRA_CTLPLN C-PLACEMENT).
    A box's value is its register name, except that a box holding a hyphenated alias which is its own name with hyphens
    (name `sitez`, alias `site-z`) is placed under that alias. Add a box to the register and it appears here."""
    out = []
    for d in devices(reg):
        spelled = [a for a in d.get("aliases", []) if "-" in a and a.replace("-", "").lower() == d["name"].lower()]
        out.append(spelled[0].lower() if spelled else d["name"])
    return tuple(out)


def lane_suffix(label: str, reg: dict | None = None) -> str | None:
    """The `~lane` suffix the box's seats carry, derived from its register row: "" for the box that runs every lane no
    other box claims (lane_letters_default), `~<first lane letter>` for a box with lane letters, else `~<NAME>` upper-case.
    None when the register does not hold the box."""
    name = resolve(label, reg)
    for d in devices(reg):
        if d["name"] == name:
            if d.get("lane_letters_default"):
                return ""
            letters = d.get("lane_letters") or []
            return "~" + (letters[0] if letters else name.upper())
    return None


def seat_serial(base: str, label: str, reg: dict | None = None) -> str:
    """`base` (e.g. a Tier-1 serial without a lane) carried to the box: base + lane_suffix. "" when the box is unknown."""
    suffix = lane_suffix(label, reg)
    return "" if suffix is None else base + suffix


def setting() -> tuple:
    """(claim, basis): the box's own AGENTBUS_DEVICE setting -- the process environment, else the persisted user setting
    (HKCU\\Environment; AGENTBUS_REG_KEY overrides the key for proofs) for a process started before it was made.
    ("", "unset") when neither holds it. Never derived from a path (LD-0405)."""
    claim = os.environ.get("AGENTBUS_DEVICE", "").strip()
    if claim:
        return claim, "process environment"
    key = os.environ.get("AGENTBUS_REG_KEY", "HKCU\\Environment")
    try:
        import winreg
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key.split("\\", 1)[1]) as k:
            claim = str(winreg.QueryValueEx(k, "AGENTBUS_DEVICE")[0]).strip()
    except (ImportError, IndexError, OSError):
        claim = ""
    return (claim, "persisted user setting %s" % key) if claim else ("", "unset")


def this_device(reg: dict | None = None) -> tuple:
    """(name or None, basis): this box's canonical register name, resolved from its own setting."""
    claim, basis = setting()
    if not claim:
        return None, "AGENTBUS_DEVICE unset (process environment and persisted user setting)"
    name = resolve(claim, reg)
    return (name, "AGENTBUS_DEVICE=%s (%s)" % (claim, basis)) if name else (
        None, "AGENTBUS_DEVICE=%s is not in the device register" % claim)


def main(argv: list) -> int:
    try:
        if argv[:1] == ["names"] and len(argv) == 1:
            print("\n".join(names()))
            return 0
        if argv == ["this"]:
            name, basis = this_device()
            if name is None:
                print("ERROR: this box is unresolved: %s" % basis, file=sys.stderr)
                return 2
            print(name)
            return 0
        if argv == ["placement"]:
            print("\n".join(placement_values()))
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
    print("usage: python lib/devices.py names | placement | resolve <label> | queue <label> | this", file=sys.stderr)
    return 64


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
