# TO COMM_ASSIST.TO-CA-k-4 -- round 19 CA-k-4: deploy the mail object's list of open drafts (one targeted apply of module.ldo_001, code only, pinned build)

<to_id>COMM_ASSIST.TO-CA-k-4</to_id>
<project>COMM_ASSIST</project>
<issued_to>0.7.0_AE_CloudOps~CA</issued_to>
<issued_by>2.0.0_SA_COO~CA</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>19</round>
<workstream>DEPLOY19PEND</workstream>

**Directive:** D9 | **Fabric:** laptop | **Decomp cell:** `CA-k-4` (`decompositions/COMM_ASSIST_DECOMP.round19.md`, cell table and AMENDMENT 1) | **outcome_ref:** FWD-4, FWD-13 |
**depends_on:** CA-k-1 (merged `2d0a8f5027`), CA-k-2 (merged `d128627a96`), CA-k-3 (merged; the pin is the trunk after it); the GO waits on the three halves
**GO WRITTEN** (see below). The three halves are SIGNED on the pin; this order is `pending`.

---

## WORKER FACE

### GO

GO -- written by 2.0.0_SA_COO~CA 2026-10-15 ~05:2xZ. All three halves SIGNED on the pin `93a3f55d25`: COO (`2.0.0_SA_COO~CA/NEVER_WIDEN_HALF_COO_COMM_ASSIST_R19_PENDING_DEPLOY_20261015.md`, commit `e28d2754f7`, fixed `603acb636a`), CTO (`1.0.0_SA_CTO/NEVER_WIDEN_HALF_CTO_COMM_ASSIST_R19_PENDING_DEPLOY_20261015.md` @2c942a35b1), CVO (`3.0.0_SA_CVO/NEVER_WIDEN_HALF_CVO_COMM_ASSIST_R19_PENDING_DEPLOY_20261015.md` @e605a5dcc0, the base CVO standing in for the unregistered `3.0.0_SA_CVO~L`). The CTO's conditions bind: C1 the act runs only when you can finish it in ONE sitting (apply, AFTER reads, re-plan, ledger close), after the 05:00Z spend-limit reset; a stalled half-landed apply is the NEVER-2 case, so if your seat is stopped on a limit, do not begin; C2 the dead-letter queue after-read must equal the BEFORE read, and any rise means a rollback the same hour; C3 the foreign registry payload (`catalog_fork_keys.json` +4954) is noted for a later `build.sh` cell and is not a condition; C4 the 5 GB free-space precondition stands (do not clean up files to make room). The CVO adds none and notes: after a rollback and redeploy, a `pending_list` entry for a draft answered under the old code would show as open until the 7-day prune or the newest-20 cap, so a redeploy cell must reconcile `pending_list` against `pending`.
Timing: apply after the 05:00Z reset and BEFORE 19:30Z, so it lands ahead of the End of Day window (20:00Z-21:45Z); if you cannot finish in one sitting before 19:30Z, do not apply until the window has closed and report. Rollback is a targeted apply from a detached worktree at `0774100edc` (the commit the CA-j-14 package was built from; its Terraform default is `enforce`), NEVER from `afa8752f44` (its default is `record`).

The three halves BIND, and the COO half's Branch A / Branch B, rollback and conditions ARE the procedure. Read all three in full (all under `org/missions/D9/COMM/COMM_ASSIST/deliverables/`):
- COO `2.0.0_SA_COO~CA/NEVER_WIDEN_HALF_COO_COMM_ASSIST_R19_PENDING_DEPLOY_20261015.md`
- CTO `1.0.0_SA_CTO/NEVER_WIDEN_HALF_CTO_COMM_ASSIST_R19_PENDING_DEPLOY_20261015.md`
- CVO `3.0.0_SA_CVO/NEVER_WIDEN_HALF_CVO_COMM_ASSIST_R19_PENDING_DEPLOY_20261015.md`

### THE CELL

`CA-k-4`. The same two Lambdas as your last order (`CA-j-14`, ledger `comm-assist-r18-records-deploy`, CLOSED @1540Z), now on `BBiNwhfKGcPciG5+zFa2KCIsJ/kF18g+x4ozNN2EnIA=` with the ingress mark in `enforce` mode. The trunk carries the mail object's list of open drafts on top of that package (cell `CA-k-1`): `mail_requests.py` keeps `state["pending_list"]` (a newer considered mail ADDS and never overwrites; `state["pending"]` stays the newest) and `tenant.py` resolves a reply and a signed answer by tag and lists every open draft. This cell ships exactly that: code only. No environment value, policy, secret or Terraform resource moves; the trunk's Terraform default reads `enforce`, equal to what is live.

### DO, IN THIS ORDER (the laptop, from the shared trunk at or after this order's GO)

