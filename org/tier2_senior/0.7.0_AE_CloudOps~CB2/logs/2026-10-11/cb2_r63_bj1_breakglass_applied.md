# The break-glass role exists: the stop got the canon fixed, and the re-run applied both objects in one pass — 0.7.0_AE_CloudOps~CB2

**Date:** 2026-10-11
**Task Order:** ADVI_COTBKF.TO-CB-bj-1 (AMENDMENT 1 @`85ef389f44`), risk **WORLD**
**Status:** COMPLETE

> Follows `cb2_r62_bj1_breakglass_targeted_apply.md`, which recorded the refused run. That stop was correct and is
> why this run exists; its log stands as the record of the refusal.

---

## Objective

Re-run `CB-bj-1` under AMENDMENT 1: create `cloudops-cot-restricted-breakglass-role` and its inline policy — now
named `RestrictedPrefixGetPutList` — by a targeted apply of exactly two IAM addresses, under the re-signed FWD-7
pair, so they never land as a rider on an untargeted apply (row `D2-S95`).

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| safe-apply.sh | `-chdir=.../shared-infra apply <saved plan>` | **PASS (rc=0)** | `NAMING-PLAN: PASS 2 graded` where round 62 read `REFUSE 2 graded` at rc=7 |
| opal_naming.py `grade()` | on all three names | PASS | `NO-SYSTEM-ASKED` for the new name is the **intended** verdict — the ruling's own subject says so |
| deploy_ledger.py | `open` (4 legs), `close-leg` ×4, `close`; `close --gate-refused` on r62 | PARTIAL | the r62 `--gate-refused` is not executable — see Decisions 4 |
| proof-of-spec-check | `<instance> AC1,AC2,AC3` | PASS | caught `kind: iam` being graded as a git ref |
| comp-iam / comp-schedule | not run | SKIPPED | DECLARED-NOT-APPLICABLE in the order's preflight |

**What worked:** checking `grade()` at the source *before* applying. The gate's PASS could have been accepted
blindly; reading the builder showed the new name returns `NO-SYSTEM-ASKED` rather than `CONFORMANT`, and the
ruling commit's subject confirms that is the designed outcome. A PASS you understand is worth more than one you
are relieved by.

**What failed:** nothing. Two instrument notes, both reported: `proof-of-spec-check` grades `kind: iam` as a
git-pinned artifact, which no live IAM object can satisfy; and AMENDMENT 1 named a ledger verb that did not exist
when the entry it targets was closed.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 0 | Hash the three NEW pins | all **equal**; `.tf` blob `1985337a9c…` on **both** reads the amendment names; worktree clean |
| 1 | `.open_deploys/` union, then open a NEW entry | **46 of 46** trees, per-tree 17–29, **104 distinct**; r62's own entry surfaced and was **measured, not acted on** |
| 2 | Targeted plan + the amendment's new STOP | `2 to add, 0 to change, 0 to destroy`; planned role name **MATCH**; policy `RestrictedPrefixGetPutList` |
| 3 | `safe-apply.sh` on the **saved** plan | **rc=0**, `NAMING-PLAN: PASS 2 graded`, `Apply complete! Resources: 2 added, 0 changed, 0 destroyed.` |
| 4 | Proof 1 on live IAM | ARN returned; `length(Statement)` = **1**; one principal; **4** actions, **0** deletes |
| 5 | Proof 2, plan only | `BREAKGLASS-PLAN-AFTER resources=242 the_two=2 the_two_changed=0` |
| 6 | Close the ledger | 4/4 proven, CLOSED |

## Verification

```
Apply complete! Resources: 2 added, 0 changed, 0 destroyed.
  aws_iam_role.restricted_breakglass        [id=cloudops-cot-restricted-breakglass-role]
  aws_iam_role_policy.restricted_breakglass [id=…-role:RestrictedPrefixGetPutList]

get-role  -> arn:aws:iam::313476888478:role/cloudops-cot-restricted-breakglass-role
          -> length(Statement) = 1
          -> arn:aws:iam::313476888478:user/Andrew_Berman_Console   (that ARN, nothing else)
get-role-policy RestrictedPrefixGetPutList -> 4 actions, 0 deletes, Cottonwood-only

BREAKGLASS-PLAN-AFTER resources=242 the_two=2 the_two_changed=0
```

---

## Decisions Made

1. **Read the trust's statement count separately rather than trusting a one-line principal output.** A single ARN
   on one line is exactly what would hide a second statement, and AC2's "and nothing else" is the half of the
   criterion a naive read drops. `length(Statement)` = 1 makes it measured.

