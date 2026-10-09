# Never-widen COO half: partner_roster T-1 correction into its two live readers (CTO~DELL1 ruling 1296, option (a))

**Author:** `2.0.0_SA_COO~G1` (dell1), 2026-10-09 ~01:0xZ. **For:** `1.0.0_SA_CTO~DELL1` (ruling msg 1296) and the laptop
`1.0.0_SA_CTO` re-signature (relayed by `0.0.0_AB_MSTR~DELL1`; the laptop half @21a5ceab0f covered the old key).
**Executor:** `0.7.0_AE_CloudOps~DELL1`. No IAM is touched (Step F conditions of msgs 1245/1255 carried, nothing to report).
**Status:** COO half SIGNED for legs A and B below, on the pre-check conditions stated. The deprecated loose key
`s3://opal-data-mdpf/code/scripts/gold/partner_roster.json` is NOT touched.

Superseded text: v1 of this file (@0a875b3c7d) declined the loose-key act.

## Correction to the ruling's mechanism

Ruling 1296 says to fix the emitter "via the bundle re-mint". The bundle does not reach the emitter:

- `bundles.accrual_bridge` feeds `mdpf-accrual-trigger` (`.tools/safe_deploy_core.py:245-262`).
- The emitter reads `partner_roster.json` from its own Lambda package (`channel_sources.py:123-130`), built from
  `infra/aws/lambda/opal-assets/opal-assets-daily-emitter/`.

The ruling's intent (the fix goes where the emitter reads) therefore needs **two legs**. A carries the bundle re-mint the ruling
names. B is the emitter fix the acceptance grades.

## Measured (2026-10-09 00:2xZ-00:5xZ)

| surface | live | HEAD |
|---|---|---|
| authority `data/mdpf/config/partner_roster.json` | -- | blob eb3bff48c8, md5 3d309b26, sha256 4c104d9b.. (LF) |
| bundle `s3://opal-data-assets/portal/gold/mdpf/_code/mdpf-accrual-bridge.tar.gz` | version BtC_0xCV5wIH1yJmIYw1XdDVh5UN_YC6 (2026-08-11T08:41:37Z); roster-authority-sha256 e86e4631..; script-sha256 648cf3f5.. | roster 4c104d9b..; script 648cf3f5.. (unchanged) |
| emitter Lambda `opal-assets-daily-emitter` | CodeSha256 n/Tu1ns1eNl1vLBiR29ZttXGVjuzz5DAsjV5gBut/2k=, LastModified 2026-08-11T01:28:40Z; artifact `s3://opal-313476888478-lambda-artifacts/opal-assets/opal-assets-daily-emitter.zip` version LEBxFtsuAQOsw4xcjeDepTZrRCj9CWAt (2026-08-11T01:18:24Z), no aliases | vendored roster md5 a22fc62b (07-28 bytes) |

Roster delta, live vs HEAD: 14 JSON differences. Two are values: Cottonwood `bd_holdings_s2` and `bd_allocations_s2` `cadence`
D+2 -> T-1. The rest are description, provenance and evidence text, plus two `cadence_corrected` blocks.
`gate_policy.per_partner_max_lag_trading_days.cottonwood` is unchanged (3).

**Widening hazard on the emitter (pre-check B0 exists for this):** four emitter commits are newer than the live code and were
never deployed: ae106b1124 and aaf2be288f (08-26), 650df7371e (09-21), 85dd7adc26 (10-01, Cottonwood custom models). A build
from HEAD ships all four. This half does NOT cover them.

## Writers counted

| property | writers | rule read |
|---|---|---|
| the bundle object | 1: the safe-deploy in-flow mint | `safe_deploy_core.py` bundles map (whole-bundle republish, sha-stamped metadata) |
| the emitter's code | 1: Terraform (`safe-apply -target` on the emitter's module in `infra/aws/terraform/opal-assets`) | targeted plan must read code hash only |
| Cottonwood emitter row labels | 1: `channel_sources.accept_date` (`:164-196`) | read below |
| accrual output's roster stamp | 1: `build_portal_gold_accrual.py` | reads no `cadence` (0 reads); stamps the roster sha |

