# TO COMM_ASSIST.TO-CA-l-4 -- round 20 CA-l-4: deploy the narrower package (one targeted apply of module.ldo_001, code only, pinned build, 39 files become 34)

<to_id>COMM_ASSIST.TO-CA-l-4</to_id>
<project>COMM_ASSIST</project>
<issued_to>0.7.0_AE_CloudOps~CA</issued_to>
<issued_by>2.0.0_SA_COO~CA</issued_by>
<issued_date>2026-10-15</issued_date>
<status>staged</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>GO</placeholders>
<round>20</round>
<workstream>DEPLOY20NARROW</workstream>

**Directive:** D9 | **Fabric:** laptop | **Decomp cell:** `CA-l-4` (`decompositions/COMM_ASSIST_DECOMP.round20.md`, cell table) | **outcome_ref:** FWD-4, FWD-13 |
**depends_on:** CA-l-2 (merged `c91b5dc61d`), CA-l-3 (merged; the pin is the trunk after it); the GO waits on the three halves
**STAGED.** The GO block below is not written until the three halves are SIGNED on the pin; this order is `staged` until then and the seat does not begin.

---

## WORKER FACE

### GO

<<ISSUER: GO line -- "GO -- written by 2.0.0_SA_COO~CA" plus the date and time>>. All three halves SIGNED on the pin `863dc0f739`: COO (`2.0.0_SA_COO~CA/NEVER_WIDEN_HALF_COO_COMM_ASSIST_R20_NARROW_DEPLOY_20261015.md`, commit <<ISSUER: COO half commit>>), CTO (<<ISSUER: CTO half path under 1.0.0_SA_CTO/ and its commit>>), CVO (<<ISSUER: CVO half path under 3.0.0_SA_CVO/ and its commit>>). <<ISSUER: the conditions the CTO and CVO halves add, if any; the COO half already carries the R19 conditions: one sitting, dead-letter queue unchanged, 5 GB, the gate line, check_j5_obs not DIRTY>>
Timing: apply BEFORE 19:30Z, so it lands ahead of the End of Day window (20:00Z-21:45Z); if you cannot finish in one sitting before 19:30Z, do not apply until the window has closed and report.
Rollback is a targeted apply from a detached worktree at `93a3f55d25` (the commit the live CA-k-4 package was built from; its Terraform default is `enforce`), NEVER from `afa8752f44` (its default is `record`).

The three halves BIND, and the COO half's Branch A / Branch B, rollback and conditions ARE the procedure. Read all three in full (all under `org/missions/D9/COMM/COMM_ASSIST/deliverables/`):
- COO `2.0.0_SA_COO~CA/NEVER_WIDEN_HALF_COO_COMM_ASSIST_R20_NARROW_DEPLOY_20261015.md`
- CTO `1.0.0_SA_CTO/<<ISSUER: CTO half file name>>`
- CVO `3.0.0_SA_CVO/<<ISSUER: CVO half file name>>`

### THE CELL

`CA-l-4`. The same two Lambdas as your last order (`CA-k-4`, ledger `comm-assist-r19-pending-deploy`, CLOSED), now on `nQlJW0j/a2nE1om0ZbXm9CTMxAVDXwUQNju62S4xa9k=` (the CA-k-4 package, 39 files, built at `93a3f55d25`) with the ingress mark in `enforce` mode. The trunk carries `build.sh` packaging only the twelve registry files named in `infra/aws/lambda/teams-chat-assist/registry_files.txt` (cell `CA-l-2`): the package drops `catalog_fork_keys.json`, `event_rules.json`, `key_rulings.json`, `name_rulings.json` and `root_map.json` and holds 34 files. This cell ships exactly that: code only (the source hash and last-modified of the handler and `ingress[0]`). No environment value (`INGRESS_MARK_MODE=enforce`, the 15 key names), policy, secret or Terraform resource moves; the trunk's Terraform default reads `enforce`, equal to what is live.

### DO, IN THIS ORDER (the laptop, from the shared trunk at or after this order's GO)

0. DISK FIRST: `df` on `C:` must read at least 5 GB free. Below that, create nothing (no worktree, no build, no ledger), stop and report the measured figure; do not delete files to make room.
1. `git worktree add --detach <scratch> 863dc0f739` (outside every other worktree). Every build, test, init, plan, apply and re-plan below runs FROM that pinned worktree. Confirm `git -C <scratch> status --porcelain` is empty.
2. Open the ledger `comm-assist-r20-narrow-deploy` (`python .tools/deploy_ledger.py open ...` from the shared trunk), naming both functions (code only; no image). Commit the entry AND the sentinel BEFORE the act.
3. BEFORE reads, saved in your deliverables folder `org/missions/D9/COMM/COMM_ASSIST/deliverables/0.7.0_AE_CloudOps~CA/r20/`: both functions' `CodeSha256`, `LastModified` and environment KEY NAMES (never values); the live zip with its sha256 and base64 sha256 (the rollback copy, 39 files); the dead-letter queue `teams-global-chat-assist-dlq.fifo` `ApproximateNumberOfMessages` and `ApproximateNumberOfMessagesNotVisible` (the issuer last read 0 and 0); the output of `python org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r18/checks/check_j5_obs.py` (it must NOT read `DIRTY`; the issuer's `probe:` row is counted apart).
   If the live hash is not `nQlJW0j/a2nE1om0ZbXm9CTMxAVDXwUQNju62S4xa9k=` or the mode is not `enforce`, that is Branch B: another writer moved something. Stop and report.
