# /canonical-drive AMGT_CORPUS -- 2.0.0_SA_COO~X -- 2026-09-30 17Z (host opal_bloomberg)

| time | limb | round | act |
|---|---|---|---|
| 17:0xZ | L8 | 25 | aa-2 leg c: TSM's newest block reads `CUR_MKT_CAP` USD (quote); RESAPP `2.0.0_SA_COO~Z` told FWD-30 is unblocked |
| 17:01Z | L8 | 25 | aa-2 leg d started (`d25.py write`, a named script, `-u`) |
| 17:04Z | L8 | 25 | leg v served read: `/thesis` TSM `CUR_MKT_CAP` USD, `NET_DEBT` no currency; BA unchanged (the negative arm); census 49 -> 11 |
| 17:0xZ | L8 | 25 | aa-4's trigger read: ac-3 AC1 40/40 by this seat's own run; the BP/NG raw is trusted |
| 17:1xZ-17:25Z | L8 | 25 | aa-4 serializing dry run (`aa4_dryrun.py`), as below; COO half `dc5cd3a3c3` |
| 17:36Z | L8 | 25 | aa-4 CTO half `c3889f8a9b` SIGNED: items 1-3 accepted; the 18 sign changes are corrections |
| 17:47Z | L10 | 25 | Andrew: "Go with sequence" (the `/next-calls` options 1-3) |

**aa-2 to the start of leg d:** CTO half `21f7a96cf6` (4 conditions); ledger `3d5235be21`; leg a 6/6 fields; leg b map `d66497aec3`;
leg c 22/22 blocks matching (units 38, signs 38, header labels 53, all header scope).

**aa-4's dry run:** 1 captured write per name; BP 211 units (10 `PROF_MARGIN` -> UNRESOLVED), NG 174; BP's case ABSENT carrying a
778.57 input; NG's case ABSENT -> SERVED 1,298.21.

## Compiler Tools

- `c25_verify.py`, `d25.py`, `aa4_dryrun.py` and `capture_lib._invoke`.
- Gaps: the rail flagged a `find(` inside a heredoc.
