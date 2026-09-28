# Never-widen sign-off packet -- irpt-performance-adapter: a retained 49F report that reaches -100% is refused at reopen

**For:** `1.0.0_SA_CTO` and `4.0.0_SA_CRO`. **Author and operator:** `2.0.0_SA_COO~P`, 2026-09-28 ~23:4xZ.
**Source:** the CRO's D1 RESULT on the adapter NEW-01 guard (@5f82151a2e: NOT MET, the page reopens RETAINED reports,
26 reopens, 0 engine runs) and 1.0.0_SA_CTO 102447 ("cut the remedy"). Cell IB-pr-194, carried by the REOPENED
order `IRPT_BCKEND.TO-IB-pr-191` (worker ~63, complete), merged on CLOUD @ae8da14d12. **Ledger (opened before any
write):** `irpt-adapter-reopen-guard-20260928` (U1 closed; D1, A1 open). It serves the open D1 of
`irpt-adapter-implausible-guard-20260928`.

## 1. Both readers of the served figure (the count the last packet missed)

The Performance page gets a 49F figure from ONE of two readers inside `retained.py` `RetainedPerformance._compute`:
- **Compute (fresh):** no accepted pointer exists -> `f49_engine.calculate` -> persist -> answer. Guarded since
  22:02Z by IB-pr-191 (hcZpXDDo): a linked day with r_net <= -1 refuses EngineReturnImplausible.
- **Reopen (retained):** an accepted pointer exists -> `reopen(existing)` returns the stored report, with no engine
  read. NOT guarded today; this packet adds the guard.

The page reads almost only the second: 26 reopens and 0 engine runs across the CRO's two walks.

## 2. The change (90c4b596f3; `performance/retained.py` only, plus tests)

- `implausible_engine_series(report)` is True when any point of `returns.daily_cumulative_series` has a cumulative
  value <= -1.0. A cumulative value <= -1 means some linked day had r_net <= -1, the IB-pr-191 predicate.
- `reopen(pointer, *, check_engine_series)`: the reopen of an EXISTING pointer (`check_engine_series=True`) raises
  `f49_engine.EngineReturnImplausible` when the owner's firm is 49 Financial and the predicate holds. The boundary
  names it DEPENDENCY_UNAVAILABLE (`entry.py`, since hcZpXDDo). The fresh path's own read-back after persist is
  unchanged (`check_engine_series=False`); under the guarded `calculate` it cannot hold this shape.
- **Nothing in the store is deleted, rewritten or re-derived.** The two reports stay retained; only their reopen
  answer changes. Rolling back restores the old answer.

**Checks** (COO-authored, dry-run at the base, re-run by the COO on the worker branch and on CLOUD after merge):
- P19-4-AC1 (fixture): a report retained through the PRE-guard engine (f49_engine.py at 8d7a8b10fe, as served before
  hcZpXDDo) reopens as EngineReturnImplausible; a clean account reopens with the same report and no second engine
  read. Base: DID NOT RAISE (the live bug).
- P19-4-AC2 (the live store, read-only): of the 23 retained 49F reports in `irpt-requests` + S3, the predicate flags
  exactly 790fe675 and 74fb35a4 (the NEW-01 account's 1Y and YTD) and passes the other 21.
- P19-1-AC1..3 still PASS. On CLOUD after merge: 38 passed (retained, f49_engine, public_reasons).

## 3. The artifact and the move

| | live | new |
|---|---|---|
| irpt-performance-adapter CodeSha256 | `hcZpXDDo..` (S3 version wVW7wVQw.) | `qfxZ0DzB..` (S3 version 5bmwADQs.) |

- **Source map:** one staged pin moves, `retained.py` b18cb77c7d -> 90c4b596f3 (commit 40b755719d). All 69 pinned
  blobs were measured equal to the live zip before the edit.
- **Census:** 69 -> 69; ONLY `retained.py` differs.
- **flat_zip_module_census:** pin skew 0. **~Y zip_module_census:** the flagged set is byte-equal to live; the live zip
  also flags `retained.py` STALE against the tree, which this move resolves.
- **Cold start:** with `/var/task` mapped (the ~Y smoke is non-discriminating on this Windows host), the new and the
  live zip both import `runtime` and answer `{}` with a named envelope. After apply: a REAL cold-start invoke.
- **Dry plan** (performance root, plan var default null): **0/1/0**, code only (`s3_object_version` wVW7wVQw ->
  5bmwADQs, `source_code_hash` hcZpXDDo -> qfxZ0DzB). No plan is armed; IAM unchanged.
- **Rollback:** re-apply at S3 version wVW7wVQw. (hcZpXDDo).

## 4. Blast radius (both readers)

- **Reopen reader, moves:** exactly 2 of the 23 retained 49F reports (790fe675, 74fb35a4). Before: served -100.00%.
  After: refused by name, DEPENDENCY_UNAVAILABLE.
- **Reopen reader, unchanged:** the other 21 retained 49F reports (the predicate passes them, measured), every
  retained COT and INF report (the check is 49F-only), and every refusal branch.
- **Compute reader, unchanged:** IB-pr-191's guard is already served; `f49_engine.py` and `entry.py` do not move.
- **Not closed by this act:** the 2 near-miss invested accounts (row S184) have no retained report with a point at or
  below -1 and keep serving about -100% on compute. Their close is the consolidated holdings gold (Andrew-direct
  ~22:4xZ).
- **Reachable:** the Performance route; today walk principals and Andrew on DEV.

## 5. Proof at apply (D1) and after (A1)

- **D1, discriminating on the reopen reader:**
  - before the apply, the CRO walk reads NEW-01 1Y and YTD (the reopened 790fe675 / 74fb35a4: served -100.00%) and
    one control;
  - apply;
  - CodeSha256 readback == qfxZ0DzB; a REAL cold-start invoke answers; re-plan shows no changes;
  - the same walk reads NEW-01 1Y and YTD as a named refusal, with the control unchanged.
- **A1:** the page shows the refusal in words.
- The implausible-guard ledger's D1 closes on the same after-read.

## What the halves sign against

This file's committed blob; 90c4b596f3 (merged @ae8da14d12); source-map commit 40b755719d; artifact qfxZ0DzB with
its census, gates, 0/1/0 plan and rollback; and the blast radius in section 4, counting both readers.
