# NFRA_OPALAI task order -- `OA-f-13` -- DIRECT ACT, ADDENDUM R2-A11: the WFP wall's sublayer read-back accepts the weight the engine assigned and prints it

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_OPALAI/decompositions/NFRA_OPALAI_DECOMP.md</decomp_doc>
<owned_cells>OA-f-13</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPALAI~28</issued_to>
<issued_by>2.0.0_SA_COO~AI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a one-file script fix; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- nothing reaches AWS.
comp-adversary: DECLARED-NOT-APPLICABLE -- AC1's top, flag and name arms are the controls around the seam arm.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OA-f-13` (decomposition ADDENDUM R2-A11)

`opal_ai/opal/runtime/provision/wall-dapi-8194-wfp.ps1` installs a persistent WFP sublayer `opal_runtime_dapi_8194_wall`
(requested weight 0xFFFF) and two BLOCK filters in it. It compiles a C# class `OpalWfp` from the here-string `$cs`. In real
mode, step (c) calls `[OpalWfp]::Verify()`, which returns one `VERIFY: <name> OK|FAIL` line for the sublayer and one per
filter. The PowerShell tail exits 4 unless every line ends with `' OK'`.

**The defect, measured:** `Verify()` grades the sublayer as
`Str(s.display.name) == SUBLAYER_NAME && s.weight == SUBLAYER_WEIGHT && (s.flags & FLAG_PERSISTENT) != 0`. On this box the
engine holds the sublayer at weight 0xFFE2, because other vendors' sublayers occupy 0xFFFF..0xFFE3. So VERIFY prints FAIL
and the script exits 4, although the sublayer and both filters are installed and the wall works.

**Fix, in `wall-dapi-8194-wfp.ps1` only, inside the C# class:**
- Add `public static string SubLayerLine(string name, ushort weight, uint flags)`. It returns
  `"VERIFY: " + SUBLAYER_NAME + " WEIGHT 0x" + weight.ToString("X4") + (ok ? " OK" : " FAIL")`, where `ok` is
  `name == SUBLAYER_NAME && (flags & FLAG_PERSISTENT) != 0`. The weight is printed and never graded.
- In `Verify()`, when `FwpmSubLayerGetByKey0` succeeds, add `SubLayerLine(Str(s.display.name), s.weight, s.flags)` as the
  sublayer line. When it fails, keep the line `VERIFY: opal_runtime_dapi_8194_wall FAIL`. Free the memory as today.
- Keep the two filter lines, `Apply`, `ScanPermit`, `Remove`, the `-Plan` text and the PowerShell tail byte-for-byte.
  The tail's `EndsWith(' OK')` test must still grade the new line, which is why the weight comes before the verdict.

Add one comment line naming why the weight is printed, not graded. Change no other file.

## 2. BOUNDS

1. **`opal_ai` is a nested repository** at `<worktree>/opal_ai`, on its own branch off `bd7cd5d1ce`. Commit with
   `git -C opal_ai commit --author "0.9.0_WK_NFRA_OPALAI~28 <0.9.0_WK_NFRA_OPALAI~28@opal.agent>" -F <msgfile> -- opal/runtime/provision/wall-dapi-8194-wfp.ps1`,
   the msgfile written with the Write tool. The parent gitlink is NOT yours.
2. **Never run the script in real or `-Remove` mode, and never elevate.** AC1 runs only `-Plan` and the compiled class,
   as yourself. Never edit `C:\opal_runtime`.
3. Flip the `<status>` tag IN PLACE, by replacing the single tag, only when AC1 passes. Commit the parent-side files with
   `.tools/safe-commit.sh --author "0.9.0_WK_NFRA_OPALAI~28 <0.9.0_WK_NFRA_OPALAI~28@opal.agent>" -F <msgfile> -- <paths>`.
   Standing: no push, no install, no vendor call. REFUSE a criterion you cannot meet as written, with its measurement.

## 3. SURFACES

<paths>
opal_ai/opal/runtime/provision/wall-dapi-8194-wfp.ps1
org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~28/**
org/missions/D6/NFRA/NFRA_OPALAI/surprise-channel/investigations/**
org/missions/D6/NFRA/NFRA_OPALAI/task-orders/NFRA_OPALAI.TO-OA-f-13.wfp-sublayer-readback-weight.md
</paths>

Rows: `INVESTIGATION_v1.Z.md`, id `NFRA_OPALAI-Z-W28-S<k>`, with an exact `HH:MMZ` `surfaced_at`.

## 4. PROOF OF SPEC (literal; run from your worktree root, after the nested commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OA-f-13"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~AI/round2/checks/f13.AC1.sh; echo "exit=$?"</invocation><expect>seam 'VERIFY: opal_runtime_dapi_8194_wall WEIGHT 0xFFE2 OK'; top '... WEIGHT 0xFFFF OK'; flag '... WEIGHT 0xFFE2 FAIL'; name '... WEIGHT 0xFFE2 FAIL'; wire calls>=1 compares=0; plan COMPILE:OK=1 rc=0; parse errors=0; other files changed vs bd7cd5d1ce=0 -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~28/NFRA_OPALAI.TO-OA-f-13.wfp-sublayer-readback-weight.proof_of_spec.json`.
Report once: the changed region, the nested commit hash, AC1's line, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** a direct act ruled by the issuer inside its own decomposition (`/canonical-drive` obligation 7), on row
Z-S54. `1.0.0_SA_CTO~O` msg 28164 point 2 said to diagnose `Verify()`'s sublayer read at an elevated sitting with a
`netsh wfp show` dump, then fix it. That dump exists: F11_SUBLAYER_EVIDENCE.json, from Andrew's elevated
`netsh wfp show state`, shows weight 65506 (0xFFE2), the PERSISTENT flag, 29 higher-weight sublayers, and both filters
inside our key. The fix prints the read-back weight, so the next elevated run also shows whether the C# read agrees with
`netsh`.

Not on the close-run path: the wall is installed and AC3 passed. This lands on r2-dev only AFTER the pending G-PUSH of
`bd7cd5d` (card @9c15c703a6), and it rides the cutover push.

LOCAL direct act, one cell, one criterion. AC1 has the seam arm plus three control arms (top, flag, name), a wiring read,
the script's own `-Plan`, and the bounds.

SPAWN: slot `~28`. Disk 107 GB free (15:0xZ), so the old disk limit is lifted; the worktree is sparse anyway, with the cone
widened for row Z-S55: `.tools`, `lib`, `org/modules`, `org/ref`, `org/standards`, `org/surprise_channel`, `infra/logic`,
and the NFRA_OPALAI tree.

Dry-run at base (OA_F13_REF=bd7cd5d1ce): f13.AC1 FAIL as expected. The seam, top, flag and name arms fail with "does not
contain a method named 'SubLayerLine'"; wire calls=0 compares=1. The plan, parse and bounds arms already hold (the
controls). Positive control: a scratch copy patched to the spec printed all four expected lines, wire calls=1 compares=0,
and `-Plan` rc=0.

fanout: 1 of 1 chains, cap 8.

<status>pending</status>
<direct_act>true</direct_act>
<slot>~28</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
