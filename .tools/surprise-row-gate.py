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
import inspect
import json
import os
import re
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
ID_RE = re.compile(r"^(?P<project>[A-Z0-9_]+)-(?P<z>Z-)?(?:W(?P<w>[0-9]+)-|(?P<c>C-))?S(?P<k>[0-9]+)$")
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
TERMINAL_TO_WORDS = ("complete", "completed", "closed", "done", "superseded", "cancelled", "canceled", "withdrawn")

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
        m = TO_STATUS_RE.search(text)
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


def _coordinate_violations(rel, folder_kind, added, committer, c_in_schema, merging=False,
                           parent_ids=None):
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
                                            parent_ids=None):
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
    if open_items:
        out.append("%s: NEW row (%s) while %d of %d investigation item(s) under %s are NOT "
                   "dispositioned (latest carrier reads UNDER_INVESTIGATION): %s. The slug waits until every "
                   "investigation is CVO-checked; an existing item is dispositioned by a NEW row that names it in "
                   "`adjudicates` (spine L10 precondition; Andrew-direct 2026-09-03 'Recs approved')."
                   % (rid, route_word, len(open_items), len(latest), code, ", ".join(open_items)))
    return out


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


def _open_tos_for_project(root, code, merging=False):
    """The census below, read ONCE per (root, code, merging) per gate run. The caller asks per NEW remediation row
    plus once for its notes, so a 20-row slug would otherwise re-run the same proof-of-spec checks up to 40 times.
    HEAD and the index do not move inside one gate process, so the first answer is the answer."""
    key = (root, code, bool(merging))
    if key not in _OPEN_TOS_CACHE:
        _OPEN_TOS_CACHE[key] = _open_tos_census(root, code, merging=merging)
    return _OPEN_TOS_CACHE[key]


def _open_tos_census(root, code, merging=False):
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
    open_ids, proven = [], []
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
        m = TO_STATUS_RE.search(text)
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
    return open_ids, len(paths), note


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


