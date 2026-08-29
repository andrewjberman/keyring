"""1.0.0_SA_CTO~Y -- (a) second-instrument re-derivation of the L3 wave-2 first-fusion headline.
Own code path: own W1/W2 construction, own SNF, own AUC, own split-half battery.
Inputs read at content-addressed identity (sha256 verified before use), never from COX's summary.
Every number printed with its denominator. Divergence from COX is reported, not reconciled.
"""

import hashlib
import json
import os
import sys
import time
import numpy as np
from scipy.stats import rankdata, spearmanr

t0 = time.time()


def log(*a):
    print(f"[{time.time() - t0:7.1f}s]", *a, flush=True)


S = sys.argv[1]
OUT = os.path.join(S, "rederive_l3w2_result.json")
R = {
    "seat": "1.0.0_SA_CTO~Y",
    "code_path": "independent (this file)",
    "inputs": {},
    "frames": {},
    "controls": {},
    "notes": [],
}


# ---------- inputs, hashed ----------
def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


FACT = ".tmp-cro-b4-eb009-audit/W_STRUCTURE_FACTORIZED.json"
STITCH = "infra/aws/globgrph/stitch_graph.json"
COH = "org/tier2_senior/0.7.0_AE_CloudOps/deliverables/D11_L3W2_FUSION/firm_cohort_shared.json"
L2 = "org/tier1_exec/4.0.0_SA_CRO~A/deliverables/NFRA_C3MATERIALIZE.TO-L2-CROA/L2_VIEW_ARTIFACTS.json"
EXP = {
    FACT: "e91d69910fc9d4eabb58eedb8a73165476225ab838977e8d6c16604af3f5e19a",
    STITCH: "7ac11d015e0ce4a068d6afb86cd51edddb8171b227afd5fc9e40ffb8d5dd5363",
    COH: "ad361014a7da885037421da005011c32b28cfb37f64da8feafad1cba95db3f19",
    L2: "19a7a0f8",
}
for p, e in EXP.items():
    h = sha(p)
    ok = h.startswith(e)
    R["inputs"][p] = {"sha256": h, "expected_prefix": e, "match": ok}
    log("INPUT", p, h[:16], "MATCH" if ok else "MISMATCH")
    if not ok:
        raise SystemExit(
            "input digest mismatch -- refusing to compute on a substituted input"
        )

ids = json.load(open(os.path.join(S, "population_ids.json")))
N = len(ids)
assert N == 19482
idx = {e: i for i, e in enumerate(ids)}
F = json.load(open(FACT))
PART = np.array(F["partitions"], dtype=np.int32)  # 25 x N
assert PART.shape == (25, N)
st = json.load(open(STITCH))
motif_ids = {
    n["id"]
    for n in st["classes_data"]["c2c3_motif"]["nodes"]
    if n.get("type") == "C2Motif"
}
fam = {}
for e in st["edges"]:
    if e.get("edge_type") == "CONTAINS" and e["source"] in motif_ids:
        fam.setdefault(e["target"], set()).add(e["source"])
families = sorted(motif_ids)
fi = {f: k for k, f in enumerate(families)}
measured = sorted(idx[t] for t in fam if t in idx)  # aligned by EXACT string equality
absent_view_members = sum(1 for t in fam if t not in idx)
n = len(measured)
log(
    "view2 alignment: aligned",
    n,
    "of",
    N,
    "| view members outside population",
    absent_view_members,
)
R["inputs"]["view2_alignment"] = {
    "aligned": n,
    "population": N,
    "outside_population": absent_view_members,
    "edges": sum(len(v) for v in fam.values()),
    "members": len(fam),
    "families": len(families),
}
assert n == 4147, n
M = np.array(measured, dtype=np.int64)

coh = json.load(open(COH))
firm = {}
for c in coh["cohort"]:
    firm[idx[c["entity_id"]]] = c["firm"]
assert len(firm) == 1941
coh_all = np.array(sorted(firm), dtype=np.int64)
coh_meas = np.array([i for i in coh_all if i in set(measured)], dtype=np.int64)
coh_abs = np.array([i for i in coh_all if i not in set(measured)], dtype=np.int64)
log("cohort 1941 = measured-in-view2", len(coh_meas), "+ absent", len(coh_abs))
R["inputs"]["cohort"] = {
    "size": len(coh_all),
    "both_measured": len(coh_meas),
    "view2_absent": len(coh_abs),
}


