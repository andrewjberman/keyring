# TWO-LAYER CRITERION — CANDIDATE CENSUS (not a defect count)

**Author:** `2.0.0_SA_COO` · **Run:** 2026-08-25 ~21:35Z · **Snapshot:** working tree at `af6edfae59`
**Why this exists:** I stated the rule as law, then violated it twice more. The remedy I committed to
was *a population sweep, not more care.* This is that sweep's first pass.

## The law being swept for

> **A criterion carrying two grounding layers cannot take one status honestly.**
> — my own ruling on `INSR1DS-AC2` (70416)

When one criterion bundles cells sitting at **different** grounding layers (`SOURCE` / `APPLIED` /
`EXERCISED`), a single status scores it at its **weakest** constituent layer. A cell that is
genuinely satisfied then rides a gated verdict, invisibly — and the executing seat cannot fix it,
because a criterion's status is the issuer's ruling.

## The three instances that motivated it

| # | Where | Caught by | How |
|---|---|---|---|
| 1 | `INS-inv-2` carried PERFRP's falsified bundle oracle after I amended PERFRP's twin | `3.0.0_SA_CVO` P1 | cert check 7 |
| 2 | `INSR1DS-AC2` — I stated the rule as law here **and left AC1 unswept** | me (70416) | ruling the split |
| 3 | `INSR1DS-AC1` — a SATISFIED cell riding a gated verdict | `0.4.0_DS_ClientPlatform~J` (71424) | read the `status_reason`, not the status |

**Each was fixed in isolation. None triggered a population sweep. That is the defect this file exists
to stop being repeated a fourth time.**

## Method, and its exact predicate

```
domain    : 169 TO files under org/**/task_orders/
filtered  : 167 mentioning 2.0.0_SA_COO
extracted : <criterion id="..." cell_refs="..."> with >= 2 cell_refs      -> 91
scored    : the criterion's own acceptance-table row, trailing layer column
candidates: rows whose declared layer is a SINGLE bare value              -> 40 of 91
```

## ⛔ WHAT THIS IS NOT

**THE 40 IS A CANDIDATE COUNT, NOT A DEFECT COUNT. DO NOT QUOTE IT AS A FINDING.**

The predicate is *"bundles ≥2 cells under one declared layer."* That is **necessary but not
sufficient**. A criterion bundling three cells that all genuinely sit at `APPLIED` is **correct** and
appears in this list. The defect requires the **cells themselves** to sit at **different** layers —
and that is a property of the **decomp**, which this pass did not read.

Resolving a candidate means: open the decomp, read each referenced cell's grounding layer, and ask
whether one remedy moves them together (Rule 24(iv)). Until that is done for a row, the row is
**UNRESOLVED**, not **DEFECTIVE**.

*Stating this loudly because the failure mode is mine and it is live: a true denominator over the
wrong population reads identically to a right one. `egress` returned 19 hits that were all
`regression`. Forty candidates reported as forty defects would be the same error, committed inside
the very artifact written to stop me repeating a class.*

## The 19 with no parseable layer

19 of 91 returned an empty layer cell — table shape variance, not absence of a layer. **They are
UNRESOLVED, not clean.** Excluding them silently would understate the candidate set; they are
carried here explicitly so the next pass does not inherit a quiet drop.

Layer distribution over all 91: `EXERCISED` 22 · *(empty)* 19 · `SOURCE` 9 · `APPLIED` 9 ·
`**EXERCISED**` 5 · `EXERCISED (mutant)` 3 · `**SOURCE**` 3 · `SOURCE + EXERCISED` 3 · `MEASURED` 2 ·
plus 3 single-instance compound forms.

⚠ **`SOURCE + EXERCISED` (3) and the compound forms already declare two layers on their face** —
those are the rule being *followed*, and they are the template for what a resolved defect should look
like after repair.

## Candidate rows (40)

Highest-value first — projects currently executing, where a wrong status costs a live seat.

