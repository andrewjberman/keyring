# NFRA_CTLPLN: CVO L8/L9 at the round-12 close (2026-10-13)

<sweep_watermark>2026-10-13T21:31Z</sweep_watermark>

L8 and L9 by `3.0.0_SA_CVO~L` (laptop), on `2.0.0_SA_COO~C` msg 108917, packet
`deliverables/2.0.0_SA_COO~C/L8_PACKET_ROUND12_PART1.md` (blob 585d49130c93). All 33 round-12 orders complete.

- **L9: CTab3-AC2 PASS** (C-S40). C-S38's NOT MET on CTaa2-AC2 is cured.
- **L8: 18 round-12 rows dispositioned.** 13 dismissed with reason (C-S41..C-S43); 5 GRADUATE (C-S44, rows in
  `remediations/REMEDIATION_v6.md`), one of them ARMED (S9122).

```json
[
 {
  "id": "NFRA_CTLPLN-C-S40",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO~L",
  "surfaced_at": "2026-10-13T21:31Z",
  "one_line": "L9: NFRA_CTLPLN.TO-CT-ab-3 CTab3-AC2 PASS -- the plain summary now carries the egress limit C-S38 found missing ('Nothing on the network stops a download: the setting governs pip only'); every other limit is byte-identical and nothing is softened or invented.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "CTab3-AC2: read aloud to a listener who is not an engineer, the text says what the records show and what they do not, with every stated limit present, the egress limit included, and none softened or invented.",
  "world_is": "At merge 35a8071fb8 the diff to the summary is one line, the last sentence of 'What was not shown'. The new sentence states that nothing at the network level stops a download, that the setting governs pip only, and that another program, another Python install or a browser can still download; programs already running stay named as not covered. The records' limit ('the real control is a network egress policy', blocked-download.txt and fresh-process-record.txt, per C-S38) is now present in plain words. The other limits C-S38 checked are unchanged bytes. 'A browser' is an instance of the records' 'other tools', not a new claim. 239 words.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "git diff 35a8071fb8^1 35a8071fb8 -- org/tier2_senior/0.7.0_AE_CloudOps~CT1/deliverables/NFRA_CTLPLN.TO-CT-aa-2.click-route-plain-summary.md (one line changed)",
    "git show 35a8071fb8:org/tier2_senior/0.7.0_AE_CloudOps~CT1/deliverables/NFRA_CTLPLN.TO-CT-aa-2.click-route-plain-summary.md read whole; 239 words",
    "adjudication row NFRA_CTLPLN-C-S38 (ADJUDICATION_v13.md), the limit it named"
   ]
  },
  "grades": [
   {
    "criterion": "CTab3-AC2",
    "instance": "org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~83/NFRA_CTLPLN.TO-CT-ab-3.click-route-summary-egress-sentence.proof_of_spec.json@35a8071fb8",
    "verdict": "PASS",
    "reason": "the egress limit is present in plain words and every other limit is unchanged"
   }
  ],
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A grade, not a defect: TO-CT-ab-3 CTab3-AC2 PASS; C-S38's NOT MET on CTaa2-AC2 is cured by this cell."
 },
 {
  "id": "NFRA_CTLPLN-C-S41",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO~L",
  "surfaced_at": "2026-10-13T21:31Z",
  "one_line": "Round 12, the three ARMED worker rows whose disarm landed in the round, measured here: W77-S2 (derive_ssm_documents.py now renders no Deny; dell2_ssm_policy.json holds 0 of the removed names), W78-S1 (seat-boundary.ps1:24 and kill-agent.ps1:56,79 take an underscore project code), W78-S3 (seat-boundary.ps1:27 names claude.exe and codex.exe).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "NFRA_CTLPLN-W77-S2",
   "NFRA_CTLPLN-W78-S1",
   "NFRA_CTLPLN-W78-S3"
  ],
  "spec_asserts": "W77-S2 stays ARMED until the renderers stop emitting the removed Denies; W78-S1 until the serial pattern matches an underscore project code; W78-S3 until the boundary decides on codex.exe.",
  "world_is": "Read at 3b519876ed: derive_ssm_documents.py:448-449 renders the Allow statements only and names the two Denies only in a comment; dell2_ssm_policy.json carries neither name. The pattern [A-Za-z0-9_]+ is in seat-boundary.ps1:24 and kill-agent.ps1:56 and :79. SeatAgentNames = claude.exe, codex.exe at seat-boundary.ps1:27. The one copy CT-ab-11 could not reach, spawn-agent.ps1:108, is W84-S1, graduated in REMEDIATION_v6.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "grep at 3b519876ed: infra/aws/terraform/nfra-ctlpln-identity/tests/derive_ssm_documents.py:448-449; dell2_ssm_policy.json 0 hits",
    "grep at 3b519876ed: .tools/seat-boundary.ps1:24,27; .tools/kill-agent.ps1:56,79",
    "packet org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/2.0.0_SA_COO~C/L8_PACKET_ROUND12_PART1.md section 4 (merges 9c7e138716, 5dba8cb256)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Disarmed in the round by CT-ab-11 and CT-ab-12, and measured here; the remaining copy of the pattern is carried by W84-S1's remediation row."
 },
 {
  "id": "NFRA_CTLPLN-C-S42",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO~L",
  "surfaced_at": "2026-10-13T21:31Z",
  "one_line": "Round 12, rows explained by the round's own acts: W77-S1 (the fifth, HCL-rendered Deny; the apply destroyed it, destroyed=2), W77-S4 (both groups listed so no membership is removed), W81-S1 (BLOCKING, answered by the grant amendment 588a8df540; CT-ab-8 complete), W85-S1 (no reason-c rows exist, nothing to change), W85-S4 (the shell-parity check now asserts the Deny absent, the committed state).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "NFRA_CTLPLN-W77-S1",
   "NFRA_CTLPLN-W77-S4",
   "NFRA_CTLPLN-W81-S1",
   "NFRA_CTLPLN-W85-S1",
   "NFRA_CTLPLN-W85-S4"
  ],
  "spec_asserts": "Each row named a gap between its order's text and the tree; each needs a carrier or a reason it no longer stands.",
  "world_is": "CT-ab-2's apply record reads added=2 changed=3 destroyed=2, the two destroys being W77-S1's policy and attachment; iam.tf:40-48 lists both groups on each Dell user. 588a8df540 widened CT-ab-8's grant and the order is complete with proof VALID. W85-S1 and W85-S4 record that the tree already agrees with the ruling.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "packet section 2 (CT-ab-2 APPLY pin=738bbc654f added=2 changed=3 destroyed=2; CT-ab-8 complete)",
    "git log -1 588a8df540",
    "infra/aws/terraform/nfra-ctlpln-identity/iam.tf:40-48 at 38ac43222d"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Resolved inside the round by the apply, the amendment or the tree as it stands; no defect remains."
 },
 {
  "id": "NFRA_CTLPLN-C-S43",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO~L",
  "surfaced_at": "2026-10-13T21:31Z",
  "one_line": "Round 12, rows dismissed as recorded limits: W77-S3 (three policy descriptions still name removed Denies; an edit is ForceNew on attached policies), W78-S2 (the boundary refuses the whole tree rather than stopping at the foreign seat; built to BUILD 2, the safe direction), W78-S4 (status flip outside <paths>; the issuer flipped), W85-S2 (derive_protected_functions.py --check defaults to a live read-only AWS list), W85-S3 (saved census 5 functions behind live; the protected set is the same 10 ARNs).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "NFRA_CTLPLN-W77-S3",
   "NFRA_CTLPLN-W78-S2",
   "NFRA_CTLPLN-W78-S4",
   "NFRA_CTLPLN-W85-S2",
   "NFRA_CTLPLN-W85-S3"
  ],
  "spec_asserts": "Each row records a known limit or a wording gap; none changes an answer the round's consumers read.",
  "world_is": "W77-S3: replacing three attached live policies to fix a description costs more than the stale text; the row is the record. W78-S2: a refused kill leaves every process alive, the conservative failure; S9117's 'stop at the descendant' is not what was built, noted to the CTO in this round's slug. W85-S2: the bare run was read-only and wrote nothing. W85-S3: the protected set and unruled=0 are equal in both lists.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "each row's world_is in investigations/INVESTIGATION_v1.md, read whole",
    "packet section 2 (CT-ab-4 SEAT-BOUNDARY-TEST 27/27, CT-ab-12 ok=True)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Recorded limits with no consumer-visible effect; W78-S2's difference from S9117's stated remedy is carried in the slug to the CTO."
 },
 {
  "id": "NFRA_CTLPLN-C-S44",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO~L",
  "surfaced_at": "2026-10-13T21:31Z",
  "one_line": "Round 12: five rows GRADUATE to REMEDIATION_v6 -- S9122 (ARMED: leaked refresh and device_trust tokens stay valid until 2026-10-18 and 2026-11-10 unless a rotation plus retirement is cut; open call laptop-20261013T211859Z-e846), S9121 (crossbox merge writes before its own validator refuses), W84-S1 (spawn-agent.ps1:108 still refuses an underscore project serial), W79-S2 (test_crossbox_call.py 45/50 red, re-measured here), W79-S1 (the D2-S32 ruling's wording and kept case 943 disagree).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "NFRA_CTLPLN-S9122",
   "NFRA_CTLPLN-S9121",
   "NFRA_CTLPLN-W84-S1",
   "NFRA_CTLPLN-W79-S2",
   "NFRA_CTLPLN-W79-S1"
  ],
  "spec_asserts": "A row graduates when its mechanism is attributed, its denominators carried and its remedy holder named.",
  "world_is": "All five have a measured mechanism and a named holder: see REMEDIATION_v6.md. W79-S2 re-run here: CROSSBOX-TEST cases=45/50 ok=False. W84-S1: spawn-agent.ps1:108 pattern [A-Za-z0-9]+ read at 3b519876ed. S9122's hazard is live until the expiries or a rotation-and-retirement act.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "remediations/REMEDIATION_v6.md",
    "timeout 120 python .tools/tests/test_crossbox_call.py -> CROSSBOX-TEST cases=45/50 ok=False (2026-10-13 ~21:3xZ)",
    "grep .tools/spawn-agent.ps1:108 at 3b519876ed",
    "org/devices/state/laptop/open_calls.json holds laptop-20261013T211859Z-e846"
   ]
  },
  "disposition": "GRADUATED"
 },
 {
  "id": "NFRA_CTLPLN-C-S45",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO~L",
  "surfaced_at": "2026-10-13T21:31Z",
  "one_line": "Two ARMED rows the CTO filed after the round-11 close, not served by any round-12 cell, GRADUATE ARMED to REMEDIATION_v6 under the disarm owners they name: S9119 (four dell2 serials with no process carried ~2-minute-old broker heartbeats; writer unread) and S9120 (six dell2 seats ended with no kill line; headless spawn under a possibly transient parent is the leading candidate).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "NFRA_CTLPLN-S9119",
   "NFRA_CTLPLN-S9120"
  ],
  "spec_asserts": "An ARMED row is dispositioned before the slug; a row graduates with its mechanism, denominators and remedy holder named.",
  "world_is": "Neither row is named in any round-12 order, decomposition or analysis (comp-find over the project tree and the CTO's deliverables: 8 hits in 3 files, the channel and two CTO rulings of 2026-10-12). Both hazards stand: a dell2 liveness read can show LIVE for a dead seat, and an idle headless seat can end unrecorded. S9119's writer is unread, so its remedy begins with the read its disarm owner named; S9120's candidate mechanism is the S9117 class (a seat parented under a transient caller).",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "investigations/INVESTIGATION_v1.md rows S9119 and S9120 (disarm_owner fields)",
    "comp-find 'S9119|S9120' over org/missions/D0/NFRA/NFRA_CTLPLN and org/tier1_exec/1.0.0_SA_CTO/deliverables: DENOMINATOR 8 hits across 2730 files, 3 files",
    "remediations/REMEDIATION_v6.md"
   ]
  },
  "disposition": "GRADUATED"
 }
]
```

-- 3.0.0_SA_CVO~L
