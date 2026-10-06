# Round 72 AMGT-av-8: three legs where the ORDER was the hard requirement, and a wrong-grain check that said "already granted" -- 0.7.0_AE_CloudOps~A

**archetype:** DEPLOY

## Objective

Execute `AMGT_RESAPP.TO-AMGT-av-8` on the GO at `3d38d16799` (msg 29815). Three legs, in order, under ONE
NEVER-2 entry: (1) GRANT -- restore `"filings/v1/"` to `local.scoped_amgt_pool_prefixes` and add
`dynamodb:BatchGetItem` to the etf-classifications statement, then one targeted `safe-apply`, then
`r72_grant_av8.sh` must read YES; (2) CODE -- one artifact at `7889ef1ae4` carrying av-1..av-7, one code-only
`safe-apply`, then `leadpanel_cold_warm.py --label after` at once; (3) DRAFTING SPLICE -- the narrow
`.evidence_records` splice on two keys. `memory_size` stays 1769. Seven CTO conditions.

AMENDMENT 1 removed the pool universe write; AMENDMENT 2 narrowed the drafting leg from a rebuild to a splice.

## Compiler Tools

| Tool | Invocation | Result |
|---|---|---|
| `r72_grant_av8.sh` | before the grant, then after | **The act's main instrument.** BEFORE: 3 controls allowed, C1/C2/C3 `implicitDeny`, `GRANT: NO`, exit=1. AFTER: same 3 controls still allowed, C1/C2/C3 `allowed`, `GRANT: YES`, exit=0. I took the BEFORE arm myself rather than inheriting the CTO half's, so the pair is mine end to end. |
| `terraform show -json` | on both saved plans | PASS. Grant plan: 4 rows, 3 no-op + 1 in-place update of `aws_iam_role_policy.scoped_amgt_api_grants`, 0 deletes, statement count 6 before and 6 after. Code plan: 49 rows, 48 no-op + 1 update, destroy/route/gateway/IAM all 0. |
| `build-and-upload-scoped-amgt.sh` | `--build-only`, then the real run | PASS. Diff identical on both passes; size `253,961,459 B` equals the COO half's independent figure **to the byte**. |
| `content_diff.py` (inside the build) | against deployed `wbIT0PHv` | 365 files, IDENTICAL 361, CHANGED 3, ADDED 1, REMOVED 0. **Read at the four lines, not from the summary and not from rc** -- the script's own comment says the diff is a report that exits 0 either way. |
| `drafting_evidence_splice.py` | `--dry-run`, then `--write --pre-act-dir` | PASS. Dry-run `SPLICE: YES` matched the half before any write. The write's own `OK` was NOT the verdict; see Verification. |
| `deploy_ledger.py` | `open` / `close-leg` x7 / `close` | PASS. One entry, 7 legs (one per act plus the gating read), committed `@e4f10c2259` **before the first apply**. |
| `proof-of-spec-check.py` | pre-commit, then on committed bytes | **VALID (rc=0)**, 12 of 12 controls discriminate, rollback named. Two first-pass violations, both artifact-coverage: an exclusion naming a pre-act DIRECTORY does not cover the FILES in it; the checker tokenizes per file. |
| comp-tool rail | denied a plain `grep` on the `.tf` | Worth logging as a mechanism, not a complaint: **the denial aborted the whole Bash call, so the heredoc writing my edit script in that same call never ran**, and the next python invocation failed on a missing file. Rule 21 says exactly this ("put a gated read in its own call"). Verification then used `git diff`, which answers "what moved" better than a grep would. |

## Deployment Sequence

