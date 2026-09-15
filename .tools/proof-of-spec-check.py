#!/usr/bin/env python3
"""proof-of-spec-check -- validate a PROOF_OF_SPEC instance against the canonical schema.

Andrew-direct 2026-08-11 ~0815Z: build TOs carry machine-readable JSON deliverable
expectations the Tier-2 assignee fills to PROVE work was done to spec. This is the
mechanical gate: a TO is not complete until its instance passes here.

Usage: proof-of-spec-check <instance.json> [expected_criterion_ids] [--governing-order <order.md>]
  --governing-order <order.md>  BIND the governing order (FE-s-37, RULING S, row S61): that order -- the one
                            being closed -- is the governing order for EVERY limb, and an instance whose
                            decomp_ref.to_ref or to_id names a DIFFERENT order is REFUSED before any limb runs,
                            by a violation naming both. to-pipeline-gate.py's complete-flip path always passes
                            it. WITHOUT it the run is UNBOUND: the order is resolved from the instance's own
                            to_ref / to_id exactly as before, and a `governing-binding: UNBOUND` frame says so.
  expected_criterion_ids: comma-separated list OR a path to a file (one id per line) --
  the TO's embedded criterion set. When given, COVERAGE is checked BEFORE quality:
  an instance valid on every row it carries can still silently OMIT a criterion
  (the row-quality/row-coverage split -- CVO's step-zero, mechanized). Missing or
  extra criteria are violations, with both denominators printed.
Exit 0 = VALID. Exit 1 = INVALID (every violation printed). Exit 2 = usage/read error.
  --self-test               exercise the SURPRISES LIMB, the v3 expect/judgment carrier, the
                            INVOCATION ALIGNMENT limb, the COUNT-BAR limb and the DRIVES limb
                            red-first (N of N printed; rc 0 only when every arm behaves) -- the
                            battery lives HERE because the checker's author seat is deliberately
                            not in the TOOL_BATTERIES lane.
  There is NO --help. An unrecognised single argument is read as an INSTANCE PATH.

COUNT-BAR LIMB and DRIVES LIMB (2026-09-13, FE-s-29; 1.0.0_SA_CTO RULINGS M(ii) and Q, rows S56, S42,
C-S67): a PASS whose zero-count bar matches evidence that ALSO carries a nonzero count of the same noun
is refused; every criterion of a new IRPT_FNTEND order declares drives="network" or drives="none", and a
drives="network" PASS whose invoked `bun test` file seeds the body through an `initial*` prop is refused.
Both REFUSE for a NEW instance and ANNOUNCE for a LEGACY one, NEW meaning the governing order was first
added in a commit descending from the ruling's pin -- repository state, never a clock or a list. And the
<placeholders> reader is LINE-ANCHORED (RULING M(i), rows S53, W4-S7). See the blocks above each limb.

INVOCATION ALIGNMENT LIMB (2026-09-12, FE-s-23, row IRPT_FNTEND-S31): each acceptance row's recorded
`invocation` is compared against the same-id criterion's <invocation> in the GOVERNING TASK ORDER,
modulo the declared placeholders and trailing/leading whitespace ONLY -- a changed flag, path, query
parameter or quoted argument is a divergence, and the frame prints both strings and the criterion id.
It closes the hole S31 measured: an issuer corrects the SPAWN PROMPT and never the task-order FILE,
the worker runs the corrected command, the record is faithful to the prompt and FOREIGN to the order,
and this checker said VALID. ENFORCE is OPT-IN: a TO carrying <placeholders>WS, PORT</placeholders>
gets VIOLATIONS; a TO without one gets the same diagnostic as ANNOUNCE frames and refuses nothing
(measured before the choice: 318 of 874 comparable rows across 294 committed instances diverge, mostly
honestly -- refusing by default would retro-invalidate the estate). See the block above the limb.

SURPRISES LIMB (Andrew-direct 2026-09-03 ~03:1xZ at the 3.0.0_SA_CVO terminal, relayed 92976, VERBATIM:
"claude.md should not have that rule to do this over mcp + any gate with proof of spec surprises field to
prevent this should be implemented now"): a surprise exists as a ROW in the project's channel or it does
not exist. Every `surprises` entry opens with the ROW ID it names ("<PROJECT>-S<n>: <one line>", site Z
"<PROJECT>-Z-S<n>"), and that id must resolve to a row in the project's INVESTIGATION file on EITHER root
(flat org/surprise_channel/<CODE>/, tree org/missions/D*/*/<CODE>/surprise-channel/investigations/).
ENFORCED when the governing TO lives under the TREE root -- prospective by construction, every tree TO is
new; ANNOUNCED (frame lines, no violation) for flat-root and unresolved TOs, so the 288 legacy instances
with free-string entries are never re-graded. Because to-workflow-gate.py's check_complete_flip runs this
checker on a terminal <status> flip, a tree TO whose instance names a surprise with no row CANNOT flip
to complete. Trap named: this gate reads FILES; it cannot see the broker plane, which is exactly why the
carrier must be the row.
Every verdict line NAMES its rc (1.0.0_SA_CTO 87900 (1c), adopted from 0.4.0_DS_ClientPlatform~N):
rc=2 is a USAGE/READ error, rc=1 is INVALID, rc=0 is VALID -- a caller reading only "non-zero"
conflates a mis-typed argument with a refuted proof. The header also prints `checker-vintage:
<hash> <UTC Z>` (1b) so no seat derives the vintage by hand in local time; when the checker's own worktree
differs from HEAD the line carries `+DIRTY(<n> lines)` (1b', 3.0.0_SA_CVO 88184) so it is true of the bytes
that ran, never only of the last commit.

Layered: jsonschema (if installed) for structure, then the conditional rules the
schema cannot express -- ALWAYS run, so absence of the jsonschema package degrades
coverage LOUDLY rather than silently passing (the import-guard-answers-completion
-not-presence class).

the L7 completion gate of the canonical fabric workflow (2026-08-24, 0.8.0_AE_CloudComp~F): every run also resolves the
GOVERNING TO and checks decomp_ref + the bidirectional cell<->criterion alignment, with
a denominator printed for each direction. ENFORCE vs ANNOUNCE is derived from that TO --
a TO carrying <decomp_ref> obliges its instance to carry decomp_ref and to close the
join; a TO without one is pre-workflow work and stays VALID. The alignment frames print
whether or not anything failed. See org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md.
decomp_ref.vintage_commit is also checked to RESOLVE to a real commit (CVO 66693,
routed CTO 66702); CONTAINMENT of the doc at that vintage is a declared NON-GOAL.
The BACKWARD direction enforces only against a DELIMITED <owned_cells> clause inside
<decomp_ref> (CTO 66893): an undelimited element cannot distinguish an owned cell from
one merely READ or explicitly EXCLUDED, so it ANNOUNCES rather than asserting.
"""
from __future__ import annotations

import json
import os
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
        # spine v3.0 L6/L7/L9 (one clause per criterion; Andrew-direct 2026-09-03 ~22:2xZ, carrier 4 of eight):
        # a MECHANICAL criterion carries `expect`, the pattern its output must match -- PASS is decided by the
        # match, never by the worker; a JUDGMENT criterion carries no verdict at all -- the CVO grades it at L9.
        # Both fields are OPTIONAL in the schema so every pre-v3 instance still validates as it did.
        if row.get("judgment") is True and row.get("status") in ("PASS", "FAIL"):
            v.append(f"acceptance[{rid}]: judgment=true carries a verdict (status={row.get('status')}) -- a judgment "
                     f"criterion is graded only by the CVO at L9 (spine v3 L9); record the output under "
                     f"UNVERIFIABLE-BY-INSTRUMENT with status_reason naming the CVO, never PASS/FAIL")
        exp = row.get("expect")
        if isinstance(exp, str) and exp.strip():
            import re as _re_x
            try:
                matched = _re_x.search(exp, row.get("output_evidence", "") or "", _re_x.S | _re_x.M) is not None
            except _re_x.error as exc:
                matched = None
                v.append(f"acceptance[{rid}]: expect is not a valid pattern ({exc}) -- a criterion whose expectation "
                         f"cannot be evaluated cannot pass")
            if matched is False and row.get("status") == "PASS":
                v.append(f"acceptance[{rid}]: status=PASS but output_evidence does NOT match expect {exp!r} -- "
                         f"the match decides a mechanical criterion, not the worker (spine v3 L7); INVALID")
            if matched is True and row.get("status") == "FAIL" and not row.get("status_reason"):
                v.append(f"acceptance[{rid}]: status=FAIL while output_evidence matches expect -- state the reason")
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


PENDING_SENTINEL = "PENDING-THIS-COMMIT"
_COMMITISH_RE = re.compile(r"^[0-9a-f]{7,40}$")
_REPO_ROOT = Path(__file__).resolve().parent.parent