0. DISK FIRST: `df` on `C:` must read at least 5 GB free. Below that, create nothing (no worktree, no build, no ledger), stop and report the measured figure; do not delete files to make room.
1. `git worktree add --detach <scratch> <the pin>` (outside every other worktree). Every build, test, init, plan, apply and re-plan below runs FROM that pinned worktree. Confirm `git -C <scratch> status --porcelain` is empty.
2. Open the ledger `comm-assist-r19-pending-deploy` (`python .tools/deploy_ledger.py open ...` from the shared trunk), naming both functions (code only; no image). Commit the entry AND the sentinel BEFORE the act.
3. BEFORE reads, saved in your deliverables folder `org/missions/D9/COMM/COMM_ASSIST/deliverables/0.7.0_AE_CloudOps~CA/r19/`: both functions' `CodeSha256`, `LastModified` and environment KEY NAMES (never values); the live zip with its sha256 (the rollback copy); the dead-letter queue `teams-global-chat-assist-dlq.fifo` `ApproximateNumberOfMessages` and `ApproximateNumberOfMessagesNotVisible` (the issuer last read 0 and 0); the output of `python org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r18/checks/check_j5_obs.py` (it must NOT read `DIRTY`; the issuer's `probe:` row is counted apart).
   If the live hash is not `BBiNwhfKGcPciG5+zFa2KCIsJ/kF18g+x4ozNN2EnIA=` or the mode is not `enforce`, that is Branch B: another writer moved something. Stop and report.
4. Build in the pinned worktree: `bash infra/aws/lambda/teams-chat-assist/build.sh`. Run the import test on `infra/aws/lambda/teams-chat-assist/dist/pkg`. Record the built zip's base64 sha256. Then run AC1 below: it must read `ok=True` BEFORE any apply. (The root needs both `dist` zips to plan: build `transcripts-pull` too if the plan asks for it, locally, uploading nothing.)
5. `TF_DATA_DIR` = a NEW scratch directory outside every git tree. `init -input=false` against the declared backend; a migrate or reconfigure prompt means STOP. Take a saved, locked, targeted plan `-target=module.ldo_001`, with NO `-var`. The CA-k-2 gate runs inside `safe-apply.sh` for this module: its line must read `LDO001-MODE verdict=OK default=enforce live=enforce`; any other verdict is Branch B (never set `LDO001_MODE_OVERRIDE`).
   - Branch A exactly -> apply that saved plan through `bash .tools/safe-apply.sh`. Branch A is `0 to add, 2 to change, 0 to destroy`: the handler and `ingress[0]` only, changed keys within {`source_code_hash`, `last_modified`} and NEVER `environment`, the after-hash equal to step 4's.
   - Anything else -> Branch B: apply nothing, close the ledger as not-applied, report.
   - Never between 20:00Z and 21:45Z.
6. AFTER: run the criteria below, then a targeted re-plan (expect no changes). Save the dead-letter queue counts again: both must read UNCHANGED from the BEFORE read. Read log lines only, never message content or the secret's value. Ten minutes on, the ingress log still shows `ingress_poll` and the mail step `polled`, and neither function log shows an error or `AccessDenied`.
7. Rollback on any AFTER failure: the COO half's rollback (the saved zip over `dist/`, then a targeted apply from a detached worktree at `0774100edc`, NOT from `afa8752f44`, whose Terraform default would flip the mode to `record`). File an ARMED row naming `2.0.0_SA_COO~CA`, and report.
8. Close the ledger and commit. Remove the pinned worktree. Send no test mail, text nobody and invoke nothing.

### RULES FOR THIS CELL

- One targeted apply, `module.ldo_001` only. Never untargeted, never bare `terraform`, never `aws lambda update-function-code`.
- No `-var`. No edit to any `.tf` or code file. Never push, `git stash`, rebase, `checkout --`, `clean`.
- The secret's value is never read, printed, logged, committed or sent.
- No non-ASCII. `dist/` is never committed.
- Refuse a criterion you cannot satisfy as written. File a BLOCKING row with the measurement and stop; do not widen.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CAk4-AC1" cell_refs="CA-k-4"><invocation>K4_PIN=93a3f55d25 python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r19/checks/check_l4_equiv.py"</invocation><expect>K4-EQUIV ok=True</expect></criterion>
`CAk4-AC1` -- the issuer's pre-flight check (read it; do not edit it), run BEFORE the apply with the pinned worktree built: the packaged-path diff from the live pin `0774100edc` carries the two CA-k-1 files, the built `mail_requests.py` and `tenant.py` equal the pin's bytes, and the built package forms the same S3 addresses and considers the same mail parties as the package the live function serves (17 probes; `lib/opal_naming.py` and three registry files from other seats are in the diff and are counted as foreign). It reads ok=False until the build exists.

