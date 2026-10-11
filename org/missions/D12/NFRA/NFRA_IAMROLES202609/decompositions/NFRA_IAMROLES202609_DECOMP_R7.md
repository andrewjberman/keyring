# NFRA_IAMROLES202609 -- L5 DECOMPOSITION, ROUND 7 (FWD-4 enrichment: the last two adoptions, and the dead grants narrowed)

**Cut by** `2.0.0_SA_COO~ZI` **at L5, 2026-10-11.**
**Consumes:** `1.0.0_SA_CTO~Z`'s round-6 analysis `ledger/ROUND_ANALYSIS.round6.md` @`2f49aa235b` (ENRICHMENT LIST E1-E3,
the rulings table), `deliverables/0.7.0_AE_CloudOps~Z/ADOPTION_PLAN_TEN.md` @`59112aafed` (Family C), and rows Z-S23 /
Z-S32 of the surprise channel.

Rounds 1-6 stay in place so their instances keep resolving. This is a seventh file, not an edit. FWD-4 is REALIZED (round
6); this round ENRICHES it and re-opens nothing.

---

## 1. THE RECTANGLE -- TWO ITEMS CUT, ONE HELD, ONE REPAIR TAKEN DIRECT

| cell | item | rows | module | issued to | risk |
|---|---|---|---|---|---|
| `IAM-x-1` | E1 adopt Family C | 6 `lambda-ec2-runtime-monitor-role` (IN USE, last 2026-10-11); 14 `sentiment_query_api-role` (underscore in the name) | row 6: a NEW file in `infra/aws/terraform/shared-infra/` (round-5 home ruling); row 14: the module the survey names | `0.7.0_AE_CloudOps~IR` | WORLD |
| `IAM-x-2` | E2 narrow the dead grants | Z-S23 `opal-smartx-lambda-role` (`opal-smartx-s3-access` on two NoSuchBucket buckets; `opal-smartx-secrets` on a us-east-2 ARN where only us-east-1 exists); Z-S32 `codebuild-semantic-clustering-role` (`CodeBuildSemanticClusteringPolicy` names a NoSuchBucket) | `smartx-pipeline/` (`-target` ONLY, row Z-S21 drift) and `news-pipeline/` | `0.7.0_AE_CloudOps~IR` | WORLD |
| -- | E3 retire `lambda-test-role` (row 7) | 7 | none | **NOT CUT** | -- |
| -- | batch repair: five disposition tokens ADOPT -> DECLARED | 1, 2, 3, 9, 11 | none | **DIRECT-ACT by the issuer** @`f05553f5be` | LOCAL |

**E3 is HELD on Andrew's word** (the analysis: deleting an IAM role cannot be undone; a re-created role gets a new role
id, so trust and resource policies that pin the old principal break). The issuer files the call with the disposition's
three-plane evidence. E3 is cut only on his yes, as an addition to this rectangle.

**Each WORLD order runs in TWO PHASES under one order**, as in round 6. PHASE A plans and surveys and applies nothing;
PHASE B applies only the plan its never-widen pair signs. The pair cannot name a blast radius before the plan is read.

**Cell ids:** `IAM-x-1`, `IAM-x-2`, checked against `CELL_ID_RE` (`.tools/to-decomp-ref-lint.py:65`) at the cut.

---

## 2. THE BATTERY (2026-10-11, base `HEAD` at the cut)

```
comp-iam           bash .tools/comp-iam stats: 219 IAM roles parsed / 196 services / 175 Lambda services.
comp-schedule      python .tools/comp-schedule --budget 120: BUDGET REACHED, 1 of 6 carriers, C1=23 (7 gates POSITIVE),
                   C2=23 PARTIAL (0 of 23 ledger entries scanned), rc=3 -- PARTIAL_OR_BLIND, never read as clean; each
                   PHASE B reads .open_deploys/ for its module before its ledger opens.
comp-adversary     premises re-derived 4 of 4: the omission rule (an aws_iam_role block never sets inline_policy or
                   managed_policy_arns); A4-r6's order (declaration committed before any import, row Z-S27); the -target
                   bound on smartx-pipeline (Z-S21, three pre-existing Lambda drifts); and that a removed statement is
                   read LIVE to name nothing (NoSuchBucket / absent secret) WITH a positive control on one existing
                   resource, since a failed read returns a value too.
live reads         lambda-ec2-runtime-monitor-role created 2026-02-06, last used 2026-10-11T04:21Z (in use);
                   sentiment_query_api-role created 2025-11-24, last used 2026-01-02;
                   codebuild-semantic-clustering-role inline: CodeBuildSemanticClusteringPolicy (1).
naming gate        dell1 LGIC_ENFORCE FWD-8 is REALIZED (@97b794cd7a, relay msgs 33178 / 33179) but NOT yet in
                   box/sitez. Until it lands, an adopted name may still be refused; the survey grades the staged
                   rename with the gate BEFORE any commit (the safe probe of row Z-S35), never by committing.
```

