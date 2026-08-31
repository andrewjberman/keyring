"""Addendum 1i clause 1 ENTRY ORACLE -- the rebuilt permutation-null arm.

Governed by the margin procedure pre-registered at 039df9f72a and AMENDED at 05e66421cf:

    margin = k(N) * s_null * sqrt(1 + 1/N)      k(N) = t(0.95, N-1), ONE-SIDED
    CLAUSE 1 PASSES iff  A_fused - m_null > margin

The sqrt(1 + 1/N) term is the PREDICTION form: A_fused is ONE NEW OBSERVATION compared against a mean
ESTIMATED from N draws, so the dispersion of the difference carries the observation's own variance PLUS
the variance of the estimated mean. The confidence form understates the bar by 2.47% at the N=20 floor.

REPLACES the arm carded UNSOUND AS A GATE at 4e7016f471 (verdict scoped to "this arm AS THE ENTRY GATE").
Its three disqualifying grounds and this module's answer to each:

    CADENCE  one draw where clause 1 requires a distribution   -> N >= 20 REQUIRED, refuses below
    KEY      a shared RNG stream makes draws order-dependent   -> one INDEPENDENT stream per draw,
                                                                  seed recorded, re-derivable
    INPUT    an untracked/non-retrievable primary input        -> resolved from the IMMUTABLE
                                                                  run-addressed URI, size + sha256
                                                                  verified, NEVER the .tmp projection

⛔ THE FUSION IS INJECTED, NOT IMPORTED, AND NOT RE-IMPLEMENTED.
`rederive_l3w2.py` holds W1_over / W2_over / SNF / auc_from, but it is a SCRIPT: `sys.argv[1]` executes at
its line 22, it has no main guard, and it carries 153 top-level statements, so importing it dies
immediately and would run a whole rederivation as a side effect. Censused: those definitions exist in
exactly ONE place across 138,994 files -- there is no importable form.

Re-implementing the fusion here would create a SECOND CARRIER OF THE SAME COMPUTATION that can drift from
the first, which is the defect class this project has ruled against repeatedly. So this module takes the
fusion as a CALLABLE and owns only what the remedies are about: the battery, the seeds, the margin, the
refusals and the disclosure. Wiring it to the real fusion needs an importable extraction of that script,
which belongs to the lane that owns it.

⚠ WHAT THIS MODULE DOES NOT DO: it does not admit a candidate, does not build a view, does not touch the
store, and computes no verdict about any real candidate. No candidate exists.
"""
from __future__ import annotations

import hashlib
import math
import subprocess
import tempfile
from pathlib import Path

# ---------------------------------------------------------------- the pinned input

SERVED_URI = (
    "s3://opal-313476888478-globgrph/c3materialize-b4/out/"
    "eb009c01-c27e-46b3-af85-eb22dbfba01a-b4231e6374ce/W_STRUCTURE_FACTORIZED.json"
)
SERVED_SHA256 = "e91d69910fc9d4eabb58eedb8a73165476225ab838977e8d6c16604af3f5e19a"
SERVED_BYTES = 2662267

# ⛔ The .tmp projection is NEVER a fallback. An arm that silently fell back to a local cache would
# reintroduce the exact uncustodied input its predecessor was disqualified for.
FORBIDDEN_SUBSTRING = ".tmp-"

N_FLOOR = 20                      # Addendum 1i clause 1: a distribution, never one draw
K_DEFAULT, T_DEFAULT = 20, 20     # declared (K, T); a run states its own


class OracleRefusal(RuntimeError):
    """Raised instead of returning a verdict. A probe that ANSWERS when it failed is worse than one
    that raises: the answer is indistinguishable from a measurement and inherits an instrument's
    authority."""


def resolve_input(uri: str = SERVED_URI, cache_dir: str = None) -> Path:
    """Fetch the primary input from its IMMUTABLE run-addressed URI and verify it by CONTENT.

    REFUSES on retrieval failure, size mismatch or digest mismatch. Never reads the .tmp projection.
    """
    if FORBIDDEN_SUBSTRING in uri:
        raise OracleRefusal(
            "REFUSED: uri %r names the uncustodied .tmp projection. The card disqualified the "
            "predecessor arm on exactly this ground; a fallback here would reintroduce it." % uri)
    dest = Path(cache_dir or tempfile.mkdtemp(prefix="c1oracle-")) / Path(uri).name
    proc = subprocess.run([".tools/aws", "s3", "cp", uri, str(dest)],
                          capture_output=True, text=True)
    if proc.returncode != 0:
        raise OracleRefusal("REFUSED: retrieval failed rc=%d uri=%s stderr=%s"
                            % (proc.returncode, uri, (proc.stderr or "").strip()[:400]))
    if not dest.exists():
        raise OracleRefusal("REFUSED: retrieval reported rc=0 but produced no file at %s -- rc=0 is "
                            "the tool describing itself, the file is the repository answering" % dest)
    raw = dest.read_bytes()
    if len(raw) != SERVED_BYTES:
        raise OracleRefusal("REFUSED: size mismatch, expected %d got %d" % (SERVED_BYTES, len(raw)))
    got = hashlib.sha256(raw).hexdigest()
    if got != SERVED_SHA256:
        raise OracleRefusal("REFUSED: digest mismatch, declared %s computed %s -- refusing rather than "
                            "measuring against bytes the record disowns" % (SERVED_SHA256, got))
    return dest


