#!/usr/bin/env python3
"""comp-parity -- DATA/served parity gate for a never-widen cutover (DATA_SSOTMG TO-4).

The daily, tolerance-aware, dual-gated proof that a canonical pipeline can stand in for the
BD-served surfaces -- the thing that must go GREEN for N days before 49F's live book flips to
Schwab-SSOT. Firm-agnostic engine; the per-firm spec is data/canonical/schwab/parity/{firm}_parity_config.yaml.

DISTINCT from comp-lambdamap parity (DEPLOY parity: record/live/S3-sha). comp-parity = DATA parity
(canonical-build vs BD-served). CTO-gated lane (a general never-widen-validation instrument).

The four tolerance classes (D3 contract) -- a naive value-diff would FAIL our own improvements, so:
  A EXACT-TIE          custodial primitives (holdings/lots) -- must match to rounding
  B BAND               derived metrics (performance/NNA) -- within a defined band
  C DRIFT-ON-DELTA     the do-better surfaces -- the value-difference is NOT a fail; the GAP must be
                       stable day-over-day (a sudden gap-change = regression; a constant gap = the
                       known improvement). Safe BECAUSE the two sides have independent upstreams.
  D SCOPE-MISMATCH     firm AUA -- compare only the Schwab-custody subset; emit the held-away remainder.
Two cross-cutting gates: dual-VINTAGE (a frozen==frozen match is a FALSE pass) + CONTENT-not-mtime.
Two cutover gates: per-account positioned parity AND firm-total-AUA consistency -- BOTH clean for N days.

The comparators below are PURE (data in, verdict out) so they are unit-testable without live data;
the I/O layer (S3 load) wraps them and runs once the parallel cadence is live.
"""
from __future__ import annotations

import json


# ---- verdict vocabulary ----
PASS = "PASS"
FAIL = "FAIL"
EXPECTED_DIVERGENCE_OK = "EXPECTED-DIVERGENCE-OK"
STALE_SKIP = "STALE-SKIP"            # vintage gate: a side wasn't fresh -> neither pass nor fail
UNVERIFIABLE = "UNVERIFIABLE"        # could-not-read a side

# tri-state exit (mirrors comp-validate / comp-lambdamap parity)
_EXIT = {PASS: 0, EXPECTED_DIVERGENCE_OK: 0, FAIL: 1, STALE_SKIP: 2, UNVERIFIABLE: 2}


def _tol_for(bd_val, abs_usd=0.0, bps=0.0):
    """Per-value tolerance = max(abs floor, bps of the bd magnitude)."""
    return max(abs_usd or 0.0, (bps or 0.0) / 10000.0 * abs(bd_val))


# ============================ CLASS A -- EXACT-TIE ============================
def compare_exact_tie(canon: dict, bd: dict, abs_usd=1.0, bps=1.0):
    """Custodial primitive: every key must tie to rounding. ANY break = FAIL (a custodian primitive
    cannot legitimately diverge once history+custody-scoped). Returns a per-surface verdict dict."""
    keys = set(canon) & set(bd)
    breaks, max_delta = [], 0.0
    for k in keys:
        d = abs(canon[k] - bd[k])
        if d > _tol_for(bd[k], abs_usd, bps):
            breaks.append((k, canon[k], bd[k], d))
        max_delta = max(max_delta, d)
    only_canon = set(canon) - set(bd)
    only_bd = set(bd) - set(canon)
    verdict = FAIL if (breaks or only_canon or only_bd) else PASS
    return {"class": "A", "verdict": verdict, "n_compared": len(keys),
            "n_breaks": len(breaks), "max_abs_delta": round(max_delta, 2),
            "key_mismatch": {"only_canonical": len(only_canon), "only_bd": len(only_bd)},
            "breaks": breaks[:20]}