# ---------- view builders ----------
def W1_over(sub, runs=None):
    runs = range(25) if runs is None else runs
    W = np.zeros((len(sub), len(sub)), dtype=np.float32)
    for r in runs:
        p = PART[r][sub]
        W += p[:, None] == p[None, :]
    W /= float(len(list(runs)))
    np.fill_diagonal(W, 0.0)
    return W


def W2_over(sub):
    B = np.zeros((len(sub), len(families)), dtype=np.float32)
    for k, i in enumerate(sub):
        for f in fam.get(ids[i], ()):
            B[k, fi[f]] = 1.0
    inter = B @ B.T
    sz = B.sum(1)
    union = sz[:, None] + sz[None, :] - inter
    with np.errstate(divide="ignore", invalid="ignore"):
        W = np.where(union > 0, inter / union, 0.0).astype(np.float32)
    np.fill_diagonal(W, 0.0)
    return W, sz


def triu(W):
    iu = np.triu_indices(W.shape[0], 1)
    return W[iu]


# ---------- SNF (Wang et al. 2014), own implementation ----------
def P_norm(W):
    W = W.astype(np.float32, copy=True)
    np.fill_diagonal(W, 0.0)
    rs = W.sum(1)
    P = np.zeros_like(W)
    nz = rs > 0
    P[nz] = W[nz] / (2.0 * rs[nz][:, None])
    np.fill_diagonal(P, 0.5)
    return P


def S_knn(W, K):
    W = W.astype(np.float32, copy=True)
    np.fill_diagonal(W, -np.inf)
    order = np.argsort(-W, axis=1, kind="stable")[
        :, :K
    ]  # tie-break: stable argsort, ascending index -- DECLARED
    Sm = np.zeros_like(W)
    rows = np.arange(W.shape[0])[:, None]
    vals = W[rows, order]
    vals[~np.isfinite(vals)] = 0.0
    rs = vals.sum(1)
    nz = rs > 0
    Sm[rows[nz], order[nz]] = vals[nz] / rs[nz][:, None]
    return Sm


def SNF(Ws, K=20, T=20):
    Ps = [P_norm(W) for W in Ws]
    Ss = [S_knn(W, K) for W in Ws]
    Ps = [(P + P.T) / 2 for P in Ps]
    for t in range(T):
        new = []
        for v in range(len(Ws)):
            other = sum(Ps[u] for u in range(len(Ws)) if u != v) / (len(Ws) - 1)
            new.append(Ss[v] @ other @ Ss[v].T)
        Ps = [(P_norm(P) + P_norm(P).T) / 2 for P in new]
    Pc = sum(Ps) / len(Ps)
    Pc = (Pc + Pc.T) / 2
    return Pc


# ---------- AUC ----------
def auc_from(values, labels_same):
    """P(within-firm pair outranks cross-firm pair), ties = 0.5 (Mann-Whitney via average ranks)."""
    v = np.asarray(values, dtype=np.float64)
    s = np.asarray(labels_same, dtype=bool)
    nw = int(s.sum())
    nc = int((~s).sum())
    r = rankdata(v, method="average")
    return float((r[s].sum() - nw * (nw + 1) / 2) / (nw * nc)), nw, nc


def pair_labels(sub):
    f = np.array([firm[i] for i in sub])
    same = f[:, None] == f[None, :]
    return triu(same)


# ---------- MAIN: T0 = COX's treatment (SNF over the 4,147 co-measured only) ----------
log("building W1, W2 over the", n, "co-measured entities")
W1 = W1_over(M)
W2, fsz = W2_over(M)
u1, u2 = triu(W1), triu(W2)
PD = len(u1)
assert PD == 8596731
R["inputs"]["view2_positive_control"] = {
    "pairs_1.0": int((u2 == 1.0).sum()),
    "pairs_0.0": int((u2 == 0.0).sum()),
    "ccy_published": {"pairs_1.0": 1702992, "pairs_0.0": 6487694},
}
R["inputs"]["view1_distinct_values_on_domain"] = int(len(np.unique(u1)))
log(
    "view2 control: 1.0 pairs",
    (u2 == 1.0).sum(),
    "0.0 pairs",
    (u2 == 0.0).sum(),
    "| pair domain",
    PD,
)

