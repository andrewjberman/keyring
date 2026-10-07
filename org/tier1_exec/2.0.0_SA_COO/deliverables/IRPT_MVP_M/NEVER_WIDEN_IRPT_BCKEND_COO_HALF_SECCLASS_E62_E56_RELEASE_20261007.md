# Never-widen COO half (IRPT_BCKEND) -- the SC-e-62 + SC-e-56 merge, the Investor Reporting bundle rebuild, and the first Holdings fire after it

Signer `2.0.0_SA_COO~M2` (IRPT_BCKEND workstream M, the Holdings snapshot's owner on dell2), 2026-10-07T16:23:36Z. Named to sign
by `1.0.0_SA_CTO~DELL2` (msgs 431 and 826; `~P2` concurs, msg 818).

**Request:** dell1 `2.0.0_SA_COO~M1`. The file is
`org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_HOLDINGS_SIX_CLASS_RELEASE_20261007.md` on
`q/dell1/secclass-r12-rel-e62e56/r2` @e03c84aa40, with ADDENDUM 1: "two members change". It reached this seat as msgs 816, 820 and
823. **r1 (@92b780879e) is NOT signed.**

**Paired with:** the CTO half `org/tier1_exec/1.0.0_SA_CTO/deliverables/NEVER_WIDEN_SECCLASS_E62_E56_IR_BUNDLE_CTO_HALF_20261007.md`
@f67ab9002b, plus its AMENDMENT 1 @6c57a70f2f. That amendment covers the first weekday fire after the merge, on this seat's
finding (msg 827).

## SIGNED, for exactly this act and nothing wider

1. **The merge.** `0.0.0_AB_MSTR` merges r2 @e03c84aa40 into CLOUD.
2. **The rebuild.** The push gate (`.tools/safe_deploy_core.py`) is the ONE writer of the key; N = 1, because the Terraform
   schedule only reads it. It rebuilds the one key
   `s3://opal-data-mdpf/code/scripts/assets_gold/investor_reporting/investor-reporting.tar.gz`. Exactly 2 of its 12 members change:

   | member | before (md5) | after (md5) |
   |---|---|---|
   | `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py` | `07b2b52d` | `d74b54d2` |
   | `docs/contracts/investor-reporting/v1/HoldingsSnapshot.schema.json` | `cd007b73` | `004631af` |

   No `tests/` path is a member, so the 3 changed tests do not ship. Both md5 columns were measured by this seat with
   `git show` on HEAD and on r2.
3. **The first Holdings fire after the merge.** The fire is `irpt-holdings-snapshot`, read ENABLED by live `get-schedule`:
   `cron(15 10 ? * MON-FRI *)` America/New_York, running this bundle URI (`infra/aws/terraform/investor-reporting/directory/schedule.tf:198`).
   - If the merge lands today, the fire is Thursday 2026-10-08 10:15 ET (14:15Z).
   - Today's fire already ran on the old bundle, publishing 2026-10-06 at 14:18-14:21Z.
   - This half covers that ONE fire, and no manual Holdings run.

## The precondition, met before signing

The newly placed check ran on r2's own producer, from a detached worktree at @e03c84aa40, as read-only local builds (no
`--upload`) plus consistent DynamoDB reads:

```
FIRM 49financial as_of=2026-10-05 held=1941 newly_placed=51 usd=7239921.61
FIRM cottonwood as_of=2026-10-05 held=1453 newly_placed=187 usd=22864368.78
FIRM inflection as_of=2026-10-02 held=1601 newly_placed=0 usd=0
HOLDINGS-CUSIP-NEWLY firms=3 total=238
SC-E56-NEWLY ok=True firms=3 of 3 listed=238 false_entries=0 control=present
```

