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
# /endpoint --forward Phase-0 outcome id. PERMANENT AND NEVER REUSED by contract
# (1.0.0_SA_CTO @b3584ea86a, landed in the skill AND the PRD template together).
OUTCOME_REF_RE = re.compile(r"^FWD-[0-9]+$")

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

    # ---- RC1 (CVO~A @0d272d257c P0-1): the FULL Draft-07 schema, not a top-level walk. ----
    # The manual walk above enforces required keys and top-level enums only. It cannot see a
    # nested enum (grounding.status), a pattern (surfaced_at), a minLength, or an allOf -- so
    # the protocol's central rule (GRADUATED requires GROUNDED + evidence) was bypassable while
    # the schema described it. A validator that is not installed is a REFUSAL, never a skip:
    # a gate that silently degrades to the top-level walk is the P0 wearing a green light.
    try:
        import jsonschema  # noqa: WPS433 -- local import so the module loads without it
    except ImportError:
        return out + ["%s: jsonschema is not importable in this Python -- the Draft-07 limb "
                      "cannot run, so this row is REFUSED (fail-closed). Install jsonschema; "
                      "do not bypass." % rid]
    for err in sorted(jsonschema.Draft7Validator(schema).iter_errors(row), key=lambda e: list(e.path)):
        ptr = "/" + "/".join(str(p) for p in err.path) if err.path else "/"
        out.append("%s: schema violation at %s -- %s" % (rid, ptr, err.message[:160]))

    # ---- RC1 (P0-1, identity half): project + fabric are GATE-REQUIRED on new rows and must ----
    # ---- AGREE WITH THE ID. Two carriers of one quantity, compared instead of derived.     ----
    m = ID_RE.match(str(rid))
    id_project = str(rid).rsplit("-S", 1)[0]
    if id_project.endswith("-Z"):
        id_project = id_project[:-2]
    id_fabric = "site-z" if (m and m.group(1)) else "laptop"
    for fld in ("project", "fabric"):
        if not str(row.get(fld, "")).strip():
            out.append("%s: NEW row carries no %r. Step-3 identity (project + fabric) is required on "
                       "every new row so the L8 monitor can GROUP without regexing an id -- a "
                       "consumer that must parse an id cannot reject a malformed one." % (rid, fld))
    if row.get("project") and row["project"] != id_project:
        out.append("%s: project=%r but the id says %r. The id prefix and the project field are two "
                   "carriers of one quantity; they must agree." % (rid, row["project"], id_project))
    if row.get("fabric") and row["fabric"] != id_fabric:
        out.append("%s: fabric=%r but the id %s the Z- infix, which means %r. site-z iff the id "
                   "carries Z-." % (rid, row["fabric"], "carries" if id_fabric == "site-z" else "lacks",
                                    id_fabric))

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
        # SCOPE_CHANGE is the ONE route that leaves this fabric: it re-enters at step 2, at a seat
        # that has an EXISTING PRD and needs to know WHICH named outcome the world contradicted.
        # Without this the route arrives saying only "some outcome is missing", and step 2 has to
        # re-derive from prose what the filing seat already knew.
        # THIS FIELD WAS DELIBERATELY WITHHELD UNTIL 2026-09-01. Ids only became citable when
        # 1.0.0_SA_CTO landed the permanence contract @b3584ea86a (next-unused numbers, retired
        # ones leave their number VACANT, renumbering FORBIDDEN). Before that a re-run could
        # renumber, and A DRIFTING ID TURNS A GROUNDED FINDING INTO A WRONG ONE WHILE IT STILL
        # LOOKS GROUNDED -- so citing an unstable id would have been worse than citing nothing.
        if route == "SCOPE_CHANGE":
            # RC3 (CVO~A @0d272d257c P0-4). A scope change is one of TWO kinds, and the old
            # single-field form could express only the first:
            #   CONTRADICTS_NAMED_OUTCOME  the world contradicted an outcome the PRD names
            #                              -> outcome_ref is a real FWD-<n>
            #   REQUIRES_UNNAMED_OUTCOME   the remedy needs an outcome the PRD names NOWHERE
            #                              -> outcome_ref is PRESENT WITH VALUE null, and
            #                                 proposed_outcome carries the plain-English ask
            # Required-null is the point: it distinguishes "there is deliberately no outcome to
            # cite" from "the filer forgot the field" WITHOUT minting a false id. FWD-NONE was
            # proposed and REJECTED -- an identifier must never carry the absence of the thing
            # it identifies. Before this, the uncovered-member case had no legal row and its
            # only gate-passing option was to misroute as DECOMP_INVALIDATING.
            kind_sc = row.get("scope_change_kind")
            ref = row.get("outcome_ref")
            if isinstance(ref, str) and ref.strip().upper() == "FWD-NONE":
                out.append("%s: outcome_ref='FWD-NONE' is REJECTED (CVO~A P0-4). An identifier may "
                           "not carry the absence of an outcome. Use scope_change_kind="
                           "REQUIRES_UNNAMED_OUTCOME with outcome_ref: null and a proposed_outcome."
                           % rid)
            if kind_sc not in ("CONTRADICTS_NAMED_OUTCOME", "REQUIRES_UNNAMED_OUTCOME"):
                out.append("%s: route=SCOPE_CHANGE carries no scope_change_kind. It must be "
                           "CONTRADICTS_NAMED_OUTCOME (a named FWD-<n> is wrong) or "
                           "REQUIRES_UNNAMED_OUTCOME (the PRD names no outcome this remedy serves). "
                           "Got %r." % (rid, kind_sc))
            elif kind_sc == "CONTRADICTS_NAMED_OUTCOME":
                if not isinstance(ref, str) or not OUTCOME_REF_RE.match(ref.strip()):
                    out.append("%s: CONTRADICTS_NAMED_OUTCOME must cite a real outcome_ref of the "
                               "form FWD-<n> (permanent, never reused). Got %r." % (rid, ref))
            else:  # REQUIRES_UNNAMED_OUTCOME
                if "outcome_ref" not in row or row["outcome_ref"] is not None:
                    out.append("%s: REQUIRES_UNNAMED_OUTCOME requires the outcome_ref KEY PRESENT "
                               "with value null (required-null), not %s." %
                               (rid, "absent" if "outcome_ref" not in row else repr(ref)))
                po = row.get("proposed_outcome")
                if not isinstance(po, str) or len(po.strip()) < 12:
                    out.append("%s: REQUIRES_UNNAMED_OUTCOME requires a usable proposed_outcome "
                               "(plain English, >=12 chars) -- the step-2 seat mints the FWD-<n> "
                               "from it. Got %r." % (rid, po))
    return out


