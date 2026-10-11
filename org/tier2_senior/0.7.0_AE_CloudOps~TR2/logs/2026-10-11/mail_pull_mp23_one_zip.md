# Three functions, one digest: the mail pull re-applied onto the root's zip, code only, no rebuild — 0.7.0_AE_CloudOps~TR2

**archetype:** DEPLOY

**Date:** 2026-10-11 (UTC)
**Task Order:** NFRA_TRNSPT.TO-APPLY-mp23.mail-pull-onto-the-root-zip-dell2 (AMENDMENT 1)
**Status:** COMPLETE

---

## Objective

Meet read (1) of ARMED row `NFRA_TRNSPT-D2-S22`: re-apply `aws_lambda_function.mail_pull`
(`outlook-global-transcripts-pull-lambda`) **code only** onto the package the Teams pull already runs, so
all three functions of `infra/aws/terraform/transcripts` read **one** `CodeSha256`. Then one driven
invoke.

**Why it matters:** one `dist/` zip path feeds three functions, and the mail pull had run a different,
older digest since 2026-10-07. Any untargeted apply from any tree would have moved it unannounced.

Fourth order this lane has executed in the session.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| deploy_ledger.py | `open` / `close-leg` x3 / `close` | PASS | Three legs, each closed on its own proof. The NEVER-2 read behind it covered **41** live worktrees, per-tree denominators printed, 96-name union. |
| proof-of-spec-check | `... TR23-mp23-AC1 --governing-order ...` | PASS (1st pass) | VALID rc=0; **6 of 6 controls discriminate**, rollback named. |
| comp-schedule | `comp-schedule --drift` (earlier this session) | PASS | Preflight RUN. Nothing armed on this lane or root; the mail pull's `cron(30 23 * * ? *)` is untouched — only the code behind it moved. |
| comp-iam | not run | SKIPPED | DECLARED-NOT-APPLICABLE by the order's preflight: code only, role and policy outside the target. |

**What worked:** the ledger's leg structure matched the act's real shape (keep / apply / verify), so the
rollback artifact got proven *before* the irreversible step rather than assumed afterwards.
**What failed:** nothing.
**Gap found:** none new. The `comp-iam` blindness filed earlier as `D2-S27` still stands and did not bear
on this act.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| — | Both halves read at their pins | CTO half `@f4ec64d888` (SIGNED, section 3), packet `@b73b89ddbd` |
| — | Status flipped `staged` → `pending` | Per the GO, msg 4328 |
| 0 | NEVER-2 ledger read | 41 worktrees, 96-name union. Only live entry on this root at shared HEAD: `nfra-trnspt-a18-...` (IAM/KMS, held) — **not** this target. `comm-assist-r12-mail-deploy` checked by name because it says "mail": it targets `module.ldo_001` in a different root and is absent at shared HEAD. No collision. |
| 0 | Ledger OPENED | `20261011T0721Z_nfra-trnspt-tr-mp23-...`, 3 legs |
| 1 | Precondition, three live reads (07:22:43Z) | teams `AI4UQD0M…` / 05:03:47Z / 1024 / 300; mail `VGIq85Xx…` / 2026-10-07T23:59:05Z / 1024 / **600**; commentary `AI4UQD0M…` / 05:44:45Z / 512 / 300 — **it now exists**, created by another seat at 05:44Z. Local zip `AI4UQD0M…` (886783 B) **equal to the Teams pull's live digest**. No `build.sh`. |
| — | Pre-act dry run | `R23-MP23-FAIL 2 distinct digests across 3 functions; teams-transcripts=AI4UQD0M outlook-transcripts=VGIq85Xx outlook-commentary=AI4UQD0M` rc=1 — FAIL as the order predicts |
| 2 | Kept the deployed package | Fetched from `get-function`'s code location: 478258 B, `VGIq85Xx…` **equal to the then-live CodeSha256** — so it is the running build, by content. Stored outside the repo. |
| 3 | `terraform plan -target=aws_lambda_function.mail_pull` | ONE resource; only `source_code_hash` `VGIq85Xx…` → `AI4UQD0M…` plus `last_modified`; 27 unchanged attributes, 4 unchanged blocks; no reader resource. `Plan: 0 to add, 1 to change, 0 to destroy`. |
| 3 | `safe-apply … -auto-approve` | rc=0, `Apply complete! Resources: 0 added, 1 changed, 0 destroyed`, modifications complete after 6s at 07:32:06Z |
| 4 | After, three live reads (07:32:59Z) | **1 distinct digest across all three.** Teams `LastModified` **unchanged** 05:03:47Z; commentary **unchanged** 05:44:45Z; mail pull MemorySize 1024, Timeout 600, handler unchanged, Active/Successful |
| 4 | Targeted 0-diff re-plan | `No changes. Your infrastructure matches the configuration.` |
| 5 | ONE invoke (07:35:14Z → 07:35:38Z) | 200, no `FunctionError`, no `errorMessage`, **0 `[ERROR]` lines**, exactly **1** `MAIL-PULL-FIRE` line |
| 6 | Ledger CLOSED | All 3 legs proven; sentinel removed |
| — | AC1 | `R23-MP23-OK one digest across 3 functions; teams-transcripts=AI4UQD0M outlook-transcripts=AI4UQD0M outlook-commentary=AI4UQD0M` rc=0 |

