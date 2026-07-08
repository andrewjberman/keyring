"""comp_honesty -- NFRA_SEMCTL GOV-A follow-on: the runnable honesty/completion checker. Makes the shared
honesty doctrine (docs/architecture/NFRA_SEMCTL_HONESTY_INVARIANTS.md, I1/I2/I3) a GATE, not prose: given a
CLAIM + its EVIDENCE (code source and/or structured evidence), returns a per-invariant PASS/FAIL/N-A verdict
with grounding, so a verifier or a commit/deploy gate can mechanically apply the honesty bar.

The three invariants (GOV-A, b9f58b442; CVO co-ratify 7aad2f834):
  I1  honest-missing (LOUD, never silent)   -- absent/degraded input surfaced with {what,count,magnitude},
                                               never silently dropped/defaulted/returned-as-success.
  I2  measure per-case, not aggregate       -- a gating number measured at the grain of the thing asserted,
                                               never an aggregate/residual that hides a per-case defect.
  I3  a control must FIRE when exercised     -- a guard/gate is real only if a known-bad input trips it;
                                               dead code / mis-keyed / write-without-exercise is worse than none.

Two check modes per invariant (mirroring comp_ladder/fidelity_check as the runnable LAW-1/2 gate):
  - STATIC (AST over Python source): detects the violation SHAPES the doctrine names (silent-except-return-0,
    cross-grain residual, dead-guard predicate) directly in code.
  - EVIDENCE (structured cross-check): rc0-while-empty (claim=success + empty artifact), aggregate-hides-per-
    case (consistent roll-up + per-case violation), dead-guard (guard literal disjoint from producer labels).

DOGFOOD (I1 on itself, per the TO): when a check CANNOT evaluate (no applicable code/evidence), it returns
N-A with a LOUD could-not-check finding -- NEVER a silent PASS. Green-theater is the exact failure this tool
exists to catch, so it refuses to commit it itself.

Self-test (`python comp_honesty.py`) runs the GOV-A worked corpus as known-bad fixtures (D_02 silent-crash /
A_00 aggregate-hide / build_canonical_prices_v2.py:584 dead-guard) + honest known-good counter-fixtures, and
asserts each check DISTINGUISHES bad from good -- exercised (GOV-A I3 applied to the checker), not asserted.

Author: 0.8.0_AE_CloudComp~D (NFRA_SEMCTL.GOV-A-FOLLOWON, build lane). 2026-07-08.
Doctrine: docs/architecture/NFRA_SEMCTL_HONESTY_INVARIANTS.md (SS2/SS4.2 check-specs).
"""

from __future__ import annotations

import ast
import json
import sys
from dataclasses import dataclass, field

PASS, FAIL, NA = "PASS", "FAIL", "N-A"

# call-name fragments that read external state or aggregate -- an except-swallow around one of these with no
# WARN is the I1 silent-missing shape (doctrine SS2 I1.a).
_READ_AGG_CALLS = ("get_object", "download_file", "download_fileobj", "read_parquet", "read_csv",
                   "read_json", "get_item", "scan", "query", "list_objects", "head_object")
_AGG_METHODS = ("sum", "agg", "groupby", "mean", "count", "aggregate")
# a handler that carries a real WARN (a loud degrade) does NOT violate I1.
_WARN_TOKENS = ("warning", "warn", "error", "critical", "raise")
_WARN_LITERAL = ("WARN", "ERROR", "SKIP", "BLOCKED", "MISSING", "could not", "could_not")


@dataclass
class Verdict:
    invariant: str          # I1 | I2 | I3
    verdict: str            # PASS | FAIL | N-A
    finding: str            # the grounding / why
    checked: str = ""       # what was actually examined (evidence trail)

    def loud(self) -> str:
        tag = {"PASS": "OK", "FAIL": "VIOLATION", "N-A": "COULD-NOT-CHECK"}[self.verdict]
        return f"[{self.invariant}] {tag}: {self.finding}" + (f"  (checked: {self.checked})" if self.checked else "")


@dataclass
class Case:
    """A claim under the honesty bar. Supply code_src (or code_path) for the STATIC checks and/or evidence
    for the EVIDENCE checks. A check with neither returns N-A (LOUD), never a silent PASS."""
    claim: str
    code_src: str = ""
    code_path: str = ""
    evidence: dict = field(default_factory=dict)

    def source(self) -> str:
        if self.code_src:
            return self.code_src
        if self.code_path:
            with open(self.code_path, encoding="utf-8", errors="replace") as fh:
                return fh.read()
        return ""


