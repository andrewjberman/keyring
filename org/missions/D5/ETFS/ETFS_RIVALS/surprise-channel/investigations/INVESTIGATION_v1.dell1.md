# ETFS_RIVALS -- surprise channel, investigations (dell1's append file)

dell1's own append file for this project's channel. ETFS_RIVALS moved to dell1 on Andrew-direct ~01:5xZ 2026-10-09
(@a0db38c8ae). The site-Z rows before that move are in `INVESTIGATION_v1.Z.md`, which only site Z writes. Rows minted here carry
dell1's coordinate `D1-` (org/devices/DEVICES.json), so they cannot collide with that file's `Z-` rows.

```json
[
  {
    "id": "ETFS_RIVALS-D1-S1",
    "project": "ETFS_RIVALS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO~RV1",
    "surfaced_at": "2026-10-09T03:12:59Z",
    "one_line": "DISARM of ETFS_RIVALS-Z-S79 and ETFS_RIVALS-Z-S80 on their disarm owner's act (2.0.0_SA_COO~V1, commit c07077f4e1, word msg 1474): RIV-tw-1 J1 AMENDMENT 1 reads J1 only on the first scheduled run that REACHED the enrichment leg, so the 2026-10-08 run (exit 97, no session) reads UNVERIFIABLE, never PASS. The act is the one sentence S79's notes name as its disarm. J1 itself stays owed.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "commit c07077f4e1 (2.0.0_SA_COO~V1), an ancestor of HEAD bc1ce7b850 (merge-base read by this seat 03:12Z): J1 at TO-RIV-tw-1 now carries 'AMENDMENT 1 ... J1 is read on the FIRST scheduled vehicle run that REACHED the enrichment leg -- its log carries the RIVALFUNDS ENRICHMENT STEP line, an enrichment exit code other than 97, and no vendor-session-failure line ... A run that did not reach the leg reads UNVERIFIABLE for J1, never PASS; the 2026-10-08 11:00Z run is such a run.' (printed from git show HEAD:<order>, one match)",
        "the same commit amends TO-RELAY-tw1-vehicle-log-20261009: the transcriber adds the verdict line '-- DID THIS FIRE REACH THE ENRICHMENT LEG? --' and the whole log is committed beside it as VEHICLE_LOG_20261009_1100Z.full.log",
        "S79 notes (@c086fcc096): 'the disarm is one sentence from the issuer -- that J1 is read on the first fire that REACHED the enrichment leg, not on the earliest date in the range'",
        "S80 (@eaf6d69c9a): disarm_owner moved to 2.0.0_SA_COO~V1 per 0.0.0_AB_MSTR~Z msg 32284"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "adjudicates": [
      "ETFS_RIVALS-Z-S79",
      "ETFS_RIVALS-Z-S80"
    ],
    "spec_asserts": "S79/S80: ARMED until the issuer states that J1 is read on the first fire that reached the enrichment leg; the CVO writes the disarm clock (surprise-row-gate R-15).",
    "world_is": "The issuer's statement is in the order at HEAD, and its predicate is sharper than the row asked for: it names the three conditions (STEP line, exit not 97, no session-failure line) and the four session-failure strings. The hazard S79 named (a non-reaching run consumed as a PASS) can no longer arise from J1's wording. What survives the disarm: (1) J1 is still owed, and the 2026-10-09 11:00Z fire reaches the leg only if the Terminal is signed in at 07:00 local; (2) a remediation row with the disarm clock is written at the round-28 slug, because a new remediation row is refused while task orders are open (2 pending at HEAD).",
    "notes": "Written as an investigation row because the surprise-row gate refuses a new remediation row mid-round (LD-0521); a REMEDIATION_v22 with this clock was refused at commit (2 of 128 orders not terminal) and withdrawn uncommitted. The remediation rows for S79 and S80, with disarm DISARMED at this row's surfaced_at, are owed at the next slug."
  },
  {
    "id": "ETFS_RIVALS-D1-S2",
    "project": "ETFS_RIVALS",
    "fabric": "dell1",
    "surfaced_by": "2.0.0_SA_COO~V1",
    "surfaced_at": "2026-10-09T04:02Z",
    "one_line": "The ruling that puts act 3's standing Bloomberg draw on MDPF_DEMQUE's books says the vehicle reads the queue's pause/stop state before each draw, but no such state exists to read and the history-owed step (tw-1 + tc-1) reads none: switching RIVALFUNDS_HISTORY_OWED to ask on the code as built would draw past a queue pause",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~V1",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Ruling XA-20261009T033809Z-8c1a (1.0.0_SA_CTO on laptop, 2026-10-09T03:42:38Z, read with `xadj.py show`), condition 1: '2.0.0_SA_COO~Q1 enters the standing request before the first run. The queue may pause or stop it at its reserve, or when a higher tier needs the budget; the vehicle reads that state before each draw.'",
        "data/etfs/scripts/rivalfunds/enrichment_bloomberg.py `_history_owed` on branch wk-ETFS_RIVALS-22 @b0b65368fb (read in full at the simulated merge onto origin/box/sitez 37aefc2855): the only gate before a request is `bbg_budget.check_points`; no queue or request-state read.",
        "org/missions/D8/MDPF/MDPF_DEMQUE/prd/MDPF_DEMQUE_PRD.md: one Grep for standing / pause / stop / reserve near state / status / read returns 2 lines (:149 the backfill allowance arithmetic, :174 a corporate-actions sentence); no readable per-request state is specified. The ruling's condition 3 names a standing request as a new request shape for C-QUOTE at Q1's next round."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "XA-...-8c1a condition 1: before each history-owed draw the vehicle reads the standing request's queue state and draws nothing when it is paused or stopped.",
    "world_is": "No queue state for a standing request exists to read (MDPF_DEMQUE PRD), and the vehicle's history-owed step reads none. Acts 1 (aw-1 deploy) and 2 (tc-1 merge) draw nothing and are unaffected; act 3 (the switch-on) cannot meet condition 1 until (i) Q1 names where the state lives and (ii) a rivalfunds cell reads it.",
    "notes": "Disarm (this seat, now): act 3's order is not cut and RIVALFUNDS_HISTORY_OWED is not set to ask until both (i) and (ii) exist; the switch stays unset. The cell for (ii) is new work outside the frozen round-28 decomposition, so it is the CTO's to place (round 29 or an addendum); (i) is Q1's interface. Owner of the remedy: 1.0.0_SA_CTO~DELL1 places it; 2.0.0_SA_COO~Q1 names the state."
  }
]
```
