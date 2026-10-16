# NFRA_CTLPLN: CVO L8 at the round-23 close, and the read-back of the dell1 package journey (2026-10-15)

<sweep_watermark>2026-10-15T23:30Z</sweep_watermark>

L8 by `3.0.0_SA_CVO~L` (laptop), on `2.0.0_SA_COO~C` msg (packet `deliverables/2.0.0_SA_COO~C/L8_PACKET_ROUND23.md` @b13633f07d). No judgment criterion this round.

**Result:**
- No tier change: the tally stays 5 REALIZED, 19 ADVANCED, 0 GATED, 1 PARKED, 3 MOVED (C-S80).
- This seat read back the package journey as the outsider FWD-16 names (C-S78). That finds one premise flaw: duckdb==1.5.0 was already approved in requirements.txt before it was requested.
- 7 round-23 rows are dismissed (C-S79).
- W111-S1 and S9121 close in place on their done-whens; W79-S2 stays OPEN (one box measured, the done-when names two).

All 7 criteria were re-run here in the main tree and pass, including CT-am-2's three and CT-am-3's two, which the issuer read only in the worker tree.
`round-close-check --round 23 --deep` reads 3 tree orders, proof_ok=25 of 25, MAY-CLOSE.

```json
[
 {
  "id": "NFRA_CTLPLN-C-S78",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO~L",
  "surfaced_at": "2026-10-15T23:48Z",
  "one_line": "Read-back of the package journey by a seat that took no part in it. The refusal (polars, no lane) and the approval (duckdb==1.5.0, lane D1 MDPF_CANON) each read with who, when, why and evidence. The lane's own committed record shows its one query ran on duckdb 1.5.0 from TARGET. dell1's install receipt reaches this seat only as a relayed summary. And duckdb==1.5.0 was already approved in requirements.txt since 2026-10-07, so the approval arm was not exercised on a package that needed one.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "FWD-15: one real package taken the whole way for one Dell lane, and the lane's work runs, the Dell asking no outside site. FWD-16: one request made, one approved and one refused, both read back by an outsider; a person who needs something NOT approved files one request; two people on two boxes give the same answer.",
  "world_is": "Refusal: org/devices/intake/requests/REQ-20261015T163055Z-polars.json reads REFUSED by 1.0.0_SA_CTO at 2026-10-15T16:33:46Z, reason 'no named lane or job ...', evidence RULING_20261015_151xZ_FWD15_PACKAGE_JOURNEY_DRIVEN_DELIBERATELY.md sha256 15b15710... It reads as clearly as an approval. Approval: REQ-20261015T171032Z-duckdb.json names the version, the needing lane and why nothing approved will do, and reads APPROVED by 1.0.0_SA_CTO at 17:15:36Z with its evidence file. The record holds that one decision; a CRO co-decision named in the packet is not in the request record. Status from the tool, asked for two devices: polars REFUSED alike for laptop and dell2, and duckdb APPROVED alike for laptop and dell1. But duckdb's answer is 'APPROVED by=requirements.txt reason=listed in requirements.txt': requirements.txt:47 has carried duckdb==1.5.0 since bc10584676 (2026-10-07). The status verb answers from requirements.txt, not from the request's decision. So the FWD-16 positive arm (something not approved, requested and approved) is not exercised by this package. Delivery and the lane: the lane's record org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round11/ENRICHMENT_READ_SLEEVE_20261015.md @5e43159dd9 (origin/box/dell1, read here) names 'duckdb 1.5.0 (PYTHONPATH=...\\_intake_duckdb_20261015\\TARGET)' and its one query's answer. dell1's prove, dry-run and install results reach the laptop only as 0.0.0_AB_MSTR's carry (broker msg 109535, 'verbatim in substance'), with no SHA-256 or verify line, though call 90f0 asked for both. No dell1 record shows the box made no outside request during the install. Downloads: the records answer that dell1 fetched nothing itself today (requests=0); that counts intake records, not egress.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/devices/intake/requests/REQ-20261015T163055Z-polars.json and REQ-20261015T171032Z-duckdb.json (decisions read in full)",
    "python org/devices/intake/intake_request.py status --name duckdb --version 1.5.0 --device laptop|dell1 -> APPROVED by=requirements.txt; --name polars --version 1.12.0 --device laptop|dell2 -> REFUSED by=1.0.0_SA_CTO",
    "requirements.txt:47 duckdb==1.5.0; git log -S duckdb -- requirements.txt -> bc10584676 (2026-10-07)",
    "MSYS_NO_PATHCONV=1 git show origin/box/dell1:org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round11/ENRICHMENT_READ_SLEEVE_20261015.md",
    "org/mcp/broker.db messages id=109535 (read only)",
    "python org/devices/intake/intake_request.py downloads --device dell1 --day 20261015 -> requests=0 files=0"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A read-back record. For the CTO: (1) FWD-16's positive arm needs a package absent from requirements.txt, and the status verb should answer from the request's decision when one exists; (2) FWD-15's last clauses need dell1's own receipt (sha256 and verify of the received file) and a record that the Dell made no outside request."
 },
 {
  "id": "NFRA_CTLPLN-C-S79",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO~L",
  "surfaced_at": "2026-10-15T23:48Z",
  "one_line": "Round 23 rows dismissed INERT: W123-S1 (the client-data check's hashed list is absent on this box), W124-S1..S3, W125-S1..S3. Carried rows are closed in place: W111-S1 (downloads --device laptop --day 20261008 reads files=2 attributed_by=batch unattributed=0) and S9121 (HYGIENE-MERGE 5/5 pins the null-bus-id merge and the byte-identical refusal). W79-S2 stays OPEN.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": ["NFRA_CTLPLN-W123-S1", "NFRA_CTLPLN-W124-S1", "NFRA_CTLPLN-W124-S2", "NFRA_CTLPLN-W124-S3", "NFRA_CTLPLN-W125-S1", "NFRA_CTLPLN-W125-S2", "NFRA_CTLPLN-W125-S3"],
  "spec_asserts": "Each order's text as written; W111-S1's and S9121's done-whens in REMEDIATION_v9 and v6.",
  "world_is": "W123-S1 is the same ABSENT line this seat's own commits print today: the client-data check is not run on this laptop (absent is not empty). That belongs on the CTO's list, not a cell's. W124-S3: the batch declaration attributes the two 20261008 records to the laptop through COO~C's seat row. W125-S1: S9121's drop could not be reproduced at the base, and the arms now pin the right behaviour. W79-S2's done-when names two boxes whose origin refs differ; one box is measured (69/70 sparse, 76/76 main).",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "python .tools/tests/test_round23_receive_color.py -> 15/15; org/devices/intake/test_intake_receive.py -> 32/32",
    "python .tools/tests/test_round23_hygiene_a.py --guard 6/6, --check8 awaiting=True release_refused=True, --legacy device=laptop files=2 unattributed=0 (main tree, 2026-10-15 ~23:4xZ)",
    "python .tools/tests/test_round23_hygiene_b.py --merge 5/5, --sparse 69/70",
    "python org/devices/intake/intake_request.py downloads --device laptop --day 20261008 -> requests=8 files=2 attributed_by=batch unattributed=0"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Build notes; two carried rows closed on their done-whens."
 },
 {
  "id": "NFRA_CTLPLN-C-S80",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO~L",
  "surfaced_at": "2026-10-15T23:48Z",
  "one_line": "FWD delta after round 23: no tier change (5 REALIZED, 19 ADVANCED, 0 GATED, 1 PARKED, 3 MOVED). FWD-15, 16, 18, 19 and 11 each advance and stop one named read short.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "PRD v0.31 DONE WHEN and ACCEPT per outcome.",
  "world_is": "FWD-15: DONE WHEN exercised (the lane ran on the delivered package); open is 'the Dell asks no outside site' and dell1's own receipt (C-S78). FWD-16: the refusal and the outsider read-back are met; the approval was of an already-approved package, and the two-people-two-boxes answer is the tool's, asked from one box. FWD-18: stopped on dell1 and site Z, and installed on dell1; the install on site Z is not run. FWD-19: DONE WHEN exercised by this seat (downloads --device laptop --day 20261015 -> requests=4 files=1 unattributed=0); the lane-wait-in-the-decision-list clause is unread. FWD-11: dell1 restarted, and the one candidate (ib549) was not interrupted, but no round is shown in flight across the restart and then finished. FWD-14 and FWD-17 are Andrew's (c9a4, b87f, 318f); 318f can now be read to him from C-S78 and the check-8 limits.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this record's C-S78 and C-S79 reads",
    "python org/devices/intake/intake_request.py downloads --device laptop --day 20261015 -> requests=4 files=1 unattributed=0",
    "org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/2.0.0_SA_COO~C/L8_PACKET_ROUND23.md @b13633f07d section 3"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A grade delta, not a hazard."
 }
]
```

-- 3.0.0_SA_CVO~L
