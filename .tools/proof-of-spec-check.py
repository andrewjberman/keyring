#!/usr/bin/env python3
"""proof-of-spec-check -- validate a PROOF_OF_SPEC instance against the canonical schema.

Andrew-direct 2026-08-11 ~0815Z: build TOs carry machine-readable JSON deliverable
expectations the Tier-2 assignee fills to PROVE work was done to spec. This is the
mechanical gate: a TO is not complete until its instance passes here.

Usage: proof-of-spec-check <instance.json> [expected_criterion_ids]
  expected_criterion_ids: comma-separated list OR a path to a file (one id per line) --
  the TO's embedded criterion set. When given, COVERAGE is checked BEFORE quality:
  an instance valid on every row it carries can still silently OMIT a criterion
  (the row-quality/row-coverage split -- CVO's step-zero, mechanized). Missing or
  extra criteria are violations, with both denominators printed.
Exit 0 = VALID. Exit 1 = INVALID (every violation printed). Exit 2 = usage/read error.

Layered: jsonschema (if installed) for structure, then the conditional rules the
schema cannot express -- ALWAYS run, so absence of the jsonschema package degrades
coverage LOUDLY rather than silently passing (the import-guard-answers-completion
-not-presence class).

PIPELINE GATE LAYER 1 (2026-08-24, 0.8.0_AE_CloudComp~F): every run also resolves the
GOVERNING TO and checks decomp_ref + the bidirectional cell<->criterion alignment, with
a denominator printed for each direction. ENFORCE vs ANNOUNCE is derived from that TO --
a TO carrying <decomp_ref> obliges its instance to carry decomp_ref and to close the
join; a TO without one is pre-pipeline work and stays VALID. The alignment frames print
whether or not anything failed. See org/ref/DIRECTIVE_EXECUTION_PIPELINE.md:170.
decomp_ref.vintage_commit is also checked to RESOLVE to a real commit (CVO 66693,
routed CTO 66702); CONTAINMENT of the doc at that vintage is a declared NON-GOAL.
The BACKWARD direction enforces only against a DELIMITED <owned_cells> clause inside
<decomp_ref> (CTO 66893): an undelimited element cannot distinguish an owned cell from
one merely READ or explicitly EXCLUDED, so it ANNOUNCES rather than asserting.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

SCHEMA_PATH = Path(__file__).resolve().parent.parent / "org" / "standards" / "PROOF_OF_SPEC.schema.json"

# A TO may name the cell-bearing run artifact explicitly.  The legacy form predates the
# tag and discovers DECOMP.md in prose, so keep it as a compatibility path -- but never
# let punctuation become part of the path (R4-DT-6: ``\S+`` swallowed an opening paren).
DECOMP_DOC_TAG_RE = re.compile(r"<decomp_doc>\s*([^<]+?)\s*</decomp_doc>", re.S)
DECOMP_DOC_VALUE_RE = re.compile(r"[\w./~-]+")
LEGACY_DECOMP_DOC_RE = re.compile(r"([\w./~-]+DECOMP\.md)")


def conditional_checks(inst: dict) -> list[str]:
    """The rules draft-07 can't carry. Each violation is one printed line."""
    v: list[str] = []
    for i, row in enumerate(inst.get("acceptance", [])):
        rid = row.get("criterion_id", f"row-{i}")
        if row.get("status") != "PASS" and not row.get("status_reason"):
            v.append(f"acceptance[{rid}]: status={row.get('status')} REQUIRES status_reason")
        if row.get("status") == "PASS" and len(row.get("output_evidence", "").strip()) < 8:
            v.append(f"acceptance[{rid}]: PASS with thin/empty output_evidence -- a bare value; INVALID")
    m = inst.get("controls", {}).get("mutant", {})
    if m.get("status") == "DID-NOT-FIRE (deliverable INVALID)":
        v.append("controls.mutant: DID-NOT-FIRE -- the deliverable is INVALID by its own control")
    d = inst.get("controls", {}).get("determinism", {})
    if d.get("status") == "UNSTABLE (deliverable INVALID)":
        v.append("controls.determinism: UNSTABLE -- the deliverable is INVALID by its own control")
    if d.get("status") == "N/A-WITH-REASON" and len(d.get("method", "").strip()) < 8:
        v.append("controls.determinism: N/A-WITH-REASON requires the reason in method")
    # PER-ARTIFACT ACCEPTANCE COVERAGE (CVO gate candidate 2026-08-11: A_03 shipped with ZERO
    # battery rows, caught by eyeball twice independently -- luck-per-firm, now machinery).
    # Heuristic linkage via the criterion-id grammar ({firm}-{group}-{artifact}-{check}): an
    # artifact's stem token must appear in >=1 criterion_id, OR the artifact is named in
    # declared_exclusions. Matching is printed, never silent.
    import re as _re
    ids_blob = " ".join(r.get("criterion_id", "") for r in inst.get("acceptance", [])).upper()
    # (excl_blob removed 2026-08-19: the blob substring match it fed was the SILENT FALSE
    #  PASS -- any incidental mention of an artifact stem anywhere in any exclusion text
    #  satisfied coverage. Exclusions are now matched precisely, on their own `item`.)
    for a in inst.get("artifacts_produced", []):
        # SCOPE IS BACKEND-DS-ID-GRAMMAR-SPECIFIC BY DESIGN: this stem-token heuristic keys on the
        # {firm}-{group}-{artifact}-{check} criterion-id grammar, which is a DS/gold convention. A
        # frontend_component (portal) does not use it -- it is INTENTIONALLY outside this heuristic
        # (COO 215014Z: a portal component was forced to mis-declare 'script' and fail here; the fix
        # was the kind enum, now carrying frontend_component). A frontend-appropriate coverage rule
        # is a follow-on gate candidate; skipping frontend_component here is correct, not a gap.
        if a.get("kind") not in ("script", "s3_object"):
            continue
        path = a.get("path_or_key", "")
        stem = Path(path).name.split(".")[0]
        tokens = {t.upper().replace("_", "") for t in _re.findall(r"[A-Za-z]+_?\d+|[A-Za-z]{3,}", stem)}
        if not tokens:
            continue
        # (1) NAMING, the original DS `{firm}-{group}-{artifact}-{check}` grammar. KEPT so every
        #     instance that passes today still passes -- this fix must not read as "the rule was
        #     disabled".
        if any(t in ids_blob.replace("-", "").replace("_", "") for t in tokens if len(t) >= 3):
            continue
        # (2) COVERAGE, which is what the rule was always FOR. An acceptance row that INVOKES the
        #     artifact, or whose verbatim output names it, is direct evidence the artifact was
        #     exercised -- strictly better evidence than its name appearing in an id.
        #     WHY THIS IS NOT A LOOSENING: the previous rule tested NAMING and called it coverage,
        #     so any TO whose issuer minted ids in another grammar (WP1-N, D1b-N, D3.1-N) FAILED no
        #     matter how complete the work was, and the only route to green was declaring the
        #     central deliverable "excluded" -- a FALSE STATEMENT. A rule whose sole escape is a lie
        #     is not enforcing anything; it is teaching the record to be wrong. (DS base declined
        #     that escape twice on 2026-08-19 and characterised the gap instead, at their own cost.)
        rows_blob = " ".join(
            f"{r.get('invocation', '')} {r.get('output_evidence', '')}"
            for r in inst.get("acceptance", [])).lower()
        if path.lower() in rows_blob or (len(stem) >= 4 and stem.lower() in rows_blob):
            continue
        # (3) EXPLICIT declaration, per COO + DS base's recommendation: the assignee names the rows
        #     that cover this artifact. Makes the link stateable when neither heuristic can see it.
        covered_by = a.get("artifact_covered_by")
        if covered_by:
            named = {str(c).strip().upper() for c in (
                covered_by if isinstance(covered_by, list) else [covered_by])}
            known = {str(r.get("criterion_id", "")).strip().upper()
                     for r in inst.get("acceptance", [])}
            unknown = named - known
            if unknown:
                v.append(f"artifact-coverage: '{path}' artifact_covered_by names criterion id(s) "
                         f"{sorted(unknown)} that do not exist in this instance -- a citation to a "
                         f"row that is not there is worse than no citation")
            continue
        # (4) EXCLUSION -- now PRECISE. This previously substring-matched the stem against a blob
        #     of ALL declared_exclusions text, so ANY incidental mention anywhere silently
        #     satisfied coverage. MEASURED 2026-08-19 on this seat's own ACCEPTED TO-1 instance:
        #     `broker.py` passed because an exclusion about the site-Z FABRIC LEG happens to
        #     contain the word "broker", and `server.py` passed because an exclusion about
        #     _ensure_commit_worker cites "server.py:~592". NEITHER declared either artifact
        #     excluded. That is a SILENT FALSE PASS of the very A_03 zero-battery class this rule
        #     exists to catch -- the opposite and more dangerous failure from the reported one,
        #     because a false FAIL is loud and argued with while a false PASS is believed.
        #     The exclusion must now name the artifact in its OWN `item` field.
        if any(stem.lower() in str(e.get("item", "")).lower() or
               path.lower() in str(e.get("item", "")).lower()
               for e in inst.get("declared_exclusions", []) if isinstance(e, dict)):
            continue
        v.append(f"artifact-coverage: '{path}' has NO acceptance row referencing it "
                 f"(tokens tried: {sorted(tokens)}; searched criterion ids, row invocations and "
                 f"output_evidence, artifact_covered_by, and exclusion ITEMS) -- "
                 f"the A_03 zero-battery class; add rows, set artifact_covered_by, or declare "
                 f"the exclusion by naming this artifact in the exclusion's item")
    return v