2. **Verified both objects on live IAM rather than from `Apply complete!`.** The apply line is a producer's
   self-report about its own run. The same `get-role` returned `NoSuchEntity` a few hours earlier beside a passing
   positive control, so the instrument has a reading both ways on this exact name — which is what makes the
   present reading mean something.

3. **Measured round 62's entry instead of acting on it when the union surfaced it.** 5 of 46 trees carry a
   pre-close snapshot; the shared tree deleted the file at `bb3ab3a85a` and the entry reads CLOSED. World-done, so
   not re-executed and not re-closed — NEVER-2's rule, and the trap is real: a stale worktree HEAD shows an entry
   present when it is terminal.

4. **Reported AMENDMENT 1's un-executable instruction rather than faking or skipping it silently.** It directs
   closing round 62 with `deploy_ledger close --gate-refused`. That entry was already terminal at **08:11:42Z**,
   and the flag landed at **08:35:25Z** in the very commit that fixed the naming defect — 24 minutes later, and
   added in response to my row `D2-S99`. The verb cannot run on a closed entry; the substance it exists to record
   was already written into that entry's legs and disposition section.

5. **Re-kinded the two IAM artifacts `iam` → `aws_resource`.** `artifact-resolution` grades an `iam` row as a git
   ref and demands a commit-ish, which no live AWS resource has — there is no etag for an IAM object. Named the
   reason in the row rather than inventing a hex, and identified each object by its terraform id with the
   producing blob and drain commit in the text.

6. **Did not assume the role, on either run.** Condition 5 forbids it absolutely; whether the console user can
   assume it is that user's to exercise and is the order's own declared BLIND. `get-role`/`get-role-policy` read
   metadata and do not assume.

---

## Files Modified

| File | Change |
|------|--------|
| `.../task-orders/ADVI_COTBKF.TO-CB-bj-1...md` | `<status>` → complete (1 line) |
| `org/critical_paths/change_management/20261011T0901Z_advi-cotbkf-r63-bj1-...md` | new entry: opened, 4 legs proven, CLOSED |
| `org/critical_paths/.open_deploys/advi-cotbkf-r63-bj1-...json` | opened then cleared by the close |
| `.../deliverables/0.7.0_AE_CloudOps~CB2/breakglass_targeted_apply_report.md` | ADDENDUM 1 (+149 lines, append-only) |
| `.../deliverables/0.7.0_AE_CloudOps~CB2/ADVI_COTBKF.TO-CB-bj-1...proof_of_spec.json` | rewritten for this run: AC1/AC2 PASS, AC3 pending |
| `org/tier2_senior/0.7.0_AE_CloudOps~CB2/logs/2026-10-11/` | this log |

**AWS: 2 IAM objects created** — `cloudops-cot-restricted-breakglass-role` and its inline policy
`RestrictedPrefixGetPutList`. Nothing changed, nothing destroyed, no object read or written under the restricted
prefix.

---

## Blockers

**None on this order.** Owned elsewhere:

- **Row `D2-S95`'s disarm is the issuer's on proof 2** (condition 6). Its evidence now exists —
  `the_two=2 the_two_changed=0` — where before it did not. Still armed until the issuer disarms it.
- **Row `D2-S92` stands:** the untargeted plan from dell2 still reads the live `opalinvest-portal` bucket as
  deleted (rc=1, 2 AccessDenied). Proof 2 ran as a plan only and nothing was applied from it. The CTO's narrowing
  — targeted applies are safe from dell2 — is now measured sound twice.
- **Row `D2-S103`:** the generated naming carriers are stale at HEAD; regeneration is the canon owner's and did
  not hold this act, since the planned name matched.
- `CB62bj1-AC3` is PENDING-ADJUDICATION for `3.0.0_SA_CVO` at L9.
- The role's trust carries **no MFA or source-IP condition** — the design the CTO half signed as written, recorded
  for the design's owner. Not a defect this act introduced.

---

## Current State

All orders this seat has held are terminal and complete: `CB-al-2`, `CB-bi-2`, `CB-bj-1`. FWD-7's break-glass role
is live and inert until the console user assumes it. Zero orders runnable.

---

## Next Steps

1. `[2.0.0_SA_COO~C2]` Disarm `D2-S95` on proof 2's line.
2. `[3.0.0_SA_CVO]` `CB62bj1-AC3` at L9.
3. `[1.0.0_SA_CTO~DELL2]` `D2-S92` — the two IAM reads for `cloudops-dell2-agent-user`, or a standing rule that
   untargeted shared-infra plans are not taken on dell2.
4. `[owner of .tools/proof-of-spec-check.py]` `kind: iam` is graded as a git ref; a live IAM object cannot satisfy
   it. `aws_resource` is the workaround used here.
5. `[0.7.0_AE_CloudOps~CB2]` Nothing. Idle on the watcher.
