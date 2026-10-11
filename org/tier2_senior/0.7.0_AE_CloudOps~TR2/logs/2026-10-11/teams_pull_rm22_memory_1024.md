# The Teams pull has headroom for the first time: memory 128 to 1024, one attribute, no rebuild — 0.7.0_AE_CloudOps~TR2

**archetype:** DEPLOY

**Date:** 2026-10-11 (UTC)
**Task Order:** NFRA_TRNSPT.TO-APPLY-rm22.teams-pull-memory-1024-dell2 (AMENDMENT 1)
**Status:** COMPLETE

---

## Objective

Disarm row `NFRA_TRNSPT-D2-S19`: raise `aws_lambda_function.pull`'s `memory_size` from the undeclared
provider default of 128 MB to 1024 MB — one attribute, a targeted `safe-apply`, **no rebuild** — then one
driven invoke. Done before the Monday 2026-10-12T13:00Z fire, which was the deadline.

Second order this lane has executed in the round; `TO-APPLY-ra22` (the refused-listing fix) closed at
~04:03Z and left the pull at `AI4UQD0ME+…aA/I=`, which is the code this act must **not** touch.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-schedule | `comp-schedule --drift` | PASS | Preflight RUN. 1 armed gate as an exception (`G-3`, CTO-owned, unrelated); nothing armed on this lane or root. C2 also confirmed this lane's `ra22` entry is gone from the authoritative tree. |
| comp-adversary | `comp-adversary compose <packet> --digest-budget 4` | PASS | Preflight RUN. 2/2 cited paths stable. The complement is the root's 6 uncited sibling `.tf` files — `mail_pull.tf`, `commentary.tf`, `readers.tf` among them, exactly the resources that must not move. Nothing contradicted the packet. |
| commit-gate.sh | `bash .tools/commit-gate.sh infra/aws/terraform/transcripts/pull.tf` | PASS | rc=0, step 0a's required gate on the edit. |
| proof-of-spec-check | `proof-of-spec-check <instance> TR22-rm22-AC1 --governing-order <order>` | PASS | **VALID rc=0 on the first pass**; 5 of 5 controls discriminate, rollback named. |
| comp-iam | not run | SKIPPED | DECLARED-NOT-APPLICABLE by the order's preflight: a memory setting, no role, policy or grant in the target. |

**What worked:** `--digest-budget 4` kept `comp-adversary` to the signal without 20 KB of digests — the
complement I needed was the sibling `.tf` list, not their contents.
**What failed:** nothing. One rail denial (R6/F4, piping a census into `tail`), correct, re-run as given.
**Gap found:** none.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| — | Both halves read at their pins | CTO half `@16fa3b73b8` (SIGNED, section 3) and packet `@f6f35a8841`. The CTO half's three cited Terraform lines **printed at HEAD before trusting them**: `pull.tf` carried no `memory_size` at all, `mail_pull.tf:104` reads 1024, `commentary.tf:280` reads 512. |
| — | Order flipped `staged` → `pending` | Per the GO (msg 4102) and `org/XXX.md` |
| 0 | Open deploy ledgers read per NEVER-2 | 24 live worktrees, per-tree denominators printed (shared 19, max 29), union 84 distinct names. The only live NFRA_TRNSPT entry in the authoritative tree, `nfra-trnspt-a18-second-reader-laptop-20261009`, targets IAM/KMS — not `aws_lambda_function.pull`. No collision. |
| 0 | Ledger OPENED | `20261011T0457Z_nfra-trnspt-tr-rm22-teams-pull-memory-1024-dell2-20261011_deploy_completion.md`, 3 legs |
| 0a | The three-line edit, `commit-gate`, commit, diff printed | commit `7bca11ddee`; `git diff --numstat HEAD~1` on the path reads **`3 0`** — three insertions, zero deletions, one file; the diff is the packet's byte for byte. Condition 4 satisfied (committed **before** the plan). |
| — | Pre-act dry run of the criterion | `R22-RM22-FAIL the pull's MemorySize is not 1024; memory=128` rc=1 — FAIL as the order predicts |
| 1 | Precondition, live reads (05:01:08Z) | pull MemorySize **128**, CodeSha256 `AI4UQD0ME+…aA/I=`, Timeout 300; mail pull `VGIq85Xx…uMNY=` (already 1024); commentary `ResourceNotFound`. **And the local zip hashed to `AI4UQD0ME+…aA/I=` (886783 B) — EQUAL to the live CodeSha256.** |
| 2 | `terraform plan -target=aws_lambda_function.pull` | ONE resource block, **ONE attribute**: `~ memory_size = 128 -> 1024`. 28 unchanged attributes, 4 unchanged blocks. **No `source_code_hash` diff, no reader resource.** `Plan: 0 to add, 1 to change, 0 to destroy`. Condition 1 satisfied. |
| 2 | `safe-apply … apply -target=… -auto-approve` | rc=0, `Apply complete! Resources: 0 added, 1 changed, 0 destroyed`; modifications complete after 6s at 05:03:47Z |
| 3 | After, live reads (05:04:23Z) | **MemorySize 1024**; pull CodeSha256 **UNCHANGED**; Timeout still 300; State Active, LastUpdateStatus Successful; mail pull unmoved (LastModified still 2026-10-07T23:59:05Z); commentary still absent. Condition 2 satisfied. |
| 3 | Targeted 0-diff re-plan | `No changes. Your infrastructure matches the configuration.` |
| 4 | ONE invoke, empty event (05:05:57Z → 05:06:26Z) | StatusCode 200, FunctionError null, no `errorMessage`. 4 series. **REPORT: Memory Size 1024 MB, Max Memory Used 101 MB**, Duration 23835.67 ms. |
| 5 | Ledger CLOSED | All 3 legs proven; sentinel removed |
| — | Criterion check, post-act | `R22-RM22-OK memory=1024 pull=AI4UQD0M mail=VGIq85Xx commentary=ABSENT` rc=0 |

