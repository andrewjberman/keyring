"""comp_output_contract.py -- THE OUTPUT CONTRACT helper (NFRA_MSBEFF.R1R3, 2026-07-23, 0.8.0_AE_CloudComp).

ONE implementation, consumed by N tools (gate condition c). Every consumer draws from the SAME
enforced-complete declaration surface (org/modules/graph/comp-output-contracts.yaml):

  R1  coverage_line(tool[, sub])  -> "COVERAGE: <denominator> | BLIND: <what it structurally cannot see>"
  R3  plane_header(tool[, sub])   -> "PLANE: <desired|applied|...> | VINTAGE: <artifact + how dated>"
  M3  verdict_exit_map()          -> (verdict_tools_by_rc, refuse_exits) DERIVED from exit_codes;
                                     classify_exit(tool, rc) is the appender's single classification point.

  registered_tools()   -> the run-time consumer denominator (tools_index keys). NEVER hand-listed --
                          this file's own subject applied to itself (TO phase-1 mandate).
  declared_tools()     -> tools with a full contract.
  pending_tools()      -> tools_index tools explicitly awaiting a contract (render UNKNOWN, loud).

UNKNOWN IS NOT A VERDICT (condition b): a tool with no declared contract renders coverage/plane as a LOUD
UNKNOWN and classifies its nonzero exits as UNKNOWN -- never a silent omission, never a defaulted PASS/FAIL.
There is no channel for "I don't know," so not-knowing must render AS not-knowing.

The consumer denominator is derived from graph-call-manifest.yaml::tools_index at run time. The
declarations are enforced 1:1 against that roster by comp-manifest-check's output-contract member, so this
sidecar is CENSUS-GRADE, not a curated subset (see the file header for why that distinction is load-bearing).

Grounding: values are declarations, not measurements. A coverage line states what a tool's class of scan
CAN and CANNOT see; it does not re-derive the tool's answer. Cheap, dependency-light, never raises to a
caller that only wants a header line -- resolution failures degrade to LOUD UNKNOWN, never a silent clean.
"""

from __future__ import annotations

import functools
from pathlib import Path
from typing import Optional

_THIS_DIR = Path(__file__).resolve().parent
_CONTRACTS = _THIS_DIR / "comp-output-contracts.yaml"
_MANIFEST = _THIS_DIR / "graph-call-manifest.yaml"
# ONTOLOGY2 canonical_source (NFRA_ONTOLOGY2 P1, ~C). The stage-2 vocabulary authority; the reader below
# loads type_tuple.<field>.enum from HERE so canonization AUTO-ACTIVATES validation with no code edit.
_RULE_BANK = _THIS_DIR / "NFRA_ONTOLOGY_RULE_BANK.yaml"
# The declared fields validated against the canon vocabulary (stage-2). plane is live today (== ~C's enum
# verbatim); grain/scope become first-class declared fields in the one-pass reconcile on ~C's canon signal.
_VOCAB_FIELDS = ("plane", "grain", "scope")

# Result-class vocabulary. UNKNOWN is a first-class outcome, distinct from FAIL (condition b).
PASS = "PASS"
FAIL = "FAIL"
VERDICT = "VERDICT"
REFUSE = "REFUSE"
UNKNOWN = "UNKNOWN"


def _load_yaml(path: Path) -> dict:
    """Best-effort YAML load. Returns {} on any failure -- callers treat an empty contract set as
    'everything UNKNOWN, loudly', which is the fail-honest posture, never a silent clean."""
    try:
        import yaml  # local import: a header-only consumer should not hard-depend on PyYAML at import
        # CSafeLoader (libyaml, ~13x): verified parse-equal on the contracts file; loader swap
        # only, no caching. SafeLoader fallback keeps a libyaml-less Python correct.
        raw = yaml.load(path.read_text(encoding="utf-8"),
                        Loader=getattr(yaml, "CSafeLoader", yaml.SafeLoader))
        return raw if isinstance(raw, dict) else {}
    except Exception:
        return {}


@functools.lru_cache(maxsize=1)
def _contracts_doc() -> dict:
    return _load_yaml(_CONTRACTS)


@functools.lru_cache(maxsize=1)
def registered_tools() -> tuple:
    """The consumer denominator: tools_index keys, at run time. Never hand-listed."""
    man = _load_yaml(_MANIFEST)
    return tuple(sorted((man.get("tools_index") or {}).keys()))