4. Build in the pinned worktree: `bash infra/aws/lambda/teams-chat-assist/build.sh` (it must print `(34 files)`). Run the import test on `infra/aws/lambda/teams-chat-assist/dist/pkg`. Record the built zip's base64 sha256. Then run AC1 below: it must read `ok=True` BEFORE any apply. (The root needs both `dist` zips to plan: build `transcripts-pull` too if the plan asks for it, locally, uploading nothing.)
5. `TF_DATA_DIR` = a NEW scratch directory outside every git tree. `init -input=false` against the declared backend; a migrate or reconfigure prompt means STOP. Take a saved, locked, targeted plan `-target=module.ldo_001`, with NO `-var`. The CA-k-2 gate runs inside `safe-apply.sh` for this module: its line must read `LDO001-MODE verdict=OK default=enforce live=enforce`; any other verdict is Branch B (never set `LDO001_MODE_OVERRIDE`).
   - Branch A exactly -> apply that saved plan through `bash .tools/safe-apply.sh`. Branch A is `0 to add, 2 to change, 0 to destroy`: the handler and `ingress[0]` only, changed keys within {`source_code_hash`, `last_modified`} and NEVER `environment`, the after-hash equal to step 4's.
   - Anything else -> Branch B: apply nothing, close the ledger as not-applied, report.
   - Never between 20:00Z and 21:45Z.
6. AFTER: run the criteria below, then a targeted re-plan (expect no changes). Save the dead-letter queue counts again: both must read UNCHANGED from the BEFORE read. Read log lines only, never message content or the secret's value. Ten minutes on, the ingress log still shows `ingress_poll` and the mail step `polled`, and neither function log shows an error or `AccessDenied`.
7. Rollback on any AFTER failure: the COO half's rollback (the saved live zip over `dist/teams-chat-assist.zip`, then a targeted apply from a detached worktree at `93a3f55d25`, NOT from `afa8752f44`, whose Terraform default would flip the mode to `record`). File an ARMED row naming `2.0.0_SA_COO~CA`, and report.
8. Close the ledger and commit. Remove the pinned worktree. Send no test mail, text nobody and invoke nothing.

### RULES FOR THIS CELL

- One targeted apply, `module.ldo_001` only. Never untargeted, never bare `terraform`, never `aws lambda update-function-code`.
- No `-var`. No edit to any `.tf` or code file. Never push, `git stash`, rebase, `checkout --`, `clean`.
- The secret's value is never read, printed, logged, committed or sent.
- No non-ASCII. `dist/` is never committed.
- Refuse a criterion you cannot satisfy as written. File a BLOCKING row with the measurement and stop; do not widen.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CAl4-AC1" cell_refs="CA-l-4"><invocation>M4_PIN=863dc0f739 python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r20/checks/check_m4_equiv.py"</invocation><expect>M4-EQUIV ok=True</expect></criterion>
`CAl4-AC1` -- the issuer's pre-flight check (read it; do not edit it), run BEFORE the apply with the pinned worktree built: the built package differs from the zip the live function serves by exactly the five dropped registry files (live-only) with nothing built-only, every other file equal but the two foreign registry rows (`legacy_addresses.json`, `reporting_policies.json`, counted and printed), the built registry files equal to the manifest's twelve, and the 17 probes (the S3 addresses for a fixed battery of chats and the mail parties) identical from the built package and from the live zip. It reads ok=False until the build exists.

<criterion id="CAl4-AC2" cell_refs="CA-l-4"><invocation>M4_PIN=863dc0f739 python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r20/checks/check_m4_live.py"</invocation><expect>RESULT: PASS</expect></criterion>
`CAl4-AC2` -- the issuer's live check (read it; do not edit it). Both functions are on one new package, not `nQlJW0j...`; the served zip hashes to it, has 34 files and every file in it equals the pin's (but the foreign set); the served registry files equal the manifest's twelve and none of the five dropped files is served; both environments carry `INGRESS_MARK_MODE=enforce`, the same fifteen key names and the other keys as recorded; the secret has a current version (value never read) and both roles may read it; the served code runs the mark checks, writes a clean mention record and mail record, keeps BOTH of two considered mails one minute apart in `state["pending_list"]`, and gives the 17 probes' recorded output (a stand-in ctx, no AWS, no network, no text sent). It FAILs at the base.

