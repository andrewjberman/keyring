# Never-widen CTO half -- the SC-e-62 + SC-e-56 merge and the Investor Reporting bundle rebuild

Signer `1.0.0_SA_CTO~DELL2` (the IRPT_BCKEND CTO half, under NFRA_CTLPLN ADDENDUM v0.12 C-ROLES), 2026-10-07 ~16:0xZ.

**Request:** dell1 `2.0.0_SA_COO~M1`, carried by `0.0.0_AB_MSTR~DELL2`:
- msg 815;
- msg 819;
- ADDENDUM 1, msg 822.

The file is `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_HOLDINGS_SIX_CLASS_RELEASE_20261007.md`
on `q/dell1/secclass-r12-rel-e62e56/r2` @e03c84aa40, with M1's COO half re-signed. **r1 (@92b780879e) is NOT signed:** its "one member
changes" was wrong.

## SIGNED, for exactly this act

1. **The merge:** `0.0.0_AB_MSTR` merges r2 (@e03c84aa40) into CLOUD.
2. **The rebuild:** the push gate rebuilds ONE key, `s3://opal-data-mdpf/code/scripts/assets_gold/investor_reporting/investor-reporting.tar.gz`,
   with **exactly two of its 12 members changed**:

   | member | before (md5) | after (md5) |
   |---|---|---|
   | `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py` | `07b2b52d` | `d74b54d2` |
   | `docs/contracts/investor-reporting/v1/HoldingsSnapshot.schema.json` | `cd007b73` | `004631af` |

3. **The rollback:** copy VersionId `Lo8nhS9k26LH0R_sbEvLi9O6CYTlMmRR` back over the key.

## Read by this seat at signing (not taken from the request)

- **The bundle's members are an explicit list** (`.tools/safe_deploy_core.py`, the `investor_reporting` entry, ~:343-431): 12 repo
  paths and nothing under `tests/`. So the 3 changed tests do not reach S3.
- **Two-dot diff of dell2 CLOUD HEAD against r2**, over every bundle member's directory: only `holdings_snapshot.py` and the v1
  schema move among members. The md5s above were printed from `git show` on both refs.
- **The candidate fixed (a near miss, read-side):** the first read compared HEAD with a `FETCH_HEAD` another seat had already moved and
  showed the schema unchanged. The read was repeated on a named ref (`refs/cto-dell2/e62r2`), which gave the values above. A shared
  `FETCH_HEAD` is not a pin.

## Conditions

1. **After the push, the new bundle is read back, not trusted.** `tar -tzf` lists 12 members; the md5s of all 12 are printed; exactly the
   two above differ, with those values. Anything else means rollback to `Lo8nhS9k...`.
2. **The Holdings publish run is NOT covered here.** It is IRPT_BCKEND's act under its own pair. The COO half of THIS release is
   `2.0.0_SA_COO~M2`'s, as named by this seat (`~P2` msg 818 concurs). That run's first step is M1's newly-placed check: about 238 rows,
   and a far count is a stop.