def artifact_resolution_check(inst: dict, inst_path=None) -> tuple[list[str], list[str]]:
    """ARTIFACT ROW RESOLUTION (2026-08-30, 1.0.0_SA_CTO~X on 2.0.0_SA_COO~X's proposal 85753). Two
    instances in one night passed this checker VALID and were caught BY HAND: TO-L3W3-COX @c36a309f4d
    named its own proof at a path that never existed in git; TO-L3W3-CCX @fa7b34274a carried the
    PENDING sentinel on rows whose artifacts had landed in an EARLIER commit. The schema validates a
    row's SHAPE; a legal-looking (commit, path) pair that git alone can falsify is invisible to it.

    For every artifacts_produced row that names a REPO artifact (kind != s3_object):
      - commit_or_etag == PENDING-THIS-COMMIT: the artifact rides the commit that will carry the proof,
        which does not exist at check time, so the path must at least EXIST IN THE WORKING TREE. A
        dead path here is a VIOLATION (the COX class).
      - a commit-ish (7-40 hex): the commit must resolve in the LOCAL object store, then
        `<commit>:<path>` must exist. Absent -> VIOLATION (a path claimed at a pin that does not
        carry it).
    CONTENT RUNG (88109): a row may carry `introduces: [token, ...]`; the tokens must be present in the
    blob at the pin and absent at `<pin>~1` (or the file absent there) -- a pin that exists but does not
    carry the change is a VIOLATION; a token present at both is "not introduced here". Rows without
    `introduces` are PRESENCE-ONLY and the frame counts them as such.
    ANNOUNCED, never a violation: a commit-ish that is not in the local object store (UNRESOLVED-HERE
    -- a cross-fabric pin before a fetch is not a false claim); s3_object rows (an ETag is not a git
    ref -- the served plane is read by a different instrument).
    NOT COVERED, stated so nobody reads a clean frame as covering it: the CCX class proper -- a PENDING
    sentinel on a row whose artifact is ALREADY committed. Before the proof's commit exists there is
    no candidate to compare against; the issuer's --stat read at close is the instrument for that.
    Every count prints with its denominator."""
    v: list[str] = []
    rows = inst.get("artifacts_produced", []) or []
    n_resolved = n_pending = n_unresolved = n_s3 = 0
    # CONTENT RUNG (2026-08-30, 1.0.0_SA_CTO 88109, one plane over from the (1a) content-not-presence
    # rule): the INDEXBYTES proof's fix row resolved because its pin EXISTED while the blob at that pin
    # LACKED the change the criterion named (the pin was another seat's unrelated commit). A row may
    # declare `introduces: [token, ...]`; then every token must be PRESENT in the blob at the pin and
    # ABSENT in the blob at the pin's PARENT (`<pin>~1`, never `^` -- a caret through a shell is not a
    # parent), or the file must be absent at the parent. A PENDING row is checked the same way against
    # the WORKTREE file and HEAD's blob. Rows WITHOUT `introduces` stay presence-resolved and the frame
    # names that class, so a clean line cannot be read as content-resolved.
    n_content = n_presence_only = 0

    def _blob(ref: str) -> bytes | None:
        try:
            o = subprocess.run(["git", "show", ref], cwd=str(_REPO_ROOT), capture_output=True, timeout=30)
        except Exception:  # noqa: BLE001
            return None
        return o.stdout if o.returncode == 0 else None

    def _content_rung(path: str, tokens: list, here: bytes | None, parent: bytes | None, where: str) -> str | None:
        """None when the tokens are introduced at `where`; else the violation text."""
        if here is None:
            return f"artifact-resolution/content: {path!r} unreadable at {where}"
        missing = [t for t in tokens if t.encode("utf-8") not in here]
        if missing:
            return (f"artifact-resolution/content: {path!r} at {where} LACKS the token(s) the row says it "
                    f"introduces: {missing} -- the pin exists but does not carry the change (88109 class)")
        if parent is not None:
            already = [t for t in tokens if t.encode("utf-8") in parent]
            if already:
                return (f"artifact-resolution/content: {path!r}: token(s) {already} are ALREADY present at the "
                        f"parent of {where} -- not introduced here; the row pins a commit that did not make the change")
        return None

    def _git_ok(*args: str) -> bool:
        try:
            return subprocess.run(["git", *args], cwd=str(_REPO_ROOT), capture_output=True,
                                  timeout=30).returncode == 0
        except Exception:  # noqa: BLE001 -- a git that cannot run is announced below, not a pass
            return False

    def _git_out(*args: str) -> str:
        try:
            o = subprocess.run(["git", *args], cwd=str(_REPO_ROOT), capture_output=True, text=True,
                               encoding="utf-8", errors="replace", timeout=30)
        except Exception:  # noqa: BLE001
            return ""
        return o.stdout if o.returncode == 0 else ""

    # CO-COMMIT RESOLUTION OF PENDING ROWS (2026-09-03, 1.0.0_SA_CTO on 3.0.0_SA_CVO~A's NFRA_CLDGRPH finding,
    # relayed 93334/93337): a PENDING-THIS-COMMIT row was HONEST at write time and PERMANENTLY UNVERIFIED after it
    # -- before the commit there was no hash to compare, after the commit nobody re-ran the checker, and the
    # co-commit that opens the gap is the spine's own prescribed L7 shape (status, proof and artifacts in one
    # commit by the actor). The CCX class ("PENDING on a row whose artifact had ALREADY landed") was disclosed as
    # NOT COVERED. It is covered now, in both contexts the checker runs in, by reading the INDEX or the RECORD:
    #   PRE-COMMIT  (the instance file is staged or untracked): the artifact must be STAGED in this same commit
    #               (`git diff --cached --name-only -- <path>` non-empty) -> CO-COMMITTED. Already committed at
    #               HEAD and not staged -> the CCX violation (pin the commit that carried it), EXCEPT in a DRY RUN
    #               (the instance unstaged) where git reports the tracked artifact MODIFIED IN PLACE -> PENDING: Rule
    #               14a forbids pre-staging it and safe-commit stages the pathspec, so it rides (row LGIC_ENFORCE-C-S9).
    #               In the worktree but not staged -> a violation (it cannot ride this commit).
    #   POST-COMMIT (the instance is tracked and unstaged; a certifier's re-run): the artifact must be TOUCHED
    #               by the instance's own commit (`git diff-tree --name-only <c> -- <path>` non-empty) ->
    #               CO-COMMITTED at <c>. Present at <c> but not touched by it -> the CCX violation. Absent -> a
    #               violation.
    #   UNKNOWN     (no instance path handed in): the old presence-only read, announced as such.
    # The content rung on a PENDING row now compares the index blob (or <c>:<path>) against its parent instead of
    # the worktree against HEAD. Fails toward a LOUD violation, never toward absence.
    inst_rel = None
    ctx = "UNKNOWN"
    inst_commit = None
    dry_run = False
    _foreign_tree = None
    if inst_path is not None:
        try:
            inst_rel = Path(inst_path).resolve().relative_to(_REPO_ROOT).as_posix()
        except ValueError:
            # NFRA_IAMROLES202609-Z-S10 (2.0.0_SA_COO~ZI, 2026-09-10): the instance lives OUTSIDE the
            # tree this script lives in -- under spine v3 that is EVERY worker instance, because every
            # worker is in a linked worktree BY CONSTRUCTION. This used to set inst_rel = None SILENTLY,
            # which dropped inst_commit, which disabled the `cat-file -e {inst_commit}:{path}` fallback
            # at the presence test -- so the artifact read as ABSENT and the violation NAMED THE
            # WORKER'S FILE. A checker that cannot see a tree must say THAT, not blame the artifact:
            # the honest party was being reported as the defective one.
            inst_rel = None
            _foreign_tree = str(Path(inst_path).resolve())
    if _foreign_tree is not None:
        # REFUSE LOUD rather than grade a pair this checker cannot see (the preferred shape named in
        # Z-S10). Resolving the foreign tree would also need git re-pointed at it; refusing is smaller,
        # cannot produce a wrong verdict in EITHER direction, and names the zero-cost workaround.
        return ([f"artifact-resolution/CHECKER-SCOPE: this proof-of-spec-check lives in {_REPO_ROOT} but the "
                 f"instance is at {_foreign_tree}, OUTSIDE that tree -- it cannot resolve the instance's commit "
                 f"and CANNOT GRADE IT. This is NOT a finding against the instance or its author. "
                 f"Run the WORKTREE'S OWN .tools/proof-of-spec-check.py from inside that worktree."], [])
    if inst_rel:
        staged_inst = _git_out("diff", "--cached", "--name-only", "--", inst_rel).strip()
        tracked_inst = _git_ok("ls-files", "--error-unmatch", "--", inst_rel)
        if staged_inst or not tracked_inst:
            ctx = "PRE-COMMIT"
            # DRY RUN vs HOOK RUN (2.0.0_SA_COO~A 93362, measured): the faces say "VALID BEFORE the flip" and 14a says
            # a seat does not pre-`git add`, so a worker's natural dry run is an UNTRACKED instance with UNTRACKED
            # artifacts and nothing staged. Inside safe-commit's hook the INSTANCE is staged; in a dry run it is not.
            # An UNTRACKED artifact (never committed anywhere) in a dry run is honestly PENDING -- it rides the commit
            # if staged, and the hook run refuses if it is not. The CCX refusal (already at HEAD, not staged) stands in
            # both, because that artifact cannot ride this commit whatever gets staged.
            dry_run = not staged_inst
        else:
            inst_commit = _git_out("log", "-1", "--format=%H", "--", inst_rel).strip() or None
            ctx = "POST-COMMIT" if inst_commit else "UNKNOWN"
    n_cocommit = 0

    for a in rows:
        if not isinstance(a, dict):
            continue
        path = str(a.get("path_or_key", "") or "")
        pin = str(a.get("commit_or_etag", "") or "")
        if a.get("kind") == "s3_object":
            n_s3 += 1
            continue
        tokens = a.get("introduces") or []
        if tokens and not (isinstance(tokens, list) and all(isinstance(t, str) and t for t in tokens)):
            v.append(f"artifact-resolution/content: {path!r} carries `introduces` that is not a list of non-empty strings")
            tokens = []
        if pin == PENDING_SENTINEL:
            present_somewhere = bool(path) and ((_REPO_ROOT / path).exists()
                                                or (inst_commit is not None and _git_ok("cat-file", "-e", f"{inst_commit}:{path}")))
            if not present_somewhere:
                v.append(f"artifact-resolution: {path!r} is PENDING-THIS-COMMIT but does NOT exist in the "
                         "working tree (nor at the instance's commit) -- a dead path cannot ride the commit that carries this proof")
                continue
            if ctx == "PRE-COMMIT":
                if _git_out("diff", "--cached", "--name-only", "--", path).strip():
                    n_cocommit += 1
                    here, parent, where = _blob(f":{path}"), _blob(f"HEAD:{path}"), "the index (co-committed)"
                elif _git_ok("ls-files", "--error-unmatch", "--", path):
                    # A TRACKED artifact MODIFIED IN PLACE in a DRY RUN is honestly PENDING (row LGIC_ENFORCE-C-S9): Rule
                    # 14a forbids pre-staging it, and safe-commit stages the pathspec, so it rides the commit that carries
                    # the proof. "Modified" is git's own answer (`diff --quiet` exits 1), never a byte compare, so a CRLF
                    # checkout of an unchanged file on an autocrlf box does not read as modified. An UNCHANGED tracked
                    # artifact is still the CCX class -- nothing of it can ride this commit -- and the hook run (not a dry
                    # run) keeps refusing an unstaged artifact, because by then it will not ride.
                    if dry_run and not _git_ok("diff", "--quiet", "--", path):
                        n_pending += 1
                        here, parent, where = ((_REPO_ROOT / path).read_bytes(), _blob(f"HEAD:{path}"),
                                               "the worktree (dry run; tracked, modified in place, rides the commit if staged with the proof)")
                    else:
                        v.append(f"artifact-resolution: {path!r} is PENDING-THIS-COMMIT but is ALREADY COMMITTED at HEAD and "
                                 "NOT staged -- it will not ride this commit; pin the row to the commit that carried it (CCX class)")
                        continue
                elif dry_run:
                    n_pending += 1
                    here, parent, where = (_REPO_ROOT / path).read_bytes(), _blob(f"HEAD:{path}"), "the worktree (dry run; untracked, rides the commit if staged with the proof)"
                else:
                    v.append(f"artifact-resolution: {path!r} is PENDING-THIS-COMMIT but exists only in the working tree and "
                             "is NOT staged while the proof IS -- it cannot ride the commit that carries this proof; stage it in the same commit")
                    continue
            elif ctx == "POST-COMMIT":
                if _git_out("diff-tree", "--no-commit-id", "--name-only", "-r", inst_commit, "--", path).strip():
                    n_cocommit += 1
                    here, parent, where = (_blob(f"{inst_commit}:{path}"), _blob(f"{inst_commit}~1:{path}"),
                                           f"the instance's commit {inst_commit[:10]} (co-committed)")
                elif _git_ok("cat-file", "-e", f"{inst_commit}:{path}"):
                    v.append(f"artifact-resolution: {path!r} is PENDING-THIS-COMMIT but PREDATES the instance's commit "
                             f"{inst_commit[:10]} (present there, not touched by it) -- pin the row to the commit that carried it (CCX class)")
                    continue
                else:
                    v.append(f"artifact-resolution: {path!r} is PENDING-THIS-COMMIT but is ABSENT at the instance's commit "
                             f"{inst_commit[:10]} -- it did not ride the commit that carries this proof")
                    continue
            else:
                n_pending += 1
                here, parent, where = (_REPO_ROOT / path).read_bytes(), _blob(f"HEAD:{path}"), "the worktree (PENDING; instance path unknown, presence only)"
            if tokens:
                err = _content_rung(path, tokens, here, parent, where)
                if err:
                    v.append(err)
                else:
                    n_content += 1
            continue
        if not _COMMITISH_RE.match(pin):
            v.append(f"artifact-resolution: {path!r} carries commit_or_etag {pin!r}, which is neither "
                     "PENDING-THIS-COMMIT nor a 7-40 hex commit-ish for a repo artifact")
            continue
        if not _git_ok("cat-file", "-e", pin + "^{commit}"):
            n_unresolved += 1
            continue
        if _git_ok("cat-file", "-e", f"{pin}:{path}"):
            n_resolved += 1
            if tokens:
                err = _content_rung(path, tokens, _blob(f"{pin}:{path}"), _blob(f"{pin}~1:{path}"), f"pin {pin}")
                if err:
                    v.append(err)
                else:
                    n_content += 1
            else:
                n_presence_only += 1
        else:
            v.append(f"artifact-resolution: {path!r} does NOT exist at its declared pin {pin} -- "
                     "the row names a (commit, path) pair git refutes")
    frames = [f"artifact-resolution: {n_resolved} resolved at pin / {n_cocommit} PENDING co-committed "
              f"({ctx}: {'staged in this commit' if ctx == 'PRE-COMMIT' else 'touched by the instance commit ' + (inst_commit or '')[:10] if ctx == 'POST-COMMIT' else 'n/a'}) / "
              f"{n_pending} pending-on-worktree ({'dry run: untracked artifacts, or tracked ones git reports modified in place, that ride the commit if staged with the proof; the hook run decides' if dry_run else 'instance path unknown; presence only'}) / "
              f"{n_unresolved} UNRESOLVED-HERE (commit not in local store; announced, not asserted) / "
              f"{n_s3} s3_object (not a git ref; skipped) -- denominator {len(rows)} row(s); "
              "a PENDING row whose artifact is ALREADY committed (CCX class) is REFUSED here whenever the instance path is known, "
              "unless a dry run finds that tracked artifact modified in place (it rides the commit)",
              f"artifact-resolution/content: {n_content} row(s) CONTENT-resolved (`introduces` tokens present at the "
              f"pin, absent at its parent) / {n_presence_only} row(s) PRESENCE-ONLY (no `introduces`; the pin exists "
              "and carries the path, nothing here says it carries the CHANGE) -- 88109 class. LIMIT (0.4.0_DS_"
              "ClientPlatform~V via 2.0.0_SA_COO 88511): CONTENT-resolved proves a TOKEN MOVED between <pin>~1 and "
              "<pin>; it does NOT prove the token means what the citing face assumes. It catches a STALE pin, never "
              "a pin cited for the wrong reason."]
    return v, frames


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
# org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md ("build routed", tooling lane;
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
# PLUS the etfs-ingest TIER form (INGEST-T3-6, INGEST-CONV-1, INGEST-INV-2), added
# 2026-08-28 by 1.0.0_SA_CTO~Z on a CTO ruling, same class as the wave-4 note above and
# for the same reason: 36 real ids invisible, and the violations they produced were worded
# AGAINST THE EXECUTOR. Measured before the fix: of 31 DECOMP.md files 30 use the
# checker-visible lowercase form and etfs-ingest is the SOLE outlier -- it did not violate
# a convention, it failed to guess one that was written down NOWHERE a decomp author reads
# (this comment block was the only statement of it, i.e. declared where only the ENFORCER
# reads it).
#
# WHY PREFIX-ANCHORED AND NOT A GENERAL UPPERCASE-MIDDLE SHAPE. The obvious branch --
# [A-Z]{1,4}\d?-\d+ -- was BUILT AND REJECTED BY ITS OWN CONTROL: it admitted 572 distinct
# NEW-ONLY tokens across the corpus, including regex character classes in source
# ('A-Z0-9' in 62 files), prose ('AMONG-THE-6', 'AS-WE-4') and foreign id schemes
# ('AWS-IAM-1', 'AC-VAL-1'). Uppercase-hyphen-digit is the most common token shape in
# prose AND in code, so a shape-general branch cannot be narrow. Anchoring on the declared
# project prefix makes it unambiguous. CONTROLS, both run at the edit:
#   POSITIVE  36 of 36 real cells now matched; legacy D1-i-2 / ETFS-d-1 / D1-m-foo intact
#   NEGATIVE  36 NEW-ONLY tokens across the corpus, ALL of them real INGEST cell ids
#             (the shape-general candidate scored 572)
# INGEST-ZZ-99 is DELIBERATELY EXCLUDED: the decomp declares it a NEGATIVE CONTROL
# ("absent from both the cell set and the criteria refs, so the extraction discriminates").
# Admitting it would have retired another instrument's discriminator as a side effect.
# A future scheme gets its own anchored branch and its own two controls -- never a widening.
# TWO ANCHORED BRANCHES ADDED 2026-08-30 (2.0.0_SA_COO~X, on 0.8.0_AE_CloudComp~Y's measurement
# 84774): the L3W3 rectangle's family slugs are sha256-derived 4-HEX (dc02 / b8a2 / c69f) and the
# carding remainder's ids are CARD-R-<4hex|m>-N -- the letters-only slug branch above saw 13 of 34
# L3W3 cells and 0 of 18 carding cells, and the only fully visible set was the issuer's own
# mechanism cells. Per the rule two lines up these are ANCHORED branches with their own controls
# (.tools/tests/test_proof_of_spec_cell_id_re.py), never a widening of the letters-only class.
CELL_ID_RE = re.compile(
    r"\b(?:[A-Z][A-Z0-9]*-(?:m-[a-z0-9_]+|[a-z]{1,4}-[a-z]?\d+)"
    r"|L3W3-[0-9a-f]{4}-\d+"
    # ANCHORED BRANCH 2026-08-30 (1.0.0_SA_CTO~X, found by its own battery while fixing 87900): the sec-7b
    # rectangle's family slugs are 4-HEX too (1c16 / 4017 / 0b5f / 4565 / 8304) under the L3S7B prefix; the
    # L3W3 branch is prefix-anchored so it did not see them, and the letters-only branch cannot (a slug that
    # opens with a digit). Controls in test_proof_of_spec_cell_id_re.py + a corpus arm over all 21 ids of
    # rectangle.final.certified.json at its pin. The m-cells (L3S7B-m-N) already match the legacy branch.
    r"|L3S7B-[0-9a-f]{4}-\d+"
    r"|CARD-R-(?:m-\d+|[0-9a-f]{4}-\d+)"
    r"|INGEST-(?:T\d|CONV|INV)-\d+)\b")