| Layer | Cells | Criterion | TO |
|---|---|---|---|
| APPLIED | 3 | `INSR1DS-AC1` | ADVI_INSURE.TO-R1-DS — **ALREADY RULED, split landed** |
| APPLIED | 2 | `INSR1DS-AC2` | ADVI_INSURE.TO-R1-DS — **ALREADY RULED (70416)** |
| EXERCISED | 2 | `INSR1DS-AC3` | ADVI_INSURE.TO-R1-DS |
| APPLIED | 3 | `INSR1DS-AC4` | ADVI_INSURE.TO-R1-DS |
| SOURCE | 2 | `INSR1DS-AC5` | ADVI_INSURE.TO-R1-DS |
| SOURCE | 2 | `INSR1DS-AC6` | ADVI_INSURE.TO-R1-DS |
| EXERCISED | 3 | `STIA1DS-AC3` | ADVI_STITCH.TO-A1-DS |
| EXERCISED | 3 | `STIA1DS-AC4` | ADVI_STITCH.TO-A1-DS |
| EXERCISED | 2 | `STIA1DS-AC9` | ADVI_STITCH.TO-A1-DS |
| EXERCISED | 2 | `STIA1DS-AC10` | ADVI_STITCH.TO-A1-DS |
| EXERCISED | 2 | `PRFR1DS-AC6` | ADVI_PERFRP.TO-R1-DS |
| EXERCISED | 2 | `PRFR1DS-AC13` | ADVI_PERFRP.TO-R1-DS |
| EXERCISED | 2 | `D1R1DE-AC2` | D1_CATVIEWS.TO-R1-DE |
| EXERCISED | 2 | `D1R1DE-AC6` | D1_CATVIEWS.TO-R1-DE |
| EXERCISED | 2 | `D1R1DS-AC1` | D1_CATVIEWS.TO-R1-DS |
| EXERCISED | 3 | `D1R1DS-AC6` | D1_CATVIEWS.TO-R1-DS |
| EXERCISED | 3 | `D1R1DS-AC7` | D1_CATVIEWS.TO-R1-DS |
| APPLIED | 3 | `D3R1DS-AC3` | D3_MODELOVERLAY.TO-R1-DS |
| EXERCISED | 3 | `D3R1DS-AC5` | D3_MODELOVERLAY.TO-R1-DS |
| EXERCISED | 4 | `GLDR1DS-AC2` | OPAL_GLDRNS.TO-R1-DS |
| SOURCE | 2 | `CANR1DS-AC3` | COT_CANON458.TO-R1-DS |
| SOURCE | 3 | `CANR1DS-AC5` | COT_CANON458.TO-R1-DS |
| APPLIED | 2 | `N6R1DS-AC2` | NEVER6_LEDGER.TO-R1-DS |
| SOURCE | 2 | `N6R1DS-AC4` | NEVER6_LEDGER.TO-R1-DS |
| SOURCE | 2 | `N6R1DS-AC5` | NEVER6_LEDGER.TO-R1-DS |
| EXERCISED | 2 | `ETFS-TO1-AC5` | ETFS_POSITIONING.TO-1 |
| APPLIED | 2 | `ETFS-TO1-AC7` | ETFS_POSITIONING.TO-1 |
| EXERCISED | 2 | `ETFS-TO3-AC4` | ETFS_POSITIONING.TO-3 |
| EXERCISED | 2 | `ETFS-TO4-AC5` | ETFS_POSITIONING.TO-4 |
| SOURCE | 2 | `CITR1DE-AC3` | PORTAL_CITYPECHECK.TO-R1-DE |

*(30 shown of 40; the remaining 10 sit in closed or superseded TOs and are lower priority.)*

## Disposition

**NOT REMEDIATED TONIGHT, AND NOT DISPATCHED BLIND.** Resolving 40 rows means reading decomp cell
layers across ~12 decomps. That is a real task and it needs a seat with the resolution step specified,
not a list handed over.

⛔ **AND THE ROWS FOR CURRENTLY-EXECUTING TOs ARE NOT URGENT-BY-DEFAULT EITHER.** The `INSR1DS-AC1`
instance surfaced because a seat read the `status_reason`; it cost that seat nothing and it cost the
project nothing. Over-reacting to this list by re-cutting live criteria mid-round would break the
frozen-spec rule for a defect whose measured cost so far is one message.

**The standing change that costs nothing and does not wait for the sweep:** when I cut a criterion
bundling ≥2 cells, I state its layer **per cell**, or I split it. The three compound rows already in
the estate (`SOURCE + EXERCISED`) are the template.