---

## Verification

### The invoke's per-series counts (counts and statuses only — the bounds bar ids)

| series | listed | held | landed | expired | read_refused | refused | packet expected | verdict |
|---|---|---|---|---|---|---|---|---|
| `monday_meeting` | 20 | 16 | 0 | 0 | **4** | 0 | 16 held, 4 rr | MATCH |
| `ocio_ic` | 8 | **8** | 0 | 0 | 0 | 0 | 8 held, 0 landed | MATCH |
| `asset_management_ic` | 7 | 7 | 0 | 0 | 0 | 0 | 7 held | MATCH |
| `research_meeting` | 0 | 0 | 0 | 0 | 0 | **1** | refused 1 | MATCH |

`totals`: listed 35, **new 0**, held 31, expired 0, refused 1. `ocio_ic` is now 8 held because its one new
row landed on the 03:40Z run of the previous order — the packet predicted exactly that, which is a small
but real check that the packet's author and the world agree.

| object | head-object |
|---|---|
| `…/state/pull_runs/run=2026-10-11T05:06:03Z/run.json` | 4064 bytes, 05:06:27Z, `aws:kms` |
| `…/state/listing_snapshots/run=2026-10-11T05:06:03Z/listing.json` | 3255 bytes, same timestamp, `aws:kms` |

### What this invoke proves, and what it does not (condition 5, in words)

**It proves the setting is live and a full run still completes at it.** The REPORT line states
`Memory Size: 1024 MB` independently of the config read.

**It does not prove the peak.** The run read **no transcript content** — `new=0`, and the four
`monday_meeting` content reads were refused and return no body — so `Max Memory Used: 101 MB` is the
idle-path cost against the packet's ~99 MB baseline. The content-reading peak is still **unmeasured**:
every prior reading of it was pinned at the old 128 MB ceiling, which is why the row was armed at all.
**The 768 MB threshold is therefore untested.** 101 MB sits below it, but 101 MB is not a content-reading
peak and is not evidence about that branch. The first measured peak is owed from the first fire that
**lands** a transcript, read from its REPORT line beside its `run.json` — the next scheduled fire is
Monday 2026-10-12T13:00Z. A peak above 768 MB is a row, not a second raise.

### Why "no rebuild" is mechanical here, not a promise