<criterion id="CAl4-AC3" cell_refs="CA-l-4"><invocation>bash "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r20/checks/check_m4_ledger.sh"</invocation><expect>RESULT: PASS</expect></criterion>
`CAl4-AC3` -- NEVER-2: the ledger `comm-assist-r20-narrow-deploy` is committed CLOSED at HEAD and its sentinel is gone. It FAILs at the base.
</proof_of_spec>

<expected_criteria>CAl4-AC1,CAl4-AC2,CAl4-AC3</expected_criteria>

Each invocation runs under `timeout 250`, from the shared trunk's root (the checks find the repository from the current directory's git toplevel). Commit the deploy evidence FIRST, then write the proof instance to
`org/missions/D9/COMM/COMM_ASSIST/deliverables/0.7.0_AE_CloudOps~CA/COMM_ASSIST.TO-CA-l-4.narrow-package-deploy.proof_of_spec.json`, pinning each artifact row to the commit that carried it, validate it with
`python .tools/proof-of-spec-check.py <instance> CAl4-AC1,CAl4-AC2,CAl4-AC3` AFTER your last commit, and flip `<status>` to `complete` only when all three PASS and the instance is VALID at the final head. Surprise rows are
`COMM_ASSIST-C20R-S<k>`, fabric `laptop`, disarm_owner `2.0.0_SA_COO~CA`, `surfaced_at` = `date -u +%FT%TZ` at filing. Append lines only to the investigation file.

<decomp_ref>
<decomp_doc>org/missions/D9/COMM/COMM_ASSIST/decompositions/COMM_ASSIST_DECOMP.round20.md</decomp_doc>
<owned_cells>CA-l-4</owned_cells>
</decomp_ref>

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/comm-assist-r20-narrow-deploy.json
org/missions/D9/COMM/COMM_ASSIST/task-orders/COMM_ASSIST.TO-CA-l-4.narrow-package-deploy.md
org/missions/D9/COMM/COMM_ASSIST/deliverables/0.7.0_AE_CloudOps~CA/
org/missions/D9/COMM/COMM_ASSIST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE the act creates no schedule; the ingress keeps its 1-minute clock (module.ldo_001) and the End of Day window 20:00Z-21:45Z is a Branch B stop. No cron, alarm, monitor or notification is created.
comp-iam: DECLARED-NOT-APPLICABLE no policy moves: Branch A is the code hash only, and any iam address or environment key in the plan is Branch B.
comp-adversary: RUN -- a second writer (NFRA_CTLPLN also deploys this module) moving the live hash or the mode before the act (step 3 -> Branch B); a package built from the moving trunk (pinned worktree, step 1); a registry file the assistant opens lazily on a path the 17 probes do not exercise failing at run time (named residual; AC1 compares the built package with the served one and the probes, AC2 runs the served-code probes against the SERVED zip, the dead-letter queue is read before and after and must be unchanged, and the rollback is one targeted apply); a foreign registry row riding the package (AC1 counts `legacy_addresses.json` and `reporting_policies.json` and compares the S3 addresses and mail parties on both packages); a file dropped that the assistant needs (AC1 requires the live-only set to be exactly the five and the registry list to equal the manifest); an environment change or the mode leaving `enforce` in the plan, or the CA-k-2 gate reading anything but OK (Branch B); the disk filling under the build (step 0, 5 GB); the secret value leaking (forbidden; never read). BLIND: a registry file read lazily on an unexercised path (above); real Teams and mail traffic after the apply is not exercised by the act (no test mail is sent).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Base `863dc0f739`: CAl4-AC1 base: ok=False until a detached worktree at the pin is built (measured at trunk `17ac3101eb` with no worktree: `M4-EQUIV ok=False dropped=0 foreign=0 probes=0 same=0 reason=RuntimeError: no detached worktree at the pin 863dc0f739`; against a scratch build from the trunk in place of the pinned worktree the check reads `ok=True dropped=5 foreign=2 probes=17 same=17`). CAl4-AC2 base: FAIL as measured (the served package is the CA-k-4 package: the CodeSha256 equals the BEFORE hash, the zip holds 39 files with 17 registry files, and the five dropped files are served; the environment, secret, served-code and 17-probe arms read True). CAl4-AC3 base: FAIL as measured (0 entries).
Source: CTO round-19 analysis ruling 2 (`ledger/ROUND_ANALYSIS.round19.md` @b4f6d499d0, msg 109356); PRD v0.10 FWD-4 and FWD-13; COO half `NEVER_WIDEN_HALF_COO_COMM_ASSIST_R20_NARROW_DEPLOY_20261015.md`; ledger precedents `comm-assist-r19-pending-deploy`, `comm-assist-r18-records-deploy`, `-enforce-deploy`, `-key-deploy`, `-fresh-deploy`.
