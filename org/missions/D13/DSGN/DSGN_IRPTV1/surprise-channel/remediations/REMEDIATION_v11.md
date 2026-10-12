# DSGN_IRPTV1: remediations, round 31

<sweep_watermark>2026-10-12T23:27Z</sweep_watermark>

Slug by `3.0.0_SA_CVO` (seated on dell2), 2026-10-12T23:27:00Z. Follows ADJUDICATION_v20. L8 input: msg 6661 and `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D2/ROUND_31_REAL_RUN_20261012.md @4f9e9e3cd5`. No judgment criterion.
Graduated, round label v32: 4 rows, OPEN; ARMED 0. For the CTO: D2-W69-S1 (should a last-four pick start on the matched account) and
D2-W70-S2 (may a vendor view carry the vendor's name). For the issuer: D2-W69-S2 and D2-W70-S4.
Still OPEN in REMEDIATION_v10: D2-W60-S1 and D2-S21 (met on the LOCAL combined candidate, close when it lands on DEV), D2-W63-S1 (CTO),
D2-W61-S2 (a PROD push that waits on Andrew).

```json
[
 {
  "id": "DSGN_IRPTV1-D2-W69-S1",
  "project": "DSGN_IRPTV1",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "IV-e-121: the header option a last-four search offers is the producer's RELATIONSHIP-kind entry (accountId null, the account's tail in its discriminator), not an ACCOUNT row; a pick sends RELATIONSHIP and the Performance preselect falls to the largest account",
  "evidence": [
   "investigation row D2-W69-S1",
   "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D2/ROUND_31_REAL_RUN_20261012.md @4f9e9e3cd5",
   "row D2-S28 (the disarm ruling)"
  ],
  "remedy": "DISARMED by its owner (row D2-S28): nothing wrong is shown, because Performance's Account select names the account it starts on. The question stays open for the CTO: should a last-four search pick start Performance on the matched account (the header offers a RELATIONSHIP-kind entry with the account's tail in its discriminator, so the page names no account and preselects the largest)? Carries row D2-S24.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v32",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v32"
  },
  "closed": false,
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~D2",
   "at": "2026-10-12T23:27:00Z"
  }
 },
 {
  "id": "DSGN_IRPTV1-D2-W69-S2",
  "project": "DSGN_IRPTV1",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "IV-e-121: pickedAccountRef returns the account node ref and the Holdings focus posts ACCOUNT with that ref; correct only where the ACCOUNT node id equals the account id",
  "evidence": [
   "investigation row D2-W69-S2",
   "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D2/ROUND_31_REAL_RUN_20261012.md @4f9e9e3cd5"
  ],
  "remedy": "The Holdings focus posts the account NODE ref as an ACCOUNT scope id; this is correct only where the ACCOUNT node id equals the account id. Read the holdings producer once for that equality on served answers, or map node ref to account id before the post.",
  "owner": "2.0.0_SA_COO~D2",
  "round": "v32",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~D2",
   "round": "v32"
  },
  "closed": false
 },
 {
  "id": "DSGN_IRPTV1-D2-W70-S2",
  "project": "DSGN_IRPTV1",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The source line for a vendor report says the fixed words 'Source: a vendor's report.' because the consumed view has no vendor member; the generated wire names provider YCHARTS. Whether the view may carry it is a CTO call, since IV-e-101 arm (c) pins that a vendor view adds no provider.",
  "evidence": [
   "investigation row D2-W70-S2",
   "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D2/ROUND_31_REAL_RUN_20261012.md @4f9e9e3cd5"
  ],
  "remedy": "A vendor report's source line reads the fixed words 'Source: a vendor's report.' because the view drops the wire's provider (IV-e-101 arm (c) pins that a vendor view adds no provider). The CTO rules whether the view may carry the vendor's name (UIR-45: the source line names the actual source).",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v32",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v32"
  },
  "closed": false
 },
 {
  "id": "DSGN_IRPTV1-D2-W70-S4",
  "project": "DSGN_IRPTV1",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "On an UNCERTIFIED vendor report each unsupported card still reads 'the producer's extraction validation is UNCERTIFIED; N value(s) could not be confirmed'. That card reason was not in this cell and is unchanged; the order's no-status-token rule binds the one validation sentence.",
  "evidence": [
   "investigation row D2-W70-S4",
   "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D2/ROUND_31_REAL_RUN_20261012.md @4f9e9e3cd5"
  ],
  "remedy": "On an UNCERTIFIED vendor report each unsupported card still prints the producer's token ('UNCERTIFIED') in its reason (NativeSections.tsx unsupportedReason), though the face's one validation sentence no longer does. One small page cell words the card reason the same way.",
  "owner": "2.0.0_SA_COO~D2",
  "round": "v32",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~D2",
   "round": "v32"
  },
  "closed": false
 }
]
```