- **Count:** 238, which equals the request's figure. This is not a far count, so no stop.
- **List:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/E56_PRECHECK_HOLDINGS_CUSIP_NEWLY_PLACED_ON_R2_20261007.json`
  (sha256 `a8aedad6b1eb...`). Its claim is `inferred`: a local build, not the served bytes.
- **Inflection's date:** Inflection built at its latest partition, 2026-10-02.

## Pins recorded before the fire (2026-10-07T16:10:46Z; the rollback target per firm)

| firm | `irpt/<firm>/platinum/holdings/current/manifest.json` VersionId | latest_date | revision | dated manifest VersionId |
|---|---|---|---|---|
| 49financial | `GtsM8pj9VnTwPZH3n5Bzp.oobsgLaja0` | 2026-10-06 | 35ea000850f7 | `jKILUvZkA_mGmj3kse518hC2bNmfotNb` |
| inflection | `a6gP7JDBtaKHr_LMKP0vQsNSegtaQQWc` | 2026-10-06 | acd27f407bbc | `znEkcH2Z7odL5LBsa6AApnql1ng0prsv` |
| cottonwood | `gF3nGvI1eKu_xPEYZXBaRl7iw55fpmnL` | 2026-10-06 | 7f69e500c18f | `p0VXpRizZCQes3Pqek65ml9NpbByXJHU` |

## Both branches, read from the producer's own rule

**Branch A: the fire publishes.** `run_firm` refuses to land a snapshot unless `validate_snapshot` passes and
`reconcile_before_after` holds; the unassigned difference control must also discriminate (`holdings_snapshot.py` ~2909-2935).
The class change does not enter the reconcile: nodes, weights and totals do not depend on classification. Per firm, this seat
reads after the fire:
- the new revision;
- the reconcile block reads reconciled;
- the class changes against the request's expectation (newly placed about 238; the five class moves tabled in e56's half);
- 0 `multi_asset` classes.

Any firm off its expectation takes Branch B for that firm.

**Branch B: the fire refuses, or a firm reads off.** A refusing producer lands nothing, and that firm keeps serving its pinned
revision. A firm that landed off-expectation is rolled back:
- re-point that firm's `current/manifest.json` to the pinned VersionId above;
- copy the bundle back to VersionId `Lo8nhS9k26LH0R_sbEvLi9O6CYTlMmRR`, the live bundle read by this seat at 16:0xZ (108,459 B,
  2026-10-07T13:31:17Z).

Both happen before the next weekday fire.

**Also bound (the CTO half's condition 1):** after the push, the new bundle is read back with `tar -tzf`. It must show 12
members, with exactly the 2 above changed; anything else means the bundle is rolled back before the fire.

## Not covered

- Any manual Holdings run.
- Any fire after the first.
- The two Lambda schema copies under `infra/aws/lambda/investor-reporting/`. They are repo-only until IRPT_BCKEND's next build
  of those functions, under that build's own pair.
- Any change to the schedule itself.

-- 2.0.0_SA_COO~M2

## AMENDMENT 1 (2026-10-07 ~16:4xZ, 2.0.0_SA_COO~M2) -- re-pointed from r2 to r3 @a87e215afc

**Why:** r2 cannot merge. Its MDPF_SECCLASS channel row S55 collides with a laptop S55 on origin (msg 864). dell1 republished
as `q/dell1/secclass-r12-rel-e62e56/r3` @a87e215afc (msg 874). That is r2 plus a merge of its r12 line, and it renumbers the row
to S58.

**Measured by this seat, not taken from the relay:**
- **Bundle members:** all 12 (the explicit list in `.tools/safe_deploy_core.py`) are byte-equal between r2 and r3. That is
  0 of 12 differing. `holdings_snapshot.py` reads `d74b54d2` and `HoldingsSnapshot.schema.json` reads `004631af` at r3.
- **The gate:** `.tools/safe_deploy_core.py` is equal between r2 and r3.
- **Against dell2 CLOUD:** r3 brings 48 files over its merge-base, against r2's 47. The one extra file is
  `org/tier1_exec/2.0.0_SA_COO~M1/drive_log_20261007T15Z_desktop-hk1uu7n.md`, a log, not a deployable path.

**Effect:** every term above now reads r3 @a87e215afc in place of r2 @e03c84aa40, and nothing else changes:
- the scope (one key, the same 2 of 12 members);
- the precondition. The 238 check stands, because the producer bytes are unchanged;
- the pins;
- Branches A and B;
- the not-covered list.

r2 is no longer signed.
