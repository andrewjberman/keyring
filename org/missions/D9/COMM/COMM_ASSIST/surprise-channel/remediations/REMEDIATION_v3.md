# COMM_ASSIST -- remediations, v3 (laptop)

<sweep_watermark>2026-10-13T21:58Z</sweep_watermark>

Author: `3.0.0_SA_CVO~L`, 2026-10-13 ~21:5xZ, at the round-16 close: this round's L10 slug. Graduated in ADJUDICATION_v2.md C-S4.
Three rows, all INERT. The round's one judgment grade, CAh3-AC2 FAIL, is C-S1 in ADJUDICATION_v1.md; its named repair (verify the
signature at the receiver against a key pinned in the assistant's deployed config, name the CloudTrail-visible residual, add a
direct-send arm to the forged-answer test) is the first round-17 input, and whether that residual meets FWD-7's "nothing else can
answer in his place" is the CTO's ENDPOINT question.

```json
[
 {
  "id": "COMM_ASSIST-W8-S6",
  "project": "COMM_ASSIST",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "on_sms_reply calls unseen(), the stale-version refusal, only when action is send or drop (tenant.py:497). The edit branch (:527-557) redrafts from the CURRENT pending draft and texts version+1, so a redraft answer given against an older version is applied to the newer draft. Today only Andrew's texts reach it, and nothing posts without his later approval; once muse answers carry a version (FWD-7), the version they carry is ignored on edit.",
  "evidence": [
   "org/missions/D9/COMM/COMM_ASSIST/surprise-channel/investigations/INVESTIGATION_v1.md row W8-S6",
   "git show 38ac43222d:data/transcripts/scripts/teams_chat/tenant.py lines 494-557",
   "adjudication row COMM_ASSIST-C-S4"
  ],
  "remedy": "P2. Round-17 cell, with FWD-7's build: the edit branch calls unseen() when the payload carries a version, and refuses with the same 'changed just before your reply' text. Done when a fixture edit answer at version N against pending version N+1 is refused and the pending draft is unchanged, and the same answer at N+1 redrafts.",
  "owner": "2.0.0_SA_COO~CA",
  "round": "v2",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~CA",
   "round": "v2"
  },
  "closed": false
 },
 {
  "id": "COMM_ASSIST-W8-S8",
  "project": "COMM_ASSIST",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The forwarder must address sms.reply to an object id, but drafts.json rows carry tag and version only (refresh.py:230-234). The id is found through the #index#sms-tag row (ldo.py:152-155).",
  "evidence": [
   "org/missions/D9/COMM/COMM_ASSIST/surprise-channel/investigations/INVESTIGATION_v1.md row W8-S8",
   "git show 38ac43222d:data/transcripts/scripts/muse_reader/refresh.py lines 228-236",
   "adjudication row COMM_ASSIST-C-S4"
  ],
  "remedy": "P3. Round-17 cell: either refresh.py carries object_id in each drafts.json row, or the forwarder makes the index read and holds the grant for it. Done when a muse answer for a pending tag reaches the right object's mailbox in a fixture run.",
  "owner": "2.0.0_SA_COO~CA",
  "round": "v2",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~CA",
   "round": "v2"
  },
  "closed": false
 },
 {
  "id": "COMM_ASSIST-W8-S9",
  "project": "COMM_ASSIST",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "muse answers by writing a file into the reader folder, but refresh.py writes only its six fixed names and no answers/ location; CA-h-2's report confirms none exists on dell2.",
  "evidence": [
   "org/missions/D9/COMM/COMM_ASSIST/surprise-channel/investigations/INVESTIGATION_v1.md row W8-S9",
   "deliverables/0.7.0_AE_CloudOps~CA2/REPORT_TO-CA-h-2.md (no answers folder, forwarder or SQS send)",
   "adjudication row COMM_ASSIST-C-S4"
  ],
  "remedy": "P3. Round-17 cell, with the forwarder: create <reader root>/answers/ and answers/done/, writable by the account muse uses. Done when the folder exists on dell2 and the refresh job leaves it untouched across one fire.",
  "owner": "2.0.0_SA_COO~CA",
  "round": "v2",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~CA",
   "round": "v2"
  },
  "closed": false
 }
]
```

-- 3.0.0_SA_CVO~L