def coverage_check(inst: dict, expected_arg: str) -> list[str]:
    """CVO step-zero mechanized: instance criterion set vs the TO's expected set."""
    p = Path(expected_arg)
    raw = p.read_text(encoding="utf-8").splitlines() if p.is_file() else expected_arg.split(",")
    expected = {s.strip() for s in raw if s.strip()}
    carried = {r.get("criterion_id", "") for r in inst.get("acceptance", [])}
    v = [f"coverage: criterion '{c}' in the TO's expected set has NO instance row (silent omission)"
         for c in sorted(expected - carried)]
    v += [f"coverage: instance row '{c}' is NOT in the TO's expected set (unexpected addition -- state it or fix the TO)"
          for c in sorted(carried - expected)]
    v.insert(0, f"coverage-frame: expected={len(expected)} carried={len(carried)} matched={len(expected & carried)}") if v else None
    return v


# ---------------------------------------------------------------------------
# PIPELINE GATE LAYER 1 -- decomp_ref + bidirectional cell<->criterion alignment.
# org/ref/DIRECTIVE_EXECUTION_PIPELINE.md:170 ("build routed", tooling lane;
# Andrew's word granted in the ratification). Built by 0.8.0_AE_CloudComp~F.
#
# THE ENFORCE DISCRIMINATOR IS THE GOVERNING TO -- NEVER A DATE, NEVER AN OPERATOR
# MARKER (CTO ruling 66492, 2026-08-24). If the TO governing this instance carries a
# <decomp_ref>, the instance MUST carry decomp_ref and the join must close -> ENFORCE.
# If the TO carries none, this is PRE-PIPELINE work completing under its own spec ->
# ANNOUNCE, and it stays VALID. A date- or marker-based ramp would retroactively
# invalidate the five in-flight instances measured 2026-08-24 (ETFS TO-1/2/3,
# D1 TO-D1b, D3 TO-D3.1); deriving the switch from the artifact itself cannot, and
# every TO cut from the ratification forward is enforced BY CONSTRUCTION because its
# issuer writes <decomp_ref> on its face.
#
# NOTHING HERE IS DERIVED. cell_refs are read as DECLARED in the TO's issuance half.
# A retrofitted derivation makes alignment LOOK satisfied while being FALSE -- the
# same class as the pre-2026-08-19 exclusion-blob substring match at :104.
WORKSPACE = Path(__file__).resolve().parent.parent
# Set by alignment_check(): True when the backward limb was ASSERTED on a delimited <owned_cells>
# set, False when it could only ANNOUNCE (undelimited), None when alignment was not evaluated.
# main() reads it to qualify the verdict line (DT~X 79061).
_BACKWARD_ASSERTED = None

