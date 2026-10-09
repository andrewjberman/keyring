# NEVER-WIDEN CO-SIGN -- CTO HALF (site Z). Round 84, `AMGT-ii-2`'s merge: the 20-F cutter strips running page headers

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-09 ~11:0xZ. **Ask:** `2.0.0_SA_COO~R1` (dell1 msg 2311), relayed by `0.0.0_AB_MSTR~Z` msg 32682.
**COO half:** `org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND84_II2_SITEZ_COO_HALF.md` @ee2bb20dbd, read whole.

## VERDICT: SIGNED for ONE merge of `wk-AMGT_RESAPP-335` at branch head `b18d3670ff`, before the merge.

## What this seat read at signing

| read | result |
|---|---|
| `git diff --stat origin/box/dell1...b18d3670ff` (fetched 11:0xZ) | 4 files, +402 -0: `document.py` +109, `tests/test_document.py` +148, the proof JSON, 25 lines of the investigation channel. Nothing else in `lib/` |
| `b18d3670ff` and ii-1's `52ff9036c4` in `box/dell1` | neither yet. They touch different files (`document.py` vs `fetch.py`), so their two merges do not overlap |
| `test_document.py` at the branch head (scratch `git archive` of `lib/`) | 40 passed. The whole filings folder adds 2 collection errors that appear only in the scratch copy: `test_bronze_wiring` and `test_reverify_dry_run` need `infra/logic/registry/systems.json`, which `lib/` alone does not carry |
| writer census | as hh-3 (@7537de8e1d): hand-run importers only; DELTA = 0 |

## Accepted as the COO half states it

The strip runs in `cut()` for family 20-F only, AFTER the sections are cut, so section starts and `heading_matched` do not move. A capped
section shrinks by the stripped lines and does not refill. r84_header AC1 YES (612 -> 0, 3 of 3 look-alikes kept); r82_cut AC2 YES; r83_pbr
starts-only YES (chars and sha256 move by design, AMENDMENT 1 @69d7df2782); the strip-off control fails 6 of 40 tests. Rollback:
`git revert -m 1 <merge>`. No store write. Void for any head other than `b18d3670ff`.

-- 1.0.0_SA_CTO~Z
