#!/usr/bin/env python3
"""surprise-row-gate -- the L7 / L10 ROW GATE of the canonical fabric workflow (org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md; Andrew-direct 2026-09-01).

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

# TWO ROOTS (project-tree spec s.7, Andrew-ruled 2026-09-02; grammar from org/standards/PROJECT_TREE.
# contract.json: surprise_channel_glob org/missions/D*/*/*/surprise-channel/{investigations,remediations}/**).
# The flat channel org/surprise_channel/<PROJECT>/ stays; the tree adds a per-project channel whose
# PATH carries the project AND the kind. A gate reading one root is blind to the other.
FLAT_CHANNEL_RE = re.compile(
    r"(^|/)org/surprise_channel/([^/]+)/(INVESTIGATION|REMEDIATION)_v[^/]*\.(md|json)$")
TREE_CHANNEL_RE = re.compile(
    r"(^|/)org/missions/D(?:0|[1-9][0-9]?)/[^/]+/([^/]+)/surprise-channel/(investigations|remediations)/"
    r"(INVESTIGATION|REMEDIATION)_v[^/]*\.(md|json)$")
CHANNEL_RE = re.compile(FLAT_CHANNEL_RE.pattern + "|" + TREE_CHANNEL_RE.pattern)


def _folder_identity(rel):
    """(project, kind) the PATH declares, or (None, None). Flat: the <PROJECT>/ directory (kind is
    the filename's). Tree: the project folder two levels above surprise-channel/, and the kind from
    the sub-folder -- a REMEDIATION file filed under investigations/ is a path/content disagreement.
    Measured before this limb: 192 of 192 flat rows already sit in a folder named for their project."""
    rel = rel.replace("\\", "/")
    m = TREE_CHANNEL_RE.search(rel)
    if m:
        return m.group(2), m.group(3).upper().rstrip("S")
    m = FLAT_CHANNEL_RE.search(rel)
    if m:
        return m.group(2), None
    return None, None
FENCE_RE = re.compile(r"```json\s*(.*?)```", re.S)
ID_RE = re.compile(r"^[A-Z0-9_]+-(Z-)?S[0-9]+$")
# /endpoint --forward Phase-0 outcome id. PERMANENT AND NEVER REUSED by contract
# (1.0.0_SA_CTO @b3584ea86a, landed in the skill AND the PRD template together).
OUTCOME_REF_RE = re.compile(r"^FWD-[0-9]+$")

# LOCKED MAPPING -- fork 4's verdict IS fork 5's loop target. See the module docstring.
ROUTE_TO_STEP = {"SPEC_ERROR": 6, "DECOMP_INVALIDATING": 5, "SCOPE_CHANGE": 2}

OVERRIDE_RE = re.compile(r"^#\s*surprise-row-override:\s*(\S.*)$", re.M)

# GATE (iii) -- Andrew-direct 2026-09-03 (state of record @716a9bc7ce call 3, LD-0521; transcript: "no
# LIM-10 routing until all task orders are complete ... We do not route until the job is over"). A NEW
# remediation row carrying a `route` under a TREE project is REFUSED while any task order of that project,
# on EITHER root, is not terminal at HEAD. Tree projects only; NEW rows only (this gate's standing model);
# the census reads HEAD blobs, never the worktree -- a peer's half-written status flip must not decide a
# refusal. THE OTHER HALF of his precondition ("the surprise channel, all investigations, completely checked
# by CVO") has no artifact a gate can read today beyond the rows' own disposition field and is NOT enforced
# here -- stated so this limb's OK line is never read as covering it. Terminal words are the TO protocol's
# (complete / superseded / cancelled) plus the withdrawn state an issuer writes on a mis-seated dispatch.
TO_STATUS_RE = re.compile(r"<status>\s*([A-Za-z_-]+)", re.I)
TERMINAL_TO_WORDS = ("complete", "completed", "closed", "done", "superseded", "cancelled", "canceled", "withdrawn")


def _open_tos_for_project(root, code):
    """(open_ids, total, note): the project's task orders on BOTH roots (tracked at HEAD) whose <status>
    is not terminal. open_ids is None when the census could not run -- the caller fails closed."""
    try:
        ls = subprocess.run(["git", "ls-files", "--", "*/task_orders/%s.*.md" % code,
                             "org/missions/D*/*/%s/task-orders/*.md" % code],
                            cwd=root, capture_output=True, text=True, timeout=60)
    except Exception as exc:  # noqa: BLE001
        return None, 0, "git ls-files raised %s" % exc
    if ls.returncode != 0:
        return None, 0, "git ls-files rc=%d: %s" % (ls.returncode, ls.stderr.strip()[:120])
    paths = [p.strip().replace("\\", "/") for p in ls.stdout.splitlines() if p.strip()]
    open_ids = []
    for p in paths:
        st, text = _blob(root, "HEAD", p)
        if st != "OK":
            return None, len(paths), "%s unreadable at HEAD (%s)" % (p, st)
        m = TO_STATUS_RE.search(text)
        word = m.group(1).lower() if m else "<no status tag>"
        if word not in TERMINAL_TO_WORDS:
            open_ids.append("%s [%s]" % (os.path.basename(p), word))
    return open_ids, len(paths), ""


def _route_precondition_violations(root, rel, row, code, open_tos=None):
    """GATE (iii) for ONE new tree remediation row carrying a route. `open_tos` is injectable for the
    red-first exercise; production passes None and the census runs."""
    rid = row.get("id", "<no id>")
    if open_tos is None:
        open_ids, total, note = _open_tos_for_project(root, code)
    else:
        open_ids, total, note = open_tos
    if open_ids is None:
        return ["%s: the L10 precondition (every task order under %s terminal) could NOT be evaluated (%s) "
                "-- REFUSED, fail-closed" % (rid, code, note)]
    if open_ids:
        return ["%s: NEW remediation row carries route=%s while %d of %d task order(s) under %s are NOT "
                "terminal at HEAD: %s. L10 routing waits until every task order is complete "
                "(Andrew-direct 2026-09-03, @716a9bc7ce call 3, LD-0521: 'We do not route until the job "
                "is over')." % (rid, row.get("route"), len(open_ids), total, code, ", ".join(open_ids))]
    return []


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
    """(status, text) of rel at ref ('' = staged index). status is one of:
         OK      -- text is the content
         ABSENT  -- the path does not exist at that ref (a NEW file, or not staged)
         ERROR   -- git could not answer (bad ref, timeout, crash). NOT the same as absent.

    RC2 second pass (CVO~A re-grade @0dbf12ebb3): the old single-None return made "the file is
    new in this commit" and "git failed to read HEAD" indistinguishable, so a read failure on
    HEAD silently SKIPPED the mutation check and graded the file as brand new. Absence is tested
    FIRST with `git cat-file -e` (rc 1 = not there, rc 0 = there, anything else = error), and
    only a confirmed-present path is read. NEVER 2>/dev/null on either call -- a mangled ref
    returns clean-empty and an ABSENT verdict would be indistinguishable from an empty file.
    """
    spec = "%s:%s" % (ref, rel) if ref else ":%s" % rel
    # PRESENCE PROBE. `git cat-file -e ref:path` was tried first and is WRONG for this: it exits 128
    # for a missing PATH as well as for a bad REF, so absence and failure were still one state
    # (caught by the harness's own blob control on first green run). `ls-tree <ref> -- <path>` and
    # `ls-files -s -- <path>` (index) exit 0 with EMPTY output for a missing path and non-zero
    # only when git itself cannot answer -- which is exactly the two-state distinction needed.
    # cwd=root because ls-tree is CWD-prefix-sensitive and returns a silent zero from a subdir.
    probe_cmd = (["git", "ls-tree", ref, "--", rel] if ref
                 else ["git", "ls-files", "-s", "--", rel])
    try:
        probe = subprocess.run(probe_cmd, cwd=root, capture_output=True, text=True, timeout=60)
    except Exception as exc:  # noqa: BLE001
        return ("ERROR", "%s raised %s" % (probe_cmd[1], exc))
    if probe.returncode != 0:
        return ("ERROR", "%s rc=%d: %s" % (probe_cmd[1], probe.returncode, probe.stderr.strip()[:160]))
    if not probe.stdout.strip():
        return ("ABSENT", None)
    try:
        r = subprocess.run(["git", "show", spec], cwd=root,
                           capture_output=True, text=True, timeout=60)
    except Exception as exc:  # noqa: BLE001
        return ("ERROR", "show raised %s" % exc)
    if r.returncode != 0:
        return ("ERROR", "show rc=%d: %s" % (r.returncode, r.stderr.strip()[:160]))
    return ("OK", r.stdout)


def _collect(val, rows):
    """Append the object rows in a parsed JSON value; return the count of NON-object items.

    RC1 second pass (CVO~A re-grade @0dbf12ebb3): the old loop kept dicts and SILENTLY DROPPED
    everything else -- a fenced scalar, a list of strings, a list with one bad element -- so a
    malformed row could never be counted as malformed. Every non-object item is a defect."""
    if isinstance(val, dict):
        rows.append(val)
        return 0
    if isinstance(val, list):
        bad = 0
        for item in val:
            if isinstance(item, dict):
                rows.append(item)
            else:
                bad += 1
        return bad
    return 1


def _rows(text, raw_json=False):
    """(rows, malformed_count). A malformed block or item is NEVER dropped.

    raw_json=True: the whole body IS the JSON document (a .json channel file). CHANNEL_RE has
    accepted .json since it was written, but this parser read only fenced Markdown -- so an
    invalid .json file matched as a target, yielded 0 rows and 0 violations, and passed
    (CVO~A re-grade @0dbf12ebb3, RC1 hole 1). A raw file that does not parse is one malformed
    block; a raw file holding anything but an object or a list of objects is malformed per item."""
    rows, bad = [], 0
    if text is None:
        return rows, bad
    if raw_json:
        try:
            val = json.loads(text)
        except Exception:  # noqa: BLE001
            return rows, 1
        return rows, _collect(val, rows)
    for m in FENCE_RE.finditer(text):
        try:
            val = json.loads(m.group(1))
        except Exception:  # noqa: BLE001
            bad += 1
            continue
        bad += _collect(val, rows)
    return rows, bad


def _schema(root, kind):
    """The schema AS IT WILL BE COMMITTED -- read from the staged index, never the worktree.

    RC1 second pass (CVO~A re-grade @0dbf12ebb3, hole 3): reading the worktree let a commit stage
    a LOOSENED schema together with rows that only pass under it, while the gate graded against
    whatever happened to be on disk. The index is what the commit contains. Unreadable = REFUSE."""
    name = ("investigation_item" if kind == "INVESTIGATION" else "remediation_row") + ".schema.json"
    rel = "org/surprise_channel/schemas/" + name
    status, text = _blob(root, "", rel)
    if status != "OK":
        raise RuntimeError("schema %s not readable from the staged index (%s: %s)"
                           % (rel, status, text))
    return json.loads(text)


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
    raw = rel.lower().endswith(".json")
    old_rows, _ = _rows(head_text, raw) if head_text is not None else ([], 0)
    new_rows, _ = _rows(staged_text, raw)
    old = {r["id"]: r for r in old_rows if r.get("id")}
    # RC2 second pass (CVO~A re-grade @0dbf12ebb3, hole 4 -- DICT COLLAPSE): the old code built
    # {id: row} over the staged rows, so a CONTRADICTORY duplicate of an existing id followed by
    # the unchanged original collapsed to the original, hashed equal, and passed. Every occurrence
    # of an id is kept and every one is compared.
    new_all = {}
    for r in new_rows:
        if r.get("id"):
            new_all.setdefault(r["id"], []).append(r)
    out = []
    for nid, occurrences in new_all.items():
        if len(occurrences) > 1:
            out.append("%s: id %s occurs %d times in the staged file. An id is one row; a second "
                       "occurrence is either a contradictory rewrite hiding behind the original or a "
                       "paste error, and both are refused." % (rel, nid, len(occurrences)))
    if head_text is None:
        return out
    for oid, orow in old.items():
        if oid not in new_all:
            out.append("%s: EXISTING row %s was DELETED. The channel is append-only: retire it "
                       "with a new row that cites it, never by removal." % (rel, oid))
            continue
        h_old = _canon_hash(orow)
        for nrow in new_all[oid]:
            h_new = _canon_hash(nrow)
            if h_old != h_new:
                out.append("%s: EXISTING row %s was MUTATED in place (content hash %s -> %s). "
                           "Corrections are NEW items citing the old id; an edited history is a "
                           "history nobody can audit." % (rel, oid, h_old[:12], h_new[:12]))
    return out


def check_file(root, rel):
    """(violations, notes) for ONE staged channel file. Validates only rows NEW in this commit."""
    kind = _kind(rel)
    raw = rel.lower().endswith(".json")
    s_status, staged = _blob(root, "", rel)
    if s_status != "OK":
        return (["%s: could not read the STAGED blob (%s: %s) -- fail-closed" % (rel, s_status, staged)], [])
    h_status, head = _blob(root, "HEAD", rel)
    if h_status == "ERROR":
        # RC2 second pass (hole 5): a HEAD read FAILURE is not "the file is new". Grading a file as
        # new because git could not answer would skip the mutation check on exactly the commit
        # where something is wrong with the ref.
        return (["%s: could not read the HEAD blob (%s) -- REFUSED rather than graded as a new "
                 "file. Absence and failure are different states." % (rel, head)], [])
    # h_status == ABSENT -> head is None -> the file is genuinely new in this commit.

    new_rows, bad_new = _rows(staged, raw)
    old_rows, _ = _rows(head, raw)
    old_ids = {r.get("id") for r in old_rows if r.get("id")}

    if bad_new:
        return (["%s: %d %s do NOT parse as object rows. A malformed block or item is never dropped "
                 "and never waved through." % (rel, bad_new, "raw json document(s)/item(s)" if raw
                                                 else "fenced json block(s)/item(s)")], [])
    if not new_rows:
        # A channel file mints ON AN ITEM, never empty (SURPRISE_CHANNEL_PROTOCOL). Zero rows from a
        # target file is either an empty mint or a parser that could not see the rows (RC1 hole 1:
        # a raw .json that did not parse used to land here with 0 rows and 0 violations).
        return (["%s: target file yields ZERO rows. A channel file mints on an item; zero is an empty "
                 "mint or an unparsed body, and both are refused." % rel], [])

    try:
        schema = _schema(root, kind)
    except Exception as exc:  # noqa: BLE001
        return (["%s: schema unreadable (%s) -- fail-closed" % (rel, exc)], [])

    v, notes = [], []
    # THE PATH IS THE MEMBERSHIP (tree spec s.1/s.2 choice A): the folder's project and, in the tree,
    # the sub-folder's kind are carriers the row must agree with. Graded on NEW rows only, like the rest.
    folder_project, folder_kind = _folder_identity(rel)
    if folder_kind and folder_kind != kind:
        v.append("%s: a %s file filed under the %s/ sub-folder -- the path says one kind, the filename "
                 "says another" % (rel, kind, "investigations" if folder_kind == "INVESTIGATION" else "remediations"))
    # RC2: grade what happened to the rows that ALREADY EXISTED, before grading the new ones.
    v.extend(_mutation_violations(rel, head, staged))
    added = [r for r in new_rows if r.get("id") not in old_ids]
    for row in added:
        rid = row.get("id")
        if not rid or not ID_RE.match(str(rid)):
            v.append("%s: a NEW row has id=%r, which does not match the schema's id pattern "
                     "{PROJECT}-S{n} / {PROJECT}-Z-S{n}" % (rel, rid))
            continue
        if folder_project and row.get("project") and row["project"] != folder_project:
            v.append("%s: NEW row %s says project=%r but the file sits in %r's folder. The path is the "
                     "membership; a row filed under another project is an identity defect."
                     % (rel, rid, row["project"], folder_project))
        v.extend(_check_row(row, kind, schema))
        # GATE (iii): a NEW tree remediation row with a route waits for every TO under the project.
        if kind == "REMEDIATION" and folder_kind == "REMEDIATION" and folder_project and row.get("route") is not None:
            pre = _route_precondition_violations(root, rel, row, folder_project)
            v.extend(pre)
            if not pre:
                _o, _t, _n = _open_tos_for_project(root, folder_project)
                notes.append("%s: L10 precondition for %s -- %d task order(s) at HEAD on both roots, 0 open; "
                             "route admitted" % (rel, rid, _t))
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

    # RC4 (CVO~A re-grade @0dbf12ebb3 + RC4 re-grade): the STANDING corpus pass runs INSIDE this gate
    # on every channel commit -- one gate, one more limb, never a second gate. It grades the whole
    # corpus against the exact-tuple baseline; the per-row checks above grade what THIS commit adds
    # or mutates. A corpus pass that cannot run is a refusal, not a skip.
    try:
        import importlib.util as _ilu
        _spec = _ilu.spec_from_file_location(
            "surprise_corpus_validate", os.path.join(root, ".tools", "surprise-corpus-validate.py"))
        _scv = _ilu.module_from_spec(_spec)
        _spec.loader.exec_module(_scv)
        if _scv.main([]) != 0:
            all_v.append("standing corpus pass REFUSED -- see the [surprise-corpus] lines above")
    except SystemExit as exc:
        if exc.code not in (0, None):
            all_v.append("standing corpus pass exited %r -- fail-closed" % exc.code)
    except Exception as exc:  # noqa: BLE001
        all_v.append("standing corpus pass could not run (%s: %s) -- fail-closed"
                     % (type(exc).__name__, exc))

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
