# IRPT_ANLREQ: remediations, round 2 ADDENDUM 1 (releases 1 and 3)

<sweep_watermark>2026-10-11T06:44Z</sweep_watermark>

Slug by `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T06:44:04Z. L8 input: `org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND2_L8_COMPILE_ADDENDUM_1_RELEASES_20261011.md @f411f4a76c (msg 4286)`. L9: `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ANLREQ_ROUND_2_RELEASES_L9_GRADE_20261011.md`.
**Release 1 stands closed as applied and read; release 3 stands closed as applied and exercised once. The thread is not live.**
Graduated, round label v3: 10 rows, OPEN. ARMED: 2 (D2-S29: release 4 cannot attach, the ports are stubs; D2-S26: one message on the
ready queue until 2026-10-15). The CTO's analysis carries D2-S20, D2-S21 and D2-S24 first (its msg 4240).

```json
[
 {
  "id": "IRPT_ANLREQ-D2-S29",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "mechanism": "Release 4 cannot attach as the tree stands: the packager's live attach and ticket-read ports are stubs that raise PACKAGER_PRINCIPAL_UNSET, and no cell builds them. FWD-1's last hop has no code.",
  "evidence": [
   "investigation rows IRPT_ANLREQ-D2-S29 and IRPT_ANLREQ-D2-S30",
   "org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND2_L8_COMPILE_ADDENDUM_1_RELEASES_20261011.md @f411f4a76c (msg 4286)"
  ],
  "remedy": "A cell builds the two ports before release 4 is cut. The CTO's ordering rule (row D2-S30) holds: the trigger that feeds real requests does not go live before the attach release can consume them.",
  "owner": "2.0.0_SA_COO~G2",
  "round": "v3",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~G2",
   "round": "v3"
  },
  "closed": false,
  "disarm": {
   "state": "ARMED",
   "owner": "2.0.0_SA_COO~G2",
   "at": null
  }
 },
 {
  "id": "IRPT_ANLREQ-D2-S26",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "One commentary_ready message for a synthetic request sits on the ready queue until about 2026-10-15T06:10Z. Its only admitted consumer is the resident's role.",
  "evidence": [
   "investigation row IRPT_ANLREQ-D2-S26",
   "org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND2_L8_COMPILE_ADDENDUM_1_RELEASES_20261011.md @f411f4a76c (msg 4286)"
  ],
  "remedy": "A measured queue depth of 0 (consumed by release 4's attach, or expired). The owner reads the depth.",
  "owner": "2.0.0_SA_COO~Y2",
  "round": "v3",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~Y2",
   "round": "v3"
  },
  "closed": false,
  "disarm": {
   "state": "ARMED",
   "owner": "2.0.0_SA_COO~Y2",
   "at": null
  }
 },
 {
  "id": "IRPT_ANLREQ-D2-S32",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "Release 1 closed on evidence that does not cover the live bytes on four points: reads 3 and 4 were measured on revision 2; three widenings are applied and unexercised; 'the original-file read does not write' is unmeasured; the source map's artifact_sha256 for irpt-status reads E7VKvhg3 while the function runs 6idtFvAm. Release 3's deny-side permissions are inferred from documents.",
  "evidence": [
   "investigation row IRPT_ANLREQ-D2-S32",
   "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ANLREQ_ROUND_2_RELEASES_L9_GRADE_20261011.md",
   "this seat's live reads 2026-10-11T06:44:04Z: irpt-status CodeSha256 6idtFvAm..., LastModified 2026-10-11T04:44:47Z; its log from the promote to 06:22Z: 30 invocations, 0 TypeError, 0 Traceback, 0 RetentionRefused; outlook-global-commentary-draft-lambda Active on AI4UQD0M..., LastModified 05:44:45Z, equal to teams-global-transcripts-pull-lambda; outlook-global-transcripts-pull-lambda on VGIq85Xx... since 2026-10-07",
   "infra/aws/lambda/ci/lambda-source-map.json at HEAD: irpt-status artifact_sha256 reads E7VKvhg3..., not the live 6idtFvAm..."
  ],
  "remedy": "Reads 3 and 4 re-run on revision 6. The source map entry records the live digest. One measured read shows the original-file route writes nothing. Each widening is exercised by its first real caller or stays stated as unexercised in the next packet.",
  "owner": "2.0.0_SA_COO~Y2",
  "round": "v3",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~Y2",
   "round": "v3"
  },
  "closed": false
 },
 {
  "id": "IRPT_ANLREQ-D2-S15",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "Release 1 read 5: a ticket-bound request never left RECEIVED; the resident worker refuses it CLOSED_COMPOSITION_REQUIRED. The read is re-homed to release 4's order as REL4-READ5 and reads FAIL.",
  "evidence": [
   "investigation rows IRPT_ANLREQ-D2-S15 and IRPT_ANLREQ-D2-S25",
   "org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND2_L8_COMPILE_ADDENDUM_1_RELEASES_20261011.md @f411f4a76c (msg 4286)"
  ],
  "remedy": "Release 4's apply order carries the read, and it passes on one ticket-bound request that reaches READY.",
  "owner": "2.0.0_SA_COO~G2",
  "round": "v3",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~G2",
   "round": "v3"
  },
  "closed": false
 },
 {
  "id": "IRPT_ANLREQ-D2-W41-S17",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "A BUILD_ONLY of irpt-commentary-draft-store-lambda refuses at the parity check: seven source_dir files are not in files[].",
  "evidence": [
   "investigation row IRPT_ANLREQ-D2-W41-S17"
  ],
  "remedy": "The source map lists the seven files, or the owner states they are deliberately outside the package, and the build reads clean.",
  "owner": "2.0.0_SA_COO~Y2",
  "round": "v3",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~Y2",
   "round": "v3"
  },
  "closed": false
 },
 {
  "id": "IRPT_ANLREQ-D2-S24",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "analysis-report does not return the retained report's ref, so the Analysis tab cannot publish an export target (DSGN_IRPTV1 row W35-S2, the finding NEEDS_SERVED_ROUTE graded by this seat today).",
  "evidence": [
   "investigation row IRPT_ANLREQ-D2-S24",
   "org/tier1_exec/3.0.0_SA_CVO/deliverables/DSGN_IRPTV1_ROUND_11_L9_GRADE_20261011.md"
  ],
  "remedy": "analysis-report returns retained_ref in the shape Performance serves (the CTO's ruling). The next issuance carries it.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v3",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v3"
  },
  "closed": false
 },
 {
  "id": "IRPT_ANLREQ-D2-S20",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The report package's 'Report' opener shows the accepted request record, not the report.",
  "evidence": [
   "investigation row IRPT_ANLREQ-D2-S20"
  ],
  "remedy": "The opener reads the report. The next issuance carries it.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v3",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v3"
  },
  "closed": false
 },
 {
  "id": "IRPT_ANLREQ-D2-S21",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "Each row of a viewer's request history should state the client its frozen selection names; the wire serves none (DSGN_IRPTV1 row W39-S2).",
  "evidence": [
   "investigation row IRPT_ANLREQ-D2-S21"
  ],
  "remedy": "The owned-request wire serves the client. The next issuance carries it.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v3",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v3"
  },
  "closed": false
 },
 {
  "id": "IRPT_ANLREQ-D2-S18",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "A filed report opens through IRPT's owned read, so a ticket's assignee who is not the uploader cannot open it.",
  "evidence": [
   "investigation row IRPT_ANLREQ-D2-S18"
  ],
  "remedy": "A candidate for the next issuance: the assignee's read path, as the CTO rules it.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v3",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v3"
  },
  "closed": false
 },
 {
  "id": "IRPT_ANLREQ-D2-S17",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The Analysis Request form's firm answer is free text sent to the upload door as the selected tenant.",
  "evidence": [
   "investigation row IRPT_ANLREQ-D2-S17"
  ],
  "remedy": "A candidate for the next issuance: a choice from the caller's allowed firms.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v3",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v3"
  },
  "closed": false
 }
]
```
