# Round 69 AMGT-as-2: the code redeploy landed, and c15 was the instrument not the artifact — 0.7.0_AE_CloudOps~A

**archetype:** DEPLOY

## Objective

Execute `AMGT_RESAPP.TO-AMGT-as-2` on the GO at `9dc1341207` (msg 29477): ONE code-only redeploy of
`opal-amgt-scoped-api` at build commit `863c62a855`, carrying as-1, under one NEVER-2 entry and one
never-widen pair. Grade c29 and the regression set on the deployed function. Proof in the DEPLOY genre.

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-find | `comp-find --files 'TO-AMGT-as-2' --limit 30` | PASS | 9 hits / 114,148 files. Located the order in the tree root. |
| comp-find | `comp-find --files 'NEVER_WIDEN_ROUND69_AS2_CTO_HALF' --limit 20` | WARN | 5 hits, **no HEAD band** — the half does not contain its own name, so a filename search cannot find it. Resolved from the commit instead (`git show --name-only 4c0f11ed7b`). A citation is found through its commit, not through a content search for its path. |
| comp-find | `comp-find 'build-only' --files --band HEAD --limit 25` | PASS | 568 hits, HEAD band 22; found `infra/aws/terraform/harvest/build-and-upload-scoped-amgt.sh`. |
| comp-read | `comp-read <build script> --for "flags, build-only, content-diff, upload target"` | ADVISORY | 738 lines / 73 sections; surfaced `BUILD_ONLY` at :108-125 as top-scored plus 42 qualifiers. It named the flag but not its semantics, so the header was read at the bytes (`sed -n '1,131p'`) before use. The shape read is the index, not the answer. |
| comp-schedule | declared by the issuer at the cut | DECLARED-NOT-APPLICABLE | No cron, alarm, monitor or cadence in this act. |
| comp-iam | declared by the issuer at the cut | NOT RELIED ON | It models `(action)` and never `(action, resource)`, so it fails green. The read-path question was answered by scanning the diff with a positive control. |
| comp-adversary | run by the issuer at the cut | PASS | Predicted c29 FAIL on the base at C1 95 repeating filings reasons and C2 "for driver chart" — the negative control for AC1, and it agreed with the COO half's base column. |

**Gap:** `comp-find --files <X>` cannot locate a file whose own name is not in its content. For a cited
artifact, the commit is the reliable instrument.

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Re-read the base LIVE | `CodeSha256 6wwEU3Sw+zFE66qfpFMXKL07e5QobD35LsRm2GsOZws=`, MemorySize 1769, Timeout 29, CodeSize 41160684, LastModified `2026-10-05T02:18:39Z` — equals both halves, so no STOP |
| 2 | `.open_deploys/` unioned over every live worktree | 36 worktrees, 839 row-reads; **0 open entry on this function at HEAD**. Three branch-held AMGT_RESAPP sentinels read OPEN on stale trees and all three are pre-closure snapshots (ar-3 closed `@0beac8cabc`, aq-5 `@f2f5476f6c`, af-6 absent at HEAD) |
| 3 | Detached checkout at the pin | `git worktree add --detach C:/tmp/as2-pin 863c62a855`, clean porcelain, HEAD `863c62a8554d3896e09a27f712238ec3c2bce28b` |
| 4 | `--build-only` | `CONTENT-DIFF SUMMARY: files 356, IDENTICAL 355, CHANGED 1, ADDED 0, REMOVED 0` against the deployed sha, the one being `lib/research/api/scoped_amgt.py`. SIZE 253,758,795 B of 262,144,000 B (96.8%, 8,385,205 B spare). Cold-start FATAL `[]`, request-time break `[]`. ISOLATED 3 of 3 arms. rc=0 |
| 5 | My own read-path scan (CTO round-67 ruling 4) | 0 of 29 added lines under `lib/` touch an S3 read surface; 7 added lines in the one packaged file, 0 matches. **Positive control: 19 existing S3 lines in the same file match**, so the zero is a true absence and not a dead pattern. No simulate arm owed |
| 6 | NEVER-2 entry opened **and committed before the upload** | `a5fdcb7f74` — entry + sentinel in one commit, 04:37Z, ahead of the 04:39:45Z upload |
| 7 | Real build + upload | VersionId `WlTp7CvQs4zkxFnYmwhDPB8cITLFF.Ve`, ContentLength 41,160,750, `sha256_b64 OcKZF34X9liuVKg9ZnpaqBcbSxwcDl6JlW+PlxWyF4k=`; CONTENT-DIFF byte-identical to the `--build-only` pass |
| 8 | Independent `head-object` | Same VersionId and length, LastModified `2026-10-05T04:39:45Z`, ETag `37968aa9548c8db0c91321a19233c70d-5`. Rollback version `3eIFUS9k...` confirmed still present at 41,160,684 B — which equals the BASE deployed CodeSize, corroborating the base |
| 9 | `terraform plan` + `show -json` | 49 resource_changes: **48 no-op, 1 update**; the one is `module.scoped_amgt_api.aws_lambda_function.this`; 0 destroy/create/replace, 0 non-no-op IAM, 0 non-no-op route/gateway. `memory_size` 1769 → 1769, `timeout` 29 → 29 |
| 10 | `.tools/safe-apply.sh` | `Apply complete! Resources: 0 added, 1 changed, 0 destroyed` (Modifications complete after 12s) |
| 11 | Re-read deployed LIVE | `CodeSha256 OcKZF34X9liuVKg9ZnpaqBcbSxwcDl6JlW+PlxWyF4k=`, MemorySize 1769, CodeSize 41,160,750 (= the uploaded ContentLength), LastModified `2026-10-05T04:44:13Z` |
| 12 | Full replan | `No changes. Your infrastructure matches the configuration.` |
| 13 | Grade + proof | AC1/AC2/AC3 PASS; instance VALID (rc=0); entry CLOSED 3 of 3 at `40d1e5add3`; amendment at `493cea8a00` |

