#!/usr/bin/env python3
"""integrate-directives -- the cross-fabric register reconcile, per ROW, keyed on PLACEMENT.

Read-only. Emits a comparison and an exchange digest; it NEVER writes DIRECTIVES.yaml.
The write is the register owner's act, taken after reading this output.

WHY PER-ROW AND NOT PER-FILE: both fabrics legitimately edit this file, so a whole-file
verdict is always "differs" and tells you nothing about WHICH side is right. The row is the
unit that has an owner. `placement` names that owner, so it is also the field that decides
who may write the row -- which makes placement itself the one field neither MSTR may resolve.

Usage:
  integrate-directives compare [--json]     CLOUD vs SITEZ, per row, with an authority verdict
  integrate-directives digest [--ref REF]   the status digest THIS fabric owes its peer
  integrate-directives --self-test          5 controls; must print PASS n/n
"""
import argparse
import hashlib
import io
import json
import os
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

REGISTER = "org/missions/DIRECTIVES.yaml"
PROJECTS = "org/projects"
# The fields a row carries. `placement` is separated deliberately -- see VERDICTS below.
CONTENT_FIELDS = ("title", "directive", "members", "stance")


def _sh(args):
    """Run git. encoding is EXPLICIT: the estate's own commit messages and register text
    carry non-ASCII, and a locale decode (cp1252 on Windows) raises rather than reads."""
    r = subprocess.run(args, capture_output=True, text=True,
                       encoding="utf-8", errors="replace", timeout=60)
    return r.returncode, r.stdout, r.stderr


def load_register(ref):
    """ref=None reads the worktree; otherwise the blob at that ref."""
    import yaml
    if ref is None:
        raw = io.open(REGISTER, encoding="utf-8").read()
    else:
        rc, out, err = _sh(["git", "show", "%s:%s" % (ref, REGISTER)])
        if rc != 0:
            raise SystemExit("BLOCKED: cannot read %s at %s -- %s" % (REGISTER, ref, err.strip()))
        # A mangled ref returns clean-empty; that is an UNRESOLVED read, never an empty register.
        if not out.strip():
            raise SystemExit("BLOCKED: %s at %s read EMPTY. That is unresolved, not absent." % (REGISTER, ref))
        raw = out
    d = yaml.safe_load(raw)
    return d.get("directives") or {}


def fabric_of(placement):
    """The owning fabric token, or None when the row does not name one.
    A row whose placement does not start with a known token is UNOWNED, and an unowned
    row is a finding -- never a default to either side."""
    p = (placement or "").strip().upper()
    for tok in ("LAPTOP", "SITEZ"):
        if p.startswith(tok):
            return tok
    return None


def project_state(code):
    p = os.path.join(PROJECTS, "%s.json" % code)
    if not os.path.exists(p):
        return {"code": code, "present": False}
    try:
        j = json.load(io.open(p, encoding="utf-8"))
    except Exception as exc:
        return {"code": code, "present": True, "unreadable": str(exc)}
    return {
        "code": code,
        "present": True,
        "status": j.get("status"),
        "dep_stage": j.get("dep_stage"),
        "prds": len(j.get("prds") or []),
    }


def digest(ref=None):
    """What THIS fabric owes its peer: for every row, the placement token and -- for rows this
    fabric OWNS -- the derived member state.

    NOTHING HERE IS WRITTEN BACK INTO THE REGISTER. Directive status is DERIVED from the member
    project files, which already carry it. Materialising it onto the register row would create a
    SECOND CARRIER of a quantity that already has one, and second carriers drift silently.
    """
    D = load_register(ref)
    rows = {}
    for code in sorted(D, key=lambda x: (len(x), x)):
        v = D[code] or {}
        members = ((v.get("members") or {}).get("projects") or [])
        row = {
            "title": v.get("title"),
            "placement_fabric": fabric_of(v.get("placement")),
            "placement_sha": hashlib.sha256(
                (v.get("placement") or "").encode("utf-8")).hexdigest()[:12],
            "members": members,
        }
        row["member_state"] = [project_state(c) for c in members]
        rows[code] = row
    return {"register": REGISTER, "ref": ref or "WORKTREE", "rows": rows}


VERDICTS = """
  AGREE            both sides byte-identical on this row. Nothing to do.
  CONTENT-DIFFERS  placement AGREES, content does not. The OWNING fabric's copy wins --
                   that is what placement is for. Mechanical, no adjudication.
  PLACEMENT-DIFFERS  the two sides disagree about WHO OWNS the row.
                   -> NEITHER MSTR MAY RESOLVE THIS. Placement is a sovereign act.
                      Two sub-cases, and they look identical in a diff:
                      (a) STALE  -- one side has not yet merged the other's record of the
                          same Andrew word. Compare the quoted words; if one side's text is
                          contained in the other's history, that side is simply behind.
                      (b) CONVERGENT -- Andrew ruled at BOTH terminals separately. Measured
                          2026-09-01: he ruled D8 to LAPTOP at the CTO terminal ~02:4xZ and
                          again at the MSTR terminal ~03:0xZ, 20 minutes apart, neither seat
                          aware of the other. Convergent, not conflicting.
                      Only if the two words genuinely CONTRADICT is this a question for him.
  ROW-MISSING      a row exists on one side only. Usually a mint the peer has not merged.
                   Never delete; merge forward.
  UNOWNED          placement names no known fabric. A FINDING, not a default -- do not
                   assign it to whichever side you happen to be standing on.
"""


