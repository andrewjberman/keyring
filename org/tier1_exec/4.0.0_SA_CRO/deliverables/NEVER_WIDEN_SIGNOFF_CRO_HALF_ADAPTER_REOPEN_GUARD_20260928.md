# NEVER-WIDEN SIGN-OFF (4.0.0_SA_CRO half) -- irpt-performance-adapter hcZpXDDo -> qfxZ0DzB: a retained 49F report whose series reaches -1 is refused at reopen (IB-pr-194)

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_ADAPTER_REOPEN_GUARD_20260928.md`
blob `7bedf42e` (at `c67141630f`, at HEAD, and on disk; read 2026-09-28 ~23:4xZ).
- **Word diff:** a new packet for a new act; it answers this seat's D1 RESULT on the first guard (`@5f82151a2e`, NOT MET:
  the page reopens retained reports). No prior packet to diff against.
- **Asked by:** 2.0.0_SA_COO~P, msg 102482. **Ledger:** `irpt-adapter-reopen-guard-20260928` (U1 closed 23:36Z; D1, A1 open).
  This seat is not in the act.

## VERDICT: SIGNED on blob 7bedf42e, with one condition

The act counts both readers of the served figure, which is the count the first packet missed, and moves exactly the two
retained reports that carry the impossible answer. It widens nothing: no store object is written, and the fresh path is
byte-for-byte the same call with one keyword.

### The artifact, read here on its own bytes

- **Bytes:** S3 `opal-313476888478-lambda-artifacts/investor-reporting/irpt-performance-adapter.zip`, VersionId `5bmwADQs`
  hashes to `qfxZ0DzB` (418,269 bytes, 69 members). The live `wVW7wVQw` hashes to `hcZpXDDo`, equal to the function's
  CodeSha256 at read time (Active, Successful, LastModified 22:02:49Z).
- **Census:** 69 -> 69; only `retained.py` differs.
- **Code (90c4b596f3):** `implausible_engine_series(report)` flags any `returns.daily_cumulative_series` point <= -1.0
  (plain number, or a dict's `cumulative` or `value`). `reopen(pointer, *, check_engine_series)` raises
  `f49_engine.EngineReturnImplausible` only when reopening an EXISTING pointer (`check_engine_series=True`), the owner's
  firm is 49 Financial and the predicate holds. The fresh path's own end-of-persist reopen passes `False`; that branch
  is otherwise unchanged. `entry.py` is byte-equal to live, so the public code is the one this seat already resolved on
  hcZpXDDo through the zip's reasons table and MRO: `EngineReturnImplausible -> DEPENDENCY_UNAVAILABLE`.
- **Tests, on the zip's own modules:** `tests/test_retained_performance.py` ran with the zip directory first on
  `sys.path` (asserted for `retained` and `f49_engine`) and `IRPT_CONTRACTS_DIR` at the zip.
  - New zip: **20 passed**.
  - Live zip, the negative control: **1 failed, 19 passed**; the one failure is
    `test_reopen_refuses_a_pre_guard_implausible_engine_report`, so the test tells the two zips apart.

### The live store, read here with the zip's own predicate (read-only)

The function's `IRPT_REQUESTS_TABLE` is `irpt-requests`. The table holds 325 items; 26 are `PERFORMANCE_ACCEPTED#`
pointers: 23 for tenant `49financial`, 2 `cottonwood`, 1 `inflection`. Each pointer's `REPORT#<id>#<revision>` index item
carries the blob (`opal-data-irpt`, `irpt/<firm>/platinum/performance_reports/<id>/<revision>.json`, versioned). All 26
blobs were read by VersionId, and each blob's sha256 equals its revision.

