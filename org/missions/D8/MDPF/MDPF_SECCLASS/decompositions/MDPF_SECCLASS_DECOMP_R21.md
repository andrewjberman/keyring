# MDPF_SECCLASS decomposition -- ROUND 21 (2.0.0_SA_COO~M1, dell1, 2026-10-12 ~09:3xZ)

**Status: DECOMPOSED.** The issuer is this seat. One issuance covers five cells.

**Cut on:** the CTO round-20 analysis, section 3, the enrichment list
(`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_MDPF_SECCLASS_ROUND_20_20261012.md` @e5adc667e2, 1.0.0_SA_CTO~DELL1 msg 4321).
- **Item 1 is cell `SC-e-91`** (row D1-S30, the retained-unclassified revisit; build, SERVED, its own never-widen pair).
- **Item 2 is cell `SC-e-92`** (row D1-S28, the cross-box deploy check's trunk-first sentinel status; build, LOCAL).
- **Item 3 is cell `SC-e-93`** (row D1-W77-S1, the NAN / NONE ticker count; read).
- **Item 4 is cell `SC-e-94`** (row D1-W78-S1, the writer of the 2026-10-06/07 partition rewrite; read).
- **Item 5 is cell `SC-e-90`** (the portal class-readers test located by content; drafted at round 20, cut now on the CTO's word).
- **Item 6 is carried, not cut:** leg G of SC-e-87 and D1-S30, read on the first post-ship as_of (Tuesday 2026-10-13's fire or later).
- Carried, not cut: e57e61 (FWD-10 apply) stays HELD on its trigger.

**State the round starts from (measured 2026-10-12 ~04:4xZ-09:3xZ, box/dell1):**
1. **C_06 never revisits a retained date's `unclassified` holdings.** `SERVED_HOLDING_CLASSES` (:274-275) contains `unclassified`, so
   `reclassify_retained` (:278-311) leaves them. `build()` returns early when no partition is newer than the watermark (:694-696), so the retained
   pass does not run on a fire that builds no new date. Where it does run, `existing['firm'].update(firm_daily_new)` (:975) replaces only the NEW
   dates in `mix_daily_summary.json`, so a retained date's firm and advisor dollars by class are never adjusted. D_04 (:486) reads that snapshot:
   its served Unclassified is $1,846,332.73 at as_of 2026-10-09 before the SC-e-87 ship and after it (row D1-S30).
2. **`.tools/crossbox-deploy-check.py` `measure_open_deploy` (:326-405)** reads each registered worktree's HEAD. A slug the trunk deleted
   (ledger closed) still reads HELD in a lagging worktree and counts as live; a registered worktree whose directory is gone reads
   `ls-tree rc=128 (not readable, not clear)` unless it also left the worktree list during the read (row D1-S28).
3. **Two served-data questions are open:** whether any served BD position carries the literal ticker `NAN` or `NONE` (the lib normalises
   it to no ticker; row D1-W77-S1), and what rewrote the 2026-10-06/07 holdings partitions at 2026-10-10T23:15Z (row D1-W78-S1).
4. **A portal test is red at origin/DEV `cdd87181d5`** (`iv-e-46.class-readers.test.ts`: its `NAMED` entries cite file:line, two lines moved).

## Rule 24 record

- **Domain:** the CTO's five items; nothing else is a cell.
- **(ii) Same grain:** one cell per item. SC-e-91 is the one served-data build; SC-e-92 a tool build; SC-e-93 and SC-e-94 reads; SC-e-90 a
  test-file repair.
- **(iii) Intent coherence:** SC-e-91's acceptance drives the module's OWN `reclassify_retained` and reads the AST of `build()`, because the
  last round's function-level acceptance passed while the served bytes did not move (row D1-S26 -> D1-S30).
- **(iv) State coherence:** SC-e-91 moves no served key by itself; the ship is a separate pair-gated act. SC-e-92 touches one tool file and no
  served key. SC-e-93 and SC-e-94 write one record each and read only. SC-e-90 touches one test file and no product file.

## The cells

| cell | what | serves | risk | depends on |
|---|---|---|---|---|
| `SC-e-91` | C_06's retained pass revisits a retained date's `unclassified` holdings on every fire, including a fire with no new partition; the retained dates' firm and advisor dollars by class move with them; unchanged relationships are not rewritten. Plus the ship's never-widen half request, both halves left unsigned. | FWD-1 (BD half) | SERVED | none (the ship is a later pair-gated act) |
| `SC-e-92` | `.tools/crossbox-deploy-check.py`: a slug the trunk deleted does not count when only a lagging worktree still carries it; a registered worktree whose directory is gone is VANISHED, not a hit; a sentinel that exists only on a worker's branch and a live sentinel at trunk still hit. | seat-gates (row D1-S28) | LOCAL | none |
| `SC-e-93` | A read: count the served BD positions, and their dollars, whose ticker is the literal `NAN` or `NONE` at the latest partition C_06 reads, with the denominator printed. | FWD-1 (the residual leg G is stated net of) | LOCAL | none |
| `SC-e-94` | A read: name the writer that rewrote the 2026-10-06 and 2026-10-07 holdings partitions at 2026-10-10T23:15Z, count the writers of the prefix in that window, and state whether the next C_06 fire re-serves those dates. | FWD-1 (the dates leg G's comparator rests on) | LOCAL | none |
| `SC-e-90` | The class-readers portal test locates each `NAMED` reader by content, not by line number, passes at origin/DEV, and a negative arm proves a missing word still fails. The test file only. | FWD-16 | LOCAL | none |

## Write sets (disjoint)

- **SC-e-91:** `data/black_diamond/scripts/gold/C_06.client_mix_timeseries.py`, new
  `data/black_diamond/scripts/gold/tests/test_c06_retained_unclassified_r21.py`, and the half request
  `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_C06_RETAINED_UNCLASSIFIED_20261012.md`.
- **SC-e-92:** `.tools/crossbox-deploy-check.py` only.
- **SC-e-93:** `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NAN_NONE_TICKER_COUNT_20261012.json` and its scratch script under `.scratch/`.
- **SC-e-94:** `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/W78_PARTITION_REWRITE_WRITER_20261012.json` and its scratch script under `.scratch/`.
- **SC-e-90:** `portal/src/pages/AdvisorIntelligence/__tests__/iv-e-46.class-readers.test.ts` only.
- Each may also append to `org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md`.

## Chains

Five cells, no edge between them: five chains. Fan-out 5 of 5, cap 8. Slots ~80 (SC-e-91, `worker`), ~81 (SC-e-92, `worker`), ~82 (SC-e-93,
`worker-light`), ~83 (SC-e-94, `worker-light`), ~84 (SC-e-90, `worker-light`, portal worktree, direct act).
The leg G read (carried item 6) is not a cell: it is the issuer's read after SC-e-91 ships and C_06 builds a date past 2026-10-09, and its
expected figure is stated at THAT as-of, never at 2026-10-08. SC-e-94's answer decides whether the 2026-10-06/07 dates are a comparator.
