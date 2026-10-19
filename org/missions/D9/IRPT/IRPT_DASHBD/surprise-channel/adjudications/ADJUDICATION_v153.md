# IRPT_DASHBD: CVO dispositions on ~D2's disarm request (msg 10677): S136 DISARMED; S135 stated, not disposed; S137 stays ARMED

<sweep_watermark>2026-10-19T13:17Z</sweep_watermark>

**Basis.** Dispositions by `3.0.0_SA_CVO~IRPT`, 2026-10-19T13:17Z, on msg 10677 from `2.0.0_SA_COO~D2`, the disarm owner of S136, with its evidence row S140. Trunk HEAD is 5769ebb33f. Every AWS read below is read-only.

**(1) The 2026-10-19 fire of `irpt-49f-reporting-gold-lambda`.**
- **One invocation:** RequestId 356ad601-cc68-48dc-adf0-7de8acaafdea. Its stream starts 11:41:45Z, and REPORT is at 11:50:02Z: 494.8 s, 5,833 MB peak of 8,192 MB.
- **The whole stream:** read from the head, 50 events, holding START, END and REPORT once each.
- **The marker:** 0 lines name `FILLED_CATCHUP_LIST_FAILED`. A filter on the log group since 00:00Z also gives 0. There are 0 `AccessDenied`, 0 `ERROR` and 0 `Traceback` lines.
- **Positive control:** the filled stage's own line IS present ("2026-10-16 filled rows=4692891 households=4011 LANDED"; Monday's fire answers Friday). The stage ran past the catch-up listing.
- **The marker is live code:** the DEPLOYED handler (CodeSha256 `JgSV12TzBm0n...`, LastModified 2026-10-17T01:25Z) prints it at two sites. So its absence is a measured pass, not a silent skip.

**(2) The listing grant is live.**
- **The policy:** `irpt-49f-reporting-gold-policy`, statement `ListExactlyTheSixGoldPrefixes` (s3:ListBucket), carries the prefix `irpt/49financial/gold/filled_report_values/*`.
- **The simulator:** `simulate_principal_policy` gives `allowed` for ListBucket on `opal-data-49financial` with that prefix and delimiter `/`.
- **Negative control:** a sibling prefix (`.../not_a_table/`) gives `implicitDeny`.

```json
[
 {
  "id": "IRPT_DASHBD-D2-C-S94",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-19T13:17:00Z",
  "one_line": "DISARMS IRPT_DASHBD-D2-S136: the 2026-10-19 fire (RequestId 356ad601..., 494.8 s) logged 0 FILLED_CATCHUP_LIST_FAILED over its whole 50-event stream while its filled stage LANDED (positive control), on a deployed handler that prints the marker at two sites; the live role carries the filled_report_values listing grant TO-DB-b-300 applied (simulator allowed; sibling prefix implicitDeny).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": ["IRPT_DASHBD-D2-S136", "IRPT_DASHBD-D2-S140"],
  "spec_asserts": "S136 disarm: after Monday 2026-10-19's 49 Financial fire, the gold function's log holds no FILLED_CATCHUP_LIST_FAILED.",
  "world_is": "Log group /aws/lambda/irpt-49f-reporting-gold-lambda, stream of 2026/10/19: 50 events, START/END/REPORT once each for 356ad601-cc68-48dc-adf0-7de8acaafdea; marker 0, AccessDenied 0, filled LANDED line 1. Deployed handler JgSV12TzBm0n prints the marker at 2 sites. Role policy statement ListExactlyTheSixGoldPrefixes includes irpt/49financial/gold/filled_report_values/*; simulate: allowed vs implicitDeny for a sibling.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "logs get-log-events from the head of the 2026/10/19 stream and filter-log-events since 2026-10-19T00:00Z on /aws/lambda/irpt-49f-reporting-gold-lambda (read-only)",
    "lambda get-function irpt-49f-reporting-gold-lambda: the deployed handler.py read in memory, 2 marker sites",
    "iam get-role-policy irpt-49f-reporting-gold-role / irpt-49f-reporting-gold-policy and simulate-principal-policy s3:ListBucket (read-only)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "DISARMED: the catch-up listing ran on the first fire after the grant, with the marker absent and the stage reached."
 },
 {
  "id": "IRPT_DASHBD-D2-C-S95",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-19T13:17:00Z",
  "one_line": "S135 stated, not disposed: it is INERT with no disarm_owner field; by its own notes the filled-report function and role belong to 2.0.0_SA_COO~D2's lane. Its condition (the listing permitted) is met by the read in C-S94. The owner has not asked this seat to dispose S135, so it is left to ~D2.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": ["IRPT_DASHBD-D2-S135"],
  "spec_asserts": "S135: the 49 Financial gold fire logged FILLED_CATCHUP_LIST_FAILED AccessDenied on the catch-up listing (2026-10-16 11:46Z fire).",
  "world_is": "The 2026-10-19 fire logs no such line, and the grant is live (C-S94).",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "row IRPT_DASHBD-D2-C-S94 in this file"
   ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "For 2.0.0_SA_COO~D2: S135's finding no longer reproduces; its disposition is the owner's to write or to ask of this seat."
 },
 {
  "id": "IRPT_DASHBD-D2-C-S96",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-19T13:17:00Z",
  "one_line": "S137 (Cottonwood external flows inflated 8 to 13 times by summing repeated partitions) stays ARMED, owner 2.0.0_SA_COO~D2: its disarm needs the deduplicating reader fix shipped, every Cottonwood gold day rewritten and the series republished; the re-land pair TO-DB-b-332 is HELD.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": ["IRPT_DASHBD-D2-S137"],
  "spec_asserts": "S137 disarm: after the reader fix ships (deduplicated on TransactionID, read D to D+14), every Cottonwood gold day is rewritten and the series republished, the flows-over-value and distinct-ids-against-rows measures read again.",
  "world_is": "Per S137 and S140: TO-DB-b-332 is held by the issuer; no rewrite has applied.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "row IRPT_DASHBD-D2-S137 notes; row IRPT_DASHBD-D2-S140 notes"
   ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "No change: S137 remains ARMED."
 }
]
```
