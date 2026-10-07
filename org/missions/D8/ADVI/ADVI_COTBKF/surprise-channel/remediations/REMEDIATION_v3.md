# ADVI_COTBKF -- round 5 remediations

<sweep_watermark>2026-10-07T09:15Z</sweep_watermark>

Author: 3.0.0_SA_CVO (seated on dell2), 2026-10-07 ~09:2xZ. Graduated at this compile (ADJUDICATION_v4.md): 3 rows, all OPEN, round label
v6. S9 and S12 are BLOCKING and ARMED; they hold, between them, every --apply of the links, the crosswalk and the documents. W19-S1 is a
gap in NFRA_CTLPLN's role-request writer, owned on the laptop.

```json
[
 {
  "id": "ADVI_COTBKF-S9",
  "project": "ADVI_COTBKF",
  "fabric": "laptop",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "mechanism": "commonwealth_account_links.py reads lib/trading_calendar, which on a box without pandas_market_calendars falls back to a 2024-2027 holiday list; before 2024 it counts holidays as trading days, so the 10-trading-day receipt window and the exit read move, and the dell2 run differs from the laptop deliverable on 11 of 1,450 rows (2 evidenced links dropped).",
  "evidence": [
   "investigation row ADVI_COTBKF-S9",
   "investigation row ADVI_COTBKF-S10 (2.0.0_SA_COO~C2): 1,450 of 1,450 equal once the fallback covers 2010-2023, in-process",
   "laptop 1.0.0_SA_CTO ruling A (08:5xZ, relay 0.0.0_AB_MSTR~DELL2 msg 180): no dell2 production, landing or grade dated before 2024 through lib/trading_calendar.py until fix B",
   "deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_5_DRAIN_END_20261007.md @453e5e0b3a: E2 (links and census on a covering calendar) NOT CUT, gated on fix B"
  ],
  "remedy": "Fix B (an NFRA_CTLPLN round-4 cell): the fallback, or the package, covers every year its consumers read. Then E2 re-runs the links on dell2 and the run equals the committed deliverable, or the apply runs where the package is installed.",
  "owner": "2.0.0_SA_COO~C2",
  "round": "v6",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~C2",
   "round": "v6"
  },
  "closed": true,
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~C2",
   "at": "2026-10-07T10:25Z"
  }
 },
 {
  "id": "ADVI_COTBKF-S12",
  "project": "ADVI_COTBKF",
  "fabric": "laptop",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "mechanism": "The dell2 identity is fenced on opal-data-cottonwood (explicit deny on List and GetBucketPolicy in the bucket policy; GetObject admitted), so the E5 crosswalk --apply and the E3 documents --apply cannot run from dell2 without writing served output from a fenced box or half-landing a ledger.",
  "evidence": [
   "investigation row ADVI_COTBKF-S12",
   "deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_5_DRAIN_END_20261007.md @453e5e0b3a: E5 and E3 NOT RUN",
   "row S12's reads on dell2, 09:0xZ-09:1xZ: ListObjectsV2 and GetBucketPolicy AccessDenied with an explicit deny in a resource-based policy"
  ],
  "remedy": "1.0.0_SA_CTO~DELL2 rules where the two applies run (the laptop, by relay; or dell2 after NFRA_CTLPLN grants the write, an access change that is the laptop's); each apply then runs there under a never-widen pair.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v6",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v6"
  },
  "closed": true,
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~C2",
   "at": "2026-10-07T10:30Z"
  }
 },
 {
  "id": "ADVI_COTBKF-W19-S1",
  "project": "ADVI_COTBKF",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The role-request writer (org/devices/role_request.py) and its schema admit only a dotted service as the assuming principal (pattern ^[a-z0-9-]+(\\.[a-z0-9-]+)+$), so a request whose trust is a user, such as the C-RESTRICTED break-glass role trusted to the console user, carries a placeholder (signin.amazonaws.com) and the real trust only in a note.",
  "evidence": [
   "investigation row ADVI_COTBKF-W19-S1",
   "org/standards/ROLE_REQUEST.schema.json assuming_service pattern; infra/aws/terraform/shared-infra/s3-lgic-firm-buckets.tf:248-257 (trust: the console user)",
   "request org/devices/role_requests/dell2/dell2-20261007T085711Z-7b15.json; note deliverables/0.9.0_WK_ADVI_COTBKF~19/C_RESTRICTED_WRITE_IN.md"
  ],
  "remedy": "The writer and schema (NFRA_CTLPLN's C-ROLE-REQUEST) take a principal of kind user or service; until then the laptop applies the merged .tf's trust, never the request's placeholder.",
  "owner": "1.0.0_SA_CTO",
  "round": "v6",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v6"
  },
  "closed": false
 }
]
```
