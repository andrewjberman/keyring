# NFRA_CTLPLN -- remediations, v7

<sweep_watermark>2026-10-14T21:30Z</sweep_watermark>

Author: `3.0.0_SA_CVO~L`, 2026-10-14 ~21:3xZ, at the round-13 close: this round's L10 slug. Graduated in ADJUDICATION_v18.md C-S49.
Three rows: W89-S3 INERT; D2-S3 and Z-S8 ARMED (filed from dell2 and site Z). Every round-13 order is terminal (six complete, CT-ac-5 parked on Andrew's word).

```json
[
 {
  "id": "NFRA_CTLPLN-W89-S3",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "infra/aws/terraform/shared-infra/s3-lgic-firm-buckets.tf builds each lgic firm bucket's policy from module.opal_name.fence_scoped_statements (:172) and never appends fence_scoped_allow_statements, while s3-49financial.tf:141 appends both. A scoped registry row on an lgic bucket therefore renders its Deny with no matching Allow: inflection carries 0 of the 4 Allow statements the module renders for it, cottonwood 0 of 2 (worker's with-state render). The real scoped row on opal-data-inflection (irpt-performance-adapter-role, GetObject and ListBucket on irpt/inflection...) is the first consumer affected.",
  "evidence": [
   "org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md row W89-S3",
   "grep over s3-lgic-firm-buckets.tf and s3-49financial.tf at HEAD (2026-10-14 ~21:2xZ)",
   "adjudication row NFRA_CTLPLN-C-S49"
  ],
  "remedy": "P2. A round-14 cell appends lookup(module.opal_name.fence_scoped_allow_statements, <bucket>, []) in s3-lgic-firm-buckets.tf beside the Deny lookup, under a never-widen pair (it widens a bucket policy). Done when the targeted plan for each lgic firm bucket shows exactly the module's Allow statements added and nothing removed, and the scoped role's real GetObject on its own prefix is admitted.",
  "owner": "2.0.0_SA_COO~C",
  "round": "v18",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~C",
   "round": "v18"
  },
  "closed": false
 },
 {
  "id": "NFRA_CTLPLN-D2-S3",
  "project": "NFRA_CTLPLN",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": ".tools/crossbox-deploy-check.py's OPEN-CALL limb matches an open_calls row of kind act through the row's PROJECT write set when the row carries no roots field. One pending act that only Andrew can do (dell2-20261013T214715Z-f61b, an execution ID for IRPT_BCKEND) therefore draws STOP on every root that project's write set covers, including applies that do not depend on the act (irpt-status, opal-ticket-api). Measured: calls_scanned=346 matched=1 verdict=STOP. The limb prints WARN today; ENFORCE turns it into a stop.",
  "evidence": [
   "org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md row D2-S3",
   "adjudication row NFRA_CTLPLN-C-S50"
  ],
  "remedy": "P2. Before ENFORCE is armed on the OPEN-CALL limb, 2.0.0_SA_COO~C rules (or cuts a cell so) a kind-act row matches only the roots it names in its own roots field, and an act row with no roots matches none. Done when the same act row reads matched=0 against irpt-status and still matches a root it names.",
  "owner": "2.0.0_SA_COO~C",
  "round": "v18",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~C",
   "round": "v18"
  },
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~C",
   "at": "2026-10-14T22:45Z"
  },
  "closed": true
 },
 {
  "id": "NFRA_CTLPLN-Z-S8",
  "project": "NFRA_CTLPLN",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "Six site Z CloudOps lanes (~MQ, ~ZS, ~ZQ, ~ZW, ~ZT, ~MI) ended between 2026-10-13 ~19:00Z and 2026-10-14 ~12:2xZ with no KILL line, no reboot, no crash and no low-memory event (positive control on the event-log reads). A seat that dies unseen holds open orders nobody works, and seat-liveness read dead=0 because their orders were placed on another box. Cause UNREAD; a clean session exit is the remaining candidate. Same class as S9120 on dell2.",
  "evidence": [
   "org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md row Z-S8",
   "adjudication row NFRA_CTLPLN-C-S50",
   "remediations/REMEDIATION_v6.md row NFRA_CTLPLN-S9120 (the dell2 instance of the class)"
  ],
  "remedy": "P2. 1.0.0_SA_CTO~Z names who reads the cause (each headless seat's stdout and stderr captured to a file per seat, a log sink, never an alert, so the next ending's last line is readable), and MSTR~Z respawns on each death it sees until then. Done when the next unexplained ending's cause is read from its captured output, or when one week passes with no unexplained ending on site Z.",
  "owner": "1.0.0_SA_CTO~Z",
  "round": "v18",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~Z",
   "round": "v18"
  },
  "disarm": {
   "state": "ARMED",
   "owner": "1.0.0_SA_CTO~Z",
   "at": null
  },
  "closed": false
 }
]
```

-- 3.0.0_SA_CVO~L
