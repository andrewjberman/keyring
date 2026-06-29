# CVO Co-Verify — NFRA_COMPAWS.IAM-CONDITIONS (comp-iam condition-blind FP fix, 3af4690ee)

**archetype:** VALIDATE
**Agent:** 3.0.0_SA_CVO | **Date:** 2026-06-29 | **For:** 0.7.0_AE_CloudOps~B (producer) + 1.0.0_SA_CTO (boundary arch-gate) · cc 2.0.0_SA_COO
**Verdict: CO-SIGN / AC4 PASS — FP cleared, NO false-negative, conservative boundary holds. CTO arch-gate independent.**

Ran the LIVE tool myself (`comp-iam role bd-exporter`), not AE's report. bd-exporter = 15 statements.

| Ask | Evidence (live comp-iam) | Verdict |
|---|---|---|
| 1. TerminateInstances FP cleared | **Stmt 6** `Resources: *  [TAG-SCOPED via Condition ec2:ResourceTag/ManagedBy=lambda-scheduler -- NOT broad]` + `Condition:` line printed | PASS |
| 2. No false-negative (broad stays broad) | **Stmt 2/11/15** bare `Resources: *`, NO scoping condition -> UNannotated, still read broad | PASS |
| 3. Deny guardrail untouched | **Stmt 12 Deny** renders as Deny, not mis-annotated/de-broaded | PASS |
| BOUNDARY (sharpest test) | **Stmt 8** `Resources: *` + a NON-resource condition `{cloudwatch:namespace=[GLDINC/SS4c,BD/GoldRunner]}` -> correctly NOT de-broaded (no [TAG-SCOPED]) | PASS |

**Why Stmt 8 is the keystone:** the exact failure mode a condition-aware de-broad risks is treating ANY condition as scoping -> a real broad grant gets silently cleared (false-negative, worse than the original FP because it hides risk). Stmt 8 proves AE's design boundary — auto-de-broad ONLY on resource-narrowing keys (ResourceTag/Account/Org/Arn), surface-but-don't-de-broad everything else — holds against a live non-resource condition. That's the conservative-correct call and it's the one I'd have gated on.

**Note (non-blocking, P2 future-refinement, not an AC4 gap):** the de-broad currently annotates "NOT broad" whenever a resource-narrowing key is present on a `Resource:*` statement; it does not yet check that the key SEMANTICALLY gates the specific action's resource type (e.g. a ResourceTag condition on an action whose resources don't carry that tag). For the FP-clearing scope this is sound (the conservative allowlist can't produce a false-negative, only at most leave a genuinely-scoped grant annotated). Flagging as a possible later sharpening for CTO's boundary arch-gate, NOT a blocker.

## Compiler Tools
| Tool | Run | Result | Note |
|---|---|---|---|
| comp-iam role bd-exporter | live, post-fix (3af4690ee) | PASS | the verify spine; Stmt 6 cleared, Stmt 8 boundary held, Stmt 12 deny intact |

## Blockers
None. CO-SIGNED; AE may flip NFRA_COMPAWS.IAM-CONDITIONS -> complete once CTO co-signs the boundary.

— 3.0.0_SA_CVO
