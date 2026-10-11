#!/usr/bin/env python3
"""surprise-row-gate -- the L7 / L10 ROW GATE of the canonical fabric workflow (org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md; Andrew-direct 2026-09-01).

AUTHORIZATION: /open-calls card 2 of 9, REC "MANDATE the three that are already schema-backed
(step 7's two trigger fields, step 9's disposition enum, step 10's route + loop_target) and DEFER
the markdown-to-JSON container swap" -> "All recs approved". The container swap was subsequently
DECLINED at this lane on measured grounds (census @0c7853c17f, DEF=1); this gate is the half that
survives, and it is the half that carries the structured guarantee.

WHAT IT REFUSES, on a staged org/surprise_channel/**/{INVESTIGATION,REMEDIATION}_v*.md:
  NEW investigation row  -> must carry spec_asserts AND world_is (the step-7 trigger's two halves)
  NEW remediation row    -> carries NO route (spine v3.0/3.1 L9/L10, carrier 6 of eight: the slug goes to the CTO,
                            the single router; the three route tokens are RETIRED). A row that still carries a
                            legacy route + loop_target pair (a round issued under v2, finishing under its cut
                            orders) keeps the pair on the LOCKED MAPPING  SPEC_ERROR->6 | DECOMP_INVALIDATING->5 |
                            SCOPE_CHANGE->2. The L10 precondition applies to EVERY new remediation row (below).
  ANY new row            -> must satisfy its schema's REQUIRED fields and closed enums
  ANY new row            -> carries an id unused in every OTHER document of its plane under the project, at the
                            graded index (the allocator race of v3's first drain, 3.0.0_SA_CVO 94007)

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
import importlib.util
import inspect
import json
import os
import re
import copy
import subprocess
import sys

# TWO ROOTS (project-tree spec s.7, Andrew-ruled 2026-09-02; grammar from org/standards/PROJECT_TREE.
# contract.json: surprise_channel_glob org/missions/D*/*/*/surprise-channel/{investigations,remediations}/**).
# The flat channel org/surprise_channel/<PROJECT>/ stays; the tree adds a per-project channel whose
# PATH carries the project AND the kind. A gate reading one root is blind to the other.
# spine v3.0 carrier 5: the ADJUDICATION document (annex 4a) -- the CVO's rows about worker rows, same schema as the
# investigation document, its own sub-folder, so L8 reads and L10 counts worker rows only.
FLAT_CHANNEL_RE = re.compile(
    r"(^|/)org/surprise_channel/([^/]+)/(INVESTIGATION|ADJUDICATION|REMEDIATION)_v[^/]*\.(md|json)$")
TREE_CHANNEL_RE = re.compile(
    r"(^|/)org/missions/D(?:0|[1-9][0-9]?)/[^/]+/([^/]+)/surprise-channel/(investigations|adjudications|remediations)/"
    r"(INVESTIGATION|ADJUDICATION|REMEDIATION)_v[^/]*\.(md|json)$")
CHANNEL_RE = re.compile(FLAT_CHANNEL_RE.pattern + "|" + TREE_CHANNEL_RE.pattern)


def _gao_name() -> str:
    """The git-author-override audit log name for THIS box: one file per box (shape (a), MSTR consensus 2026-10-11),
    the legacy shared name when AGENTBUS_DEVICE is unset or malformed."""
    dev = os.environ.get("AGENTBUS_DEVICE", "").strip()
    ok = bool(dev) and all(c in "abcdefghijklmnopqrstuvwxyz0123456789-" for c in dev)
    return "git-author-override-audit.%s.log" % dev if ok else "git-author-override-audit.log"


def _folder_identity(rel):
    """(project, kind) the PATH declares, or (None, None). Tree: the project folder two levels above
    surprise-channel/, and the kind from the sub-folder -- a REMEDIATION file filed under
    investigations/ is a path/content disagreement.

    FLAT RETURNS kind=None, DELIBERATELY, and this docstring used to claim otherwise ("kind is the
    filename's") while the code returned None. That false line is what produced ESTATE_GOVERNANCE-S5
    (3.0.0_SA_CVO): a reader checking the docstring would conclude a flat ADJUDICATION_v document
    declares its kind, and the coordinate limb -- which refuses a C- row when folder_kind is not
    "ADJUDICATION" -- therefore refused every C- row the CVO filed on the flat channel it had just
    minted. The limb now asks _is_adjudication_doc(rel) instead when folder_kind is None.

    WHY None IS KEPT RATHER THAN "FIXED" HERE, and this is now a RULING rather than a caution:
    folder_kind feeds FOUR consumers and for a flat path all four are skipped today. Returning a kind
    would also switch on the L10 precondition limbs (:1033) for the 2 flat REMEDIATION documents that
    exist (ESTATE_GOVERNANCE, NFRA_PIPELINE). 3.0.0_SA_CVO RULED IT (ESTATE_GOVERNANCE-C-S6, msg 94301):
    a flat path's kind IS the filename's WHERE KIND MATTERS -- schema, coordinate, the id census -- and
    the L10 precondition limbs DO NOT BIND on a flat channel at all, because a flat channel has no task
    orders to be terminal and an L10 read there would pass on an EMPTY INPUT SET. So consulting
    _is_adjudication_doc at the point kind is used is the DURABLE form, not a stopgap: kind where kind
    is consulted, and the order-bound limbs keyed to the tree spelling where orders exist.
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
# THE ALLOCATOR COORDINATE (Andrew-direct 2026-09-04 ~04:58Z at this terminal, "recs approved", record @9ef9a40aae; the same
# word "a for both" at the CVO's, @92af61a111; annex v3.2 + the schema half @4d65d9b496): a row minted in worker <n>'s worktree
# carries W<n> (<n> = the worker's SLOT, the ~<n> of its serial), <k> restarting per coordinate; a seat's row on the main index
# carries no W; the fabric coordinate Z- stays and nests first. C- is the CVO's coordinate for its rows in adjudications/ -- admitted
# here as a superset, REQUIRED only once the staged schema's id pattern admits it (the schema is the switch; either half alone
# fails closed). v3's first drain minted NFRA_COMPEFFICACY-S34 twice from two indexes; the coordinate makes that impossible at mint.
# CT-d-6: `z` is any fabric-COORDINATE-SHAPED infix (a capital, optional digits); the device register, never this regex, says
# which are held. W<n>- and C- keep their own meaning and can never be a coordinate (the lookahead).
ID_RE = re.compile(r"^(?P<project>[A-Z0-9_]+)-(?P<z>(?!W[0-9]*-|C-)[A-Z][0-9]*-)?(?:W(?P<w>[0-9]+)-|(?P<c>C-))?S(?P<k>[0-9]+)$")
WORKER_SERIAL_RE = re.compile(r"^0\.9\.0_WK_(?P<code>[A-Z0-9_]+?)[~_](?P<n>[0-9]+)$")
# /endpoint --forward Phase-0 outcome id. PERMANENT AND NEVER REUSED by contract
# (1.0.0_SA_CTO @b3584ea86a, landed in the skill AND the PRD template together).
OUTCOME_REF_RE = re.compile(r"^FWD-[0-9]+$")
# OWNER-AND-CARRIER LIMBS (1.0.0_SA_CTO, 2026-09-16, SELF_DRIVE_LGIC_RULINGS_20260916.md R-18(2), R-19(2), R-19 addendum,
# and A-1 of the LGIC_ENFORCE round-2 analysis; measured on LGIC_NAMING-W2-S7, LGIC_CANON-W5-S2, LGIC_ENFORCE-C-S24).
# A disarm owner is the seat that must ACT (file the evidence and send the word) while 3.0.0_SA_CVO WRITES the clock
# (R-15). So a NEW row may name neither a WORKER (terminal at its drain; can never send the word -- the duty passes to
# its issuer) nor the CVO (the writer) as disarm owner. On an EXISTING remediation row `disarm.owner` is otherwise
# immutable; it may change ONLY when the same write appends exactly one evidence entry citing a CTO ruling by id and
# vintage and nothing else moves. And the CVO's L9 fields (`adjudicates`, disposition GRADUATED) are refused on a row a
# WORKER surfaced: a worker's GRADUATED transfers the item to nobody and hides it from the CVO's compile.
RULING_CITATION_RE = re.compile(r"(?:\bR-[0-9]+\b.*@[0-9a-f]{7,40}\b)|(?:@[0-9a-f]{7,40}\b.*\bR-[0-9]+\b)")
CVO_SERIAL = "3.0.0_SA_CVO"

# LOCKED MAPPING -- fork 4's verdict IS fork 5's loop target. See the module docstring.
ROUTE_TO_STEP = {"SPEC_ERROR": 6, "DECOMP_INVALIDATING": 5, "SCOPE_CHANGE": 2}

OVERRIDE_RE = re.compile(r"^#\s*surprise-row-override:\s*(\S.*)$", re.M)

# GATE (iii) -- Andrew-direct 2026-09-03 (state of record @716a9bc7ce call 3, LD-0521; transcript: "no
# LIM-10 routing until all task orders are complete ... We do not route until the job is over"). A NEW
# remediation row carrying a `route` under a TREE project is REFUSED while any task order of that project,
# on EITHER root, is not terminal at HEAD. Tree projects only; NEW rows only (this gate's standing model);
# the census reads HEAD blobs, never the worktree -- a peer's half-written status flip must not decide a
# refusal. THE OTHER HALF of his precondition ("the surprise channel, all investigations, completely checked
# by CVO") is the SECOND LIMB below (Andrew-direct 2026-09-03 ~04:5xZ "Recs approved", CTO /open-calls CALL 2).
# Terminal words are the TO protocol's (complete / superseded / cancelled) plus the withdrawn state an issuer
# writes on a mis-seated dispatch.
# ANCHORED AT LINE START 2026-09-10 (3.0.0_SA_CVO~Z, row Z-S15 graduated at C-S16). The bare
# form was applied with .search(), so it took the FIRST occurrence anywhere in the file --
# INCLUDING INSIDE PROSE. TO-IAM-t-3's text reads "Carries NO <status> tag at all" while
# DESCRIBING A DIFFERENT DOCUMENT, so the gate captured "tag", failed to find it among the
# terminal words, and declared a COMPLETE order non-terminal. The order whose subject is
# whether status tags mean anything is the one misread on its own status tag.
# GENERAL FORM: A FIRST-MATCH READ OF A STRUCTURED FIELD ASSUMES THE FIELD APPEARS BEFORE ANY
# DISCUSSION OF IT. True of most documents; false for exactly the documents that are ABOUT the
# field -- which are the ones this estate writes when it audits its own markup.
# WHY ANCHORED AND NOT PAIRED, MEASURED OVER 208 TASK ORDERS BEFORE CHOOSING:
#   requiring </status>  -> REGRESSES 131 of 208. Most orders never close the tag; the "obvious"
#                          fix would have been far worse than the defect.
#   last-match           -> works, but changes the verdict on 2 files for the benefit of 1.
#   LINE-ANCHORED        -> 0 regressions, and disagrees with the old form on EXACTLY ONE file:
#                          the defective one. A real tag starts its line; a prose mention does not.
# DUPLICATED IN .tools/owned-paths-validate.py AS _TO_STATUS_RE -- two carriers of one pattern,
# fixed identically in the same commit. Naming it because the next edit must move both.
TO_STATUS_RE = re.compile(r"^\s*<status>\s*([A-Za-z_-]+)", re.I | re.M)
# THE LAST TAG GOVERNS (1.0.0_SA_CTO gate-owner ruling, msg 107528, 2026-10-09): an order's status is its LAST
# line-anchored <status> tag. A stale earlier duplicate (pending above complete) must not read as the status.


def _to_status_match(text):
    """The LAST line-anchored <status> match in `text`, or None (ruling msg 107528)."""
    found = list(TO_STATUS_RE.finditer(text or ""))
    return found[-1] if found else None


# `parked` (1.0.0_SA_CTO 2026-09-30, on 3.0.0_SA_CVO's MDPF_SECCLASS rounds 4-5 review Q1): a PARKED order sits OUTSIDE
# the current round's rectangle by the CTO's ruling (the relaunch brief: nothing waits on a dead seat; the order carries its
# owner and the condition that un-parks it). It is therefore not an open order of the round, and it must not pin every later
# slug's watermark. It RE-ENTERS the census the moment its issuer flips the status back (pending / staged / issued), so
# nothing is lost: this reads a parked order as not-open, never as done.
TERMINAL_TO_WORDS = ("complete", "completed", "closed", "done", "superseded", "cancelled", "canceled", "withdrawn",
                     "parked")

# GATE (iii), SECOND LIMB -- record org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260903_045xZ_RECS_
# APPROVED_CVO_SEND_REFUSED_L7_L9_GATE_III_INVESTIGATIONS_LIMB.md. A NEW route-carrying row under a TREE project is
# ALSO refused while any investigation item of that project is not dispositioned. The channel is append-only, so an
# item's disposition is its LATEST CARRIER, resolved in this order: a REMEDIATION row bearing the item's id (GRADUATED
# by construction); else the last investigation row whose `adjudicates` list names the item (that row's `disposition`
# is the item's); else the item's own row. UNDER_INVESTIGATION, or an item no row carries, is "not dispositioned".
# The census reads the INDEX (what the commit contains), so the L10 stamp row and the adjudications it carries land
# in ONE commit -- one slug, one act. An `adjudicates` entry naming an id no row carries is a phantom adjudication
# and is refused on its own.
# ROUTE-CARRYING ROW, BOTH SHAPES: a REMEDIATION row with `route`, and an INVESTIGATION row whose `disposition` is
# DECOMP_INVALIDATING -- that word is in ROUTE_TO_STEP (it IS the route to L5) and it is the shape the round-1 stamp
# took (an investigation row, not a remediation row), which the first limb's trigger never saw. Both limbs now run
# on both shapes.
UNDISPOSITIONED = ("UNDER_INVESTIGATION", None, "")
INVESTIGATION_PATTERNS = ("org/missions/D*/*/%s/surprise-channel/investigations/*",
                          "org/surprise_channel/%s/INVESTIGATION_v*")
REMEDIATION_PATTERNS = ("org/missions/D*/*/%s/surprise-channel/remediations/*",
                        "org/surprise_channel/%s/REMEDIATION_v*")
# carrier 5: the CVO's adjudication rows resolve items across documents (their `adjudicates` names investigation ids).
ADJUDICATION_PATTERNS = ("org/missions/D*/*/%s/surprise-channel/adjudications/*",
                         "org/surprise_channel/%s/ADJUDICATION_v*")

# EN-k-38 / S75: THE STALENESS THRESHOLD, A JUDGMENT (task order K38R8, graded by 3.0.0_SA_CVO at L9, not by
# this gate's own arms -- the arms only check that a fresh row PASSES and a stale one does NOT). Measured
# against LGIC_ENFORCE's own round cadence at the round-8 cut (round 1 at 2026-09-15T02:20Z through round
# 8's cut census at 2026-09-18 ~05:42 UTC -- about 75.5 hours across 7 round-to-round gaps, roughly 10.8h
# per round) and against the W7-S1 incident itself (opened OPEN+owned at round v1, first seen stale at
# round v8 -- a 7-round, 67-hour gap that survived every rowlessness-shaped instrument because the row
# EXISTS). N=2 rounds means a row must survive its OWN minting round PLUS one full further round with no
# update before it is flagged -- normal same-round or next-round remediation lag is not penalised, but a
# row idle across a round boundary is caught at the NEXT slug rather than the 7th. Applied to W7-S1's own
# numbers, N=2 would have caught it at round v3 (2026-09-17T14:12Z), about 40 hours before round 8 actually
# did.
STALE_OPEN_ROW_N_ROUNDS = 2


# FOREIGN-ROW SWEEP (2026-09-03, proposed by 1.0.0_SA_CTO~Z via 0.0.0_AB_MSTR~Z 93627, accepted at the base): on a
# shared append-only channel file, a seat that commits THE FILE carries every peer row sitting uncommitted in it under
# its own author line -- content intact, each row's `surfaced_by` true, the commit's authorship wrong. Site Z measured
# the class over the file's whole life: 28 commits, 32 rows, EXACTLY 3 sweeps carrying 6 foreign rows, no fourth; three
# real guards (a printed git status chained with &&, a byte-identity check that a peer's re-serialisation defeats, a
# habit) all missed it. The check is a SET question, stable under re-serialisation: every row NEW in this commit must
# carry a `surfaced_by` whose seat is the committer's seat. The committer is read by the estate's actor precedence
# ($OPAL_AGENT_SERIAL -> the session serial file -> GIT_AUTHOR_IDENT last), never the --author, because safe-commit's
# gate stages run before --author is applied. Compared at BASE serial (a lane and its base are one seat). Scoped to
# INVESTIGATION rows -- `surfaced_by` is theirs; a remediation row is the CVO's act about another seat's remedy. An
# unreadable committer or an unparseable surfaced_by REFUSES (fail-safe toward the wrong direction is not safe). The
# gate's audited override covers a deliberate integration of peer rows.
# BOUND, stated so the arm is never read as wider than it is (site Z's own scope correction, 93630): this is ROW-SCOPED.
# It compares row-id sets, so its subject is commits that ADD ROWS; a commit that carries a peer's uncommitted PROSE
# hunk (a correction bullet outside the row array) adds no row, yields an empty delta and PASSES -- one such case is on
# site Z's record (7abe7552b5, disclosed and closed at the time). It is deliberately NOT widened to prose: prose has
# nothing reliable to key an author on, and a guard that cannot decide its own question either fires constantly or is
# relaxed into decoration. LAPTOP POPULATION, measured the same way at adoption (20 files, 431 commits, 227 rows over
# their life): 104 commits carried 161 rows surfaced by another seat, all 104 authored by 3.0.0_SA_CVO -- not the
# accident but the pre-law practice of the channel owner filing workers' relayed surprises, retired by the carrier law
# of 2026-09-03; the arm refuses both shapes prospectively, which is what that law asks. Historical rows are not re-graded.
def _committer_serial(root):
    env = os.environ.get("OPAL_AGENT_SERIAL", "").strip()
    if env:
        return env
    sid = os.environ.get("CLAUDE_CODE_SESSION_ID", "").strip()
    if sid:
        try:
            p = os.path.join(root, "org", "mcp", "sessions", sid + ".serial")
            if os.path.isfile(p):
                with open(p, encoding="utf-8") as fh:
                    val = fh.read().strip()
                if val:
                    return val
        except OSError:
            pass
    try:
        ident = subprocess.run(["git", "var", "GIT_AUTHOR_IDENT"], cwd=root, capture_output=True, text=True,
                               encoding="utf-8", errors="replace", timeout=20).stdout
    except Exception:  # noqa: BLE001
        return ""
    return ident.split(" <", 1)[0].strip()


SERIAL_RE = re.compile(r"^\d+\.\d+\.\d+_[A-Z]{2}_[A-Za-z0-9]+")


def _base_serial(s):
    return str(s or "").strip().split("~", 1)[0]


def _seats_with_open_orders(root, code):
    """The base serials holding a NON-TERMINAL task order under the project, on both roots, read from HEAD blobs
    (never the worktree). (set, note); set is None when the census could not run -- the caller fails closed."""
    try:
        ls = subprocess.run(["git", "ls-files", "--", "*/task_orders/%s.*.md" % code,
                             "org/missions/D*/*/%s/task-orders/*.md" % code],
                            cwd=root, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=60)
    except Exception as exc:  # noqa: BLE001
        return None, "git ls-files raised %s" % exc
    if ls.returncode != 0:
        return None, "git ls-files rc=%d" % ls.returncode
    seats = set()
    for p in [x.strip().replace("\\", "/") for x in ls.stdout.splitlines() if x.strip()]:
        st, text = _blob(root, "HEAD", p)
        if st != "OK":
            continue
        m = _to_status_match(text)
        word = m.group(1).lower() if m else ""
        if word in TERMINAL_TO_WORDS:
            continue
        im = re.search(r"<issued_to>\s*([^<\n]+?)\s*</issued_to>", text, re.I)
        if im:
            seats.add(_base_serial(im.group(1)))
    return seats, ""


def _foreign_row_violations(rel, kind, added, committer, coworkers=None, merging=False,
                            parent_ids=None):
    """PURE given `coworkers`. Complaints for NEW investigation rows whose `surfaced_by` is not the committer's seat.

    CO-WORKER ADMISSION (2026-09-03, 2.0.0_SA_COO 93746, measured under round 6 of NFRA_COMPEFFICACY): ten Codex lanes
    on one project in ONE worktree share ONE investigation file, so every lane's commit necessarily carries every other
    lane's uncommitted row -- the arm refused four lanes' rows together and deadlocked the round. A row whose
    `surfaced_by` HOLDS A NON-TERMINAL TASK ORDER ON THE SAME PROJECT is a co-worker's row riding along in a shared
    worktree, not a sweep of a stranger's: it is ADMITTED and NAMED in the gate's notes (the author-line mismatch stays
    on the record without an override). A row whose surfacer holds no open order on the project -- site Z's accident
    class, a Tier-1 seat's row, a stranger -- is still refused. `coworkers` None = the census could not run -> refused.

    AT A MERGE (merging=True, MERGE_HEAD present; 0.0.0_AB_MSTR 94283, the first cross-fabric reconcile): the sweep
    does not fire, and the rows are NAMED in the notes instead. THIS IS THE SAME PRINCIPLE _coordinate_violations
    ALREADY CARRIES three hundred lines below -- the committer of a merge commit is the INTEGRATOR, never the
    allocator -- and this limb, written 2026-09-03, was simply never wired to it. MEASURED: the reconcile of
    origin/SITEZ refused on 147 of 150 new rows, every one correctly stamped with its own surfaced_by
    (3.0.0_SA_CVO~Z, 0.7.0_AE_CloudOps~Z/~S, 2.0.0_SA_COO~Z) and every one already graded by site Z's own row gate at
    ITS authorship. 147-of-150 foreign is not the signature of a sweep; it is the signature of an INTEGRATION, and the
    sweep exists to catch attribution THEFT -- a seat pulling a stranger's rows under its own author line -- which a
    merge is not: the rows arrive attributed and the merge commit is the only honest carrier for them.

    WHY THE CO-WORKER MECHANISM DOES NOT ALREADY COVER IT: a project drain passes because the worker's serial HOLDS AN
    OPEN ORDER on that project. A cross-fabric integrator carries rows from seats with no order on this fabric at all,
    so every one reads foreign. The two cases need different admissions and only one of them existed.

    BLOCKED: CONSEQUENCE WORTH STATING BECAUSE IT IS NOT OBVIOUS: safe-merge.sh grades the MERGED INDEX by calling this gate
    while MERGE_HEAD is present, so the sweep is skipped there too. That is acceptable and it is not silent -- the
    DUPLICATE-ID limb, which is the reason the drain grades the merged index at all, is untouched, and the co-worker
    admission already covered the drain case. The residual is a branch on which no hook ever ran, which is the same
    residual both sibling gates accept.
    Returns (violations, notes)."""
    if kind != "INVESTIGATION" or not added:
        return [], []
    if merging:
        # BOUNDARY (b), 3.0.0_SA_CVO 94299: the exemption is PER ROW and it is a MEASUREMENT, not an
        # inference. A row whose id a PARENT carried was CARRIED by this merge; a row in NEITHER parent
        # was MINTED in the merge commit -- the merging seat's own act -- and is swept as the
        # committer's, exactly as off a merge. Without this, "the integrator did not mint it" rests on
        # `surfaced_by`, which the integrator writes.
        if parent_ids is None:
            return ["%s: MERGE COMMIT but the parents' row ids could NOT be read, so no row can be shown "
                    "to have been CARRIED rather than MINTED here -- REFUSED, fail-closed (boundary (b))"
                    % rel], []
        carried = [r for r in added if str(r.get("id") or "").strip() in parent_ids]
        minted = [r for r in added if str(r.get("id") or "").strip() not in parent_ids]
        notes = []
        if carried:
            _seats = sorted({_base_serial(r.get("surfaced_by")) or "<unparseable>" for r in carried})
            notes.append("%s: MERGE COMMIT -- foreign-row sweep exempt for %d row(s) a PARENT carried, "
                         "attributed to %d seat(s) (%s) and graded at their own authorship. The integrator "
                         "is not their author (0.0.0_AB_MSTR 94283; boundary (b) 3.0.0_SA_CVO 94299)."
                         % (rel, len(carried), len(_seats), ", ".join(_seats)))
        if not minted:
            return [], notes
        # rows minted IN the merge fall through and are swept as the committer's
        added = minted
        notes.append("%s: %d row(s) are in NEITHER parent -- MINTED in this merge commit, so they are graded "
                     "as the committer's own (boundary (b))." % (rel, len(minted)))
        _carry_notes = notes
    else:
        _carry_notes = []
    who = _base_serial(committer)
    if not who or not SERIAL_RE.match(who):
        return ["%s: committer identity UNREADABLE (%r) while %d new row(s) are staged -- the foreign-row sweep "
                "cannot be graded; REFUSED, fail-closed" % (rel, committer, len(added))], []
    foreign, carried = [], []
    for r in added:
        sb = _base_serial(r.get("surfaced_by"))
        if not SERIAL_RE.match(sb):
            foreign.append("%s (surfaced_by %r unparseable)" % (r.get("id"), r.get("surfaced_by")))
        elif sb == who:
            continue
        elif coworkers is None:
            foreign.append("%s (surfaced_by %s; the open-order census could not run, so co-worker status is unknown)"
                           % (r.get("id"), r.get("surfaced_by")))
        elif sb in coworkers:
            carried.append("%s (surfaced_by %s, an open order on this project)" % (r.get("id"), r.get("surfaced_by")))
        else:
            foreign.append("%s (surfaced_by %s)" % (r.get("id"), r.get("surfaced_by")))
    notes = list(_carry_notes)
    if carried:
        notes.append("%s: CO-WORKER ROWS carried under %s's author line (shared worktree; each row's own surfaced_by "
                     "holds an open order on this project): %s" % (rel, who, ", ".join(carried)))
    if foreign:
        return ["%s: FOREIGN-ROW SWEEP -- %d of %d new row(s) were surfaced by a seat that is neither the committer %s "
                "nor a co-worker with an open order on this project: %s. Commit only your own rows, or integrate "
                "deliberately under the audited override." % (rel, len(foreign), len(added), who, ", ".join(foreign))], notes
    return [], notes


def _index_paths(root, patterns):
    """(paths, note): the index entries matching the pathspecs; (None, note) when git could not answer."""
    try:
        ls = subprocess.run(["git", "ls-files", "--"] + list(patterns), cwd=root, capture_output=True,
                            text=True, encoding="utf-8", errors="replace", timeout=60)
    except Exception as exc:  # noqa: BLE001
        return None, "git ls-files raised %s" % exc
    if ls.returncode != 0:
        return None, "git ls-files rc=%d: %s" % (ls.returncode, ls.stderr.strip()[:120])
    return [p.strip().replace("\\", "/") for p in ls.stdout.splitlines() if p.strip()], ""


def _is_adjudication_doc(path):
    """carrier 5 / annex 4a: the CVO's document. Its rows are ABOUT items and are not items (v3 L10 counts worker rows only)."""
    return "ADJUDICATION" in os.path.basename(str(path)).upper()


def _duplicate_ids(investigation_files):
    """PURE. {id: [paths]} for every id carried by MORE THAN ONE document of the plane (v3's first drain, 2026-09-04
    04:2xZ, 3.0.0_SA_CVO 94007: two worktrees, two indexes, one sequence -- NFRA_COMPEFFICACY-S34 minted by the CVO's
    adjudication @b50a124783 and by worker ~2 @e7dda3d93c). A repeat WITHIN one file is _mutation_violations' limb."""
    seen = {}
    for p, rows in investigation_files:
        for r in rows:
            rid = r.get("id")
            if rid and p not in seen.setdefault(rid, []):
                seen[rid].append(p)
    return {k: v for k, v in seen.items() if len(v) > 1}


def _resolve_latest(investigation_files, remediation_ids):
    """PURE. investigation_files = [(path, rows)] in path order; remediation_ids = ids of remediation rows.
    Returns (latest {item_id: disposition}, unknown [`adjudicates` targets that land on no single item]).
    ITEMS are the rows of INVESTIGATION documents. An ADJUDICATION document's rows are the CVO's rows ABOUT items
    (annex 4a): their `adjudicates` applies, their own ids are NOT items -- spine v3 L10 counts worker rows only, and
    seeding them made the CVO's own UNDER_INVESTIGATION row block the CVO's own slug (94010).
    An id carried by TWO investigation documents (the allocator race) resolves toward OPEN -- any undispositioned
    occurrence keeps it undispositioned -- and an `adjudicates` naming it is AMBIGUOUS and NOT applied (there is no
    single item to land on); the collision is reported here and by _duplicate_ids, and the corrective record is a
    NEW row. An `adjudicates` naming an adjudication row's own id is a real row, not a phantom: nothing to flip."""
    latest, carried, item_docs = {}, set(), {}
    for p, rows in investigation_files:
        adj = _is_adjudication_doc(p)
        for r in rows:
            rid = r.get("id")
            if not rid:
                continue
            carried.add(rid)
            if adj:
                continue
            item_docs.setdefault(rid, set()).add(p)
            if rid not in latest:
                latest[rid] = r.get("disposition")
            elif r.get("disposition") in UNDISPOSITIONED:
                latest[rid] = r.get("disposition")   # a second carrier that is open keeps the item open
    ambiguous = {rid for rid, docs in item_docs.items() if len(docs) > 1}
    unknown = []
    for _p, rows in investigation_files:
        for r in rows:
            for target in (r.get("adjudicates") or []):
                if target in ambiguous:
                    unknown.append("%s (by %s) -- AMBIGUOUS: %d investigation documents carry that id, so the adjudication "
                                   "lands on no single item" % (target, r.get("id"), len(item_docs[target])))
                    continue
                if target not in latest:
                    if target not in carried:
                        unknown.append("%s (by %s)" % (target, r.get("id")))
                    continue
                if r.get("disposition") in UNDISPOSITIONED:
                    # An OPEN row is its own item; its `adjudicates` never moves the target. Files fold in path order and
                    # adjudications/ sorts before investigations/, so an issuer row "adjudicating" with UNDER_INVESTIGATION
                    # overwrote the CVO's later disposition (3.0.0_SA_CVO~Z 28889: 40 of 3,886 CVO-terminal targets).
                    continue
                latest[target] = r.get("disposition")
    for rid in remediation_ids:
        if rid in latest:
            latest[rid] = "GRADUATED"
    return latest, unknown


def _latest_dispositions(root, code):
    """(latest, unknown, files_read, note) for the project's investigation items, read from the INDEX.
    latest is None when the census could not run -- the caller fails closed."""
    inv_paths, note = _index_paths(root, [p % code for p in INVESTIGATION_PATTERNS])
    if inv_paths is None:
        return None, [], 0, note
    adj_paths, note = _index_paths(root, [p % code for p in ADJUDICATION_PATTERNS])
    if adj_paths is None:
        return None, [], 0, note
    inv_paths = list(inv_paths) + [p for p in adj_paths if p not in inv_paths]   # investigations first: items are seeded there
    rem_paths, note = _index_paths(root, [p % code for p in REMEDIATION_PATTERNS])
    if rem_paths is None:
        return None, [], 0, note
    files, rem_ids = [], []
    for p in inv_paths:
        st, text = _blob(root, "", p)
        if st != "OK":
            return None, [], 0, "%s unreadable in the index (%s)" % (p, st)
        rows, bad = _rows(text, p.lower().endswith(".json"))
        if bad:
            return None, [], 0, "%s holds %d unparsed block(s)" % (p, bad)
        files.append((p, rows))
    for p in rem_paths:
        st, text = _blob(root, "", p)
        if st != "OK":
            return None, [], 0, "%s unreadable in the index (%s)" % (p, st)
        rows, bad = _rows(text, p.lower().endswith(".json"))
        if bad:
            return None, [], 0, "%s holds %d unparsed block(s)" % (p, bad)
        rem_ids.extend(r.get("id") for r in rows if r.get("id"))
    latest, unknown = _resolve_latest(files, rem_ids)
    return latest, unknown, len(files) + len(rem_paths), ""


def _gating_item_ids(root, code):
    """The ids of the investigation rows that GATE the slug (spine v3.19 L10, report 3 item 1.2): `class: BLOCKING` or
    `hazard_standing: ARMED`. An unarmed OBSERVATION row is NOTED at the round's close and counts against nothing.
    Read from the INDEX like _latest_dispositions. None when the read fails -- the caller then gates on EVERY item,
    the stricter pre-v3.19 rule, never on none."""
    inv_paths, _note = _index_paths(root, [p % code for p in INVESTIGATION_PATTERNS])
    if inv_paths is None:
        return None
    ids = set()
    for p in inv_paths:
        st, text = _blob(root, "", p)
        if st != "OK":
            return None
        rows, bad = _rows(text, p.lower().endswith(".json"))
        if bad:
            return None
        for r in rows:
            if r.get("id") and (str(r.get("class") or "").upper() == "BLOCKING"
                                or str(r.get("hazard_standing") or "").upper() == "ARMED"):
                ids.add(r["id"])
    return ids


def _remediation_ids_for_project(root, code):
    """(ids, note) -- the SET of item ids carried by a REMEDIATION row under `code`'s channel, read
    from the INDEX (never the worktree). ids is None when the census could not run -- the caller
    fails closed, exactly as `_latest_dispositions` already does on the sibling read.

    THIS IS A STANDALONE READ, NOT A SECOND RETURN VALUE BOLTED ONTO `_latest_dispositions`.
    `_resolve_latest` already folds remediation-row presence into `latest` -- it sets an item's
    resolved disposition to GRADUATED whenever a remediation row bears that id (:414-416) -- but a
    CVO row can ALSO carry `disposition: GRADUATED` directly, as its own L9 field (annex 4a, :1260),
    with NO remediation row ever minted. Both paths land on the identical string "GRADUATED" in
    `latest`, so nothing downstream of `_resolve_latest` can tell them apart; only an INDEPENDENT
    read of which ids remediation rows actually carry can (S74's structural finding). Growing
    `_latest_dispositions`'s return arity would touch every one of its existing callers and the
    self-test's literal 4-tuple fixtures for a question this gate never previously asked; a second,
    narrow read costs one census and changes nothing already wired."""
    rem_paths, note = _index_paths(root, [p % code for p in REMEDIATION_PATTERNS])
    if rem_paths is None:
        return None, note
    ids = set()
    for p in rem_paths:
        st, text = _blob(root, "", p)
        if st != "OK":
            return None, "%s unreadable in the index (%s)" % (p, st)
        rows, bad = _rows(text, p.lower().endswith(".json"))
        if bad:
            return None, "%s holds %d unparsed block(s)" % (p, bad)
        ids.update(r.get("id") for r in rows if r.get("id"))
    return ids, ""


def _remediation_rows_for_project(root, code):
    """(rows_by_id, note) -- the LATEST remediation row (the FULL dict, not just its id) per id carried
    under `code`'s REMEDIATION channel, read from the INDEX. rows_by_id is None when the census could not
    run -- the caller fails closed, the same convention as `_remediation_ids_for_project`, whose key-set
    this function's key-set equals by construction.

    A SEPARATE READ, NOT A SECOND RETURN VALUE BOLTED ONTO `_remediation_ids_for_project`: EN-k-38's
    staleness question needs the row's OWN `remediation.state`/`remediation.owner`/`remediation.round`,
    not merely that an id is carried (S74's precedent for why a narrow, independent census beats growing
    an existing one's arity). The channel is APPEND-ONLY (protocol s.0: "a correction ... is a NEW row
    citing the old id ... a reader resolves a row's state from the newest row that cites it") so the LAST
    occurrence of an id, walking `_index_paths`' file order then each file's row order, IS the newest --
    exactly the rule `_remediation_ids_for_project`'s plain `.update()` already relies on for presence;
    here the same walk keeps the row itself rather than discarding it."""
    rem_paths, note = _index_paths(root, [p % code for p in REMEDIATION_PATTERNS])
    if rem_paths is None:
        return None, note
    rows_by_id = {}
    for p in rem_paths:
        st, text = _blob(root, "", p)
        if st != "OK":
            return None, "%s unreadable in the index (%s)" % (p, st)
        rows, bad = _rows(text, p.lower().endswith(".json"))
        if bad:
            return None, "%s holds %d unparsed block(s)" % (p, bad)
        for r in rows:
            rid = r.get("id")
            if rid:
                rows_by_id[rid] = r
    return rows_by_id, ""


def _coordinate_violations(rel, folder_kind, added, committer, c_in_schema, merging=False,
                           parent_ids=None, published_ids=None):
    """PURE. THE ALLOCATOR DISCIPLINE on NEW rows (RULING 2 @9ef9a40aae; annex v3.2): a row committed by a worker
    0.9.0_WK_<CODE>~<n> carries W<n> with n EQUAL to the committer's slot (a bare S<k> from a worktree is the race the
    coordinate exists to remove; a wrong n is another worker's sequence); a seat's row carries no W; a C- row lives only
    in adjudications/ and is the CVO's; a NEW row in adjudications/ carries C- once the staged schema admits it
    (c_in_schema) -- until then the CVO's rows keep the seat form, prospective like everything in this gate.
    AT A DRAIN (merging=True, MERGE_HEAD present; 2.0.0_SA_COO~A 94157, v3's first worker drain): the committer of the
    merge commit is the DRAINING SEAT, never the allocator, so the discipline reads the ROW's own `surfaced_by` --
    the worker that minted it -- and a seat's row riding the merge is graded as a seat's. The first drain refused 15 of
    15 lawful W rows on the committer read while its own co-worker sweep admitted every one of them."""
    committer_m = WORKER_SERIAL_RE.match(str(committer or "").strip())
    # A REMEDIATION ROW *INHERITS* ITS COORDINATE; IT DOES NOT ALLOCATE ONE. This limb is the
    # ALLOCATOR discipline (see the docstring) and applying it to a remediation row asks the wrong
    # question of the wrong actor: `remediation_row.schema.json:21` says the id IS "the graduated
    # investigation item's id ... including the allocator coordinate", so a remediation for a
    # worker-minted <CODE>-W1-S43 legitimately carries W1 while being WRITTEN BY THE CVO, and a
    # remediation for the CVO's own <CODE>-C-S69 legitimately carries C- while living in
    # remediations/ rather than adjudications/. Both then refused as if the writer had minted them.
    # Measured 2026-09-10 by 3.0.0_SA_CVO on NFRA_CLDGRPH round 8: TEN coordinate refusals on one
    # 12-row REMEDIATION_v4 draft -- one C- "outside adjudications/" and nine carried W* ids -- with
    # the gate and the schema in direct contradiction on the same field. The CVO preserved the ids
    # and called it a repository contract defect rather than renumbering; it was right, and
    # renumbering would have BROKEN graduation, which resolves an item to its remediation BY ID.
    # The id/graduation tie is a DIFFERENT limb's job (_resolve_latest over rem_ids) and is untouched.
    # Ruled by 1.0.0_SA_CTO 2026-09-10 ~17:5xZ. COST: none -- one branch on a kind the gate already
    # computes. NON-APPLICATION: INVESTIGATION and ADJUDICATION documents, where a row IS minted.
    _rem_doc = (folder_kind == "REMEDIATION"
                or (folder_kind is None and _kind(rel) == "REMEDIATION"))
    out = []
    for r in added:
        rid = str(r.get("id", ""))
        m = ID_RE.match(rid)
        if not m:
            continue   # the grammar refusal is check_file's own
        if _rem_doc:
            continue   # inherited coordinate -- nothing here is an allocation claim
        w, c = m.group("w"), m.group("c")
        # BOUNDARY (b): read the ROW's surfacer only for a row a PARENT carried. A row minted IN
        # this merge is the committer's act and is graded against the COMMITTER, on a merge or off.
        _carried = bool(merging and parent_ids is not None
                        and str(r.get("id") or "").strip() in parent_ids)
        # BATCH 112: a carried row the PUBLISHED trunk already holds is another device's landed row -- noted by
        # check_file, not graded here. published_ids None (unreadable) exempts nothing.
        if _carried and published_ids is not None and str(r.get("id") or "").strip() in published_ids:
            continue
        allocator_raw = str(r.get("surfaced_by") or "").strip() if _carried else str(committer or "").strip()
        # SEAM (2026-09-10, 2.0.0_SA_COO~Z's stuck drain): `surfaced_by` legitimately carries
        # "<serial> (why it was surfaced)" -- every seat row in every channel already has that shape.
        # WORKER_SERIAL_RE is anchored ^...$, so the annotation made a WORKER's row read as a SEAT's
        # and the row became LEGAL WHERE WRITTEN (commit path grades the bare --author committer) and
        # ILLEGAL WHERE IT LANDS (drain path grades the annotated field). Grade the LEADING SERIAL,
        # which is what the docstring above always said this limb reads. A serial never contains
        # whitespace, so the first token is the whole of it.
        allocator = allocator_raw.split()[0] if allocator_raw else allocator_raw
        wm = WORKER_SERIAL_RE.match(allocator) if _carried else committer_m
        # NOTE (2026-09-10 parity merge, steward read by 1.0.0_SA_CTO~Z): a SECOND remediation guard
        # stood here on the SITEZ side (`_is_rem` -> pass, narrowing ONLY this W-arm), reached by an
        # estate census -- 195 of 195 rows lacking `surfaced_by` are remediations, 0 investigations,
        # across 13 files / 4 projects. It is REMOVED as dead code: the CLOUD side's `if _rem_doc:
        # continue` above (line ~479) subsumes it -- `_kind(rel)` there is byte-identical to this
        # predicate, and it `continue`s the whole row BEFORE this arm is reached, so this block could
        # never execute. TWO FABRICS INDEPENDENTLY GUARDED THE SAME PLANE -- CLOUD by reading
        # remediation_row.schema.json:21, SITEZ by censusing the rows -- and converged on the identical
        # fix; that convergence is the strongest evidence the guard is right. CLOUD's is kept because
        # it is the SUPERSET: it also skips the C-arm, so a remediation legitimately carrying a C- id
        # (a remediation of the CVO's own adjudication row) is admitted too -- a case the W-only
        # narrowing missed. Leaving a dead guard that READS live is the very trap this estate spent
        # the day removing, so it goes rather than lingering as a second thing to reason about.
        if wm:
            if w is None:
                out.append("%s: NEW row %s %s worker %s carries no W<n>. A worker mints <CODE>-W%s-S<k> (its own "
                           "slot, the next unused k within it); a bare S<k> from a worktree is the allocator race that "
                           "minted S34 twice at v3's first drain (94007)."
                           % (rel, rid, "surfaced by" if merging else "committed by", allocator, wm.group("n")))
            elif int(w) != int(wm.group("n")):
                out.append("%s: NEW row %s carries W%s but the %s worker %s's slot is %s -- a row is minted in "
                           "its own coordinate, never another worker's."
                           % (rel, rid, w, "surfacing" if merging else "committing", allocator, wm.group("n")))
        elif w is not None:
            out.append("%s: NEW row %s carries W%s but the %s %s is not a worker -- a seat's row on the main index "
                       "carries no W (the coordinate names the allocator, and a seat allocates on the main index)."
                       % (rel, rid, w, "surfacer" if _carried else "committer", allocator))
        if c:
            # ESTATE_GOVERNANCE-S5 (3.0.0_SA_CVO): a FLAT ADJUDICATION_v document declares its kind in
            # its FILENAME, not its folder, so _folder_identity returns None for it and this limb used to
            # refuse every C- row the CVO filed there -- on the one document only that seat writes, again.
            # The flat arm had never been exercised because no flat channel had carried a C- row before.
            _is_adj = folder_kind == "ADJUDICATION" or (folder_kind is None and _is_adjudication_doc(rel))
            if not _is_adj:
                out.append("%s: NEW row %s carries C- outside adjudications/ -- C- is the CVO's coordinate for its "
                           "adjudication rows (annex 4a) and lives nowhere else." % (rel, rid))
            else:
                # THE C- ARM UNDER merging -- the W- arm's own principle at :420, applied here
                # (3.0.0_SA_CVO 94313, the coordinate's owner stating the rule; 0.0.0_AB_MSTR 94311
                # finding the gap). On a merge the identity graded is the ROW's own surfaced_by, NEVER
                # the committer: an integrator carrying the CVO's adjudication rows forward is not
                # their author. A ~lane counts -- a 3.0.0_SA_CVO~Z row minted on the other fabric is
                # the CVO's. Off a merge the arm is unchanged: a C- row committed by anyone but the
                # CVO refuses, which is the narrowness arm in both directions.
                _c_who = str(r.get("surfaced_by") or "").strip() if _carried else committer
                if _base_serial(_c_who) != "3.0.0_SA_CVO":
                    out.append("%s: NEW row %s carries C- but the %s %s is not 3.0.0_SA_CVO."
                               % (rel, rid, "surfacer" if _carried else "committer", _c_who))
        elif (folder_kind == "ADJUDICATION" or (folder_kind is None and _is_adjudication_doc(rel))) \
                and c_in_schema:
            out.append("%s: NEW row %s in adjudications/ carries no C- while the staged schema admits it -- the CVO's rows "
                       "mint in the C- coordinate (<CODE>-C-S<k>)." % (rel, rid))
    return out


def _merge_in_progress(root):
    """True iff MERGE_HEAD exists -- the commit about to be created is a merge and its committer is the draining seat,
    not the rows' allocator (the same predicate .tools/git-hooks/owned-paths-check.sh:73 exempts a merge on)."""
    try:
        r = subprocess.run(["git", "rev-parse", "-q", "--verify", "MERGE_HEAD"], cwd=root, capture_output=True,
                           text=True, encoding="utf-8", errors="replace", timeout=20)
    except Exception:  # noqa: BLE001
        return False
    return r.returncode == 0 and bool(r.stdout.strip())


def _carried_decision(staged_blob, other_blob, local_commits):
    """PURE. True iff a merge only CARRIES a channel file (3.0.0_SA_CVO ruling @6166eb7b25,
    CVO_RULING_ROW_GATE_MERGE_CARRIED_NOT_MADE_20261003.md, on 1.0.0_SA_CTO batch 234 item 4): (a) the merged blob is the
    OTHER parent's byte for byte, and (b) the local side made no commit to the file since the merge-base. An empty blob id
    is a read that failed, and a failed read is never "carried"."""
    return bool(staged_blob) and staged_blob == other_blob and local_commits == 0


def _carried_from_other_parent(root, rel):
    """(carried, other_side_commits) for ONE channel file on a merge in progress; (False, []) on anything else.

    WHY (0.0.0_AB_MSTR 104796/104801): the laptop's pull of origin was refused because origin had mutated and deleted
    AMGT_HARVST rows on Andrew's site-Z order ("summarily delete this context rot"). The laptop made no commit to those
    files, so the merge did not make the change; it only carried it, and on a merge there is no override path (see the
    BLOCKED print in main). Fail-closed: a conflicted index entry (stage != 0), any git error or an unparseable answer
    returns not-carried, and the change is refused exactly as before. COST: five git reads, only when the mutation limb
    already fired on a merge. NON-APPLICATION: every non-merge commit; a file the merge made or a conflict resolved; a file
    the local side also touched."""
    if not _merge_in_progress(root):
        return (False, [])

    def _git(*args):
        r = subprocess.run(["git"] + list(args), cwd=root, capture_output=True, text=True, encoding="utf-8",
                           errors="replace", timeout=30)
        return r.returncode, r.stdout.strip()

    try:
        rc1, staged = _git("ls-files", "-s", "--", rel)          # "<mode> <sha> <stage>\t<path>", one line when resolved
        rc2, other = _git("ls-tree", "MERGE_HEAD", "--", rel)     # "<mode> blob <sha>\t<path>"
        rc3, base = _git("merge-base", "HEAD", "MERGE_HEAD")
        if rc1 or rc2 or rc3 or not base or "\n" in staged:
            return (False, [])
        rc4, local = _git("rev-list", "--count", "%s..HEAD" % base, "--", rel)
        rc5, theirs = _git("log", "--format=%h", "%s..MERGE_HEAD" % base, "--", rel)
        if rc4 or rc5:
            return (False, [])
        sp, op = staged.split(), other.split()
        s_sha = sp[1] if len(sp) >= 3 and sp[2] == "0" else ""
        o_sha = op[2] if len(op) >= 3 and op[1] == "blob" else ""
        n_local = int(local)
    except Exception:  # noqa: BLE001
        return (False, [])
    if not _carried_decision(s_sha, o_sha, n_local):
        return (False, [])
    return (True, theirs.split())


def _plane_patterns(kind):
    """The documents that share ONE id sequence: the investigation plane (investigations + the CVO's adjudications) or
    the remediation plane. ACROSS planes ids collide BY DESIGN (a remediation row bears its graduated item's id)."""
    if kind == "REMEDIATION":
        return REMEDIATION_PATTERNS
    return INVESTIGATION_PATTERNS + ADJUDICATION_PATTERNS


def _plane_docs(root, code, kind, exclude_rel):
    """([(path, {ids})], note) for every OTHER document of the plane under the project, read from the INDEX;
    (None, note) when the census could not run -- the caller fails closed."""
    paths, note = _index_paths(root, [p % code for p in _plane_patterns(kind)])
    if paths is None:
        return None, note
    docs, ex = [], exclude_rel.replace("\\", "/")
    for p in paths:
        if p == ex:
            continue
        st, text = _blob(root, "", p)
        if st != "OK":
            return None, "%s unreadable in the index (%s)" % (p, st)
        rows, bad = _rows(text, p.lower().endswith(".json"))
        if bad:
            return None, "%s holds %d unparsed block(s)" % (p, bad)
        docs.append((p, {r.get("id") for r in rows if r.get("id")}))
    return docs, ""


def _plane_duplicates(root, code):
    """({id: [paths]}, note) over the project's investigation plane in the INDEX; (None, note) when it could not run."""
    docs, note = _plane_docs(root, code, "INVESTIGATION", "")
    if docs is None:
        return None, note
    return _duplicate_ids([(p, [{"id": i} for i in sorted(ids)]) for p, ids in docs]), ""



# THE ONE DECLARED DUPLICATE-ID BASELINE (3.0.0_SA_CVO 94346). EXACT, not a pattern: this id, in
# THESE TWO documents, and nowhere else -- keyed the way surprise-corpus-validate keys its four
# legacy failures (a known pair admitted, anything NEW refuses).
# WHY IT MUST EXIST: without it, EVERY fabric's first merge of this history refuses once on a defect
# the record already closed. That is what happened to site Z's return leg.
# RESOLVED ON THE RECORD BY C-S2 @f4b41b1c20: it adjudicates the WORKER's S34 and states that the
# adjudication document's own S34 is a CVO row and NOT an item under the census fix @72d05b2642, so
# the id resolves to the worker's. S37 and S38 cite it.
# MINTED @b50a124783 (3.0.0_SA_CVO, adjudications/, BEFORE the C- coordinate existed at annex v3.3)
#    and @e7dda3d93c (0.9.0_WK_NFRA_COMPEFFICACY~2, investigations/).
# NOT REPAIRABLE: re-iding either row is an in-place edit of an id in an APPEND-ONLY channel -- the
# mutation this gate refuses and the class the channel exists to prevent; a new row cannot unmint an
# old id. 0.0.0_AB_MSTR routed rather than repaired and was right to.
_DUPLICATE_ID_BASELINE = {
    "NFRA_COMPEFFICACY-S34": frozenset({
        "org/missions/D11/NFRA/NFRA_COMPEFFICACY/surprise-channel/adjudications/ADJUDICATION_v1.md",
        "org/missions/D11/NFRA/NFRA_COMPEFFICACY/surprise-channel/investigations/INVESTIGATION_v1.md",
    }),
}


def _duplicate_is_declared(rid, docs):
    """True iff this id AND the COMPLETE set of documents carrying it are the declared pair.

    The whole collision must sit inside the declared set: S34 in a THIRD document is a NEW collision
    and refuses. The baseline is a fact about two files, never an amnesty for an id.
    """
    known = _DUPLICATE_ID_BASELINE.get(str(rid or "").strip())
    if not known:
        return False
    return {str(d).replace("\\", "/") for d in docs} <= known

def _duplicate_id_violations(rel, kind, added, code, plane_docs, note=""):
    """PURE given `plane_docs`. UNIQUENESS ACROSS DOCUMENTS (2026-09-04, 3.0.0_SA_CVO 94007, v3's first drain): a NEW
    row's id must exist in NO other document of its plane under the project at the graded index. Two worktrees, two
    indexes, one sequence minted NFRA_COMPEFFICACY-S34 twice (@b50a124783 in adjudications/, @e7dda3d93c in
    investigations/); the drain merged the union without a gate and the rollup let the last-read document win. This
    limb refuses what THIS index carries -- a worker's worktree index cannot see the main index's allocations, so the
    drain grades the MERGED index (the COO's half, /dispatch Step 5) and an allocator coordinate in the id (the annex's
    Z- precedent) removes the race; neither is this limb. None = the census could not run -> refused, fail-closed."""
    if not added:
        return [], []
    if plane_docs is None:
        return ["%s: the id-uniqueness census over %s's %s plane could NOT run (%s) -- REFUSED, fail-closed"
                % (rel, code, kind.lower(), note or "no reason given")], []
    out, notes = [], []
    for r in added:
        rid = r.get("id")
        if not rid:
            continue
        hits = [p for p, ids in plane_docs if rid in ids]
        if hits and _duplicate_is_declared(rid, list(hits) + [rel]):
            # DECLARED, AND SAID OUT LOUD. A pass that hides a known collision is the vacuous-pass
            # class; the note carries the resolving record so the reader meets the adjudication.
            notes.append("%s: %s is the DECLARED duplicate-id baseline -- two allocators, one sequence, minted "
                         "@b50a124783 and @e7dda3d93c before the C- coordinate existed; RESOLVED on the record by "
                         "C-S2 @f4b41b1c20 and not repairable in an append-only channel. Admitted here; a THIRD "
                         "document carrying this id, or any other duplicate, still REFUSES." % (rel, rid))
            continue
        if hits:
            out.append("%s: NEW row %s -- that id already exists in %s (the same plane of %s's channel, at the graded "
                       "index). An id is ONE row across the project's documents; mint the next unused number over EVERY "
                       "document of the plane (ids are permanent and never renumbered, @b3584ea86a). Two allocators "
                       "minting one sequence is the collision the CVO measured at v3's first drain (94007)."
                       % (rel, rid, ", ".join(hits), code))
    return out, notes


def _parent_row_ids(root, rel):
    """(ids, note): every row id the MERGE'S PARENTS carry in `rel`, or (None, note) if unreadable.

    BOUNDARY (b), 3.0.0_SA_CVO 94299. The parents are HEAD (this branch) and MERGE_HEAD (the branch
    being merged). A row whose id appears in either was CARRIED by the merge; a row in neither was
    MINTED in the merge commit and is the merging seat's own act.

    None on failure, never an empty set: "the parents carry nothing" and "the parents could not be
    read" are different answers and only one of them may exempt a row. The callers fail closed.
    """
    ids, notes = set(), []
    for ref in ("HEAD", "MERGE_HEAD"):
        st, text = _blob(root, ref, rel)
        if st == "ERROR":
            return None, "%s unreadable at %s" % (rel, ref)
        if st == "ABSENT" or not text:
            continue          # a parent that never had this file carries no ids from it
        rows, _bad = _rows(text, rel.lower().endswith(".json"))
        for r in rows:
            rid = str((r or {}).get("id") or "").strip()
            if rid:
                ids.add(rid)
    return ids, "; ".join(notes)


# The ONE published trunk both devices commit to (LD-0613). Not a device fact: the ref name is the same on both.
PUBLISHED_REF = "refs/remotes/origin/CLOUD"
# PER-BOX BRANCHES (2026-10-08, build item B1, 1.0.0_SA_CTO PER_BOX_BRANCH_BUILD_PLACEMENT_20261008.md; Andrew ~18:0xZ):
# a box branch on origin is PUBLISHED too. Its rows were graded when its box committed them, and the integrator that
# merges it into CLOUD cannot re-mint them; with CLOUD alone as "published", every integration of a box branch that
# carries a new row would be refused at the integrator. The union below is a no-op while no origin/box/* ref exists.
PUBLISHED_BOX_PREFIX = "refs/remotes/origin/box/"


def _published_refs(root):
    """origin/CLOUD first, then every origin/box/* ref. A failed listing yields CLOUD alone (today's behaviour)."""
    refs = [PUBLISHED_REF]
    try:
        r = subprocess.run(["git", "for-each-ref", "--format=%(refname)", PUBLISHED_BOX_PREFIX], cwd=root,
                           capture_output=True, text=True, encoding="utf-8", errors="surrogateescape", timeout=60)
        if r.returncode == 0:
            refs.extend(x.strip() for x in r.stdout.splitlines() if x.strip())
    except Exception:  # noqa: BLE001
        pass
    return refs


def _published_row_ids(root, rel):
    """Every row id the PUBLISHED trunk carries in `rel`, or None if unreadable (the caller then exempts nothing).

    WHY (1.0.0_SA_CTO, IRPT RULINGS batch 112, 0.0.0_AB_MSTR 104055): the coordinate limb grades a row a merge
    parent carries by its own surfaced_by. That is right at a WORKER DRAIN -- the worker branch is unpublished and
    its rows are graded once, there. But a row the published trunk ALREADY carries was landed by another device's
    push: the merging device cannot re-mint it, and refusing it blocks every later integration of origin (row
    NFRA_OPALAI-Z-S55, a worker row without W<n> landed on origin by site Z @9c392a7db9). Such a row is NOTED, not
    refused. A worker's unpublished drain row is never on this ref, so drains are graded exactly as before.
    COST: one git read per channel file per merge. NON-APPLICATION: off a merge; a row minted in the merge commit
    (in neither parent); every limb other than the coordinate discipline.
    """
    ids = set()
    for ref in _published_refs(root):
        st, text = _blob(root, ref, rel)
        if st == "ERROR":
            if ref == PUBLISHED_REF:
                return None          # the trunk unreadable: exempt nothing, exactly as before
            continue                 # an unreadable box ref only narrows the exemption, never widens it
        if st == "ABSENT" or not text:
            continue
        rows, _bad = _rows(text, rel.lower().endswith(".json"))
        ids |= {str((r or {}).get("id") or "").strip() for r in rows} - {""}
    return ids


def _row_is_other_fabric(row):
    """True iff the row's id carries the `Z-` coordinate segment. NOT A FABRIC TEST. NOT A DECISION.

    BLOCKED: RETIRED AS A DISCRIMINATOR 2026-09-11 AND DELIBERATELY LEFT UNUSED -- DO NOT REACH FOR IT.
    It decided the L10 merge exemption in both precondition limbs until Andrew's ~19:3xZ scoping
    ("the surprise-row gate must be project specific") replaced it with `_row_was_carried`. Read that
    function for the rule that actually holds.

    THE DOCSTRING THIS ONE REPLACES WAS FALSE ON HALF THE ESTATE, and the falsity is the whole
    lesson: it said "a row without [`Z-`] is THIS fabric's record". That is true ON THE LAPTOP and
    INVERTED ON SITE Z, because the sentence names no vantage point and the name `other_fabric`
    silently assumes one. A CONSTANT CANNOT ANSWER "WHICH FABRIC AM I" -- only the device can. Cost:
    100 already-committed laptop rows arriving by an authorised CLOUD->SITEZ merge read as native
    here, and the gate refused the leg while citing Andrew correctly.

    What it still says CORRECTLY is the narrow syntactic fact: an id is
    `<CODE>-(Z-)?(W<n>-|C-)?S<k>` and this returns whether the `Z-` segment is present. That is a
    statement about the STRING, never about which machine is asking. Unparseable -> False.
    A self-test arm asserts this name appears in NEITHER precondition limb.
    """
    m = ID_RE.match(str((row or {}).get("id") or "").strip())
    return bool(m and m.group("z"))


def _row_was_carried(row, parent_ids):
    """True iff this row's id is present in the MERGE'S PARENTS -- history arriving, not an act.

    THE L10 PRECONDITION IS A CONDITION ON A ROUTING ACT (Andrew, LD-0521, @716a9bc7ce call 3: "We do
    not route until the job is over"). A row the merge CARRIES was routed by whoever minted it, under
    whatever preconditions held at that seat; the merge only re-states it in this branch's record. A
    row MINTED in the merge commit is the merging seat's OWN routing act, and the precondition binds
    it in full.

    THIS REPLACES A FABRIC CONSTANT -- `_row_is_other_fabric`, the `Z-` coordinate -- IN BOTH
    PRECONDITION LIMBS. That test could not be right on both boxes at once: its own docstring says a
    row without `Z-` is "THIS fabric's record", which is true on the laptop and INVERTED on site Z. So
    100 already-committed laptop rows arriving by merge read as native here and refused an authorised
    CLOUD->SITEZ leg, with the gate's refusal text citing Andrew correctly the whole time. A guard
    whose truth depends on which machine runs it is not a guard.
    Andrew-direct 2026-09-11 ~19:3xZ, VERBATIM: "the surprise-row gate must be project specific".
    Provenance is both project-agnostic and fabric-agnostic, so it is correct on either box without a
    device lookup and without a second carrier of "which fabric am I" to drift.

    NOT AN INVENTION -- `_coordinate_violations` and the foreign-row sweep ALREADY decide carried-vs-
    minted from `_parent_row_ids`, on the same `_pids` read. This makes two limbs consistent with two
    others rather than adding a test.

    FAIL-CLOSED: `parent_ids` None -- no merge, or parents unreadable -- exempts NOTHING.
    `_parent_row_ids` returns None rather than an empty set precisely so that "the parents carry
    nothing" and "the parents could not be read" stay different answers, and only one of them may
    exempt a row.
    """
    if parent_ids is None:
        return False
    rid = str((row or {}).get("id") or "").strip()
    return bool(rid) and rid in parent_ids


def _investigations_precondition_violations(rel, row, code, route_word, dispositions, merging=False,
                                            parent_ids=None, gating=None, watermark=None, surfaced_at=None):
    """GATE (iii) second limb for ONE new route-carrying row. `dispositions` is the 4-tuple from
    _latest_dispositions (injectable for the self-test).

    AT A MERGE: not evaluated -- see the block below and _route_precondition_violations' twin."""
    if merging and _row_was_carried(row, parent_ids):
        # CARRIED BY THE MERGE == HISTORY ARRIVING, NOT A ROUTING ACT (see _row_was_carried).
        # SUPERSEDES THE PER-FABRIC COORDINATE TEST (3.0.0_SA_CVO 94337) ON ANDREW'S ~19:3xZ SCOPING.
        # That ruling was right that the blanket merge exemption was too wide, and right that each
        # fabric's CVO slugs its own projects; the defect was the PROXY it used. `Z-` names WHICH BOX
        # minted a row, and the gate needs to know WHETHER THIS COMMIT MINTED IT -- on the laptop the
        # two coincide, on site Z they invert. Provenance answers the question the proxy was standing
        # in for, on both boxes.
        # A row MINTED in the merge commit falls through and BINDS -- including a `Z-` row, which the
        # old test would have exempted. So does any row whose parents could not be read.
        # No violations. The ANNOUNCEMENT is the caller's note, one per row-bearing file.
        return []
    rid = row.get("id", "<no id>")
    latest, unknown, nfiles, note = dispositions
    if latest is None:
        return ["%s: the L10 precondition (every investigation item under %s dispositioned) could NOT be "
                "evaluated (%s) -- REFUSED, fail-closed" % (rid, code, note)]
    out = []
    if unknown:
        out.append("%s: `adjudicates` names %s -- an adjudication that lands on no single item under %s (a phantom "
                   "id, or an id two investigation documents carry) is refused" % (rid, ", ".join(unknown), code))
    open_items = sorted(k for k, v in latest.items() if v in UNDISPOSITIONED)
    if gating is not None:
        # spine v3.19 (report 3 item 1.2): only BLOCKING or ARMED rows hold the slug; `gating` None = every item gates.
        open_items = [k for k in open_items if k in gating]
    if open_items and watermark is not None:
        # THE SWEEP WATERMARK (see SWEEP_WATERMARK_RE): an item surfaced after the slug's declared cut is the next
        # sweep's. `surfaced_at` is injected by the caller (PURE here); a missing entry holds the slug.
        open_items, _after = _split_by_watermark([(k, (surfaced_at or {}).get(k)) for k in open_items], watermark)
    if open_items:
        out.append("%s: NEW row (%s) while %d of %d BLOCKING/ARMED-or-ungraded investigation item(s) under %s are NOT "
                   "dispositioned (latest carrier reads UNDER_INVESTIGATION): %s. The slug waits until every "
                   "investigation is CVO-checked; an existing item is dispositioned by a NEW row that names it in "
                   "`adjudicates` (spine L10 precondition; Andrew-direct 2026-09-03 'Recs approved')."
                   % (rid, route_word, len(open_items), len(latest), code, ", ".join(open_items)))
    return out


def _graduated_without_row(latest, remediation_ids):
    """PURE. `latest` is the {item_id: disposition} dict `_resolve_latest`/`_latest_dispositions`
    already produce; `remediation_ids` is the set of item ids a REMEDIATION row under the project
    actually carries (`_remediation_ids_for_project`). Returns the sorted list of item ids whose
    LATEST disposition is GRADUATED while NO remediation row bears that id -- S74's structural
    finding stated as a predicate: `_resolve_latest` writes "GRADUATED" onto `latest[rid]` either
    because a remediation row exists (the automatic path, :414-416) OR because the CVO put
    `disposition: GRADUATED` directly on the investigation row itself at L9 (annex 4a, :1260) with
    no remediation row ever minted -- and the two paths are indistinguishable from `latest` alone,
    which is why this function takes the independent remediation census as a second argument rather
    than re-deriving it. `latest is None` or `remediation_ids is None` (either census could not run)
    returns None, never an empty list -- "could not check" and "checked, none missing" must not
    collapse into the same value, the same fail-closed discipline `_investigations_precondition_
    violations` already applies to `latest is None` two functions above."""
    if latest is None or remediation_ids is None:
        return None
    return sorted(rid for rid, disp in latest.items() if disp == "GRADUATED" and rid not in remediation_ids)


def _graduated_without_row_violations(rel, row, code, route_word, dispositions, remediation_census,
                                      merging=False, parent_ids=None):
    """THE SLUG-TIME LIMB (EN-g-37, S74): refuses a NEW route-carrying row -- the slug -- while a
    GRADUATED item under `code` carries no remediation row. `dispositions` is the 4-tuple from
    `_latest_dispositions` (injectable, same convention as `_investigations_precondition_
    violations`); `remediation_census` is the (ids, note) tuple from `_remediation_ids_for_project`
    (injectable the same way).

    WHY THIS MATTERS STRUCTURALLY, NOT JUST AS A RULE: this gate already grades a NEW remediation
    row as the slug act (module docstring, "carrier 6 of eight"), so a remediation row for a missed
    clock can only ever be written INSIDE a round's own slug commit or a LATER round's. A round that
    closes its slug without one leaves the item invisible to every later round that has no reason to
    look at it -- 14 of 16 known instances trace to exactly the two rounds where this was not run.

    AT A MERGE: a CARRIED row is not evaluated -- see `_row_was_carried` and the twin limbs' twin
    blocks; a row MINTED in the merge commit is the merging seat's own routing act and binds."""
    if merging and _row_was_carried(row, parent_ids):
        return []
    rid = row.get("id", "<no id>")
    latest, unknown, nfiles, note = dispositions
    if latest is None:
        return ["%s: the rowlessness precondition (every GRADUATED item under %s carries a "
                "remediation row) could NOT be evaluated (%s) -- REFUSED, fail-closed" % (rid, code, note)]
    rem_ids, rnote = remediation_census
    if rem_ids is None:
        return ["%s: the rowlessness precondition (every GRADUATED item under %s carries a "
                "remediation row) could NOT be evaluated -- the remediation census failed (%s) "
                "-- REFUSED, fail-closed" % (rid, code, rnote)]
    rowless = _graduated_without_row(latest, rem_ids)
    if not rowless:
        return []
    return ["%s: NEW row (%s) while %d GRADUATED item(s) under %s carry NO remediation row: %s. "
            "A missed clock cannot be written outside a round once its slug closes -- the row goes "
            "in BEFORE this commit, in the SAME slug (S74)." % (rid, route_word, len(rowless), code, ", ".join(rowless))]


def _round_num(v):
    """int from a `vN` round token (`remediation.round`, or a row's own `round`), or None when it does
    not parse -- never raises. PURE, and deliberately permissive about WHAT it is handed: the caller
    decides whose round field this reads."""
    m = re.match(r"^v([0-9]+)$", str(v or ""))
    return int(m.group(1)) if m else None


def _stale_open_row(rows_by_id, current_round, n_rounds):
    """PURE. rows_by_id is the {id: row} dict `_remediation_rows_for_project` produces (the LATEST
    remediation row per id, by construction -- the row EXISTS, which is exactly why EN-g-37's
    rowlessness limb can never see it, S75's own class). current_round is the int round number of THIS
    slug (read from the NEW remediation row's own `round`, e.g. 8 from "v8"); n_rounds is the threshold N
    -- a JUDGMENT call the caller supplies (STALE_OPEN_ROW_N_ROUNDS), never derived by this function.

    Returns the sorted list of ids whose LATEST remediation row is `remediation.state == "OPEN"`, carries
    a non-empty `remediation.owner`, AND whose own `remediation.round` sits `n_rounds` or more rounds
    behind `current_round` -- OPEN, OWNED, UNMOVED, stated as a predicate.

    `rows_by_id is None`, `current_round is None` or `n_rounds is None` (any input could not be produced)
    returns None, never an empty list -- "could not check" and "checked, none stale" must not collapse
    into the same value, the same fail-closed discipline its sibling rowlessness core already applies."""
    if rows_by_id is None or current_round is None or n_rounds is None:
        return None
    out = []
    for rid, row in rows_by_id.items():
        rem = row.get("remediation") if isinstance(row, dict) else None
        if not isinstance(rem, dict):
            continue
        if rem.get("state") != "OPEN":
            continue
        if not str(rem.get("owner", "")).strip():
            continue
        row_round = _round_num(rem.get("round"))
        if row_round is None:
            continue
        if current_round - row_round >= n_rounds:
            out.append(rid)
    return sorted(out)


def _stale_open_row_violations(rel, row, code, route_word, remediation_rows, n_rounds=STALE_OPEN_ROW_N_ROUNDS,
                               merging=False, parent_ids=None):
    """THE STALENESS LIMB (EN-k-38, S75): refuses a NEW remediation row -- the slug -- while an EXISTING
    remediation row under `code` sits OPEN, carries a named owner, and has not moved for `n_rounds` or
    more rounds measured against THIS slug's own round. `remediation_rows` is the (rows_by_id, note)
    tuple from `_remediation_rows_for_project` (injectable, same convention as the sibling census EN-g-37
    uses).

    WHY THIS IS A DIFFERENT QUESTION FROM ITS SIBLING ROWLESSNESS LIMB (EN-g-37), NOT THE SAME ONE
    TWICE: that limb asks whether a remediation row EXISTS for a GRADUATED item; this one asks whether
    an EXISTING remediation row has MOVED. A check scoped to rowlessness cannot see a defect in a row
    that is present (Rule 22's shared-blindness clause) -- W7-S1 survived eight rounds because every
    instrument that looked asked only the first question, and the row was never missing.

    THE ROUND COMES FROM THE ROW BEING COMMITTED, NOT FROM A CLOCK: a remediation row's own `round`
    field IS the slug's round (schema-required, `^v[0-9]+$`); reading it off the row under grading keeps
    this limb PURE and POSITION-INDEPENDENT the same way its sibling is, with no wall-clock dependency.

    AT A MERGE: a CARRIED row is not evaluated -- see `_row_was_carried` and the twin limb's twin block;
    a row MINTED in the merge commit is the merging seat's own routing act and binds.

    RETURNS (violations, notes). THE STALE-SET BRANCH DISCLOSES; THE TWO EVALUABILITY BRANCHES REFUSE, and
    the split is not a softening -- it is the rule 1.0.0_SA_CTO ruled after this limb deadlocked round 8's
    L10 against its sibling: A GATE REFUSES AN ACT ONLY WHEN THAT ACT CAN REMEDY THE GATE'S CONDITION;
    WHEN IT CANNOT, THE GATE DISCLOSES.

      - census unreadable  -> REFUSE. The channel file the writer is editing is the one that failed to
                             parse; the committing act CAN fix it. Coupled, so fail-closed stands.
      - `round` unparseable -> REFUSE. It is a defect in THIS row, which the writer owns outright.
      - N rows are stale    -> DISCLOSE. The stale rows belong to OTHER items, frequently to OTHER SEATS,
                             and NO SINGLE SLUG CAN MOVE THEM. Measured 2026-09-18 on the first slug this
                             pair ever graded: the sibling rowlessness limb DEMANDED 8 new rows and this
                             limb refused all 8 as new rows, against 91 stale rows accumulated over eight
                             rounds that predate this limb entirely. There was no ordering of the slug
                             author's own acts that cleared it, so as a refusal this limb blocked EVERY
                             slug on the project indefinitely rather than only that one.

    S75's finding is fully served by disclosure: its whole point was that a row which EXISTS but has not
    MOVED is invisible to every instrument that looks, and a printed stale set at slug time is exactly the
    look nobody was taking. A REFUSAL FORM needs a reachable remedy first -- a backlog-clearing cell with
    an owner -- and that is a later round's work, not a condition on this one's slug."""
    if merging and _row_was_carried(row, parent_ids):
        return [], []
    rid = row.get("id", "<no id>")
    current_round = _round_num(row.get("round"))
    rows_by_id, rnote = remediation_rows
    if rows_by_id is None:
        return ["%s: the staleness precondition (every OPEN, owned remediation row under %s has moved "
                "within %d round(s)) could NOT be evaluated -- the remediation census failed (%s) -- "
                "REFUSED, fail-closed" % (rid, code, n_rounds, rnote)], []
    if current_round is None:
        return ["%s: NEW row (%s) carries no parseable `round` (round=%r) -- the staleness precondition "
                "needs the slug's own round to measure a gap against, so this REFUSES rather than skip "
                "the check" % (rid, route_word, row.get("round"))], []
    stale = _stale_open_row(rows_by_id, current_round, n_rounds)
    if not stale:
        return [], []
    return [], ["%s: STALENESS DISCLOSED (not a refusal) -- %d OPEN, owned remediation row(s) under %s "
                "have not moved for %d or more round(s): %s. A row that EXISTS, is OPEN and is OWNED goes "
                "stale silently and no rowlessness limb will ever see it (S75). THIS SLUG IS NOT REFUSED "
                "FOR IT: these rows are other items', often other seats', and no single slug can move "
                "them -- clearing them needs its own cell with an owner."
                % (rid, len(stale), code, n_rounds, ", ".join(stale))]


def _proof_verdict(root, inst, rel, _run=None):
    """(True, note) when proof-of-spec-check reads the instance `inst` VALID with `rel` bound as its governing order.

    THE INVOCATION IS THE FLIP LIMB'S, NOT A COPY OF ITS RULE: to-pipeline-gate.py's terminal-flip limb runs exactly
    `python .tools/proof-of-spec-check.py <instance> --governing-order <order>` before it admits a flip to complete.
    So "terminal by proof" here means "the gate that grades flips would admit this order's flip right now". `_run` is
    injectable for the self-test. Anything but rc=0, including a checker that raises, leaves the order OPEN: when the
    proof cannot be read, the status word still governs, as it did before this limb existed."""
    chk = os.path.join(root, ".tools", "proof-of-spec-check.py")
    if not os.path.isfile(chk):
        return False, "proof-of-spec-check.py is missing"
    run = _run or (lambda argv: subprocess.run(argv, cwd=root, capture_output=True, text=True, encoding="utf-8",
                                               errors="replace", timeout=180))
    try:
        r = run(["python", chk, os.path.join(root, inst), "--governing-order", rel])
    except Exception as exc:  # noqa: BLE001
        return False, "the checker raised %s" % exc
    if r.returncode == 0:
        return True, "%s VALID with --governing-order %s" % (inst, rel)
    lines = (r.stdout or r.stderr or "").strip().splitlines()
    return False, "%s: checker rc=%d (%s)" % (inst, r.returncode, lines[-1][:120] if lines else "no output")


def _proof_terminal(root, rel, order_text, merging=False, _run=None):
    """(True, note) when the order at `rel` is terminal BY ITS PROOF although its <status> word is not terminal.

    THE SPINE READS TERMINALITY FROM THE PROOF, NEVER FROM THE STATUS FIELD (CANONICAL_FABRIC_WORKFLOW_20260901.md
    :436, the L10 precondition, "each finished with a valid proof-of-spec instance"; :487-488, "from the proof-of-spec
    instances at HEAD and never from a `<status>` field"). This gate read only the status word, so an order whose
    criterion FAILED on a VALID proof, a measurement the round exists to take, stayed `pending` and refused every
    remediation row of its project (LGIC_NAMING round 1: LN-e-3, LN-e-5 and LN-l-3 held 20 rows until the issuer flipped
    them by 1.0.0_SA_CTO's RULING T). Parked by 1.0.0_SA_CTO until LGIC_NAMING's round-2 recut was issued; it was.

    ONLY WIDENS: this runs only for an order whose status word is NOT terminal. An order whose word IS terminal reads
    terminal exactly as before, even with no instance. The spine says that case is not terminal; tightening it
    would strand rows across every project that closed orders by the word, so it is a named residual, not done here.

    The instance lookup is the flip limb's naming (to-pipeline-gate.py: <stem>.proof_of_spec.json or
    <stem>_PROOF_OF_SPEC.json; tree `deliverables/*/`, flat `task_orders` -> `deliverables`), restricted to TRACKED
    files present at the read ref (HEAD, or the merged index at a merge). More than one candidate is ambiguous and
    leaves the order OPEN. THE CHECKER READS THE WORKTREE, so both the instance and the order must match the read ref
    (line endings normalised); otherwise the verdict would describe the worktree, not the record, and the order
    stays OPEN."""
    ref = "" if merging else "HEAD"
    where = "the merged index" if merging else "HEAD"
    stem = os.path.basename(rel).rsplit(".md", 1)[0]
    names = (stem + ".proof_of_spec.json", stem + "_PROOF_OF_SPEC.json")
    to_dir = os.path.dirname(rel).replace("\\", "/")
    if to_dir.endswith("/task-orders"):
        specs = ["%s/deliverables/*/%s" % (to_dir[:-len("/task-orders")], n) for n in names]
    else:
        specs = ["%s/%s" % (to_dir.replace("task_orders", "deliverables"), n) for n in names]
    try:
        ls = subprocess.run(["git", "ls-files", "--"] + specs, cwd=root, capture_output=True, text=True,
                            encoding="utf-8", errors="replace", timeout=60)
    except Exception as exc:  # noqa: BLE001
        return False, "instance census raised %s" % exc
    if ls.returncode != 0:
        return False, "instance census rc=%d" % ls.returncode
    cands = sorted({p.strip().replace("\\", "/") for p in ls.stdout.splitlines() if p.strip()})
    if not cands:
        return False, "no proof-of-spec instance tracked"
    if len(cands) > 1:
        return False, "%d instances (%s) -- ambiguous, the status word governs" % (len(cands), ", ".join(cands))
    inst = cands[0]
    st, itext = _blob(root, ref, inst)
    if st != "OK":
        return False, "%s not readable at %s (%s)" % (inst, where, st)
    for p, blob_text in ((inst, itext), (rel, order_text)):
        try:
            with open(os.path.join(root, p), "r", encoding="utf-8", errors="surrogateescape", newline="") as fh:
                wt = fh.read()
        except OSError as exc:
            return False, "%s unreadable in the worktree (%s)" % (p, exc)
        if wt.replace("\r\n", "\n") != (blob_text or "").replace("\r\n", "\n"):
            return False, "%s in the worktree differs from %s -- the checker would grade the worktree" % (p, where)
    return _proof_verdict(root, inst, rel, _run=_run)


_OPEN_TOS_CACHE = {}


def _open_tos_for_project(root, code, merging=False, round_n=None):
    """The census below, read ONCE per (root, code, merging, round_n) per gate run. The caller asks per NEW remediation
    row plus once for its notes, so a 20-row slug would otherwise re-run the same proof-of-spec checks up to 40 times.
    HEAD and the index do not move inside one gate process, so the first answer is the answer."""
    key = (root, code, bool(merging), round_n)
    if key not in _OPEN_TOS_CACHE:
        _OPEN_TOS_CACHE[key] = _open_tos_census(root, code, merging=merging, round_n=round_n)
    return _OPEN_TOS_CACHE[key]


POINTER_OVERRIDE_RE = re.compile(r"^#\s*pipeline-override:\s*this file is a POINTER\b", re.M)


def _is_pointer_text(text):
    """True for a seat-home POINTER file (CTO ruling R2): not an order, never counted by the open-order census."""
    first = next((ln for ln in text.splitlines() if ln.strip()), "")
    return bool(POINTER_OVERRIDE_RE.search(text)) or first.startswith("# POINTER (not an order)")


TO_ROUND_RE = re.compile(r"^\s*<round>\s*v?([0-9]+)", re.I | re.M)


def _open_tos_census(root, code, merging=False, round_n=None):
    """(open_ids, total, note): the project's task orders on BOTH roots (tracked at HEAD) that are not terminal.

    An order is terminal when its <status> word is terminal, OR when its proof-of-spec instance reads VALID bound to
    it (_proof_terminal: the spine's rule, widening only). `note` names every order admitted by the second path, so
    the widening is visible wherever the census is reported. open_ids is None when the census could not run -- the
    caller fails closed. The open_ids label shape `<basename> [<word>]` is unchanged (the POSN_ASTTAX round-2
    exception matches on it)."""
    try:
        ls = subprocess.run(["git", "ls-files", "--", "*/task_orders/%s.*.md" % code,
                             "org/missions/D*/*/%s/task-orders/*.md" % code],
                            cwd=root, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=60)
    except Exception as exc:  # noqa: BLE001
        return None, 0, "git ls-files raised %s" % exc
    if ls.returncode != 0:
        return None, 0, "git ls-files rc=%d: %s" % (ls.returncode, ls.stderr.strip()[:120])
    paths = [p.strip().replace("\\", "/") for p in ls.stdout.splitlines() if p.strip()]
    open_ids, proven, pointers = [], [], []
    for p in paths:
        # (c) THE READ (3.0.0_SA_CVO 94299): at a merge the record is the MERGED INDEX, not HEAD. A
        # task order arriving IN this commit is present at stage 0 and ABSENT at HEAD, so the HEAD read
        # reported "unreadable at HEAD" about a file that is right there -- a WRONG DIAGNOSIS, which is a
        # defect even where the verdict would not change. `_blob(root, "", p)` is the index
        # (`git show :<path>`), the same source _latest_dispositions has always used.
        st, text = _blob(root, "" if merging else "HEAD", p)
        if st != "OK":
            return None, len(paths), "%s unreadable at %s (%s)" % (
                p, "the merged index" if merging else "HEAD", st)
        if _is_pointer_text(text):
            pointers.append(os.path.basename(p))
            continue
        if round_n is not None:
            # spine v3.19 (report 3 item 1.3, LD-0521's deadlock): the slug's round counts ITS orders only. An order
            # carrying no <round> tag still counts -- an unreadable round fails toward refusing, never toward admission.
            rm = TO_ROUND_RE.search(text)
            if rm and int(rm.group(1)) != round_n:
                continue
        m = _to_status_match(text)
        word = m.group(1).lower() if m else "<no status tag>"
        if word not in TERMINAL_TO_WORDS:
            label = "%s [%s]" % (os.path.basename(p), word)
            ok, _why = _proof_terminal(root, p, text, merging=merging)
            (proven if ok else open_ids).append(label)
    note = ""
    if proven:
        note = ("%d order(s) terminal by a VALID proof-of-spec instance at %s although the status word is not "
                "terminal (spine :436, :487-488): %s" % (len(proven), "the merged index" if merging else "HEAD",
                                                         ", ".join(proven)))
    if pointers:
        note += ("; " if note else "") + "%d seat-home POINTER file(s) not counted: %s" % (len(pointers), ", ".join(pointers))
    return open_ids, len(paths), note


# =================================================================================================
# THE ACCEPTANCE SWEEP (AMGT-rk-57, row AMGT_RESAPP-Z-S169, ruling s.3.3 @9c8e04cd9a `:81-85`)
# =================================================================================================
# VALID names well-formedness, not passing. `_open_tos_census` above counts an order terminal on a
# VALID proof-of-spec instance whatever its criteria's own PASS/FAIL verdicts read -- that is the
# spine's rule (:436, :487-488) and this sweep does NOT change it (see _open_tos_census, _proof_terminal,
# _proof_verdict, all untouched). What was missing is a SECOND read, beside the census, that answers the
# question the census's name suggests but its code does not: did the criteria actually PASS. This sweep
# is that second read -- a DISCLOSURE at slug time and a CLI limb, never a violation (a slug cannot
# remedy a FAILED criterion; the CVO grades acceptance at L9, the COO recuts at L10 -- see the
# `_stale_open_row_violations` docstring's own rule, ~:991, "A GATE REFUSES AN ACT ONLY WHEN THAT ACT CAN
# REMEDY THE GATE'S CONDITION").

_PROOF_BLOCK_RE = re.compile(r"^[ \t]*<proof_of_spec>[ \t]*$(.*?)^[ \t]*</proof_of_spec>", re.M | re.S)
_CRITERION_OPEN_RE = re.compile(r"<criterion\b([^>]*)>")
_CRITERION_ID_RE = re.compile(r'id\s*=\s*"([^"]+)"')
_CRITERION_JUDGMENT_RE = re.compile(r'judgment\s*=\s*"true"', re.I)
_ORDER_ROUND_RE = re.compile(r"^\s*<round>\s*([0-9]+)\s*</round>", re.M)


def _order_criteria(text):
    """[{'id': cid, 'judgment': bool}, ...] in document order, parsed from the order's FIRST
    <proof_of_spec> block (falls back to the whole text when the block tag itself is missing, so a
    malformed order still yields what it can rather than nothing). PURE: string in, list out.
    _PROOF_BLOCK_RE is line-anchored on both the opening and closing tag (the way _ORDER_ROUND_RE
    already anchors <round>), so a prose mention of the tag earlier in the order text -- backticked,
    mid-sentence -- can no longer swallow the real block (row AMGT_RESAPP-Z-S176)."""
    m = _PROOF_BLOCK_RE.search(text or "")
    block = m.group(1) if m else (text or "")
    out = []
    for om in _CRITERION_OPEN_RE.finditer(block):
        attrs = om.group(1)
        idm = _CRITERION_ID_RE.search(attrs)
        if not idm:
            continue
        out.append({"id": idm.group(1), "judgment": bool(_CRITERION_JUDGMENT_RE.search(attrs))})
    return out


def _order_round(text):
    """int or None -- the order's own line-anchored <round>N</round> (its record face). PURE."""
    m = _ORDER_ROUND_RE.search(text or "")
    return int(m.group(1)) if m else None


def _order_label(code, rel):
    """'<order basename>' for a sweep row label: the order's file stem (no `.md`) with the leading
    `<code>.TO-` prefix stripped, so the label names the exact order without repeating the whole
    project code on every printed row. PURE."""
    stem = os.path.basename(rel)
    if stem.endswith(".md"):
        stem = stem[:-3]
    prefix = "%s.TO-" % code
    if stem.startswith(prefix):
        stem = stem[len(prefix):]
    return stem


def _acceptance_rows_from_instance(inst_text):
    """({criterion_id: row}, error_or_None) parsed from an instance JSON blob's own `acceptance` array
    (schema: org/standards/PROOF_OF_SPEC.schema.json:183-260). A row with no `criterion_id` is skipped;
    a duplicate id keeps the LAST row (the schema does not forbid a duplicate id, so this is a reading
    choice, not a validation -- proof-of-spec-check.py's own frames are the validator for that). A
    non-parsing blob, or one whose `acceptance` is not a list, returns ({}, <reason>)."""
    try:
        obj = json.loads(inst_text)
    except Exception as exc:  # noqa: BLE001
        return {}, "instance JSON did not parse (%s)" % exc
    acc = obj.get("acceptance") if isinstance(obj, dict) else None
    if not isinstance(acc, list):
        return {}, "instance carries no acceptance array"
    rows = {}
    for row in acc:
        if isinstance(row, dict) and row.get("criterion_id"):
            rows[row["criterion_id"]] = row
    return rows, None


def _classify_acceptance(rows_by_id, criteria):
    """PURE. rows_by_id: {criterion_id: row-dict}; criteria: [{'id': cid, 'judgment': bool}, ...].
    Returns (results, PASS, FAIL, UNVERIFIABLE): results is [{'id', 'status', 'reason'}, ...] in
    criteria order. A JUDGMENT criterion is ALWAYS UNVERIFIABLE, even beside a PASS row -- the CVO
    grades judgment at L9, never this sweep (schema :255). A criterion with no row (missing, or the
    instance could not be read at all -- the caller passes rows_by_id={} for that) is UNVERIFIABLE, its
    reason naming that. A row's own `status` of exactly PASS or FAIL maps 1:1; every other legal value
    (UNCOMPUTABLE-BY-CONSTRUCTION, UNVERIFIABLE-BY-INSTRUMENT, N/A-BY-CONSTRUCTION, UNCOMPUTABLE) and any
    unrecognised value is UNVERIFIABLE -- this sweep is not a second grader of those states, it only
    separates PASS, FAIL and everything else."""
    results = []
    p = f = u = 0
    for c in criteria:
        cid = c["id"]
        if c.get("judgment"):
            results.append({"id": cid, "status": "UNVERIFIABLE",
                            "reason": "judgment criterion, graded at L9, never self-graded"})
            u += 1
            continue
        row = rows_by_id.get(cid)
        if row is None:
            results.append({"id": cid, "status": "UNVERIFIABLE", "reason": "no acceptance row for this id"})
            u += 1
            continue
        st = row.get("status")
        if st == "PASS":
            results.append({"id": cid, "status": "PASS", "reason": ""})
            p += 1
        elif st == "FAIL":
            results.append({"id": cid, "status": "FAIL", "reason": (row.get("status_reason") or "")[:200]})
            f += 1
        else:
            results.append({"id": cid, "status": "UNVERIFIABLE", "reason": "row status=%r" % st})
            u += 1
    return results, p, f, u


def _instance_for_order(root, rel, merging=False):
    """(status, inst_path_or_None, payload) -- locate the order's proof-of-spec instance using the SAME
    naming `_proof_terminal` uses (the two candidate names, `deliverables/*/`, tracked at the read ref),
    duplicated here rather than called into so `_proof_terminal` stays byte-for-byte untouched (this
    cell's own bound). status is one of:
      OK          -- exactly one candidate, read cleanly; inst_path set, payload is its TEXT
      ABSENT      -- no instance tracked; payload is the reason string
      AMBIGUOUS   -- more than one candidate tracked; payload is the reason string
      ERROR       -- git could not answer, or the blob could not be read; payload is the reason string
    This is a DISCLOSURE read (for the acceptance sweep), never the terminality gate -- it does NOT
    compare the instance/order text against the worktree the way `_proof_terminal` must."""
    ref = "" if merging else "HEAD"
    stem = os.path.basename(rel).rsplit(".md", 1)[0]
    names = (stem + ".proof_of_spec.json", stem + "_PROOF_OF_SPEC.json")
    to_dir = os.path.dirname(rel).replace("\\", "/")
    if to_dir.endswith("/task-orders"):
        specs = ["%s/deliverables/*/%s" % (to_dir[:-len("/task-orders")], n) for n in names]
    else:
        specs = ["%s/%s" % (to_dir.replace("task_orders", "deliverables"), n) for n in names]
    try:
        ls = subprocess.run(["git", "ls-files", "--"] + specs, cwd=root, capture_output=True, text=True,
                            encoding="utf-8", errors="replace", timeout=60)
    except Exception as exc:  # noqa: BLE001
        return "ERROR", None, "instance census raised %s" % exc
    if ls.returncode != 0:
        return "ERROR", None, "instance census rc=%d" % ls.returncode
    cands = sorted({p.strip().replace("\\", "/") for p in ls.stdout.splitlines() if p.strip()})
    if not cands:
        return "ABSENT", None, "no proof-of-spec instance tracked"
    if len(cands) > 1:
        return "AMBIGUOUS", None, "%d instances (%s) -- ambiguous" % (len(cands), ", ".join(cands))
    inst = cands[0]
    st, itext = _blob(root, ref, inst)
    if st != "OK":
        return "ERROR", inst, "%s not readable at %s (%s)" % (inst, "the merged index" if merging else "HEAD", st)
    return "OK", inst, itext


def _task_order_paths_for_sweep(root, code):
    """(paths_or_None, note) -- the SAME two glob patterns `_open_tos_census` uses (tree + legacy flat),
    kept as a SEPARATE literal here (not a shared call) so `_open_tos_census` stays byte-for-byte
    untouched, per this cell's own bound."""
    try:
        ls = subprocess.run(["git", "ls-files", "--", "*/task_orders/%s.*.md" % code,
                             "org/missions/D*/*/%s/task-orders/*.md" % code],
                            cwd=root, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=60)
    except Exception as exc:  # noqa: BLE001
        return None, "git ls-files raised %s" % exc
    if ls.returncode != 0:
        return None, "git ls-files rc=%d: %s" % (ls.returncode, ls.stderr.strip()[:120])
    return sorted({p.strip().replace("\\", "/") for p in ls.stdout.splitlines() if p.strip()}), ""


def _acceptance_sweep(root, code, round_n=None, merging=False, _paths=None):
    """Over every tree task order of `code` (the SAME order listing `_open_tos_census` uses), classify
    every criterion PASS / FAIL / UNVERIFIABLE (see `_classify_acceptance`) and return:
      {"orders": [...], "criteria": n, "PASS": a, "FAIL": b, "UNVERIFIABLE": c,
       "round": round_n, "unrounded": k}
    `orders` holds one entry per order that carries at least one criterion:
      {"order": rel, "label": <order basename>, "round": N or None, "results": [...]}
    (results from `_classify_acceptance`). `round_n` filters to orders whose OWN <round> equals it;
    None sweeps every round. An order without a <round> tag is counted in `unrounded` and EXCLUDED from
    a round_n-filtered sweep (it cannot match a round it does not carry) but INCLUDED when round_n is
    None -- printed, never dropped, per this cell's own rule. This is a READ: nothing here refuses
    anything, and it never enters the violations list (see the caller in check_file).

    `_paths` is INJECTABLE, same convention as `_route_precondition_violations`'s `open_tos=None`: every
    production caller (the slug-time note, the `--acceptance` CLI) passes None and gets the full tree
    listing below. A caller that supplies its own list gets exactly that list swept instead of the
    project-wide `git ls-files` -- for a battery that needs ONE order's real bytes without the O(orders)
    subprocess cost of sweeping all of them (measured ~160s unfiltered on AMGT_RESAPP's 127 orders,
    against a 120s grading bound)."""
    if _paths is not None:
        paths, note = _paths, ""
    else:
        paths, note = _task_order_paths_for_sweep(root, code)
    if paths is None:
        return {"orders": [], "criteria": 0, "PASS": 0, "FAIL": 0, "UNVERIFIABLE": 0,
                "round": round_n, "unrounded": 0, "error": note}
    ref = "" if merging else "HEAD"
    orders_out = []
    total_p = total_f = total_u = 0
    unrounded = 0
    for rel in paths:
        st, otext = _blob(root, ref, rel)
        if st != "OK":
            continue
        order_round = _order_round(otext)
        if order_round is None:
            unrounded += 1
        if round_n is not None and order_round != round_n:
            continue
        criteria = _order_criteria(otext)
        if not criteria:
            continue
        inst_status, inst_path, payload = _instance_for_order(root, rel, merging=merging)
        if inst_status == "OK":
            rows_by_id, err = _acceptance_rows_from_instance(payload)
            reason_override = err
        else:
            rows_by_id, reason_override = {}, payload
        if reason_override:
            results = [{"id": c["id"], "status": "UNVERIFIABLE", "reason": reason_override} for c in criteria]
            total_u += len(criteria)
        else:
            results, p, f, u = _classify_acceptance(rows_by_id, criteria)
            total_p += p
            total_f += f
            total_u += u
        orders_out.append({"order": rel, "label": _order_label(code, rel), "round": order_round,
                           "results": results})
    return {"orders": orders_out, "criteria": total_p + total_f + total_u, "PASS": total_p,
            "FAIL": total_f, "UNVERIFIABLE": total_u, "round": round_n, "unrounded": unrounded}


def _flagged_rows(sweep, status):
    """[str, ...] '<order basename>:<criterion-id> (<reason>)' for every criterion classed `status`
    (FAIL or UNVERIFIABLE) in `sweep`'s orders, in order. PURE."""
    out = []
    for o in sweep.get("orders", []):
        for r in o.get("results", []):
            if r.get("status") == status:
                reason = r.get("reason") or ""
                out.append("%s:%s (%s)" % (o["label"], r["id"], reason) if reason
                          else "%s:%s" % (o["label"], r["id"]))
    return out


# Andrew's call 1 YES, relayed by CTO 21533: POSN round 2 ONLY may route with
# S2-1/S3-1 unrun. The immutable record pins all 19 authorized row contents,
# their filing paths and the two unchanged order blobs. This is NOT the broad
# override: every other limb, including investigation completion, still runs.
POSN_R2_EXCEPTION_PIN = "10ceba8c43"
POSN_R2_EXCEPTION_PATH = (
    "org/tier1_exec/3.0.0_SA_CVO/deliverables/"
    "POSN_ASTTAX_ROUND2_ROUTING_EXCEPTION_20260911_Z.json")


def _posn_round2_terminal_exception(root, rel, row, code, open_ids, total):
    """Match the exact authorized case; an absent/unreadable record never grants it."""
    if code != "POSN_ASTTAX" or not open_ids or total != 8:
        return False
    allowed_paths = (
        "org/missions/D4/POSN/POSN_ASTTAX/surprise-channel/adjudications/ADJUDICATION_v3.md",
        "org/missions/D4/POSN/POSN_ASTTAX/surprise-channel/remediations/REMEDIATION_v2.md")
    if rel.replace("\\", "/") not in allowed_paths:
        return False
    status, text = _blob(root, POSN_R2_EXCEPTION_PIN, POSN_R2_EXCEPTION_PATH)
    if status != "OK":
        return False
    try:
        record = json.loads(text)
        if (record["schema_version"] != 1 or record["project"] != code
                or record["round"] != 2 or record["authority_message_id"] != 21533
                or record["expected_total_orders"] != total):
            return False
        orders = record["orders"]
        if len(orders) != 2 or sorted(open_ids) != sorted(o["open_label"] for o in orders):
            return False
        if not any(r["path"] == rel.replace("\\", "/") and r["id"] == row.get("id")
                   and r["sha256"] == _canon_hash(row) for r in record["rows"]):
            return False
        import hashlib
        for order in orders:
            state, body = _blob(root, "HEAD", order["path"])
            if state != "OK" or hashlib.sha256(body.encode("utf-8")).hexdigest() != order["sha256"]:
                return False
    except (KeyError, TypeError, ValueError):
        return False
    return True


# LD-0562, relay 22245: round 3 ONLY carries S2/S3/T6/T7 unrun. Use the
# already-established immutable-record mechanism, never the round-2 exception
# or a commit-wide override. All non-terminality limbs still run independently.
POSN_R3_EXCEPTION_PIN = "fa2b1764c4"
POSN_R3_EXCEPTION_PATH = (
    "org/tier1_exec/3.0.0_SA_CVO/deliverables/"
    "POSN_ASTTAX_ROUND3_ROUTING_EXCEPTION_20260913_Z.json")


def _posn_round3_terminal_exception(root, rel, row, code, open_ids, total):
    """Admit only LD-0562's exact recorded round-3 rows and unchanged orders."""
    if code != "POSN_ASTTAX" or not open_ids or total != 15:
        return False
    allowed_paths = (
        "org/missions/D4/POSN/POSN_ASTTAX/surprise-channel/adjudications/ADJUDICATION_v5.md",
        "org/missions/D4/POSN/POSN_ASTTAX/surprise-channel/remediations/REMEDIATION_v3.md")
    rel = rel.replace("\\", "/")
    if rel not in allowed_paths:
        return False
    status, text = _blob(root, POSN_R3_EXCEPTION_PIN, POSN_R3_EXCEPTION_PATH)
    if status != "OK":
        return False
    try:
        record = json.loads(text)
        if (record["schema_version"] != 1 or record["project"] != code
                or record["round"] != 3 or record["authority_message_id"] != 22245
                or record["authority_pin"] != "b75f5a805a"
                or record["expected_total_orders"] != total):
            return False
        orders = record["orders"]
        if len(orders) != 4 or sorted(open_ids) != sorted(o["open_label"] for o in orders):
            return False
        if not any(r["path"] == rel and r["id"] == row.get("id")
                   and r["sha256"] == _canon_hash(row) for r in record["rows"]):
            return False
        import hashlib
        for order in orders:
            state, body = _blob(root, "HEAD", order["path"])
            if state != "OK" or hashlib.sha256(body.encode("utf-8")).hexdigest() != order["sha256"]:
                return False
    except (KeyError, TypeError, ValueError):
        return False
    return True


# THE SWEEP WATERMARK (1.0.0_SA_CTO RULING 102674, one IRPT_BCKEND project sweep over every workstream-round drained
# since the last watermark, while later rounds keep running; 3.0.0_SA_CVO 102703: sweep 1 landed only by audited
# override because both GATE (iii) limbs counted orders issued and rows filed AFTER the sweep's cut).
# HOW A SLUG DECLARES ITS SCOPE: the slug's own document (the REMEDIATION or ADJUDICATION file being committed) carries
# ONE line-anchored element, `<sweep_watermark>YYYY-MM-DDTHH:MM(:SS)Z</sweep_watermark>` -- the UTC instant of the
# sweep's cut. When present, a task order FIRST ADDED to git after that instant, and an investigation item whose
# `surfaced_at` is after it, do not hold the slug: they belong to the next sweep. An order or item whose time cannot be
# read still holds it (an unreadable time fails toward refusal). A document with NO watermark keeps the whole-project
# rule unchanged. A prose mention of the tag is not the element (line-anchored, as <round> and <status> are).
SWEEP_WATERMARK_RE = re.compile(
    r"^[ \t]*<sweep_watermark>[ \t]*([0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}(?::[0-9]{2})?Z)[ \t]*</sweep_watermark>[ \t]*$",
    re.M)


def _parse_utc(s):
    """datetime (UTC, aware) from an ISO-8601 string, or None. PURE; never raises."""
    import datetime as _dt
    try:
        v = str(s or "").strip().replace("Z", "+00:00")
        if not v:
            return None
        d = _dt.datetime.fromisoformat(v)
        return d if d.tzinfo else d.replace(tzinfo=_dt.timezone.utc)
    except (ValueError, TypeError):
        return None


def _sweep_watermark(text):
    """The declared sweep watermark of a slug document (aware datetime), or None. PURE. Two DIFFERENT watermark
    lines in one document are ambiguous and read as None -- the whole-project rule, the stricter one."""
    vals = {m.group(1) for m in SWEEP_WATERMARK_RE.finditer(text or "")}
    return _parse_utc(next(iter(vals))) if len(vals) == 1 else None


def _split_by_watermark(entries, watermark):
    """PURE. entries: [(label, when-or-None)]. Returns (holding, after): with no watermark every entry holds; with one,
    an entry strictly AFTER the watermark is `after` (the next sweep's), everything else -- including an unreadable
    time -- holds."""
    if watermark is None:
        return [lbl for lbl, _w in entries], []
    holding, after = [], []
    for lbl, when in entries:
        (after if (when is not None and when > watermark) else holding).append(lbl)
    return holding, after


def _order_first_added(root, code):
    """{basename: aware datetime of the commit that first ADDED it} for the project's task orders at HEAD, one git
    call per order. A failed read maps to None (holds the slug)."""
    out = {}
    try:
        ls = subprocess.run(["git", "ls-files", "--", "*/task_orders/%s.*.md" % code,
                             "org/missions/D*/*/%s/task-orders/*.md" % code],
                            cwd=root, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=60)
        paths = [p.strip().replace("\\", "/") for p in ls.stdout.splitlines() if p.strip()] if ls.returncode == 0 else []
    except Exception:  # noqa: BLE001
        paths = []
    for p in paths:
        try:
            lg = subprocess.run(["git", "log", "--diff-filter=A", "--format=%aI", "--", p], cwd=root,
                                capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=60)
            lines = [x for x in lg.stdout.splitlines() if x.strip()] if lg.returncode == 0 else []
            out[os.path.basename(p)] = _parse_utc(lines[-1]) if lines else None
        except Exception:  # noqa: BLE001
            out[os.path.basename(p)] = None
    return out


def _item_surfaced_at(root, code):
    """{item id: aware datetime of its `surfaced_at`} over the project's investigation documents in the INDEX.
    A missing or unparseable time maps to None (holds the slug)."""
    out = {}
    paths, _note = _index_paths(root, [p % code for p in INVESTIGATION_PATTERNS])
    for p in paths or []:
        st, text = _blob(root, "", p)
        if st != "OK":
            continue
        try:
            rows, _ = _rows(text)
        except Exception:  # noqa: BLE001
            continue
        for r in rows or []:
            if isinstance(r, dict) and r.get("id") and r["id"] not in out:
                out[r["id"]] = _parse_utc(r.get("surfaced_at"))
    return out


# THE ROW'S OWN WORKSTREAM (1.0.0_SA_CTO msg 107639, on dell2 msg 2176 via 0.0.0_AB_MSTR 107638; rule 27: a WORKSTREAM is
# a SCOPE). A project running interleaved workstreams (IRPT_BCKEND ~P/~Y/~M) never had every order terminal at once, so
# the project-wide wait below never cleared. A new remediation row now waits only on the open orders of the workstream(s)
# of the orders it cites; a row whose workstream cannot be resolved keeps the project-wide wait (never looser).
TO_WORKSTREAM_RE = re.compile(r"<workstream>\s*([^<\n]+?)\s*</workstream>", re.I)
TO_ISSUED_BY_RE = re.compile(r"<issued_by>\s*([^<\n]+?)\s*</issued_by>", re.I)
TO_ISSUED_TO_RE = re.compile(r"<issued_to>\s*([^<\n]+?)\s*</issued_to>", re.I)
_WS_CACHE = {}


def _order_workstream(text):
    """PURE. An order's workstream: its <workstream> tag, else the lane of its <issued_by> COO with any trailing instance
    digits dropped (`2.0.0_SA_COO~Y2` issues `<workstream>~Y</workstream>`, measured on IRPT_BCKEND), else None."""
    m = TO_WORKSTREAM_RE.search(text or "")
    if m and m.group(1).strip():
        return m.group(1).strip()
    m = TO_ISSUED_BY_RE.search(text or "")
    if m and "~" in m.group(1):
        return "~" + re.sub(r"\d+$", "", m.group(1).split("~", 1)[1].strip())
    return None


def _workstream_map(root, code, merging=False):
    """{order basename: (workstream or None, issued_to)} over the project's orders (the census's listing), or None when
    any order is unreadable. Read once per (root, code, merging) per gate run."""
    key = (root, code, bool(merging))
    if key in _WS_CACHE:
        return _WS_CACHE[key]
    out = None
    try:
        ls = subprocess.run(["git", "ls-files", "--", "*/task_orders/%s.*.md" % code,
                             "org/missions/D*/*/%s/task-orders/*.md" % code],
                            cwd=root, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=60)
        if ls.returncode == 0:
            out = {}
            for p in [x.strip().replace("\\", "/") for x in ls.stdout.splitlines() if x.strip()]:
                st, text = _blob(root, "" if merging else "HEAD", p)
                if st != "OK":
                    out = None
                    break
                m = TO_ISSUED_TO_RE.search(text)
                out[os.path.basename(p)] = (_order_workstream(text), m.group(1).strip() if m else "")
    except Exception:  # noqa: BLE001
        out = None
    _WS_CACHE[key] = out
    return out


def _row_workstreams(row, code, wsmap):
    """PURE. The set of workstreams of the orders `row` cites, or None when it cannot be resolved (no cited order found,
    or a cited order with no workstream). A row cites an order by a worker coordinate `<CODE>-...-W<n>-S<k>` in its id
    or text (the order issued to 0.9.0_WK_<CODE>~<n>) or by an order id `TO-...` in its text."""
    if not wsmap:
        return None
    text = json.dumps(row, ensure_ascii=False)
    workers = {"0.9.0_WK_%s~%s" % (code, n) for n in re.findall(r"%s-(?:[A-Za-z0-9]+-)*?W(\d+)-S\d+" % re.escape(code), text)}
    cited = set(re.findall(r"\bTO-[A-Za-z0-9][A-Za-z0-9-]*[A-Za-z0-9]", text))
    hits = [ws for base, (ws, to) in wsmap.items()
            if (to and to in workers) or any(base.startswith("%s.%s." % (code, c)) for c in cited)]
    if not hits or any(ws is None for ws in hits):
        return None
    return set(hits)


def _scope_open_to_workstreams(open_ids, row_ws, order_ws):
    """PURE. The open-order labels (`<basename> [<word>]`) that bind a row of workstream(s) `row_ws`: an order of one of
    those workstreams, or an order whose workstream is unknown. row_ws None -> every label (the project-wide wait)."""
    if row_ws is None or open_ids is None:
        return open_ids
    keep = []
    for lbl in open_ids:
        ws = (order_ws.get(lbl.split(" [", 1)[0]) or (None, ""))[0]
        if ws is None or ws in row_ws:
            keep.append(lbl)
    return keep


def _route_precondition_violations(root, rel, row, code, open_tos=None, route_word=None, merging=False,
                                   parent_ids=None, watermark=None, issued_at=None, workstreams=None):
    """GATE (iii) first limb for ONE new tree row carrying a route. `open_tos` is injectable for the
    red-first exercise; production passes None and the census runs.

    AT A MERGE: a CARRIED row is not evaluated -- see the block below and the twin limb's."""
    if merging and _row_was_carried(row, parent_ids):
        # CARRIED BY THE MERGE == HISTORY ARRIVING, NOT A ROUTING ACT (see _row_was_carried).
        # SUPERSEDES THE PER-FABRIC COORDINATE TEST (3.0.0_SA_CVO 94337) ON ANDREW'S ~19:3xZ SCOPING.
        # That ruling was right that the blanket merge exemption was too wide, and right that each
        # fabric's CVO slugs its own projects; the defect was the PROXY it used. `Z-` names WHICH BOX
        # minted a row, and the gate needs to know WHETHER THIS COMMIT MINTED IT -- on the laptop the
        # two coincide, on site Z they invert. Provenance answers the question the proxy was standing
        # in for, on both boxes.
        # A row MINTED in the merge commit falls through and BINDS -- including a `Z-` row, which the
        # old test would have exempted. So does any row whose parents could not be read.
        # No violations. The ANNOUNCEMENT is the caller's note, one per row-bearing file.
        return []
    rid = row.get("id", "<no id>")
    route_word = route_word or row.get("route")
    if open_tos is None:
        open_ids, total, note = _open_tos_for_project(root, code, merging=merging, round_n=_round_num(row.get("round")))
        if workstreams is None and open_ids:
            _wm = _workstream_map(root, code, merging=merging)
            workstreams = (_row_workstreams(row, code, _wm), _wm or {})
    else:
        open_ids, total, note = open_tos
    if open_ids is None:
        return ["%s: the L10 precondition (every task order under %s terminal) could NOT be evaluated (%s) "
                "-- REFUSED, fail-closed" % (rid, code, note)]
    _row_ws = None
    if workstreams is not None and open_ids:
        _row_ws = workstreams[0]
        open_ids = _scope_open_to_workstreams(open_ids, _row_ws, workstreams[1])
    if open_ids and watermark is not None:
        # THE SWEEP WATERMARK (see SWEEP_WATERMARK_RE): an order first added after the slug's declared cut is the next
        # sweep's and does not hold this one. Labels are `<basename> [<word>]`, so the lookup keys on the basename.
        when = issued_at if issued_at is not None else _order_first_added(root, code)
        open_ids, _after = _split_by_watermark(
            [(lbl, when.get(lbl.split(" [", 1)[0])) for lbl in open_ids], watermark)
    if open_ids:
        if _posn_round2_terminal_exception(root, rel, row, code, open_ids, total):
            return []
        if _posn_round3_terminal_exception(root, rel, row, code, open_ids, total):
            return []
        return ["%s: NEW remediation row (%s) while %d of %d task order(s) under %s%s are NOT "
                "terminal at HEAD: %s. The slug waits until every task order is complete "
                "(Andrew-direct 2026-09-03, @716a9bc7ce call 3, LD-0521: 'We do not route until the job "
                "is over')." % (rid, route_word, len(open_ids), total, code,
                                " in the row's workstream(s) %s" % ",".join(sorted(_row_ws)) if _row_ws
                                else (" (the row's workstream unresolved: project-wide)" if workstreams is not None else ""),
                                ", ".join(open_ids))
                + (" Already terminal by proof: %s." % note if note else "")]
    return []


_GATE_TAG = "surprise-row-gate"

def _dispatched_from_argv_or_env(argv):
    """The paths to grade: ARGV first, the STAGED env var only when argv is empty.

    THE ~32 KB ARGV CLIFF (0.0.0_AB_MSTR 94338): the pre-commit hook passed this list as UNQUOTED
    ARGV, and Windows caps a command line near 32,767 chars -- so on a large merge python NEVER
    STARTED (rc 126, "Argument list too long") and the gate that carries the merge exemptions was
    exactly the gate that could not run. Bisected on this box: 300 paths / 29,098 B rc 0;
    400 paths / 38,798 B rc 126. The estate's real paths put the cliff near 320 files. It fails
    CLOSED, so nothing landed -- but the only escape left was blanket `--no-verify`, which discards
    every other gate too.
    MEASURED: the ENVIRONMENT removes the cliff rather than raising it (516,000 B -> rc 0 here).

    ARGV REMAINS THE CONTRACT. A bare call with no env still grades NOTHING, because safe-merge.sh
    relies on exactly that and says so. And the SOURCE is printed whenever it is not argv: an input
    whose origin is invisible is how a vacuous pass reads as a clean one.
    """
    args = [a for a in argv if a and not a.startswith("--")]
    if args:
        return args, "argv"
    env = os.environ.get("STAGED", "")
    if env.strip():
        paths = [p.strip() for p in env.replace("\r", "").split("\n") if p.strip()]
        if paths:
            print("[%s] input: %d path(s) from the STAGED environment variable "
                  "(argv was empty; the ~32 KB argv cliff, 0.0.0_AB_MSTR 94338)"
                  % (_GATE_TAG, len(paths)))
            return paths, "env"
    return [], "none"


def _repo_root():
    try:
        out = subprocess.run(["git", "rev-parse", "--show-toplevel"],
                             capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=20)
        if out.returncode == 0:
            return out.stdout.strip()
    except Exception:  # noqa: BLE001
        pass
    return os.getcwd()


def _honour_audit_line(root, reason, log_path=None, agent=None, now=None):
    """Append the gate's OWN audit line when it honours SURPRISE_ROW_OVERRIDE. Tagged
    SURPRISE-ROW-OVERRIDE-HONOURED so it never counts as safe-commit's SURPRISE-ROW-OVERRIDE line
    (safe-commit's is written BEFORE the export; this one is written by the process that honoured
    the variable, whoever set it). Measured 2026-09-11 (0.0.0_AB_MSTR 95721, LD-0549): a hand-exported
    variable was honoured and left NO line, so an unaudited override was indistinguishable from one
    nobody declared. Returns the path written, or None (a failed write never blocks the gate: the
    override is already honoured by the caller, and a write failure is printed, not raised)."""
    import datetime as _dt
    agent = agent or os.environ.get("GIT_AUTHOR_NAME") or os.environ.get("OPAL_AGENT_SERIAL") or "UNKNOWN"
    ts = now or _dt.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    p = log_path or os.environ.get("SAFE_COMMIT_AUDIT_LOG") or os.path.join(root, "org", _gao_name())
    try:
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "a", encoding="utf-8", newline="\n") as fh:
            fh.write("%s SURPRISE-ROW-OVERRIDE-HONOURED  %s  reason=%s  provenance=UNVERIFIED-BY-GATE\n"
                     % (ts, agent, str(reason).replace("\n", " ").strip()))
        return p
    except Exception as exc:  # noqa: BLE001
        print("[surprise-row-gate] WARN: could not write the honour audit line to %s (%s: %s)"
              % (p, type(exc).__name__, exc), file=sys.stderr)
        return None


