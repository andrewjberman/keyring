# NFRA_OPALAI task order -- `OA-f-9` -- DIRECT ACT, ADDENDUM R2-A7: the launcher starts a usable Analyst (Process.Start, refs readable, its config set) and jq is provisioned

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_OPALAI/decompositions/NFRA_OPALAI_DECOMP.md</decomp_doc>
<owned_cells>OA-f-9</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPALAI~24</issued_to>
<issued_by>2.0.0_SA_COO~AI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- script changes; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- nothing reaches AWS.
comp-adversary: DECLARED-NOT-APPLICABLE -- AC2's no-jq arm and AC3's refs-write arms are the adversary read.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OA-f-9` (decomposition ADDENDUM R2-A7)

The runtime account `Opal_Agent` runs the Teams Analyst (Claude Code) from a read-only checkout of `opal_ai`. The
operator starts it with `opal_ai/opal/runtime/launcher.ps1 -Config <runtime.config.json>`: fetch, then the launch gate
`launch-gate.ps1` AS Opal_Agent, then Claude Code AS Opal_Agent in `checkout_dir\opal\runtime`. On 2026-09-30 the
operator measured four defects in that launcher and its provisioning:
- `Start-Process -Credential` gives an Opal_Agent window that shows output but never takes keyboard input, at High and
  at Medium integrity. .NET `[System.Diagnostics.Process]::Start(<ProcessStartInfo>)` from a Medium-integrity
  (non-elevated) operator shell gives a window that does take typing. The command line through that API is capped at
  1024 characters.
- Under `$ErrorActionPreference = 'Stop'`, git's progress lines on stderr (`2>&1`) abort the fetch.
- The fence `opal_ai/opal/agent/hooks/concierge-gate.sh` finds `jq` on PATH only (`:35-45`) and otherwise denies every
  call. Nothing provisions jq for Opal_Agent.
- The Analyst's working directory is `opal/runtime`, so it cannot read its operating references in
  `opal/agent/refs/`. Also, nothing sets `OPAL_RUNTIME_CONFIG`, so the fence's G1 denies every write, including the
  thread memory it must write under `state_dir`.

Your nested base is the local round-2 DEV (`nfra-opalai-r2-dev`, `0a5c7c2`). Build there:

1. **`opal_ai/opal/runtime/launcher.ps1`.** Keep its three steps and every existing refusal. Change it as follows.
   - **First, before reading the config:** when the current token is elevated
     (`([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)`),
     print `LAUNCHER: REFUSE ELEVATED -- run the launcher from a non-elevated operator shell; the only measured typeable
     Analyst window comes from a Medium-integrity parent.` and `exit 6`.
   - Resolve `-Config` to its full path once, so the children get an absolute path.
   - **Fetch and merge:** set `$ErrorActionPreference = 'Continue'` around each git call and restore `'Stop'` after it.
     Judge each call by its `$LASTEXITCODE`, and keep the existing REFUSE lines.
   - **No `Start-Process -Credential` anywhere.** Write one helper that builds a
     `System.Diagnostics.ProcessStartInfo` from the stored credential:
     - `UserName`; `Domain` = the credential's domain, or `$env:COMPUTERNAME` when blank (split `DOMAIN\user` when
       present); `Password` = the SecureString;
     - `LoadUserProfile = $true`, `UseShellExecute = $false`, and the `WorkingDirectory` passed in.

     The helper never reads or sets `.EnvironmentVariables`: reading that property copies the OPERATOR's environment
     into the child. Start both children with `[System.Diagnostics.Process]::Start($psi)`.
   - **The gate:** FileName `powershell.exe`, Arguments `-NoProfile -ExecutionPolicy Bypass -File "<launch-gate.ps1>"
     -Config "<config>"`, WorkingDirectory `state_dir`. Set `RedirectStandardOutput = $true`,
     `RedirectStandardError = $true` and `CreateNoWindow = $true`. Read both streams to their end, `WaitForExit()`, then
     take `ExitCode`. The gate's output comes back on this pipe; no temp file. When the start throws, print `LAUNCHER:
     REFUSE GATE-NOT-STARTED -- <message>` and `exit 1`.
   - **The Analyst** (after `GATE: PASS` and the existing `resolve-claude.ps1` step, which stays as it is):
     - **refs path:** `$refsDir` = the full path of `Join-Path $runtimeDir '..\agent\refs'`. It is derived from the
       config's `checkout_dir` and never typed. When it does not exist, print `LAUNCHER: REFUSE REFS-MISSING` and
       `exit 1`.
     - **process:** FileName `powershell.exe`, WorkingDirectory `$runtimeDir`, no redirection, and Arguments
       `-NoExit -ExecutionPolicy Bypass -Command "$host.UI.RawUI.WindowTitle = 'Opal_Agent Analyst';
       $env:OPAL_RUNTIME_CONFIG = '<config full path>'; & '<claude exe>' --add-dir '<refsDir>'"`.
     - **refusals:** when any of the three values contains a `'`, or the Arguments string is longer than 1000
       characters, print `LAUNCHER: REFUSE ARGLEN` and `exit 1`.
     - **report:** on start, print `OK: Analyst window started, pid <id>`.
   - Type no drive-letter path anywhere.
2. **`opal_ai/opal/agent/hooks/concierge-gate.sh`, the jq lookup only (`:35-45`).** Use `jq` from PATH; else
   `$HOME/.local/bin/jq.exe`, then `$HOME/.local/bin/jq`, the first that is executable. That folder is the runtime
   account's own profile, where Claude Code's installer also puts `claude.exe`; it is not a workspace file. With none
   of the three, keep the fail-closed deny and its `jq not found` wording, naming both places. Update header item 3 to
   match. Change nothing else in the fence.
3. **`opal_ai/opal/runtime/provision/provision-account.ps1`: an optional config key `jq_exe`** (a `jq.exe` the
   operator supplies).
   - When it is set, `-Plan` prints ONE more line, `PLAN: JQ <jq_exe> -> <account> profile .local\bin\jq.exe`.
   - Also when it is set, the real (elevated) mode copies that file to `<Opal_Agent's profile>\.local\bin\jq.exe`,
     creating the folder. The profile is the `LocalPath` of the `Win32_UserProfile` whose SID is the account's. When
     the account has no profile yet, it prints `WARN: JQ-DEFERRED -- <account> has no profile yet; re-run after its
     first logon` and continues.
   - When the key is absent, nothing changes: the same 10 `PLAN:` lines.
   - Update the header's line count and add the key to the `.PARAMETER Config` text.
4. **`opal_ai/opal/runtime/provision/runtime.config.example.json`** gains `"jq_exe": "<path to jq.exe to install for
   the runtime account, optional>"`.
5. You MAY add a case to `opal_ai/opal/agent/hooks/test_concierge_gate.sh` for the `$HOME/.local/bin` lookup. Change no
   other file.

## 2. BOUNDS

1. **`opal_ai` is a nested repository** at `<worktree>/opal_ai`, on its own branch off `0a5c7c2`. Commit with
   `git -C opal_ai commit --author "0.9.0_WK_NFRA_OPALAI~24 <0.9.0_WK_NFRA_OPALAI~24@opal.agent>" -F <msgfile> --
   <nested paths>`, the msgfile written with the Write tool. The parent `opal_ai` gitlink is NOT yours.
2. Never run the launcher or the provisioning script with a real config. Never elevate, never log on or start a process
   as `Opal_Agent`, and never edit anything under `C:\opal_runtime` or `C:\Users\Opal_Agent`. AC1 runs the launcher
   with a MISSING config, and AC2 runs provisioning in `-Plan` only. The live run is the close run's, not yours.
3. Standing: no push, no install, no vendor call. REFUSE a criterion you cannot meet as written, and report the refusal
   with its measurement. Never repair a criterion, widen it, or meet it by a route this face does not name.

## 3. SURFACES

<paths>
opal_ai/opal/runtime/launcher.ps1
opal_ai/opal/agent/hooks/concierge-gate.sh
opal_ai/opal/agent/hooks/test_concierge_gate.sh
opal_ai/opal/runtime/provision/provision-account.ps1
opal_ai/opal/runtime/provision/runtime.config.example.json
org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~24/**
org/missions/D6/NFRA/NFRA_OPALAI/surprise-channel/investigations/**
</paths>

Read-only reference: `opal_ai/opal/runtime/resolve-claude.ps1` and `opal_ai/opal/runtime/launch-gate.ps1` (both
unchanged). Rows: `org/missions/D6/NFRA/NFRA_OPALAI/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, id
`NFRA_OPALAI-Z-W24-S<k>` (none exist at the cut; the first is S1).

## 4. PROOF OF SPEC (literal; run from your worktree root, after the nested commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OA-f-9"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~AI/round2/checks/f9.AC1.sh; echo "exit=$?"</invocation><expect>Start-Process -Credential=0; Process.Start>=2; temp-file=0; stdout-pipe>=1; --add-dir>=1; agent\refs>=1; OPAL_RUNTIME_CONFIG>=1; REFUSE ELEVATED>=1; .EnvironmentVariables=0; drive-letter literals=0; parse errors=0; behaviour 'LAUNCHER: REFUSE ELEVATED' rc=6 when elevated=True, else 'ERROR: config not found' rc=2; other files changed vs 0a5c7c2=0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OA-f-9"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~AI/round2/checks/f9.AC2.sh; echo "exit=$?"</invocation><expect>arm1 HOME jq -> deny lines=0; arm2 no jq -> 'jq not found' lines>=1; arm3 PLAN: JQ lines=1 naming jq_exe=1; arm4 PLAN: JQ lines=0, PLAN lines=10 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OA-f-9"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~AI/round2/checks/f9.AC3.sh; echo "exit=$?"</invocation><expect>arm1 refs Write G1-deny=1; arm2 refs Edit G1-deny=1; arm3 state_dir Write deny=0 -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~24/NFRA_OPALAI.TO-OA-f-9.launcher-process-start-refs-jq.proof_of_spec.json`.
Report once: the launcher's changed regions, the fence's jq lookup, the provisioning jq step, the nested commit hash,
and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** a direct act cut by the issuer inside its own decomposition (`/canonical-drive` obligation 7). Two inputs:
- row `NFRA_OPALAI-Z-S50` (surfaced by `1.0.0_SA_CTO~O`; G-ACCT step 6 defects 5 and 6, plus defect 1 from the
  handoff list), with operator launcher v2's measured pattern (`launch-v2.ps1`, operator-local, outside the repo);
- `CTO_RULING_20261001_NFRA_OPALAI_ANALYST_REFS_READ.md` @2b8f3151c6, which `1.0.0_SA_CTO~O` ordered cut "in the
  same order as the Z-S50 launcher fix" (msg 27482).

No `<round>` (the R2-A1 precedent).

Three issuer choices, each recorded here:
- **The refs path is derived from the config's `checkout_dir`** (`$runtimeDir\..\agent\refs`), not from
  `$PSScriptRoot`. The two are equal when the launcher runs from the checkout, which is the cutover run. Run from
  anywhere else, `$PSScriptRoot` would hand the Analyst refs from outside the launch gate's clean-at-PROD check. This
  keeps the ruling's substance: derived, never typed, exactly `agent/refs`.
- **An elevated parent is REFUSED, not re-launched through explorer** as v2 does. The product launcher takes `-Config`,
  and `explorer.exe <file>.cmd` cannot carry an argument. Refusing is the minimum fail-closed form of the row's
  "Medium-integrity parent".
- **The jq lookup gains `$HOME/.local/bin`** instead of provisioning editing Opal_Agent's registry PATH (a hive load,
  untestable without elevation). It stays inside the fence's design rule: the runtime account's own profile, no
  workspace file.

Added from the measurement: nothing sets `OPAL_RUNTIME_CONFIG` for the Analyst (`git grep` at 0a5c7c2: only
teams-watch.py reads it; the operator's User/Machine env is empty). Without it G1 denies every write, including
thread memory under `state_dir`, which the ruling's item 2 relies on. The launcher now sets it inside the child's own
command, which keeps the "no operator environment" rule.

The ruling's three acceptance clauses map as follows:
- **NEGATIVE (write):** this order's AC3.
- **POSITIVE (the Analyst reads `refs/TEAMS_DUTY.md` and passes launch step 2):** the close run's live launch.
- **NEGATIVE (scope: a Read of `agent/hooks/concierge-gate.sh` is refused or prompted):** also the close run's live
  launch, after the r2-dev line reaches `opal_ai` PROD at the cutover (G-PUSH, `0.0.0_AB_MSTR~Z` on Andrew's word).

SPAWN ONLY WHEN: at the cut. Slot `~24`, nested worktree `--nested opal_ai=0a5c7c2`.

Dry-run at base (main tree, `OA_F9_REF=0a5c7c2`):
- f9.AC1 base: FAIL as expected (`Start-Process -Credential=2; Process.Start=0; temp-file=1; --add-dir=0;
  OPAL_RUNTIME_CONFIG=0; REFUSE ELEVATED=0`; behaviour `ERROR: config not found` rc=2, token not elevated).
- f9.AC2 base: FAIL as expected (`arm1 HOME jq -> deny lines=1`; arm2 deny 1; `PLAN: JQ lines=0`; arm4 PLAN lines=10).
- f9.AC3 base: PASS as expected (control: refs Write and Edit G1-denied, state_dir Write allowed).

<status>pending</status>
<direct_act>true</direct_act>
<slot>~24</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
