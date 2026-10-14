# TO COMM_ASSIST.TO-CA-i-5 -- round 17 CA-i-5: install the muse answer forwarder on dell2 (the answers folder, the user environment, one scheduled task, one end-to-end refusal test; FWD-7, FWD-8)

<to_id>COMM_ASSIST.TO-CA-i-5</to_id>
<project>COMM_ASSIST</project>
<issued_to>0.7.0_AE_CloudOps~CA2</issued_to>
<issued_by>2.0.0_SA_COO~CA</issued_by>
<issued_date>2026-10-14</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>17</round>
<workstream>FWDINSTALL</workstream>

**Directive:** D9 | **Fabric:** laptop | **Decomp cell:** `CA-i-5` (`decompositions/COMM_ASSIST_DECOMP.round17.md`) | **outcome_ref:** FWD-7, FWD-8 |
**depends_on:** CA-i-3 (forwarder, merged), CA-i-11 (`seq` in the reader rows, live on dell2), CA-i-12 (the receiver's replay guard, live). Addressed by crossbox ORDER to device dell2.

---

## SEAT FACE (read in full; this order is your whole context)

### THE CELL

You hosted the muse reader folder on dell2 in round 16 (`MuseReaderRefresh`, folder `%USERPROFILE%\muse-reader`). Andrew will answer a waiting draft from muse by writing a SIGNED answer file into `answers\` in that folder. The assistant (in AWS) verifies the signature and acts only if it is muse's.
You install the small job that carries each answer file to the assistant: `data/transcripts/scripts/muse_reader/forwarder.py` (already in the repository checkout; read its header). It checks only the shape and the tag, sends each file once, and records what it did in `answers\done\` and `answers\rejected\`. It does NOT check
signatures: the assistant does. You install no key, build nothing, and change no policy, firewall rule or sshd setting. Muse is NOT asked to sign anything yet: a further assistant change (a time bound on signed answers) must be live first.

### DO, IN THIS ORDER

1. **Precondition.** From the repository root of the dell2 checkout run `python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r17/checks/check_i5_pre.py"`. It must print `ok=True` BEFORE anything is installed (the folder's `drafts.json` carries `object_id` and `seq` on every row, the forwarder file is in your checkout, the live assistant gives a
   mailbox address, and your identity is a dell2 user in the admin group). If your checkout does not yet hold the pin of this order's issuance commit, run this box's normal sync (`.tools/box-sync.sh`) once and run the check again. Still `ok=False`: stop and file a BLOCKING row with the line.
2. **The address, from the live assistant.** Read the live handler function's environment (`aws lambda get-function-configuration --function-name teams-global-chat-assist-handler-lambda`, read-only) and set TWO user-level environment variables for the account that runs the task, from those values (never typed): `MUSE_MAILBOX_URL` = the function's `LDO_MAILBOX_URL`, `MUSE_LDO_ID` = its `LDO_ID`
   (`[Environment]::SetEnvironmentVariable('<name>', '<value>', 'User')`). Print the NAMES set and whether each equals the function's value; do not print any secret (there is none: both are addresses).