OWNED_CELLS_RE = re.compile(r"<owned_cells>(.*?)</owned_cells>", re.S)
# (1a) 2026-08-30, 1.0.0_SA_CTO 87900: the <decomp_ref> element's CONTENT is the claim, not its
# PRESENCE. Three tooling faces carried "<decomp_ref>NONE -- one-branch remediation under its own
# charter</decomp_ref>": the presence test ENFORCEd them and then refused cell_refs they must not
# invent -- the checker demanding a value it forbids. A body that declares no decomposition (NONE /
# none / absent / n/a, with no decomp doc and no cell id) takes the ANNOUNCE branch, and the branch
# line prints WHY. A body naming a decomp doc takes ENFORCE regardless of any leading word.
DECOMP_REF_NONE_RE = re.compile(r"^\s*(NONE|None|none|ABSENT|Absent|absent|N/A|n/a)\b")
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
                ["git", "ls-files", "--", "*/task_orders/*.md", "*/task-orders/*.md"],  # R-ii: both roots
                cwd=WORKSPACE, capture_output=True, text=True, encoding="utf-8", errors="replace", check=True).stdout
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
            cwd=WORKSPACE, capture_output=True, text=True, encoding="utf-8", errors="replace").returncode
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


# ---------------------------------------------------------------------------
# GOVERNING-ORDER BINDING (2026-09-14, FE-s-37; 1.0.0_SA_CTO RULING S @942e4ff992 s.2; row IRPT_FNTEND-S61).
# THE CLASS. Every limb that decides ENFORCE vs ANNOUNCE -- alignment, surprises, invocation, count-bar, drives --
# reads its governing order through _resolve_governing_to, and that resolver took decomp_ref.to_ref, a field the
# graded party writes, as the SOURCE. 3.0.0_SA_CVO measured it on FE-s-29's own instance: to_ref pointed at the real
# round-4 order TO-FE-s-28 moved the count-bar and drives limbs to ANNOUNCE/LEGACY and no violation named the mismatch.
# THE BINDING. A caller that KNOWS the order -- to-pipeline-gate.py check_complete_flip, which is closing it -- passes
# --governing-order <path>. Then (a) BEFORE any limb runs, an instance whose decomp_ref.to_ref or to_id names a
# DIFFERENT order is refused by a violation naming both; and (b) that path IS the governing order for every limb, so
# the limbs read the flipped order whatever the instance says. to_ref and to_id stay CROSS-CHECKS, never the source.
# THE to_id CROSS-CHECK IS SLUG-TOLERANT, MEASURED BEFORE IT WAS WRITTEN: of 337 committed estate instances whose
# sibling order exists, 336 carry to_ref == that order (0 name another), and an EXACT to_id match would refuse 119 of
# them (a slug on one side -- `X.TO-CG-I-2` vs `X.TO-CG-I-2.edge-side-drop` -- or an order with no <to_id> tag). So an
# id matches the order when it equals the order's <to_id>, its filename stem, or an `id="..."` declaration, or when
# one is the other plus a `.`-delimited suffix and the shorter carries `.TO`. A bare `X` never matches `X.TO-1`, and
# `...FE-s-2` never matches `...FE-s-29`.
# UNBOUND (the CLI without --governing-order): resolution is exactly what it was, and a frame says the run is UNBOUND.
# No verdict is looser than before the binding existed; an unbound run is simply not protected from its own to_ref.
_BOUND_ORDER: Path | None = None   # set once by main() from --governing-order; None = UNBOUND
_TO_ID_TAG_RE = re.compile(r"<to_id>\s*([^<\s]+)\s*</to_id>")


def _ws_rel(p: str) -> str:
    """`p` as a repo-relative posix path when it lies inside WORKSPACE, else its absolute posix form -- so a to_ref
    written absolute, with backslashes or with `./` compares equal to the same file written plainly."""
    q = Path(str(p).strip())
    if not q.is_absolute():
        q = WORKSPACE / q
    try:
        return q.resolve().relative_to(WORKSPACE.resolve()).as_posix()
    except ValueError:
        return q.resolve().as_posix()


def _same_order_id(a: str, b: str) -> bool:
    """True when two TO ids name the same order: equal, or one is the other plus a `.`-delimited slug and the
    shorter carries `.TO` (the block above: 119 of 337 committed instances need the slug tolerance)."""
    if not a or not b:
        return False
    if a == b:
        return True
    short, long_ = (a, b) if len(a) < len(b) else (b, a)
    return ".TO" in short and long_.startswith(short + ".")


def _order_id_forms(rel: str, text: str) -> list:
    """The ids an order answers to: its <to_id> tag (first 8000 chars, where the header lives) and its filename stem."""
    forms = []
    m = _TO_ID_TAG_RE.search(text[:8000])
    if m:
        forms.append(_canonical_to_id(m.group(1)))
    name = rel.rsplit("/", 1)[-1]
    if name.endswith(".md"):
        forms.append(name[:-3])
    return [f for f in forms if f]


def governing_binding_check(inst: dict, bound_rel: str | None, bound_text: str | None = None) -> tuple[list, list]:
    """(violations, frames). The binding's cross-check, run by main() BEFORE any limb. `bound_text` is injectable so
    the self-test exercises it without a repo; left None it is read from WORKSPACE/bound_rel."""
    if bound_rel is None:
        return [], ["governing-binding: UNBOUND -- no --governing-order was given, so the governing order below is "
                    "resolved from the instance's OWN decomp_ref.to_ref (else its to_id), fields the graded party "
                    "writes. to-pipeline-gate.py's complete-flip path binds it to the order being flipped (FE-s-37); "
                    "this run's verdict is exactly what it was before the binding existed."]
    v: list = []
    if bound_text is None:
        try:
            bound_text = (WORKSPACE / bound_rel).read_text(encoding="utf-8", errors="replace")
        except Exception as exc:  # noqa: BLE001
            return ([f"governing-binding: the order being flipped, '{bound_rel}', cannot be read ({exc}) -- every "
                     f"limb is bound to it, so none can be graded; fail-closed"],
                    [f"governing-binding: BOUND to '{bound_rel}' (--governing-order) -- UNREADABLE"])
    dref = inst.get("decomp_ref")
    declared = str(dref.get("to_ref", "") or "").strip() if isinstance(dref, dict) else ""
    ref_state = "absent"
    if declared:
        drel = _ws_rel(declared)
        if drel == bound_rel:
            ref_state = "names it"
        else:
            ref_state = "names ANOTHER order"
            v.append(f"governing-binding: the order being flipped is '{bound_rel}' but the instance's "
                     f"decomp_ref.to_ref names '{drel}' -- REFUSED before any limb runs. The governing order is the "
                     f"order being closed, never a field the graded party writes (1.0.0_SA_CTO RULING S, row "
                     f"IRPT_FNTEND-S61); point to_ref at '{bound_rel}' or close the order it names.")
    cid = _canonical_to_id(str(inst.get("to_id", "") or ""))
    id_state = "absent"
    if cid:
        forms = _order_id_forms(bound_rel, bound_text)
        if any(_same_order_id(cid, f) for f in forms) or ('id="' + cid + '"') in bound_text[:8000]:
            id_state = "names it"
        else:
            id_state = "names ANOTHER order"
            others = sorted(t for t in _tracked_task_orders()
                            if t != bound_rel and _same_order_id(cid, t.rsplit("/", 1)[-1][:-3]))
            where = ("'%s'" % "', '".join(others[:3])) if others else "no tracked order whose filename carries it"
            v.append(f"governing-binding: the order being flipped is '{bound_rel}' (it answers to {forms}) but the "
                     f"instance's to_id is '{cid}', which names {where} -- REFUSED before any limb runs "
                     f"(1.0.0_SA_CTO RULING S, row IRPT_FNTEND-S61).")
    frames = [f"governing-binding: BOUND to '{bound_rel}' (--governing-order: the order being flipped) -- every limb "
              f"below reads THIS order; decomp_ref.to_ref {ref_state}; to_id {id_state}. The instance's own fields "
              f"are cross-checks, never the source."]
    return v, frames


def _resolve_governing_to(inst: dict) -> tuple[Path | None, str, int]:
    """(path, note, scanned). Resolution is CONTENT-based: a TO is the file that
    DECLARES id="<canonical>", never the file whose NAME looks right (Rule 22a -- a
    filename-resolved check reports drift where there is none and reads CLEAN where two
    copies have silently diverged). An explicit decomp_ref.to_ref wins when present --
    UNLESS the run is BOUND (--governing-order, FE-s-37): then the bound order is the
    answer and to_ref / to_id are never consulted here."""
    _dref = inst.get("decomp_ref", {})
    if not isinstance(_dref, dict):
        # SHAPE ERROR, NOT A VERDICT. decomp_ref must be the OBJECT form
        # ({doc, vintage_commit, to_ref}). A bare string used to reach .get() and raise
        # AttributeError, which exited rc=1 -- BYTE-IDENTICAL to a legitimate INVALID.
        # Surfaced by 0.6.0_AE_PartnerETL (71621), reproduced on a committed peer instance.
        raise TypeError(
            f"decomp_ref must be an OBJECT (doc/vintage_commit/to_ref), got {type(_dref).__name__}"
        )
    if _BOUND_ORDER is not None:
        # BOUND (FE-s-37). The order being flipped IS the governing order for every limb; governing_binding_check
        # (main, before any limb) has already cross-checked to_ref and to_id against it.
        rel = _ws_rel(str(_BOUND_ORDER))
        if not _BOUND_ORDER.is_file():
            return None, f"the bound governing order '{rel}' (--governing-order) does not resolve to a file", 0
        if not _is_tracked(rel):
            return None, (f"the bound governing order '{rel}' (--governing-order) resolves to an UNTRACKED file "
                          f"-- committed state is required to enforce against it"), 0
        return _BOUND_ORDER, "BOUND via --governing-order: the order being flipped", 0
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
    for f in list((WORKSPACE / "org").rglob("task_orders/*.md")) + list((WORKSPACE / "org" / "missions").rglob("task-orders/*.md")):  # R-ii: both roots
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
    present = blob is not None
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
        # DELIMITER-TOLERANT (2026-09-03, 3.0.0_SA_CVO~A 93412 -- NFRA_CLDGRPH-S5's class recurred within the hour:
        # cell_refs="CG-s-2 CG-s-9" parsed as ONE phantom id and blocked the completion flip). A cell id never carries
        # whitespace, so commas, semicolons and whitespace are all separators -- the same tolerance <owned_cells>
        # already gets above. The encoding convention stays commas; the parser stops making a space a defect.
        # Convention documented in org/standards/DECOMP_CELL_ID_CONVENTION.md; site Z hit the same class
        # on NFRA_OPSEC202609-Z-S11 ("OP-s-17 OP-s-16" read as one literal, blaming the DECOMP).
        refs = [c.strip() for c in re.split(r"[\s,;]+", attrs.get("cell_refs", "")) if c.strip()]
        crits[cid] = refs
        if not refs:
            no_refs.append(cid)
    exp = re.search(r"<expected_criteria>(.*?)</expected_criteria>", text, re.S)
    # (1a) CONTENT, NOT PRESENCE: a present element whose body declares NONE (and names no doc and
    # no cell id) is a declaration of NO decomposition -> ANNOUNCE. The doc wins over the word.
    body = re.sub(r"<owned_cells>.*?</owned_cells>|<decomp_doc>.*?</decomp_doc>", "", blob, flags=re.S) if present else ""
    declares_none = bool(present and DECOMP_REF_NONE_RE.match(body) and not doc and not declared)
    if present and DECOMP_REF_NONE_RE.match(body) and (doc or declared):
        branch_reason = (f"<decomp_ref> body opens with a NONE-word but names a decomp "
                         f"({doc or 'cell ids'}) -- the doc wins, ENFORCE")
    elif declares_none:
        branch_reason = f"<decomp_ref> body declares NO decomposition: '{body.strip()[:60]}'"
    elif present:
        branch_reason = f"<decomp_ref> names {doc or 'cell ids without a doc'}"
    else:
        branch_reason = "the governing TO carries NO <decomp_ref> element"
    return {
        "has_decomp_ref": present and not declares_none,
        "decomp_ref_present": present,
        "decomp_ref_declares_none": declares_none,
        "decomp_ref_branch_reason": branch_reason,
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
            f"alignment: ANNOUNCE -- {to['decomp_ref_branch_reason']}, so this is "
            "work completing under its own spec; decomp_ref is not required "
            "and this instance stays VALID on that basis (CTO ruling 66492; CONTENT-not-presence "
            "1.0.0_SA_CTO 87900). A TO whose <decomp_ref> NAMES a decomp is enforced here by "
            "construction.")
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
    frames.append(f"alignment: ENFORCE ({to['decomp_ref_branch_reason']})")

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


