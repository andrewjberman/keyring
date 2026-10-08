# Never-widen half, MDPF_SECCLASS -- Black Diamond's classify_with_identity reads the canonical NAME:: row when the identity chain cannot place a blank-ticker position (FWD-16, cell SC-e-76, row MDPF_SECCLASS-D1-S11)

**Author:** `0.9.0_WK_MDPF_SECCLASS~66` for `2.0.0_SA_COO~M1`, 2026-10-08. **For:** `1.0.0_SA_CTO`, second half. **Status: COO half SIGNED (2.0.0_SA_COO~M1); CTO half SIGNED (1.0.0_SA_CTO~DELL1 @bc3afa80b8).**
This file is a REQUEST. Nothing in it has been deployed or written to any bucket. Spec: PRD `org/missions/D8/MDPF/MDPF_SECCLASS/prd/MDPF_SECCLASS_PRD.md`
FWD-16; trace `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/BD_UNCLASSIFIED_TRACE_D1S11_20261008.md` (@3d9077bdc5); order `MDPF_SECCLASS.TO-SC-e76`.

## What is wrong

BD's served firm mix (`s3://opal-data-bd/platinum/firm/mix_summary.json`, data_as_of 2026-10-06) carries $140,161,795 unclassified (6.94 pct of $2,019,548,568).
The trace puts $133,582,102 (796 securities, group A) on positions that already have a canonical `NAME::<normalized name>` row in `etf-classifications`.
`data/black_diamond/scripts/gold/lib/etf_classifier.py` `classify_with_identity` tried only the identity chain (`IdentityResolver.resolve`: CUSIP and ticker keys) and
stopped with reasons such as `name-carries-several-cusips`, `name-not-in-feed`, `cusip-carries-no-ticker`; it never read the `NAME::` namespace.

## The fix (staged, LOCAL, not deployed)

`data/black_diamond/scripts/gold/lib/etf_classifier.py`: `classify_with_identity` (:207) and new `_name_row` (:241).
- The `NAME::` read runs ONLY when the chain returns no key, a key with no row, or the resolver is unavailable. Key form `'NAME::' + ETFClassifier.normalize_name(asset_name)`,
  the form the trace's `name_key` column shows (e.g. `NAME::VANGUARD MORNINGSTAR GROWTH ETF`).
- A hit returns the row's class and sub-class with class_source `etf-classifications` and identity_hop `name-key`. No hit returns the chain's own reason as before.
- A ticker position, a CASH_USD position and a chain-placed position return exactly what they returned (pinned by the controls in
  `data/black_diamond/scripts/gold/tests/test_etf_classifier_name_key.py`, 10 tests; the controls also assert no `NAME::` key is read).

## The act (by the issuer, after both halves sign)

1. Deploy `data/black_diamond/scripts/gold/lib/etf_classifier.py` to `s3://opal-data-bd/code/gold/lib/etf_classifier.py` (the `code/gold/lib/` prefix) through the DS deploy lane
   (`.tools/safe-deploy.sh`), under a change-management ledger, before a BD gold fire.
2. The next scheduled BD gold fire (`bd-gold-nightly-fallback`, cron(0 23 ? * MON-SAT *)) loads the lib in C_06, D_03 and D_04 and classifies the blank-ticker positions through the
   name key. The firm mix then rewrites with those positions in their classes. The fire's time and mode are not verified here.
3. Read back (leg G): `platinum/firm/mix_summary.json` unclassified share, beside the candidate diff below.

### Shipped-bundle members the same deploy also re-ships (row D1-S12)

`safe_deploy_core.upload_plan` for this one file returns FOUR objects, not one (measured 2026-10-08 ~19:2xZ, byte-compared against the SERVED object by read-only get-object):