# ONE READ PER (ref, path) PER GRADING RUN. main() switches this on for a real grade; None (the default) means no
# memo, which is what --self-test and --acceptance get, since the self-test rewrites its scratch repos between reads.
# A grade never writes to git, so HEAD, MERGE_HEAD and the index it reads cannot change under it. ERROR is never
# kept: a git failure is re-asked. Profile, 743-path merge, 38 channel files: 11,144 reads cost 1,125 s of 1,147 s,
# and 8,828 of them were _seats_with_open_orders re-reading one project's task orders once per channel file.
_BLOB_MEMO = None


def _blob(root, ref, rel):
    if _BLOB_MEMO is None:
        return _blob_read(root, ref, rel)
    key = (root, ref, rel)
    if key not in _BLOB_MEMO:
        got = _blob_read(root, ref, rel)
        if got[0] == "ERROR":
            return got
        _BLOB_MEMO[key] = got
    return _BLOB_MEMO[key]


def _blob_read(root, ref, rel):
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
        # encoding= is EXPLICIT (2.0.0_SA_COO~Z finding 19466, 2026-09-03): text=True alone decodes the pipe with
        # locale.getpreferredencoding() -- cp1252 on site Z -- so one non-cp1252 byte anywhere in the file
        # (a U+2B50 star at HEAD) emptied stdout and the gate refused EVERY new row as "ZERO rows".
        probe = subprocess.run(probe_cmd, cwd=root, capture_output=True, text=True,
                               encoding="utf-8", errors="surrogateescape", timeout=60)
    except Exception as exc:  # noqa: BLE001
        return ("ERROR", "%s raised %s" % (probe_cmd[1], exc))
    if probe.returncode != 0:
        return ("ERROR", "%s rc=%d: %s" % (probe_cmd[1], probe.returncode, probe.stderr.strip()[:160]))
    if not probe.stdout.strip():
        return ("ABSENT", None)
    try:
        r = subprocess.run(["git", "show", spec], cwd=root, capture_output=True, text=True,
                           encoding="utf-8", errors="surrogateescape", timeout=60)
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
    """The schema kind. An ADJUDICATION document (carrier 5) validates against the investigation schema."""
    return "REMEDIATION" if "REMEDIATION" in os.path.basename(rel).upper() else "INVESTIGATION"


