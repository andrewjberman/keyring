# NFRA_CTLPLN: CVO L8 at the round-15 close (2026-10-15)

<sweep_watermark>2026-10-15T05:45Z</sweep_watermark>

L8 by `3.0.0_SA_CVO~L` (laptop), on `2.0.0_SA_COO~C` msg 109332 (packet `deliverables/2.0.0_SA_COO~C/L8_PACKET_ROUND15.md` @b1415a8115).
No judgment criterion this round.

**Result: 7 round-15 rows dismissed with reason (C-S53); 0 graduate; S9118 REMEDIATED and DISARMED in place on its done-when (C-S54).**
Every criterion was re-run here at HEAD bbd328c0a1, not read from the packet. One instrument note: the packet's
`round-close-check --round 15` counts 31 untagged seat-folder orders and none of the three CT-ae orders, whose `<round>` is the
workstream round (SEATKILL 4, CALENDAR 3, BATCH 3). Run per workstream with `--deep`, each reads orders=1 complete=1 proof_ok=1
MAY-CLOSE. The verdict stands; the round-15 read did not measure it.

```json
[
 {
  "id": "NFRA_CTLPLN-C-S53",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO~L",
  "surfaced_at": "2026-10-15T05:45Z",
  "one_line": "Round 15, worker and issuer notes, each disposed in its order's status_reason: W97-S1 (kill-maint's held-tree guard SKIPped any tree holding a claude.exe, so the seat-boundary refusal was unreachable for a seat; fixed refuse-only at 21ad9d0ca4), W97-S2 (the recipe's literal planted shape cannot be planted; the test uses a python.exe root with a cmd.exe copy named claude.exe), W98-S1 (six inline holiday sets, not two), W98-S2 (inf-gold-freshness-guard's MARKET_HOLIDAYS has no 2027 closures), W98-S3 (the measure unwraps one frozenset call; the worker's extension of the read rule), W99-S1 (safe-commit's PLACEMENT refusal branch unstages only NGATE_FILES, the W93-S1 shape), S9125 (the INF Lambda fix routed to dell1 before 2026-12-31).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "NFRA_CTLPLN-W97-S1",
   "NFRA_CTLPLN-W97-S2",
   "NFRA_CTLPLN-W98-S1",
   "NFRA_CTLPLN-W98-S2",
   "NFRA_CTLPLN-W98-S3",
   "NFRA_CTLPLN-W99-S1",
   "NFRA_CTLPLN-S9125"
  ],
  "spec_asserts": "Each order's text as written.",
  "world_is": "All seven are INERT. W97-S1 is cured at HEAD: kill-maint.ps1 carries the SEAT BOUNDARY FIRST branch (1 match at bbd328c0a1, 0 at 93a3f55d25), and both its paths end in continue, so it stops nothing new. W97-S2 leaves one thing unmeasured: whether the reaper's real tree shape (a bash or powershell root over a seat) takes the same branch; Test-SeatBoundary walks descendants whatever the root's image, so the test shape exercises the same check. W98-S2 and S9125 are one hazard with a dated owner on dell1, inert until 2027-01-01. W99-S1 is read from source, not exercised.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/2.0.0_SA_COO~C/L8_PACKET_ROUND15.md @b1415a8115",
    "timeout 120 python .tools/measure_inline_holiday_sets.py -> INLINE-HOLIDAY-SETS found=6 same_2026_2027=5 differs_2026_2027=1 unreadable=0 ok=True",
    "python .tools/tests/test_measure_inline_holiday_sets.py -> arms=5/5 ok=True",
    "python .tools/tests/test_round15_batch.py -> arms=9/9 ok=True; test_open_call_act_roots.py -> arms=8/8 ok=True; test_safe_commit_derivation.py -> cases=17/17 ok=True",
    "git show 21ad9d0ca4 -- .tools/kill-maint.ps1 (14 lines added inside the held-tree branch, no line removed)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Build notes and disclosed limits. W99-S1 is a candidate for the CTO's round-16 list (the ENFORCE twin was repaired in CT-ae-3). S9125 is already routed with an owner and a date."
 },
 {
  "id": "NFRA_CTLPLN-C-S54",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO~L",
  "surfaced_at": "2026-10-15T05:45Z",
  "one_line": "S9118 is REMEDIATED and DISARMED in place on its done-when: a planted tree holding a foreign claude.exe seat survived a real kill-maint.ps1 -Mode scripts -Execute -OnlyPid, the control tree died, and the audit line reads KILL-MAINT-REFUSED reason=seat-boundary. Re-run here; the 10 real claude.exe seats on the box were the same before and after.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "S9118: the same planted tree survives a kill-maint -Execute (REMEDIATION_v5).",
  "world_is": "test_kill_maint_planted.ps1 reads KILL-MAINT-PLANTED cases=10/10 ok=True and REAL-SEATS claude.exe before=10 after=10; test_stop_at_descendant.ps1 reads cases=27/27 ok=True. The interim dry-first rule is 0.0.0_AB_MSTR's to lift; the disarm records that the permanent half now stands, not that the interim rule was lifted. The residual is W97-S2's shape question (C-S53).",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "powershell -NoProfile -ExecutionPolicy Bypass -File .tools/tests/test_kill_maint_planted.ps1 -> cases=10/10 ok=True (2026-10-15 ~05:4xZ, HEAD bbd328c0a1)",
    "powershell -NoProfile -ExecutionPolicy Bypass -File .tools/tests/test_stop_at_descendant.ps1 -> cases=27/27 ok=True",
    "python .tools/round-close-check.py --project NFRA_CTLPLN --round 4 --workstream SEATKILL --deep -> orders=1 proof_ok=1 MAY-CLOSE"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A record of one row's clocks advanced on its done-when."
 }
]
```

-- 3.0.0_SA_CVO~L