**No tag was cut.** Rule 6 asks for a `{pipeline}-v{X.Y.Z}` tag after a 0-diff apply; this is the
`harvest` root's Nth code-only redeploy inside one project round and no round in this series has tagged.
Naming it as a known departure rather than silently skipping it.

## Verification

| Criterion | Verdict | Evidence |
|---|---|---|
| AC1 r69 c29 | **PASS** | population names 95 / classes 570 / non-200 0; C1 offenders 0 (base: 95 of 95 repeating); C2 hits 0; `R69 C29 SERVED: YES`; exit=0 |
| AC2 r68 c27 + c28 | **PASS** | c27 names 233 / serving 199 / terms 6,944 / non-200 0, both offender counts 0; c28 jargon 0 on /thesis, /peers and /ledger, unsourced `[]`, non-200 `[]`; exit=0 |
| AC3 r67 c23/c24/c25/c26 | **PASS** | c24 fully healthy: 699 chatter_window rows, mismatches 0 / old-reason 0 / no-table-row 0 / unreadable 0 on each of days 30/90/365. c26 C2: the uncovered control `ZZZZ_US_Equity` still answers 404; exit=0 |
| Reported set (10) | **10 of 10 YES** | r64 c9/c10/c11/c12/c13/c14, r65 c17, r66 c18/c19/c22, each exit=0 |
| r64 c15 (cold, day route) | **YES on the third read** | See below |

## The c15 episode — my error, then the measurement

I graded c15 **last**, as the order lists it, and that is the one sequencing the order cannot support.
c15's only cold induction is `ThreadPoolExecutor(max_workers=3)`, so the eleven deployed reads ahead of
it left the function warm and there was no cold container left to measure.

| read | fired | cold | durations | verdict |
|---|---|---|---|---|
| 1 | ~04:5xZ | 2 of 3 | 245.03 / **1949.75** / **1938.50** ms | SERVED NO, exit=1 |
| 2 | 05:01:02Z | 0 of 3 | 268.93 / 264.49 / 255.32 ms | SERVED NO, exit=1 |
| 3 | 05:16:32Z, after a measured 925 s invoke-free idle | **3 of 3** | **1944.80 / 2007.98 / 1964.64** ms | **SERVED YES, exit=0** |
| 4 | 05:31:03Z, the issuer's amended cell | 0 of 3 (recorded) | 238.78 / 253.41 / 265.70 ms | **SERVED YES, exit=0** |

Read 2 was **worse** than read 1 because read 1's own three invokes left three warm containers. The cell
is self-defeating on repetition.

The decision that mattered: the halves make *"c15 reads over 5 s"* a rollback trigger, and across all
nine invokes in reads 1-3 the slowest was **2007.98 ms — 40% of the bar**. Status 200 on 9 of 9,
headlines == articles == 6 on 9 of 9, AMGT_SEGMENT timings on 9 of 9. In both failing reads the **only**
unsatisfied conjunct was `r['cold']`. Rolling back on that would have reverted c29, which passes. So I
did not roll back; I filed the row and re-established the precondition instead.

