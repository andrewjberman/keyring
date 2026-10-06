"""Shape test for org/devices/DEVICES.json (NFRA_CTLPLN FWD-2, contract C-REGISTRY).

Run: python org/devices/test_devices.py   (exit 0 = every check passed)

Checks the register is one consistent source: unique box names and aliases, one control plane, one integrator,
disjoint lane letters with one default box, every value's claim in the declared claim set, and every MEASURED
inbound queue present in the pinned bytes (git:<commit>:<path>) the register cites for it.
"""
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent
ROLES = {"control-plane", "integrator", "execution"}
REQUIRED = ("name", "aliases", "role", "role_claim", "inbound_queue", "inbound_queue_claim", "seat_limit",
            "seat_limit_claim", "lane_letters", "lane_letters_default", "lane_letters_claim")


def check(reg):
    """Return a list of failure strings for the register dict; empty means it passes."""
    fails = []
    claims = set(reg.get("claim_values", []))
    devices = reg.get("devices", [])
    if not devices:
        return ["no devices"]
    seen, letters, defaults = {}, {}, []
    for d in devices:
        missing = [k for k in REQUIRED if k not in d]
        if missing:
            fails.append("%s: missing %s" % (d.get("name"), missing))
            continue
        for label in [d["name"]] + list(d["aliases"]):
            if label in seen:
                fails.append("label %r used by %s and %s" % (label, seen[label], d["name"]))
            seen[label] = d["name"]
        if d["role"] not in ROLES:
            fails.append("%s: role %r not in %s" % (d["name"], d["role"], sorted(ROLES)))
        for k in [k for k in d if k.endswith("_claim")]:
            if d[k] not in claims:
                fails.append("%s: %s=%r not in claim_values" % (d["name"], k, d[k]))
        for ch in d["lane_letters"]:
            if ch in letters:
                fails.append("lane letter %s on %s and %s" % (ch, letters[ch], d["name"]))
            letters[ch] = d["name"]
        if d["lane_letters_default"]:
            defaults.append(d["name"])
        if d["inbound_queue_claim"] == "measured":
            # A measured value names the pinned bytes it was read from: "git:<commit>:<path> ...".
            pin = d.get("inbound_queue_source", "").split(" ")[0]
            parts = pin.split(":", 2)
            text = ""
            if len(parts) == 3 and parts[0] == "git":
                r = subprocess.run(["git", "-C", str(ROOT), "show", "%s:%s" % (parts[1], parts[2])],
                                   capture_output=True, text=True, encoding="utf-8", errors="replace")
                text = r.stdout if r.returncode == 0 else ""
            if d["inbound_queue"].replace("agentbus-ajbdev-", "") not in text:
                fails.append("%s: measured queue %r not found at %r" % (d["name"], d["inbound_queue"], pin))
    roles = [d.get("role") for d in devices]
    for role in ("control-plane", "integrator"):
        if roles.count(role) != 1:
            fails.append("role %s held by %d boxes (want 1)" % (role, roles.count(role)))
    if len(defaults) != 1:
        fails.append("lane_letters_default on %d boxes (want 1): %s" % (len(defaults), defaults))
    return fails


def main():
    reg = json.loads((HERE / "DEVICES.json").read_text(encoding="utf-8"))
    fails = check(reg)
    # Negative controls: each mutant must be caught, or the checks above prove nothing.
    mutants = {
        "duplicate alias": lambda r: r["devices"][1]["aliases"].append("laptop"),
        "second integrator": lambda r: r["devices"][0].update(role="integrator"),
        "claim outside the set": lambda r: r["devices"][0].update(role_claim="assumed"),
        "shared lane letter": lambda r: r["devices"][0]["lane_letters"].append("Z"),
        "measured queue absent from its source": lambda r: r["devices"][0].update(inbound_queue="agentbus-ajbdev-nope.fifo"),
    }
    for name, mutate in mutants.items():
        m = json.loads(json.dumps(reg))
        mutate(m)
        if not check(m):
            fails.append("CONTROL: mutant %r not caught" % name)
    for f in fails:
        print("FAIL: " + f)
    n = len(reg.get("devices", []))
    print("RESULT: %d device(s), %d mutant(s) caught, %d failure(s)" % (n, len(mutants), len(fails)))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
