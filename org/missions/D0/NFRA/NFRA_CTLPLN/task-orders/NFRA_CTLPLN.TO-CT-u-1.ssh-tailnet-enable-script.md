# TO NFRA_CTLPLN.TO-CT-u-1 -- workstream REMOTE CT-u-1: the one script that turns on key-only SSH over the tailnet on a Windows box

<to_id>NFRA_CTLPLN.TO-CT-u-1</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~61</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-12</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>REMOTE</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-u-1` (`decompositions/NFRA_CTLPLN_DECOMP.remote1.md`) | **outcome_ref:** FWD-27 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

FWD-27: every box on the tailnet answers an SSH login from the laptop by key, and nothing else. The setup needs an ELEVATED
PowerShell on each box; no agent session is elevated and none can answer a UAC prompt. So a person (Andrew) runs ONE line per box in an
elevated PowerShell, and this cell builds the script that line runs. The script must be safe to run twice, must show what it changed,
and must be able to undo itself. You build the script and prove it WITHOUT elevation, using its `-Plan` and `-SelfTest` modes. You do
not enable anything on any machine.

### BUILD

One file: `.tools/ssh-tailnet-enable.ps1` (Windows PowerShell 5.1 compatible; ASCII only). Parameters:
`-PublicKey <path-or-string>` (repeatable as an array), `-Plan`, `-Rollback`, `-SelfTest`, `-ReceiptDir <path>` (default below).

What a real (elevated, not `-Plan`) run does, in order, each step idempotent:
1. **A. Service.** If the capability `OpenSSH.Server~~~~0.0.1.0` is not installed, `Add-WindowsCapability -Online -Name 'OpenSSH.Server~~~~0.0.1.0'`.
   `Set-Service -Name sshd -StartupType Automatic; Start-Service sshd`.
2. **B. Firewall.** Disable the rule `OpenSSH SSH Server (sshd)` if it exists. Ensure exactly one inbound rule named
   `OpenSSH Server (Tailscale only)`: `-Direction Inbound -Protocol TCP -LocalPort 22 -Action Allow -RemoteAddress 100.64.0.0/10 -Profile Any`.
   If it exists, `Set-NetFirewallRule` its `-RemoteAddress` to `100.64.0.0/10` (the laptop's existing rule carries `Any` and must be fixed).
3. **C. Default shell.** `HKLM:\SOFTWARE\OpenSSH` value `DefaultShell` = `$env:SystemRoot\System32\WindowsPowerShell\v1.0\powershell.exe`.
4. **D. Keys.** Write each `-PublicKey` line to `$env:ProgramData\ssh\administrators_authorized_keys` (append only the lines not already
   present), then set the ACL to SYSTEM and Administrators only (`icacls ... /inheritance:r /grant "SYSTEM:F" /grant "Administrators:F"`).
   Then `Restart-Service sshd`.
5. **Password authentication.** The script NEVER turns `PasswordAuthentication` off in the same run that first installs a key. It sets
   `PasswordAuthentication no` in `$env:ProgramData\ssh\sshd_config` ONLY when the key file already holds at least one key line BEFORE
   this run started AND the caller passes `-DisablePassword`. With no key present it REFUSES (prints `REFUSED: no key present, password auth left on`,
   exits 2). A box with no key and no password is unreachable; that is the failure this rule prevents.
6. **Receipt.** Writes `<ReceiptDir>/ssh_enable_<UTC stamp>.json`. Default `ReceiptDir` = `org/devices/state/<device>/` under the repo
   root, where `<device>` is `$env:AGENTBUS_DEVICE` (refuse with `REFUSED: AGENTBUS_DEVICE unset` if empty). The receipt holds
   BEFORE and AFTER of: the sshd service (status, start type), the two firewall rules (enabled, remote address), the key file (exists,
   line count, ACL), the password-auth setting; the list of steps that CHANGED something; the mode; and the rollback block (below).
   Never print or store a key's body: store only each key's type, comment and SHA256 fingerprint.
   The receipt is written with `ConvertTo-Json -Compress` (no spaces after `:` or `,`) and has these exact top-level keys: `"mode"`
   (`plan`, `apply` or `rollback`), `"device"`, `"utc"`, `"before"`, `"after"`, `"changed_steps"`, `"rollback"`; and `"before"` / `"after"` each
   hold these exact keys: `"sshd_status"`, `"sshd_start_type"`, `"tailnet_rule_remote_address"` (the remote address of the rule
   `OpenSSH Server (Tailscale only)`, or `absent`), `"default_rule_enabled"` (true or false), `"key_lines"` (a count), `"password_auth"`
   (`yes`, `no` or `default`). In `-Plan` mode `"after"` holds the values the real run WOULD leave.

`-Plan`: runs the same reads, prints BEFORE and what each step WOULD change, writes the receipt with `"mode":"plan"` and also prints the receipt as one
compact JSON line on stdout (compact form, so the text `"mode":"plan"` appears with no space), changes nothing, and runs UNELEVATED. It must not call any mutating cmdlet.
`-Rollback`: `Stop-Service sshd; Set-Service sshd -StartupType Disabled; Remove-NetFirewallRule -DisplayName 'OpenSSH Server (Tailscale only)'`
and nothing else. The same block is printed by every run.
`-SelfTest`: no admin needed, no machine change. Parses the file with the PowerShell parser (no parse errors), and runs these cases
against fakes (functions it can swap for the real cmdlets by a `$script:Backend` table): (1) `-Plan` calls zero mutating cmdlets;
(2) a run with no key and `-DisablePassword` is REFUSED and `PasswordAuthentication` is untouched; (3) a second run changes nothing
(idempotent); (4) the firewall step rewrites a rule whose remote address is `Any` to `100.64.0.0/10`; (5) `AGENTBUS_DEVICE` unset
refuses; (6) no key body appears in the receipt. LAST line: `SSH-ENABLE-SELFTEST cases=<k>/<n> ok=<True|False>`.

### RULES FOR THIS CELL

**Nothing you run changes this or any machine.** You do not run the script without `-Plan` or `-SelfTest`. You call no `Add-WindowsCapability`,
`Set-Service`, `New-NetFirewallRule`, `Set-NetFirewallRule`, `Remove-NetFirewallRule` or registry write outside the fake backend. You do
not edit `sshd_config`, `administrators_authorized_keys` or any firewall rule on the real machine. You send nothing on the agent bus
and push nothing. No box name, serial of a box, user name or path under a user's home is typed into the file: the device comes from
`AGENTBUS_DEVICE`, the repo root from `git rev-parse --show-toplevel`. No non-ASCII character in any file you write. The law files
`CLAUDE.md` and `org/XXX.md` are LOCKED. No alert, monitor or timeout is built.
FOUND SOMETHING ODD OFF-TASK? Append ONE row (`spec_asserts` + `world_is`) to
`org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (id `NFRA_CTLPLN-W61-S<k>`) and keep working.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTu1-AC1" cell_refs="CT-u-1"><invocation>powershell -NoProfile -ExecutionPolicy Bypass -File .tools/ssh-tailnet-enable.ps1 -SelfTest</invocation><expect>SSH-ENABLE-SELFTEST cases=</expect></criterion>
`CTu1-AC1` -- every case passing; the line reads `ok=True`.

