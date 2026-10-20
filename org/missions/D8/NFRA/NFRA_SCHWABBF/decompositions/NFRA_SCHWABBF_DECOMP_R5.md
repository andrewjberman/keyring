# NFRA_SCHWABBF decomposition -- ROUND 5 (2026-10-20, issuer 2.0.0_SA_COO~SB): meta and `_ops` as the builder's state tier, in the firm bucket

Cut on the CTO's go (msgs 109961, 109964, 109966, 109970), PRD v1.0 @cb8f734709 (ADMITTED) and the CTO's ruling on rolling objects (msg 109970), in parallel with round 4 (silver). Andrew-direct ~17:0xZ, verbatim: "a, yes. this needs to go through the same full bronze/silver process that the other masters go through." and ~16:3xZ: "I dont care about that 0824, I want the new Cottonwood accounts taken care of and the 0840 tax sma account sorted out."
**The cutover is ONE act across every tier: no data moves until rounds 4 and 5 are both merged and the gateway edit is ready.**

## The state contract (fixed here; every cell builds against it)

`meta/` and `_ops/` become the builder's `state` tier (PRD v1.0, on the CRO's msg 109963). For a FIRM-FORM master M (08403355 under `49financial`; 08719286, 08134043, 08165601, 08480305 under `cottonwood`) with firm F, the object lives at `address('schwab', F, 'state', <table>, 'date=YYYY-MM-DD')` plus `/` plus a file name that starts with `{M}.`. The bucket is the FIRM bucket the builder returns: `s3://opal-data-49financial/schwab/49financial/state/...`; `s3://opal-data-cottonwood/schwab/cottonwood/state/...` (measured ~17:3xZ; bronze and silver stay in `opal-data-assets`). Mapping of 08403355's objects (counts measured 2026-10-20 ~17:4xZ: 6,898 under `meta/`, 32 under `_ops/`):

| today (`s3://opal-data-assets/schwab/08403355/...`) | state table | new key (`date=` and file name) |
|---|---|---|
| `meta/complete/date=D.json` | `complete` | `date=D/08403355.complete.json` (D = the business date) |
| `meta/conversions/{run_id}.json` (run id `YYYYMMDDTHHMMSSZ-xxxxxxxx`) | `conversions` | `date={UTC date of the run id}/08403355.{run_id}.json` |
| `meta/pulls/{RUNID}.json` (`YYYYMMDDTHHMMSSZ`) | `pulls` | `date={UTC date of RUNID}/08403355.{RUNID}.json` |
| `_ops/daily_pull/runs/{RUNID}.json` | `daily_pull` | `date={UTC date of RUNID}/08403355.{RUNID}.json` |
| `_ops/daily_pull/last_run.json` (ROLLING) | `daily_pull` | `date={UTC date of the write}/08403355.last_run.json` |
| `meta/backfill-status.json` (ROLLING) | `backfill_status` | `date={UTC date of the write}/08403355.backfill-status.json` |

Rolling objects (CTO ruling, msg 109970): readers take the NEWEST partition at or before today. No fixed sentinel date. The shared backfill-status writer module switches per master like C-KEYFORM; **every other family and every other master keeps its current key byte-for-byte**.
Old-form masters (08242234, 08335338): unchanged, `meta/` and `_ops/` stay in `opal-data-assets` under their master folder.
The completion markers' notification: the existing S3 notification on `schwab/08335338/meta/complete/` (`silver.tf` ~811-820, 0833's dispatcher) is 0833's and is not touched; 0840's markers have no notification today.

## The rectangle (round 5)

| cell | item | PRD rows | outcome | status | placement | risk | worker_class | depends on |
|---|---|---|---|---|---|---|---|---|
| `BF-p-5` | the converter family writes the completion marker, the conversion manifest and the backfill status for firm-form masters to the state tier in the firm bucket (code, twins, tests) | C-TIERS v1.0 | FWD-1, FWD-6 | NOT-EVALUATED | laptop | WORLD (`infra/` floor; nothing deployed) | worker | -- |
| `BF-v-5` | the puller writes its run records and last_run for 0840 to the state tier in the firm bucket | C-TIERS v1.0, C-DAILY | FWD-6 | NOT-EVALUATED | laptop | WORLD (`infra/` floor; nothing deployed) | worker | -- |
| `BF-x-5` | the move tool gains the state tier for 08403355 (cross-bucket copy with rename, sha-verified) | C-TIERS v1.0, C-MOVE | FWD-4 | NOT-EVALUATED | laptop | LOCAL | worker | -- |
| `BF-g-5` | IAM text: the box role and the converter role may write the firm bucket's state prefix, enumerated per master (Terraform text only) | C-TIERS v1.0, C-ALONGSIDE (IAM shape) | FWD-1, FWD-6, FWD-8 | NOT-EVALUATED | laptop | WORLD (`infra/` floor; nothing applied) | worker | -- |

Not in this rectangle: the gateway side (`2.0.0_SA_COO~O` owns it; named to them: `completion_prefixes` and `family_depth.py` move to the firm bucket and the newest-partition read); the Alongside box (`~SA`); the CVO/gateway date message; the release acts, re-cut after rounds 4 and 5 merge.

**Chains (M = 4; fan-out 4 of 4, cap 8).** P (slot ~1), V (~2), X (~3), G (~4): no edges. Round 4 has drained, so the slots are free.