def _first_token(val):
    s = str(val or "").strip()
    return s.split()[0] if s else ""


def _owner_field_violations(rid, owner, field):
    """PURE. R-18(2) and R-19(2) on a NEW row: a disarm owner that can never act (a WORKER serial) or that is the WRITER
    of the clock (3.0.0_SA_CVO) is refused, naming who to name instead."""
    v = _first_token(owner)
    if not v:
        return []
    if WORKER_SERIAL_RE.match(v):
        return ["%s: %s=%r names a WORKER serial. A worker is terminal at its drain and can never send the owner's "
                "word, so the duty passes to its ISSUER (R-18): name the issuer" % (rid, field, owner)]
    if v == CVO_SERIAL or _base_serial(v) == CVO_SERIAL:
        return ["%s: %s=%r names the CVO, the only WRITER of a disarm clock (R-15); a disarm owner is never the "
                "writer (R-19): name the artifact's owner, or 1.0.0_SA_CTO where the artifact is the CVO's own row"
                % (rid, field, owner)]
    return []


def _worker_carrier_violations(rid, row):
    """PURE. A-1 (LGIC_ENFORCE-C-S24): `adjudicates` and disposition GRADUATED are the CVO's L9 fields; on a row a
    WORKER surfaced they are refused, because a worker's GRADUATED transfers the item to nobody."""
    sb = _first_token(row.get("surfaced_by"))
    if not WORKER_SERIAL_RE.match(sb):
        return []
    out = []
    if row.get("adjudicates"):
        out.append("%s: `adjudicates` on a row surfaced by WORKER %s. `adjudicates` is the L9 adjudication carrier and "
                   "it is 3.0.0_SA_CVO's field (A-1, LGIC_ENFORCE-C-S24): a worker files its finding as "
                   "UNDER_INVESTIGATION and the CVO dispositions it" % (rid, sb))
    if row.get("disposition") == "GRADUATED":
        out.append("%s: disposition=GRADUATED on a row surfaced by WORKER %s. GRADUATED is a TRANSFER the CVO makes at "
                   "L9 with a remediation row as its landing surface; a worker's GRADUATED transfers the item to nobody "
                   "and hides it from the CVO's compile (A-1, LGIC_ENFORCE-C-S24)" % (rid, sb))
    return out


