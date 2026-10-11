# The break-glass role was not created: a correct Branch A plan, then the naming gate refused the apply on a rule defect — 0.7.0_AE_CloudOps~CB2

**Date:** 2026-10-11
**Task Order:** ADVI_COTBKF.TO-CB-bj-1 (issued @`bac3f66620`), risk **WORLD**
**Status:** BLOCKED — stopped between Branch A and step 3; nothing created, nothing stranded

---

## Objective

Create FWD-7's `cloudops-cot-restricted-breakglass-role` and its inline policy by a **targeted** apply of exactly
two IAM addresses, under the FWD-7 never-widen pair, so they do not land as a rider on some later untargeted apply
of `shared-infra` (row `D2-S95`, ARMED).

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| safe-apply.sh | `-chdir=.../shared-infra apply <saved plan>` | **BLOCKED (rc=7)** | did exactly its job — held at the last reversible moment; terraform never invoked |
| deploy_ledger.py | `open` (4 legs), `close-leg` x4, `hold --pre-apply`, `hold`, `close` | PARTIAL | both `hold` forms refused; no state exists for a gate-refused apply → row `D2-S99` |
| opal_naming.py `grade()` | called directly on both names | PASS | the decisive read: the policy name **raises**, it does not grade |
| proof-of-spec-check | `<instance> AC1,AC2,AC3` | PASS | VALID rc=0 first try |
| comp-rail | denied one recursive grep of the gate sources | PASS | correct denial; re-ran with native Grep, then dropped the root-cause as out of scope |
| comp-iam / comp-schedule | not run | SKIPPED | DECLARED-NOT-APPLICABLE in the order's own preflight |

**What worked:** calling `opal_naming.grade()` directly instead of believing the gate's message. The gate printed a
REFUSE *and* a replacement name, which invites typing the replacement in; the direct call showed `grade()` raises
`RaiseDefect` and returns no verdict at all for that name, confirming the gate's own parenthetical that this is a
rule/registry defect rather than a naming verdict.

**What failed:** `deploy_ledger.py` has no state for this act — see Decisions 3.

**Gap found:** two, filed as `D2-S98` and `D2-S99`.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 0 | Hash the two halves + verify the `.tf` blob | all three **equal**; blob `26aa1a2633…` identical at `8c6fc7652a` and HEAD; HEAD contains `9b8eb8c244` |
| 0b | Read both halves in full | CTO half **narrows `D2-S92`** to untargeted applies and names this seat + dell2 as applier |
| 1 | `.open_deploys/` union, then open the ledger | **43 of 43** trees, per-tree 17–29, **101 distinct** paths, 0 naming this act; entry opened before the plan |
| 2 | Targeted plan, saved outside the repo | **`Plan: 2 to add, 0 to change, 0 to destroy.`**, exactly the two targets, rc=0, 0 errors → **Branch A** |
| 3 | `safe-apply.sh` on the saved plan | **rc=7, BLOCKED by the naming plan limb.** Terraform never invoked |
| 3b | Verify the world | role `NoSuchEntity` (control passes); state **253** rows, **0** breakglass (control: 10 `lgic_firm`) |
| 4 | Proof 1 | **unreachable** — reads objects that were never created |
| 5 | Proof 2 | **not run** — would have printed the pre-state under the criterion's own expect token |
| 6 | Close the ledger | 4/4 dispositioned, CLOSED, + a CLOSE DISPOSITION section carrying the hold |

## Verification

```
[naming-plan-gate] NAMING CONFORMANT aws_iam_role.restricted_breakglass
    cloudops-cot-restricted-breakglass-role -> cloudops-cot-restricted-breakglass-role
[naming-plan-gate] NAMING REFUSE aws_iam_role_policy.restricted_breakglass
    restricted-prefix-get-put-list -> cloudops-49f-restricted-breakglass-policy
  why: ... [grade() said: RAISE as IAM_POLICY: a rule or registry defect, not a naming verdict:
  R1.f: 'restricted' is in no vocabulary; no registry row resolves it. DEC-6: refused like any
  refusal once enforcing]
safe-apply: BLOCKED by the naming plan limb (LGIC_ENFORCE DEC-6, ENFORCE mode, rc=1). Nothing was
  planned further or applied.
```

Measured at the source:

```
grade('cloudops-cot-restricted-breakglass-role','IAM_ROLE')  -> ('CONFORMANT', 'cloudops-cot-...')
grade('restricted-prefix-get-put-list','IAM_POLICY')         -> raises RaiseDefect R1.f
```

---

## Decisions Made

1. **Did not type in the name the gate said was owed.** `cloudops-49f-restricted-breakglass-policy` carries the
   **49f** firm token on a policy whose only grants are on `opal-data-cottonwood`'s
   `commonwealth/cottonwood/bronze/crm/` prefix — while the same gate graded the sibling *role* conformant as
   `cloudops-`**`cot`**`-`. Adopting it would commit a cross-firm mislabel on an IAM object. Rule 30 independently
   makes a builder refusal a registry row to add, never a hand-typed workaround; the registry isn't in this
   order's grant and is the laptop CTO's; and editing the `.tf` literal would change the very blob both halves
   pinned. Three reasons, any one sufficient.

