# Round-15 L9, the R4 ruling, and ADJUDICATION_v14 -- `3.0.0_SA_CVO~Z`

**Date:** 2026-09-21
**Task Order:** ad-hoc (AMGT_RESAPP L9; R4 routed by `1.0.0_SA_CTO~Z` msg 23922)
**Status:** COMPLETE for this seat's scope; project still held on three Andrew words

---

## Objective

Grade round 15 at L9; answer R4 (grade vs terminality), a governance fork routed here; disposition the surprise
items the COO's round-16 census handed back, which turned out to be all 62 open items for rounds 14-15.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| `surprise-row-gate.py` `_latest_dispositions` / `_resolve_latest` / `_graduated_without_row` | called directly, then simulated over the new file before commit | PASS | the census of record; the simulation matched the committed index exactly (3 open, 23 owed) |
| `surprise-row-gate.py --acceptance --round N` | rounds 13, 14 | PASS | exposed S176 live (160/30 vs 165/31) |
| `surprise-row-gate.py <file>` (staged) | on ADJUDICATION_v14 | correct REFUSAL | 4 ARMED rows without `disarm_owner`; fixed and recommitted |
| `comp-tool-hud.sh` rail | tripped twice on raw grep over a directory | WARN, correct | routed to native Grep |

**What worked:** simulating the resolver over the new document before commit; the three parallel read-only evidence
forks (8/7/4 rows).
**What failed:** nothing in the tools; my own round-14 L9 is the defect this block repairs.
**Gap found:** the sweep's unanchored parser (S176), now a round-17 cell.

---

## Work Completed

1. **Round-15 L9** @`3bb2627c03`: 3 of 3 terminal; two cells re-verified on a fourth instrument (pytest re-run 24/0;
   the arity fix read at source). Ratified by `1.0.0_SA_CTO~Z` (@`a73b85c64f`).
2. **R4 ruling** @`335faf48fe`: terminality and acceptance are two axes; a FAIL on a terminal order is admissible at
   L10 only as an L9-classed CRITERION defect with the act shown correct on another instrument; never flipped. Round
   13's three stand. Flagged S176 live before round 16 issued. The CTO took it as a cell, then moved it to round 17
   because round 16 had already issued.
3. **ADJUDICATION_v14** @`913a02de36`: 62 -> 3 open (held: W37-S1, W49-S2, W49-S4), 23 rows C-S322..C-S344.
   rk-43 AC5 graded NOT_EVALUATED (headed-session instrument). rk-44 AC3 classed a criterion defect under R4 via the
   live task store plus a positive-control task (0x0 today); the "quoted is normal" claim rejected on a 5-of-18
   control population. Eleven self-graduated COO disarm records superseded. 23 remediation rows owed at L10, named.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Disposition all 62, not the census's 11 | The L10 precondition counts every open item; 11 would have left 51 blocking |
| rk-43 AC5 NOT_EVALUATED, not graded from payloads | The criterion names a headed human session; C-S273 precedent forbids converting payloads into a render verdict |
| Anchor-and-dismiss classes (C-S335/336, C-S337/338) | Round-13 pattern; keeps remediation debt to one row per remedy, not per instance |
| Send S176 before the rest | Andrew's 15:12Z word fixes a round's cell set at issuance; timing mattered |

---

## Self-corrections on the record

- My round-14 L9 filed no channel rows; found by the COO's subtraction.
- It named rk-61 AC2 as the declared judgment criterion; rk-43 AC5 is. The CTO ratified the mislabel.
- It called W60-S3 unrepaired two days after `3795d4f487` fixed it.
- Drafted W47-S2 as "comment stale"; HEAD `dfc382cb7a` had fixed it (S190). Caught before commit.

## Open Items / Follow-ups

- 23 REMEDIATION rows owed at the true L10 close (GATE (iii) refuses them while 5 orders are open).
- Round 16 (4 cells) at L9 when it drains; round 17 (S176-anchor) after.
- W38-S5, W37-S2, W40-S1 handed to the CTO's next analysis.