def _route_precondition_violations(root, rel, row, code, open_tos=None, route_word=None, merging=False,
                                   parent_ids=None):
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
        open_ids, total, note = _open_tos_for_project(root, code, merging=merging)
    else:
        open_ids, total, note = open_tos
    if open_ids is None:
        return ["%s: the L10 precondition (every task order under %s terminal) could NOT be evaluated (%s) "
                "-- REFUSED, fail-closed" % (rid, code, note)]
    if open_ids:
        if _posn_round2_terminal_exception(root, rel, row, code, open_ids, total):
            return []
        if _posn_round3_terminal_exception(root, rel, row, code, open_ids, total):
            return []
        return ["%s: NEW remediation row (%s) while %d of %d task order(s) under %s are NOT "
                "terminal at HEAD: %s. The slug waits until every task order is complete "
                "(Andrew-direct 2026-09-03, @716a9bc7ce call 3, LD-0521: 'We do not route until the job "
                "is over')." % (rid, route_word, len(open_ids), total, code, ", ".join(open_ids))
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
    p = log_path or os.environ.get("SAFE_COMMIT_AUDIT_LOG") or os.path.join(root, "org", "git-author-override-audit.log")
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
    id_fabric = "site-z" if (m and m.group("z")) else "laptop"
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
                if _monotone_advance(orow, nrow):
                    continue  # the two clocks moved forward on a remediation row; noted by check_file, never refused
                out.append("%s: EXISTING row %s was MUTATED in place (content hash %s -> %s). "
                           "Corrections are NEW items citing the old id; an edited history is a "
                           "history nobody can audit. A remediation row's own clocks may advance in place "
                           "(disarm ARMED->DISARMED with `at`, remediation OPEN->REMEDIATED, closed false->true, "
                           "nothing else changed)." % (rel, oid, h_old[:12], h_new[:12]))
    return out


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
    if o.get("closed") is False and n.get("closed") is True:
        moved = True
        n["closed"] = False
    # THE FOURTH ADMITTED MOVE (R-19 addendum @06061b21af): `disarm.owner` may change ONLY when the same write appends
    # exactly ONE evidence entry citing a CTO ruling by id and vintage (`R-<n>` and `@<hash>`) and NO clock moves.
    # Measured need: LGIC_CANON-W5-S2 and C-S20 were ruled reassigned (R-19) and the field was immutable, so a ruling
    # had no landing surface; measured hazard the immutability guards: a graded party renaming its way out of a
    # hazard -- which is why the citation is required and the clock may not move in the same write.
    owner_moved = False
    if isinstance(od, dict) and isinstance(nd, dict) and od.get("owner") != nd.get("owner"):
        oe, ne = o.get("evidence"), n.get("evidence")
        if (isinstance(oe, list) and isinstance(ne, list) and len(ne) == len(oe) + 1 and ne[:len(oe)] == oe
                and RULING_CITATION_RE.search(str(ne[-1]))):
            owner_moved = True
            nd["owner"] = od.get("owner")
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
    v.extend(_mutation_violations(rel, head, staged))
    added = [r for r in new_rows if r.get("id") not in old_ids]
    # UNIQUENESS ACROSS DOCUMENTS (94007): every NEW id is unused in every OTHER document of its plane at the index.
    if folder_project and added:
        _pd, _pn = _plane_docs(root, folder_project, kind, rel)
        _dv, _dn = _duplicate_id_violations(rel, kind, added, folder_project, _pd, _pn)
        v.extend(_dv)
        notes.extend(_dn)
    # THE ALLOCATOR DISCIPLINE (RULING 2 @9ef9a40aae): W<n> from its own worker only; no W from a seat; C- the CVO's, in
    # adjudications/ only, required once the staged schema admits it.
    _cmt = _committer_serial(root)
    # BOUNDARY (b): one read of the merge's parents per channel file, shared by both limbs.
    _mrg_now = _merge_in_progress(root)
    _pids, _pnote = _parent_row_ids(root, rel) if _mrg_now else (None, "")
    _c_in_schema = "C-" in str(((schema.get("properties") or {}).get("id") or {}).get("pattern", ""))
    v.extend(_coordinate_violations(rel, folder_kind, added, _cmt, _c_in_schema,
                                    merging=_mrg_now, parent_ids=_pids))
    # FOREIGN-ROW SWEEP: every new investigation row is the committer's own, or a co-worker's riding along.
    _cw = _seats_with_open_orders(root, folder_project)[0] if folder_project else set()
    _fv, _fn = _foreign_row_violations(rel, kind, added, _cmt, coworkers=_cw,
                                       merging=_mrg_now, parent_ids=_pids)
    v.extend(_fv)
    notes.extend(_fn)
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
            _mrg = _merge_in_progress(root)
            # PROVENANCE COMES FROM THE `_pids` READ ALREADY TAKEN ABOVE for the coordinate limb and
            # the foreign-row sweep -- one read of the merge's parents per channel file, now shared by
            # four limbs instead of two. No second read, and no way for the two answers to disagree.
            pre = _route_precondition_violations(root, rel, row, folder_project, route_word=_route_word,
                                                 merging=_mrg, parent_ids=_pids)
            pre.extend(_investigations_precondition_violations(rel, row, folder_project, _route_word,
                                                               _latest_dispositions(root, folder_project),
                                                               merging=_mrg, parent_ids=_pids))
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
                _l, _u, _nf, _ = _latest_dispositions(root, folder_project)
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
    arms = [
        # THE HONOUR AUDIT LINE (2026-09-11, 0.0.0_AB_MSTR 95721): the gate records every override it honours.
        ("honour audit line: written with the HONOURED token, agent, reason and UNVERIFIED provenance",
         lambda: (lambda t: "SURPRISE-ROW-OVERRIDE-HONOURED  9.9.9_XX_TEST  reason=why: repro  provenance=UNVERIFIED-BY-GATE" in t
                  and t.startswith("2026-09-11T00:00:00Z ") and "SURPRISE-ROW-OVERRIDE  " not in t.replace("HONOURED  ", ""))(_honour_line())),
        ("honour audit line: an unwritable log path returns None and never raises (the override stays honoured)",
         lambda: _honour_audit_line(root, "x", log_path=os.path.join(_tmpd, "audit.log", "nope", "z.log")) is None),
        ("one item UNDER_INVESTIGATION -> refused, names it",
         lambda: any("X_PRJ-S1" in x and "NOT dispositioned" in x for x in _investigations_precondition_violations(
             "r", row, "X_PRJ", "route=SPEC_ERROR", ({"X_PRJ-S1": "UNDER_INVESTIGATION", "X_PRJ-S2": "GRADUATED"}, [], 1, "")))),
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
         lambda: "_open_tos_for_project(root, code, merging=merging)"
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


def main(argv):
    root = _repo_root()
    if "--self-test" in argv:
        return _self_test(root)
    _disp, _src = _dispatched_from_argv_or_env(argv[1:])
    files = [a.replace("\\", "/") for a in _disp]
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
                  "org/git-author-override-audit.log before exporting. If this override did not come "
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