The root computes `source_code_hash = filebase64sha256(local.pull_zip)`. At step 1 the local zip hashed to
`AI4UQD0ME+…aA/I=` — **equal to the live `CodeSha256`** — so no code change *could* ride the apply, and
indeed the plan carried no `source_code_hash` diff. `build.sh` was never run. That ordering matters: the
binding was established *before* the plan, so the plan's silence on the code hash is corroboration rather
than the sole control.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Printed the CTO half's three cited Terraform lines before relying on them | A citation ages separately from the text it quotes. The half's whole "why 1024" rests on `mail_pull.tf:104`; reading the bytes costs one call and turns an inherited claim into a measured one. |
| **Generated** the reader-trust tfvars by piping `get-role`'s output to the file, rather than reusing the file I wrote for `ra22` | Condition 3 says read from applied state. Reusing an hour-old file would have been a typed value with extra steps; generating it means the value cannot drift from the world even if someone had changed the trust between the two orders. |
| Kept the tfvars outside the repo again | No committed artifact should assert a routing decision that is Andrew's. Same reasoning as `ra22`; row `NFRA_TRNSPT-D2-S17` still carries the durable fix. |
| Did not file a row for the stale `ra22` sentinels | `C:/dev/anl-r1g-pin` and `C:/dev/wk-irpt-dashbd-89` carry this lane's CLOSED `ra22` sentinel as OPEN because their HEADs predate its close. The artifact is world-done and the authoritative tree is correct; this is the Z-S308 class, which `comp-schedule` already drops, and those paths are not this lane's write surface. Declared as an exclusion in the instance instead of minting a row for a known class. |
| Stated the 768 MB threshold as **untested** rather than passed | 101 MB is below 768, so a careless reading would call the threshold clear. It is not: the run never exercised the content path. Reporting it as passed would be the exact "a clean invoke read as proof of the peak" hazard the preflight names. |
| No tag, no core-document edit | Same as `ra22`: this root carries one tag across all its applies, and a memory integer is not a structural change to `pipeline_inventory.xml`. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `infra/aws/terraform/transcripts/pull.tf` | +3 lines: the `memory_size = 1024` declaration and its two comment lines | Yes — `7bca11ddee` |
| `org/.../task_orders/NFRA_TRNSPT.TO-APPLY-rm22....md` | `<status>` staged → pending | This commit |
| `org/critical_paths/change_management/20261011T0457Z_...rm22..._deploy_completion.md` | Opened, 3 legs closed, entry CLOSED | Opened at `9e9e6e62f3`; closes ride this commit |
| `org/critical_paths/.open_deploys/nfra-trnspt-tr-rm22-...json` | Sentinel created then REMOVED by the close | This commit |
| `org/.../deliverables/NFRA_TRNSPT.TO-APPLY-rm22....proof_of_spec.json` | New, VALID rc=0 | This commit |
| this log | New | This commit |

No `.py` touched. The only world change is one integer on one function.

---

## Blockers

None. The order is executed end to end and the ledger is closed.

One item is **owed by this lane's successor or by whoever reads Monday's fire**, and it is not a blocker
today: the first content-reading peak. See "What this invoke proves" above.

---

## Current State

Written for a reader with zero prior context. **`teams-global-transcripts-pull-lambda` now runs at 1024 MB
with its code untouched.** Live reads at 05:04:23Z: `MemorySize` 1024, `CodeSha256`
`AI4UQD0ME+ABza1X0BrBjGjpqjN7f2fc0Cdxb88aA/I=` — the same value as before the act — `Timeout` 300, State
Active. The targeted plan changed exactly one resource and on it exactly one attribute, so nothing else in
`infra/aws/terraform/transcripts` moved: the mail pull is still on `VGIq85Xx…uMNY=` with its 2026-10-07
timestamp, the commentary function is still `ResourceNotFound`, no reader resource appeared, and the
targeted 0-diff re-plan reads clean. The driven invoke returned 200 with no `errorMessage`, four series
matching the packet on every cell (35 listed, 0 new, 31 held, 1 refused), and wrote both a run record
(4064 B) and a listing snapshot (3255 B). Its REPORT line reads `Memory Size: 1024 MB, Max Memory Used:
101 MB` — **the setting is proven live; the peak is not, because the run landed nothing and so never read
transcript content.** `R22-RM22-OK` rc=0 where the same check printed `R22-RM22-FAIL memory=128` before the
act. The ledger
`org/critical_paths/change_management/20261011T0457Z_nfra-trnspt-tr-rm22-teams-pull-memory-1024-dell2-20261011_deploy_completion.md`
is **CLOSED**, three legs proven, sentinel removed. Row `NFRA_TRNSPT-D2-S19` is disarmed by the act; the
issuer owns the row's disarm record. **Monday 2026-10-12T13:00Z** is the first unattended run at the new
size and the first chance to read a true content-reading peak.

---

## Next Steps

1. **[`2.0.0_SA_COO~T2`] Flip this order's `<status>` to complete, grade `TR22-rm22-AC1`, and record the
   disarm of row `NFRA_TRNSPT-D2-S19`** — the proof instance is written and VALID. The flip, the grade and
   the row's disarm are the issuer's, not the applier's.
2. **[`2.0.0_SA_COO~T2`, after Monday 2026-10-12T13:00Z] Read the first content-reading peak** from that
   fire's REPORT line beside its `run.json`. Under 768 MB closes the question; above 768 MB is a surprise
   row, not a second raise. This lane measured only the idle path.
3. **[`2.0.0_SA_COO~T2` / `1.0.0_SA_CTO~DELL2`] Row `NFRA_TRNSPT-D2-S17` is still open** — the defaultless
   `second_reader_trust_principal_arns`. Two applies in a row have now worked around it by reading applied
   state. A committed tfvars or a default would retire the workaround.
4. **[`0.7.0_AE_CloudOps~TR2`] Nothing.** This lane holds no further order and is IDLE.
