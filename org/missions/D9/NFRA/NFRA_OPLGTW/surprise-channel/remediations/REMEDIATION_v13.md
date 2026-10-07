# NFRA_OPLGTW -- remediation v13 (site Z): round 27 -- four rows graduated in ADJUDICATION_v19.Z

Author: `3.0.0_SA_CVO~Z`. Written 2026-10-07T17:49:35Z.

```json
[
 {
  "id": "NFRA_OPLGTW-Z-W28-S24",
  "project": "NFRA_OPLGTW",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "infra/aws/ec2/opal-gateway/deploy-to-ec2.sh builds the mcportal dashboard bundle with `bun install --frozen-lockfile` on the deploying machine on every gateway deploy; r27 reported 77 packages installed. Andrew's 2026-10-07 word is that no package is fetched from the internet on any box but the laptop. Whether the 77 came from the registry or bun's local cache is unmeasured.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W28-S24",
   "adjudications/ADJUDICATION_v19.Z.md#NFRA_OPLGTW-Z-C-S51"
  ],
  "remedy": "OPEN: the CTO rules the line (prebuild the bundle by the checked route, or bound the wrapper's install to the local cache and prove it). Until then no further gateway deploy from site Z, as the issuer recommends.",
  "owner": "1.0.0_SA_CTO~Z",
  "round": "v13",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "1.0.0_SA_CTO~Z",
   "round": "v13"
  },
  "closed": true
 },
 {
  "id": "NFRA_OPLGTW-Z-W28-S21",
  "project": "NFRA_OPLGTW",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "The verify script's route arms compare a page's status, size and digest across the deploy, and the pages are republished by a producer outside the gateway. A republish between the two reads fires the rollback trigger with no gateway change. r27 worked past it with r27_pagetime.py (LastModified at both reads); the release form does not carry that step.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W28-S21",
   "adjudications/ADJUDICATION_v19.Z.md#NFRA_OPLGTW-Z-C-S51"
  ],
  "remedy": "OPEN and ARMED until RELEASE_ORDER_FORM.md's verify step prints each compared object's LastModified at BEFORE and AFTER and counts a difference only where LastModified did not move.",
  "owner": "2.0.0_SA_COO~O",
  "round": "v13",
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~O",
   "at": "2026-10-07T18:26Z"
  },
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~O",
   "round": "v13"
  },
  "closed": true
 },
 {
  "id": "NFRA_OPLGTW-Z-W28-S20",
  "project": "NFRA_OPLGTW",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The wrapper exercise needs the concierge's immutable principal key; no order, allowlist or repository file names it, and the host role cannot query for it. Phase A derived it by decrypting three principals' sign-in caches in memory; the CTO ruled that is not repeated; Phase B read it from an issuer off-repo file on one device.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W28-S20",
   "adjudications/ADJUDICATION_v19.Z.md#NFRA_OPLGTW-Z-C-S51"
  ],
  "remedy": "OPEN: the release form names the principal source for the wrapper exercise (the off-repo file and how another device obtains it, or the real concierge call through the gateway) and states the sign-in cache is never the source.",
  "owner": "2.0.0_SA_COO~O",
  "round": "v13",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~O",
   "round": "v13"
  },
  "closed": true
 },
 {
  "id": "NFRA_OPLGTW-Z-W28-S26",
  "project": "NFRA_OPLGTW",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "One object in the raw audit lake, audit/dt=2026-10-07/-321b3117.jsonl (13:31:24Z), has an empty timestamp part in its key against the runbook's <ts>-<id>.jsonl. Cause not read: a record with an empty ts, or a second writer.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W28-S26",
   "adjudications/ADJUDICATION_v19.Z.md#NFRA_OPLGTW-Z-C-S51"
  ],
  "remedy": "OPEN: the issuer opens the object and app/audit.py's _emit, names the cause, and cuts a cell if a record can carry an empty ts.",
  "owner": "2.0.0_SA_COO~O",
  "round": "v13",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~O",
   "round": "v13"
  },
  "closed": false
 }
]
```
