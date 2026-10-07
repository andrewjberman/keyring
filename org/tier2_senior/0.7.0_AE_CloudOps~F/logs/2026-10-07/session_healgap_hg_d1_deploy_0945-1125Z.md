# 0.7.0_AE_CloudOps~F -- MDPF_HEALGAP.TO-HG-d1: the Rebalancer runner's guard reaches the live Lambda

**archetype:** DEPLOY

**Session:** 2026-10-07 ~09:45-11:25Z. **Seated by:** `1.0.0_SA_CTO` msg 106115 on
`CTO_RULINGS_FOR_THE_DELLS_20261007_0930Z.md` section 2. **Issuer:** `2.0.0_SA_COO~G1` (dell1).

## Current State

**The deploy is landed, graded and closed.** `cot-rebalancer-runner` runs the HG-t-1 build: live `CodeSha256
QxLvPLTMO5YSkS+vaRXEkhaA78ZAr1arTyS0ADOOMvk=`, `LastModified 2026-10-07T10:44:25Z`, `State Active`,
`LastUpdateStatus Successful`. The apply was `0 added / 1 changed / 0 destroyed` on one targeted resource, the
targeted re-plan returned `No changes` at `-detailed-exitcode` rc=0, and Deployment Rule 4's parity loop is closed
(the source map's `artifact_sha256` and `last_deployed_commit 8af853ce59` agree with a fresh live read).

`HG1-d1-AC1` DEPLOYED-OK, `HG1-d1-AC2` UNCHANGED-OK, both invoked twice and byte-identical. `proof-of-spec-check.py`
**VALID rc=0** against the governing order, run before the flip. Order flipped `staged -> pending -> complete`. The
NEVER-2 ledger entry opened at deploy START and CLOSED in-session with all five legs proven and the sentinel removed
-- nothing stranded. Tag `opal-assets-v0.51.0` created (previous was `v0.50.0`, read not assumed).

What this does and does not buy: it puts the code that makes a second same-day invocation safe onto the live
function. **FWD-1 is not REALIZED by it** -- the induced morning failure and HG-t-2's re-attempt target are both held
on PRD ACT 1 per the COO half's own "Not signed here".

Everything with its instrument: `org/missions/D8/MDPF/MDPF_HEALGAP/deliverables/0.7.0_AE_CloudOps~F/REPORT_TO_HG_D1_20261007.md`.

### Three things worth keeping from how this went

1. **The carrier was the trunk, and nothing polls git for a seat.** The issuer sits on dell1 and reads NOT REGISTERED
   on the laptop broker, which is localhost-only, so the order could not reach this inbox. The order was found by
   reading `origin/CLOUD` directly after asking `0.0.0_AB_MSTR` to name the carrier; the CTO's relay (msg 106155)
   confirmed the same file independently. A seat seated across devices should read the trunk, not wait on mail.
2. **Both never-widen halves were verified by their own bytes, not from the request.** The COO half asserts the CTO
   half is signed; that assertion was checked by hashing both half files at dell1's reported GO commit `297e25e870`
   and at HEAD -- identical blobs. A citation ages separately from the text it quotes.
3. **The named sha was an unbuilt target.** Before the apply, the live function and the staged S3 artifact were BOTH
   the 2026-09-11 vintage, so `QxLvPLTM...` existed in neither place. `BUILD_ONLY=1` first, then compare, then upload
   -- that ordering is what made CTO half condition 2 ("sha equal before the upload") checkable at all, and this
   box reproducing dell1's sha byte-for-byte is the real evidence the build is deterministic across boxes.

## Blockers

**None. Nothing is owed by this seat on this order.** Four items are owed by others or by tomorrow:

1. **The next 06:00Z stamp read** (`meta/<next date>-complete.json` at ~06:01Z). CTO half condition 3 names it the
   ledger's verify leg while the order's act step 5 directs closing the ledger before the acceptance reads. A
   next-day read cannot gate an entry opened today without it blaring past its window. Flagged, not resolved here.
   **Owner `2.0.0_SA_COO~G1`.**
2. **Three surprise rows owed an id**, full text in `SURPRISE_ROWS_OWED_FROM_TO_HG_D1_20261007.md`. The order reserves
   minting to dell1; the proof gate refuses an id-less row. Rather than drop them or forge an id they are a committed
   file. **Carried by `0.0.0_AB_MSTR`, filed by the issuer.**
3. **The terminal `<status>` beyond `complete`** is the issuer's.
4. **Push:** `8c03191a87` and `5aa57cf269` were LOCAL at send time (origin/CLOUD `f90db47701` by `ls-remote`); the
   earlier three had already been merged to origin. The tag is local. `CLOUD` is `0.0.0_AB_MSTR`'s to push.

## Next Steps

1. **[`2.0.0_SA_COO~G1`]** Read tomorrow's 06:00Z stamp as the ledger's verify leg, and decide whether ACT 1 releases
   HG-t-2 and the FWD-1 exercise.
2. **[`0.0.0_AB_MSTR`]** Carry the three rows to dell1; push the two local commits and the tag on Andrew's word.
3. **[tool owners, from the rows]** The order's `<paths>` grant is narrower than `record-terraform-deploy.sh` which
   the order itself directs; `deploy_ledger.py close` rewrites ten other seats' sentinels; `safe-apply`'s naming limb
   reports a mangled-path fault as an `LGIC_ENFORCE` naming BLOCK.

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `comp-read` | `comp-read infra/aws/terraform/opal-assets/cot_rebalancer_runner.tf --for "..."` | **Worked, and changed the plan.** Found the module at `:133` and the function name at `:33`; this is how the apply directory was established as `opal-assets`, NOT `cot-pipeline` -- which the order implies through its paths but never states. Surfaced 11 qualifiers. |
| `comp-find` | `comp-find NON-APPEND-EDIT --limit 40` | Worked. 193 hits / 224,442 files scanned. Established the startup A.2 audit findings are an OWNED class (owner `0.7.0_AE_CloudOps`, gate CTO) already examined that morning by `0.7.0_AE_CloudOps~E`, so they were not re-filed. **Cost note: ~2 min, twice backgrounded past the 120s timeout.** |
| `comp-which` | startup A.3 exercise | PATH 104 of 104 comp-tools resolve bare; a forwarder RAN. |
| `deploy_ledger.py` | `open` / `close-leg` x5 / `close` | Worked. **Gap found:** `close` rewrote ten OTHER seats' `.open_deploys` sentinels (row 2 of the owed surprises). |
| `record-terraform-deploy.sh` | `... opal-assets --function cot-rebalancer-runner --version opal-assets-v0.51.0 --author ...` | rc=0 after an initial rc=2 **refusal of the bare pipeline call** -- 37 stale `.tfplan` files meant the bare scope would have written 12 function rows, 11 not this act's. The refusal was correct and the `--function` form is both the true scope and the narrower write. |
| `proof-of-spec-check.py` | `... HG1-d1-AC1,HG1-d1-AC2 --governing-order ...` | INVALID twice, then **VALID rc=0**. Its enum errors are precise and worth reading verbatim rather than guessing: `deployed_state`, `kind` and `phase` are closed enums, `controls` admits no extra keys, `cell_refs` belongs on the order's criterion tags and not in the instance, and a repo artifact's `commit_or_etag` must be 7-40 hex. |
| `safe-commit.sh` | 5 commits, exact pathspecs | Worked, but **lost two races to `.git/index.lock`** on a shared index with several live seats; one lock was held 250s by another seat's git process. Retried, never cleared another seat's lock. The tool's own advice -- ask the repository, not its stdout -- was the right check both times. |
| `safe-apply.sh` | `-chdir=infra/aws/terraform/opal-assets apply -target=module.cot_rebalancer_runner` | **Failed closed at rc=7 on the first attempt** because `MSYS_NO_PATHCONV=1` was exported, which CLAUDE.md bans for `safe-apply` by name. My error. Nothing planned, nothing applied. Clean rc=0 unset. |
| `comp-iam` | not re-run | No `iam.tf` change was made, so the trigger does not fire. The order's `<preflight>` records `comp-iam service cot-rebalancer-runner` RUN at L5: new code uses `s3:ListBucket` (GRANTED), drops the `s3:GetObject` call (UNGRANTED). |

**One instrument failure of my own, recorded because it read like a finding:** a content check compared the live
`CodeSha256` against a hash of `/tmp/lambda-artifact-cot-rebalancer-runner.zip` and printed `MISMATCH`. The zip had
been consumed by the real upload, so the comparison was a sha against a traceback -- rule 22a's "a failed retrieval
returns a VALUE", committed by the very rule meant to catch it. Redone soundly against the S3 object version the plan
named (`uNNJvohJ8HVjIlEcIjEmpouzIRxLROD8`): sha256 `QxLvPLTMO5YSkS+vaRXEkhaA78ZAr1arTyS0ADOOMvk=`, 12,290 bytes,
equal to the live `CodeSha256`, with a one-byte-appended negative control that diverged completely. Deployed bytes
equal the build input by CONTENT, not by filename.

-- `0.7.0_AE_CloudOps~F`
