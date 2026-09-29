# NFRA_OPALAI task order -- `OA-f-8` -- DIRECT ACT, ADDENDUM R2-A6: the launcher starts Claude Code from a resolved path, not a bare name

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_OPALAI/decompositions/NFRA_OPALAI_DECOMP.md</decomp_doc>
<owned_cells>OA-f-8</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPALAI~23</issued_to>
<issued_by>2.0.0_SA_COO~AI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a script change; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- nothing reaches AWS.
comp-adversary: DECLARED-NOT-APPLICABLE -- AC1's two refusal arms are the adversary read.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OA-f-8` (decomposition ADDENDUM R2-A6)

`opal_ai/opal/runtime/launcher.ps1` is run by the operator. After the launch gate passes, it starts Claude Code AS the
account `Opal_Agent` with `Start-Process -FilePath 'claude.exe' ...` (`:107`, a bare name). G-ACCT step 4
(`0.0.0_AB_MSTR~Z`, 2026-09-29) installed Claude Code for `Opal_Agent` at `C:\Users\Opal_Agent\.local\bin\claude.exe`,
and the installer reported that folder is NOT on `Opal_Agent`'s PATH. So the bare name fails at step 6.

Your nested base is the local round-2 DEV (`nfra-opalai-r2-dev`, `dcececf53c`). There:
1. NEW `opal_ai/opal/runtime/resolve-claude.ps1 -Config <json>`: prints ONE line and exits.
   - `CLAUDE_EXE: <path>`, exit 0, when the config's OPTIONAL key `claude_exe` names an existing file; otherwise when
     `claude.exe` resolves on PATH (`Get-Command`).
   - Else `LAUNCHER: REFUSE CLAUDE-NOT-FOUND -- set claude_exe in the runtime config to the Claude Code install for the
     runtime account`, exit 5.
   - It reads only the config and PATH. No device path is baked in; the operator's config carries the install path.
2. `launcher.ps1` calls it (resolved beside the launcher via `$PSScriptRoot`), refuses with its line and a non-zero exit
   when it refuses, and passes the resolved path to the `Start-Process` that starts Claude Code. No bare `'claude.exe'`
   literal remains in any `Start-Process`. Nothing else in the launcher changes.
3. `opal_ai/opal/runtime/provision/runtime.config.example.json` gains the optional key `claude_exe`, with a placeholder
   value and nothing machine-specific.
Change no other file.

## 2. BOUNDS

1. **`opal_ai` is a nested repository** at `<worktree>/opal_ai`, on its own branch off `dcececf53c`. Commit with
   `git -C opal_ai commit --author "0.9.0_WK_NFRA_OPALAI~23 <0.9.0_WK_NFRA_OPALAI~23@opal.agent>" -F <msgfile> --
   <nested paths>`, the msgfile written with the Write tool. The parent `opal_ai` gitlink is NOT yours.
2. Never run the launcher, never elevate, never log on as `Opal_Agent`, and never edit `C:\opal_runtime\runtime.config.json`.
   The live run is G-ACCT step 6, `0.0.0_AB_MSTR~Z`'s.
3. Standing: no push, no install, no vendor call. REFUSE a criterion you cannot meet as written, and report the refusal
   with its measurement. Never repair a criterion, widen it, or meet it by a route this face does not name.

## 3. SURFACES

<paths>
opal_ai/opal/runtime/resolve-claude.ps1
opal_ai/opal/runtime/launcher.ps1
opal_ai/opal/runtime/provision/runtime.config.example.json
org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~23/**
org/missions/D6/NFRA/NFRA_OPALAI/surprise-channel/investigations/**
</paths>

Rows: `org/missions/D6/NFRA/NFRA_OPALAI/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, id
`NFRA_OPALAI-Z-W23-S<k>` (none exist at the cut; the first is S1).

## 4. PROOF OF SPEC (literal; run from your worktree root, after the nested commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OA-f-8"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~AI/round2/checks/f8.AC1.sh; echo "exit=$?"</invocation><expect>arm1='CLAUDE_EXE: ...fake-claude.exe' rc=0; arm2='LAUNCHER: REFUSE CLAUDE-NOT-FOUND ...' rc=5; arm3='LAUNCHER: REFUSE CLAUDE-NOT-FOUND ...' -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OA-f-8"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~AI/round2/checks/f8.AC2.sh; echo "exit=$?"</invocation><expect>launcher calls resolve-claude>=1; bare 'claude.exe' in Start-Process=0; example names claude_exe>=1; parse-clean scripts=2 of 2; other files changed vs dcececf53c=0 -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~23/NFRA_OPALAI.TO-OA-f-8.launcher-resolves-claude-exe.proof_of_spec.json`.
Report once: the resolver in full, the launcher's changed region, the nested commit hash, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** a direct act ruled by the issuer inside its own decomposition (`/canonical-drive` obligation 7), on
`0.0.0_AB_MSTR~Z`'s G-ACCT report (msg 20260929T021622Z): the Claude Code install is off Opal_Agent's PATH, and
`launcher.ps1:107` starts `'claude.exe'` by bare name, so step 6 would fail. No `<round>` (the R2-A1 precedent). Nested base:
the local round-2 DEV `dcececf53c`. At step 6, `0.0.0_AB_MSTR~Z` adds `"claude_exe": "C:\\Users\\Opal_Agent\\.local\\bin\\claude.exe"`
to the operator's `C:\opal_runtime\runtime.config.json` (operator-owned, outside every repo) and runs the launcher from the
scratch copy at this cell's nested commit.

SPAWN ONLY WHEN: at the cut. Slot `~23`, nested worktree `--nested opal_ai=dcececf53c`.

Dry-run at base (opal_ai dcececf53c):
- f8.AC1 base: FAIL as expected (`resolve-claude.ps1 absent`).
- f8.AC2 base: FAIL as expected (`launcher calls resolve-claude=0; bare 'claude.exe' in Start-Process=1; example names claude_exe=0`).

<status>complete</status>
<direct_act>true</direct_act>
<slot>~23</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