# Cell-id grammar, validated against BOTH live decomps before encoding (2026-08-24):
# etfs-positioning/20260821T194927Z -> 23 ids; d1-catviews/20260824T195537Z -> 28 ids,
# which reproduces that decomp's OWN declared arithmetic ("Total: 28 cells"). Covers
# ETFS-a-1 (prefix-group-index) and D1-inv-1 / D1-h-r1 (multi-letter group, lettered
# index) alike.
# PLUS the word-suffixed MECHANISM form (W4-m-joinable, L1-m-graindecl): wave 4 named its
# mechanism cells after their SUBJECT, and the digits-only final segment encoded wave 3's
# grammar as if it were the general one -- 5 real ids invisible, and the violations they
# produced were worded AGAINST THE ISSUER (75278). The word branch is deliberately narrow:
# it admits a word final segment ONLY on the '-m-' mechanism group, so prose tokens like
# D11-era-things stay unmatched.
CELL_ID_RE = re.compile(r"\b[A-Z][A-Z0-9]*-(?:m-[a-z0-9_]+|[a-z]{1,4}-[a-z]?\d+)\b")
OWNED_CELLS_RE = re.compile(r"<owned_cells>(.*?)</owned_cells>", re.S)
CRITERION_TAG_RE = re.compile(r"<criterion\b([^>]*?)/?>")
ATTR_RE = re.compile(r'(\w+)\s*=\s*"([^"]*)"')


_TRACKED_TOS = None


def _tracked_task_orders() -> set:
    """Repo-relative paths of TRACKED task-order files, posix-normalised.

    COO 67721 / 67951: a corpus read from the shared WORKING TREE lets a peer's half-written
    file change this gate's verdict, and nothing in the verdict records which state it was
    built against. ~190 dirty paths live here; uncommitted work is visible to peer instruments
    the moment it hits disk, and the remedy is on the READER.

    FAIL-CLOSED-TO-EMPTY IS DELIBERATE: if `git ls-files` cannot run, this returns an EMPTY
    set, which makes the corpus empty and the gate ANNOUNCE rather than refuse. A gate that
    cannot establish committed state must not refuse anyone's commit on a corpus it could not
    read -- and callers print the corpus denominator, so an empty one is visible, not silent.
    """
    global _TRACKED_TOS
    if _TRACKED_TOS is None:
        try:
            out = subprocess.run(
                ["git", "ls-files", "--", "*/task_orders/*.md"],
                cwd=WORKSPACE, capture_output=True, text=True, check=True).stdout
            _TRACKED_TOS = {ln.strip().replace("\\", "/") for ln in out.splitlines() if ln.strip()}
        except Exception:  # noqa: BLE001
            _TRACKED_TOS = set()
    return _TRACKED_TOS


