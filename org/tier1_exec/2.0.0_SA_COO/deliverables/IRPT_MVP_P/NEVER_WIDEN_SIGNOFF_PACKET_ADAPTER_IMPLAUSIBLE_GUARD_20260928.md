# Never-widen sign-off packet -- irpt-performance-adapter: an impossible engine day is refused by name, never served as -100%

**For:** `1.0.0_SA_CTO` and `4.0.0_SA_CRO`. **Author and operator:** `2.0.0_SA_COO~P`, 2026-09-28 ~21:4xZ.
**Source:** NEW-01 (HIGH; CRO re-walk @f330857833, CTO 102357), cause measured in row IRPT_BCKEND-S177; round-19 cell
IB-pr-191 (task order `IRPT_BCKEND.TO-IB-pr-191`, worker ~61, complete), merged on CLOUD @4f47d58fe3. The producer
fix is routed separately (CTO ruling 102411, row S181). **Ledger (opened before any write):**
`irpt-adapter-implausible-guard-20260928` (U1 closed; D1, A1 open).

## 1. What NEW-01 is

An invested 49 Financial account answers YTD -100.00% on the Performance page (shots 20260928T133602Z#138/#139). The
49F engine table `canonical/twr_daily` carries one OK row on 2026-04-16 for that account: bmv 13,360.59, emv 0.0,
cf_net 0.0, so r_net = -1.0 (`c02_twr_engine.py:264` has no guard below -1). The adapter links
`running *= 1 + r_net` (`f49_engine.py:199-204`), so every later day multiplies that zero and the account answers
-100% while it holds ~98.6k today. Year to date: 28 OK account-days carry r_net <= -0.999 across 24 accounts; 17 of
those accounts hold value now.

## 2. The change (57a58117fb; `performance/f49_engine.py` and `performance/entry.py`, plus a test)

- `f49_engine.py`: `class EngineReturnImplausible(EnginePerformanceRefused)`; `calculate` raises it when any row linked
  inside the window carries `r_net <= -1.0`, before any report is built. Fixed text; no account, date or value in it.
- `entry.py` `build_entry` reasons: `"EngineReturnImplausible": "DEPENDENCY_UNAVAILABLE"` (an engine answer our checks
  refuse is a dependency the caller does not control, the InflectionPerformanceRefused precedent). Without it the MRO
  walk would answer OBJECT_NOT_COVERED ("this account is not covered"), which is false. Every existing line unchanged.
- `parity_period_returns.py` and the producer are untouched.

**Checks** (COO-authored, dry-run at the base, re-run by the COO on the worker branch and on CLOUD after merge):
- P19-1-AC1 (fixture, the measured NEW-01 shape): refuses as EngineReturnImplausible; the control account computes.
- P19-1-AC2 (live twr_daily, read-only): YTD 2026-01-01..2026-09-25 for the NEW-01 account refuses as
  EngineReturnImplausible (base: served -1.0); a live control account computes 0.069071.
- P19-1-AC3: the boundary line reads DEPENDENCY_UNAVAILABLE; the EnginePerformanceRefused line is unchanged.
- Performance suite on CLOUD after merge: 19 passed (test_f49_engine + test_public_reasons).

## 3. The artifact and the move

| | live | new |
|---|---|---|
| irpt-performance-adapter CodeSha256 | `F0bYtOfB..` (S3 version G4UtfeeR.) | `hcZpXDDo..` (S3 version wVW7wVQw.) |

- **Source map:** only two staged pins move, `entry.py` c8ef8b7751 -> 57a58117fb and `f49_engine.py` 8d7a8b10fe ->
  57a58117fb (commit 1af199f0f8). All 69 pinned blobs were measured equal to the live zip before the edit.
- **Census:** 69 -> 69; ONLY `entry.py` and `f49_engine.py` differ.
- **flat_zip_module_census:** shared-package pin skew 0 (rc 0).
- **~Y zip_module_census:** with the performance package's own entry/handler/transport named as intended, the flagged
  set (errors, maintained_sources, request_composition, resolve, routetable) is byte-equal to live; the live zip fails
  a superset. No flagged module moves.
- **Cold start:** the ~Y smoke cannot run on this Windows host (live env points at `/var/task/firm_registry.json`);
  it fails identically on the live zip, so it is stated as non-discriminating here. With `/var/task` mapped to the
  extraction dir, the new and the live zip both import `runtime` and answer `{}` with a named UNAVAILABLE envelope.
  After apply, a real cold-start invoke must answer.
- **Dry plan** (performance root, `approved_performance_plan` default null): **0/1/0**, code only
  (`s3_object_version` G4UtfeeR -> wVW7wVQw, `source_code_hash` F0bYtOfB -> hcZpXDDo). No plan is armed; IAM unchanged.
- **Rollback:** re-apply at S3 version G4UtfeeR. (F0bYtOfB), restored as latest.

## 4. Blast radius

- **Moves:** a 49F Performance read whose window links a day with r_net <= -1. Before: served, a wrong figure
  (-100%, or a sign-flipped series below -1). After: refused by name, public DEPENDENCY_UNAVAILABLE.
- **Unchanged:** every window with no such day (the control computes identically); INF and COT (not on the engine
  path); every refusal branch; the render delegate path; every vendor path. No plan is armed.
- **Reachable:** the Performance route; today, walk principals and Andrew on DEV. The route is not open to firm users
  (STATUS~P Parked row 1).
- **Named consequence:** the 17 invested accounts with such a day show a refusal, not a figure, until the producer fix
  (S181) lands. A refusal replaces a wrong number; it does not add one.

## 5. Proof at apply (D1) and after (A1)

- **D1:** live before-read of the served F0bYtOfB: the cold-start probe's refusal branch (as at 09-27 23:47Z); apply;
  CodeSha256 readback == hcZpXDDo; a cold-start invoke answers; the same refusal-branch read after, unchanged;
  re-plan No changes.
- **A1:** the next walk window: the NEW-01 account's YTD on the signed-in page shows a named refusal, not -100%; a
  control account still shows its figure.

## What the halves sign against

This file's committed blob; 57a58117fb (merged @4f47d58fe3); source-map commit 1af199f0f8; artifact hcZpXDDo with
its census, gates, 0/1/0 plan and rollback; and the blast radius in section 4.
