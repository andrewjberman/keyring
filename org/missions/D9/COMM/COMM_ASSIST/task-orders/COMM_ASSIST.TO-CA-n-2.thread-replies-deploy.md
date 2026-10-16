# TO COMM_ASSIST.TO-CA-n-2 -- round 21 CA-n-2: deploy the poller that reads replies in older threads (one targeted apply of module.ldo_001, code only, pinned build)

<to_id>COMM_ASSIST.TO-CA-n-2</to_id>
<project>COMM_ASSIST</project>
<issued_to>0.7.0_AE_CloudOps~COMM1</issued_to>
<issued_by>2.0.0_SA_COO~CA</issued_by>
<issued_date>2026-10-16</issued_date>
<status>staged</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>21</round>
<workstream>DEPLOY21THREADS</workstream>

**Directive:** D9 | **Fabric:** laptop | **Decomp cell:** `CA-n-2` (`decompositions/COMM_ASSIST_DECOMP.round21.md`) | **outcome_ref:** FWD-3, FWD-13 |
**depends_on:** CA-n-1 (merged `1aa63bde67`); the GO waits on the three halves signed on the pin
**STAGED:** the GO is written here when the CTO and CVO halves are SIGNED on the pin `1aa63bde67`.

---

## WORKER FACE

### GO

(not yet written)

The three halves BIND, and the COO half's Branch A / Branch B, rollback and conditions ARE the procedure. Read all three in full (all
under `org/missions/D9/COMM/COMM_ASSIST/deliverables/`):
- COO `2.0.0_SA_COO~CA/NEVER_WIDEN_HALF_COO_COMM_ASSIST_R21_THREADS_DEPLOY_20261016.md`
- CTO `1.0.0_SA_CTO/NEVER_WIDEN_HALF_CTO_COMM_ASSIST_R21_THREADS_DEPLOY_20261016.md`
- CVO `3.0.0_SA_CVO/NEVER_WIDEN_HALF_CVO_COMM_ASSIST_R21_THREADS_DEPLOY_20261016.md`

### THE CELL

`CA-n-2`. The two Lambdas `teams-global-chat-assist-handler-lambda` and `teams-global-chat-assist-ingress-lambda`, now on
`gSq68yr2uV/DwTwAuhWRGzRJoSTo3fzU4mmeitNCpok=` (the CA-l-4 package, 34 files, built at `863dc0f739`), ingress mark mode `enforce`. The
trunk at the pin carries `channel_mentions.py` reading the replies of a bounded set of channel threads (cell CA-n-1). This cell ships
exactly that: code only (the source hash and last-modified of the handler and `ingress[0]`). No environment value, policy, secret or
Terraform resource moves.

### DO, IN THIS ORDER (the laptop, from the shared trunk at or after this order's GO)

0. DISK FIRST: `df` on `C:` must read at least 5 GB free. Below that, create nothing, stop and report the figure.
1. `git worktree add --detach <scratch> 1aa63bde67` (outside every other worktree). Every build, init, plan, apply and re-plan below
   runs FROM that pinned worktree. Confirm `git -C <scratch> status --porcelain` is empty.
2. Open the ledger `comm-assist-r21-threads-deploy` (`python .tools/deploy_ledger.py open ...` from the shared trunk), naming both
   functions (code only; no image). Commit the entry AND the sentinel BEFORE the act.
3. BEFORE reads, saved in `org/missions/D9/COMM/COMM_ASSIST/deliverables/0.7.0_AE_CloudOps~COMM1/r21/`: both functions'
   `CodeSha256`, `LastModified` and environment KEY NAMES (never values); the live zip with its sha256 and base64 sha256 (the
   rollback copy); the dead-letter queue `teams-global-chat-assist-dlq.fifo` `ApproximateNumberOfMessages` and
   `ApproximateNumberOfMessagesNotVisible` (the issuer last read 0 and 0). If the live hash is not
   `gSq68yr2uV/DwTwAuhWRGzRJoSTo3fzU4mmeitNCpok=` or the mode is not `enforce`, that is Branch B: stop and report.
