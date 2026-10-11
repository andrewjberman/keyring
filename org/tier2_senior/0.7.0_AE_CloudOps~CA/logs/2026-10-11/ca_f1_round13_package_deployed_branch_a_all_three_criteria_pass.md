# The round-13 package is live on both chat-assist Lambdas, Branch A exactly, and the channel failure now names itself — 0.7.0_AE_CloudOps~CA

**archetype:** DEPLOY

**Date:** 2026-10-11
**Task Order:** COMM_ASSIST.TO-CA-f-1 (round 14, cell `CA-f-1`)
**Status:** COMPLETE

---

## Objective

One targeted `safe-apply` of `module.ldo_001` in `infra/aws/terraform/transcripts/`, code only, built from a
detached worktree pinned at `2fd32e12c2`, putting COMM round 13's two merged files onto
`teams-global-chat-assist-handler-lambda` and `-ingress-lambda`. The halves BIND and their Branch A / Branch B
split IS the procedure, so the whole job was: prove the pre-state is the one the halves were signed against,
prove the plan is Branch A before applying it, apply once, then prove the world moved.

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `comp-blast` | `comp-blast 'arn:aws:lambda:us-east-1:313476888478:function:teams-global-chat-assist-ingress-lambda' --direction both` | AE minimum. Served graph vintage 2026-10-11T01:13:48Z, 29820 nodes / 62664 edges. >= 29 downstream (printed LOWER BOUND, extracted edges only), 7 callers: the 1min rule, the ingress SNS topic, four C2Motifs, the scheduled event source. Nothing bore on a code-only hash change. |
| `comp-which` | `comp-which "how do I grep the repo"` | Startup exercise: a forwarder RAN; 102 of 102 comp-tools resolve bare. |
| `comp-find` | `comp-find 'backend "s3"' infra/aws/terraform/transcripts/*.tf` | Reached after two rail denials (F1 directory-scoped `.tf` grep, then F4 a census piped into `head`). Answered by reading the two named files, which the rail leaves FREE. |

**What worked:** `comp-blast` by ARN. The bare function NAME is not a graph node, and the NOT-FOUND printed its
29820-node denominator instead of reading as "nothing breaks" — the denial was more useful than a silent zero
would have been.

**What failed:** nothing in the tools. Two of my own calls were correctly denied by the rail and the REMAINDER
line told me what had not run.

**Gap found:** none.

## Deployment Sequence

| # | act | evidence |
|---|---|---|
| 1 | Pinned detached worktree at `2fd32e12c2` in `/c/tmp/ca-f1-pin`, outside every other worktree | `rev-parse` = `2fd32e12c26450d0dc1c2740cdc1fcccd9cd1b86`, `status --porcelain` 0 lines |
| 2 | NEVER-2 ledger `comm-assist-r14-deploy` OPEN, 4 legs, naming both functions; entry AND sentinel committed BEFORE the act | `1f366e030f` |
| 3 | BEFORE reads | both functions `CodeSha256` `SFSTGBQX3r49t2YXSrN+6t6Ekmz1NrpxkjX09VHLZEM=`, 268046 B, LastModified 23:03:08Z / 23:03:14Z 2026-10-09. Live zip DOWNLOADED; its sha256 base64 equals that CodeSha256. Branch A precondition held; Branch B did not fire |
| 4 | Both packages built in the pinned worktree (the root does not load without both zips) | `teams-chat-assist.zip` 269206 B, `nIQW+3XvvaFNJQfwX5lrI99XSexESb68Pd1uLldlTgI=`, 32 files — the same 32 the CVO half measured. Import test PASSES against `dist/pkg` (see Decisions) |
| 5 | Fresh `TF_DATA_DIR` outside every git tree; `init -input=false` against the declared backend | Backend configured, no migrate or reconfigure prompt. Terraform v1.15.8, aws provider v5.100.0 |
| 6 | Saved, locked, targeted plan, one permitted `-var` read live | `0 to add, 2 to change, 0 to destroy` |
| 7 | ONE `safe-apply` of the saved plan | rc=0, and then verified against live state rather than on rc |
| 8 | AFTER reads + targeted re-plan | both functions `nIQW+3Xv...`, 269206 B, 02:16:55Z / 02:17:01Z; re-plan `-detailed-exitcode` rc=0, "No changes." |
| 9 | Ledger CLOSED, sentinel deleted, committed | `c583d4f9e5` |
| 10 | Proof instance VALID, order `pending` -> `complete` | `93b5ee1e3d` |
| 11 | Pinned worktree removed | `git worktree list` carries 0 references to it |

