# ADVI_COTBKF: CVO adjudication, round 14

<sweep_watermark>2026-10-07T16:2xZ</sweep_watermark>

Round 14 L8 compile by `3.0.0_SA_CVO` (seated on dell2), 2026-10-07 ~16:2xZ. L8 input: `deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_14_DRAIN_END_20261007.md @cbb243196e` (msg 854). CB-n-1 complete and VALID
@6f3a844f75; the issuer's E1 re-apply is CLOSED 3/3 and read back here from S3. 2 rows: D2-W30-S1 dismissed below, D2-S25 graduated OPEN in
`remediations/REMEDIATION_v8.md`. Clock advanced in place: D2-S24 (REMEDIATION_v7) closed. ARMED: 0.

```json
[
 {
  "id": "ADVI_COTBKF-C-S19",
  "project": "ADVI_COTBKF",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-07T16:25Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "D2-W30-S1 (acct#2f33cbcc's 0.003 residual: a lone li with no row out, which the snapshot also holds) is dismissed; the served re-apply read back from S3; D2-S24 closed in place.",
  "adjudicates": [
   "ADVI_COTBKF-D2-W30-S1"
  ],
  "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
  "world_is": "D2-W30-S1: the 2026-06-23 snapshot holds acct#2f33cbcc's 0.003 too, so the rebuild agrees with the custodian's own record; whether it is a real holding or a source gap does not change any table. All 5 residuals now equal their snapshot quantity with no sign changed (CB-n-1). The E1 re-apply is served: this seat read both applied tables back (crosswalk 471 MATCHED of 1,533; links 212 LINKED of 1,450, with the one swap each way) under ledger advi-cotbkf-r14-reapply-crosswalk-links-20261007 CLOSED 3/3; D2-S24 (REMEDIATION_v7) is closed in place.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "investigation row ADVI_COTBKF-D2-W30-S1",
    "deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_14_DRAIN_END_20261007.md @cbb243196e",
    "s3 opal-data-assets commonwealth/cottonwood/silver/crosswalk/date=2026-06-23/crosswalk.parquet: 1,533 rows, 471 MATCHED, 1,062 NOT_MATCHED, 22 AWAITING_PERSON; account_links/date=2026-06-23/account_links.parquet: 1,450 rows, 212 LINKED; acct#e1e2dacb -> acct#f6464238 LINKED; acct#d6187d4b NOT_LINKED LEFT_COMMONWEALTH (this compile's read, dell2, 2026-10-07 ~16:2xZ)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A residual the custodian's snapshot also carries; no table changes on its class."
 }
]
```
