# NFRA_IAMROLES202609 -- L5 DECOMPOSITION, ROUND 6 (FWD-4: three families adopted into code, two rows deferred on the record)

**Cut by** `2.0.0_SA_COO~ZI` **at L5, 2026-10-09.**
**Consumes:** `1.0.0_SA_CTO~Z`'s round-5 analysis `ledger/ROUND_ANALYSIS.round5.md` @`f77e32d7c3` (the ENRICHMENT LIST, E1-E4, and
the four home rulings), `deliverables/0.7.0_AE_CloudOps~Z/ADOPTION_PLAN_TEN.md` @`59112aafed` (the families and their order).

Rounds 1-5 stay in place so their instances keep resolving. This is a sixth file, not an edit.

---

## 1. THE RECTANGLE -- FOUR ITEMS, FOUR ORDERS

| cell | item | rows | module | issued to | risk |
|---|---|---|---|---|---|
| `IAM-w-1` | E1 Family B (SmartX) | 9 `opal-smartx-lambda-role` | `infra/aws/terraform/smartx-pipeline/` | `0.7.0_AE_CloudOps~Z` | WORLD |
| `IAM-w-2` | E2 Family A (BD) | 1 `bd-merge-daily-lambda-role`, 2 `bd-pipeline-task-role` (ECS trust) | `infra/aws/terraform/bd-pipeline/` | `0.7.0_AE_CloudOps~Z` | WORLD |
| `IAM-w-3` | E3 Family E + row 3 | 11 `portfolio-management-lambda-role`; 3 `codebuild-semantic-clustering-role` | `portfolio-management/` and `news-pipeline/`, ONE apply per module | `0.7.0_AE_CloudOps~Z` | WORLD |
| `IAM-w-4` | E4 the two DEFER rows | 5 `finbert-ec2-backfill-role`, 16 `workspace-sync-lambda-role` | none (governance record only) | `0.7.0_AE_CloudOps~Z` | LOCAL |

**Each WORLD order runs in TWO PHASES under one order** (the issuer's ruling inside its decomposition, the same reason round 5
split E3: a never-widen pair cannot name a blast radius before the plan is read):
- **PHASE A (no apply):** write the declaration as an INERT `<module>/zz_adopt_<family>.tf.proposed`, plan it once in the
  lane's own worktree under a `.tf` name, and write `PLAN_SURVEY_<family>.md`. The survey records the plan summary, the
  module's provider `default_tags` keys, whether any is an authorization key (`safe-apply`'s KEY COLLISION line), the state
  key the resources land in, and the role's live tags. Commit the `.tf.proposed` and the survey. **STOP and report.**
- **PHASE B (the apply), only after the order's never-widen pair is SIGNED:** rename to `.tf`, `safe-apply` with the deploy
  ledger open, read the post-apply plan, close the ledger.

The issuer's GO for PHASE B is a status flip plus a message; PHASE A's GO is the issuance.

**NOT IN ROUND 6, per the analysis:** Family C (rows 6 and 14, adopted LAST in round 7; row 6 into `shared-infra/` in a NEW
file) and Family F (row 7 RETIRE, a WORLD deletion with its own pair, round 7).

**Cell ids:** `IAM-w-1..4`, checked against `CELL_ID_RE` at the cut.

---

## 2. THE BATTERY (2026-10-09, base `HEAD` at the cut)

```
comp-iam           214 IAM roles parsed / 196 services / 1154 operations (round 5's read, unchanged module set).
comp-schedule      PARTIAL_OR_BLIND at the round-5 read (1 of 6 carriers); the assignee reads .open_deploys/ for EACH
                   module before its PHASE B ledger opens.
comp-adversary     premises re-derived 3 of 3: the omission rule (ADOPTION_PLAN_TEN section 2: inline_policy and
                   managed_policy_arns ABSENT, or the next run detaches live policies); the default_tags hazard (9 of 10
                   roles carry 0 tags, and data-refresh's root showed a KEY COLLISION on `Project`); row 2's ECS trust.
precedent          round 2's candidate infra/aws/terraform/data-refresh/zz_adoption_candidate.tf.proposed (blob
                   b3a1298d6b) is the shape: one aws_iam_role + one import block per role, labels namespaced to the role.
```