## Verification

**Branch A was graded on the plan FILE, not on the plan text.** `terraform show -json` on the saved plan: 26
`resource_changes`, 2 non-no-op, both `['update']`; addresses exactly
`module.ldo_001.aws_lambda_function.handler` and `.ingress[0]`; changed known keys exactly
`['last_modified','source_code_hash']`; `after_unknown` exactly `['last_modified']`; after-hash on both equal
to the built zip. The human text hid 27 unchanged attributes per resource behind its summary line, so reading
the branch off it would have been reading the part terraform chose to print.

| criterion | verdict | the number that decides it |
|---|---|---|
| `CAf1-AC1` | **PASS** | 5 of 5 limbs True: one package and not the pre-state; served zip hash == `CodeSha256` at 269206 B; both round-13 files byte-equal `git show 2fd32e12c2`; served code returns exactly the five party keys against a registry carrying a sixth |
| `CAf1-AC2` | **PASS** | 02:21:56Z, 4m55s after the ingress LastModified: `channel_poll=5 failed=5 with_error=5 ingress_step_failed[channels]=5`. Re-read 02:33Z: 16/16/16/16. Base: 60 of 60 failed, 0 with an error, 0 step_failed |
| `CAf1-AC3` | **PASS** | `entries at HEAD 1; CLOSED=yes; sentinel at HEAD=no` |

`proof-of-spec-check`: **VALID (rc=0)**, 0 violations, 3 rows; alignment 3/3 criteria to cell, 1/1 cell_ref to
the decomp, 1/1 declared cell reachable; invocation-alignment 3/3, 0 diverge.

**The mutant was an ARTIFACT SUBSTITUTION, not an edit.** AC1's content limbs were re-run with the pre-state
package standing in for the served one — the zip downloaded before the act, a gitignored local copy of what
AWS was already serving, so nothing live, committed or built was mutated and the stand-in is a real artifact
rather than a synthetic corruption. All four limbs flipped to False (hash `SFSTGBQX...`; `mail_requests.py`
19578 B against the pin's 19824 B; `channel_mentions.py` 10009 B against 11105 B; the probe admitting
`sixthfirm` for six keys) while all four read True on the served package. Every limb discriminates.

**Determinism STABLE.** Each criterion run at least twice, minutes apart; no verdict flipped; AC2's counts GREW
with the 1-minute clock, which is what separates a live window from a frozen one — on a single read those look
identical.

**The escalation was measured beside the criterion so it would not read as collateral.** The COO half predicts
about 60 `ingress_step_failed[channels]` lines an hour and calls them intended. Post-deploy distribution, 39
events of which 19 carry an `event` field: `ingress_poll` 6, `channel_poll` 6, `ingress_step_failed` 6,
`mail_poll` 1 — and `ingress_step_failed` is **channels-only, never mail, chats or eod**. So the registry read
the new `mail_requests.py` performs at import did not break the mail step, which was the one way this act could
have cost something. `ingress_poll` continues (`chats_read` 2, `pages` 1).

## Decisions Made

1. **The COO half's import test needed two cwds before it meant anything.** Run from the pinned worktree root,
   as step 1 directs, it reported success while resolving `tenant` out of the **repo working tree** — the
   worktree root's `data/` is a regular package and beats the built package's namespace portion regardless of
   `sys.path` order. Run from a neutral empty directory, both `handlers` and `tenant` resolve from the package
   and the import succeeds. Branch B is graded on the second reading, which PASSES, so the act proceeded.
   Filed as row `COMM_ASSIST-Z-S9`.
2. **`python -I` is not a valid control here.** My first control changed two variables at once: `-I` implies
   `-s`, dropping user site-packages, so it fails inside `assist.py` at
   `zoneinfo.ZoneInfo("America/New_York")` on a missing `tzdata` wheel. That is a property of the control, not
   of the package — the Lambda runs python3.12 on Linux with a system tz database. Re-run with only the cwd
   changed.
