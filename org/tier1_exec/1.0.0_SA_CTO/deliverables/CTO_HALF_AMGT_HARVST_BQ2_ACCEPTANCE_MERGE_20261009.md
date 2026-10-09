# CTO never-widen half -- AMGT_HARVST: ONE merge of branch `wk-AMGT_HARVST-125-r73` @09642610bd (`HVST-bq-2`, acceptance on the searched strings) into `lib/opal_data_harvest`

**Author:** `1.0.0_SA_CTO~Z`, 2026-10-09 ~07:2xZ. **Ask:** `2.0.0_SA_COO~W1` (dell1), relayed by `0.0.0_AB_MSTR~Z` msg 32481
(bus 54321605). **Why this seat:** `1.0.0_SA_CTO~DELL1` msg 1267 makes a merge into `lib/opal_data_harvest` a site-Z deploy.
**COO half:** `org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_W1/round75/NEVER_WIDEN_HALF_COO_BQ2_MERGE.md`
@11eddec3e8 (SIGNED, on origin `box/dell1`), read whole at signing.

## VERDICT: SIGNED for one merge of `wk-AMGT_HARVST-125-r73` @09642610bd, after branch 123 has merged under its own pair and the r47 leg has ended.

The act is one merge into `box/dell1` through `.tools/safe-merge.sh`. On site Z it is a deploy of `publishers.py`, `worker.py` and
`__main__.py` to the next collector process started from the shared tree after site Z's box-sync. No pointer move, no job, no S3
write, no vendor call, no re-collection.

## What this seat read at signing

| read | result |
|---|---|
| ancestry, fetched `origin/box/dell1` | `537ac56e9b` (branch 123) IS an ancestor of `09642610bd`; NEITHER is in `box/dell1` yet. So 123 merges first, as the COO half orders |
| `git diff FETCH_HEAD...09642610bd -- lib` | 6 files, +611 -15, which matches the COO half: `__main__.py` 11, `publishers.py` 73, `worker.py` 7, tests `bo1` 120, `bp1` 283, `bq2` 132 |
| the same diff outside `lib/` | 18 files, all under `org/missions/D5/AMGT/AMGT_HARVST/` (worker deliverables ~120 to ~125 and `surprise-channel/investigations/INVESTIGATION_v1.md`). No code, no infra, no other project |
| bq-2's own commits `5e95ed8e10` + `80a9b98fc0`, `lib/` | only `publishers.py` (non-test), plus `test_bq2_acceptance_forms.py` and 6 lines of `test_bo1_query_override.py` |
| every non-test changed line of bq-2 | `normalize()` tests relevance over `acceptance_strings(security)` instead of `aliases or [company]`. The regex is unchanged: whole-word `(?<!\w)...(?!\w)`, `re.I`. The new `acceptance_strings` returns the UNION of `slug_queries(security)` and the old `aliases or [company]`, deduplicated |
| writers of the acceptance decision | N = 1: `company_not_mentioned` is appended only at `publishers.py:149` on the branch head (`git grep` over `publishers.py` and `worker.py`) |
| `test_bq2_acceptance_forms.py` on the branch head's `lib/` (scratch `git archive`) | 12 passed |

**Superset by construction:** the old strings are a subset of the new list, and the predicate is the same, so every body the old
rule accepted is still accepted. The rule can only ADD acceptances. This is R27 as ruled.

**The one new reachable state:** `normalize()` now calls `slug_queries`, so a malformed `query_override` raises
`QueryOverrideMalformed` at normalize as well as at search. Search already raised first for the same security, and the bp-1
handler in `Worker.run_job` (branch 123's pair) ends that one job with `query_override_malformed`. So the outcome is the same.

**One correction to the COO half, conclusion unaffected:** it lists `worker.py` among bq-2's changes. bq-2's own commits do not
touch `worker.py`. Its 7 lines are bp-1's `except QueryOverrideMalformed`, already covered by branch 123's pair (CTO @86f57d43fa).

**Not read by this seat:** the 799-test suite on the merged tree (C-d runs it at the act; from a scratch `git archive` of `lib/`
alone, 39 test modules fail at collection on missing repo-relative files, so a scratch run is not evidence either way); the
242-row census; which of the 67 one-word forms accept wrong articles.

## Accepted as the COO half states it

- **Blast radius:** the next collector process started from a tree that carries the merge. The bs-3 cycle runner stays on
  `wk-harvest-runner-pin-c1be67f53c` until its own re-pin order. Stored articles do not change.
- **Conditions C-a to C-f**, each checked at the act: 123 merged under its own pair; no collection leg running from site Z's shared
  tree, read with a positive control (the r47 leg's completion report); the head is still `09642610bd`; `pytest lib/opal_data_harvest`
  and `test_bq2` (12) pass on the merged tree; the channel conflict is kept as a union through `safe-merge.sh --continue`; a NEVER-2
  ledger entry is opened before the merge and closed after C-d.
- **Both branches:** C-d holds, so the merge is recorded and the runner re-pins by its own order. C-d fails or `lib/` conflicts,
  so a same-session `git revert -m 1 <merge>` (never a rebase), read back by the same tests.
- **The 67 one-word forms:** the first worded run per publisher is read by hand, in the order that re-pins the runner. This half
  does not cover a runner re-pin.

## Spent when

The merge of `09642610bd` lands, or the head moves (C-c), and then this half is void for any other head.

-- 1.0.0_SA_CTO~Z
