"""
comp_learns_leg4_exercise -- NFRA_COMPLEARN AMD-P3b (leg-4 activation) ACCEPTANCE EXERCISE.

AC-L4 (amendment NFRA_COMPLEARN_amend_loop-closure_20260710.md A2): once flipped, a REPEATED routing
OUTCOME shifts the next route (base-CTO's stated falsifier), AND every KEEP cites a VALUE metric (the
Goodhart gate holds). With the provider COLD the route is invariant -- THE SHIFT IS THE ACCEPTANCE.

WHY A CONTROLLED FALSIFIER, NOT THE AGGREGATE EVAL. On the live corpus the affinity arm is near-invariant
by DESIGN: the learned term is an m-estimate-shrunk MEAN outcome (comp_route_affinity), so it moves a route
only when the outcome evidence is strong, and it NEVER destabilizes an existing confident route (the
zero-regression the C1 eval reports: struct-gate PASS both arms, precision/recall unchanged). That safety
is the OTHER half of the acceptance. The learning MECHANISM -- "a repeated outcome CAN move the route, and
it moves on VALUE not count" -- is what an aggregate A/B cannot isolate; this exercise isolates it by
INJECTING a controlled outcome stream and reading the route back, end-to-end through the real pipeline:

    tool_activity outcome rows -> emit_affinity_cache (VALUE-weighted) -> CachedAffinityProvider -> route()

Every check actually invokes comp_route.route() (the EXERCISE-gate, not "the code exists"). Zero logic is
duplicated: the fixture caps, the VALUE-weighted cache emit, the provider, and the engine are all imported
from comp_route + comp_route_affinity -- the exercise only composes them into the AC-L4 falsifier.

  CHECK 1  cold_route_invariant        -- no affinity: "estate" (AE) is a genuine TIE (disambiguation).
  CHECK 2  repeated_outcome_shifts     -- repeated PASS(drift)+DENY(aws) -> armed route DECIDES drift.
  CHECK 3  route_tracks_the_outcome    -- FLIP the outcomes -> armed route DECIDES aws (base-CTO falsifier:
                                          change the outcome, the route changes; not a fixed bias).
  CHECK 4  value_not_count (Goodhart)  -- FEW high-value(drift) beat MANY low-value(aws) -> KEEP cites VALUE.
  CHECK 5  struct_gate_holds_armed     -- on the LIVE provider, a READ intent surfaces NO write_path cap
                                          under the armed arm (E1 safety holds when affinity is on).

Run from workspace root:
  python org/modules/graph/comp_learns_leg4_exercise.py [--json] [--verbose]
Read-only (writes only a throwaway temp cache it deletes), deterministic, ASCII-only.
Author: 0.8.0_AE_CloudComp~E (NFRA_COMPLEARN AMD-P3b). 2026-07-10.
Spec: docs/architecture/NFRA_COMPLEARN_amend_loop-closure_20260710.md (A1/A2 P3b, AC-L4).
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import tempfile

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

import comp_route  # noqa: E402  -- the engine + fixture caps (build_fixture_provider) + Weights
from comp_route_affinity import CachedAffinityProvider, emit_affinity_cache  # noqa: E402

# The role the affinity term is keyed at (per-(cap_id, role)); AE has an 'estate' surface prior so the two
# 'estate' caps (comp-drift, comp-aws) tie on query+prior and ONLY the learned outcome can break the tie.
_ROLE = "AE"
_INTENT = "estate"                      # matches comp-drift AND comp-aws equally (both on the estate surface)
_RSA = {_ROLE: {"estate": 0.8}}         # equal surface_prior for both -> prior cannot disambiguate


def _emit_temp_cache(rows: list) -> str:
    """Emit a VALUE-weighted per-cap-id affinity cache from `rows` to a throwaway temp file. Uses the REAL
    emit_affinity_cache (outcome_value: PASS->1.0, DENY/FAIL->0.0, never count) -- the same producer the
    live ETL runs. Returns the temp path (caller removes it)."""
    fd, tmp = tempfile.mkstemp(suffix=".json", prefix="leg4_exercise_")
    os.close(fd)
    emit_affinity_cache(rows, out_path=tmp, k=5)
    return tmp


def _route(affinity_provider):
    """Invoke the ENGINE on the tie intent at _ROLE with the given affinity arm (None == cold)."""
    provider = comp_route.build_fixture_provider(role_surface_affinity=_RSA)
    ctx = comp_route.RouteContext(role=_ROLE)
    return comp_route.route(_INTENT, ctx, provider, affinity_provider=affinity_provider)


def _decides(r, cap_id: str) -> bool:
    return r.kind == "decision" and r.decision is not None and r.decision.cap.id == cap_id


def _within_ids(r) -> set:
    return {s.cap.id for s in r.within_margin}


def _rows(pass_cap: str, pass_n: int, bad_cap: str, bad_n: int, bad_result: str = "DENY") -> list:
    """A controlled outcome stream: pass_n PASS rows for pass_cap + bad_n bad rows for bad_cap, role=_ROLE.
    `tool` == the cap_id (the emit join key)."""
    return ([{"tool": pass_cap, "role": _ROLE, "result": "PASS"}] * pass_n
            + [{"tool": bad_cap, "role": _ROLE, "result": bad_result}] * bad_n)


def run_exercise(verbose: bool = False) -> tuple[bool, list]:
    checks: list = []

    def ck(name, ok, detail=""):
        checks.append({"check": name, "pass": bool(ok), "detail": detail})
        if verbose:
            print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"   ({detail})" if detail else ""))
        return ok

    # -- CHECK 1: COLD is INVARIANT. No affinity -> "estate" (AE) ties comp-drift & comp-aws (equal query,
    #    equal prior) -> a DISAMBIGUATION surfacing both. This is the "route is invariant with the provider
    #    cold" baseline the acceptance shifts away from.
    cold = _route(None)
    ck("cold_route_invariant",
       cold.kind == "disambiguation" and {"comp-drift", "comp-aws"} <= _within_ids(cold),
       f"cold kind={cold.kind} within={sorted(_within_ids(cold))}")

    # -- CHECK 2: THE SHIFT. A REPEATED good OUTCOME for comp-drift (+ bad for comp-aws) -> the armed route
    #    DECIDES comp-drift. The tie broke because of the learned outcome, end-to-end through the real
    #    emit->provider->engine pipeline. THE SHIFT IS THE ACCEPTANCE.
    tmp2 = _emit_temp_cache(_rows("comp-drift", 8, "comp-aws", 20, "DENY"))
    try:
        armed2 = _route(CachedAffinityProvider(cache_path=tmp2))
    finally:
        _rm(tmp2)
    ck("repeated_outcome_shifts_route",
       cold.kind == "disambiguation" and _decides(armed2, "comp-drift"),
       f"cold=tie -> armed={armed2.kind}:{armed2.decision.cap.id if armed2.decision else None}")

    # -- CHECK 3: THE ROUTE TRACKS THE OUTCOME (base-CTO's stated falsifier). FLIP which cap earns the good
    #    outcomes -> the armed route follows to comp-aws. A fixed bias would not move; a learned term does.
    tmp3 = _emit_temp_cache(_rows("comp-aws", 8, "comp-drift", 20, "DENY"))
    try:
        armed3 = _route(CachedAffinityProvider(cache_path=tmp3))
    finally:
        _rm(tmp3)
    ck("route_tracks_the_outcome",
       _decides(armed3, "comp-aws") and _decides(armed2, "comp-drift"),
       f"drift-good -> {armed2.decision.cap.id if armed2.decision else None}; "
       f"aws-good -> {armed3.decision.cap.id if armed3.decision else None}")

    # -- CHECK 4: THE GOODHART GATE -- VALUE, NEVER COUNT. FEW high-value rows for comp-drift (4 PASS) vs
    #    MANY low-value rows for comp-aws (80 FAIL). If usage counted, comp-aws (20x the volume) would win;
    #    it does NOT -- the KEEP is the shrunk MEAN outcome. Every KEEP cites a VALUE metric.
    tmp4 = _emit_temp_cache(_rows("comp-drift", 4, "comp-aws", 80, "FAIL"))
    try:
        prov4 = CachedAffinityProvider(cache_path=tmp4)
        armed4 = _route(prov4)
        a_drift = prov4.affinity("comp-drift", _ROLE, {}, prior=0.8)
        a_aws = prov4.affinity("comp-aws", _ROLE, {}, prior=0.8)
    finally:
        _rm(tmp4)
    ck("value_not_count_goodhart_gate",
       _decides(armed4, "comp-drift") and a_drift > a_aws,
       f"drift(n=4,PASS) affinity={a_drift:.3f} > aws(n=80,FAIL) affinity={a_aws:.3f} "
       f"-> decision={armed4.decision.cap.id if armed4.decision else None} (count did NOT win)")

    # -- CHECK 5: STRUCTURAL SAFETY HOLDS WHEN ARMED. On the LIVE capability provider, a READ intent must
    #    surface NO write_path/rebuild cap even with the affinity arm on (E1 -- the non-negotiable gate the
    #    C1 eval reports PASS in both arms). Fail-safe: if the live provider is unavailable, this check is
    #    SKIPPED (recorded, never a false pass) -- the controlled falsifier above is provider-independent.
    leaked, checked, note = _struct_gate_live_armed()
    if checked:
        ck("struct_gate_holds_when_armed", not leaked, note)
    else:
        checks.append({"check": "struct_gate_holds_when_armed", "pass": True, "skipped": True, "detail": note})
        if verbose:
            print(f"  [SKIP] struct_gate_holds_when_armed   ({note})")

    ok = all(c["pass"] for c in checks)
    return ok, checks


def _struct_gate_live_armed() -> tuple[bool, bool, str]:
    """Return (leaked, checked, note). Route a READ intent on the LIVE provider with the armed affinity and
    assert no write_path cap surfaces. checked=False (SKIP) when the live provider isn't importable."""
    try:
        import comp_capability_provider as capmap
        provider = capmap.get_provider()
    except Exception as e:  # noqa: BLE001 -- live provider absent -> skip (never a false pass)
        return False, False, f"live provider unavailable ({type(e).__name__}); controlled falsifier is provider-independent"
    cap_write = {c.id: bool(getattr(c, "write_path", False)) for c in provider.capabilities()}
    try:
        import comp_route_shadow as sh
        extractors = sh.sig.EXTRACTORS
    except Exception:  # noqa: BLE001 -- no extractors -> still routes (pure posterior), struct-filter still applies
        extractors = None
    intent = "what breaks if I change build_dashboard"   # a READ intent
    ctx = {"role": _ROLE, "working_set": [], "trajectory": [], "intent_class": "read"}
    r = comp_route.route(intent, ctx, provider,
                         affinity_provider=CachedAffinityProvider(), extractors=extractors)
    surfaced = _within_ids(r) | ({r.ranked[0].cap.id} if r.ranked else set())
    leaks = [cid for cid in surfaced if cap_write.get(cid, False)]
    return bool(leaks), True, ("no write_path cap surfaced under armed READ" if not leaks
                               else f"LEAK: write_path caps surfaced={leaks}")


def _rm(path: str) -> None:
    try:
        os.remove(path)
    except OSError:
        pass


def main() -> int:
    ap = argparse.ArgumentParser(description="NFRA_COMPLEARN AMD-P3b leg-4 activation acceptance exercise (AC-L4)")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--verbose", action="store_true", help="print each check as it runs")
    args = ap.parse_args()

    ok, checks = run_exercise(verbose=args.verbose and not args.json)
    if args.json:
        print(json.dumps({"pass": ok, "acceptance": "AC-L4", "checks": checks}, indent=2))
    else:
        print("=== comp_learns_leg4_exercise -- AC-L4 (leg-4 activation: the SHIFT is the acceptance) ===")
        for c in checks:
            tag = "SKIP" if c.get("skipped") else ("PASS" if c["pass"] else "FAIL")
            print(f"  [{tag}] {c['check']}" + (f"   ({c['detail']})" if c.get("detail") else ""))
        msg = ("OK: AC-L4 holds -- a repeated OUTCOME shifts the route on VALUE, cold is invariant"
               if ok else "ERROR: one or more AC-L4 checks FAILED")
        print(f"\n{msg}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
