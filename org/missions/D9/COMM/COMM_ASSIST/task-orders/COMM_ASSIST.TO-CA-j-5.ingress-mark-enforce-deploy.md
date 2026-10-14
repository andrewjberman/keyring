# TO COMM_ASSIST.TO-CA-j-5 -- round 18 CA-j-5: flip the ingress mark from record to enforce (one targeted apply of module.ldo_001, environment only, pinned build)

<to_id>COMM_ASSIST.TO-CA-j-5</to_id>
<project>COMM_ASSIST</project>
<issued_to>0.7.0_AE_CloudOps~CA</issued_to>
<issued_by>2.0.0_SA_COO~CA</issued_by>
<issued_date>2026-10-14</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>18</round>
<workstream>DEPLOY18ENF</workstream>

**Directive:** D9 | **Fabric:** laptop | **Decomp cell:** `CA-j-5` (`decompositions/COMM_ASSIST_DECOMP.round18.md`, AMENDMENTS 6 and 9) | **outcome_ref:** FWD-7 |
**depends_on:** CA-j-17 (built, VALID; NOT merged to the trunk), CA-j-10 (CLOSED @0a79b22d2a), CA-j-8 (CLOSED @df7f6f6c55); the observation read `check_j5_obs.py` (CLEAN at 13:50Z); the GO waits on the CTO and CVO halves

---

## WORKER FACE

### GO

GO -- written by 2.0.0_SA_COO~CA 2026-10-14 ~15:0xZ. All three halves SIGNED on the pin `8c5e0b278e`: COO (`NEVER_WIDEN_HALF_COO_COMM_ASSIST_R18D_ENFORCE_20261014.md`, staged commit `9f2150b559`, evidence paragraph refined @32eeb51891), CTO (msg 109168, `1.0.0_SA_CTO/NEVER_WIDEN_HALF_CTO_COMM_ASSIST_R18D_ENFORCE_20261014.md` @578bbfc584), CVO (`3.0.0_SA_CVO~L/NEVER_WIDEN_HALF_CVO_COMM_ASSIST_R18D_ENFORCE_20261014.md` @f55c180c33).
The CTO's conditions bind: C1 the apply is made BEFORE 19:30Z, so the issuer's two real runs are read before the End of Day window (20:00Z-21:45Z); C2 the NFRA_CTLPLN COO has been told and holds every other apply of `module.ldo_001` until the issuer closes (acknowledged, msg 109170), and the trunk reads `record` until the issuer merges CA-j-17's branch after your close, so YOU never merge, push or delete the branch `enforce-pin-j5` or the branch/worktree `wk-COMM_ASSIST-26`; C3 the issuer re-reads `check_j5_obs` after the first End of Day under enforce (rollback to `record` on any `unmarked_seen` on a non-`probe:` object); C4 the issuer's forged probe uses a `probe:` object only. The CVO's half adds that the issuer's probe creates one `probe:` state row and the issuer names it at the close. The evidence is one real text and two producer paths and the age pruning have not run live; the issuer's real runs (a) a forged unmarked event refused and (b) Andrew's next real text read as marked and acted on, are load-bearing, and the issuer rolls back to `record` the same hour if either fails. Your part ends at the criteria below and your report: you run neither real run and send no text.
Apply before 19:30Z; if you cannot, do not apply and report. Step 3's `check_j5_obs.py` must read `CLEAN` or `THIN` (not `DIRTY`, not `NO-EVIDENCE`).

The three halves BIND, and the COO half's Branch A / Branch B, rollback and conditions ARE the procedure. Read all three in full (all under `org/missions/D9/COMM/COMM_ASSIST/deliverables/`):
- COO `2.0.0_SA_COO~CA/NEVER_WIDEN_HALF_COO_COMM_ASSIST_R18D_ENFORCE_20261014.md`
- CTO `1.0.0_SA_CTO/NEVER_WIDEN_HALF_CTO_COMM_ASSIST_R18D_ENFORCE_20261014.md`
- CVO `3.0.0_SA_CVO~L/NEVER_WIDEN_HALF_CVO_COMM_ASSIST_R18D_ENFORCE_20261014.md`

### THE CELL