# ============================ CLASS B -- BAND ============================
def compare_band(canon: dict, bd: dict, band_bps=None, band_pct=None, band_pp=None):
    """Derived metric: within a defined band. band_bps for returns, band_pct for $, band_pp for shares."""
    keys = set(canon) & set(bd)
    outside, max_delta = [], 0.0
    for k in keys:
        d = abs(canon[k] - bd[k])
        if band_bps is not None:
            limit = band_bps / 10000.0                       # return delta in absolute (e.g. 0.0025)
        elif band_pct is not None:
            limit = band_pct / 100.0 * abs(bd[k])
        elif band_pp is not None:
            limit = band_pp                                  # percentage-point delta on a share
        else:
            limit = 0.0
        if d > limit:
            outside.append((k, canon[k], bd[k], d))
        max_delta = max(max_delta, d)
    verdict = FAIL if outside else PASS
    return {"class": "B", "verdict": verdict, "n_compared": len(keys),
            "n_outside_band": len(outside), "max_abs_delta": round(max_delta, 6),
            "outside": outside[:20]}


# ==================== CLASS C -- DRIFT-ON-DELTA (the keystone) ====================
def compare_drift_on_delta(canon_agg, bd_agg, prev_gap, envelope_pct=10.0, delta_drift_pct=2.0):
    """Do-better surface. The value-difference is NOT a fail (canonical is intentionally more accurate).
    PASS iff (i) the gap is within an EXPLAINED envelope (|gap| <= envelope% of bd, same sign) AND
    (ii) the gap is STABLE day-over-day (|gap - prev_gap| <= delta_drift% of bd). A sudden gap-change
    = FAIL (a regression on either independent upstream moves the delta); a constant gap = PASS (the
    known improvement). prev_gap=None on the first day -> establish the baseline (EXPECTED-DIVERGENCE-OK).
    Safe BECAUSE the two sides have independent upstreams (canonical=Schwab raw, BD=DataMining)."""
    gap = canon_agg - bd_agg
    env_limit = envelope_pct / 100.0 * abs(bd_agg) if bd_agg else float("inf")
    in_envelope = abs(gap) <= env_limit
    if prev_gap is None:
        # first day: record the baseline gap; in-envelope = EXPECTED-DIVERGENCE-OK, else FAIL (mis-mapped?)
        v = EXPECTED_DIVERGENCE_OK if in_envelope else FAIL
        return {"class": "C", "verdict": v, "gap": round(gap, 2), "prev_gap": None,
                "in_envelope": in_envelope, "delta_stable": None, "baseline": True}
    drift = abs(gap - prev_gap)
    drift_limit = delta_drift_pct / 100.0 * abs(bd_agg) if bd_agg else float("inf")
    delta_stable = drift <= drift_limit
    # a HUGE-but-stable gap = wrong-surface-mapping (envelope catches it); an unstable gap = regression
    if not in_envelope:
        v = FAIL                                             # mis-mapped surface (stable but huge)
    elif not delta_stable:
        v = FAIL                                             # the regression (gap moved)
    else:
        v = EXPECTED_DIVERGENCE_OK                           # expected, stable do-better gap
    return {"class": "C", "verdict": v, "gap": round(gap, 2), "prev_gap": round(prev_gap, 2),
            "gap_drift": round(drift, 2), "in_envelope": in_envelope, "delta_stable": delta_stable}


# ==================== CLASS D -- SCOPE-MISMATCH (firm AUA) ====================
def compare_scope_subset(canon: dict, bd_full: dict, custody_accts: set, abs_usd=1.0, bps=1.0):
    """Firm AUA: canonical is Schwab-custody-only; BD's total includes held-away. Filter BD to the
    custody subset (DERISK-2 census = the single classification), exact-tie on that subset, and EMIT
    the excluded held-away remainder ($, census-bounded) so the ~$243M exclusion is TRANSPARENT, never
    a silent drop. Firm-wide reconstructs = Schwab-subset (parity-proven) + held-away (known-excluded)."""
    bd_subset = {k: v for k, v in bd_full.items() if k in custody_accts}
    held_away = {k: v for k, v in bd_full.items() if k not in custody_accts}
    held_away_total = round(sum(held_away.values()), 2)
    inner = compare_exact_tie(canon, bd_subset, abs_usd, bps)
    inner["class"] = "D"
    inner["held_away_excluded_aua"] = held_away_total       # the transparent GATE-D.2 remainder
    inner["held_away_n_accts"] = len(held_away)
    inner["bd_subset_aua"] = round(sum(bd_subset.values()), 2)
    return inner