# ---------------------------------------------------------------------------
# small AST helpers
# ---------------------------------------------------------------------------
def _parse(src: str):
    try:
        return ast.parse(src)
    except SyntaxError:
        return None


def _call_name(node) -> str:
    """dotted call name for a Call node's func (e.g. 's3.get_object' -> 'get_object', 'df.sum' -> 'sum')."""
    f = node.func if isinstance(node, ast.Call) else node
    if isinstance(f, ast.Attribute):
        return f.attr
    if isinstance(f, ast.Name):
        return f.id
    return ""


def _body_calls(nodes) -> list:
    out = []
    for n in nodes:
        for sub in ast.walk(n):
            if isinstance(sub, ast.Call):
                out.append(sub)
    return out


def _handler_is_silent_return(handler) -> tuple:
    """A handler whose body is effectively 'return 0 / return None / return / pass' (a silent swallow)."""
    body = [s for s in handler.body if not isinstance(s, ast.Pass)]
    if not body:
        return (True, "pass")
    if len(body) == 1 and isinstance(body[0], ast.Return):
        v = body[0].value
        if v is None:
            return (True, "return")
        if isinstance(v, ast.Constant) and (v.value is None or v.value == 0):
            return (True, f"return {v.value!r}")
    return (False, "")


def _handler_has_warn(handler) -> bool:
    for sub in ast.walk(handler):
        if isinstance(sub, ast.Call):
            nm = _call_name(sub).lower()
            if any(w in nm for w in _WARN_TOKENS):
                return True
        if isinstance(sub, ast.Constant) and isinstance(sub.value, str):
            if any(tok.lower() in sub.value.lower() for tok in _WARN_LITERAL):
                return True
        if isinstance(sub, ast.Raise):
            return True
    return False


# ---------------------------------------------------------------------------
# I1 -- honest-missing (LOUD, never silent)
# ---------------------------------------------------------------------------
def check_i1(case: Case) -> Verdict:
    findings = []
    checked = []

    # EVIDENCE: rc0-while-empty -- a completeness/Success claim whose named output artifact is absent/empty.
    ev = case.evidence or {}
    if "claims_success" in ev and "output_artifact" in ev:
        checked.append("rc0-while-empty")
        art = ev["output_artifact"] or {}
        b = art.get("bytes")
        empty = (b is None) or (isinstance(b, (int, float)) and b <= 0) or art.get("absent")
        if ev.get("claims_success") and empty:
            findings.append(f"claim asserts success but named output '{art.get('named', '?')}' is "
                            f"absent/byte-empty (bytes={b}) -- rc0-while-empty (silent success over nothing)")

    # STATIC: except -> silent return around a read/aggregation with no WARN carrying a count.
    src = case.source()
    if src:
        tree = _parse(src)
        if tree is None:
            findings.append("code did not parse -- cannot statically check I1 (surfaced, not swallowed)")
        else:
            checked.append("silent-except-swallow (AST)")
            for node in ast.walk(tree):
                if not isinstance(node, ast.Try):
                    continue
                try_calls = _body_calls(node.body)
                touches_state = any(_call_name(c) in _READ_AGG_CALLS or _call_name(c) in _AGG_METHODS
                                    for c in try_calls)
                if not touches_state:
                    continue
                for h in node.handlers:
                    silent, how = _handler_is_silent_return(h)
                    if silent and not _handler_has_warn(h):
                        ln = getattr(h, "lineno", "?")
                        findings.append(f"except@L{ln} -> '{how}' around a read/aggregation with NO WARN -- "
                                        f"silent-missing (I1.a): an absent/failed input is swallowed as success")

    if not checked:
        return Verdict("I1", NA, "no code_src/code_path and no {claims_success,output_artifact} evidence -- "
                       "could NOT check honest-missing (LOUD N-A, not a silent PASS)")
    if findings:
        return Verdict("I1", FAIL, " ; ".join(findings), checked=", ".join(checked))
    return Verdict("I1", PASS, "no silent-missing shape found: reads/aggregations degrade LOUD or the claimed "
                   "output is present", checked=", ".join(checked))


# ---------------------------------------------------------------------------
# I2 -- measure per-case, not aggregate
# ---------------------------------------------------------------------------
def _is_sum_call(node) -> bool:
    for sub in ast.walk(node):
        if isinstance(sub, ast.Call) and _call_name(sub) in ("sum",) or (
                isinstance(sub, ast.Attribute) and sub.attr == "sum"):
            return True
    return False


