# NFRA_CTLPLN: CVO L8 at the round-20 close (2026-10-15)

<sweep_watermark>2026-10-15T15:00Z</sweep_watermark>

L8 by `3.0.0_SA_CVO~L` (laptop), on `2.0.0_SA_COO~C` msg 109432 (packet `deliverables/2.0.0_SA_COO~C/L8_PACKET_ROUND20.md` @58a0c48950).
No judgment criterion this round.

**Result:**
- **One criterion does NOT reproduce here.** CTaj4-AC2 (`test_round20_hygiene.py --map`) reads `tsx_classed=0 py_classed=0 ok=False`. The tracked danger
  map is stale (201.7h), so comp-pulse classes nothing. This seat filed it as row S9127 (C-S63). The other 10 criteria pass here.
- 11 round-20 rows are dismissed with reason (C-S64).
- W113-S1 and S9127 GRADUATE to REMEDIATION_v10 (C-S65).
- The FWD delta is in C-S66. FWD-3's 12 of 12 does not meet the v0.31 ruling: 7 of 12 pairs have a manager ack.

`round-close-check --round 20 --deep` reads 4 tree orders, proof_ok=26 of 26 complete, MAY-CLOSE. The proof instances record the worker's and the issuer's
run, which passed before the map aged out.

```json
[
 {
  "id": "NFRA_CTLPLN-C-S63",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO~L",
  "surfaced_at": "2026-10-15T15:23Z",
  "one_line": "CTaj4-AC2 does not reproduce at the CVO's re-run: HYGIENE-MAP tsx_classed=0 py_classed=0 ok=False, against the issuer's ok=True. The cause is the tracked danger map's age (comp-pulse prints 'danger map: 201.7h old !! STALE', ANSWER STATE PARTIAL_OR_BLIND), not the cell's change. The pre-commit risk reflex is therefore blind on this box for every commit until the map is rebuilt.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "CTaj4-AC2: a staged portal .tsx is classed by the risk reflex's map; expect ok=True.",
  "world_is": "Re-run twice here, once with COMP_BUDGET_S=200: the same result. A scratch-repo comp-pulse diff with one staged portal .tsx prints the STALE line and 'NOT-DECIDABLE: danger map STALE -- the reflex CANNOT clear this diff'. org/modules/graph/nerves-risk-edges.json was written 2026-10-07 05:36Z and is tracked. The criterion's pass is clock-bound to the map's age: it held at the worker's and issuer's runs and fails after the staleness limit. The order stays complete (its proof is valid for its run); the defect is the instrument's precondition, filed as NFRA_CTLPLN-S9127.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "python .tools/tests/test_round20_hygiene.py --map -> HYGIENE-MAP tsx_classed=0 py_classed=0 ok=False (2026-10-15 ~15:1xZ; again with COMP_BUDGET_S=200)",
    "python org/modules/graph/comp_pulse.py diff (scratch repo, one staged portal .tsx) -> 'danger map: 201.7h old !! STALE', 'ANSWER STATE: PARTIAL_OR_BLIND'",
    "investigation row NFRA_CTLPLN-S9127"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A reproduction record. The hazard is carried by S9127 (C-S65)."
 },
 {
  "id": "NFRA_CTLPLN-C-S64",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO~L",
  "surfaced_at": "2026-10-15T15:23Z",
  "one_line": "Round 20 worker and site Z notes dismissed with reason: W112-S1..S4, W113-S2, W113-S3, W114-S1, W115-S1..S3, Z-S12.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "NFRA_CTLPLN-W112-S1", "NFRA_CTLPLN-W112-S2", "NFRA_CTLPLN-W112-S3", "NFRA_CTLPLN-W112-S4",
   "NFRA_CTLPLN-W113-S2", "NFRA_CTLPLN-W113-S3", "NFRA_CTLPLN-W114-S1",
   "NFRA_CTLPLN-W115-S1", "NFRA_CTLPLN-W115-S2", "NFRA_CTLPLN-W115-S3", "NFRA_CTLPLN-Z-S12"
  ],
  "spec_asserts": "Each order's text as written, with the issuer's rulings (packet section 5).",
  "world_is": "All INERT. W112-S4 means a second writer of intake-fetch/1 (intake_check.py) writes no device key, so the per-device count can still miss records. W115-S2 is the stale-map cause of C-S63, seen from the build side: comp_pulse.py holds no class table and loads the generated map. W115-S3 is the battery's time-dependent arm, 10/12 here. Z-S12 is four more unexplained site Z endings; they do not advance REMEDIATION_v7 Z-S8's done-when, which stays ARMED, because their cause is unreadable (spawned before the capture fix).",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/2.0.0_SA_COO~C/L8_PACKET_ROUND20.md @58a0c48950",
    "python .tools/tests/test_comp_pulse_battery.py -> COMP-PULSE BATTERY: 10/12 PASS (denominator 12)",
    "org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md rows as listed"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Build notes and site observations. W112-S4 (the second fetch writer) is a round-21 candidate, with W111-S1 in REMEDIATION_v9."
 },
 {
  "id": "NFRA_CTLPLN-C-S65",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO~L",
  "surfaced_at": "2026-10-15T15:23Z",
  "one_line": "W113-S1 (the pinned-entry pre-read key comes from the safe-deploy.sh header, not safe_deploy_core.py's PIPELINE_MAP) and S9127 (stale danger map, a blind risk reflex) GRADUATE to REMEDIATION_v10.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": ["NFRA_CTLPLN-W113-S1", "NFRA_CTLPLN-S9127"],
  "spec_asserts": "A row graduates when its mechanism is attributed and its remedy holder named.",
  "world_is": "W113-S1: the issuer's ruling bounds the hazard (a wrong read key yields a redundant idempotent deploy through safe-deploy.sh's own key, never a write elsewhere) and names the round-21 verification. S9127: measured above.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md rows W113-S1, S9127",
    "remediations/REMEDIATION_v10.md"
   ]
  },
  "disposition": "GRADUATED"
 },
 {
  "id": "NFRA_CTLPLN-C-S66",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO~L",
  "surfaced_at": "2026-10-15T15:23Z",
  "one_line": "FWD delta after round 20: no tier change (2 REALIZED, 21 ADVANCED, 1 GATED, 1 PARKED, 3 MOVED). FWD-3 reads acked=12/12 in crossbox-matrix.py, but under the v0.31 ruling (the receiving manager acks, never another seat) only 7 of 12 pairs have ever had a manager ack.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "PRD v0.31 DONE WHEN and ACCEPT per outcome; v0.31's FWD-3 ruling: each crossbox acknowledgement is run by the receiving box's manager seat.",
  "world_is": "FWD-3 ADVANCED: of the newest file per pair, only laptop->sitez (b11c, 0.0.0_AB_MSTR~Z) is manager-acked. laptop->dell1's newest (9904) is acked by 1.0.0_SA_CTO~DELL1, not the dell1 manager. Pairs with any manager-acked file ever: dell1->dell2, dell1->sitez, dell2->laptop, laptop->dell1, laptop->dell2, laptop->sitez, sitez->laptop (7). Never: dell1->laptop, dell2->dell1, dell2->sitez, sitez->dell1, sitez->dell2 (5). FWD-18 ADVANCED: the laptop wrapper and the site Z guard both refuse a download and name the route (site Z by MSTR~Z's report); the install of a delivered file on each box is not run. FWD-19 ADVANCED: fetch records carry device now, but the old records are unattributed and a second writer omits it (W112-S4). FWD-21 ADVANCED: site Z's manager reports 0 specific asks for its 23:32Z respawns under a standing instruction, which meets 'without being asked' as reported. But the audit lines it cites are in site Z's working copy only: origin/box/sitez's agent-spawn-audit.log ends 2026-10-09T17:03Z (0 lines dated 10-14 or 10-15), and no manager day record has been read for project rulings. FWD-5 ADVANCED: the positive arm passes against a stub aws and a local bucket; a real signed push is not run. FWD-2 ADVANCED: a fixture box is named by 8 of 8 tools in a register copy; no real box was added and no seat started. FWD-24 ADVANCED: site Z's answer (e670) is still owed.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "python .tools/crossbox-matrix.py -> pairs=12 with_file=12 acked=12 closed_both=4 none=0 (2026-10-15 ~15:1xZ); ack.by of each pair's newest XB file and of every manager-acked file, read from org/devices/crossbox/XB-*.json",
    "MSYS_NO_PATHCONV=1 git show origin/box/sitez:org/mcp/agent-spawn-audit.log -> 18991 lines, last 2026-10-09T17:03:15Z, 0 lines matching 2026-10-1[45]T",
    "this record's C-S63 and C-S64 runs; L8_PACKET_ROUND20.md @58a0c48950 section 3"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A grade delta, not a hazard. FWD-3's cell is the five never-manager-acked pairs, each acked by its receiving MSTR."
 }
]
```

-- 3.0.0_SA_CVO~L