| population | count | result of `implausible_engine_series` |
|---|---|---|
| 49financial retained reports | 23 | **2 flagged**: revisions `790fe675` and `74fb35a4`, each 69 points with a minimum of exactly -1.0 (the NEW-01 account's 1Y and YTD) |
| 49financial, the other 21 | 21 | pass; the lowest minimum among them is -0.0879 |
| cottonwood, inflection | 3 | pass (minima -0.0118, -0.0210); the check is 49F-only anyway |

That is the packet's "exactly 2 of 23", measured here independently. The near-miss accounts (row S184) have no retained
report at or below -1, so the act does not move them, as section 4 says.

### Blast radius, read from the producer's own rule

- **Reopen reader, moves:** the two reports above, from a served -100.00% to DEPENDENCY_UNAVAILABLE.
- **Reopen reader, unchanged:** 21 49F reports, 3 other-tenant reports, every refusal branch (measured: the predicate
  passes them).
- **Compute reader, unchanged:** the first guard stays as served; `f49_engine.py` and `entry.py` do not move.
- **Store, unchanged:** nothing written; rollback (re-apply `wVW7wVQw`) restores the old answer.
- **Not closed:** the 2 near-miss invested accounts keep serving about -100% on compute (S184); their close is the
  consolidated holdings gold, per Andrew's ~22:4xZ word.
- **Plan:** 0/1/0, code only (`s3_object_version` wVW7wVQw -> 5bmwADQs; `source_code_hash` hcZpXDDo -> qfxZ0DzB). IAM unchanged.

### Condition (D1): the before/after read is the reopen path, on the NEW-01 account's retained 1Y and YTD, plus a control

This seat takes the BEFORE-read on hcZpXDDo by `/ui-walk` right after this half lands: the NEW-01 account's 1Y and YTD
(the reopened `790fe675` and `74fb35a4`) and one invested control account's YTD. After ~P's apply (CodeSha256 readback
`qfxZ0DzB`, a real cold-start invoke, re-plan No changes), the same three reads: NEW-01 1Y and YTD refuse by name, the
control is unchanged. Only then does this ledger's D1 close, and with it the open D1 of
`irpt-adapter-implausible-guard-20260928`. A refusal-only read, or a compute-path read, does not count.

## D1 RESULT (2026-09-29 00:2xZ): MET on the reopen path

- **Apply:** ~P applied `qfxZ0DzB` at 00:11:21Z (msg 102497). Read here at the walk's start: get-function CodeSha256
  `qfxZ0DzBGcSrD2B0ownwGZtSLskLGuw4vnqyASd0AMA=`, Active, Successful.
- **BEFORE-read, on hcZpXDDo** (walks `20260928T235131Z` #012, `20260929T000244Z` #010 and #006): NEW-01 1Y
  -100.00%; NEW-01 YTD -100.00%; control YTD 5.93%.
- **AFTER-read, on qfxZ0DzB** (walk `20260929T001245Z`, 00:12-00:21Z, disarmed with the login REFUSED):

| read | before | after |
|---|---|---|
| NEW-01 account, YTD (#010) | -100.00% | "Performance for this account is temporarily unavailable right now. It becomes available again once the upstream data source Opal Capital relies on for this account answers." Picker: "YTD unavailable". |
| NEW-01 account, 1Y (#014) | -100.00% | the same refusal; Details: DEPENDENCY_UNAVAILABLE. Picker: "1Y unavailable". |
| control account, YTD (#006) | 5.93% | 5.93%, answered January 2nd to September 22nd, 2026. Picker: "YTD 5.93%". |

- The reopen path is what the walk exercises (the retained pointers `790fe675` and `74fb35a4` exist and the fresh
  path is unchanged), so this read discriminates on the act's own reader. A1 (the page shows the refusal in words) is
  met by the same shots. Both this ledger's D1 and the open D1 of `irpt-adapter-implausible-guard-20260928` may close.
- **Carried, not closed:** the 2 near-miss invested accounts (S184) keep serving about -100% on compute.

## What this half signs against

- Packet blob `7bedf42e`.
- Commit 90c4b596f3 (merged at ae8da14d12); source-map commit 40b755719d.
- Artifact `qfxZ0DzB` (S3 `5bmwADQs`) with its 69-file census, the 0/1/0 plan and rollback to `wVW7wVQw`.
- The blast radius above: 2 of 23 retained 49F reports move, 24 of 26 retained reports and both other tenants unchanged,
  the store untouched, the near-miss pair named as not closed.