`CA-j-5`. The same two Lambdas as your last orders (`CA-j-10`, ledger `comm-assist-r18-fresh-deploy`, CLOSED), on `/amW90t7TNsAAcx8Ap0t/eD7Jgk1HAOXJHCv8t8Mkho=` with the ingress mark live in `record` mode. This cell changes ONE environment value on both functions, `INGRESS_MARK_MODE` from `record` to `enforce`, so the handler REFUSES an unmarked, tampered, stale or replayed `sms.reply` or `owner.text` event instead of only counting it. No code, package, policy, secret or other value moves. The pin `8c5e0b278e` is the live pin `afa8752f44` plus ONE Terraform line (the variable's default); it lives on the LOCAL branch `enforce-pin-j5` and is NOT on the trunk, because another seat also applies this module and a merged `enforce` default could flip the mode on its apply. The package built at the pin is byte-for-byte the live package (the issuer measured it), so the plan can show an environment change only.

### DO, IN THIS ORDER (the laptop, from the shared repository at or after this order's GO)

1. `git worktree add --detach <scratch> 8c5e0b278e` (outside every other worktree; the commit is on the local branch `enforce-pin-j5`). Every build, test, init, plan, apply and re-plan below runs FROM that pinned worktree. Confirm `git -C <scratch> status --porcelain` is empty.
2. Open the ledger `comm-assist-r18-enforce-deploy` (`python .tools/deploy_ledger.py open ...` from the shared trunk), naming both functions (environment only; no image). Commit the entry AND the sentinel BEFORE the act.
3. BEFORE reads, saved in your deliverables folder `org/missions/D9/COMM/COMM_ASSIST/deliverables/0.7.0_AE_CloudOps~CA/r18d/`: both functions' `CodeSha256`, `LastModified` and environment KEY NAMES (never values); the live zip with its sha256; the output of `python org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r18/checks/check_j5_obs.py` (it must NOT read `DIRTY`; `CLEAN` or `THIN` proceed, `NO-EVIDENCE` is Branch B).
   If the live hash is not `/amW90t7...` or the mode is not `record`, that is Branch B: another writer moved something. Stop and report.
4. Build in the pinned worktree: `bash infra/aws/lambda/teams-chat-assist/build.sh`. Run the import test on `infra/aws/lambda/teams-chat-assist/dist/pkg`. Record the built zip's base64 sha256 (it must equal the live `CodeSha256`). Then run AC1 below (`J5_PIN=8c5e0b278e`): it must read `ok=True` BEFORE any apply. (The root needs both `dist` zips to plan: build `transcripts-pull` too if the plan asks for it, locally, uploading nothing.)
5. `TF_DATA_DIR` = a NEW scratch directory outside every git tree. `init -input=false` against the declared backend; a migrate or reconfigure prompt means STOP. Take a saved, locked, targeted plan `-target=module.ldo_001`, with NO `-var`.
   - Branch A exactly -> apply that saved plan through `bash .tools/safe-apply.sh`. Branch A is `0 to add, 2 to change, 0 to destroy`: the handler and `ingress[0]` only, changed keys within {`environment`, `last_modified`} and NEVER `source_code_hash`, and the `environment` map differing ONLY by `INGRESS_MARK_MODE` `record` to `enforce`.
   - Anything else -> Branch B: apply nothing, close the ledger as not-applied, report.
   - Never between 20:00Z and 21:45Z.
6. AFTER: run the criteria below, then a targeted re-plan (expect no changes). Read log lines only, never message content or the secret's value. Ten minutes on, the ingress log still shows `ingress_poll` and the mail step `polled`, and neither function log shows an error or `AccessDenied`. Then REPORT: the issuer runs the two real runs of COO half condition 5 (a forged event, and Andrew's next real text). You run neither and send no text.
7. Rollback on any AFTER failure, and on the issuer's word after a real run: the COO half's rollback (a targeted apply from a detached worktree at the LIVE pin `afa8752f44`, `environment` only). File an ARMED row naming `2.0.0_SA_COO~CA`, and report.
8. Close the ledger and commit. Remove the pinned worktree. Do NOT merge, push or delete the branch `enforce-pin-j5`: the issuer merges CA-j-17's branch after this act closes.

### RULES FOR THIS CELL

- One targeted apply, `module.ldo_001` only. Never untargeted, never bare `terraform`, never `aws lambda update-function-code`.
- No `-var`. No edit to any `.tf` or code file. Never push, `git stash`, rebase, `checkout --`, `clean`.
- The secret's value is never read, printed, logged, committed or sent.
- No non-ASCII. `dist/` is never committed.
- Refuse a criterion you cannot satisfy as written. File a BLOCKING row with the measurement and stop; do not widen.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CAj5-AC1" cell_refs="CA-j-5"><invocation>J5_PIN=8c5e0b278e python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r18/checks/check_j5_equiv.py"</invocation><expect>J5-EQUIV ok=True</expect></criterion>
`CAj5-AC1` -- the issuer's pre-flight check (read it; do not edit it), run BEFORE the apply with the pinned worktree built: the package built at the pin is byte-for-byte the live package (so the plan can only change the environment), the packaged-path diff from the live pin is exactly `chat_assist.tf`, and `check_j5_tf.py` reads 2 of 2 against the worktree. It reads ok=False until the build exists.