**Write sets (disjoint).**
- BF-p-5: `data/assets/scripts/silver/conversion_manifest.py`, `data/assets/scripts/silver/schwab_runtime.py`, `data/assets/scripts/lib/backfill_status.py` (the shared writer: CTO msg 109970 condition 1 asks it to switch per master), the five vendored twins of `backfill_status.py` (schwab, etf, eclipse, orion, blackdiamond Lambda dirs, so every Lambda directory equals the source), the two Schwab twins of `conversion_manifest.py` and `schwab_runtime.py`, `data/assets/scripts/lib/tests/test_backfill_status.py`, `data/assets/scripts/silver/tests/test_schwab_state_firm_key.py` (new). Round 4 has merged, so `conversion_manifest.py` already carries the silver rule.
- BF-v-5: `infra/aws/ec2/canonical-schwab-si2/sdd-daily-pull.ps1`, `data/canonical/schwab/tests/test_sdd_daily_pull_state.py` (new).
- BF-x-5: `data/canonical/schwab/keyform/move_bronze_key_form.py`, `data/canonical/schwab/tests/test_move_bronze_key_form.py`, `data/canonical/schwab/tests/fixtures/move_listing_state.json` (new).
- BF-g-5: `infra/aws/terraform/canonical-schwab-ec2/monolith-iam.tf`, `infra/aws/terraform/opal-assets/silver.tf`, `data/canonical/schwab/tests/test_firm_prefix_grants.py`.
- **Overlaps with round 4:** `conversion_manifest.py`, `move_bronze_key_form.py` and its test, `silver.tf` and `test_firm_prefix_grants.py` were edited in round 4; round 4 merged before this issuance (cdce7d6d13, f6078a5d99, 16d4ae3ea0), so each round-5 cell starts from the merged code and no two workers edit one file.

## AMENDMENT 1 (2026-10-20 ~19:2xZ, issuer 2.0.0_SA_COO~SB; surprise row `NFRA_SCHWABBF-W4-S9`): the fence cell `BF-h-5`

Worker `~4` read the firm buckets' own policies at the cell: each carries `DenyForeignFirmPrincipals` (Deny `s3:*` to every principal outside the firm's fence patterns and the registry's exemption rows), and neither the box role (`quartz-si2-spike-role`) nor the converter role (`opal-assets-silver-schwab-role`) is in either. So the identity-side grants of `BF-g-5` alone leave every state write refused. The issuer rules inside its own decomposition: ONE cell is added. The precedent is the scoped exemption row (`opal-clientops-ews-role`, `schwab/49financial/state/ews_store/current/`).

| cell | item | PRD rows | outcome | status | placement | risk | worker_class | depends on |
|---|---|---|---|---|---|---|---|---|
| `BF-h-5` | registry text: scoped exemption rows in `infra/logic/registry/exemptions.json` so the box role and the converter role pass the firm buckets' fence for the state prefixes only (text; nothing applied) | C-TIERS v1.0, C-ALONGSIDE (IAM shape) | FWD-1, FWD-6, FWD-8 | NOT-EVALUATED | laptop | WORLD (`infra/` floor; nothing applied) | worker | `BF-g-5` (merged) |

Write set: `infra/logic/registry/exemptions.json`, `data/canonical/schwab/tests/test_fence_state_rows.py` (new). Chain: one (slot `~4`, re-seated). The apply is the CloudOps lane's act under `safe-apply` after the never-widen pair (COO half: `ledger/NEVER_WIDEN_BF5_STATE_FENCE_COO_HALF.md`; the CTO half is owed).

## Rule 24 record (the cell set is a schema)

- **MECE over a declared domain.** Domain: the writers, movers and permissions of the `meta/` and `_ops/` trees of the in-scope masters (census 2026-10-20: writers = the converter family (completion marker, conversion manifest, backfill status), the puller (pull record, run record, last_run); mover = the move tool; permission = the box role and the converter role; readers outside this repo = the gateway (`family_depth.py`, `completion_prefixes`), `2.0.0_SA_COO~O`'s) = four cells plus the gateway. Remainder: none.
- **Same grain. Intent coherence. State coherence.** One cell per write set; none writes to S3, applies Terraform, deletes, deploys, or contacts Schwab.

## Battery (round 5)

- `comp-schedule`: DECLARED-NOT-APPLICABLE. The pull-fire times (09:45, 10:15, 10:45, 21:45, 22:15, 22:45Z) are inlined into BF-v-5.
- `comp-iam`: RUN. Denominator: `monolith-iam.tf` (the box role: `_ops` and `meta/pulls` grants for the three masters at ~86-90) and `silver.tf` (the converter write grant at ~372-420 scopes `meta/` per master in `opal-data-assets` only), 2 Terraform files, and the FIRM buckets `opal-data-49financial` and `opal-data-cottonwood`, whose own policies were NOT read (blind). Neither role can write the firm bucket today: a firm-form conversion's completion marker and a pull's run record would be refused at their first write. The live IAM plane: 0 roles read.
- `comp-adversary`: DECLARED-NOT-APPLICABLE as a lens run. Findings inlined: (1) state moves to a DIFFERENT BUCKET, so every client call that wrote `MONOLITH_BUCKET` for meta needs a bucket argument per master; (2) the backfill-status writer is shared with other families, so the per-master switch must not touch their keys; (3) the rolling objects take the write date, so a reader that wants "the latest" lists and takes the newest partition; (4) a conversion manifest or marker written at the old key after the cutover would be a second form (FWD-4): the converter's meta writes switch in the same release; (5) the existing 0833 notification on `meta/complete/` must not be edited.

## Not in round 5

The gateway edit; the Cottonwood puller and box (`~SA`); the date message; the release acts; the 0840 backfill and held-days record.