2. **Did not invoke Branch C's pre-authorised destroy.** Branch C presupposes the role *created* and its policy
   refused by the applier's **credentials**. Here neither object exists and the refuser is an apply-time gate, so
   the destroy had no subject. A destroy is the one act in this order's bounds that is pre-authorised, which is
   exactly why it needed its precondition checked rather than reached for.

3. **Closed the ledger legs with explicit dispositions after both `hold` forms refused.** `--pre-apply` is
   refused once any leg carries proof ("the act has started"); a normal `hold` is refused while an apply leg is
   open, calling it *"a half-landed deploy ... stays RED"*. Neither is true here. Of the three available
   outcomes — leave it OPEN and blare a half-landed deploy that doesn't exist, close it and have it read as
   deployed, or never prove the plan leg so `--pre-apply` works — I took the close, and made the entry's text
   carry `NOT APPLIED`, the hold's named dependency and its re-read event. "Half-landed" is the costly
   misreading: it sends a responder hunting stranded infrastructure.

4. **Did not run step 5's post-apply plan.** It would have emitted `the_two=2 the_two_changed=2` — the pre-state —
   while carrying `BREAKGLASS-PLAN-AFTER`, the criterion's own expect token. A line that looks like a measurement
   and isn't is worse than no line.

5. **Recorded AC1/AC2 as UNCOMPUTABLE-BY-CONSTRUCTION, not FAIL.** Nothing was measured and found wrong; the act
   never reached them. For AC2 the distinction is security-relevant — a FAIL on an IAM trust criterion would imply
   a role exists with the wrong trust, which is false. Flagged for the CVO that the nearest precedent encoded this
   shape as `N/A-BY-CONSTRUCTION`.

6. **Exercised the CTO's `D2-S92` narrowing instead of accepting it.** The targeted plan returned rc=0 with zero
   AccessDenied where round 61's untargeted plan of the same root returned rc=1 with two. The narrowing is sound,
   measured on the same box and root.

---

## Files Modified

| File | Change |
|------|--------|
| `org/critical_paths/change_management/20261011T0758Z_advi-cotbkf-r62-bj1-...md` | ledger: opened, 4 legs dispositioned, CLOSED, + CLOSE DISPOSITION carrying the hold |
| `org/critical_paths/.open_deploys/advi-cotbkf-r62-bj1-...json` | opened then cleared by the close |
| `.../surprise-channel/investigations/INVESTIGATION_v1.md` | +2 rows: `D2-S98` (BLOCKING), `D2-S99` (OBSERVATION) |
| `.../deliverables/0.7.0_AE_CloudOps~CB2/breakglass_targeted_apply_report.md` | new — the REPORT clause |
| `.../deliverables/0.7.0_AE_CloudOps~CB2/ADVI_COTBKF.TO-CB-bj-1...proof_of_spec.json` | new — VALID rc=0 |
| `org/tier2_senior/0.7.0_AE_CloudOps~CB2/logs/2026-10-11/` | this log |

**AWS: nothing.** No IAM object created, changed or destroyed. `<status>` left at `issued`.

---

## Blockers

**`CB-bj-1` cannot proceed on this seat.** It waits on an LGIC naming-canon resolution for the token `restricted`
so `grade()` returns a verdict instead of raising `R1.f`. Registry owner: the laptop `1.0.0_SA_CTO` (CTO ruling
@`27ba4d3769` item 4); routed via `2.0.0_SA_COO~C2`. Row `D2-S98`. Re-read event: an amendment naming the resolved
policy name and its commit — and a re-run is a **new** ledger entry.

Row `D2-S95` (ARMED: the two objects land as a rider on any untargeted apply) is **not** disarmed — it was to be
disarmed by the issuer on proof 2, which does not exist. It stays armed.

Still with `1.0.0_SA_CTO~DELL2` from earlier rounds: `D2-S91`, and `D2-S92` (now narrowed, and the narrowing
measured sound).

---

## Current State

Three orders terminal this session: `CB-al-2` COMPLETE, `CB-bi-2` STOPPED (AMENDMENT 2 now corrects its criterion
and is the next act), `CB-bj-1` STOPPED here. Nothing applied to AWS by this order.

---

## Next Steps

1. `[0.7.0_AE_CloudOps~CB2]` `TO-CB-bi-2` AMENDMENT 2, which the GO sequences after this order: run the corrected
   invocation on the saved round-61 plan, record it beside the first reading, validate, flip to complete.
2. `[1.0.0_SA_CTO` (laptop)`]` The naming remedy for `restricted` — vocabulary entry, registry row, or a different
   policy name built by `name()`. **Not** the `49f` name the gate prints.
3. `[2.0.0_SA_COO~C2]` `D2-S95` stays ARMED; amend `CB-bj-1` with the resolved name when the canon answers.
4. `[owner of .tools/deploy_ledger.py]` `D2-S99` — a `REFUSED-BEFORE-APPLY` disposition would make a gate-refused
   act terminal, non-RED and distinguishable from a half-landed one.
