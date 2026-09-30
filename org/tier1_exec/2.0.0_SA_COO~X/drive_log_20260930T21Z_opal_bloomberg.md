# /canonical-drive AMGT_CORPUS -- 2.0.0_SA_COO~X -- 2026-09-30 21Z (host opal_bloomberg)

| time | limb | round | act |
|---|---|---|---|
| 21:xxZ | L7 | 26 | workers report in turn: ab-1, ab-3, ab-5, ab-2 |
| 21:xxZ-22:2xZ | L7->L8 | 26 | each tip re-graded, as below |
| 22:2xZ | L7->L8 | 26 | merges: ab-1 `78842bba5e`, ab-3 `c50db70fb0` (after waiting out a peer's staged index), ab-5 `9753b57672`, ab-2 `6cfc6bab90` (a structural channel resolve to 136 rows) |
| 22:2xZ | L8 | 26 | drain hygiene, as below; rulings `f2f77b132a` (S18 binds ab-4; S19 accepted; W5-S7 carried) |
| 22:2xZ | L8 | 26 | the ab-4 serializing dry run over every key started (`m4_dryrun.py`) |

**The re-grades:** AC1 and AC2 by this seat's own runs; the diff paths inside each grant; the proof VALID with the order's arguments;
**every artifact pin read by CONTENT** (`git show <pin>:<path>` equal to HEAD).

**Drain hygiene:** 902 + 313 passed. The 2 failures are pre-existing at the round-26 base `f40d29ede1` (read by a detached base
worktree).

## Compiler Tools

- `regrade.sh` (pins by content) and `merge_worker.sh` (channel conflicts resolved structurally, anything else STOPS).
- Gaps:
  - the first `regrade.sh` globbed every old proof instance in a slot folder (fixed: the instance is named from the order);
  - ab-3's sparse worktree could not run the api suite whole (terraform and registry files are outside the cone), so it was run on
    the full tree.
