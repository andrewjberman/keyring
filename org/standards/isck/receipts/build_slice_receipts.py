#!/usr/bin/env python
"""WP-3b AC6 -- build the two receipt/evidence pairs, computing every digest from the OBJECT DB.

WHY A TOOL AND NOT TWO HAND-WRITTEN JSON FILES. `receipt_problem()` recomputes `manifest_digest` and
`evidence_digest` from `git cat-file blob <commit>:<path>` -- the COMMITTED bytes. A digest taken
over the working-tree file is a different number the moment Git's EOL policy touches the file, and
that exact split has cost this seat four corrections in this TO (once it refused a certification
receipt whose evidence I had hashed at 890 bytes / 5 CR where the blob was 885 / 0). So the manifest
digest is read from the blob, and the evidence is written LF-only and hashed as the bytes written.

WHAT IT REFUSES TO GUESS: the run pin. It is passed, resolved to 40 hex, and the runner's own stdout
must NAME it -- that is the R4-CVO-5 binding (`a run_commit the evidence never mentions is a claim,
not a run`), whose recorded negative control is this seat's own e8d3326bd5.

THE RECEIPT IS NOT THE REGISTRY WRITE. This TO delivers evidence; recording it on the frozen
v0.3-candidate+27 label is the label owner's act (`1.0.0_SA_CTO~X`).
"""
import hashlib
import json
import os
import subprocess
import sys

CR = chr(13)

HERE = os.path.dirname(os.path.abspath(__file__))
ISCK = os.path.dirname(HERE)
ROOT = os.path.abspath(os.path.join(ISCK, "..", "..", ".."))
sys.path.insert(0, ISCK)

MANIFEST_PATH = ("org/tier2_senior/0.4.0_DT_ClientPlatform/deliverables/D11_MANIFEST/"
                 "graph_object_manifest.declared.json")
RUNNER = "org/standards/isck/ledger/battery/run_slice.py"


def sha(b):
    return "sha256:" + hashlib.sha256(b).hexdigest()


def blob(commit, path):
    return subprocess.check_output(["git", "-C", ROOT, "cat-file", "blob", "%s:%s" % (commit, path)])


def run_slice(pin):
    """One clean-extract run. Returns its stdout, and REFUSES a run that did not exit 0."""
    out = subprocess.run([sys.executable, os.path.join(ROOT, RUNNER), "--run-commit", pin],
                         cwd=ISCK, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    # STRIP EVERY CR, not just CRLF pairs. The child runs inside the extract and writes CRLF to a
    # pipe; the parent re-translates its own newline on the way out, so a child line arrives here as
    # CR CR LF and a single CRLF->LF pass leaves ONE CR behind. Measured: 43 CRLF survived a replace
    # that read as correct. The evidence is line-oriented text with no legitimate bare CR, and its
    # digest must equal the committed blob's -- the fourth CRLF correction in this TO, and the class
    # always looks handled right up until the digest moves.
    text = out.stdout.decode("utf-8", "replace").replace(CR, "")
    if out.returncode != 0:
        raise SystemExit("REFUSING: the slice run exited %d; a receipt is cut from a PASS, and a "
                         "receipt for a failing run is the only thing worse than no receipt\n%s"
                         % (out.returncode, text[-2000:]))
    return text


def write(path, text):
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    with open(path, "rb") as fh:
        return sha(fh.read())


def build(kind, pin, header, body, label):
    ev_rel = "org/standards/isck/receipts/%s" % kind.replace("_receipt", "_evidence.txt")
    rc_rel = "org/standards/isck/receipts/%s.json" % kind
    text = header + "\n" + body
    if pin not in text and pin[:10] not in text:
        raise SystemExit("REFUSING: the evidence for %s never names run_commit %s -- that is a "
                         "claim, not a run (R4-CVO-5)" % (kind, pin[:10]))
    ev_digest = write(os.path.join(ROOT, ev_rel), text)
    receipt = {
        "kind": kind,
        "candidate_id": label["candidate_id"],
        "contract_bundle_id": label["contract_bundle_id"],
        "manifest_path": MANIFEST_PATH,
        "manifest_digest": sha(blob("HEAD", MANIFEST_PATH)),
        "result": "PASS",
        "evidence_path": ev_rel,
        "evidence_digest": ev_digest,
        "run_commit": pin,
    }
    with open(os.path.join(ROOT, rc_rel), "w", encoding="utf-8", newline="\n") as fh:
        json.dump(receipt, fh, indent=2, sort_keys=True)
        fh.write("\n")
    print("WROTE %s  (evidence %s, %d bytes)" % (rc_rel, ev_digest[:23] + "...", len(text)))
    return receipt


def main():
    if len(sys.argv) < 2:
        print("usage: build_slice_receipts.py <run-commit>")
        return 2
    import bundle_identity as bi
    pin = subprocess.check_output(["git", "-C", ROOT, "rev-parse", "--verify",
                                   "%s^{commit}" % sys.argv[1]]).decode().strip()
    label = bi.derive(pin)
    print("run pin %s | label %s" % (pin, label["candidate_id"]))

    first = run_slice(pin)
    second = run_slice(pin)

    # THE REPLAY EVIDENCE IS A SECOND, INDEPENDENT EXTRACT -- and the comparison is COMPUTED here
    # rather than asserted in prose. Volatile lines (temp paths, the snapshot's byte digest) are
    # excluded BY NAME and the exclusion is printed, so a reader can see what was compared instead
    # of trusting that "identical" meant everything.
    keys = ("AC3 admission", "AC3 falsifier", "bundle_digest", "AC4 replay", "AC4 agreement",
            "AC4 sec-2e", "AC4 falsifier", "AC5 verdict", "AC2 census", "emitted")
    def sel(t):
        return [ln for ln in t.split("\n") if any(k in ln for k in keys)]
    a, b = sel(first), sel(second)
    same = a == b
    cmp_block = ("\nDETERMINISM ACROSS TWO INDEPENDENT EXTRACTS OF %s\n"
                 "compared %d substantive line(s); EXCLUDED by name: the extract's temp path and\n"
                 "the AC5 published-artifact byte digest (both vary per run by construction)\n"
                 "VERDICT: %s\n" % (pin[:10], len(a),
                                    "IDENTICAL" if same else "DIFFER -- the run is not reproducible"))
    if not same:
        for x, y in zip(a, b):
            if x != y:
                cmp_block += "  run1: %s\n  run2: %s\n" % (x, y)
        raise SystemExit("REFUSING: two extracts of one pin disagree\n" + cmp_block)

    build("vertical_slice_receipt", pin,
          "WP-3b VERTICAL SLICE -- the runner's own stdout, first clean extract of %s\n"
          "42 real parts from the declared population; every number below was COUNTED by the run.\n"
          % pin, first, label)
    build("historical_replay_receipt", pin,
          "WP-3b HISTORICAL REPLAY -- second independent clean extract of %s\n"
          "The replay claim: both AC4 anchors resolve and agree, sec 2e holds in BOTH directions,\n"
          "an unbindable anchor is refused, and the whole run reproduces from a fresh extract.\n"
          % pin + cmp_block, second, label)
    print("\nBOTH PAIRS WRITTEN. They are NOT yet valid receipts: receipt_problem() reads the OBJECT\n"
          "DATABASE, so the files must be COMMITTED and then validated at that commit.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
