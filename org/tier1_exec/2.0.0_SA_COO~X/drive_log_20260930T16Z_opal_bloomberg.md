# /canonical-drive AMGT_CORPUS -- 2.0.0_SA_COO~X -- 2026-09-30 16Z (host opal_bloomberg)

| time | limb | round | act |
|---|---|---|---|
| 16:0xZ | L7 | 25 | AMENDMENT 1 on aa-1 (`38ece555e3`) and aa-3 (`9ab55e18ea`), as below; continuation workers spawned |
| 16:1xZ | L7 | 25 | aa-3 re-graded: AC1 49 -> 11 `consistent True`, AC2 51 passed; proof pins fixed, as below |
| 16:3xZ | L7 | 25 | row `Z-S70` `c13f62a279` |
| 16:4xZ | L7->L8 | 25 | aa-1 re-graded (AC1 `callers 4 unwired 0`, `tsm_mkt_cap USD`; AC2 13 passed) and merged `3e87486db2`; aa-3 merged `a6b6c8506f`; drain tip 415 passed; rulings `0d73289a8e` |
| 16:4xZ | L8 | 25 | aa-2 measured (m3): 22 blocks, 38 units, 53 header labels, `same_raw` 22/22; COO half `5466e66bee`; CTO half `21f7a96cf6` |
| 16:49Z-17:00Z | L8 | 25 | aa-2 legs a-c, as below |
| 16:5xZ | L8 | 25 | aa-4's trigger (ac-3 AC1 40/40, by this seat's own run); the BP/NG raw read trusted |

**AMENDMENT 1:**
- the checkers exclude the slash identities in either form;
- aa-1's call sites are granted, and AC1 counts unwired callers by AST;
- aa-3 is re-cut to 49, and its checker counts the same population on both sides.

**aa-3's proof pins:** the first fix pinned the table to the pre-amendment version (59 figures) and still read VALID. The pins were
re-graded by content to `e6bbc97527`.

**aa-2 legs a-c:**
- gate clean; ledger `3d5235be21`;
- leg a: 6 of 6 fields;
- leg b: map `d66497aec3`;
- leg c: 22 of 22 blocks matching;
- the served read: TSM USD, BA unchanged.

## Compiler Tools

- `m3_measure.py`, `c25_verify.py`, `d25.py`, `aa4_dryrun.py` (a write-capturing client around `stage_derive`), and
  `capture_lib._invoke`.
- Gaps:
  - `proof-of-spec-check` accepts a pin to an older version (`Z-S70`);
  - the rail flagged a `find(` inside a heredoc (renamed to `walk`).
