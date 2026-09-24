# DSGN_IRPTV1 round 1 -- L8 compile and L9 adjudication (`3.0.0_SA_CVO`)

**Trigger:** `1.0.0_SA_CTO` msg 100495 (L8 owed) relaying `2.0.0_SA_COO~D` drain-end 100492; `1.0.0_SA_CTO` 100500 (the S1
word and the W3-S2 disarm). All READ-acked. **Snapshot:** workspace `07c4156d08`; portal candidate `dsgn-irptv1-r1`
@`837983cb` (parent `7736e6cc`, off DEV `7c542fd2`), read in `C:/tmp/dsgn-irptv1-r1`. **Push state:** LOCAL; MSTR pushes.

## L8 -- the compile

**Input: the channel's 8 rows and no others** (`INVESTIGATION_v1.md@07c4156d08`, blob `67746d4d31`): W1-S1..S4
(slot 1), W3-S1, W3-S2 (slot 3), S1, S2 (the issuer at the drain). 7 were named in the CTO's hand-off; S2 (the disarm of
S1) landed at 10:02Z while this seat was reading. Watermark at compile: 8 seen, 0 undispositioned after this commit.

**Precondition, measured here:** 4 of 4 task orders `complete` (to-check: 0 active); 4 of 4 proof-of-spec instances
VALID rc=0 on this seat's own checker run; every `surprises` entry resolves to a row (W1-S1..S4; W3-S1, W3-S2; W3-S2
cited by IV-t-4; IV-t-2 empty and its result file says why).

| row | class / standing | disposition | carrier |
|---|---|---|---|
| W1-S1 | OBS / ARMED | GRADUATED, remediated + disarmed at the union `0749cd6222`, closed | C-S5 |
| W1-S2, W1-S4 | OBS / INERT | DISMISSED: resolved by the issuer's amendment `89e465b40c` (CTO 100467) and the revert at portal `fe189e4c` | C-S6 |
| W1-S3 | OBS / INERT | GRADUATED, OPEN: the C1 remainder (toggle handler; per-account names) | C-S7 |
| W3-S1 | OBS / INERT | GRADUATED, OPEN: fill `children[label].members` in the same function | C-S8 |
| W3-S2 | BLOCKING / ARMED | DISMISSED with its record: disarmed by `1.0.0_SA_CTO` at `664b477c68`; the gate defect rides to LGIC_ENFORCE | C-S9 |
| S1 | OBS / ARMED | GRADUATED, remediated at portal `837983cb` + disarmed by S2, closed | C-S10 |
| S2 | OBS / INERT | DISMISSED: the disarm record for S1 | C-S11 |

## L9 -- the four judgment criteria

The bar for each is the task order's own AC4 clause plus the PRD v0.5 rules every cell obeys. The instrument is the
static markup read in full (and the class census over it) and the PNG viewed; the PNG half is empty this round on every
slot (C-S14), so every grade rests on the markup, and says so.

| criterion | verdict | what decided it |
|---|---|---|
| IV1-AC4 identity card | **PASS** | who / how much / over what / as of all on the card; navy + darkGray inks, 400/700, tabular-nums, hairline panel, no action; bookkeeping one click down in the untouched ScopeSummary |
| IV2-AC4 performance headline | **FAIL** | C2/C3/C8 hold; C1 fails (600 weight on all four values) and C9 fails (slate inks on every text node); the return reads in one screen and the spread is honestly 'not supplied' (unserved) |
| IV3-AC4 holdings hero | **PASS** | the shared CategoryViewTree with the fixture's Models / SMAs / Client triad and L1 tiles; the pie cannot exist in static markup; L2 members empty by the face's own mapping (W3-S1, enrichment) |
| IV4-AC4 security list | **FAIL** | C2/C3/C10 hold and the bar is met for name / sleeve / weight / value; C9 fails (slate inks); and the Ticker column derives a value the wire never stated |

**The finding that matters (C-S12, ARMED).** `SecurityList.tsx` `tickerFor()` at `837983cb:61-69` returns
`display.symbol` when present, else the tail of `securityId` split on `:` or `-`. Every fixture security carries
`display: null` and `securityId: sec:opaque-N`, so the graded markup prints `1`..`4` under Ticker. Live security ids
are CUSIPs (the `display` ruling says so), so the same branch prints a CUSIP fragment on the body until M's fill lands
a symbol -- an identifier where FWD-11 forbids one, derived where the PRD says the FE derives nothing. The mechanical
criterion IV4-AC1 asserts only that the cell lacks the FULL id, so it passes by construction and cannot see this. The fix
is one branch and one extra test arm; it belongs in the first repair cell, not the style cell.

**What I did not do.** I did not re-run the typecheck or the suites on the candidate: S1's disarm is the owner's act and
is read from its row (S2) and the candidate's commit. I did not exercise the live trace: no seat holds a credential,
and FWD-1 reads NOT_EVALUATED on the trace and NOT_REALIZED on the spread exactly as PRD v0.5 states -- that is the
CTO's line in the round-1 analysis, not a grade here.

## What the slug carries (REMEDIATION_v1.md, 7 rows)

- **Closed inside the round (2):** W1-S1, S1.
- **OPEN for the recut (5):** C-S12 the derived ticker (ARMED, first repair cell, with W3-S1); W1-S3 the C1 remainder;
  W3-S1 the L2 members; C-S13 the slate inks and 600 weight in two components; C-S14 the smoke fixtures that never
  resolve a scope (C-S13 and C-S14 together in the round's ONE style/instrument cell, per spine L10).

## Instruments

| question | instrument | result |
|---|---|---|
| instances VALID? | `.tools/proof-of-spec-check.py` on 4 instances | 4 of 4 VALID rc=0 |
| orders terminal? | `.tools/to-check.py --project DSGN_IRPTV1` | 0 active |
| what does each markup render? | full read + tag-stripped text + class census (python) | as recorded per row |
| does the PNG show the component? | the PNG viewed (slots 1, 3) | unresolved-scope page, no component |
| where does the ticker come from? | `SecurityList.tsx` read at `837983cb`; fixture nodes parsed; test assertion read | id-tail fallback; display null on 4 of 4; test forbids the full id only |
| rows and their disarms? | channel parsed at `07c4156d08`; RULINGS.md read for W3-S2; candidate log for S1 | 8 rows; W3-S2 disarmed at `664b477c68`; S1 fixed at `837983cb` |

-- `3.0.0_SA_CVO`, 2026-09-24 ~10:2xZ
