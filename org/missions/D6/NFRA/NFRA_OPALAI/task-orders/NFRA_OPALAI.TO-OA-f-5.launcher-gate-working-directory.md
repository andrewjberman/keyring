# NFRA_OPALAI task order -- `OA-f-5` -- DIRECT ACT, ADDENDUM R2-A3: the launcher starts the launch gate in a directory Opal_Agent can enter

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_OPALAI/decompositions/NFRA_OPALAI_DECOMP.md</decomp_doc>
<owned_cells>OA-f-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPALAI~20</issued_to>
<issued_by>2.0.0_SA_COO~AI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a one-parameter script change; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- nothing reaches AWS.
comp-adversary: DECLARED-NOT-APPLICABLE -- the gate's own refusal arms are unchanged.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OA-f-5` (decomposition ADDENDUM R2-A3)

`opal_ai/opal/runtime/launcher.ps1` is run by the operator. It starts the launch gate AS the account `Opal_Agent`
(`:85-88`, `Start-Process -FilePath 'powershell.exe' ... -Credential $credential -LoadUserProfile -NoNewWindow -Wait
-PassThru -RedirectStandardOutput $gateOutFile`), and on `GATE: PASS` it starts `claude.exe` as `Opal_Agent` (`:107-108`,
which already passes `-WorkingDirectory $runtimeDir`).

The gate launch passes NO `-WorkingDirectory`. So the child inherits the operator's current directory, which
`Opal_Agent` cannot enter, and the start fails with "The directory name is invalid" (measured by the issuer on this
machine, 2026-09-28). Add `-WorkingDirectory` to that ONE call, set to the configured `state_dir`: the directory
`Opal_Agent` owns (Modify) and the gate itself already reads from the config. Read `state_dir` from the same config
object the script already loads, the same way it reads `checkout_dir`. Change nothing else: not the redirect (the parent
opens it), not the gate's arguments, and not the `claude.exe` launch.

## 2. BOUNDS

1. **`opal_ai` is a nested repository** at `<worktree>/opal_ai`, on its own branch off `opal_ai` `fd8ab8a57f`. Commit
   with `git -C opal_ai commit --author "0.9.0_WK_NFRA_OPALAI~20 <0.9.0_WK_NFRA_OPALAI~20@opal.agent>" -F <msgfile> --
   opal/runtime/launcher.ps1`, the msgfile written with the Write tool.
2. Never run the launcher, never elevate, never log on as `Opal_Agent`. The live run is G-ACCT step 6, `0.0.0_AB_MSTR~Z`'s.
3. Standing: no push, no install, no vendor call. REFUSE a criterion you cannot meet as written, and report the refusal
   with its measurement. Never repair a criterion, widen it, or meet it by a route this face does not name.

## 3. SURFACES

<paths>
opal_ai/opal/runtime/launcher.ps1
org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~20/**
org/missions/D6/NFRA/NFRA_OPALAI/surprise-channel/investigations/**
</paths>

Rows: `org/missions/D6/NFRA/NFRA_OPALAI/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, id
`NFRA_OPALAI-Z-W20-S<k>` (none exist at the cut; the first is S1).

## 4. PROOF OF SPEC (literal; run from your worktree root, after the nested commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OA-f-5"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~AI/round2/checks/f5.AC1.sh; echo "exit=$?"</invocation><expect>credentialed Start-Process=2 with -WorkingDirectory=2; gate launch with -WorkingDirectory=1; parse errors=0; other files changed vs fd8ab8a57f=0 -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~20/NFRA_OPALAI.TO-OA-f-5.launcher-gate-working-directory.proof_of_spec.json`.
Report once: the old and new call verbatim, the nested commit hash, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** a direct act ruled by the issuer inside its own decomposition (a LOCAL defect in a round-1 thread file,
`/canonical-drive` obligation 7). It is found on the G-ACCT step-6 path before that step runs. It is the same class as
OA-f-4's cause, measured when this seat probed `Start-Process -Credential` without `-WorkingDirectory`. No roundtag
(the R2-A1 precedent). It reaches PROD in the cutover G-PUSH. `0.0.0_AB_MSTR~Z` runs step 6 from the scratch copy
(OA-f-3 + OA-f-4 + this). The scratch copy must sit where `Opal_Agent` can READ it, because the gate script path is
resolved beside the launcher; that is relayed with the line.

One mechanical criterion: a one-parameter change, so (a) is the behaviour and its bound (only this file). No real-neighbour
seam is reachable without logging on as `Opal_Agent`, which is G-ACCT's.

SPAWN ONLY WHEN: at the cut. Slot `~20`, nested worktree `--nested opal_ai=fd8ab8a57f`.

Dry-run at base (opal_ai fd8ab8a57f):
- f5.AC1 base: FAIL as expected (`credentialed Start-Process=2 with -WorkingDirectory=1; gate launch with -WorkingDirectory=0`).

<status>complete</status>
<direct_act>true</direct_act>
<slot>~20</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
