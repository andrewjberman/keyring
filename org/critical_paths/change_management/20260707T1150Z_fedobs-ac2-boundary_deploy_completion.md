# Deploy Completion Record
**Date opened:** 2026-07-07T11:50:15.300084+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260707T115458Z
**Deploy:** NFRA_FEDOBS-P1 AC2 read-only-on-truth boundary role (fedobs.tf db0753623, authored by 0.5.0_AE_OpalETL; COO-ruled globgrph-owner coordinated apply). Additive-only crown-jewel: opal-globgrph-fedobs-emitter-task -- Allow PutObject fedobs findings/signals ONLY + explicit Deny-overrides-Allow on the truth prefixes.
**Authored by:** 0.7.0_AE_CloudOps
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | fedobs.tf db0753623 (0.5.0) on CLOUD | hash pushed origin/CLOUD | fedobs.tf db0753623 (0.5.0) + 2 coordinated-apply tag-fixes (0.7.0~B: comma->dashes charset, project->subproject collision) committed + pushed origin/CLOUD | CLOSED 20260707T115457Z |
| L2 | activation | coordinated safe-apply fedobs (3 resources) | targeted plan 3add/0chg/0destroy applied + 0-diff | safe-apply (HALTGT, targeted): Apply complete 3 added/0 changed/0 destroyed (opal-globgrph-fedobs-emitter-task + FedobsEmitterLogs + FedobsWriteScoped). 2 pre-apply fixes needed (IAM tag charset + default_tags collision; plan doesn't validate either). 0-diff re-plan: infrastructure matches. | CLOSED 20260707T115457Z |
| L3 | verify | live get-role-policy shows FedobsDenyWriteTruth + scoped-write-only | Rule-22a applied + CVO AC2 exercise-cert (write-to-truth -> AccessDenied) | Rule-22a live get-role-policy: FedobsWriteScoped has FedobsFindingsAndSignalsWrite(Allow PutObject findings/signals) + FedobsOwnRead + FedobsDenyWriteTruth(Deny PutObject/DeleteObject on truth prefixes) -- the AC2 Deny-overrides-Allow boundary is LIVE. CVO AC2 exercise-cert (real write-to-truth -> AccessDenied via 0.5.0's fedobs_emit.py --assert-boundary) = CVO scope, handed off. | CLOSED 20260707T115458Z |

## Log

- 20260707T115015Z OPENED by 0.7.0_AE_CloudOps with 3 leg(s)
- 20260707T115457Z LEG L1 closed: fedobs.tf db0753623 (0.5.0) + 2 coordinated-apply tag-fixes (0.7.0~B: comma->dashes charset, project->subproject collisi
- 20260707T115457Z LEG L2 closed: safe-apply (HALTGT, targeted): Apply complete 3 added/0 changed/0 destroyed (opal-globgrph-fedobs-emitter-task + FedobsE
- 20260707T115458Z LEG L3 closed: Rule-22a live get-role-policy: FedobsWriteScoped has FedobsFindingsAndSignalsWrite(Allow PutObject findings/signals) + F
- 20260707T115458Z CLOSED -- all 3 legs proven
