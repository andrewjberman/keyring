#!/usr/bin/env python3
"""surprise-row-gate -- the STEP-7 / STEP-10 ROW VALIDATOR (Andrew-direct 2026-09-01).

AUTHORIZATION: /open-calls card 2 of 9, REC "MANDATE the three that are already schema-backed
(step 7's two trigger fields, step 9's disposition enum, step 10's route + loop_target) and DEFER
the markdown-to-JSON container swap" -> "All recs approved". The container swap was subsequently
DECLINED at this lane on measured grounds (census @0c7853c17f, DEF=1); this gate is the half that
survives, and it is the half that carries the structured guarantee.

WHAT IT REFUSES, on a staged org/surprise_channel/**/{INVESTIGATION,REMEDIATION}_v*.md:
  NEW investigation row  -> must carry spec_asserts AND world_is (the step-7 trigger's two halves)
  NEW remediation row    -> must carry route AND loop_target, and the pair must satisfy the
                            LOCKED MAPPING  SPEC_ERROR->6 | DECOMP_INVALIDATING->5 | SCOPE_CHANGE->2
  ANY new row            -> must satisfy its schema's REQUIRED fields and closed enums

=================================================================================================
PROSPECTIVE BY CONSTRUCTION, AND THAT IS A DESIGN CHOICE WITH A REASON
=================================================================================================
~190 rows across 18 files predate these fields. Making them schema-REQUIRED would invalidate every
one of them at a stroke; making them gate-required for EVERY row would refuse every future append
to a legacy file. So the gate diffs ROW IDS between HEAD and the STAGED blob and validates ONLY
IDS THAT ARE NEW IN THIS COMMIT. Andrew-direct 2026-09-01: "Dont get caught up on historical TOs,
this is a relatively new system and something we need to maintain now and prospectively."

=================================================================================================
WHY route AND loop_target DO NOT DRIFT, THOUGH THEY ARE TWO CARRIERS OF ONE QUANTITY
=================================================================================================
Fork 5 ruled the loop target IS fork 4's output -- it is DERIVED, not independently chosen. Storing
both is a two-carrier design and two carriers of one quantity drift; that is a measured class in
this estate, not a theoretical one. The reason to store it anyway is that a reader of ONE ROW must
be able to act without recomputing the mapping. THE GATE IS WHAT MAKES THE TWO CARRIERS ONE: a pair
that contradicts the mapping is REFUSED, so the stored value can never disagree with the derived
one. Remove this check and the field becomes a second, decaying carrier.

READS STAGED BYTES (`git show :path`), never the worktree -- the sibling to-proof-of-spec-check.sh
established that as the correct read, and a worktree read grades bytes the commit will not contain.

FAIL-CLOSED. An unreadable blob, an unparseable block, or an unexpected exception REFUSES.
A gate that fails open is not a gate.
"""
import json
import os
import re
import subprocess
import sys

CHANNEL_RE = re.compile(
    r"(^|/)org/surprise_channel/[^/]+/(INVESTIGATION|REMEDIATION)_v[^/]*\.(md|json)$")
FENCE_RE = re.compile(r"```json\s*(.*?)```", re.S)
ID_RE = re.compile(r"^[A-Z0-9_]+-(Z-)?S[0-9]+$")

# LOCKED MAPPING -- fork 4's verdict IS fork 5's loop target. See the module docstring.
ROUTE_TO_STEP = {"SPEC_ERROR": 6, "DECOMP_INVALIDATING": 5, "SCOPE_CHANGE": 2}

OVERRIDE_RE = re.compile(r"^#\s*surprise-row-override:\s*(\S.*)$", re.M)


def _repo_root():
    try:
        out = subprocess.run(["git", "rev-parse", "--show-toplevel"],
                             capture_output=True, text=True, timeout=20)
        if out.returncode == 0:
            return out.stdout.strip()
    except Exception:  # noqa: BLE001
        pass
    return os.getcwd()


def _blob(root, ref, rel):
    """Bytes of rel at ref ('' = staged index). None when the path does not exist there.

    NEVER 2>/dev/null on this read -- a mangled ref returns clean-empty and an ABSENT verdict
    would be indistinguishable from an empty file (CLAUDE.md Git).
    """
    spec = "%s:%s" % (ref, rel) if ref else ":%s" % rel
    try:
        r = subprocess.run(["git", "show", spec], cwd=root,
                           capture_output=True, text=True, timeout=60)
    except Exception:  # noqa: BLE001
        return None
    if r.returncode != 0:
        return None
    return r.stdout


def _rows(text):
    """(rows, malformed_count) over EVERY fenced json block. A malformed block is NEVER dropped."""
    rows, bad = [], 0
    if text is None:
        return rows, bad
    for m in FENCE_RE.finditer(text):
        try:
            val = json.loads(m.group(1))
        except Exception:  # noqa: BLE001
            bad += 1
            continue
        if isinstance(val, list):
            rows.extend([v for v in val if isinstance(v, dict)])
        elif isinstance(val, dict):
            rows.append(val)
    return rows, bad


def _schema(root, kind):
    name = ("investigation_item" if kind == "INVESTIGATION" else "remediation_row") + ".schema.json"
    p = os.path.join(root, "org", "surprise_channel", "schemas", name)
    with open(p, "r", encoding="utf-8") as fh:
        return json.load(fh)


def _kind(rel):
    return "REMEDIATION" if "REMEDIATION" in os.path.basename(rel).upper() else "INVESTIGATION"