3. **The two Lambda schema copies** under `infra/aws/lambda/investor-reporting/` change in the repo only. They reach a served function
   only at IRPT_BCKEND's next build of it, under that build's own half. Today 0 canonical `multi_asset` rows exist (M1's scans), so the
   enum narrowing refuses nothing that is served.

-- 1.0.0_SA_CTO~DELL2

## AMENDMENT 1 (2026-10-07 ~16:1xZ, on `2.0.0_SA_COO~M2` msg 827): condition 2 was wrong -- the scheduled Holdings fire IS covered

**Why condition 2 was wrong.**
- `irpt-holdings-snapshot` reads ENABLED, `cron(15 10 ? * MON-FRI *)` America/New_York.
- It dispatches the runner at this exact bundle key (`infra/aws/terraform/investor-reporting/directory/schedule.tf`
  `irpt_runner_bundle_uri`, read by this seat).
- So the merge alone makes the next weekday fire publish with the new code at every firm. A scheduled producer moved by a bundle is a
  second writer of the served Holdings. Condition 2 did not count it.

**What this half now covers.** The merge, the bundle rebuild, AND the FIRST scheduled Holdings fire after it (next: 2026-10-08 10:15 ET),
at each firm the schedule serves. It is covered under these terms:

1. **Precondition, before the merge.** `~M2` runs M1's newly-placed check on r2
   (`R11_CHECKS/holdings_cusip_newly_placed.py` + `sc_e56_newly_placed_check.py`) and prints ok=True with its count. A count far from
   about 238, or ok=False, means NO merge.
2. **Branch A (the fire publishes).** Per firm:
   - the new `latest.json` revision is recorded;
   - `reconcile_before_after` passed (the producer's own gate);
   - the count of holdings whose class changed is printed beside the expected (e56's half table).
3. **Branch B (the fire refuses, or a firm's count is off).** That firm's `latest.json` is re-pointed at its prior revision, recorded
   before the fire. Then the bundle key is restored to `Lo8nhS9k...` before the following weekday fire.
4. **Before the fire,** each firm's current `latest.json` revision is recorded as its rollback pin.

Condition 3 stands. The COO half that covers this fire is `~M2`'s.

-- 1.0.0_SA_CTO~DELL2

## CARRY to r3 (2026-10-07 ~16:4xZ, on MSTR msg 873): this half, with AMENDMENT 1, covers `q/dell1/secclass-r12-rel-e62e56/r3` @a87e215afc

**Read by this seat on named refs, not taken from dell1's statement.**
- **Refs:** `refs/cto-dell2/e62r3` @a87e215afc; origin CLOUD fetched as `refs/cto-dell2/origin-cloud` @124bf03071.
- **What r3 contributes beyond origin** (three-dot diff from the merge base): **14 files.** They are:
  - the two bundle members;
  - the three tests;
  - the two Lambda schema copies;
  - the investor-reporting Terraform CHANGELOG;
  - MDPF_SECCLASS records: the order, the proof, the half requests, the newly-placed list and its check script.
  No other deployed path.
- **Merge:** `git merge-tree --write-tree` of origin with r3 reads clean.
- **Bundle members:**
  - `holdings_snapshot.py` reads `d74b54d2` and the v1 schema `004631af`, the same as r2;
  - the other 10 members equal origin by md5 (directory_runner, ids.py, DirectoryEntry schema, schwab_account_codes .py/.json,
    trading_calendar, both runner_common, checked).
- **Exactly 2 of 12 members change,** as signed.

The terms are unchanged: AMENDMENT 1's precondition, both branches and the per-firm pins; condition 1's tar read-back after the push.
r1 and r2 are no longer the act.

-- 1.0.0_SA_CTO~DELL2

## CARRY to r4 (2026-10-07 ~17:3xZ, on MSTR msg 921): this half, with AMENDMENT 1, covers `q/dell1/secclass-r12-rel-e62e56/r4` @73c5a770df

**Read on named refs.** Refs: `refs/cto-dell2/e62r4` @73c5a770df and origin CLOUD @4487fce9a5.
- **What r4 contributes beyond origin** (three-dot): the same **14 files** as r3. The CHANGELOG.json entry is now a union with dell2's.
- **Merge:** `merge-tree` with origin reads clean.
- **Members:** `holdings_snapshot.py` `d74b54d2` and the v1 schema `004631af`; the other 10 members equal origin by md5.
- **Exactly 2 of 12 members change,** as signed.

**A correction to the relayed wording:** msg 921 says the deploy scope is "holdings_snapshot.py + 3 tests". The bundle carries no tests,
and its two changed members are `holdings_snapshot.py` and the v1 schema. This half binds the two members, not the relayed wording.

r1, r2 and r3 are no longer the act.

-- 1.0.0_SA_CTO~DELL2

## Condition 1 DISCHARGED (2026-10-07 ~18:4xZ): the tar read-back, read independently by this seat

The served key moved at 18:33:12Z by the CLOUD push gate:
- **New version:** `JITP9ecNeQyAnAmKo90oxqWyFemEqVaI`, 108,774 B, IsLatest; tar md5 `7de9bbd51be6919a1ee2beb9f69a8860`.
- **Rollback point:** `Lo8nhS9k...`.

This seat fetched both versions by VersionId and compared every member:
- **12 members in each;** 0 added, 0 removed.
- **Exactly 2 changed:**
  - `holdings_snapshot.py` `07b2b52d` -> `d74b54d2`;
  - `docs/contracts/investor-reporting/v1/HoldingsSnapshot.schema.json` `cd007b73` -> `004631af`.
- **The other 10 are equal:** directory_runner, schwab_account_codes .py and .json, the three runner_common, firm_registry.json,
  DirectoryEntry schema, ids.py, trading_calendar.
- **0 tests.**

`2.0.0_SA_COO~M2` read the same independently (COO half @31ae01919c, msg 984). Two independent reads agree.

Owed next under AMENDMENT 1: `~M2`'s per-firm pins re-read just before the 2026-10-08 10:15 ET fire, then the per-firm read, Branch A
or B.

-- 1.0.0_SA_CTO~DELL2
