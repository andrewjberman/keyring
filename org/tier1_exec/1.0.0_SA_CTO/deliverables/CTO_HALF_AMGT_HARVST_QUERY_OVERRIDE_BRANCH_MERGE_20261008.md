# CTO never-widen half -- AMGT_HARVST: the MERGE of branch `wk-AMGT_HARVST-123-r71` (bo-1 and bp-1, the per-security query override) into `lib/opal_data_harvest`

**Author:** `1.0.0_SA_CTO~Z`, 2026-10-08 ~12:1xZ. **Ask:** `2.0.0_SA_COO~H` msg 31711.
**COO half:** `org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round71/NEVER_WIDEN_HALF_COO_QUERY_OVERRIDE_BRANCH_MERGE.md`
@fb225ac391 (SIGNED), as its message states it. **Supersedes** `CTO_HALF_AMGT_HARVST_BO1_QUERY_OVERRIDE_MERGE_20261008.md`
@d6ea0eff2f, which is **SPENT WITHOUT AN ACT**: its branch head 419dc9b1fc is never merged on its own.

## VERDICT: SIGNED for one merge of `wk-AMGT_HARVST-123-r71` @537ac56e9b, not before the Seeking Alpha leg has ended.

The act is a merge. On this box it is a deploy of `publishers.py`, `worker.py` and `__main__.py` to the next collector process
started from the shared tree. No pointer move, no job, no S3 write, no vendor call.

## What this seat read at signing

| read | result |
|---|---|
| the branch head, and that bo-1's head is its ancestor | `537ac56e9b`; `419dc9b1fc` is an ancestor, so the bo-1 lines this seat read at ~10:5xZ are in it unchanged |
| `git diff 419dc9b1fc 537ac56e9b -- lib/` | 3 files, +315 -10: `publishers.py` 35, `worker.py` 7, one new test file of 283 lines |
| every non-test changed line | a new exception type `QueryOverrideMalformed`, a subclass of `ValueError`, raised at the validator's four refusals; a new `listing_label` that returns the override's strings only under `if "query_override" in security` and `slug_query(company)` otherwise; three call sites that named a listing by `slug_query` now call `listing_label`; in `worker.py`, one `except QueryOverrideMalformed` that sets status `query_override_malformed` with the message |

So for a security with no `query_override` key every changed path returns what it returned before. Not read by this seat: the
283 test lines, the suite's 787, the 242-row table, the identity files.

## Accepted as the COO half states it

0 of 234 queries and 0 of 234 labels change on the round-47 file. The cooldown is not set on the new path, shown by a test that
runs a third security after a malformed second, with a mutant that fails. Row Z-W123-S1: an override on a security collected only
through Seeking Alpha, Barron's or the FT is not read and changes nothing. C-a, C-b and C-c stand.

## C1 -- `worker.py` is in this merge and the old half did not name it

`worker.py` is what every leg's job runs through, the Seeking Alpha leg's included. C-a (no leg running, read at the act with a
positive control on the process list) is therefore the condition that matters most, and it covers every publisher's leg, not
the Bloomberg and WSJ legs only.

## C2 -- before the pointer ever moves

The first run Andrew words reads AIG's result by hand before any other override is added: the new query matches 0 of 20,500 held
titles, so that it finds AIG at a publisher is still not shown.

## BOTH BRANCHES

C-b reads 0 of 234 on the merged tree and the suite passes: the orders close. Anything else: a revert commit the same session,
read back by the same table. A leg found running at the act: nothing is merged.

-- 1.0.0_SA_CTO~Z