# ==================== CUTOVER-JUMP measure (vs a non-uniformly-stale BD -- NOT a tie-gate) ====================
def measure_cutover_jump(canon: dict, bd: dict, structural_mult=1.5):
    """Two-track model (Andrew 2026-06-29): BD lags >=1wk NON-UNIFORMLY (per-account), so it CANNOT be the
    correctness reference -- exact-tie against it is structurally impossible. So canonical-vs-BD is NOT a
    pass/fail tie; it MEASURES the cutover display-JUMP (how much the firm's numbers move when we flip from
    lagged-BD to current-canonical) + flags only STRUCTURAL breaks (>= structural_mult x, e.g. the 2x
    doubling) which are real defects, not lag. Correctness is gated elsewhere (canonical vs Schwab-raw).
    Empirical basis: a uniform date-shift does NOT align them (canonical-06-18 vs BD-06-24 = 99.5% break,
    WORSE than same-date 49%), so the lag is non-uniform -> measure, don't tie."""
    keys = set(canon) & set(bd)
    if not keys:
        return {"track": "cutover_jump", "verdict": "NO-OVERLAP", "n": 0}
    deltas = sorted(abs(canon[k] - bd[k]) for k in keys)
    n = len(deltas)
    total_canon = sum(canon[k] for k in keys)
    total_bd = sum(bd[k] for k in keys)
    structural = []
    for k in keys:
        lo, hi = min(canon[k], bd[k]), max(canon[k], bd[k])
        if lo > 0 and hi / lo >= structural_mult:
            structural.append((k, round(canon[k], 0), round(bd[k], 0), round(hi / lo, 2)))
    # the headline JUMP = the firm-total display change at cutover (canonical fresher -> expected non-zero)
    return {"track": "cutover_jump", "verdict": "MEASURED", "n": n,
            "median_abs_delta": round(deltas[n // 2], 2),
            "p95_abs_delta": round(deltas[min(n - 1, int(n * 0.95))], 2),
            "headline_jump_usd": round(total_canon - total_bd, 2),
            "headline_jump_pct": round((total_canon - total_bd) / total_bd * 100, 3) if total_bd else None,
            "structural_breaks": sorted(structural, key=lambda x: -x[3])[:20],
            "n_structural": len(structural)}


# ==================== cross-cutting gates ====================
def vintage_ok(canon_age_h, bd_age_h, max_age_h):
    """Dual-vintage: BOTH sides must be fresher than max_age. A frozen==frozen match is a FALSE pass,
    so a stale side -> STALE-SKIP (does not advance the streak, does not reset it). The false-PASS killer."""
    if canon_age_h is None or bd_age_h is None:
        return STALE_SKIP                                    # could-not-read a vintage
    return PASS if (canon_age_h <= max_age_h and bd_age_h <= max_age_h) else STALE_SKIP


def total_aua_consistency(bd_served_total, canonical_schwab, surplus, xref_fresh,
                          explained_deltas=None):
    """Firm-total gate (S7 +1): BD-served firm total == canonical(Schwab) + surplus(non-Schwab), delta
    ZERO or fully EXPLAINED. CATCHES the aggregate-masking case (per-account-within-tolerance summing to
    a firm-total drift). HARD PREREQ: a fresh account_xref -- a stale xref makes the account-set delta a
    data artifact, so a stale-xref 'match' is a FALSE pass (STALE-SKIP, like the vintage gate)."""
    if not xref_fresh:
        return {"verdict": STALE_SKIP, "reason": "account_xref STALE -> the account-set delta is a "
                "data artifact, not a reconciliation; refresh xref to MEASURE the true delta"}
    reconstruction = canonical_schwab + surplus
    delta = bd_served_total - reconstruction
    explained = round(sum((explained_deltas or {}).values()), 2)
    residual = round(delta - explained, 2)
    verdict = PASS if abs(residual) < 1.0 else FAIL          # zero (to the $) or fully explained
    return {"verdict": verdict, "bd_served_total": bd_served_total, "reconstruction": reconstruction,
            "delta": round(delta, 2), "explained": explained, "unexplained_residual": residual,
            "explained_deltas": explained_deltas or {}}


# ==================== day-roll-up + streak ====================
def day_verdict(surface_verdicts, total_aua_verdict, require_both_gates=True):
    """A day is CLEAN iff every in-scope surface is PASS/EXPECTED-DIVERGENCE-OK AND none is STALE-SKIP
    on a should-be-fresh date AND (if required) the total-AUA gate is PASS. Any FAIL = NOT-CLEAN; any
    STALE-SKIP = the day is STALE (holds the streak, doesn't advance/reset)."""
    states = [v["verdict"] for v in surface_verdicts]
    if require_both_gates:
        states.append(total_aua_verdict["verdict"])
    if FAIL in states or UNVERIFIABLE in states:
        return FAIL
    if STALE_SKIP in states:
        return STALE_SKIP
    return PASS                                              # all PASS / EXPECTED-DIVERGENCE-OK


def update_streak(prev_streak, day):
    """CLEAN -> +1; FAIL -> reset to 0 (a real divergence breaks the proof); STALE-SKIP -> HOLD
    (does not advance, does not reset -- but is escalated, a stalled cadence is its own problem)."""
    if day == PASS:
        return prev_streak + 1
    if day == FAIL:
        return 0
    return prev_streak                                       # STALE-SKIP holds


def cutover_ready(streak, target):
    return streak >= target


def overall_exit(surface_verdicts, total_aua_verdict):
    states = [v["verdict"] for v in surface_verdicts] + [total_aua_verdict["verdict"]]
    return max(_EXIT.get(s, 0) for s in states)


# ==================== CLI + config (the I/O wrapper around the tested core) ====================
def load_config(path):
    import yaml  # noqa: PLC0415
    with open(path, encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def validate_config(cfg):
    """Structure-validate the firm parity spec (runs WITHOUT live data). TWO-TRACK model: a CORRECTNESS
    track (canonical vs schwab_raw -- the hard cutover gate) + a CUTOVER-JUMP track (canonical vs bd_served
    -- informational). Returns (ok, issues)."""
    issues = []
    corr = (cfg.get("correctness_track") or {}).get("surfaces", [])
    jump = (cfg.get("cutover_jump_track") or {}).get("surfaces", [])
    if not corr:
        issues.append("missing correctness_track.surfaces (the hard cutover gate = canonical vs Schwab-raw)")
    for s in corr:
        sid = s.get("id", "<no-id>")
        if not s.get("canonical", {}).get("table"):
            issues.append(f"correctness/{sid}: missing canonical.table")
        ctype = s.get("correctness_type")
        # PASSTHROUGH -> must name a schwab_raw feed (exact-tie ref); DERIVED -> must name derived_from + a check.
        if ctype == "passthrough" and not s.get("schwab_raw", {}).get("table"):
            issues.append(f"correctness/{sid}: passthrough missing schwab_raw.table (the custodian tie ref)")
        elif ctype == "derived" and not (s.get("derived_from") and s.get("check")):
            issues.append(f"correctness/{sid}: derived missing derived_from + check (the reconciliation spec)")
        elif ctype not in ("passthrough", "derived"):
            issues.append(f"correctness/{sid}: correctness_type must be passthrough|derived, got {ctype!r}")
        if s.get("tolerance_class") not in ("A", "B", "C", "D"):
            issues.append(f"correctness/{sid}: bad tolerance_class {s.get('tolerance_class')!r}")
    for s in jump:
        sid = s.get("id", "<no-id>")
        # NAMESPACE GUARD: bd_served must be a BD gold/platinum path, never the canonical root.
        for p in str(s.get("bd_served", {}).get("path", "")).split(","):
            if p.strip().startswith("canonical/schwab"):
                issues.append(f"jump/{sid}: bd_served {p!r} points at the CANONICAL root (cross-stream map)")
    if not (cfg.get("correctness_track") or {}).get("total_aua_gate"):
        issues.append("missing correctness_track.total_aua_gate (S7 firm-total-consistency)")
    return (not issues), issues


def main(argv=None):
    import argparse  # noqa: PLC0415
    ap = argparse.ArgumentParser(prog="comp-parity",
                                 description="DATA/served parity gate for a never-widen cutover "
                                             "(DATA_SSOTMG TO-4). Distinct from comp-lambdamap parity "
                                             "(DEPLOY parity).")
    ap.add_argument("firm", nargs="?", default="49f")
    ap.add_argument("--config", default=None)
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args(argv)
    cfg_path = a.config or f"data/canonical/schwab/parity/{a.firm}_parity_config.yaml"
    cfg = load_config(cfg_path)
    ok, issues = validate_config(cfg)
    corr = (cfg.get("correctness_track") or {}).get("surfaces", [])
    jump = (cfg.get("cutover_jump_track") or {}).get("surfaces", [])
    out = {"firm": cfg.get("firm"), "config": cfg_path, "config_valid": ok, "issues": issues,
           "model": "two-track (correctness vs Schwab-raw [hard gate] + cutover-jump vs BD [informational])",
           "correctness_surfaces": len(corr), "jump_surfaces": len(jump),
           "cutover_streak_target": cfg.get("cutover_gate", {}).get("clean_streak_target"),
           # RECORDED static prior result -- NOT re-measured by this run. This CLI load+validate+prints
           # config only; the live comparators are defined but NOT invoked here. Reserved words (the
           # proof-class) are legal only on a source-confirmed / re-measured claim (CLAUDE.md Rule-22),
           # so this is labeled RECORDED (M3 fix: was a hardcoded reserved-word headline printed as a verdict).
           "day1": "RECORDED (static, NOT re-measured by this run): G1 correctness measured 0/5892 "
                   "value-breaks / $0 max delta (canonical_holdings vs schwab/silver/rps) at the DATA_SSOTMG "
                   "G1 pass; vs-BD 49% break = BD non-uniform lag. Re-run the live comparators to re-confirm.",
           "run_status": "TWO-TRACK CONFIG-READY (this run validates CONFIG only). Correctness track: G1 has "
                         "a RECORDED prior clean result (see day1) -- NOT re-measured here. Remaining surfaces' "
                         "schwab_raw refs to confirm per-provenance + grain-aware loaders."}
    if a.json:
        print(json.dumps(out, indent=2))
    else:
        print(f"comp-parity {out['firm']} -- DATA/served parity gate (DATA_SSOTMG TO-4), TWO-TRACK")
        print(f"  config: {cfg_path}  | valid: {'OK' if ok else 'ISSUES'}")
        for i in issues:
            print(f"    ISSUE: {i}")
        print(f"  correctness surfaces (vs Schwab-raw, HARD gate): {len(corr)}")
        print(f"  cutover-jump surfaces (vs BD, informational):    {len(jump)}  | streak target: {out['cutover_streak_target']}")
        print(f"  G1: {out['day1']}")
    return 0 if ok else 2


if __name__ == "__main__":
    import sys as _sys
    _sys.exit(main())
