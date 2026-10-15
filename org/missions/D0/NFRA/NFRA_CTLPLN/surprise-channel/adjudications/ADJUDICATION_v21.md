# NFRA_CTLPLN: CVO L8 at the round-16 close (2026-10-15)

<sweep_watermark>2026-10-15T08:00Z</sweep_watermark>

L8 by `3.0.0_SA_CVO~L` (laptop), on `2.0.0_SA_COO~C` msg 109367 (packet `deliverables/2.0.0_SA_COO~C/L8_PACKET_ROUND16.md` @aed7c25cca).
No judgment criterion this round.

**Result: 3 round-16 rows dismissed with reason (C-S55); W100-S1 GRADUATES ARMED to REMEDIATION_v8 for the CTO (C-S56).** Every criterion was re-run
here. `round-close-check --round 16 --deep` reads orders=26, proof_ok=25 of 25 complete, `TREE orders counted by decomposition round: 3`, MAY-CLOSE. The
round-15 instrument note in ADJUDICATION_v20 is cured by CT-af-2: `--round 15` now counts TO-CT-ae-1..3.

```json
[
 {
  "id": "NFRA_CTLPLN-C-S55",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO~L",
  "surfaced_at": "2026-10-15T08:00Z",
  "one_line": "Round 16 worker notes, each disposed in its order's status_reason: W100-S2 (check-removable also refuses ignored non-cache paths, so it never says REMOVABLE for a worktree that ran the tests), W101-S1 (eight untagged seat-folder orders that name a decomposition now scope to its round; the issuer ruled this is ruling 4's intent), W102-S1 (the suite pins the base to the issuance commit, not HEAD).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "NFRA_CTLPLN-W100-S2",
   "NFRA_CTLPLN-W101-S1",
   "NFRA_CTLPLN-W102-S1"
  ],
  "spec_asserts": "Each order's text as written.",
  "world_is": "All three are INERT. W100-S2 is a strictness beyond the CTO's definition: the issuer's real check of the three round-16 worktrees read NOT-REMOVABLE MERGED for each, with porcelain empty, own >= 1 and HEAD in box/laptop, so the drain still removes by hand (packet D1, a round-17 candidate). W101-S1 changes no verdict: all 16 round verdicts are MAY-CLOSE before and after. W102-S1 is a correct pin.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/2.0.0_SA_COO~C/L8_PACKET_ROUND16.md @aed7c25cca",
    "python .tools/tests/test_worktree_gc_own_commit.py -> arms=8/8 ok=True; python .tools/worktree_gc.py --selftest -> cases=3/3 ok=True",
    "python .tools/tests/test_round_close_decomp_round.py -> arms=6/6 ok=True; python .tools/round-close-check.py --selftest -> cases=30/30 ok=True",
    "python .tools/tests/test_placement_unstage.py -> arms=4/4 ok=True; test_round15_batch.py -> arms=9/9 ok=True; test_safe_commit_derivation.py -> cases=17/17 ok=True",
    "python .tools/round-close-check.py --project NFRA_CTLPLN --round 16 --deep -> verdict=MAY-CLOSE (2026-10-15 ~07:5xZ)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Build notes and a disclosed strictness. W100-S2 is the round-17 candidate the issuer names (check-removable reads porcelain only)."
 },
 {
  "id": "NFRA_CTLPLN-C-S56",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO~L",
  "surfaced_at": "2026-10-15T08:00Z",
  "one_line": "W100-S1 GRADUATES ARMED to REMEDIATION_v8: worktree_gc.py --go force-removes a merged, idle, dirty worktree with an own commit (Andrew's standing word of 2026-10-08), while --check-removable refuses the same path (the CTO's round-15 ruling 1). The two verdicts disagree until the CTO rules.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "NFRA_CTLPLN-W100-S1"
  ],
  "spec_asserts": "A row graduates when its mechanism is attributed and its remedy holder named.",
  "world_is": "The disagreement is measured by the worker's arms (test_worktree_gc_own_commit.py 8/8 here). A merged worktree's commits are in trunk, so --go loses no commit; what it can lose is uncommitted files. Andrew's word covers merged worktrees ('force-removing merged worktrees is mandatory'; an unmerged commit still goes to its owner). The ruling is the CTO's; the issuer's recommendation is to keep --go.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md row W100-S1",
    "org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/2.0.0_SA_COO~C/L8_PACKET_ROUND16.md @aed7c25cca section D2",
    "remediations/REMEDIATION_v8.md"
   ]
  },
  "disposition": "GRADUATED"
 }
]
```

-- 3.0.0_SA_CVO~L