log("SNF main K=20 T=20 ...")
FU = SNF([W1, W2], 20, 20)
uf = triu(FU)
R["fused"] = {
    "pair_domain": PD,
    "distinct_values": int(len(np.unique(uf))),
    "min": float(uf.min()),
    "max": float(uf.max()),
    "exact_zeros": int((uf == 0).sum()),
    "sha256_float32_triu": hashlib.sha256(uf.astype(np.float32).tobytes()).hexdigest(),
    "cox_sha256": "d0263653b0a36b29ced066be8d43b18c7c0c641874aa01977d2f0459d307bf48",
}
log(
    "fused: distinct",
    R["fused"]["distinct_values"],
    "max",
    uf.max(),
    "zeros",
    (uf == 0).sum(),
    "sha",
    R["fused"]["sha256_float32_triu"][:16],
)

# positions of cohort entities inside M
posM = {i: k for k, i in enumerate(M)}
cm = np.array([posM[i] for i in coh_meas])
labB = pair_labels(coh_meas)


def sub_triu(W, pos):
    return triu(W[np.ix_(pos, pos)])


fB = {}
for name, W in (("view1", W1), ("view2", W2), ("fused", FU)):
    a, nw, nc = auc_from(sub_triu(W, cm), labB)
    fB[name] = {
        "AUC": round(a, 4),
        "within_pairs": nw,
        "cross_pairs": nc,
        "pairs": nw + nc,
    }
    log("FRAME B (1,820 both-measured)", name, "AUC", round(a, 4), "pairs", nw + nc)
fB["entities"] = int(len(coh_meas))
fB["cox_published"] = {"view1": 0.7429, "view2": 0.5203, "fused": 0.5114}
fB["sec63_predicate_fused_ge_view1"] = fB["fused"]["AUC"] >= fB["view1"]["AUC"]
R["frames"]["B_both_measured_1820"] = fB

# ---------- FRAME A: full 1,941 -- fused = SNF where both measured, view-1 PASS-THROUGH otherwise (as ruled 80833) ----------
W1A = W1_over(
    coh_all
)  # view 1 over the whole cohort (19,482-measured view; all 1,941 present)
labA = pair_labels(coh_all)
posA = {i: k for k, i in enumerate(coh_all)}
FA = W1A.copy()  # pass-through default
both = np.zeros(len(coh_all), dtype=bool)
both[[posA[i] for i in coh_meas]] = True
sel = np.array([posA[i] for i in coh_meas])
cmm = np.array([posM[i] for i in coh_meas])
FA[np.ix_(sel, sel)] = FU[np.ix_(cmm, cmm)]  # fused values where both measured
uA1, uAf = triu(W1A), triu(FA)
bothpair = triu(both[:, None] & both[None, :])
fA = {"entities": int(len(coh_all)), "view2_absent_entities": int(len(coh_abs))}
a, nw, nc = auc_from(uA1, labA)
fA["view1"] = {
    "AUC": round(a, 4),
    "within_pairs": nw,
    "cross_pairs": nc,
    "pairs": nw + nc,
}
a, nw, nc = auc_from(uAf, labA)
fA["fused_with_passthrough"] = {
    "AUC": round(a, 4),
    "within_pairs": nw,
    "cross_pairs": nc,
    "pairs": nw + nc,
    "CAVEAT": "MIXED SCALE: SNF values (max ~0.005, transition-normalised) and view-1 pass-through values (0..1) are ranked in ONE pool; a rank AUC over that pool is partly a statement about which stratum a pair fell in, not only about firm separation. Reported as ruled; the stratified rows beside it are the interpretable ones.",
}
a, nw, nc = auc_from(uAf[~bothpair], labA[~bothpair])
fA["passthrough_pairs_only_view1"] = {
    "AUC": round(a, 4),
    "within_pairs": nw,
    "cross_pairs": nc,
    "pairs": nw + nc,
}
a, nw, nc = auc_from(uAf[bothpair], labA[bothpair])
fA["both_measured_pairs_only_fused"] = {
    "AUC": round(a, 4),
    "within_pairs": nw,
    "cross_pairs": nc,
    "pairs": nw + nc,
    "note": "== Frame B fused by construction",
}
fA["view2"] = {
    "AUC": fB["view2"]["AUC"],
    "effective_denominator_entities": int(len(coh_meas)),
    "ABSENT_entities": int(len(coh_abs)),
    "pairs": fB["view2"]["pairs"],
    "note": "view 2 has no value on the 121 ABSENT; its row is Frame B's",
}
fA["sec63_predicate_fusedPT_ge_view1"] = (
    fA["fused_with_passthrough"]["AUC"] >= fA["view1"]["AUC"]
)
R["frames"]["A_full_cohort_1941"] = fA
log(
    "FRAME A (1,941): view1",
    fA["view1"]["AUC"],
    "fused+PT",
    fA["fused_with_passthrough"]["AUC"],
    "PT-only",
    fA["passthrough_pairs_only_view1"]["AUC"],
)