@functools.lru_cache(maxsize=1)
def declared_tools() -> tuple:
    return tuple(sorted((_contracts_doc().get("contracts") or {}).keys()))


@functools.lru_cache(maxsize=1)
def pending_tools() -> tuple:
    return tuple(sorted(_contracts_doc().get("pending_declaration") or []))


def contract_for(tool: str, subcommand: Optional[str] = None) -> Optional[dict]:
    """The resolved contract dict for `tool` (subcommand override merged over the tool default), or None
    if the tool has no declared contract (pending or absent). None is the caller's UNKNOWN signal."""
    base = (_contracts_doc().get("contracts") or {}).get(tool)
    if not isinstance(base, dict):
        return None
    if subcommand:
        override = (base.get("by_subcommand") or {}).get(subcommand)
        if isinstance(override, dict):
            merged = dict(base)
            merged.update(override)
            return merged
    return base


# ----------------------------------------------------------------------------------------------------
# R1 -- COVERAGE LINE
# ----------------------------------------------------------------------------------------------------

def coverage_line(tool: str, subcommand: Optional[str] = None) -> str:
    """R1: the denominator scanned + the named structural blind spots for this invocation class.
    A tool with no declared contract renders a LOUD UNKNOWN (condition b), never an omitted line."""
    c = contract_for(tool, subcommand)
    if c is None:
        why = ("registered but awaiting a contract" if tool in pending_tools()
               else "not registered in tools_index" if tool not in registered_tools()
               else "no contract")
        return f"COVERAGE: UNKNOWN -- no output contract declared for '{tool}' ({why}); coverage NOT asserted"
    cov = str(c.get("coverage") or "UNKNOWN -- coverage field empty")
    blind = c.get("blind_spots") or []
    blind_txt = "; ".join(str(b) for b in blind) if blind else "none declared"
    return f"COVERAGE: {cov} | BLIND: {blind_txt}"


# ----------------------------------------------------------------------------------------------------
# R3 -- PLANE / VINTAGE HEADER
# ----------------------------------------------------------------------------------------------------

def plane_header(tool: str, subcommand: Optional[str] = None) -> str:
    """R3: the plane read (desired vs applied / source vs projection) + the vintage. Generalizes
    comp-kuzu's provenance header. LOUD UNKNOWN for an undeclared tool (condition b)."""
    c = contract_for(tool, subcommand)
    if c is None:
        return f"PLANE: UNKNOWN | VINTAGE: UNKNOWN -- no output contract declared for '{tool}'"
    plane = str(c.get("plane") or "UNKNOWN")
    vintage = str(c.get("vintage") or "UNKNOWN")
    return f"PLANE: {plane} | VINTAGE: {vintage}"


def header_block(tool: str, subcommand: Optional[str] = None) -> str:
    """Both lines, ready to print to stderr (keeps stdout parseable, like comp-kuzu's provenance header)."""
    return coverage_line(tool, subcommand) + "\n" + plane_header(tool, subcommand)


# ----------------------------------------------------------------------------------------------------
# M3 -- VERDICT-SET DERIVATION (retires the frozen VERDICT_EXIT_TOOLS / _REFUSE_EXITS)
# ----------------------------------------------------------------------------------------------------

def _exit_class(spec) -> str:
    """Normalize an exit_codes value to a result class. `pass`/`fail` shorthand or a {class: ...} dict."""
    if isinstance(spec, str):
        s = spec.strip().lower()
        return {"pass": PASS, "fail": FAIL, "verdict": VERDICT, "refuse": REFUSE}.get(s, FAIL)
    if isinstance(spec, dict):
        s = str(spec.get("class", "")).strip().lower()
        return {"pass": PASS, "fail": FAIL, "verdict": VERDICT, "refuse": REFUSE}.get(s, FAIL)
    return FAIL


@functools.lru_cache(maxsize=1)
def _exit_table() -> dict:
    """{tool: {rc:int -> class:str}} derived from every declared exit_codes block. The single source
    for classify_exit. Built once; a tool with no exit_codes block simply has no rc entries here."""
    table: dict = {}
    for tool, c in (_contracts_doc().get("contracts") or {}).items():
        if not isinstance(c, dict):
            continue
        ecs = c.get("exit_codes") or {}
        rc_map: dict = {}
        for rc, spec in ecs.items():
            try:
                rc_map[int(rc)] = _exit_class(spec)
            except (TypeError, ValueError):
                continue
        if rc_map:
            table[tool] = rc_map
    return table


