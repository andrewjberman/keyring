# NFRA_OPALAI task order -- `OA-f-4` -- DIRECT ACT, ADDENDUM R2-A2: verify-boundary.ps1 probes as Opal_Agent without WinRM

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_OPALAI/decompositions/NFRA_OPALAI_DECOMP.md</decomp_doc>
<owned_cells>OA-f-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPALAI~19</issued_to>
<issued_by>2.0.0_SA_COO~AI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a script change; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- nothing reaches AWS.
comp-adversary: DECLARED-NOT-APPLICABLE -- AC2 is the adversary arm: an arm that cannot start must never read as DENIED-OK.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OA-f-4` (decomposition ADDENDUM R2-A2; CTO ruling msg 26260)

`opal_ai/opal/runtime/provision/verify-boundary.ps1` proves the Windows account `Opal_Agent`'s boundary with two arms,
run AS that account:
- the PROBE arm: a read of the workspace probe file must be DENIED;
- the CONTROL arm: a write and read of a marker in `state_dir` must succeed.

Today it runs both through `Invoke-Command -ComputerName localhost -Credential` (`:93`, `:98`), which needs the WinRM
service. WinRM is stopped on this machine and will NOT be enabled (CTO ruling: it would add a standing remoting listener
for a one-time check). So both arms error, and the script wrongly prints `BOUNDARY: BREACH`.

Rewrite ONLY the two arms' execution, and keep the semantics:
1. Each arm runs AS `Opal_Agent` with `Start-Process -FilePath powershell.exe -ArgumentList <-NoProfile
   -ExecutionPolicy Bypass -Command ...> -Credential $credential -WorkingDirectory $stateDir -Wait -PassThru
   -WindowStyle Hidden`. `-WorkingDirectory` is REQUIRED: without it the child inherits the operator's current
   directory, which `Opal_Agent` cannot enter, and the start fails ("The directory name is invalid", measured by the
   issuer).
2. Each arm writes its verdict (`DENIED`, `ALLOWED`, `OK`, or `ERROR:<message>`) into its OWN file under `$stateDir`
   (for example `boundary-probe.verdict` and `boundary-control.verdict`). The script deletes any old verdict file
   before starting that arm, and reads the file after `-Wait` returns.
3. **An arm that cannot START, or that leaves no verdict file, is `ERROR`, never `DENIED`.** When either arm is
   `ERROR`, the one output line is `BOUNDARY: ERROR probe=<...> control=<...>` and the exit code is `3`: a NEW code,
   distinct from `0` DENIED-OK, `1` BREACH and `4` NOT-PROVISIONED. Update the synopsis block to list it. `BREACH`
   (exit 1) stays for a probe that is ALLOWED or a control that returns anything but `OK`, when both arms RAN.
4. Add ONE optional parameter, `-CredPath`, whose default is today's path (`$env:USERPROFILE\.opal_runtime\opal_agent_cred.xml`).
   Nothing else in the script's interface changes. It is the test seam AC2 uses.
Change no other file.

**AMENDMENT 1 (CTO ruling msg 26294, after 0.0.0_AB_MSTR~Z's real run at 23:39Z read `BOUNDARY: ERROR` exit 3):** both
children STARTED as Opal_Agent, so the logon works, but each printed its own script text. The ArgumentList element
`"`"$probeCmd`""` wraps the script in literal double quotes, so `-Command` evaluated a quoted STRING. Fix:
5. pass each arm's script with `-EncodedCommand <base64 of the UTF-16LE bytes>`
   (`[Convert]::ToBase64String([Text.Encoding]::Unicode.GetBytes($cmd))`), which has no quoting layer. No `-Command`
   remains in the file;
6. add ONE optional switch, `-SelfTestAsCurrentUser`: the arms go through the SAME Start-Process + `-EncodedCommand`
   path but WITHOUT `-Credential`, as the current user. It is the test seam AC3 uses to prove each arm RUNS and writes
   its verdict file. The default (no switch) always runs as Opal_Agent. The ERROR-never-DENIED-OK semantics are
   unchanged.

## 2. BOUNDS