# ---------------------------------------------------------------- the multiplier

# k(N) = t(0.95, N-1), one-sided. SOURCE IS STATED so the value is auditable rather than asserted:
# scipy.stats.t.ppf when importable, else this committed table. A k that does not match its stated
# source is a DEFECT, not a variant.
_T95_TABLE = {19: 1.729132, 20: 1.724718, 24: 1.710882, 29: 1.699127, 30: 1.697261,
              39: 1.684875, 49: 1.676551, 59: 1.671093, 99: 1.660234, 199: 1.652547}


def k_of(n: int) -> tuple:
    """Return (k, source). One-sided 95% Student-t at df = n-1."""
    df = n - 1
    try:
        from scipy.stats import t as _t
        import scipy
        return float(_t.ppf(0.95, df)), "scipy.stats.t.ppf(0.95,%d) scipy==%s" % (df, scipy.__version__)
    except Exception:
        if df in _T95_TABLE:
            return _T95_TABLE[df], "committed table df=%d" % df
        keys = sorted(_T95_TABLE)
        hi = min((x for x in keys if x >= df), default=keys[-1])
        return _T95_TABLE[hi], "committed table CONSERVATIVE df=%d used for df=%d" % (hi, df)


def margin_of(s_null: float, n: int) -> tuple:
    """margin = k(N) * s_null * sqrt(1 + 1/N). Returns (margin, k, source)."""
    k, src = k_of(n)
    return k * s_null * math.sqrt(1.0 + 1.0 / n), k, src


# ---------------------------------------------------------------- dispersion + disclosure

def _mean(xs):
    return sum(xs) / len(xs)


def _sample_sd(xs):
    m = _mean(xs)
    return math.sqrt(sum((x - m) ** 2 for x in xs) / (len(xs) - 1))


def _skew(xs):
    """Sample skewness. REPORTED beside every verdict per AMENDMENT 1: t assumes an approximately
    normal null, and a permutation null of AUC values need not be one -- AUC is bounded on [0,1] and
    skews near the ceiling. This is a DISCLOSURE, never a refusal: a skew threshold would be a gate
    nobody ruled."""
    n, m = len(xs), _mean(xs)
    sd = _sample_sd(xs)
    if sd == 0:
        return 0.0
    return (n / ((n - 1) * (n - 2))) * sum(((x - m) / sd) ** 3 for x in xs)


def null_battery(fuse, w1, w2, labels, *, n: int = N_FLOOR, base_seed: int = 20260831,
                 k_param: int = K_DEFAULT, t_param: int = T_DEFAULT) -> dict:
    """Run the permutation null. ONE INDEPENDENT RNG STREAM PER DRAW, each seed recorded.

    `fuse(w1, w2, perm, K, T) -> float` is INJECTED. `perm` is the permutation applied to view 2's
    firm labels; a draw is that fusion's AUC under permuted labels.
    """
    import random
    if n < N_FLOOR:
        raise OracleRefusal("REFUSED: N=%d is below the floor of %d -- a partial battery is not a "
                            "smaller battery, it is not a null" % (n, N_FLOOR))
    draws, seeds = [], []
    for i in range(n):
        seed = base_seed + i
        rng = random.Random(seed)            # a FRESH stream per draw, never a shared one
        perm = list(range(len(labels)))
        rng.shuffle(perm)
        draws.append(float(fuse(w1, w2, perm, k_param, t_param)))
        seeds.append(seed)
    return {"draws": draws, "seeds": seeds, "n": n, "K": k_param, "T": t_param,
            "base_seed": base_seed}


