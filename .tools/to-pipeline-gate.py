#!/usr/bin/env python3
"""to-pipeline-gate.py -- the L6 gate of the canonical fabric workflow (org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md).
The file keeps its historical name; renaming a gate breaks the hook chain on every device.

AUTHORITY: Andrew-direct 2026-09-01 at the 3.0.0_SA_CVO terminal -- "re-authorize the three
enforcement checks and add the stage-3 preflight" / "we need these set up in a manner that they
are actually mandated" / "I prefer gates and deterministic methodology because anything that is
simply 'guidance' may dissipate or otherwise be inconsistent over long-running sessions."

WHAT THIS GATES, AND WHY IT IS THE KEYSTONE
  org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md specifies five enforcement checks. Check 1 (the
  proof-of-spec validation gate) IS BUILT and DOES enforce -- but only on an instance whose
  GOVERNING TO carries a naming <decomp_ref>. MEASURED 2026-09-01: 130 of 2233 TO files carry
  one = 5.8%. Check 1 is therefore inert on 94% of the estate, not because it is broken but
  because nothing ever required the TO to carry the element that activates it.

  CHECK 2 IS THAT REQUIREMENT. Gate the neck of the funnel: a TO that conformantly requires a
  decomp structurally requires the decomp, which requires the PRD, which requires registration.
  One gate at TO issuance enforces the entire upstream funnel without taxing any other act.

  PROSPECTIVE ONLY (Andrew-direct, same terminal): this fires on NEWLY ADDED TO files. Existing
  TOs are not back-filled and are not refused. A gate that retroactively refuses 2,103 files
  would be ignored wholesale, which is the failure mode CLAUDE.md rule 21 limb (iii) records.
  ONE EXCEPTION, AND ONLY ONE (Andrew-direct card 6, ~18:4xZ 2026-09-13, "recs approved", record
  @e2210bf34c, on 1.0.0_SA_CTO's REC in the IRPT_FNTEND round-4 analysis s.6): GATE (viii), the
  <placeholders> declaration, ALSO grades a TO staged as MODIFIED -- if and only if that TO ALREADY
  DECLARES <placeholders> at HEAD. Nothing is back-filled: an order that declares the element is by
  construction not one of the legacy files the rule above protects, and a modify of an order that does
  not declare it is graded by nothing here. Every other limb stays newly-added only.

THE THREE-VALUE PREFLIGHT ENUM, AND WHY NOT TWO
  RUN | DECLARED-NOT-APPLICABLE | (absent -> refused). A two-value RUN/SKIPPED enum forces a
  genuinely-inapplicable tool to be recorded as SKIPPED -- a vocabulary with no not-applicable
  value encodes non-application as a violation. Eight instances of that class were measured on
  2026-09-01 alone.

FAIL-CLOSED. An unreadable file, an unparseable block or an unexpected exception REFUSES.
A gate that fails open is not a gate.
"""
import ast
import os
import inspect
import posixpath
import re
import pathlib
import shlex
import subprocess
import sys

# TWO ROOTS (project-tree spec s.7/s.8, Andrew-ruled 2026-09-02 ~20:0xZ; `task-orders` with the hyphen is
# the TREE spelling, prospective only): the flat seat-dir task_orders/ population stays exactly as it is;
# the tree adds org/missions/D*/MACRO/PROJECT/task-orders/. A gate that reads one root is blind to the
# other for the whole dual-register period.
# The tree's level grammar is DATA: org/standards/PROJECT_TREE.contract.json (COO, contract_version 0.1.0)
# -- directive folder ^D(0|[1-9][0-9]?)$, task_orders_glob org/missions/D*/*/*/task-orders/*.md. The
# regexes below are that contract's values; a change there is a change here, stated in its `readers`.
_TREE_D = r"D(?:0|[1-9][0-9]?)"
TO_PATH_RE = re.compile(r"(^|/)org/.*/task_orders/[^/]+\.md$|(^|/)org/missions/" + _TREE_D + r"/[^/]+/[^/]+/task-orders/[^/]+\.md$")
TREE_TO_RE = re.compile(r"(^|/)(org/missions/(" + _TREE_D + r")/([^/]+)/([^/]+))/task-orders/[^/]+\.md$")
DECOMP_RE = re.compile(r"<decomp_ref>(.*?)</decomp_ref>", re.S)
PREFLIGHT_RE = re.compile(r"<preflight>(.*?)</preflight>", re.S)
NONE_WORD_RE = re.compile(r"^\W*(NONE|N/?A|NO\b)", re.I)
OVERRIDE_RE = re.compile(r"^#\s*pipeline-override:\s*(\S.*)$", re.M)

# Each preflight tool must appear with a disposition. The tool names are the ratified ones.
PREFLIGHT_TOOLS = ("comp-schedule", "comp-iam", "comp-adversary")
DISPOSITION_RE = r"(RUN|DECLARED-NOT-APPLICABLE)"

# THIRD ADMISSIBILITY LIMB (Andrew-direct 2026-09-01, "All recs approved" -- open-call 3 of 9).
# The ratified fork-1 gate was runtime-OR-vintage. MEASURED 2026-09-01 across all 8 candidate
# lenses: that predicate admits 7 of 8 and is NOT what separated the strong lenses from the weak
# ones. A vintage dates the CORPUS; it cannot say the lens was BLIND ON YOUR SUBJECT -- and that
# is the failure a decomp actually eats. Specimen: `comp-dataflow origin perfrp_emit_core.py`
# returned "2 reads scanned, 2 unresolved-dynamic (blind)" -- a vintage alone would have shown two
# rows and read as an answer.
#
# So a RUN disposition must carry, ON ITS OWN LINE, either a DENOMINATOR (any digit -- the count
# the lens scanned) or an explicit blindness/coverage word. COST: none for the seven admitted
# lenses, which already print one unprompted. NON-APPLICATION: a lens whose output is a single
# boolean over a named subject has no population and owes no denominator -- declare it
# DECLARED-NOT-APPLICABLE with that as the reason.
COVERAGE_WORD_RE = re.compile(
    r"(BLIND|COVERAGE|DENOMINATOR|UNRESOLVED|SCANNED|NOT-?FOUND|REFUSED|\d)", re.I)

# STEP-3 FABRIC DECLARATION (Andrew-direct 2026-09-01, "All recs approved" -- open-call 4 of 9).
# From the canonical-workflow transcript: "we need to discuss at that point if this is going to be
# a laptop fabric project or a site Z fabric project". MEASURED 2026-09-01: 0 of 349 project JSONs
# carry ANY fabric/device/host/site key -- the fork has NO CARRIER AT ALL. Folded into this same
# choke point because layer 3 already OPENS org/projects/<code>.json to read dep_stage; this is one
# more key on a read that already happens. PROSPECTIVE ONLY per Andrew-direct "don't get caught up
# on historical TOs" -- it binds a project the moment someone cuts a NEW TO against it, never
# retroactively.
# NFRA_CTLPLN.TO-CT-c-6 (round 3, PRD C-PLACEMENT, FWD-7; CTO msg 105973): dell1 and dell2 joined the enum as
# boxes of their own. Rule-24 record: org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~5/FABRIC_ENUM_RULE24_RECORD.md
# NFRA_CTLPLN.TO-CT-t-3 (FWD-2) and NFRA_CTLPLN.TO-CT-ab-8: FABRIC_ENUM is DERIVED from the device register (below, after
# _fabric_values()). .tools/missions-tree-index.py resolves it from the same register read (lib/devices.py placement_values()),
# never by AST on a literal; a box added to org/devices/DEVICES.json reaches the gate with no edit.


def _fabric_values():
    """The fabric values the device register allows (lib/devices.py placement_values), loaded by file path. An unreadable
    register raises: the callers refuse (fail-closed), never fall back to FABRIC_ENUM."""
    import importlib.util as _ilu
    spec = _ilu.spec_from_file_location(
        "opal_devices_for_gate", os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "lib", "devices.py"))
    mod = _ilu.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.placement_values()


# The gate's fabric enum IS the register's placement values. Derived at import: an unreadable register raises here, so the
# gate refuses to run at all (fail-closed) rather than falling back to a list.
FABRIC_ENUM = tuple(_fabric_values())

# GATE (i) -- Andrew-direct 2026-09-03 (state of record @716a9bc7ce call 3, LD-0521; his conditional
# "If there's any chance of doing this out of order, we need more gates" became his ask): L7 WORKERS ARE
# TIER-2 SEATS ONLY. A NEW tree task order whose <issued_to> names a Tier-0 serial (0.0.<n>_*: MSTR and the
# utility seats) or a Tier-1 serial (*_SA_*: the exec tier) is REFUSED. Prospective, TREE projects only --
# every tree TO is new by construction, so nothing historical is re-graded; a flat-root TO is left to its
# 2,000-file legacy population. Measured the same night, before this limb existed: TO-CE-DISC-2 ->
# 1.0.0_SA_CTO and TO-CE-TP-1 -> 3.0.0_SA_CVO were cut through this gate and WITHDRAWN by their issuer on
# his correction ("Only tier2 agents are workers, MSTR does not 'WORK' on projects, they are an integrator").
# A `~lane` suffix is stripped before the tier is read (a lane of an exec is still an exec). A value that
# is not a serial at all (an executor CLASS, prose) is not this limb's -- the seating clause owns that shape.
ISSUED_TO_RE = re.compile(r"<issued_to>\s*([^<\n]+?)\s*</issued_to>", re.I)
ISSUED_BY_RE = re.compile(r"<issued_by>\s*([^<\n]+?)\s*</issued_by>", re.I)
ISSUER_PROSE_RE = re.compile(r"^\s*[*_`]*\s*Issuer\s*[*_`]*\s*:", re.I | re.M)
SERIAL_RE = re.compile(r"^\d+\.\d+\.\d+_[A-Z]{2}_[A-Za-z0-9]+")
TIER01_RE = re.compile(r"^(?:0\.0\.\d+_[A-Z]{2}_|\d+\.\d+\.\d+_SA_)")
# THE GRANT CANNOT BE EMPTY (Andrew-direct 2026-09-04 ~04:58Z at this terminal, "recs approved" on /open-calls CALL 1 REC (c),
# record @9ef9a40aae; ADHC_OWNPTH.005; registry stanza @e08447ff7d): a spine-v3 worker 0.9.0_WK_<CODE>~<n> is enumerated in
# no lane and is admitted to exactly the paths its NON-TERMINAL order names in its <paths> block at HEAD. So a NEW tree order
# issued to a worker without that block -- or with an empty one -- is an order that cannot be executed without the override
# the ruling retired, and the cut is where it is refused. Measured before this limb: 0 of 171 files under org/missions
# carried a <paths> block; the first drain's worker committed both its surfaces through the override.
WORKER_SERIAL_RE = re.compile(r"^0\.9\.0_WK_[A-Z0-9_]+?[~_][0-9]+$")
# LINE-ANCHORED (94157 gap (a)): the block is the <paths> tag ALONE on its line through the </paths> tag alone on its
# line; a prose mention of `<paths>` earlier in the file is not the block and is not graded as one.
PATHS_BLOCK_RE = re.compile(r"^[ \t]*<paths>[ \t]*\r?\n(.*?)^[ \t]*</paths>[ \t]*$", re.S | re.I | re.M)

# GATE (viii) -- THE PLACEHOLDER DECLARATION IS MANDATORY ON A NEW TREE ORDER (1.0.0_SA_CTO ruling D,
# closing by name the weakness FE-s-23 shipped with; decomp cell FE-s-28, rows S31/S38/S43).
#
# WHAT IT ARMS, AND WHY ONLY THE ISSUER CAN ARM IT. .tools/proof-of-spec-check.py compares each
# acceptance row's RECORDED invocation against the same-id <invocation> in the governing TO and
# normalises EXACTLY two things: whitespace at the ends, and expansion of the placeholders THE TO
# DECLARES. Its _declared_placeholders() returns None when the <placeholders> element is absent, and
# None means ANNOUNCE -- the divergence prints and refuses nothing. So the enforcement is switched on
# by the ISSUER: the exact party whose prompt-only correction the limb exists to catch (round 2, row
# S31 -- two criteria corrected in a SPAWN PROMPT and never in the file; the checker then read VALID
# over 20 rows and 0 violations). An integrity check the checked party may decline to arm is a
# courtesy, not an enforcement. NON-APPLICATION: none -- an opt-in integrity check has no honest scope.
#
# THE BOUNDARY, AND WHY IT IS THIS ONE. Measured over the tracked corpus at the cut: 2559 task-order
# files, 305 of them TREE orders, and 2 carry <placeholders> (FE-s-23, which invented the element, and
# FE-s-28, which mandates it). Refusing the corpus would block 2557 files; grandfathering by DATE or by
# PROJECT is the opt-in again under a new name and drifts the moment the date passes. So this limb binds
# exactly WHAT AN ISSUANCE ADDS, which is the prospective scope this gate already owns and states once,
# in _newly_added: main() sends only newly-added (git A/R) paths through check_file, so a MODIFICATION of
# an existing order -- a status flip, an amendment -- is never graded and the 2557 stay committable BY
# CONSTRUCTION. No second vintage mechanism is added here: a duplicate control with its own drift is
# worse than the one that already works (same finding as the criterion-grammar limb above). The boundary
# is written into the refusal TEXT so a seat that hits it learns the rule instead of guessing at it.
#
# ONE NARROW EXTENSION OF THAT BOUNDARY (2026-09-13, FE-s-29 limb 4; Andrew-direct card 6 ~18:4xZ, "recs
# approved", record @e2210bf34c, on 1.0.0_SA_CTO's REC in the IRPT_FNTEND round-4 analysis s.6): a task
# order staged as MODIFIED is ALSO graded by this limb -- ONLY IF THE ORDER ALREADY DECLARES <placeholders>
# AT HEAD. An amendment could otherwise delete or break the declaration that armed the checker on a live
# order and nothing would say so (the modify exemption 3.0.0_SA_CVO qualified). An order that does not
# already declare is still never graded on a modify -- nothing is back-filled, and the 2,103-file
# back-fill the PROSPECTIVE ONLY rule exists to prevent is untouched, because an order that declares is by
# construction not a legacy file. _placeholder_modify_violations() below; main() feeds it _staged_modified().
#
# LINE-ANCHORED (2026-09-13, FE-s-29 limb 1; 1.0.0_SA_CTO RULING M(i) @23af9479ab; rows S53, W4-S7): the
# element is the tag STANDING ON ITS OWN LINE. The unanchored `<placeholders>(.*?)</placeholders>` under
# re.S read from the FIRST prose mention of the tag to the real element's close, so S53 measured, by calling
# this function on real bytes, (C) an undeclared invocation token ADMITTED when the criteria sat inside that
# span and (D) an order with NO element ADMITTED when its prose quoted this gate's own help text.
#
# CASE-SENSITIVE ON PURPOSE, AND MIRRORED FROM THE CONSUMER. The two regexes below are byte-identical to
# proof-of-spec-check.py's PLACEHOLDERS_TAG_RE / PLACEHOLDER_TOKEN_RE. A tolerant reader here (re.I, say)
# would ADMIT a <PLACEHOLDERS> element the checker cannot see -- an order that passes the gate arming
# nothing, which is precisely the state this limb exists to end. .tools/tests/test_mandatory_placeholders.py
# and .tools/tests/test_placeholders_reader.py hold the cross-tool arms that keep the two readers equal.
PLACEHOLDERS_TAG_RE = re.compile(r"^[ \t]*<placeholders>(.*?)</placeholders>[ \t]*$", re.M)
PLACEHOLDER_TOKEN_RE = re.compile(r"<([A-Z][A-Z0-9_]*)>")
INVOCATION_TAG_RE = re.compile(r"<invocation>(.*?)</invocation>", re.S)
PLACEHOLDERS_BOUNDARY = (
    "BOUNDARY (what this binds and what it does not): it binds a task order STAGED AS ADDED (git status "
    "A or R) under org/missions/D<n>/<MACRO>/<CODE>/task-orders/ -- what an ISSUANCE ADDS -- and a "
    "MODIFICATION of such an order ONLY WHEN THE ORDER ALREADY DECLARES <placeholders> AT HEAD (Andrew-direct "
    "card 6, 2026-09-13, record @e2210bf34c). It does NOT bind a MODIFICATION of an existing order that does "
    "not already declare the element (a status flip, an amendment), and it does NOT bind the flat-root legacy "
    "population under org/**/task_orders/. Measured at the FE-s-28 cut: 2559 task-order files tracked, 305 "
    "tree, 2 carrying the element -- the others stay committable because none of them is ever newly-added "
    "again and none of them declares. The element is read LINE-ANCHORED: the tag must stand on its own line."
)
PLACEHOLDERS_HOWTO = (
    "SATISFY IT with one line in the worker face: <placeholders>WS, PORT</placeholders> naming every "
    "<TOKEN> the order's own <invocation> strings carry, or <placeholders>NONE</placeholders> when they "
    "are literal (an explicit NONE is ENFORCE over an EMPTY substitution set, not a waiver). The element "
    "is lowercase and exact -- proof-of-spec-check.py reads it case-sensitively."
)


# GATE (iv) -- LD-0521 Amendment 3 (Andrew at the 0.0.0_AB_MSTR terminal 2026-09-03 ~04:0xZ: "COO is the only agent
# that does task orders"). A NEWLY ADDED tree task order commits only under 2.0.0_SA_COO or one of its ~lanes, read
# by the estate's actor precedence (.tools/lib/resolve-actor.sh): $OPAL_AGENT_SERIAL (per process) -> the session's
# org/mcp/sessions/<id>.serial file -> GIT_AUTHOR_IDENT last. MEASURED 2026-09-03 (2.0.0_SA_COO, message 93110): at
# pre-commit time GIT_AUTHOR_IDENT reads the git CONFIG name, never safe-commit's --author, so a limb keyed on it alone
# refused the one seat it exists to admit on every standard safe-commit; the two per-process carriers were present and
# unread. The wrapper's --author is a CLAIM; the process carriers are the actor. A MODIFICATION of an existing task
# order -- the worker's own status flip, admitted by the lane grant that made task-orders/** ANY -- is not this limb's:
# main() sends only newly-added paths through check_file. Prospective, tree projects only. An unreadable identity
# REFUSES (fail-closed): a gate that cannot see who is committing must not admit an issuance.
ISSUER_SERIAL = "2.0.0_SA_COO"


def _committer_serial(root):
    """The committing seat's serial by the resolve-actor precedence: $OPAL_AGENT_SERIAL, then
    org/mcp/sessions/$CLAUDE_CODE_SESSION_ID.serial, then the name before ' <' in GIT_AUTHOR_IDENT (the config
    name at pre-commit time -- a last resort, never the --author), or '' when nothing answers."""
    env = os.environ.get("OPAL_AGENT_SERIAL", "").strip()
    if env:
        return env
    sid = os.environ.get("CLAUDE_CODE_SESSION_ID", "").strip()
    if sid:
        try:
            p = os.path.join(root, "org", "mcp", "sessions", sid + ".serial")
            if os.path.isfile(p):
                with open(p, encoding="utf-8") as fh:
                    v = fh.read().strip()
                if v:
                    return v
        except OSError:
            pass
    try:
        ident = subprocess.run(["git", "var", "GIT_AUTHOR_IDENT"], cwd=root, capture_output=True, text=True, encoding="utf-8", errors="replace",
                               timeout=20).stdout
    except Exception:  # noqa: BLE001
        return ""
    return ident.split(" <", 1)[0].strip()


def _issuer_identity_violations(rel, author):
    """GATE (iv): complaints about WHO is committing a NEW tree TO. [] for flat-root TOs (out of scope)."""
    rel = rel.replace("\\", "/")
    if not TREE_TO_RE.search(rel):
        return []
    if not author:
        return ["%s: committer identity UNREADABLE -- a NEW tree task order commits only under %s; REFUSED, fail-closed"
                % (rel, ISSUER_SERIAL)]
    base = author.split("~", 1)[0].strip()
    if base != ISSUER_SERIAL:
        return ["%s: a NEW tree task order committed under %r. COO is the only agent that does task orders (LD-0521 "
                "A3): a new file under org/missions/*/*/*/task-orders/ commits only under %s or a ~lane of it. A "
                "worker's own <status> flip on an EXISTING task order is a modification and is not this limb's."
                % (rel, author, ISSUER_SERIAL)]
    return []


# CELL-REFERENCE RESOLUTION AT THE CUT (2026-09-03, 1.0.0_SA_CTO on 3.0.0_SA_CVO~A 93412 + the issuer's own evidence
# 93419): NFRA_CLDGRPH-S5's class recurred 62 minutes after its instance was fixed -- a criterion whose cell_refs did not
# resolve against the decomposition passed this gate at issuance and could only fail at the worker's proof check, after
# the order was cut, dispatched and worked; S5 cost a round trip and a BLOCKING row when found at the flip. Every tree
# task order already names its decomposition (<decomp_doc>) and its cells (<owned_cells>, criterion cell_refs), so the
# resolution is knowable the moment the face is written. This limb reads the decomposition from the INDEX (what the
# commit contains), then HEAD, then the worktree; every cell token (commas, semicolons or whitespace between them) must
# match the cell-id grammar AND be a cell of that decomposition. An unreadable or absent decomposition is a NOTE, never a
# refusal here -- to-decomp-ref-lint.py owns absence. Tree task orders only, NEW files only (this gate's standing model).
DECOMP_DOC_TAG_RE = re.compile(r"<decomp_doc>\s*([^<]+?)\s*</decomp_doc>", re.S)
OWNED_CELLS_RE = re.compile(r"<owned_cells>(.*?)</owned_cells>", re.S)
CRITERION_TAG_RE = re.compile(r"<criterion\b([^>]*?)/?>")
# spine v3.0 L6 carrier 4 (one clause per criterion): a criterion WITH a body carries its invocation and expectation as
# children; the self-closing v2 shape is refused on a NEW tree order. The block regex refuses to open on a self-closing
# tag (the lookbehind), so a v2 tag never swallows the text up to the next </criterion>.
CRITERION_BLOCK_RE = re.compile(r"<criterion\b([^>]*?)(?<!/)>(.*?)</criterion>", re.S)
CRITERION_SELFCLOSE_RE = re.compile(r"<criterion\b[^>]*?/>")
ATTR_RE = re.compile(r'(\w+)\s*=\s*"([^"]*)"')
# The same grammar as .tools/proof-of-spec-check.py CELL_ID_RE (its anchored branches included); a change there is a
# change here, and the checker's battery (.tools/tests/test_proof_of_spec_cell_id_re.py) is the control for both.
CELL_ID_RE = re.compile(
    r"\b(?:[A-Z][A-Z0-9]*-(?:m-[a-z0-9_]+|[a-z]{1,4}-[a-z]?\d+)"
    r"|L3W3-[0-9a-f]{4}-\d+"
    r"|L3S7B-[0-9a-f]{4}-\d+"
    r"|CARD-R-(?:m-\d+|[0-9a-f]{4}-\d+)"
    r"|INGEST-(?:T\d|CONV|INV)-\d+)\b")


def _split_cells(value):
    return [c for c in re.split(r"[\s,;]+", value or "") if c]


def _decomp_text(root, doc):
    """(text, where) for the decomposition at `doc`: the index first, then HEAD, then the worktree; (None, why)."""
    for ref, where in ((":" + doc, "index"), ("HEAD:" + doc, "HEAD")):
        try:
            r = subprocess.run(["git", "show", ref], cwd=root, capture_output=True, text=True, encoding="utf-8",
                               errors="replace", timeout=30)
        except Exception as exc:  # noqa: BLE001
            return None, "git show raised %s" % exc
        if r.returncode == 0 and r.stdout.strip():
            return r.stdout, where
    p = os.path.join(root, doc)
    if os.path.isfile(p):
        try:
            with open(p, encoding="utf-8", errors="replace") as fh:
                return fh.read(), "worktree"
        except OSError as exc:
            return None, "worktree read failed (%s)" % exc
    return None, "not in the index, not at HEAD, not in the worktree"


def _cell_refs_violations(root, rel, text, decomp_text=None):
    """(violations, notes) for a NEW tree TO's cell references. `decomp_text` is injectable for the battery."""
    rel = rel.replace("\\", "/")
    if not TREE_TO_RE.search(rel):
        return [], []
    m = DECOMP_RE.search(text)
    if not m or NONE_WORD_RE.match(m.group(1).strip()):
        return [], []
    body = m.group(1)
    dm = DECOMP_DOC_TAG_RE.search(body)
    doc = dm.group(1).strip() if dm else ""
    owned = _split_cells(" ".join(OWNED_CELLS_RE.findall(body)))
    crit = []
    for tag in CRITERION_TAG_RE.finditer(text):
        attrs = dict(ATTR_RE.findall(tag.group(1)))
        for c in _split_cells(attrs.get("cell_refs", "")):
            crit.append((attrs.get("id", "").strip() or "<no id>", c))
    v, notes = [], []
    for label, tok in [("owned_cells", c) for c in owned] + [("criterion %s" % cid, c) for cid, c in crit]:
        if not CELL_ID_RE.fullmatch(tok):
            v.append("%s: %s names %r, which is not a cell id by the decomposition grammar (a stray delimiter, a typo, "
                     "or prose in an attribute)" % (rel, label, tok))
    if not doc:
        notes.append("%s: <decomp_ref> names no <decomp_doc>; cell references graded on grammar only" % rel)
        return v, notes
    if decomp_text is None:
        decomp_text, where = _decomp_text(root, doc)
    else:
        where = "injected"
    if decomp_text is None:
        notes.append("%s: decomposition %s unreadable (%s) -- cell references graded on grammar only; absence is "
                     "to-decomp-ref-lint's" % (rel, doc, where))
        return v, notes
    ids = set(CELL_ID_RE.findall(decomp_text))
    if not ids:
        notes.append("%s: decomposition %s carries no cell id by the grammar -- cell references graded on grammar only" % (rel, doc))
        return v, notes
    for label, tok in [("owned_cells", c) for c in owned] + [("criterion %s" % cid, c) for cid, c in crit]:
        if CELL_ID_RE.fullmatch(tok) and tok not in ids:
            v.append("%s: %s names cell %r, which is not a cell of %s (%d cell ids read from the %s) -- a criterion that "
                     "cites a cell the decomposition lacks cannot be proved by the assignee (NFRA_CLDGRPH-S5 class)"
                     % (rel, label, tok, doc, len(ids), where))
    if not v:
        notes.append("%s: %d owned cell(s) and %d criterion reference(s) resolve against %s (%d cell ids, %s)"
                     % (rel, len(owned), len(crit), doc, len(ids), where))
    return v, notes


