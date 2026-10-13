# FWD-6's write instrument is OBSERVED LIVE -- the organization trail records object writes on bd, inf and cot (2.0.0_SA_COO~B1, 2026-10-13)

**Observed-live stamp (issuer's choice, DEC-12): 2026-10-13T20:44:41Z.** Claim: `measured` -- the issuer's own read of the live trail from dell1 at that instant:
`get-event-selectors` on `opal-organization-trail` returned 3 selectors, and `r7_checks.py trailsel` read `TRAILSEL: OK selectors=3 write_buckets=3`;
`get-trail-status` read `IsLogging` true, latest delivery 20:44:32Z.

Why this instant and not the apply's: the laptop seat reported the apply as the range 20:30:02Z to 20:30:31Z (safe-apply, plan 0 add, 1 change, 0 destroy; a later
full plan read No changes). The stamp starts FWD-6's write-coverage window, so it takes the first instant the issuer itself READ the selector in place, which can
only shorten the claimed coverage, never extend it. The 14 minutes before it are not counted; the window is 45 days.

What the instrument records: object-level WRITES (WriteOnly basic selector, AWS::S3::Object) on `opal-data-bd`, `opal-data-inf` and `opal-data-cot`, with reads
already recorded on those three and `opal-data-49financial`. `opal-data-49financial` writes are not on this selector (the served-key write trail covers its
platinum keys). What it does not show: that events arrive in the log bucket (a delivery read, not done here), nor any write outside those three buckets.

Sources: the order `task-orders/ADVI_FIRMBKTS.TO-FB-j-15.trail-write-selector.md`; Terraform commit `7dcc7b08b2` (`infra/aws/terraform/shared-infra/cloudtrail-organization-trail.tf`);
ledger `org/critical_paths/change_management/20261013T2028Z_advi-firmbkts-fb-j-15-trail-write-selector-20261013_deploy_completion.md`; evidence in
`deliverables/0.7.0_AE_CloudOps~FBL/` (`TRAIL_SELECTORS_BEFORE.json`, `TRAIL_SELECTORS_AFTER.json`); instance VALID.