4. Build in the pinned worktree: `bash infra/aws/lambda/teams-chat-assist/build.sh` (it must print `(34 files)`). Record the built
   zip's base64 sha256. Then run AC1 below: it must read `ok=True` BEFORE any apply.
5. `TF_DATA_DIR` = a NEW scratch directory outside every git tree. `init -input=false` against the declared backend; a migrate or
   reconfigure prompt means STOP. A saved, locked, targeted plan `-target=module.ldo_001`, NO `-var`. The CA-k-2 gate inside
   `safe-apply.sh` must read `LDO001-MODE verdict=OK default=enforce live=enforce`; any other verdict is Branch B.
   - Branch A exactly -> apply that saved plan through `bash .tools/safe-apply.sh`. Branch A is `0 to add, 2 to change, 0 to
     destroy`: the handler and `ingress[0]` only, changed keys within {`source_code_hash`, `last_modified`}, NEVER `environment`,
     the after-hash equal to step 4's.
   - Anything else -> Branch B: apply nothing, close the ledger as not-applied, report.
   - Never between 20:00Z and 21:45Z.
6. AFTER: run AC2, then a targeted re-plan (expect no changes). Save the dead-letter queue counts again: both UNCHANGED. Ten minutes
   on, read log lines only (never message content): the ingress log shows `channel_poll` with `calls` at most 20, `ingress_poll`,
   the mail step `polled`; neither function log shows an error or `AccessDenied`.
7. Rollback on any AFTER failure: the COO half's rollback (the saved live zip over `dist/teams-chat-assist.zip`, then a targeted
   apply from a detached worktree at `863dc0f739`). File an ARMED row naming `2.0.0_SA_COO~CA`, and report.
8. Close the ledger and commit. Remove the pinned worktree. Send no test mail, text nobody and invoke nothing.

### RULES FOR THIS CELL

- One targeted apply, `module.ldo_001` only. Never untargeted, never bare `terraform`, never `aws lambda update-function-code`.
- No `-var`. No edit to any `.tf` or code file. Never push, `git stash`, rebase, `checkout --`, `clean`.
- The secret's value is never read, printed, logged, committed or sent. No non-ASCII. `dist/` is never committed.
- Refuse a criterion you cannot satisfy as written. File a BLOCKING row with the measurement and stop; do not widen.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CAn2-AC1" cell_refs="CA-n-2"><invocation>N2_PIN=1aa63bde67 python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r21/checks/check_n2_equiv.py"</invocation><expect>N2-EQUIV ok=True</expect></criterion>
`CAn2-AC1` -- the issuer's pre-flight check, BEFORE the apply with the pinned worktree built: the same file set as the zip the live
function serves; the files that differ are `channel_mentions.py` and at most the three foreign registry files; the 17 address probes
equal; the N1 arms 8 of 8 on the built package. The issuer read `ok=True differ=4 foreign=3 probes=17 same=17 n1=8 of 8` on its own
pinned build at ~21:3xZ.

<criterion id="CAn2-AC2" cell_refs="CA-n-2"><invocation>N2_PIN=1aa63bde67 N2_MODE=live python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r21/checks/check_n2_equiv.py"</invocation><expect>N2-LIVE ok=True</expect></criterion>
`CAn2-AC2` -- the issuer's live check: both functions on one new package (not `gSq68...`), the served zip hashing to it, the served
`channel_mentions.py` the pin's, both environments `enforce` with the same fifteen key names, the N1 arms 8 of 8 and the 17 probes
on the SERVED zip. It FAILs at the base (measured: the PRE hash, the old `channel_mentions.py`, N1 2 of 8).

