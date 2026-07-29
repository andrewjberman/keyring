# DEPLOY LEDGER: etfs-reports orchestrator -- CSV-attach + email_qa mode

**Opened:** 2026-07-29T03:00Z by 0.7.0_AE_CloudOps~A
**Status:** OPEN -- deploy in progress. Unclosed at session end = COO alarm.

## Authorization chain
- Andrew-direct 2026-07-29 ~0135Z (via DS~A terminal, recorded + broadcast): month-end ETFS report
  email must carry the per-firm CSVs, not only the PDF.
- Patch authored by 0.4.0_DS_ClientPlatform~A @17bcbff520; blocked from their lane by owned-paths
  (correct); handed to AE.
- CTO gate ruling 20260729T022305Z: APPROVED post-freeze window, deadline Aug 1 10:00 ET.
- CTO ruling 024911Z: email_qa mode RULED IN, two conditions (structurally send-free; fixture
  discipline w/ disclosed deletion). Ratified as authored at 86 lines, 025334Z.
- **ANDREW-DIRECT 2026-07-29 ~0253-0254Z, at the 0.7.0_AE_CloudOps~A terminal, VERBATIM:**
  *"Ok so did you run the terraform apply or no? Is this thing properly deployed or no?"* -- then,
  after status (not applied, staged @4f4de0a438, freeze holds) + offer that his word overrides:
  *"Yes run it now"* -- and, during execution: *"WE dont leave half deployed work"* / *"this is a
  major anti pattern"* (drive-to-full-completion reinforcement).
  Broadcast to CTO 025955Z / COO 025959Z / MSTR 030003Z. This ledger is the durable record.
- Scope note: this GO covers the ETFS deploy ONLY. The MDPF 4c apply stays post-17:15Z per CTO.

## Change
- File: `infra/aws/lambda/etfs-reports-orchestrator/lambda_function.py` (ONLY file; TF zips it
  inline via data.archive_file -- no S3 artifact leg, no IAM change, no schedule change).
- Content: (1) `_month_csv_keys` -- enumerate `platinum/reports/{month}/*.csv` from S3;
  (2) `_build_report_email` builder split (build-only, no send) + `_email_report` = builder + the
  ONE `ses.send_raw_email` call site; CSVs attached as text/csv; zero-CSV month disclosed in body;
  (3) `email_qa` handler mode -- send-free by call-graph (no ses/ec2/ssm reachable), returns the
  built MIME's attachment filename list; manual invoke only, never scheduled.
- Staged deliverable: `org/tier2_senior/0.7.0_AE_CloudOps/deliverables/etfs_reports_email_csv_attach_plus_email_qa_20260729.patch` @4f4de0a438.
- Baseline (pre-apply, live-grounded 024xZ): CodeSha256 `yjOnWLNAQZlQ9X1TzsMU88X710dIbZx+WwCEXkIdDHI=`,
  LastModified 2026-06-25T23:36Z (first code change to this Lambda).

## Planned sequence (Rule 2 + cloud-ops pre-flight)
patch apply -> commit-gate -> safe-commit -> targeted plan (aws_lambda_function.orchestrator) ->
safe-apply -> applied-truth CodeSha256 (!= baseline, == new archive hash) -> 0-diff plan -> tag
etfs-reports-v{next} -> push --follow-tags -> QA: seed platinum/reports/9999-qa/ (synthetic PDF +
3 CSVs) -> invoke email_qa month=9999-qa (expect exactly the 4 fixture filenames, both directions)
-> invoke email_qa month=2026-06 (real data: expect PDF-only + zero CSVs, proves disclosure branch)
-> DELETE the 9999-qa fixtures (keys listed below on execution) -> ledger CLOSE + reports.

## Execution record
- (appended as executed)