def check_i2(case: Case) -> Verdict:
    findings = []
    checked = []

    # EVIDENCE: aggregate-hides-per-case -- a roll-up that is internally consistent while a per-case measure
    # at the asserted grain is violated (the A_00 class).
    ev = case.evidence or {}
    if "aggregate" in ev and "per_case" in ev:
        checked.append("aggregate-vs-per-case")
        agg = ev["aggregate"] or {}
        pc = ev["per_case"] or {}
        if pc.get("violation") and agg.get("consistent", True):
            findings.append(f"aggregate '{agg.get('metric', '?')}'={agg.get('value', '?')} reads consistent "
                            f"while per-case ({pc.get('grain', '?')}) is violated: {pc.get('detail', '?')} -- "
                            f"the roll-up HIDES a per-case corruption (I2)")

    # EVIDENCE: cross-grain residual -- total and parts from different grains.
    if "residual" in ev:
        checked.append("cross-grain-residual")
        r = ev["residual"] or {}
        if r.get("total_grain") and r.get("parts_grain") and r["total_grain"] != r["parts_grain"]:
            findings.append(f"bucket derived as total({r['total_grain']}) - sum(parts:{r['parts_grain']}) "
                            f"across MISMATCHED grains -- collapses real magnitude into a phantom (I2)")

    # STATIC: a subtraction with a .sum() operand (residual candidate) + absence-classification (~isin/not in).
    src = case.source()
    if src:
        tree = _parse(src)
        if tree is None:
            findings.append("code did not parse -- cannot statically check I2 (surfaced, not swallowed)")
        else:
            checked.append("residual/absence-classification (AST)")
            for node in ast.walk(tree):
                if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Sub):
                    if _is_sum_call(node.right) or _is_sum_call(node.left):
                        findings.append(f"L{getattr(node, 'lineno', '?')}: residual 'X - sum(...)' -- a bucket "
                                        f"by subtraction; verify total-grain == parts-grain (I2 candidate)")
                # absence-classification: `~df[...].isin(...)` or a `not in` used to assign a bucket
                if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.Invert):
                    if any(isinstance(c, ast.Call) and _call_name(c) == "isin" for c in ast.walk(node)):
                        findings.append(f"L{getattr(node, 'lineno', '?')}: '~(...).isin(...)' -- classifying by "
                                        f"ABSENCE from a set, not a positive per-case tag (I2 candidate)")

    if not checked:
        return Verdict("I2", NA, "no code_src/code_path and no {aggregate,per_case}/{residual} evidence -- "
                       "could NOT check per-case measurement (LOUD N-A, not a silent PASS)")
    if findings:
        return Verdict("I2", FAIL, " ; ".join(findings), checked=", ".join(checked))
    return Verdict("I2", PASS, "measurement is per-case / positively-tagged at the asserted grain; no aggregate "
                   "hiding a per-case defect", checked=", ".join(checked))


# ---------------------------------------------------------------------------
# I3 -- a control must FIRE when exercised
# ---------------------------------------------------------------------------
def check_i3(case: Case) -> Verdict:
    findings = []
    checked = []
    ev = case.evidence or {}

    # EVIDENCE: dead-guard -- the guard's predicate literal is disjoint from the labels the producer emits.
    if "guard" in ev:
        checked.append("dead-guard (literal vs producer labels)")
        g = ev["guard"] or {}
        lit = g.get("literal")
        producer = set(g.get("producer_labels") or [])
        if lit is not None and producer and lit not in producer:
            findings.append(f"guard filters on '{lit}' which the producer NEVER emits (emits {sorted(producer)}) "
                            f"-> the predicate can never match -> the safety block is unreachable DEAD CODE (I3)")

    # EVIDENCE: unexercised control -- a declared control with no exercised red-fixture.
    if "control" in ev:
        checked.append("red-fixture presence")
        c = ev["control"] or {}
        if c.get("name") and not c.get("red_fixture"):
            findings.append(f"control '{c['name']}' has NO exercised red-fixture (a known-bad it must reject) -- "
                            f"exists != fires; unexercised guards certify GREEN they cannot back (I3)")

    # STATIC: a guard whose comparison literal set is disjoint from the produced-label set, when both are given
    # in evidence, OR (weaker) surface every equality-filter literal for a producer-set cross-check.
    src = case.source()
    if src and ev.get("producer_labels_for_static"):
        tree = _parse(src)
        if tree is not None:
            checked.append("equality-guard literals (AST)")
            producer = set(ev["producer_labels_for_static"])
            for node in ast.walk(tree):
                if isinstance(node, ast.Compare) and any(isinstance(o, ast.Eq) for o in node.ops):
                    for comp in node.comparators:
                        if isinstance(comp, ast.Constant) and isinstance(comp.value, str):
                            if comp.value not in producer:
                                findings.append(f"L{getattr(node, 'lineno', '?')}: equality guard on "
                                                f"'{comp.value}' not in producer labels {sorted(producer)} "
                                                f"-> dead guard (I3)")

    if not checked:
        return Verdict("I3", NA, "no {guard}/{control} evidence and no producer-label set for static check -- "
                       "could NOT check fire-when-exercised (LOUD N-A, not a silent PASS)")
    if findings:
        return Verdict("I3", FAIL, " ; ".join(findings), checked=", ".join(checked))
    return Verdict("I3", PASS, "the control's predicate is reachable (matches produced labels) and/or an "
                   "exercised red-fixture is present", checked=", ".join(checked))


