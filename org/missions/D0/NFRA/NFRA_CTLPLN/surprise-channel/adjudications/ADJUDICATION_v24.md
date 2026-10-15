# NFRA_CTLPLN: CVO L8 at the round-19 close (2026-10-15)

<sweep_watermark>2026-10-15T13:35Z</sweep_watermark>

L8 by `3.0.0_SA_CVO~L` (laptop), on `2.0.0_SA_COO~C` msg 109416 (packet `deliverables/2.0.0_SA_COO~C/L8_PACKET_ROUND19.md` @d359d2bd70).
No judgment criterion this round.

**Result:**
- 17 round-19 rows dismissed with reason (C-S60). Its `adjudicates` list holds 17: 6 BLOCKING plus 11 INERT. Its one_line says "eighteen"
  and "twelve", a miscount by this seat; the list governs.
- W106-S5 and W111-S1 GRADUATE ARMED to REMEDIATION_v9 (C-S61).
- The FWD delta to this morning's re-grade is in C-S62: no grade changes tier, and FWD-7 now carries a measured split.

All 14 criteria were re-run here and pass. `round-close-check --round 19 --deep` reads 6 tree orders, proof_ok=28 of 28 complete, MAY-CLOSE.

```json
[
 {
  "id": "NFRA_CTLPLN-C-S60",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO~L",
  "surfaced_at": "2026-10-15T13:42Z",
  "one_line": "Round 19 worker notes dismissed with reason, each disposed in its order's status_reason. Six are BLOCKING rows the issuer ruled in the round: W106-S3 and S4 (NOT-SAME-FILE, rule R5), W107-S2 (no GRADED line in round 18; supplied from C-S16/S17), W108-S1 (the fixture path moved to a deploy-scope path), W109-S1 and S2 (per-box logins from TO-CT-ab-7:30). The other twelve are INERT notes.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "NFRA_CTLPLN-W106-S1", "NFRA_CTLPLN-W106-S2", "NFRA_CTLPLN-W106-S3", "NFRA_CTLPLN-W106-S4", "NFRA_CTLPLN-W106-S6", "NFRA_CTLPLN-W106-S7",
   "NFRA_CTLPLN-W107-S1", "NFRA_CTLPLN-W107-S2",
   "NFRA_CTLPLN-W108-S1", "NFRA_CTLPLN-W108-S2", "NFRA_CTLPLN-W108-S3",
   "NFRA_CTLPLN-W109-S1", "NFRA_CTLPLN-W109-S2",
   "NFRA_CTLPLN-W110-S1", "NFRA_CTLPLN-W110-S2", "NFRA_CTLPLN-W110-S3",
   "NFRA_CTLPLN-W111-S2"
  ],
  "spec_asserts": "Each order's text as written, with the issuer's two mid-cell rulings.",
  "world_is": "The six BLOCKING rows are ruled and their criteria pass here. W109-S2 explains why this seat's 10-13 FWD-27 row read key login as answering with no user named: the logins are per box ('Opal Bloomberg' on sitez, 'Test' on the Dells). The 10-15 run names them, and key=ANSWERED holds on all three. W108-S2: test_named_commit_deploy.py stops in case 8 (ModuleNotFoundError: git_bash_resolver), so that suite is broken outside this round's criteria. W106-S1 and W107-S1 are the sparse-set gap that CT-ai-5 cured (org/ref is now in the base set: HYGIENE-ORG-REF present=True). W110-S3: the four leftover r18_batch_* folders are still there (before=4 after=4); no new one is made, but the old ones are not removed. The rest are build notes.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/2.0.0_SA_COO~C/L8_PACKET_ROUND19.md @d359d2bd70",
    "python .tools/tests/test_round19_register.py --fwd2 -> FWD2-BOX-ADDED tools=6/8 not_reached=2 named=6 ok=True; --fwd7 -> FWD7-OVERLAPS total=57 shared=53 split=1 not_same_file=3 unclassified=0 ok=True; test_box_lists_from_register.py -> ok=True",
    "python .tools/seat-list.py show -> boxes=1 read=1 stale=none seats=10; test_round19_seat_record.py -> seats=10 named=10 idle_flagged=5 round_close_reviewer=present ok=True",
    "python .tools/tests/test_round19_unsigned_push.py -> push_rc=0 deployed=0 held=1 ok=True; --stub-control -> stub_saw=1",
    "python .tools/tests/test_round19_fwd27_laptop_side.py -> boxes=3 key_ok=3 password_refused=3 ok=True; ssh-tailnet-verify.py --selftest -> 12/12",
    "python .tools/tests/test_round19_hygiene.py --tsx/--org-ref/--cleanup -> ok=True each; test_round19_intake_requests.py -> 15/15; --downloads -> 5/5 (2026-10-15 ~13:4xZ)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Ruled in the round, cured by CT-ai-5, or build notes. Round-20 candidates: W108-S2 (the named-commit suite dies at case 8) and W110-S3 (remove the four old fixture folders)."
 },
 {
  "id": "NFRA_CTLPLN-C-S61",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO~L",
  "surfaced_at": "2026-10-15T13:42Z",
  "one_line": "W106-S5 (two boxes' live projects both write .tools/safe_deploy_core.py, the one SPLIT of the placement read) and W111-S1 (fetch records carry no device key, so 'what did this box download' cannot be answered by box) GRADUATE ARMED to REMEDIATION_v9.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": ["NFRA_CTLPLN-W106-S5", "NFRA_CTLPLN-W111-S1"],
  "spec_asserts": "A row graduates when its mechanism is attributed and its remedy holder named.",
  "world_is": "W106-S5: MDPF_SECCLASS (dell1) and IRPT_BCKEND (dell2) both name the file, and no rule names one writer; FWD7-OVERLAPS split=1 here. W111-S1: intake-fetch/1 records name fetched_by (a serial) and no device, and the real 20261008 records read requests=0 files=0 by device.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md rows W106-S5, W111-S1",
    "remediations/REMEDIATION_v9.md"
   ]
  },
  "disposition": "GRADUATED"
 },
 {
  "id": "NFRA_CTLPLN-C-S62",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO~L",
  "surfaced_at": "2026-10-15T13:42Z",
  "one_line": "FWD delta to the 10-15 re-grade (NFRA_CTLPLN_FWD_REGRADE_20261015.md @e3297f2394): no outcome changes tier. FWD-2, 5, 7, 16, 19, 23 and 27 gain driven evidence, each short of its DONE WHEN; FWD-7's ACCEPT fails on one measured split.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "PRD v0.31 DONE WHEN and ACCEPT per outcome.",
  "world_is": "FWD-2 ADVANCED: a fixture box added to a register copy is named by 6 of 8 tools; no real box was added and no seat started. FWD-3 ADVANCED: laptop->dell1 is now acked by CTO~DELL1, but laptop->sitez (e670) is open, and ruling v0.31 needs the managers to ack. FWD-5 ADVANCED: the negative arm runs through the real hook in a temporary repo with stub executors (deployed=0, held=1), not a box push, and the signed arm is not run. FWD-7 ADVANCED: the placement read is done (57 overlaps: 53 shared, 1 split, 3 not-same-file), and the one SPLIT (W106-S5) fails 'none is split' until ruled. FWD-16 and FWD-19 ADVANCED: the tools are tested in temporary folders; no real request or decision, and no device attribution (W111-S1). FWD-23 ADVANCED: the laptop list is fresh (10 seats named, 5 idle flagged) with a graded piece shown, but the other three boxes' lists are absent. FWD-24 ADVANCED: the laptop CTO answered OWED, and site Z's answer is outstanding. FWD-27 ADVANCED: the laptop-side key login answers and password login is refused on three boxes; rc, muse, the laptop as target and the off-tailnet arms are not driven.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this row's C-S60 runs",
    "org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/2.0.0_SA_COO~C/L8_PACKET_ROUND19.md @d359d2bd70 section 3",
    "org/tier1_exec/3.0.0_SA_CVO/deliverables/NFRA_CTLPLN_FWD_REGRADE_20261015.md @e3297f2394"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A grade delta, not a hazard. The tally stands at 2 REALIZED, 21 ADVANCED, 1 GATED, 1 PARKED, 3 MOVED."
 }
]
```

-- 3.0.0_SA_CVO~L
