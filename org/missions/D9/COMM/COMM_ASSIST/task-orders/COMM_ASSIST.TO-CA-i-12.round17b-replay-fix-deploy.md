# TO COMM_ASSIST.TO-CA-i-12 -- round 17 CA-i-12: deploy the replay fix (one targeted apply of module.ldo_001, code only, pinned build)

<to_id>COMM_ASSIST.TO-CA-i-12</to_id>
<project>COMM_ASSIST</project>
<issued_to>0.7.0_AE_CloudOps~CA</issued_to>
<issued_by>2.0.0_SA_COO~CA</issued_by>
<issued_date>2026-10-14</issued_date>
<status>staged</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>17</round>
<workstream>DEPLOY17B</workstream>

**Directive:** D9 | **Fabric:** laptop | **Decomp cell:** `CA-i-12` (`decompositions/COMM_ASSIST_DECOMP.round17.md`, AMENDMENT 4) | **outcome_ref:** FWD-7 |
**depends_on:** CA-i-10 (merged `8a480805e5`), CA-i-4 (CLOSED @4df21cf33f); the GO waits on the CTO and CVO halves

---

## WORKER FACE

### GO

The issuer flips `<status>` to `pending` and writes `GO` on the line below once all three halves are SIGNED on the pin. Until then, do nothing.

GO -- (not yet written). The halves BIND, and the COO half's Branch A / Branch B, rollback and conditions ARE the procedure. Read all three in full (all under `org/missions/D9/COMM/COMM_ASSIST/deliverables/`):
- COO `2.0.0_SA_COO~CA/NEVER_WIDEN_HALF_COO_COMM_ASSIST_R17B_DEPLOY_20261014.md`
- CTO and CVO: named in the GO line

### THE CELL

