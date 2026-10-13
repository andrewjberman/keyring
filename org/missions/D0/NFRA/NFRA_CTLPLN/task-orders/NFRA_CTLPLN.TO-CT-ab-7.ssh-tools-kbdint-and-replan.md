# TO NFRA_CTLPLN.TO-CT-ab-7 -- workstream SSHTOOLS round 1 (cell CT-ab-7): the SSH read grades a password path only when one exists, uses the right key, and the enable script disables the default rule a fresh install creates (FWD-27)

<to_id>NFRA_CTLPLN.TO-CT-ab-7</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~80</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-13</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>SSHTOOLS</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-ab-7` (`decompositions/NFRA_CTLPLN_DECOMP.round12.md`) | **outcome_ref:** FWD-27 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

MEASURED 2026-10-13 14:51Z from the laptop, after Andrew's `-DisablePassword` runs: every box advertises `publickey,keyboard-interactive`; a keyboard-interactive attempt (`ssh -vv -o PreferredAuthentications=keyboard-interactive`) gets NO prompt from the server (no `info_req`; the server answers `Permission denied` at once), so no password path exists. But `.tools/ssh-tailnet-verify.py` lists `PASSWORD_METHODS = ("password", "keyboard-interactive")` (about :61) and `password_verdict` (about :145-158) reads ADVERTISED whenever either name is listed, so every box reads not done. Second: the tool calls a bare `ssh` (about :161) with no `-i`; Git Bash's ssh reads `/home/<user>/.ssh`, not `%USERPROFILE%\.ssh`, where the laptop's key `id_ed25519` lives, so a key login from the laptop reads DENIED although it works with `-i` (measured: sitez `Opal_Bloomberg`, dell1 `DESKTOP-HK1UU7N`, dell2 `DESKTOP-N8RJV0A` answer with `-i %USERPROFILE%\.ssh\id_ed25519 -o IdentitiesOnly=yes`). Third, `.tools/ssh-tailnet-enable.ps1` builds its plan once from the BEFORE read (`Get-Observed` about :357/:578, `New-Plan` :397 called :607); step A installs OpenSSH Server (`Do.AddCapability`, :420), which CREATES the default rule `OpenSSH SSH Server (sshd)` (Private, remote Any, port 22); step B disables that rule only if it was observed enabled (:434-437), so on a fresh install it stays ENABLED (msg 108698, seen on dell1 and dell2). Apply never re-plans (:634-645); the self-test's fake install (:214) creates no rule and `New-Fake` starts with the rule present (:247, :253), so the self-test misses it.

### BUILD

1. `ssh-tailnet-verify.py`: the password arm probes `password` and `keyboard-interactive` separately. `password` listed -> ADVERTISED. `keyboard-interactive` listed -> drive one keyboard-interactive attempt non-interactively and grade by whether the server sent a prompt (an `info_req` / prompt in `-vv` output): a prompt -> ADVERTISED; no prompt -> `KBDINT-NO-PROMPT`, which counts as refused. Print the method list and the verdict on each box line.
2. `ssh-tailnet-verify.py`: a `--identity <path>` option (default: `%USERPROFILE%\.ssh\id_ed25519` when it exists, resolved with `os.path.expanduser`/`USERPROFILE`, not the MSYS home), passed as `-i <path> -o IdentitiesOnly=yes` to the key-login probe. A per-box user map: `--user-for <box>=<user>` (repeatable), so one run can read sitez as `Opal Bloomberg`, dell1/dell2 as `Test`, and the laptop with its own user; a user with a space is passed with `-l`.
3. `ssh-tailnet-enable.ps1`: after step A installs the capability, re-read the observed state and re-plan before step B, so a default rule the install created is disabled; the receipt records `default_rule_enabled` AFTER. Fix the self-test's fake install to create the default rule ENABLED, and add a self-test case: from not-installed, apply leaves the default rule disabled.
4. Add self-test cases to `ssh-tailnet-verify.py --selftest` (stub ssh): keyboard-interactive with no prompt reads refused; keyboard-interactive with a prompt reads ADVERTISED; `--identity` reaches the argv; `--user-for` with a space reaches `-l`.

### RULES FOR THIS CELL

Write surface = the `<paths>`. Never run the enable script for real (self-test only; it needs elevation and changes a box); no real SSH login attempt beyond what the self-tests stub; no aws, no push. `.tools/safe-commit.sh` for every commit. Do NOT commit the `portal` gitlink. ASCII only; Python 3.11 standard library; Windows PowerShell 5.1 syntax. CLAUDE.md and org/XXX.md are LOCKED. FOUND SOMETHING ODD OFF-TASK? Append ONE row to `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (id `NFRA_CTLPLN-W80-S<k>`, `surfaced_at` = `date -u +%FT%TZ`) and keep working.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTab7-AC1" cell_refs="CT-ab-7"><invocation>python .tools/ssh-tailnet-verify.py --selftest</invocation><expect>SSH-VERIFY-SELFTEST cases=12/12 ok=True</expect></criterion>
`CTab7-AC1` -- the old 8 cases and EXACTLY the four new cases of BUILD 4 pass (base: `cases=8/8`).

<criterion id="CTab7-AC2" cell_refs="CT-ab-7"><invocation>powershell -NoProfile -ExecutionPolicy Bypass -File .tools/ssh-tailnet-enable.ps1 -SelfTest</invocation><expect>SSH-ENABLE-SELFTEST cases=7/7 ok=True</expect></criterion>
`CTab7-AC2` -- the old 6 cases and EXACTLY the one new fresh-install case of BUILD 3 pass (base: `cases=6/6`).
</proof_of_spec>

<expected_criteria>CTab7-AC1,CTab7-AC2</expected_criteria>

Each invocation runs from the worktree root under `timeout 120`; record the criterion text as the invocation. Write the proof instance to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~80/NFRA_CTLPLN.TO-CT-ab-7.ssh-tools-kbdint-and-replan.proof_of_spec.json`, validate it with `python .tools/proof-of-spec-check.py <instance> CTab7-AC1,CTab7-AC2`, flip `<status>` to `complete` only when both pass and the instance is VALID (if refused as outside your grant, leave it `pending` and say so). Report the last line of the enable self-test at the base too (before your edit).

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round12.md</decomp_doc>
<owned_cells>CT-ab-7</owned_cells>
</decomp_ref>

<paths>
.tools/ssh-tailnet-verify.py
.tools/ssh-tailnet-enable.ps1
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call.
comp-adversary: RUN -- a real keyboard-interactive password prompt read as refused (the prompt case reads ADVERTISED); a re-plan that disables the tailnet rule instead of the default one (the fresh-install case checks both rules); a self-test that touches the real box (fakes only); BLIND: a server that prompts only for an existing user (the live read uses each box's real user).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: COO~C measurements 2026-10-13 14:4xZ-14:5xZ; MSTR msg 108698.