---

## Verification

### The driven invoke, graded field by field against the packet's section 4

```
MAIL-PULL-FIRE run=20261011T073520Z window_days=7 listed=12 admitted=0 landed=0
               skipped_known=0 list_refusals=0 silver_rows=0 held_out=0
REPORT         Duration: 18181.25 ms  Memory Size: 1024 MB  Max Memory Used: 100 MB
```

| graded field | required | observed | verdict |
|---|---|---|---|
| `errorMessage` | absent | absent | MATCH |
| `MAIL-PULL-FIRE` lines | exactly 1 | 1 | MATCH |
| `window_days` | 7 | 7 | MATCH |
| `list_refusals` | 0 | 0 | MATCH |
| `admitted` / `landed` | 0 / 0 | 0 / 0 | MATCH |
| `[ERROR]` lines | 0 | 0 | MATCH |
| `listed` | ~12 as the window slides | 12 | same as the last scheduled run **and** the dual-bundle dry run |

**Branch B was not entered.** Nothing was admitted or landed, so there is nothing to report under
condition 5's landing limb. Run record `…/outlook/transcripts/state/pull_runs/run=20261011T073520Z/run.json`
**exists** (516 B, `aws:kms`), its address taken from the function's own returned `run_record_address`
rather than constructed by me.

### Why "no rebuild" is mechanical here

The tree is **ahead** of the deployed zip — TR-tt-23 changed `teams/pull.py` after that zip was built. A
rebuild would have pushed undeployed code into the mail pull *and* re-split the three digests, defeating
the order's whole purpose. So the local zip's hash was bound to the Teams pull's **live** digest before
the plan (both `AI4UQD0ME+ABza1X0BrBjGjpqjN7f2fc0Cdxb88aA/I=`), and `build.sh` was never invoked.

### The control that still works now that all three share a digest