# ---------------------------------------------------------------------------
# SURPRISES LIMB (2026-09-03, 1.0.0_SA_CTO, Andrew-direct via 3.0.0_SA_CVO 92976). See the module docstring.
# The id grammar is surprise-row-gate.py's ID_RE, anchored at the start of the entry and followed by a
# boundary -- one carrier of the grammar would be better; until the two files share a module this is a
# COPY and is named as one (a change there is a change here).
# The allocator coordinate (RULING 2 @9ef9a40aae, annex v3.2): W<n> for a worker's row, C- for the CVO's, Z- nests first.
SURPRISE_ID_RE = re.compile(r"^\s*([A-Z0-9_]+-(?:Z-)?(?:W[0-9]+-|C-)?S[0-9]+)\b")
_TREE_TO_RE = re.compile(r"(^|/)org/missions/D(?:0|[1-9][0-9]?)/[^/]+/[^/]+/task-orders/[^/]+\.md$")
_FENCE_RE = re.compile(r"```json\s*(.*?)```", re.S)


def _channel_row_ids(code: str) -> tuple[set, int]:
    """(row ids, files scanned) across BOTH channel roots for one project. Reads the WORKTREE (this
    checker runs at completion, not at commit; the row gate is the staged-index reader). A fenced
    block that does not parse is skipped and counted in the scan -- absence of an id is what the
    caller grades, and a malformed channel file is the row gate's finding, not this limb's."""
    if not code:
        return set(), 0
    files = list(WORKSPACE.glob("org/surprise_channel/%s/INVESTIGATION_v*" % code))
    files += list(WORKSPACE.glob("org/missions/D*/*/%s/surprise-channel/investigations/INVESTIGATION_v*" % code))
    ids: set = set()
    for f in files:
        try:
            text = f.read_text(encoding="utf-8", errors="replace")
        except Exception:  # noqa: BLE001
            continue
        blocks = [text] if f.suffix.lower() == ".json" else _FENCE_RE.findall(text)
        for b in blocks:
            try:
                val = json.loads(b)
            except Exception:  # noqa: BLE001
                continue
            rows = val if isinstance(val, list) else [val]
            for r in rows:
                if isinstance(r, dict) and isinstance(r.get("id"), str):
                    ids.add(r["id"])
    return ids, len(files)


def _governing_is_tree(inst: dict) -> tuple[bool, str]:
    """(enforce, reason). ENFORCE iff the governing TO resolves under the tree root."""
    try:
        to_path, note, _scanned = _resolve_governing_to(inst)
    except Exception as exc:  # noqa: BLE001
        return False, "governing TO could not be resolved (%s)" % exc
    if to_path is None:
        return False, "governing TO unresolved -- " + note
    rel = str(to_path).replace("\\", "/")
    try:
        rel = str(Path(to_path).resolve().relative_to(WORKSPACE.resolve())).replace("\\", "/")
    except Exception:  # noqa: BLE001
        pass
    if _TREE_TO_RE.search(rel):
        return True, "governing TO is under the TREE root (%s)" % rel
    return False, "governing TO is under the FLAT root (%s) -- legacy, announce only" % rel


def surprises_check(inst: dict, enforce: bool | None = None, row_ids: set | None = None,
                    files_scanned: int | None = None) -> tuple[list[str], list[str]]:
    """(violations, frames). Every entry of `surprises` must open with a row id that resolves to a row
    in the project's channel. ENFORCE -> violations; ANNOUNCE -> frame lines only. `enforce`,
    `row_ids` and `files_scanned` are injectable so the self-test exercises the limb without a repo."""
    v: list[str] = []
    frames: list[str] = []
    entries = inst.get("surprises", []) or []
    if not isinstance(entries, list):
        return v, ["surprises-frame: `surprises` is not a list -- the schema owns that complaint"]
    if enforce is None:
        enforce, reason = _governing_is_tree(inst)
    else:
        reason = "mode injected by caller"
    code = _project_code(str(inst.get("to_id", "")))
    if row_ids is None:
        row_ids, files_scanned = _channel_row_ids(code)
    files_scanned = 0 if files_scanned is None else files_scanned
    defects: list[str] = []
    n_with_id = n_resolved = 0
    for i, e in enumerate(entries):
        s = e if isinstance(e, str) else json.dumps(e)
        m = SURPRISE_ID_RE.match(s)
        if not m:
            defects.append("surprises[%d] carries NO row id -- a surprise that is not a row in the project's "
                           "channel does not exist (Andrew-direct 2026-09-03); open the entry with '<PROJECT>-S<n>: '"
                           % i)
            continue
        n_with_id += 1
        rid = m.group(1)
        if rid in row_ids:
            n_resolved += 1
        else:
            defects.append("surprises[%d] names row id %s which resolves to NO row in %s's channel "
                           "(%d INVESTIGATION file(s) scanned on both roots) -- the row must be committed "
                           "before the instance cites it" % (i, rid, code or "<unparsed project>", files_scanned))
    frames.append("surprises-frame: %d entr%s; %d open with a row id; %d resolve to a channel row; %d channel "
                  "file(s) scanned (flat+tree) for %s; mode %s -- %s"
                  % (len(entries), "y" if len(entries) == 1 else "ies", n_with_id, n_resolved, files_scanned,
                     code or "<unparsed project>", "ENFORCE" if enforce else "ANNOUNCE", reason))
    if enforce:
        v.extend(defects)
    else:
        frames.extend("surprises-announce (would REFUSE under a tree TO): " + d for d in defects)
    return v, frames


# ---------------------------------------------------------------------------
# INVOCATION ALIGNMENT LIMB (2026-09-12, 0.9.0_WK_IRPT_FNTEND~3 on IRPT_FNTEND.TO-FE-s-23,
# decomp cell FE-s-23, channel row IRPT_FNTEND-S31).
#
# THE CLASS. The spine has the ISSUER substitute <WS>/<PORT> into the worker face at spawn,
# so an issuer is ALWAYS editing the criterion string on the way out. Once you are editing
# it, nothing stops a SUBSTANTIVE correction going only there. MEASURED: on IRPT_FNTEND round 2
# an issuer corrected two print-route URLs in the SPAWN PROMPT and never in the task-order FILE;
# the worker ran the corrected URLs, recorded them faithfully, and THIS CHECKER returned
# VALID (rc=0) over 20 rows with 0 violations -- because nothing here compared a RECORDED
# invocation against the text of the criterion it claims to satisfy. The prompt is gone the
# moment the worker ends; the RECORD is what the CVO grades and every successor reads.
#
# WHAT IS COMPARED, AND WHAT IS NOT NORMALISED AWAY. Per row: the instance's `invocation`
# against the same-id criterion's <invocation> in the governing TO. Normalisation is EXACTLY
# TWO THINGS -- placeholder expansion, and whitespace at the ENDS of the string. A difference
# in a flag, a path, a query parameter or a quoted argument is NOT normalised away; those are
# the four shapes the seeded battery refuses (.tools/tests/test_invocation_limb.py).
# A repeated placeholder is a BACKREFERENCE: <WS> twice in one invocation must expand to the
# SAME value, so two different workspaces in one command cannot pass as one substitution.
#
# BLOCKED: ENFORCE IS OPT-IN, VIA A DECLARATION IN THE GOVERNING TO, AND THAT IS NOT A SOFTENING --
# IT IS THE ONLY BRANCH THE MEASUREMENT ALLOWS. The corpus was read UNSCOPED before this limb
# was written: 294 committed instances, 275 with a governing TO under the tree root, 1481
# acceptance rows, 874 of them comparable -- and 318 of those 874 DIVERGE under the rule above.
# The dominant shapes are honest ones (a worker adding the `timeout 120` bound the order's
# BOUNDS section demanded but its <invocation> omitted; a record eliding a long path to
# `.../x.txt`). Refusing by default would retro-INVALIDATE work across every project in the
# estate and refuse in-flight completion flips in projects this cell does not own. So the
# discriminator is a DECLARATION the TO makes: <placeholders>WS, PORT</placeholders>. Present
# -> the substitution set is KNOWN, comparison is exact modulo exactly those tokens, and a
# mismatch is a VIOLATION. Absent -> the set is a GUESS (the <UPPER> heuristic), and a guess
# must not refuse: the divergence is PRINTED with both strings on every run and refuses nothing.
# Same shape as <owned_cells> (CTO 66893): an opt-in delimiter that turns an announce into an
# assertion, because the undelimited form cannot tell a claim from a read-dependency.
# Census before choosing the token: 0 of 2554 task-order files carry <placeholders> today, so
# nothing in the estate is retro-enforced by construction.
# WARN: NAMED WEAKNESS, not hidden: the opt-in is written by the ISSUER, and the issuer is the
# party whose prompt-only correction this limb exists to catch. The ANNOUNCE branch is what
# covers the un-opted case -- it prints both strings for the CVO at L8/L9 -- and making the
# declaration MANDATORY at the L6 gate is a different cell's business, deliberately not done here.
CRITERION_SELFCLOSE_RE = re.compile(r"<criterion\b([^>]*?)/>", re.S)
# The paired form must not swallow a self-closing tag: `[^>]*?` alone matches up to the `/`
# of `... />` and then `(.*?)</criterion>` runs on to the NEXT criterion's closing tag,
# attributing that criterion's invocation to the self-closed id. Measured on
# IRPT_FNTEND.TO-FE-s-15: F15-AC12 (self-closing, judgment) took F15-AC13's invocation.
CRITERION_BLOCK_RE = re.compile(r"<criterion\b((?:(?!/>)[^>])*?)>(.*?)</criterion>", re.S)
INVOCATION_TAG_RE = re.compile(r"<invocation>(.*?)</invocation>", re.S)
# LINE-ANCHORED (2026-09-13, FE-s-29 limb 1; 1.0.0_SA_CTO RULING M(i) @23af9479ab; rows S53, W4-S7).
# The element is the <placeholders> tag STANDING ON ITS OWN LINE, open and close on that one line.
# The unanchored `<placeholders>(.*?)</placeholders>` under re.S took the FIRST open tag in the file,
# and every order that EXPLAINS the rule mentions the tag in prose before declaring it -- so the span
# ran from the prose mention to the real element's close and harvested every word between (367 names
# for a 1-token declaration on FE-s-28's own face, W4-S7). S53 measured the two consequences by calling
# the gate's own function on real bytes: (C) an invocation token the element does NOT declare was
# admitted because the criteria sat inside the span, and (D) an order with NO element was admitted
# because its prose quoted the gate's own help text. Anchored, both refuse, and the two orders that
# declared at the time (FE-s-23, FE-s-28) are still read -- every declaring order in the estate writes
# the element on one line. .tools/tests/test_placeholders_reader.py holds the five cases.
# BYTE-IDENTICAL to .tools/to-pipeline-gate.py's PLACEHOLDERS_TAG_RE, and both batteries compare them:
# a gate reading a looser pattern than this checker would admit an order that arms nothing here.
PLACEHOLDERS_TAG_RE = re.compile(r"^[ \t]*<placeholders>(.*?)</placeholders>[ \t]*$", re.M)
PLACEHOLDER_TOKEN_RE = re.compile(r"<([A-Z][A-Z0-9_]*)>")


def _to_invocations(text: str) -> dict:
    """{criterion_id: invocation string or None}. None = the criterion carries no
    <invocation> (a judgment criterion, or a prose-only clause) and is NOT comparable."""
    out: dict = {}
    for m in CRITERION_SELFCLOSE_RE.finditer(text):
        cid = dict(ATTR_RE.findall(m.group(1))).get("id", "").strip()
        if cid:
            out.setdefault(cid, None)
    for m in CRITERION_BLOCK_RE.finditer(text):
        cid = dict(ATTR_RE.findall(m.group(1))).get("id", "").strip()
        if not cid:
            continue
        i = INVOCATION_TAG_RE.search(m.group(2))
        out[cid] = i.group(1).strip() if i else None
    return out


def _declared_placeholders(text: str):
    """The TO's declared substitution set, or None when it declares none.

    None and set() are DIFFERENT: None = undeclared = ANNOUNCE; an empty/NONE declaration =
    ENFORCE with no token expanded at all (a TO whose invocations are literal)."""
    m = PLACEHOLDERS_TAG_RE.search(text)
    if m is None:
        return None
    names = {n.upper() for n in re.findall(r"[A-Za-z][A-Za-z0-9_]*", m.group(1))}
    names.discard("NONE")
    return names


def _invocation_pattern(to_inv: str, names) -> str:
    """The criterion's invocation as a regex: literal everywhere, `(\\S+)` at each occurrence
    of a placeholder in `names`, and a BACKREFERENCE at every repeat of the same placeholder.
    `\\S+` cannot cross whitespace or a newline, so an expansion can never swallow an added
    flag, an added argument or an appended query parameter -- the literal tail would then have
    nothing to match and the row diverges, which is the whole point."""
    pat, last, seen = "", 0, {}
    for m in PLACEHOLDER_TOKEN_RE.finditer(to_inv):
        if m.group(1) not in names:
            continue
        pat += re.escape(to_inv[last:m.start()])
        if m.group(1) in seen:
            pat += "\\%d" % seen[m.group(1)]
        else:
            seen[m.group(1)] = len(seen) + 1
            pat += r"(\S+)"
        last = m.end()
    return pat + re.escape(to_inv[last:])