def run_case(case: Case) -> list:
    return [check_i1(case), check_i2(case), check_i3(case)]


def gate(case: Case) -> bool:
    """Gate helper: a case PASSES the honesty bar iff no invariant FAILs. N-A does NOT pass silently -- it is
    surfaced (the caller decides), but gate() treats an N-A on an invariant the caller asked about as a
    non-pass would be too strict for a generic gate, so gate() returns False only on an explicit FAIL and
    leaves N-A visible in the verdicts for the caller to weigh."""
    return not any(v.verdict == FAIL for v in run_case(case))


# ===========================================================================
# SELF-TEST -- the GOV-A worked corpus as known-bad fixtures + honest counter-fixtures. Each check must
# DISTINGUISH bad from good (exercised, GOV-A I3 applied to the checker itself). `python comp_honesty.py`.
# ===========================================================================
def _self_test() -> bool:
    results = []

    def ck(name, cond, detail=""):
        results.append(bool(cond))
        print(f"  [{'PASS' if cond else 'FAIL'}] {name}" + (f"   ({detail})" if detail and not cond else ""))

    # ---- I1: cot D_02 silent-crash-behind-optional (served-confirmed 2026-07-07) ----
    d02_bad = Case(
        claim="cot D_02 completed successfully (advisors gold built)",
        code_src=(
            "def build_advisors(s3):\n"
            "    try:\n"
            "        raw = s3.get_object(Bucket='opal-data-cot', Key='silver/advisors.parquet')\n"
            "        return process(raw)\n"
            "    except Exception:\n"
            "        return 0\n"),
        evidence={"claims_success": True,
                  "output_artifact": {"named": "opal-data-cot/gold/entities/advisors/", "bytes": 0}})
    v = check_i1(d02_bad)
    ck("I1 FLAGS D_02 silent-crash (except->return 0 + empty artifact while claiming success)", v.verdict == FAIL,
       v.loud())

    d03_good = Case(  # cot D_03 degrade-LOUD on empty composition (the honest counterpart)
        claim="cot D_03 degraded loud on empty composition",
        code_src=(
            "def build_composition(s3, log):\n"
            "    try:\n"
            "        raw = s3.get_object(Bucket='opal-data-cot', Key='silver/holdings.parquet')\n"
            "        return process(raw)\n"
            "    except EmptyHoldings as e:\n"
            "        log.warning('WARN: holdings empty for %s (0 rows) -- skip composition, downstream builds', e)\n"
            "        return 0\n"),
        evidence={"claims_success": True,
                  "output_artifact": {"named": "opal-data-cot/gold/composition/", "bytes": 4096}})
    vg = check_i1(d03_good)
    ck("I1 PASSES D_03 degrade-loud (WARN carries the reason + artifact present)", vg.verdict == PASS, vg.loud())

    # ---- I2: cot A_00 accounts_dimension aggregate-hides-per-case (served-confirmed, 825-row dim) ----
    a00_bad = Case(
        claim="cot A_00 accounts_dimension is correct (tax_status 100% taxable)",
        evidence={"aggregate": {"metric": "tax_status", "value": "100% taxable", "consistent": True},
                  "per_case": {"grain": "per-account", "violation": True,
                               "detail": "12% null names, qualified_flag 100% False -- per-account tax destroyed"}})
    v2 = check_i2(a00_bad)
    ck("I2 FLAGS A_00 aggregate-hides-per-case (consistent roll-up, per-account clobber)", v2.verdict == FAIL,
       v2.loud())

    a00_good = Case(
        claim="accounts_dimension measured per-account (positive tag)",
        evidence={"aggregate": {"metric": "tax_status", "value": "62% taxable", "consistent": True},
                  "per_case": {"grain": "per-account", "violation": False,
                               "detail": "each account carries a positively-tagged tax_status; 0% null names"}})
    v2g = check_i2(a00_good)
    ck("I2 PASSES honest per-account measure (no per-case violation under a consistent aggregate)",
       v2g.verdict == PASS, v2g.loud())

    # I2 static: the ADVI_INFFEE cross-grain residual shape (source-confirmed)
    inffee = Case(claim="non-fee AUA computed",
                  code_src="def nonfee(total, parts):\n    return total - parts['aua'].sum()\n")
    v2s = check_i2(inffee)
    ck("I2 FLAGS the residual 'total - sum(parts)' shape statically (INFFEE class)", v2s.verdict == FAIL, v2s.loud())

    # ---- I3: cot build_canonical_prices_v2.py:584 dead-guard (confirmed 2026-07-07) ----
    dead_guard = Case(
        claim="build_canonical_prices Step-5b share-class denomination guard protects against mispricing",
        evidence={"guard": {"literal": "t1_transaction_observed",
                            "producer_labels": ["transaction_observed", "transaction_observed_capped"]}})
    v3 = check_i3(dead_guard)
    ck("I3 FLAGS build_canonical_prices:584 dead-guard (literal producer never emits -> unreachable)",
       v3.verdict == FAIL, v3.loud())

    live_guard = Case(  # the honest counterpart: the guard literal IS produced, and a red-fixture exists
        claim="share-class guard fires on mispricing",
        evidence={"guard": {"literal": "transaction_observed",
                            "producer_labels": ["transaction_observed", "transaction_observed_capped"]},
                  "control": {"name": "share_class_denomination_guard", "red_fixture": True}})
    v3g = check_i3(live_guard)
    ck("I3 PASSES a reachable guard with an exercised red-fixture", v3g.verdict == PASS, v3g.loud())

    # I3 static dead-guard (the bd-49f clone gate keying a foreign literal)
    static_dead = Case(
        claim="cot validate_sl_nightly_gate fires",
        code_src="def gate(df):\n    hit = df[df['account_id'] == 'JONES_ACCOUNT_ID']\n    return len(hit) == 0\n",
        evidence={"producer_labels_for_static": ["COT_ACCT_1", "COT_ACCT_2"]})
    v3s = check_i3(static_dead)
    ck("I3 FLAGS a static equality-guard on a foreign literal (49F-clone gate can't fire in cot)",
       v3s.verdict == FAIL, v3s.loud())

    # ---- DOGFOOD: I1 on the checker itself -- an un-checkable case returns LOUD N-A, never silent PASS ----
    empty = Case(claim="something happened", evidence={})
    va = run_case(empty)
    ck("DOGFOOD: no code + no evidence -> every invariant returns LOUD N-A (not a silent PASS)",
       all(v.verdict == NA for v in va), "; ".join(v.loud() for v in va))

    passed = sum(1 for r in results if r)
    print(f"\n=== comp_honesty self-test (GOV-A worked corpus, exercised): {passed}/{len(results)} PASS ===")
    return passed == len(results)