<criterion id="CAn2-AC3" cell_refs="CA-n-2"><invocation>bash "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r21/checks/check_n2_ledger.sh"</invocation><expect>RESULT: PASS</expect></criterion>
`CAn2-AC3` -- NEVER-2: the ledger `comm-assist-r21-threads-deploy` is committed CLOSED at HEAD and its sentinel is gone. It FAILs at
the base.
</proof_of_spec>

<expected_criteria>CAn2-AC1,CAn2-AC2,CAn2-AC3</expected_criteria>

Each invocation runs under `timeout 250`, from the shared trunk's root (the checks find the repository from the current directory's
git toplevel). Commit the deploy evidence FIRST, then write the proof instance to
`org/missions/D9/COMM/COMM_ASSIST/deliverables/0.7.0_AE_CloudOps~COMM1/COMM_ASSIST.TO-CA-n-2.thread-replies-deploy.proof_of_spec.json`,
pinning each artifact row to the commit that carried it, validate it with
`python .tools/proof-of-spec-check.py <instance> CAn2-AC1,CAn2-AC2,CAn2-AC3` AFTER your last commit, and flip `<status>` to
`complete` only when all three PASS and the instance is VALID at the final head. Surprise rows are `COMM_ASSIST-C21D-S<k>`, fabric
`laptop`, disarm_owner `2.0.0_SA_COO~CA`, `surfaced_at` = `date -u +%FT%TZ` at filing. Append lines only to the investigation file.

<decomp_ref>
<decomp_doc>org/missions/D9/COMM/COMM_ASSIST/decompositions/COMM_ASSIST_DECOMP.round21.md</decomp_doc>
<owned_cells>CA-n-2</owned_cells>
</decomp_ref>

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/comm-assist-r21-threads-deploy.json
org/missions/D9/COMM/COMM_ASSIST/task-orders/COMM_ASSIST.TO-CA-n-2.thread-replies-deploy.md
org/missions/D9/COMM/COMM_ASSIST/deliverables/0.7.0_AE_CloudOps~COMM1/
org/missions/D9/COMM/COMM_ASSIST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE the act creates no schedule; the ingress keeps its 1-minute clock and the End of Day window 20:00Z-21:45Z is a Branch B stop. No cron, alarm, monitor or notification is created.
comp-iam: DECLARED-NOT-APPLICABLE no policy moves: Branch A is the code hash only; the replies route is already granted (the End of Day reader in assist.py calls it).
comp-adversary: RUN -- a second writer moving the live hash or the mode before the act (step 3 -> Branch B); a package built from the moving trunk (pinned worktree, step 1); foreign registry rows riding the package (AC1 counts the three foreign files and the 17 probes compare the S3 addresses and mail parties on both packages); a thread read that fails holding back a channel (CA-n-1 arm 8, run again by AC1 and AC2 on the built and served code); the poll overspending the gateway (N1 `budget` arm; the 10-minute log read checks `calls` at most 20); an environment change or the mode leaving `enforce` (Branch B); the secret leaking (never read). BLIND: real Teams traffic after the apply is not exercised by the act.
lane: the <paths> block IS the grant (worker RULING 1). The lane is the COMM macro CloudOps lane (CLAUDE.md rule 34).
</preflight>

Base `1aa63bde67`: CAn2-AC1 base: ok=False until a detached worktree at the pin is built (measured: `reason=RuntimeError: no detached worktree at the pin 1aa63bde67`); against the issuer's own pinned build (since removed) `ok=True differ=4 foreign=3 probes=17 same=17 n1=8 of 8`. CAn2-AC2 base: FAIL as measured (`hashes [PRE, PRE]`, the old `channel_mentions.py`, N1 2 of 8 on the served zip; probes 17 same 17). CAn2-AC3 base: FAIL as measured (no entry).
Source: CTO ruling on call 446a (@f418537712, msg 109753); PRD v0.10 FWD-3 and FWD-13; COO half `NEVER_WIDEN_HALF_COO_COMM_ASSIST_R21_THREADS_DEPLOY_20261016.md`; ledger precedent `comm-assist-r20-narrow-deploy`.