`CA-i-12`. The same two Lambdas as your last order (`CA-i-4`, ledger `comm-assist-r17-deploy`, CLOSED), now on `lRKObLMbn1kTWSXtohLxZ33HYVq7aBd1o/fjLfaA1Rw=`. The trunk carries ONE more change on top of that package: `tenant.py`, cell `CA-i-10`
(a signed muse answer must carry the draft's version and seq, and the same signed bytes never act twice). This cell ships exactly that: code only. No environment value moves.

### DO, IN THIS ORDER (the laptop, from the shared trunk at or after this order's issuance commit)

1. `git worktree add --detach <scratch> 8a480805e5` (outside every other worktree). Every build, test, init, plan, apply and re-plan below runs FROM that pinned worktree. Confirm `git -C <scratch> status --porcelain` is empty.
2. Open the ledger `comm-assist-r17b-deploy` (`python .tools/deploy_ledger.py open ...` from the shared trunk), naming both functions. Commit the entry AND the sentinel BEFORE the act.
3. BEFORE reads, saved in your deliverables folder `org/missions/D9/COMM/COMM_ASSIST/deliverables/0.7.0_AE_CloudOps~CA/`: both functions' `CodeSha256` and `LastModified`; both functions' environment KEY NAMES (never values); the live zip with its sha256.
   If the live hash is not `lRKObLMb...`, that is Branch B: another writer moved it. Stop and report.
4. Build in the pinned worktree: `bash infra/aws/lambda/transcripts-pull/build.sh` and `bash infra/aws/lambda/teams-chat-assist/build.sh`. Run the import test on `infra/aws/lambda/teams-chat-assist/dist/pkg`. Record the built zip's base64 sha256.
   Then run AC1 below: it must read `ok=True` BEFORE any apply.
5. `TF_DATA_DIR` = a NEW scratch directory outside every git tree. `init -input=false` against the declared backend; a migrate or reconfigure prompt means STOP. Take a saved, locked, targeted plan `-target=module.ldo_001`, with NO `-var`.
   - Branch A exactly -> apply that saved plan through `bash .tools/safe-apply.sh`. Branch A is `0 to add, 2 to change, 0 to destroy`: the handler and `ingress[0]` only, changed keys within {`source_code_hash`, `last_modified`} and NOTHING else (no `environment`), the after-hash equal to step 4's.
   - Anything else -> Branch B: apply nothing, close the ledger as not-applied, report.
   - Never between 20:00Z and 21:45Z.
6. AFTER: run the criteria below, then a targeted re-plan (expect no changes). Read log lines only, never message content. Ten minutes on, the ingress log still shows `ingress_poll` and the mail step `polled`.
7. Rollback on any AFTER failure: the COO half's rollback (the saved zip over `dist/`, then the same targeted apply). File an ARMED row naming `2.0.0_SA_COO~CA`, and report.
8. Close the ledger and commit. Remove the pinned worktree. Send no test mail, text nobody and invoke nothing.

### RULES FOR THIS CELL

- One targeted apply, `module.ldo_001` only. Never untargeted, never bare `terraform`, never `aws lambda update-function-code`.
- No `-var`. No edit to any `.tf` or code file. Never push, `git stash`, rebase, `checkout --`, `clean`.
- No non-ASCII. `dist/` is never committed.
- Refuse a criterion you cannot satisfy as written. File a BLOCKING row with the measurement and stop; do not widen.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CAi12-AC1" cell_refs="CA-i-12"><invocation>python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r17/checks/check_i12_equiv.py"</invocation><expect>I12-EQUIV ok=True</expect></criterion>
`CAi12-AC1` -- the issuer's pre-flight check (read it; do not edit it), run BEFORE the apply with the pinned worktree built: the packaged-path diff from the deployed pin is exactly `tenant.py`, the built `tenant.py` equals the pin's bytes, and the built package forms the same S3 addresses and considers the same mail parties as the package the live function serves (17 probes). It reads ok=False until the build exists.

<criterion id="CAi12-AC2" cell_refs="CA-i-12"><invocation>python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r17/checks/check_i12_live.py"</invocation><expect>RESULT: PASS</expect></criterion>
`CAi12-AC2` -- the issuer's live check (read it; do not edit it). Both functions are on one new package, not `lRKObLMb...`; the served zip hashes to it and its four files equal the pin's; both environments as recorded; the served code routes `muse.reply`, accepts a real signature, refuses another key, stamps `ldo-001`, refuses a payload without version, carries seq, and holds the acted-set guard. It FAILs at the base.

<criterion id="CAi12-AC3" cell_refs="CA-i-12"><invocation>bash "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r17/checks/check_i12_ledger.sh"</invocation><expect>RESULT: PASS</expect></criterion>
`CAi12-AC3` -- NEVER-2: the ledger `comm-assist-r17b-deploy` is committed CLOSED at HEAD and its sentinel is gone. It FAILs at the base.
</proof_of_spec>

<expected_criteria>CAi12-AC1,CAi12-AC2,CAi12-AC3</expected_criteria>

Each invocation runs under `timeout 120`. Write the proof instance to
`org/missions/D9/COMM/COMM_ASSIST/deliverables/0.7.0_AE_CloudOps~CA/COMM_ASSIST.TO-CA-i-12.round17b-replay-fix-deploy.proof_of_spec.json`, validate it with
`python .tools/proof-of-spec-check.py <instance> CAi12-AC1,CAi12-AC2,CAi12-AC3`, and flip `<status>` to `complete` only when all three PASS and the instance is VALID. Surprise rows are
`COMM_ASSIST-C12-S<k>`, fabric `laptop`, disarm_owner `2.0.0_SA_COO~CA`, `surfaced_at` = `date -u +%FT%TZ` at filing. Append lines only to the investigation file.

<decomp_ref>
<decomp_doc>org/missions/D9/COMM/COMM_ASSIST/decompositions/COMM_ASSIST_DECOMP.round17.md</decomp_doc>
<owned_cells>CA-i-12</owned_cells>
</decomp_ref>

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/comm-assist-r17b-deploy.json
org/missions/D9/COMM/COMM_ASSIST/task-orders/COMM_ASSIST.TO-CA-i-12.round17b-replay-fix-deploy.md
org/missions/D9/COMM/COMM_ASSIST/deliverables/0.7.0_AE_CloudOps~CA/
org/missions/D9/COMM/COMM_ASSIST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE the act creates no schedule; the ingress keeps its 1-minute clock (module.ldo_001) and the End of Day window 20:00Z-21:45Z is a Branch B stop. No cron, alarm, monitor or notification is created.
comp-iam: DECLARED-NOT-APPLICABLE no policy moves: Branch A is the code hash only, and any iam address or environment key in the plan is Branch B.
comp-adversary: RUN -- a second writer (NFRA_CTLPLN also deploys this module) moving the live hash before the act (step 3 -> Branch B); a package built from the moving trunk (pinned worktree, step 1); a foreign file riding the package (AC1 asserts the packaged-path diff is exactly tenant.py); an environment change slipping into the plan (Branch B); a replay guard that blocks a legitimate answer (covered by round 17's receiver checks and AC2's probe). BLIND: muse cannot reach the receiver end to end until the forwarder is installed (cell CA-i-5), so the guard is exercised by the checks, not by a live answer.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Base `8a480805e5`: CAi12-AC1 base: FAIL as expected (no built package at the pin). CAi12-AC2 base: FAIL as expected (pre-state hash; the served tenant.py lacks the guard). CAi12-AC3 base: FAIL as expected (0 entries). AC1 green arm: PASS as measured (17 of 17, files=1) on the issuer's real pre-flight build of the pin; AC2's probe green on that same build (route, accept, refuse, stamp, version, seq, guard).
Source: COO half `NEVER_WIDEN_HALF_COO_COMM_ASSIST_R17B_DEPLOY_20261014.md`; the first deploy's halves (CTO `d7cd346166`, CVO `d2c7360c00`, whose "Carried" section is this cell's reason); ledger precedent `comm-assist-r17-deploy`.