def _run_cli(argv) -> int:
    """comp-honesty <case.json> | comp-honesty --file <src.py> [--evidence <ev.json>]. Prints per-invariant
    verdicts (LOUD). Exit 1 if ANY invariant FAILs (gate mode); exit 0 if all PASS/N-A."""
    case = None
    if len(argv) == 1 and argv[0].endswith(".json"):
        with open(argv[0], encoding="utf-8") as fh:
            spec = json.load(fh)
        case = Case(claim=spec.get("claim", "(no claim)"), code_src=spec.get("code_src", ""),
                    code_path=spec.get("code_path", ""), evidence=spec.get("evidence", {}))
    elif "--file" in argv:
        path = argv[argv.index("--file") + 1]
        ev = {}
        if "--evidence" in argv:
            with open(argv[argv.index("--evidence") + 1], encoding="utf-8") as fh:
                ev = json.load(fh)
        case = Case(claim=f"honesty check of {path}", code_path=path, evidence=ev)
    if case is None:
        print("usage: comp-honesty <case.json> | comp-honesty --file <src.py> [--evidence <ev.json>]")
        return 2
    print(f"comp-honesty: {case.claim}")
    verdicts = run_case(case)
    for v in verdicts:
        print("  " + v.loud())
    n_fail = sum(1 for v in verdicts if v.verdict == FAIL)
    n_na = sum(1 for v in verdicts if v.verdict == NA)
    print(f"  => {n_fail} VIOLATION(s), {n_na} could-not-check, "
          f"{sum(1 for v in verdicts if v.verdict == PASS)} clean")
    return 1 if n_fail else 0


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] not in ("--self-test", "selftest"):
        sys.exit(_run_cli(sys.argv[1:]))
    sys.exit(0 if _self_test() else 1)
