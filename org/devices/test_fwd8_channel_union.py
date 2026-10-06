"""FWD-8 read half (NFRA_CTLPLN C-ONE-WRITER): the channel readers see the UNION of a channel's per-box files.

Run: python org/devices/test_fwd8_channel_union.py   (exit 0 = every check passed)

Fixture: a throwaway git repo holding ONE tree-project channel (FIXT) split across three append files -- the laptop's
INVESTIGATION_v1.md, a device-suffixed INVESTIGATION_v1.sitez.md and a lane-letter-suffixed INVESTIGATION_v1.Z.md (the form
SURPRISE_CHANNEL_PROTOCOL.md s.8 rules today). Read through the REAL tools, unedited:
  - .tools/comp-surprise.py --project FIXT --json, run with the fixture as its working tree (its ROOT is the cwd's top level);
  - .tools/surprise-row-gate.py _plane_duplicates, the gate's own cross-document id census over the fixture's INDEX.
NEGATIVE CONTROL: an id minted in two boxes' files must be reported as a duplicate, or the clean result proves nothing.
"""
import importlib.util
import json
import os
import pathlib
import subprocess
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parents[2]
TOOLS = ROOT / ".tools"
CH = "org/missions/D0/NFRA/FIXT/surprise-channel/investigations"


def row(rid, fabric):
    return {"id": rid, "project": "FIXT", "fabric": fabric, "surfaced_by": "2.0.0_SA_COO~C", "surfaced_at": "2026-10-06T16:00Z",
            "one_line": "fixture row %s" % rid, "class": "OBSERVATION", "hazard_standing": "NONE"}


def doc(rows):
    return "# FIXT -- fixture channel\n\n```json\n%s\n```\n" % json.dumps(rows, indent=2)


def git(root, *args):
    return subprocess.run(["git", "-C", str(root)] + list(args), capture_output=True, text=True, encoding="utf-8",
                          errors="replace")


def build(root, files):
    git(root, "init", "-q")
    git(root, "config", "core.autocrlf", "false")
    d = root / CH
    d.mkdir(parents=True, exist_ok=True)
    for f in d.iterdir():
        f.unlink()
    for name, rows in files.items():
        (d / name).write_text(doc(rows), encoding="utf-8", newline="\n")
    git(root, "add", "-A")


def surprise_ids(root):
    r = subprocess.run([sys.executable, str(TOOLS / "comp-surprise.py"), "--project", "FIXT", "--json"], cwd=str(root),
                       capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=120)
    try:
        data = json.loads(r.stdout)
    except ValueError:
        return None, r.stdout[-300:] + r.stderr[-300:]
    items = data.get("items", data) if isinstance(data, dict) else data
    return sorted(i.get("id") for i in items if isinstance(i, dict)), ""


def gate():
    spec = importlib.util.spec_from_file_location("srg", str(TOOLS / "surprise-row-gate.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main():
    results = []
    g = gate()
    with tempfile.TemporaryDirectory() as tmp:
        root = pathlib.Path(tmp)
        build(root, {"INVESTIGATION_v1.md": [row("FIXT-S1", "laptop"), row("FIXT-S2", "laptop")],
                     "INVESTIGATION_v1.sitez.md": [row("FIXT-S3", "sitez")],
                     "INVESTIGATION_v1.Z.md": [row("FIXT-S4", "sitez")]})
        ids, err = surprise_ids(root)
        results.append(("comp-surprise reads all three per-box files of one channel",
                        ids == ["FIXT-S1", "FIXT-S2", "FIXT-S3", "FIXT-S4"], "%s %s" % (ids, err)))
        dups, note = g._plane_duplicates(str(root), "FIXT")
        results.append(("surprise-row-gate census over the union: no duplicate id", dups == {}, "%s %s" % (dups, note)))
        docs, note = g._plane_docs(str(root), "FIXT", "INVESTIGATION", "")
        names = sorted(os.path.basename(p) for p, _ in (docs or []))
        results.append(("surprise-row-gate plane holds all three files",
                        names == ["INVESTIGATION_v1.Z.md", "INVESTIGATION_v1.md", "INVESTIGATION_v1.sitez.md"], str(names)))

        build(root, {"INVESTIGATION_v1.md": [row("FIXT-S1", "laptop"), row("FIXT-S2", "laptop")],
                     "INVESTIGATION_v1.sitez.md": [row("FIXT-S2", "sitez")]})
        dups, note = g._plane_duplicates(str(root), "FIXT")
        results.append(("CONTROL: an id minted in two boxes' files is reported", sorted(dups or {}) == ["FIXT-S2"]
                        and len((dups or {}).get("FIXT-S2", [])) == 2, "%s %s" % (dups, note)))
    fails = 0
    for name, ok, detail in results:
        print("%s: %s" % ("PASS" if ok else "FAIL", name))
        if not ok:
            fails += 1
            print("      " + detail)
    print("RESULT: %d passed, %d failed (of %d)" % (len(results) - fails, fails, len(results)))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