# ---------- L3-C01 split-half + permutation battery (Addendum 1 / 1a form) ----------
rng = np.random.default_rng(20260829)
half1 = list(range(0, 12))
half2 = list(range(12, 25))
W1a = W1_over(M, half1)
W1b = W1_over(M, half2)
log("SNF split-half a (runs 0-11) ...")
Fa = triu(SNF([W1a, W2], 20, 20))
log("SNF split-half b (runs 12-24) ...")
Fb = triu(SNF([W1b, W2], 20, 20))


def topdec_jaccard(x, y, frac=0.10):
    k = int(round(frac * len(x)))
    tx = set(np.argpartition(-x, k - 1)[:k].tolist())
    ty = set(np.argpartition(-y, k - 1)[:k].tolist())
    return len(tx & ty) / len(tx | ty), k


rho_obs = float(spearmanr(Fa, Fb).correlation)
J_obs, k = topdec_jaccard(Fa, Fb)
log(
    "split-half observed rho",
    round(rho_obs, 4),
    "J",
    round(J_obs, 4),
    "top-decile k",
    k,
)
NPERM = 5
nulls_rho = []
nulls_J = []
for p in range(NPERM):
    perm = rng.permutation(n)
    W2p = W2[np.ix_(perm, perm)]
    log(f"permutation {p + 1}/{NPERM}: SNF(W1b, W2 permuted) ...")
    Fbp = triu(SNF([W1b, W2p], 20, 20))
    nulls_rho.append(float(spearmanr(Fa, Fbp).correlation))
    nulls_J.append(topdec_jaccard(Fa, Fbp)[0])
    log("   null rho", round(nulls_rho[-1], 4), "J", round(nulls_J[-1], 4))


def battery(name, obs, nulls):
    # Addendum 1b @4c1886a50f: a run-N artifact carries the battery as EVIDENCE ONLY -- null, spread, n_permutations, observed --
    # with floor_status HELD-UNEXERCISED and NO floor_derivation block. No floor is computed or claimed here.
    null = float(np.mean(nulls))
    spread = float(np.std(nulls, ddof=1))
    return {
        "metric_domain": f"both-measured, {PD} pairs",
        "null": round(null, 6),
        "spread": round(spread, 6),
        "n_permutations": NPERM,
        "nulls": [round(x, 6) for x in nulls],
        "observed": round(obs, 6),
        "validity_arm_control_below_observed": bool(all(x < obs for x in nulls)),
        "held_floor": {"rho": 0.90, "J": 0.80}[name],
        "observed_clears_HELD_floor": bool(obs >= {"rho": 0.90, "J": 0.80}[name]),
    }


R["L3C01"] = {
    "method": "split-half over DISJOINT halves of the 25 accepted runs (0-11 / 12-24), each fused identically with view 2 at K=20 T=20; compared over the full both-measured pair domain; permuted-labels control = SNF(W1 half b, W2 with entities permuted) vs fused half a; seed 20260829",
    "observed": {
        "rho": round(rho_obs, 6),
        "J": round(J_obs, 6),
        "top_decile_k": k,
        "pair_denominator": PD,
    },
    "floor_status": "HELD-UNEXERCISED",
    "battery_evidence": {
        "rho": battery("rho", rho_obs, nulls_rho),
        "J": battery("J", J_obs, nulls_J),
    },
    "no_floor_derivation_block": "per Addendum 1b @4c1886a50f -- same-run derivation is prohibited; a later consumer derives the floor pointing backward",
    "cox_published": {
        "rho": 0.958398,
        "J": 0.803263,
        "null_rho": -0.144792,
        "null_J": 0.179046,
        "n_permutations": 1,
    },
}
json.dump(R, open(OUT, "w"), indent=1)
log("checkpoint written")

# ---------- CONTROLS on Frame B: is the collapse the METHOD, the WEAK VIEW, or ABSENT-HANDLING? ----------
ctrl = {}