def invocation_alignment_check(inst: dict, to_text: str | None = None,
                               to_label: str | None = None) -> tuple[list, list]:
    """(violations, frames). `to_text`/`to_label` are injectable so the battery exercises the
    limb without planting a task order in the live estate."""
    v: list[str] = []
    frames: list[str] = []
    if to_text is None:
        try:
            to_path, note, _scanned = _resolve_governing_to(inst)
        except Exception as exc:  # noqa: BLE001 -- a shape error is layer 1's complaint, not this limb's
            return v, ["invocation-frame: NOT EVALUATED -- governing TO could not be resolved (%s)" % exc]
        if to_path is None:
            return v, ["invocation-frame: NOT EVALUATED -- governing TO unresolved: %s. A recorded "
                       "invocation can only be compared against a criterion that resolves." % note]
        to_text = to_path.read_text(encoding="utf-8", errors="replace")
        to_label = str(to_path.relative_to(WORKSPACE)).replace("\\", "/")
    to_inv = _to_invocations(to_text)
    declared = _declared_placeholders(to_text)
    enforce = declared is not None
    rows = inst.get("acceptance", []) or []
    n_cmp = n_ok = n_nocrit = n_noinv = 0
    defects: list[str] = []
    for r in rows:
        if not isinstance(r, dict):
            continue
        rid = str(r.get("criterion_id", "") or "").strip()
        rec = str(r.get("invocation", "") or "").strip()
        if rid not in to_inv:
            n_nocrit += 1          # coverage_check owns "this id is not in the TO"
            continue
        if to_inv[rid] is None or not rec:
            n_noinv += 1           # judgment / prose criterion: nothing to compare against
            continue
        n_cmp += 1
        spec = to_inv[rid]
        names = declared if enforce else {
            t for t in PLACEHOLDER_TOKEN_RE.findall(spec)}
        try:
            ok = re.fullmatch(_invocation_pattern(spec, names), rec, re.S) is not None
        except re.error:  # noqa: PERF203 -- an unbuildable pattern is announced, never a silent pass
            ok = False
        if ok:
            n_ok += 1
            continue
        defects.append(
            "invocation-alignment[%s]: the RECORDED invocation is NOT the criterion's invocation "
            "modulo the placeholder(s) %s.\n      TO-CRITERION: %s\n      INSTANCE-RECORD: %s\n"
            "      -- a correction that reaches the spawn prompt and never the task-order FILE "
            "leaves the record ungoverned; the prompt is gone, the record is what the CVO grades "
            "(IRPT_FNTEND-S31)" % (rid, sorted(names) or "<none>", spec, rec))
    frames.append(
        "invocation-frame: governing TO=%s; placeholders %s"
        % (to_label or "<injected>",
           ("DECLARED %s -> ENFORCE" % (sorted(declared) or "<none>")) if enforce
           else "UNDECLARED -> ANNOUNCE (the <UPPER> heuristic is a guess, and a guess must not "
                "refuse; declare <placeholders>WS, PORT</placeholders> in the TO to enforce)"))
    frames.append(
        "invocation-alignment (recorded invocation -> criterion text): %d/%d comparable row(s) "
        "match modulo placeholder expansion; %d diverge. NOT COMPARABLE: %d row(s) name no "
        "criterion in the TO (coverage_check owns that), %d row(s) whose criterion carries no "
        "<invocation> (judgment/prose). Rows in instance: %d."
        % (n_ok, n_cmp, len(defects), n_nocrit, n_noinv, len(rows)))
    if enforce:
        v.extend(defects)
    else:
        frames.extend("invocation-announce (would REFUSE under a TO declaring <placeholders>): "
                      + d for d in defects)
    return v, frames


# ---------------------------------------------------------------------------
# THE PROSPECTIVE BOUNDARY SHARED BY THE COUNT-BAR LIMB AND THE DRIVES LIMB (2026-09-13,
# 0.9.0_WK_IRPT_FNTEND~4 on IRPT_FNTEND.TO-FE-s-29, decomp cell FE-s-29).
#
# NEW vs LEGACY IS DERIVED FROM REPOSITORY STATE -- never a clock, never a list of instances, never a
# declaration the graded party writes. An instance is NEW when its GOVERNING ORDER was first ADDED in a
# commit that DESCENDS FROM the commit that recorded the ruling the limb enforces, and LEGACY when that
# add commit does not. An order's add commit is fixed the moment the issuance lands, so neither the
# issuer (by omitting a declaration -- 1.0.0_SA_CTO's condition on the drives limb) nor the worker (by
# anything written in the instance) can move an order across the line. The ruling pins are
# CONTENT-CHECKED by the batteries (the document at the pin carries the ruling's own words), so each is
# an authority citation, not an operator marker.
# NON-APPLICATION, stated so a quiet frame is not read as a verdict: a governing order that does not
# resolve, an add commit git cannot name, or a ruling pin absent from this object store (a cross-fabric
# reader before a fetch) leaves the boundary UNREAD, and the limb ANNOUNCES and says so in its frame.
RULING_DOC = "org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_ANALYSIS_IRPT_FNTEND_ROUND4_20260913.md"
COUNT_BAR_RULING = "23af9479ab"          # RULING M(ii): first landed with the round-4 analysis
DRIVES_RULING = {"IRPT_FNTEND": "4f6c7abc7b"}  # RULING Q + the CTO's condition: drives= is MANDATORY
_GOV_CACHE: dict = {}


def _git_rc(*args: str) -> int:
    try:
        return subprocess.run(["git", *args], cwd=str(_REPO_ROOT), capture_output=True, timeout=60).returncode
    except Exception:  # noqa: BLE001 -- a git that cannot run leaves the boundary UNREAD, never a pass
        return -1


def _governing_rel(inst: dict):
    """(repo-relative path of the governing order or None, note). Memoised per (to_ref, to_id): the
    resolution scans every tracked task order and both limbs below need it."""
    dref = inst.get("decomp_ref")
    key = (json.dumps(dref, sort_keys=True, default=str), str(inst.get("to_id", "")))
    if key not in _GOV_CACHE:
        try:
            p, note, _scanned = _resolve_governing_to(inst)
        except Exception as exc:  # noqa: BLE001 -- a shape error is layer 1's complaint
            p, note = None, "governing TO could not be resolved (%s)" % exc
        rel = None
        if p is not None:
            try:
                rel = p.resolve().relative_to(WORKSPACE.resolve()).as_posix()
            except ValueError:
                rel = str(p).replace("\\", "/")
        _GOV_CACHE[key] = (rel, note)
    return _GOV_CACHE[key]


_ADD_COMMIT_CACHE: dict = {}


def _order_add_commit(rel: str):
    """The EARLIEST commit that added `rel`, or None. --full-history, because `git log -- <path>`
    simplifies history and can drop the very commit that introduced a file on a merged side branch.
    Memoised per path: both limbs ask it about the same order on every run."""
    if rel not in _ADD_COMMIT_CACHE:
        _ADD_COMMIT_CACHE[rel] = _order_add_commit_uncached(rel)
    return _ADD_COMMIT_CACHE[rel]


def _order_add_commit_uncached(rel: str):
    try:
        out = subprocess.run(["git", "log", "--full-history", "--diff-filter=A", "--format=%H", "--", rel],
                             cwd=str(_REPO_ROOT), capture_output=True, text=True, encoding="utf-8",
                             errors="replace", timeout=60)
    except Exception:  # noqa: BLE001
        return None
    if out.returncode != 0:
        return None
    lines = [ln.strip() for ln in out.stdout.splitlines() if ln.strip()]
    return lines[-1] if lines else None


def _cut_after(rel, ruling: str):
    """(True | False | None, reason). True: `rel` was first added in a commit that descends from
    `ruling` (NEW). False: it was not (LEGACY). None: the boundary could not be read (ANNOUNCE)."""
    if not rel:
        return None, "the governing order did not resolve, so the boundary is UNREAD"
    add = _order_add_commit(rel)
    if not add:
        return None, "no add commit is readable for %s, so the boundary is UNREAD" % rel
    if _git_rc("cat-file", "-e", ruling + "^{commit}") != 0:
        return None, ("the ruling pin %s is not in this object store (a cross-fabric reader before a fetch?), "
                      "so the boundary is UNREAD" % ruling)
    rc = _git_rc("merge-base", "--is-ancestor", ruling, add)
    if rc == 0:
        return True, "%s was added at %s, which DESCENDS from the ruling @%s -> NEW" % (rel, add[:10], ruling)
    if rc == 1:
        return False, ("%s was added at %s, which does NOT descend from the ruling @%s -> LEGACY"
                       % (rel, add[:10], ruling))
    return None, "git merge-base returned rc=%d, so the boundary is UNREAD" % rc


# ---------------------------------------------------------------------------
# COUNT-BAR LIMB (2026-09-13, FE-s-29 limb 2; 1.0.0_SA_CTO RULING M(ii) @23af9479ab; row IRPT_FNTEND-S56).
#
# THE CLASS. conditional_checks() decides a mechanical criterion with an UNANCHORED re.search of the
# bar over the evidence and raises nothing when it matches. So a `0 fail` bar PASSES ` 10 fail`
# (shape a -- the 0 of 10) and PASSES any evidence that ALSO carries a contradicting count (shape b --
# F17-AC8's committed evidence holds its deciding ` 0 fail` AND a BEFORE note's ` 1 fail`). No false
# PASS has happened; what kept the estate clean was diligence, which is not a control.
# THE RULE. For a PASS row whose bar asserts ZERO of a noun (`0 fail`, `0 arm\(s\) failed`, `0 errors`)
# and whose bar DOES match its evidence, the evidence may carry no NONZERO count of that noun.
# REFUSE for a NEW instance, ANNOUNCE for a LEGACY one (the boundary above).
# ANCHORING. A count in the evidence is left-anchored with (?<![0-9.A-Za-z_]) and NEVER with \b -- a \b anchor
# false-fails `\x1b[1m4 passed`, because the ANSI code puts a word character before the count (1.0.0_SA_CTO
# 96370, tested with the grader's own call). A digit directly after a letter or underscore ENDS an identifier
# (`F47-AC2 PROBLEMS` is criterion F47-AC2's label, not 2 problems -- row IRPT_FNTEND-W3-S41, 1.0.0_SA_CTO
# round-8 analysis). ANSI escapes are replaced by a SPACE before counting, never removed: removal would glue a
# real count to the word before it (`pass\x1b[0m4 fail` -> `pass4 fail`), and the identifier rule would then hide
# it. A count preceded by `of ` is a DENOMINATOR (`0 of 487 fail`), not a count of the noun.
# NON-APPLICATION: a bar with no zero-count noun; a bar that does NOT match its evidence (conditional_checks
# already refuses that PASS); key=value bars (`rc=0`, `LEAKS: 0`) -- the ruling names count nouns, and a
# `rc=0` bar beside an honest `rc=1` inside a test's own printed arms would be refused for the wrong reason.
_ANSI_RE = re.compile(r"\x1b\[[0-9;?]*[A-Za-z]|\[(?:[0-9]{1,3};)*[0-9]{1,3}m")
_BAR_ZERO_RE = re.compile(r"(?<![0-9.\\\[{,|])0(?:[ \t]+|\\s[+*]?|\\t|\[ \\t\][+*]?)+([A-Za-z][A-Za-z_]*)")
_NOUN_STOP = frozenset(("of", "on", "in", "at", "to", "and", "or", "each", "the", "a", "an", "is", "are", "was",
                        "for", "with", "from", "by", "as", "if", "via", "per", "post", "pre", "exit", "exits"))


def _zero_count_nouns(expect: str) -> list:
    """The nouns a bar asserts ZERO of, read from the bar's own text, lower-cased and de-pluralised."""
    out: list = []
    for m in _BAR_ZERO_RE.finditer(expect or ""):
        noun = m.group(1).lower()
        if noun in _NOUN_STOP:
            continue
        stem = noun[:-1] if len(noun) > 3 and noun.endswith("s") and not noun.endswith("ss") else noun
        if stem not in out:
            out.append(stem)
    return out


def _nonzero_counts(evidence: str, stem: str) -> list:
    """Every NONZERO count of `stem` in the ANSI-stripped evidence, as the printed fragment."""
    clean = _ANSI_RE.sub(" ", evidence or "")
    pat = re.compile(r"(?<![0-9.A-Za-z_])(?<!of )([0-9]+)[ \t]+" + re.escape(stem) + r"[A-Za-z_()]*", re.I)
    return [m.group(0) for m in pat.finditer(clean) if int(m.group(1)) != 0]


def count_bar_check(inst: dict, enforce: bool | None = None) -> tuple[list, list]:
    """(violations, frames). `enforce` is injectable so the self-test exercises the limb without a repo."""
    v: list = []
    frames: list = []
    if enforce is None:
        rel, note = _governing_rel(inst)
        new, reason = _cut_after(rel, COUNT_BAR_RULING)
        if rel is None:
            reason = "%s (%s)" % (reason, note)
        enforce = new is True
    else:
        reason = "mode injected by caller"
    n_bar = n_bad = 0
    defects: list = []
    for r in inst.get("acceptance", []) or []:
        if not isinstance(r, dict) or r.get("status") != "PASS":
            continue
        exp = r.get("expect")
        if not isinstance(exp, str) or not exp.strip():
            continue
        nouns = _zero_count_nouns(exp)
        if not nouns:
            continue
        ev = r.get("output_evidence", "") or ""
        try:
            matched = re.search(exp, ev, re.S | re.M) is not None
        except re.error:
            continue  # conditional_checks owns an unevaluable bar
        if not matched:
            continue  # conditional_checks owns a PASS whose bar does not match
        n_bar += 1
        hits = [(s, frag) for s in nouns for frag in _nonzero_counts(ev, s)]
        if not hits:
            continue
        n_bad += 1
        rid = str(r.get("criterion_id", "?"))
        defects.append(
            "count-bar[%s]: the bar %r asserts ZERO of %s and its own search DOES match the evidence -- but the "
            "evidence also carries a NONZERO count for that noun: %s. A PASS decided by a substring of a "
            "contradicting summary is not a PASS (row S56: shape a, ' 10 fail' contains '0 fail'; shape b, a "
            "deciding ' 0 fail' beside a BEFORE note's ' 1 fail'). Evidence hygiene: output_evidence carries the "
            "deciding run only; earlier runs go in status_reason (RULING M(ii) @%s)."
            % (rid, exp, ", ".join(repr(n) for n in nouns),
               "; ".join(repr(f.strip()) for _, f in hits[:4]), COUNT_BAR_RULING))
    frames.append("count-bar-frame: %d PASS row(s) carry a zero-count bar that matches its evidence; %d of them "
                  "carry a contradicting NONZERO count; mode %s -- %s"
                  % (n_bar, n_bad, "ENFORCE" if enforce else "ANNOUNCE", reason))
    if enforce:
        v.extend(defects)
    else:
        frames.extend("count-bar-announce (would REFUSE for an order cut after RULING M(ii) @%s): %s"
                      % (COUNT_BAR_RULING, d) for d in defects)
    return v, frames