def _is_tracked(rel: str) -> bool:
    # Ask git about THE FILE, never about corpus membership. The corpus glob is scoped to
    # */task_orders/*.md for DISCOVERY; a declared to_ref may legitimately live elsewhere
    # (wave-4 TOs live in deliverables/D11_W4/), and glob membership answered "is this in my
    # directory shape", not "is this committed" -- a discriminator on the DIRECTORY that
    # falsely reported 3 of 3 committed wave-4 TOs UNTRACKED and silently disabled alignment
    # for the wave (75078). Fail-closed-to-False keeps the documented announce behavior.
    try:
        rc = subprocess.run(
            ["git", "ls-files", "--error-unmatch", "--", rel.replace("\\", "/")],
            cwd=WORKSPACE, capture_output=True, text=True).returncode
        return rc == 0
    except Exception:  # noqa: BLE001
        return False


def _canonical_to_id(raw: str) -> str:
    """The bare TO id. to_id fields carry trailing issuer/amendment prose in practice
    ('ETFS_POSITIONING.TO-2 (issuer ... @10f94e4f13; Amendment C ...)'), so the id is
    the leading whitespace-delimited token."""
    return raw.strip().split()[0].rstrip(".,;:") if raw.strip() else ""


def _project_code(raw_to_id: str) -> str:
    return _canonical_to_id(raw_to_id).split(".", 1)[0].upper()


def _dep_stage(code: str) -> str | None:
    """Pipeline registration = a dep_stage key in the project JSON (enforcement layer 3,
    landed @c4d8c0025d). Printed as FRAME; the enforce decision belongs to the TO."""
    f = WORKSPACE / "org" / "projects" / f"{code}.json"
    if not f.is_file():
        return None
    try:
        return json.loads(f.read_text(encoding="utf-8")).get("dep_stage")
    except Exception:  # noqa: BLE001
        return None


def _resolve_governing_to(inst: dict) -> tuple[Path | None, str, int]:
    """(path, note, scanned). Resolution is CONTENT-based: a TO is the file that
    DECLARES id="<canonical>", never the file whose NAME looks right (Rule 22a -- a
    filename-resolved check reports drift where there is none and reads CLEAN where two
    copies have silently diverged). An explicit decomp_ref.to_ref wins when present."""
    _dref = inst.get("decomp_ref", {})
    if not isinstance(_dref, dict):
        # SHAPE ERROR, NOT A VERDICT. decomp_ref must be the OBJECT form
        # ({doc, vintage_commit, to_ref}). A bare string used to reach .get() and raise
        # AttributeError, which exited rc=1 -- BYTE-IDENTICAL to a legitimate INVALID.
        # Surfaced by 0.6.0_AE_PartnerETL (71621), reproduced on a committed peer instance.
        raise TypeError(
            f"decomp_ref must be an OBJECT (doc/vintage_commit/to_ref), got {type(_dref).__name__}"
        )
    declared = str(_dref.get("to_ref", "")).strip()
    if declared:
        p = Path(declared)
        if not p.is_absolute():
            p = WORKSPACE / declared
        if p.is_file():
            rel = declared.replace("\\", "/")
            if not _is_tracked(rel):
                # EXISTS but UNCOMMITTED. Not a false citation -- an unstable one. Enforcing
                # alignment against a half-written TO is the hazard itself, so this announces
                # rather than either refusing or silently enforcing.
                return None, (f"decomp_ref.to_ref '{declared}' resolves to an UNTRACKED file "
                              f"-- committed state is required to enforce against it"), 0
            return p, "declared via decomp_ref.to_ref", 0
        return None, f"decomp_ref.to_ref '{declared}' does not resolve to a file", 0
    cid = _canonical_to_id(str(inst.get("to_id", "")))
    if not cid:
        return None, "instance carries no parseable to_id", 0
    needle = 'id="' + cid + '"'
    tracked = _tracked_task_orders()
    hits, scanned = [], 0
    for f in (WORKSPACE / "org").rglob("task_orders/*.md"):
        rel = str(f.relative_to(WORKSPACE)).replace("\\", "/")
        if rel not in tracked:
            continue          # never ADOPT a peer's in-flight TO as governing authority
        scanned += 1
        try:
            if needle in f.read_text(encoding="utf-8", errors="replace")[:8000]:
                hits.append(f)
        except Exception:  # noqa: BLE001
            continue
    if not hits:
        return None, "no TO declares " + needle, scanned
    if len(hits) > 1:
        rel = sorted(str(h.relative_to(WORKSPACE)) for h in hits)
        return None, f"AMBIGUOUS -- {len(hits)} TOs declare {needle}: {rel}", scanned
    return hits[0], "resolved by declared " + needle, scanned