def _criterion_grammar_violations(rel, text):
    """spine v3.0 L6 (carrier 4 of eight; Andrew-direct 2026-09-03 ~22:2xZ at the CRO terminal): ONE CLAUSE PER CRITERION
    on a NEW tree task order. A mechanical criterion carries exactly one <invocation> and exactly one <expect> as children;
    a judgment criterion carries judgment="true" and needs neither (the CVO grades it at L9); a criterion with two of either
    is COMPOUND and refused; the self-closing v2 shape is refused with the grammar named, because the spine's transition
    rule makes every NEW issuance v3. Flat-root orders are not graded (the legacy population)."""
    rel = rel.replace("\\", "/")
    if not TREE_TO_RE.search(rel):
        return []
    v = []

    # WARN: CRITERION PRESENCE -- D0_INFRA_TIGHTENING s.6 ROW 10 (placed 1.0.0_SA_CTO 94994).
    #
    # THE LIMBS BELOW GRADE THE GRAMMAR OF CRITERIA THAT EXIST. Both are `for` loops over
    # matches, so a face carrying ZERO criteria runs ZERO iterations and produces ZERO
    # violations -- the gate passes it, and THE ORDER CAN THEN NEVER BE CLOSED.
    # .tools/proof-of-spec-check.py reads cell_refs EXCLUSIVELY from these tags (":435 --
    # NOTHING HERE IS DERIVED") and the acceptance-row schema exposes no cell_refs field, so a
    # prose-only acceptance section yields `0/0 criteria carry >=1 cell_ref` and the `complete`
    # flip is STRUCTURALLY UNREACHABLE no matter how good the work is.
    #
    # MEASURED, and the issuer who added this limb is the one who caused it:
    # ETFS_GUARDRAIL.TO-EG-s-22 was cut with a prose acceptance section, PASSED THIS GATE at
    # issuance, and its assignee then finished 7 of 7 arms and could not flip (row
    # ETFS_GUARDRAIL-W1-S32). The assignee held the face in its own <paths> grant and REFUSED to
    # add the tags itself -- editing the issuance half so your own proof validates certifies an
    # alignment the cut never declared -- which is the only reason the defect was visible.
    #
    # NOTE: A GATE THAT GRADES ONLY WHAT IS PRESENT CANNOT SEE AN OMISSION. Same class as the
    # dep_stage enum note below, from the other direction: there a wrong vocabulary hid matching
    # violations; here an empty set passes vacuously.
    #
    # VINTAGE: PROSPECTIVE-ONLY, AND NO NEW MECHANISM IS ADDED FOR IT. This function has ONE
    # production call site (check_file), and main() calls check_file only over `targets`, which
    # requires `p in added` -- and _newly_added's own docstring states the contract: "A
    # modification (M) does not: this gate never refuses an existing TO." So a pre-existing
    # untagged face is never graded by this limb, and a SECOND vintage mechanism here would be a
    # duplicate control with its own drift risk on a gate that already solved this and wrote it
    # down.
    n_crit = len(re.findall(r"<criterion\b", text))
    if n_crit == 0:
        v.append("%s: carries ZERO <criterion> tags. A face with no criterion PASSES every grammar\n"
                 "  check vacuously and can NEVER be closed: proof-of-spec-check reads cell_refs only\n"
                 "  from <criterion> tags, so the instance reads '0/0 criteria carry >=1 cell_ref' and\n"
                 "  the complete flip is unreachable. Add at least one:\n"
                 "    <criterion id=\"..\" cell_refs=\"..\"><invocation>..</invocation><expect>..</expect></criterion>\n"
                 "  or a judgment criterion <criterion id=\"..\" cell_refs=\"..\" judgment=\"true\"/>." % rel)

    for m in CRITERION_SELFCLOSE_RE.finditer(text):
        attrs = dict(ATTR_RE.findall(m.group(0)))
        if attrs.get("judgment", "").strip().lower() == "true":
            continue
        v.append("%s: criterion %s is the v2 self-closing shape. spine v3.0 L6: a mechanical criterion is\n"
                 "    <criterion id=\"..\" cell_refs=\"..\"><invocation>..</invocation><expect>..</expect></criterion>\n"
                 "  (one of each; the checker decides PASS by the match), or judgment=\"true\" with no children (graded by\n"
                 "  the CVO at L9). A compound criterion is split at the cut." % (rel, attrs.get("id", "<no id>")))
    for m in CRITERION_BLOCK_RE.finditer(text):
        attrs = dict(ATTR_RE.findall(m.group(1)))
        cid = attrs.get("id", "<no id>")
        if attrs.get("judgment", "").strip().lower() == "true":
            continue
        n_inv = len(re.findall(r"<invocation\b", m.group(2)))
        n_exp = len(re.findall(r"<expect\b", m.group(2)))
        if n_inv > 1 or n_exp > 1:
            v.append("%s: criterion %s is COMPOUND (%d <invocation>, %d <expect>) -- one clause per criterion; split it "
                     "into one criterion per invocation+expect pair (spine v3.0 L6)" % (rel, cid, n_inv, n_exp))
        elif n_inv < 1 or n_exp < 1:
            v.append("%s: criterion %s is mechanical (no judgment=\"true\") but carries %d <invocation> and %d <expect>; "
                     "it needs exactly one of each, or judgment=\"true\" (spine v3.0 L6)" % (rel, cid, n_inv, n_exp))
    return v


_TABLE_FIRST_COL_RE = re.compile(r"^\|\s*([^|\n]+?)\s*\|", re.M)


def _declared_cells(decomp_text):
    """The decomposition's OWN cell ids: those written in the FIRST column of a table row, where a decomposition
    declares its cells. Any other id in the text is a CITATION -- another project's cell named as an input, a gate or
    an edge -- and no issuance of this project can own it (LGIC_ENFORCE-S1; measured 2026-09-15 at HEAD: MDPF_TAXSMA
    declares 27 of the 31 ids it carries, the other 4 NFRA_OPLGTW's; LGIC_NAMING 15 of 20, the other 5 LGIC_ENFORCE's).
    A text that declares none in a table keeps the prior reading: every id."""
    text = decomp_text or ""
    declared = set()
    for m in _TABLE_FIRST_COL_RE.finditer(text):
        declared.update(CELL_ID_RE.findall(m.group(1)))
    return declared or set(CELL_ID_RE.findall(text))


def _coverage_gap(decomp_text, owned_union):
    """PURE. (missing, unknown, ids): the decomposition's DECLARED cell ids no staged order owns, the owned ids the
    decomposition lacks, and the declared id set (_declared_cells)."""
    ids = _declared_cells(decomp_text)
    owned = set(owned_union)
    return sorted(ids - owned), sorted(owned - ids), ids


def _coverage_groups(root, targets):
    """I/O half: {(code, rel_json, doc): [owned cell ids...]} over the NEWLY ADDED tree task orders."""
    return _coverage_scan(root, targets)[0]


def _coverage_scan(root, targets):
    """I/O half: (groups, overrides). groups is _coverage_groups'; overrides is {(code, rel_json, doc): [(rel, reason)]}
    for the NEW orders carrying the '# pipeline-override:' line the coverage refusal offers. check_file audits that
    line and returns before any per-order limb; this is the coverage limb reading the same line, which it never did,
    so the refusal named an escape nothing read (LGIC_ENFORCE-S1)."""
    groups, overrides = {}, {}
    for rel in targets:
        rel = rel.replace("\\", "/")
        if not TREE_TO_RE.search(rel):
            continue
        code, rel_json, err = _project_row_rel(root, rel)
        if not code or not rel_json or err:
            continue
        try:
            with open(os.path.join(root, rel), "r", encoding="utf-8", errors="replace") as fh:
                text = fh.read()
        except OSError:
            continue
        m = DECOMP_RE.search(text)
        if not m or NONE_WORD_RE.match(m.group(1).strip()):
            continue
        dm = DECOMP_DOC_TAG_RE.search(m.group(1))
        doc = dm.group(1).strip() if dm else ""
        owned = _split_cells(" ".join(OWNED_CELLS_RE.findall(m.group(1))))
        groups.setdefault((code, rel_json, doc), []).extend(owned)
        ov = OVERRIDE_RE.search(text)
        if ov:
            overrides.setdefault((code, rel_json, doc), []).append((rel, ov.group(1).strip()))
    return groups, overrides


def _coverage_grade(groups, stage_of, decomp_of, overrides=None):
    """PURE given its two readers. spine v3.0 L6 (carrier 1 of eight; Andrew-direct 2026-09-03 ~22:2xZ): ONE issuance
    covers EVERY cell. For a tree project whose row reads dep_stage DECOMP (the issuance moment), the union of
    <owned_cells> across the staged NEW orders must equal the named decomposition's cell set; a missing cell REFUSES,
    naming it. A project already EXECUTING is a recut and is NOT graded here -- a recut covers the affected cells,
    which no gate can enumerate. An unreadable decomposition is a NOTE (absence is to-decomp-ref-lint's)."""
    v, notes = [], []
    for (code, rel_json, doc), owned in sorted(groups.items()):
        stage = stage_of(code, rel_json)
        if stage != "DECOMP":
            notes.append("%s: issuance coverage not graded (dep_stage=%r; only a DECOMP-stage issuance must cover every "
                         "cell -- a recut covers its affected cells)" % (code, stage))
            continue
        if not doc:
            notes.append("%s: issuance coverage not graded (no <decomp_doc> named)" % code)
            continue
        decomp_text = decomp_of(doc)
        if decomp_text is None:
            notes.append("%s: issuance coverage not graded (decomposition %s unreadable; absence is to-decomp-ref-lint's)"
                         % (code, doc))
            continue
        missing, unknown, ids = _coverage_gap(decomp_text, owned)
        if not ids:
            notes.append("%s: issuance coverage not graded (%s carries no cell id by the grammar)" % (code, doc))
            continue
        cited = len(set(CELL_ID_RE.findall(decomp_text)) - ids)
        if cited:
            notes.append("%s: %d id(s) in %s are cited, not declared in a table's first column -- another project's "
                         "cells, not required of this issuance" % (code, cited, doc))
        ovs = (overrides or {}).get((code, rel_json, doc)) or []
        if missing and ovs:
            notes.append("%s: the issuance under %s owns %d of %d cell(s) of %s -- MISSING: %s -- ADMITTED under the "
                         "audited override on %s (%s)" % (code, rel_json, len(ids) - len(missing), len(ids), doc,
                                                         ", ".join(missing), ovs[0][0], ovs[0][1]))
        elif missing:
            v.append("%s: the issuance under %s owns %d of %d cell(s) of %s -- MISSING: %s. spine v3.0 L6: ONE issuance "
                     "covers EVERY cell of the decomposition; cut the missing order(s) in this same commit, or take the "
                     "audited '# pipeline-override:' on one order with the reason" % (
                         code, rel_json, len(ids) - len(missing), len(ids), doc, ", ".join(missing)))
        else:
            notes.append("%s: issuance coverage %d of %d cell(s) of %s owned by the staged orders" % (code, len(ids), len(ids), doc))
    return v, notes


def _row_stage_at(root, rel_json, ref):
    """dep_stage of a project row at `ref` ("" = the staged index, "HEAD" = the last commit), or None.

    NEVER THE WORKTREE. The first cut of `stage_of` opened the file on disk, which is the
    worktree-vs-record class -- a peer's UNCOMMITTED edit to project.json could change another seat's
    coverage grade, and the gate would report on a state no commit ever held.
    """
    spec = ("%s:%s" % (ref, rel_json)) if ref else (":%s" % rel_json)
    try:
        p = subprocess.run(["git", "show", spec], cwd=root, capture_output=True, text=True,
                           encoding="utf-8", errors="replace", timeout=30)
        if p.returncode != 0:
            return None
        import json as _j
        return (_j.loads(p.stdout) or {}).get("dep_stage")
    except Exception:  # noqa: BLE001
        return None


def _coverage_violations(root, targets):
    # COVERAGE GRADES THE ISSUANCE **MOMENT**, SO IT READS **HEAD** -- the stage BEFORE this commit.
    # ⛔ THE COUPLING THIS FIXES, measured by exercise: the limb grades only at DECOMP, and `stage_of`
    # used to read the WORKTREE. So a COO obeying spine s.4 carrier 2 -- "the COO flips EXECUTING in
    # the issuance commit" -- flipped the row to EXECUTING and TURNED THIS LIMB OFF in the same act.
    # THE ONLY WAY TO GET COVERAGE GRADED WAS TO VIOLATE CARRIER 2. That is why the flip drifted on
    # v3's first fresh-project round (4.0.0_SA_CRO 94331). Reading HEAD decouples them: at the issuance
    # moment the row still reads DECOMP, so coverage grades AND the flip may land in the same commit.
    # A genuine recut (row already EXECUTING at HEAD) is still not graded here, exactly as documented.
    groups, overrides = _coverage_scan(root, targets)
    return _coverage_grade(groups,
                           lambda code, rel_json: _row_stage_at(root, rel_json, "HEAD"),
                           lambda doc: _decomp_text(root, doc)[0],
                           overrides)


def _carrier2_violations(root, targets):
    """SPINE s.4 CARRIER 2: after an L6 issuance the project row must read EXECUTING.

    CARRIER 2 GRADES THE ISSUANCE **RESULT**, SO IT READS THE **STAGED INDEX** (else HEAD) -- the
    stage AFTER this commit. Coverage reads HEAD, this reads the index; two limbs, two moments, both
    satisfiable at once. Read from ONE moment they are mutually exclusive, which was the defect.

    WHY A REFUSER AT ALL (1.0.0_SA_CTO's design call on 4.0.0_SA_CRO 94331): carrier 2 is one of the
    spine's s.4 clauses that BINDS BY READING rather than by enforcement, and s.4 exists precisely to
    name what is still owed a refuser. It drifted on the first fresh-project round, silently, and the
    measured consequence was that cvo_send_guard's executing census did not carry the project at all --
    so the CVO's one-send rule did not bind for it and every reader of dep_stage saw a project at L5
    while two orders were complete and a drain had landed.

    ⛔ IT IS NOT AN APPROVAL GATE (CLAUDE.md forbids inventing one): it grades the issuance's OWN
    contents against the spine, exactly as the coverage limb grades "every cell covered". Nobody's
    permission is added to anything.
    NOT "this commit changed project.json" -- "AFTER this commit the row READS EXECUTING", so a recut
    mid-round whose row is already EXECUTING passes without re-flipping a field that is already right.
    """
    out = []
    for (code, rel_json, _doc) in sorted({k for k in _coverage_groups(root, targets)}):
        after = _row_stage_at(root, rel_json, "") or _row_stage_at(root, rel_json, "HEAD")
        if after != "EXECUTING":
            out.append("%s: this commit adds NEW tree task order(s) but %s reads dep_stage=%r after it. "
                       "Spine s.4 carrier 2: THE COO FLIPS EXECUTING IN THE ISSUANCE COMMIT. Until it does, "
                       "cvo_send_guard's executing census omits the project (so the L8 one-send rule does not "
                       "bind for it) and every reader of dep_stage -- the L10 precondition, R6's close limbs, "
                       "the drain-prep probes -- sees a project still at L5 while its orders run. Stage the "
                       "row with the issuance. FIX: set dep_stage EXECUTING in project.json and re-commit."
                       % (code, rel_json, after))
    return out


_SELF_SRC = pathlib.Path(__file__).read_text(encoding="utf-8", errors="replace") \
    if "__file__" in dir() else ""


def _merge_probe_is_merge_head_only():
    """True iff _merge_in_progress tests MERGE_HEAD and nothing else, judged on its CODE lines.

    STOP: read the FUNCTION, never grep the module. Two earlier cuts of this check split the
    module source on a marker -- and found THIS helper's own occurrence of that marker first, so
    it graded itself, and its own token list contains "parents". Adding the signature to the
    marker just moved the collision. `inspect.getsource(fn)` returns that function and nothing
    else, so there is no corpus for the checker to pollute.

    Comments and the docstring are stripped because _merge_in_progress deliberately WARNS about
    the parent-count shape in prose; an arm that greps the whole body convicts it for its own
    warning. That is the difference between reading the tool and reading the world.
    """
    try:
        body = inspect.getsource(_merge_in_progress)
    except Exception:  # noqa: BLE001
        return False
    code, in_doc = [], False
    for ln in body.split(chr(10)):
        t = ln.strip()
        if t.startswith(chr(34) * 3):
            in_doc = not in_doc
            continue
        if in_doc or not t or t.startswith("#"):
            continue
        code.append(t)
    body = chr(10).join(code)
    if "MERGE_HEAD" not in body or "--git-path" not in body:
        return False
    return not any(tok in body for tok in ("rev-list", "parents", "HEAD^", "^2"))


def _merge_exemption_precedes_checks():
    """True iff main() consults the merge probe BEFORE it reads the staged-added set.

    Same instrument rule as above: read main()'s own source, not the module's.
    """
    try:
        body = inspect.getsource(main)
    except Exception:  # noqa: BLE001
        return False
    i_probe = body.find("_merge_in_progress(root)")
    i_added = body.find("added = _newly_added(root)")
    return 0 <= i_probe < i_added


def _carrier2_grades_state_after():
    """True iff _carrier2_violations decides on the row's STATE AFTER the commit, judged on CODE lines.

    The distinction that matters: "AFTER this commit the row reads EXECUTING" (correct -- a recut whose
    row is already EXECUTING passes) versus "this commit CHANGED project.json" (wrong -- it would refuse
    a legitimate recut for not re-flipping a field that is already right). Comments and the docstring are
    stripped, because this function's own prose necessarily discusses the shape it forbids.
    """
    try:
        src = inspect.getsource(_carrier2_violations)
    except Exception:  # noqa: BLE001
        return False
    code, in_doc = [], False
    for ln in src.split(chr(10)):
        t = ln.strip()
        if t.startswith(chr(34) * 3):
            in_doc = not in_doc
            continue
        if in_doc or not t or t.startswith("#"):
            continue
        code.append(t)
    body = chr(10).join(code)
    reads_after = ('_row_stage_at(root, rel_json, "")' in body)
    compares_executing = ('!= "EXECUTING"' in body)
    no_diffing = not any(tok in body for tok in ("git diff", "--name-only", "changed"))
    return reads_after and compares_executing and no_diffing