## Leg A -- re-mint `bundles.accrual_bridge` from HEAD

- Act: the safe-deploy in-flow mint from HEAD (LF bytes). Members: the roster (changes) and `build_portal_gold_accrual.py`
  (sha 648cf3f5.., identical, so it does not change).
- Verify: new version's metadata `roster-authority-sha256` = 4c104d9b.. (full value from `git show HEAD:<path> | sha256sum`) and
  `script-sha256` = 648cf3f5.. unchanged.
- Expected outcome, from the reader's rule: the accrual build reads no cadence. Served value delta 0; the output's
  `partner_roster_sha256` stamp changes at the next accrual run. Both branches: mint lands -> the stamp changes and nothing else;
  mint fails -> the old version stays served (no partial state: one object).
- Rollback: re-point to version BtC_0xCV5wIH1yJmIYw1XdDVh5UN_YC6 (copy it over the key).

## Leg B -- the emitter's vendored roster

- **B0 pre-check (positive control, no write):** find the commit whose `BUILD_ONLY` build of the emitter reproduces the live
  CodeSha256 n/Tu1ns1.. (start at 9abdfa4c30, 2026-08-11T01:16Z). **If no commit reproduces it, leg B stops here** and returns to
  this seat. A build whose input is not the live tree plus the roster is not covered.
- **B1 build input:** the tree at the B0 commit with ONLY `partner_roster.json` replaced by `git show HEAD:data/mdpf/config/partner_roster.json`
  (LF). Verify the package's roster md5 = 3d309b26 and that every other member's hash equals the B0 build. Do not commit the
  re-vendored file onto the emitter directory at HEAD in a way a later HEAD build reads as "deployed": the repo copy is updated
  by its own commit, and the four undeployed commits stay undeployed. The ledger names this pin.
- **B2 activation:** upload the artifact; targeted plan reads code hash and object version only (0/1/0); `safe-apply -target`;
  `get-function-configuration` CodeSha256 = the B1 build.
- **Expected outcome, from `accept_date`'s rule.** Acceptance is `raw_lag <= max_lag`. For Cottonwood, max_lag stays 3, so
  **which partitions are accepted or refused does not change, and no row value changes.** What changes on Cottonwood rows:
  `declared_cadence` D+2 -> T-1, and `cadence_normalized_lag_td = max(0, raw_lag - offset)` with offset 2 -> 1:

  | raw lag (td) | before: norm, state | after: norm, state |
  |---|---|---|
  | 0 or 1 | 0, at_declared_cadence | 0, at_declared_cadence |
  | 2 (one missed day) | 0, at_declared_cadence | **1, within_slip_tolerance** |
  | 3 | 1, within_slip_tolerance | 2, within_slip_tolerance |
  | 4+ | refused | refused |

  Branches: B2 lands -> the labels above, nothing else; B2 fails -> the live code stays (one function, no partial state).
- **Not moved by this act (state coherence):** the Cottonwood window stays 3. Under T-1 the cadence+slip convention reads 2;
  changing it is a roster value change, not in scope.
- **Acceptance (ruling 1296):** (1) the deployed package's `partner_roster.json` reads `cadence` T-1 on both Cottonwood feeds;
  (2) a seeded missed Cottonwood day computes lag > 0: `accept_date` from the deployed package, with dates whose newest partition is
  2 trading days behind run_date, returns `cadence_normalized_lag_td` 1 and `within_slip_tolerance` (and 0 /
  `at_declared_cadence` on the B0 build, as the negative arm); (3) the next scheduled emitter run's Cottonwood rows read
  `declared_cadence` T-1.
- **Rollback:** re-point the function to artifact version LEBxFtsuAQOsw4xcjeDepTZrRCj9CWAt (CodeSha256 n/Tu1ns1..) by
  targeted apply.

## Ledger

One ledger, legs A1 mint, A2 verify, B0 control, B1 build, B2 apply, B3 verify, B4 next-run read. Opened by the executor at start.