def _check_row(row, kind, schema):
    """Complaints about ONE NEW row. Schema-required + closed enums + the step-7/10 fields."""
    out = []
    rid = row.get("id", "<no id>")
    props = schema.get("properties", {})

    for req in schema.get("required", []):
        if req not in row or row[req] in (None, "", [], {}):
            out.append("%s: missing required field %r" % (rid, req))

    for key, val in row.items():
        if key not in props:
            out.append("%s: field %r is not in the schema (additionalProperties is false)"
                       % (rid, key))
            continue
        enum = props[key].get("enum")
        if enum is not None and val not in enum:
            out.append("%s: %s=%r is not in the ratified enum %s" % (rid, key, val, enum))

    if kind == "INVESTIGATION":
        # STEP-7 TRIGGER, both halves. A row that cannot state both is an opinion, not a mismatch.
        for half in ("spec_asserts", "world_is"):
            v = row.get(half)
            if not isinstance(v, str) or len(v.strip()) < 8:
                out.append(
                    "%s: NEW investigation row carries no usable %r. The step-7 trigger is "
                    "\"did I have to do something the TO did not say to do, or could I not do "
                    "something the TO said to do?\" -- BOTH halves are required so the worker "
                    "judges FORM, never SIGNIFICANCE." % (rid, half))
        # ARMED obliges a named owner. The schema says so conditionally; say it at the gate too,
        # because a conditional bar inside a schema nobody runs refuses nothing.
        if row.get("hazard_standing") == "ARMED" and not str(row.get("disarm_owner", "")).strip():
            out.append("%s: hazard_standing=ARMED with no disarm_owner -- ARMED without an owner "
                       "is a hazard nobody has agreed to hold" % rid)
    else:
        route, target = row.get("route"), row.get("loop_target")
        if route is None:
            out.append("%s: NEW remediation row carries no `route`. One axis: what does the remedy "
                       "need that does not exist yet? %s" % (rid, " | ".join(ROUTE_TO_STEP)))
        if target is None:
            out.append("%s: NEW remediation row carries no `loop_target`" % rid)
        if route in ROUTE_TO_STEP and target is not None:
            want = ROUTE_TO_STEP[route]
            if target != want:
                out.append(
                    "%s: route=%s implies loop_target=%d but the row says %r. THE MAPPING IS "
                    "LOCKED -- the loop target is not an independent decision, it IS the route's "
                    "output, and this check is the only thing keeping two carriers of one quantity "
                    "from drifting." % (rid, route, want, target))
    return out


def check_file(root, rel):
    """(violations, notes) for ONE staged channel file. Validates only rows NEW in this commit."""
    kind = _kind(rel)
    staged = _blob(root, "", rel)
    if staged is None:
        return (["%s: could not read the STAGED blob -- fail-closed" % rel], [])
    head = _blob(root, "HEAD", rel)          # None = the file is new in this commit

    new_rows, bad_new = _rows(staged)
    old_rows, _ = _rows(head)
    old_ids = {r.get("id") for r in old_rows if r.get("id")}

    if bad_new:
        return (["%s: %d fenced json block(s) do NOT parse. A malformed block is never dropped and "
                 "never waved through." % (rel, bad_new)], [])

    try:
        schema = _schema(root, kind)
    except Exception as exc:  # noqa: BLE001
        return (["%s: schema unreadable (%s) -- fail-closed" % (rel, exc)], [])

    v, notes = [], []
    added = [r for r in new_rows if r.get("id") not in old_ids]
    for row in added:
        rid = row.get("id")
        if not rid or not ID_RE.match(str(rid)):
            v.append("%s: a NEW row has id=%r, which does not match the schema's id pattern "
                     "{PROJECT}-S{n} / {PROJECT}-Z-S{n}" % (rel, rid))
            continue
        v.extend(_check_row(row, kind, schema))
    notes.append("%s: %d new row(s) of %d total checked (%d pre-existing, NOT re-graded)"
                 % (rel, len(added), len(new_rows), len(old_ids)))
    return (v, notes)


def main(argv):
    root = _repo_root()
    files = [a.replace("\\", "/") for a in argv[1:] if not a.startswith("-")]
    targets = [f for f in files if CHANNEL_RE.search(f)]
    if not targets:
        print("[surprise-row-gate] OK: no surprise-channel rows in this commit "
              "(denominator: %d dispatched path(s))." % len(files))
        return 0

    all_v, all_notes = [], []
    for rel in targets:
        v, notes = check_file(root, rel)
        all_v.extend(v)
        all_notes.extend(notes)

    for n in all_notes:
        print("[surprise-row-gate] %s" % n)
    if all_v:
        print("[surprise-row-gate] BLOCKED -- %d violation(s) on NEW rows:" % len(all_v),
              file=sys.stderr)
        for x in all_v:
            print("    %s" % x, file=sys.stderr)
        print("    override (audited): put '# surprise-row-override: <reason>' in the commit "
              "message body", file=sys.stderr)
        return 1
    print("[surprise-row-gate] OK: %d file(s), all new rows carry their step-7/step-10 fields."
          % len(targets))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv))
    except Exception as exc:  # noqa: BLE001
        print("[surprise-row-gate] REFUSED: unexpected error (%s: %s). Fail-closed."
              % (type(exc).__name__, exc), file=sys.stderr)
        sys.exit(1)