# ---------------------------------------------------------------------------
# DRIVES LIMB -- THE SEEDED-CRITERION LIMB (2026-09-13, FE-s-29 limb 3; 1.0.0_SA_CTO RULING Q and its
# condition @4f6c7abc7b; rows S42 (substrate half), C-S67).
#
# THE CLASS. This portal has no DOM test environment (C-S67: package.json names neither happy-dom nor
# jsdom; bunfig.toml absent), so under renderToStaticMarkup a body that MOUNTED from the network and a
# body SEEDED through a component's `initial*` props render identically. A seeded criterion and a
# browser-driven one both invoke `bun test <file>` -- ONLY THE INVOKED TEST FILE'S CONTENT tells them
# apart, which is why this limb lives in the checker and reads that file.
# THE RULE (the CTO's condition, binding): every criterion of a NEW IRPT_FNTEND order declares
# drives="network" or drives="none" on its criterion element; a new instance whose governing order has a
# criterion declaring NEITHER (or any other value) is REFUSED; legacy instances ANNOUNCE. For a
# drives="network" criterion, a PASS whose invoked test (or a __tests__ helper it imports) passes a seeding
# prop is REFUSED. An explicit drives="none" is enforcement, not a waiver -- it satisfies the declaration
# and claims nothing about the network, so it is not read for seeding.
# THE SEEDING PROPS, BY SUBTRACTION FROM A MEASURED DENOMINATOR: the IR components declare 15 `initial*`
# props (portal src/pages/InvestorReporting at 2026-09-13: TabShell, ReportingTab, HoldingsTab,
# AnalysisTab, GenerateComposer, Preview). MINUS the 5 that seed UI STATE rather than fetched content
# (initialTab, initialPeriod, initialPhase, initialComparisonKeys, initialVariantChoice) = the 10 below.
# The ruling names three (the first three); the other seven seed the same fetched bodies by another name,
# and a limb that saw only the three could be satisfied by the party it grades.
# WHERE THE FILE IS READ, and its vintage printed: the directory the RECORDED invocation `cd`s into (the
# bytes that ran), else <this tree>/<suffix of the order's cd <WS>/...>, else the main worktree's.
# A drives="network" PASS whose invoked test cannot be read is REFUSED under ENFORCE: the limb cannot
# establish the criterion does not pass by seeding, and admitting what it cannot read is the direction
# this ruling exists to close. Run the checker where the invocation's portal worktree exists.
# NAMED WEAKNESSES: a seeding helper placed OUTSIDE a __tests__ directory is not followed (the component
# sources declare the same props, so following every relative import would refuse every test); an
# invocation that runs no `bun test` is counted and not read. L9 grades both by judgment.
SEED_PROPS_RULED = ("initialEnvelope", "initialHoldingsEnvelope", "initialReport")
SEED_PROPS_MEASURED = ("initialSnapshot", "initialHoldingsSnapshot", "initialSnapshotEnvelope",
                       "initialAnalysisReport", "initialAnalysisRequests", "initialRequests", "initialJob")
SEED_PROPS = SEED_PROPS_RULED + SEED_PROPS_MEASURED
_SEED_RE = re.compile(r"\b(" + "|".join(SEED_PROPS) + r")\b")
DRIVES_VALUES = ("network", "none")
_SHELL_SPLIT_RE = re.compile(r"&&|\|\||;|\|")
_BUN_VALUE_FLAGS = frozenset(("-t", "--test-name-pattern", "--timeout", "--preload", "--rerun-each",
                              "--coverage-reporter", "--coverage-dir", "--reporter", "--reporter-outfile",
                              "--max-concurrency", "--seed", "--path-ignore-patterns"))
_TEST_FILE_RE = re.compile(r"[._](?:test|spec)\.[cm]?[jt]sx?$")
_PRUNE_DIRS = frozenset(("node_modules", ".git", "dist", "build", "coverage", ".scratch", ".worktrees"))
_JS_LEX_RE = re.compile(r"""("(?:\\.|[^"\\\n])*"|'(?:\\.|[^'\\\n])*'|`(?:\\.|[^`\\])*`)|(/\*.*?\*/|//[^\n]*)""", re.S)
_IMPORT_RE = re.compile(r"""(?:\bfrom\s*|\bimport\s*\(\s*|\brequire\s*\(\s*|\bimport\s+)['"](\.{1,2}/[^'"]+)['"]""")
_IMPORT_EXTS = ("", ".ts", ".tsx", ".mts", ".js", ".jsx", ".mjs", ".cjs")


def _strip_js_comments(text: str) -> str:
    """Comments removed, strings kept, line count preserved -- a prop named in a COMMENT is not a seed."""
    return _JS_LEX_RE.sub(lambda m: m.group(1) if m.group(1) is not None else "\n" * m.group(2).count("\n"), text)


def _criteria_attrs(text: str) -> dict:
    """{criterion_id: attributes} for every criterion element (paired and self-closing) in a TO."""
    out: dict = {}
    for m in CRITERION_SELFCLOSE_RE.finditer(text):
        attrs = dict(ATTR_RE.findall(m.group(1)))
        if attrs.get("id", "").strip():
            out.setdefault(attrs["id"].strip(), attrs)
    for m in CRITERION_BLOCK_RE.finditer(text):
        attrs = dict(ATTR_RE.findall(m.group(1)))
        if attrs.get("id", "").strip():
            out[attrs["id"].strip()] = attrs
    return out


def _bun_test_call(inv: str | None):
    """(cd token or None, [target args]) for the `bun test` call in `inv`, or None if it runs none."""
    if not inv:
        return None
    import shlex
    cwd = None
    for seg in _SHELL_SPLIT_RE.split(inv):
        try:
            toks = shlex.split(seg, posix=True)
        except ValueError:
            toks = seg.split()
        if not toks:
            continue
        if toks[0] == "cd" and len(toks) > 1:
            cwd = toks[1]
            continue
        for j in range(len(toks) - 1):
            if re.split(r"[\\/]", toks[j])[-1].lower() in ("bun", "bun.exe") and toks[j + 1] == "test":
                args, skip = [], False
                for a in toks[j + 2:]:
                    if skip:
                        skip = False
                        continue
                    if a.startswith("("):
                        break              # a recorded invocation's trailing prose, never a target
                    if a.startswith("-"):
                        skip = a in _BUN_VALUE_FLAGS
                        continue
                    if not re.fullmatch(r"[\w.@/~<>-]+", a):
                        break
                    args.append(a)
                return cwd, args
    return None


def _native_path(p: str) -> Path:
    """An MSYS `/c/...` path as recorded by a Git Bash worker, as this process can open it."""
    if os.name == "nt":
        m = re.match(r"^/(?:cygdrive/)?([A-Za-z])(/.*)?$", p)
        if m:
            return Path("%s:%s" % (m.group(1).upper(), m.group(2) or "/"))
    return Path(p)


def _main_worktree():
    try:
        out = subprocess.run(["git", "rev-parse", "--path-format=absolute", "--git-common-dir"],
                             cwd=str(_REPO_ROOT), capture_output=True, text=True, timeout=30)
    except Exception:  # noqa: BLE001
        return None
    p = Path(out.stdout.strip()) if out.returncode == 0 and out.stdout.strip() else None
    return p.parent if p is not None and p.name == ".git" else None


def _cwd_candidates(spec_cd, rec_cd) -> list:
    """[(label, dir)] in the order the invoked test is looked for."""
    c: list = []
    if rec_cd and "<" not in rec_cd:
        c.append(("recorded cd", _native_path(rec_cd)))
    roots = [("this tree", _REPO_ROOT)]
    mw = _main_worktree()
    if mw is not None and mw.resolve() != _REPO_ROOT.resolve():
        roots.append(("main worktree", mw))
    if spec_cd and "<WS>" in spec_cd:
        suffix = spec_cd.split("<WS>", 1)[1].lstrip("/\\")
        c.extend((lbl, (r / suffix) if suffix else r) for lbl, r in roots)
    elif spec_cd and "<" not in spec_cd:
        sp = _native_path(spec_cd)
        c.extend([("order cd", sp)] if sp.is_absolute() else [(lbl, r / spec_cd) for lbl, r in roots])
    elif not spec_cd:
        c.extend(roots)
    seen, out = set(), []
    for lbl, d in c:
        k = str(d).lower()
        if k not in seen:
            seen.add(k)
            out.append((lbl, d))
    return out


def _walk_tests(base: Path):
    for dp, dn, fn in os.walk(str(base)):
        dn[:] = [d for d in dn if d not in _PRUNE_DIRS]
        for f in fn:
            if _TEST_FILE_RE.search(f):
                yield Path(dp) / f


def _match_targets(cwd: Path, targets: list) -> list:
    """The test files `bun test <targets>` runs from `cwd`: an existing file, every test under an existing
    directory, else every test whose path CONTAINS the argument (bun's filter). No target = every test."""
    if not cwd.is_dir():
        return []
    if not targets:
        return sorted(_walk_tests(cwd))
    out: set = set()
    everything = None
    for t in targets:
        if "<" in t:
            return []                      # an unexpanded placeholder cannot be resolved to a file
        p = cwd / t
        if p.is_file():
            out.add(p)
        elif p.is_dir():
            out.update(_walk_tests(p))
        else:
            if everything is None:
                everything = [(f, f.relative_to(cwd).as_posix()) for f in _walk_tests(cwd)]
            key = t[2:] if t.startswith("./") else t
            out.update(f for f, rel in everything if key in rel)
    return sorted(out)


def _helper_closure(files: list) -> list:
    """Every file under a __tests__ directory reachable from `files` by RELATIVE import, transitively."""
    seen = {f.resolve() for f in files}
    queue, helpers = list(seen), []
    while queue and len(seen) < 400:
        f = queue.pop()
        try:
            code = _strip_js_comments(f.read_text(encoding="utf-8", errors="replace"))
        except Exception:  # noqa: BLE001
            continue
        for m in _IMPORT_RE.finditer(code):
            base = f.parent / m.group(1)
            hit = next((Path(str(base) + e) for e in _IMPORT_EXTS if Path(str(base) + e).is_file()), None)
            if hit is None:
                hit = next((base / ("index" + e) for e in _IMPORT_EXTS[1:] if (base / ("index" + e)).is_file()), None)
            if hit is None:
                continue
            hit = hit.resolve()
            if hit not in seen and "__tests__" in hit.parts:
                seen.add(hit)
                queue.append(hit)
                helpers.append(hit)
    return sorted(helpers)


def _read_invoked_tests(spec_inv, rec_inv):
    """('ok' | 'unresolved' | 'not-bun', [(label, text)], note). The ORDER's invocation names the targets
    (the issuer's text, which the invocation limb holds the record to); the RECORD's cd says where they ran."""
    sc, rc_ = _bun_test_call(spec_inv), _bun_test_call(rec_inv)
    if sc is None and rc_ is None:
        return "not-bun", [], "the invocation runs no `bun test`, so there is no invoked test file to read"
    targets = (sc or rc_)[1]
    tried = []
    for label, cwd in _cwd_candidates(sc[0] if sc else None, rc_[0] if rc_ else None):
        tried.append(str(cwd))
        files = _match_targets(cwd, targets)
        if not files:
            continue
        helpers = _helper_closure(files)
        try:
            h = subprocess.run(["git", "-C", str(cwd), "rev-parse", "--short", "HEAD"], capture_output=True,
                               text=True, timeout=30).stdout.strip()
        except Exception:  # noqa: BLE001
            h = ""
        pairs = []
        for p in files + helpers:
            try:
                pairs.append((p.as_posix(), p.read_text(encoding="utf-8", errors="replace")))
            except Exception:  # noqa: BLE001
                return "unresolved", [], "invoked test %s is not readable" % p
        return "ok", pairs, ("read %d test file(s) + %d __tests__ helper(s) under %s (%s%s)"
                             % (len(files), len(helpers), cwd, label, ", checkout @" + h if h else ""))
    return "unresolved", [], "bun test targets %s matched no test file under any of: %s" % (targets, "; ".join(tried))


def _seed_hits(pairs: list) -> list:
    """[(file, line, prop)] for every seeding prop named in CODE (comments stripped) of the read files."""
    hits = []
    for label, text in pairs:
        code = _strip_js_comments(text)
        for m in _SEED_RE.finditer(code):
            hits.append((label, code.count("\n", 0, m.start()) + 1, m.group(1)))
    return hits


def _order_project(to_rel, inst: dict) -> str:
    m = re.search(r"org/missions/D[0-9]+/[^/]+/([^/]+)/task-orders/", (to_rel or "").replace("\\", "/"))
    return m.group(1) if m else _project_code(str(inst.get("to_id", "")))