def aucB(W):  # AUC on the 1,820 both-measured cohort frame, W indexed like M
    a, nw, nc = auc_from(sub_triu(W, cm), labB)
    return round(a, 4)


log("C1: SNF(W1, W1) -- view 1 fused with ITSELF")
F11 = SNF([W1, W1], 20, 20)
ctrl["C1_view1_with_itself"] = {
    "fused_AUC_1820": aucB(F11),
    "expect": "~view1 0.74 if SNF preserves a discriminating view; a collapse here would be the METHOD/normalisation, not view 2",
}
log("   ->", ctrl["C1_view1_with_itself"]["fused_AUC_1820"])
log("C2: SNF(W1, W2 permuted) -- view 2 carrying NO firm-aligned structure")
perm = rng.permutation(n)
F1p = SNF([W1, W2[np.ix_(perm, perm)]], 20, 20)
ctrl["C2_view1_with_permuted_view2"] = {
    "fused_AUC_1820": aucB(F1p),
    "expect": "if ~0.51 like the real fusion, view 2's actual content is not what flattens view 1 -- any near-uniform second view does",
}
log("   ->", ctrl["C2_view1_with_permuted_view2"]["fused_AUC_1820"])
log("C3: SNF(W1, W2 with K=100) -- neighbourhood size sensitivity")
F100 = SNF([W1, W2], 100, 20)
ctrl["C3_K100"] = {"fused_AUC_1820": aucB(F100)}
log("   ->", ctrl["C3_K100"]["fused_AUC_1820"])
# ABSENT treatments over D = measured ∪ the cohort's 121 view-2-ABSENT entities
D = np.array(sorted(set(measured) | set(coh_abs.tolist())), dtype=np.int64)
posD = {i: k for k, i in enumerate(D)}
W1D = W1_over(D)
W2D, _ = W2_over(D)
absD = np.array([posD[i] for i in coh_abs])
cmD = np.array([posD[i] for i in coh_meas])
caD = np.array([posD[i] for i in coh_all])


def aucD(W, pos, lab):
    a, nw, nc = auc_from(triu(W[np.ix_(pos, pos)]), lab)
    return round(a, 4)


log("T1: ABSENT-as-ZERO over", len(D), "entities")
FT1 = SNF(
    [W1D, W2D], 20, 20
)  # W2D rows for absent entities are already 0 (no families)
ctrl["T1_absent_as_zero"] = {
    "domain": int(len(D)),
    "fused_AUC_1820": aucD(FT1, cmD, labB),
    "fused_AUC_1941_genuinely_fused": aucD(FT1, caD, labA),
}
log("   ->", ctrl["T1_absent_as_zero"])
log("T2: ABSENT-as-NEUTRAL (mean measured off-diagonal W2)")
mu = float(u2.mean())
W2N = W2D.copy()
W2N[absD, :] = mu
W2N[:, absD] = mu
np.fill_diagonal(W2N, 0.0)
FT2 = SNF([W1D, W2N], 20, 20)
ctrl["T2_absent_as_neutral_mean"] = {
    "domain": int(len(D)),
    "neutral_value": round(mu, 6),
    "fused_AUC_1820": aucD(FT2, cmD, labB),
    "fused_AUC_1941_genuinely_fused": aucD(FT2, caD, labA),
}
log("   ->", ctrl["T2_absent_as_neutral_mean"])
log("T3: ABSENT abstains (view 2 copies view 1 on absent rows/cols)")
W2C = W2D.copy()
W2C[absD, :] = W1D[absD, :]
W2C[:, absD] = W1D[:, absD]
np.fill_diagonal(W2C, 0.0)
FT3 = SNF([W1D, W2C], 20, 20)
ctrl["T3_absent_abstains_copies_view1"] = {
    "domain": int(len(D)),
    "fused_AUC_1820": aucD(FT3, cmD, labB),
    "fused_AUC_1941_genuinely_fused": aucD(FT3, caD, labA),
}
log("   ->", ctrl["T3_absent_abstains_copies_view1"])
ctrl["T0_cox_treatment"] = {
    "domain": n,
    "fused_AUC_1820": fB["fused"]["AUC"],
    "note": "SNF over the co-measured 4,147 only (ABSENT excluded from the diffusion)",
}
R["controls"] = ctrl
R["elapsed_s"] = round(time.time() - t0, 1)
json.dump(R, open(OUT, "w"), indent=1)
log("DONE ->", OUT)
