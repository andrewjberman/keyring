# NFRA_CTLPLN -- remediations, v8

<sweep_watermark>2026-10-15T08:00Z</sweep_watermark>

Author: `3.0.0_SA_CVO~L`, 2026-10-15 ~08:0xZ, at the round-16 close: this round's L10 slug. Graduated in ADJUDICATION_v21.md C-S56. One row, ARMED.
Every round-16 order is terminal (three complete).

```json
[
 {
  "id": "NFRA_CTLPLN-W100-S1",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": ".tools/worktree_gc.py --go force-removes a worktree that is merged into the trunk, has an own commit, is idle 24 h and holds uncommitted files (the MERGED class, Andrew's standing word of 2026-10-08), while --check-removable on the same path answers NOT-REMOVABLE MERGED (the CTO's round-15 ruling 1: a dirty worktree is never removed). The next --go removes the uncommitted files that --check-removable protects.",
  "evidence": [
   "org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md row W100-S1",
   "python .tools/tests/test_worktree_gc_own_commit.py -> arms=8/8 ok=True (2026-10-15 ~07:5xZ)",
   "adjudication row NFRA_CTLPLN-C-S56"
  ],
  "remedy": "P2. 1.0.0_SA_CTO rules which verdict governs a merged dirty worktree: keep --go as it is under Andrew's word (and align --check-removable with it), or make --go keep a dirty one. Done when both verbs return the same verdict for the same planted worktree.",
  "owner": "1.0.0_SA_CTO",
  "round": "v21",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "1.0.0_SA_CTO",
   "round": "v21"
  },
  "disarm": {
   "state": "DISARMED",
   "owner": "1.0.0_SA_CTO",
   "at": "2026-10-15T09:45Z"
  },
  "closed": true
 }
]
```

-- 3.0.0_SA_CVO~L
