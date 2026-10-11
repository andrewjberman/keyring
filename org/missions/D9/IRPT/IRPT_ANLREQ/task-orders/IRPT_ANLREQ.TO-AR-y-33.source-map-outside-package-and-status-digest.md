# TO IRPT_ANLREQ.TO-AR-y-33 -- the source map says which files are outside a package on purpose; it records irpt-status's live digest

<to_id>IRPT_ANLREQ.TO-AR-y-33</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~53</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>
<workstream>Y</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD (the build script and its map; BUILD_ONLY builds, nothing uploaded or applied) The class is WORLD because the L6 gate's floor for an `infra/` path is WORLD; the cell itself builds, uploads and applies nothing. |
**Decomp cell:** `AR-y-33` (`decompositions/IRPT_ANLREQ_DECOMP_R3_Y.md`) | **outcome_ref:** FWD-1 | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~53`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-53` (branch `wk-IRPT_ANLREQ-53`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~53 <0.9.0_WK_IRPT_ANLREQ~53@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing.
- Every build here is `BUILD_ONLY=1` with `TMPDIR` pointing OUTSIDE the worktree. Never run the script without `BUILD_ONLY=1`: without it
  it uploads.

### THE CELL (`AR-y-33`, inlined)

*The source map says, per function, which source-dir files are outside the package ON PURPOSE, and the parity check honours it, so the
store function builds clean with no skip flag; the map records irpt-status's live digest.*

**Part A -- the store function builds without a skip flag.**
- `BUILD_ONLY=1 bash infra/aws/lambda/ci/build-and-upload.sh investor-reporting irpt-commentary-draft-store-lambda` ends
  `PARTIAL -- 0 built, 1 failed` today. Its members stage and verify; the refusal is the parity check `ADHC_DRIFTD.002`
  (`build-and-upload.sh:413-457`): seven top-level `.py` files sit in the function's source dir
  (`infra/aws/lambda/investor-reporting/reports/`) and are in no `files[]` of a function sharing that dir --
  `build_resident_package.py`, `currency_authority.py`, `custody_write.py`, `generate_installed.py`, `request_composition.py`,
  `resident_installed.py`, `status_installed.py`. They are other functions' members, staged from that dir by `staged_from` rows, and are
  outside the store's import closure. The live store was built with `BAU_PARITY_SKIP=1`, which turns the WHOLE check off.
- **Build a declared exclusion instead of a blanket skip.** A function's entry in `infra/aws/lambda/ci/lambda-source-map.json` may carry
  `"outside_package": {"<file name>": "<one-line reason>", ...}`: source-dir files that are deliberately not this function's members.
  The parity check treats a file named there as accounted for, for THAT function only. Every other file is checked as today. A name in
  `outside_package` that is ALSO in the function's `files[]`, or that does not exist in the source dir, is an ERROR that fails that
  function's build with a line naming it (a stale declaration must not rot silently).
- Give `irpt-commentary-draft-store-lambda` that key with the seven files, each with its reason (which function packages it; read the
  map's `staged_from` rows to say so truthfully). Do NOT add the seven to its `files[]`: the package must not change.
- Document the key in the comment block above the check, in the same style as the block that is there.

**Part B -- the map records irpt-status's live digest.**
- `functions["irpt-status"].artifact_sha256` reads `E7VKvhg3E9D5euWO+S649/iyAJ05xUmFPqHEAKDTFxA=`. The function runs
  `6idtFvAmYk73wJdr5DPRIyEPrLeWgzjlqbdNr5f1wxc=` (revision 6, applied 2026-10-11; a BUILD_ONLY of irpt-status from this map prints that
  digest). Set the field to the live digest. Change NOTHING else in that entry: not a pin, not a member, not a sha256 of a member.
- If the entry carries another field that records the applied artifact (an S3 version id, an applied-at stamp), leave it and name it in
  your report with its value; do not guess a value for it.

**Not yours:** any other function's entry; `BAU_PARITY_SKIP` itself (it stays, as the rare override); any upload or apply.

### ACCEPTANCE

<criterion id="AR33-y-AC1" cell_refs="AR-y-33"><invocation>python C:/dev/wk-irpt-anlreq-53/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r3/ar3_checks.py y33-store --root C:/dev/wk-irpt-anlreq-53</invocation><expect>Y33-STORE-OK</expect></criterion>
`AR33-y-AC1`: without `BAU_PARITY_SKIP`, the store's BUILD_ONLY prints its `BUILD_ONLY:` line and none of the seven is in the built zip.

<criterion id="AR33-y-AC2" cell_refs="AR-y-33"><invocation>python C:/dev/wk-irpt-anlreq-53/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r3/ar3_checks.py y33-control --root C:/dev/wk-irpt-anlreq-53</invocation><expect>Y33-CONTROL-OK</expect></criterion>
`AR33-y-AC2`: the difference control of AC1 -- a file in the source dir that is neither packaged nor declared outside STILL refuses the
build by name. (The check writes one probe file into `reports/` and removes it; it passes at the base and must still pass.)

<criterion id="AR33-y-AC3" cell_refs="AR-y-33"><invocation>python C:/dev/wk-irpt-anlreq-53/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r3/ar3_checks.py y33-digest --root C:/dev/wk-irpt-anlreq-53</invocation><expect>Y33-DIGEST-OK</expect></criterion>
`AR33-y-AC3`: the map records `6idtFvAm...` for irpt-status and a BUILD_ONLY of irpt-status still prints that digest.

<expected_criteria>AR33-y-AC1 AR33-y-AC2 AR33-y-AC3</expected_criteria>

The issuer runs a BUILD_ONLY of every investor-reporting function at the drain and compares each digest with the base's.

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~53/` and this order's
  file (status flip only).
- READ only: everything else under `infra/aws/lambda/`.
- No live act: `BUILD_ONLY=1` always; never upload, never apply, never call a live API. Git Bash default utilities only in the script (no
  `pgrep`, `flock`, `wget`); the script resolves its JSON tool itself -- use that, not a bare `jq`. No non-ASCII in what you add.

<paths>
infra/aws/lambda/ci/lambda-source-map.json
infra/aws/lambda/ci/build-and-upload.sh
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R3_Y.md</decomp_doc> (round 3, workstream Y), cell `AR-y-33`.
<owned_cells>AR-y-33</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR33-y-AC1 AR33-y-AC2 AR33-y-AC3. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~53/IRPT_ANLREQ.TO-AR-y-33.source-map-outside-package-and-status-digest.proof_of_spec.json`.
Validate it AFTER its commit with `python .tools/proof-of-spec-check.py <instance> AR33-y-AC1,AR33-y-AC2,AR33-y-AC3`.
</proof_of_spec>

**REPORT (once):** each check line verbatim; the commit; the store's built digest before (with `BAU_PARITY_SKIP=1`) and after (without),
which must be EQUAL since the package did not change -- if they differ, that is a BLOCKING row, not a pass; any other applied-artifact
field you found on the irpt-status entry; any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- build-and-upload.sh is the one builder of every Lambda in the map (235 function entries, as 2.0.0_SA_COO~P2 counted them in msg 3997; not re-counted here); the change is inside the parity block (:413-457) and is keyed on a new per-function map member, so a function without the member takes the old path. The drain re-builds every investor-reporting function and compares digests with the base. comp-routes: DECLARED-NOT-APPLICABLE. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE. comp-iam: DECLARED-NOT-APPLICABLE. comp-adversary: RUN -- AR33-y-AC1 base FAIL as expected (PARTIAL, 0 built); AR33-y-AC2 base PASS as expected (the control: probe named in a parity refusal, probe removed, reports/ clean after); AR33-y-AC3 base FAIL as expected (the map records E7VKvhg3 while a BUILD_ONLY prints 6idtFvAm).
lane: IRPT_COMPLETION_SOURCE_MAP admits COO~Y and a worker through this order's paths; build-and-upload.sh is shared CI, named in paths.
</preflight>

Source: CTO round-3 analysis @430d79e86d section 4 Y3 and Y4 (first item), section 2 rows D2-W41-S17 and D2-S32. The issuer rules, inside
its decomposition, the SECOND of the analysis's two ways for Y3 ("says they are outside the package on purpose"): listing the seven in
`files[]` would change the live store's bytes for no behaviour, and the blanket skip hides every future unregistered file.