| # | Step | Evidence |
|---|---|---|
| 1 | Base re-read **live** | `wbIT0PHv...`, 1769, `19:14:52Z` -- equals both halves. No STOP. |
| 2 | Condition 6 union | 41 worktrees, **41/41 resolved, 0 unresolved**, per-tree denominator 5-29. Parsed with `sed -n 's/^worktree //p'`, never a positional field. |
| 3 | The one open entry, re-verified | `amgt-corpus-r36-al5` still OPEN, 0/4 legs proven, window expired **20.7h** ago. Ruled non-blocking by the issuer in round 71 (msg 29756); re-read rather than carried on trust. No new ruling sought. |
| 4 | BEFORE state of both write keys | BA `.zSrn...` 105,318 B; ASML `kQZe...` 13,039 B. Both match the halves' declared base. |
| 5 | NEVER-2 opened + committed | `@e4f10c2259`, 7 legs, before any apply |
| 6 | Grant edits + commit | `@7e4fc71394`, committed **before** the apply so the desired state could not outlive a crash unrecorded |
| 7 | Targeted grant apply | `0 added, 1 changed, 0 destroyed` |
| 8 | **Gate: `GRANT: YES`** | condition 1 cleared; only then was the code leg started |
| 9 | Detached checkout + `--build-only` | `7889ef1ae438dda0...`, porcelain 0; diff exactly the halves' list |
| 10 | Real build + upload | VersionId `G8NmPF6to8CB.Q7QKTkQFFMdiV_PLg3e`, sha `2lUlZomo...`, 41,226,617 B; diff reproduced |
| 11 | Code apply (saved plan) + leadpanel | Applied in the SAME call as the measurement to keep the cold window tight; measurement 10 s after the apply |
| 12 | Live verify + 0-diff | `2lUlZomo...`, 1769; re-plan `No changes` |
| 13 | Splice dry-run, then write | BA -> `0vKJaKGBgj...`, ASML -> `FWeloN5...` |
| 14 | AC1, AC2, AC3, AC4 | all PASS |

## Verification

**AC1** c39/c41/c43/c44/c45 all YES. **AC2** c42 YES, 6 of 6, run after the splice as its own wording requires.
**AC3** r71 c34/c36/c38 and r70 c30-c33 all YES, no regression, c38 worst read 340 ms against a 2000 ms bar.
**AC4** `GRANT: YES`. Every criterion run literally and **unpiped**, so `$?` is the criterion's own.

**Attribution is measured, not argued.** The base arm was taken *between* the legs -- grant landed, code
absent -- which the issuer's own preflight arm cannot provide. All five AC1 cells read NO there, at counts
equal to the COO half's before-table (137 / 2,389 / 0 / 94 / 680). Post-code: 0 / 0 / **12 rows** / 0 / 0.
So the grant alone moved none of the five, and `c43` needed **both** legs. That is CTO condition 1's ordering
turned from an argument into a measurement.

**The splice, verified rather than trusted.** The script prints its own `OK`; condition 4 asks for byte
equality. The step that makes the rest rigorous: the stored format **round-trips the PRE bytes exactly and
the POST bytes exactly** on both keys, so value equality *is* byte equality. On that footing: top-level key
sets identical (BA 15, ASML 16); 0 fields outside the two spliced paths moved; 0 `denominators` sub-keys
other than `evidence_records` moved; `evidence_records` gained exactly `P0276/P0277/P0278` and `P0086`, 0
removed, 0 pre-existing records modified.

**The two harms were tested for by name.** A small diff does not prove the wider rebuild did not run.
AMENDMENT 2 says a full `--rebuild-pool` deletes ASML's `thesis_driver_provenance` and adds
`anchored`/`text_original` to every BA sentence. Measured: `thesis_driver_provenance` present pre **and**
post; BA `"anchored"` 0 -> 0 and `"text_original"` 0 -> 0.

## A wrong-grain check that failed in the comfortable direction

A first check asked *does the policy document contain the string `BatchGetItem`* and answered **TRUE for the
BEFORE state** -- contradicting the CTO half, which had read etf-classifications as GetItem only.

The half was right and the check was wrong. Re-asked per statement at `(action, resource)` grain: the
pre-existing `BatchGetItem` is `Sid ReadRankedAxesAndPoints` on `table/opal-harvest-security-metrics`, a
**different table**. On `table/etf-classifications` it is NOT granted before and GRANTED after.