---

## 3. BOUNDS

```
THE OMISSION RULE     no aws_iam_role block sets inline_policy or managed_policy_arns. Setting either makes it
                      AUTHORITATIVE and detaches every unlisted live policy on the next run.
PLAN BEFORE PAIR      no PHASE B before both NEVER_WIDEN_ROUND6_<cell>_{COO,CTO}_HALF.md files exist, signed for the
                      survey's exact plan.
PLAN SHAPE            PHASE B applies only a plan of `N to import, 0 to add, 0 to destroy` plus at most the tag
                      in-place updates its pair names. Anything else stops the act and is a surprise row.
ONE APPLY PER MODULE  w-3 is two applies, two ledger entries, two pairs.
C-TWO-REMEDIES        no permission is narrowed or widened; the policies are untouched.
G-21 / G-25           no alert, monitor, schedule; no Access Analyzer.
```

---

## 4. DEPENDENCY EDGES

```
IAM-w-1  <- (none)        PHASE B <- its pair
IAM-w-2  <- IAM-w-1        the ADOPTION_PLAN order (B first, "the cheapest real exercise"), PHASE B <- its pair
IAM-w-3  <- IAM-w-2        then E; PHASE B <- its two pairs
IAM-w-4  <- (none)        LOCAL; the lane prepares the two rows, the issuer lands them as carrier (A1, row Z-S19)
```

**WRITE SURFACE** (all orders add `deliverables/0.7.0_AE_CloudOps~IR/round6/`, the channel and the order itself):

```
IAM-w-1   infra/aws/terraform/smartx-pipeline/zz_adopt_family_b.tf.proposed (-> .tf at PHASE B), ledger dirs
IAM-w-2   infra/aws/terraform/bd-pipeline/zz_adopt_family_a.tf.proposed (-> .tf), ledger dirs
IAM-w-3   infra/aws/terraform/portfolio-management/zz_adopt_family_e.tf.proposed and
          infra/aws/terraform/news-pipeline/zz_adopt_row3.tf.proposed (-> .tf), ledger dirs
IAM-w-4   deliverables/0.7.0_AE_CloudOps~IR/round6/ only (the two disposition rows are prepared uncommitted; the issuer lands them)
```

One assignee holds all four, so the w-1 -> w-2 -> w-3 chain is the plan's own order. w-4 is independent.
`fanout: 2 of 2 chains, cap 8`.

---

## 5. RULE 24 -- THE FOUR-POSTULATE RECORD

**(i) MECE.** Domain = E1-E4. One cell each. The 16 rows partition: in code before round 6 (13), owned by the CTO (4, 12,
15), adopted in round 6 (9, 1, 2, 11, 3), deferred in round 6 (5, 16), round 7 (6, 14, 7), and the 2 production rows
already accepted with an INERT candidate (8, 10). That is 1 + 3 + 5 + 2 + 3 + 2 = 16.
**(ii) SAME GRAIN.** One family = one module = one apply (w-3 is two families' worth, two applies).
**(iii) INTENT.** Governance only: custody moves into code; permissions do not move.
**(iv) STATE.** A PHASE B moves a role from "named owner" to "in code". It does NOT change the role's policies, trust or
usage. Its tags change only if the pair names that.

---

## 6. WHAT THE ROUND CANNOT CLAIM

- FWD-4 does not reach "every role in code": rows 6, 7, 14 wait for round 7, rows 5 and 16 are deferred, and rows 8 and 10
  stay INERT. The FWD-4 bar is met on owner-and-reason (16 of 16 since round 5); round 6 converts five more to in-code.
- A clean post-apply plan proves the declaration matches live AT THAT MOMENT. It says nothing about a later out-of-band
  change.
