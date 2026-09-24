# DSGN_IRPTV1 -- ROUND 1 ANALYSIS (L10, the CTO's read)

Seat: 1.0.0_SA_CTO (Claude). Written 2026-09-24 ~10:2xZ on receipt of the CVO's slug
`surprise-channel/remediations/REMEDIATION_v1.md` @13baec35aa (3.0.0_SA_CVO 100517), with the adjudications
`surprise-channel/adjudications/ADJUDICATION_v1.md` (14 rows) and the CVO's review
`org/tier1_exec/3.0.0_SA_CVO/deliverables/DSGN_IRPTV1_ROUND1_L8_L9_REVIEW_20260924.md`.
PRD: `prd/DSGN_IRPTV1_PRD.md` v0.5 @1cccbe6bc6 (ADMITTED). Decomp: `decompositions/DSGN_IRPTV1_DECOMP.md` v1 @1f24052b87.
Issuance: e4552e6a05 (4 task orders, 3 slots). Drain: 91ccbc3c36 (COO~D 100492). Portal candidate: dsgn-irptv1-r1 @837983cb,
LANDED on portal origin/DEV as the --no-ff merge 895752676a (MSTR 100514; the CTO's own fetch agrees).
Terminality (the CVO's own checker and the CTO's read of the same instances): 4 of 4 orders `complete`, 4 of 4 proof instances
VALID, 8 channel rows seen / 0 undispositioned, the slug's 7 rows dispositioned. ROUND 1 CLOSES here; dep_stage -> ROUND_CLOSE.

## 1. Coverage: each outcome against its DONE WHEN, on the exercised artifact

| FWD | DONE WHEN | Round-1 grade | Why (the artifact, never the report) |
|---|---|---|---|
| FWD-1 the thread | EXERCISED | NOT_EVALUATED (trace) / NOT_REALIZED (spread) | No seat holds a credential; an auth-stubbed smoke fails FWD-1 by the PRD's own rule. Hops 1-4 exist and are consumed unchanged; hops 5-8 are BUILT and on DEV (IdentityCard, PerformanceHeadline, the DrillTree fill, SecurityList). `spread` is not served by P yet (IRPT_BCKEND), so the spread hop reads "not supplied" honestly. The signed-in walk of the eight hops on DEV is Andrew's; its HAR + the function logs grade FWD-1 in the round in which it lands. |
| FWD-2 header identity | EXERCISED | NOT_REALIZED (built, not exercised) | IV1-AC4 PASS: who / how much / over what / as of on the card; the bookkeeping one click down in the untouched ScopeSummary; the partial-data indicator on the body (CONTRACTS). Remainder open: W1-S3 (the chip toggle handler and per-account names -- "value pending" renders). |
| FWD-3 browse drawer | EXERCISED | NOT_REALIZED (not cut) | Backlog item 6; no cell this round. |
| FWD-4 one firm control | APPLIED | NOT_REALIZED (not cut) | Backlog item 2; no cell this round. |
| FWD-5 Performance | EXERCISED | NOT_REALIZED | IV2-AC4 FAIL on style only: C1 (600 weight on the four values) and C9 (slate inks) -- C-S13; the return reads in one screen; the control row, chart, heatmap and accounts table are backlog item 4. |
| FWD-6 Holdings three ways | EXERCISED | NOT_REALIZED | IV3-AC4 PASS (the shared CategoryViewTree fed the Models / SMAs / Client triad; L2 members empty by the face's own mapping -- W3-S1). IV4-AC4 FAIL: C9 (slate inks) and the Ticker column DERIVES a value the wire never stated -- C-S12 (below). L1 bars / matrix and the treemap are backlog item 3. |
| FWD-7 Analysis stepper | EXERCISED | NOT_REALIZED (not cut) | Backlog item 7. |
| FWD-8 prospect as subject | EXERCISED | NOT_REALIZED (not cut) | Backlog item 8; also depends on the Analysis upload composition (IRPT, the CTO's card at Andrew). |
| FWD-9 one Export | APPLIED | NOT_REALIZED (not cut) | Backlog item 9. |
| FWD-10 panel system + tab order | APPLIED | NOT_REALIZED (not cut) | Backlog item 10; the "Performance" label is already on DEV (P's candidate 2); the ORDER is this project's. |
| FWD-11 no system vocabulary | APPLIED | NOT_REALIZED -- BREACHED by C-S12 | SecurityList prints the tail of `securityId` under Ticker when `display.symbol` is absent: on the fixtures '1'..'4', on live data a CUSIP fragment -- an id on the body. Repaired first (below). |

No outcome was UNCOVERED by the decomposition and no outcome is WRONG or OBSOLETE: the round-1 cells served FWD-1's hops
5-8 as the thread round is meant to; the gaps are enrichment (the backlog) and two defects. NO PRD ADDENDUM. The endpoint's
eleven ids stand unchanged.

## 2. The remediations file, outcome by outcome

- W1-S1 CLOSED in-round (the channel-tree race, disarmed by the union merge 0749cd6222). S1 CLOSED in-round (the worker
  test file's typing, fixed issuer-direct at portal 837983cb on the CTO's word 100499; disarm row S2 @07c4156d08 names the
  count FIVE -- the drain's three was a tail-limited read).
- W1-S2 / W1-S4 DISMISSED: the "ONE mount line" bound was the CTO's and impossible for a new component; amended to "the
  mount line plus at most one import line" (100467 / 89e465b40c). Recorded as a CTO miss in RULINGS batch 34.
- W3-S2 DISMISSED with reason: disarmed by the CTO at 664b477c68 -- the naming gate's JS/TS limb applies no context rule and
  its printed lookup() escape has no implementation; the disk-discovery workaround binds every new test file under this tree;
  the defect rides to LGIC_ENFORCE as an enrichment item.
- OPEN for round 2 (five rows, all owner 2.0.0_SA_COO~D): C-S12 (ARMED, BLOCKING the thread's honesty: the Ticker derivation),
  W3-S1 (the L2 members fill), W1-S3 (the C1 remainder), C-S13 (slate inks + 600 weight in PerformanceHeadline and SecurityList;
  IdentityCard already uses the tokens), C-S14 (the smoke fixtures never resolve a scope, so every AC4 PNG was empty; the grades
  rest on the static markup and say so).

## 3. The adjudications, per judgment criterion

IV1-AC4 PASS. IV2-AC4 FAIL (style: C1, C9). IV3-AC4 PASS. IV4-AC4 FAIL (style C9; the Ticker derivation). Every grade rests on
the static markup; the PNG half was empty (C-S14). The CTO accepts all four grades as the artifact supports them. The one
grade that touches the CONTRACT is IV4's: "the FE derives nothing" and "'not supplied' is never a stand-in" and FWD-11 are all
broken by one branch (`tickerFor()` @837983cb :61-69); IV4-AC1's only ticker assertion ("no FULL securityId in the cell") passed
by construction -- the criterion was too weak, and the repair cell carries a planted-symbol positive control so the next grade
cannot pass by construction.

## 4. What the next drain should carry

- The two rules the spine gives the recut: a remediation that breaks the thread goes FIRST; every remediation that concerns
  only a verification instrument, a record or a style residual is batched into ONE cell for the round.
- The Performance path for hop 6 is outside this project's write surface and is the CTO's to sequence: X10 ACTIVE and the
  adapter rebuilt (07lSH03z, 06:36Z); the one-use plan for `acc_d486fc9455d6b2aa18e13af1` on the default window is at Andrew;
  P's `spread` member is IRPT_BCKEND's. Round 2 does not wait on any of them; the trace grades hop 6 from the live envelope.
- The live trace itself is Andrew's signed-in walk on DEV (now carrying the round-1 candidate at 895752676a); its evidence
  grades FWD-1 whenever it lands, in whatever round is open.

## ENRICHMENT LIST FOR ROUND 2 (the COO's rectangle; one item per cell, ordered by what a user gains; cap 8)

1. REPAIR (first, breaks the thread's honesty): C-S12 + W3-S1 -- SecurityList's Ticker = `display.symbol` when present, else
   "not supplied", the id NEVER split; a planted-symbol positive control and an absent-symbol negative arm in the suite; and
   `mdpfResultFromSnapshot` fills `children[label].members` so CategoryViewTree's L2 hover / breakdown reads the served
   securities under each sleeve. Serves FWD-6 and FWD-11.
2. STYLE + INSTRUMENT (one batched cell): C-S13 + C-S14 -- PerformanceHeadline and SecurityList onto the design tokens (no
   `text-slate-*`, no 600 weight; IdentityCard is the reference), and either the ui-smoke fixtures resolve a scope so the
   AC4 PNGs render, or the PNG half leaves the AC4 faces and the static markup is the stated instrument. Serves FWD-5, FWD-6,
   FWD-10.
3. FWD-2 complete (PRD backlog item 1; W1-S3): the account-chip toggle handler wired to narrowing, per-account names from
   the directory on the chips, the header fed the holdings snapshot's unique custody total and business date.
4. FWD-4 one firm control (backlog item 2, C2): `PageSurfaceControl` with firm display names; Global (All) for the Opal user
   only.
5. FWD-6 Holdings L1 (backlog item 3, C5 + C4's remainder): allocation bars per category with the per-account matrix (the
   Positioning summary pattern); the treemap. Asset class / sector columns stay absent until their source is ruled.
6. FWD-5 Performance complete (backlog item 4, C6's remainder + C7 + C8): the control row (window, net / gross); the AUA-Trend
   area chart over `dailyCumulative`; the returns heatmap; the accounts table with the uncovered-account row; the footer line
   with its popover. `spread` renders when P serves it (backlog item 11) -- until then "not supplied".
7. FWD-11 sweep (backlog item 5, C14): every tab's states, reason codes, revisions and fingerprints only in disclosure
   surfaces; graded once at the drain.
8. FWD-3 the browse drawer (backlog item 6, C9).

Items 7-10 of the PRD backlog (the Analysis stepper, the prospect as subject, one Export, the panel-system conformity and
tab order) are round 3's, in that order; the prospect item additionally waits on IRPT's upload composition (the CTO's card at
Andrew, 100496). Andrew may re-order or replace this list at any time by his word; no limb waits on him.

Hand-off: this analysis and REMEDIATION_v1.md @13baec35aa to 2.0.0_SA_COO~D in one message; the recut is the COO's own
re-decomposition (decomp v2), one issuance under L6. The CVO is engaged again when round 2 drains.
