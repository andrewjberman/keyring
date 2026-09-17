# AMGT_RESAPP round 12: a redeploy regression rolled back, and four issuer amendments the workers never had to discover -- 2.0.0_SA_COO~Z

**archetype:** COORDINATE
**Date:** 2026-09-16
**Task Order:** AMGT_RESAPP round 12, the issuer's L7 drain (16 orders AMGT-rk-1..rk-16)
**Status:** WORKING -- 7 of 16 terminal, 2 workers live, 0 calls open at 1.0.0_SA_CTO~Z

---

## Objective

Continue the round after the 07:56Z reboot recovery (previous log, 13:37-15:05Z): drain the completions, cut the CTO's rulings
into the orders BEFORE the workers reach them, and keep the served plane honest.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| safe-merge.sh | 4 drains (wk-12-25 twice, wk-12-26, wk-12-24) | 4 MERGED | 3 hit the channel append collision; the scratch `union_channel.py` resolved each as HEAD rows + branch-appended rows, counts printed |
| safe-commit.sh | amendments 6-9, the rollback ledger, the log | 6 PASS | row gate, to-pipeline-gate (viii) on every modify, msg-verify MATCH each |
| safe-apply.sh | the rollback, from `C:/tmp/coo-amgt-rk2-rollback` | Apply complete 0/2/0 | blocked once on a ROUTINE halt surface (182 pending, 2 stale RED ledgers); `HALT_ACK=1` only after reading 0 STOP-class lines in 550 |
| terraform plan (targeted) | twice before the apply, once after | 2 changes, then No changes | the second plan is the rollback's 0-diff proof |
| deploy_ledger.py | open / close-leg x5 / close | CLOSED 16:22:03Z | the 15:19Z act had NO entry: rk-2's grant never named the directory (issuer defect, row W24-S4) |
| census.py (scratch) | pre/post GET route census | 5 of 8 -> 7 of 8 | the instrument that made the regression and its repair both measurable |
| comp-tool rail | two compound calls carrying `find`/`grep` segments | DENIED, whole call aborted | neither the drain nor the ledger-open inside them ran; caught by re-reading the artifacts, not by the exit code |

**What worked:** running every queued order's criteria against the live world before any worker reached them. Eleven defects in
eight orders were found that way, including three that could never pass and two that could never fail.
**What failed:** my own amendment 2 (pre-reboot) shipped two of those defects, and rk-2's own face ordered a ledger entry its grant
could not write. Both are recorded as rows rather than quietly fixed.

---

## Work Completed

### 1. The regression, and the rollback (rows W24-S3, S128)
`AMGT-rk-2`'s worker applied the co-signed grant and redeployed the adapter at **15:19:34Z**. The redeploy exposed a pre-existing
defect it could not fix: `lib/research/rules/peer.py` and `figure.py` read `deliverables/0.9.0_WK_AMGT_RESAPP~8/distributions/*.json`
**at import time**, and the Lambda zip carries no `org/` tree, so **`/overlay` and `/thesis` went 200 -> 500** for every
model-block-covered key. `lib/research/rules/` was in no round-12 grant.
I escalated at 15:39Z; `1.0.0_SA_CTO~Z` ruled ROLLBACK FIRST on the worker's report or at 16:05Z, whichever came first, and amended
its own co-sign half: **a function-code redeploy's blast radius is EVERY route the function serves**, not the two the half named.
Executed at the bound, after the worker had committed and left the deploy in place:
- pre-census 16:07:51Z -- 5 of 8 GET routes at 200
- artifact latest <- the co-signed version (sha verified BEFORE the copy), then a TARGETED apply of code + policy
- post-census 16:19:54Z -- **7 of 8**, `/overlay` and `/thesis` restored, none lost, `/print` 500 pre-existing
- both IAM limbs read back at the nine; env unchanged; 0-diff replan
Ledger `20260916T1606Z_amgt-scoped-api-rk2-rollback-20260916` CLOSED with 5 legs, committed `817d827e39`. The CTO verified it on its
own instruments at 16:27Z and closed the escalation.

### 2. Four issuer amendments
| # | Commit | What |
|---|--------|------|
| 6 | d1540135e1 | the QUEUED-order dry run: 7 criteria re-cut over 5 orders, rk-14's grant widened to the presets' real home, rk-13 AC4 added on ruling S120 |
| 7 | cace3c693d | both CTO rulings: rk-3 AC3 at the latest generation's own date; cell K's ONE SHAPE across rk-7 AC3 and rk-12 AC4; the dated fallback as rk-7 AC4 |
| 8 | 91141aebd2 | the adapter partition: rk-12/rk-16 route criteria moved to rk-6, rk-15's served criterion to rk-7, two chain-A grants narrowed, rk-6's missing co-sign bound added |
| 9 | 1c0639a019 | rk-2 re-cut: AC7 non-regression census, AC8 packaging census, AC5 onto the route that exists, grant widened to `rules/` and the ledger |

### 3. Drains and spawns
rk-3 COMPLETE (`8cd7afd41c`), rk-5 COMPLETE (`b57d3ac097`), rk-2 drained OPEN (`ec4bf1f8d0`). Fresh slots spawned at HEAD for
rk-2 (the packaging fix-forward) and rk-13 (the ranker re-run).

---

## Decisions Made

- **Cell K's ONE SHAPE is the enqueue route**, not an adapter that sends: the adapter role holds NO SQS grant and the ruling's
  condition (5) forbids adding one, while the enqueue Lambda already holds it. Recorded with its reason in row S126.
- **AC8 is a STATIC census, not a smoke run.** An extracted-artifact run raises ModuleNotFoundError on this box for EVERY artifact
  (Linux-built extensions), so it could never discriminate here. Stated in the criterion.
- **Worktrees are kept after their drains.** Removing one is a recursive delete; chain A's portal merge branch lives in ~23's.

---

## Blockers

None at this seat. Three cards stand at Andrew: CARD 1 (the model-block pull), CARD 2 (the filings batch) and CARD 3 (the portal
DEV fast-forward and push, ruled ONE reserved leg by the CTO). Without them the product is five names and the page is on one disk.

---

## Next Steps

1. Drain rk-2 and rk-13 as they report; union the channel.
2. Then rk-6 (chain B, carrying rk-12's and rk-16's adapter halves), rk-8 (chain A, once rk-2 has landed) and rk-14 (chain C).
3. rk-7 spawns only after rk-15 drains, per amendment 8's sequence.
4. At drain-end: ONE L8 packet to `3.0.0_SA_CVO~Z`, carrying the held partition (70 names: 23 on CARD 1, 47 on no carded decision),
   the moved-criterion map so L9 grades each cell whole, and the CRO's item-5 finding that the page is on one disk.

Push state: LOCAL on SITEZ (LD-0522 puts the push with `0.0.0_AB_MSTR~Z`).
