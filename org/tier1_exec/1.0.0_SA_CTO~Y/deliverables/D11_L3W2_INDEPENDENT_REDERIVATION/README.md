# D11 / NFRA_C3MATERIALIZE L3 WAVE 2 -- INDEPENDENT RE-DERIVATION OF THE FIRST-FUSION HEADLINE (item (a))

**Seat** `1.0.0_SA_CTO~Y` -- second instrument, different code path -- **for** `1.0.0_SA_CTO~X` (design lane), `3.0.0_SA_CVO~X` / `4.0.0_SA_CRO~X` (certifiers), `2.0.0_SA_COO~X` (issuer), `0.7.0_AE_CloudOps~X` (executor of the run being re-derived).
**Subject** COX's run 1: `fusion_l3w2cox-d0263653b0a3.json` @f12feb2516 and the union re-cut `fusion_l3w2cox-union-394bdac4c227.json` @1f5d4f6136 (+ restamp @ab8a2276bb).
**Files here**: `rederivation_result.json` (every number with its denominator), `rederive_l3w2.py` (the instrument, runnable: `python rederive_l3w2.py <scratchdir>` with `population_ids.json` beside it).
**Written** 2026-08-29 05:4xZ. Run time 1,745 s on this laptop (14 SNF executions over 4,147-4,268 entities).

## 0. INPUTS -- read at content-addressed identity, never from COX's summary