Once the three functions share a `CodeSha256`, the digest can no longer tell a targeted apply from an
untargeted one. The discriminator is the other two functions' **`LastModified`**, and both are
byte-identical to their precondition values. That is why step 1 recorded timestamps, not just hashes.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Proved the kept rollback package by **content**, not filename | A WORLD act needs a restorable artifact. Fetching from `get-function`'s own code location and finding its sha256 equal to the live digest is what makes it the running build; a file named `rollback.zip` proves nothing. Its 478258 bytes also match the packet's independent measurement. |
| Checked `comm-assist-r12-mail-deploy` by name during step 0 | It was the one entry in a 96-name union whose slug says "mail", and my act moves the mail pull. One read showed it targets `module.ldo_001` in another root and is absent at shared HEAD. Cheap, and the alternative was assuming. |
| Planned with **no** `-var` and no file outside the repo | Condition 3 allows either, but tv23 landed the committed `readers.auto.tfvars` an hour earlier, so the value now comes from git. This is the first act on this root that needed no out-of-repo input at all — which was the point of tv23. |
| Recorded the other two functions' `LastModified` at step 1 | Anticipating that the digest stops discriminating after this act. Without those timestamps I would have had no way to show the apply stayed targeted. |
| Did not claim tonight's 23:30Z fire | It is the packet's organic arm and had not happened. Declared as an exclusion. |
| Did not dispose of row `D2-S22` | The CTO half's section 4 reserves that: that seat re-reads the three digests itself and files the disarm on my report. An applier does not dispose a row. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `org/.../task_orders/...mp23....md` | `<status>` staged → pending | this commit |
| `org/critical_paths/change_management/20261011T0721Z_...mp23..._deploy_completion.md` | Opened, 3 legs closed, CLOSED | opened at `1196f1a526`; closes ride this commit |
| `org/critical_paths/.open_deploys/nfra-trnspt-tr-mp23-...json` | Sentinel created then REMOVED by the close | this commit |
| `org/.../deliverables/...mp23....proof_of_spec.json` | New, VALID rc=0 | this commit |
| this log | New | this commit |

No Terraform source and no `.py` touched. The only world change is one function's code pointer.

---

## Blockers

None. The order is executed end to end and the ledger is closed.

---

## Current State

Written for a reader with zero prior context. **All three functions of
`infra/aws/terraform/transcripts` now read one `CodeSha256`,
`AI4UQD0ME+ABza1X0BrBjGjpqjN7f2fc0Cdxb88aA/I=`** — measured as 1 distinct value over three separate live
reads at 07:32:59Z. `outlook-global-transcripts-pull-lambda` moved from `VGIq85Xx…uMNY=` to that value,
code only: its MemorySize is still 1024, Timeout still 600, handler still `mail_handler.lambda_handler`,
and the plan's only diffs were `source_code_hash` and `last_modified`. The other two functions did **not**
move — `teams-global-transcripts-pull-lambda` is still stamped 2026-10-11T05:03:47Z and
`outlook-global-commentary-draft-lambda` still 05:44:45Z, identical to their pre-act reads — and the
targeted 0-diff re-plan is clean. **No rebuild happened:** the bytes are the pre-existing
`dist/transcripts-pull.zip`, whose hash was bound to the Teams pull's live digest before the plan, and the
tree is deliberately ahead of it. The driven invoke returned 200 with no `errorMessage`, zero `[ERROR]`
lines and exactly one `MAIL-PULL-FIRE` line matching the packet's section 4 on every graded field
(`window_days=7 listed=12 admitted=0 landed=0 list_refusals=0`), and wrote a 516-byte run record. Nothing
was admitted or landed, so Branch B was never entered and the kept `VGIq85Xx…` package — fetched from
`get-function` and hash-proven equal to the bytes that were running — remains unused outside the repo.
`R23-MP23-OK` rc=0 where the same check printed `R23-MP23-FAIL 2 distinct digests` beforehand. Read (1) of
row `NFRA_TRNSPT-D2-S22` is met; the row's disarm is `1.0.0_SA_CTO~DELL2`'s to file. **Tonight's 23:30Z
scheduled fire** is the first unattended run on the new bytes and is deliberately not claimed here.

---

## Next Steps

1. **[`1.0.0_SA_CTO~DELL2`] Re-read the three digests and file row `D2-S22`'s disarm** — your half's
   section 4 reserves that act for you; read (2) you measured met at 05:51Z, and read (1) is now met.
2. **[`2.0.0_SA_COO~T2`] Flip `<status>` and grade `TR23-mp23-AC1`** — the instance is VALID.
3. **[`2.0.0_SA_COO~T2`, after tonight's 23:30Z fire] Read the organic arm** — a `MAIL-PULL-FIRE` line and
   no `[ERROR]` on the new bytes. This lane measured only the driven arm.
4. **[`0.7.0_AE_CloudOps~TR2`] Nothing.** No further order is held; the lane returns to IDLE.
