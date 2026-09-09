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

THE THREE-VALUE PREFLIGHT ENUM, AND WHY NOT TWO
  RUN | DECLARED-NOT-APPLICABLE | (absent -> refused). A two-value RUN/SKIPPED enum forces a
  genuinely-inapplicable tool to be recorded as SKIPPED -- a vocabulary with no not-applicable
  value encodes non-application as a violation. Eight instances of that class were measured on
  2026-09-01 alone.

FAIL-CLOSED. An unreadable file, an unparseable block or an unexpected exception REFUSES.
A gate that fails open is not a gate.
"""
import os
import inspect
import re
import pathlib
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
FABRIC_ENUM = ("laptop", "site-z")

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


def _coverage_gap(decomp_text, owned_union):
    """PURE. (missing, unknown, ids): the decomposition's cell ids no staged order owns, the owned ids the decomposition
    lacks, and the decomposition's id set."""
    ids = set(CELL_ID_RE.findall(decomp_text or ""))
    owned = set(owned_union)
    return sorted(ids - owned), sorted(owned - ids), ids


def _coverage_groups(root, targets):
    """I/O half: {(code, rel_json, doc): [owned cell ids...]} over the NEWLY ADDED tree task orders."""
    groups = {}
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
    return groups


def _coverage_grade(groups, stage_of, decomp_of):
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
        if missing:
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
    return _coverage_grade(_coverage_groups(root, targets),
                           lambda code, rel_json: _row_stage_at(root, rel_json, "HEAD"),
                           lambda doc: _decomp_text(root, doc)[0])


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
    arms = [
        ("coverage RED: two orders own a-1, a-2 of three -> refused naming CE-a-3",
         lambda: any("MISSING: CE-a-3" in x for x in grade(["CE-a-1", "CE-a-2"])[0])),
        ("coverage GREEN: three cells owned -> admitted, coverage noted 3 of 3",
         lambda: grade(["CE-a-1", "CE-a-2", "CE-a-3"])[0] == [] and any("3 of 3" in n for n in grade(["CE-a-1", "CE-a-2", "CE-a-3"])[1])),
        ("coverage NOT GRADED at EXECUTING (a recut): admitted, noted",
         lambda: grade(["CE-a-1"], stage="EXECUTING")[0] == [] and any("not graded" in n for n in grade(["CE-a-1"], stage="EXECUTING")[1])),
        ("coverage NOT GRADED when the decomposition is unreadable: admitted, noted",
         lambda: grade(["CE-a-1"], text=None)[0] == []),
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
    issuance. A modification (M) does not: this gate never refuses an existing TO.
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
        if code.startswith("A") or code.startswith("R"):
            added.add(path)
    return added


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
    if fabric is None:
        return ["%s: project %s declares NO fabric. Step 3 requires the laptop-vs-site-Z call to "
                "be MADE and RECORDED before a TO is cut against it. Set \"fabric\" to one of: %s"
                % (rel, cand, " | ".join(FABRIC_ENUM))]
    if str(fabric).strip().lower() not in FABRIC_ENUM:
        return ["%s: project %s has fabric=%r, which is NOT in the ratified enum (%s)"
                % (rel, cand, fabric, " | ".join(FABRIC_ENUM))]
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
    elif len(m_body.strip()) < 40:
        out.append("SURFACE MANIFEST heading is present but the section is EMPTY (%d chars). A "
                   "heading is not a manifest." % len(m_body.strip()))
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
        return ([], notes)

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
    # GATE (v) -- a NEW tree TO issued to a worker carries its grant, the <paths> block (RULING 1 @9ef9a40aae).
    v.extend(_worker_grant_violations(rel, text))
    # GATE (iv) -- a NEW tree TO commits only under 2.0.0_SA_COO (LD-0521 A3).
    v.extend(_issuer_identity_violations(rel, _committer_serial(root)))
    # CELL REFERENCES resolve against the named decomposition at the cut (S5's class, 2026-09-03).
    _cv, _cn = _cell_refs_violations(root, rel, text)
    v.extend(_cv)
    notes.extend(_cn)
    # spine v3.0 L6 carrier 4: one clause per criterion on a NEW tree order.
    v.extend(_criterion_grammar_violations(rel, text))

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
DONE_WORDS = ("complete", "completed", "closed", "done")


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
    return out.stdout.decode("utf-8", errors="replace")


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
    m = STATUS_RE.search(staged)
    if not m or m.group(1).lower() not in DONE_WORDS:
        return []  # not a flip to a terminal state

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
    stem = os.path.basename(rel).rsplit(".md", 1)[0]
    names = (stem + ".proof_of_spec.json", stem + "_PROOF_OF_SPEC.json")
    to_dir = os.path.dirname(rel).replace("\\", "/")
    if to_dir.endswith("/task-orders"):
        import glob as _glob
        cands = [c for n in names
                 for c in _glob.glob(os.path.join(root, to_dir[:-len("/task-orders")], "deliverables", "*", n))]
    else:
        cands = [os.path.join(root, to_dir.replace("task_orders", "deliverables"), n) for n in names]
    inst = None
    for cand_path in cands:
        if os.path.isfile(cand_path):
            inst = cand_path
            break
    if inst is None:
        return ["%s: flips to '%s' on PIPELINE-REGISTERED project %s, and NO proof-of-spec "
                "instance was found beside it. Layer 1: no VALID instance, no complete flip."
                % (rel, m.group(1), cand)]
    chk = os.path.join(root, ".tools", "proof-of-spec-check.py")
    if not os.path.isfile(chk):
        return ["%s: proof-of-spec-check.py is MISSING -- fail-closed rather than pass a flip "
                "whose validator cannot run" % rel]
    try:
        r = subprocess.run(["python", chk, inst], cwd=root,
                           capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=180)
    except Exception as exc:  # noqa: BLE001
        return ["%s: could not run the validator (%s) -- fail-closed" % (rel, exc)]
    if r.returncode != 0:
        head = (r.stdout or r.stderr or "").strip().splitlines()
        why = head[-1][:160] if head else "rc=%d" % r.returncode
        return ["%s: flips to '%s' but its instance is NOT VALID (rc=%d) -- %s"
                % (rel, m.group(1), r.returncode, why)]
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
    for k in sorted(fabric_counts, key=lambda x: (-fabric_counts[x], x)):
        flag = "  <- not in the ratified enum" if (
            k != "<ABSENT>" and k.strip().lower() not in FABRIC_ENUM) else ""
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


def main(argv):
    root = _repo_root()
    if "--sweep" in argv[1:]:
        return sweep(root)
    if "--self-test" in argv[1:]:
        return _self_test()

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

    # LAYER 1 half B runs on EVERY staged TO, added or modified -- a `complete` flip is almost
    # always a MODIFY, so scoping this to newly-added (as layers 2/3 correctly are) would make it
    # structurally unable to ever fire. Different question, different scope, stated so the
    # asymmetry reads as deliberate rather than as an oversight.
    flip_targets = sorted(p for p in dispatched if TO_PATH_RE.search(p))
    for rel in flip_targets:
        all_v.extend(check_complete_flip(root, rel))

    for n in all_notes:
        print("[to-pipeline-gate] NOTE: %s" % n)

    if all_v:
        print("[to-pipeline-gate] REFUSED -- %d violation(s) across %d newly-added TO file(s):"
              % (len(all_v), len(targets)), file=sys.stderr)
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