def _parse_to(text: str) -> dict:
    """The TO's ISSUANCE half, read exactly as declared."""
    m = re.search(r"<decomp_ref>(.*?)</decomp_ref>", text, re.S)
    blob = m.group(1) if m else None
    doc = ""
    if blob:
        explicit = DECOMP_DOC_TAG_RE.search(blob)
        if explicit:
            candidate = explicit.group(1).strip()
            # Explicit but malformed is a broken declaration, never a reason to fall
            # back to some other path mentioned in prose inside the same element.
            doc = candidate if DECOMP_DOC_VALUE_RE.fullmatch(candidate) else ""
        else:
            d = LEGACY_DECOMP_DOC_RE.search(blob)
            doc = d.group(1) if d else ""
    # THE DELIMITED OWNED-CELLS CLAUSE (CTO 66893). WHY IT EXISTS: the wide harvest read
    # EVERY cell id in the whole <decomp_ref> element as a cell the TO CLAIMS, so a
    # READ-DEPENDENCY became an unclaimed claim and -- the inversion AE~G named -- an
    # EXPLICIT EXCLUSION CLAUSE ("NOT in this TO: ...") was reported as a claim the TO
    # failed to discharge. A seat reading that violation without opening the TO would
    # conclude the exact OPPOSITE of what the TO says.
    owned = OWNED_CELLS_RE.search(blob) if blob else None
    owned_raw = owned.group(1) if owned else ""
    delimited = owned is not None
    if delimited:
        declared = sorted(set(CELL_ID_RE.findall(owned_raw)))
        # "ids only, no prose inside the delimiter" is CTO's constraint (a) -- made
        # MECHANICAL rather than aspirational: strip the ids and the separators, and
        # anything with word characters left over is prose that crept back in.
        residue = CELL_ID_RE.sub("", owned_raw)
        stray = re.sub(r"[\s,;]+", "", residue)
    else:
        declared = sorted(set(CELL_ID_RE.findall(blob))) if blob else []
        stray = ""
    crits: dict[str, list[str]] = {}
    no_refs: list[str] = []
    for tag in CRITERION_TAG_RE.finditer(text):
        attrs = dict(ATTR_RE.findall(tag.group(1)))
        cid = attrs.get("id", "").strip()
        if not cid:
            continue
        refs = [c.strip() for c in attrs.get("cell_refs", "").split(",") if c.strip()]
        crits[cid] = refs
        if not refs:
            no_refs.append(cid)
    exp = re.search(r"<expected_criteria>(.*?)</expected_criteria>", text, re.S)
    return {
        "has_decomp_ref": blob is not None,
        "declared_cells": declared,
        "delimited": delimited,
        "delimiter_stray_text": stray,
        "decomp_doc": doc,
        "criteria": crits,
        "criteria_without_cell_refs": no_refs,
        "expected_criteria": (
            [c.strip() for c in exp.group(1).split(",") if c.strip()] if exp else []),
    }


def _decomp_cell_ids(rel_or_abs: str) -> tuple[set, str]:
    """(ids, error). The id space the decomp actually declares."""
    if not rel_or_abs:
        return set(), "no valid decomp artifact path found in the TO's <decomp_ref>"
    p = Path(rel_or_abs)
    if not p.is_absolute():
        p = WORKSPACE / rel_or_abs
    if not p.is_file():
        return set(), f"decomp artifact '{rel_or_abs}' does not resolve to a file"
    try:
        return set(CELL_ID_RE.findall(p.read_text(encoding="utf-8", errors="replace"))), ""
    except Exception as exc:  # noqa: BLE001
        return set(), f"decomp artifact unreadable: {exc}"


def _vintage_resolves(vintage: str) -> bool:
    """Does this hash name a real commit in THIS repo?

    `^{commit}` is deliberate: it peels tags and REFUSES a hash that resolves to a
    non-commit object, so a tree/blob hash cannot masquerade as a vintage.
    """
    if not vintage:
        return False
    try:
        return subprocess.run(
            ["git", "cat-file", "-e", f"{vintage}^{{commit}}"],
            cwd=WORKSPACE, capture_output=True).returncode == 0
    except Exception:  # noqa: BLE001
        return False


def vintage_check(inst: dict) -> tuple[list, list]:
    """decomp_ref.vintage_commit must RESOLVE. (violations, frames)

    FOUND IN VERIFICATION, NOT IN AUTHORING -- 3.0.0_SA_CVO, 66693: the field was
    REQUIRED by schema and its VALUE was never checked by any layer, so a hash ONE
    CHARACTER OFF the true one read VALID. Reproduced at this seat on ETFS TO-3:
    20c092c0da (real) VALID; 20c092c0db VALID; deadbeef99 VALID.

    WHY THIS IS NOT PEDANTRY, in CVO's words: AN UNVERIFIED VINTAGE IS WORSE THAN A
    MISSING ONE -- a missing one makes a reader ask, a wrong one makes them stop
    asking. And the dangerous input is not `deadbeef99`; it is the one-character slip,
    which looks exactly like a real hash and survives human review too. The field
    exists to pin WHICH version of the decomp the work was built against (Rule 22: a
    citation without a vintage is not a citation) -- an unresolvable one pins nothing
    while looking like it does.

    Runs whenever the instance CARRIES a decomp_ref, on either branch: the claim is
    the instance's own, so it is checkable regardless of what the governing TO does.

    NAMED NON-GOAL (CTO 66702, declared here rather than silently absent):
    CONTAINMENT -- whether that vintage's tree actually contains decomp_ref.doc, and
    whether the doc at that vintage carries the cited cells -- is NOT checked. It is
    the layer-5 judgment residue's mechanical edge and costs a git read per check,
    and the existence check already kills the one-char-off class that was measured.
    A real instance citing a RESOLVING vintage whose tree lacks the doc re-opens this
    as its own item.
    """
    frames: list[str] = []
    v: list[str] = []
    dr = inst.get("decomp_ref")
    if not isinstance(dr, dict):
        return v, frames
    vintage = str(dr.get("vintage_commit", "")).strip()
    if not vintage:
        return v, frames  # absence is the schema's business, not this check's
    if _vintage_resolves(vintage):
        frames.append(f"vintage-frame: decomp_ref.vintage_commit {vintage} RESOLVES to a "
                      f"commit in this repo (containment NOT checked -- declared non-goal)")
    else:
        v.append(f"decomp_ref.vintage_commit: '{vintage}' does NOT resolve to a commit in "
                 f"this repo -- the field exists to pin WHICH decomp vintage the work was "
                 f"built against, and an unresolvable hash pins nothing while looking like "
                 f"it does. A one-character slip reads exactly like a real hash to a human "
                 f"reviewer, which is why this is mechanical")
    return v, frames