<criterion id="CAk4-AC2" cell_refs="CA-k-4"><invocation>K4_PIN=93a3f55d25 python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r19/checks/check_l4_live.py"</invocation><expect>RESULT: PASS</expect></criterion>
`CAk4-AC2` -- the issuer's live check (read it; do not edit it). Both functions are on one new package, not `BBiNwhfK...`; the served zip hashes to it and every file in it equals the pin's; both environments carry `INGRESS_MARK_MODE=enforce`, the same fifteen key names and the other keys as recorded; the secret has a current version (value never read) and both roles may read it; the served code runs the mark checks, writes a clean mention record and mail record, and keeps BOTH of two considered mails one minute apart in `state["pending_list"]` with `state["pending"]` the newer (a stand-in ctx, no AWS, no network, no text sent). It FAILs at the base.

<criterion id="CAk4-AC3" cell_refs="CA-k-4"><invocation>bash "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r19/checks/check_l4_ledger.sh"</invocation><expect>RESULT: PASS</expect></criterion>
`CAk4-AC3` -- NEVER-2: the ledger `comm-assist-r19-pending-deploy` is committed CLOSED at HEAD and its sentinel is gone. It FAILs at the base.
</proof_of_spec>

<expected_criteria>CAk4-AC1,CAk4-AC2,CAk4-AC3</expected_criteria>

Each invocation runs under `timeout 250`, from the shared trunk's root (the checks find the repository from the current directory's git toplevel). Commit the deploy evidence FIRST, then write the proof instance to
`org/missions/D9/COMM/COMM_ASSIST/deliverables/0.7.0_AE_CloudOps~CA/COMM_ASSIST.TO-CA-k-4.pending-drafts-deploy.proof_of_spec.json`, pinning each artifact row to the commit that carried it, validate it with
`python .tools/proof-of-spec-check.py <instance> CAk4-AC1,CAk4-AC2,CAk4-AC3` AFTER your last commit, and flip `<status>` to `complete` only when all three PASS and the instance is VALID at the final head. Surprise rows are
`COMM_ASSIST-C19R-S<k>`, fabric `laptop`, disarm_owner `2.0.0_SA_COO~CA`, `surfaced_at` = `date -u +%FT%TZ` at filing. Append lines only to the investigation file.

<decomp_ref>
<decomp_doc>org/missions/D9/COMM/COMM_ASSIST/decompositions/COMM_ASSIST_DECOMP.round19.md</decomp_doc>
<owned_cells>CA-k-4</owned_cells>
</decomp_ref>

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/comm-assist-r19-pending-deploy.json
org/missions/D9/COMM/COMM_ASSIST/task-orders/COMM_ASSIST.TO-CA-k-4.pending-drafts-deploy.md
org/missions/D9/COMM/COMM_ASSIST/deliverables/0.7.0_AE_CloudOps~CA/
org/missions/D9/COMM/COMM_ASSIST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE the act creates no schedule; the ingress keeps its 1-minute clock (module.ldo_001) and the End of Day window 20:00Z-21:45Z is a Branch B stop. No cron, alarm, monitor or notification is created.
comp-iam: DECLARED-NOT-APPLICABLE no policy moves: Branch A is the code hash only, and any iam address or environment key in the plan is Branch B.
comp-adversary: RUN -- a second writer (NFRA_CTLPLN also deploys this module) moving the live hash or the mode before the act (step 3 -> Branch B); a package built from the moving trunk (pinned worktree, step 1); a foreign file riding the package (AC1 counts `lib/opal_naming.py` and the registry files and compares the S3 addresses and mail parties on both packages); an environment change or the mode leaving `enforce` in the plan, or the CA-k-2 gate reading anything but OK (Branch B); the list writer failing inside the mail handler (AC2's served-code probe drives two mails through the served writer; the unit tests and `check_l1_pending` read it at the merge; the dead-letter queue is read before and after and must be unchanged); the disk filling under the build (step 0, 5 GB); the secret value leaking (forbidden; never read). BLIND: a real pair of considered mails is not in hand (Andrew's calls 44eb and e435), so the list is exercised by the probe and the tests until the dell2 pick-up and the FWD-13 exercise (CA-k-5).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Base `93a3f55d25`: CAk4-AC1 base: ok=False until a detached worktree at the pin is built (measured at the trunk `d128627a96` with no worktree: `K4-EQUIV ok=False ... reason=RuntimeError: no detached worktree at the pin`; foreign=4). CAk4-AC2 base: FAIL as measured (the served package is the CA-j-14 package: the CodeSha256 equals the BEFORE hash, `mail_requests.py` and `tenant.py` differ from the trunk's, and the served-code probe reads `pending_list: False`). CAk4-AC3 base: FAIL as measured (0 entries).
Source: CTO round-18 analysis ruling 2 (`ledger/ROUND_ANALYSIS.round18.md` @5e4395ae5c, msg 109267); PRD v0.10 FWD-4 and FWD-13; COO half `NEVER_WIDEN_HALF_COO_COMM_ASSIST_R19_PENDING_DEPLOY_20261015.md`; ledger precedents `comm-assist-r18-records-deploy`, `-enforce-deploy`, `-key-deploy`, `-fresh-deploy`.