def classify_exit(tool: str, exit_code: int) -> str:
    """THE single classification point for the appender (M3). Derived from the declared contracts:
      rc 0                                   -> PASS
      declared tool, rc in its exit_codes    -> that class (VERDICT / REFUSE / FAIL / PASS)
      declared tool, rc NOT in its exit_codes-> FAIL (an unexpected exit for a contract we DO know)
      undeclared tool (pending / absent)     -> UNKNOWN (condition b -- never defaulted PASS/FAIL)
    """
    if exit_code == 0:
        return PASS
    table = _exit_table()
    if tool in table:
        return table[tool].get(exit_code, FAIL)
    # No declared exit contract for this tool -> honest UNKNOWN, loud, not a silent FAIL.
    return UNKNOWN


# ----------------------------------------------------------------------------------------------------
# E4.2 -- THE FAIL COLUMN'S THREE MEANINGS, SEPARATED IN THE MACHINE RECORD
# (NFRA_VELOCITY_ESTATE WS-E4.2, COO dispatch 20260730T053344Z)
#
# A single FAIL token conflates three things with different owners and opposite signs:
#   (a) a DELIBERATE NEGATIVE CONTROL -- a probe engineered to fail, to prove a tool can
#       detect. More of these is BETTER. Counting them as failures makes improving
#       discipline look like degrading quality, which is the two-meaning-null that makes
#       "are we getting better?" unanswerable in either direction.
#   (b) a TOOL USAGE ERROR -- the caller passed something the tool cannot act on. Says
#       nothing about the estate; it is a fact about the invocation.
#   (c) a GENUINE FINDING -- the tool worked and the estate is wrong.
#
# DERIVED, NOT FROZEN (inherits E4.1 condition 1): the kind comes from the tool's own
# declared exit contract via an optional `kind:` on a fail-class exit. There is no
# hand-maintained tool list here and there must never be one.
#
# TWO DISTINCT "I DO NOT KNOW" BUCKETS, both LOUD, neither defaulted into (a)/(b)/(c) --
# this is E4.1 condition 2's discipline applied one level down:
#   UNDECLARED_RC   the rc is absent from the contract entirely. We do not know what this
#                   exit MEANS. Measured 2026-07-30: 19 rows across 6 tools carry rc=120,
#                   declared by nobody -- 21% of the post-M3 FAIL population. TWO causal
#                   hypotheses were tested and BOTH REFUTED (harness-rc corruption: the
#                   rate ROSE after MSTR's 07-28 mount fix, 0.120% -> 0.727%; CPython
#                   broken-pipe flush: a piped python exits 1, not 120, and
#                   comp-opalbizsem --list exits 2 both piped and unpiped). The cause is
#                   UNDETERMINED and is an owned item for the tool owners to declare. It is
#                   NOT assigned a meaning here, because a plausible-but-wrong bucket is
#                   worse than an honest unknown.
#   KIND_UNDECLARED the rc IS declared fail but carries no `kind:`. We know it failed; we
#                   do not know which of the three it is. Bounded and visible, exactly like
#                   pending_declaration -- so the tail can never grow silently.
# ----------------------------------------------------------------------------------------------------

FK_NEGATIVE_CONTROL = "negative_control"
FK_USAGE_ERROR = "usage_error"
FK_FINDING = "finding"
FK_UNDECLARED_RC = "undeclared_rc"
FK_KIND_UNDECLARED = "kind_undeclared"

_FAIL_KIND_VOCAB = {
    "negative_control": FK_NEGATIVE_CONTROL,
    "usage": FK_USAGE_ERROR,
    "usage_error": FK_USAGE_ERROR,
    "finding": FK_FINDING,
}


@functools.lru_cache(maxsize=1)
def _fail_kind_table() -> dict:
    """{tool: {rc:int -> kind:str}} from the declared `kind:` on each exit_codes entry.
    A tool with no kinds declared simply has no entries -- it renders KIND_UNDECLARED."""
    table: dict = {}
    for tool, c in (_contracts_doc().get("contracts") or {}).items():
        if not isinstance(c, dict):
            continue
        rc_map: dict = {}
        for rc, spec in (c.get("exit_codes") or {}).items():
            if not isinstance(spec, dict):
                continue
            kind = str(spec.get("kind", "")).strip().lower()
            if not kind:
                continue
            try:
                rc_map[int(rc)] = _FAIL_KIND_VOCAB.get(kind, FK_KIND_UNDECLARED)
            except (TypeError, ValueError):
                continue
        if rc_map:
            table[tool] = rc_map
    return table