def _self_test():
    """RED/GREEN arms for carriers 1 (coverage) and 4 (criterion grammar), pure -- no repo read."""
    decomp = "cells: CE-a-1 CE-a-2 CE-a-3 (three)"
    grade = lambda owned, stage="DECOMP", text=decomp: _coverage_grade(  # noqa: E731
        {("X_PRJ", "org/missions/D0/X/X_PRJ/project.json", "d.md"): owned}, lambda c, r: stage, lambda d: text)
    tree = "org/missions/D0/X/X_PRJ/task-orders/X_PRJ.TO-1.md"
    v2 = '<criterion id="C1" cell_refs="CE-a-1"/>'
    v3 = '<criterion id="C1" cell_refs="CE-a-1"><invocation>echo 1</invocation><expect>1</expect></criterion>'
    comp = '<criterion id="C2" cell_refs="CE-a-1"><invocation>a</invocation><expect>x</expect><expect>y</expect></criterion>'
    judg = '<criterion id="C3" cell_refs="CE-a-1" judgment="true"/>'
    noexp = '<criterion id="C4" cell_refs="CE-a-1"><invocation>a</invocation></criterion>'
    SO = lambda files, ver="v0.4", last="abc123def456": _signoff_violations("t", "X_PRJ", "prd/X_PRJ_PRD.md", ver, last, files)  # noqa: E731
    _cro = {"signed_by": "4.0.0_SA_CRO", "verdict": "SIGNED", "prd_version": "v0.4", "prd_pin": "abc123de"}
    _cvo = {"signed_by": "3.0.0_SA_CVO~Z", "verdict": "SIGNED", "prd_version": "v0.4", "prd_pin": "abc123de"}
    ph_inv = ('<criterion id="C1" cell_refs="CE-a-1"><invocation>cd <WS> && timeout 120 python x.py'
              '</invocation><expect>OK</expect></criterion>')
    ph_lit = ('<criterion id="C1" cell_refs="CE-a-1"><invocation>timeout 120 python x.py</invocation>'
              '<expect>OK</expect></criterion>')
    ph = _placeholder_declaration_violations
    _ck = ("X_PRJ", "org/missions/D0/X/X_PRJ/project.json", "d.md")
    _tbl = "| cell | x |\n|---|---|\n| `CE-a-1` | a |\n| `CE-a-2` | b |\n\nCE-a-2 waits on OG-r-1, another project's cell.\n"
    _cg = lambda owned, ov=None: _coverage_grade({_ck: owned}, lambda c, r: "DECOMP", lambda d: _tbl, ov)  # noqa: E731
    # GATE (ix) fixture: a battery in the SHAPE of test_proof_of_spec_alignment.py (arms named in check(), printed as
    # `  {verdict:4s} {name}`, a %d RESULT line, a BATTERY PASS line). Pure; the real bytes are the battery's.
    _ov_red = ("results = []\n"
               "def check(name, ok):\n    results.append((name, 'PASS' if ok else 'FAIL'))\n"
               "check('fail-closed: a bogus ref is a violation', True)\n"
               "for name, verdict in results:\n    print(f'  {verdict:4s} {name}')\n"
               "print('[x] RESULT: %d arm(s) failed of %d' % (0, len(results)))\n"
               "print('BATTERY PASS -- every arm as expected')\n")
    def _ov_limb6(stub_v):
        """Z-S1: run the REAL check_file on an order carrying '# pipeline-override:', with LIMB 6 stubbed to stub_v."""
        import shutil
        import tempfile
        g = globals()
        real = g["check_prd_signoff"]
        g["check_prd_signoff"] = lambda root, rel: (list(stub_v), [])
        d = tempfile.mkdtemp(prefix="tpg-z-s1-")
        try:
            rel = "org/missions/D0/X/X_PRJ/task-orders/X_PRJ.TO-1.md"
            p = os.path.join(d, rel)
            os.makedirs(os.path.dirname(p))
            with open(p, "w", encoding="utf-8") as fh:
                fh.write("# X_PRJ TO-1" + chr(10) + chr(10) + "# pipeline-override: self-test" + chr(10))
            return check_file(d, rel)
        finally:
            g["check_prd_signoff"] = real
            shutil.rmtree(d, ignore_errors=True)

    _PPT = "org/missions/D9/IRPT/X/task-orders/"
    _PPD = "org/missions/D9/IRPT/X/deliverables/"

    def _pp(files, rel, staged):
        """W42-S4: create `files` in a temp root, resolve the candidates for `rel`, return them root-relative ('/')."""
        import shutil
        import tempfile
        d = tempfile.mkdtemp(prefix="tpg-w42-s4-")
        try:
            for f in files:
                p = os.path.join(d, *f.split("/"))
                os.makedirs(os.path.dirname(p), exist_ok=True)
                with open(p, "w", encoding="utf-8") as fh:
                    fh.write("{}")
            cands, _ = _proof_instance_candidates(d, rel, staged)
            return [os.path.relpath(c, d).replace(os.sep, "/") for c in cands]
        finally:
            shutil.rmtree(d, ignore_errors=True)

    _refused = ["t: project X_PRJ PRD prd/X_PRJ_PRD.md ratified-text half reads REFUSED (3.0.0_SA_CVO~O)"]
    arms = [
        # Z-S1 (3.0.0_SA_CVO~O verdict @c6d6f60d62): '# pipeline-override:' does NOT bypass LIMB 6
        ("override RED (Z-S1): an order carrying '# pipeline-override:' against a REFUSED half is STILL refused",
         lambda: _ov_limb6(_refused)[0] == _refused),
        ("override GREEN (Z-S1): the same order against a SIGNED PRD (LIMB 6 clean) is admitted by the override",
         lambda: _ov_limb6([])[0] == [] and any("OVERRIDE taken" in n for n in _ov_limb6([])[1])),
        # LIMB 6 -- the PRD sign-off gate (L4-R), pure arms; the tilde signer counts for its base serial
        ("signoff RED: no files -> refused naming BOTH reviewers",
         lambda: len(SO({})) == 2 and all("NO sign-off" in x for x in SO({}))),
        ("signoff RED: CRO signed, CVO missing -> refused naming the ratified-text half / CVO only",
         lambda: len(SO({"4.0.0_SA_CRO.json": _cro})) == 1 and "3.0.0_SA_CVO" in SO({"4.0.0_SA_CRO.json": _cro})[0] and "ratified-text" in SO({"4.0.0_SA_CRO.json": _cro})[0]),
        ("signoff RED: one verdict REFUSED -> refused, review_ref named",
         lambda: any("reads REFUSED" in x and "r@1" in x for x in SO({"4.0.0_SA_CRO.json": _cro, "3.0.0_SA_CVO.json": dict(_cvo, verdict="REFUSED", review_ref="r@1")}))),
        ("signoff RED: STALE legacy file (signed v0.3, PRD v0.4) -> refused, naming the half",
         lambda: any("brief half reads STALE" in x for x in SO({"4.0.0_SA_CRO.json": dict(_cro, prd_version="v0.3"), "3.0.0_SA_CVO.json": _cvo}))),
        ("signoff (v3.15): a legacy pair at the current version is ADMITTED regardless of the pin (half-binding supersedes pin-binding)",
         lambda: SO({"4.0.0_SA_CRO.json": _cro, "3.0.0_SA_CVO.json": _cvo}, last="ffff0000eeee") == []),
        ("signoff GREEN: both SIGNED at the current version and pin, CVO via a ~Z lane -> admitted",
         lambda: SO({"4.0.0_SA_CRO.json": _cro, "3.0.0_SA_CVO~Z.json": _cvo}) == []),
        ("signoff RED: an unreadable sign-off file is NOT a sign-off",
         lambda: any("not readable" in x for x in SO({"4.0.0_SA_CRO.json": None, "3.0.0_SA_CVO.json": _cvo}))),
        ("coverage RED: two orders own a-1, a-2 of three -> refused naming CE-a-3",
         lambda: any("MISSING: CE-a-3" in x for x in grade(["CE-a-1", "CE-a-2"])[0])),
        ("coverage GREEN: three cells owned -> admitted, coverage noted 3 of 3",
         lambda: grade(["CE-a-1", "CE-a-2", "CE-a-3"])[0] == [] and any("3 of 3" in n for n in grade(["CE-a-1", "CE-a-2", "CE-a-3"])[1])),
        ("coverage NOT GRADED at EXECUTING (a recut): admitted, noted",
         lambda: grade(["CE-a-1"], stage="EXECUTING")[0] == [] and any("not graded" in n for n in grade(["CE-a-1"], stage="EXECUTING")[1])),
        ("coverage NOT GRADED when the decomposition is unreadable: admitted, noted",
         lambda: grade(["CE-a-1"], text=None)[0] == []),
        ("coverage (S1): an id the decomposition only CITES is not required -> admitted, the citation noted",
         lambda: _cg(["CE-a-1", "CE-a-2"])[0] == [] and any("1 id(s)" in n and "cited" in n for n in _cg(["CE-a-1", "CE-a-2"])[1])),
        ("coverage (S1): a DECLARED cell still missing -> refused naming it, and not the cited id",
         lambda: any("MISSING: CE-a-2" in x and "OG-r-1" not in x for x in _cg(["CE-a-1"])[0])),
        ("coverage (S1): the override the refusal offers ADMITS the missing cell, noted with its order",
         lambda: _cg(["CE-a-1"], {_ck: [("t.md", "why")]})[0] == []
                 and any("ADMITTED" in n and "t.md" in n for n in _cg(["CE-a-1"], {_ck: [("t.md", "why")]})[1])),
        ("grammar: v2 self-closing criterion on a tree order -> refused, grammar named",
         lambda: any("v2 self-closing" in x for x in _criterion_grammar_violations(tree, v2))),
        ("grammar: v3 mechanical criterion (one invocation, one expect) -> admitted",
         lambda: _criterion_grammar_violations(tree, v3) == []),
        ("grammar: COMPOUND criterion (two expects) -> refused",
         lambda: any("COMPOUND" in x for x in _criterion_grammar_violations(tree, comp))),
        ("grammar: judgment=true self-closing -> admitted (graded by the CVO)",
         lambda: _criterion_grammar_violations(tree, judg) == []),
        ("grammar: mechanical criterion without <expect> -> refused",
         lambda: any("exactly one of each" in x for x in _criterion_grammar_violations(tree, noexp))),
        ("grammar: a flat-root order is not graded (legacy population)",
         lambda: _criterion_grammar_violations("org/tier2_senior/A/task_orders/X.TO-1.md", v2) == []),
        # GATE (vii): <issued_by> -- the field a DOWNSTREAM gate reads (2026-09-10, msg 20981).
        # The FOUR refusals are the point; an arm that only proves the green case is half a test.
        ("issued_by GREEN: tag present and non-empty -> admitted",
         lambda: _issued_by_violations(tree, "<issued_by>2.0.0_SA_COO~ZZ</issued_by>" + chr(10) + v3) == []),
        ("issued_by RED: no tag at all -> refused, and the refusal NAMES the downstream gate",
         lambda: any("HALTGT" in x and "issued_by" in x for x in _issued_by_violations(tree, v3))),
        ("issued_by RED: tag present but EMPTY -> refused (halt-gate CONTINUES past an empty match)",
         lambda: _issued_by_violations(tree, "<issued_by></issued_by>" + chr(10) + v3) != []),
        ("issued_by RED: a markdown Issuer: line ALONE -> still refused, and the refusal says the prose is MACHINE-INVISIBLE",
         lambda: any("MACHINE-INVISIBLE" in x for x in
                     _issued_by_violations(tree, "**Issuer:** 2.0.0_SA_COO~ZZ" + chr(10) + v3))),
        ("issued_by: a flat-root order is NOT graded (same scope as every other gate in this file)",
         lambda: _issued_by_violations("org/tier2_senior/A/task_orders/X.TO-1.md", v3) == []),
        # GATE (v): the grant cannot be empty (RULING 1 @9ef9a40aae)
        ("grant RED: a worker order with NO <paths> block -> refused, names the ruling",
         lambda: any("NO <paths> block" in x for x in _worker_grant_violations(tree, "<issued_to>0.9.0_WK_X_PRJ~2</issued_to>\n" + v3))),
        ("grant GREEN: a worker order with two entries (a file, a glob) -> admitted",
         lambda: _worker_grant_violations(tree, "<issued_to>0.9.0_WK_X_PRJ~2</issued_to>\n<paths>\n  org/modules/graph/cli.py\n  .tools/tests/test_x_*.py\n</paths>\n" + v3) == []),
        ("grant RED: an EMPTY block (blank + comment lines only) -> refused",
         lambda: any("EMPTY" in x for x in _worker_grant_violations(tree, "<issued_to>0.9.0_WK_X_PRJ~2</issued_to>\n<paths>\n\n  # nothing\n</paths>\n"))),
        ("grant RED: an absolute entry and a climbing entry -> each refused",
         lambda: len(_worker_grant_violations(tree, "<issued_to>0.9.0_WK_X_PRJ~2</issued_to>\n<paths>\n/etc/x\norg/../secret\norg/ok.py\n</paths>\n")) == 2),
        ("grant: a prose mention of <paths> before the block is NOT the block (94157 gap (a)) -- the block after it is graded",
         lambda: _worker_grant_violations(tree, "<issued_to>0.9.0_WK_X_PRJ~2</issued_to>\nthe `<paths>` block below names the grant\n<paths>\norg/ok.py\n</paths>\n" + v3) == []),
        ("grant: a prose mention with NO block after it -> refused as NO block",
         lambda: any("NO <paths> block" in x for x in _worker_grant_violations(tree, "<issued_to>0.9.0_WK_X_PRJ~2</issued_to>\nsee <paths> in the protocol\n" + v3))),
        # CARRIER 2 + THE DECOUPLING (4.0.0_SA_CRO 94331; the coupling measured by exercise before the fix).
        # THE ARM THAT MATTERS IS THE THIRD: the two limbs must read DIFFERENT refs. Read from ONE moment
        # they are mutually exclusive -- coverage grades only at DECOMP, carrier 2 requires EXECUTING --
        # which is why obeying carrier 2 used to turn coverage OFF.
        ("carrier2: coverage reads HEAD (the issuance MOMENT), never the worktree",
         lambda: '_row_stage_at(root, rel_json, "HEAD")' in inspect.getsource(_coverage_violations)
         and "open(os.path.join(root, rel_json)" not in inspect.getsource(_coverage_violations)),
        ("carrier2: the limb reads the STAGED INDEX first, HEAD as fallback (the issuance RESULT)",
         lambda: '_row_stage_at(root, rel_json, "")' in inspect.getsource(_carrier2_violations)),
        ("carrier2 DECOUPLING: the two limbs read DIFFERENT refs -- one moment each",
         lambda: '"HEAD"' in inspect.getsource(_coverage_violations)
         and '_row_stage_at(root, rel_json, "")' in inspect.getsource(_carrier2_violations)
         and inspect.getsource(_coverage_violations) != inspect.getsource(_carrier2_violations)),
        ("carrier2: the refusal names the MEASURED consequence, not just the rule",
         lambda: "executing census" in inspect.getsource(_carrier2_violations)
         and "one-send rule does not" in inspect.getsource(_carrier2_violations)),
        # STOP: THIS ARM GRADES CODE, NOT PROSE. Its first cut greped the docstring for a phrase and
        # failed on a capitalisation difference in the sentence it was quoting -- the third time tonight
        # a check read the tool instead of the world. The predicate is a NAMED HELPER now: a lambda doing
        # multi-line string surgery is where both that bug and its two failed repairs lived.
        ("carrier2: it grades the STATE AFTER (a recut whose row already reads EXECUTING passes)",
         lambda: _carrier2_grades_state_after()),
        # MERGE EXEMPTION (94264). A self-test cannot safely open a real merge in the shared tree,
        # so these are structural + a function-level probe; the behavioural arm is 0.0.0_AB_MSTR's
        # own reconcile, which is the RED case that produced the finding.
        ("merge: the gate HAS a merge exemption at all (its two siblings did; this one did not)",
         lambda: "_merge_in_progress" in _SELF_SRC and "MERGE COMMIT -- task-order checks exempt" in _SELF_SRC),
        # STOP: THIS ARM GRADES CODE, NOT PROSE. Its first cut asserted that the string "two
        # parents" was absent from the function -- and FAILED on the function's own WARNING
        # against that very shape. A check that parses prose reads the TOOL, not the world
        # (the estate has that finding twice already). It now strips comments and the docstring
        # and grades the EXECUTABLE lines only.
        ("merge: the probe tests MERGE_HEAD and nothing else -- no parent-count test in the CODE",
         lambda: _merge_probe_is_merge_head_only()),
        ("merge: the exemption is NOT conditioned on how the staged list was sourced",
         lambda: "OWNED_PATHS_STAGED_FILES" not in inspect.getsource(main).split("added = _newly_added")[0]
         and _merge_exemption_precedes_checks()),
        ("merge: _merge_in_progress returns False in a clean tree (positive control on the probe)",
         lambda: _merge_in_progress(_repo_root()) is False),
        ("merge: a NON-merge commit still reaches the task-order checks (the exemption is narrow)",
         lambda: _merge_exemption_precedes_checks()),
        # _top_section BACKTICK TOLERANCE (94213 refusal 2). The RED arm is the bug that was LIVE:
        # it fails against the pre-patch gate and passes after, which is what makes it a control.
        ("endpoint RED: a heading whose command is fenced IS found (was a FALSE ABSENCE)",
         lambda: _top_section("## ENDPOINT (step 2, `/endpoint --forward`)\nbody\n",
                              ENDPOINT_HEADING) is not None),
        ("endpoint GREEN: the bare template heading still found; a DIFFERENT heading still None",
         lambda: _top_section("## ENDPOINT (step 2, /endpoint --forward)\nbody\n",
                              ENDPOINT_HEADING) is not None
         and _top_section("## ENDPOINTS (step 2, /endpoint --forward)\nbody\n",
                          ENDPOINT_HEADING) is None
         and _top_section("## ENDPOINT (step 3, /endpoint --forward)\nbody\n",
                          ENDPOINT_HEADING) is None),
        ("endpoint: a fenced heading INSIDE a ``` fence is still not a section (f1 falsifier holds)",
         lambda: _top_section("```\n## ENDPOINT (step 2, `/endpoint --forward`)\n```\n",
                              ENDPOINT_HEADING) is None),
        ("grant: a seat's order without <paths> is not graded (its grant is its lanes); a flat-root worker order is not graded",
         lambda: _worker_grant_violations(tree, "<issued_to>0.8.0_AE_CloudComp~J</issued_to>\n" + v3) == []
         and _worker_grant_violations("org/tier2_senior/A/task_orders/X.TO-1.md", "<issued_to>0.9.0_WK_X_PRJ~2</issued_to>\n") == []),
        # GATE (viii): the <placeholders> declaration is MANDATORY on a NEW tree order (ruling D, cell FE-s-28).
        # BOTH DIRECTIONS, because a limb that cannot admit is a brick and a limb that cannot refuse is a constant.
        # The REAL-BYTES arms (this estate's own corpus, the end-to-end git states, and the cross-tool agreement
        # with proof-of-spec-check's reader) live in .tools/tests/test_mandatory_placeholders.py.
        ("placeholders RED: a new tree order with NO <placeholders> element -> refused",
         lambda: any("NO <placeholders> element" in x for x in ph(tree, ph_inv))),
        ("placeholders GREEN: <placeholders>WS</placeholders> covering the order's own <WS> -> admitted",
         lambda: ph(tree, "<placeholders>WS</placeholders>\n" + ph_inv) == []),
        ("placeholders GREEN: an explicit NONE over literal invocations -> admitted (ENFORCE, empty set)",
         lambda: ph(tree, "<placeholders>NONE</placeholders>\n" + ph_lit) == []),
        ("placeholders RED: an EMPTY <placeholders></placeholders> element -> refused (an oversight and an intentional NONE must differ)",
         lambda: any("EMPTY" in x for x in ph(tree, "<placeholders></placeholders>\n" + ph_lit))),
        ("placeholders RED: a declaration that omits a token its OWN <invocation> carries -> refused, naming <WS>",
         lambda: any("<WS>" in x and "does not declare" in x for x in ph(tree, "<placeholders>PORT</placeholders>\n" + ph_inv))),
        ("placeholders RED: an UPPERCASE <PLACEHOLDERS> element is not the element -- refused, because the checker's reader is case-sensitive too",
         lambda: any("NO <placeholders> element" in x for x in ph(tree, "<PLACEHOLDERS>WS</PLACEHOLDERS>\n" + ph_inv))),
        ("placeholders: a flat-root order is NOT graded (the legacy population, same scope as every limb here)",
         lambda: ph("org/tier2_senior/A/task_orders/X.TO-1.md", ph_inv) == []),
        ("placeholders: the refusal TEXT names the element, the boundary it binds, what it does NOT bind, and how to satisfy it",
         lambda: all(k in ph(tree, ph_inv)[0] for k in ("<placeholders>", "BOUNDARY", "STAGED AS ADDED",
                                                        "MODIFICATION", "org/**/task_orders/",
                                                        "<placeholders>NONE</placeholders>"))),
        ("placeholders: the element regex is BYTE-IDENTICAL to proof-of-spec-check's (a tolerant reader would admit an order arming nothing)",
         lambda: PLACEHOLDERS_TAG_RE.pattern == r"^[ \t]*<placeholders>(.*?)</placeholders>[ \t]*$"
         and PLACEHOLDERS_TAG_RE.flags & re.M and not PLACEHOLDERS_TAG_RE.flags & re.S
         and PLACEHOLDER_TOKEN_RE.pattern == r"<([A-Z][A-Z0-9_]*)>"),
        # LIMB 1 (RULING M(i), S53): LINE-ANCHORED. Pure arms here; the five REAL-BYTES cases live in
        # .tools/tests/test_placeholders_reader.py.
        ("placeholders RED (S53 D): a PROSE line quoting the element mid-sentence is NOT a declaration -> refused",
         lambda: any("NO <placeholders> element" in x for x in ph(tree, "the help says " + PLACEHOLDERS_HOWTO + "\n" + ph_inv))),
        ("placeholders RED (S53 C): an element BELOW its criteria still grades their tokens -- a prose mention above cannot widen the set",
         lambda: any("<PORT>" in x for x in ph(tree, "a `<placeholders>` mention\n" + ph_inv.replace("<WS>", "<WS> <PORT>")
                                                  + "\n<placeholders>WS</placeholders>\n"))),
        ("placeholders GREEN: the element on its own line BELOW a prose mention is read as exactly its own tokens",
         lambda: ph(tree, "a `<placeholders>` mention\n" + ph_inv + "\n  <placeholders>WS</placeholders>  \n") == []),
        # LIMB 4 (Andrew-direct card 6): a MODIFY is graded ONLY when the order already declares at HEAD.
        ("placeholders MODIFY RED: a declaring order whose amendment DELETES the element -> refused, naming the modify",
         lambda: any("MODIFIED" in x and "NO <placeholders> element" in x
                     for x in _placeholder_modify_violations(tree, "<placeholders>WS</placeholders>\n" + ph_inv, ph_inv))),
        ("placeholders MODIFY GREEN: a declaring order amended with its declaration intact -> admitted",
         lambda: _placeholder_modify_violations(tree, "<placeholders>WS</placeholders>\n" + ph_inv,
                                                "<placeholders>WS</placeholders>\n" + ph_inv + "\namended\n") == []),
        ("placeholders MODIFY: an order that does NOT declare at HEAD is NOT graded, whatever it stages (no back-fill)",
         lambda: _placeholder_modify_violations(tree, ph_inv, ph_inv + "\namended\n") == []
         and _placeholder_modify_violations(tree, ph_inv, "<placeholders>PORT</placeholders>\n" + ph_inv) == []),
        ("placeholders MODIFY: a flat-root order is NOT graded on a modify either",
         lambda: _placeholder_modify_violations("org/tier2_senior/A/task_orders/X.TO-1.md",
                                                "<placeholders>WS</placeholders>\n" + ph_inv, ph_inv) == []),
        ("placeholders MODIFY: main() reads the MODIFIED set from its own function, and the ADDED set's contract is unchanged",
         lambda: "_staged_modified(root)" in inspect.getsource(main)
         and 'code.startswith("A") or code.startswith("R")' in inspect.getsource(_newly_added)),
        # GATE (ix) -- the OUTPUT-VOCABULARY limb (FE-s-36). Pure arms; the REAL-SHAPE controls (F28-AC6 as issued and
        # as re-cut, two runner criteria, an absent target, round 5) live in .tools/tests/test_output_vocabulary.py.
        ("vocabulary: a `0 fail` bar reduces to one run -- its digit a NUMBER SLOT, its lookbehind dropped",
         lambda: _ov_bar_runs(r"(?<![0-9])0 fail")[0] == [_OV_SLOT + " fail"]),
        ("vocabulary: a back-referenced count reduces to number slots, escaped parens to literals",
         lambda: _ov_bar_runs(r"RESULT: (\d+) of \1 arm\(s\) behaved")[0]
         == ["RESULT: " + _OV_SLOT + " of " + _OV_SLOT + " arm(s) behaved"]),
        ("vocabulary: an alternation is not reduced (ANNOUNCE, never refuse)",
         lambda: _ov_bar_runs(r"BATTERY (PASS|OK)")[0] is None),
        ("vocabulary: one python program is evaluable; bun is a RUNNER; a `;` list is not one program",
         lambda: _ov_program("cd <WS> && timeout 300 python .tools/tests/x.py")[:2] == ("PY", ".tools/tests/x.py")
         and _ov_program("cd <WS>/portal && timeout 120 bun test a.test.ts")[0] == "RUNNER"
         and _ov_program("cd <WS>/portal && timeout 180 bun run typecheck; echo rc=$?")[0] == "OTHER"),
        ("vocabulary RED: a battery printing `  {verdict:4s} {name}` lines cannot print `0 fail` -> REFUSED",
         lambda: _ov_judge(_ov_bar_runs("0 fail")[0], False, _ov_templates(_ov_red)[0])[0][1] == "REFUSED"),
        ("vocabulary GREEN: the same battery prints `BATTERY PASS` -> ADMITTED",
         lambda: _ov_judge(["BATTERY PASS"], False, _ov_templates(_ov_red)[0])[0][1] == "ADMITTED"),
        ("vocabulary GREEN: a %d count beside authored words -> ADMITTED (`RESULT: 0 arm(s) failed of`)",
         lambda: _ov_judge(_ov_bar_runs(r"RESULT: 0 arm\(s\) failed of")[0], False,
                           _ov_templates(_ov_red)[0])[0][1] == "ADMITTED"),
        ("vocabulary: a word only a runtime field carries is UNDECIDED (announced); a conditional of constants resolves",
         lambda: _ov_judge(["READERS: yes"], False, _ov_templates("import sys\nprint('READERS: %s' % sys.argv[1])\n")[0])[0][1]
         == "UNDECIDED"
         and _ov_judge(["READERS: yes"], False,
                       _ov_templates("s = 1\nprint('READERS: %s' % ('yes' if s else 'no'))\n")[0])[0][1] == "ADMITTED"),
        ("vocabulary: a line left open with end='' carries on, so its value on the next print is not refused (F5-AC1)",
         lambda: _ov_judge(["NAMES=served x"], False,
                           _ov_templates("print('NAMES=', end='')\nprint('served x')\n")[0])[0][1] != "REFUSED"),
        ("vocabulary: a bare relay, a non-git subprocess and a file printing nothing are OPEN; a git subprocess is not",
         lambda: _ov_templates("import sys\nprint(sys.argv[1])\n")[1] != ""
         and _ov_templates("import subprocess, sys\nsubprocess.run([sys.executable, 'x.py'])\nprint('A')\n")[1] != ""
         and _ov_templates("x = 'A'\n")[1] != ""
         and _ov_templates("import subprocess\nsubprocess.run(['git', 'status'])\nprint('A')\n")[1] == ""),
        ("vocabulary: check_file wires the limb, and the limb reads the tool from the INDEX (`git show :<path>`)",
         lambda: "_output_vocabulary_violations(root, rel, text)" in inspect.getsource(check_file)
         and '":" + rel' in inspect.getsource(_ov_tool)),
        # FE-s-37 -- THE GOVERNING ORDER IS THE ORDER BEING FLIPPED (RULING S, row S61). Source arms; the REAL-SHAPE arms
        # (FE-s-29's instance doctored to FE-s-28 in a real index, its positive control, the committed corpus) live in
        # .tools/tests/test_governing_binding.py.
        ("binding: check_complete_flip hands the checker the flipped order (`--governing-order`, rel), not the instance alone",
         lambda: '"--governing-order", rel' in inspect.getsource(check_complete_flip)),
        ("binding: a refused flip names the checker's VIOLATION lines, not only its verdict line",
         lambda: '"VIOLATION: "' in inspect.getsource(check_complete_flip)),
        # W42-S4 -- the <proof_of_spec> block may name its instance; the tag only ADDS a candidate, never refuses.
        ("proof path W42-S4: a tag-named instance (to_id, not stem) that exists in the deliverables is the candidate",
         lambda: _pp([_PPD + "W~42/X.TO-IB-mr-2.proof_of_spec.json"], _PPT + "X.TO-IB-m19-2.long-name.md",
                     "<proof_of_spec>\nInstance at `" + _PPD + "W~42/X.TO-IB-mr-2.proof_of_spec.json`.\n</proof_of_spec>\n")
         == [_PPD + "W~42/X.TO-IB-mr-2.proof_of_spec.json"]),
        ("proof path W42-S4: no named path -> the stem search runs as before (flat seat, both names)",
         lambda: _proof_instance_candidates("R", "org/tier2_senior/A/task_orders/X.TO-1.md",
                                            "<proof_of_spec>\nno path here\n</proof_of_spec>\n")
         == ([os.path.join("R", "org/tier2_senior/A/deliverables", "X.TO-1.proof_of_spec.json"),
              os.path.join("R", "org/tier2_senior/A/deliverables", "X.TO-1_PROOF_OF_SPEC.json")], None)),
        ("proof path W42-S4: a named path outside the deliverables is ignored -> the stem instance is used, no refusal",
         lambda: _pp([_PPD + "W/X.TO-1.proof_of_spec.json", "org/missions/D9/IRPT/Y/deliverables/W/X.TO-1.proof_of_spec.json"],
                     _PPT + "X.TO-1.md",
                     "<proof_of_spec>\n`org/missions/D9/IRPT/Y/deliverables/W/X.TO-1.proof_of_spec.json`\n</proof_of_spec>\n")
         == [_PPD + "W/X.TO-1.proof_of_spec.json"]),
        ("proof path W42-S4: two existing named instances -> not chosen between; the stem search runs",
         lambda: _pp([_PPD + "W/a.proof_of_spec.json", _PPD + "W/b.proof_of_spec.json", _PPD + "W/X.TO-1.proof_of_spec.json"],
                     _PPT + "X.TO-1.md",
                     "<proof_of_spec>\n`" + _PPD + "W/a.proof_of_spec.json` and `" + _PPD + "W/b.proof_of_spec.json`\n"
                     "</proof_of_spec>\n")
         == [_PPD + "W/X.TO-1.proof_of_spec.json"]),
        ("proof path W42-S4: the schema path beside the instance path in one block -> the instance is used",
         lambda: _pp([_PPD + "W/X.TO-IB-mr-2.proof_of_spec.json"], _PPT + "X.TO-1.md",
                     "<proof_of_spec>\nValidate against `org/standards/PROOF_OF_SPEC.schema.json`; instance `" + _PPD
                     + "W/X.TO-IB-mr-2.proof_of_spec.json`.\n</proof_of_spec>\n")
         == [_PPD + "W/X.TO-IB-mr-2.proof_of_spec.json"]),
        ("proof path W42-S4: template glob text (`deliverables/*/<full-stem>...`) is ignored -> the stem instance",
         lambda: _pp([_PPD + "W/X.TO-1.proof_of_spec.json"], _PPT + "X.TO-1.md",
                     "<proof_of_spec>\n`deliverables/*/<full-stem>.proof_of_spec.json`\n</proof_of_spec>\n")
         == [_PPD + "W/X.TO-1.proof_of_spec.json"]),
        ("proof path W42-S4: the tag's instance absent on disk, the stem instance present -> the stem instance",
         lambda: _pp([_PPD + "W/X.TO-1.proof_of_spec.json"], _PPT + "X.TO-1.md",
                     "<proof_of_spec>\n`" + _PPD + "W/X.TO-IB-mr-2.proof_of_spec.json`\n</proof_of_spec>\n")
         == [_PPD + "W/X.TO-1.proof_of_spec.json"]),
        ("proof path W42-S4: the tag never refuses (the second element is always None)",
         lambda: _proof_instance_candidates("R", _PPT + "X.TO-1.md",
                                            "<proof_of_spec>\n`a/b.proof_of_spec.json` `c/d.proof_of_spec.json`\n"
                                            "</proof_of_spec>\n")[1] is None),
        # GATE (x) WORKSTREAM KEY (row IRPT_BCKEND-S179): per-workstream rounds.
        ("round-issuer GREEN (S179): round 13 at HEAD under workstream ~P; a ~M order into round 13 -> admitted",
         lambda: _round_issuer_violations(tree, "<round>13</round>\n<workstream>~M</workstream>\n" + v3,
                                          {("~P", 13): ["org/missions/D0/X/X_PRJ/task-orders/X_PRJ.TO-0.md"]}) == []),
        ("round-issuer RED (S179): round 13 at HEAD under workstream ~P; a second ~P order into round 13 -> refused",
         lambda: any("workstream ~P round 13" in x and "S154" in x for x in
                     _round_issuer_violations(tree, "<round>13</round>\n<workstream>~P</workstream>\n" + v3,
                                              {("~P", 13): ["org/missions/D0/X/X_PRJ/task-orders/X_PRJ.TO-0.md"]}))),
        ("round-issuer RED (S179): a prose mention of <workstream> is inert -- keyed as the bare round, still collides",
         lambda: any("round 13" in x and "S154" in x for x in
                     _round_issuer_violations(tree, "<round>13</round>\nthe `<workstream>~M</workstream>` element\n" + v3,
                                              {13: ["org/missions/D0/X/X_PRJ/task-orders/X_PRJ.TO-0.md"]}))),
        # GATE (x) -- ONE ISSUER PER ROUND (row AMGT_RESAPP-Z-S154; Rule 27; cell AMGT-rk-55). Pure
        # arms; the real-index battery (a scratch git repo, the gate's own CLI, real committed
        # bytes) lives in .tools/tests/test_gate_x_round_issuer.py.
        ("round-issuer RED: a second order into round 13 (already at HEAD) -> refused naming round 13 and S154",
         lambda: any("round 13" in x and "S154" in x for x in
                     _round_issuer_violations(tree, "<round>13</round>\n" + v3,
                                              {13: ["org/missions/D0/X/X_PRJ/task-orders/X_PRJ.TO-0.md"]}))),
        ("round-issuer GREEN: the next round (14), none at HEAD yet -> admitted",
         lambda: _round_issuer_violations(tree, "<round>14</round>\n" + v3,
                                          {13: ["org/missions/D0/X/X_PRJ/task-orders/X_PRJ.TO-0.md"]}) == []),
        ("round-issuer RED: no line-anchored <round>N</round> element -> refused naming the missing key",
         lambda: any("line-anchored" in x and "<round>" in x for x in _round_issuer_violations(tree, v3, {}))),
        ("round-issuer: a flat-root order is NOT graded (the legacy population, same scope as every limb here)",
         lambda: _round_issuer_violations("org/tier2_senior/A/task_orders/X.TO-1.md", "<round>13</round>\n" + v3,
                                          {13: ["org/tier2_senior/A/task_orders/X.TO-0.md"]}) == []),
        ("round-issuer: a prose mention of <round> is inert -- not read as the key, still refused as missing",
         lambda: any("line-anchored" in x for x in
                     _round_issuer_violations(tree, "the `<round>` element names the round\n" + v3, {}))),
        ("round-issuer GREEN: no <round> but a line-anchored <direct_act>true</direct_act> -> admitted (row AMGT_RESAPP-Z-W58-S2)",
         lambda: _round_issuer_violations(tree, "<direct_act>true</direct_act>\n" + v3, {}) == []),
        ("round-issuer RED: a prose mention of <direct_act>true</direct_act> is inert -- still refused as missing",
         lambda: any("line-anchored" in x for x in
                     _round_issuer_violations(tree, "this order sets <direct_act>true</direct_act> nowhere\n" + v3, {}))),
        ("round-issuer RED: <direct_act>false</direct_act> does not exempt -- declares NOT round-less, still refused as missing",
         lambda: any("line-anchored" in x for x in
                     _round_issuer_violations(tree, "<direct_act>false</direct_act>\n" + v3, {}))),
        ("round-issuer RED: <round>13</round> together with <direct_act>true</direct_act> does not exempt -- round collision still enforced (an order cannot claim direct-act to dodge collision review)",
         lambda: any("round 13" in x and "S154" in x for x in
                     _round_issuer_violations(tree, "<direct_act>true</direct_act>\n<round>13</round>\n" + v3,
                                              {13: ["org/missions/D0/X/X_PRJ/task-orders/X_PRJ.TO-0.md"]}))),
        # GATE (xi) -- THE STATUS-ELEMENT LIMB (row AMGT_RESAPP-Z-S153; cell AMGT-rk-56). Pure arms;
        # the real-index battery (a scratch git repo, the gate's own CLI, real committed bytes)
        # lives in .tools/tests/test_gate_xi_status_element.py.
        ("status-element RED: no <status> element at all -> refused naming S153",
         lambda: any("S153" in x and "NO <status> element" in x for x in _status_element_violations(tree, v3))),
        ("status-element RED: a backticked prose mention only -> refused identically to no element",
         lambda: any("S153" in x for x in
                     _status_element_violations(tree, "flip `<status>` to `complete`\n" + v3))),
        ("status-element GREEN: <status>pending</status> on its own line -> admitted",
         lambda: _status_element_violations(tree, "<status>pending</status>\n" + v3) == []),
        ("status-element RED: born <status>complete</status> at issuance -> refused as born terminal",
         lambda: any("born terminal" in x for x in
                     _status_element_violations(tree, "<status>complete</status>\n" + v3))),
        ("status-element: a flat-root order is NOT graded (the legacy population, same scope as every limb here)",
         lambda: _status_element_violations("org/tier2_senior/A/task_orders/X.TO-1.md", v3) == []),
        # GATE (xii) -- the risk class (spine v3.19 L6). One positive per class, the three refusals, and scope.
        ("risk: <risk>LOCAL</risk> on a product-only order -> admitted",
         lambda: _risk_violations(tree, "<risk>LOCAL</risk>\n<paths>\nportal/src/a.tsx\n</paths>\n" + v3) == []),
        ("risk RED: no <risk> element -> refused",
         lambda: any("NO <risk> element" in x for x in _risk_violations(tree, v3))),
        ("risk RED: a prose mention of <risk>LOCAL</risk> is inert -> refused as missing",
         lambda: any("NO <risk> element" in x for x in _risk_violations(tree, "declare <risk>LOCAL</risk> here\n" + v3))),
        ("risk RED: off the enum -> refused",
         lambda: any("off the enum" in x for x in _risk_violations(tree, "<risk>LOW</risk>\n" + v3))),
        ("risk RED: LOCAL on an infra/ path -> below its WORLD floor",
         lambda: any("below its floor WORLD" in x for x in
                     _risk_violations(tree, "<risk>LOCAL</risk>\n<paths>\ninfra/aws/terraform/x/main.tf\n</paths>\n" + v3))),
        ("risk RED: SERVED with a safe-apply invocation -> below its WORLD floor",
         lambda: any("below its floor WORLD" in x for x in _risk_violations(
             tree, "<risk>SERVED</risk>\n" + v3.replace("echo 1", "bash .tools/safe-apply.sh x")))),
        ("risk: WORLD on an infra/ path -> admitted (at the floor)",
         lambda: _risk_violations(tree, "<risk>WORLD</risk>\n<paths>\ninfra/aws/lambda/x.py\n</paths>\n" + v3) == []),
        ("risk: SERVED above a LOCAL floor -> admitted (a class may sit above its floor)",
         lambda: _risk_violations(tree, "<risk>SERVED</risk>\n" + v3) == []),
        ("risk: a flat-root order is NOT graded",
         lambda: _risk_violations("org/tier2_senior/A/task_orders/X.TO-1.md", v3) == []),
        # THE LAST TAG GOVERNS (1.0.0_SA_CTO ruling msg 107528): the complete-flip limb's read.
        ("last-tag: deleting a stale 'pending' above 'complete' is NOT a flip",
         lambda: _is_terminal_flip("<status>pending</status>\n<status>complete</status>\n",
                                   "<status>complete</status>\n") is None),
        ("last-tag: pending -> complete IS a flip",
         lambda: _is_terminal_flip("<status>pending</status>\n", "<status>complete</status>\n") == "complete"),
        ("last-tag: 'complete' then 'pending' reads pending (not terminal), whatever the first tag says",
         lambda: _is_terminal_flip(None, "<status>complete</status>\n<status>pending</status>\n") is None),
        ("last-tag: 'pending' then 'complete' on a new file reads complete (graded)",
         lambda: _is_terminal_flip(None, "<status>pending</status>\n<status>complete</status>\n") == "complete"),
        ("last-tag: a re-edit that keeps the same tags is still graded (only a REMOVED duplicate is exempt)",
         lambda: _is_terminal_flip("<status>complete</status>\n", "<status>complete</status>\nmore\n") == "complete"),
        ("redaction: an account number -> acct#<8hex> on a line is a pure redaction",
         lambda: _is_pure_redaction("<status>complete</status>\nacct 12345678 bal 10\n",
                                    "<status>complete</status>\nacct acct#0a1b2c3d bal 10\n")),
        ("redaction: a removed figure and a deleted line are a pure redaction",
         lambda: _is_pure_redaction("<status>complete</status>\nbalance 1,234.56 ok\nrow 998877 x\n",
                                    "<status>complete</status>\nbalance ok\n")),
        ("redaction: an id -> [redacted] is a pure redaction",
         lambda: _is_pure_redaction("<status>complete</status>\nid 55554444\n", "<status>complete</status>\nid [redacted]\n")),
        ("redaction: an id swap beside an untouched date and ratio is a pure redaction (dell2 msg 3813)",
         lambda: _is_pure_redaction("<status>complete</status>\nacct 12345678 ratio 2.43x on 2026-04-07 row W10-S4\n",
                                    "<status>complete</status>\nacct acct#0a1b2c3d ratio 2.43x on 2026-04-07 row W10-S4\n")),
        ("redaction: an id inside markdown bold with a possessive is a pure redaction (dell2 msg 3813)",
         lambda: _is_pure_redaction("<status>complete</status>\n**12345678**'s value 2.47x\n",
                                    "<status>complete</status>\n**acct#0a1b2c3d**'s value 2.47x\n")),
        ("redaction: a backtick-wrapped id -> backtick-wrapped token is a pure redaction (dell2 msg 3820)",
         lambda: _is_pure_redaction("<status>complete</status>\nsee `12345678` here\n",
                                    "<status>complete</status>\nsee `acct#0a1b2c3d` here\n")),
        ("redaction: an id inside a path (FLOW_RESIDUAL_<id>_R2.json) -> token is a pure redaction (dell2 msg 3820)",
         lambda: _is_pure_redaction("<status>complete</status>\nfile FLOW_RESIDUAL_12345678_R2.json on 2026-10-09\n",
                                    "<status>complete</status>\nfile FLOW_RESIDUAL_acct#0a1b2c3d_R2.json on 2026-10-09\n")),
        ("rename: an account-number filename -> acct#<8hex> filename is a redaction rename (dell2 msg 3850)",
         lambda: _redaction_rename_ok("org/x/task-orders/IRPT_DASHBD.TO-DB-b-6.12345678-tieout.md",
                                      "org/x/task-orders/IRPT_DASHBD.TO-DB-b-6.acct#0a1b2c3d-tieout.md")),
        ("rename: a rename that changes other text is NOT a redaction rename",
         lambda: not _redaction_rename_ok("org/x/task-orders/IRPT_DASHBD.TO-DB-b-6.12345678-tieout.md",
                                          "org/x/task-orders/IRPT_DASHBD.TO-DB-b-7.acct#0a1b2c3d-tieout.md")),
        ("rename: a rename with no acct# token is NOT a redaction rename",
         lambda: not _redaction_rename_ok("org/x/task-orders/A.TO-1.12345678.md", "org/x/task-orders/A.TO-1.redacted.md")),
        ("redaction: a marker standing where a NON-digit word stood is NOT a redaction",
         lambda: not _is_pure_redaction("<status>complete</status>\nresult PASS\n",
                                        "<status>complete</status>\nresult acct#0a1b2c3d\n")),
        ("redaction: an ADDED line is NOT a redaction (graded as a flip)",
         lambda: not _is_pure_redaction("<status>complete</status>\nacct 12345678\n",
                                        "<status>complete</status>\nacct acct#0a1b2c3d\nnew claim\n")),
        ("redaction: a changed word is NOT a redaction",
         lambda: not _is_pure_redaction("<status>complete</status>\nresult PASS 12345678\n",
                                        "<status>complete</status>\nresult FAIL acct#0a1b2c3d\n")),
        ("redaction: a dropped word with no digit is NOT a redaction",
         lambda: not _is_pure_redaction("<status>complete</status>\nnot met 12345678\n",
                                        "<status>complete</status>\nmet acct#0a1b2c3d\n")),
        ("redaction: pending -> complete with a redaction is NOT a pure redaction (the status line changed)",
         lambda: not _is_pure_redaction("<status>pending</status>\nacct 12345678\n",
                                        "<status>complete</status>\nacct acct#0a1b2c3d\n")),
        ("crlf: a CRLF order and its LF twin read the same (placeholders element matches)",
         lambda: _lf("<placeholders>NONE</placeholders>\r\n<status>pending</status>\r\n") == "<placeholders>NONE</placeholders>\n<status>pending</status>\n"
         and PLACEHOLDERS_TAG_RE.search(_lf("<placeholders>NONE</placeholders>\r\n")) is not None),
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
    print("[to-pipeline-gate --self-test] RESULT: %d arm(s) failed of %d" % (failed, len(arms)))
    return 1 if failed else 0


def _issued_by_violations(rel, text):
    """GATE (vii): a NEW tree task order carries a machine-readable <issued_by>.

    ROUTED 2026-09-10 by 2.0.0_SA_COO~ZZ (msg 20981), found by worker 0.9.0_WK_NFRA_REPORT~3 on
    NFRA_REPORT RP-s-23 and filed as that lane's Z-S21: safe-apply, the deploy path the order
    itself MANDATES in NEVER-class terms, was mechanically blocked because
    .tools/halt-gate-check.sh:142-160 halt_gate_worker_issuer() greps the order for the
    <issued_by> tag to admit the worker on a gated verb -- and CONTINUES past an empty match, so
    with no tag anywhere the worker-admission path at :172 cannot resolve an issuer at all.

    WHY THE DEFECT COULD SURVIVE L6: this gate already enforces <decomp_ref>, <issued_to>, the
    <paths> grant, the preflight batteries, cell-id resolution and criterion grammar -- and NOT the
    one field a DOWNSTREAM gate needs. An order could be fully L6-conformant and still unable to
    seat its worker on any gated verb. It surfaced at exactly ONE cell because the missing tag does
    not block ordinary worker action: it blocks the HALTGT checkpoint, and RP-s-23 was the only
    cell in its round calling a gated verb. On a round with no deploy cell it never appears.

    MEASURED BEFORE LANDING, 163 tree task orders: 122 carry the tag, 41 do not, and only FOUR of
    those 41 are NON-TERMINAL -- so this refuses new defects without stranding a live population.
    The convention is settled and wide: 2.0.0_SA_COO~A carries it at line 6 of every NFRA_CLDGRPH
    order, beside <issued_to>. Refusing at AUTHORSHIP stops it being discovered at a deploy.

    THE MARKDOWN SPELLING IS REFUSED ON PURPOSE. 2.0.0_SA_COO~ZZ offered a second shape -- teach
    halt-gate-check to also read a prose Issuer: line. DECLINED: two accepted spellings for one
    machine contract is how a convention drifts, and the estate has already settled on the tag at
    122 of 163. The prose line is NAMED in the refusal instead, because that is the exact mistake
    being made and the author is otherwise looking straight at what they believe is an issuer.
    """
    rel = rel.replace("\\", "/")
    if not TREE_TO_RE.search(rel):
        return []   # flat-root legacy population, out of scope like every other gate in this file
    m = ISSUED_BY_RE.search(text)
    if m and m.group(1).strip():
        return []
    prose = "" if not ISSUER_PROSE_RE.search(text) else (
        " This order DOES carry a human Issuer: line -- that is a RECORD-FACE line and it is "
        "MACHINE-INVISIBLE; the downstream gate greps the tag, never the prose.")
    return ["%s: NEW tree task order carries no non-empty <issued_by>. halt-gate-check.sh's HALTGT "
            "checkpoint resolves the worker's issuer from that tag, so without it the worker CANNOT "
            "BE ADMITTED on a gated verb (safe-apply / safe-deploy) -- including one this order's "
            "own cell mandates.%s Add the <issued_by> tag beside <issued_to>." % (rel, prose)]


def _issued_to_tier_violations(rel, text):
    """GATE (i): complaints about a NEW tree TO's <issued_to>. [] for flat-root TOs (out of scope)."""
    rel = rel.replace("\\", "/")
    if not TREE_TO_RE.search(rel):
        return []
    out = []
    for m in ISSUED_TO_RE.finditer(text):
        raw = m.group(1).strip()
        base = raw.split("~", 1)[0].strip()
        if not SERIAL_RE.match(base):
            continue
        if TIER01_RE.match(base):
            tier = "0" if base.startswith("0.0.") else "1"
            out.append("%s: <issued_to>%s</issued_to> names a TIER-%s seat. L7 workers are TIER-2 ONLY "
                       "(Andrew-direct 2026-09-03, @716a9bc7ce call 3, LD-0521): a Tier-1 exec does not hold a "
                       "task order and 0.0.0_AB_MSTR integrates and never works a project. Re-address to a "
                       "Tier-2 seat, or land the decision as SPEC at its L-owner (L4 CTO / L5 COO)."
                       % (rel, raw, tier))
    return out


def _worker_grant_violations(rel, text):
    """GATE (v): a NEW tree order issued_to a worker carries a non-empty <paths> block -- one path per line, relative to
    the repo root, globs allowed, '#' lines ignored -- because the lane resolver (ADHC_OWNPTH.005) admits the worker to
    exactly those paths and nothing else. Entries that climb ('..') or start at a filesystem root are refused. [] for
    flat-root orders and for orders issued to a seat (a seat's grant is its lanes)."""
    rel = rel.replace("\\", "/")
    if not TREE_TO_RE.search(rel):
        return []
    who = [m.group(1).strip() for m in ISSUED_TO_RE.finditer(text)]
    if not any(WORKER_SERIAL_RE.match(w) for w in who):
        return []
    m = PATHS_BLOCK_RE.search(text)
    if not m:
        return ["%s: issued_to a worker (%s) with NO <paths> block. The order IS the worker's grant (Andrew-direct "
                "2026-09-04 'recs approved' @9ef9a40aae, ADHC_OWNPTH.005): the lane resolver admits the worker to exactly "
                "the paths this block names, so an order without one cannot be executed without the override the ruling "
                "retired. Add <paths>...</paths>: one path per line, relative to the repo root, globs allowed, every file "
                "the worker will write (deliverables/<serial>/ is the tree convention and needs no entry)."
                % (rel, ", ".join(who))]
    entries = [ln.strip().strip("`").strip() for ln in m.group(1).splitlines()]
    entries = [e for e in entries if e and not e.startswith("#")]
    out = []
    if not entries:
        out.append("%s: the <paths> block is EMPTY -- an empty grant. Name every file the worker will write." % rel)
    for e in entries:
        n = e.replace("\\", "/")
        if n.startswith("/") or re.match(r"^[A-Za-z]:", n) or ".." in n.split("/"):
            out.append("%s: <paths> entry %r is not a repo-relative path (no leading /, no drive letter, no '..')." % (rel, e))
    return out


def _placeholder_declaration_violations(rel, text):
    """GATE (viii): a NEW tree order declares the substitution set that arms the invocation-alignment
    limb of .tools/proof-of-spec-check.py on its own issuance. [] for flat-root orders (legacy
    population). See the block comment at PLACEHOLDERS_TAG_RE for the authority and the boundary."""
    rel = rel.replace("\\", "/")
    if not TREE_TO_RE.search(rel):
        return []
    m = PLACEHOLDERS_TAG_RE.search(text)
    if m is None:
        return ["%s: NO <placeholders> element. The invocation-alignment limb of proof-of-spec-check.py "
                "ENFORCES only when the governing TO declares its substitution set; undeclared, it ANNOUNCES "
                "and refuses nothing -- so an issuance without this element arms no check on itself, and the "
                "divergence it exists to catch (a criterion corrected in the SPAWN PROMPT and never in this "
                "file, round 2 row S31) reads VALID. 1.0.0_SA_CTO ruling D: the declaration is MANDATORY at "
                "L6. %s %s" % (rel, PLACEHOLDERS_BOUNDARY, PLACEHOLDERS_HOWTO)]
    names = {n.upper() for n in re.findall(r"[A-Za-z][A-Za-z0-9_]*", m.group(1))}
    if not names:
        return ["%s: the <placeholders> element is EMPTY. An empty element and an intentional "
                "<placeholders>NONE</placeholders> read IDENTICALLY to proof-of-spec-check.py (both ENFORCE "
                "over an empty set), so the empty form cannot be told from an oversight by any reader. "
                "Declare the tokens, or write NONE and mean it. %s" % (rel, PLACEHOLDERS_HOWTO)]
    declared = set(names)
    declared.discard("NONE")
    used = set()
    for i in INVOCATION_TAG_RE.finditer(text):
        used |= set(PLACEHOLDER_TOKEN_RE.findall(i.group(1)))
    missing = sorted(used - declared)
    if missing:
        return ["%s: <placeholders> declares {%s} but this order's own <invocation> strings carry %s, which "
                "it does not declare. An UNDECLARED token is NOT expanded under ENFORCE -- it stays literal, "
                "so every recorded run of that criterion will diverge from the criterion and the worker "
                "cannot fix it (editing the issuance half to make its own proof validate is refused). "
                "Declare every token the invocations carry. %s"
                % (rel, ", ".join(sorted(declared)) or "nothing",
                   ", ".join("<%s>" % t for t in missing), PLACEHOLDERS_HOWTO)]
    return []


def _placeholder_modify_violations(rel, head_text, staged_text):
    """GATE (viii) ON A MODIFY (FE-s-29 limb 4; Andrew-direct card 6, record @e2210bf34c). PURE.

    `head_text` is the order as committed at HEAD, `staged_text` as staged. [] when the order is not a
    tree order, or when it does NOT ALREADY DECLARE <placeholders> at HEAD -- a modify of an undeclared
    order is never graded, so nothing is back-filled. Otherwise the STAGED bytes are graded exactly as a
    newly-added order's are: an amendment that deletes, empties or under-declares the element of an order
    that armed the checker is refused, naming that it is a MODIFY of a declaring order."""
    rel = rel.replace("\\", "/")
    if not TREE_TO_RE.search(rel) or head_text is None or PLACEHOLDERS_TAG_RE.search(head_text) is None:
        return []
    if staged_text is None:
        return ["%s: staged as MODIFIED and ALREADY DECLARES <placeholders> at HEAD, but its staged bytes are "
                "unreadable -- refusing; a gate that cannot read its subject must not pass it" % rel]
    return ["%s [MODIFIED; the order already declares <placeholders> at HEAD, so GATE (viii) grades the "
            "amendment -- Andrew-direct card 6, record @e2210bf34c]: %s" % (rel, x.split(": ", 1)[-1])
            for x in _placeholder_declaration_violations(rel, staged_text)]


# GATE (xi) -- THE STATUS-ELEMENT LIMB, ON NEWLY-ADDED TREE ORDERS ONLY (row AMGT_RESAPP-Z-S153,
# surfaced by 4.0.0_SA_CRO~Z 2026-09-17; ROUND_ANALYSIS.round13.md s.4 row R14-T2; cell AMGT-rk-56).
# MEASURED: all 15 round-13 task orders (AMGT-rk-19..rk-30) were born with NO <status> element at
# all, while each worker face's closing step tells the worker to flip <status> to complete, and
# to-check.py lists all 15 as '??'. Round-12 orders carried the element from their adding commit.
# No limb of check_file() reads the record face's status -- this is that limb.
#
# LINE-ANCHORED, the same discipline as PLACEHOLDERS_TAG_RE and ROUND_ELEMENT_RE above, and for the
# identical reason: a backticked prose mention of the tag ("flip `<status>` to `complete`") must
# read IDENTICALLY to an order with no element at all, never as the element -- the Z-S15 / to-check
# FIX C class every downstream status reader (to-check.py:113-122, surprise-row-gate.py:1125-1165,
# owned-paths-validate.py:125-140) already learned the hard way.
#
# TERMINAL AT ISSUANCE IS ALSO REFUSED. An order is issued OPEN; the word must not be one either
# sibling gate treats as terminal -- DONE_WORDS below (this file: complete, completed, closed,
# done) UNION surprise-row-gate.py:152 TERMINAL_TO_WORDS (adds superseded, cancelled, canceled,
# withdrawn) -- READ AS ONE SET. Mirrored here, not imported: these are two standalone CLI tools
# with no import path between them, the same shape as PLACEHOLDERS_TAG_RE's cross-tool mirror
# above; the next edit to either terminal-word tuple must move both.
#
# SCOPE. [] for flat-root orders (the legacy population, same scope as every limb in this file). A
# MODIFY is never graded by this limb: main() sends only the NEWLY-ADDED (git A/R) set through
# check_file(), exactly as GATE (viii)'s newly-added half does -- a worker adding the element at
# close to a legacy untagged order is a MODIFICATION and is admitted, as S153's own world_is
# anticipates. NO BACK-FILL: the 3 untagged orders already at HEAD at the cut
# (rk-20.price-generation-contract, rk-23.artifact-name-encoding, rk-30.scores-adapter-model-tab)
# are prospective-only and are not touched by this limb or any other (the gate's own doctrine,
# :1757-1762 above).
STATUS_ELEMENT_RE = re.compile(r"^[ \t]*<status>\s*([A-Za-z_-]+)\s*</status>[ \t]*$", re.M)
GATE_XI_TERMINAL_WORDS = ("complete", "completed", "closed", "done",
                          "superseded", "cancelled", "canceled", "withdrawn", "not_met")


def _status_element_violations(rel, text):
    """GATE (xi): PURE, no I/O. [] for flat-root orders. A NEWLY-ADDED tree task order must carry a
    LINE-ANCHORED <status>WORD</status> element (STATUS_ELEMENT_RE) -- missing, or present only as
    a prose mention that does not match the anchored regex, is refused naming row
    AMGT_RESAPP-Z-S153. Present but carrying a word in GATE_XI_TERMINAL_WORDS is refused as "born
    terminal" -- an order is issued open, and a terminal word belongs to the worker's close."""
    rel = rel.replace("\\", "/")
    if not TREE_TO_RE.search(rel):
        return []
    m = STATUS_ELEMENT_RE.search(text or "")
    if m is None:
        return ["%s: a NEW tree task order carries NO <status> element on its own line -- issue it "
                "with <status>pending</status> in the record face; the worker flips it at close and "
                "every status reader keys on it (row AMGT_RESAPP-Z-S153: 15 of 15 round-13 orders "
                "were born untagged)." % rel]
    word = m.group(1).lower()
    if word in GATE_XI_TERMINAL_WORDS:
        return ["%s: born terminal -- <status>%s</status> at issuance. An order is issued OPEN; a "
                "terminal word belongs to the worker's close, not the issuance (row "
                "AMGT_RESAPP-Z-S153)." % (rel, m.group(1))]
    return []


# GATE (xii) -- THE RISK CLASS (spine v3.19 L6; report 3 wave 2, Andrew-approved 2026-09-24, record
# org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260924_154xZ_REPORT3_REFINEMENTS_APPROVED_BOTH_REPORTS_TO_CTO.md).
# A NEWLY-ADDED tree order carries a line-anchored <risk>LOCAL|SERVED|WORLD</risk>; the class decides which limbs
# engage (LOCAL: proof + checker + the COO's real run; SERVED adds the CVO's judgment grade; WORLD adds the CTO's
# exercised read and the change-management entry). The floor is inferred: a <paths> entry under infra/ or an
# invocation carrying a deploy verb is WORLD, and a declared class below it is refused. Newly-added only, like (xi).
RISK_ELEMENT_RE = re.compile(r"^\s*<risk>\s*([A-Za-z]+)\s*</risk>", re.I | re.M)
RISK_ORDER = ("LOCAL", "SERVED", "WORLD")
RISK_DEPLOY_VERB_RE = re.compile(
    r"\b(safe-apply|terraform\s+apply|safe-deploy|safe-ec2-deploy|aws\s+lambda\s+update-function|"
    r"aws\s+s3\s+(?:cp|sync|mv|rm)\b[^\n<]*s3://|git\s+push|prod-deploy)\b", re.I)


def _risk_floor(text):
    """(floor, reason) from the order's own <paths> and invocations -- PURE."""
    blk = re.search(r"^<paths>\s*$(.*?)^</paths>", text or "", re.M | re.S)
    for ln in (blk.group(1).splitlines() if blk else []):
        p = ln.strip().lstrip("-").strip().strip("`").replace("\\", "/")
        if p.startswith("infra/"):
            return "WORLD", "<paths> names %s (an infrastructure path)" % p
    for inv in re.findall(r"<invocation>(.*?)</invocation>", text or "", re.S):
        m = RISK_DEPLOY_VERB_RE.search(inv)
        if m:
            return "WORLD", "an invocation carries the deploy verb %r" % m.group(1)
    return "LOCAL", "no infrastructure path and no deploy verb"


def _risk_violations(rel, text):
    """GATE (xii): PURE, no I/O. [] for flat-root orders."""
    rel = rel.replace("\\", "/")
    if not TREE_TO_RE.search(rel):
        return []
    m = RISK_ELEMENT_RE.search(text or "")
    if m is None:
        return ["%s: a NEW tree task order carries NO <risk> element on its own line -- declare "
                "<risk>LOCAL</risk>, <risk>SERVED</risk> or <risk>WORLD</risk> in the record face (spine v3.19 L6: "
                "the class decides which limbs engage)." % rel]
    word = m.group(1).upper()
    if word not in RISK_ORDER:
        return ["%s: <risk>%s</risk> is off the enum (LOCAL, SERVED, WORLD)." % (rel, m.group(1))]
    floor, why = _risk_floor(text)
    if RISK_ORDER.index(word) < RISK_ORDER.index(floor):
        return ["%s: <risk>%s</risk> is below its floor %s -- %s (spine v3.19 L6: a declared class below the "
                "inferred floor is refused; declare %s)." % (rel, word, floor, why, floor)]
    return []


# GATE (ix) -- THE OUTPUT-VOCABULARY LIMB: A BAR ITS TOOL CAN NEVER PRINT IS REFUSED AT THE CUT (FE-s-36;
# 1.0.0_SA_CTO ruling N; row S55). Built 2026-09-13 by 0.9.0_WK_IRPT_FNTEND~4 on IRPT_FNTEND.TO-FE-s-36.
#
# THE SHAPE. F28-AC6 as issued (@b6062ad2a2) expected `0 fail` from .tools/tests/test_proof_of_spec_alignment.py,
# which prints only `BATTERY PASS` or `BATTERY FAILED` (:458-460) and `N/M arms as expected`. `0 fail` is a TEST
# RUNNER's summary word (bun prints ` 0 fail`); the battery never authors it, so the criterion could never pass and
# nothing said so until a worker ran it. Round 4 cut five criteria against an assumption about a tool's output and a
# worker's refusal caught every one (S55). This limb reads the tool at the cut and refuses that shape.
#
# WHAT IT READS -- and nothing else:
#   1. the criterion's <invocation>. It is EVALUATED only when it is ONE program: optional leading `cd <WS>` or
#      `cd <WS>/<sub>`, optional `timeout N` and VAR=value prefixes, then `python|python3|py <path>.py [args]`.
#      A pipe, a list (`;`, `||`, a second `&&` command), a redirect or a substitution means the evidence is not one
#      program's output -> NOT EVALUATED. Any other program (bun, pytest, node, npm, a comp-tool, a shell script) is a
#      RUNNER whose vocabulary this limb does not model -> NOT EVALUATED, and never refused.
#   2. the named .py file FROM THE INDEX (`git show :<path>`) -- what exists AT THE CUT. Absent there (the ordinary
#      case: the worker writes the test) -> ANNOUNCED, never refused. It never runs the file, and never runs a test.
#   3. the file's AUTHORED TEXT, by `ast`: every string literal, every f-string, %-format and .format() template, and
#      every print() argument list joined by its separator. A field is resolved when the file binds it only to
#      authored strings (a constant, a conditional of constants, a name assigned only such values); otherwise it is a
#      FIELD that may carry any text. Digits in a template and any field are NUMBER SLOTS.
#   4. the <expect> bar, parsed as the regex it is (the checker grades it with an unanchored search): its literal runs,
#      with every digit run, \d class and digit back-reference as a NUMBER SLOT. Lookarounds and anchors are dropped
#      (only ever loosening). An alternation, or a bar with no two-letter word, cannot be reduced -> ANNOUNCED.
#
# THE DECISION, per literal run of the bar:
#   ADMITTED   some ONE template authors the run: every letter of it is authored text, counts on number slots.
#   ANNOUNCED  no template authors it whole, but one authors at least one WORD of it in place while a field could
#              carry the rest (a label held in a variable) -- the limb cannot tell, says so, and refuses nothing.
#   REFUSED    no template authors even one word of the run in place -- the bar's words never appear, in that
#              arrangement, in any line the tool can write. That is F28-AC6: `fail` is authored in the battery (an arm
#              is named `fail-closed: ...`) but never after a number, and `0 fail` needs a count before it.
#
# WHAT IT CANNOT KNOW, STATED RATHER THAN GUESSED (each is an ANNOUNCE or a stated assumption, never a silent pass):
#   - a tool whose output is not its own: it prints nothing itself, prints a bare value (`print(out)`), runs a
#     program other than git (sys.executable, bun, a shell), or hands off to a runner or another module's main()
#     (unittest.main, pytest.main, runpy, exec, X.main()) -> the file is OPEN -> ANNOUNCED.
#   - ASSUMPTION A (stated): a tool's verdict vocabulary is the text it AUTHORS. Text it relays INSIDE an authored
#     line (a diagnostic after `<-`) is not credited with a bar's words, and a module it imports as a library is not
#     read (the limb builds no call graph). A bar that could only ever match relayed text is refused -- it would pass
#     on a diagnostic, which is its own defect.
#   - ASSUMPTION B (stated): a bar line is written by ONE template -- with ONE modelled exception. A call that leaves
#     its line open (print(..., end="") or a write()) is read as continuing into ANY later call, and in such a
#     file any line may begin mid-way: that only ever loosens. MEASURED before landing, over all 359 tracked tree
#     orders: NFRA_CLDGRPH F5-AC1 prints `UNREACHABLE_REFUSAL_NAMES=` with end="" and its value on the next
#     print; without the exception it was the one honest bar refused. A word spliced from fragments at run time
#     is still not credited.
#   - it cannot see an interpreter traceback, argparse usage text, or `timeout`'s own output; none is a verdict.
#
# BOUNDARY: the scope this gate already owns -- a tree order STAGED AS ADDED (git A/R), mechanical criteria only
# (judgment="true" is graded at L9). It never grades a MODIFICATION and never grades an existing order.
OV_TAG = "OUTPUT-VOCABULARY"
_OV_FIELD = "\x00"      # a template field: any text
_OV_DIGIT = "\x01"      # a digit run authored in a template
_OV_SLOT = "\x02"       # a number slot in a bar
_OV_PYTHONS = ("python", "python3", "py", "python.exe", "python3.exe", "py.exe")
_OV_MAX_ALTS = 32
_OV_WORD_RE = re.compile(r"[A-Za-z]+")
_OV_CACHE = {}


def _ov_program(invocation):
    """(kind, rel, args, why). kind: 'PY' (evaluable: rel is the repo-relative .py path), 'RUNNER' (another program;
    never evaluated) or 'OTHER' (not one program's output, or a path outside the workspace; never evaluated)."""
    inv = (invocation or "").strip()
    probe = PLACEHOLDER_TOKEN_RE.sub("PH", inv)
    if (re.search(r"\$\(|`|[<>]|\|\||;|\n", probe) or re.search(r"(?<!&)&(?!&)", probe)
            or re.search(r"(?<!\|)\|(?!\|)", probe)):
        return "OTHER", None, "", ("a compound shell line (a pipe, a list, a redirect or a substitution): its output "
                                   "is not one program's")
    segs = [s.strip() for s in inv.split("&&") if s.strip()]
    cwd = ""
    while segs and re.match(r"^cd\s", segs[0]):
        tgt = segs[0][2:].strip().strip("'\"")
        if tgt in ("<WS>", "<WS>/", ".", "./"):
            cwd = ""
        elif tgt.startswith("<WS>/") and not PLACEHOLDER_TOKEN_RE.search(tgt[5:]) and ".." not in tgt.split("/"):
            cwd = tgt[5:].strip("/")
        else:
            return "OTHER", None, "", "it changes into %s, which is not the workspace root or a directory under <WS>" % tgt
        segs = segs[1:]
    if len(segs) != 1:
        return "OTHER", None, "", "it runs %d commands after its cd, so its output is not one program's" % len(segs)
    try:
        tok = shlex.split(segs[0], posix=True)
    except ValueError as exc:
        return "OTHER", None, "", "its command does not tokenise (%s)" % exc
    while tok and re.match(r"^[A-Za-z_][A-Za-z0-9_]*=", tok[0]):
        tok = tok[1:]
    if tok and tok[0] == "timeout":
        tok = tok[1:]
        while tok and tok[0].startswith("-"):
            tok = tok[2:] if tok[0] in ("-s", "-k") else tok[1:]
        if tok and re.match(r"^\d+(\.\d+)?[smhd]?$", tok[0]):
            tok = tok[1:]
    if not tok:
        return "OTHER", None, "", "no program after its prefixes"
    base = tok[0].replace("\\", "/").rsplit("/", 1)[-1].lower()
    if base not in _OV_PYTHONS:
        return "RUNNER", None, "", "the program is %s, a runner whose own vocabulary this limb does not model" % tok[0]
    if len(tok) < 2 or tok[1].startswith("-") or not tok[1].endswith(".py"):
        return "OTHER", None, "", "python is not invoked on a .py file directly (a flag, -m or -c)"
    script = tok[1]
    if script.startswith("<WS>/"):
        script = script[5:]
    if PLACEHOLDER_TOKEN_RE.search(script) or script.startswith("/") or re.match(r"^[A-Za-z]:", script):
        return "OTHER", None, "", "the script path %s is not relative to the workspace" % tok[1]
    rel = posixpath.normpath(posixpath.join(cwd, script)) if cwd else posixpath.normpath(script)
    if rel.startswith(".."):
        return "OTHER", None, "", "the script path climbs out of the workspace"
    return "PY", rel, " ".join(tok[2:]), ""


def _ov_bar_runs(expect):
    """(runs, icase, why). runs: the bar's literal runs that carry a two-letter word, digits as _OV_SLOT; None + why
    when the bar cannot be reduced to required text."""
    try:
        import re._parser as _sp  # noqa: PLC0415 -- Python 3.11+
    except ImportError:  # pragma: no cover
        import sre_parse as _sp  # noqa: PLC0415
    try:
        parsed = _sp.parse(expect)
    except Exception as exc:  # noqa: BLE001
        return None, False, "the bar does not compile as a regex (%s)" % exc
    icase = bool(parsed.state.flags & re.I)
    runs, dgroups, bad = [[]], set(), []

    def brk():
        if runs[-1]:
            runs.append([])

    def slot():
        if not (runs[-1] and runs[-1][-1] == _OV_SLOT):
            runs[-1].append(_OV_SLOT)

    def is_digit_in(av):
        return bool(av) and all((o == _sp.CATEGORY and a == _sp.CATEGORY_DIGIT) or (o == _sp.RANGE and a == (48, 57))
                                for o, a in av)

    def is_digit_node(items):
        items = list(items)
        if len(items) != 1:
            return False
        o, a = items[0]
        if o == _sp.IN:
            return is_digit_in(a)
        if o in (_sp.MAX_REPEAT, _sp.MIN_REPEAT):
            return a[0] >= 1 and is_digit_node(a[2])
        return False

    def walk(items):
        for op, av in items:
            if op == _sp.LITERAL:
                runs[-1].append(chr(av))
            elif op == _sp.IN and is_digit_in(av):
                slot()
            elif op in (_sp.MAX_REPEAT, _sp.MIN_REPEAT):
                if av[0] >= 1 and is_digit_node(av[2]):
                    slot()
                else:
                    brk()
            elif op == _sp.SUBPATTERN:
                group, add_f, _del_f, sub = av
                if add_f & re.I:
                    bad.append("a group carries its own (?i) flag")
                if group is not None and is_digit_node(sub):
                    dgroups.add(group)
                walk(sub)
            elif op == _sp.GROUPREF:
                if av in dgroups:
                    slot()
                else:
                    brk()
            elif op in (_sp.ASSERT, _sp.ASSERT_NOT, _sp.AT):
                pass
            elif op == _sp.BRANCH:
                bad.append("the bar has alternatives")
            else:
                brk()
    walk(parsed)
    if bad:
        return None, icase, bad[0]
    out = []
    for r in runs:
        s = re.sub(r"[0-9]+", _OV_SLOT, "".join(r))
        s = re.sub(_OV_SLOT + "+", _OV_SLOT, s)
        if any(len(w) >= 2 for w in _OV_WORD_RE.findall(s)):
            out.append(s)
    if not out:
        return None, icase, ("no literal run of the bar carries a two-letter word, so any tool printing a number "
                             "could satisfy it")
    return out, icase, ""


def _ov_norm(s):
    """A template skeleton: authored digit runs become _OV_DIGIT, adjacent fields collapse to one."""
    s = re.sub(r"[0-9]+", _OV_DIGIT, s)
    return re.sub(_OV_FIELD + "+", _OV_FIELD, s)


def _ov_product(parts):
    """Concatenate lists of alternatives. A part that would push the product past the cap becomes ONE field -- it
    keeps every other part's authored text (collapsing the whole template would hide authored words)."""
    acc = [""]
    for alts in parts:
        alts = alts or [_OV_FIELD]
        if len(acc) * len(alts) > _OV_MAX_ALTS:
            alts = [_OV_FIELD]
        acc = [a + b for a in acc for b in alts]
    return list(dict.fromkeys(acc))


_OV_PCT_RE = re.compile(r"%(\([^)]*\))?([#0\- +]*)(\*|\d+)?(?:\.(\*|\d+))?[hlL]?([diouxXeEfFgGcrsa%])")
_OV_NUM_SPEC = "bcdeEfFgGnoxX%,_"


class _OvSource:
    """The authored text of ONE python file: name bindings, and the alternatives an expression can print."""

    def __init__(self, tree):
        self.binds, self.augs = {}, {}
        for node in ast.walk(tree):
            if isinstance(node, ast.Assign):
                for t in node.targets:
                    self._bind(t, node.value)
            elif isinstance(node, ast.AnnAssign):
                self._bind(node.target, node.value)
            elif isinstance(node, ast.NamedExpr):
                self._bind(node.target, node.value)
            elif isinstance(node, ast.AugAssign):
                if isinstance(node.target, ast.Name) and isinstance(node.op, ast.Add):
                    self.augs.setdefault(node.target.id, []).append(node.value)
                else:
                    self._unbind(node.target)
            elif isinstance(node, (ast.For, ast.AsyncFor, ast.comprehension)):
                self._unbind(node.target)
            elif isinstance(node, ast.withitem) and node.optional_vars is not None:
                self._unbind(node.optional_vars)
            elif isinstance(node, ast.arg):
                self.binds.setdefault(node.arg, []).append(None)
            elif isinstance(node, ast.ExceptHandler) and node.name:
                self.binds.setdefault(node.name, []).append(None)
            elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                self.binds.setdefault(node.name, []).append(None)
            elif isinstance(node, (ast.Import, ast.ImportFrom)):
                for a in node.names:
                    self.binds.setdefault((a.asname or a.name).split(".")[0], []).append(None)

    def _bind(self, tgt, val):
        if val is None:
            self._unbind(tgt)
        elif isinstance(tgt, ast.Name):
            self.binds.setdefault(tgt.id, []).append(val)
        elif (isinstance(tgt, (ast.Tuple, ast.List)) and isinstance(val, (ast.Tuple, ast.List))
              and len(tgt.elts) == len(val.elts) and not any(isinstance(e, ast.Starred) for e in tgt.elts + val.elts)):
            for t, v in zip(tgt.elts, val.elts):
                self._bind(t, v)
        else:
            self._unbind(tgt)

    def _unbind(self, tgt):
        for n in ast.walk(tgt):
            if isinstance(n, ast.Name):
                self.binds.setdefault(n.id, []).append(None)

    def alts(self, node, depth=0, seen=frozenset()):
        """What `node` can print, as alternative skeleton strings; [_OV_FIELD] when the file does not author it."""
        F = [_OV_FIELD]
        if node is None or depth > 6:
            return F
        if isinstance(node, ast.Constant):
            v = node.value
            if isinstance(v, str):
                return [v]
            if isinstance(v, bool) or v is None:
                return [str(v)]
            if isinstance(v, (int, float)):
                return [_OV_DIGIT]
            return F
        if isinstance(node, ast.JoinedStr):
            parts = []
            for p in node.values:
                if isinstance(p, ast.Constant):
                    parts.append([str(p.value)])
                elif isinstance(p, ast.FormattedValue):
                    parts.append(self._formatted(p, depth, seen))
                else:
                    parts.append(F)
            return _ov_product(parts)
        if isinstance(node, ast.BinOp):
            if isinstance(node.op, ast.Add):
                return _ov_product([self.alts(node.left, depth + 1, seen), self.alts(node.right, depth + 1, seen)])
            if isinstance(node.op, ast.Mod):
                args = node.right.elts if isinstance(node.right, ast.Tuple) else [node.right]
                out = []
                for left in self.alts(node.left, depth + 1, seen):
                    out.extend(self._percent(left, args, depth, seen))
                return list(dict.fromkeys(out))[:_OV_MAX_ALTS] or F
            return F
        if isinstance(node, ast.IfExp):
            return list(dict.fromkeys(self.alts(node.body, depth + 1, seen) + self.alts(node.orelse, depth + 1, seen)))
        if isinstance(node, ast.BoolOp):
            out = []
            for v in node.values:
                out.extend(self.alts(v, depth + 1, seen))
            return list(dict.fromkeys(out))[:_OV_MAX_ALTS]
        if isinstance(node, ast.Name):
            bs = self.binds.get(node.id)
            if node.id in seen or not bs or any(b is None for b in bs):
                return F
            inner = seen | {node.id}
            base = []
            for b in bs:
                base.extend(self.alts(b, depth + 1, inner))
            for a in self.augs.get(node.id, []):
                base = base + _ov_product([base, self.alts(a, depth + 1, inner)])
            base = list(dict.fromkeys(base))
            return base if len(base) <= _OV_MAX_ALTS else F
        if isinstance(node, ast.Call):
            f = node.func
            if isinstance(f, ast.Attribute):
                if f.attr == "format":
                    return [re.sub(r"\{[^{}]*\}", _OV_FIELD, s.replace("{{", "\x03").replace("}}", "\x04"))
                            .replace("\x03", "{").replace("\x04", "}") for s in self.alts(f.value, depth + 1, seen)]
                if f.attr in ("upper", "lower", "title", "capitalize", "casefold", "swapcase"):
                    return [getattr(s, f.attr)() for s in self.alts(f.value, depth + 1, seen)]
                if f.attr in ("strip", "lstrip", "rstrip"):
                    return self.alts(f.value, depth + 1, seen)
                if f.attr in ("ljust", "rjust", "center", "zfill"):
                    return _ov_product([F, self.alts(f.value, depth + 1, seen), F])
            if isinstance(f, ast.Name) and f.id == "str" and len(node.args) == 1:
                return self.alts(node.args[0], depth + 1, seen)
            if isinstance(f, ast.Name) and f.id in ("len", "int", "sum", "max", "min", "round", "float", "abs"):
                return [_OV_DIGIT]
            return F
        return F

    def _formatted(self, p, depth, seen):
        spec = ""
        if p.format_spec is not None:
            if not all(isinstance(v, ast.Constant) for v in p.format_spec.values):
                return [_OV_FIELD]
            spec = "".join(str(v.value) for v in p.format_spec.values)
        if spec and spec[-1] in _OV_NUM_SPEC:
            return [_OV_DIGIT]
        base = self.alts(p.value, depth + 1, seen)
        if spec or p.conversion in (ord("r"), ord("a")):
            return _ov_product([[_OV_FIELD], base, [_OV_FIELD]])
        return base

    def _percent(self, left, args, depth, seen):
        parts, i, pos = [], 0, 0
        for m in _OV_PCT_RE.finditer(left):
            parts.append([left[pos:m.start()]])
            pos = m.end()
            key, _flags, width, prec, conv = m.groups()
            if conv == "%":
                parts.append(["%"])
                continue
            i += (width == "*") + (prec == "*")
            if key is not None or i >= len(args):
                parts.append([_OV_FIELD])
            elif conv in "diouxXeEfFgG":
                parts.append([_OV_DIGIT])
            else:
                a = self.alts(args[i], depth + 1, seen)
                parts.append(_ov_product([[_OV_FIELD], a, [_OV_FIELD]]) if (width or conv in "ra") else a)
            i += 1
        parts.append([left[pos:]])
        return _ov_product(parts)


def _ov_dotted(f):
    if isinstance(f, ast.Name):
        return f.id
    if isinstance(f, ast.Attribute):
        head = _ov_dotted(f.value)
        return (head + "." + f.attr) if head else "?." + f.attr
    return ""


_OV_HANDOFF = ("unittest.main", "pytest.main", "doctest.testmod", "doctest.testfile", "runpy.run_path",
               "runpy.run_module", "exec", "os.system", "os.popen", "pty.spawn", "subprocess.getoutput",
               "subprocess.getstatusoutput")
_OV_SUBPROC = ("run", "call", "check_call", "check_output", "Popen")


def _ov_templates(src):
    """(templates, open_why) for one python source. Raises SyntaxError when it does not parse."""
    tree = ast.parse(src)
    s = _OvSource(tree)
    sub_names = {a.asname or a.name for n in ast.walk(tree) if isinstance(n, ast.ImportFrom) and n.module == "subprocess"
                 for a in n.names}
    tmpls, open_why, n_print, continued, line_tmpls = set(), "", 0, False, []
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            v = node.value
            tmpls.update({v, _OV_PCT_RE.sub(_OV_FIELD, v), re.sub(r"\{[^{}]*\}", _OV_FIELD, v)})
        elif isinstance(node, (ast.JoinedStr, ast.BinOp)):
            tmpls.update(s.alts(node))
        elif isinstance(node, ast.Call):
            d = _ov_dotted(node.func)
            if d == "print" or d.endswith(("stdout.write", "stderr.write")):
                n_print += 1
                sep = [" "]
                for kw in node.keywords:
                    if kw.arg == "sep":
                        sep = s.alts(kw.value)
                if any(isinstance(a, ast.Starred) for a in node.args):
                    open_why = open_why or "it prints an unpacked sequence at line %d (a relay)" % node.lineno
                    continue
                arg_alts = [s.alts(a) for a in node.args]
                if node.args and all(x == [_OV_FIELD] for x in arg_alts):
                    open_why = open_why or ("it prints a bare value it does not author at line %d (a relay: that "
                                            "line can be anything)" % node.lineno)
                parts = []
                for k, x in enumerate(arg_alts):
                    if k:
                        parts.append(sep)
                    parts.append(x)
                end = ["\n"]
                for kw in node.keywords:
                    if kw.arg == "end":
                        end = s.alts(kw.value)
                if d != "print" or any("\n" not in e for e in end):
                    parts.append([_OV_FIELD])   # the line goes on in a later call (ASSUMPTION B's modelled case)
                    continued = True
                made = _ov_product(parts)
                line_tmpls.extend(made)
                tmpls.update(made)
            elif isinstance(node.func, ast.Attribute) and node.func.attr == "format":
                tmpls.update(s.alts(node))
            elif d in _OV_HANDOFF or d.startswith("os.exec") or d.startswith("os.spawn"):
                open_why = open_why or "it hands its output to %s at line %d" % (d, node.lineno)
            elif (d.startswith("subprocess.") and d.split(".", 1)[1] in _OV_SUBPROC) or d in sub_names:
                a0 = node.args[0] if node.args else None
                prog = (a0.elts[0].value if isinstance(a0, (ast.List, ast.Tuple)) and a0.elts
                        and isinstance(a0.elts[0], ast.Constant) and isinstance(a0.elts[0].value, str) else None)
                if prog is None or prog.replace("\\", "/").rsplit("/", 1)[-1] not in ("git", "git.exe"):
                    open_why = open_why or ("it runs %s at line %d, and that program's output may reach its own"
                                            % (prog or "a program it does not name literally", node.lineno))
            elif isinstance(node.func, ast.Attribute) and node.func.attr == "main" and not (
                    isinstance(node.func.value, ast.Name) and node.func.value.id == "self"):
                open_why = open_why or "it hands off to %s() at line %d" % (d, node.lineno)
    if continued:   # a line may also BEGIN mid-way, after a call that left its line open
        tmpls.update(_OV_FIELD + t for t in line_tmpls)
    if n_print == 0:
        open_why = open_why or "it prints nothing itself, so its output is produced elsewhere"
    return sorted({_ov_norm(t) for t in tmpls if _OV_WORD_RE.search(t)}), open_why


def _ov_masks(run):
    m = {}
    for i, c in enumerate(run):
        m[c] = m.get(c, 0) | (1 << i)
    return m


def _ov_produce(run, tmpl, at, forward=True):
    """Can `run` be written by `tmpl` contiguously, starting exactly at `at` (forward) or ending exactly at `at`
    (backward)? A field carries anything; a number slot needs an authored digit run or a field. The template's own
    ends are CLOSED (ASSUMPTION B): the run may not continue past them."""
    if not run:
        return True
    if forward:
        seq = tmpl[at:]
    else:
        run, seq = run[::-1], tmpl[:at][::-1]
    n, mk = len(run), _ov_masks(run)
    full, goal, slot, m = (1 << (n + 1)) - 1, 1 << n, mk.get(_OV_SLOT, 0), 1
    for c in seq:
        if c == _OV_FIELD:
            m = full & ~((m & -m) - 1)
        elif c == _OV_DIGIT:
            m = (m & slot) << 1
        else:
            m = (m & mk.get(c, 0)) << 1
        if m & goal:
            return True
        if not m:
            return False
    return False


def _ov_clean(run, tmpl):
    """ADMITTED shape: `tmpl` writes `run` with EVERY letter authored; fields carry only counts and punctuation."""
    n, mk = len(run), _ov_masks(run)
    goal, slot = 1 << n, mk.get(_OV_SLOT, 0)
    cf = []
    for r in range(n + 1):
        fl = next((j for j in range(r, n) if run[j].isalpha()), n)
        cf.append(((1 << (fl + 1)) - 1) & ~((1 << r) - 1))
    m = 0
    for c in tmpl:
        m |= 1
        if c == _OV_FIELD:
            out, x = 0, m
            while x:
                low = x & -x
                out |= cf[low.bit_length() - 1]
                x ^= low
            m = out
        elif c == _OV_DIGIT:
            m = (m & slot) << 1
        else:
            m = (m & mk.get(c, 0)) << 1
        if m & goal:
            return True
    return False


def _ov_anchored(run, tmpl):
    """UNDECIDED shape: `tmpl` authors at least one WORD (two letters or more) of `run` in place, and fields could
    carry the rest."""
    for w in _OV_WORD_RE.finditer(run):
        if len(w.group(0)) < 2:
            continue
        a = tmpl.find(w.group(0))
        while a != -1:
            if (_ov_produce(run[:w.start()], tmpl, a, forward=False)
                    and _ov_produce(run[w.end():], tmpl, a + len(w.group(0)))):
                return True
            a = tmpl.find(w.group(0), a + 1)
    return False


def _ov_judge(runs, icase, tmpls):
    """[(run, 'ADMITTED'|'UNDECIDED'|'REFUSED')] over the tool's templates."""
    T = [t.lower() for t in tmpls] if icase else list(tmpls)
    out = []
    for r in runs:
        rr = r.lower() if icase else r
        words = _OV_WORD_RE.findall(rr)
        verdict = "REFUSED"
        if any(all(w in t for w in words) and _ov_clean(rr, t) for t in T):
            verdict = "ADMITTED"
        elif any(_ov_anchored(rr, t) for t in T):
            verdict = "UNDECIDED"
        out.append((r, verdict))
    return out


def _ov_show(s):
    return s.replace(_OV_SLOT, "<n>").replace(_OV_DIGIT, "<n>").replace(_OV_FIELD, "{...}")


def _ov_tool(root, rel):
    """(templates, open_why, err) for the file at `rel` IN THE INDEX -- what exists at the cut. err 'ABSENT' when the
    index does not carry it; cached per process."""
    key = (root, rel)
    if key not in _OV_CACHE:
        try:
            out = subprocess.run(["git", "show", ":" + rel], cwd=root, capture_output=True, timeout=30)
        except Exception as exc:  # noqa: BLE001
            _OV_CACHE[key] = (None, "", "the index could not be read (%s)" % exc)
        else:
            if out.returncode != 0:
                _OV_CACHE[key] = (None, "", "ABSENT")
            else:
                try:
                    t, why = _ov_templates(out.stdout.decode("utf-8", errors="replace"))
                    _OV_CACHE[key] = (t, why, "")
                except (SyntaxError, ValueError, RecursionError) as exc:
                    _OV_CACHE[key] = (None, "", "it does not parse as python (%s)" % exc)
    return _OV_CACHE[key]


def _output_vocabulary_violations(root, rel, text):
    """GATE (ix): (violations, notes) for ONE newly-added tree order. See the block comment at OV_TAG."""
    rel = rel.replace("\\", "/")
    if not TREE_TO_RE.search(rel):
        return [], []
    v, notes = [], []
    tally = dict(admitted=0, refused=0, announced=0, runner=0, other=0)
    n_mech = 0

    def announce(cid, why):
        tally["announced"] += 1
        notes.append("%s ANNOUNCE: %s criterion %s -- %s. Not judged, not refused." % (OV_TAG, rel, cid, why))

    for m in CRITERION_BLOCK_RE.finditer(text):
        attrs = dict(ATTR_RE.findall(m.group(1)))
        if attrs.get("judgment", "").strip().lower() == "true":
            continue
        invs = INVOCATION_TAG_RE.findall(m.group(2))
        exps = re.findall(r"<expect>(.*?)</expect>", m.group(2), re.S)
        if len(invs) != 1 or len(exps) != 1:
            continue   # the criterion-grammar limb owns that shape
        n_mech += 1
        cid = attrs.get("id", "<no id>")
        kind, tool, args, why = _ov_program(invs[0])
        if kind != "PY":
            tally["runner" if kind == "RUNNER" else "other"] += 1
            continue
        tmpls, open_why, err = _ov_tool(root, tool)
        if err == "ABSENT":
            announce(cid, "TARGET ABSENT AT THE CUT: %s is not in the index, so there is no output to read (the "
                          "ordinary case: the worker writes it)" % tool)
            continue
        if err:
            announce(cid, "%s cannot be read: %s" % (tool, err))
            continue
        if open_why:
            announce(cid, "%s's output is not only its own text: %s" % (tool, open_why))
            continue
        runs, icase, bwhy = _ov_bar_runs(exps[0])
        if runs is None:
            announce(cid, "the bar cannot be reduced to required text: %s" % bwhy)
            continue
        judged = _ov_judge(runs, icase, tmpls + ([_ov_norm(args)] if args else []))
        bad = [r for r, x in judged if x == "REFUSED"]
        und = [r for r, x in judged if x == "UNDECIDED"]
        if bad:
            tally["refused"] += 1
            longest = max(_OV_WORD_RE.findall(bad[0]), key=len)
            near = [t for t in tmpls if (longest.lower() in t.lower() if icase else longest in t)][:2]
            v.append("%s: criterion %s -- %s: its bar <expect>%s</expect> needs the text %r, and the tool it names, %s "
                     "(read from the index at the cut; %d authored templates), writes no line that can carry it: no "
                     "template authors a word of it in place with its counts on a number slot%s. The bar can never "
                     "match this tool's output (F28-AC6's shape: `0 fail` is a runner's summary, never printed by a "
                     "python battery). FIX: expect a line the tool itself prints, or name the tool that prints this bar. "
                     "BOUNDARY: graded only on a tree order STAGED AS ADDED; a runner (bun, pytest, ...), a compound "
                     "line, a target absent at the cut and a tool whose output is not only its own are ANNOUNCED, never "
                     "refused -- GATE (ix) in .tools/to-pipeline-gate.py states what the limb reads and cannot know."
                     % (rel, cid, OV_TAG, exps[0], _ov_show(bad[0]), tool, len(tmpls),
                        ("; nearest authored lines carrying %r: %s" % (longest, " | ".join(repr(_ov_show(t)[:90]) for t in near)))
                        if near else "; the word %r is authored nowhere in it" % longest))
        elif und:
            announce(cid, "UNDECIDED: %s authors a word of %r in place, but only a field it fills at run time could "
                          "carry the rest" % (tool, _ov_show(und[0])))
        else:
            tally["admitted"] += 1
    if n_mech:
        notes.append("%s: %s -- %d mechanical criteria: %d evaluated and admitted, %d refused, %d announced, %d not "
                     "evaluated (a runner's vocabulary), %d not evaluated (not one python program's output)"
                     % (OV_TAG, rel, n_mech, tally["admitted"], tally["refused"], tally["announced"], tally["runner"],
                        tally["other"]))
    return v, notes


# GATE (x) -- ONE ISSUER PER ROUND, keyed to the ROUND, never the serial (row AMGT_RESAPP-Z-S154;
# CLAUDE.md Rule 27, "and a WORKSTREAM IS A SCOPE, NOT A ROUND"; decomp cell AMGT-rk-55). MEASURED
# 2026-09-17: round 13 of AMGT_RESAPP was issued TWICE by two continuations of ONE COO seat serial
# (2.0.0_SA_COO~Z); GATE (iv) above grades WHO commits and passed both times, because it is keyed to
# the SERIAL and nothing in this file read the ROUND. This limb does.
#
# THE KEY. The record face already carries it: `<round>N</round>` on its own line (the rk-22
# template, the rk-19 order). LINE-ANCHORED, the same discipline as PLACEHOLDERS_TAG_RE above -- a
# prose mention of `<round>` in a worker face is inert and must not be read as the element.
#
# THE CENSUS. `head_rounds` is {round:int -> [order path, ...]} for the project's TREE task orders
# TRACKED AT HEAD, read with `git ls-files` + `git show HEAD:<path>` -- never the worktree, because
# the worktree can carry a rename or an edit not yet staged. HEAD does not move inside one gate
# process, so it is read ONCE per (root, code) and cached -- the same shape as the _open_tos_census
# cache in the sibling gate, surprise-row-gate.py.
#
# THE SCOPE. Flat-root orders are not graded (the legacy population, same scope as every limb in
# this file). No order at HEAD is back-filled with a <round> element by this limb or any other --
# an unrounded order at HEAD simply carries no entry in head_rounds and is never the COLLIDING side
# of a refusal; it can still be graded on the MISSING-KEY arm if it is itself staged as ADDED, which
# it is not (it is already at HEAD). A MODIFICATION is not graded here: main() feeds this limb only
# the NEWLY-ADDED (git A/R) set, exactly as GATE (viii)'s newly-added half does -- a worker's status
# flip and a COO re-cut of an existing order are modifications by construction (Rule 27).
ROUND_ELEMENT_RE = re.compile(r"^[ \t]*<round>\s*([0-9]+)\s*</round>[ \t]*$", re.M)

# THE WORKSTREAM KEY (row IRPT_BCKEND-S179; Rule 27 "a WORKSTREAM is a SCOPE, not a round"). An order
# may carry a line-anchored <workstream>NAME</workstream> element (same discipline as ROUND_ELEMENT_RE:
# a prose mention is inert). The census then keys it by (NAME, round) and a collision is looked up
# under the order's OWN (workstream, round), so two workstreams of one project each issue their own
# round N. An order WITHOUT the element keys by the bare round int, exactly as before.
WORKSTREAM_ELEMENT_RE = re.compile(r"^[ \t]*<workstream>\s*(\S+?)\s*</workstream>[ \t]*$", re.M)


def _round_key(text, n):
    """The census/lookup key for an order declaring round `n`: (workstream, n) when a line-anchored
    <workstream> element is present, else the bare int `n` (the pre-S179 shape, unchanged)."""
    w = WORKSTREAM_ELEMENT_RE.search(text or "")
    return (w.group(1), n) if w else n


def _round_key_label(k):
    return "workstream %s round %d" % k if isinstance(k, tuple) else "round %d" % k

# THE NARROW EXEMPTION (row AMGT_RESAPP-Z-W58-S2; ROUND_ANALYSIS.round14.md s.2.1): an order that
# declares itself round-less EXPLICITLY, via a line-anchored <direct_act>true</direct_act> element
# (same discipline as ROUND_ELEMENT_RE -- a prose mention is inert), is exempted from the missing-
# <round> refusal below; the round-collision branch is UNCHANGED, so <direct_act>true</direct_act>
# alongside a <round> element never dodges collision review.
DIRECT_ACT_ELEMENT_RE = re.compile(r"^[ \t]*<direct_act>\s*true\s*</direct_act>[ \t]*$", re.M)

_HEAD_ROUNDS_CACHE = {}


def _head_rounds_for_project(root, code):
    """({round:int -> [order path, ...]}, unrounded_count, total) for `code`'s TREE task orders
    TRACKED AT HEAD, read ONCE per (root, code) per gate run and cached (see the GATE (x) comment
    above). The dict is None when the census could not run -- the caller fails closed on the LIMB,
    never the whole gate (a census failure here must not silently admit every round collision)."""
    key = (root, code)
    if key not in _HEAD_ROUNDS_CACHE:
        _HEAD_ROUNDS_CACHE[key] = _head_rounds_census(root, code)
    return _HEAD_ROUNDS_CACHE[key]


def _head_rounds_census(root, code):
    try:
        ls = subprocess.run(["git", "ls-files", "--", "org/missions/D*/*/%s/task-orders/*.md" % code],
                            cwd=root, capture_output=True, text=True, encoding="utf-8", errors="replace",
                            timeout=60)
    except Exception:  # noqa: BLE001
        return None, 0, 0
    if ls.returncode != 0:
        return None, 0, 0
    paths = sorted({p.strip().replace("\\", "/") for p in ls.stdout.splitlines() if p.strip()})
    rounds, unrounded = {}, 0
    for p in paths:
        text = _head_blob(root, p)
        if text is None:
            continue
        m = ROUND_ELEMENT_RE.search(text)
        if m:
            rounds.setdefault(_round_key(text, int(m.group(1))), []).append(p)
        else:
            unrounded += 1
    return rounds, unrounded, len(paths)


def _round_issuer_violations(rel, text, head_rounds):
    """GATE (x): PURE, no I/O. `head_rounds` is {round:int -> [order path, ...]} for the project's
    TREE orders TRACKED AT HEAD (the caller's census, see _head_rounds_census). [] when `rel` is not
    a tree order (the flat-root legacy population is not graded). Otherwise the order MUST carry a
    line-anchored <round>N</round> element -- a prose mention of the tag is not the element and is
    not read as one; missing -> REFUSED naming the missing key, UNLESS the order carries a line-
    anchored <direct_act>true</direct_act> element (row AMGT_RESAPP-Z-W58-S2: a narrow exemption for
    an order that declares itself round-less by design, not a general weakening -- see
    DIRECT_ACT_ELEMENT_RE above). And its round must carry NO order at HEAD yet -- found -> REFUSED
    naming every colliding order in that round in ONE message, so the issuer sees the whole set, and
    citing row AMGT_RESAPP-Z-S154."""
    rel = rel.replace("\\", "/")
    m_code = TREE_TO_RE.search(rel)
    if not m_code:
        return []
    m = ROUND_ELEMENT_RE.search(text or "")
    if not m:
        if DIRECT_ACT_ELEMENT_RE.search(text or ""):
            return []
        return ["%s: NO line-anchored <round>N</round> element -- ONE ISSUER PER ROUND is keyed to "
                "the ROUND, never the serial (Rule 27; row AMGT_RESAPP-Z-S154), and this limb needs "
                "the key on its own line to enforce it. A prose mention of <round> elsewhere in the "
                "face is not the element. Add '<round>N</round>' naming this order's round, or a "
                "line-anchored '<direct_act>true</direct_act>' declaring this order round-less by "
                "design (row AMGT_RESAPP-Z-W58-S2)." % rel]
    key = _round_key(text, int(m.group(1)))
    existing = (head_rounds or {}).get(key) or []
    if existing:
        code = m_code.group(5)
        return ["%s: %s of %s already has an issuance at HEAD (%d order(s): %s); ONE ISSUER "
                "PER ROUND is keyed to the ROUND, never the serial (Rule 27; row "
                "AMGT_RESAPP-Z-S154). A re-cut into the first issuance MODIFIES its orders and adds "
                "no file. A SECOND WORKSTREAM of the project issues its own round by carrying a "
                "line-anchored '<workstream>NAME</workstream>' element beside <round> (row "
                "IRPT_BCKEND-S179); this limb reads no override."
                % (rel, _round_key_label(key), code, len(existing),
                   ", ".join(os.path.basename(p) for p in sorted(existing)))]
    return []


def _staged_modified(root):
    """The set of paths STAGED AS MODIFIED (git status M), or None when the index cannot be read."""
    try:
        out = subprocess.run(["git", "diff", "--cached", "--name-status"],
                             cwd=root, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=30)
    except Exception:  # noqa: BLE001
        return None
    if out.returncode != 0:
        return None
    return {ln.split("\t")[-1].strip() for ln in out.stdout.splitlines()
            if len(ln.split("\t")) >= 2 and ln.split("\t")[0].strip().startswith("M")}


def _repo_root():
    try:
        out = subprocess.run(["git", "rev-parse", "--show-toplevel"],
                             capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=20)
        if out.returncode == 0:
            return out.stdout.strip()
    except Exception:  # noqa: BLE001
        pass
    return os.getcwd()


def _newly_added(root):
    """The set of paths STAGED AS ADDED. Prospective-only scoping lives here.

    A rename (R) counts as added at its new path -- moving a TO into task_orders/ is an
    issuance. A modification (M) does not: no limb that reads THIS set refuses an existing TO.
    The ONE limb that grades a modification -- GATE (viii), and only on an order that ALREADY
    DECLARES <placeholders> at HEAD (Andrew-direct card 6, record @e2210bf34c) -- reads its own
    set, _staged_modified(), so this set's contract is unchanged.
    """
    try:
        out = subprocess.run(["git", "diff", "--cached", "--name-status"],
                             cwd=root, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=30)
    except Exception:  # noqa: BLE001
        return None  # fail closed: caller refuses
    if out.returncode != 0:
        return None
    added = set()
    for line in out.stdout.splitlines():
        parts = line.split("\t")
        if len(parts) < 2:
            continue
        code = parts[0].strip()
        path = parts[-1].strip()
        if code.startswith("R") and len(parts) == 3 and _is_redaction_rename(root, code, parts[1].strip(), path):
            print("NOTE: %s: a pure redaction RENAME of a terminal order (%s, account id -> acct#<8hex> in the name only); "
                  "not an issuance." % (path, parts[1].strip()), file=sys.stderr)
            continue
        if code.startswith("A") or code.startswith("R"):
            added.add(path)
    return added


def _redaction_rename_ok(old_path, new_path):
    """PURE: the new path differs from the old ONLY by digit-bearing tokens becoming acct#<8hex>, at least one of them."""
    if old_path == new_path or not _REDACT_TOKEN_RE.search(new_path):
        return False
    parts = _REDACT_ANY_MARK_RE.split(new_path)
    return bool(re.fullmatch(_REDACT_ID_PAT.join(re.escape(p) for p in parts), old_path))


def _is_redaction_rename(root, code, old_path, new_path):
    """dell2 1.0.0_SA_CTO~DELL2 msg 3850 via 0.0.0_AB_MSTR 108074 (containment ruling @0e8209c33c): a rename of a TERMINAL order whose
    content is byte-identical (git similarity R100) and whose name changes only by an account id -> acct#<8hex> is not an issuance."""
    if code != "R100" or not _redaction_rename_ok(old_path, new_path):
        return False
    head = _head_blob(root, old_path)
    return head is not None and _last_status(head)[0] in DONE_WORDS


def _staged_redaction_renames(root):
    """{new path} of pure redaction renames in the index (empty on any read failure: the ordinary limbs then grade it)."""
    try:
        out = subprocess.run(["git", "diff", "--cached", "--name-status", "-M"], cwd=root, capture_output=True, text=True,
                             encoding="utf-8", errors="replace", timeout=30)
    except Exception:  # noqa: BLE001
        return set()
    found = set()
    for line in (out.stdout or "").splitlines():
        parts = line.split("\t")
        if len(parts) == 3 and _is_redaction_rename(root, parts[0].strip(), parts[1].strip(), parts[2].strip()):
            found.add(parts[2].strip())
    return found


def _check_preflight(body):
    """Return a list of complaints about the preflight block body."""
    problems = []
    for tool in PREFLIGHT_TOOLS:
        pat = re.compile(re.escape(tool) + r"\s*[:=]\s*" + DISPOSITION_RE, re.I)
        m = pat.search(body)
        if not m:
            problems.append(
                "preflight names no disposition for %s -- expected "
                "'%s: RUN' or '%s: DECLARED-NOT-APPLICABLE <reason>'" % (tool, tool, tool))
            continue
        # The remainder of the disposition's OWN LINE. Reading to the next 200 chars lets the
        # FOLLOWING TOOL'S line be scored as this tool's evidence -- caught by the bare-reason
        # control on first exercise, 2026-09-01. Both limbs below share this bound.
        eol = body.find("\n", m.end())
        tail = (body[m.end():] if eol == -1 else body[m.end():eol]).strip()
        if m.group(1).upper() == "DECLARED-NOT-APPLICABLE":
            if len(tail) < 8:
                problems.append(
                    "%s is DECLARED-NOT-APPLICABLE with no reason ON ITS OWN LINE -- a bare "
                    "not-applicable is a skip wearing a tidier label" % tool)
        else:
            # THIRD LIMB: a RUN owes a denominator or an explicit blindness statement.
            if not COVERAGE_WORD_RE.search(tail):
                problems.append(
                    "%s: RUN carries NO DENOMINATOR OR BLIND/COVERAGE STATEMENT on its own line. "
                    "A vintage dates the corpus; it cannot say the lens was blind on THIS "
                    "subject. Record what it scanned (e.g. '%s: RUN -- 395 .tf files, 24 "
                    "policy blocks never seen') or what it could not see." % (tool, tool))
    return problems


# LAYER 3's TEETH. The pipeline doc landed the `dep_stage` ENUM (COO @c4d8c0025d) and routed a
# "sweep hook" that never shipped. MEASURED 2026-09-01: 316 of 348 project JSONs carry NO dep_stage
# key -- the enum exists and nothing populates it, which is why 139 of 281 proof instances sit under
# the resulting waiver. A standalone sweep would only REPORT that. Folding the requirement into the
# SAME choke-point makes it populate itself: a project cannot have a NEW TO cut against it until its
# stage is declared. Forward-only by construction -- no back-fill, which the doc forbids as "a guess
# about history wearing a controlled vocabulary's clothing".
# THE RATIFIED ENUM IS SIX VALUES, NOT SEVEN. Authority: COO's Rule-24 record
# org/tier1_exec/2.0.0_SA_COO/deliverables/DEP_STAGE_ENUM_RULE24_RECORD_20260821.md:41-46, which
# transitions DECOMP -> EXECUTING directly on "first TO cut from a decomp cell". There is no
# intermediate state and the record's own postulate work explains why.
#
# CORRECTED 2026-09-01 ~19:0xZ. This tuple carried a SEVENTH value, `TOS_CUT`, that was NEVER
# RATIFIED -- introduced by 3.0.0_SA_CVO when this gate was built, from the ten-step map's step 6
# rather than from the enum's authority. Rule 24 binds any schema an agent AUTHORS **OR ADOPTS**,
# and this was a bad adoption by the seat that mandated the rule.
#
# AND THE CONSEQUENCE IS THE SHARP PART: THE WRONG ENUM SUPPRESSED A REAL FINDING. `--sweep`
# reported `BRIEF x2` as off-enum and said NOTHING about `TOS_CUT x2`, which is equally off-enum --
# because this tuple had been widened to admit it. A GATE WHOSE VOCABULARY IS WRONG CANNOT SEE THE
# VIOLATIONS THAT MATCH ITS OWN ERROR, and it reports CLEAN on exactly those. The refusal message
# printed the bad value back to every seat it refused, and it went out in two fabric broadcasts.
DEP_STAGE_ENUM = ("REGISTERED", "PRD", "DECOMP", "EXECUTING", "ROUND_CLOSE", "CLOSED")
PROJECT_RE = re.compile(r"([A-Z][A-Z0-9]*(?:_[A-Z0-9]+)*)")


def _project_of(rel):
    """The project code a TO filename declares, or None. TOs are named PROJECT.TO-NAME.md."""
    base = os.path.basename(rel)
    m = PROJECT_RE.match(base)
    return m.group(1) if m else None


def _project_row_rel(root, rel):
    """(code, rel_json, err): the TO's project code, the repo-relative path of its register row, and an
    error string when the path itself is inconsistent. ONE resolver for BOTH roots, used by every limb:
      TREE  org/missions/D*/MACRO/PROJECT/task-orders/X.md -> org/missions/D*/MACRO/PROJECT/project.json
            -- derived from the PATH, never looked up; the filename's code must equal the folder's
            PROJECT, and a TO filed under another project's folder is an identity defect, reported.
      FLAT  org/.../task_orders/PROJECT.TO-x.md -> org/projects/PROJECT.json, the EXACT code only.
    THE WALK-BACK (FOO_BAR_BAZ -> FOO_BAR -> FOO) IS RETIRED, in all four places it lived: once macro
    folders exist a walked-back code resolves a PROJECT to its MACRO (spec s.7). Measured before
    retiring it (2026-09-02): of 2,235 flat TOs, 1,968 resolve exactly, 264 have no row under any
    spelling, and THREE resolved only by walk-back -- every one to a row that is not its project
    (SCTY_ONBOARDING_GUARDRAILS -> SCTY, ADHC_PREFLT_TO -> ADHC_PREFLT, ADHC_COMPIL_V2 -> ADHC_COMPIL).
    It was already wrong three times and had never once saved a correct resolution."""
    code = _project_of(rel)
    if not code:
        return None, None, None
    m = TREE_TO_RE.search(rel.replace("\\", "/"))
    if m:
        if m.group(5) != code:
            return code, None, ("%s: the filename says project %r but the tree folder is %r. A tree TO "
                                "lives in ITS project's task-orders/ -- the path is the membership."
                                % (rel, code, m.group(5)))
        rel_json = m.group(2) + "/project.json"
        # R-iv (CVO review @580c4f72a2): the ROW's project_code must equal the folder too. The generator's
        # R4 catches it when `check` runs; the gate reads the row ITSELF here, so a TO cannot be graded
        # against a row that claims another project. The read is best-effort: an unreadable row is layer
        # 3's refusal, not this one's.
        try:
            import json as _j
            with open(os.path.join(root, rel_json), "r", encoding="utf-8") as fh:
                pc = _j.load(fh).get("project_code")
        except Exception:  # noqa: BLE001
            pc = None
        if pc is not None and pc != m.group(5):
            return code, None, ("%s: the tree row %s says project_code %r but its folder is %r. Two carriers of "
                                "one identity disagree; the row is graded against nothing until they agree "
                                "(generator refusal R4)." % (rel, rel_json, pc, m.group(5)))
        return code, rel_json, None
    return code, "org/projects/%s.json" % code, None


def check_project_stage(root, rel):
    """LAYER 3: the TO's project must exist and declare a dep_stage from the ratified enum."""
    import json
    code, rel_json, err = _project_row_rel(root, rel)
    if not code:
        return ["%s: filename declares no PROJECT code -- a TO is named "
                "PROJECT.TO-NAME.md so its project is resolvable without opening it" % rel]
    if err:
        return [err]
    p = os.path.join(root, rel_json)
    cand = rel_json  # the messages below name the row by PATH, which is unambiguous across two roots
    if not os.path.isfile(p):
        return ["%s: NO project row at %s. A TO cannot be cut against an unregistered project -- "
                "registration is stage 1 (tree: mkdir + project.json in ONE commit; flat: "
                "org/projects/<CODE>.json, exact code, no walk-back)." % (rel, rel_json)]
    try:
        with open(p, "r", encoding="utf-8") as fh:
            doc = json.load(fh)
        stage = doc.get("dep_stage")
    except Exception as exc:  # noqa: BLE001
        return ["%s: project JSON %s is unreadable (%s) -- fail-closed" % (rel, cand, exc)]
    if stage is None:
        return ["%s: project %s declares NO dep_stage. Set it before cutting a TO -- the pipeline "
                "stage must be machine-readable (layer 3). Enum: %s"
                % (rel, cand, " | ".join(DEP_STAGE_ENUM))]
    if stage not in DEP_STAGE_ENUM:
        return ["%s: project %s has dep_stage=%r, which is NOT in the ratified enum (%s)"
                % (rel, cand, stage, " | ".join(DEP_STAGE_ENUM))]
    # STEP-3 FABRIC FORK. Same read, one more key. A project whose execution fabric is undeclared
    # cannot have work dispatched against it -- the laptop and site-Z fabrics are different worlds
    # and the choice was being made implicitly, by whoever happened to pick up the TO.
    fabric = doc.get("fabric")
    try:
        values = _fabric_values()
    except Exception as exc:  # noqa: BLE001
        return ["%s: project %s -- the device register is unreadable (%s) -- fail-closed" % (rel, cand, exc)]
    if fabric is None:
        return ["%s: project %s declares NO fabric. Step 3 requires the laptop-vs-site-Z call to "
                "be MADE and RECORDED before a TO is cut against it. Set \"fabric\" to one of: %s"
                % (rel, cand, " | ".join(values))]
    if str(fabric).strip().lower() not in values:
        return ["%s: project %s has fabric=%r, which is NOT in the ratified enum (%s)"
                % (rel, cand, fabric, " | ".join(values))]
    return []


# FOURTH LIMB -- THE ENDPOINT SECTION IS MANDATORY.
# ANDREW-DIRECT 2026-09-01, VERBATIM, relayed by 1.0.0_SA_CTO (msg 92478) from its own terminal:
#  "yes endpoint section is mandatory and it is written by running endpoint --forward skill
#   process."
# An explicit Andrew word on a NEW REFUSAL CONDITION, which is the one thing no agent may implement
# without him (CLAUDE.md: never implement an approval gate unless Andrew explicitly asks).
#
# WHY IT IS A ROUTING FAILURE, NOT A TIDINESS ONE. Step 10's third limb asks "does the PRD name this
# OUTCOME?" With no ENDPOINT section that question has NO ANSWER and the scope-change route silently
# collapses into the spec-error route -- every misrouted scope change lands on COO as a TO amendment
# instead of on CTO as a PRD revision.
# AND AS OF TONIGHT IT IS WORSE THAN A SILENT COLLAPSE: surprise-row-gate.py REFUSES
# route=SCOPE_CHANGE without an outcome_ref matching FWD-n, and FWD ids exist ONLY in an ENDPOINT
# section. A PRD without one makes a genuine scope change UNFILEABLE -- the row cannot be written and
# the finding has nowhere to go. Two gates landed hours apart can compose into a dead end; this limb
# is what stops that one.
ENDPOINT_HEADING = "## ENDPOINT (step 2, /endpoint --forward)"


def _prd_paths(doc):
    """Every PRD path a project JSON names. Tolerates all THREE shapes measured in the estate.

    MEASURED 2026-09-01 over 349 project JSONs: `prds` is a LIST in 327, ABSENT in 21, and a bare
    STRING in 1. A resolver written against the common shape alone would throw on that one file --
    and it would throw inside a GATE, i.e. it would fail closed on a project whose only sin is an
    old field shape.
    """
    v = doc.get("prds")
    if not v:
        return []
    if isinstance(v, str):
        return [v]
    out = []
    for item in v:
        if isinstance(item, str):
            out.append(item)
        elif isinstance(item, dict) and item.get("path"):
            out.append(item["path"])
    return out


def check_endpoint_section(root, rel):
    """LIMB 4: a pipeline-registered project's PRD must carry a non-empty ENDPOINT section."""
    import json
    code, rel_json, err = _project_row_rel(root, rel)
    if not code or err:
        return [], []
    p = os.path.join(root, rel_json)
    cand = code  # the messages below name the project by CODE
    if not os.path.isfile(p):
        return [], []          # layer 3 already refuses this; do not double-report
    try:
        with open(p, "r", encoding="utf-8") as fh:
            doc = json.load(fh)
    except Exception:  # noqa: BLE001
        return [], []          # layer 3 already fail-closed on an unreadable project JSON

    if doc.get("dep_stage") is None:
        return [], []          # not pipeline-registered -> this limb does not apply
    # dep_stage=REGISTERED means "project registered; NO purpose-level PRD yet" at the ratifying
    # record. Demanding an ENDPOINT section there would refuse a project for being at the stage the
    # enum defines as pre-PRD.
    if doc.get("dep_stage") == "REGISTERED":
        return [], ["%s: project %s is at dep_stage=REGISTERED (pre-PRD by definition) -- endpoint "
                    "limb does not apply" % (rel, cand)]

    paths = _prd_paths(doc)
    if not paths:
        # NOT REFUSED, AND THE RESTRAINT IS DELIBERATE. Andrew's word makes the SECTION mandatory.
        # It is NOT a word about a project that names no PRD at all -- that is a different defect,
        # and converting his authorization into a refusal he did not give is precisely the
        # inferred-gate prohibition (ANDREW_DIRECT_20260804_1827Z). Surfaced loudly, never widened.
        return [], ["%s: WARN -- project %s names NO PRD (`prds` absent/empty), so the mandatory "
                    "ENDPOINT section CANNOT BE CHECKED. This limb passes and the hole is stated "
                    "rather than silently widened into a refusal Andrew did not authorize. 21 of "
                    "349 project JSONs are in this shape." % (rel, cand)]

    found, missing = [], []
    for rp in paths:
        ap = os.path.join(root, rp.replace("\\", "/"))
        if not os.path.isfile(ap):
            missing.append("%s (FILE NOT FOUND)" % rp)
            continue
        try:
            with open(ap, "r", encoding="utf-8", errors="replace") as fh:
                body = fh.read()
        except Exception as exc:  # noqa: BLE001
            missing.append("%s (unreadable: %s)" % (rp, exc))
            continue
        # Top-level heading only: a fenced, illustrative copy of the title (as _PRD_TEMPLATE.md
        # carries) must not satisfy this limb (CVO~A @dddd96477d falsifier 1, shared with limb 5).
        section = _top_section(body, ENDPOINT_HEADING)
        if section is None:
            missing.append("%s (no top-level ENDPOINT heading)" % rp)
            continue
        section = section.strip()
        if len(section) < 12:
            missing.append("%s (ENDPOINT heading present but section EMPTY)" % rp)
            continue
        found.append(rp)

    if found:
        return [], ["%s: ENDPOINT section OK in %s" % (rel, found[0])]
    return ([("%s: project %s is pipeline-registered and NONE of its %d named PRD(s) carry a "
              "non-empty '%s' section -- %s. Andrew-direct 2026-09-01: the endpoint section is "
              "MANDATORY and is written by running /endpoint --forward. Without it, step 10 cannot "
              "ask 'does the PRD name this outcome?', so a scope change silently reroutes as a spec "
              "error -- and with the outcome_ref gate live it becomes UNFILEABLE instead."
              % (rel, cand, len(paths), ENDPOINT_HEADING, "; ".join(missing)))], [])


PRD_HEADER_SCHEMA_REL = "org/standards/PRD_HEADER.schema.json"
MANIFEST_HEADING_RE = re.compile(r"^##\s+.*SURFACE MANIFEST", re.M | re.I)
# The minimum body a SURFACE MANIFEST section must carry to count as populated.
# PROMOTED FROM A BARE LITERAL TO A NAMED CONSTANT 2026-09-09 (1.0.0_SA_CTO~Z, on 3.0.0_SA_CVO~Z's
# verification msg 20602). .tools/prd-manifest-gate.py enforces the SAME rule at COMMIT time and had
# COPIED this 40, so the CTO's claim that the two gates "cannot drift apart" was true of the two
# IMPORTED symbols (_top_section, MANIFEST_HEADING_RE) and FALSE of this third shared thing. It now
# imports this name, so tuning the floor moves both refusals together.
# HONEST PROVENANCE: 40 is UNMEASURED and inherited -- no derivation appears in this file's history,
# and it is NOT re-justified here. What changed is that it is now named, shared, and CONTROLLED AT
# ITS BOUNDARY by prd-manifest-gate.py --self-test (a 39-char body must refuse, a 41-char body must
# pass), so a future change to it fails a test instead of silently disagreeing across two gates.
MANIFEST_MIN_BODY_CHARS = 40
PRD_FENCE_RE = re.compile(r"```json\s*(.*?)```", re.S)
# An outcome DEFINITION is the id at LINE START followed by 2+ spaces and text -- the card form
# /endpoint --forward emits. A MENTION ("a row citing `FWD-9` passes") is mid-line and does not
# match; neither does a possessive at line start ("FWD-7's message ...", no 2-space gap).
# MEASURED before this limb existed: a bare id sweep of ETFS_GUARDRAIL_PRD.md read NINE outcomes
# against a header listing EIGHT, because the ENDPOINT section QUOTES a CVO finding about FWD-9.
# A limb counting mentions would refuse its own first PRD on a quotation.
# COLUMN-ALIGNED IDS (2026-09-03, 2.0.0_SA_COO 93532 -- three round-5 orders refused on ONE character): the card form
# pads the id to one text column, so a one-digit id is followed by TWO spaces and a two-digit id by ONE. The first
# two-digit outcome in the estate (NFRA_COMPEFFICACY FWD-10, PRD v0.5) therefore read as a MENTION and the header was
# refused for listing an outcome the section "did not define". A definition is the id at line start followed by
# whitespace up to the text column: 2+ spaces after any id, or exactly one after an id of two or more digits. The
# mention exclusions stand: an apostrophe ("FWD-7's"), a backtick, or a mid-line citation still do not match.
FWD_DEF_RE = re.compile(r"^[ \t]*(FWD-[0-9]+)(?:[ \t]{2,}|(?<=[0-9]{2})[ \t])\S", re.M)


# A fence OPENER by the CommonMark grammar the estate's documents actually use: 0-3 spaces of indent,
# then a run of THREE OR MORE backticks or tildes, then an info string. A backtick opener's info
# string may not itself contain a backtick (that line is inline code, not a fence).
_FENCE_OPEN_RE = re.compile(r"^( {0,3})(`{3,}|~{3,})(.*)$")
# A top-level heading: '## ' at COLUMN 0, no leading whitespace. This is the one grammar used for the
# heading being sought AND for the boundary of the section it introduces. Stricter than CommonMark
# (which admits 1-3 spaces) ON PURPOSE: an indented heading the gate cannot see makes limb 4 REFUSE
# loudly ("no ENDPOINT section") -- fail-closed. The fence grammar below is PERMISSIVE for the same
# reason in the other direction: a fence the gate fails to blank lets a heading INSIDE it count --
# fail-open. Strict where a miss refuses; permissive where a miss admits.
_H2_RE = re.compile(r"(?m)^## [^\n]*$")


def _blank_fences(text):
    """A SAME-LENGTH copy of text with every fenced block turned to spaces (newlines kept), so an
    offset found in the copy indexes the ORIGINAL. This is how a heading is found at TOP LEVEL only
    while the section it introduces -- which may itself contain fenced blocks, like the ENDPOINT's
    FWD cards -- is sliced intact from the original.

    A LINE SCANNER, not a regex, because the fence grammar is stateful: a block opened by a run of N
    markers closes only at a line of the SAME marker with a run of AT LEAST N (0-3 spaces of indent,
    nothing else but trailing whitespace), and a block never closed runs to END OF FILE. Each rule is
    a falsifier CVO~A landed on the earlier regex forms:
      @df87b39f6e f3/f4  ``` only was blanked -> a ~~~ fence hid nothing
      @ef6a37e098 f7     a ~~~~ opener could not be closed by an exact-three closer -> the regex
                         failed to MATCH and the whole block stayed visible
      @ef6a37e098 f8     a 1-space-indented ``` fence (legal Markdown, present in this estate's
                         architecture documents) was not a fence at column 0 -> visible
      @ef6a37e098 f11    a ```` outer block was closed by the ``` opener of an INNER FWD card -> the
                         outer block's tail stayed visible
      @ef6a37e098        an EOF-unclosed fence -- Markdown blanks it to the end; the regex needed a
                         closer to match at all, so it blanked nothing
    Every one of those is fail-OPEN: a heading inside an unblanked fence counts as top level."""
    out = []
    fence_char = None
    fence_len = 0
    for line in text.split("\n"):
        body = line.rstrip("\r")
        if fence_char is None:
            m = _FENCE_OPEN_RE.match(body)
            if m and not (m.group(2)[0] == "`" and "`" in m.group(3)):
                fence_char = m.group(2)[0]
                fence_len = len(m.group(2))
                out.append(" " * len(line))
            else:
                out.append(line)
            continue
        stripped = body.lstrip(" ")
        run = stripped.rstrip(" \t")
        if (len(body) - len(stripped) <= 3 and run and set(run) == {fence_char}
                and len(run) >= fence_len):
            fence_char = None
        out.append(" " * len(line))
    return "\n".join(out)


def _top_section(text, heading):
    """The ORIGINAL-text body of the section introduced by `heading` when that heading is a
    TOP-LEVEL heading -- '## ' at column 0, outside every fence -- or None. Body runs to the next
    top-level '## ' heading by the SAME grammar.

    `heading` is the exact title string (matched as a WHOLE LINE: '^## <title>$' with trailing
    whitespace tolerated) or a compiled regex that is itself anchored at line start.

    History of this function, kept because each cut was falsified by CVO~A on its own bytes:
      @dddd96477d f1  plain str.find() selected an ILLUSTRATIVE title inside a ``` fence first
      @df87b39f6e f1  the title embedded MID-LINE in prose satisfied the blanked-copy find()
      @df87b39f6e f2  the title in INDENTED code (not fenced) satisfied it
      @df87b39f6e f3  a section wholly inside a ~~~ fence satisfied it
    One anchored, unindented, whole-line, fence-aware grammar closes all four at once."""
    blank = _blank_fences(text)
    if isinstance(heading, str):
        # BACKTICK-INSENSITIVE (2026-09-04, 1.0.0_SA_CTO, on 2.0.0_SA_COO 94213 refusal 2).
        # An EXACT-string compare made this a FALSE-ABSENCE generator: NFRA_OUTSET's PRD wrote the
        # heading as "## ENDPOINT (step 2, `/endpoint --forward`)" -- the template title with the
        # command in code fences -- and the gate reported the MANDATORY section MISSING. That is the
        # dangerous direction: the limb exists so step 10 can ask "does the PRD name this outcome?",
        # and surprise-row-gate.py refuses route=SCOPE_CHANGE without an outcome_ref that only an
        # ENDPOINT section supplies -- so a false absence makes a real scope change UNFILEABLE.
        # Backticks are markdown decoration on the TITLE TEXT and carry no meaning here, so they are
        # tolerated ANYWHERE inside the title. Nothing else loosens: every non-backtick character is
        # still matched exactly and the match is still whole-line, anchored at column 0 and
        # fence-aware, so no DIFFERENT heading becomes reachable.
        # COST: one "`*" per character in the compiled pattern. NON-APPLICATION: a compiled-regex
        # `heading` is passed through untouched -- its author already owns its own grammar.
        pat = re.compile(r"(?m)^" + "`*".join(re.escape(c) for c in heading) + r"[ \t]*$")
    else:
        pat = heading
    m = pat.search(blank)
    if not m:
        return None
    end = m.end()
    nxt = _H2_RE.search(blank, end)
    return text[end:] if not nxt else text[end:nxt.start()]


# ---------------------------------------------------------------------------------------------
# LIMB 6 -- THE PRD SIGN-OFF GATE (L4-R). Andrew-direct 2026-09-10 ~21:2xZ at the 1.0.0_SA_CTO
# terminal, VERBATIM: "I dont want to ask shit this should be entirely automatic and gated, CRO and
# CVO should have to sign off on PRD before COO gets it." Spine v3.14. A task order is REFUSED unless
# its project's PRD carries, at the PRD's CURRENT prd_version, a SIGNED sign-off file from EACH of
# 4.0.0_SA_CRO (the brief half) and 3.0.0_SA_CVO (the ratified-text half), at
#   org/missions/D<n>/<MACRO>/<CODE>/prd/signoff/<serial>.json
# in lane TREE_PRD_SIGNOFF, which the PRD's author (ANY_CTO on prd/**) cannot write. A sign-off is
# VERSION-BOUND: a bump re-opens both. Measured cause: 13 corrections in three unrequested review
# passes on two PRDs the flow had already declared decomposable (CVO d0e72ccd56; CRO e975e96fc0,
# 637b2f8178). No new owner; two mechanical carriers (this limb, and the notifier withholding the
# COO delivery). Non-retroactive per v3.13 for rounds already cut.
# ---------------------------------------------------------------------------------------------
SIGNOFF_REVIEWERS = ("4.0.0_SA_CRO", "3.0.0_SA_CVO")   # the two PRIMARY reviewers; the lib holds the full rule


def _signoff_lib():
    import importlib.util as _ilu
    _spec = _ilu.spec_from_file_location("prd_signoff_lib", os.path.join(os.path.dirname(os.path.abspath(__file__)), "prd_signoff_lib.py"))
    _m = _ilu.module_from_spec(_spec)
    _spec.loader.exec_module(_m)
    return _m


def _base_serial_of(s):
    s = str(s or "").strip()
    return s.split("~", 1)[0]


def _signoff_violations(rel, code, prd_rel, prd_version, prd_last_commit, files, prd_text=None, coo_lane=None, designated=None):
    """PURE given `prd_text`. v3.15: the verdict is prd_signoff_lib.evaluate() -- each half (ratified-text =
    ENDPOINT + CONTRACTS; brief = every other section) bound to the HASH of its sections, legacy files
    bound to prd_version. `prd_version` / `prd_last_commit` are kept in the signature for the callers
    that still pass them; when `prd_text` is None a minimal text carrying only the header is synthesised
    so legacy (version-bound) files still grade."""
    lib = _signoff_lib()
    if prd_text is None:
        prd_text = '```json\n{"prd_version": "%s"}\n```\n' % prd_version
    r = lib.evaluate(prd_text, files, coo_lane_of_project=coo_lane, designated=designated)
    return lib.violations(rel, code, prd_rel, r)


def check_prd_signoff(root, rel):
    """LIMB 6 wrapper: resolve the TO's project the way limb 4 does, then grade every named PRD's sign-offs
    through prd_signoff_lib (one rule; the notifier and prd-signoff.py call the same one)."""
    import json
    lib = _signoff_lib()
    code, rel_json, err = _project_row_rel(root, rel)
    if not code or err:
        return [], []
    p = os.path.join(root, rel_json)
    if not os.path.isfile(p):
        return [], []
    try:
        with open(p, "r", encoding="utf-8") as fh:
            doc = json.load(fh)
    except Exception:  # noqa: BLE001
        return [], []
    if doc.get("dep_stage") is None or doc.get("dep_stage") == "REGISTERED":
        return [], []
    paths = _prd_paths(doc)
    if not paths:
        return [], []
    v, notes = [], []
    for rp in paths:
        rp = rp.replace("\\", "/")
        ap = os.path.join(root, rp)
        if not os.path.isfile(ap):
            continue  # limb 4 already names a missing PRD
        try:
            with open(ap, "r", encoding="utf-8", errors="replace") as fh:
                text = fh.read()
        except Exception:  # noqa: BLE001
            continue
        if not lib.prd_header(text).get("prd_version"):
            continue  # limb 5 refuses a header-less PRD; do not double-report
        # NON-RETROACTIVITY (spine v3.13; the v3.14 L4-R block's "the gate binds from the next prd_version"): a PRD
        # last committed before the law commit is grandfathered; its first bump after the law binds it. One rule,
        # in the lib, shared with prd-signoff.py status and the notifier.
        bound, why = lib.bound_by_law(root, rp)
        if not bound:
            notes.append("%s: L4-R not applied to %s -- %s" % (rel, rp, why))
            continue
        files = lib.read_signoff_files(os.path.join(os.path.dirname(ap), lib.SIGNOFF_DIR))
        r = lib.evaluate(text, files, coo_lane_of_project=doc.get("coo_lane"), designated=lib.designated_brief_signer(doc)[0],
                         brief_by_cro=lib.brief_written_by_cro(root, text)[0])
        sv = lib.violations(rel, code, rp, r)
        if sv:
            v.extend(sv)
        else:
            notes.append("%s: L4-R sign-offs OK for %s at %s (%s)" % (
                rel, rp, r["prd_version"], ", ".join("%s=%s" % (h, r["halves"][h]["by"]) for h in lib.HALVES)))
        # Andrew-direct 2026-09-28 ~18:05Z ruling 4: L4-R stays ENDPOINT-bound, but a ratified half whose own
        # text moved since signing is SAID, never admitted silently. A WARN, not a refusal.
        for h in lib.HALVES:
            st = r["halves"][h]
            if st["state"] == "SIGNED" and "text CHANGED since signed" in str(st["detail"]):
                notes.append("%s: WARN -- %s %s half: %s (signed by %s, %s); admitted by ENDPOINT hash, the "
                             "changed text is unreviewed" % (rel, rp, h, st["detail"], st["by"], st["file"]))
    return v, notes



def _prd_conformance(prd_text, header_schema, expect):
    """LIMB 5 core, pure: complaints about ONE PRD's step-4 SHAPE. `expect` = {project, directive,
    fabric} from the project JSON (missing keys are not compared). Returns [] when conformant.

    ANDREW-DIRECT 2026-09-02 (/open-calls CALL 2, "All recs approved"): a step-4 conformance check,
    authorized as ONE limb inside THIS existing gate and never a second gate. What it refuses:
      (a) no PRD_HEADER block (the FIRST fenced ```json in the file) or one that fails
          org/standards/PRD_HEADER.schema.json
      (b) header identity disagreeing with the register row (project / directive / fabric)
      (c) no SURFACE MANIFEST section (the step-4 -> step-5 handoff contract, CVO~A adopted)
      (d) header.endpoint_outcomes != the outcomes DEFINED in the ENDPOINT section, either direction
    It does NOT judge the PRD's content -- only that the machinery step 5 and step 10 read is present
    and self-consistent."""
    import json  # local, matching limb 4's style -- this module does not import json at top level
    out = []
    m = PRD_FENCE_RE.search(prd_text)
    if not m:
        return ["PRD carries no fenced ```json block -- the PRD_HEADER block must be the FIRST fenced "
                "json in the file (org/standards/PRD_HEADER.schema.json)"]
    try:
        header = json.loads(m.group(1))
    except Exception as exc:  # noqa: BLE001
        return ["PRD_HEADER block does not parse as JSON (%s)" % exc]
    try:
        import jsonschema
    except ImportError:
        return ["jsonschema is not importable -- the PRD_HEADER limb cannot run; REFUSED (fail-closed)"]
    for err in sorted(jsonschema.Draft7Validator(header_schema).iter_errors(header),
                      key=lambda e: list(e.path)):
        ptr = "/" + "/".join(str(p) for p in err.path) if err.path else "/"
        out.append("PRD_HEADER violation at %s -- %s" % (ptr, err.message[:140]))
    if out:
        return out
    for key in ("project", "directive", "fabric"):
        want = expect.get(key)
        if want is not None and header.get(key) != want:
            out.append("PRD_HEADER.%s=%r but the register row says %r -- two carriers of one quantity "
                       "must agree" % (key, header.get(key), want))
    # CVO~A re-grade @d019922d68 (A): a heading INSIDE a code fence and an EMPTY heading both used to
    # satisfy this. Headings are searched with every fenced block blanked out, and the section must
    # carry a non-trivial body before the next top-level heading. Row-schema enforcement is NOT
    # widened into here -- that is step 5's contract, not this limb's.
    m_body = _top_section(prd_text, MANIFEST_HEADING_RE)
    if m_body is None:
        out.append("PRD has no top-level SURFACE MANIFEST section (a heading inside a code fence does "
                   "not count) -- step 5 cannot run a battery on prose (CVO~A @0d272d257c; contract "
                   "@4bb2c5d94f)")
    elif len(m_body.strip()) < MANIFEST_MIN_BODY_CHARS:
        # WORDING CORRECTED 2026-09-09 (3.0.0_SA_CVO~Z msg 20602): this said the section "is EMPTY",
        # which is FALSE for the case that actually trips it -- a well-formed header row plus one
        # data row measures 39 chars and is not empty at all. A true refusal carrying a false reason
        # sends the next actor to the wrong repair: a reader told EMPTY hunts for a missing section
        # when the remedy is ADD ROWS.
        out.append("SURFACE MANIFEST heading is present but the section is UNDER-POPULATED (%d "
                   "chars, floor %d). The section exists -- it needs MORE ROWS, not a new heading. "
                   "A heading is not a manifest." % (len(m_body.strip()), MANIFEST_MIN_BODY_CHARS))
    section = _top_section(prd_text, ENDPOINT_HEADING)
    if section is None:
        return out  # limb 4 owns the missing-ENDPOINT complaint; do not double-report
    defined = set(FWD_DEF_RE.findall(section))
    listed = set(header.get("endpoint_outcomes") or [])
    key = lambda s: int(s.split("-")[1])  # noqa: E731
    if defined - listed:
        out.append("ENDPOINT section DEFINES %s but PRD_HEADER.endpoint_outcomes omits them"
                   % ", ".join(sorted(defined - listed, key=key)))
    if listed - defined:
        out.append("PRD_HEADER.endpoint_outcomes lists %s but the ENDPOINT section defines no such outcome "
                   "(a mention in prose is not a definition)" % ", ".join(sorted(listed - defined, key=key)))
    return out


def check_prd_conformance(root, rel):
    """LIMB 5 wrapper: resolve the TO's project the same way limb 4 does, then grade every named PRD
    that carries an ENDPOINT section. Reads PRD and schema from the STAGED INDEX, so a PRD edited in
    the same commit is graded as it will be committed."""
    import json as _json
    code, rel_json, err = _project_row_rel(root, rel)
    if not code or err:
        return [], []
    p = os.path.join(root, rel_json)
    if not os.path.isfile(p):
        return [], []
    # CVO~A re-grade @d019922d68 (B): the project row is read from the STAGED INDEX like everything
    # else this limb compares -- a worktree read let staged directive=D9 pass against a worktree/header
    # D8. The worktree file above is used only to resolve the row; the CONTENT comes from the index.
    staged_json = _staged_blob(root, rel_json)
    if staged_json is None:
        return (["%s: %s unreadable from the staged index -- the step-4 conformance limb cannot compare "
                 "the header against the register; REFUSED (fail-closed)" % (rel, rel_json)], [])
    try:
        doc = _json.loads(staged_json)
    except Exception as exc:  # noqa: BLE001
        return (["%s: %s does not parse from the staged index (%s) -- REFUSED" % (rel, rel_json, exc)], [])
    if doc.get("dep_stage") in (None, "REGISTERED"):
        return [], []
    paths = _prd_paths(doc)
    if not paths:
        return [], []
    schema_txt = _staged_blob(root, PRD_HEADER_SCHEMA_REL)
    if schema_txt is None:
        return (["%s: %s unreadable from the staged index -- the step-4 conformance limb cannot run; "
                 "REFUSED (fail-closed)" % (rel, PRD_HEADER_SCHEMA_REL)], [])
    try:
        header_schema = _json.loads(schema_txt)
    except Exception as exc:  # noqa: BLE001
        return (["%s: %s does not parse (%s) -- REFUSED" % (rel, PRD_HEADER_SCHEMA_REL, exc)], [])
    expect = {k: doc.get(k) for k in ("project_code", "directive", "fabric")}
    expect["project"] = expect.pop("project_code")
    v, notes, graded = [], [], 0
    for rp in paths:
        rp = rp.replace("\\", "/")
        txt = _staged_blob(root, rp)
        if txt is None or _top_section(txt, ENDPOINT_HEADING) is None:
            continue  # limb 4 reports absent/unreadable/endpoint-less PRDs
        # PARENT PRD (2026-09-03, 1.0.0_SA_CTO, the ADVI_INSURE / ADVI_49F retrofits): a project's prds[] may list a
        # PARENT program PRD for context (ADVI_INSURE lists D2_ADVI_49F_E2E_PRD.md, whose header names ADVI_49F). Grading
        # that header against this project's row would refuse every child of every program PRD on identity. A listed PRD
        # whose header names ANOTHER project is graded by that project's own row and is NOTED here, not graded; a PRD with
        # no header, or a header naming THIS project, is graded exactly as before.
        _hm = PRD_FENCE_RE.search(txt)
        if _hm:
            try:
                _hp = (_json.loads(_hm.group(1)) or {}).get("project")
            except Exception:  # noqa: BLE001
                _hp = None
            if _hp and _hp != expect.get("project"):
                notes.append("%s: %s carries a PRD_HEADER for project %s (a parent or sibling PRD listed for context) -- "
                             "graded by that project's row, not this one" % (rel, rp, _hp))
                continue
        graded += 1
        for c in _prd_conformance(txt, header_schema, expect):
            v.append("%s: %s: %s" % (rel, rp, c))
    if graded:
        notes.append("%s: step-4 conformance graded %d PRD(s) with an ENDPOINT section%s"
                     % (rel, graded, "" if v else " -- OK"))
    return v, notes


def check_file(root, rel):
    """Return (violations, notes) for ONE newly-added TO file."""
    v, notes = [], []
    full = os.path.join(root, rel)
    try:
        with open(full, "r", encoding="utf-8", errors="replace") as fh:
            text = fh.read()
    except Exception as exc:  # noqa: BLE001
        return (["UNREADABLE (%s) -- refusing; a gate that cannot read its subject "
                 "must not pass it" % exc], notes)

    ov = OVERRIDE_RE.search(text)
    if ov:
        # AUDITED means WRITTEN (2026-09-03, 1.0.0_SA_CTO; spec water test cell L6.pipeline-override-audited): the
        # canonical spec said this override is "audited" while the gate only PRINTED it. The sibling issuance hook
        # appends to org/to-pos-override-audit.log; this appends to its own sink in the same shape. A sink that cannot
        # be written is a NOTE, never a refusal -- the override was already legal, the audit is the record of it.
        reason = ov.group(1).strip()
        try:
            who = subprocess.run(["git", "var", "GIT_AUTHOR_IDENT"], cwd=root, capture_output=True, text=True, encoding="utf-8", errors="replace",
                                 timeout=20).stdout.split(" <")[0].strip() or "<unknown author>"
        except Exception:  # noqa: BLE001
            who = "<unknown author>"
        import datetime as _dt
        line = "%s | %s | %s | %s\n" % (_dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%dT%H%M%SZ"), who, rel, reason)
        try:
            with open(os.path.join(root, "org", "to-pipeline-override-audit.log"), "a", encoding="utf-8") as fh:
                fh.write(line)
            notes.append("OVERRIDE taken on %s -- reason: %s (audited: org/to-pipeline-override-audit.log)" % (rel, reason))
        except Exception as exc:  # noqa: BLE001
            notes.append("OVERRIDE taken on %s -- reason: %s (AUDIT SINK UNWRITABLE: %s -- the override stands, the record does not)"
                         % (rel, reason, exc))
        # LIMB 6 IS NOT OVERRIDABLE (3.0.0_SA_CVO~O verdict @c6d6f60d62, row NFRA_OPLGTW-Z-S1): the override's written
        # scope is pipeline SHAPE (:511, :1994), and CLAUDE.md 27 L4-R names no exception. An issuer's own line must not
        # void another seat's L4-R refusal -- OG-e-1 @11657b48df was cut 84 s after a REFUSED stamp this way.
        so_v, so_notes = check_prd_signoff(root, rel)
        return (so_v, notes + so_notes)

    # THE <decomp_ref> PRESENCE CHECK IS NOT DUPLICATED HERE, DELIBERATELY.
    # .tools/git-hooks/to-proof-of-spec-check.sh:60-71 already refuses a NEW TO that lacks
    # <decomp_ref> when its project is pipeline-registered, it is WIRED into .git/hooks/pre-commit
    # (:130-131, fail-closed at :132), and it reads STAGED content via `git show :path` rather than
    # the worktree -- which is the more correct read. Two gates enforcing one predicate with two
    # different override tokens is worse than one; this file owns only what that one does not.
    # Found 2026-09-01 AFTER building a duplicate of it. Recorded rather than quietly dropped.
    m = DECOMP_RE.search(text)
    if m and NONE_WORD_RE.match(m.group(1).strip()):
        notes.append("%s: <decomp_ref> declares NONE -- allowed (one-branch work under its own "
                     "charter); layer 1 reads it as ANNOUNCE, not ENFORCE." % rel)

    # GATE (i) -- Tier-0/1 in <issued_to> on a NEW tree TO is refused (2026-09-03, @716a9bc7ce call 3).
    v.extend(_issued_to_tier_violations(rel, text))
    # GATE (vii) -- a NEW tree TO carries the machine-readable <issued_by> that a DOWNSTREAM
    # gate needs to seat its worker (2026-09-10, 2.0.0_SA_COO~ZZ msg 20981 / that lane's Z-S21).
    v.extend(_issued_by_violations(rel, text))
    # GATE (v) -- a NEW tree TO issued to a worker carries its grant, the <paths> block (RULING 1 @9ef9a40aae).
    v.extend(_worker_grant_violations(rel, text))
    # GATE (viii) -- a NEW tree TO DECLARES its placeholder substitution set, which is what ARMS the
    # invocation-alignment limb of proof-of-spec-check.py on the issuance being cut (1.0.0_SA_CTO ruling D,
    # cell FE-s-28). Opt-in enforcement is armed by the party the check exists to catch.
    v.extend(_placeholder_declaration_violations(rel, text))
    # GATE (xi) -- a NEW tree TO carries a line-anchored <status> element, not born terminal
    # (row AMGT_RESAPP-Z-S153; cell AMGT-rk-56).
    v.extend(_status_element_violations(rel, text))
    # GATE (xii) -- a NEW tree TO declares its <risk> class, never below the floor its paths and invocations imply.
    v.extend(_risk_violations(rel, text))
    # GATE (iv) -- a NEW tree TO commits only under 2.0.0_SA_COO (LD-0521 A3).
    v.extend(_issuer_identity_violations(rel, _committer_serial(root)))
    # CELL REFERENCES resolve against the named decomposition at the cut (S5's class, 2026-09-03).
    _cv, _cn = _cell_refs_violations(root, rel, text)
    v.extend(_cv)
    notes.extend(_cn)
    # spine v3.0 L6 carrier 4: one clause per criterion on a NEW tree order.
    v.extend(_criterion_grammar_violations(rel, text))
    # GATE (ix) -- a criterion whose bar its named tool can never print is refused; what the limb cannot
    # evaluate is ANNOUNCED (FE-s-36, 1.0.0_SA_CTO ruling N, row S55). See the block comment at OV_TAG.
    _ov_v, _ov_n = _output_vocabulary_violations(root, rel, text)
    v.extend(_ov_v)
    notes.extend(_ov_n)

    # LAYER 3's teeth -- and this is what ACTIVATES the sibling gate above. That gate fires only
    # when the project is "pipeline-registered", whose predicate is `dep_stage` present in the
    # project JSON. MEASURED 2026-09-01: 316 of 349 projects have no dep_stage, so the sibling is
    # inert on 90% of the estate. Requiring the stage is the missing keystone, not the decomp_ref
    # check -- that was already built.
    v.extend(check_project_stage(root, rel))

    # LIMB 4 -- the mandatory ENDPOINT section (Andrew-direct 2026-09-01 via 92478). See
    # check_endpoint_section for the authorization, the routing argument, and what it CANNOT check.
    ep_v, ep_notes = check_endpoint_section(root, rel)
    v.extend(ep_v)
    notes.extend(ep_notes)
    # LIMB 5 -- step-4 conformance (Andrew-direct 2026-09-02 CALL 2): one more limb on THIS gate.
    pc_v, pc_notes = check_prd_conformance(root, rel)
    v.extend(pc_v)
    notes.extend(pc_notes)
    # LIMB 6 -- the PRD sign-off gate (Andrew-direct 2026-09-10 ~21:2xZ; spine v3.14 L4-R): both reviewers
    # SIGNED at the PRD's current prd_version, or no task order is cut against it.
    so_v, so_notes = check_prd_signoff(root, rel)
    v.extend(so_v)
    notes.extend(so_notes)

    pm = PREFLIGHT_RE.search(text)
    if not pm:
        v.append("%s: NO <preflight> block. Stage 3 must record comp-schedule, comp-iam and "
                 "comp-adversary, each RUN or DECLARED-NOT-APPLICABLE with a reason "
                 "(Andrew-direct 2026-09-01)." % rel)
    else:
        for p in _check_preflight(pm.group(1)):
            v.append("%s: %s" % (rel, p))
    return (v, notes)


STATUS_RE = re.compile(r"<status>\s*([A-Za-z_-]+)", re.I)
STATUS_LINE_RE = re.compile(r"^[ \t]*<status>\s*([A-Za-z_-]+)", re.I | re.M)
DONE_WORDS = ("complete", "completed", "closed", "done")
# THE LAST TAG GOVERNS (1.0.0_SA_CTO gate-owner ruling, msg 107528, 2026-10-09): an order's status is its LAST
# line-anchored <status> tag. A stale earlier duplicate (pending above complete) must not read as the status.
# A change that only REMOVES an earlier duplicate while the last tag is unchanged is NOT a flip.


def _last_status(text):
    """(word or None, count of line-anchored tags). The LAST line-anchored tag; with none, the old first-match read."""
    found = list(STATUS_LINE_RE.finditer(text or ""))
    if found:
        return found[-1].group(1).lower(), len(found)
    m = STATUS_RE.search(text or "")
    return (m.group(1).lower() if m else None), 0


def _is_terminal_flip(head_text, staged_text):
    """(terminal word or None). None = not a flip this limb grades. PURE.

    A staged order whose last tag is terminal is graded, EXCEPT when HEAD's last tag is the same word and the change
    removed one or more earlier tags (a stale duplicate deleted; ruling msg 107528)."""
    word, n_staged = _last_status(staged_text)
    if word not in DONE_WORDS:
        return None
    if head_text is not None:
        head_word, n_head = _last_status(head_text)
        if head_word == word and n_staged < n_head:
            return None
    return word


_REDACT_ID_RE = re.compile(r"(?<![A-Za-z0-9-])[A-Za-z0-9-]*\d[A-Za-z0-9-]*(?![A-Za-z0-9-])")
_REDACT_TOKEN_RE = re.compile(r"acct#[0-9a-f]{8}")
_REDACT_MARK_RE = re.compile(r"\[redacted\]", re.IGNORECASE)
_REDACT_PH = "<<ID>>"


_REDACT_STRIP = ",;:.()[]'\"*`"
_REDACT_ANY_MARK_RE = re.compile(r"acct#[0-9a-f]{8}|\[redacted\]", re.IGNORECASE)
_REDACT_ID_PAT = r"[A-Za-z0-9-]*\d[A-Za-z0-9-]*"


def _redact_marker(tok):
    """True when a staged token (punctuation, markdown and a trailing 's stripped) is a redaction marker."""
    t = tok[:-2] if tok.endswith("'s") else tok
    t = t.strip(_REDACT_STRIP)
    return bool(_REDACT_TOKEN_RE.fullmatch(t)) or t.lower() == "redacted"


def _redaction_line_ok(head_line, staged_line):
    """True when staged_line is head_line with digit-bearing tokens replaced by acct#<8hex> or [redacted], or removed. PURE.

    Marker-anchored (dell2 2.0.0_SA_COO~C2 msg 3813 via 0.0.0_AB_MSTR 108061): each marker in the staged line stands where ONE
    digit-bearing token stood in HEAD, and every other character must match exactly -- so a date or a ratio left untouched beside a
    swapped id still compares equal, and markdown or a possessive around the marker is literal text on both sides."""
    if head_line == staged_line:
        return True
    parts = _REDACT_ANY_MARK_RE.split(staged_line)
    if len(parts) > 1 and re.fullmatch(_REDACT_ID_PAT.join(re.escape(p) for p in parts), head_line):
        return True
    # Figures removed outright: every head token is kept, replaced by a marker, or (only if it carries a digit) dropped.
    ht, sti = head_line.split(), staged_line.split()
    j = 0
    for tok in ht:
        has_digit = any(c.isdigit() for c in tok)
        if j < len(sti) and (sti[j] == tok or (has_digit and _redact_marker(sti[j]))):
            j += 1
        elif has_digit:
            continue
        else:
            return False
    return j == len(sti)


def _is_pure_redaction(head_text, staged_text):
    """True when staged differs from HEAD ONLY by redaction: id tokens -> acct#<8hex> or [redacted], digit figures removed, or whole
    lines deleted. No line added, no other word changed. PURE. dell2 containment ruling @0e8209c33c; 1.0.0_SA_CTO path (b), 2026-10-09."""
    import difflib
    if head_text is None or staged_text is None or head_text == staged_text:
        return False
    a, b = head_text.split("\n"), staged_text.split("\n")
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
        if op in ("equal", "delete"):
            continue
        if op == "insert":
            return False
        # replace: each staged line must be a redaction of a DISTINCT head line, in order; unmatched head lines read as deleted.
        i = i1
        for j in range(j1, j2):
            while i < i2 and not _redaction_line_ok(a[i], b[j]):
                i += 1
            if i >= i2:
                return False
            i += 1
    return True


def _lf(text):
    """Normalise line endings on read (CRLF and a lone CR -> LF); the element regexes end a tab-or-space star dollar and cannot match before a CR."""
    return text.replace("\r\n", "\n").replace("\r", "\n")


def _head_blob(root, rel):
    """The HEAD content of rel, or None (a new file, or unreadable)."""
    try:
        out = subprocess.run(["git", "show", "HEAD:" + rel], cwd=root, capture_output=True, timeout=30)
    except Exception:  # noqa: BLE001
        return None
    return _lf(out.stdout.decode("utf-8", errors="replace")) if out.returncode == 0 else None


def _staged_blob(root, rel):
    """The STAGED content of rel, or None. Reading the index -- not the worktree -- is the
    correct read: a seat can stage a conformant file and then edit the worktree copy. The
    sibling gate at .tools/git-hooks/to-proof-of-spec-check.sh does this and mine did not."""
    try:
        out = subprocess.run(["git", "show", ":" + rel], cwd=root,
                             capture_output=True, timeout=30)
    except Exception:  # noqa: BLE001
        return None
    if out.returncode != 0:
        return None
    return _lf(out.stdout.decode("utf-8", errors="replace"))


# The order's own <proof_of_spec> block may NAME its instance (row IRPT_BCKEND-W42-S4, 1.0.0_SA_CTO ruling): an
# instance keyed off the to_id rather than the file stem is otherwise invisible to the stem search.
# NOTE: THE TAG ONLY ADDS A CANDIDATE, IT NEVER REFUSES (amended after a census: the first form refused 11 in-flight
# orders whose blocks also cite the schema, template glob text or a non-instance file). Only a LITERAL backticked path
# whose basename is an instance name counts; it is used when exactly one such path exists on disk inside the
# deliverables dir the stem search reads. Every other case falls back to the stem search exactly as before.
PROOF_BLOCK_RE = re.compile(r"^[ \t]*<proof_of_spec>(.*?)</proof_of_spec>", re.M | re.S)
PROOF_PATH_RE = re.compile(r"`([^`\s]+)`")
PROOF_INSTANCE_SUFFIXES = (".proof_of_spec.json", "_PROOF_OF_SPEC.json")


def _proof_tag_instances(root, staged, deliv):
    """The literal instance paths the <proof_of_spec> block names that exist on disk inside `deliv`."""
    block = PROOF_BLOCK_RE.search(staged or "")
    if not block:
        return []
    base = os.path.normpath(os.path.join(root, *deliv.split("/")))
    found = set()
    for named in PROOF_PATH_RE.findall(block.group(1)):
        if any(ch in named for ch in "*<>") or not posixpath.basename(named).endswith(PROOF_INSTANCE_SUFFIXES):
            continue
        path = os.path.normpath(os.path.join(root, *named.split("/")))
        try:
            inside = os.path.normcase(os.path.commonpath([path, base])) == os.path.normcase(base)
        except ValueError:  # a different drive is never inside
            inside = False
        if inside and os.path.isfile(path):
            found.add(path)
    return sorted(found)


def _proof_instance_candidates(root, rel, staged):
    """(candidate paths, None) for the order `rel` whose staged text is `staged`: the tag-named instance when exactly
    one exists, otherwise the stem search as before. The second element is always None -- the tag never refuses."""
    stem = os.path.basename(rel).rsplit(".md", 1)[0]
    names = (stem + ".proof_of_spec.json", stem + "_PROOF_OF_SPEC.json")
    to_dir = os.path.dirname(rel).replace("\\", "/")
    tree = to_dir.endswith("/task-orders")
    deliv = (to_dir[:-len("/task-orders")] + "/deliverables") if tree else to_dir.replace("task_orders", "deliverables")
    tagged = _proof_tag_instances(root, staged, deliv)
    if len(tagged) == 1:
        return tagged, None
    if tree:
        import glob as _glob
        found = [c for n in names
                 for c in _glob.glob(os.path.join(root, to_dir[:-len("/task-orders")], "deliverables", "*", n))]
        return _newest_instance_only(root, found), None
    return [os.path.join(root, to_dir.replace("task_orders", "deliverables"), n) for n in names], None


def _newest_instance_only(root, found):
    """The instances to grade. INERT unless armed (flag file org/mcp/proof-newest-instance.enforce, or PROOF_NEWEST_INSTANCE=1):
    unarmed, `found` comes back unchanged, in the glob's own order, and the first one that exists is graded as it always was.
    Armed, with two or more, the ONE newest by .tools/proof_instance_select.py (uncommitted, then latest commit time, then ~N)."""
    import importlib.util
    helper = os.path.join(os.path.dirname(os.path.abspath(__file__)), "proof_instance_select.py")
    if not os.path.isfile(helper):
        return found   # this script was copied away from .tools (a test, a mutant control): grade as before, never crash
    spec = importlib.util.spec_from_file_location("proof_instance_select", helper)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.select(root, found)


def check_complete_flip(root, rel):
    """LAYER 1, half B -- 'No VALID instance -> no complete flip.'

    The pipeline doc's layer 1 says an instance is INVALID without a decomp_ref + bidirectional
    mapping, AND that no VALID instance means no `complete` flip. The FIRST half is built and
    lives in proof-of-spec-check.py's alignment arms. The SECOND half -- the thing that actually
    stops the flip -- was never wired to anything. This is that wire.

    SCOPED to pipeline-registered projects (dep_stage present), the same predicate the sibling
    decomp_ref gate uses. Old projects close freely: gating every historical close on an instance
    that never existed would refuse legitimate housekeeping and get the gate disabled wholesale.
    """
    staged = _staged_blob(root, rel)
    if staged is None:
        return []  # not staged (or unreadable as a blob) -- other arms own that
    if rel in _staged_redaction_renames(root):
        print("NOTE: %s: a pure redaction RENAME of a terminal order (byte-identical content); not re-graded as a flip." % rel,
              file=sys.stderr)
        return []
    head = _head_blob(root, rel)
    flip_word = _is_terminal_flip(head, staged)
    if flip_word is None:
        return []  # not a flip to a terminal state (or only a stale earlier duplicate removed; ruling msg 107528)
    # PATH (b), 1.0.0_SA_CTO 2026-10-09 (dell2 containment ruling @0e8209c33c; relay msg 108054): an order ALREADY terminal at HEAD
    # whose change is ONLY a redaction of client account data is not a new flip. Its instance was graded at the original flip, and the
    # containment moved its artifacts out of the repo, so re-grading it would refuse the very redaction that removes the data.
    if head is not None and _last_status(head)[0] == flip_word and _is_pure_redaction(head, staged):
        print("NOTE: %s: already '%s' at HEAD and the change is a pure redaction (id -> acct#<8hex>/[redacted], figures or lines "
              "removed); not re-graded as a flip." % (rel, flip_word), file=sys.stderr)
        return []

    import json
    code, rel_json, err = _project_row_rel(root, rel)
    if not code or err:
        return []
    p = os.path.join(root, rel_json)
    cand = code  # the message below names the project by CODE
    if not os.path.isfile(p):
        return []
    try:
        with open(p, "r", encoding="utf-8") as fh:
            if json.load(fh).get("dep_stage") is None:
                return []  # not pipeline-registered -- out of scope by design
    except Exception:  # noqa: BLE001
        return []

    # Pipeline-registered AND flipping terminal: the instance must exist and be VALID.
    # FLAT: <seat>/deliverables/<TO>.proof_of_spec.json beside <seat>/task_orders/. TREE (ruled
    # 2026-09-02, s.6 option ii): deliverables/<serial>/ sub-folders, the owner in the path -- so the
    # instance is searched one level down, under whichever serial the TO assigned.
    cands, refused = _proof_instance_candidates(root, rel, staged)
    if refused:
        return [refused]
    inst = None
    for cand_path in cands:
        if os.path.isfile(cand_path):
            inst = cand_path
            break
    if inst is None:
        return ["%s: flips to '%s' on PIPELINE-REGISTERED project %s, and NO proof-of-spec "
                "instance was found beside it. Layer 1: no VALID instance, no complete flip."
                % (rel, flip_word, cand)]
    chk = os.path.join(root, ".tools", "proof-of-spec-check.py")
    if not os.path.isfile(chk):
        return ["%s: proof-of-spec-check.py is MISSING -- fail-closed rather than pass a flip "
                "whose validator cannot run" % rel]
    # THE GOVERNING ORDER IS THE ORDER BEING FLIPPED (FE-s-37; 1.0.0_SA_CTO RULING S @942e4ff992 s.2; row
    # IRPT_FNTEND-S61). This call used to hand the checker the instance ALONE, and the checker then read its governing
    # order from the instance's own decomp_ref.to_ref -- a field the graded party writes -- so pointing to_ref at a real
    # pre-ruling order moved the count-bar and drives limbs to LEGACY and nothing named the mismatch. The flip knows
    # which order it closes; it says so, and the checker binds every limb to it and refuses an instance whose to_ref or
    # to_id names another order, before any limb runs.
    try:
        r = subprocess.run(["python", chk, inst, "--governing-order", rel], cwd=root,
                           capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=180)
    except Exception as exc:  # noqa: BLE001
        return ["%s: could not run the validator (%s) -- fail-closed" % (rel, exc)]
    if r.returncode != 0:
        head = (r.stdout or r.stderr or "").strip().splitlines()
        why = head[-1][:160] if head else "rc=%d" % r.returncode
        out = ["%s: flips to '%s' but its instance is NOT VALID (rc=%d) -- %s"
               % (rel, flip_word, r.returncode, why)]
        # NAME WHAT REFUSED, not only the verdict line: the verdict reads "INVALID (rc=1)" for every cause, so a seat
        # reading this refusal could not tell a binding refusal from any other (FE-s-37).
        viol = [ln.strip()[len("VIOLATION: "):] for ln in (r.stdout or "").splitlines()
                if ln.strip().startswith("VIOLATION: ")]
        out.extend("%s: instance VIOLATION: %s" % (rel, x[:700]) for x in viol[:12])
        if len(viol) > 12:
            out.append("%s: ... and %d more instance violation(s) -- run the checker on %s to read them"
                       % (rel, len(viol) - 12, os.path.relpath(inst, root).replace("\\", "/")))
        return out
    return []


def sweep(root):
    """LAYER 3's reporting half -- COO's TO sweep as an instrumented pass, not a heroic one.

    Read-only. Prints the dep_stage distribution with its denominator so the pipeline's own
    machine-readable stage is measurable rather than asserted. Never refuses; rc is always 0.
    """
    import glob as _glob
    import json
    files = sorted(_glob.glob(os.path.join(root, "org", "projects", "*.json")))
    counts, unreadable = {}, 0
    fabric_counts = {}
    for f in files:
        try:
            with open(f, "r", encoding="utf-8") as fh:
                doc = json.load(fh)
            st = doc.get("dep_stage")
            fb = doc.get("fabric")
        except Exception:  # noqa: BLE001
            unreadable += 1
            continue
        key = "<ABSENT>" if st is None else str(st)
        counts[key] = counts.get(key, 0) + 1
        fkey = "<ABSENT>" if fb is None else str(fb)
        fabric_counts[fkey] = fabric_counts.get(fkey, 0) + 1
    total = len(files)
    print("[to-pipeline-gate --sweep] dep_stage across org/projects/")
    print("  DENOMINATOR: %d project JSON(s), %d unreadable" % (total, unreadable))
    for k in sorted(counts, key=lambda x: (-counts[x], x)):
        flag = "  <- not in the ratified enum" if (
            k != "<ABSENT>" and k not in DEP_STAGE_ENUM) else ""
        print("    %-16s %4d  (%.1f%%)%s" % (k, counts[k], 100.0 * counts[k] / max(total, 1), flag))
    absent = counts.get("<ABSENT>", 0)
    print("  NOTE: <ABSENT> is FORWARD-ONLY by ruling -- these are NOT back-filled. The gate "
          "populates the enum as NEW TOs are cut, never retroactively.")
    print("  Projects that cannot take a new TO until their stage is declared: %d" % absent)
    print()
    print("[to-pipeline-gate --sweep] fabric across org/projects/  (step-3 laptop-vs-site-Z fork)")
    print("  DENOMINATOR: %d project JSON(s), %d unreadable" % (total, unreadable))
    fabric_ok = _fabric_values()
    for k in sorted(fabric_counts, key=lambda x: (-fabric_counts[x], x)):
        flag = "  <- not in the ratified enum" if (
            k != "<ABSENT>" and k.strip().lower() not in fabric_ok) else ""
        print("    %-16s %4d  (%.1f%%)%s"
              % (k, fabric_counts[k], 100.0 * fabric_counts[k] / max(total, 1), flag))
    fabsent = fabric_counts.get("<ABSENT>", 0)
    print("  Projects that cannot take a new TO until their fabric is declared: %d" % fabsent)
    return 0


_GATE_TAG = "to-pipeline-gate"

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


def _merge_in_progress(root):
    """True iff a merge is in progress -- MERGE_HEAD exists.

    MERGE_HEAD *ONLY*. Do NOT add "HEAD has two parents" as a second condition: in a PRE-COMMIT
    hook HEAD is the PREVIOUS commit, so a two-parent-HEAD test silently exempts the next ORDINARY
    commit after any merge, for every agent. owned-paths-check.sh:69-75 carries that finding and it
    was caught by exercising the hook while HEAD happened to be a merge.

    `--git-path` rather than "$GIT_DIR/MERGE_HEAD": a linked worktree keeps its own.
    """
    try:
        p = subprocess.run(["git", "rev-parse", "--git-path", "MERGE_HEAD"], cwd=root,
                           capture_output=True, text=True)
        if p.returncode != 0:
            return False
        return os.path.isfile(os.path.join(root, p.stdout.strip()))
    except Exception:  # noqa: BLE001
        return False


def _rounds_cli(root, args):
    """`--rounds <CODE>` -- read-only, GATE (x)'s own census, the read the COO runs before cutting a
    round. Prints, for `<CODE>`'s TREE task orders TRACKED AT HEAD: one line per round with its
    order count, the unrounded count, and the denominator ("N order(s) at HEAD"). rc 0 always -- an
    informational read, not an enforcement decision; a census that could not run says so and still
    returns 0 rather than blocking a read nobody staged anything against."""
    idx = args.index("--rounds")
    if idx + 1 >= len(args):
        print("[to-pipeline-gate --rounds] needs a <CODE> argument, e.g. --rounds AMGT_RESAPP")
        return 0
    code = args[idx + 1]
    rounds, unrounded, total = _head_rounds_for_project(root, code)
    if rounds is None:
        print("[to-pipeline-gate --rounds] could not read tree orders for %s at HEAD (git ls-files "
              "failed) -- 0 order(s) at HEAD." % code)
        return 0
    for k in sorted(rounds, key=lambda k: (k[1], k[0]) if isinstance(k, tuple) else (k, "")):
        print("%s: %d order(s)" % (_round_key_label(k), len(rounds[k])))
    print("unrounded: %d order(s)" % unrounded)
    print("%d order(s) at HEAD" % total)
    return 0


def _status_census(root, code):
    """({"with": [order,...], "without": [order,...], "words": {word:int}}, total) for `code`'s TREE
    task orders TRACKED AT HEAD, read with `git ls-files` + `git show HEAD:<path>` -- never the
    worktree (the same shape as _head_rounds_census). (None, 0) when the census could not run."""
    try:
        ls = subprocess.run(["git", "ls-files", "--", "org/missions/D*/*/%s/task-orders/*.md" % code],
                            cwd=root, capture_output=True, text=True, encoding="utf-8", errors="replace",
                            timeout=60)
    except Exception:  # noqa: BLE001
        return None, 0
    if ls.returncode != 0:
        return None, 0
    paths = sorted({p.strip().replace("\\", "/") for p in ls.stdout.splitlines() if p.strip()})
    with_status, without_status, words = [], [], {}
    for p in paths:
        text = _head_blob(root, p)
        m = STATUS_ELEMENT_RE.search(text) if text is not None else None
        if m:
            with_status.append(p)
            w = m.group(1).lower()
            words[w] = words.get(w, 0) + 1
        else:
            without_status.append(p)
    return {"with": with_status, "without": without_status, "words": words}, len(paths)


def _status_census_cli(root, args):
    """`--status-census <CODE>` -- read-only, GATE (xi)'s own census (row AMGT_RESAPP-Z-S153; cell
    AMGT-rk-56). Prints, for `<CODE>`'s TREE task orders TRACKED AT HEAD: orders WITH a
    line-anchored <status> element (count), orders WITHOUT (each named), the status-word
    distribution, and the denominator ("N order(s) at HEAD"). rc 0 always -- an informational read,
    not an enforcement decision, the same shape as --rounds."""
    idx = args.index("--status-census")
    if idx + 1 >= len(args):
        print("[to-pipeline-gate --status-census] needs a <CODE> argument, e.g. --status-census AMGT_RESAPP")
        return 0
    code = args[idx + 1]
    census, total = _status_census(root, code)
    if census is None:
        print("[to-pipeline-gate --status-census] could not read tree orders for %s at HEAD (git "
              "ls-files failed) -- 0 order(s) at HEAD." % code)
        return 0
    print("WITH a line-anchored <status> element: %d" % len(census["with"]))
    print("WITHOUT a line-anchored <status> element: %d" % len(census["without"]))
    for p in sorted(census["without"]):
        print("  %s" % os.path.basename(p))
    print("word distribution:")
    for w in sorted(census["words"], key=lambda x: (-census["words"][x], x)):
        print("  %-16s %4d" % (w, census["words"][w]))
    print("%d order(s) at HEAD" % total)
    return 0


def main(argv):
    root = _repo_root()
    if "--sweep" in argv[1:]:
        return sweep(root)
    if "--self-test" in argv[1:]:
        return _self_test()
    if "--rounds" in argv[1:]:
        return _rounds_cli(root, argv[1:])
    if "--status-census" in argv[1:]:
        return _status_census_cli(root, argv[1:])

    # ⛔ MERGE EXEMPTION (2026-09-04, 1.0.0_SA_CTO on 0.0.0_AB_MSTR's 94264). A MERGE IS NOT
    # AUTHORSHIP. This gate had none while BOTH its siblings did -- owned-paths-check.sh:85 and
    # surprise-row-gate.py -- so it graded the INTEGRATOR as the author of every task order any
    # merge carried. Measured on the first cross-fabric reconcile: 27 of site Z's ALREADY-COMMITTED
    # orders (each verified present at origin/SITEZ with `git cat-file -e`) were refused as "a NEW
    # tree task order committed under 0.0.0_AB_MSTR", plus 153 criterion-grammar refusals because
    # their fabric's orders are v2 and ours is v3. THAT BLOCKED EVERY CROSS-FABRIC RECONCILE THAT
    # CARRIES A TASK ORDER, which from now on is all of them.
    #
    # AND THE VERSION-SKEW HALF IS A RULING, NOT A SIDE EFFECT: the spine's own transition rule is
    # that a round open at an amendment finishes under the task orders ALREADY CUT. v3's criterion
    # grammar binds orders cut AFTER v3; it does not retro-refuse orders that were valid when and
    # where they were written. A merge is exactly the moment that rule has to hold, so the exemption
    # IS the mechanism for it rather than a hole beside it.
    #
    # ⛔ NOT CONDITIONED ON HOW THE STAGED LIST WAS SOURCED. owned-paths-check.sh:76-84 shipped that
    # guard and it KILLED the exemption in production -- the active pre-commit hoists the staged list
    # into an env var, so the guard's condition was always false in a real run and true only on the
    # direct-invocation path the author tested. A MERGE IS A MERGE REGARDLESS OF HOW THE STAGED LIST
    # WAS SOURCED.
    #
    # RESIDUAL, STATED RATHER THAN PAPERED OVER: a merge can carry a task order that was never gated
    # anywhere (a branch on which no hook ran). This exemption admits that case, exactly as both
    # siblings do. The control for it is the DRAIN's refuser (safe-merge.sh), which grades the merged
    # index before the merge commits -- not this gate, which cannot tell a fresh order from an
    # already-landed one once both are simply "staged".
    if _merge_in_progress(root):
        print("[to-pipeline-gate] OK: MERGE COMMIT -- task-order checks exempt; merged orders were "
              "gated at their own authorship, on their own fabric's spine version "
              "(0.0.0_AB_MSTR 94264; siblings owned-paths-check.sh:85, surprise-row-gate.py).")
        return 0

    added = _newly_added(root)
    if added is None:
        print("[to-pipeline-gate] REFUSED: could not read the staged index. Fail-closed.",
              file=sys.stderr)
        return 1

    # Consider only paths the caller dispatched AND that git says are newly added.
    _disp, _src = _dispatched_from_argv_or_env(argv[1:])
    dispatched = [a.replace("\\", "/") for a in _disp]
    targets = sorted(p for p in dispatched
                     if TO_PATH_RE.search(p) and p in added)

    any_to = [p for p in dispatched if TO_PATH_RE.search(p)]
    if not targets and not any_to:
        print("[to-pipeline-gate] OK: no task_orders/*.md in this commit "
              "(denominator: %d dispatched path(s), %d staged-added)."
              % (len(dispatched), len(added)))
        return 0

    all_v, all_notes = [], []
    for rel in targets:
        v, notes = check_file(root, rel)
        all_v.extend(v)
        all_notes.extend(notes)
    # spine v3.0 L6 carrier 1: ONE issuance covers EVERY cell -- graded over the staged set, not per file.
    if targets:
        _cov_v, _cov_n = _coverage_violations(root, targets)
        _cov_v.extend(_carrier2_violations(root, targets))
        all_v.extend(_cov_v)
        all_notes.extend(_cov_n)

    # GATE (x) -- ONE ISSUER PER ROUND, keyed to the ROUND (row AMGT_RESAPP-Z-S154; Rule 27; cell
    # AMGT-rk-55). A NEWLY-ADDED tree order names its round, and a second issuance into a round that
    # already has one at HEAD is refused with every colliding order named. Flat-root orders are not
    # graded (_round_issuer_violations returns [] on them); the census is cached once per project code.
    for rel in targets:
        m_code = TREE_TO_RE.search(rel)
        if not m_code:
            continue
        try:
            with open(os.path.join(root, rel), "r", encoding="utf-8", errors="replace") as fh:
                rtext = fh.read()
        except Exception:  # noqa: BLE001
            continue  # already refused as UNREADABLE by check_file above
        head_rounds, _unrounded, _total = _head_rounds_for_project(root, m_code.group(5))
        if head_rounds is None:
            all_notes.append("GATE (x): round census for %s could not run (git ls-files failed) -- "
                             "the round-issuer limb did not grade %s." % (m_code.group(5), rel))
            continue
        all_v.extend(_round_issuer_violations(rel, rtext, head_rounds))

    # LAYER 1 half B runs on EVERY staged TO, added or modified -- a `complete` flip is almost
    # always a MODIFY, so scoping this to newly-added (as layers 2/3 correctly are) would make it
    # structurally unable to ever fire. Different question, different scope, stated so the
    # asymmetry reads as deliberate rather than as an oversight.
    flip_targets = sorted(p for p in dispatched if TO_PATH_RE.search(p))
    for rel in flip_targets:
        all_v.extend(check_complete_flip(root, rel))

    # GATE (viii) ON A MODIFY (FE-s-29 limb 4; Andrew-direct card 6, record @e2210bf34c): a tree TO staged as
    # MODIFIED is graded by the <placeholders> limb ONLY IF it already declares the element at HEAD. The
    # staged bytes are read from the INDEX (never the worktree), and HEAD decides "already declares".
    modified = _staged_modified(root)
    if modified is None:
        print("[to-pipeline-gate] REFUSED: could not read the staged index for modified orders. Fail-closed.",
              file=sys.stderr)
        return 1
    mod_targets = sorted(p for p in dispatched if TREE_TO_RE.search(p) and p in modified)
    n_mod_graded = 0
    for rel in mod_targets:
        head = _head_blob(root, rel)
        if head is not None and PLACEHOLDERS_TAG_RE.search(head) is not None:
            n_mod_graded += 1
        all_v.extend(_placeholder_modify_violations(rel, head, _staged_blob(root, rel)))
    if mod_targets:
        all_notes.append("GATE (viii) on a modify: %d of %d staged-MODIFIED tree order(s) already declare "
                         "<placeholders> at HEAD and were graded; the other %d do not and are not graded "
                         "(Andrew-direct card 6)." % (n_mod_graded, len(mod_targets), len(mod_targets) - n_mod_graded))

    for n in all_notes:
        print("[to-pipeline-gate] NOTE: %s" % n)

    if all_v:
        print("[to-pipeline-gate] REFUSED -- %d violation(s) across %d newly-added TO file(s) and %d modified "
              "declaring TO file(s):" % (len(all_v), len(targets), n_mod_graded), file=sys.stderr)
        for x in all_v:
            print("    %s" % x, file=sys.stderr)
        print("  FIX: add the two blocks to the TO face, or -- if this TO genuinely stands "
              "outside the pipeline -- add a line '# pipeline-override: <reason>' "
              "(audited, and it prints).", file=sys.stderr)
        return 1

    print("[to-pipeline-gate] OK: %d newly-added TO file(s) carry <decomp_ref> and a complete "
          "<preflight> block." % len(targets))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv))
    except Exception as exc:  # noqa: BLE001
        print("[to-pipeline-gate] REFUSED: unexpected error (%s). Fail-closed." % exc,
              file=sys.stderr)
        sys.exit(1)
