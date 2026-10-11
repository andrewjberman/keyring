# NFRA_TRNSPT: remediations, round 22

<sweep_watermark>2026-10-11T06:38Z</sweep_watermark>

Round 22 slug by `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T06:38:23Z. L8 input: `org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/2.0.0_SA_COO~T2/R22_CLOSE.md @733aec56af (msg 4030)`, with msg 4289 (TO-APPLY-a18 terminal @18d031aaa7). No judgment criterion.
Graduated, round label v23: 5 rows, OPEN. ARMED: 1 (D2-S22), disarm owner `1.0.0_SA_CTO~DELL2`.
This seat's earlier ARMED row D2-S19 (the pull at its 128 MB ceiling) is disarmed and dismissed: the function reads 1024 MB live.
FWD-8 is ungraded (row D2-S24). Also carried by the close record, not rows: the handler's totals line omits read_refused;
`test_eod_voice.py` does not collect.

```json
[
 {
  "id": "NFRA_TRNSPT-D2-S22",
  "project": "NFRA_TRNSPT",
  "fabric": "dell2",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "mechanism": "One dist zip path feeds every function of the transcripts Terraform root. An untargeted apply from a tree without the three fix commits reverts the Teams pull's code and its memory setting; a pre-fix zip was built on this box at 05:26Z. Read live, the two pull functions carry two different code hashes.",
  "evidence": [
   "investigation rows NFRA_TRNSPT-D2-S22 and NFRA_TRNSPT-D2-S23",
   "this seat's live reads 2026-10-11T06:38:23Z: teams-global-transcripts-pull-lambda MemorySize 1024, CodeSha256 AI4UQD0M... (equal to the local dist zip), LastModified 2026-10-11T05:03:47Z; one run since at 1024 MB used 101 MB; outlook-global-transcripts-pull-lambda CodeSha256 VGIq85Xx..., LastModified 2026-10-07T23:59:05Z"
  ],
  "remedy": "The CTO's disarm read: every function of the root reads one live CodeSha256, built from a tree that holds fd74f984ac, 5ae3b3ddd9 and 7bca11ddee. Until then no untargeted apply runs on this root.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v23",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v23"
  },
  "closed": false,
  "disarm": {
   "state": "ARMED",
   "owner": "1.0.0_SA_CTO~DELL2",
   "at": null
  }
 },
 {
  "id": "NFRA_TRNSPT-D2-S16",
  "project": "NFRA_TRNSPT",
  "fabric": "dell2",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "The scheduled Teams pull failed on every fire from 2026-10-09T16:00Z (21 invocations) because one refused content read raised. The fix is deployed and ran clean once on a seat-driven invoke. The scheduled trigger has not fired on the new code.",
  "evidence": [
   "investigation row NFRA_TRNSPT-D2-S16",
   "this seat's read of the pull's log since 2026-10-09T12:00Z (first pass): 21 [ERROR] GatewayGraphError from 16:01Z to 22:03Z on 2026-10-09; the one driven invocation of 2026-10-11T03:38Z logs none",
   "this seat's live reads 2026-10-11T06:38:23Z: teams-global-transcripts-pull-lambda MemorySize 1024, CodeSha256 AI4UQD0M... (equal to the local dist zip), LastModified 2026-10-11T05:03:47Z; one run since at 1024 MB used 101 MB; outlook-global-transcripts-pull-lambda CodeSha256 VGIq85Xx..., LastModified 2026-10-07T23:59:05Z",
   "org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/2.0.0_SA_COO~T2/R22_CLOSE_READBACK_20261011.md"
  ],
  "remedy": "Read the Monday 2026-10-12 13:00Z fire from run.json per-series counts, with the function's REPORT line beside it (peak memory at 1024 MB is unmeasured). That read closes this row.",
  "owner": "2.0.0_SA_COO~T2",
  "round": "v23",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~T2",
   "round": "v23"
  },
  "closed": false
 },
 {
  "id": "NFRA_TRNSPT-D2-S15",
  "project": "NFRA_TRNSPT",
  "fabric": "dell2",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "Four monday_meeting transcripts (2026-04-10, 04-13, 05-04, 06-01) are listed by the gateway and their content is refused; they never landed and are ABSENT by this route. Any meeting not landed within about 120 days is lost the same way, and research_meeting's listing is refused today.",
  "evidence": [
   "investigation row NFRA_TRNSPT-D2-S15",
   "org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/2.0.0_SA_COO~T2/R22_CLOSE_READBACK_20261011.md section 3"
  ],
  "remedy": "The CTO rules FWD-3 on the 4 (accepted as lost, or another source named) and FWD-2's wording for research_meeting. Andrew's SharePoint folder link is the open call.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v23",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v23"
  },
  "closed": false
 },
 {
  "id": "NFRA_TRNSPT-D2-S17",
  "project": "NFRA_TRNSPT",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The transcripts Terraform root has no default and no tfvars for second_reader_trust_principal_arns, so every plan needs a -var. A guessed value on an untargeted apply would rewrite who may read the tier.",
  "evidence": [
   "investigation row NFRA_TRNSPT-D2-S17"
  ],
  "remedy": "A committed tfvars or a default for the variable, taken from applied state. It names who reads the tier, so it is the CTO's call.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v23",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v23"
  },
  "closed": false
 },
 {
  "id": "NFRA_TRNSPT-D2-S20",
  "project": "NFRA_TRNSPT",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "readers.tf states 'NOT APPLIED -- plan only' at HEAD while the second reader's role has been live since 2026-10-09T09:55:13Z. The file's header says the opposite of the applied state.",
  "evidence": [
   "investigation row NFRA_TRNSPT-D2-S20"
  ],
  "remedy": "The header states the applied state, in the commit that next touches the file.",
  "owner": "2.0.0_SA_COO~T2",
  "round": "v23",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~T2",
   "round": "v23"
  },
  "closed": false
 }
]
```