def _canon_hash(row):
    """Canonical content hash of one row: key-sorted, whitespace-free JSON. Two rows with the
    same hash are byte-equivalent as DATA regardless of how the fenced block was laid out."""
    import hashlib
    blob = json.dumps(row, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(blob.encode("utf-8")).hexdigest()


def _mutation_violations(rel, head_text, staged_text):
    """RC2 (CVO~A @0d272d257c P0-2): APPEND-ONLY AS A CONTROL, NOT PROSE.

    The protocol says corrections are NEW items and an existing row is never edited in place
    (SURPRISE_CHANNEL_PROTOCOL.md:29-33). Until this function, the gate graded only ids absent
    from HEAD, so a changed or deleted EXISTING row was invisible to it -- and the watcher counts
    ids, so a same-id rewrite left the count unchanged and emitted nothing. The corpus already
    holds the failure mode: three authors wrote lifecycle prose into an existing enum field.

    A pre-existing id must be byte-equivalent as DATA, or absent from HEAD. Anything else is a
    violation carrying the old and new content hashes. The escape is the SAME audited override
    the rest of this gate uses ('# surprise-row-override: <reason>'); there is deliberately no
    second one."""
    if head_text is None:
        return []
    old_rows, _ = _rows(head_text)
    new_rows, _ = _rows(staged_text)
    old = {r["id"]: r for r in old_rows if r.get("id")}
    new = {r["id"]: r for r in new_rows if r.get("id")}
    out = []
    for oid, orow in old.items():
        if oid not in new:
            out.append("%s: EXISTING row %s was DELETED. The channel is append-only: retire it "
                       "with a new row that cites it, never by removal." % (rel, oid))
            continue
        h_old, h_new = _canon_hash(orow), _canon_hash(new[oid])
        if h_old != h_new:
            out.append("%s: EXISTING row %s was MUTATED in place (content hash %s -> %s). "
                       "Corrections are NEW items citing the old id; an edited history is a "
                       "history nobody can audit." % (rel, oid, h_old[:12], h_new[:12]))
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
    # RC2: grade what happened to the rows that ALREADY EXISTED, before grading the new ones.
    v.extend(_mutation_violations(rel, head, staged))
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