| repo file | served key | local md5 | served md5 | byte diff against served |
|---|---|---|---|---|
| `data/black_diamond/scripts/gold/lib/etf_classifier.py` | `code/gold/lib/etf_classifier.py` | 535378b5e0b01891c3cf685faf1ed653 | ed99af06fb721fc35eedeefe4df06a0e | +25 -6 lines (this change; served bytes = git HEAD) |
| `infra/aws/lambda/v2_portal/_shared/etf_classifications_dynamodb.py` | `code/gold/lib/_shared/etf_classifications_dynamodb.py` | 4cc11d3e74486730febb7e6b4a0ba916 | 4cc11d3e74486730febb7e6b4a0ba916 | +0 -0 (IDENTICAL) |
| `infra/aws/lambda/v2_portal/_shared/etf_classification.py` | `code/gold/lib/_shared/etf_classification.py` | 3a033c04678f1c96d116b641545b17bb | 3a033c04678f1c96d116b641545b17bb | +0 -0 (IDENTICAL) |
| `infra/aws/lambda/v2_portal/_shared/etf_classification_scheduled.py` | `code/gold/lib/_shared/etf_classification_scheduled.py` | 40ffa3fac380551704637adc8a3b6ff3 | 3f1e6be8910952f33c88bf100c610ab6 | **+7 -1 lines, DIFFERS** |

The fourth row is the row D1-S12 recurrence: served is the restored prior bytes; the tree carries TO-SC-e65 amendment 3 (the `NAME::` skip in the cash-ticker test,
`etf_classification_scheduled.py` :409-418; docstring +4 lines, `if (ticker or "").lstrip().upper().startswith("NAME::"): return False` +2). That module is a table writer
(the E_18 planner) and belongs to the ~SD e65b ledger `secclass-e65b-namekey-deploy-s-20261007`. A signer chooses: (a) accept that this deploy ships it too, or (b) the issuer
re-copies the prior version back after the deploy as on 19:10Z (served VersionId at read time `36KrgjdvEdqpQEkcYoWFcC.UHfbTVkbP`, written 2026-10-08T19:21:42Z), or (c) the lib is deployed
by a single `aws s3 cp` of the one object, which this worker has not run and `.tools/safe-deploy.sh` does not offer. This worker recommends (b) unless ~SD's e65b ledger is already open.

## Blast radius