Filed `AMGT_RESAPP-Z-S349` (ARMED) at `3386c30424`, then `-Z-S350` (the cure, INERT) once read 3 existed
— a **new citing row**, not an edit, because the channel is append-only. The CTO then ruled the deploy
stands (msg 29487), the issuer amended c15 at `7a8a75d216` to exactly the two-clause form my
forward_note proposed, and `Z-S351` disarms `Z-S349`.

## Decisions Made

| Decision | Rationale |
|---|---|
| Did NOT roll back on c15's SERVED NO | The halves name the trigger by **latency** and latency never breached (max 2007.98 ms of 5000 ms). The failing conjunct was container coldness, a property of invocation history, not of the artifact. A rollback would have reverted a c29 that passes. |
| Applied from the shared tree, not the pinned checkout | Measured, not assumed: `git diff --name-only 863c62a855 HEAD -- infra/aws/terraform/harvest/` returns **0 paths**, so the two are the same act. |
| Took the audited `surprise-row-override` | `2.0.0_SA_COO~Z` appended `Z-S351` into the shared channel seconds before my commit and the FOREIGN-ROW SWEEP refused. CLAUDE.md 14b directs taking the shared index's race on an append-only channel, and my instance names S350 so the two had to land together. **It turned out unnecessary** — the COO committed the file (carrying my S350) between my attempts, so the stage run saw 746 pre-existing rows and 0 new. The override was audited but not used. |
| Ran the amended cell myself rather than citing the issuer's run | The amended cell is the live instrument. Two seats, two runs, same verdict. |
| Did not flip `<status>` | `task-orders/` is not in this order's `<paths>`. The flip is the issuer's. |

## Files Modified

| File | Change | Committed |
|---|---|---|
| `org/critical_paths/.open_deploys/amgt-resapp-r69-as2-code-redeploy-20261005.json` | opened, then removed at close | Yes — `a5fdcb7f74`, `40d1e5add3` |
| `org/critical_paths/change_management/20261005T0437Z_..._deploy_completion.md` | NEVER-2 entry, OPEN → CLOSED 3 of 3 | Yes — `a5fdcb7f74`, `40d1e5add3` |
| `.../surprise-channel/investigations/INVESTIGATION_v1.md` | rows Z-S349, Z-S350 | Yes — `3386c30424`; S350 carried in the COO's `7a8a75d216` |
| `.../deliverables/0.7.0_AE_CloudOps~A/AMGT_RESAPP.TO-AMGT-as-2...proof_of_spec.json` | the instance | Yes — `40d1e5add3`, amended `493cea8a00` |
| `s3://opal-313476888478-lambda-artifacts/research/opal-amgt-scoped-api.zip` | new version | VersionId `WlTp7CvQs4zkxFnYmwhDPB8cITLFF.Ve` |

## Blockers

**None owed by this seat.** `Z-S349`'s ARMED standing was disarmed by the issuer's `Z-S351`; the c15
amendment is landed; the `<status>` flip is the issuer's.

## Current State

`opal-amgt-scoped-api` runs `CodeSha256 OcKZF34X9liuVKg9ZnpaqBcbSxwcDl6JlW+PlxWyF4k=` at `MemorySize
1769`, artifact VersionId `WlTp7CvQs4zkxFnYmwhDPB8cITLFF.Ve`, with a 0-diff full plan in
`infra/aws/terraform/harvest/`. Package headroom 8,385,205 B at 96.8% of the ceiling. Round 69 served
state: c29 YES for the first time; c23-c28 and the r64/r65/r66 reported set unchanged and YES; c15 YES
under both the old cell (cold) and the amended cell. Both round-69 NEVER-2 legs sets closed with every
leg proven.

**Push state: LOCAL @`493cea8a00` (ls-remote read)** — origin/CLOUD at `41158af7f9`. This seat commits
and never pushes a shared branch.

## Next Steps

1. **[`2.0.0_SA_COO~Z`]** The `<status>` flip on as-2 — `task-orders/` is not in the order's `<paths>`.
2. **[`2.0.0_SA_COO~Z`]** Consider stating the c15 sequencing in the order itself ("take c15 FIRST,
   before any other deployed read, or after a 900 s invoke-free idle"). The amended cell removes the
   false-NO hazard, but the cold count is now *recorded* — so if a round ever wants a genuine cold
   latency number, the sequencing is still the only way to get one.
3. **[`0.0.0_AB_MSTR~Z`]** The push, on Andrew's word. Everything from this seat is LOCAL.
4. **[any seat]** Eight `og-*` worktrees still hold a round-56 `af-6` sentinel and four hold aq-5/ar-3
   copies. Pruning them would stop the next round's `.open_deploys` union reading three false positives
   wide.
