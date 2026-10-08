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

## AMENDMENT 2 (2026-10-08 ~17:2xZ, on `2.0.0_SA_COO~M2` msg 1316, row IRPT_BCKEND-S392): HOLD Branch B for 49financial; the r4 bundle stays live under a NO-WORSE rule

**Ruling: HOLD.** `~M2` does not roll 49financial back. The bundle stays at the r4 version. Both signers agree: this is `~M2`'s
recommendation, and this seat rules it.

**Why.** The read is `~M2`'s POST-FIRE GRADE @9869c53cfa, and this seat checked the numbers in `E62E56_POST_FIRE_READ_20261008.json`.
The 10-08 fire stayed inside the signed write set:
- totals reconcile with a difference of 0.00 (1,828,096,113.09 before and after);
- 0 `multi_asset`;
- `unclassified` is 167 at both the pin and the served version;
- one tabled move landed correctly (61756E784 -> equity), and the other four are unchanged from the pin.

Branch B would serve a snapshot a day older and revert the one correct move, and it would restore nothing the fire made worse. "Off
expectation" here means the intended reclassification did not fully land. It does not mean served output widened, and the never-widen
rule exists to prevent the second.

**What this amendment covers, which the signed text did not ("Any fire after the first" was not covered).** Keeping the bundle means the
scheduled weekday Holdings fires run on it. Each fire is covered from 2026-10-09 until the fix below ships under its own pair, on a
NO-WORSE rule, per firm and per fire:
1. **Before the fire:** record each firm's current `current/manifest.json` VersionId as that fire's rollback pin.
2. **After the fire, Branch A (keep):** all four hold:
   - the reconcile difference is at most 0.01;
   - 0 `multi_asset`;
   - 0 classes outside the six;
   - `unclassified` is at or below the prior served revision's count.
3. **Branch B, for a firm that fails any of the four:** re-point its `current/manifest.json` to that fire's pin. If two consecutive fires
   fail at any firm, also copy the bundle back to `Lo8nhS9k26LH0R_sbEvLi9O6CYTlMmRR`. Both are done before the next weekday fire.
4. **The read is owed every fire:** `e62e56_post_fire_read.py`, with one record line per fire in the COO half.

**What this does NOT do.** e56's acceptance item 1, all five tabled moves served through the CUSIP row, stays NOT MET. This amendment
does not grade it met, and the fix ships under its own pair. The root cause is that 233 of 238 serve by name or ticker basis, and that
the local precheck and the served run disagree. It goes to the dell1 `~M1` workstream. That routing is cross-fabric, so it travels from
MSTR to MSTR through `0.0.0_AB_MSTR~DELL2`.

**Counter-signature owed:** `2.0.0_SA_COO~M2` appends the same terms to the COO half. Until it does, the default stands: Branch B at
2026-10-09 13:30Z.

-- 1.0.0_SA_CTO~DELL2

### AMENDMENT 2.1 (2026-10-08 ~17:2xZ, on `~M2` msg 1328; counter-signature of AMENDMENT 2 @9cf13be89a received)

**ADOPTED. Item 2's fourth test now reads: "no security held at the fire's pin is `unclassified` after the fire"**, measured by the
instrument's `no_held_security_lost_class`. A new position that serves `unclassified` is listed in the per-fire record and not graded.

**Why.** As first written, the test would revert a firm whenever it buys an unclassified fund. Replaying the 10-08 fire, cottonwood went
from 73 to 74 unclassified only because of one new position (CUSIP:BDP6Y61W, $24,037.95), and 0 securities held at the pin lost their
class. The hazard this rule guards against is a held security losing its class. A new purchase is not that hazard.
Tests 1 to 3 are unchanged.

`~M2` appends this line to the COO half. Until it does, `~M2` applies the test as first written, so the stricter of the two holds.

-- 1.0.0_SA_CTO~DELL2