---

## 3. BOUNDS

```
THE OMISSION RULE     no aws_iam_role block sets inline_policy or managed_policy_arns (x-1 and x-2 alike).
                      x-2 manages an inline policy ONLY as its own aws_iam_role_policy resource.
PLAN BEFORE PAIR      no PHASE B before both NEVER_WIDEN_ROUND7_<cell>_{COO,CTO}_HALF.md exist, signed for the survey's plan.
ORDER OF ACTS         A4-r6, carried: commit the declaration on the worker branch BEFORE any import, then the -target
                      apply, then drain the same session, then the untargeted shared-tree plan reads 0 to destroy.
NAMING                if the gate refuses a name on a limb no override reaches, the cell STOPS before any import and
                      the issuer brings it to 1.0.0_SA_CTO~Z (the analysis' rule for row 14).
ONE APPLY PER MODULE  x-1 is two applies (shared-infra + row 14's module); x-2 is two applies (smartx-pipeline, news-pipeline).
x-1 PERMISSIONS       none move (C-TWO-REMEDIES): custody and the module's default_tags only.
x-2 PERMISSIONS       ONLY statements whose every resource is read live as non-existent are removed; every other
                      statement of the policy is byte-identical after. Nothing is added. No trust change.
G-21 / G-25           no alert, monitor, schedule; no Access Analyzer.
```

---

## 4. DEPENDENCY EDGES

```
IAM-x-1  <- (none)        PHASE B <- its pair(s)
IAM-x-2  <- (none)        PHASE B <- its pair(s)
```

The two orders share no module unless the survey homes row 14 in `news-pipeline/`. In that case the two PHASE B applies
there serialize on `.open_deploys/`: the second opens its ledger only after the first closes.
`fanout: 2 of 2 chains, cap 8`. One assignee holds both, so they run in the order the assignee takes them.

**WRITE SURFACE** (both orders add `deliverables/0.7.0_AE_CloudOps~IR/round7/`, the ledger dirs, the channel and the order itself):

```
IAM-x-1   infra/aws/terraform/shared-infra/zz_adopt_family_c_row6.tf.proposed (-> .tf at PHASE B);
          row 14: PHASE A commits its draft as deliverables/0.7.0_AE_CloudOps~IR/round7/zz_adopt_family_c_row14.tf.draft
          and names the home module in the survey. An issuer amendment admits
          infra/aws/terraform/<that module>/zz_adopt_family_c_row14.tf before PHASE B. No path is granted before its
          module is known.
IAM-x-2   infra/aws/terraform/smartx-pipeline/zz_narrow_z_s23.tf.proposed (-> .tf);
          infra/aws/terraform/news-pipeline/zz_narrow_z_s32.tf.proposed (-> .tf)
```

---

## 5. RULE 24 -- THE FOUR-POSTULATE RECORD

**(i) MECE.** Domain = E1, E2, E3 and the batch repair (the analysis' list). E1 -> x-1, E2 -> x-2, E3 -> HELD (not cut,
named), repair -> DIRECT-ACT. Each item is in exactly one place.
**(ii) SAME GRAIN.** One cell = one analysis item; one apply = one module.
**(iii) INTENT.** x-1 moves custody only; x-2 removes dead permissions only. The two are kept in separate cells because
they are different remedies (C-TWO-REMEDIES) and get separate pairs.
**(iv) STATE.** x-1 moves a role from "named owner" to "in code" and changes at most its tags. x-2 removes statements that
reach nothing live and changes no live statement, no trust and no tag. Neither moves the other's rows, and neither
retires a role.

---

## 6. WHAT THE ROUND CANNOT CLAIM

- After round 7, at most 8 of 16 rows are in code. Row 7 waits on Andrew, rows 5 and 16 stay deferred, and rows 8 and 10
  stay INERT. FWD-4 already stands on owner-and-reason.
- x-2 proves the removed statements named nothing AT THE READ. A bucket name is global, and nothing here stops someone
  from creating that name later. That is exactly why the dead Allow is removed rather than left.
