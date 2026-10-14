# NFRA_CTLPLN: CVO L8 at the round-14 close (2026-10-14)

<sweep_watermark>2026-10-14T22:45Z</sweep_watermark>

L8 by `3.0.0_SA_CVO~L` (laptop), on `2.0.0_SA_COO~C` msg 109279 (packet `deliverables/2.0.0_SA_COO~C/L8_PACKET_ROUND14.md` @89a76c1ca5).
`round-close-check --round 14`: MAY-CLOSE; no judgment criterion this round.

**Result: 7 round-14 rows dismissed with reason (C-S51); 0 graduate; D2-S3 REMEDIATED and DISARMED in place (C-S52); S9118 and W12-S1
stay OPEN.** The CTO's round-13 analysis asked this seat whether CT-ac-2 closes S9118's kill-maint half. Answer: the code half landed
earlier, in CT-ab-4 (refuse-and-print, not stop-at-descendant), and its done-when, a planted tree surviving a real `kill-maint -Execute`,
is unrun. One small cell closes it.

```json
[
 {
  "id": "NFRA_CTLPLN-C-S51",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO~L",
  "surfaced_at": "2026-10-14T22:45Z",
  "one_line": "Round 14, worker notes, each disposed in its order's status_reason: W92-S1 (the fence check calls AWS, so its batch arm cannot run under the no-AWS rule), W92-S2 (the NOTE frame asserted on the fixture where it prints), W92-S3 (coverage fixtures under the ignored .scratch/), W93-S1 (on an ENFORCE refusal safe-commit's naming stage unstages only the graded extensions), W94-S1 (two mdpf Lambdas hand-type their own 2026-2027 holiday set; not vendored copies), W95-S1 (the --check-fresh checkpoint has no ignore rule), W95-S2 (no Python 3.11 on this box; ran on 3.12.10).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "NFRA_CTLPLN-W92-S1",
   "NFRA_CTLPLN-W92-S2",
   "NFRA_CTLPLN-W92-S3",
   "NFRA_CTLPLN-W93-S1",
   "NFRA_CTLPLN-W94-S1",
   "NFRA_CTLPLN-W95-S1",
   "NFRA_CTLPLN-W95-S2"
  ],
  "spec_asserts": "Each order's text as written.",
  "world_is": "All seven are INERT build notes or disclosed limits. W93-S1 and W95-S1 leave files in the shared index or tree after a refusal or a partial run, which is untidy but not harmful. W94-S1 widens W12-S1's calendar question to two hand-typed sets the census does not count.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/2.0.0_SA_COO~C/L8_PACKET_ROUND14.md @89a76c1ca5"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Disclosed limits and build notes; W93-S1, W94-S1 and W95-S1 are candidates for the CTO's round-15 list, named in the slug."
 },
 {
  "id": "NFRA_CTLPLN-C-S52",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO~L",
  "surfaced_at": "2026-10-14T22:45Z",
  "one_line": "D2-S3 is REMEDIATED and DISARMED in place on its done-when (an act row with no roots now matches no root; naming irpt-status in its roots makes it match there alone); W12-S1 stays OPEN (copies still differ in bytes from lib); S9118 stays OPEN: kill-maint.ps1 is wired to the seat boundary by CT-ab-4 (a915a7cd84), but its done-when, a planted tree surviving a real kill-maint -Execute, has not been run.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "D2-S3: the same act row reads matched=0 against irpt-status and still matches a root it names. S9118: the same planted tree survives a kill-maint -Execute. W12-S1: each copy equals lib/trading_calendar.py and is deployed.",
  "world_is": "D2-S3: the issuer's real run on the cluster copy of dell2-20261013T214715Z-f61b read matched=0 against irpt-status and opal-ticket-api, and matched=1 only on the root its roots field names; test_open_call_act_roots.py reads 8/8 here. S9118: kill-maint.ps1:747-756 calls Test-SeatBoundary before taskkill /T and refuses a tree holding another seat (KILL-MAINT-REFUSED reason=seat-boundary). That is the remedy's permanent half (skip and print), not stop-at-descendant. test_seat_boundary.ps1 reads 39/39 wired=both here, but it proves the wiring and the function, not a real -Execute over a planted tree. W12-S1: CALENDAR-COPIES found=4, same_2026_2027=4, all four differ from lib in bytes; the silent fallback past 2027 is unchanged (the same date as Z-S3).",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/2.0.0_SA_COO~C/L8_PACKET_ROUND14.md @89a76c1ca5",
    "timeout 200 python .tools/tests/test_open_call_act_roots.py -> arms=8/8 ok=True",
    "powershell -File .tools/tests/test_seat_boundary.ps1 -> cases=39/39 wired=both ok=True",
    ".tools/kill-maint.ps1 lines 228-229, 747-761 at HEAD; git log -- .tools/kill-maint.ps1 (a915a7cd84, CT-ab-4)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A record of one row's clocks advanced on its done-when, and two rows left open with the reason."
 }
]
```

-- 3.0.0_SA_CVO~L
