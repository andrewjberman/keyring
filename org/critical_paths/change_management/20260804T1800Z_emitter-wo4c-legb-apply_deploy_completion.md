# Deploy-completion ledger: opal-assets-daily-emitter -- WO-4c + Leg B (ONE apply, split-in-time)

**Opened:** 2026-08-04T18:00Z by 0.7.0_AE_CloudOps
**Status:** CLOSED 2026-08-04T18:04Z -- all legs proven, nothing stranded
**Authority:** CTO split-in-time ruling 044318Z (ONE post-17:15Z emitter apply carrying WO-4c + Leg B,
cross-citing); WO-4c deploy freeze condition VERIFIED discharged (today's 17:15Z emitter fire ran
17:15:17Z, log-stream grounded, apply began after).

## Payload (both legs in the one artifact)

- **WO-4c** (@ad641d1960 + @6da43f1c6c, committed last night under the CTO deploy freeze):
  roster-declared cadence acceptance in the emitter; acceptance window = roster gate_policy
  per-partner max_lag (offset-0 basis).
- **Leg B** (@bf502e3c4, this session): cot_total relationship-grain collapse (vendored DC1
  collapse + binding equality assert). Battery: dual-day 07-30 delta ties DC1's 205,070.77 to the
  cent; clean-day control identical; unequal/NaN/equal-pair refusal legs exercised; tests 59/59.
- Source-map parity rider: walk_daily_aua.py registered (@ this session's map fix commit) --
  build gate ADHC_DRIFTD.002 refused until registered.

## Legs

| # | leg | evidence | status |
|---|---|---|---|
| L1 | artifact build+upload (build-and-upload.sh opal-assets opal-assets-daily-emitter) | rc=0; S3 opal-assets/opal-assets-daily-emitter.zip new version + content-sha256 metadata | DONE |
| L2 | tf plan -target=module.emitter | 0/1/0 in-place: s3_object_version mjr9ZaKM->eITd_Zed, source_code_hash H6bq4C2w->oV2seRZK (exactly the artifact flip, nothing else) | DONE |
| L3 | safe-apply targeted | "0 added, 1 changed, 0 destroyed" | DONE |
| L4 | 0-diff replan | "No changes. Your infrastructure matches the configuration." | DONE |
| L5 | live CodeSha256 == planned hash | get-function-configuration: oV2seRZKxW/gWSZ8DqnPgO+xlMhEygjfkpt1rhflsZQ= EQUAL; LastModified 2026-08-04T18:01:55Z | DONE |
| L6 | tag opal-assets-v0.37.0 + MSTR push request | annotated tag on the ledger commit; push rides the integrator sweep | DONE |

**Deliberately NOT ridden:** the opal-assets root's other found-unapplied work (mirror_cot ET
migration, bd49f_reporting_io) -- other seats' items, surfaced 08-04 morning triage, owners to claim.
