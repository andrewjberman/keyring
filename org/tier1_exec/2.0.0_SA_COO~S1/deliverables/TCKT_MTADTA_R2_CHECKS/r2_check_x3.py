"""TCKT_MTADTA round 2, cell MD-x-3 checks (the first-content read). Run from the repo (worktree) root.

  python r2_check_x3.py reads -> X3-READS-OK  (counts only: volume per person, event types, the id-only actor count)
  python r2_check_x3.py quiet -> X3-QUIET-OK  (a day with no rows reads as quiet, never blank; a refused door raises)
"""
import base64
import importlib.util
import json
import os
import sys

ROOT = os.getcwd()
SCRIPT = os.path.join(ROOT, "data", "m365_metadata", "scripts", "silver", "first_content.py")
EIGHT = [n + "@opalinvest.com" for n in ("andrew", "alyssa", "bobby", "manav", "yang", "menachem", "jim", "jeanette")]
PFX = "m365-metadata/trino/"
COV1 = PFX + "gold/collection_coverage/date=2026-10-15/coverage_20261015T200000Z.json"
COV2 = PFX + "gold/collection_coverage/date=2026-10-15/coverage_20261015T210000Z.json"


def load():
    if not os.path.exists(SCRIPT):
        raise FileNotFoundError(SCRIPT)
    spec = importlib.util.spec_from_file_location("x3_first_content", SCRIPT)
    m = importlib.util.module_from_spec(spec)
    sys.path.insert(0, os.path.dirname(SCRIPT))
    spec.loader.exec_module(m)
    return m


def row(op, wl, name="recon-synthetic.xlsx"):
    return {"event_id": "e", "creation_time": "2026-10-15T14:00:00Z", "operation": op, "workload": wl, "file_name": name,
            "folder": "Shared Documents/Synthetic", "site": "https://synthetic.example/sites/ops", "subject_hash": "ab" * 32,
            "participants": "internal-other,external"}


def fake(counts, quiet=False, refuse=False):
    calls = []

    def invoke(p):
        calls.append(p["op"])
        if refuse:
            return {"ok": False, "error": "refused"}
        if p["op"] == "get_day":
            n = counts.get(p["person"], 0)
            return {"ok": True, "rows": [row("FileAccessed", "SharePoint") for _ in range(n)] + ([row("Send", "Exchange")] if n else [])}
        if p["op"] == "list_state":
            return {"ok": True, "keys": [] if quiet else [COV1, COV2]}
        if p["op"] == "get_state":
            doc = {"records": [{"content_type": "Audit.SharePoint", "dropped": {"SharePoint": 3}, "dropped_id_only": 2 if p["key"] == COV1 else 1}]}
            return {"ok": True, "body_b64": base64.b64encode(json.dumps(doc).encode()).decode()}
        return {"ok": False}

    return invoke, calls


def reads():
    m = load()
    bad = []
    counts = {"yang@opalinvest.com": 4, "bobby@opalinvest.com": 1}
    invoke, calls = fake(counts)
    text = m.report(invoke, "2026-10-15")
    if calls.count("get_day") != 8:
        bad.append("the eight days were not all asked for (%d get_day calls)" % calls.count("get_day"))
    for needle in ("yang@opalinvest.com", "bobby@opalinvest.com"):
        if needle not in text:
            bad.append("no volume line for %s" % needle)
    if "SharePoint" not in text or "FileAccessed" not in text or "Send" not in text:
        bad.append("no event-type histogram")
    if not any(("id-only" in ln.lower() and "3" in ln) for ln in text.splitlines()):
        bad.append("the id-only actor count (2 + 1 across the day's fires) is missing")
    for secret in ("recon-synthetic", "Synthetic", "synthetic.example", "abababab", "internal-other"):
        if secret in text:
            bad.append("the report carries %r; counts only" % secret)
    if bad:
        print("X3-READS-REFUSED " + "; ".join(bad))
        return 1
    print("X3-READS-OK lines=%d" % len(text.splitlines()))
    return 0


def quiet():
    m = load()
    bad = []
    invoke, _ = fake({}, quiet=True)
    text = m.report(invoke, "2026-10-15")
    if not text.strip() or "no activity collected" not in text:
        bad.append("a quiet day must read 'no activity collected', not blank")
    invoke, _ = fake({}, refuse=True)
    try:
        m.report(invoke, "2026-10-15")
        bad.append("a refused door did not raise")
    except RuntimeError:
        pass
    if bad:
        print("X3-QUIET-REFUSED " + "; ".join(bad))
        return 1
    print("X3-QUIET-OK")
    return 0


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else ""
    fn = {"reads": reads, "quiet": quiet}.get(mode)
    try:
        sys.exit(fn() if fn else 2)
    except FileNotFoundError as e:
        print("X3-%s-REFUSED missing %s" % (mode.upper(), e))
        sys.exit(1)
    except Exception as e:  # noqa: BLE001
        print("X3-%s-REFUSED %s: %s" % (mode.upper(), type(e).__name__, e))
        sys.exit(1)
