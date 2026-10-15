# NFRA_CTLPLN: CVO L8 at the round-17 close (2026-10-15)

<sweep_watermark>2026-10-15T09:30Z</sweep_watermark>

L8 by `3.0.0_SA_CVO~L` (laptop), on `2.0.0_SA_COO~C` msg 109382 (packet `deliverables/2.0.0_SA_COO~C/L8_PACKET_ROUND17.md` @24e899265f).
No judgment criterion this round.

**Result: 5 round-17 rows dismissed with reason (C-S57); 0 graduate; W100-S1 REMEDIATED and DISARMED in place on its done-when (C-S58).** Every
criterion was re-run here, including the real sparse run. `round-close-check --round 17 --deep` reads 2 tree orders, proof_ok=24 of 24 complete, MAY-CLOSE.

```json
[
 {
  "id": "NFRA_CTLPLN-C-S57",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO~L",
  "surfaced_at": "2026-10-15T09:45Z",
  "one_line": "Round 17 worker and issuer notes, each disposed in its order's status_reason: W103-S1 (a sparse worktree also needs org/modules/graph, org/devices and infra/logic/registry for safe-commit's gates), W103-S2 (preserve follows a directory junction; symlinks unmeasured, WinError 1314), W104-S1 (the fixture layout named one level too deep), W104-S2 (BLOCKING: the dispatch SKILL.md byte budget refused the worker's text; the issuer landed a shorter recipe, net -48 bytes, at 43f9022522), S9126 (worktree_gc reads its own command line, so an ABSOLUTE --only path reports SKIP IN USE for every worktree).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "NFRA_CTLPLN-W103-S1",
   "NFRA_CTLPLN-W103-S2",
   "NFRA_CTLPLN-W104-S1",
   "NFRA_CTLPLN-W104-S2",
   "NFRA_CTLPLN-S9126"
  ],
  "spec_asserts": "Each order's text as written.",
  "world_is": "All five are INERT. W104-S2 is cured: 43f9022522 rewrites the recipe paragraph shorter (2 insertions, 7 deletions, one file) and the dispatch skill now states the sparse default. S9126 fails safe: an absolute path makes the verb refuse, never remove. A relative path reads correctly, and the issuer's real run used one. W103-S1 names a gap in the sparse folder set that wk-provision.sh should carry. Whether it does is the packet's own unmeasured item (safe-commit in a worktree cut by the new script).",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/2.0.0_SA_COO~C/L8_PACKET_ROUND17.md @24e899265f",
    "python .tools/tests/test_worktree_gc_preserve.py -> arms=9/9 ok=True; test_worktree_gc_own_commit.py -> arms=8/8 ok=True; worktree_gc.py --selftest -> cases=3/3 ok=True",
    "python .tools/tests/test_wk_sparse_provision.py -> arms=7/7 ok=True; bash .tools/wk-provision.sh --self-test -> 0 arm(s) failed of 8",
    "python .tools/tests/test_wk_sparse_provision.py --real -> SPARSE-REAL ratio=0.02 du_sparse=105M green=True (2026-10-15 ~09:4xZ)",
    "git show --stat 43f9022522"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Build notes, a fail-safe defect and a BLOCKING row cured in the round. S9126 and W103-S1 are candidates for the CTO's round-18 list."
 },
 {
  "id": "NFRA_CTLPLN-C-S58",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO~L",
  "surfaced_at": "2026-10-15T09:45Z",
  "one_line": "W100-S1 is REMEDIATED and DISARMED in place on its done-when: on the real merged worktree ctlpln-103 with a planted untracked file, --check-removable read REMOVABLE-AFTER-PRESERVE and --go --only preserved the file to a branch and removed the tree. Both verbs agree, and the file reads back from the preserve commit.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "W100-S1 (REMEDIATION_v8): done when both verbs return the same verdict for the same planted worktree.",
  "world_is": "Read here: branch preserve/wk-NFRA_CTLPLN-103-20261015T085906Z resolves to 1e32e8229a, and git show 1e32e8229a:PLANTED_BY_ISSUER.txt returns the planted line. HEAD's worktree_gc.py carries REMOVABLE-AFTER-PRESERVE (4 matches). The preserve arms read 9/9 here. The CTO's ruling (preserve, then remove) keeps Andrew's word that merged worktrees are force-removed and loses no uncommitted file. Residual: --go without --only has never been run on the real repository (packet section 6).",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "git rev-parse preserve/wk-NFRA_CTLPLN-103-20261015T085906Z -> 1e32e8229a; git show 1e32e8229a:PLANTED_BY_ISSUER.txt",
    "python .tools/tests/test_worktree_gc_preserve.py -> arms=9/9 ok=True",
    "org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/2.0.0_SA_COO~C/L8_PACKET_ROUND17.md @24e899265f section 3"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A record of one row's clocks advanced on its done-when."
 }
]
```

-- 3.0.0_SA_CVO~L
