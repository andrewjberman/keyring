# The reader-trust value is in git, read from the world and proven equal to it — 0.7.0_AE_CloudOps~TR2

**archetype:** IMPLEMENT

**Date:** 2026-10-11 (UTC)
**Task Order:** NFRA_TRNSPT.TO-APPLY-tv23.readers-auto-tfvars-from-applied-state-dell2
**Status:** COMPLETE

---

## Objective

Retire the workaround my own row `NFRA_TRNSPT-D2-S17` described: put the transcripts root's
reader-trust value in git, **read from applied state**, so no applier ever supplies it from outside the
repo again. The variable keeps no default, so a tree without the file still refuses to plan rather than
planning against a silent fallback. **Nothing is applied — DELTA=0 is the proof**, and the CTO ruled a
verified DELTA=0 needs no never-widen pair.

Third order this lane has executed in the session, and the first that changes nothing in AWS.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-iam | `comp-iam role <both reader roles>`; `comp-iam roles` | **FAIL (silent)** | Preflight RUN. Returned `No role matching` for both roles, which exist and are applied. Cause established, not guessed: `comp-iam roles` emitted 884 TF-derived role lines with no transcripts reader among them, and all four names are `local.*` from `jsondecode(NAMES.json)`. Filed as row `NFRA_TRNSPT-D2-S27`. |
| proof-of-spec-check | `proof-of-spec-check <instance> TR23-tv23-AC1 --governing-order <order>` | PASS (4th pass) | Each refusal was correct and taught something: the DEPLOY/LOCAL conflict, then the BUILD controls shape, then the forbidden root fields. VALID rc=0. |
| comp-find / Grep | `comp-find` for the instance convention; native Grep for the default-assignment census | PASS | |
| comp-schedule | not run | SKIPPED | DECLARED-NOT-APPLICABLE by the order's preflight: nothing applied, no schedule touched. |

**What worked:** `proof-of-spec-check` as an adversary rather than a rubber stamp — it refused four times
and each refusal named a real defect, including one in my own reasoning (claiming a genre the order cannot
confer).
**What failed:** `comp-iam`, silently, on exactly the roles the order asked about. See the row.
**Gap found:** two, both mine and both caught by instruments: my first variable census matched the word
"default" in description prose and so reported a default where none exists; my first channel validator
regex spanned several JSON blocks in a file that has grown past one array. Neither reached a commit.

---

## What was done

| Step | Action | Result |
|------|--------|--------|
| 1 | Live read of the second reader's trust | ONE principal: `arn:aws:iam::313476888478:user/Opal_Terminal` (06:51:07Z) |
| 1 | "Any OTHER defaultless variable?" | **No.** 5 variable blocks in the root, 4 `default =` assignments, exactly one defaultless — this variable. Denominator printed. |
| 2 | `readers.auto.tfvars` written | ARN list **generated** from the `get-role` output by a script, never typed; header records source, read time, the ruling, and that a change needs Andrew's C-READERS word |
| 3 | `.gitignore` negation | ONE line, `!transcripts/readers.auto.tfvars`. `check-ignore` before `:5:*.auto.tfvars`, after `:10:!transcripts/readers.auto.tfvars` |
| 4 | `readers.tf` headers | **Two** false "NOT APPLIED" claims, not one — the second reader's and the silver reader's. Both corrected to measured applied state. Comment lines only; variable block untouched, still no default. |
| 5 | Proof plan, no `-var` | `No changes. Your infrastructure matches the configuration.` over all six reader resources |
| 6 | Negative control | tfvars aside -> rc=1, `Error: No value for required variable` at `readers.tf line 18`; restored, sha256 identical |
| 7 | Commit | `e284d59428` (three files) and `255007fc37` (the silver header the check caught) |
| — | AC1 | `R23-TV23-OK declared=1 live=1 equal; no default; header states the applied state` rc=0 |
| — | **Mutant** | Planted `user/MUTANT_WRONG_PRINCIPAL`: the plan proposed updating `aws_iam_role.second_reader`'s `assume_role_policy`, 1 to change. **FIRED-AS-EXPECTED.** Restored, sha256 identical, no mutant text left. |
| — | Determinism | Two same-input plan runs and two check runs, verdicts compared equal. **STABLE.** |

### Scope controls on the negation (it must not widen)

`transcripts/other.auto.tfvars`, `transcripts/terraform.tfvars`, `inf-pipeline/readers.auto.tfvars` and
`shared-infra/anything.auto.tfvars` are **all still ignored** by the original patterns; only the one named
path is trackable.

### The BLIND item the preflight asked about