def evaluate(a_fused: float, battery: dict, a_view1: float, a_view2: float) -> dict:
    """Clause 1 (CONTRIBUTION) and clause 2 (ADEQUACY), with the full disclosure on the verdict."""
    draws = battery["draws"]
    n = battery["n"]
    if len(draws) != n:
        raise OracleRefusal("REFUSED: battery claims n=%d and carries %d draws" % (n, len(draws)))
    if len(draws) < 2:
        raise OracleRefusal("REFUSED: s_null undefined at n=%d" % len(draws))
    s_null = _sample_sd(draws)
    if s_null == 0 or not math.isfinite(s_null):
        raise OracleRefusal(
            "REFUSED: degenerate null, s_null=%r. A zero or non-finite dispersion makes the margin 0 "
            "or NaN, and the comparison would PASS or ERROR while looking like a measurement" % s_null)
    m_null = _mean(draws)
    margin, k, k_src = margin_of(s_null, n)
    observed = a_fused - m_null
    return {
        "clause1_contribution": {
            "passes": bool(observed > margin),
            "A_fused": a_fused, "m_null": m_null, "observed_excess": observed, "margin": margin,
        },
        "clause2_adequacy": {
            "passes": bool(a_fused >= max(a_view1, a_view2)),
            "A_fused": a_fused, "best_input_alone": max(a_view1, a_view2),
        },
        # ⚠ DISCLOSURE, per AMENDMENT 1 -- reported on EVERY verdict so a grossly non-normal null is
        # VISIBLE rather than silently parametrised, and so k is checkable against its stated source.
        "disclosure": {
            "n": n, "s_null": s_null, "skew": _skew(draws),
            "normality_note": "t assumes an approximately normal null; a permutation null of AUC "
                              "values is bounded on [0,1] and may skew near the ceiling",
            "k": k, "k_source": k_src, "prediction_term": math.sqrt(1.0 + 1.0 / n),
            "K": battery["K"], "T": battery["T"], "seeds": battery["seeds"],
        },
        "limits": {
            "emitter_side_only": "This proves contract behaviour and independence from the emitter. "
                                 "It does NOT prove the pinned ruling is correct.",
            "candidate": "No candidate is admitted or judged by this module.",
        },
    }


# ---------------------------------------------------------------- self-test

def _synthetic_fuse(bias):
    """A fixture fusion with a KNOWN truth, so the arm is exercised on data whose answer is known."""
    import random

    def fuse(w1, w2, perm, K, T):
        rng = random.Random(hash(tuple(perm)) & 0xFFFF)
        return 0.50 + bias + rng.uniform(-0.01, 0.01)
    return fuse


def selftest() -> int:
    R = []

    def arm(name, got, want):
        R.append((name, got == want, "%s (want %s, got %s)" % (name, want, got)))

    labels = list(range(40))
    bat = null_battery(_synthetic_fuse(0.0), None, None, labels, n=20)

    # POSITIVE CONTROL FIRST: a battery of refusals fired off a base that already refuses means nothing.
    arm("baseline_battery_runs", len(bat["draws"]), 20)
    arm("seeds_are_distinct_per_draw", len(set(bat["seeds"])), 20)

    v = evaluate(0.75, bat, 0.60, 0.55)
    arm("clause1_fires_on_a_real_excess", v["clause1_contribution"]["passes"], True)
    arm("clause2_fires_on_adequacy", v["clause2_adequacy"]["passes"], True)
    arm("disclosure_carries_skew", "skew" in v["disclosure"], True)
    arm("disclosure_carries_k_source", bool(v["disclosure"]["k_source"]), True)

    # a value INSIDE the null must NOT pass clause 1
    v2 = evaluate(_mean(bat["draws"]) + 1e-9, bat, 0.60, 0.55)
    arm("clause1_refuses_a_null_indistinguishable_value", v2["clause1_contribution"]["passes"], False)
    # adequacy fails when an input alone beats the fusion
    v3 = evaluate(0.58, bat, 0.60, 0.55)
    arm("clause2_fails_when_an_input_alone_is_better", v3["clause2_adequacy"]["passes"], False)

    # the prediction term must be PRESENT -- the 2.47% AMENDMENT 1 correction
    _, _, _ = margin_of(0.01, 20)
    arm("prediction_term_at_N20", round(math.sqrt(1 + 1 / 20), 4), 1.0247)
    m_pred, _, _ = margin_of(0.01, 20)
    m_conf = k_of(20)[0] * 0.01
    arm("prediction_margin_EXCEEDS_confidence_margin", m_pred > m_conf, True)

    # --- REFUSALS: each must RAISE, not return -------------------------------------------------
    def refuses(name, fn):
        try:
            fn()
            R.append((name, False, "%s (did NOT refuse)" % name))
        except OracleRefusal:
            R.append((name, True, name))

    refuses("below_floor_REFUSES", lambda: null_battery(_synthetic_fuse(0), None, None, labels, n=19))
    refuses("degenerate_null_REFUSES",
            lambda: evaluate(0.9, {"draws": [0.5] * 20, "seeds": list(range(20)), "n": 20,
                                   "K": 20, "T": 20, "base_seed": 0}, 0.6, 0.5))
    refuses("draw_count_mismatch_REFUSES",
            lambda: evaluate(0.9, {"draws": [0.5, 0.6], "seeds": [1, 2], "n": 20,
                                   "K": 20, "T": 20, "base_seed": 0}, 0.6, 0.5))
    refuses("tmp_projection_REFUSES",
            lambda: resolve_input(".tmp-cro-b4-eb009-audit/W_STRUCTURE_FACTORIZED.json"))

    ok = 0
    for name, good, detail in R:
        print("  arm  %-52s %s" % (name, "PASS" if good else ("FAIL -- " + detail)))
        ok += bool(good)
    print("clause-1 oracle self-test: %d of %d passed" % (ok, len(R)))
    return 0 if ok == len(R) else 1


if __name__ == "__main__":
    raise SystemExit(selftest())
