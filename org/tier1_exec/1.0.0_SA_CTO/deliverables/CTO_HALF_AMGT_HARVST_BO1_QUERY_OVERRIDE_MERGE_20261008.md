# CTO never-widen half -- AMGT_HARVST HVST-bo-1: the MERGE of a stored per-security query override into `lib/opal_data_harvest`

**Author:** `1.0.0_SA_CTO~Z`, 2026-10-08 ~10:5xZ. **Ask:** `2.0.0_SA_COO~H` msg 31678.
**COO half:** `org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round70/NEVER_WIDEN_HALF_COO_BO1_QUERY_OVERRIDE_MERGE.md`
@6b9d3118c6 (SIGNED), read whole.

**SPENT WITHOUT AN ACT (2026-10-08 ~12:1xZ):** superseded by `CTO_HALF_AMGT_HARVST_QUERY_OVERRIDE_BRANCH_MERGE_20261008.md`,
which signs the one branch holding bo-1 and bp-1 at 537ac56e9b. Nothing was merged under this half.

## VERDICT (spent): SIGNED for one merge of branch `wk-AMGT_HARVST-122-r70` @419dc9b1fc, not before the Seeking Alpha leg has ended. Two conditions beyond the COO half's three.

The act is a merge. On this box it is a deploy of `publishers.py` and `__main__.py` to the next collector process started from
the shared tree. No pointer move, no job, no S3 write, no vendor call.

## What this seat read at signing

| read | result |
|---|---|
| the branch head | `419dc9b1fc` |
| `git diff c92e860791 419dc9b1fc -- lib/` | 3 files, +149 -5: `publishers.py` +25, `__main__.py` +11 -4, one new test file |
| the changed code, every non-context line | `slug_queries` returns the override ONLY under `if "query_override" in security`; `universe()` copies the field ONLY under `if "query_override" in rec`. With no such key both functions run their old lines. `_LEGAL_SUFFIX` and `slug_query` are not in the diff |
| callers of `slug_queries` in the package on the branch | 1, `publishers.py:754`, inside the sitemap discovery. The COO half's N = 1 holds |

Not read by this seat: the 242-row table, the 15 tests, the suite's 778, the identity files.

## Accepted as the COO half states it

On the round-47 file the config points at, CHANGED 0 of 234. On the new unpointed file, CHANGED 1 (AIG_US_Equity) and IDENTICAL
241. The override is inert until the pointer moves, and the pointer waits on Andrew's word (R22). C-a (no leg running, read at
the act with a positive control), C-b (the table re-read on the merged tree) and C-c (a ledger entry) stand as written.

## C1 -- the half's own text and the code disagree on the field's shape; settle it before the merge

The COO half's table reads the field as `["American International Group"]`, a list. The code accepts only an object
`{value, reason, source}` and raises on a list. One of the two is mis-stated. Print AIG's record from the new identity file
beside the validator's verdict on it; the half is corrected to what the file holds.

## C2 -- three things closed before the pointer ever moves, not before this merge

- **A malformed override raises `ValueError`.** Show what that stops: the one job for that security, or the whole run. A stored
  typo in one record must not end a 242-name run. If it ends the run, that is repaired first.
- **Row Z-W122-S1:** the stored provenance label reads the derived string while the search used the override. A record that says
  it searched for one thing and searched for another is repaired first.
- **The new query matches 0 of 20,500 held titles**, so that it finds AIG at a publisher is not shown. It is shown by the first
  run Andrew words, and that run's AIG result is read by hand before any other override is added.

## BOTH BRANCHES

As the COO half: C-b reads 0 of 234 and the order closes; anything else, or a failing suite on the merged tree, is a revert
commit the same session. A leg found running at the act: nothing is merged.

-- 1.0.0_SA_CTO~Z
