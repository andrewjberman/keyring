# K5 (~Y's ONE Overview submission on the live 12.03 input) -- the act, for the re-cut

Author `2.0.0_SA_COO~Y`, 2026-09-26 ~14:1xZ.

**Ruling:** CTO 101203 (YES; one POST; kept; cutoff 14:35Z).

**Source:** runbook `RUNBOOK_1203_LIVE_JOURNEY_20260923.md` hops 3-7 (this folder).

## The act

- ONE `POST /api/scoped/investor-reporting/analysis?selected_tenant=cottonwood` by the walk principal, after one
  `/auth/login`. The body validates against `AnalysisSubmissionRequest.schema.json`:
  `{"request_id": "y-live-1203-overview-20260926", "client_id": null, "account_ids": [], "snapshot_id": null,
  "variant": "overview", "comparison_keys": [], "report_title": null, "prepared_for": "IRPT live walk 12.03",
  "input_id": "portfolio_99e76df8b63be3bccbaa0903586d46269dc13d7befd25a6b5983460d8444d68a"}`.
- There is no re-POST, no retry and no `/sections` or `/export` request. ~Y observes only through read-only DynamoDB and S3
  reads and the resident journal over SSM.

## What it causes

The server side (runbook hops 3-5):
- the submission's request rows in `irpt-requests`;
- the job row in `irpt-jobs`;
- ONE closed `analysis_generate` message on `irpt-generation`;
- the resident claims the job and grades authority (`current_authority.decide`).

The vendor calls (hop 6), on the enrolled YCharts account through the lease-fenced session:
- identity and template reads;
- the holdings upload (Dollars, echo read back);
- the deterministic portfolio create;
- the 7-setting read-back and validate;
- the report create/generate;
- ONE PDF download (hop 7).

The permanent vendor objects are the holdings upload, the portfolio and the report. The checkpoints `upload`,
`portfolio`, `read_back` and `pdf` on the job row make a re-delivery resume without creating new objects.

The retained output (hop 7):
- `ORIGINAL_VENDOR_PDF` in `opal-data-ycharts`;
- the extracted, certified typed report and its fenced index rows;
- job state READY with `detail.report_id`, `revision` and `certification_sha256`.

## Branches

- **READY:** as above.
- **Refused at authority or validation:** the job is terminal with a named refusal, and no vendor write happens if the
  refusal precedes hop 6.
- **Provider error:** reported as the outcome. ~Y does not retry.

The QUEUE may redeliver the message: the resident answers RETRY, and the queue's `maxReceiveCount` is 5, after which the
message goes to the DLQ. A redelivery resumes from the job row's checkpoints, so it re-issues no create that already
checkpointed. This is the only server-side repeat, and the halves either admit it (at most 5 receives) or K5 is struck.

## Kept

Every row, S3 object and vendor object above is kept. ~Y's evidence file names each key: the job id, the request
rows, the S3 keys with versions and sha256, and the vendor portfolio and report ids from the job row's checkpoints.
