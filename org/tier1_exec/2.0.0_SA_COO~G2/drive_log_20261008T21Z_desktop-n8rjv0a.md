# /canonical-drive IRPT_YCDGEN -- 2.0.0_SA_COO~G2 on dell2, 2026-10-08 19:4x-22:2xZ

## F1 svc release (ledger irpt-ycdgen-f1-svc-20261008)
- 19:4x-20:5xZ laptop applies: step D 18:55Z, cell D2 leg A 20:29:25Z (SendCommand), leg B shell window OPEN 20:49:58Z (F1 host only, hard close 06:00Z). Before-notice for the three host sends answered YES by laptop CTO 107186; CTO~DELL2 GO msg 1571.
- 20:53Z P1 read-only (SSM fbce151c): st24, andrew only, queue 0/0. 20:54Z D2 attempt 1 refused at the fetch (host role lacks s3:GetObjectVersion; nothing moved); wrapper re-pointed to fetch by key (sha256 binds). 20:55Z D2 (SSM 959fadc3) rc 0, st25 live; V1 PASS (svc=OPAL, other=YCHARTS). Evidence @472bed6100.
- Secret reader: laptop ADD 21:01Z rolled back (AWS reordered the Principal array); laptop ~C ruled set-compare (this seat's rec); retry ADD 21:04:07Z verified.
- 21:10Z F1 ran as svc through CloudFront (Andrew "just go ahead" at the dell2 terminal): login 200, upload NORMALIZED, submit QUEUED REQ-8966d24f.... The resident refused on the Opal path at 21:10:31Z: retained_for_retry class=LayoutRefused. Cause measured: no brand*.json in the root, no IRPT_BRAND_SPEC/IRPT_OPAL_LOGO; layout_overview._asset_path finds the asset only via git roots or env. Row IRPT_YCDGEN-D2-S3 @537c36c037; YCharts markers 0 of 40 journal lines. Leg F1 closed as a FINDING.
- Own defect, corrected: the first run read status with the client request id (INVALID_INPUT); the --read re-poll by the server id was a SECOND secret read (21:11:33Z), reported late as a correction to MSTR; re-poll read QUEUED/ANALYSIS_QUEUED for ~20 min, then 401 on token expiry.
- CTO~DELL2 ruling 1664: reader off now (REMOVED 21:27:47Z, verified by simulation), st25 kept until the retained message dead-letters (an st24 retry would route svc to YCHARTS), then X1+V2. The 22:05Z one-shot was cancelled.

## Next cell
- CTO~DELL2 ruling 1717 on this seat's rec: YCD-w-6, brand.json (03_extract_brand_spec.py) + the laptop's byte-exact logo under ycharts/research/brand/, _asset_path packaged-first. Issued @ece534127f (addendum M; risk WORLD, the gate's floor for an infra path). Laptop logo committed LOCAL @6d71a05c62 (sha256 02477c76..., 3853 B), not yet reachable from dell2; the worker spawns when it is.

## Rules received
- Workers run Sonnet 5.5: spawn only as worker / worker-light, no model override (MSTR 1670); the definitions' YAML broke and was fixed 846cbbe61e (MSTR 1771).
- dep_stage flips regenerate org/projects/<CODE>.json in the same commit (CTO 1699).
- dell2 deploys go to 0.7.0_AE_CloudOps~DELL2 (Andrew ~22:0xZ, MSTR 1753); the shared tree is on box/dell2 since 20:00:46Z (MSTR 1527).

## tick 90 -- ~22:24Z
lease FULL. L7 round 6 | w-6 issued, worker waits on the logo commit | thread n (F1 FINDING D2-S3) | NO-OP: the logo commit is not reachable; the retained message is on its last receive.

## Compiler Tools
- comp-find / comp-which: none this window (reads were exact files and host reads over SSM).
- Rail: one remote host script misread as a repo search; re-run with the audited marker.
