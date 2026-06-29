"""Unit tests for comp-parity comparator logic (DATA_SSOTMG TO-4). Pure functions -> testable
WITHOUT live parallel data (the live S3-read run is cadence-gated; the LOGIC is verified here)."""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import comp_parity_cli as cp


# ---- CLASS A: EXACT-TIE ----
def test_class_a_exact_tie_pass_within_tolerance():
    canon = {"a": 1000.00, "b": 2000.005}
    bd = {"a": 1000.00, "b": 2000.00}            # b within $1 floor
    r = cp.compare_exact_tie(canon, bd, abs_usd=1.0, bps=1.0)
    assert r["verdict"] == cp.PASS and r["n_breaks"] == 0


def test_class_a_exact_tie_fail_on_break_and_key_mismatch():
    canon = {"a": 1000.0, "b": 2000.0, "c_only_canon": 5.0}
    bd = {"a": 1050.0, "b": 2000.0}              # a breaks ($50 > $1/1bp); c is canon-only
    r = cp.compare_exact_tie(canon, bd, abs_usd=1.0, bps=1.0)
    assert r["verdict"] == cp.FAIL
    assert r["n_breaks"] == 1 and r["key_mismatch"]["only_canonical"] == 1


# ---- CLASS B: BAND ----
def test_class_b_band_within_and_outside():
    canon = {"x": 0.0510}; bd = {"x": 0.0500}    # 10bp return delta
    assert cp.compare_band(canon, bd, band_bps=25)["verdict"] == cp.PASS       # within 25bp
    assert cp.compare_band(canon, bd, band_bps=5)["verdict"] == cp.FAIL        # outside 5bp


# ---- CLASS C: DRIFT-ON-DELTA (the keystone) ----
def test_class_c_first_day_baseline_in_envelope():
    # canonical $174M vs BD $180M (do-better gap ~3%) -> within 10% envelope -> baseline OK
    r = cp.compare_drift_on_delta(174_000_000, 180_000_000, prev_gap=None, envelope_pct=10, delta_drift_pct=2)
    assert r["verdict"] == cp.EXPECTED_DIVERGENCE_OK and r["baseline"] is True


def test_class_c_stable_gap_is_ok_not_a_fail():
    # the do-better gap held constant day-over-day -> EXPECTED-DIVERGENCE-OK (value-diff is NOT a fail)
    prev_gap = 174_000_000 - 180_000_000           # -6M yesterday
    r = cp.compare_drift_on_delta(174_500_000, 180_500_000, prev_gap=prev_gap, envelope_pct=10, delta_drift_pct=2)
    assert r["verdict"] == cp.EXPECTED_DIVERGENCE_OK and r["delta_stable"] is True


def test_class_c_sudden_gap_change_is_a_fail():
    # the gap MOVED (a regression on one independent upstream) -> FAIL even though both in envelope
    prev_gap = -6_000_000
    r = cp.compare_drift_on_delta(160_000_000, 180_000_000, prev_gap=prev_gap, envelope_pct=15, delta_drift_pct=2)
    assert r["verdict"] == cp.FAIL and r["delta_stable"] is False


def test_class_c_huge_stable_gap_is_mis_map_fail():
    # gap is stable but HUGE (outside envelope) -> wrong-surface mapping, not a do-better -> FAIL
    r = cp.compare_drift_on_delta(50_000_000, 180_000_000, prev_gap=(50_000_000 - 180_000_000),
                                  envelope_pct=10, delta_drift_pct=2)
    assert r["verdict"] == cp.FAIL and r["in_envelope"] is False


# ---- CLASS D: SCOPE-MISMATCH ----
def test_class_d_filters_bd_to_custody_and_emits_held_away():
    canon = {"s1": 100.0, "s2": 200.0}                       # Schwab-custody (canonical)
    bd_full = {"s1": 100.0, "s2": 200.0, "ha1": 76.5, "ha2": 10.0}  # BD incl held-away
    r = cp.compare_scope_subset(canon, bd_full, custody_accts={"s1", "s2"}, abs_usd=1.0, bps=1.0)
    assert r["verdict"] == cp.PASS                           # Schwab subset ties
    assert r["held_away_excluded_aua"] == 86.5 and r["held_away_n_accts"] == 2  # transparent remainder


# ---- VINTAGE gate (dual-fresh) ----
def test_vintage_dual_fresh_pass_one_stale_skip():
    assert cp.vintage_ok(10, 12, max_age_h=30) == cp.PASS
    assert cp.vintage_ok(10, 99, max_age_h=30) == cp.STALE_SKIP   # BD side stale -> false-PASS killer
    assert cp.vintage_ok(None, 12, max_age_h=30) == cp.STALE_SKIP # could-not-read vintage


# ---- TOTAL-AUA consistency gate (S7) ----
def test_total_aua_stale_xref_is_stale_skip_not_pass():
    # the stale-xref blocker: a stale xref makes the account-set delta a data artifact -> NOT a clean pass
    r = cp.total_aua_consistency(1_812_018_889, 1_591_227_965, 269_524_130, xref_fresh=False)
    assert r["verdict"] == cp.STALE_SKIP


def test_total_aua_clean_when_explained():
    # fresh xref + the delta fully explained (price-date/inclusion) -> PASS
    bd, canon, surplus = 1_860_752_096, 1_591_227_965, 269_524_131    # reconstruction off by ~$1
    r = cp.total_aua_consistency(bd, canon, surplus, xref_fresh=True)
    assert r["verdict"] == cp.PASS and abs(r["unexplained_residual"]) < 1.0


def test_total_aua_unexplained_residual_fails():
    r = cp.total_aua_consistency(1_900_000_000, 1_591_227_965, 269_524_130, xref_fresh=True)
    assert r["verdict"] == cp.FAIL and r["unexplained_residual"] > 1.0


# ---- day roll-up + streak ----
def test_day_verdict_and_streak_mechanics():
    pass_v = [{"verdict": cp.PASS}, {"verdict": cp.EXPECTED_DIVERGENCE_OK}]
    aua_pass = {"verdict": cp.PASS}
    assert cp.day_verdict(pass_v, aua_pass) == cp.PASS
    assert cp.day_verdict([{"verdict": cp.FAIL}], aua_pass) == cp.FAIL
    assert cp.day_verdict([{"verdict": cp.STALE_SKIP}], aua_pass) == cp.STALE_SKIP
    # streak: CLEAN +1, FAIL resets, STALE holds
    assert cp.update_streak(3, cp.PASS) == 4
    assert cp.update_streak(3, cp.FAIL) == 0          # a real divergence breaks the proof
    assert cp.update_streak(3, cp.STALE_SKIP) == 3    # stale holds, doesn't advance/reset
    assert cp.cutover_ready(5, 5) is True and cp.cutover_ready(4, 5) is False


# ---- CUTOVER-JUMP measure (two-track model: vs-BD is a magnitude, not a tie) ----
def test_cutover_jump_measures_not_ties_and_flags_structural():
    # canonical (current) vs BD (lagged, non-uniform): small drifts + one 2x structural defect
    canon = {"a": 100.0, "b": 200.0, "c": 651546.0, "d": 50.0}
    bd    = {"a": 101.0, "b": 198.0, "c": 1302754.0, "d": 50.0}   # c is ~2x = structural
    r = cp.measure_cutover_jump(canon, bd, structural_mult=1.5)
    assert r["track"] == "cutover_jump" and r["verdict"] == "MEASURED"
    assert r["n"] == 4 and r["n_structural"] == 1                  # only c flagged (>=1.5x)
    assert r["structural_breaks"][0][0] == "c"                     # the 2x doubling surfaces
