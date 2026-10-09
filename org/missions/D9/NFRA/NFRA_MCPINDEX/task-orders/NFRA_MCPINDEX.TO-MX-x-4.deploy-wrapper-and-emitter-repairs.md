# NFRA_MCPINDEX task order -- `MX-x-4` -- the round's batch repair: the deploy wrapper's UTF-8 manifest rewrite, the halt gate's per-session serial, and the catalog emitter's declared inputs

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.md</decomp_doc>
<owned_cells>MX-x-4</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPINDEX.TO-MX-x-4</to_id>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~23</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS change.
comp-adversary: DECLARED-NOT-APPLICABLE -- shared-tooling repairs, each proven by its own test with both arms.
EGRESS CLASS, declared: NONE (offline tests only).
</preflight>

## 1. THE CELL -- `MX-x-4` (round 6; `ROUND_ANALYSIS.round5.md` @1edec80f63 section 5 item 6; rows Z-W21-S23, Z-W21-S21, Z-W21-S7, Z-S57)

These are three repairs to SHARED tooling that every seat runs. Each must keep today's correct behaviour, and its test
must prove both arms.

**(a) The deploy wrapper's manifest rewrite (row Z-W21-S23).**
- `infra/aws/ec2/safe-ec2-deploy.sh:206-214` rewrites `infra/aws/ec2/EC2_MANIFEST.json` with
  `jq "... .deployed_commit = ... | ._last_updated = ..." "$MANIFEST" | tr -d '\r' > "$TEMP"`, then `mv`. The same shape
  is at :99.
- On this device it turned 4 unrelated lines' unicode-escaped dashes into mojibake (dep-branch commits e159e023f0 and
  da1f54bfda).
- Replace the rewrite with a Python JSON parse and dump, UTF-8 in and out, preserving the file's escape style, key
  order and newline convention.
- Only `services.<svc>.deployed_commit`, `deployed_at`, `previous_deployed_commit` (if the wrapper sets it) and
  `_last_updated` may move.
- Keep the wrapper's interface and exit codes. Put the logic in a small helper the test can call.
- New test `.tools/tests/test_safe_ec2_deploy_manifest.py`. On a fixture manifest carrying `—`-style escapes and
  non-ASCII, it proves:
  - exactly the target keys change;
  - every other service entry is byte-equal after a round trip;
  - a negative control: the old `jq | tr` shape run on the same fixture differs. Skip that control, with the reason
    printed, if `jq` is absent.

**(b) The halt gate's serial in a shared-session worktree (row Z-W21-S21).**
- `.tools/halt-gate-check.sh` `halt_gate_resolve_serial()` (:68-84) reads `${CLAUDE_CODE_SESSION_ID}.serial`, first
  from `${repo_root}/org/mcp/sessions`, then from `${HALT_GATE_SHARED_ROOT}/org/mcp/sessions`.
- A worker worktree that shares the issuer's session id resolves to the ISSUER's serial (rc=3 on the deployer).
- Make an explicit per-tree declaration win: `OPAL_AGENT_SERIAL` exported in the environment, or the worktree's own
  `org/mcp/sessions/<session>.serial`, before the shared root.
- Behaviour for a tree with neither is UNCHANGED: it falls back to the shared root exactly as today.
- New test `.tools/tests/test_halt_gate_session_serial.sh`, in temp dirs with fake session files, covering three arms:
  - a worktree declaring its own serial resolves to its own;
  - the issuer's tree resolves to the issuer;
  - a tree declaring nothing resolves through the shared root as before.
  It exits 0 only when all three hold.

**(c) The catalog emitter's hidden inputs (row Z-W21-S7).**
- `workflows/atom_decomposition/emit_catalog_v02.py` hard-codes `CENSUS_DIR` (:386) and `PORTAL_API` (:429).
- With the census absent, `census_text()` (:403-407) returns `None`, and `census_ref_for()` (:410-422) silently writes
  `"NONE -- uncensused (L-14)"` over existing rows.
- Take both as declared arguments (`--census-dir`, `--portal-api`). The defaults are today's paths, so a plain
  invocation still works where the inputs exist.
- REFUSE (non-zero exit, nothing written) when the census directory is absent or empty. Never write "uncensused" over a
  row that has a census ref.
- New test `workflows/atom_decomposition/tests/test_emit_declared_inputs.py`, offline in a temp dir, proving:
  - absent census -> refusal, and the output catalog untouched;
  - present census -> the emitted rows carry their census refs.

**Z-S57's channel resolver is NOT in this cell.** It was the issuer's own scratch and is fixed (drive log
2026-09-29T08Z).

**Other seats:** MX-d-6 RUNS the emitter this round at its own base. Keep the default invocation working.

## 2. BOUNDS

1. Tests are offline. No AWS call, no deploy, no manifest edit to the real `EC2_MANIFEST.json`.
2. Every changed script keeps its existing interface for current callers. A caller you would break is a BLOCKING row.
3. Nothing under `data/cot/`. No push. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
infra/aws/ec2/safe-ec2-deploy.sh
.tools/halt-gate-check.sh
.tools/tests/test_safe_ec2_deploy_manifest.py
.tools/tests/test_halt_gate_session_serial.sh
workflows/atom_decomposition/emit_catalog_v02.py
workflows/atom_decomposition/tests/test_emit_declared_inputs.py
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~23/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W23-S<k>`; re-read the file for the next free k at commit time;
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`.

## 4. PROOF OF SPEC (literal; run from your worktree root)

<proof_of_spec>
  <expected_criteria>AC1,AC2,AC3</expected_criteria>
  <criterion id="AC1" cell_refs="MX-x-4" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round6/checks/x4.AC1.sh; echo "exit=$?"</invocation><expect>pytest passes with 0 failed -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-x-4" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round6/checks/x4.AC2.sh; echo "exit=$?"</invocation><expect>three arms pass (own serial / issuer serial / shared-root fallback) -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MX-x-4" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round6/checks/x4.AC3.sh; echo "exit=$?"</invocation><expect>pytest passes with 0 failed (absent census refuses; present census keeps refs) -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~23/NFRA_MCPINDEX.TO-MX-x-4.deploy-wrapper-and-emitter-repairs.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the proof instance at the `<instance_path>`. Report once, in your final message, naming every existing caller of
the three scripts you checked. Do not edit this task order beyond your status flip.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round-6 item 6, the batch repair cell. Item 5 (the gateway suite green, or each red
named with its owner) is the issuer's drain check, not a face criterion; the MX-d-5 assertion retirement rides MX-d-6.
Battery dry-run at base: x4.AC1, AC2 and AC3 each FAIL as expected (test file absent).

<status>complete</status>
<round>6</round>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