This is the `(action)` vs `(action, resource)` defect cloud-ops documents for `comp-iam` -- "a role holding
`s3:GetObject` on ANY bucket reports GRANTED for a call to EVERY other" -- reproduced in a hand-rolled check.
The lesson is that the defect lives in the **question**, not in any one tool, and it fails toward
"already granted, nothing to do", which is the direction that stops you doing the work.

Both stale `.tf` comments were rewritten rather than left to be trusted (condition 2 named only one of them):
the `:343-349` note claiming "NOT BatchGetItem", and the rk-91 note at `:123` claiming no reader remained
under `filings/v1/`. The file now records the **rule** rather than the fact: a prefix lives there exactly as
long as a reader does.

## An expectation that was not met

The COO half expected the cold Lead Panel read **lower**. It is not distinguishably lower: 6998-8638 ms
against round 71's 7306-7777 -- the min fell, the max **rose**, so the band widened rather than moved, and it
sits inside the half's own stated before-band. On two runs of n 6 that is no change either way, and I claim
none.

Filed as surprise row **`AMGT_RESAPP-Z-S355`** rather than smoothed over, with the probable reason the two do
not meet: the half states its expectation in **call counts** (60/72 from 153/167) and
`leadpanel_cold_warm.py` measures **wall time**. A real call reduction need not show in wall time if the
removed calls were not on the critical path. So the row is not evidence the reduction failed -- it is
evidence this instrument cannot see it, and that distinction is the whole content of the row.

The warm column is unambiguous and is where round 71's `served_cache` work shows: warm chatter 532-682 ms,
warm price 61-297 ms, all 9 routes 200.

**RESOLVED by issuer ruling msg 29828, after this log's first draft.** The call-count plane was already
measured and I did not have it: `c46` local reads **60/72, from 153/167**. So the call reduction is REAL, my
wall-time read is the outcome plane, and **both stand**. The conclusion is therefore not "the row is open"
but a finding: **the first-request call count was not the dominant cold cost**, which carries to round 73.
Per CTO ruling 2, provisioned concurrency goes on Andrew's list because the cold read stays above about 2 s.
Nothing is owed by this seat on `Z-S355`, so no resolving row was filed -- recording it here instead, which
is where it costs nothing.

Worth keeping as a method note: the row was right to say "this instrument cannot see it" rather than "the
reduction failed". Had it asserted the latter, the ruling would have been a correction instead of a join,
and a true measurement on one plane would have been written into the channel as a failure on another.

## Decisions Made

| Decision | Why |
|---|---|
| Treat msg 29814 (CTO half SIGNED) as **not** a GO | A half-signature is not authorization. The authorizing facts are the issuer's GO (msg 29815) and the order's own last `<status>` tag reading `go`. Both were checked before the first act. |
| Commit the `.tf` **before** the grant apply | If the apply landed and the session died, an uncommitted edit would leave the world holding a grant git cannot see. The reverse risk (committed, unapplied) is visible and is exactly what the open NEVER-2 entry records. |
| Take the base arm **between** the legs | A base arm before both legs cannot say which leg moved a cell, and this act's central condition is a claim about precisely that. |
| Run the splice dry-run early, before the code leg | Read-only, and it operates on S3 objects the code leg does not touch, so it was free early warning on the leg furthest away. |
| Issue the code apply and the leadpanel measurement in ONE call | The cold column is perishable. Two cold-dependent reads could not both be protected in round 71; here the apply and the measurement were put in the same call, 10 s apart. |
| Re-verify al-5 instead of citing the round-71 ruling | A ruling is about a state, and states change. Re-read: unchanged, now 20.7h dead. **No new ruling sought** -- the issuer decided this exact entry and re-asking would manufacture friction. |
| Report the cold number as a non-result | The half expected lower. Reporting "all 9 routes faster" would have been true of the warm column and misleading about the one the half asked after. |
| Name the two pre-act FILES in the exclusion, not the directory | The checker tokenizes per file; a directory-level exclusion left both files uncovered. Its refusal was correct and specific. |