def compare(a_ref, b_ref, a_name, b_name):
    A, B = load_register(a_ref), load_register(b_ref)
    out = []
    for code in sorted(set(A) | set(B), key=lambda x: (len(x), x)):
        if code not in A or code not in B:
            out.append((code, "ROW-MISSING", "present only on %s" % (a_name if code in A else b_name)))
            continue
        pa, pb = A[code].get("placement"), B[code].get("placement")
        fa, fb = fabric_of(pa), fabric_of(pb)
        if fa is None or fb is None:
            out.append((code, "UNOWNED", "placement names no fabric on %s" %
                        (a_name if fa is None else b_name)))
            continue
        if pa != pb:
            same_owner = "same owner (%s), text differs" % fa if fa == fb else "OWNER DIFFERS: %s vs %s" % (fa, fb)
            out.append((code, "PLACEMENT-DIFFERS", same_owner))
            continue
        diff = [f for f in CONTENT_FIELDS if A[code].get(f) != B[code].get(f)]
        if diff:
            out.append((code, "CONTENT-DIFFERS", "owner %s wins; fields: %s" % (fa, ", ".join(diff))))
        else:
            out.append((code, "AGREE", "owner %s" % fa))
    return out


def self_test():
    """Five controls. Each must DISCRIMINATE -- an arm that cannot fail proves nothing."""
    checks = []
    base = {"D1": {"title": "t", "directive": "d", "placement": "LAPTOP -- x",
                   "members": {"projects": []}, "stance": "s"}}

    def cmp2(a, b):
        return _compare_dicts(a, b)

    def _compare_dicts(A, B):
        res = []
        for code in sorted(set(A) | set(B)):
            if code not in A or code not in B:
                res.append((code, "ROW-MISSING"))
                continue
            pa, pb = A[code].get("placement"), B[code].get("placement")
            fa, fb = fabric_of(pa), fabric_of(pb)
            if fa is None or fb is None:
                res.append((code, "UNOWNED"))
                continue
            if pa != pb:
                res.append((code, "PLACEMENT-DIFFERS"))
                continue
            if [f for f in CONTENT_FIELDS if A[code].get(f) != B[code].get(f)]:
                res.append((code, "CONTENT-DIFFERS"))
                continue
            res.append((code, "AGREE"))
        return res

    import copy
    a = copy.deepcopy(base)
    checks.append(("identical -> AGREE", cmp2(a, copy.deepcopy(base))[0][1] == "AGREE"))
    b = copy.deepcopy(base)
    b["D1"]["stance"] = "CHANGED"
    checks.append(("content moved -> CONTENT-DIFFERS", cmp2(a, b)[0][1] == "CONTENT-DIFFERS"))
    c = copy.deepcopy(base)
    c["D1"]["placement"] = "SITEZ -- x"
    checks.append(("placement moved -> PLACEMENT-DIFFERS", cmp2(a, c)[0][1] == "PLACEMENT-DIFFERS"))
    e = copy.deepcopy(base)
    e["D1"]["placement"] = "AT ANDREW -- not set"
    checks.append(("unowned placement -> UNOWNED", cmp2(a, e)[0][1] == "UNOWNED"))
    checks.append(("missing row -> ROW-MISSING", cmp2(a, {})[0][1] == "ROW-MISSING"))

    ok = sum(1 for _, r in checks if r)
    for name, r in checks:
        print("  %-40s %s" % (name, "PASS" if r else "FAIL"))
    print("self-test: %s (%d/%d -- the instrument discriminates)" %
          ("PASS" if ok == len(checks) else "FAIL", ok, len(checks)))
    return 0 if ok == len(checks) else 1


def main(argv):
    ap = argparse.ArgumentParser(prog="integrate-directives")
    ap.add_argument("mode", nargs="?", default="compare", choices=["compare", "digest"])
    ap.add_argument("--a", default="origin/CLOUD")
    ap.add_argument("--b", default="origin/SITEZ")
    ap.add_argument("--ref", default=None)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args(argv)

    if args.self_test:
        return self_test()

    if args.mode == "digest":
        d = digest(args.ref)
        if args.json:
            print(json.dumps(d, indent=1, ensure_ascii=True))
            return 0
        print("REGISTER DIGEST -- %s @ %s" % (d["register"], d["ref"]))
        print("  DENOMINATOR: %d directive row(s)" % len(d["rows"]))
        for code, r in d["rows"].items():
            owned = r["placement_fabric"] or "UNOWNED"
            st = ["%s=%s" % (m["code"], m.get("status") or "?") for m in r["member_state"]]
            print("  %-4s %-7s %-34s %s" % (code, owned, (r["title"] or "")[:34],
                                            (", ".join(st))[:70] or "(no members)"))
        return 0

    rows = compare(args.a, args.b, args.a, args.b)
    if args.json:
        print(json.dumps([{"code": c, "verdict": v, "note": n} for c, v, n in rows],
                         indent=1, ensure_ascii=True))
        return 0
    print("REGISTER COMPARE  %s  vs  %s" % (args.a, args.b))
    print("  DENOMINATOR: %d row(s) across both sides" % len(rows))
    print()
    for c, v, n in rows:
        print("  %-4s %-18s %s" % (c, v, n))
    from collections import Counter
    tally = Counter(v for _, v, _ in rows)
    print()
    print("  " + " | ".join("%s %d" % (k, tally[k]) for k in sorted(tally)))
    if tally.get("PLACEMENT-DIFFERS"):
        print()
        print("  BLOCKED: a placement disagreement is NOT an MSTR's to resolve. See VERDICTS.")
    print(VERDICTS)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
