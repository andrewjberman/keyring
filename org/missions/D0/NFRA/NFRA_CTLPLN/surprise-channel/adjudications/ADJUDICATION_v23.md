# NFRA_CTLPLN: CVO L8 at the round-18 close (2026-10-15)

<sweep_watermark>2026-10-15T11:25Z</sweep_watermark>

L8 by `3.0.0_SA_CVO~L` (laptop), on `2.0.0_SA_COO~C` msg 109394 (packet `deliverables/2.0.0_SA_COO~C/L8_PACKET_ROUND18.md` @c34d3f13fe).
No judgment criterion this round.

**Result: 8 round-18 rows dismissed with reason (C-S59); 0 graduate.** Every criterion was re-run here, including the real sparse safe-commit arm. Box and
portal worktree counts were taken before and after it: box 2 and 2, portal 8 and 8. `round-close-check --round 18 --deep` reads 1 tree order, proof_ok=23
of 23 complete, MAY-CLOSE.

```json
[
 {
  "id": "NFRA_CTLPLN-C-S59",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO~L",
  "surfaced_at": "2026-10-15T11:30Z",
  "one_line": "Round 18 worker notes W105-S1..S8 dismissed with reason: probe placement (S1), a sparse worktree lacks org/ref so the author check WARNs (S2), provision always adds a portal worktree (S3), a portal worktree count drop not attributed (S4), four leftover temp fixtures (S5), a repository-wide prune in the test, now removed (S6), the merged rbndv2-8 worktree gone between two reads (S7), and author-warn lines left in a tracked audit log (S8).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "NFRA_CTLPLN-W105-S1",
   "NFRA_CTLPLN-W105-S2",
   "NFRA_CTLPLN-W105-S3",
   "NFRA_CTLPLN-W105-S4",
   "NFRA_CTLPLN-W105-S5",
   "NFRA_CTLPLN-W105-S6",
   "NFRA_CTLPLN-W105-S7",
   "NFRA_CTLPLN-W105-S8"
  ],
  "spec_asserts": "Each order's text as written.",
  "world_is": "All eight are INERT. S6 is cured: test_round18_batch.py at HEAD names the prune only in a comment (:236), and this seat's --real run left the box at 2 worktrees and the portal at 8. S7: rbndv2-8 (wk-DSGN_RBNDV2-8) was merged by its owner's round-2 drain (5d77dd8806), and its tip e09ef0f0e5 is in box/laptop, so no commit is lost. A prune removes only an admin entry, never a directory or a branch, so the prune is not the remover; the owner's drain-time removal of a merged worktree (Andrew's standing word) is the likely one, not proven. Whether any uncommitted file was in it is unread. S2 becomes a refusal when the author check is armed (CTO msg 107910), so a sparse worker would then fail its first commit unless org/ref joins the base set.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/2.0.0_SA_COO~C/L8_PACKET_ROUND18.md @c34d3f13fe",
    "python .tools/tests/test_round18_batch.py -> arms=3/4 skipped=1 ok=True; --real -> arms=4/5 skipped=1 ok=True and SAFE-COMMIT-SPARSE exit=0 tip_moved=True folders=7 green=True (2026-10-15 ~11:2xZ)",
    "python .tools/tests/test_worktree_gc_preserve.py -> arms=9/9 ok=True",
    "git worktree list | wc -l and git -C portal worktree list | wc -l before and after the --real run: 2/2 and 8/8",
    "git merge-base --is-ancestor e09ef0f0e5 HEAD -> true; git log --author 2.0.0_SA_COO~RB: 5d77dd8806 (drain of worker ~8)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Build notes and cured test hygiene. Round-19 candidates: W105-S2 (add org/ref to the sparse base set before the author check refuses) and W105-S5 (the four leftover temp fixtures)."
 }
]
```

-- 3.0.0_SA_CVO~L