def alignment_check(inst: dict) -> tuple[list, list]:
    """(violations, frames). FRAMES PRINT WHETHER OR NOT ANYTHING FAILS -- a count with
    no denominator beside it is the exact class this gate exists to close, and a bare
    'aligned' is as unreadable as a bare 0."""
    global _BACKWARD_ASSERTED
    _BACKWARD_ASSERTED = None  # reset per call: an early return leaves "not evaluated", never a stale value
    frames: list[str] = []
    v: list[str] = []
    code = _project_code(str(inst.get("to_id", "")))
    stage = _dep_stage(code)
    frames.append(
        f"alignment-frame: project={code or '<unparsed>'} "
        f"dep_stage={stage if stage else 'ABSENT (not pipeline-registered)'}")

    # The instance's OWN claim, checked on either branch -- an ANNOUNCE verdict must not
    # launder an unresolvable vintage just because the governing TO is pre-pipeline.
    vv, vf = vintage_check(inst)
    v.extend(vv)
    frames.extend(vf)

    to_path, note, scanned = _resolve_governing_to(inst)
    if to_path is None:
        frames.append("alignment-frame: governing TO UNRESOLVED -- " + note
                      + (f" (scanned {scanned} TO file(s))" if scanned else ""))
        # FAIL CLOSED ON UNKNOWN, BUT ONLY WHERE UNKNOWN IS ACTUALLY A DEFECT.
        # The enforce discriminator lives in the TO, so an unresolved TO means the gate
        # DID NOT RUN. Returning no violation there would pass on UNKNOWN -- and the
        # cheapest route around this whole gate would be a bogus to_ref. Two closures,
        # deliberately narrow so the 126 of 131 instances whose projects are not
        # pipeline-registered are untouched:
        #   (a) a DECLARED decomp_ref.to_ref that does not resolve is a broken citation
        #       and is always a violation -- the instance made a claim that is false.
        #   (b) an id-scan miss on a PIPELINE-REGISTERED project is a violation: a
        #       pipeline project's instance must be joinable to its TO. On a project
        #       with no dep_stage it stays an announce, because there is nothing to
        #       join to and no claim was made.
        if "UNTRACKED" in note:
            frames.append(
                "alignment: NOT EVALUATED -- the governing TO exists but is UNCOMMITTED. "
                "A peer's (or this seat's) in-flight edit must not become the authority a "
                "verdict is built against; commit it and re-run. Not a violation.")
        elif str(inst.get("decomp_ref", {}).get("to_ref", "")).strip():
            v.append(f"decomp_ref.to_ref: {note} -- a declared reference that does not "
                     f"resolve is a false citation, and the alignment join CANNOT RUN "
                     f"without it; this is UNKNOWN, not PASS")
        elif stage:
            v.append(f"alignment: governing TO UNRESOLVED ({note}) on a PIPELINE-REGISTERED "
                     f"project (dep_stage={stage}) -- the enforce discriminator lives in "
                     f"the TO, so this instance CANNOT be shown to satisfy layer 1; state "
                     f"the TO with decomp_ref.to_ref. UNKNOWN is not PASS")
        else:
            frames.append(
                "alignment: NOT EVALUATED -- no governing TO resolved and the project is "
                "not pipeline-registered, so there is nothing to join to and nothing is "
                "claimed. Announce only.")
        return v, frames
    frames.append(f"alignment-frame: governing TO={to_path.relative_to(WORKSPACE)} ({note}"
                  + (f", scanned {scanned}" if scanned else "") + ")")

    to = _parse_to(to_path.read_text(encoding="utf-8", errors="replace"))
    if not to["has_decomp_ref"]:
        frames.append(
            "alignment: ANNOUNCE -- the governing TO carries NO <decomp_ref>, so this is "
            "PRE-PIPELINE work completing under its own spec; decomp_ref is not required "
            "and this instance stays VALID on that basis (CTO ruling 66492). A TO cut "
            "under the pipeline carries <decomp_ref> and is enforced here by construction.")
        return v, frames

    # ENFORCE from here: the TO declared a decomp, so the instance owes the join.
    dr = inst.get("decomp_ref")
    if not isinstance(dr, dict):
        v.append("decomp_ref: the governing TO carries <decomp_ref>, so this instance MUST "
                 "carry a decomp_ref object (doc + vintage_commit + to_ref) -- pipeline "
                 "gate layer 1; without it NO cell<->criterion join is computable at all")
        frames.append(
            "alignment: ENFORCE (TO carries <decomp_ref>) -- instance decomp_ref ABSENT")
        return v, frames
    frames.append("alignment: ENFORCE (TO carries <decomp_ref>)")

    inst_doc = str(dr.get("doc", "")).strip()
    if inst_doc and to["decomp_doc"] and (
            Path(inst_doc).as_posix() != Path(to["decomp_doc"]).as_posix()):
        v.append(f"decomp_ref.doc: instance names '{inst_doc}' but the governing TO names "
                 f"'{to['decomp_doc']}' -- the instance and its TO disagree about which "
                 f"decomp this work discharges")
    cells, err = _decomp_cell_ids(to["decomp_doc"] or inst_doc)
    if err:
        v.append(f"decomp-resolution: {err} -- cell_refs cannot be checked against an "
                 f"unreadable decomp, and an unresolvable citation is not a citation")
        return v, frames
    frames.append(f"alignment-frame: decomp id space = {len(cells)} distinct cell id(s) in "
                  f"{to['decomp_doc'] or inst_doc}")

    crits = to["criteria"]
    n_crit = len(crits)
    # FORWARD 1 -- every criterion names at least one cell.
    missing = to["criteria_without_cell_refs"]
    frames.append(f"alignment-forward-1 (criterion -> cell): "
                  f"{n_crit - len(missing)}/{n_crit} criteria carry >=1 cell_ref")
    for cid in missing:
        v.append(f"alignment: criterion '{cid}' carries NO cell_refs -- REFUSED, never "
                 f"retrofitted: a derived cell_ref makes alignment LOOK satisfied while "
                 f"being FALSE")
    # FORWARD 2 -- every named cell exists in the decomp's id space.
    all_refs = sorted({c for refs in crits.values() for c in refs})
    unknown = [c for c in all_refs if c not in cells]
    frames.append(f"alignment-forward-2 (cell_ref -> decomp): "
                  f"{len(all_refs) - len(unknown)}/{len(all_refs)} distinct cell_ref(s) "
                  f"resolve to an id declared in the decomp")
    for c in unknown:
        owners = sorted(k for k, refs in crits.items() if c in refs)
        v.append(f"alignment: cell_ref '{c}' (cited by {owners}) does NOT exist in "
                 f"{to['decomp_doc']} -- a citation to a cell that is not there is worse "
                 f"than no citation")
    # BACKWARD -- every cell the TO declared is reachable from some criterion.
    # ENFORCE ONLY ON A DELIMITED SET (CTO 66893 constraint (b)). On an undelimited
    # <decomp_ref> the harvest cannot tell an OWNED cell from one merely READ or
    # explicitly EXCLUDED, so a mismatch there is NOT evidence of an over-claim and must
    # not be asserted as one. It announces instead -- an honest "I cannot tell" beats a
    # confident inversion of the TO's own words.
    declared = to["declared_cells"]
    delimited = to["delimited"]
    # 2026-08-28 (DT~X 79061, six KEYFILL faces): when the delimiter is absent this limb ANNOUNCES
    # instead of asserting -- correct -- but the run still ended in a bare "VALID", so a VALID on an
    # undelimited face read as the same statement as a VALID on a delimited one. The verdict line
    # now carries the degradation (main() reads this flag); rc is unchanged.
    _BACKWARD_ASSERTED = bool(delimited)
    if to["delimiter_stray_text"]:
        v.append(f"decomp_ref/<owned_cells>: contains non-id text "
                 f"({to['delimiter_stray_text'][:60]!r}) -- the delimiter is machine-parsed "
                 f"and carries CELL IDS ONLY; prose belongs in the <decomp_ref> body or a "
                 f"sibling <decomp_context>, never inside the delimiter")
    reached = {c for c in declared if any(c in refs for refs in crits.values())}
    src = "<owned_cells>" if delimited else "<decomp_ref> (UNDELIMITED, wide harvest)"
    frames.append(f"alignment-backward (declared cell -> criterion): "
                  f"{len(reached)}/{len(declared)} cell(s) declared in the TO's "
                  f"{src} are reachable from >=1 criterion")
    unreached = sorted(set(declared) - reached)
    if unreached and not delimited:
        frames.append(
            f"alignment-backward: UNDELIMITED -- {len(unreached)} harvested id(s) "
            f"{unreached} are not reached by any criterion, but this <decomp_ref> has no "
            f"<owned_cells> delimiter, so a READ-DEPENDENCY or an EXPLICIT EXCLUSION "
            f"CLAUSE reads here as a claim. NOT asserted as a violation. Add "
            f"<owned_cells>id, id</owned_cells> inside <decomp_ref> to make this enforceable.")
    for c in unreached if delimited else []:
        v.append(f"alignment: declared cell '{c}' is named in the TO's <owned_cells> but NO "
                 f"criterion references it -- the TO claims a cell it never discharges")
    frames.append(
        "alignment-scope: this closes the TO against ITSELF and against the decomp's id "
        "space. Whether the TO's declared set IS the decomp's complete criterion-bearing "
        "set is a CVO cert judgment (enforcement layer 5), NOT asserted here.")
    return v, frames