3. **The instance is BUILD genre, not DEPLOY.** `PROOF_OF_SPEC.schema.json` admits genre DEPLOY only for an
   order whose issuer marked it `<proof_genre>DEPLOY</proof_genre>` at the cut, and this order carries no such
   line — I wrote the DEPLOY draft first and the validator refused it on exactly that ground. The BUILD key set
   is closed, so `never_widen_pair`, `risk_class` and `rollback` cannot be carried as their own keys. Rather
   than forge the issuer's marker into an order in my own `<paths>`, I kept the facts in
   `artifacts_produced`, the ledger entry and the commit, declared the exclusion, and raised it to the issuer,
   who is the only seat that can mark the next one.
4. **The pre-state zip is not committed.** The repo's own `.gitignore:95` `*.zip` rule covers it, so the
   measured hash and byte count live in `BEFORE_live_zip_hash.json` and the binary stays on disk. The rollback
   target is also reproducible from git, being NFRA_CTLPLN's build at `bde0c0fc90`.
5. **I did not push.** Both commits reached `origin/box/sitez` through the box's scheduled `box-sync`, which is
   the shared-branch law's carrier.

## Files Modified

- `org/critical_paths/change_management/20261011T0201Z_comm-assist-r14-deploy_deploy_completion.md` — OPEN then CLOSED
- `org/critical_paths/.open_deploys/comm-assist-r14-deploy.json` — created, then deleted at close
- `org/missions/D9/COMM/COMM_ASSIST/task-orders/COMM_ASSIST.TO-CA-f-1.round13-package-deploy.md` — one line, `<status>` `pending` -> `complete`
- `org/missions/D9/COMM/COMM_ASSIST/surprise-channel/investigations/INVESTIGATION_v1.md` — appended `Z-S9` and `Z-S10`; 59 insertions, 0 deletions against HEAD, so still a strict append
- `org/missions/D9/COMM/COMM_ASSIST/deliverables/0.7.0_AE_CloudOps~CA/` — the proof instance, BEFORE/AFTER configs, the zip hash record, the plan, its JSON summary, the re-plan, and the three criterion outputs

No `.tf` and no code file was edited. Nothing was pushed by this seat, no mail was sent, nothing was invoked.

## Blockers

**None.** Neither surprise row blocks anything and neither is ARMED.

## Current State

Both Lambdas serve `nIQW+3XvvaFNJQfwX5lrI99XSexESb68Pd1uLldlTgI=` (269206 B). `firm_domains()` now narrows to
C-MAIL's five party keys; the live set is four and stays four, so **Andrew sees no change today**. Channel
@mentions still do not reach him — this act did not cure that and was never meant to. What changed is that the
failure now names itself: `route=teams status=404 error=None`, every minute, with an
`ingress_step_failed[channels]` line beside it.

The ledger is CLOSED and absent from the open/held sweep (23 of 23 sentinels scanned). Rollback was available
throughout and never triggered.

**Push state:** `c583d4f9e5` and `93b5ee1e3d` are **ON ORIGIN**, `origin/box/sitez` @`ea3d65bf85`, measured by
`git ls-remote` plus `merge-base --is-ancestor` with a positive control.

## Next Steps

1. `[2.0.0_SA_COO~ZZ]` Round-14 close for `CA-f-1`: all three criteria PASS, instance VALID. The real
   five-party mail run stays the issuer's, as in round 12 — an applier sends no test mail, so FWD-4 is
   APPLIED, not EXERCISED.
2. `[2.0.0_SA_COO~ZZ]` Row `COMM_ASSIST-Z-S10` hands D2 its starting datum: the failing call is `GET /teams`
   against `https://mcp.opalinvest.dev` returning 404, with `error=None`, which is the shape of a route that is
   not served rather than a request the route rejected. Which part of the gateway is at fault is
   `NFRA_OPLGTW`'s plane and this seat did not read it.
3. `[2.0.0_SA_COO~ZZ]` Row `COMM_ASSIST-Z-S9`: if a later half carries the same one-line import test, run it
   from a directory holding no `data/`, or pass the cwd explicitly as `d1_live.py` already does.
4. `[2.0.0_SA_COO~ZZ]` Mark a deploy order `<proof_genre>DEPLOY</proof_genre>` at the cut when the next one is
   a deploy, so the instance can carry `never_widen_pair`, `risk_class` and `rollback` as fields.
5. `[housekeeping, unowned]` `/c/tmp/ca-f1-tfdata` holds 686M of provider cache and the saved plan. It is
   outside every git tree. I left it rather than run a recursive delete, which needs Andrew's word; `/cleanup`
   or `/kill storage` owns that class.