def classify_fail_kind(tool: str, exit_code: int, synthetic: bool = False) -> Optional[str]:
    """E4.2's single derivation point. Returns None when the row is NOT a FAIL -- the field
    is absent rather than falsely populated, so a consumer can never read a kind off a PASS.

    Precedence, and the order is deliberate:
      synthetic flag set            -> NEGATIVE_CONTROL (a deliberate probe is a probe even
                                       if its rc also happens to be contracted)
      result class is not FAIL      -> None
      rc declared with a `kind:`    -> that kind
      rc declared fail, no `kind:`  -> KIND_UNDECLARED (loud)
      rc not declared at all        -> UNDECLARED_RC   (loud)
    """
    if synthetic:
        return FK_NEGATIVE_CONTROL
    if exit_code == 0:
        return None
    if classify_exit(tool, exit_code) != FAIL:
        return None
    declared_rcs = _exit_table().get(tool) or {}
    if exit_code not in declared_rcs:
        return FK_UNDECLARED_RC
    return (_fail_kind_table().get(tool) or {}).get(exit_code, FK_KIND_UNDECLARED)


def fail_kind_coverage() -> dict:
    """The migration denominator for E4.2: how many declared fail-exits carry a `kind:`.
    Printed on reports so the tail is visible and bounded, never silent."""
    total = kinded = 0
    missing = []
    for tool, rc_map in _exit_table().items():
        for rc, cls in rc_map.items():
            if cls != FAIL:
                continue
            total += 1
            if (_fail_kind_table().get(tool) or {}).get(rc):
                kinded += 1
            else:
                missing.append("%s:rc%d" % (tool, rc))
    return {"declared_fail_exits": total, "with_kind": kinded,
            "without_kind": sorted(missing),
            "note": ("an exit without a `kind:` renders KIND_UNDECLARED, loudly; it is never "
                     "defaulted into negative_control / usage_error / finding")}


# ----------------------------------------------------------------------------------------------------
# E4.3 ELEMENT 1 -- THE VERDICT BASIS, STAMPED AT WRITE TIME
# (NFRA_VELOCITY_ESTATE WS-E4.3, COO GO 20260730T072044Z)
#
# Lives HERE, not in the re-baseline module, because BOTH consumers must draw the basis identity
# from ONE implementation: the appender (stamping it on every new row) and comp_msbeff_rebaseline
# (labelling the re-derived series). Two implementations of a denominator's own identity is the
# exact defect this file's supersession history records four generations of -- see the yaml header.
#
# WHY AT WRITE TIME AND NOT AT RE-BASELINE TIME: a row that records only `result` forces its basis
# to be INFERRED later, and that inference only works while the contract surface has not moved. It
# will move -- 50 of 70 registered tools are still undeclared. Every row written without a basis is
# a row that will need re-baselining, and a re-baselined series cannot separate "the verdict logic
# changed" from "the estate changed". Stamping at write time makes each row permanently
# self-describing, so no future contract change can ever require re-baselining it.
#
# COST, MEASURED not estimated: 0.104 ms per call (read + sha256 of a ~33KB yaml), ~66 ms/day
# fabric-wide at 606 rows/day. comp_log_auto runs one process per tool call, so the lru_cache below
# gives one hash per process rather than per row. This is not a performance question.
# ----------------------------------------------------------------------------------------------------

@functools.lru_cache(maxsize=1)
def contract_surface_id() -> str:
    """Identity of the contract surface a derived verdict came from: declared version + content hash.

    The HASH IS LOAD-BEARING and must never be dropped for brevity: a hand edit that does not bump
    `version:` still changes every derived verdict, so a version-only id is a lie with a version
    number on it. (A test fails RED if the hash half goes away.)
    """
    import hashlib
    if not _CONTRACTS.exists():
        return "UNKNOWN-no-contract-surface"
    raw = _CONTRACTS.read_bytes()
    ver = "?"
    for line in raw.decode("utf-8", "replace").splitlines():
        if line.startswith("version:"):
            ver = line.split(":", 1)[1].strip()
            break
    return "v%s+%s" % (ver, hashlib.sha256(raw).hexdigest()[:16])


