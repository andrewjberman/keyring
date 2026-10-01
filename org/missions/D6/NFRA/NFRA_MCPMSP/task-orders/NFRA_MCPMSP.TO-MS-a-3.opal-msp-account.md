# NFRA_MCPMSP task order -- `MS-a-3` -- ROUND 1, hop 4 live: the `Opal_MSP` account on the site-Z box

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPMSP/decompositions/NFRA_MCPMSP_DECOMP.md</decomp_doc>
<owned_cells>MS-a-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_MCPMSP~4</issued_to>
<issued_by>2.0.0_SA_COO~MS</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- a Windows local account; nothing reaches AWS.
comp-adversary: DECLARED-NOT-APPLICABLE -- thread round; the boundary probe (AC2) is the adversary read.
EGRESS CLASS, declared: none.
</preflight>

## 1. THE CELL -- `MS-a-3` (decomposition section 2)

Create the partner runtime's dedicated local account on this box with the harness `MS-t-3` built (earlier in your
queue; merged, with its nested opal_ai commit):

1. Write the REAL config OUTSIDE every repo at `C:\opal_runtime_msp\runtime.msp.config.json`, from
   `opal_ai/opal/runtime-msp/provision/runtime.msp.config.example.json` (`account_name` `Opal_MSP`,
   `checkout_dir` `C:\opal_runtime_msp\opal_ai`, `state_dir` `C:\opal_runtime_msp\state`, the workspace probe file,
   `prod_ref` `PROD`).
2. `provision-account.ps1 -Config C:\opal_runtime_msp\runtime.msp.config.json -Plan`, then the same WITHOUT `-Plan` in
   an ELEVATED session. **Elevation is G-ADMIN (Andrew):** if your shell is not elevated, the script prints
   `ELEVATION REQUIRED` and does nothing; then file ONE BLOCKING row naming G-ADMIN, record the `-Plan` output, and
   stop -- never try to elevate yourself.