<criterion id="CTu1-AC2" cell_refs="CT-u-1"><invocation>powershell -NoProfile -ExecutionPolicy Bypass -File .tools/ssh-tailnet-enable.ps1 -Plan -ReceiptDir $env:TEMP</invocation><expect>"mode":"plan"</expect></criterion>
`CTu1-AC2` -- a real `-Plan` on this unelevated machine prints BEFORE, lists the steps it would change, and writes a receipt; it changes nothing.
</proof_of_spec>

<expected_criteria>CTu1-AC1,CTu1-AC2</expected_criteria>

Each invocation runs from the worktree root under `timeout 120`. Write the proof instance to
`org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~61/NFRA_CTLPLN.TO-CT-u-1.ssh-tailnet-enable-script.proof_of_spec.json`, validate it with
`python .tools/proof-of-spec-check.py <instance> CTu1-AC1,CTu1-AC2`, and flip `<status>` to `complete` only when every mechanical criterion
passes and the instance is VALID. Your queue then continues with `CT-u-2` (the issuer hands it to you).

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.remote1.md</decomp_doc>
<owned_cells>CT-u-1</owned_cells>
</decomp_ref>

<paths>
.tools/ssh-tailnet-enable.ps1
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE the script is not run elevated by this cell and makes no AWS call.
comp-adversary: RUN -- password auth switched off before a key exists (REFUSED, case 2); a second run changing state (case 3); a rule named for the tailnet but admitting Any (case 4, the laptop's measured rule); a key body leaking into the receipt (case 6); a worker running the mutating path on a real machine (the rules forbid it and `-Plan` is the only real run); BLIND: what a real elevated run does on a box with a different OpenSSH build.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: PRD `prd/NFRA_CTLPLN_PRD.md` v0.23 FWD-27; plan `org/tier1_exec/1.0.0_SA_CTO/deliverables/LD0644_ROLLOUT_PLAN_CLUSTER_REMOTE_ACCESS_TAILNET_20261011.md` sections 3 and 7;
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261012_015xZ_SSH_OVER_TAILNET_EXECUTE_COO_C.md` (CTO msg 108406).