def main() -> int:
    if len(sys.argv) not in (2, 3):
        print(__doc__)
        return 2
    try:
        inst = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        print(f"READ-ERROR: {exc}")
        return 2

    violations: list[str] = []
    if len(sys.argv) == 3:
        violations.extend(coverage_check(inst, sys.argv[2]))
    else:
        print("NOTE: no expected_criterion_ids given -- COVERAGE UNCHECKED (row quality only; "
              "an omitted criterion is invisible to this run). The cert consumer runs step-zero.")
    try:
        import jsonschema  # type: ignore

        for err in sorted(jsonschema.Draft7Validator(schema).iter_errors(inst), key=str):
            violations.append(f"schema: {'/'.join(str(p) for p in err.absolute_path) or '<root>'}: {err.message}")
        structural = "jsonschema"
    except ImportError:
        # Degrade LOUDLY: minimal required-keys check only.
        structural = "FALLBACK (jsonschema not installed -- structural coverage PARTIAL; install for full)"
        for k in schema.get("required", []):
            if k not in inst:
                violations.append(f"schema-fallback: missing required key '{k}'")

    violations.extend(conditional_checks(inst))
    # PIPELINE GATE LAYER 1. Runs on EVERY instance: its own first act is to decide
    # ENFORCE vs ANNOUNCE from the governing TO, so it must not be called conditionally
    # here -- a caller-side condition would be a second, silently divergent copy of the
    # discriminator.
    align_violations, align_frames = alignment_check(inst)
    violations.extend(align_violations)

    n_acc = len(inst.get("acceptance", []))
    print(f"proof-of-spec-check | structural={structural} | acceptance rows={n_acc} | violations={len(violations)}")
    for line in align_frames:
        print(f"  {line}")
    # ALIGNMENT AND SCHEMA ARE DIFFERENT ORACLES, AND THE ALIGNMENT LINES ARE BYTE-IDENTICAL
    # ON A VALID AND AN INVALID INSTANCE. Measured 2026-08-26 on one real instance: stripping
    # NINE required properties left forward-1 13/13, forward-2 22/22 and backward 22/22
    # completely unchanged while the run went rc=0 -> rc=1. So a seat quoting "alignment closes
    # both directions" states something TRUE that carries ZERO information about structural
    # validity -- and those sub-lines do get quoted in certs and returns.
    # The rc and the VALID/INVALID line already discriminate; this annotates the lines that do
    # not, so the figures cannot be lifted out of an INVALID run and read as reassurance.
    # Surfaced by 0.4.0_DS_ClientPlatform~Q, who hit it by modelling an instance on a peer's
    # file instead of on the schema and then READ THE OUTPUT HONESTLY.
    if align_frames and violations:
        print("  WARN: alignment above is computed on a STRUCTURALLY INVALID instance. Those "
              "figures describe the criterion-to-cell MAPPING ONLY and are identical to what a "
              "VALID instance prints -- they are NOT evidence of validity. Do not quote them "
              "without the verdict.")
    for line in violations:
        print(f"  VIOLATION: {line}")
    if violations:
        print("INVALID")
    elif _BACKWARD_ASSERTED is False:
        # A VALID whose backward limb was never asserted is a WEAKER statement than a VALID on a
        # delimited face, and nothing in the bare word said so (DT~X 79061). Same rc; the verdict
        # line names the limb it could not enforce.
        print("VALID -- alignment-backward UNASSERTED (undelimited <decomp_ref>: put "
              "<owned_cells>id, id</owned_cells> INSIDE <decomp_ref> to make it enforceable)")
    else:
        print("VALID")
    return 0 if not violations else 1


if __name__ == "__main__":
    # A CRASH IS NOT A VERDICT, AND IT MUST NOT BORROW ONE'S EXIT CODE.
    # rc=1 means INVALID -- a real adjudication about the caller's instance. rc=2 means
    # "this tool could not answer" (the existing READ-ERROR convention at main()).
    # An UNCAUGHT exception used to fall through Python's default rc=1, so a tool crash and
    # a legitimate INVALID were INDISTINGUISHABLE to a caller checking only the rc -- and
    # every TO comment in the estate instructs callers to check the rc. That is an
    # instrument failing in the direction of its own normal-looking output.
    # Class surfaced by 0.6.0_AE_PartnerETL (71621) on the decomp_ref-as-string case;
    # this handler closes the CLASS, not that one field.
    try:
        sys.exit(main())
    except SystemExit:
        raise
    except Exception as exc:  # noqa: BLE001
        import traceback

        traceback.print_exc()
        print(f"TOOL-ERROR: {type(exc).__name__}: {exc}")
        print("NOT-A-VERDICT: this is a tool failure (rc=2), not an INVALID instance (rc=1).")
        sys.exit(2)
