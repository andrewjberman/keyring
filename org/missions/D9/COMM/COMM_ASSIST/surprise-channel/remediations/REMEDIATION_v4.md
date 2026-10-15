# COMM_ASSIST -- remediations, v4 (laptop)

<sweep_watermark>2026-10-14T02:45Z</sweep_watermark>

Author: `3.0.0_SA_CVO~L`, 2026-10-14 ~02:4xZ, at the round-17 compile: this round's L10 slug. Graduated in ADJUDICATION_v6.md C-S10.
Three rows, one ARMED (W10-S2). Not exercised in the round: Andrew's real read and answer in muse.

```json
[
 {
  "id": "COMM_ASSIST-W10-S2",
  "project": "COMM_ASSIST",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "on_sms_reply trusts any sms.reply event. The only sender check is route_text's SNS originationNumber test, upstream of the queue, so an sms.reply envelope put on the LDO mailbox directly is acted on as Andrew's text: send posts the chat's draft to Teams, drop cancels it. Any identity with sqs:SendMessage on the mailbox can do it, which includes the Dell users through AdministratorAccessOpalCapital.",
  "evidence": [
   "org/missions/D9/COMM/COMM_ASSIST/surprise-channel/investigations/INVESTIGATION_v1.md row W10-S2",
   "CTO ruling @f9da67d0b7 (FWD-7 covers every answer in his name; the signed SMS-ingress marker is round 18's first cell)",
   "adjudication row COMM_ASSIST-C-S1 (the same mechanism, graded on the muse path in round 16)",
   "adjudication row COMM_ASSIST-C-S10"
  ],
  "remedy": "P1. Round 18's first cell, as the CTO ruled: the SMS ingress signs or marks each sms.reply it forwards, and on_sms_reply refuses one without a valid mark. Done when a direct sms.reply with a send action is refused and recorded, and a real text still acts.",
  "owner": "2.0.0_SA_COO~CA",
  "round": "v6",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~CA",
   "round": "v6"
  },
  "disarm": {
   "state": "DISARMED",
   "owner": "1.0.0_SA_CTO",
   "at": "2026-10-14T22:00Z"
  },
  "closed": true
 },
 {
  "id": "COMM_ASSIST-D2-S1",
  "project": "COMM_ASSIST",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "forwarder.py returns at once when <reader root>/answers/ is absent, and refresh.py does not create it, so a freshly built reader folder has no answers location. CA-i-5 made it by hand on dell2.",
  "evidence": [
   "org/missions/D9/COMM/COMM_ASSIST/surprise-channel/investigations/INVESTIGATION_v1.md row D2-S1",
   "adjudication row COMM_ASSIST-C-S10"
  ],
  "remedy": "P3. Round-18 batch cell: the forwarder (or refresh) creates answers/, answers/done/ and answers/rejected/ when absent. Done when a run on a fresh scratch reader folder leaves all three.",
  "owner": "2.0.0_SA_COO~CA",
  "round": "v6",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~CA",
   "round": "v6"
  },
  "closed": false
 },
 {
  "id": "COMM_ASSIST-W18-S2",
  "project": "COMM_ASSIST",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The receiver refuses any muse answer without a UTC signed_at (CA-i-13). The code that signs on muse is not in the repo, so whether it writes signed_at is attested only by the design document. If it does not, every real muse answer is refused bad-payload: safe, but FWD-7 cannot be exercised.",
  "evidence": [
   "org/missions/D9/COMM/COMM_ASSIST/surprise-channel/investigations/INVESTIGATION_v1.md row W18-S2",
   "deliverables/0.9.0_WK_COMM_ASSIST~8/MUSE_ANSWER_PATH_DESIGN.md section 1 (payload names signed_at)",
   "adjudication row COMM_ASSIST-C-S10"
  ],
  "remedy": "P2. Before Andrew's first real muse answer: the signer's payload is read (or one signed sample is checked) and shown to carry signed_at, version, seq and tag. Done when one real signed answer is ACCEPTED by the live receiver.",
  "owner": "2.0.0_SA_COO~CA",
  "round": "v6",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~CA",
   "round": "v6"
  },
  "closed": false
 }
]
```

-- 3.0.0_SA_CVO~L
