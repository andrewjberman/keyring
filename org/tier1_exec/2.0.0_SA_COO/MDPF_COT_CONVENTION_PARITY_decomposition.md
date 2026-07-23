# MDPF_COT_CONVENTION_PARITY -- COO decomposition (W-1..W-6)

**Charter:** `docs/architecture/MDPF_COT_CONVENTION_PARITY_PRD.md` @e1d525341 (Andrew-direct, CTO-bound).
**COO owner:** `2.0.0_SA_COO` (decomposition + W-1/W-4/W-5 clock + synthesis). **CTO gate.**
**Record note:** the record caught up to execution -- CTO fast-tracked W-2b/W-3/W-6 directly during the
~20min the TO record lagged Andrew's charter (owned: COO prioritized the live $1.78B->$1.95B publish-path over
formalizing; CTO's direct dispatch was the correct correction). This doc formalizes all six.

## The bound convention (Andrew's articulation, PRD @e1d525341)
"Interpolated" is a **provenance class** on the model series, NEVER an additive dollar series. COT total AUA is a
**measured** quantity from daily holdings snapshots ($458M-class). Per-firm + Global convention parity:
**total / model / non-model-balance**, with the standing per-date identity **total == model + non_model**. The
tooltip must read Total from the TOTAL series, model buckets as detail, non-model as the balance -- and NEVER
sum a provenance channel as dollars. Verified quantities (NOT reopened): $458M (COT total holdings),
$124,376,009.73 (COT model overlay), their difference $334M-class (non-model balance).

## Work items

| WI | Title | Owner | Status | Acceptance |
|---|---|---|---|---|
| **W-1** | 49F/INF canonical total/model/non-model assessment | COO->DS (clock: COO) | TODO | For 49F + INF: confirm the total/model/non-model-balance triple + the per-date identity holds on the served artifacts; cite the source series per firm (49F schwab-rps / INF eclipse+orion). No new numbers reopened. |
| **W-2b** | COT daily artifact: total series + non-model balance | DS | **EXECUTING** (CTO fast-track) | COT daily artifact carries the measured TOTAL series ($458M-class) + non-model = total - model ($334M-class), additive per DS pre-scoping, through production scripts. |
| **W-3a** | Tooltip stops summing the provenance channel | DE | **EXECUTING** (CTO fast-track, Andrew-watched) | Daily-view tooltip reads Total from the TOTAL series, model buckets as detail; the $124M+$124M=$248M double-count is GONE. Data-independent; mutant-proof + condition-4; own promote behind tonight's. |
| **W-3b** | Total/balance display wired to W-2b shape | DE | BLOCKED on W-2b | Wires when DS's W-2b artifact shape lands; renders total/model/non-model-balance per the convention. |
| **W-4** | Standing identity-gate cell: total == model + non_model | COO (clock: COO) | TODO | A gate CELL (per-date, per-firm) asserting total == model + non_model to the cent; reads from the artifact (DE's count-axis note: account_count_by_model_key + cottonwood_fold). Lands as an instrument, not a review. |
| **W-5** | Convention record (doctrine) | COO (clock: COO) | TODO | The convention (provenance-class-never-additive; measured-total; the identity) recorded as durable doctrine so future surfaces inherit it. |
| **W-6** | Global bell curve = 3-firm (COT parity on a Global surface) | DS(data)+DE(key) | **DONE + byte-verified** | Global bell renders 49F+INF+COT (294 COT accounts folded); json/portfolios/account-distribution.json cottonwood-present (md5 f45c37e1, active 7,913). >> CLOCK: legacy smartx Lambda rewrites this key ~13:00Z daily -> CTO ruled (a) 0.7.0 disable Step-4 write tonight + (b) DE re-point bell to MDPF key. **P2 instance #1** (producer-set != consumption-set). |

## Sequencing
W-2b/W-3/W-6 = P0 opening moves of the serving-architecture program (already executing/done). W-1/W-4/W-5 on the
COO clock, non-blocking the live product. W-4's identity cell is a candidate P2 parity-instrument sibling (a
standing per-date check, not a one-time verify). W-5 folds into the synthesis architecture doc + doctrine.

## Not reopened
$458M / $124,376,009.73 / their difference are verified quantities. This family is REPRESENTATION + CONVENTION
(how the tooltip/bell read + label them), never a re-derivation of tonight's numbers.

-- `2.0.0_SA_COO`, ~20:11Z (formalizing behind CTO's fast-track execution)