def derived_basis_id() -> str:
    """The basis label for a verdict derived under the CURRENT contract surface."""
    return "derived@" + contract_surface_id()


def verdict_exit_map() -> tuple:
    """Back-compat derivation for any consumer that wants the old shapes, DERIVED not frozen:
      (verdict_tools: frozenset,  refuse_exits: frozenset[(tool, rc)])
    A tool is a 'verdict tool' if any of its declared nonzero exits classify VERDICT."""
    table = _exit_table()
    verdict_tools = frozenset(t for t, m in table.items() if any(cls == VERDICT for cls in m.values()))
    refuse_exits = frozenset((t, rc) for t, m in table.items()
                             for rc, cls in m.items() if cls == REFUSE)
    return verdict_tools, refuse_exits


# ----------------------------------------------------------------------------------------------------
# STAGE-2 vocabulary validation (NFRA_ONTOLOGY2 <-> TOOLARCH seam). CTO~Z two-stage ruling (184541Z):
# STAGE 1 (live) = the registration invariant enforces PRESENCE of a plane/coverage declaration; STAGE 2
# (this) = declaration VALUES validate against ~C's canonical (rail,grain,plane,scope) vocabulary, out-of-
# vocab -> LOUD fail. This is the READER ~C green-lit building against the draft (185356Z/200041Z): it loads
# the enums from the rule bank canonical_source, so ~C's canonization AUTO-ACTIVATES it with NO code edit and
# NO restated enum copy. It is NOT wired into the blocking completeness gate here -- that wiring + adding
# grain/scope to every declaration is the ONE-PASS RECONCILE done together on ~C's canonization signal, so
# the gate never blocks in a half-reconciled state.
# ----------------------------------------------------------------------------------------------------

class CanonVocabUnavailable(Exception):
    """The ONTOLOGY2 canonical_source could not be READ or PARSED.

    DISTINCT from 'read fine, but carries no type_tuple'. Collapsing those two was a FAIL-OPEN
    (CVO~Z finding 221805Z, test specified by ~C): _load_yaml swallowed every read failure and returned
    {}, so the empty dict reached the gate BEFORE any exception could, the fail-closed handler never
    fired, and a missing/moved rule bank SILENTLY DISARMED the whole stage-2 axis while printing a benign
    'DORMANT (pre-canonization)' line and returning PASS. The docstring said fail-closed; the path was
    fail-open. An instrument that lies about its own posture is the exact class this program closes."""


@functools.lru_cache(maxsize=1)
def canon_vocab_strict() -> dict:
    """The canonical (rail,grain,plane,scope) enums from the ONTOLOGY2 rule bank.

    RAISES CanonVocabUnavailable when the canonical_source cannot be read/parsed -- so the caller's
    fail-closed handler actually fires. Returns {} ONLY for the genuinely different condition: the file
    parsed fine and carries no `type_tuple` section.

    Reading from the canonical_source (never a hardcoded copy) is the whole point: a token shift at ~C's
    gate is picked up automatically. LAW-2: an enum extension is a rule-bank version bump; the enum is a
    CLOSED set here."""
    if not _RULE_BANK.exists():
        raise CanonVocabUnavailable(f"canonical_source MISSING at {_RULE_BANK}")
    try:
        import yaml
        doc = yaml.load(_RULE_BANK.read_text(encoding="utf-8"),
                        Loader=getattr(yaml, "CSafeLoader", yaml.SafeLoader))
    except Exception as e:  # noqa: BLE001
        raise CanonVocabUnavailable(
            f"canonical_source UNREADABLE ({type(e).__name__}: {str(e)[:120]})") from e
    if not isinstance(doc, dict):
        raise CanonVocabUnavailable(
            f"canonical_source did not parse to a mapping (got {type(doc).__name__})")
    tt = doc.get("type_tuple")
    if not isinstance(tt, dict):
        return {}          # READ FINE, section absent -- a DIFFERENT condition, reported differently
    out = {}
    for field in ("rail",) + _VOCAB_FIELDS:
        enum = (tt.get(field) or {}).get("enum") if isinstance(tt.get(field), dict) else None
        if isinstance(enum, list):
            out[field] = list(enum)
    return out


