# T5 dead-consumer kill wave: 5 kills executed + verified, sovereign-ordered; live chain untouched

**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE

**Serial:** `0.7.0_AE_CloudOps~F` -- Window: 2026-08-04T04:26Z-05:15Z (COO GO 042634Z, CTO
split-gate ruling 042600Z under Andrew's categorical word)
**Commits:** K1 @ce77c1107, K2 @4fce27eff, K3 @1805ea2ae, K4 @5b54436a0, K5 @bd1470c80 + closes
(this commit) **Tags:** mdpf-pipeline-v2.0.1 **Applies:** 2 targeted safe-applies (3+2 destroys,
mdpf-pipeline) + 1 targeted safe-apply (4 destroys, canonical-schwab-si2-schedule, after init
-reconfigure) **S3:** 10 objects deleted (delete markers recorded per key)

---

## Summary

The dead-consumer half of the T5 teardown, executed the night the gate opened. Five kills, each:
one commit + a change record with rollback note in org/critical_paths/change_management/ + live
destroy verification with a positive control. Scope discipline held: everything live-serving,
chain-coupled, rider-blocked, or CTO-frozen was left standing and the record says why per row
(kill-list amendment #5 @same commit as this log).

Two judgment calls worth the record: (a) K5 widened from the verdicted rule to its single-purpose
role+policy ONLY after a live blast-check proved the two LIVE daily-pull rules target a different
role -- killing the rule alone would have manufactured a fresh dead grant; (b) row 17's shadow-S3Key
half is a recorded NO-OP -- the "declarations" are graph entries from out-of-scope writer code, and
a kill wave must not invent a deletion where no resource exists.

## Compiler Tools

| Run | Observed | Verdict |
|---|---|---|
| `comp-iam gaps` (after iam.tf change, AE minimum + risk-reflex citation) | Zero checker-related gaps; 17 pre-existing estate items unrelated to this change | PASS -- removal introduced no gap |
| `comp-grep` x4 (TF management-plane checks per resource root) | freshness-checker in mdpf-pipeline iam.tf; SSM doc TF-managed legacy-emit-ssm.tf; si2 rule in its own root; live daily-pulls NOT in TF (0/462 files) | PASS -- every kill routed via its true management plane (Rule: TF-managed dies via TF) |
| Targeted plans + safe-applies (Rule 18) | 3/3 plans read exactly the intended destroys (3, 2, 4); applies matched; K5 root needed init -reconfigure first | PASS -- no non-target drift touched |
| Live verifies (Rule 22a/22b) | NoSuchEntity / InvalidDocument / ResourceNotFoundException on all killed resources, each with a SAME-CALL-SHAPE positive control; live pulls ENABLED post-kill; protected S3 survivors listed intact | PASS -- every death exercised, none inferred |

## Blockers

None. The remaining kill-list rows are gated exactly as designed (three-gate teardown / C1+C2 at DS
/ riders / DE-lane row 15 flagged).

## Next Steps

1. **[2.0.0_SA_COO + 1.0.0_SA_CTO]** Kill-wave report (sent this window) -- validation at your gates.
2. **[0.4.0_DE]** Row 15 dead root fetcher (portal-side) -- flagged, not touched (GO exclusion).
3. **[0.7.0_AE_CloudOps~F]** Event-driven standby; T3.B on the T2.C clock (bound now 09:50-10:00 ET
   per v3); remaining teardown waves on their gates.