def drives_check(inst: dict, to_text: str | None = None, to_label: str | None = None, to_rel: str | None = None,
                 enforce: bool | None = None, reader=None) -> tuple[list, list]:
    """(violations, frames). `to_text`/`to_rel`/`enforce`/`reader` are injectable so the batteries exercise the
    limb on real order bytes and the self-test without a repo. With `to_rel` given and `enforce` None, the
    boundary is DERIVED from that real order's add commit even when `to_text` is injected."""
    v: list = []
    frames: list = []
    if to_text is None:
        rel, note = _governing_rel(inst)
        if rel is None:
            return v, ["drives-frame: NOT EVALUATED -- governing TO unresolved: %s" % note]
        to_rel = rel
        try:
            to_text = (WORKSPACE / rel).read_text(encoding="utf-8", errors="replace")
        except Exception as exc:  # noqa: BLE001
            return v, ["drives-frame: NOT EVALUATED -- governing TO unreadable (%s)" % exc]
        to_label = rel
    code = _order_project(to_rel, inst)
    ruling = DRIVES_RULING.get(code)
    if enforce is None:
        if ruling is None:
            enforce, reason = False, ("project %s is not under the drives= ruling (RULING Q binds %s); a "
                                      "declaration here is read, never required" % (code or "<unparsed>",
                                                                                    sorted(DRIVES_RULING)))
        else:
            new, reason = _cut_after(to_rel, ruling)
            enforce = new is True
    else:
        reason = "mode injected by caller"
    crit = _criteria_attrs(to_text)
    invs = _to_invocations(to_text)
    tally = {"network": 0, "none": 0, "neither": [], "other": []}
    defects: list = []
    for cid, attrs in crit.items():
        d = attrs.get("drives")
        if d in DRIVES_VALUES:
            tally[d] += 1
        elif d is None:
            tally["neither"].append(cid)
        else:
            tally["other"].append("%s=%r" % (cid, d))
    if ruling is not None and tally["neither"]:
        defects.append("drives: %d of %d criteria declare NEITHER drives=\"network\" nor drives=\"none\": %s. "
                       "1.0.0_SA_CTO's condition on RULING Q (@%s): every new IRPT_FNTEND criterion declares one; an "
                       "undeclared criterion is how a seeded criterion escapes a limb an issuer must remember to arm."
                       % (len(tally["neither"]), len(crit), ", ".join(tally["neither"]), ruling))
    if tally["other"]:
        defects.append("drives: criteria declare a value that is neither \"network\" nor \"none\": %s"
                       % ", ".join(tally["other"]))
    n_net = n_clean = n_seeded = n_unread = n_notbun = 0
    row_frames: list = []
    for r in inst.get("acceptance", []) or []:
        if not isinstance(r, dict) or r.get("status") != "PASS":
            continue
        rid = str(r.get("criterion_id", "") or "").strip()
        if (crit.get(rid) or {}).get("drives") != "network":
            continue
        n_net += 1
        state, pairs, note = (reader or _read_invoked_tests)(invs.get(rid), r.get("invocation"))
        if state == "not-bun":
            n_notbun += 1
            row_frames.append("drives[%s]=network: NOT READ -- %s" % (rid, note))
            continue
        if state != "ok":
            n_unread += 1
            defects.append("drives[%s]=network: the invoked test CANNOT BE READ here -- %s. The limb cannot establish "
                           "that this PASS does not rest on a seeded body, so it does not admit it (RULING Q); run the "
                           "checker where the invocation's portal worktree exists." % (rid, note))
            continue
        hits = _seed_hits(pairs)
        if hits:
            n_seeded += 1
            defects.append("drives[%s]=network: SEEDED -- the invoked test passes %s, so under renderToStaticMarkup "
                           "its body is indistinguishable from one that mounted from the network (S42, C-S67). A "
                           "drives=\"network\" criterion cannot pass by seeding (RULING Q). %s"
                           % (rid, "; ".join("%s:%d %s" % (f.rsplit("/", 1)[-1], ln, p) for f, ln, p in hits[:6]),
                              note))
        else:
            n_clean += 1
            row_frames.append("drives[%s]=network: %s; seeding props named in code: none" % (rid, note))
    frames.append("drives-frame: governing TO=%s; %d criteria: network=%d none=%d neither=%d other=%d; %d PASS "
                  "row(s) on network criteria: %d read clean, %d SEEDED, %d unreadable, %d not a bun test; mode %s -- %s"
                  % (to_label or "<injected>", len(crit), tally["network"], tally["none"], len(tally["neither"]),
                     len(tally["other"]), n_net, n_clean, n_seeded, n_unread, n_notbun,
                     "ENFORCE" if enforce else "ANNOUNCE", reason))
    frames.extend(row_frames)
    if enforce:
        v.extend(defects)
    else:
        frames.extend("drives-announce (would REFUSE for a new order under RULING Q): " + d for d in defects)
    return v, frames


def _self_test() -> int:
    """RED-FIRST BATTERY for the surprises limb. Six arms; each names its expectation; N of N printed.
    A gate never exercised on its failure limbs is a gate that cannot fail."""
    base = {"to_id": "NFRA_TESTPROJ.TO-X-1", "surprises": []}
    rows = {"NFRA_TESTPROJ-S1", "NFRA_TESTPROJ-Z-S2"}
    arms = []

    def arm(name, inst, enforce, rows_, expect_v, expect_frame_sub=None):
        v, f = surprises_check(inst, enforce=enforce, row_ids=rows_, files_scanned=1)
        ok = (len(v) == expect_v) and (expect_frame_sub is None or any(expect_frame_sub in x for x in f))
        arms.append((name, ok, len(v), expect_v, f[-1][:110] if f else ""))

    arm("A ENFORCE + entry without a row id -> 1 violation",
        dict(base, surprises=["the tool crashed on a directory subject"]), True, rows, 1)
    arm("B ENFORCE + row id that resolves to no row -> 1 violation",
        dict(base, surprises=["NFRA_TESTPROJ-S9: a row nobody committed"]), True, rows, 1)
    arm("C ENFORCE + row id that resolves -> 0 violations",
        dict(base, surprises=["NFRA_TESTPROJ-S1: the interim grammar was superseded mid-round"]), True, rows, 0)
    arm("D ENFORCE + site-Z id that resolves -> 0 violations",
        dict(base, surprises=["NFRA_TESTPROJ-Z-S2 -- site Z row"]), True, rows, 0)
    arm("E ANNOUNCE + entry without a row id -> 0 violations, 1 announce frame",
        dict(base, surprises=["legacy free-string surprise"]), False, rows, 0, "surprises-announce")
    arm("F ENFORCE + empty list -> 0 violations, frame says 0 entries",
        dict(base, surprises=[]), True, rows, 0, "0 entries")
    # ---- spine v3 carrier 4: the expect match and the judgment refusal (pure, conditional_checks) ----
    def _row(**kw):
        r = {"criterion_id": "V3-AC1", "criterion_verbatim": "the deciding line is printed", "method": "command",
             "invocation": "echo deciding=42", "output_evidence": "deciding=42", "denominator": "1 of 1", "status": "PASS"}
        r.update(kw)
        return r
    def _v3(name, row, expect_n, needle):
        got = [x for x in conditional_checks({"acceptance": [row]}) if x.startswith("acceptance[")]
        ok = len(got) == expect_n and (expect_n == 0 or any(needle in x for x in got))
        arms.append((name, ok, len(got), expect_n, got[0][:110] if got else ""))
    _v3("G expect matches output + PASS -> 0 violations", _row(expect=r"deciding=\d+"), 0, "")
    _v3("H expect does NOT match output + PASS -> 1 violation (the match decides)", _row(expect=r"deciding=7\b"), 1, "does NOT match expect")
    _v3("I expect is an invalid pattern -> 1 violation", _row(expect="deciding=("), 1, "not a valid pattern")
    _v3("J judgment=true with status PASS -> 1 violation (no verdict on a judgment criterion)", _row(judgment=True), 1, "carries a verdict")
    _v3("K judgment=true under UNVERIFIABLE-BY-INSTRUMENT with a reason -> 0 violations",
        _row(judgment=True, status="UNVERIFIABLE-BY-INSTRUMENT", status_reason="judgment criterion; the CVO grades it at L9"), 0, "")
    _v3("L no expect, no judgment (a pre-v3 row) -> 0 violations (graded as before)", _row(), 0, "")

    # ---- FE-s-23: the INVOCATION ALIGNMENT limb (the prompt/record divergence, row S31) ----
    def _to_fixture(inv, placeholders=None, judgment=False):
        ph = ("<placeholders>%s</placeholders>\n" % placeholders) if placeholders is not None else ""
        if judgment:
            body = '<criterion id="V23-AC1" cell_refs="FIX-a-1" judgment="true"/>'
        else:
            body = ('<criterion id="V23-AC1" cell_refs="FIX-a-1"><invocation>%s</invocation>'
                    '<expect>x</expect></criterion>' % inv)
        return ph + body

    def _inv(name, to_text, recorded, expect_v, needle=None):
        inst_ = {"to_id": "NFRA_TESTPROJ.TO-X-1",
                 "acceptance": [{"criterion_id": "V23-AC1", "invocation": recorded}]}
        got, fr = invocation_alignment_check(inst_, to_text=to_text, to_label="<fixture>")
        ok = (len(got) == expect_v) and (needle is None or any(needle in x for x in got + fr))
        arms.append((name, ok, len(got), expect_v, (got[0] if got else (fr[-1] if fr else ""))[:110]))

    _inv("M invocation limb: ENFORCE, record differs only by placeholder expansion (<WS> twice, "
         "same value, + <PORT>) -> 0 violations",
         _to_fixture("cd <WS>/portal && node s.mjs <WS>/out.png --port <PORT>", placeholders="WS, PORT"),
         "cd /c/tmp/ws-7/portal && node s.mjs /c/tmp/ws-7/out.png --port 5181", 0)
    _inv("N invocation limb: ENFORCE, a CHANGED FLAG in the recorded invocation -> 1 violation "
         "naming BOTH strings",
         _to_fixture("cd <WS>/portal && timeout 120 bun test x", placeholders="WS"),
         "cd /c/tmp/ws-7/portal && timeout 180 bun test x", 1, "TO-CRITERION:")
    _inv("O invocation limb: ENFORCE expands ONLY the DECLARED placeholders, so an undeclared "
         "<FOO> stays literal -> 1 violation",
         _to_fixture("run --path <FOO>/a", placeholders="WS"), "run --path /tmp/a", 1)
    _inv("P invocation limb: UNDECLARED <placeholders> -> ANNOUNCE; the same changed flag "
         "PRINTS with both strings and refuses nothing",
         _to_fixture("cd <WS>/portal && timeout 120 bun test x"),
         "cd /c/tmp/ws-7/portal && timeout 180 bun test x", 0, "invocation-announce")
    _inv("Q invocation limb: a judgment criterion carries no <invocation>, so the row is NOT "
         "COMPARABLE -> 0 violations",
         _to_fixture(None, placeholders="WS", judgment=True),
         "read the two PNGs beside this instance", 0, "row(s) whose criterion carries no")
    _inv("R invocation limb: a REPEATED placeholder is a backreference -- two different "
         "expansions of <WS> in one invocation -> 1 violation",
         _to_fixture("cd <WS>/portal && node s.mjs <WS>/out.png", placeholders="WS"),
         "cd /c/tmp/ws-7/portal && node s.mjs /c/tmp/ws-9/out.png", 1)

    # ---- FE-s-29 limb 2: the COUNT-BAR limb (RULING M(ii), row S56). Pure: the mode is injected; the
    # real-bytes arms (a real bun summary, F17-AC8's committed evidence, the derived boundary) live in
    # .tools/tests/test_count_bar_limb.py.
    def _cb(name, evidence, enforce, expect_v, needle=None, bar="0 fail"):
        row = {"criterion_id": "V29-AC5", "status": "PASS", "expect": bar, "output_evidence": evidence}
        got, fr = count_bar_check({"acceptance": [row]}, enforce=enforce)
        ok = len(got) == expect_v and (needle is None or any(needle in x for x in got + fr))
        arms.append((name, ok, len(got), expect_v, (got[0] if got else (fr[-1] if fr else ""))[:110]))

    _cb("S count-bar: ENFORCE, bar '0 fail' over ' 10 fail' (the bar's own search MATCHES) -> 1 violation",
        " 0 pass\n 10 fail\nRan 10 tests across 1 file.", True, 1, "NONZERO count")
    _cb("T count-bar: ENFORCE, a deciding ' 0 fail' beside a BEFORE note's ' 1 fail' -> 1 violation",
        " 335 pass\n 1 skip\n 0 fail\n(BEFORE: 333 pass / 1 skip / 1 fail)", True, 1, "1 fail")
    _cb("U count-bar: ENFORCE, a genuine ' 0 fail' -> 0 violations", " 5 pass\n 0 fail\n", True, 0)
    _cb("V count-bar: ENFORCE, an ANSI-coloured genuine zero -> 0 violations (never a \\b anchor)",
        "\x1b[0m\x1b[32m 5 pass\x1b[0m\n\x1b[0m\x1b[2m 0 fail\x1b[0m\n", True, 0)
    _cb("W count-bar: ANNOUNCE (legacy), the same contradiction -> 0 violations, an announce frame",
        " 0 fail\n(BEFORE: 1 fail)", False, 0, "count-bar-announce")
    _cb("X count-bar: ENFORCE, '0 of 487 fail' is a DENOMINATOR, not a count -> 0 violations",
        " 486 pass\n 0 fail\n0 of 487 fail", True, 0)
    _cb("Y count-bar: ENFORCE, an ANSI-coloured contradicting ' 10 fail' -> 1 violation (stripped, then counted)",
        "\x1b[0m\x1b[31m 10 fail\x1b[0m\n", True, 1, "NONZERO count")
    _cb("Y2 count-bar: ENFORCE, an id's trailing digit before the noun ('F47-AC2 PROBLEMS') is NOT a count -> 0 "
        "violations (row W3-S41)", "F47-AC2 PROBLEMS list: []\nVALIDATE -> 0 problems\n", True, 0, bar="0 problems")
    _cb("Y3 count-bar: ENFORCE, a real count an ANSI escape glues to a word ('pass\\x1b[0m4 fail') -> 1 violation "
        "(the escape reads as a space)", " 0 fail\n5 pass\x1b[0m4 fail\n", True, 1, "4 fail")

    # ---- FE-s-29 limb 3: the DRIVES limb (RULING Q + the CTO's condition). Pure: the order text, the mode
    # and the file reader are injected; the real-bytes arms (the six seeded suites, F19's browser suite,
    # the round-4 instances, the derived boundary) live in .tools/tests/test_seeded_limb.py.
    def _dr_to(attr):
        return ('<criterion id="V29-AC8" cell_refs="FIX-a-1"%s><invocation>cd <WS>/portal && bun test '
                'src/x.test.ts</invocation><expect>x</expect></criterion>' % attr)

    def _dr(name, attr, test_code, enforce, expect_v, needle=None, state="ok"):
        inst_ = {"to_id": "IRPT_FNTEND.TO-X-1", "acceptance": [
            {"criterion_id": "V29-AC8", "status": "PASS", "invocation": "cd /c/x/portal && bun test src/x.test.ts"}]}
        rd = lambda _s, _r: (state, [("x.test.ts", test_code)] if state == "ok" else [], "fixture reader")  # noqa: E731
        got, fr = drives_check(inst_, to_text=_dr_to(attr), to_label="<fixture>", enforce=enforce, reader=rd)
        ok = len(got) == expect_v and (needle is None or any(needle in x for x in got + fr))
        arms.append((name, ok, len(got), expect_v, (got[0] if got else (fr[-1] if fr else ""))[:110]))

    seeded = "render(createElement(Tab, { initialEnvelope: env, initialReport: r }))"
    browser = "// no initialEnvelope here: the body mounts from the wire\nspawnSync('node', ['driver.mjs'])"
    _dr("Z1 drives: ENFORCE, a criterion declaring NEITHER -> 1 violation", "", browser, True, 1, "NEITHER")
    _dr("Z2 drives: ANNOUNCE (legacy), the same order -> 0 violations, an announce frame", "", browser, False, 0,
        "drives-announce")
    _dr("Z3 drives: ENFORCE, drives=network over a test that SEEDS -> 1 violation", ' drives="network"', seeded,
        True, 1, "SEEDED")
    _dr("Z4 drives: ENFORCE, drives=network over a test naming the prop only in a COMMENT -> 0 violations",
        ' drives="network"', browser, True, 0)
    _dr("Z5 drives: ENFORCE, drives=\"browser\" is neither value -> 1 violation", ' drives="browser"', browser,
        True, 1, "neither")
    _dr("Z6 drives: ENFORCE, drives=network whose invoked test cannot be read -> 1 violation (fail-closed)",
        ' drives="network"', "", True, 1, "CANNOT BE READ", state="unresolved")
    _dr("Z7 drives: ENFORCE, an explicit drives=none over a seeding test -> 0 violations (declared, not network)",
        ' drives="none"', seeded, True, 0)

    # ---- FE-s-37: the GOVERNING-ORDER BINDING (RULING S, row S61). Pure: the bound order's text is injected; the
    # real-shape arms (FE-s-29 doctored to FE-s-28 through check_complete_flip in a real index, the positive control,
    # the committed corpus, the tools S61 measured) live in .tools/tests/test_governing_binding.py.
    import inspect
    _b29 = "org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-29.checker-limbs.md"
    _b28 = "org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-28.mandatory-placeholders.md"
    _t29 = "<to_id>IRPT_FNTEND.TO-FE-s-29</to_id>\n<status>complete</status>\n"

    def _bi(ref=None, tid="IRPT_FNTEND.TO-FE-s-29"):
        return dict({"to_id": tid}, **({"decomp_ref": {"to_ref": ref}} if ref is not None else {}))

    def _bd(name, inst_, bound, expect_v, needles=(), text=_t29):
        got, fr = governing_binding_check(inst_, bound, bound_text=text)
        ok = len(got) == expect_v and all(n in " ".join(got + fr) for n in needles)
        arms.append((name, ok, len(got), expect_v, (got[0] if got else (fr[-1] if fr else ""))[:110]))

    _bd("B1 binding: BOUND, to_ref names the flipped order -> 0 violations, frame BOUND", _bi(_b29), _b29, 0,
        ("BOUND to",))
    _bd("B2 binding: BOUND, to_ref names ANOTHER real order (FE-s-28) -> 1 violation naming BOTH paths", _bi(_b28),
        _b29, 1, (_b29, _b28))
    _bd("B3 binding: BOUND, to_ref written absolute with backslashes, same file -> 0 violations",
        _bi(str(WORKSPACE / _b29).replace("/", "\\")), _b29, 0)
    _bd("B4 binding: BOUND, no to_ref, to_id names ANOTHER order -> 1 violation", _bi(None, "IRPT_FNTEND.TO-FE-s-28"),
        _b29, 1, ("to_id",))
    _bd("B5 binding: BOUND, to_id carries the order's slug (the 119-instance shape) -> 0 violations",
        _bi(_b29, "IRPT_FNTEND.TO-FE-s-29.checker-limbs"), _b29, 0)
    _bd("B6 binding: BOUND, `...FE-s-2` is not `...FE-s-29` (no `.` boundary) -> 1 violation",
        _bi(_b29, "IRPT_FNTEND.TO-FE-s-2"), _b29, 1)
    _bd("B7 binding: BOUND, a bare project code names no order -> 1 violation", _bi(_b29, "IRPT_FNTEND"), _b29, 1)
    _bd("B8 binding: BOUND, an order with NO <to_id> tag answers to its filename stem -> 0 violations",
        _bi(_b29, "IRPT_FNTEND.TO-FE-s-29"), _b29, 0, text="# an order without a header tag\n")
    _bd("B9 binding: UNBOUND -> 0 violations, and the frame SAYS the run is unbound", _bi(_b28), None, 0, ("UNBOUND",))
    _msrc, _rsrc = inspect.getsource(main), inspect.getsource(_resolve_governing_to)
    _order_ok = (_msrc.index("governing_binding_check(") < min(_msrc.index("conditional_checks(inst)"),
                                                               _msrc.index("alignment_check(inst)"))
                 and _rsrc.index("_BOUND_ORDER is not None") < _rsrc.index('_dref.get("to_ref"'))
    arms.append(("B10 binding: main() runs the binding before every limb; the resolver reads the bound order before "
                 "to_ref", _order_ok, 0, 0, "source order"))

    passed = sum(1 for a in arms if a[1])
    print("proof-of-spec-check --self-test (surprises limb + v3 carrier 4 + invocation alignment + count-bar + drives "
          "+ governing-order binding)")
    for name, ok, got, exp, tail in arms:
        print("  %s  %s  (violations got=%d expected=%d)  %s" % ("PASS" if ok else "FAIL", name, got, exp, tail))
    print("  RESULT: %d of %d arm(s) behaved" % (passed, len(arms)))
    return 0 if passed == len(arms) else 1


