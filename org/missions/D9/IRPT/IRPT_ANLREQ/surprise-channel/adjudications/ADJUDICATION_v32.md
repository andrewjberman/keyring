# IRPT_ANLREQ: CVO dispositions on the CTO's four requests (msg 20261021T164401Z): W55-S25, W155-S3, W285-S1 DISARMED; W92-S2 DISMISSED

<sweep_watermark>2026-10-21T16:55Z</sweep_watermark>

Author: 3.0.0_SA_CVO~DELL2, 2026-10-21.

**Basis.** Dispositions by `3.0.0_SA_CVO~DELL2`, 2026-10-21T16:55Z, on `1.0.0_SA_CTO~DELL2`'s requests
`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_DISARM_REQUESTS_IRPT_ANLREQ_ROUND60_FOUR_ROWS_20261021.md` @6e5b8afbd8. The CTO is the
disarm owner of all four rows. Each named read was re-run by this seat:

- **W55-S25:** `python -m pytest -q intake/tests/test_correction_words.py` in `infra/aws/lambda/investor-reporting`, at box/dell2
  HEAD, prints `9 passed`.
- **W155-S3:** IB2's receipt `irpt_anlreq_commentary_e2e7n/A_E2E7N.txt`.
  - Line 2: `A mint ok name=E2E7N SYNTHETIC FILER at 15:02:57Z`.
  - Line 9: `P4 packager outcome=ATTACHED at 15:07:08Z`.
  - This seat also read packager ATTACHED in the 7K and 7M packets (v30, v31).
- **W285-S1:** `git -C portal grep -l -i "meeting request" origin/PROD -- src` at origin/PROD `234cddba` lists
  `MeetingRequestParts.tsx`, `TicketCenter.tsx`, `api/endpoints/tickets.ts` and the `meeting-request` and
  `meeting-outcome-visibility` tests.
- **W92-S2:** a premise superseded by ruling.
  - Andrew-direct 2026-10-14 made the Ticket Center Opal-only.
  - Andrew-direct 2026-10-19 made the filer Opal staff, filing for any firm. That word is also the basis of TCKT_VNEXT ADJUDICATION_v21's
    FWD-2 grade.
  - A partner human's refusal at CREATE is now the intended behaviour.

**Still ARMED and BLOCKING after this file: 10.**
- `2.0.0_SA_COO~Y2`: W62-S5, W166-S1, W297-S1, W306-S1, W309-S2, W313-S1, W369-S1.
- `2.0.0_SA_COO~G2`: S29.
- `2.0.0_SA_COO~T2`: W225-S1.
- `2.0.0_SA_COO~P2` with `~Y2`: W55-S5.

The round-60 slug waits on them.

```json
[
 {
  "id": "IRPT_ANLREQ-D2-C-S11",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~DELL2",
  "surfaced_at": "2026-10-21T16:55:00Z",
  "one_line": "DISARMS IRPT_ANLREQ-D2-W55-S25: the correction-words reader test that failed on the st32-era package passes at box/dell2 HEAD (9 passed); the held-member ruling was overtaken by the later status releases.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": ["IRPT_ANLREQ-D2-W55-S25"],
  "spec_asserts": "W55-S25 (BLOCKING, ARMED): the release uploads.py declares 24 correction words that the st32 ops/status.py does not; AC1 not met.",
  "world_is": "infra/aws/lambda/investor-reporting: python -m pytest -q intake/tests/test_correction_words.py -> 9 passed (this seat, 2026-10-21 ~16:50Z).",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_DISARM_REQUESTS_IRPT_ANLREQ_ROUND60_FOUR_ROWS_20261021.md section 1 @6e5b8afbd8",
    "pytest re-run by this seat: 9 passed"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "DISARMED: the two word lists agree in the tree the resident releases are built from; the named test passes."
 },
 {
  "id": "IRPT_ANLREQ-D2-C-S12",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~DELL2",
  "surfaced_at": "2026-10-21T16:55:00Z",
  "one_line": "DISMISSES IRPT_ANLREQ-D2-W92-S2: a partner-firm advisor refused at CREATE is the intended behaviour since Andrew's Opal-only (2026-10-14) and staff-filer (2026-10-19) words; partner self-filing would be a new outcome on a PRD addendum.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": ["IRPT_ANLREQ-D2-W92-S2"],
  "spec_asserts": "W92-S2 (BLOCKING, ARMED): a partner-firm advisor's Analysis Request is refused at CREATE (403), so no request-id fix reaches that advisor's ticket.",
  "world_is": "The Ticket Center is Opal-only and the filer is Opal staff naming the Advisor (Andrew-direct 2026-10-14 and 2026-10-19); every live run since files as a staff principal and reaches READY.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_DISARM_REQUESTS_IRPT_ANLREQ_ROUND60_FOUR_ROWS_20261021.md section 2 @6e5b8afbd8",
    "org/missions/D7/TCKT/TCKT_VNEXT/surprise-channel/adjudications/ADJUDICATION_v21.md (the same two words, read for FWD-2)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Premise superseded by Andrew's rulings; not a loss in the product as now specified."
 },
 {
  "id": "IRPT_ANLREQ-D2-C-S13",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~DELL2",
  "surfaced_at": "2026-10-21T16:55:00Z",
  "one_line": "DISARMS IRPT_ANLREQ-D2-W155-S3: each live run mints its owner row before filing and the packager then reads ATTACHED (7N receipt lines 2 and 9; 7K and 7M packets).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": ["IRPT_ANLREQ-D2-W155-S3"],
  "spec_asserts": "W155-S3 (BLOCKING, ARMED): the packager stops at CurrentAuthorityRefused ACTOR_NOT_FOUND while the synthetic owner's user row is absent.",
  "world_is": "A_E2E7N.txt:2 'A mint ok name=E2E7N SYNTHETIC FILER at 15:02:57Z'; :9 'P4 packager outcome=ATTACHED at 15:07:08Z'.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/tier2_senior/0.7.0_AE_CloudOps~IB2/deliverables/irpt_anlreq_commentary_e2e7n/A_E2E7N.txt lines 2 and 9",
    "org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/adjudications/ADJUDICATION_v31.md (7M packager ATTACHED)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "DISARMED: the authority path is exercised live with the owner row present; a real staff owner always has one."
 },
 {
  "id": "IRPT_ANLREQ-D2-C-S14",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~DELL2",
  "surfaced_at": "2026-10-21T16:55:00Z",
  "one_line": "DISARMS IRPT_ANLREQ-D2-W285-S1: the meeting-request form is on portal origin/PROD 234cddba (MeetingRequestParts.tsx, TicketCenter.tsx, tickets.ts and its tests), so the recut that omitted it is superseded.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": ["IRPT_ANLREQ-D2-W285-S1"],
  "spec_asserts": "W285-S1 (BLOCKING, ARMED): the AR-y-385 PROD recut leaves the approved meeting-request form out whole.",
  "world_is": "git -C portal grep -l -i 'meeting request' origin/PROD -- src at 234cddba lists src/pages/TicketCenter/MeetingRequestParts.tsx, TicketCenter.tsx, src/api/endpoints/tickets.ts, __tests__/meeting-request.test.tsx, __tests__/meeting-outcome-visibility.test.tsx.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_DISARM_REQUESTS_IRPT_ANLREQ_ROUND60_FOUR_ROWS_20261021.md section 4 @6e5b8afbd8",
    "portal origin/PROD 234cddba grep re-run by this seat"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "DISARMED: the form reached PROD by a later release."
 }
]
```

-- `3.0.0_SA_CVO~DELL2`
