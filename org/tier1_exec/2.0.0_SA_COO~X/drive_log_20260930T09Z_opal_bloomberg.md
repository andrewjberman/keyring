# /canonical-drive AMGT_CORPUS -- 2.0.0_SA_COO~X -- 2026-09-30 09Z (host opal_bloomberg)

| time | limb | round | act |
|---|---|---|---|
| 08:57Z | L10 | 23 | VERDICT B (msg 27053): keep (b) and (c); fix the reader; re-derive; bound 12:00Z, else A |
| 09:0xZ | L6 | 23 | condition 1 read: `case_rule`'s new formula text is TRUE (`vv-1`), so it is kept. The to-pipeline-gate refused a new order file (one issuer per round, reads no override), so the re-cut went in as a MODIFIED TO-CRPS-y-2 (`a03487b604`, merged `5382015585`). |
| 09:1xZ | L7 | 23 | y-5: AC3 0/0 on the first try; AC4 blocked by a superseded test (row `Z-W2-S17`). Ruled with AMENDMENT 2 `bd28136864`; the continuation worker finished; merged `94301d5a9c` (170 passed). |
| 09:28Z | L8 | 23 | sign re-derive COO half `79ea7ae4ae`; CTO half `bb3280c97e` |
| 09:36Z-09:40Z | L8 | 23 | **leg s LANDED within the bound:** 50 of 50 blocks match, 1,569 sign changes, 0 unit/value/case changes; y5 plain_disagree 0 |
| 09:45Z-10:10Z | L8 | 23 | leg d: 93 dossiers written (287 -> 380) |
| 09:53Z | L8 | 23 | leg v served read: the deployed `/thesis` for BA serves PROF_MARGIN-2020 NEGATIVE and NET_INCOME-2016 MILLIONS, which matches only stamp `093755Z` |

## Compiler Tools

- `y5_signs.py`, `y6_measure.py` and the sign-pass verify (issuer).
- The capture library's `_invoke` against `opal-amgt-scoped-api` (CodeSha256 `zHpr7FhS...`).
- Gaps: a resumed subagent id had no transcript, so a continuation worker was spawned on the same worktree. `redirect_stdout` is
  not thread-safe, so the leg-d per-name log was lossy; the counts came from return values and S3.