def canon_vocab() -> dict:
    """LENIENT wrapper: {} on ANY unavailability. For advisory callers (validate_declaration_vocab)
    that must never raise. A GATE must use canon_vocab_strict() -- swallowing the read failure here is
    precisely what made the gate fail-open."""
    try:
        return canon_vocab_strict()
    except CanonVocabUnavailable:
        return {}


def validate_declaration_vocab(tool: str, subcommand: Optional[str] = None) -> list:
    """STAGE-2: for the declared fields (plane/grain/scope) that are PRESENT on this tool's contract, verify
    the value is in the canon enum. Returns a list of violation strings (empty = clean). Two dormancy rules
    keep it false-positive-free before the one-pass reconcile:
      - canon vocab absent (pre-canonization)         -> [] (dormant).
      - a field ABSENT from the declaration           -> NOT a violation (presence is the reconcile's job;
                                                          stage-2 validates VALUES, stage-1 owns PRESENCE).
    So today it validates plane values (all == ~C's enum, all pass) and is silent on the not-yet-declared
    grain/scope -- exactly the safe interim CTO~Z ruled."""
    vocab = canon_vocab()
    if not vocab:
        return []
    c = contract_for(tool, subcommand)
    if c is None:
        return []  # undeclared tools are stage-1's UNKNOWN, not stage-2's problem
    violations = []
    for field in _VOCAB_FIELDS:
        if field not in c:
            continue  # absent -> reconcile's job, not a value violation
        val = c.get(field)
        allowed = vocab.get(field)
        if allowed is None:
            continue  # the rule bank does not (yet) carry this field's enum
        if val not in allowed:
            violations.append(f"{tool}.{field}={val!r} NOT in canon {field} enum {allowed}")
    return violations


def validate_all_declarations() -> dict:
    """Sweep every declared tool through stage-2. {tool: [violations]} for tools with >=1 violation; {} when
    clean or dormant. This is what the stage-2 gate member will consume on the canonization signal."""
    out = {}
    for tool in declared_tools():
        v = validate_declaration_vocab(tool)
        if v:
            out[tool] = v
    return out


def stage2_status() -> dict:
    """One-call status for reports: is stage-2 armed (canon vocab present), and does the current surface pass?"""
    vocab = canon_vocab()
    return {
        "canon_vocab_present": bool(vocab),
        "fields_loaded": sorted(vocab),
        "declared_tools_swept": len(declared_tools()),
        "violations": validate_all_declarations(),
    }


def undeclared_registered() -> tuple:
    """tools_index tools with no full contract -- the honest denominator of the migration tail.
    Every one renders UNKNOWN. The registration invariant keeps this bounded (pending or declared)."""
    dec = set(declared_tools())
    return tuple(t for t in registered_tools() if t not in dec)


def coverage_summary() -> dict:
    """One-call census for reports / --self-test: the denominator this contract is OF."""
    reg = registered_tools()
    dec = declared_tools()
    pend = pending_tools()
    return {
        "registered": len(reg),          # tools_index (the consumer denominator, run-time)
        "declared": len(dec),            # full contracts
        "pending": len(pend),            # explicitly awaiting (render UNKNOWN)
        "undeclared_registered": len(undeclared_registered()),
        "verdict_tools": len(verdict_exit_map()[0]),
        "refuse_exits": len(verdict_exit_map()[1]),
    }


if __name__ == "__main__":
    import json
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "--self-test":
        s = coverage_summary()
        print(json.dumps(s, indent=2))
        vt, re_ = verdict_exit_map()
        print("\nVERDICT tools (derived):", ", ".join(sorted(vt)))
        print("REFUSE exits (derived):", ", ".join(f"{t}:{rc}" for t, rc in sorted(re_)))
        # Sanity: every declared+pending tool must be in the registered roster (the gate enforces this
        # at commit; here we just surface it).
        reg = set(registered_tools())
        stray = [t for t in list(declared_tools()) + list(pending_tools()) if t not in reg]
        print("\nstray (declared/pending but NOT in tools_index):", stray or "none")
        sys.exit(0)
    # default: print a couple of header samples
    for t in ["comp-blast", "comp-iam", "comp-does-not-exist"]:
        print(f"--- {t} ---")
        print(header_block(t))
