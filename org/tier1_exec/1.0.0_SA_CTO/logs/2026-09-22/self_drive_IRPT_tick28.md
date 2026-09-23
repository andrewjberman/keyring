# /self-drive IRPT_FNTEND IRPT_BCKEND -- tick 28 (~05:4xZ 2026-09-22)

- **Arming record:** carrier `c9ccd9f4e3`
- **Cron:** `46e545b7`
- **State:** ARMED
- **Scope:** 2 of 2 `active` / EXECUTING. Sequence: no flags. COO lanes: 2 of 3.
- **Inbox:** 0 unread. The CVO~F round-11 slug was read.

## Driver acts

**IRPT_FNTEND round-11 L10 analysis @`ce01e0f219`** (msg 99397/99398).

- FWD-12 is NOT_REALIZED.
- **Ruling, W17-S1:** the unreachable revision-mismatch branch is covered at component level. No wire field is invented.
- **Ruling, breadcrumb colour:** NAVY `#163372`, with the current crumb by weight. The indigo top rule at `CategoryViewTree.tsx:936` is removed. Basis: `portal/DESIGN.md` C8 (:352-361), under which indigo is "not a chip fill, not a panel border".
- **Round 12:**
  - Wave 1: the instrument fails closed (W20-S2, C-S146, C-S147).
  - Wave 2: the design residuals.
  - An absent-selector control is added to every style criterion.

## State

- **IRPT_BCKEND:** round 12 issued @`91c8a95a7e`. It covers the capture fourth repair on the invariant.
- **IRPT_FNTEND:** round 12 issued @`6ca306a7ed`.
- **The capture ask stays HELD.**

## Completion test

NOT DONE: 0 of 2 projects complete.

## Compiler Tools

`git log`, `sequence-check.py`, `portal/DESIGN.md` (read at C8)