3. **Run it once by hand** to create the folders and prove it starts: from the repository root, `python data\transcripts\scripts\muse_reader\forwarder.py --root "%USERPROFILE%\muse-reader"` (with the two variables in that session's environment). It must print `MUSE-FORWARD sent=0 rejected=0 failed=0` and leave `answers\`, `answers\done\` and `answers\rejected\` in place.
4. **Schedule it.** Register ONE Windows scheduled task named `MuseAnswerForward`, every 2 minutes, no end date, run as the same user as `MuseReaderRefresh` (S4U), executing from the repository root:
   `powershell -NoProfile -Command "$env:MUSE_MAILBOX_URL=[Environment]::GetEnvironmentVariable('MUSE_MAILBOX_URL','User'); $env:MUSE_LDO_ID=[Environment]::GetEnvironmentVariable('MUSE_LDO_ID','User'); python data\transcripts\scripts\muse_reader\forwarder.py --root $env:USERPROFILE\muse-reader"`
   (the task reads the two variables itself, so the schedule works whether or not the session carries them). Record the exact registration command in your report. Start it once and wait for it to finish.
5. **Read the install back.** Run `check_i5_install.py` (AC2 below): `ok=True`.
6. **The end-to-end refusal test.** Run `check_i5_e2e.py` (AC3 below) ONCE from the repository root. It writes one answer for a draft that is waiting now, signed by a THROWAWAY key (never muse's), runs the forwarder once, and reads the draft's state until the assistant has recorded a `bad-signature` refusal. The signature cannot verify, so no draft is touched and nothing is sent to anyone.
   The test file stays in `answers\done\` as the record. Run it once only.
7. **Rows and report.** Any surprise is a row `COMM_ASSIST-CA2-S<k>` appended to the investigation file; keep its line endings.

### RULES

- Edit nothing outside `<paths>` and the dell2 things above (two user environment variables, the `answers\` folders, the one scheduled task). AWS: reads, plus the forwarder's own `sqs send-message` (through the job and the test). No other write, no IAM change, no firewall or sshd change, no new key.
- **ROLLBACK (yours to run on the issuer's word, and the report states it):** `Unregister-ScheduledTask -TaskName MuseAnswerForward -Confirm:$false`; remove the two user environment variables (`[Environment]::SetEnvironmentVariable('MUSE_MAILBOX_URL', $null, 'User')`, the same for `MUSE_LDO_ID`); the `answers\` folder may stay (it holds only the test record).
- This is not an alert, monitor or notification: the job only moves files and sends one queue message per answer. If you think it needs one, stop and file a row.
- A refused or unmet criterion is reported with its measurement, never repaired by widening it.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CAi5-AC1" cell_refs="CA-i-5"><invocation>python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r17/checks/check_i5_pre.py"</invocation><expect>I5-PRE ok=True</expect></criterion>
`CAi5-AC1` -- the precondition, run BEFORE the install (also true after it): dell2, every reader row carries `object_id` and the `seq` key, the forwarder file is present, the live assistant gives a mailbox address and id, and the caller is a dell2 admin-group user. It prints ok=False at the base.

<criterion id="CAi5-AC2" cell_refs="CA-i-5"><invocation>python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r17/checks/check_i5_install.py"</invocation><expect>I5-INSTALL ok=True</expect></criterion>
`CAi5-AC2` -- the install: the task `MuseAnswerForward` exists with last result 0, the two user variables equal the live assistant's values, and the three `answers` folders exist. It prints ok=False at the base.

<criterion id="CAi5-AC3" cell_refs="CA-i-5"><invocation>python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r17/checks/check_i5_e2e.py"</invocation><expect>I5-E2E ok=True</expect></criterion>
`CAi5-AC3` -- the seam against the REAL neighbours, end to end on a forged answer: folder, forwarder, queue, assistant; the assistant records a `bad-signature` refusal for that draft's tag and nothing else happens. It prints ok=False at the base.
</proof_of_spec>

<expected_criteria>CAi5-AC1,CAi5-AC2,CAi5-AC3</expected_criteria>

Each invocation runs from the repository root under `timeout 200` (AC3 waits up to 150 seconds). Write the proof instance to
`org/missions/D9/COMM/COMM_ASSIST/deliverables/0.7.0_AE_CloudOps~CA2/COMM_ASSIST.TO-CA-i-5.install-the-answer-forwarder-on-dell2.proof_of_spec.json`, validate it with `python .tools/proof-of-spec-check.py <instance> CAi5-AC1,CAi5-AC2,CAi5-AC3` from inside the checkout, and flip `<status>` to
`complete` only when all three pass and the instance is VALID. Commit with `.tools/safe-commit.sh` under your own serial. Your final report names: the three output lines, the exact scheduled-task registration command, the names of the variables set, and the rollback command.
Your surprise rows are `COMM_ASSIST-CA2-S<k>`.

<decomp_ref>
<decomp_doc>org/missions/D9/COMM/COMM_ASSIST/decompositions/COMM_ASSIST_DECOMP.round17.md</decomp_doc>
<owned_cells>CA-i-5</owned_cells>
</decomp_ref>

<paths>
org/missions/D9/COMM/COMM_ASSIST/task-orders/COMM_ASSIST.TO-CA-i-5.install-the-answer-forwarder-on-dell2.md
org/missions/D9/COMM/COMM_ASSIST/deliverables/0.7.0_AE_CloudOps~CA2/
org/missions/D9/COMM/COMM_ASSIST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a Windows scheduled task on one dell2 account, not an EventBridge rule or Lambda trigger; the 2-minute cadence is the order's own (step 4) and checked by AC2's last result.
comp-iam: DECLARED-NOT-APPLICABLE no grant moves; the Dell users hold the admin group (CTO ruling @53acd6fe5f, applied) and the job uses sqs:SendMessage on the mailbox under it; AC1 reads the identity.
comp-adversary: RUN -- the address typed instead of read from the live assistant (refused: AC2 compares both variables to the live function); a forwarder that signs or verifies anything (refused: the cell; the forwarder holds no key); the test aimed at a draft with muse's real key (refused: AC3 uses a throwaway key that is not pinned, and the action is a drop that cannot verify); installing before the reader rows carry seq (refused: AC1); muse asked to sign a real answer too early (refused: the cell; a time bound on signed answers goes live first). BLIND: muse's real signed answer is Andrew's act and is not exercised here; the off-tailnet and write permissions on the answers folder (the same Test account as the agents) are not changed by this order.
naming: a local scheduled-task name and two user environment variable names; no S3 address, AWS resource or registry name is created (CLAUDE.md rule 30 non-application).
lane: the <paths> block IS the grant (worker RULING 1); the scheduled task, the two variables and the answers folders are the named dell2 writes and are not repo paths.
</preflight>

Base: CAi5-AC1 base: FAIL as expected (device laptop, no folder); CAi5-AC2 base: FAIL as expected (this box is not dell2); CAi5-AC3 base: FAIL as expected (this box is not dell2). The check logic was exercised once from the laptop with the device gate removed: AC1 `ok=True` (7 rows, object_id 7, seq key 7, forwarder, mailbox) and AC3 `ok=True forwarded=1 refused=bad-signature` against the live assistant on a scratch copy of the folder (so the path folder -> forwarder -> queue -> receiver is proven before this order).
Source: CVO half `NEVER_WIDEN_HALF_CVO_COMM_ASSIST_R17B_DEPLOY_20261014.md` ("C-S5: YES"); issuer ruling R-8; CA-i-3 report; PRD v0.7 FWD-7, FWD-8.