3. Read AC1 and AC2. `launch-gate.ps1` needs the opal_ai PROD checkout, which waits on G-PUSH (opal_ai DEV -> PROD,
   `0.0.0_AB_MSTR~Z` on Andrew's word); it is NOT a criterion here and runs at the close.

**AMENDMENT 1 (issuer, 2026-09-30) -- item 0, before the account act.** Andrew ran item 2 in an elevated session and
`provision-account.ps1` failed at parameter binding, before any act: "Cannot validate argument on parameter
'Description'. The character length of the 86 argument is too long ... fewer than or equal to '48' characters". Measured
after: no `Opal_MSP` user, no `C:\opal_runtime_msp\state`, no credential file. The description is a pre-existing literal
(`opal/runtime/provision/provision-account.ps1:116`, identical at opal_ai DEV `fd8ab8a` line 101, NFRA_OPALAI's OA-t-2):
`New-LocalUser -Description` accepts at most 48 characters.
0. In your nested `opal_ai` worktree, shorten ONLY that literal to 48 characters or fewer (for example
   `'Opal runtime agent (provision-account.ps1)'`, 42). Change nothing else. Re-run AC2 of MS-t-3
   (`bash org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/2.0.0_SA_COO~MS/round1/checks/t3.AC2.sh`) and require PASS
   (the default config still plans `Opal_Agent`). Commit it in the nested repo with a message that names NFRA_OPALAI
   OA-t-2 and OA-t-3 (it also unblocks `Opal_Agent`'s own provisioning), and fast-forward nothing yourself -- the
   issuer drains it. File one OBSERVATION row. Then STOP and report: the account act (items 1-3) is Andrew's elevated
   re-run, after which you continue with AC1/AC2 when the issuer hands the order back.

**AMENDMENT 2 (issuer, 2026-09-30) -- item 0b, the boundary verifier's run-as route.** After item 0, Andrew's elevated
run provisioned `Opal_MSP` (AC1 PASS on the issuer's run: exists, enabled, admin=0, codex=0, Opal_Agent unchanged).
AC2 then read `BOUNDARY: BREACH probe=ERROR:Connecting to remote server localhost failed ...`: `verify-boundary.ps1`
runs both probes with `Invoke-Command -ComputerName localhost -Credential` (`:107`, `:112`), which needs WinRM (not
enabled on this box) and, for a non-admin account, Remote Management Users membership -- a security change this project
will not make. It also labels an inability to RUN as the account a `BREACH`, which is false. The sibling
`launcher.ps1:100-102` already runs as the account with `Start-Process -Credential ... -LoadUserProfile`.
0b. In `opal/runtime/provision/verify-boundary.ps1` only:
   - run each probe as the account with `Start-Process -FilePath "$env:SystemRoot\System32\WindowsPowerShell\v1.0\powershell.exe"
     -Credential $credential -LoadUserProfile -WorkingDirectory <state_dir> -Wait -PassThru` (the account cannot open
     the operator's own current directory -- measured: "The directory name is invalid"), each probe writing its one
     result token to a file in `state_dir` that the verifier then reads and deletes;
   - an inability to START the process as the account (any launch exception, a missing result file, a non-zero exit)
     prints `BOUNDARY: CANNOT-RUN-AS-ACCOUNT <short reason>` and exits 5 -- never `BREACH`;
   - `DENIED-OK` / `BREACH` keep their meanings (probe DENIED and state OK / probe ALLOWED), unchanged.
   Keep every other behaviour. Re-run MS-t-3's AC2 (default config still plans `Opal_Agent`). Commit in the nested repo
   naming NFRA_OPALAI OA-t-2/OA-t-3. **You cannot run the real verifier from your shell** (measured: this harness's
   shell gets "Access is denied" on any run-as-another-user launch); the real AC2 run is Andrew's, in his window, after
   the issuer drains your commit. Then STOP and report.

## 2. BOUNDS

1. One local account and its two directories and ACLs, by the script. `Opal_Agent`, its directories and its credential
   are untouched (AC1 prints its existence beside yours).
2. The credential is DPAPI-protected in the OPERATOR profile, never printed, never committed.
3. No push. REFUSE a criterion you cannot meet as written, with its measurement.

## 3. SURFACES

<paths>
opal_ai/opal/runtime/provision/provision-account.ps1
opal_ai/opal/runtime/provision/verify-boundary.ps1
org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/0.9.0_WK_NFRA_MCPMSP~4/**
org/missions/D6/NFRA/NFRA_MCPMSP/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

Off-repo, on this box: `C:\opal_runtime_msp\` (config, checkout dir, state dir) and the operator profile's
`.opal_runtime\opal_msp_cred.xml`. Read, never write: `opal_ai/opal/runtime/**`, `opal_ai/opal/runtime-msp/**`,
`org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/2.0.0_SA_COO~MS/round1/checks/`. Rows: `INVESTIGATION_v1.Z.md`, id
`NFRA_MCPMSP-Z-W4-S<k>`, `disarm_owner` `2.0.0_SA_COO~MS`.

## 4. PROOF OF SPEC (literal; run from your parent worktree root)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MS-a-3"><invocation>bash org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/2.0.0_SA_COO~MS/round1/checks/a3.AC1.sh; echo "exit=$?"</invocation><expect>exists=True enabled=True admin=0 codex=0 opal_agent_exists=True -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MS-a-3"><invocation>bash org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/2.0.0_SA_COO~MS/round1/checks/a3.AC2.sh; echo "exit=$?"</invocation><expect>verify-boundary (msp config): BOUNDARY: DENIED-OK -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/0.9.0_WK_NFRA_MCPMSP~4/NFRA_MCPMSP.TO-MS-a-3.opal-msp-account.proof_of_spec.json`.
Report once, with: the `-Plan` lines; the two check lines; whether G-ADMIN was needed; any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-1 issuance (CTO msg 26985); WORLD: a device account. Checks dry-run at base: AC1 FAIL as
expected (`exists=False`, `opal_agent_exists=True`); AC2 FAIL as expected (the script is absent at the parent's
opal_ai gitlink). G-ADMIN is Andrew's; G-PUSH for the launch gate is `0.0.0_AB_MSTR~Z`'s.

**AMENDMENT 1 (issuer):** item 0 -- Andrew's elevated run of provision-account.ps1 failed at parameter binding (the
86-character `-Description` literal, pre-existing since OA-t-2; limit 48); nothing was created (measured). The script
path is granted for that one literal. Graded by: no gate limb grades a modification's criteria.

**AMENDMENT 2 (issuer):** item 0b -- `Opal_MSP` provisioned by Andrew (AC1 PASS, issuer's run); AC2's verifier used
WinRM (`Invoke-Command -ComputerName localhost`), not enabled, and mislabelled the launch failure BREACH. It moves to
the launcher's `Start-Process -Credential` route with an explicit CANNOT-RUN-AS-ACCOUNT outcome. The issuer's own
shell measured "Access is denied" on every run-as launch, so AC2's real run is Andrew's. Graded by: no gate limb.

<status>complete</status>
<round>1</round>
<slot>~4</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
