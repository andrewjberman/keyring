# DENOMINATOR CROSS-EXAMINATION QUEUE — questionable tools ranked by measured usage

**Author:** 3.0.0_SA_CVO · 2026-07-29 ~17:25Z · **archetype:** VALIDATE
**Andrew-direct:** *"anything without an explicit denominator that fits into this category, do a
cross-examination based on tool-call counts from the mcp comp-tool jsonl and the session logs and
see what is called the most, rank the questionable tools by frequency of use and lets go down the
line from there analyzing and refining as needed."*

**Method:** questionable = UNCLASSIFIED ∪ `declares_denominator_in_output:False` ∪
`knows_own_denominator:False` ∪ (PERSISTED + non-kuzu universe). Usage cross-examined from BOTH
sources: `org/mcp/comp-tool-runs.jsonl` (9,758 rows, 07-14→now, real clock) and
`org/compiler-tools-log.md` per-run rows (27k, longer history). 7d column = current relevance.

**Headline: 82 of 89 tools flag** — the class is systemic, not a few offenders. 63 have measured
usage; **19 flagged tools have ZERO measured usage ever** (a /prune-quant retirement census in
waiting, incl. comp-whoread — a SIMULATE-class tool nobody has invoked).

## The queue (top 20 by combined use; walk order = 7d-weighted)

| # | tool | combined | jsonl | 7d | md-log | flags |
|---|------|----------|-------|----|--------|-------|
| 1 | comp-surface-check | 13,849 | 3,671 | 1,217 | 10,178 | no-denom-in-output, denom-unknowable |
| 2 | comp-pulse | 6,642 | 3,307 | 1,132 | 3,335 | denom-unknowable |
| 3 | comp-kuzu | 3,515 | 924 | 313 | 2,591 | no-denom-in-output, denom-unknowable |
| 4 | comp-pipescript | 2,937 | 145 | 95 | 2,792 | no-denom-in-output, denom-unknowable |
| 5 | comp-system | 1,212 | 592 | 480 | 620 | denom-unknowable |
| 6 | comp-iam | 958 | 217 | 185 | 741 | denom-unknowable |
| 7 | comp-blast | 777 | 97 | 52 | 680 | persisted-non-kuzu-surface |
| 8 | pipescript | 644 | 66 | 41 | 578 | UNCLASSIFIED (→ comp-opalbizsem, ~C WS1) |
| 9 | comp-routes | 527 | 116 | 95 | 411 | persisted-non-kuzu-surface |
| 10 | comp-manifest-check | 521 | 192 | 121 | 329 | denom-unknowable |
| 11 | comp-transform | 419 | 25 | 19 | 394 | no-denom-in-output, persisted-non-kuzu |
| 12 | comp-platinum | 377 | 28 | 10 | 349 | no-denom-in-output, persisted-non-kuzu |
| 13 | comp-validate | 278 | 24 | 22 | 254 | no-denom-in-output, persisted-non-kuzu |
| 14 | comp-aws | 261 | 20 | 13 | 241 | denom-unknowable |
| 15 | comp-trace | 254 | 2 | 2 | 252 | persisted-non-kuzu (historical; near-dead now) |
| 16 | comp-lambdamap | 177 | 32 | 9 | 145 | no-denom-in-output, persisted-non-kuzu |
| 17 | comp-build | 162 | 4 | 4 | 158 | persisted-non-kuzu-surface |
| 18 | comp-cache | 159 | 34 | 23 | 125 | denom-unknowable |
| 19 | comp-types | 140 | 28 | 24 | 112 | persisted-non-kuzu-surface |
| 20 | comp-drift | 121 | 10 | 3 | 111 | denom-unknowable |

## FIRST-PASS FINDING (before any per-tool walk): THE CARDS DRIFT IN BOTH DIRECTIONS

The refresh_mechanism field over-credits (stamps "gate-enforced at registration" on tools whose
DATA is snapshot-frozen — pipescript's 44d resolver PASSES a staleness query; registration-fresh ≠
data-fresh — the field-semantics split is ~C's WS3). And the top of this table shows the INVERSE:
**#1 and #2's cards under-credit their own behavior** — comp-pulse PRINTS a full denominator every
run ("N file(s) checked against 1484 danger node(s) — a MEASURED result, not a default") and
comp-surface-check prints its examined count, yet their cards flag them. Observed dozens of times
this session at commit time. **So the walk is not only "fix tools" — it is "reconcile card vs
BEHAVIOR per tool," in whichever direction the drift runs.** A card that under-credits teaches
agents to distrust a sound instrument; one that over-credits teaches them to trust a hollow one.

## Walk order (7d-weighted, skipping what is already in flight)

1. comp-surface-check + comp-pulse (2,349/7d combined — hook-embedded, so every commit inherits
   their card truth; likely card-fix not tool-fix)
2. comp-system (480/7d — the ~Z parity instrument; card claims vs its --check output)
3. comp-kuzu (313/7d — the canonical substrate itself; provenance header vs card)
4. comp-iam (185/7d — already has the deepest known-insufficiency record; card should carry it)
5. comp-manifest-check (121/7d) · comp-routes (95/7d) · comp-blast (52/7d — persisted surface,
   what snapshot does it read?)
SKIP as in-flight: comp-pipescript (WS4), pipescript (WS1/opalbizsem). PARK: the 19 zero-use
flagged tools → /prune-quant census after the walk.

— 3.0.0_SA_CVO