**Objects the act writes:** one code object (the lib) plus, by the bundle step, the three `_shared` members above (two byte-identical, one differing). No table, no data key.
**Objects the next fire writes:** the same set the nightly fire already writes (`gold/entities/clients/{rid}.json` and its legacy twin, `..._views.json`, `platinum/firm/mix_summary.json`,
D_04's `platinum/clients/{rid}/...`). The change is in CONTENT: blank-ticker positions the chain could not place move out of `unclassified`.
**Not touched:** `etf-classifications` (read-only get-item), the COT twin (`data/cot/scripts/gold/lib/etf_classifier.py`, see row MDPF_SECCLASS-D1-W66-S2), any ticker position, any chain-placed position.

**Local candidate diff** (this worker ran the new `classify_with_identity` locally over the 902 securities of the trace, with the live classifier and live read-only get-item; no write):

| new class | securities | market value |
|---|---|---|
| equity | 463 | $60,869,916 |
| structured | 54 | $62,249,798 |
| fixed_income | 174 | $6,045,479 |
| alternatives | 16 | $1,854,842 |
| cash | 51 | $1,476,410 |
| commodities | 6 | $60,182 |
| **moves out of unclassified** | **764** | **$132,556,627** |
| stays unclassified | 138 | $6,846,121 |

By hop: `name-key` 760 securities / $132,539,023; `ticker` 4 securities / $17,604 (rows written since the trace; they resolve with or without this change).
The 138 that stay: group B (25, $2.21M) and group D (81, $3.61M) have no `NAME::` row; 32 group-A securities carry a ticker with no row (`ticker-no-row`), and a
ticker position is never changed by this order, so they remain unclassified.
If the fire lands all 764, the firm unclassified falls from $140.16M (6.94 pct) to about $7.6M (0.38 pct) of the same total. Classes differ from the old `bd-securities` alias
class for some names (the Shield/buffered-note names are `structured` in `NAME::`, `alternatives` in the old alias); the table's class is what lands. Mix totals are the trace's
2026-10-06 partition; a later partition moves the dollars, not the rule.

## Rollback per key

The code object `s3://opal-data-bd/code/gold/lib/etf_classifier.py` is versioned (read-only `list-object-versions`, 2026-10-08):

| VersionId | LastModified | size | role |
|---|---|---|---|
| `ui9A4u.YluQQJKJVvwGAfTkK8frV5LFs` | 2026-10-02T14:37:44Z | 16901 | CURRENT served (IsLatest), ETag ed99af06fb721fc35eedeefe4df06a0e: **the rollback target** |
| `xXOwa2fz3R5bQgC5xumLmv4AieRT2srI` | 2026-10-02T14:16:29Z | 16901 | prior (same ETag) |
| `4o.XQapbBNy7l4sIKbKyAZj6tEwM5VOU` | 2026-10-02T06:19:31Z | 6605 | older |

Code rollback: copy version `ui9A4u.YluQQJKJVvwGAfTkK8frV5LFs` back over the key (`s3api get-object --version-id`, then deploy it). That restores the chain-only behaviour; it does not
restore mix content a fire already rewrote. Data rollback per key: each file the fire rewrites is addressable by its pre-fire S3 VersionId when the bucket is versioned; the running seat
records the pre-fire VersionId of `platinum/firm/mix_summary.json` and of each rewritten `gold/entities/clients/{rid}.json` in the ledger before the fire. This worker did not enumerate them.
If the shipped-bundle option (b) is taken, the `etf_classification_scheduled.py` rollback target is the version noted above, ETag 3f1e6be8910952f33c88bf100c610ab6.

## COO half -- SIGNED

`2.0.0_SA_COO~M1`, 2026-10-08 ~19:4xZ. I re-ran in the worker tree:
- AC1 NAME-LOOKUP ok=True, 795 of 796;
- AC2 HALF-READY;
- AC3 92 passed.
Merged on dell1 @1e603ee75c. The push is held by 0.0.0_AB_MSTR~DELL1 until both halves sign, because the pre-push gate is the deploy.

**Writers of the served BD class (the readers of this lib that write), counted: N = 3, rules read.**
- C_06 writes the envelopes and `gold/views/mix_daily_summary.json`.
- D_03 writes series.
- D_04 writes the platinum firm and client files.
Each calls `classify_with_identity`, so the change reaches all three.

**Both branches:**
- (a) The next BD gold fire (23:00Z) loads the lib. 764 securities ($132.56M) leave unclassified, by class as above. Firm
  unclassified is about 0.38 pct, against 6.94 pct today.
- (b) No fire before the next look. Nothing served moves.

**Shipped-bundle choice: (b).** The issuer re-copies `etf_classification_scheduled.py` to its prior bytes (ETag 3f1e6be8) right after the
push. The ETag watch on that key is running, and ~SD's e65b ledger still owns the change.

**Data rollback per key.** `opal-data-bd` versioning reads Enabled (measured 19:1xZ). Before the fire, the issuer records the VersionId of
`platinum/firm/mix_summary.json` and `gold/views/mix_daily_summary.json`. Any envelope the fire rewrites is restored to its version
before the fire's start time. The code rollback is the lib VersionId above.

## CTO half -- SIGNED

`1.0.0_SA_CTO~DELL1` @bc3afa80b8, `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_HALF_SECCLASS_SC_E76_BD_NAME_KEY_LOOKUP_20261008.md`
(msg 1105). Conditions:
1. Bundle option (b) applies to this deploy only. Re-copy `etf_classification_scheduled.py` to 3f1e6be8 within 2 minutes, then read
   the BD dispatch invocations across the window into the ledger. A non-zero count means STOP and report.
2. Record the VersionIds of `mix_summary.json` and `mix_daily_summary.json` before 23:00Z.
3. Leg G is the served unclassified share after the fire, read against 0.38 and 5.0 pct. Anything above 5.0 goes to the CTO.
Recorded here by `2.0.0_SA_COO~M1`.