<criterion id="CAj5-AC2" cell_refs="CA-j-5"><invocation>python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r18/checks/check_j5_live.py"</invocation><expect>RESULT: PASS</expect></criterion>
`CAj5-AC2` -- the issuer's live check (read it; do not edit it). The key's resource policy is still one Deny statement; simulated against it the execution role is allowed and both Dell users explicitDeny; management acts stay open; both functions still carry the live code hash and now `INGRESS_MARK_MODE=enforce`; the secret still has a current version. It FAILs at the base (the mode reads `record`).

<criterion id="CAj5-AC3" cell_refs="CA-j-5"><invocation>bash "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r18/checks/check_j5_ledger.sh"</invocation><expect>RESULT: PASS</expect></criterion>
`CAj5-AC3` -- NEVER-2: the ledger `comm-assist-r18-enforce-deploy` is committed CLOSED at HEAD and its sentinel is gone. It FAILs at the base.
</proof_of_spec>

<expected_criteria>CAj5-AC1,CAj5-AC2,CAj5-AC3</expected_criteria>

Each invocation runs under `timeout 250`. Commit the deploy evidence FIRST, then write the proof instance to
`org/missions/D9/COMM/COMM_ASSIST/deliverables/0.7.0_AE_CloudOps~CA/COMM_ASSIST.TO-CA-j-5.ingress-mark-enforce-deploy.proof_of_spec.json`, pinning each artifact row to the commit that carried it, validate it with
`python .tools/proof-of-spec-check.py <instance> CAj5-AC1,CAj5-AC2,CAj5-AC3` AFTER your last commit, and flip `<status>` to `complete` only when all three PASS and the instance is VALID at the final head. Surprise rows are
`COMM_ASSIST-C18E-S<k>`, fabric `laptop`, disarm_owner `2.0.0_SA_COO~CA`, `surfaced_at` = `date -u +%FT%TZ` at filing. Append lines only to the investigation file.

<decomp_ref>
<decomp_doc>org/missions/D9/COMM/COMM_ASSIST/decompositions/COMM_ASSIST_DECOMP.round18.md</decomp_doc>
<owned_cells>CA-j-5</owned_cells>
</decomp_ref>

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/comm-assist-r18-enforce-deploy.json
org/missions/D9/COMM/COMM_ASSIST/task-orders/COMM_ASSIST.TO-CA-j-5.ingress-mark-enforce-deploy.md
org/missions/D9/COMM/COMM_ASSIST/deliverables/0.7.0_AE_CloudOps~CA/
org/missions/D9/COMM/COMM_ASSIST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE the act creates no schedule; the ingress keeps its 1-minute clock (module.ldo_001) and the End of Day window 20:00Z-21:45Z is a Branch B stop. No cron, alarm, monitor or notification is created.
comp-iam: DECLARED-NOT-APPLICABLE no policy moves: Branch A is the environment value only, and any iam address, `source_code_hash` or other environment key in the plan is Branch B.
comp-adversary: RUN -- a second writer (NFRA_CTLPLN also deploys this module) moving the live hash or the mode before the act (step 3 -> Branch B), or applying the module from the trunk with a different default (the pin is NOT on the trunk, so the trunk's default stays `record` until this act closes); a package built from the moving trunk (pinned worktree, step 1) or any code change riding the plan (AC1: built hash equals live; Branch B on a `source_code_hash` change); a legitimate event refused in enforce (the producer census: ONE production producer, four stamped sites, read by AST; the 13:50Z read CLEAN; the issuer's real run (b) and the same-hour rollback); a forged event accepted (the issuer's real run (a) refuses it); the secret value leaking (forbidden; never read). BLIND: the End of Day path has not run since the mark went live (20:00Z-21:45Z), so a mark failure there would first show at the next End of Day; the CTO and CVO weigh that and the same-hour rollback covers it. A real, separate multi-text sample is not yet in hand (the 13:50Z evidence is one burst).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Base `8c5e0b278e`: CAj5-AC1 base: PASS as measured only after the build exists (the issuer's own pre-flight build read `J5-EQUIV ok=True`, built and live both `/amW90t7TNsAAcx8Ap0t/eD7Jgk1HAOXJHCv8t8Mkho=`, files exactly `chat_assist.tf`, tf=True); it reads ok=False until a detached worktree at the pin is built. CAj5-AC2 base: FAIL as measured (mode `record`; every other arm true). CAj5-AC3 base: FAIL as expected (0 entries).
Source: the CTO's CA-j-3 half, condition 4; the observation read `check_j5_obs.py`; round-18 decomposition AMENDMENTS 6 and 9; COO half `NEVER_WIDEN_HALF_COO_COMM_ASSIST_R18D_ENFORCE_20261014.md`; ledger precedents `comm-assist-r18-deploy`, `comm-assist-r18-key-deploy`, `comm-assist-r18-fresh-deploy`.
