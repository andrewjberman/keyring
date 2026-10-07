"""NFRA_CTLPLN CT-b-2 (FWD-14): read-only check that every other box answers on TCP 3389 over the tailnet."""
import json
import os
import socket
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PORT = 3389
TIMEOUT = 5


def this_box():
    name = os.environ.get("AGENTBUS_DEVICE")
    if not name and sys.platform == "win32":
        try:
            import winreg
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Environment") as k:
                name = winreg.QueryValueEx(k, "AGENTBUS_DEVICE")[0]
        except OSError:
            name = None
    return (name or socket.gethostname()).strip().lower()


def probe(addr):
    try:
        with socket.create_connection((addr, PORT), timeout=TIMEOUT):
            return "open"
    except socket.timeout:
        return "timeout"
    except OSError as e:
        return "timeout" if "timed out" in str(e) else "refused"


def main():
    with open(os.path.join(HERE, "DEVICES.json"), encoding="utf-8") as f:
        devices = json.load(f)["devices"]
    me = this_box()
    results = []
    for d in devices:
        names = {d["name"].lower()} | {a.lower() for a in d.get("aliases", [])}
        addr = d.get("tailnet_address")
        if me in names or not addr:
            continue
        state = probe(addr)
        print("%s %s:%d %s" % (d["name"], addr, PORT, state))
        results.append((d["name"], "open" if state == "open" else "closed"))
    print("RDP-REACH " + " ".join("%s=%s" % r for r in results) + " checked=%d" % len(results))


if __name__ == "__main__":
    main()