_GATE_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _fabric_of_id(rid):
    """CT-d-6 (NFRA_CTLPLN, CTO msg 106069): (box, devices_module, register, why). The box the id's coordinate names, read from
    the device register's `row_coordinate` field -- never a literal. `box` is None with `why` set when the register cannot be
    read (REFUSED, no two-fabric fallback) or the id carries a coordinate the register does not hold."""
    try:
        spec = importlib.util.spec_from_file_location("opal_devices", os.path.join(_GATE_ROOT, "lib", "devices.py"))
        dev = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(dev)
        reg = dev.load()
        coords = {}
        for d in dev.devices(reg):
            if "row_coordinate" not in d:
                raise dev.RegisterError("device %r carries no row_coordinate" % d.get("name"))
            if d["row_coordinate"] in coords:
                raise dev.RegisterError("row_coordinate %r held by two devices" % d["row_coordinate"])
            coords[d["row_coordinate"]] = d["name"]
    except Exception as exc:  # noqa: BLE001 -- any failure to read the register is a refusal, never a default
        return None, None, None, ("the device register cannot be read (%s: %s); this row is REFUSED, the gate has no built-in "
                                  "fabric list" % (type(exc).__name__, exc))
    m = ID_RE.match(str(rid))
    coord = (m.group("z") or "")[:-1] if m else ""
    if coord not in coords:
        return None, dev, reg, ("the id carries the coordinate %r, which the device register does not hold; registered "
                                "coordinates: %s" % (coord, ", ".join(repr(c) for c in sorted(coords) if c)))
    return coords[coord], dev, reg, ""


def _fabric_identity_violations(rid, fabric):
    """The id-to-fabric half of RC1 identity: the row's `fabric` must be the box its id's coordinate names (bare = the box whose
    coordinate is empty; a Dell's id carries D1-/D2- as read from the register). Returns a list of complaints."""
    box, dev, reg, why = _fabric_of_id(rid)
    if box is None:
        return ["%s: fabric=%r -- %s" % (rid, fabric, why)]
    held = {d["name"]: d["row_coordinate"] for d in dev.devices(reg)}
    forms = "; ".join("%s = id <CODE>-%sS<n>" % ("/".join([d["name"]] + list(d.get("aliases", []))),
                                                  d["row_coordinate"] + "-" if d["row_coordinate"] else "")
                      for d in dev.devices(reg))
    if dev.resolve(str(fabric), reg) == box:
        return []
    named = dev.resolve(str(fabric), reg)
    if named is not None and not held[box] and held[named]:
        return ["%s: fabric=%r but the id carries no coordinate. A row filed on %s is written <CODE>-%s-S<n> (worker: "
                "<CODE>-%s-W<n>-S<k>); a bare id is the laptop's. Fabrics: %s." % (rid, fabric, named, held[named], held[named], forms)]
    return ["%s: fabric=%r but the id's coordinate %r means box %r. Fabrics and their id forms: %s."
            % (rid, fabric, held[box], box, forms)]


def _check_row(row, kind, schema, carried=False):
    """Complaints about ONE NEW row. Schema-required + closed enums + the step-7/10 fields.

    `carried` (R-28, 1.0.0_SA_CTO 2026-09-16): True only for a row a MERGE CARRIED from a parent (`_row_was_carried`).
    The OWNER-AND-CARRIER limbs (R-18(2), R-19(2), A-1) grade the AUTHORING act -- who a seat named as owner, which
    fields a worker wrote -- so they bind where the row is minted, exactly as the two L10 precondition limbs do. Measured
    on the CLOUD->SITEZ leg: SITEZ had never touched D14, so 9 LGIC rows minted 02:54-10:45 EDT, BEFORE these limbs
    landed @9d10c4b796 (11:40 EDT), read as NEW there and refused a merge that has no override path -- rows the
    mutation limb forbids editing, whose clocks were already DISARMED or INERT. Schema and enum limbs still grade."""
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
    id_project = m.group("project") if m else str(rid).rsplit("-S", 1)[0]
    for fld in ("project", "fabric"):
        if not str(row.get(fld, "")).strip():
            out.append("%s: NEW row carries no %r. Step-3 identity (project + fabric) is required on "
                       "every new row so the L8 monitor can GROUP without regexing an id -- a "
                       "consumer that must parse an id cannot reject a malformed one." % (rid, fld))
    if row.get("project") and row["project"] != id_project:
        out.append("%s: project=%r but the id says %r. The id prefix and the project field are two "
                   "carriers of one quantity; they must agree." % (rid, row["project"], id_project))
    if row.get("fabric"):
        out += _fabric_identity_violations(rid, row["fabric"])

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
        if not carried:
            out += _owner_field_violations(rid, row.get("disarm_owner"), "disarm_owner")
            out += _worker_carrier_violations(rid, row)
    else:
        dz = row.get("disarm")
        if isinstance(dz, dict) and not carried:
            out += _owner_field_violations(rid, dz.get("owner"), "disarm.owner")
        route, target = row.get("route"), row.get("loop_target")
        # REMEDIATED-IN-ROUND (2026-09-03, the gate-model fork between 1.0.0_SA_CTO and 1.0.0_SA_CTO~Z, ruled at the
        # base -- relay 93568, ruling 93571): the route enum answers "what does the remedy need that does not exist
        # yet"; a remedy EXECUTED inside the round by the row's owner is a member that enum does not cover, and refusing
        # it forced a slug to land as re-entry rows (NFRA_OPSEC202609, site Z). A NEW remediation row may omit `route`
        # and `loop_target` IF AND ONLY IF remediation.state is REMEDIATED and, when ARMED, disarm.state is DISARMED;
        # the row's required `evidence` is where the executed remedy is cited. An OPEN row without a route is still a
        # graduated item whose remedy needs a task order, a cell or an outcome -- the route IS the decision -- refused.
        # spine v3.0/3.1 L9/L10 (carrier 6 of eight; Andrew-direct 2026-09-03 ~22:2xZ at the CRO terminal): a remediation
        # row carries NO route -- the slug goes to 1.0.0_SA_CTO, the single router, who answers with a PRD addendum or the
        # round-N analysis; the three route tokens are RETIRED. The limb that refused an OPEN route-less row ("the route
        # IS the decision") is retired with them. A legacy pair that IS present (a round issued under v2, finishing under
        # its cut orders) still keeps the locked mapping below, so the two carriers cannot drift while they exist.
        if target is None and route is not None:
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
    old_all = {}
    for r in old_rows:
        if r.get("id"):
            old_all.setdefault(r["id"], []).append(r)
    # RC2 second pass (CVO~A re-grade @0dbf12ebb3, hole 4 -- DICT COLLAPSE): the old code built
    # {id: row} over the staged rows, so a CONTRADICTORY duplicate of an existing id followed by
    # the unchanged original collapsed to the original, hashed equal, and passed. Every occurrence
    # of an id is kept and every one is compared.
    new_all = {}
    for r in new_rows:
        if r.get("id"):
            new_all.setdefault(r["id"], []).append(r)
    out = []
    # GRADE WHAT THE CHANGE INTRODUCES (1.0.0_SA_CTO msg 107628): a duplicate id ALREADY at HEAD (an admitted DUAL-MINT)
    # does not refuse a commit that leaves it alone; only a duplicate the diff adds -- more occurrences than HEAD
    # carries -- is refused. The copies already there are graded below like any existing row.
    for nid, occurrences in new_all.items():
        if len(occurrences) > max(1, len(old_all.get(nid, []))):
            out.append("%s: id %s occurs %d times in the staged file (HEAD carries %d). An id is one row; a second "
                       "occurrence is either a contradictory rewrite hiding behind the original or a "
                       "paste error, and both are refused." % (rel, nid, len(occurrences), len(old_all.get(nid, []))))
    if head_text is None:
        return out
    for oid, orows in old_all.items():
        if oid not in new_all:
            out.append("%s: EXISTING row %s was DELETED. The channel is append-only: retire it "
                       "with a new row that cites it, never by removal." % (rel, oid))
            continue
        if len(orows) > 1:
            # A DUPLICATE ALREADY AT HEAD: every copy must survive byte-equivalent as DATA; neither is edited or removed.
            hs_old = sorted(_canon_hash(r) for r in orows)
            hs_new = sorted(_canon_hash(r) for r in new_all[oid])
            if hs_new != hs_old and len(hs_new) < len(hs_old):
                out.append("%s: EXISTING row %s was DELETED (one of the %d copies HEAD carries). The channel is "
                           "append-only." % (rel, oid, len(hs_old)))
            elif hs_new != hs_old:
                out.append("%s: EXISTING row %s was MUTATED in place (content hashes %s -> %s). Corrections are NEW "
                           "items citing the old id." % (rel, oid, ",".join(h[:12] for h in hs_old),
                                                        ",".join(h[:12] for h in hs_new)))
            continue
        orow = orows[0]
        h_old = _canon_hash(orow)
        for nrow in new_all[oid]:
            h_new = _canon_hash(nrow)
            if h_old != h_new:
                if _monotone_advance(orow, nrow):
                    continue  # the two clocks moved forward on a remediation row; noted by check_file, never refused
                out.append("%s: EXISTING row %s was MUTATED in place (content hash %s -> %s). "
                           "Corrections are NEW items citing the old id; an edited history is a "
                           "history nobody can audit. A remediation row's own clocks may advance in place "
                           "(disarm ARMED->DISARMED with `at`, remediation OPEN->REMEDIATED or OPEN->CLOSED_UNREMEDIATED adding "
                           "only `remediation.closure`, closed false->true, nothing else changed)." % (rel, oid, h_old[:12], h_new[:12]))
    return out


def _dual_mint_decision(head_rows, other_rows, staged_rows, published):
    """PURE. {id: (refs carrying HEAD's copy, refs carrying MERGE_HEAD's copy)} for every DUAL-MINT in a merge.

    1.0.0_SA_CTO ruling msg 107530 (2026-10-09, on 0.0.0_AB_MSTR's relay
    org/tier0_exec/0.0.0_AB_MSTR/deliverables/RELAY_20261009T0042Z_DELL1_SURPRISE_ROW_DUPLICATE_ID_GATE_GAP.md): one row id
    minted on two boxes is a DUAL-MINT, not a mutation. An id qualifies only when ALL hold: (a) each merge parent carries
    exactly one row under it and the two differ; (b) the merged file carries exactly those two rows under it, both
    byte-equivalent as DATA, nothing else; (c) each copy is already on a published ref (`published` = [(ref, {id: set of
    content hashes})], origin/CLOUD and every origin/box/*). Anything else keeps the duplicate-id and MUTATED findings."""
    def _by_id(rows):
        d = {}
        for r in rows or []:
            rid = str((r or {}).get("id") or "").strip()
            if rid:
                d.setdefault(rid, []).append(_canon_hash(r))
        return d
    h, o, s = _by_id(head_rows), _by_id(other_rows), _by_id(staged_rows)
    out = {}
    for rid, hh in h.items():
        oh = o.get(rid)
        if len(hh) != 1 or not oh or len(oh) != 1 or hh[0] == oh[0]:
            continue
        if sorted(s.get(rid, [])) != sorted([hh[0], oh[0]]):
            continue
        rh = [ref for ref, m in published if hh[0] in m.get(rid, ())]
        ro = [ref for ref, m in published if oh[0] in m.get(rid, ())]
        if rh and ro:
            out[rid] = (rh, ro)
    return out


def _dual_mints(root, rel, head_text, staged_text):
    """The reader for _dual_mint_decision: {} off a merge, or when any parent or the trunk cannot be read (fail closed:
    the duplicate-id and MUTATED findings then stand). An unreadable origin/box/* ref only narrows what is published.
    COST: one read per published ref per channel file, only on a merge whose parents both carry the file."""
    if head_text is None or not _merge_in_progress(root):
        return {}
    st, other = _blob(root, "MERGE_HEAD", rel)
    if st != "OK" or not other:
        return {}
    raw = rel.lower().endswith(".json")
    published = []
    for ref in _published_refs(root):
        pst, ptext = _blob(root, ref, rel)
        if pst == "ERROR":
            if ref == PUBLISHED_REF:
                return {}
            continue
        if pst != "OK" or not ptext:
            continue
        m = {}
        for r in _rows(ptext, raw)[0]:
            rid = str((r or {}).get("id") or "").strip()
            if rid:
                m.setdefault(rid, set()).add(_canon_hash(r))
        published.append((ref.replace("refs/remotes/", ""), m))
    return _dual_mint_decision(_rows(head_text, raw)[0], _rows(other, raw)[0], _rows(staged_text, raw)[0], published)


# CLOSED_UNREMEDIATED (proposal org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_PROPOSAL_20261003_REMEDIATION_STATE_
# CLOSED_UNREMEDIATED.md @759c693537; CVO concurrence cvoO_CONCUR_CLOSED_UNREMEDIATED_20261003.md @cfcae02e52). A row
# that finished while world != spec as asserted carries remediation.closure {reason, pointer}; the schema's conditionals
# grade a NEW row, and these two helpers grade what the schema cannot see: the closure on the IN-PLACE clock path (only
# NEW rows meet the schema) and whether the pointer resolves.
CLOSURE_REASONS = ("NOT_A_DEFECT", "CARRIED_BY", "IRREMEDIABLE", "ACCEPTED_BY_RULING")


def _closure_shape_ok(closure):
    """PURE. True iff `closure` is exactly {reason in CLOSURE_REASONS, pointer: a string of 3+ characters}."""
    return (isinstance(closure, dict) and set(closure) == {"reason", "pointer"}
            and closure.get("reason") in CLOSURE_REASONS
            and isinstance(closure.get("pointer"), str) and len(closure["pointer"].strip()) >= 3)


def _closure_pointer_violations(rid, closure, known_ids, path_exists):
    """PURE given its oracles. The pointer's FIRST token is what it names:
    CARRIED_BY -- a row id in the project's channel (never the row itself), or else a repo path that exists;
    ACCEPTED_BY_RULING -- a repo path that exists (an `@vintage` or `:line` suffix is stripped);
    NOT_A_DEFECT / IRREMEDIABLE -- free-form evidence, graded only for presence by the shape check.
    `known_ids` None = the project census could not run -> refused (fail-closed), never waved through."""
    if not isinstance(closure, dict):
        return []
    reason, pointer = closure.get("reason"), str(closure.get("pointer") or "").strip()
    head = pointer.split()[0] if pointer else ""
    path = head.split("@", 1)[0].split(":", 1)[0]
    if reason == "CARRIED_BY":
        if ID_RE.match(head):
            if known_ids is None:
                return ["%s: closure CARRIED_BY %s -- the project's row ids could not be read, so the successor cannot "
                        "be confirmed (fail-closed)" % (rid, head)]
            if head == rid:
                return ["%s: closure CARRIED_BY names the row itself; a carrier is another row or an order" % rid]
            if head not in known_ids:
                return ["%s: closure CARRIED_BY %s -- no such row in the project's channel" % (rid, head)]
            return []
        if path and path_exists(path):
            return []
        return ["%s: closure CARRIED_BY %r -- neither a row id of the project nor a repo path that exists"
                % (rid, head)]
    if reason == "ACCEPTED_BY_RULING":
        if path and path_exists(path):
            return []
        return ["%s: closure ACCEPTED_BY_RULING %r -- the ruling record must be a repo path that exists" % (rid, head)]
    return []


def _disarms_violations(rid, disarms, known_ids):
    """PURE given its oracle. `disarms` (remediation_row.schema.json, 2026-10-05, 1.0.0_SA_CTO~Z on 3.0.0_SA_CVO~Z msg
    29407): the ids a NEW remediation row's disarm clock also disarms -- the append-only landing surface for a row written
    INERT with no `disarm` block (AMGT_RESAPP-Z-S11). Every id must name a row the project's INVESTIGATION plane
    (investigations/ + adjudications/) carries at the graded index, the same reference discipline as a phantom
    `adjudicates` and a CARRIED_BY closure pointer. `known_ids` None = the census could not run -> refused (fail-closed).
    The shape (array of id strings) is the schema's limb; a non-list here returns nothing."""
    if not isinstance(disarms, list) or not disarms:
        return []
    if known_ids is None:
        return ["%s: `disarms` names %d id(s) but the project's investigation-plane ids could not be read, so the "
                "targets cannot be confirmed (fail-closed)" % (rid, len(disarms))]
    unknown = [str(t) for t in disarms if t not in known_ids]
    if unknown:
        return ["%s: `disarms` names %s -- no investigation or adjudication row of the project carries %s. A disarm "
                "lands on a real row; a phantom target disarms nothing and is refused"
                % (rid, ", ".join(unknown), "that id" if len(unknown) == 1 else "those ids")]
    return []