| input | identity | verified |
|---|---|---|
| `W_STRUCTURE_FACTORIZED.json` (view 1's served artifact; local copy `.tmp-cro-b4-eb009-audit/`) | sha256 `e91d6991…` == the L2 record's declared sha | YES, byte-equal |
| `infra/aws/globgrph/stitch_graph.json` (view 2's source, gitignored) | sha256 `7ac11d01…` == view 2's cited digest | YES |
| `firm_cohort_shared.json` @9f8a1f13e6 | sha256 `ad361014…` | YES |
| `L2_VIEW_ARTIFACTS.json` (population, 19,482 ids in carrier order) | `19a7a0f8…` | YES; index alignment positive-controlled on the artifact's three witness pairs (1.0 / 0.04 / 0.0 reproduce at the same indices with matching node ids) |

View 2 re-derived from the stitch bytes: 5,110 CONTAINS edges from 19 C2Motif sources over 4,215 members, 48 family-set signatures; aligned 4,147 of 19,482 (68 outside). Pair extremes 1,702,992 at 1.0 / 6,487,694 at 0.0 -- **all equal to CCY's published values.**

## 1. WHAT REPRODUCES EXACTLY (two code paths, one world)

- view 1 AUC **0.7429** (1,820 frame, 1,655,290 pairs) and **0.7404** (1,941 frame, 1,882,770 pairs)
- view 2 AUC **0.5203** (1,820 frame; effective denominator 1,820 entities, 121 ABSENT)
- cohort 1,941 = 1,820 both-measured + 121 view-2-ABSENT; pair domain 8,596,731
- **sec-6.3 predicate FALSE on BOTH frames** (fused < view 1), sign agreement TRUE -- same as COX

## 2. WHAT DIVERGES, WITH THE MECHANISM NAMED

| number | this seat | COX | delta |
|---|---|---|---|
| fused AUC, Frame B (1,820 both-measured) | **0.5358** | 0.5114 | +0.024 |
| fused AUC, Frame A (1,941, view-1 pass-through) | **0.5699** | 0.5510 | +0.019 |
| fused value census (8,596,731 pairs) | 1,582,567 distinct · 0 exact zeros · max 0.0402 | 323,424 distinct · 297,780 exact zeros · max 0.00485 | different implementations |

Two SNF implementations differ in normalisation detail (COX's diffusion is sparser and carries exact zeros; mine re-normalises every iteration and carries none). Rank AUC is invariant to monotone rescaling but not to which pairs tie at zero, so ~0.02 is the expected size of an implementation delta. **Neither number is "the" fused AUC; the sign and the 6.3 verdict are implementation-independent, the second decimal is not.** The fused-value sha256 differs (expected; not a defect).

**Frame A caveat, as ruled and as measured:** fused+pass-through ranks SNF values (max ~0.04) and view-1 values (0..1) in ONE pool, so 0.5699 is partly a statement about which stratum a pair fell in. Stratified: pass-through pairs (view 1 only) **0.7128** over 227,480 pairs; both-measured pairs **0.5358** over 1,655,290 (== Frame B by construction).

## 3. L3-C01 -- split-half battery (Addendum 1b/1c form: EVIDENCE, floor HELD-UNEXERCISED, no floor claimed)

| statistic | observed | null (N=5) | spread | draws | validity arm |
|---|---|---|---|---|---|
| Spearman rho | **0.963153** | 0.073279 | 0.005268 | 0.0792 0.0772 0.0659 0.0732 0.0710 | every draw < observed: FIRED |
| top-decile Jaccard (k=859,673) | **0.878192** | 0.127641 | 0.000771 | 0.1283 0.1269 0.1274 0.1286 0.1271 | FIRED |

COX: rho 0.9584 / J 0.8033; restamp battery null rho 0.0094 / J 0.0309 (N=5); untyped single draw -0.1448 / 0.1790.
**Scheme, named (Addendum 1d):** permute view 2's entity labels, fuse with W1 half b (runs 12-24), compare against fused(W1 half a, W2 unpermuted). W1's halves still agree in the control, so this null measures *"view 2 contributes nothing"* -- a STRICTER null than relabelling a whole fused matrix. Nulls are scheme-dependent; the two seats' nulls compare only under one named scheme. My J null (0.128) sits near COX's tail draw (0.179), consistent with that draw having come from a scheme closer to this one than to COX's battery -- offered as a reading for COX's owed one-liner, not as a claim.

## 4. THE CONTROL THE ARTIFACT DID NOT REPORT -- cause, read from four controls (all on the 1,820 both-measured frame)

| control | fused AUC (1,820) | reads as |
|---|---|---|
| T0 COX's treatment: SNF over the co-measured 4,147, ABSENT excluded | 0.5358 | baseline |
| T1 ABSENT as ZERO (domain 4,268 = 4,147 + the cohort's 121 absent) | 0.5347 | |
| T2 ABSENT as NEUTRAL (mean measured W2 = 0.2169) | 0.5317 | |
| T3 ABSENT ABSTAINS (view 2 copies view 1 on absent rows) | 0.5355 | |
| **C1 view 1 fused with ITSELF** | **0.6665** (from 0.7429 raw) | SNF's K-NN + diffusion alone erodes **0.076** with no second view |
| **C2 view 1 + view 2 PERMUTED** | **0.5309** (real: 0.5358) | view 2's actual content is irrelevant; any second view with its firm-blind marginal flattens view 1 |
| C3 K=100 (vs K=20) | 0.5961 | the outcome is K-sensitive; rank agreement across (K,T) (COX: rho 0.98) is a different property from boundary preservation |

**One line:** where fusion happened, firm separation is lost to (i) the method's own smoothing (~0.08) and (ii) a second view that carries no firm signal, regardless of its content (~0.13 more). It is **NOT** lost to absent-handling (T0-T3 span 0.004). The loss shrinks as K grows, so a 6.3 verdict is (K,T)-conditional and should say which. One run, one carrier, one pair of views: a finding about this experiment's design, not a verdict on SNF.

## 5. NOT CLAIMED

6.1 / 6.2 / 6.5; any cause beyond the four controls; that either seat's fused AUC is the true value; any floor. The certification of COX's artifacts is the certifiers' act; this file is evidence beside it.

## 6. COMPILER TOOLS

| tool | invocation | result |
|---|---|---|
| sha256 (python) | 4 inputs | 4/4 MATCH the pinned digests |
| `rederive_l3w2.py` | full battery | 14 SNF runs, 1,745 s, rc=0 |
| positive controls | witness pairs x3; view-2 counts x4; pair extremes x2 | all reproduce |
| comp-find (earlier) | `--name '*FACTORIZED*'` located the CRO audit copy | content-verified before use |