1. **`opal_ai` is a nested repository** at `<worktree>/opal_ai`, on its own branch off `opal_ai` `fd8ab8a57f`. Commit
   with `git -C opal_ai commit --author "0.9.0_WK_NFRA_OPALAI~19 <0.9.0_WK_NFRA_OPALAI~19@opal.agent>" -F <msgfile> --
   opal/runtime/provision/verify-boundary.ps1`, the msgfile written with the Write tool.
2. Never enable WinRM, never elevate, and never log on as `Opal_Agent` yourself. The account exists and its credential
   file is real, but the REAL run is `0.0.0_AB_MSTR~Z`'s (G-ACCT step 3). AC2 runs only with a credential for a
   NON-EXISTENT user.
3. Standing: no push, no install, no vendor call. REFUSE a criterion you cannot meet as written, and report the refusal
   with its measurement. Never repair a criterion, widen it, or meet it by a route this face does not name.

## 3. SURFACES

<paths>
opal_ai/opal/runtime/provision/verify-boundary.ps1
org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~19/**
org/missions/D6/NFRA/NFRA_OPALAI/surprise-channel/investigations/**
</paths>

Rows: `org/missions/D6/NFRA/NFRA_OPALAI/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, id
`NFRA_OPALAI-Z-W19-S<k>` (none exist at the cut; the first is S1).

## 4. PROOF OF SPEC (literal; run from your worktree root, after the nested commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OA-f-4"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~AI/round2/checks/f4.AC1.sh; echo "exit=$?"</invocation><expect>Invoke-Command/ComputerName=0; Start-Process with -Credential -Wait -WorkingDirectory>=2; parse errors=0; other files changed vs fd8ab8a57f=0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OA-f-4"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~AI/round2/checks/f4.AC2.sh; echo "exit=$?"</invocation><expect>rc=3 line='BOUNDARY: ERROR probe=... control=...' -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OA-f-4"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~AI/round2/checks/f4.AC3.sh; echo "exit=$?"</invocation><expect>-EncodedCommand refs>=1 -Command refs=0; rc=1 line='BOUNDARY: BREACH probe=ALLOWED control=OK'; verdict files>=2 -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~19/NFRA_OPALAI.TO-OA-f-4.verify-boundary-without-winrm.proof_of_spec.json`.
Report once: the diff of the script (the changed region), the nested commit hash, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** a direct act, outside round 2's issuance (it carries no `<round>`, the R2-A1 precedent), on
`1.0.0_SA_CTO~O`'s ruling msg 26260 (file `deliverables/1.0.0_SA_CTO~O/RULING_G-ACCT_STEP3_NO_WINRM_20260928.md`).
`0.0.0_AB_MSTR~Z` then re-runs G-ACCT step 3 from a scratch copy whose diff against PROD fd8ab8a equals OA-f-3's line
plus this order's change, and continues to steps 4-6. It reaches PROD in the cutover G-PUSH.

**Measured by the issuer at the cut (this session's tool sandbox):**
- `Start-Process -Credential` as Opal_Agent WITHOUT `-WorkingDirectory` fails with "The directory name is invalid".
- WITH it, it fails "Access is denied" in 3 of 3 variants.
- `BUILTIN\Users` contains `NT AUTHORITY\Authenticated Users` and `INTERACTIVE`, so group membership is not the
  obvious cause. A sandbox-originated logon is not evidence about the real account, so the real arm is MSTR~Z's run.

SPAWN ONLY WHEN: at the cut. Slot `~19`, nested worktree `--nested opal_ai=fd8ab8a57f`.

Dry-run at base (opal_ai fd8ab8a57f):
- f4.AC1 base: FAIL as expected (`Invoke-Command/ComputerName=2; Start-Process with -Credential -Wait -WorkingDirectory=0`).
- f4.AC2 base: FAIL as expected (`rc=1 line='none'`: no `-CredPath` parameter, so no BOUNDARY line).

f4.AC3 (amendment 1) base: FAIL as expected at fd8ab8a57f and at the defective 6b13ff892f (`-EncodedCommand refs=0`,
no BOUNDARY line, 0 verdict files). Gate limb: to-pipeline-gate grades a MODIFIED order only on GATE (viii)
placeholders (NONE), so no limb graded this amendment.

<status>complete</status>
<direct_act>true</direct_act>
<slot>~19</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