## Files Modified

| Path | Commit |
|---|---|
| `scoped-amgt-api.tf` (2 substantive lines + both comments) | `7e4fc71394` |
| `.open_deploys/amgt-resapp-r72-av8.json` | opened `e4f10c2259`, removed at close `a329b1eb00` |
| `change_management/20261005T2316Z_..._deploy_completion.md` | `e4f10c2259` -> CLOSED 7/7 `a329b1eb00` |
| `deliverables/0.7.0_AE_CloudOps~A/...av-8...proof_of_spec.json` | `a329b1eb00`, VALID on committed bytes |
| `deliverables/0.7.0_AE_CloudOps~A/LEADPANEL_AFTER_av8.txt` | `a329b1eb00` |
| `deliverables/0.7.0_AE_CloudOps~A/av8-pre-act/{BA,ASML}...json` | `a329b1eb00` -- committed because they ARE the splice rollback |
| `surprise-channel/investigations/INVESTIGATION_v1.md` | `a329b1eb00`, row `Z-S355`; appended in the SHARED tree per 14b's inversion; re-parsed to 773 rows, 0 duplicate ids |

No pool universe write, no `--rebuild-pool`, no memory change, no IAM beyond leg 1, no S3 delete, no vendor
call, no shared-branch push, no portal promote. `ad2-pre-bytes/` was untracked in my deliverables dir from an
earlier act and was deliberately **not** committed.

## Blockers

**None.** Nothing is owed by this seat on av-8.

## Current State

`opal-amgt-scoped-api` runs `2lUlZomoyb2ttLBaQTg6l3ysfw2aEjZGD7mInm8J/WQ=` at memory 1769, carrying
av-1..av-7, with the `filings/v1/` read and `dynamodb:BatchGetItem` granted on the live role. Both drafting
keys carry the spliced evidence. All four criteria pass; the NEVER-2 entry is CLOSED 7/7 with every leg's
readback; all three rollbacks are named and intact.

**Push state: LOCAL @27b7916ac5** (shared-tree HEAD, which has advanced past my `a329b1eb00` with peers'
commits); `origin/CLOUD` reads `01a47ac2e7` (`git ls-remote`). Pushing `CLOUD` is `0.0.0_AB_MSTR`'s on
Andrew's word.

## Next Steps

1. ~~Row `Z-S355`: re-measure on the call-count plane?~~ **RULED, msg 29828: no re-measure owed.** Both
   planes stand -- `c46` local 60/72 from 153/167 on the call-count plane, 6,998-8,638 ms with no
   distinguishable change on the outcome plane. The finding that carries forward is that the first-request
   call count was NOT the dominant cold cost. Nothing owed by this seat. `2.0.0_SA_COO~Z` closes av-8 after
   its own real run.
2. **[`2.0.0_SA_COO~Z`]** The pool universe write returns in round 73 with a rule that keeps the prior
   `form_expected` when the input does not measure it. Row `Z-W243-S1` was **disarmed**, not resolved.
3. **[`2.0.0_SA_COO~X`]** Close `amgt-corpus-r36-al5` SUPERSEDED. Now measured dead across two rounds.
4. **[Andrew's list, per CTO ruling 2 as relayed in msg 29828]** PROVISIONED CONCURRENCY, because the cold
   read stays above about 2 s. This is the ~7-8.6 s cold start, the remaining Lead Panel slowness, and no
   redeploy of this shape reaches it -- a per-container memo is empty on a cold container. It is now an
   owned item rather than an open question.
5. **[`0.7.0_AE_CloudOps`]** The restored `filings/v1/` grant is load-bearing only while av-4's
   `read_segment_breakdown` exists. The rewritten comment states that, so a future least-privilege pass
   removes it for the right reason.
