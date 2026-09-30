"""TR-g-1 -- the registry rows and the regenerated targets (issuer's check; base: FAIL as expected on both modes).

usage: python r1_registry_check.py rows     -> REGISTRY-OK outlook=<addr> sharepoint=<addr>   (validate rc 0 + both addresses build)
       python r1_registry_check.py targets  -> TARGETS-IN-SYNC n=N                             (generate in place; git reports no moved target)
"""
import subprocess
import sys


def rows():
    sys.path.insert(0, ".")
    from lib.opal_naming import address  # noqa: E402
    rc = subprocess.call([sys.executable, "lib/opal_naming.py", "validate"])
    if rc != 0:
        print("REGISTRY-REFUSED validate rc=%d" % rc)
        return 1
    try:
        o = address("outlook", "transcripts", "bronze", "analysis_commentary", "date=2026-09-23", "msg_x.json")
        s = address("sharepoint", "transcripts", "bronze", "market_update", "date=2026-07-27", "x.pptx")
    except Exception as e:  # noqa: BLE001
        print("REGISTRY-REFUSED %s" % e)
        return 1
    print("REGISTRY-OK outlook=%s sharepoint=%s" % (o, s))
    return 0


def targets():
    """generate IN PLACE (the builder rewrites only its marked spans inside each carrier), then ask git whether any
    target moved: clean = the committed targets are what the registry produces now."""
    out = subprocess.run([sys.executable, "lib/opal_naming.py", "targets"], capture_output=True, text=True)
    # lines read: "SHIP <plane> <path> measured: ..." or "REPO-ONLY <plane> <path> measured: ..."
    paths = [ln.split()[2] for ln in out.stdout.splitlines()
             if ln.startswith(("SHIP ", "REPO-ONLY ")) and len(ln.split()) > 2 and "/" in ln.split()[2]]
    if not paths:
        print("TARGETS-BAD could not parse the target list: %s" % out.stdout[:800])
        return 1
    rc = subprocess.call([sys.executable, "lib/opal_naming.py", "generate", "--out", "."])
    if rc != 0:
        print("TARGETS-BAD generate rc=%d" % rc)
        return 1
    ws = [p for p in paths if not p.startswith("portal/")]
    moved = subprocess.run(["git", "diff", "--name-only", "--"] + ws, capture_output=True, text=True).stdout.split()
    portal = [p[len("portal/"):] for p in paths if p.startswith("portal/")]
    if portal:
        moved += ["portal/" + m for m in subprocess.run(["git", "-C", "portal", "diff", "--name-only", "--"] + portal,
                                                          capture_output=True, text=True).stdout.split()]
    if moved:
        print("TARGETS-STALE n=%d moved=%s (regenerated in place; commit them)" % (len(paths), moved))
        return 1
    print("TARGETS-IN-SYNC n=%d" % len(paths))
    return 0


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) == 2 else ""
    sys.exit({"rows": rows, "targets": targets}.get(mode, lambda: (print("usage: rows|targets"), 2)[1])())