# MONOTONE STATE ADVANCE (2026-09-03, 3.0.0_SA_CVO 93695 item 4, measured on the round-5 slug): a routed remediation
# row's two clocks -- disarm.state / disarm.at and remediation.state -- and its `closed` flag can only land ON that row
# (a second row with the same id is refused; the id IS the graduated item), yet the mutation limb read any in-place
# change as a mutation, so closing S13 and S14 had no gate-clean path and rode the audited override. The advance is
# admitted when, and only when: disarm.state ARMED -> DISARMED with `at` set from null to a timestamp; and/or
# remediation.state OPEN -> REMEDIATED; and/or closed false -> true; and EVERY OTHER FIELD is byte-equal as data. Any
# other change -- a reversal, a reworded remedy, a touched evidence list -- is the mutation it always was.
def _monotone_advance(old, new):
    """PURE. True iff `new` differs from `old` only by a forward move of the remediation row's clocks."""
    if not isinstance(old, dict) or not isinstance(new, dict):
        return False
    # CVO C3 (@cfcae02e52): `closed` true on an ARMED row needs disarm DISARMED in the same row -- on this path too, because
    # only NEW rows meet the schema's allOf. A live hazard never closes ARMED, whatever the remediation state.
    if (new.get("closed") is True and str(new.get("hazard_standing") or "").upper() == "ARMED"
            and (new.get("disarm") or {}).get("state") != "DISARMED"):
        return False
    o = json.loads(json.dumps(old))
    n = json.loads(json.dumps(new))
    moved = False
    od, nd = o.get("disarm"), n.get("disarm")
    if isinstance(od, dict) and isinstance(nd, dict):
        if od.get("state") == "ARMED" and nd.get("state") == "DISARMED" and not od.get("at") and nd.get("at"):
            moved = True
            nd["state"], nd["at"] = od.get("state"), od.get("at")
    orm, nrm = o.get("remediation"), n.get("remediation")
    if isinstance(orm, dict) and isinstance(nrm, dict):
        if orm.get("state") == "OPEN" and nrm.get("state") == "REMEDIATED":
            moved = True
            nrm["state"] = orm.get("state")
        elif (orm.get("state") == "OPEN" and nrm.get("state") == "CLOSED_UNREMEDIATED"
              and "closure" not in orm and _closure_shape_ok(nrm.get("closure"))):
            # CVO C1 (@cfcae02e52): the same in-place clock, with exactly ONE added field, `closure`.
            moved = True
            nrm["state"] = orm.get("state")
            del nrm["closure"]
    if o.get("closed") is False and n.get("closed") is True:
        moved = True
        n["closed"] = False
    # THE FOURTH ADMITTED MOVE (R-19 addendum @06061b21af): `disarm.owner` may change ONLY when the same write appends
    # exactly ONE evidence entry citing a CTO ruling by id and vintage (`R-<n>` and `@<hash>`) and NO clock moves.
    # Measured need: LGIC_CANON-W5-S2 and C-S20 were ruled reassigned (R-19) and the field was immutable, so a ruling
    # had no landing surface; measured hazard the immutability guards: a graded party renaming its way out of a
    # hazard -- which is why the citation is required and the clock may not move in the same write.
    # R-42 EXTENSION (1.0.0_SA_CTO, 2026-09-18): the move admits `remediation.owner` on the SAME terms, because a
    # ruling that reassigns a row must be able to land on EVERY field that names an ADDRESSEE -- and `remediation.owner`
    # names who performs the remedy. Measured need: R-42 placed IRPT_BCKEND's W4-S25/W4-S28 on a live lane after their
    # disarm owner (a CELL) went terminal; `3.0.0_SA_CVO` moved `disarm.owner`, found this limb refused the
    # `remediation.owner` half ALONE and BOTH-TOGETHER, and reported the ruling as DESIRED-NOT-APPLIED rather than
    # attempting a write the gate would refuse. That is the SAME "a ruling had no landing surface" shape the R-19
    # addendum was written to fix, one field over.
    # THE ADDRESSEE SET IS THREE FIELDS, not one, and the third was found by `3.0.0_SA_CVO` reading the SCHEMA rather
    # than the code (97793): `remediation_row.schema.json` describes the TOP-LEVEL `owner` in its own words as "the lane
    # that builds the remediation" -- which names who must ACT, so R-42's principle makes it an addressee too. There is
    # no who-filed field on the remediation plane at all; PROVENANCE for a finding lives on the INVESTIGATION row as
    # `surfaced_by`, which this move never touches. So all three of `owner`, `disarm.owner` and `remediation.owner` are
    # addressees and all three must be able to follow a ruling.
    # ⛔ AND A SUBSET MAY MOVE IN ONE WRITE. This seat first admitted exactly ONE field per move and argued that kept
    # each reassignment inspectable -- that reasoning does not survive the three-field fact: it would force THREE
    # writes to relocate ONE row, each citing the same ruling, for no added discrimination, since the diff already
    # shows which fields moved and to what while the citation records why. The constraints that make the move safe are
    # unchanged and neither is loosened: EXACTLY ONE appended evidence entry citing a ruling by id and vintage, and NO
    # clock may move in the same write. Only the FIELD SET widened.
    owner_moved = False
    _owner_holders = [(o, n), (od, nd), (o.get("remediation"), n.get("remediation"))]
    _changed = [(a, b) for a, b in _owner_holders
                if isinstance(a, dict) and isinstance(b, dict) and a.get("owner") != b.get("owner")]
    if _changed:
        oe, ne = o.get("evidence"), n.get("evidence")
        if (isinstance(oe, list) and isinstance(ne, list) and len(ne) == len(oe) + 1 and ne[:len(oe)] == oe
                and RULING_CITATION_RE.search(str(ne[-1]))):
            owner_moved = True
            for _a, _b in _changed:
                _b["owner"] = _a.get("owner")
            n["evidence"] = oe
    if owner_moved:
        return (not moved) and o == n
    return moved and o == n


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
    if folder_kind and folder_kind != kind and not (folder_kind == "ADJUDICATION" and kind == "INVESTIGATION"):
        v.append("%s: a %s file filed under the %s/ sub-folder -- the path says one kind, the filename "
                 "says another" % (rel, kind, folder_kind.lower() + "s"))
    if folder_kind == "ADJUDICATION" and "ADJUDICATION" not in os.path.basename(rel).upper():
        v.append("%s: a file under adjudications/ is named ADJUDICATION_v<N>.md (annex 4a); this one is not" % rel)
    # RC2: grade what happened to the rows that ALREADY EXISTED, before grading the new ones.
    _mut = _mutation_violations(rel, head, staged)
    # DUAL-MINT (1.0.0_SA_CTO msg 107530): one id minted on two boxes, each copy already published, both kept verbatim side
    # by side by the merge. Admitted with a note; the channel's CVO dispositions it. Neither copy is edited or renumbered.
    _dm = _dual_mints(root, rel, head, staged) if _mut else {}
    if _dm:
        _mut = [x for x in _mut if not any(re.search(r"\b(id|row) %s (occurs|was MUTATED)" % re.escape(i), x) for i in _dm)]
        for _i in sorted(_dm):
            notes.append("%s: DUAL-MINT -- row id %s carries two different rows, one from each merge parent, each already "
                         "on a published ref (HEAD's copy on %s; MERGE_HEAD's copy on %s). Both kept verbatim side by "
                         "side, neither edited or renumbered; the channel's CVO dispositions it (1.0.0_SA_CTO msg 107530)"
                         % (rel, _i, ", ".join(_dm[_i][0]), ", ".join(_dm[_i][1])))
    # A MERGE THAT ONLY CARRIES A ROW CHANGE NOTES IT (3.0.0_SA_CVO ruling @6166eb7b25): only the mutation and deletion
    # findings convert, and only when the whole file is the other parent's and this side never touched it. A duplicate-id
    # finding stays a violation.
    _md = [x for x in _mut if re.search(r"EXISTING row \S+ was (DELETED|MUTATED)", x)]
    if _md:
        _carried, _theirs = _carried_from_other_parent(root, rel)
        if _carried:
            _ids = sorted({m.group(1) for x in _md for m in [re.search(r"EXISTING row (\S+) was", x)] if m})
            notes.append("%s: MERGE CARRIES %d row change(s) it did not make -- NOTED, not refused (3.0.0_SA_CVO ruling "
                         "@6166eb7b25): the merged blob equals MERGE_HEAD's and this side made 0 commits to the file since "
                         "the merge-base. Rows: %s. Other-side commits: %s"
                         % (rel, len(_md), ", ".join(_ids), ", ".join(_theirs[:20]) or "<none listed>"))
            _mut = [x for x in _mut if x not in _md]
    v.extend(_mut)
    added = [r for r in new_rows if r.get("id") not in old_ids]
    # CLOSED_UNREMEDIATED POINTERS: a row ENTERING the state in this commit (a NEW row, or an in-place clock move) has its
    # pointer resolved against the project's channel ids and the index. COST: one id census per file, only when such a
    # row exists. NON-APPLICATION: rows already CLOSED_UNREMEDIATED at HEAD; investigation files.
    if kind == "REMEDIATION":
        _old_state = {r.get("id"): (r.get("remediation") or {}).get("state") for r in old_rows if r.get("id")}
        _entering = [r for r in new_rows if (r.get("remediation") or {}).get("state") == "CLOSED_UNREMEDIATED"
                     and _old_state.get(r.get("id")) != "CLOSED_UNREMEDIATED"]
        if _entering:
            _proj = _folder_identity(rel)[0] or str(_entering[0].get("project") or "")
            _rem_ids, _ = _remediation_ids_for_project(root, _proj) if _proj else (None, "")
            _inv_paths, _ = _index_paths(root, [pat % _proj for pat in INVESTIGATION_PATTERNS]) if _proj else (None, "")
            _known = None
            if _rem_ids is not None and _inv_paths is not None:
                _known = set(_rem_ids)
                for _ip in _inv_paths:
                    _st, _tx = _blob(root, "", _ip)
                    if _st != "OK":
                        _known = None
                        break
                    _known.update(r.get("id") for r in _rows(_tx, _ip.lower().endswith(".json"))[0] if r.get("id"))
            _exists = lambda _p: _blob(root, "", _p)[0] == "OK"  # noqa: E731
            for _r in _entering:
                v.extend(_closure_pointer_violations(_r.get("id"), (_r.get("remediation") or {}).get("closure"),
                                                     _known, _exists))
    # `disarms` TARGETS (2026-10-05): every id a NEW remediation row's `disarms` names is a row of the project's
    # investigation plane at the index. COST: one plane census per file, only when such a row exists. NON-APPLICATION:
    # rows already at HEAD (the mutation limb forbids changing their `disarms`); investigation files.
    if kind == "REMEDIATION":
        _dz_rows = [r for r in new_rows if r.get("id") not in old_ids and r.get("disarms")]
        if _dz_rows:
            _proj = _folder_identity(rel)[0] or str(_dz_rows[0].get("project") or "")
            _pd, _pn = _plane_docs(root, _proj, "INVESTIGATION", "") if _proj else (None, "no project for the file")
            _plane_ids = None if _pd is None else {i for _p, ids in _pd for i in ids}
            for _r in _dz_rows:
                v.extend(_disarms_violations(_r.get("id"), _r.get("disarms"), _plane_ids))
    # FUTURE-DATED STAMP DISCLOSURE (2026-10-02, 1.0.0_SA_CTO~Z on 3.0.0_SA_CVO~Z msg 28369): a NEW row whose surfaced_at is
    # more than 10 min after the commit time is a typed or projected stamp, and it moves every watermark and cursor that
    # reads it. WARN only: it refuses nothing, and arming it as a refusal is announced first. COST: one parse per new row.
    # NON-APPLICATION: rows already at HEAD; a row with no parseable surfaced_at (the schema limb grades that).
    import datetime as _dtm
    _now_utc = _dtm.datetime.now(_dtm.timezone.utc)
    for _r in added:
        _sa = _parse_utc(_r.get("surfaced_at"))
        if _sa is not None and _sa > _now_utc + _dtm.timedelta(minutes=10):
            notes.append("WARN: %s: NEW row %s carries surfaced_at %s, %d min after the commit time %s -- a future "
                         "stamp moves every watermark that reads it; write the time the row is surfaced"
                         % (rel, _r.get("id"), _r.get("surfaced_at"), int((_sa - _now_utc).total_seconds() // 60),
                            _now_utc.strftime("%Y-%m-%dT%H:%MZ")))
    # UNIQUENESS ACROSS DOCUMENTS (94007): every NEW id is unused in every OTHER document of its plane at the index.
    # GRADE WHAT THE CHANGE INTRODUCES, cross-document limb (1.0.0_SA_CTO ruling on 0.0.0_AB_MSTR msg 107744, 2026-10-09):
    # on a MERGE, a row this file already carries on a published ref (origin/CLOUD or an origin/box/*) was landed by
    # another box's push. The merging box did not introduce it and cannot re-mint it, so it is NOTED, not graded here.
    # A row on no published ref (a worker's drain row, a row minted in the merge) is graded exactly as before.
    _uadd = added
    if folder_project and added and _merge_in_progress(root):
        _upub = _published_row_ids(root, rel)
        if _upub:
            _ukeep = [r for r in added if str(r.get("id") or "").strip() not in _upub]
            if len(_ukeep) != len(added):
                notes.append("%s: MERGE -- id-uniqueness across documents not re-graded for %d row(s) this file already "
                             "carries on a published ref: %s (1.0.0_SA_CTO ruling on msg 107744)"
                             % (rel, len(added) - len(_ukeep),
                                ", ".join(sorted(str(r.get("id")) for r in added if r not in _ukeep))))
            _uadd = _ukeep
    if folder_project and _uadd:
        _pd, _pn = _plane_docs(root, folder_project, kind, rel)
        _dv, _dn = _duplicate_id_violations(rel, kind, _uadd, folder_project, _pd, _pn)
        v.extend(_dv)
        notes.extend(_dn)
    # THE ALLOCATOR DISCIPLINE (RULING 2 @9ef9a40aae): W<n> from its own worker only; no W from a seat; C- the CVO's, in
    # adjudications/ only, required once the staged schema admits it.
    _cmt = _committer_serial(root)
    # BOUNDARY (b): one read of the merge's parents per channel file, shared by both limbs.
    _mrg_now = _merge_in_progress(root)
    _pids, _pnote = _parent_row_ids(root, rel) if _mrg_now else (None, "")
    _c_in_schema = "C-" in str(((schema.get("properties") or {}).get("id") or {}).get("pattern", ""))
    _pub = _published_row_ids(root, rel) if _mrg_now else None
    v.extend(_coordinate_violations(rel, folder_kind, added, _cmt, _c_in_schema,
                                    merging=_mrg_now, parent_ids=_pids, published_ids=_pub))
    if _mrg_now and _pids is not None and _pub:
        _onpub = sorted(str(r.get("id")) for r in added
                        if str(r.get("id") or "").strip() in _pids and str(r.get("id") or "").strip() in _pub)
        if _onpub:
            notes.append("%s: MERGE -- coordinate discipline not applied to %d row(s) the published trunk (%s) already "
                         "carries: %s (batch 112)" % (rel, len(_onpub), PUBLISHED_REF + " or an origin/box/* ref", ", ".join(_onpub)))
    # FOREIGN-ROW SWEEP: every new investigation row is the committer's own, or a co-worker's riding along.
    _cw = _seats_with_open_orders(root, folder_project)[0] if folder_project else set()
    _fv, _fn = _foreign_row_violations(rel, kind, added, _cmt, coworkers=_cw,
                                       merging=_mrg_now, parent_ids=_pids)
    v.extend(_fv)
    notes.extend(_fn)
    # PER-FILE MEMO (CVO~Z msg 28783, 2026-10-02): the project-wide reads below are invariant across the rows of ONE
    # file in ONE gate run (same index, same HEAD), but the loop re-ran them for every new row -- ~25 s per row, so a
    # 100-row remediation file ran past 60 min and held the shared index. Each is computed once per file here and
    # handed out as a deep copy, so no row can see another row's mutation. Scope is this call only: nothing is
    # cached across files, commits or the self-test's fixtures.
    _pc_store = {}

    def _pc(fn, *a, **k):
        key = (fn.__name__, a, tuple(sorted(k.items())))
        if key not in _pc_store:
            _pc_store[key] = fn(*a, **k)
        return copy.deepcopy(_pc_store[key])

    for row in added:
        rid = row.get("id")
        if not rid or not ID_RE.match(str(rid)):
            v.append("%s: a NEW row has id=%r, which does not match the id grammar "
                     "<CODE>-(Z-)?(W<n>-|C-)?S<k> (annex v3.2 section 4)" % (rel, rid))
            continue
        if folder_project and row.get("project") and row["project"] != folder_project:
            v.append("%s: NEW row %s says project=%r but the file sits in %r's folder. The path is the "
                     "membership; a row filed under another project is an identity defect."
                     % (rel, rid, row["project"], folder_project))
        # R-28: a CARRIED row is not re-graded on the owner-and-carrier limbs; `_pids` None (no merge, or parents
        # unreadable) carries nothing, so off a merge and fail-closed every limb grades.
        v.extend(_check_row(row, kind, schema, carried=_mrg_now and _row_was_carried(row, _pids)))
        # GATE (iii), both limbs, both route shapes: a NEW tree row that carries a route waits for every TO under
        # the project to be terminal AND every investigation item under it to be dispositioned.
        # spine v3.0 L10 carrier 6: the precondition applies to EVERY new remediation row under a tree project (the slug
        # is cut at round close), not only to a route-carrying one; a DECOMP_INVALIDATING disposition (an investigation
        # OR an adjudication row) waits the same way.
        _route_word = None
        if kind == "REMEDIATION" and folder_kind == "REMEDIATION":
            _route_word = ("route=%s (a legacy v2 pair)" % row.get("route")) if row.get("route") is not None \
                else "the slug (spine v3: every new remediation row)"
        elif kind == "INVESTIGATION" and folder_kind in ("INVESTIGATION", "ADJUDICATION") and row.get("disposition") == "DECOMP_INVALIDATING":
            _route_word = "disposition=DECOMP_INVALIDATING (carried in the slug)"
        if folder_project and _route_word is not None:
            _mrg = _pc(_merge_in_progress, root)
            # PROVENANCE COMES FROM THE `_pids` READ ALREADY TAKEN ABOVE for the coordinate limb and
            # the foreign-row sweep -- one read of the merge's parents per channel file, now shared by
            # four limbs instead of two. No second read, and no way for the two answers to disagree.
            # THE SWEEP WATERMARK: read from THIS document's staged bytes; absent -> the whole-project rule.
            _wm = _sweep_watermark(staged)
            pre = _route_precondition_violations(root, rel, row, folder_project, route_word=_route_word,
                                                 merging=_mrg, parent_ids=_pids, watermark=_wm)
            pre.extend(_investigations_precondition_violations(rel, row, folder_project, _route_word,
                                                               _pc(_latest_dispositions, root, folder_project),
                                                               merging=_mrg, parent_ids=_pids,
                                                               gating=_pc(_gating_item_ids, root, folder_project),
                                                               watermark=_wm,
                                                               surfaced_at=(_pc(_item_surfaced_at, root, folder_project)
                                                                            if _wm is not None else None)))
            # EN-g-37 / S74: rowlessness only -- a GRADUATED item under this project with no
            # remediation row bearing its id. Staleness (a row that EXISTS but has not moved) is a
            # DIFFERENT question this limb cannot see and does not attempt (EN-k-38).
            pre.extend(_graduated_without_row_violations(rel, row, folder_project, _route_word,
                                                         _pc(_latest_dispositions, root, folder_project),
                                                         _pc(_remediation_ids_for_project, root, folder_project),
                                                         merging=_mrg, parent_ids=_pids))
            # EN-k-38 / S75: staleness only -- an EXISTING remediation row under this project that is
            # OPEN, owned and has not moved for STALE_OPEN_ROW_N_ROUNDS or more rounds against THIS
            # slug's own round. REMEDIATION-plane only: `remediation.round` is the field this limb reads,
            # and only a NEW remediation row carries a round for THIS slug to measure against -- a
            # DECOMP_INVALIDATING investigation row (the other route_word shape above) has no round field
            # at all and is not this limb's question.
            if kind == "REMEDIATION" and folder_kind == "REMEDIATION":
                _kv, _kn = _stale_open_row_violations(rel, row, folder_project, _route_word,
                                                      _pc(_remediation_rows_for_project, root, folder_project),
                                                      merging=_mrg, parent_ids=_pids)
                pre.extend(_kv)
                notes.extend(_kn)
            v.extend(pre)
            if _mrg:
                _carried = _row_was_carried(row, _pids)
                notes.append("%s: MERGE COMMIT -- L10 precondition for %s on row %s: %s. The discriminator is "
                             "CARRIED-vs-MINTED against the merge's parents (Andrew ~19:3xZ; supersedes the "
                             "`Z-` fabric proxy, which inverted by device). NOT exempt on a merge: the "
                             "duplicate-id limb."
                             % (rel, folder_project, rid,
                                "NOT evaluated -- CARRIED by the merge, routed at its own authorship"
                                if _carried else
                                ("EVALUATED -- MINTED in this commit, the precondition binds" if _pids is not None
                                 else "EVALUATED -- the merge's parents could not be read, fail-closed")))
            elif not pre:
                _o, _t, _n = _open_tos_for_project(root, folder_project)
                _l, _u, _nf, _ = _pc(_latest_dispositions, root, folder_project)
                # THE ACCEPTANCE SWEEP (S169, AMGT-rk-57): a NOTE beside the census note, never a
                # violation -- a slug is not refused on a FAIL (the rule at ~:991). The round is the
                # NEW remediation row's own `round`, the same field `_stale_open_row_violations` reads.
                _acc_round = _round_num(row.get("round"))
                _ak = ("_acceptance_sweep", folder_project, _acc_round, _mrg)
                if _ak not in _pc_store:
                    _pc_store[_ak] = _acceptance_sweep(root, folder_project, round_n=_acc_round, merging=_mrg)
                _acc_sweep = copy.deepcopy(_pc_store[_ak])
                _acc_fails = _flagged_rows(_acc_sweep, "FAIL")
                _acc_unv = _flagged_rows(_acc_sweep, "UNVERIFIABLE")
                notes.append("%s: ACCEPTANCE (round %s, the slug's own): PASS %d / FAIL %d / "
                             "UNVERIFIABLE %d of %d criteria over %d order(s); unrounded %d; FAIL: %s; "
                             "UNVERIFIABLE: %s"
                             % (rel, _acc_round if _acc_round is not None else "?", _acc_sweep["PASS"],
                                _acc_sweep["FAIL"], _acc_sweep["UNVERIFIABLE"], _acc_sweep["criteria"],
                                len(_acc_sweep["orders"]), _acc_sweep["unrounded"],
                                "; ".join(_acc_fails) or "none", "; ".join(_acc_unv) or "none"))
                if _o:
                    _basis = ("LD-0562 / COO 22245 / " + POSN_R3_EXCEPTION_PIN
                              if _posn_round3_terminal_exception(root, rel, row, folder_project, _o, _t)
                              else "Andrew call 1 YES / CTO 21533 / " + POSN_R2_EXCEPTION_PIN)
                    notes.append("%s: L10 NAMED EXCEPTION for %s -- %s; "
                                 "%d of %d orders STILL OPEN, explicitly unrun: %s. Exact row and order "
                                 "content matched; other limbs passed. NOT the broad override."
                                 % (rel, rid, _basis, len(_o), _t, ", ".join(_o)))
                else:
                    notes.append("%s: L10 precondition for %s -- %d task order(s) at HEAD on both roots, 0 open; %d "
                             "investigation item(s) across %d channel file(s) in the index, 0 undispositioned; "
                             "route admitted%s" % (rel, rid, _t, len(_l or {}), _nf, ("; " + _n) if _n else ""))
    notes.append("%s: %d new row(s) of %d total checked (%d pre-existing, NOT re-graded)"
                 % (rel, len(added), len(new_rows), len(old_ids)))
    return (v, notes)


# The parent set for the DRAIN arms: every row id those arms treat as having been CARRIED by the
# worker branch being merged. Boundary (b) makes that explicit -- an arm about "the worker minted
# this" must SAY the parent carried it, or the row is minted in the merge and graded as the
# committing seat's, which for a bare S<k> from a SEAT is lawful and would silently pass.
_DRAIN_PIDS = {"X_PRJ-W2-S1", "X_PRJ-W3-S1", "X_PRJ-S9", "X_PRJ-W2-S2", "X_PRJ-S40"}
_S34_INV = "org/missions/D11/NFRA/NFRA_COMPEFFICACY/surprise-channel/investigations/INVESTIGATION_v1.md"
_S34_ADJ = "org/missions/D11/NFRA/NFRA_COMPEFFICACY/surprise-channel/adjudications/ADJUDICATION_v1.md"


def _self_test(root):
    """The battery of gate (iii)'s second limb: five injected arms (pure) and one live census. Red and green."""
    row = {"id": "X_PRJ-S9", "route": "SPEC_ERROR"}
    # PROOF TERMINALITY fixtures: LGIC_NAMING's real round-2 orders (status `pending` at HEAD b02fdaa849, proofs VALID).
    _ln = "org/missions/D14/LGIC/LGIC_NAMING/"
    _LN_E3 = _ln + "task-orders/LGIC_NAMING.TO-LN-e-3-r2.namer-comparison.md"
    _LN_E5 = _ln + "task-orders/LGIC_NAMING.TO-LN-e-5-r2.reader-scoring.md"
    _LN_E3_INST = _ln + "deliverables/0.9.0_WK_LGIC_NAMING~6/LGIC_NAMING.TO-LN-e-3-r2.namer-comparison.proof_of_spec.json"
    _LN_E5_INST = _ln + "deliverables/0.9.0_WK_LGIC_NAMING~6/LGIC_NAMING.TO-LN-e-5-r2.reader-scoring.proof_of_spec.json"

    def _head_text(r, rel):
        return _blob(r, "HEAD", rel)[1]

    class _FakeRun(object):
        def __init__(self, rc):
            self.returncode, self.stdout, self.stderr = rc, "INVALID (rc=%d)" % rc, ""

    def _raise(argv):
        raise RuntimeError("injected")
    import tempfile as _tf
    _tmpd = _tf.mkdtemp(prefix="srg-honour-")
    _tlog = os.path.join(_tmpd, "audit.log")
    def _honour_line():
        p = _honour_audit_line(root, "why: repro", log_path=_tlog, agent="9.9.9_XX_TEST", now="2026-09-11T00:00:00Z")
        txt = open(p, encoding="utf-8").read() if p else ""
        return txt
    # DUAL-MINT fixtures (1.0.0_SA_CTO msg 107530): the AMGT_HARVST-Z-S106 shape -- site Z's copy on origin/CLOUD,
    # dell1's on origin/box/dell1, one shared row X-S1 untouched.
    _dz = {"id": "X_PRJ-Z-S106", "one_line": "site Z copy"}
    _dd = {"id": "X_PRJ-Z-S106", "one_line": "dell1 copy"}
    _d0 = {"id": "X_PRJ-S1", "one_line": "shared"}
    _dn = {"id": "X_PRJ-S2", "one_line": "a new row appended later"}
    _dpub = [("origin/CLOUD", {"X_PRJ-Z-S106": {_canon_hash(_dz)}, "X_PRJ-S1": {_canon_hash(_d0)}}),
             ("origin/box/dell1", {"X_PRJ-Z-S106": {_canon_hash(_dd)}, "X_PRJ-S1": {_canon_hash(_d0)}})]
    _djs = lambda rows: json.dumps(rows)  # noqa: E731
    arms = [
        # DUAL-MINT (1.0.0_SA_CTO msg 107530): both copies kept side by side, each on a published ref -> admitted.
        ("DUAL-MINT: one id, a different row in each parent, both kept in the merge, each on a published ref -> admitted, refs named",
         lambda: _dual_mint_decision([_d0, _dd], [_d0, _dz], [_d0, _dd, _dz], _dpub)
         == {"X_PRJ-Z-S106": (["origin/box/dell1"], ["origin/CLOUD"])}),
        ("DUAL-MINT NARROWNESS: the other parent's copy is on NO published ref -> NOT admitted",
         lambda: _dual_mint_decision([_d0, _dd], [_d0, _dz], [_d0, _dd, _dz], _dpub[1:]) == {}),
        ("DUAL-MINT NARROWNESS: the merge kept only ONE copy (one overwrote the other) -> NOT admitted (a mutation)",
         lambda: _dual_mint_decision([_d0, _dd], [_d0, _dz], [_d0, _dz], _dpub) == {}),
        ("DUAL-MINT NARROWNESS: a copy EDITED in the merge, or a third copy -> NOT admitted",
         lambda: (_dual_mint_decision([_d0, _dd], [_d0, _dz], [_d0, _dd, dict(_dz, one_line="edited")], _dpub) == {}
                  and _dual_mint_decision([_d0, _dd], [_d0, _dz], [_d0, _dd, _dz, _dz], _dpub) == {})),
        ("DUAL-MINT NARROWNESS: the same row in both parents is no dual mint -> nothing admitted",
         lambda: _dual_mint_decision([_d0, _dz], [_d0, _dz], [_d0, _dz, _dz], _dpub) == {}),
        ("DUAL-MINT FILTER: the duplicate-id and MUTATED findings for the admitted id are the ONLY ones it removes",
         lambda: (lambda mut: (len(mut) == 3 and [x for x in mut if not any(
             re.search(r"\b(id|row) %s (occurs|was MUTATED)" % re.escape(i), x) for i in ["X_PRJ-Z-S106"])]
             == [m for m in mut if "X_PRJ-S1 " in m]))(
             _mutation_violations("x.json", _djs([_d0, _dd]), _djs([dict(_d0, one_line="edited"), _dd, _dz])))),
        # THE ROW'S OWN WORKSTREAM (1.0.0_SA_CTO msg 107639): another lane's open order does not hold a remediation row.
        ("WORKSTREAM: another lane's open order does NOT block a row of workstream ~Y",
         lambda: _route_precondition_violations(
             None, "r", {"id": "X_PRJ-D2-W7-S1", "route": "SPEC_ERROR"}, "X_PRJ",
             open_tos=(["X_PRJ.TO-p-1.a.md [issued]"], 3, ""), route_word="the slug",
             workstreams=({"~Y"}, {"X_PRJ.TO-p-1.a.md": ("~P", "0.9.0_WK_X_PRJ~9"),
                                   "X_PRJ.TO-y-1.b.md": ("~Y", "0.9.0_WK_X_PRJ~7")})) == []),
        ("WORKSTREAM: the row's OWN lane's open order still blocks it",
         lambda: any("X_PRJ.TO-y-1.b.md" in x and "workstream(s) ~Y" in x for x in _route_precondition_violations(
             None, "r", {"id": "X_PRJ-D2-W7-S1", "route": "SPEC_ERROR"}, "X_PRJ",
             open_tos=(["X_PRJ.TO-p-1.a.md [issued]", "X_PRJ.TO-y-1.b.md [issued]"], 3, ""), route_word="the slug",
             workstreams=({"~Y"}, {"X_PRJ.TO-p-1.a.md": ("~P", "0.9.0_WK_X_PRJ~9"),
                                   "X_PRJ.TO-y-1.b.md": ("~Y", "0.9.0_WK_X_PRJ~7")})))),
        ("WORKSTREAM: an open order of UNKNOWN workstream still blocks (never looser)",
         lambda: _scope_open_to_workstreams(["X_PRJ.TO-q-1.c.md [issued]"], {"~Y"}, {"X_PRJ.TO-q-1.c.md": (None, "")})
         == ["X_PRJ.TO-q-1.c.md [issued]"]),
        ("WORKSTREAM resolve: worker coordinate W7 -> the order issued to ~7 -> ~Y; an order id TO-p-1 -> ~P",
         lambda: (_row_workstreams({"id": "X_PRJ-D2-W7-S1"}, "X_PRJ",
                                   {"X_PRJ.TO-y-1.b.md": ("~Y", "0.9.0_WK_X_PRJ~7"), "X_PRJ.TO-p-1.a.md": ("~P", "x")})
                  == {"~Y"}
                  and _row_workstreams({"id": "X_PRJ-S4", "evidence": ["per TO-p-1 criterion 2"]}, "X_PRJ",
                                       {"X_PRJ.TO-p-1.a.md": ("~P", "x"), "X_PRJ.TO-p-11.z.md": ("~M", "y")}) == {"~P"})),
        ("WORKSTREAM resolve: no cited order, or a cited order with no workstream -> None (the project-wide wait)",
         lambda: (_row_workstreams({"id": "X_PRJ-S4"}, "X_PRJ", {"X_PRJ.TO-p-1.a.md": ("~P", "x")}) is None
                  and _row_workstreams({"id": "X_PRJ-W7-S1"}, "X_PRJ", {"X_PRJ.TO-y-1.b.md": (None, "0.9.0_WK_X_PRJ~7")})
                  is None)),
        ("WORKSTREAM: an order's workstream is its <workstream> tag, else its issuing COO's lane",
         lambda: (_order_workstream("<issued_by>2.0.0_SA_COO~Y2</issued_by>\n<workstream>~Y</workstream>") == "~Y"
                  and _order_workstream("<issued_by>2.0.0_SA_COO~P2</issued_by>") == "~P"
                  and _order_workstream("<issued_by>2.0.0_SA_COO</issued_by>") is None)),
        # GRADE WHAT THE CHANGE INTRODUCES (1.0.0_SA_CTO msg 107628): an admitted pair already at HEAD freezes nothing.
        ("PAIR AT HEAD: a commit that appends a NEW id beside an admitted DUAL-MINT pair -> passes",
         lambda: _mutation_violations("x.json", _djs([_d0, _dd, _dz]), _djs([_d0, _dd, _dz, _dn])) == []),
        ("PAIR AT HEAD: a NEW duplicate the diff introduces (the new id twice) -> still refused",
         lambda: any("id X_PRJ-S2 occurs 2 times" in x for x in _mutation_violations(
             "x.json", _djs([_d0, _dd, _dz]), _djs([_d0, _dd, _dz, _dn, dict(_dn, one_line="other")])))),
        ("PAIR AT HEAD: a THIRD copy of the paired id -> refused",
         lambda: any("id X_PRJ-Z-S106 occurs 3 times" in x for x in _mutation_violations(
             "x.json", _djs([_d0, _dd, _dz]), _djs([_d0, _dd, _dz, dict(_dz, one_line="third")])))),
        ("PAIR AT HEAD: one copy EDITED -> MUTATED; one copy DROPPED -> DELETED",
         lambda: (any("X_PRJ-Z-S106 was MUTATED" in x for x in _mutation_violations(
             "x.json", _djs([_d0, _dd, _dz]), _djs([_d0, _dd, dict(_dz, one_line="edited")])))
             and any("X_PRJ-Z-S106 was DELETED" in x for x in _mutation_violations(
                 "x.json", _djs([_d0, _dd, _dz]), _djs([_d0, _dd]))))),
        # MERGE CARRIED, NOT MADE (3.0.0_SA_CVO ruling @6166eb7b25): the pure decision and its three narrowness arms.
        ("MERGE CARRIED: merged blob equals the other parent's and the local side made 0 commits -> carried (noted)",
         lambda: _carried_decision("a1b2c3", "a1b2c3", 0) is True),
        ("MERGE CARRIED NARROWNESS: the local side also touched the file -> NOT carried (refused)",
         lambda: _carried_decision("a1b2c3", "a1b2c3", 1) is False),
        ("MERGE CARRIED NARROWNESS: the merged blob differs from the other parent's (merge-made or conflict-resolved) -> NOT carried",
         lambda: _carried_decision("a1b2c3", "a1b2c4", 0) is False),
        ("MERGE CARRIED fail-closed: a failed blob read (empty id) -> NOT carried",
         lambda: _carried_decision("", "", 0) is False),
        ("MERGE CARRIED off a merge: no MERGE_HEAD -> NOT carried, without reading anything",
         lambda: (_merge_in_progress(root) or _carried_from_other_parent(root, "x/INVESTIGATION_v1.md") == (False, []))),
        # THE HONOUR AUDIT LINE (2026-09-11, 0.0.0_AB_MSTR 95721): the gate records every override it honours.
        ("honour audit line: written with the HONOURED token, agent, reason and UNVERIFIED provenance",
         lambda: (lambda t: "SURPRISE-ROW-OVERRIDE-HONOURED  9.9.9_XX_TEST  reason=why: repro  provenance=UNVERIFIED-BY-GATE" in t
                  and t.startswith("2026-09-11T00:00:00Z ") and "SURPRISE-ROW-OVERRIDE  " not in t.replace("HONOURED  ", ""))(_honour_line())),
        ("honour audit line: an unwritable log path returns None and never raises (the override stays honoured)",
         lambda: _honour_audit_line(root, "x", log_path=os.path.join(_tmpd, "audit.log", "nope", "z.log")) is None),
        ("one item UNDER_INVESTIGATION -> refused, names it",
         lambda: any("X_PRJ-S1" in x and "NOT dispositioned" in x for x in _investigations_precondition_violations(
             "r", row, "X_PRJ", "route=SPEC_ERROR", ({"X_PRJ-S1": "UNDER_INVESTIGATION", "X_PRJ-S2": "GRADUATED"}, [], 1, "")))),
        # spine v3.19 (report 3 item 1.2): only BLOCKING or ARMED rows hold the slug.
        ("v3.19: an unarmed OBSERVATION item UNDER_INVESTIGATION does NOT hold the slug",
         lambda: _investigations_precondition_violations(
             "r", row, "X_PRJ", "route=SPEC_ERROR", ({"X_PRJ-S1": "UNDER_INVESTIGATION"}, [], 1, ""), gating=set()) == []),
        ("v3.19: a BLOCKING or ARMED item UNDER_INVESTIGATION still holds it",
         lambda: any("X_PRJ-S1" in x for x in _investigations_precondition_violations(
             "r", row, "X_PRJ", "route=SPEC_ERROR", ({"X_PRJ-S1": "UNDER_INVESTIGATION"}, [], 1, ""), gating={"X_PRJ-S1"}))),
        ("v3.19: gating None (the read failed) gates on EVERY item, the stricter rule",
         lambda: _investigations_precondition_violations(
             "r", row, "X_PRJ", "route=SPEC_ERROR", ({"X_PRJ-S1": "UNDER_INVESTIGATION"}, [], 1, ""), gating=None) != []),
        # THE SWEEP WATERMARK (1.0.0_SA_CTO RULING 102674; 3.0.0_SA_CVO 102703).
        ("watermark: a line-anchored <sweep_watermark> parses; prose, two different values and a bad time read None",
         lambda: (_sweep_watermark("x\n<sweep_watermark>2026-09-29T09:30:00Z</sweep_watermark>\n") is not None
                  and _sweep_watermark("the `<sweep_watermark>2026-09-29T09:30Z</sweep_watermark>` tag") is None
                  and _sweep_watermark("<sweep_watermark>2026-09-29T09:30Z</sweep_watermark>\n"
                                       "<sweep_watermark>2026-09-29T10:30Z</sweep_watermark>\n") is None
                  and _sweep_watermark("<sweep_watermark>2026-13-45T09:30Z</sweep_watermark>\n") is None)),
        ("watermark: an order issued AFTER it, still open, does NOT hold the slug",
         lambda: _route_precondition_violations(
             root, "r", row, "X_PRJ", open_tos=(["X_PRJ.TO-9.late.md [pending]"], 5, ""), route_word="the slug",
             watermark=_parse_utc("2026-09-29T09:30:00Z"),
             issued_at={"X_PRJ.TO-9.late.md": _parse_utc("2026-09-29T10:00:00Z")}) == []),
        ("watermark: an order issued BEFORE it, still open, DOES hold the slug",
         lambda: any("X_PRJ.TO-3.early.md" in x for x in _route_precondition_violations(
             root, "r", row, "X_PRJ", open_tos=(["X_PRJ.TO-3.early.md [pending]", "X_PRJ.TO-9.late.md [pending]"], 5, ""),
             route_word="the slug", watermark=_parse_utc("2026-09-29T09:30:00Z"),
             issued_at={"X_PRJ.TO-3.early.md": _parse_utc("2026-09-29T08:00:00Z"),
                        "X_PRJ.TO-9.late.md": _parse_utc("2026-09-29T10:00:00Z")}))),
        ("watermark: an open order whose issue time is unreadable still holds the slug",
         lambda: _route_precondition_violations(
             root, "r", row, "X_PRJ", open_tos=(["X_PRJ.TO-4.x.md [pending]"], 5, ""), route_word="the slug",
             watermark=_parse_utc("2026-09-29T09:30:00Z"), issued_at={}) != []),
        ("watermark: NO watermark keeps the whole-project rule (a late open order holds)",
         lambda: _route_precondition_violations(
             root, "r", row, "X_PRJ", open_tos=(["X_PRJ.TO-9.late.md [pending]"], 5, ""), route_word="the slug",
             watermark=None, issued_at={"X_PRJ.TO-9.late.md": _parse_utc("2026-09-29T10:00:00Z")}) != []),
        ("watermark: an ARMED item surfaced AFTER it does not hold the slug; one surfaced BEFORE does",
         lambda: (_investigations_precondition_violations(
                      "r", row, "X_PRJ", "the slug", ({"X_PRJ-S7": "UNDER_INVESTIGATION"}, [], 1, ""), gating={"X_PRJ-S7"},
                      watermark=_parse_utc("2026-09-29T09:30:00Z"),
                      surfaced_at={"X_PRJ-S7": _parse_utc("2026-09-29T09:45:00Z")}) == []
                  and _investigations_precondition_violations(
                      "r", row, "X_PRJ", "the slug", ({"X_PRJ-S7": "UNDER_INVESTIGATION"}, [], 1, ""), gating={"X_PRJ-S7"},
                      watermark=_parse_utc("2026-09-29T09:30:00Z"),
                      surfaced_at={"X_PRJ-S7": _parse_utc("2026-09-29T09:00:00Z")}) != [])),
        # spine v3.19 (report 3 item 1.3): the round tag the per-round census reads.
        ("v3.19: <round> tag parses at line start, `2` and `v2` alike; a prose mention does not",
         lambda: (int(TO_ROUND_RE.search("x\n<round>2</round>\n").group(1)) == 2
                  and int(TO_ROUND_RE.search("<round>v2</round>").group(1)) == 2
                  and TO_ROUND_RE.search("the <round>3</round> tag is prose") is None)),
        # L10 MERGE EXEMPTION (0.0.0_AB_MSTR 94293) + the NARROWNESS arm that earns it. Written as a
        # PARAMETER defaulting False on 94295's constraint: an exemption read INTERNALLY from
        # MERGE_HEAD would put all SEVEN direct-call arms below on the exempt path whenever a merge
        # happened to be open, and they would pass while testing nothing -- the fix disarming the
        # battery that guards the limb it fixes, silently, because a disarmed arm and a passing arm
        # print the same line. The False default means those seven arms need no edit and still mean
        # what they meant.
        # CARRIED-vs-MINTED REPLACES THE `Z-` FABRIC PROXY IN BOTH PRECONDITION LIMBS
        # (1.0.0_SA_CTO~Z as gate owner, on Andrew-direct 2026-09-11 ~19:3xZ: "the surprise-row gate
        # must be project specific"). The five arms below REPLACE five that asserted the proxy; they
        # are rewritten rather than deleted, because the NARROWNESS they protected -- the exemption
        # must not become blanket again -- is exactly what still has to be proved.
        # WHY THE PROXY WENT: `_row_is_other_fabric` is a CONSTANT, not a comparison. Its docstring
        # says a row without `Z-` is "THIS fabric's record" -- true on the laptop, INVERTED on site Z.
        # Measured: 100 already-committed IRPT_FNTEND rows arriving by an authorised CLOUD->SITEZ
        # merge read as native here and refused the leg. A guard whose truth depends on which box
        # runs it is not a guard, and no arm written on one box could have caught it.
        # RED-FIRST, the discriminating exercise 4.0.0_SA_CRO~Z set as the acceptance bar (21600):
        # these arms were run against the PRE-FIX code and FAILED ON THE ANSWER, not the signature --
        # 12 failed / 4 controls green before, 0 failed / 4 controls green after.
        ("carried/minted MERGE: a row CARRIED by the merge -> NOT evaluated (history arriving)",
         lambda: _route_precondition_violations(None, "r", {"id": "X_PRJ-S3", "route": "SPEC_ERROR"},
                                                "X_PRJ", open_tos=({"TO-1"}, 3, ""), route_word="w",
                                                merging=True, parent_ids={"X_PRJ-S3"}) == []),
        ("carried/minted NARROWNESS: a row MINTED in the merge commit -> STILL REFUSED. This is the "
         "arm that earns the exemption: it is the merging seat's own routing act.",
         lambda: _route_precondition_violations(None, "r", {"id": "X_PRJ-S3", "route": "SPEC_ERROR"},
                                                "X_PRJ", open_tos=({"TO-1"}, 3, ""), route_word="w",
                                                merging=True, parent_ids=set()) != []),
        ("carried/minted NARROWNESS, THE INVERSION THE PROXY GOT WRONG: a MINTED row WITH a `Z-` "
         "coordinate -> STILL REFUSED. The old test exempted exactly this.",
         lambda: _route_precondition_violations(None, "r", {"id": "X_PRJ-Z-S3", "route": "SPEC_ERROR"},
                                                "X_PRJ", open_tos=({"TO-1"}, 3, ""), route_word="w",
                                                merging=True, parent_ids=set()) != []),
        ("carried/minted FABRIC-AGNOSTIC: a CARRIED row is exempt with OR without `Z-` -- the answer "
         "must not depend on which device runs the gate",
         lambda: _route_precondition_violations(None, "r", {"id": "X_PRJ-S3", "route": "SPEC_ERROR"},
                                                "X_PRJ", open_tos=({"TO-1"}, 3, ""), route_word="w",
                                                merging=True, parent_ids={"X_PRJ-S3"}) == []
         and _route_precondition_violations(None, "r", {"id": "X_PRJ-Z-S3", "route": "SPEC_ERROR"},
                                            "X_PRJ", open_tos=({"TO-1"}, 3, ""), route_word="w",
                                            merging=True, parent_ids={"X_PRJ-Z-S3"}) == []),
        ("carried/minted FAIL-CLOSED: parent_ids=None (parents unreadable) exempts NOTHING, even a "
         "`Z-` row. 'The parents carry nothing' and 'could not be read' stay different answers.",
         lambda: _route_precondition_violations(None, "r", {"id": "X_PRJ-Z-S3", "route": "SPEC_ERROR"},
                                                "X_PRJ", open_tos=({"TO-1"}, 3, ""), route_word="w",
                                                merging=True, parent_ids=None) != []),
        ("carried/minted: a CARRIED row OFF a merge -> STILL REFUSED (the exemption is the merge's)",
         lambda: _route_precondition_violations(None, "r", {"id": "X_PRJ-S3", "route": "SPEC_ERROR"},
                                                "X_PRJ", open_tos=({"TO-1"}, 3, ""), route_word="w",
                                                merging=False, parent_ids={"X_PRJ-S3"}) != []),
        ("carried/minted: an UNPARSEABLE id is never exempt -- an id the gate cannot read cannot be "
         "matched against a parent",
         lambda: _route_precondition_violations(None, "r", {"id": "not-an-id", "route": "SPEC_ERROR"},
                                                "X_PRJ", open_tos=({"TO-1"}, 3, ""), route_word="w",
                                                merging=True, parent_ids={"X_PRJ-S3"}) != []),
        ("carried/minted (investigations limb): CARRIED -> NOT evaluated; MINTED -> REFUSED; a MINTED "
         "`Z-` row -> REFUSED; parents unreadable -> REFUSED",
         lambda: _investigations_precondition_violations(
             "r", {"id": "X_PRJ-S3"}, "X_PRJ", "route=SPEC_ERROR",
             ({"X_PRJ-S1": "UNDER_INVESTIGATION"}, [], 1, ""), merging=True,
             parent_ids={"X_PRJ-S3"}) == []
         and _investigations_precondition_violations(
             "r", {"id": "X_PRJ-S3"}, "X_PRJ", "route=SPEC_ERROR",
             ({"X_PRJ-S1": "UNDER_INVESTIGATION"}, [], 1, ""), merging=True, parent_ids=set()) != []
         and _investigations_precondition_violations(
             "r", {"id": "X_PRJ-Z-S3"}, "X_PRJ", "route=SPEC_ERROR",
             ({"X_PRJ-S1": "UNDER_INVESTIGATION"}, [], 1, ""), merging=True, parent_ids=set()) != []
         and _investigations_precondition_violations(
             "r", {"id": "X_PRJ-Z-S3"}, "X_PRJ", "route=SPEC_ERROR",
             ({"X_PRJ-S1": "UNDER_INVESTIGATION"}, [], 1, ""), merging=True, parent_ids=None) != []),
        ("carried/minted READ: BOTH precondition limbs decide on _row_was_carried, and NEITHER still "
         "calls the fabric proxy -- read from the functions, not the module",
         lambda: "_row_was_carried(row, parent_ids)" in inspect.getsource(_route_precondition_violations)
         and "_row_was_carried(row, parent_ids)" in inspect.getsource(_investigations_precondition_violations)
         and "_row_is_other_fabric" not in inspect.getsource(_route_precondition_violations)
         and "_row_is_other_fabric" not in inspect.getsource(_investigations_precondition_violations)),
        ("carried/minted READ: the production caller passes the SHARED _pids to both limbs, so the "
         "coordinate limb and the precondition limbs cannot disagree about provenance",
         lambda: inspect.getsource(check_file).count("parent_ids=_pids") >= 3),
        # (c) THE READ. Structural, and read from the FUNCTION not the module -- a checker that greps its
        # module finds its own occurrence first (learned twice tonight in to-pipeline-gate).
        ("(c) read: _open_tos_for_project takes the ref from `merging`, not always HEAD",
         lambda: '_blob(root, "" if merging else "HEAD", p)' in inspect.getsource(_open_tos_census)),
        ("(c) read: the production caller passes merging through",
         lambda: "_open_tos_for_project(root, code, merging=merging, round_n=_round_num(row.get(\"round\")))"
         in inspect.getsource(_route_precondition_violations)),
        # THE C- ARM UNDER merging (0.0.0_AB_MSTR 94311, rule stated by 3.0.0_SA_CVO 94313). The MUTANT is
        # the arm that earns it: an integrator MINTING a C- row by hand on a merge must still refuse.
        ("C- MERGE: a CVO-surfaced C- row carried by a DIFFERENT committer on a merge -> admitted",
         lambda: _coordinate_violations("org/missions/D0/NFRA/X/surprise-channel/adjudications/ADJUDICATION_v1.md",
                                        "ADJUDICATION", [{"id": "X-C-S7", "surfaced_by": "3.0.0_SA_CVO"}],
                                        "0.0.0_AB_MSTR", False, merging=True,
                                        parent_ids={"X-C-S7"}) == []),
        ("C- MERGE: a ~lane surfacer (3.0.0_SA_CVO~Z, the other fabric's) is the CVO -> admitted",
         lambda: _coordinate_violations("org/missions/D0/NFRA/X/surprise-channel/adjudications/ADJUDICATION_v1.md",
                                        "ADJUDICATION", [{"id": "X-C-S8", "surfaced_by": "3.0.0_SA_CVO~Z"}],
                                        "0.0.0_AB_MSTR", False, merging=True,
                                        parent_ids={"X-C-S8"}) == []),
        ("C- MERGE MUTANT: a C- row the INTEGRATOR surfaced (not the CVO) -> still REFUSED on a merge",
         lambda: any("is not 3.0.0_SA_CVO" in x and "surfacer" in x for x in _coordinate_violations(
             "org/missions/D0/NFRA/X/surprise-channel/adjudications/ADJUDICATION_v1.md", "ADJUDICATION",
             [{"id": "X-C-S9", "surfaced_by": "0.0.0_AB_MSTR"}], "0.0.0_AB_MSTR", False, merging=True,
             parent_ids={"X-C-S9"}))),
        # BOUNDARY (b) -- THE ARM THAT MAKES THE EXEMPTION A MEASUREMENT RATHER THAN AN INFERENCE:
        # the same CVO-surfaced row, but present in NEITHER parent, was MINTED in the merge commit and
        # is graded as the COMMITTER's. Without this the integrator could exempt any row by writing a
        # surfaced_by it chose.
        ("(b) C- MINTED: a CVO-surfaced C- row in NEITHER parent -> graded as the COMMITTER's, REFUSED",
         lambda: any("is not 3.0.0_SA_CVO" in x and "committer" in x for x in _coordinate_violations(
             "org/missions/D0/NFRA/X/surprise-channel/adjudications/ADJUDICATION_v1.md", "ADJUDICATION",
             [{"id": "X-C-S7", "surfaced_by": "3.0.0_SA_CVO"}], "0.0.0_AB_MSTR", False, merging=True,
             parent_ids=set()))),
        ("(b) FAIL-CLOSED: merging with parent_ids=None exempts NOTHING",
         lambda: _coordinate_violations(
             "org/missions/D0/NFRA/X/surprise-channel/adjudications/ADJUDICATION_v1.md", "ADJUDICATION",
             [{"id": "X-C-S7", "surfaced_by": "3.0.0_SA_CVO"}], "0.0.0_AB_MSTR", False, merging=True,
             parent_ids=None) != []),
        ("C- NARROWNESS: the SAME CVO-surfaced row off a merge under a foreign committer -> still REFUSED",
         lambda: any("is not 3.0.0_SA_CVO" in x and "committer" in x for x in _coordinate_violations(
             "org/missions/D0/NFRA/X/surprise-channel/adjudications/ADJUDICATION_v1.md", "ADJUDICATION",
             [{"id": "X-C-S7", "surfaced_by": "3.0.0_SA_CVO"}], "0.0.0_AB_MSTR", False, merging=False))),
        # ESTATE_GOVERNANCE-S5: the FLAT adjudication document. Three arms as 3.0.0_SA_CVO specified.
        ("S5 flat: a C- row in a FLAT ADJUDICATION_v document is ADMITTED (was refused, x4)",
         lambda: _coordinate_violations("org/surprise_channel/ESTATE_GOVERNANCE/ADJUDICATION_v1.md", None,
                                        [{"id": "ESTATE_GOVERNANCE-C-S1", "surfaced_by": "3.0.0_SA_CVO"}],
                                        "3.0.0_SA_CVO", False) == []),
        ("S5 flat NARROWNESS: a C- row in a FLAT INVESTIGATION_v is STILL REFUSED",
         lambda: any("C- is the CVO's coordinate" in x or "C-" in x for x in _coordinate_violations(
             "org/surprise_channel/ESTATE_GOVERNANCE/INVESTIGATION_v1.md", None,
             [{"id": "ESTATE_GOVERNANCE-C-S1", "surfaced_by": "3.0.0_SA_CVO"}], "3.0.0_SA_CVO", False))),
        ("S5: the TREE arm is unchanged -- a C- row under adjudications/ still admitted",
         lambda: _coordinate_violations("org/missions/D0/NFRA/X_PRJ/surprise-channel/adjudications/ADJUDICATION_v1.md",
                                        "ADJUDICATION", [{"id": "X_PRJ-C-S1", "surfaced_by": "3.0.0_SA_CVO"}],
                                        "3.0.0_SA_CVO", False) == []),
        # RE-CUT TWICE, NEVER DELETED. First it asserted the BLANKET merge exemption this seat
        # shipped; 94337 replaced that with the per-fabric `Z-` proxy; Andrew's ~19:3xZ scoping
        # replaced the proxy with provenance. Each re-cut kept the arm pointing at the law that
        # actually holds, so the history of the rule is legible in the battery that guards it.
        ("L10 MERGE: undispositioned items, a CARRIED row, merging=True -> NO violations",
         lambda: _investigations_precondition_violations(
             "r", {"id": "X_PRJ-Z-S9", "route": "SPEC_ERROR"}, "X_PRJ", "route=SPEC_ERROR",
             ({"X_PRJ-S1": "UNDER_INVESTIGATION"}, [], 1, ""), merging=True,
             parent_ids={"X_PRJ-Z-S9"}) == []),
        ("L10 NARROWNESS: the SAME undispositioned items with merging=False are still REFUSED",
         lambda: _investigations_precondition_violations(
             "r", row, "X_PRJ", "route=SPEC_ERROR",
             ({"X_PRJ-S1": "UNDER_INVESTIGATION"}, [], 1, ""), merging=False) != []),
        ("L10 MERGE: a CARRIED row is exempt even when the DISPOSITION census itself failed -- the "
         "row was routed elsewhere, so this branch owes no census for it",
         lambda: _investigations_precondition_violations(
             "r", {"id": "X_PRJ-Z-S9"}, "X_PRJ", "route=SPEC_ERROR",
             (None, [], 0, "git rc=128"), merging=True, parent_ids={"X_PRJ-Z-S9"}) == []),
        ("L10 MERGE: and a MINTED row on a merge is still REFUSED when the census failed -- two "
         "independent fail-closed paths, neither masking the other",
         lambda: _investigations_precondition_violations(
             "r", {"id": "X_PRJ-S9"}, "X_PRJ", "route=SPEC_ERROR",
             (None, [], 0, "git rc=128"), merging=True, parent_ids=set()) != []),
        # ROUTE LIMB -- ITS FIRST BATTERY. 94295: this limb had ZERO arms and its only caller was the
        # production path, so nothing would have caught a regression in it and nothing did catch the
        # merge defect either. Red, green, fail-closed, then the merge pair.
        ("route RED: an OPEN task order -> refused, names the count and cites the ruling",
         lambda: any("1 of 3" in x and "LD-0521" in x for x in _route_precondition_violations(
             None, "r", row, "X_PRJ", open_tos=({"TO-1"}, 3, ""), route_word="route=SPEC_ERROR"))),
        ("route GREEN: zero open task orders -> admitted",
         lambda: _route_precondition_violations(
             None, "r", row, "X_PRJ", open_tos=(set(), 3, ""), route_word="route=SPEC_ERROR") == []),
        ("route: the open-order census could not run -> refused fail-closed",
         lambda: any("fail-closed" in x for x in _route_precondition_violations(
             None, "r", row, "X_PRJ", open_tos=(None, 0, "git rc=128"), route_word="route=SPEC_ERROR"))),
        ("route MERGE: an OPEN task order, a CARRIED row, merging=True -> NO violations "
         "(94293 -> 94337 -> Andrew ~19:3xZ)",
         lambda: _route_precondition_violations(
             None, "r", {"id": "X_PRJ-Z-S9"}, "X_PRJ", open_tos=({"TO-1"}, 3, ""), route_word="w",
             merging=True, parent_ids={"X_PRJ-Z-S9"}) == []),
        ("route NARROWNESS: the SAME open order with merging=False is still REFUSED",
         lambda: _route_precondition_violations(
             None, "r", row, "X_PRJ", open_tos=({"TO-1"}, 3, ""), route_word="w", merging=False) != []),
        ("every item dispositioned -> admitted",
         lambda: _investigations_precondition_violations("r", row, "X_PRJ", "route=SPEC_ERROR",
                                                          ({"X_PRJ-S1": "DISMISSED_WITH_REASON", "X_PRJ-S2": "GRADUATED"}, [], 1, "")) == []),
        ("adjudication by a later row flips the item (pure resolver)",
         lambda: _resolve_latest([("f", [{"id": "X_PRJ-S1", "disposition": "UNDER_INVESTIGATION"},
                                          {"id": "X_PRJ-S2", "disposition": "DECOMP_INVALIDATING", "adjudicates": ["X_PRJ-S1"]}])], [])
         == ({"X_PRJ-S1": "DECOMP_INVALIDATING", "X_PRJ-S2": "DECOMP_INVALIDATING"}, [])),
        ("a remediation row bearing the id resolves it GRADUATED; a phantom target is reported",
         lambda: _resolve_latest([("f", [{"id": "X_PRJ-S1", "disposition": "UNDER_INVESTIGATION"},
                                          {"id": "X_PRJ-S2", "disposition": "GRADUATED", "adjudicates": ["X_PRJ-S7"]}])], ["X_PRJ-S1"])
         == ({"X_PRJ-S1": "GRADUATED", "X_PRJ-S2": "GRADUATED"}, ["X_PRJ-S7 (by X_PRJ-S2)"])),
        ("census could not run -> refused fail-closed",
         lambda: any("fail-closed" in x for x in _investigations_precondition_violations(
             "r", row, "X_PRJ", "route=SPEC_ERROR", (None, [], 0, "git ls-files rc=128")))),
        ("phantom adjudication -> its own refusal",
         lambda: any("phantom" in x for x in _investigations_precondition_violations(
             "r", row, "X_PRJ", "route=SPEC_ERROR", ({"X_PRJ-S1": "GRADUATED"}, ["X_PRJ-S7 (by X_PRJ-S2)"], 1, "")))),
    ]
    # REMEDIATED-IN-ROUND: the four cells of the route-less admission, graded through _check_row with the committed schema.
    try:
        rschema = _schema(root, "REMEDIATION")
    except Exception as exc:  # noqa: BLE001
        rschema = None
        arms.append(("remediation schema readable for the route-less arms", lambda exc=exc: (_ for _ in ()).throw(exc)))
    base_rem = {"id": "X_PRJ-S3", "project": "X_PRJ", "fabric": "laptop", "class": "OBSERVATION", "hazard_standing": "INERT",
                "mechanism": "a stale token in one doc", "evidence": ["docs/x.md:12 @abcdef1234 -- the token"],
                "remedy": "the token re-pointed in place", "owner": "1.0.0_SA_CTO", "round": "v1",
                "remediation": {"state": "OPEN", "owner": "1.0.0_SA_CTO", "round": "v1"}}
    def rem(**over):
        r = json.loads(json.dumps(base_rem))
        r.update(over)
        return r
    noroute = lambda r: any("carries no `route`" in x for x in _check_row(r, "REMEDIATION", rschema))  # noqa: E731
    CLOSURE_OK = {"reason": "IRREMEDIABLE", "pointer": "org/x.md:3 -- gone"}
    if rschema is not None:
        arms += [
            ("OPEN remediation, no route -> ADMITTED (spine v3 carrier 6: the route is retired; the slug goes to the CTO)",
             lambda: not noroute(rem()) and _check_row(rem(), "REMEDIATION", rschema) == []),
            ("REMEDIATED, INERT, no route -> admitted",
             lambda: not noroute(rem(remediation={"state": "REMEDIATED", "owner": "1.0.0_SA_CTO", "round": "v1"}))),
            ("REMEDIATED but still ARMED (disarm ARMED), no route -> admitted by this limb (the clocks are the schema's allOf)",
             lambda: not noroute(rem(hazard_standing="ARMED", remediation={"state": "REMEDIATED", "owner": "1.0.0_SA_CTO", "round": "v1"},
                                     disarm={"state": "ARMED", "owner": "1.0.0_SA_CTO", "at": None}))),
            ("legacy pair route SPEC_ERROR + loop_target 5 -> REFUSED (a pair that is present keeps the locked map)",
             lambda: any("MAPPING IS" in x for x in _check_row(rem(route="SPEC_ERROR", loop_target=5), "REMEDIATION", rschema))),
            ("carrier 5: an adjudication document's row dispositions an investigation item across documents; the CVO's row is NOT an item",
             lambda: _resolve_latest([(INV, [{"id": "X_PRJ-S1", "disposition": "UNDER_INVESTIGATION"}]),
                                      (ADJ, [{"id": "X_PRJ-S2", "disposition": "GRADUATED", "adjudicates": ["X_PRJ-S1"]}])], [])
             == ({"X_PRJ-S1": "GRADUATED"}, [])),
            ("carrier 5: adjudications/ path resolves to (project, ADJUDICATION)",
             lambda: _folder_identity("org/missions/D0/NFRA/NFRA_CLDGRPH/surprise-channel/adjudications/ADJUDICATION_v1.md") == ("NFRA_CLDGRPH", "ADJUDICATION")),
            ("REMEDIATED and DISARMED, no route -> admitted",
             lambda: not noroute(rem(hazard_standing="ARMED", remediation={"state": "REMEDIATED", "owner": "1.0.0_SA_CTO", "round": "v1"},
                                     disarm={"state": "DISARMED", "owner": "1.0.0_SA_CTO", "at": "2026-09-03T11:00Z"}))),
            ("OPEN with route SPEC_ERROR + loop_target 6 -> no route complaint (unchanged)",
             lambda: not noroute(rem(route="SPEC_ERROR", loop_target=6))),
            # CLOSED_UNREMEDIATED (proposal @759c693537, CVO concurrence @cfcae02e52): the schema conditionals.
            ("CLOSED_UNREMEDIATED + closure (IRREMEDIABLE, pointer), INERT, closed -> admitted",
             lambda: _check_row(rem(closed=True, remediation={"state": "CLOSED_UNREMEDIATED", "owner": "1.0.0_SA_CTO", "round": "v1",
                                                               "closure": CLOSURE_OK}),
                                "REMEDIATION", rschema) == []),
            ("CLOSED_UNREMEDIATED without closure -> REFUSED",
             lambda: _check_row(rem(closed=True, remediation={"state": "CLOSED_UNREMEDIATED", "owner": "1.0.0_SA_CTO", "round": "v1"}),
                                "REMEDIATION", rschema) != []),
            ("closure on an OPEN row -> REFUSED",
             lambda: _check_row(rem(remediation={"state": "OPEN", "owner": "1.0.0_SA_CTO", "round": "v1", "closure": CLOSURE_OK}),
                                "REMEDIATION", rschema) != []),
            ("closure reason outside the four -> REFUSED",
             lambda: _check_row(rem(closed=True, remediation={"state": "CLOSED_UNREMEDIATED", "owner": "1.0.0_SA_CTO", "round": "v1",
                                                               "closure": {"reason": "WONTFIX", "pointer": "org/x.md:3"}}),
                                "REMEDIATION", rschema) != []),
            ("closure without a pointer -> REFUSED",
             lambda: _check_row(rem(closed=True, remediation={"state": "CLOSED_UNREMEDIATED", "owner": "1.0.0_SA_CTO", "round": "v1",
                                                               "closure": {"reason": "IRREMEDIABLE"}}),
                                "REMEDIATION", rschema) != []),
            ("C3: ARMED + closed + CLOSED_UNREMEDIATED + disarm still ARMED -> REFUSED",
             lambda: _check_row(rem(hazard_standing="ARMED", closed=True,
                                    disarm={"state": "ARMED", "owner": "1.0.0_SA_CTO", "at": None},
                                    remediation={"state": "CLOSED_UNREMEDIATED", "owner": "1.0.0_SA_CTO", "round": "v1",
                                                 "closure": CLOSURE_OK}),
                                "REMEDIATION", rschema) != []),
            ("C3: ARMED + closed + CLOSED_UNREMEDIATED + DISARMED -> admitted",
             lambda: _check_row(rem(hazard_standing="ARMED", closed=True,
                                    disarm={"state": "DISARMED", "owner": "1.0.0_SA_CTO", "at": "2026-10-04T00:00Z"},
                                    remediation={"state": "CLOSED_UNREMEDIATED", "owner": "1.0.0_SA_CTO", "round": "v1",
                                                 "closure": CLOSURE_OK}),
                                "REMEDIATION", rschema) == []),
            ("control: INERT + closed + OPEN -> REFUSED (unchanged)",
             lambda: _check_row(rem(closed=True), "REMEDIATION", rschema) != []),
        ]
    # CLOSED_UNREMEDIATED pointer checks (proposal section 2 item 5), pure: known ids and a path oracle are injected.
    _pex = lambda p: p in {"org/tier1_exec/1.0.0_SA_CTO/deliverables/R.md", "org/missions/D9/NFRA/X/task-orders/T.md"}  # noqa: E731
    _cpv = lambda reason, pointer, known=frozenset({"X_PRJ-S9"}): _closure_pointer_violations(  # noqa: E731
        "X_PRJ-S3", {"reason": reason, "pointer": pointer}, set(known), _pex)
    arms += [
        ("pointer: CARRIED_BY a row id present in the project -> admitted", lambda: _cpv("CARRIED_BY", "X_PRJ-S9 carries it") == []),
        ("pointer: CARRIED_BY a row id absent from the project -> REFUSED", lambda: _cpv("CARRIED_BY", "X_PRJ-S10") != []),
        ("pointer: CARRIED_BY its own id -> REFUSED", lambda: _cpv("CARRIED_BY", "X_PRJ-S3", known={"X_PRJ-S3"}) != []),
        ("pointer: CARRIED_BY an order path that exists -> admitted",
         lambda: _cpv("CARRIED_BY", "org/missions/D9/NFRA/X/task-orders/T.md") == []),
        ("pointer: ACCEPTED_BY_RULING a record path that exists (with @vintage) -> admitted",
         lambda: _cpv("ACCEPTED_BY_RULING", "org/tier1_exec/1.0.0_SA_CTO/deliverables/R.md@abc1234567") == []),
        ("pointer: ACCEPTED_BY_RULING a path that does not exist -> REFUSED",
         lambda: _cpv("ACCEPTED_BY_RULING", "org/nowhere.md") != []),
        ("pointer: IRREMEDIABLE free-form evidence -> admitted", lambda: _cpv("IRREMEDIABLE", "the paths are gone; see S42") == []),
        ("pointer: project ids unreadable (None) on CARRIED_BY -> REFUSED (fail-closed)",
         lambda: _closure_pointer_violations("X_PRJ-S3", {"reason": "CARRIED_BY", "pointer": "X_PRJ-S9"}, None, _pex) != []),
    ]
    # `disarms` TARGETS (2026-10-05), pure: the project's investigation-plane ids are injected.
    _plane = {"X_PRJ-S11", "X_PRJ-C-S412"}
    arms += [
        ("disarms: every id a row of the plane carries (an item and a CVO row) -> admitted",
         lambda: _disarms_violations("X_PRJ-S500", ["X_PRJ-S11", "X_PRJ-C-S412"], _plane) == []),
        ("disarms: one id no row carries -> REFUSED, names the phantom id",
         lambda: any("X_PRJ-S999" in x for x in _disarms_violations("X_PRJ-S500", ["X_PRJ-S11", "X_PRJ-S999"], _plane))),
        ("disarms: the plane census could not run (None) -> REFUSED (fail-closed)",
         lambda: _disarms_violations("X_PRJ-S500", ["X_PRJ-S11"], None) != []),
        ("disarms: absent or empty -> nothing to check",
         lambda: _disarms_violations("X_PRJ-S500", None, None) == [] and _disarms_violations("X_PRJ-S500", [], None) == []),
        ("disarms READ: check_file grades NEW remediation rows only, against the INVESTIGATION plane",
         lambda: (lambda src: "_disarms_violations(" in src and 'r.get("id") not in old_ids and r.get("disarms")' in src
                  and '_plane_docs(root, _proj, "INVESTIGATION", "")' in src)(inspect.getsource(check_file))),
    ]
    # FOREIGN-ROW SWEEP arms (pure), the class site Z measured; includes the mutant (a clean commit under the WRONG seat).
    fr = lambda rows, who, cw=frozenset(): _foreign_row_violations("f", "INVESTIGATION", rows, who, coworkers=cw)[0]  # noqa: E731
    fn_ = lambda rows, who, cw=frozenset(): _foreign_row_violations("f", "INVESTIGATION", rows, who, coworkers=cw)[1]  # noqa: E731
    mine = {"id": "X_PRJ-S1", "surfaced_by": "0.8.0_AE_CloudComp~B"}
    theirs = {"id": "X_PRJ-S2", "surfaced_by": "3.0.0_SA_CVO"}
    cowork = {"id": "X_PRJ-S4", "surfaced_by": "0.8.0_AE_CloudComp~J"}
    arms += [
        ("sweep: own row under own seat (lane vs base) -> admitted", lambda: fr([mine], "0.8.0_AE_CloudComp") == []),
        ("sweep: a peer's row under my seat -> refused, names the id and its surfacer",
         lambda: any("FOREIGN-ROW SWEEP" in x and "X_PRJ-S2" in x and "3.0.0_SA_CVO" in x for x in fr([theirs], "0.8.0_AE_CloudComp"))),
        ("sweep: one own + one foreign -> refused naming ONLY the foreign one",
         lambda: any("1 of 2" in x and "X_PRJ-S2" in x and "X_PRJ-S1" not in x for x in fr([mine, theirs], "0.8.0_AE_CloudComp"))),
        ("sweep MUTANT: a clean commit graded under the WRONG seat -> refused (discriminates on authorship, not count)",
         lambda: fr([mine], "2.0.0_SA_COO") != []),
        ("sweep: unparseable surfaced_by -> refused (fail-safe)", lambda: any("unparseable" in x for x in fr([{"id": "X_PRJ-S3", "surfaced_by": "someone"}], "0.8.0_AE_CloudComp"))),
        ("sweep: committer unreadable -> refused fail-closed", lambda: any("UNREADABLE" in x for x in fr([mine], "Andrew Berman"))),
        # MERGE EXEMPTION (94283). The NARROWNESS arm is the one that earns it: the same rows,
        # merging=False, must still refuse -- an exemption that cannot be shown to STOP applying
        # is a hole. Mirrors the arm that earned to-pipeline-gate's exemption an hour earlier.
        ("sweep MERGE: foreign rows on a merge -> NO violations (0.0.0_AB_MSTR 94283)",
         lambda: _foreign_row_violations("f", "INVESTIGATION", [theirs, mine], "0.0.0_AB_MSTR",
                                         coworkers=set(), merging=True,
                                         parent_ids={"X_PRJ-S1", "X_PRJ-S2"})[0] == []),
        ("sweep MERGE: the exemption ANNOUNCES itself and names the surfacing seats (not a silent pass)",
         lambda: any("MERGE COMMIT -- foreign-row sweep exempt" in n and "3.0.0_SA_CVO" in n
                     for n in _foreign_row_violations("f", "INVESTIGATION", [theirs, mine],
                                                      "0.0.0_AB_MSTR", coworkers=set(), merging=True,
                                                      parent_ids={"X_PRJ-S1", "X_PRJ-S2"})[1])),
        ("(b) sweep MINTED: a foreign row in NEITHER parent -> swept as the committer's, REFUSED",
         lambda: _foreign_row_violations("f", "INVESTIGATION", [theirs], "0.0.0_AB_MSTR",
                                         coworkers=set(), merging=True, parent_ids=set())[0] != []),
        ("(b) sweep MIXED: a carried row is exempt and a minted one in the SAME file still refuses",
         lambda: (lambda vn: vn[0] != [] and any("MINTED in this merge commit" in n for n in vn[1])
                  and any("a PARENT carried" in n for n in vn[1]))(
             _foreign_row_violations("f", "INVESTIGATION", [mine, theirs], "0.0.0_AB_MSTR",
                                     coworkers=set(), merging=True, parent_ids={"X_PRJ-S1"}))),
        ("(b) sweep FAIL-CLOSED: merging with parent_ids=None refuses rather than exempting",
         lambda: any("fail-closed" in x for x in _foreign_row_violations(
             "f", "INVESTIGATION", [theirs], "0.0.0_AB_MSTR", coworkers=set(), merging=True,
             parent_ids=None)[0])),
        ("sweep NARROWNESS: the SAME rows with merging=False are still REFUSED",
         lambda: _foreign_row_violations("f", "INVESTIGATION", [theirs, mine], "0.0.0_AB_MSTR",
                                         coworkers=set(), merging=False)[0] != []),
        ("sweep: remediation rows out of scope", lambda: _foreign_row_violations("f", "REMEDIATION", [theirs], "0.8.0_AE_CloudComp", coworkers=set())[0] == []),
        # co-worker admission (the shared-worktree class of 93746)
        ("co-worker: a row whose surfacer holds an open order on the project -> admitted, NAMED in notes",
         lambda: fr([cowork], "0.7.0_AE_CloudOps", {"0.8.0_AE_CloudComp", "0.7.0_AE_CloudOps"}) == []
         and any("CO-WORKER ROWS" in n and "X_PRJ-S4" in n for n in fn_([cowork], "0.7.0_AE_CloudOps", {"0.8.0_AE_CloudComp", "0.7.0_AE_CloudOps"}))),
        ("co-worker: the same row when its surfacer holds NO open order -> refused (a stranger's row)",
         lambda: fr([cowork], "0.7.0_AE_CloudOps", {"0.7.0_AE_CloudOps"}) != []),
        ("co-worker: census could not run (None) -> refused, says so",
         lambda: any("could not run" in x for x in fr([cowork], "0.7.0_AE_CloudOps", None))),
        ("co-worker MUTANT: a Tier-1 seat's row never holds an order -> refused even beside co-workers",
         lambda: fr([theirs], "0.7.0_AE_CloudOps", {"0.8.0_AE_CloudComp", "0.7.0_AE_CloudOps"}) != []),
    ]
    # monotone state advance on an existing remediation row (93695 item 4)
    base_row = {"id": "X-S1", "remedy": "fix the thing", "evidence": ["a@b"], "hazard_standing": "ARMED", "closed": False,
                "owner": "x",
                "disarm": {"state": "ARMED", "owner": "x", "at": None}, "remediation": {"state": "OPEN", "owner": "x", "round": "v1"}}
    def adv(**over):
        r = json.loads(json.dumps(base_row))
        for k, val in over.items():
            if isinstance(val, dict) and isinstance(r.get(k), dict):
                r[k].update(val)
            else:
                r[k] = val
        return r
    arms += [
        ("advance: disarm ARMED->DISARMED with `at` set -> admitted", lambda: _monotone_advance(base_row, adv(disarm={"state": "DISARMED", "at": "2026-09-03T14:00Z"}))),
        ("advance: remediation OPEN->REMEDIATED -> admitted", lambda: _monotone_advance(base_row, adv(remediation={"state": "REMEDIATED"}))),
        ("advance: all three clocks at once -> admitted", lambda: _monotone_advance(base_row, adv(disarm={"state": "DISARMED", "at": "2026-09-03T14:00Z"}, remediation={"state": "REMEDIATED"}, closed=True))),
        ("advance MUTANT: DISARMED without `at` -> refused (a clock needs its timestamp)", lambda: not _monotone_advance(base_row, adv(disarm={"state": "DISARMED"}))),
        ("advance MUTANT: a reversal DISARMED->ARMED -> refused",
         lambda: not _monotone_advance(adv(disarm={"state": "DISARMED", "at": "2026-09-03T14:00Z"}), base_row)),
        ("advance MUTANT: the clock moves AND the remedy is reworded -> refused",
         lambda: not _monotone_advance(base_row, adv(remediation={"state": "REMEDIATED"}, remedy="fix the other thing"))),
        ("advance: no change at all -> not an advance (False)", lambda: not _monotone_advance(base_row, adv())),
        # CLOSED_UNREMEDIATED clock (CVO C1): OPEN -> CLOSED_UNREMEDIATED in place, adding `closure` only.
        ("advance CU: OPEN->CLOSED_UNREMEDIATED adding a well-formed closure -> admitted",
         lambda: _monotone_advance(base_row, adv(remediation={"state": "CLOSED_UNREMEDIATED", "closure": {"reason": "IRREMEDIABLE", "pointer": "org/x.md:3"}}))),
        ("advance CU: with closed false->true and disarm ARMED->DISARMED in the same write -> admitted",
         lambda: _monotone_advance(base_row, adv(disarm={"state": "DISARMED", "at": "2026-10-04T00:00Z"}, closed=True,
                                                 remediation={"state": "CLOSED_UNREMEDIATED", "closure": {"reason": "IRREMEDIABLE", "pointer": "org/x.md:3"}}))),
        ("advance CU MUTANT: state moves but no closure -> refused",
         lambda: not _monotone_advance(base_row, adv(remediation={"state": "CLOSED_UNREMEDIATED"}))),
        ("advance CU MUTANT: closure added but state stays OPEN -> refused",
         lambda: not _monotone_advance(base_row, adv(remediation={"closure": {"reason": "IRREMEDIABLE", "pointer": "org/x.md:3"}}))),
        ("advance CU MUTANT: REMEDIATED->CLOSED_UNREMEDIATED -> refused",
         lambda: not _monotone_advance(adv(remediation={"state": "REMEDIATED"}),
                                       adv(remediation={"state": "CLOSED_UNREMEDIATED", "closure": {"reason": "IRREMEDIABLE", "pointer": "org/x.md:3"}}))),
        ("advance CU MUTANT: the remedy reworded in the same write -> refused",
         lambda: not _monotone_advance(base_row, adv(remedy="something else",
                                                     remediation={"state": "CLOSED_UNREMEDIATED", "closure": {"reason": "IRREMEDIABLE", "pointer": "org/x.md:3"}}))),
        ("advance CU MUTANT: another field added beside closure -> refused",
         lambda: not _monotone_advance(base_row, adv(remediation={"state": "CLOSED_UNREMEDIATED", "note": "x", "closure": {"reason": "IRREMEDIABLE", "pointer": "org/x.md:3"}}))),
        ("advance CU MUTANT: a closure reason outside the four -> refused",
         lambda: not _monotone_advance(base_row, adv(remediation={"state": "CLOSED_UNREMEDIATED",
                                                                  "closure": {"reason": "WONTFIX", "pointer": "org/x.md:3"}}))),
        ("advance C3 MUTANT: an ARMED row closed (CLOSED_UNREMEDIATED) while disarm stays ARMED -> refused",
         lambda: not _monotone_advance(base_row, adv(closed=True, remediation={"state": "CLOSED_UNREMEDIATED", "closure": {"reason": "IRREMEDIABLE", "pointer": "org/x.md:3"}}))),
        ("advance C3 MUTANT: an ARMED row closed (REMEDIATED) while disarm stays ARMED -> refused (the schema allOf, on the clock path)",
         lambda: not _monotone_advance(base_row, adv(closed=True, remediation={"state": "REMEDIATED"}))),
        # THE FOURTH ADMITTED MOVE (R-19 addendum): owner change with a same-write CTO-ruling citation, nothing else.
        ("advance OWNER: disarm.owner changes AND exactly one CTO-ruling citation is appended -> admitted",
         lambda: _monotone_advance(base_row, adv(disarm={"owner": "2.0.0_SA_COO~G"},
                                                 evidence=["a@b", "SELF_DRIVE_LGIC_RULINGS_20260916.md@4a55888962 R-19 ruling 1"]))),
        ("advance OWNER MUTANT: owner changes with NO citation -> refused (the field stays immutable)",
         lambda: not _monotone_advance(base_row, adv(disarm={"owner": "2.0.0_SA_COO~G"}))),
        ("advance OWNER MUTANT: owner changes with an evidence entry that cites no ruling -> refused",
         lambda: not _monotone_advance(base_row, adv(disarm={"owner": "2.0.0_SA_COO~G"}, evidence=["a@b", "see the message"]))),
        ("advance OWNER MUTANT: owner changes AND the clock moves in the same write -> refused",
         lambda: not _monotone_advance(base_row, adv(disarm={"owner": "2.0.0_SA_COO~G", "state": "DISARMED", "at": "2026-09-16T15:00Z"},
                                                     evidence=["a@b", "SELF_DRIVE_LGIC_RULINGS_20260916.md@4a55888962 R-19"]))),
        ("advance OWNER MUTANT: owner changes and the existing evidence is REWRITTEN under the citation -> refused",
         lambda: not _monotone_advance(base_row, adv(disarm={"owner": "2.0.0_SA_COO~G"},
                                                     evidence=["z@z", "SELF_DRIVE_LGIC_RULINGS_20260916.md@4a55888962 R-19"]))),
        # R-42 EXTENSION: `remediation.owner` on the same terms, and EXACTLY ONE owner field per move.
        ("advance OWNER R-42: remediation.owner changes AND exactly one CTO-ruling citation is appended -> admitted",
         lambda: _monotone_advance(base_row, adv(remediation={"owner": "2.0.0_SA_COO~B"},
                                                 evidence=["a@b", "SELF_DRIVE_LGIC_RULINGS_20260917.md@57bc083d45 R-42"]))),
        ("advance OWNER R-42 MUTANT: remediation.owner changes with NO citation -> refused",
         lambda: not _monotone_advance(base_row, adv(remediation={"owner": "2.0.0_SA_COO~B"}))),
        ("advance OWNER R-42: BOTH nested owners move under ONE citation -> ADMITTED (a subset of the addressee set "
         "relocates in one write; the diff shows which fields moved, the citation says why)",
         lambda: _monotone_advance(base_row, adv(disarm={"owner": "2.0.0_SA_COO~B"}, remediation={"owner": "2.0.0_SA_COO~B"},
                                                 evidence=["a@b", "SELF_DRIVE_LGIC_RULINGS_20260917.md@57bc083d45 R-42"]))),
        ("advance OWNER R-42: the TOP-LEVEL owner ('the lane that builds the remediation', an ADDRESSEE per the schema) "
         "moves under one citation -> ADMITTED",
         lambda: _monotone_advance(base_row, adv(owner="2.0.0_SA_COO~B",
                                                 evidence=["a@b", "SELF_DRIVE_LGIC_RULINGS_20260917.md@57bc083d45 R-42"]))),
        ("advance OWNER R-42: ALL THREE addressee owners relocate in one write -> ADMITTED",
         lambda: _monotone_advance(base_row, adv(owner="2.0.0_SA_COO~B", disarm={"owner": "2.0.0_SA_COO~B"},
                                                 remediation={"owner": "2.0.0_SA_COO~B"},
                                                 evidence=["a@b", "SELF_DRIVE_LGIC_RULINGS_20260917.md@57bc083d45 R-42"]))),
        ("advance OWNER R-42 MUTANT: all three move with NO citation -> refused",
         lambda: not _monotone_advance(base_row, adv(owner="2.0.0_SA_COO~B", disarm={"owner": "2.0.0_SA_COO~B"},
                                                     remediation={"owner": "2.0.0_SA_COO~B"}))),
        ("advance OWNER R-42 MUTANT: remediation.owner moves AND a clock moves in the same write -> refused",
         lambda: not _monotone_advance(base_row, adv(remediation={"owner": "2.0.0_SA_COO~B", "state": "REMEDIATED"},
                                                     evidence=["a@b", "SELF_DRIVE_LGIC_RULINGS_20260917.md@57bc083d45 R-42"]))),
        ("advance OWNER R-42 CONTROL: the DISARM half still admits exactly as before (no regression)",
         lambda: _monotone_advance(base_row, adv(disarm={"owner": "2.0.0_SA_COO~G"},
                                                 evidence=["a@b", "SELF_DRIVE_LGIC_RULINGS_20260917.md@57bc083d45 R-42"]))),
    ]
    # OWNER-AND-CARRIER LIMBS on NEW rows (R-18(2), R-19(2), A-1) -- graded through _check_row with the committed schemas;
    # each limb has a positive (refuses) and a negative (a legitimate owner or carrier passes this limb) arm.
    try:
        ischema = _schema(root, "INVESTIGATION")
    except Exception as exc:  # noqa: BLE001
        ischema = None
        arms.append(("investigation schema readable for the owner/carrier arms", lambda exc=exc: (_ for _ in ()).throw(exc)))
    _toks = ("(R-18)", "(R-19)", "C-S24")
    def _has(rows_out, tok):
        return any(tok in x for x in rows_out)
    def _none(rows_out):
        return not any(t in x for x in rows_out for t in _toks)
    if ischema is not None:
        inv = lambda **kw: dict({"id": "X_PRJ-W2-S3", "project": "X_PRJ", "fabric": "laptop"}, **kw)  # noqa: E731
        arms += [
            ("R-18(2) inv: disarm_owner names a WORKER serial -> refused, names the issuer",
             lambda: _has(_check_row(inv(hazard_standing="ARMED", disarm_owner="0.9.0_WK_X_PRJ~2"), "INVESTIGATION", ischema), "(R-18)")),
            ("R-19(2) inv: disarm_owner names the CVO -> refused (the owner is never the writer)",
             lambda: _has(_check_row(inv(hazard_standing="ARMED", disarm_owner="3.0.0_SA_CVO"), "INVESTIGATION", ischema), "(R-19)")),
            ("owner CONTROL inv: disarm_owner names a COO lane -> no owner complaint",
             lambda: _none(_check_row(inv(hazard_standing="ARMED", disarm_owner="2.0.0_SA_COO~G"), "INVESTIGATION", ischema))),
            ("A-1: `adjudicates` on a WORKER's row -> refused, names the CVO's field",
             lambda: _has(_check_row(inv(surfaced_by="0.9.0_WK_X_PRJ~3", adjudicates=["X_PRJ-W2-S2"]), "INVESTIGATION", ischema), "C-S24")),
            ("A-1: disposition GRADUATED on a WORKER's row -> refused",
             lambda: _has(_check_row(inv(surfaced_by="0.9.0_WK_X_PRJ~3", disposition="GRADUATED"), "INVESTIGATION", ischema), "C-S24")),
            ("A-1 CONTROL: the same fields on the CVO's own row -> no carrier complaint",
             lambda: _none(_check_row(inv(surfaced_by="3.0.0_SA_CVO", disposition="GRADUATED", adjudicates=["X_PRJ-W2-S2"]), "INVESTIGATION", ischema))),
            ("A-1 CONTROL: a WORKER's row filed UNDER_INVESTIGATION with no adjudicates -> no carrier complaint",
             lambda: _none(_check_row(inv(surfaced_by="0.9.0_WK_X_PRJ~3", disposition="UNDER_INVESTIGATION"), "INVESTIGATION", ischema))),
            # R-28: the owner-and-carrier limbs grade the AUTHORING act, so a row CARRIED by a merge is not re-graded.
            ("R-28 CARRIED inv: CVO disarm_owner + a WORKER's GRADUATED/adjudicates on a carried row -> no owner/carrier complaint",
             lambda: _none(_check_row(inv(surfaced_by="0.9.0_WK_X_PRJ~3", hazard_standing="ARMED", disarm_owner="3.0.0_SA_CVO",
                                          disposition="GRADUATED", adjudicates=["X_PRJ-W2-S2"]), "INVESTIGATION", ischema, carried=True))),
            ("R-28 NARROWNESS inv: the SAME row not carried (minted) -> still refused on the R-19 and A-1 limbs it trips",
             lambda: all(_has(_check_row(inv(surfaced_by="0.9.0_WK_X_PRJ~3", hazard_standing="ARMED", disarm_owner="3.0.0_SA_CVO",
                                             disposition="GRADUATED", adjudicates=["X_PRJ-W2-S2"]), "INVESTIGATION", ischema), t)
                         for t in ("(R-19)", "C-S24"))),
            ("R-28 NARROWNESS schema: a carried row is still graded on the schema (an enum outside the ratified set refuses)",
             lambda: any("not in the ratified enum" in x for x in _check_row(inv(disposition="NOT_A_DISPOSITION"), "INVESTIGATION", ischema, carried=True))),
            ("R-28 WIRING: check_file passes carried only as a merge AND a parent-carried id (fail-closed on None parents)",
             lambda: "carried=_mrg_now and _row_was_carried(row, _pids)" in inspect.getsource(check_file)
             and _row_was_carried({"id": "X_PRJ-S3"}, None) is False),
        ]
    if rschema is not None:
        arms += [
            ("R-18(2) rem: disarm.owner names a WORKER serial -> refused",
             lambda: _has(_check_row(rem(hazard_standing="ARMED", disarm={"state": "ARMED", "owner": "0.9.0_WK_X_PRJ~2", "at": None}), "REMEDIATION", rschema), "(R-18)")),
            ("R-19(2) rem: disarm.owner names the CVO -> refused",
             lambda: _has(_check_row(rem(hazard_standing="ARMED", disarm={"state": "ARMED", "owner": "3.0.0_SA_CVO", "at": None}), "REMEDIATION", rschema), "(R-19)")),
            ("owner CONTROL rem: disarm.owner names the CTO -> no owner complaint",
             lambda: _none(_check_row(rem(hazard_standing="ARMED", disarm={"state": "ARMED", "owner": "1.0.0_SA_CTO", "at": None}), "REMEDIATION", rschema))),
            ("R-28 CARRIED rem: disarm.owner names a WORKER on a carried row -> no owner complaint",
             lambda: _none(_check_row(rem(hazard_standing="ARMED", disarm={"state": "DISARMED", "owner": "0.9.0_WK_X_PRJ~2", "at": "2026-09-16T14:05Z"}), "REMEDIATION", rschema, carried=True))),
        ]
    # THE ITEM CENSUS and THE ALLOCATOR RACE (94007 / 94010, v3's first drain): items vs the CVO's rows; one id, two documents.
    ADJ = "org/missions/D11/NFRA/X_PRJ/surprise-channel/adjudications/ADJUDICATION_v1.md"
    INV = "org/missions/D11/NFRA/X_PRJ/surprise-channel/investigations/INVESTIGATION_v1.md"
    INV2 = "org/missions/D11/NFRA/X_PRJ/surprise-channel/investigations/INVESTIGATION_v2.md"
    two_docs = lambda a, b: _resolve_latest([(INV, [{"id": "X_PRJ-S4", "disposition": a}]),  # noqa: E731
                                             (INV2, [{"id": "X_PRJ-S4", "disposition": b}])], [])[0]
    coll = _resolve_latest([(INV, [{"id": "X_PRJ-S4", "disposition": "UNDER_INVESTIGATION"}]),
                            (INV2, [{"id": "X_PRJ-S4", "disposition": "UNDER_INVESTIGATION"}]),
                            (ADJ, [{"id": "X_PRJ-S9", "disposition": "DISMISSED_WITH_REASON", "adjudicates": ["X_PRJ-S4"]}])], [])
    arms += [
        ("census: an UNDER_INVESTIGATION row of the CVO's own (adjudications/, no adjudicates) is not an item and does not block the slug",
         lambda: _investigations_precondition_violations("r", row, "X_PRJ", "the slug", (
             _resolve_latest([(INV, [{"id": "X_PRJ-S1", "disposition": "GRADUATED"}]),
                              (ADJ, [{"id": "X_PRJ-S2", "disposition": "UNDER_INVESTIGATION"}])], [])[0], [], 2, "")) == []),
        ("census MUTANT: the same UNDER_INVESTIGATION row filed as an investigation row DOES block (the document decides, not the seat)",
         lambda: _investigations_precondition_violations("r", row, "X_PRJ", "the slug", (
             _resolve_latest([(INV, [{"id": "X_PRJ-S1", "disposition": "GRADUATED"}, {"id": "X_PRJ-S2", "disposition": "UNDER_INVESTIGATION"}])], [])[0], [], 1, "")) != []),
        ("fold order: an issuer's OPEN row adjudicating a CVO-dispositioned item does not re-open it (28889)",
         lambda: _resolve_latest([(ADJ, [{"id": "X_PRJ-S9", "disposition": "DISMISSED_WITH_REASON", "adjudicates": ["X_PRJ-S1"]}]),
                                  (INV, [{"id": "X_PRJ-S1", "disposition": "UNDER_INVESTIGATION"},
                                         {"id": "X_PRJ-S2", "disposition": "UNDER_INVESTIGATION", "adjudicates": ["X_PRJ-S1"]}])], [])
         == ({"X_PRJ-S1": "DISMISSED_WITH_REASON", "X_PRJ-S2": "UNDER_INVESTIGATION"}, [])),
        ("fold order control: a DISPOSITIONED issuer row still applies after the CVO's (later file wins, as before)",
         lambda: _resolve_latest([(ADJ, [{"id": "X_PRJ-S9", "disposition": "DISMISSED_WITH_REASON", "adjudicates": ["X_PRJ-S1"]}]),
                                  (INV, [{"id": "X_PRJ-S1", "disposition": "UNDER_INVESTIGATION"},
                                         {"id": "X_PRJ-S2", "disposition": "GRADUATED", "adjudicates": ["X_PRJ-S1"]}])], [])[0]["X_PRJ-S1"]
         == "GRADUATED"),
        ("census: `adjudicates` naming an adjudication-document row's own id -> a real row, not a phantom, nothing to flip",
         lambda: _resolve_latest([(INV, [{"id": "X_PRJ-S1", "disposition": "GRADUATED"}]),
                                  (ADJ, [{"id": "X_PRJ-S2", "disposition": "DISMISSED_WITH_REASON"},
                                         {"id": "X_PRJ-S3", "disposition": "DISMISSED_WITH_REASON", "adjudicates": ["X_PRJ-S2"]}])], [])
         == ({"X_PRJ-S1": "GRADUATED"}, [])),
        ("collision: one id in TWO investigation documents, one occurrence open -> OPEN whichever document is read first",
         lambda: two_docs("DISMISSED_WITH_REASON", "UNDER_INVESTIGATION") == {"X_PRJ-S4": "UNDER_INVESTIGATION"}
         and two_docs("UNDER_INVESTIGATION", "DISMISSED_WITH_REASON") == {"X_PRJ-S4": "UNDER_INVESTIGATION"}),
        ("collision: `adjudicates` naming an id two investigation documents carry -> AMBIGUOUS, not applied, refused by the limb",
         lambda: coll[0] == {"X_PRJ-S4": "UNDER_INVESTIGATION"} and any("AMBIGUOUS" in u for u in coll[1])
         and any("no single item" in x for x in _investigations_precondition_violations("r", row, "X_PRJ", "the slug", (coll[0], coll[1], 3, "")))),
        ("collision: _duplicate_ids reports the plane collision (the CVO's row and a worker's row on one id) and nothing else",
         lambda: _duplicate_ids([(INV, [{"id": "X_PRJ-S1"}, {"id": "X_PRJ-S34"}]), (ADJ, [{"id": "X_PRJ-S34"}, {"id": "X_PRJ-S35"}])])
         == {"X_PRJ-S34": [INV, ADJ]}),
        ("uniqueness limb: a NEW row whose id sits in another document of the plane -> refused, names the document",
         lambda: any(("already exists in " + ADJ) in x and "X_PRJ-S34" in x for x in _duplicate_id_violations(
             INV, "INVESTIGATION", [{"id": "X_PRJ-S34"}], "X_PRJ", [(ADJ, {"X_PRJ-S34"})])[0])),
        ("uniqueness limb: a NEW row with the next unused id -> admitted",
         lambda: _duplicate_id_violations(INV, "INVESTIGATION", [{"id": "X_PRJ-S35"}], "X_PRJ", [(ADJ, {"X_PRJ-S34"})])[0] == []),
        ("uniqueness limb: the plane census could not run -> refused fail-closed, names the reason",
         lambda: any("fail-closed" in x and "rc=128" in x for x in _duplicate_id_violations(
             INV, "INVESTIGATION", [{"id": "X_PRJ-S35"}], "X_PRJ", None, "git ls-files rc=128")[0])),
        # THE DECLARED BASELINE (3.0.0_SA_CVO 94346) and its NARROWNESS, which is the whole point: the
        # baseline is a fact about TWO named files, never an amnesty for an id.
        ("baseline: the declared S34 pair -> ADMITTED, and the note names the resolving record C-S2",
         lambda: (lambda vn: vn[0] == [] and any("C-S2 @f4b41b1c20" in n for n in vn[1]))(
             _duplicate_id_violations(_S34_INV, "INVESTIGATION", [{"id": "NFRA_COMPEFFICACY-S34"}],
                                      "NFRA_COMPEFFICACY", [(_S34_ADJ, {"NFRA_COMPEFFICACY-S34"})]))),
        ("baseline NARROWNESS: the SAME id in a THIRD document -> still REFUSED",
         lambda: _duplicate_id_violations(_S34_INV, "INVESTIGATION", [{"id": "NFRA_COMPEFFICACY-S34"}],
                                          "NFRA_COMPEFFICACY",
                                          [(_S34_ADJ, {"NFRA_COMPEFFICACY-S34"}),
                                           ("org/surprise_channel/X/INVESTIGATION_v1.md",
                                            {"NFRA_COMPEFFICACY-S34"})])[0] != []),
        ("baseline NARROWNESS: a DIFFERENT id in the same two documents -> still REFUSED",
         lambda: _duplicate_id_violations(_S34_INV, "INVESTIGATION", [{"id": "NFRA_COMPEFFICACY-S40"}],
                                          "NFRA_COMPEFFICACY",
                                          [(_S34_ADJ, {"NFRA_COMPEFFICACY-S40"})])[0] != []),
        ("uniqueness limb: the planes are separate -- remediation rows read remediation documents only; investigation rows read investigations + adjudications",
         lambda: _plane_patterns("REMEDIATION") == REMEDIATION_PATTERNS
         and _plane_patterns("INVESTIGATION") == INVESTIGATION_PATTERNS + ADJUDICATION_PATTERNS),
    ]
    # EN-g-37 / S74: THE SLUG-TIME LIMB -- a GRADUATED item under a project with NO remediation row
    # bearing its id refuses the slug. `_graduated_without_row` is the PURE core; `_graduated_
    # without_row_violations` is the wrapper `check_file` calls, with the same merge-carried
    # exemption as the twin L10 precondition limbs. Red and green, plus the two fail-closed arms and
    # the negative control that this limb never reaches for k-38's staleness question.
    arms += [
        ("EN-g-37 rowlessness POSITIVE: a GRADUATED item WITH a remediation row -> not flagged (the automatic path)",
         lambda: _graduated_without_row({"X_PRJ-S1": "GRADUATED"}, {"X_PRJ-S1"}) == []),
        ("EN-g-37 rowlessness MUTANT: a GRADUATED item (the CVO's own L9 field) with NO remediation row -> flagged",
         lambda: _graduated_without_row({"X_PRJ-S1": "GRADUATED"}, set()) == ["X_PRJ-S1"]),
        ("EN-g-37 rowlessness: a non-GRADUATED item with no remediation row -> NOT flagged (rowlessness grades GRADUATED only, not staleness)",
         lambda: _graduated_without_row({"X_PRJ-S1": "UNDER_INVESTIGATION"}, set()) == []),
        ("EN-g-37 rowlessness: fails closed (None, never an empty list) when the dispositions census could not run",
         lambda: _graduated_without_row(None, {"X_PRJ-S1"}) is None),
        ("EN-g-37 rowlessness: fails closed (None, never an empty list) when the remediation census could not run",
         lambda: _graduated_without_row({"X_PRJ-S1": "GRADUATED"}, None) is None),
        ("EN-g-37 violations POSITIVE: a compliant slug (the GRADUATED item has its remediation row) -> admitted",
         lambda: _graduated_without_row_violations("r", row, "X_PRJ", "the slug",
                                                    ({"X_PRJ-S1": "GRADUATED"}, [], 1, ""), ({"X_PRJ-S1"}, "")) == []),
        ("EN-g-37 violations MUTANT: a rowless GRADUATED item -> the slug is REFUSED, naming the id",
         lambda: any("X_PRJ-S1" in x and "NO remediation row" in x for x in _graduated_without_row_violations(
             "r", row, "X_PRJ", "the slug", ({"X_PRJ-S1": "GRADUATED"}, [], 1, ""), (set(), "")))),
        ("EN-g-37 violations: the dispositions census failing REFUSES fail-closed, names the reason",
         lambda: any("fail-closed" in x for x in _graduated_without_row_violations(
             "r", row, "X_PRJ", "the slug", (None, [], 0, "git rc=128"), (set(), "")))),
        ("EN-g-37 violations: the remediation census failing REFUSES fail-closed, names the reason",
         lambda: any("fail-closed" in x for x in _graduated_without_row_violations(
             "r", row, "X_PRJ", "the slug", ({"X_PRJ-S1": "GRADUATED"}, [], 1, ""), (None, "git rc=128")))),
        ("EN-g-37 violations AT A MERGE: a CARRIED row is not evaluated (history arriving, not a routing act)",
         lambda: _graduated_without_row_violations("r", {"id": "X_PRJ-S9"}, "X_PRJ", "the slug",
                                                    ({"X_PRJ-S1": "GRADUATED"}, [], 1, ""), (set(), ""),
                                                    merging=True, parent_ids={"X_PRJ-S9"}) == []),
        ("EN-g-37 violations AT A MERGE: a row MINTED in the merge (not in the parents) still binds",
         lambda: any("X_PRJ-S1" in x for x in _graduated_without_row_violations(
             "r", {"id": "X_PRJ-S9"}, "X_PRJ", "the slug", ({"X_PRJ-S1": "GRADUATED"}, [], 1, ""), (set(), ""),
             merging=True, parent_ids={"X_PRJ-OTHER"}))),
        ("EN-g-37 NEGATIVE CONTROL: k-38's staleness question (an OPEN row that EXISTS) is invisible to this limb by construction",
         lambda: _graduated_without_row({"X_PRJ-S1": "UNDER_INVESTIGATION"}, {"X_PRJ-S1"}) == []
         and "_stale_open_row" not in inspect.getsource(_graduated_without_row)
         and "_stale_open_row" not in inspect.getsource(_graduated_without_row_violations)),
    ]
    # EN-k-38 / S75: THE STALENESS LIMB -- an EXISTING remediation row under a project that is OPEN,
    # carries a named owner, and has not moved for STALE_OPEN_ROW_N_ROUNDS or more rounds is DISCLOSED on
    # the slug (it REFUSED until 2026-09-18; see the wrapper's docstring for why that deadlocked). `_stale_open_row` is the PURE core; `_stale_open_row_violations` is the wrapper `check_file`
    # calls, with the same merge-carried exemption as EN-g-37's twin. Red and green, the fail-closed
    # arms, the non-open/non-owned negative arms, and the DISCRIMINATION arm (`k38-distinct`) proving
    # this limb catches a row EN-g-37's rowlessness limb ADMITS -- the round bought two questions, not
    # one asked twice.
    _stale_rr = lambda **kw: dict({"remediation": {"state": "OPEN", "owner": "1.0.0_SA_CTO", "round": "v1"}}, **kw)  # noqa: E731
    arms += [
        ("EN-k-38 staleness POSITIVE: an OPEN, owned row within the N-round window -> not flagged",
         lambda: _stale_open_row({"X_PRJ-W1-S1": _stale_rr()}, 2, STALE_OPEN_ROW_N_ROUNDS) == []),
        ("EN-k-38 staleness MUTANT: the SAME row, N or more rounds behind the slug's round -> flagged",
         lambda: _stale_open_row({"X_PRJ-W1-S1": _stale_rr()}, 1 + STALE_OPEN_ROW_N_ROUNDS, STALE_OPEN_ROW_N_ROUNDS)
         == ["X_PRJ-W1-S1"]),
        ("EN-k-38 staleness: a REMEDIATED row, however old, is NOT flagged (staleness grades OPEN only)",
         lambda: _stale_open_row({"X_PRJ-W1-S1": _stale_rr(remediation={"state": "REMEDIATED", "owner": "1.0.0_SA_CTO", "round": "v1"})},
                                 8, STALE_OPEN_ROW_N_ROUNDS) == []),
        ("EN-k-38 staleness: an OPEN row with NO owner is NOT flagged (owned is a required half, not a courtesy)",
         lambda: _stale_open_row({"X_PRJ-W1-S1": _stale_rr(remediation={"state": "OPEN", "owner": "  ", "round": "v1"})},
                                 8, STALE_OPEN_ROW_N_ROUNDS) == []),
        ("EN-k-38 staleness: fails closed (None, never an empty list) when the remediation census could not run",
         lambda: _stale_open_row(None, 8, STALE_OPEN_ROW_N_ROUNDS) is None),
        ("EN-k-38 staleness: fails closed (None) when the slug's own round did not parse",
         lambda: _stale_open_row({"X_PRJ-W1-S1": _stale_rr()}, None, STALE_OPEN_ROW_N_ROUNDS) is None),
        ("EN-k-38 staleness: fails closed (None) when no threshold is supplied",
         lambda: _stale_open_row({"X_PRJ-W1-S1": _stale_rr()}, 8, None) is None),
        ("EN-k-38 POSITIVE: a fresh OPEN row, legitimately in flight -> no violation and nothing disclosed",
         lambda: _stale_open_row_violations("r", {"id": "X_PRJ-W1-S2", "round": "v2"}, "X_PRJ", "the slug",
                                            ({"X_PRJ-W1-S1": _stale_rr()}, "")) == ([], [])),
        ("EN-k-38 MUTANT: a stale OPEN, owned row STILL SURFACES -- disclosed, naming the id and S75",
         lambda: any("X_PRJ-W1-S1" in n and "S75" in n for n in _stale_open_row_violations(
             "r", {"id": "X_PRJ-W1-S2", "round": "v%d" % (1 + STALE_OPEN_ROW_N_ROUNDS)}, "X_PRJ", "the slug",
             ({"X_PRJ-W1-S1": _stale_rr()}, ""))[1])),
        ("EN-k-38 THE DEADLOCK ARM: a stale row does NOT refuse the slug -- the violation half is EMPTY. "
         "Round 8's L10 deadlocked because this branch refused the very rows its sibling limb demanded, "
         "against 91 stale rows no single slug could move (1.0.0_SA_CTO, 2026-09-18)",
         lambda: _stale_open_row_violations(
             "r", {"id": "X_PRJ-W1-S2", "round": "v%d" % (1 + STALE_OPEN_ROW_N_ROUNDS)}, "X_PRJ", "the slug",
             ({"X_PRJ-W1-S1": _stale_rr()}, ""))[0] == []),
        ("EN-k-38 the two EVALUABILITY branches still REFUSE, because the committing act CAN fix both: "
         "an unreadable census fails closed",
         lambda: any("fail-closed" in x for x in _stale_open_row_violations(
             "r", {"id": "X_PRJ-W1-S2", "round": "v8"}, "X_PRJ", "the slug", (None, "git rc=128"))[0])),
        ("EN-k-38 evaluability: the NEW row's own round does not parse -> REFUSED, not silently skipped",
         lambda: any("no parseable" in x for x in _stale_open_row_violations(
             "r", {"id": "X_PRJ-W1-S2", "round": "not-a-round"}, "X_PRJ", "the slug",
             ({"X_PRJ-W1-S1": _stale_rr()}, ""))[0])),
        ("EN-k-38 AT A MERGE: a CARRIED row is not evaluated (history arriving, not a routing act)",
         lambda: _stale_open_row_violations("r", {"id": "X_PRJ-S9", "round": "v8"}, "X_PRJ", "the slug",
                                            ({"X_PRJ-W1-S1": _stale_rr()}, ""),
                                            merging=True, parent_ids={"X_PRJ-S9"}) == ([], [])),
        ("EN-k-38 AT A MERGE: a row MINTED in the merge (not in the parents) still discloses",
         lambda: any("X_PRJ-W1-S1" in n for n in _stale_open_row_violations(
             "r", {"id": "X_PRJ-S9", "round": "v8"}, "X_PRJ", "the slug", ({"X_PRJ-W1-S1": _stale_rr()}, ""),
             merging=True, parent_ids={"X_PRJ-OTHER"})[1])),
        ("EN-k-38 NEGATIVE CONTROL: g-37's rowlessness question (a GRADUATED item with no remediation row) "
         "is invisible to this limb by construction",
         lambda: _stale_open_row({}, 8, STALE_OPEN_ROW_N_ROUNDS) == []
         and "_graduated_without_row" not in inspect.getsource(_stale_open_row)
         and "_graduated_without_row" not in inspect.getsource(_stale_open_row_violations)),
        ("EN-k-38 DISCRIMINATION (k38-distinct): a GRADUATED item WITH its remediation row -- the row EXISTS -- "
         "is SILENT to g-37's rowlessness limb, and the SAME row is SURFACED by k-38's staleness limb for "
         "being OPEN, owned and unmoved: the round bought two questions, not one asked twice. The arm's "
         "second half now reads k-38's NOTES rather than its violations -- the DISCRIMINATION is unchanged "
         "and only the INSTRUMENT k-38 answers with moved, from refusal to disclosure (1.0.0_SA_CTO, "
         "2026-09-18: a gate refuses an act only when that act can remedy its condition)",
         lambda: _graduated_without_row_violations("r", row, "X_PRJ", "the slug",
                                                    ({"X_PRJ-W1-S1": "GRADUATED"}, [], 1, ""), ({"X_PRJ-W1-S1"}, "")) == []
         and any("X_PRJ-W1-S1" in n and "S75" in n for n in _stale_open_row_violations(
             "r", {"id": "X_PRJ-W1-S2", "round": "v%d" % (1 + STALE_OPEN_ROW_N_ROUNDS)}, "X_PRJ", "the slug",
             ({"X_PRJ-W1-S1": _stale_rr()}, ""))[1])),
    ]
    # THE ALLOCATOR COORDINATE (RULING 2 @9ef9a40aae): the grammar and the discipline, red and green.
    WK = "0.9.0_WK_X_PRJ~2"
    cv = lambda rows, who, fk="INVESTIGATION", cs=False: _coordinate_violations("f", fk, rows, who, cs)  # noqa: E731
    arms += [
        ("grammar: X_PRJ-W2-S1 parses (project, w=2); X_PRJ-Z-W3-S2 (z, w=3); X_PRJ-C-S1 (c); X_PRJ-S5 plain",
         lambda: ID_RE.match("X_PRJ-W2-S1").group("project", "w") == ("X_PRJ", "2")
         and ID_RE.match("X_PRJ-Z-W3-S2").group("z", "w") == ("Z-", "3")
         and ID_RE.match("X_PRJ-C-S1").group("c") == "C-" and ID_RE.match("X_PRJ-S5").group("w", "c") == (None, None)),
        ("grammar MUTANTS: W before Z, W without n, C and W together, no dash -> refused",
         lambda: all(ID_RE.match(x) is None for x in ("X_PRJ-W2-Z-S1", "X_PRJ-W-S1", "X_PRJ-C-W2-S1", "X_PRJ-W2S1"))),
        ("discipline: worker ~2 mints X_PRJ-W2-S1 -> admitted", lambda: cv([{"id": "X_PRJ-W2-S1"}], WK) == []),
        ("discipline: worker ~2 mints X_PRJ-W3-S1 -> refused (another worker's coordinate)",
         lambda: any("slot is 2" in x for x in cv([{"id": "X_PRJ-W3-S1"}], WK))),
        ("discipline: worker ~2 mints a bare X_PRJ-S40 -> refused (the race)",
         lambda: any("carries no W<n>" in x for x in cv([{"id": "X_PRJ-S40"}], WK))),
        ("discipline: a seat mints X_PRJ-W2-S1 -> refused; a seat's bare X_PRJ-S40 -> admitted",
         lambda: any("is not a worker" in x for x in cv([{"id": "X_PRJ-W2-S1"}], "2.0.0_SA_COO"))
         and cv([{"id": "X_PRJ-S40"}], "2.0.0_SA_COO") == []),
        ("discipline: the CVO mints X_PRJ-C-S1 in adjudications/ -> admitted; in investigations/ -> refused; the COO in adjudications/ -> refused",
         lambda: cv([{"id": "X_PRJ-C-S1"}], "3.0.0_SA_CVO~A", "ADJUDICATION") == []
         and any("outside adjudications/" in x for x in cv([{"id": "X_PRJ-C-S1"}], "3.0.0_SA_CVO", "INVESTIGATION"))
         and any("not 3.0.0_SA_CVO" in x for x in cv([{"id": "X_PRJ-C-S1"}], "2.0.0_SA_COO", "ADJUDICATION"))),
        ("discipline: a NEW seat-form row in adjudications/ -> admitted while the schema lacks C-, refused once it admits it",
         lambda: cv([{"id": "X_PRJ-S40"}], "3.0.0_SA_CVO", "ADJUDICATION", False) == []
         and any("carries no C-" in x for x in cv([{"id": "X_PRJ-S40"}], "3.0.0_SA_CVO", "ADJUDICATION", True))),
        ("discipline: the underscore author form 0.9.0_WK_X_PRJ_2 resolves to slot 2",
         lambda: cv([{"id": "X_PRJ-W2-S1"}], "0.9.0_WK_X_PRJ_2") == [] and cv([{"id": "X_PRJ-W3-S1"}], "0.9.0_WK_X_PRJ_2") != []),
        # AT A DRAIN (94157): the allocator is the row's surfaced_by, never the merge committer
        ("drain: worker ~2's W2 row surfaced_by ~2, merged by the COO~A -> admitted",
         lambda: _coordinate_violations("f", "INVESTIGATION", [{"id": "X_PRJ-W2-S1", "surfaced_by": "0.9.0_WK_X_PRJ~2"}], "2.0.0_SA_COO~A", False, merging=True, parent_ids=_DRAIN_PIDS) == []),
        ("drain: a W3 row surfaced_by ~2 -> refused (another worker's coordinate, read on the row)",
         lambda: any("slot is 2" in x for x in _coordinate_violations("f", "INVESTIGATION", [{"id": "X_PRJ-W3-S1", "surfaced_by": "0.9.0_WK_X_PRJ~2"}], "2.0.0_SA_COO~A", False, merging=True, parent_ids=_DRAIN_PIDS))),
        ("drain: a bare S<k> row surfaced_by a worker -> refused (the race)",
         lambda: any("carries no W<n>" in x for x in _coordinate_violations("f", "INVESTIGATION", [{"id": "X_PRJ-S40", "surfaced_by": "0.9.0_WK_X_PRJ~2"}], "2.0.0_SA_COO~A", False, merging=True, parent_ids=_DRAIN_PIDS))),
        ("drain: a seat's W row riding the merge -> refused (a seat's row carries no W)",
         lambda: any("is not a worker" in x for x in _coordinate_violations("f", "INVESTIGATION", [{"id": "X_PRJ-W2-S1", "surfaced_by": "3.0.0_SA_CVO"}], "2.0.0_SA_COO~A", False, merging=True, parent_ids=_DRAIN_PIDS))),
        ("drain MUTANT: the same lawful W2 row graded NOT merging under the COO~A committer -> refused (the first drain's defect, kept as the negative control)",
         lambda: _coordinate_violations("f", "INVESTIGATION", [{"id": "X_PRJ-W2-S1", "surfaced_by": "0.9.0_WK_X_PRJ~2"}], "2.0.0_SA_COO~A", False, merging=False) != []),
        # BATCH 112: a carried row the published trunk already holds is noted, not graded; a drain's row is still graded.
        ("published: a bare S<k> worker row a parent carries AND origin/CLOUD carries, merged by MSTR -> admitted",
         lambda: _coordinate_violations("f", "INVESTIGATION", [{"id": "X_PRJ-S40", "surfaced_by": "0.9.0_WK_X_PRJ~2"}], "0.0.0_AB_MSTR", False, merging=True, parent_ids={"X_PRJ-S40"}, published_ids={"X_PRJ-S40"}) == []),
        ("published NEGATIVE: the same row carried by a parent but NOT on the published trunk (a worker drain) -> refused",
         lambda: any("carries no W<n>" in x for x in _coordinate_violations("f", "INVESTIGATION", [{"id": "X_PRJ-S40", "surfaced_by": "0.9.0_WK_X_PRJ~2"}], "2.0.0_SA_COO~A", False, merging=True, parent_ids={"X_PRJ-S40"}, published_ids=set()))),
        ("published FAIL-CLOSED: the trunk unreadable (published_ids None) exempts nothing",
         lambda: any("carries no W<n>" in x for x in _coordinate_violations("f", "INVESTIGATION", [{"id": "X_PRJ-S40", "surfaced_by": "0.9.0_WK_X_PRJ~2"}], "0.0.0_AB_MSTR", False, merging=True, parent_ids={"X_PRJ-S40"}, published_ids=None))),
        ("published NOT CARRIED: a row on the trunk but in NEITHER parent (minted in the merge) -> graded as the committer's",
         lambda: any("is not a worker" in x for x in _coordinate_violations("f", "INVESTIGATION", [{"id": "X_PRJ-W2-S1", "surfaced_by": "0.9.0_WK_X_PRJ~2"}], "2.0.0_SA_COO", False, merging=True, parent_ids=set(), published_ids={"X_PRJ-W2-S1"}))),
        # THE REMEDIATION PLANE (2026-09-10): W is INHERITED there, so the arm must not grade it.
        # The three REFUSALS below are the point -- a fix that only proves the new case is half a test.
        ("remediation: the CVO files a W row in remediations/ (the id EQUALS the graduated worker id) -> ADMITTED",
         lambda: _coordinate_violations("org/missions/D0/NFRA/X/surprise-channel/remediations/REMEDIATION_v2.Z.md",
                                        "REMEDIATION", [{"id": "X_PRJ-W2-S1"}], "3.0.0_SA_CVO~Z", False) == []),
        ("remediation AT A DRAIN: a carried W row with NO surfaced_by, merged by the integrator -> ADMITTED (the 18-row refusal)",
         lambda: _coordinate_violations("org/missions/D0/NFRA/X/surprise-channel/remediations/REMEDIATION_v2.Z.md",
                                        "REMEDIATION", [{"id": "X_PRJ-W2-S1", "surfaced_by": ""}], "0.0.0_AB_MSTR~Z",
                                        False, merging=True, parent_ids=_DRAIN_PIDS) == []),
        ("remediation LEGACY FLAT: folder_kind None + REMEDIATION in the basename -> ADMITTED (the 6 flat rows)",
         lambda: _coordinate_violations("org/surprise_channel/X_PRJ/REMEDIATION_v1.Z.md", None,
                                        [{"id": "X_PRJ-W2-S1"}], "3.0.0_SA_CVO~Z", False) == []),
        ("NEGATIVE CONTROL: the SAME W row in the INVESTIGATION plane, seat committer -> STILL REFUSED (the narrowing did not leak)",
         lambda: any("is not a worker" in x for x in
                     _coordinate_violations("f", "INVESTIGATION", [{"id": "X_PRJ-W2-S1"}], "3.0.0_SA_CVO~Z", False))),
        ("NEGATIVE CONTROL: flat INVESTIGATION_v1.md, folder_kind None, seat's W row -> STILL REFUSED (basename match is REMEDIATION-only)",
         lambda: any("is not a worker" in x for x in
                     _coordinate_violations("org/surprise_channel/X_PRJ/INVESTIGATION_v1.Z.md", None,
                                            [{"id": "X_PRJ-W2-S1"}], "3.0.0_SA_CVO~Z", False))),
        ("NEGATIVE CONTROL: wrong-slot discipline survives in the INVESTIGATION plane at a drain -> STILL REFUSED",
         lambda: any("slot is 2" in x for x in
                     _coordinate_violations("f", "INVESTIGATION", [{"id": "X_PRJ-W3-S1", "surfaced_by": "0.9.0_WK_X_PRJ~2"}],
                                            "2.0.0_SA_COO~A", False, merging=True, parent_ids=_DRAIN_PIDS))),
        # A REMEDIATION ROW INHERITS ITS COORDINATE (1.0.0_SA_CTO 2026-09-10, on 3.0.0_SA_CVO's
        # NFRA_CLDGRPH round-8 refusals). The two arms the gate refused, and their negative controls
        # in the SAME shape -- the discriminator is the DOCUMENT KIND and nothing else about the row.
        ("remediation: the CVO's row inheriting a WORKER's X_PRJ-W1-S43 -> ADMITTED (inherited, not allocated)",
         lambda: cv([{"id": "X_PRJ-W1-S43"}], "3.0.0_SA_CVO", "REMEDIATION") == []),
        ("remediation: a C- row living in remediations/ -> ADMITTED (C- names the ORIGINAL allocator)",
         lambda: cv([{"id": "X_PRJ-C-S69"}], "3.0.0_SA_CVO", "REMEDIATION") == []),
        ("remediation MUTANT, the negative control: the SAME two rows in an INVESTIGATION document still REFUSE",
         lambda: any("is not a worker" in x for x in cv([{"id": "X_PRJ-W1-S43"}], "3.0.0_SA_CVO", "INVESTIGATION"))
         and any("outside adjudications/" in x for x in cv([{"id": "X_PRJ-C-S69"}], "3.0.0_SA_CVO", "INVESTIGATION"))),
        ("remediation: the FLAT document form (folder_kind None, kind read from the FILENAME) -> ADMITTED, and a flat INVESTIGATION name still refuses",
         lambda: _coordinate_violations("org/surprise_channel/X_PRJ/REMEDIATION_v4.md", None, [{"id": "X_PRJ-W1-S43"}], "3.0.0_SA_CVO", False) == []
         and _coordinate_violations("org/surprise_channel/X_PRJ/INVESTIGATION_v1.md", None, [{"id": "X_PRJ-W1-S43"}], "3.0.0_SA_CVO", False) != []),
        ("identity half: X_PRJ-W2-S1 with project X_PRJ agrees; X_PRJ-Z-W2-S1 reads site-z",
         lambda: not any("project=" in x for x in _check_row({"id": "X_PRJ-W2-S1", "project": "X_PRJ", "fabric": "laptop"}, "INVESTIGATION", {"properties": {"id": {}, "project": {}, "fabric": {}}, "required": []}))
         and any("site-z" in x for x in _check_row({"id": "X_PRJ-Z-W2-S1", "project": "X_PRJ", "fabric": "laptop"}, "INVESTIGATION", {"properties": {"id": {}, "project": {}, "fabric": {}}, "required": []}))),
        # THE LAST TAG GOVERNS (1.0.0_SA_CTO ruling msg 107528): a stale earlier duplicate is not the status.
        ("last-tag: 'pending' then 'complete' reads complete; 'complete' then 'pending' reads pending; none reads None",
         lambda: _to_status_match("<status>pending</status>\n<status>complete</status>\n").group(1) == "complete"
         and _to_status_match("<status>complete</status>\n<status>pending</status>\n").group(1) == "pending"
         and _to_status_match("no tag here, only `<status>` in prose\n") is None),
        # PROOF TERMINALITY (1.0.0_SA_CTO 2026-09-15; spine :436, :487-488). RED-FIRST: every arm below FAILS on the
        # pre-change module, which has neither _proof_terminal nor _proof_verdict. The LIVE arms read real bytes.
        ("proof terminality LIVE: LGIC_NAMING LN-e-3-r2 (VALID proof, its FAIL the round's measurement) reads terminal by proof",
         lambda: _proof_terminal(root, _LN_E3, _head_text(root, _LN_E3))[0] is True),
        ("proof terminality DOCTORED PAIR, real bytes: LN-e-3-r2's instance bound to LN-e-5-r2's order -> NOT terminal "
         "(the checker's binding limb refuses), while LN-e-5-r2's own instance bound to it -> terminal",
         lambda: _proof_verdict(root, _LN_E3_INST, _LN_E5)[0] is False
         and _proof_verdict(root, _LN_E5_INST, _LN_E5)[0] is True),
        ("proof terminality: a checker verdict of rc=1 (INVALID) keeps the order OPEN",
         lambda: _proof_terminal(root, _LN_E3, _head_text(root, _LN_E3), _run=lambda a: _FakeRun(1))[0] is False),
        ("proof terminality: a checker that could not answer (rc=2) or that RAISES keeps the order OPEN",
         lambda: _proof_terminal(root, _LN_E3, _head_text(root, _LN_E3), _run=lambda a: _FakeRun(2))[0] is False
         and _proof_terminal(root, _LN_E3, _head_text(root, _LN_E3), _run=_raise)[0] is False),
        ("proof terminality: no tracked instance -> OPEN, and the checker is never run",
         lambda: _proof_terminal(root, "org/missions/D0/XXXX/X_NONE/task-orders/X_NONE.TO-z-1.none.md", "",
                                 _run=_raise) == (False, "no proof-of-spec instance tracked")),
        ("proof terminality GRAIN GUARD: an order whose text at the read ref differs from the worktree -> OPEN, before the checker runs",
         lambda: (lambda r: r[0] is False and "differs from" in r[1])(
             _proof_terminal(root, _LN_E3, "<status>pending</status>\n", _run=_raise))),
        ("proof terminality READ: the census consults the proof only past a non-terminal word, and keeps the "
         "`<basename> [<word>]` label the POSN_ASTTAX exception matches on",
         lambda: "_proof_terminal(root, p, text, merging=merging)" in inspect.getsource(_open_tos_census)
         and 'label = "%s [%s]" % (os.path.basename(p), word)' in inspect.getsource(_open_tos_census)
         and "if word not in TERMINAL_TO_WORDS:" in inspect.getsource(_open_tos_census)),
        ("proof terminality READ: the invocation is the flip limb's (python <checker> <instance> --governing-order <order>)",
         lambda: '"--governing-order", rel]' in inspect.getsource(_proof_verdict)),
    ]
    # THE ACCEPTANCE SWEEP (AMGT-rk-57, row AMGT_RESAPP-Z-S169, ruling s.3.3 @9c8e04cd9a `:81-85`): pure
    # classifier fixtures first, then two LIVE arms on THIS project's own real bytes.
    # THE REAL-BYTES CHECK (rk-30 page-half classifies AC1 PASS/AC2 FAIL, the round-13 sweep beside
    # `_open_tos_census`'s note) is `.tools/tests/test_acceptance_sweep.py`'s job, NOT this arm list's --
    # these classify arms stay PURE and read no repo, matching the self-test's own discipline (every
    # other arm here that reads real git bytes is a PROOF TERMINALITY arm, a pre-existing exception this
    # cell does not extend).
    arms += [
        ("acceptance classify: PASS and FAIL map 1:1 from the row's own status",
         lambda: (lambda res, p, f, u: p == 1 and f == 1 and u == 0
                  and res[0]["status"] == "PASS" and res[1]["status"] == "FAIL")(
             *_classify_acceptance({"AC1": {"criterion_id": "AC1", "status": "PASS"},
                                    "AC2": {"criterion_id": "AC2", "status": "FAIL", "status_reason": "x"}},
                                   [{"id": "AC1", "judgment": False}, {"id": "AC2", "judgment": False}]))),
        ("acceptance classify: every OTHER legal status (UNCOMPUTABLE-BY-CONSTRUCTION, "
         "UNVERIFIABLE-BY-INSTRUMENT, N/A-BY-CONSTRUCTION, UNCOMPUTABLE) plus an unrecognised value "
         "all map to UNVERIFIABLE",
         lambda: all(_classify_acceptance({"AC1": {"criterion_id": "AC1", "status": s}},
                                          [{"id": "AC1", "judgment": False}])[3] == 1
                    for s in ("UNCOMPUTABLE-BY-CONSTRUCTION", "UNVERIFIABLE-BY-INSTRUMENT",
                             "N/A-BY-CONSTRUCTION", "UNCOMPUTABLE", "SOMETHING-ELSE"))),
        ("acceptance classify: a judgment criterion is UNVERIFIABLE even beside a PASS row (graded at "
         "L9, never self-graded)",
         lambda: _classify_acceptance({"AC1": {"criterion_id": "AC1", "status": "PASS"}},
                                      [{"id": "AC1", "judgment": True}])[1:] == (0, 0, 1)),
        ("acceptance classify: a criterion with no row at all is UNVERIFIABLE, reason-carrying",
         lambda: (lambda res, p, f, u: u == 1 and "no acceptance row" in res[0]["reason"])(
             *_classify_acceptance({}, [{"id": "AC9", "judgment": False}]))),
        ("acceptance sweep: contributes NO violation -- check_file's own source only ever passes the "
         "sweep's output to `notes`, never to `v`",
         lambda: (lambda src: "_acceptance_sweep(" in src and "ACCEPTANCE (round" in src
                  and not any(("v.append" in ln or "v.extend" in ln) and "_acc" in ln
                             for ln in src.splitlines()))(inspect.getsource(check_file))),
    ]
    arms += [
        ("census POINTER: a seat-home POINTER is skipped (both markers), a real open order is not",
         lambda: _is_pointer_text("# POINTER (not an order) -- x\n") and _is_pointer_text("\n# POINTER (not an order) -- x")
         and _is_pointer_text("# t\n# pipeline-override: this file is a POINTER in the lane\n")
         and not _is_pointer_text("# TO X\n<status>pending</status>\n")
         and "_is_pointer_text(text)" in inspect.getsource(_open_tos_census)),
    ]
    failed = 0
    for name, fn in arms:
        ok = False
        try:
            ok = bool(fn())
        except Exception as exc:  # noqa: BLE001
            name += " (raised %s: %s)" % (type(exc).__name__, exc)
        print("  %s  %s" % ("PASS" if ok else "FAIL", name))
        failed += 0 if ok else 1
    latest, unknown, nfiles, note = _latest_dispositions(root, "NFRA_COMPEFFICACY")
    if latest is None:
        print("  LIVE  census for NFRA_COMPEFFICACY DID NOT RUN (%s)" % note)
        failed += 1
    else:
        open_items = sorted(k for k, v in latest.items() if v in UNDISPOSITIONED)
        dups, dnote = _plane_duplicates(root, "NFRA_COMPEFFICACY")
        print("  LIVE  NFRA_COMPEFFICACY: %d item(s) across %d file(s); undispositioned %d: %s; phantom/ambiguous %d; "
              "duplicate ids across documents %s"
              % (len(latest), nfiles, len(open_items), ", ".join(open_items) or "-", len(unknown),
                 ("DID NOT RUN (%s)" % dnote) if dups is None else
                 ("%d: %s" % (len(dups), "; ".join("%s in %s" % (k, ", ".join(os.path.basename(x) for x in v))
                                                    for k, v in sorted(dups.items())) or "-"))))
    print("RESULT: %d arm(s) failed of %d (+ live census)" % (failed, len(arms)))
    return 1 if failed else 0


def _acceptance_cli(root, argv):
    """`--acceptance <CODE> [--round N]`: read-only CLI limb -- the hand sweep, mechanized (S169,
    AMGT_RESAPP-Z-S169, ruling s.3.3). Prints the sweep and ALWAYS returns 0: this is a disclosure,
    never a gate -- a FAIL criterion does not refuse anything here or anywhere else in this module."""
    try:
        code = argv[argv.index("--acceptance") + 1]
    except (ValueError, IndexError):
        print("[surprise-row-gate] --acceptance needs a <CODE>", file=sys.stderr)
        return 0
    round_n = None
    if "--round" in argv:
        try:
            round_n = int(argv[argv.index("--round") + 1])
        except (ValueError, IndexError):
            print("[surprise-row-gate] --round needs an integer", file=sys.stderr)
            return 0
    sweep = _acceptance_sweep(root, code, round_n=round_n)
    fails = _flagged_rows(sweep, "FAIL")
    unvs = _flagged_rows(sweep, "UNVERIFIABLE")
    print("[surprise-row-gate] ACCEPTANCE %s (round %s): PASS %d / FAIL %d / UNVERIFIABLE %d of %d "
          "criteria over %d order(s); unrounded %d; FAIL: %s; UNVERIFIABLE: %s"
          % (code, round_n if round_n is not None else "ALL", sweep["PASS"], sweep["FAIL"],
             sweep["UNVERIFIABLE"], sweep["criteria"], len(sweep["orders"]), sweep["unrounded"],
             "; ".join(fails) or "none", "; ".join(unvs) or "none"))
    return 0


def main(argv):
    root = _repo_root()
    if "--self-test" in argv:
        return _self_test(root)
    if "--acceptance" in argv:
        return _acceptance_cli(root, argv)
    _disp, _src = _dispatched_from_argv_or_env(argv[1:])
    files = [a.replace("\\", "/") for a in _disp]
    targets = [f for f in files if CHANNEL_RE.search(f)]
    _baseline_rel = "org/surprise_channel/.corpus-baseline.json"
    _baseline_staged = _baseline_rel in files  # GATSCP GS-e-4: a baseline reset triggers the corpus pass
    if not targets and not _baseline_staged:
        print("[surprise-row-gate] OK: no surprise-channel rows in this commit "
              "(denominator: %d dispatched path(s))." % len(files))
        return 0

    global _BLOB_MEMO
    _BLOB_MEMO = {}
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
        # GATSCP GS-t-1: scoped to the act -- the dispatched channel paths; a bystander's failure prints STANDING.
        _act_argv = []
        for _t in targets:
            _act_argv += ["--act", _t]
        if _baseline_staged:
            _act_argv += ["--act", _baseline_rel]
        if _scv.main(_act_argv) != 0:
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
        # THE AUDITED OVERRIDE, HONOURED HERE (2026-09-03, 1.0.0_SA_CTO on 1.0.0_SA_CTO~Z's measurement via 93575): this
        # gate cannot see the commit message, so it always exited 1 on a violation; safe-commit read the message, audited
        # the '# surprise-row-override: <reason>' and warned -- and then the pre-commit hook re-ran this gate and refused
        # anyway. The override therefore never worked on any path. safe-commit now exports SURPRISE_ROW_OVERRIDE after
        # writing its audit line; when it is set, the violations print as WARN and the gate exits 0. A raw `git commit`
        # never has it, so an un-audited override is still impossible. The variable carries the reason, never a bare flag.
        _ovr = os.environ.get("SURPRISE_ROW_OVERRIDE", "").strip()
        if _ovr:
            # BLOCKED: THIS LINE USED TO READ "(audited by safe-commit)" UNCONDITIONALLY (found 2026-09-10 by
            # 1.0.0_SA_CTO~Z while measuring 0.0.0_AB_MSTR~Z's 20975, which announced it would set this
            # variable BY HAND for a merge). The gate cannot see who set the variable. safe-commit writes
            # the audit line at safe-commit.sh:758 and THEN exports; a hand-exported variable is honoured
            # identically and leaves NO audit line -- so the gate was printing a provenance claim it had
            # not verified, and an unaudited override wore the name of an audited one. State the reason,
            # name where the audit must be, and do not certify an auditor this process never observed.
            print("[surprise-row-gate] OVERRIDDEN (reason given): %s -- %d violation(s) on NEW rows follow as WARN."
                  % (_ovr, len(all_v)), file=sys.stderr)
            print("    PROVENANCE NOT VERIFIED BY THIS GATE: safe-commit writes an audit line to "
                  "org/git-author-override-audit.<device>.log before exporting. If this override did not come "
                  "from safe-commit, NO audit line exists and this is an UNAUDITED override.",
                  file=sys.stderr)
            for x in all_v:
                print("    WARN: %s" % x, file=sys.stderr)
            # THE GATE'S OWN LINE (2026-09-11, 1.0.0_SA_CTO on 0.0.0_AB_MSTR 95721 / LD-0549): whoever set the
            # variable, the process that HONOURED it records that it did, under a token that never counts
            # as safe-commit's. A hand-exported override now leaves a line naming its provenance UNVERIFIED.
            _wrote = _honour_audit_line(root, _ovr)
            if _wrote:
                print("    honour line written: %s (SURPRISE-ROW-OVERRIDE-HONOURED; safe-commit's own "
                      "SURPRISE-ROW-OVERRIDE line is the audited one, present only if it ran)" % _wrote, file=sys.stderr)
            return 0
        print("[surprise-row-gate] BLOCKED -- %d violation(s) on NEW rows:" % len(all_v),
              file=sys.stderr)
        for x in all_v:
            print("    %s" % x, file=sys.stderr)
        # THE REMEDY IS PATH-SPECIFIC AND SAYING SO IS THE WHOLE FIX (2026-09-10, 0.0.0_AB_MSTR~Z 20975:
        # a seat spent THREE commits on the printed instruction, including one with --cleanup=verbatim).
        # MEASURED: safe-commit.sh:767 exports SURPRISE_ROW_OVERRIDE after auditing the message line, so
        # the message-body form WORKS on the commit path exactly as printed. safe-merge.sh has ZERO hits
        # for that variable across 315 lines -- so on a MERGE there is no override limb at all, and the
        # printed instruction could never fire there. One remedy, two paths, only one of them reachable.
        print("    override (audited) ON A COMMIT: put '# surprise-row-override: <reason>' in the "
              "commit message body and commit via .tools/safe-commit.sh -- it audits the line, then "
              "exports SURPRISE_ROW_OVERRIDE for the hook.", file=sys.stderr)
        print("    ON A MERGE (safe-merge.sh) THERE IS NO OVERRIDE PATH: the merged index is graded "
              "BEFORE a merge commit message exists, and safe-merge sets no override variable. Fix "
              "the state the violation names, or route it to the gate's owner (1.0.0_SA_CTO).",
              file=sys.stderr)
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
