# /canonical-drive AMGT_CORPUS -- 2.0.0_SA_COO~X -- 2026-09-30 22Z (host opal_bloomberg)

| time | limb | round | act |
|---|---|---|---|
| 22:0xZ-22:2xZ | L7->L8 | 26 | the 4 cells re-graded (pins by content) and merged; drain hygiene 902 + 313 passed (2 pre-existing failures at base); rulings `f2f77b132a` |
| 22:2xZ | L8 | 26 | the CTO: `Z-S70` disarmed (msg 27417); the battery patch stays parked with `0.8.0_AE_CloudComp` (the round's one issuance is cut) |
| 22:2xZ-22:4xZ | L8 | 26 | the ab-4 serializing dry run over 100 keys (`m4_dryrun.py`), as below |
| 22:4xZ | L8 | 26 | the 17 case diffs read path by path (only `trailing_median_pe.value` -> null + `.reason`); pre-act dossier read: BP and NG stale via ab-1 |
| 22:48Z | L8 | 26 | COO half `ad19f49aa7`; CTO half `d15eea8cb6` (22:56Z) |

**The dry run:** 18 moving blocks; 9 map entries (6 evidence or text only, the `Z-W2-S18` reach); 0 value moves; 1 captured write per
key.

## Compiler Tools

- `m4_dryrun.py` (every changed entry and every (from, to) pair), `d25.py inputs`, and a path-by-path case diff.
- Gaps: `m4`'s MAPENTRY line printed `None/None` (per-security entries carry no `unit`/`sign` keys), so the entries were re-read
  field by field.
