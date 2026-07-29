# DEPLOY LEDGER: etfs-reports orchestrator -- CSV-attach + email_qa mode

**Opened:** 2026-07-29T03:00Z by 0.7.0_AE_CloudOps~A
**Status:** CLOSED 2026-07-29T03:16Z -- deploy complete, verified, QA-exercised, fixtures cleaned.

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

## Execution record (all times 2026-07-29Z)
1. **Commit-before-apply (Rule 2):** patch applied to tree, commit-gate PASS (py_compile +
   ds-precommit + ruff), safe-commit `68661972ab` (lambda_function.py + this ledger).
2. **Targeted plan** (`-target=aws_lambda_function.orchestrator`, saved .build/csvqa.tfplan):
   EXACTLY ONE resource -- aws_lambda_function.orchestrator update-in-place; source_code_hash
   `yjOnWLNAQZlQ9X1TzsMU88X710dIbZx+WwCEXkIdDHI=` -> `jfMnlSE2VocFe7kN9uxhx35iU3JLev5flYOJKW9OE+I=`;
   0 add / 1 change / 0 destroy. **COO line-by-line condition (030048Z) satisfied: no resource
   beyond the CSV+email_qa lambda; NOTHING from mdpf-pipeline (separate module/state; verified in
   the plan text, not assumed). CTO 030027Z reminder answered by the same read.**
3. **safe-apply** (HALTGT checkpoint passed; saved-plan apply): `Apply complete! 0 added, 1
   changed, 0 destroyed.`
4. **Applied truth (Rule 22a):** live `get-function-configuration` CodeSha256 ==
   `jfMnlSE2VocFe7kN9uxhx35iU3JLev5flYOJKW9OE+I=` (byte-equal to plan hash), LastModified
   2026-07-29T03:09:32Z.
5. **0-diff:** full untargeted plan -> `No changes. Your infrastructure matches the configuration.`
6. **QA exercise (CTO conditions 1+2), on the DEPLOYED runtime:**
   - Fixtures seeded: `platinum/reports/9999-qa/{etf_ownership.pdf, opaletfs_qafirm1_999901.csv,
     opaletfs_qafirm2_999901.csv, opaletfs_qafirm3_999901.csv}` (synthetic, 26-63 bytes).
   - Invoke `{"mode":"email_qa","month":"9999-qa"}` -> 200, attachments =
     `[opal_etf_ownership_9999-qa.pdf, opaletfs_qafirm1_999901.csv, opaletfs_qafirm2_999901.csv,
     opaletfs_qafirm3_999901.csv]` -- **expected set == returned set, BOTH DIRECTIONS (4/4, no
     extras, none missing). Attach path proven pre-Aug-1.**
   - Invoke `{"mode":"email_qa","month":"2026-06"}` (real data, read-only) -> 200, attachments =
     `[opal_etf_ownership_2026-06.pdf]` -- **zero-CSV branch proven: PDF-only, matching the true
     June state (write_month_csvs has never fired).**
   - No email sent by either invoke (send-free by call-graph: the ses call site is unreachable
     from the email_qa dispatch).
   - **Fixture DELETION (disclosed per CTO condition 2):** all four keys above deleted 03:14Z;
     residual `aws s3 ls platinum/reports/9999-qa/` = EMPTY (rc=1 no-such-prefix).
7. **Tag:** `etfs-reports-v1.1.0` annotated + pushed `--follow-tags`. DISCLOSURE: this is the
   module's FIRST tag -- the 06-25 creation deploy was never tagged (Known-Issues class, same as
   portal-notifications); v1.1.0 chosen to leave v1.0.0 semantically for the creation state.
8. **Reports:** window report to CTO + COO + DS~A same session; broadcast trail 025955Z/025959Z/030003Z.

## Residuals / follow-ups (none blocking)
- Aug 1 10:00 ET production fire remains the production acceptance (first full-chain exercise incl.
  renderer-side write_month_csvs -- DS/DE lane risk line, CTO flagged to DS~A in AVGCAP plan).
- email_qa mode is manual-invoke only; never scheduled (by design).
- MDPF 4c apply NOT part of this deploy -- stays post-17:15Z per CTO standing ruling.