**Answered: no other root reads this variable.** `second_reader_trust_principal_arns` appears in exactly
three lines of one file across all of `infra/` — `readers.tf:12` (comment), `:15` (the block), `:35` (its
use in the trust policy).

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| **Generated** the ARN list from the API output instead of transcribing it | The order forbids typing the value. A script that reads `get-role` and writes the file cannot transcribe it wrong; a human copying one ARN can. The check then re-reads live and compares, so git and the world are shown equal twice by different means. |
| Ran a real mutant rather than asserting the plan is a good oracle | "No changes" is worthless unless a wrong value makes it say otherwise. Planting a wrong principal and watching the plan propose an `assume_role_policy` update is what turns the 0-change result from a tautology into evidence. A plan cannot apply, so this cost nothing but a restore-and-hash-check. |
| Wrote the instance as **genre BUILD**, not DEPLOY | The order's header marks `<proof_genre>DEPLOY</proof_genre>` with `<risk>LOCAL</risk>`, and those cannot both hold: the checker admits DEPLOY only at SERVED or WORLD, and then also requires a never-widen pair the CTO says this act does not need. The checker states outright that the graded party cannot confer DEPLOY on itself. BUILD is the only genre I can honestly claim, and it is graded **more** strictly, not less — it demanded the mutant above. The header needs one of two issuer amendments; raised in the report, not worked around silently. |
| Corrected the silver reader's header too, after measuring it | The check caught the second claim. Rather than take the 0-change plan as sufficient proof that the silver reader is applied, I read the role live (`CreateDate` 2026-10-09T14:07:25Z, policy attached) before writing the claim — a header should not assert something I inferred. |
| Filed `D2-S27` for comp-iam but did **not** file a row for the order's genre/risk conflict | The comp-iam blindness is an ownerless instrument gap that grows with every canon-conformant resource. The genre conflict is a one-field defect in the issuer's own artifact, which the issuer may amend without a CTO ruling — telling them directly is faster than a channel row and does not manufacture friction. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `infra/aws/terraform/transcripts/readers.auto.tfvars` | New, tracked, 1 ARN read from applied state | `e284d59428` |
| `infra/aws/terraform/.gitignore` | One negation line + why | `e284d59428` |
| `infra/aws/terraform/transcripts/readers.tf` | Comment headers only, both corrected | `e284d59428`, `255007fc37` |
| `org/missions/.../surprise-channel/investigations/INVESTIGATION_v1.md` | +1 row `NFRA_TRNSPT-D2-S27` (main array 77 rows, 0 duplicate ids, 9 trailing blocks intact) | this commit |
| `org/.../deliverables/...tv23...proof_of_spec.json` | New, VALID rc=0 | this commit |
| this log | New | this commit |

**Nothing in AWS changed.** No apply of any kind was run.

---

## Blockers

None. The order is executed end to end.

---

## Current State

Written for a reader with zero prior context. The transcripts Terraform root's reader-trust value now
lives in git at `infra/aws/terraform/transcripts/readers.auto.tfvars`, tracked by a single `.gitignore`
negation that leaves `*.auto.tfvars` in force everywhere else. It holds one principal,
`arn:aws:iam::313476888478:user/Opal_Terminal`, generated from the live trust policy of
`teams-global-transcripts-second-reader-role` rather than typed. The variable in `readers.tf` still
carries **no default**, proven by moving the file aside and watching terraform refuse with `No value for
required variable`. A plan over all six reader resources with no `-var` reads **`No changes`**, so the
committed value and the applied value are shown equal rather than assumed equal — and a planted wrong
principal makes that same plan propose an `assume_role_policy` update, so the 0-change result is a real
oracle. Both of `readers.tf`'s headers now state measured applied state instead of claiming "NOT APPLIED
-- plan only". `R23-TV23-OK declared=1 live=1 equal; no default; header states the applied state`.
**Nothing was applied.** Row `D2-S17` is retired in substance and `D2-S20` is satisfied for both headers,
though disposing of a row is the CVO's and the issuer's, not mine. `NFRA_TRNSPT.TO-APPLY-mp23` is in this
lane's folder and its GO has arrived (msg 4328); it is the next act.

---

## Next Steps

1. **[`0.7.0_AE_CloudOps~TR2`] Begin `NFRA_TRNSPT.TO-APPLY-mp23`** — its GO has landed. This is the next act
   and it is not blocked.
2. **[`2.0.0_SA_COO~T2`] Amend this order's header, one field** — `<risk>SERVED</risk>` if the DEPLOY proof
   genre is intended, or `<proof_genre>BUILD</proof_genre>` if `<risk>LOCAL</risk>` is. As written the two
   cannot both be satisfied, and the instance is BUILD for that reason.
3. **[`2.0.0_SA_COO~T2`] Flip `<status>` and grade `TR23-tv23-AC1`**; the instance is VALID. Rows `D2-S17`
   and `D2-S20` are satisfied in substance and are yours and the CVO's to dispose.
4. **[`1.0.0_SA_CTO~DELL2`] Row `NFRA_TRNSPT-D2-S27`** — comp-iam cannot see any role whose Terraform name is
   computed, and it says so silently. LGIC rule 30 mandates that form, so the blind set grows. The fix is in
   comp-iam's TF parser or a cross-check against the live IAM census it already has.