def checker_vintage() -> str:
    """The commit that last touched THIS checker, as `<hash> <YYYY-MM-DDTHH:MM:SSZ>` -- UTC with a Z,
    or the hash alone. (1b) 2026-08-30, 1.0.0_SA_CTO 87900: an instance carried the checker vintage as
    "3948c766a7 (2026-08-30 01:00:15)" -- a local time without a zone for a commit made 05:00:15Z --
    hand-derived by the seat because the checker printed none. The instrument that pins vintages
    prints its own, correctly, so no seat has to derive it. Never a local time; never a typed Z."""
    try:
        out = subprocess.run(
            ["git", "log", "-1", "--format=%H|%cI", "--", str(Path(__file__).resolve())],
            capture_output=True, text=True, encoding="utf-8", errors="replace", cwd=str(_REPO_ROOT), timeout=20)
        if out.returncode != 0 or "|" not in out.stdout:
            return "UNREAD (git log failed; the hash is not knowable here)"
        h, ci = out.stdout.strip().split("|", 1)
        return f"{h[:10]} {iso_offset_to_utc_z(ci)}{worktree_dirty_suffix(Path(__file__).resolve(), _REPO_ROOT)}"
    except Exception:  # noqa: BLE001 -- a vintage line must never turn the checker into rc=2
        return "UNREAD (exception reading git log)"


def worktree_dirty_suffix(path, repo_root) -> str:
    """(1b', 3.0.0_SA_CVO 88184) The vintage line names the tool's last COMMIT; when the tool's worktree
    differs from HEAD the bytes that RAN are not those bytes, and a seat grading under an uncommitted
    checker change would print a vintage that is false of the run (measured 15:0xZ: "checker-vintage:
    cec2a9b663" beside a content line only 4200a54390 can emit). Returns "" for a clean file, or
    "+DIRTY(<added>+<deleted> lines)" from `git diff --numstat HEAD -- <path>`; an unreadable diff is
    announced as +DIRTY(UNREAD) rather than passed off as clean."""
    try:
        out = subprocess.run(["git", "diff", "--numstat", "HEAD", "--", str(path)],
                             capture_output=True, text=True, encoding="utf-8", errors="replace", cwd=str(repo_root), timeout=20)
    except Exception:  # noqa: BLE001
        return "+DIRTY(UNREAD)"
    if out.returncode != 0:
        return "+DIRTY(UNREAD)"
    line = out.stdout.strip()
    if not line:
        return ""
    parts = line.split("\t")
    try:
        n = int(parts[0]) + int(parts[1])
    except (ValueError, IndexError):
        return "+DIRTY(binary)"
    return f"+DIRTY({n} lines)"


def iso_offset_to_utc_z(ci: str) -> str:
    """%cI (ISO 8601 with a numeric offset) -> UTC rendered with a literal Z that is TRUE, because the
    offset was applied first. A string without an offset is returned as the hash-only sentinel."""
    from datetime import datetime, timezone
    try:
        dt = datetime.fromisoformat(ci.strip())
    except ValueError:
        return "(date unparsed)"
    if dt.tzinfo is None:
        return "(date carried no offset; not rendered)"
    return dt.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def main() -> int:
    global _BOUND_ORDER
    if len(sys.argv) == 2 and sys.argv[1] == "--self-test":
        return _self_test()
    # --governing-order <order.md> (FE-s-37) is lifted out of argv FIRST, so the positional contract below -- one
    # instance path, then an optional id list -- is exactly what it was.
    args: list[str] = []
    bound_arg = None
    i = 1
    while i < len(sys.argv):
        a = sys.argv[i]
        if a == "--governing-order" or a.startswith("--governing-order="):
            val = a.split("=", 1)[1] if "=" in a else (sys.argv[i + 1] if i + 1 < len(sys.argv) else "")
            i += 1 if "=" in a else 2
            if not val.strip():
                print("USAGE-ERROR (rc=2): --governing-order needs the path of the order being closed")
                return 2
            bound_arg = val
            continue
        args.append(a)
        i += 1
    if len(args) not in (1, 2):
        print(__doc__)
        print("USAGE-ERROR (rc=2): expected <instance.json> [expected_criterion_ids] [--governing-order <order.md>]")
        return 2
    bound_rel = None
    if bound_arg is not None:
        bound_rel = _ws_rel(bound_arg)
        if Path(bound_rel).is_absolute() or bound_rel.startswith("../"):
            print(f"USAGE-ERROR (rc=2): --governing-order '{bound_arg}' lies OUTSIDE this checker's tree "
                  f"({WORKSPACE}) -- run that tree's own .tools/proof-of-spec-check.py")
            return 2
        _BOUND_ORDER = WORKSPACE / bound_rel
    try:
        inst = json.loads(Path(args[0]).read_text(encoding="utf-8"))
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        print(f"READ-ERROR (rc=2): {exc}")
        return 2

    violations: list[str] = []
    # THE BINDING RUNS FIRST (FE-s-37): an instance naming a different order than the one being closed is refused
    # before any limb runs, and every limb below then reads the bound order. Unbound, this only prints its frame.
    bind_violations, bind_frames = governing_binding_check(inst, bound_rel)
    violations.extend(bind_violations)
    if len(args) == 2:
        violations.extend(coverage_check(inst, args[1]))
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
    # ARTIFACT ROW RESOLUTION (2026-08-30): runs on every instance; its frame prints its denominator
    # and names the class it does NOT cover, so a clean line cannot be read wider than it is.
    res_violations, res_frames = artifact_resolution_check(inst, inst_path=Path(args[0]))
    violations.extend(res_violations)
    align_frames = list(bind_frames) + list(align_frames) + res_frames
    # SURPRISES LIMB (2026-09-03): runs on every instance; ENFORCE vs ANNOUNCE is derived from the
    # governing TO's root, never from a caller-side flag -- the same one-discriminator rule as layer 1.
    sur_violations, sur_frames = surprises_check(inst)
    violations.extend(sur_violations)
    align_frames = align_frames + sur_frames
    # INVOCATION ALIGNMENT LIMB (2026-09-12, FE-s-23): runs on EVERY instance and prints its
    # denominator whether or not anything diverged. ENFORCE vs ANNOUNCE is derived from the
    # governing TO's own <placeholders> declaration, never from a caller-side flag -- the same
    # one-discriminator rule as layer 1 and the surprises limb.
    inv_violations, inv_frames = invocation_alignment_check(inst)
    violations.extend(inv_violations)
    align_frames = align_frames + inv_frames
    # COUNT-BAR LIMB and DRIVES LIMB (2026-09-13, FE-s-29 limbs 2 and 3): run on EVERY instance and print
    # their denominators. NEW vs LEGACY is derived from the governing order's add commit against the ruling
    # pin (the shared boundary above), never from a caller-side flag.
    cb_violations, cb_frames = count_bar_check(inst)
    violations.extend(cb_violations)
    align_frames = align_frames + cb_frames
    dr_violations, dr_frames = drives_check(inst)
    violations.extend(dr_violations)
    align_frames = align_frames + dr_frames

    n_acc = len(inst.get("acceptance", []))
    print(f"proof-of-spec-check | structural={structural} | acceptance rows={n_acc} | violations={len(violations)}")
    print(f"  checker-vintage: {checker_vintage()}")
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
        print("INVALID (rc=1)")
    elif _BACKWARD_ASSERTED is False:
        # A VALID whose backward limb was never asserted is a WEAKER statement than a VALID on a
        # delimited face, and nothing in the bare word said so (DT~X 79061). Same rc; the verdict
        # line names the limb it could not enforce.
        print("VALID (rc=0) -- alignment-backward UNASSERTED (undelimited <decomp_ref>: put "
              "<owned_cells>id, id</owned_cells> INSIDE <decomp_ref> to make it enforceable)")
    else:
        print("VALID (rc=0)")
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
