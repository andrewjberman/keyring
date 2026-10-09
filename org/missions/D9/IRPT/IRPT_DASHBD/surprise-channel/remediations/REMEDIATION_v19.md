# IRPT_DASHBD -- rounds 41-43 remediations

<sweep_watermark>2026-10-09T12:43Z</sweep_watermark>

Graduated at the rounds-41-43 L8 (ADJUDICATION_v25.md), round label v44: 4 rows, OPEN; S40 ARMED (disarm owner 2.0.0_SA_COO~D2).

```json
[
  {
    "id": "IRPT_DASHBD-S40",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "The first scheduled R37 fire (11:41:45Z, RequestId 356ac8d2) logged LOTS_SKIPPED 2026-10-08: a realized lot id repeats with the same closing date, quantity AND proceeds, so DB-b-73's extended key (adds proceeds) is still not unique on 2026-10-08.",
    "evidence": [
      "investigation row IRPT_DASHBD-S40",
      "CloudWatch /aws/lambda/irpt-49f-reporting-gold-lambda stream 2026/10/09/[$LATEST]40136c6cd88d4880be5378a65a2dd26b, RequestId 356ac8d2-cc68-48dc-adf0-7de8acaafdea"
    ],
    "remedy": "Find the realized-lot rows that repeat with the same closing date, quantity and proceeds on 2026-10-08 in the custodian partition, name what distinguishes them (or that nothing does: true duplicates), fix the key or de-duplicate by rule, and backfill the skipped day under the release's pair; until then each skipped day is stated on the page, not shown as no lots.",
    "owner": "2.0.0_SA_COO~D2",
    "round": "v44",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~D2",
      "round": "v44"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~D2",
      "at": null
    }
  },
  {
    "id": "IRPT_DASHBD-W62-S1",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "realized_gain, now a member of the realized primary key, is rewritten after realized_rows() checks the key (in-kind and wash-sale re-measurement), so key uniqueness is held by two guards on two values of the same column.",
    "evidence": [
      "investigation row IRPT_DASHBD-W62-S1",
      "data/assets/scripts/gold/irpt_reporting/account_activity_lots.py realized_rows() (key check on source gain) and the re-measure branches that assign r[\"realized_gain\"]"
    ],
    "remedy": "Check key uniqueness on the final realized_gain value (after the in-kind and wash-sale re-measurement), not before it, or drop realized_gain from the key.",
    "owner": "2.0.0_SA_COO~D2",
    "round": "v44",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~D2",
      "round": "v44"
    },
    "closed": false
  },
  {
    "id": "IRPT_DASHBD-W64-S1",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "DB-b-85's verify-persisted re-read the persisted object from S3 (version-pinned from the index row) and checked its sha256 against the revision, its report_kind, its as_of_date and its composition_sha256 binding. IB-pr-405 returns the index only, so DB-b-89's verify-persisted checks that the route's report_index names the same report_id and revision as the refs, bound to the same artifact_id and composition_sha256; the blob is not re-read.",
    "evidence": [
      "investigation row IRPT_DASHBD-W64-S1",
      "docs/contracts/investor-reporting/v1/OwnedAnalysisRequest.schema.json:88-106"
    ],
    "remedy": "Restore a content-level persisted check (sha256, report_kind, as_of_date and composition binding) through an owned content read, or state that verify-persisted is index-only.",
    "owner": "2.0.0_SA_COO~P2",
    "round": "v44",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~P2",
      "round": "v44"
    },
    "closed": false
  },
  {
    "id": "IRPT_DASHBD-S41",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "PROOF_OF_SPEC.schema.json artifacts_produced cannot register a live AWS resource that is not S3 or DynamoDB: kind has no Secrets Manager (or Lambda/IAM-resource) member whose rows are exempt from git resolution, so an AE order whose deliverable IS an AWS resource must omit it from artifacts_produced.",
    "evidence": [
      "investigation row IRPT_DASHBD-S41",
      "org/standards/PROOF_OF_SPEC.schema.json (artifacts_produced[].kind enum; required commit_or_etag)"
    ],
    "remedy": "Give PROOF_OF_SPEC.schema.json artifacts_produced a kind for live AWS resources (a secret, a Lambda, an IAM resource) exempt from git resolution, so an AE order can register what it produced.",
    "owner": "1.0.0_SA_CTO~DELL2",
    "round": "v44",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL2",
      "round": "v44"
    },
    "closed": false
  }
]
```
