# DSGN_RBNDV2 -- DECOMPOSITION (L5) -- ROUND 3, THE MODAL CHART REPAIR (PRD v0.1)

```json
{
 "project": "DSGN_RBNDV2",
 "directive": "D13",
 "macro": "DSGN",
 "fabric": "laptop",
 "decomp_version": "v3",
 "step": 5,
 "prd_ref": "org/missions/D13/DSGN/DSGN_RBNDV2/prd/DSGN_RBNDV2_PRD.md@e71a48e4b0 (v0.1, RATIFIED; both halves signed)",
 "round_analysis_ref": "org/missions/D13/DSGN/DSGN_RBNDV2/ledger/ROUND_ANALYSIS.round2.md@3c2a9cae02 (1.0.0_SA_CTO; CTO msg 109392)",
 "author": "2.0.0_SA_COO~RB",
 "round": 3,
 "rectangle": "the CTO's round-2 enrichment items 1 and 2 (item 1: the chart ticks and the footer clip in the Fear and Greed and Market Regime modals; item 2: the merge-time portal checks, which is the drain's own act); item 3 (the FWD-5 walk) starts on Andrew's YES to call 3c44; FWD-4 waits on call be0b",
 "cells": 1,
 "chains": 1,
 "join_cells": 0,
 "portal_base": "feature/dsgn-rbndv2-light @826551e2 (local, no upstream, never pushed)",
 "frozen": true
}
```

**Author:** `2.0.0_SA_COO~RB`. **Input:** the CTO's round-2 analysis (msg 109392) over the CVO's L9 grades `ADJUDICATION_v2.md` and `ADJUDICATION_v3.md` (RB2M4-AC3 NOT MET: the chart ticks of two modals are
literal white on the new silver body, and the Market Regime signal row is clipped by the footer). **Frozen at the cut.**

**Rulings reaching the cell:** PRD CONTRACTS C-BRANCH, C-MODAL, C-WALK; TOKEN FORMATS (`--rb-*` are HEX, read as `var(--rb-X)`; `--bg-surface`, `--hairline`, `--semantic-*` are HSL triples, read as `hsl(var(--X))`). The worker gets the worker face only.

## 1. THE DOMAIN, BY SUBTRACTION (Rule 24(i))

Denominator: the CTO's round-2 enrichment list, 3 items plus the FWD-4 hold. Item 1 PLACED as `RV-c-1`. Item 2 (every merge onto the branch runs the portal's typecheck, lint and the relevant tests and prints the counts in the merge record)
is the COO's drain act, not a worker cell: it was run by hand on the round-1 and round-2 merges (typecheck rc=0, 22 of 22 tests, eslint rc=0) and from this round on the counts are printed in each merge commit message
and in the round's close record. Item 3 (the FWD-5 walk) is HELD by the CTO's own condition (Andrew's YES to call `3c44`) and is cut when that word lands. FWD-4 HELD (call `be0b`). Remainder after subtraction: items 3 and FWD-4, held with their conditions.

**The measured population of item 1** (native Grep at the feature branch @826551e2): `FearGreedModal.tsx` holds 10 literal white chart props (`rgba(255,255,255,` at lines 401, 405, 406, 423, 424, 885, 889, 890, 907, 908: grid, axis stroke, tick fill) and
`MarketRegimeModal.tsx` holds 5 (lines 606, 610, 611, 625, 626). The footer clip has an exact cause: `MarketRegimeModal.tsx:484` passes `max-h-[72vh]` to `ModalFrame`, capping the surface below the frame's own
`max-h-[calc(100vh_-_2rem)]`, so the body scrolls inside a smaller box; no other modal passes a `max-h`. The same literal-white chart class may exist in the other three market modals; this cell reports them and does not touch them (a wall).

## 2. THE CELL -- 1 (round 3)

| cell | what it builds | serves | writes | reads (never writes) | risk | class |
|---|---|---|---|---|---|---|
| `RV-c-1` | the 15 literal white chart props in the two modals read tokens: tick fill `var(--rb-ink-3)`, axis stroke `var(--rb-quiet)`, grid stroke `var(--rb-rule)`; and `MarketRegimeModal` drops `max-h-[72vh]` from its `ModalFrame` className so the frame's own cap rules and the footer does not clip the signal row | FWD-3, FWD-5 | `src/components/market-performance/FearGreedModal.tsx`, `src/components/market-performance/MarketRegimeModal.tsx`, `src/components/market-performance/__tests__/dsgn-rbndv2/` | `src/ui/components/modal/ModalFrame.tsx`, `src/index.css` | LOCAL | worker-light |

## 3. PLACEMENT, EDGES, BATTERY

One portal cell, one worktree from the feature branch; M = 1 chain, N = 1, cap 8; the write set is disjoint from every other open order (none is open). The closing proof is a computed-style read of a chart tick's `fill` in each modal and of the
signal row against the footer in the live build, by the COO at the drain, then the CVO's grade. comp-iam, comp-schedule: not applicable. comp-adversary: the two files exist at the feature tip; the graph check (portal rule 20): the two modals have one importer each
(`SentimentGauge.tsx`).

## 4. RULE 24 FOUR-POSTULATE RECORD

(i) MECE over the CTO's list by subtraction (section 1). (ii) One grain, one cell. (iii) One intent: the modal charts and the footer cap of two files. (iv) State coherence: the chart series colours, tooltips and data logic do not move; only the
tick, axis and grid chrome and one cap class change.

## 5. FINDINGS FOR THE CTO (at the cut)

- The footer clip is a one-class cause (`max-h-[72vh]` passed by the modal), so the cell is small; the 15-prop chart class is the real work.
- Item 2 is executed as drain discipline; the counts print in the merge commit message.

**Addendum 1 (issuer, 2026-10-15 ~12:0xZ; the issuer rules inside its own decomposition, /canonical-drive obligation 7):** one DIRECT-ACT cell, from the `RV-c-1` worker's rows `DSGN_RBNDV2-W10-S1` and `W10-S2`: `IndexPerformanceModal.tsx`
(lines 456, 460, 461, 472, 473, 479) and `RSIModal.tsx` (lines 229, 334, 351, 370, 375, 376) hold the same literal white chart props the CTO named in the other two modals. They are on the round-2 adoption list (`RV-m-4`), so a modal whose axes
cannot be read is the same defect (C-MODAL, FWD-3). Gate limb: none graded the amendment.

| cell | what it builds | serves | writes | reads (never writes) | risk |
|---|---|---|---|---|---|
| `RV-c-2` | DIRECT-ACT: the literal white chart props of `IndexPerformanceModal.tsx` and `RSIModal.tsx` read the same tokens as `RV-c-1`: grid stroke `var(--rb-rule)`, axis stroke `var(--rb-quiet)`, tick fill `var(--rb-ink-3)`; any other white-alpha chart literal maps by alpha (at or below 0.15 to rule, 0.4 to quiet, 0.5 or more to ink-3) and is named | FWD-3, FWD-5 | `src/components/market-performance/IndexPerformanceModal.tsx`, `src/components/market-performance/RSIModal.tsx`, `src/components/market-performance/__tests__/dsgn-rbndv2/` | `src/components/market-performance/FearGreedModal.tsx` | LOCAL |

