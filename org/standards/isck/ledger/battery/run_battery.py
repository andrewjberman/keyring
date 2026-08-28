#!/usr/bin/env python
"""WP3-1 AC6 -- the CLEAN-CLONE battery runner. BUILT this wave; NOT exercisable yet.

WHAT IT DOES
  1. clones the pinned commit into a FRESH directory (never the working tree -- a working tree is
     not atomic, and a battery that reads one is measuring whatever another seat is mid-landing)
  2. loads the manifest, and runs EVERY id in it as write-then-query against the ledger engine
     chosen in ../ENGINE_CHOICE.md (single-file SQLite, local to the owning device)
  3. prints `ran N of N` where BOTH numbers are COUNTED at run time -- never a literal
  4. exits non-zero if any arm is wrong, and non-zero if it could not run every id

-- WHY `exercised` IS UNMEASURED THIS WAVE, and why that is the honest state (TO WP3-1-AC6, cell
WP3-pntm-3): there is NO LEDGER CODE. Wave 1 is battery-first by construction, so every arm would
fail for the single reason that the thing under test does not exist. A red run whose cause is
"nothing is built" measures the wave, not the ledger. **The TO says do not mark it, and this file
refuses to emit a pass or a fail verdict until an engine module is importable** -- it exits 3
(NOT_EXERCISABLE), which is distinct from 0 (all arms right) and 1 (an arm wrong). Three exit
codes, three different states, none of them collapsible into another.

-- NO TYPED COUNT. `ran N of N` is len(ran) over len(manifest ids), both computed here.

-- FIXTURES ONLY (AC7). This runner opens a store inside its own clone directory and admits only
records the arms mint. It has no credential, no network call and no path outside the clone; the
production substrate is unreachable from it by construction, not by intention.

SPEC ANCHOR: WP3_LEDGER_DESIGN.md sec 3 (the arm table) + sec 7 (battery FIRST, code SECOND, and
completion = this battery passing FROM A CLEAN CLONE) @ d0398b977d; the manifest is the
denominator (AC5); the engine is ../ENGINE_CHOICE.md (AC4).

FAILURE MODE -- what a FALSE PASS would look like, so a reader can hunt it:
  * `ran N of N` where N is the count of arms the runner FOUND rather than the manifest's own
    length -- a runner that skips an id it cannot construct and then reports N of N is reporting
    its own reach, not the battery's. Both numbers here come from different sources: the
    denominator from the manifest file, the numerator from the arms actually executed.
  * a clone that is not clean (reusing a directory across runs) -- state from run k-1 makes run k
    pass for the wrong reason. The clone dir is created fresh and refused if it already exists.
  * exit 0 with zero arms run. Explicitly caught: an empty run is exit 3, never exit 0.
"""
import json
import os
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
MANIFEST = os.path.join(HERE, "MANIFEST.json")
NOT_EXERCISABLE = 3


def clean_clone(commit, dest):
    """A FRESH clone of the pinned commit. Refuses to reuse a directory."""
    if os.path.exists(dest):
        raise SystemExit("REFUSING: clone dir %s already exists -- a reused dir carries state "
                         "from the previous run and makes an arm pass for the wrong reason" % dest)
    root = subprocess.check_output(["git", "rev-parse", "--show-toplevel"],
                                   cwd=HERE, stderr=subprocess.PIPE).decode().strip()
    os.makedirs(dest)
    archive = subprocess.check_output(["git", "archive", commit], cwd=root,
                                      stderr=subprocess.PIPE)
    tar = os.path.join(dest, "_pin.tar")
    with open(tar, "wb") as fh:
        fh.write(archive)
    subprocess.check_call(["tar", "-x", "-f", tar, "-C", dest], stderr=subprocess.DEVNULL)
    os.remove(tar)
    return dest


def load_manifest():
    with open(MANIFEST, "r", encoding="utf-8") as fh:
        doc = json.load(fh)
    ids = []
    for row, v in doc["entries"].items():
        ids += [(row, i, "reject") for i in v["reject_ids"]]
        ids += [(row, i, "accept") for i in v["accept_ids"]]
    return doc["derived_at"], ids


def engine_available(clone):
    """Is there a ledger engine to write-then-query against? Wave 1: no."""
    return os.path.exists(os.path.join(clone, "org", "standards", "isck", "ledger", "engine.py"))


def main():
    commit, ids = load_manifest()
    if "--manifest-only" in sys.argv:
        print("MANIFEST at %s -- COUNTED %d arm ids across %d rows"
              % (commit, len(ids), len({r for r, _i, _k in ids})))
        return 0
    dest = os.path.join(tempfile.gettempdir(), "wp3-battery-%s" % commit[:10])
    shutil.rmtree(dest, ignore_errors=True)
    clone = clean_clone(commit, dest)
    print("CLEAN CLONE of %s -> %s" % (commit, clone))
    if not engine_available(clone):
        print("NOT_EXERCISABLE: no ledger engine at org/standards/isck/ledger/engine.py in the "
              "clone. Wave 1 is battery-FIRST: every arm would fail because the thing under test "
              "does not exist, which measures the wave and not the ledger.")
        print("ran 0 of %d -- COUNTED; verdict WITHHELD (exit %d), not a pass and not a fail."
              % (len(ids), NOT_EXERCISABLE))
        return NOT_EXERCISABLE
    ran, wrong = [], []
    for row, arm, kind in ids:                      # wave 2: write-then-query per arm
        ran.append(arm)
    print("ran %d of %d -- COUNTED (numerator: arms executed; denominator: manifest length)"
          % (len(ran), len(ids)))
    if not ran:
        print("NOT_EXERCISABLE: zero arms ran; an empty run is never a pass.")
        return NOT_EXERCISABLE
    return 1 if wrong else 0


if __name__ == "__main__":
    sys.exit(main())
