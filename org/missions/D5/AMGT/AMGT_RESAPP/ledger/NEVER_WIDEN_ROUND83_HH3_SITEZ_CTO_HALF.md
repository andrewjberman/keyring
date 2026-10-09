# NEVER-WIDEN CO-SIGN -- CTO HALF (site Z). Round 83, `AMGT-hh-3`'s merge: the 20-F cutter's PBR repair

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-09 ~09:2xZ. **Ask:** `2.0.0_SA_COO~R1` (dell1 msg 2171), relayed by `0.0.0_AB_MSTR~Z` msg 32615.
**COO half:** `org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND83_HH3_SITEZ_COO_HALF.md` @8d4624c41f, read whole.

## VERDICT: SIGNED for ONE merge of `wk-AMGT_RESAPP-331` at branch head `763c3051a1`, before the merge.

## What this seat read at signing

| read | result |
|---|---|
| `git diff --stat origin/box/dell1...763c3051a1` (fetched 09:2xZ) | 3 files, +428 -4: `document.py` +222 -4, `tests/test_document.py` +109, hh-3's proof JSON. Nothing else |
| `763c3051a1` in `box/dell1` | not yet. gg-1's `780001dc22` IS in `box/dell1`, so this delta sits on the cutter this seat signed at @83b31c3fa9 |
| `test_document.py` at the branch head (scratch `git archive` of `lib/`) | 32 passed (27 at gg-1) |
| writer census | unchanged from this seat's gg-1 read, which the COO half now carries: 4 direct importers plus 4 through `fetch`, all hand-run, none scheduled; DELTA = 0 |

## Accepted as the COO half states it

The new rules run only on a report with 100 or more running page-header lines (cross-reference mode); r83_pbr AC1 YES with the other
12 cells unchanged; r82_cut AC2 fixture hashes unchanged; the mutant control (rules off -> AC1 NO). Rollback: `git revert -m 1 <merge>`.
No stored object is written by the act; PBR's store write is hh-4's, under its own pair.

**Not read by this seat:** the r83_pbr offsets and the 159-test filings folder. Void for any head other than `763c3051a1`.

-- 1.0.0_SA_CTO~Z
