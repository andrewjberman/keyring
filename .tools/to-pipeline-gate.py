#!/usr/bin/env python3
"""to-pipeline-gate.py -- LAYER 2 of the DIRECTIVE EXECUTION PIPELINE enforcement architecture.

AUTHORITY: Andrew-direct 2026-09-01 at the 3.0.0_SA_CVO terminal -- "re-authorize the three
enforcement layers and add the stage-3 preflight" / "we need these set up in a manner that they
are actually mandated" / "I prefer gates and deterministic methodology because anything that is
simply 'guidance' may dissipate or otherwise be inconsistent over long-running sessions."

WHAT THIS GATES, AND WHY IT IS THE KEYSTONE
  org/ref/DIRECTIVE_EXECUTION_PIPELINE.md specifies five enforcement layers. Layer 1 (the
  proof-of-spec validation gate) IS BUILT and DOES enforce -- but only on an instance whose
  GOVERNING TO carries a naming <decomp_ref>. MEASURED 2026-09-01: 130 of 2233 TO files carry
  one = 5.8%. Layer 1 is therefore inert on 94% of the estate, not because it is broken but
  because nothing ever required the TO to carry the element that activates it.

  LAYER 2 IS THAT REQUIREMENT. Gate the neck of the funnel: a TO that conformantly requires a
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
import re
import subprocess
import sys

TO_PATH_RE = re.compile(r"(^|/)org/.*/task_orders/[^/]+\.md$")
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


def _repo_root():
    try:
        out = subprocess.run(["git", "rev-parse", "--show-toplevel"],
                             capture_output=True, text=True, timeout=20)
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
                             cwd=root, capture_output=True, text=True, timeout=30)
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


def check_project_stage(root, rel):
    """LAYER 3: the TO's project must exist and declare a dep_stage from the ratified enum."""
    import json
    code = _project_of(rel)
    if not code:
        return ["%s: filename declares no PROJECT code -- a TO is named "
                "PROJECT.TO-NAME.md so its project is resolvable without opening it" % rel]
    p = os.path.join(root, "org", "projects", code + ".json")
    # Walk the code back the way the estate's own resolvers do (FOO_BAR_BAZ -> FOO_BAR -> FOO).
    cand = code
    while not os.path.isfile(p) and "_" in cand:
        cand = cand.rsplit("_", 1)[0]
        p = os.path.join(root, "org", "projects", cand + ".json")
    if not os.path.isfile(p):
        return ["%s: NO project JSON for %r (org/projects/%s.json). A TO cannot be cut against "
                "an unregistered project -- registration is stage 1." % (rel, code, code)]
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
    code = _project_of(rel)
    if not code:
        return [], []
    p = os.path.join(root, "org", "projects", code + ".json")
    cand = code
    while not os.path.isfile(p) and "_" in cand:
        cand = cand.rsplit("_", 1)[0]
        p = os.path.join(root, "org", "projects", cand + ".json")
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
FWD_DEF_RE = re.compile(r"^[ \t]*(FWD-[0-9]+)[ \t]{2,}\S", re.M)


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
        pat = re.compile(r"(?m)^" + re.escape(heading) + r"[ \t]*$")
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
    code = _project_of(rel)
    if not code:
        return [], []
    p = os.path.join(root, "org", "projects", code + ".json")
    cand = code
    while not os.path.isfile(p) and "_" in cand:
        cand = cand.rsplit("_", 1)[0]
        p = os.path.join(root, "org", "projects", cand + ".json")
    if not os.path.isfile(p):
        return [], []
    # CVO~A re-grade @d019922d68 (B): the project row is read from the STAGED INDEX like everything
    # else this limb compares -- a worktree read let staged directive=D9 pass against a worktree/header
    # D8. The worktree file above is used only to resolve the code; the CONTENT comes from the index.
    rel_json = "org/projects/%s.json" % cand
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
        notes.append("OVERRIDE taken on %s -- reason: %s" % (rel, ov.group(1).strip()))
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
    code = _project_of(rel)
    if not code:
        return []
    cand, p = code, os.path.join(root, "org", "projects", code + ".json")
    while not os.path.isfile(p) and "_" in cand:
        cand = cand.rsplit("_", 1)[0]
        p = os.path.join(root, "org", "projects", cand + ".json")
    if not os.path.isfile(p):
        return []
    try:
        with open(p, "r", encoding="utf-8") as fh:
            if json.load(fh).get("dep_stage") is None:
                return []  # not pipeline-registered -- out of scope by design
    except Exception:  # noqa: BLE001
        return []

    # Pipeline-registered AND flipping terminal: the instance must exist and be VALID.
    inst = None
    for cand_path in (
            os.path.join(root, os.path.dirname(rel).replace("task_orders", "deliverables"),
                         os.path.basename(rel).rsplit(".md", 1)[0] + ".proof_of_spec.json"),
            os.path.join(root, os.path.dirname(rel).replace("task_orders", "deliverables"),
                         os.path.basename(rel).rsplit(".md", 1)[0] + "_PROOF_OF_SPEC.json")):
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
                           capture_output=True, text=True, timeout=180)
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


def main(argv):
    root = _repo_root()
    if "--sweep" in argv[1:]:
        return sweep(root)
    added = _newly_added(root)
    if added is None:
        print("[to-pipeline-gate] REFUSED: could not read the staged index. Fail-closed.",
              file=sys.stderr)
        return 1

    # Consider only paths the caller dispatched AND that git says are newly added.
    dispatched = [a.replace("\\", "/") for a in argv[1:]]
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
