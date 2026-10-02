# NFRA_OPALAI task order -- `OA-f-12` -- DIRECT ACT, ADDENDUM R2-A10: the claude resolver accepts a configured path the non-elevated operator cannot see into

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_OPALAI/decompositions/NFRA_OPALAI_DECOMP.md</decomp_doc>
<owned_cells>OA-f-12</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPALAI~27</issued_to>
<issued_by>2.0.0_SA_COO~AI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a one-file script fix; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- nothing reaches AWS.
comp-adversary: DECLARED-NOT-APPLICABLE -- AC1's miss and found arms are the controls around the seam arm.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OA-f-12` (decomposition ADDENDUM R2-A10)

`opal_ai/opal/runtime/launcher.ps1` starts the Teams Analyst as the local account `Opal_Agent`. It is run by the
OPERATOR and refuses an elevated token, so it always runs NON-elevated. Before it starts the Analyst, it calls
`opal_ai/opal/runtime/resolve-claude.ps1 -Config <json>`:

- the resolver prints `CLAUDE_EXE: <path>` (exit 0) when the config key `claude_exe` names an existing file, or else
  when `claude.exe` is on PATH;
- otherwise it prints `LAUNCHER: REFUSE CLAUDE-NOT-FOUND ...` and exits 5.

**The defect, measured:** the real config's `claude_exe` is the Claude Code install inside Opal_Agent's OWN profile. A
non-elevated operator gets `Test-Path : Access is denied` on that path. The resolver runs with
`$ErrorActionPreference = 'Stop'`, so it THROWS and prints neither line, and the launcher dies before starting the
Analyst.

**Fix, in `resolve-claude.ps1` only:**
- When `claude_exe` is set and the existence test fails with an ACCESS-DENIED error (`UnauthorizedAccessException`,
  or `PermissionDenied`), print `CLAUDE_EXE: <the configured path>` and exit 0, with no error text on any stream. The
  configured path is trusted as given: the operator cannot see into another account's profile, and the Analyst's own
  start fails loudly (`LAUNCHER: REFUSE ANALYST-NOT-STARTED`) if the path is wrong.
- When the path is readable and missing, or `claude_exe` is unset and PATH has no claude, keep today's behaviour
  exactly: the PATH fallback, then `LAUNCHER: REFUSE CLAUDE-NOT-FOUND`, exit 5.
- When the path exists, keep `CLAUDE_EXE: <path>`, exit 0.

Add one comment line naming why access-denied is trusted. Change no other file.

## 2. BOUNDS

1. **`opal_ai` is a nested repository** at `<worktree>/opal_ai`, on its own branch off `0fb3fcb694`. Commit with
   `git -C opal_ai commit --author "0.9.0_WK_NFRA_OPALAI~27 <0.9.0_WK_NFRA_OPALAI~27@opal.agent>" -F <msgfile> -- opal/runtime/resolve-claude.ps1`,
   the msgfile written with the Write tool. The parent gitlink is NOT yours.
2. **Never run the launcher.** Never elevate, never start a process as another account, and never edit `C:\opal_runtime`.
   AC1 runs only the resolver, as yourself.
3. **Your parent worktree is a SPARSE checkout** (the disk is at its limit): only the cone you need is on disk. Do not
   widen it and do not run a full checkout.
4. Flip the `<status>` tag IN PLACE, by replacing the single tag, only when AC1 passes. Standing: no push, no install,
   no vendor call. REFUSE a criterion you cannot meet as written, with its measurement.

## 3. SURFACES

<paths>
opal_ai/opal/runtime/resolve-claude.ps1
org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~27/**
org/missions/D6/NFRA/NFRA_OPALAI/surprise-channel/investigations/**
org/missions/D6/NFRA/NFRA_OPALAI/task-orders/NFRA_OPALAI.TO-OA-f-12.resolver-unreadable-profile.md
</paths>

Read-only: `C:\opal_runtime\runtime.config.json` (AC1 reads its `claude_exe`). Rows: `INVESTIGATION_v1.Z.md`, id
`NFRA_OPALAI-Z-W27-S<k>`, with an exact `HH:MMZ` `surfaced_at`.

## 4. PROOF OF SPEC (literal; run from your worktree root, after the nested commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OA-f-12"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~AI/round2/checks/f12.AC1.sh; echo "exit=$?"</invocation><expect>seam 'CLAUDE_EXE: <the configured path>' rc=0 access-denied text=0; miss 'LAUNCHER: REFUSE CLAUDE-NOT-FOUND ...' rc=5; found 'CLAUDE_EXE: ...fake-claude.exe' rc=0; parse errors=0; other files changed vs 0fb3fcb694=0 -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~27/NFRA_OPALAI.TO-OA-f-12.resolver-unreadable-profile.proof_of_spec.json`.
Report once: the resolver's changed region, the nested commit hash, AC1's line, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** a direct act ruled by the issuer inside its own decomposition (`/canonical-drive` obligation 7). It was
found while preparing the item-0 close run, after the 8194 wall un-held it (OA-f-11 @3f534f490a).

The seam is between two earlier orders:
- OA-f-8 wrote the resolver to `Test-Path` the configured `claude_exe` as the operator;
- OA-f-9 made the launcher refuse an elevated parent.

Since OA-f-9, the operator is always non-elevated and cannot read Opal_Agent's profile. Measured 2026-10-02 ~03:2xZ:
`resolve-claude.ps1` from r2-dev 0fb3fcb694 against the real `C:\opal_runtime\runtime.config.json`, non-elevated, gave
`Test-Path : Access is denied` and threw. So the close-run launch would die before starting the Analyst. Operator
launcher v2 never hit this, because it used `claude_exe` without a test.

The fix must reach opal_ai PROD before the close run. That is a G-PUSH, `0.0.0_AB_MSTR~Z` on Andrew's word, and it
carries the OA-f-11 installer too.

LOCAL direct act, one cell, one criterion. AC1 has the seam arm plus two control arms (miss, found).

SPAWN: slot `~27`, SPARSE worktree (DISK AT LIMIT, msg 28169).

Dry-run at base (OA_F12_REF=0fb3fcb694): f12.AC1 FAIL as expected:
- seam `none` rc=1 with access-denied text 1 (the defect);
- miss and found arms already correct (the controls hold at base).

<status>complete</status>
<direct_act>true</direct_act>
<slot>~27</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
