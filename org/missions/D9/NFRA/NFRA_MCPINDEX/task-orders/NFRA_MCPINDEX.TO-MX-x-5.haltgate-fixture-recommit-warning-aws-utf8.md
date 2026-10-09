# NFRA_MCPINDEX task order -- `MX-x-5` -- the round's batch repair: the halt-gate scoping fixture, proof-of-spec-check's re-commit warning, and the aws shim's UTF-8 output

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.md</decomp_doc>
<owned_cells>MX-x-5</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPINDEX.TO-MX-x-5</to_id>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~27</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS change.
comp-adversary: DECLARED-NOT-APPLICABLE -- shared-tooling repairs, each proven by its own test with both arms.
EGRESS CLASS, declared: NONE (offline tests only).
</preflight>

## 1. THE CELL -- `MX-x-5` (round 7; `ROUND_ANALYSIS.round6.md` @361b186c92 section 3a row Z-W23-S2, section 5 item 5; rows Z-W23-S2, Z-S75)

Three repairs to SHARED tooling every seat runs. Each keeps today's correct behaviour, and its test proves both arms.

**(a) The halt gate's recipient-scoping fixture (row Z-W23-S2).** `.tools/test-haltgt-recipient-scoping.sh:24,27,39`
identifies the gate's serial through the retired `.agent_context`; at base it reads `2 passed, 6 failed`. Round 6
(MX-x-4) moved `.tools/halt-gate-check.sh` `halt_gate_resolve_serial()` to a session-resolved serial (an exported
`OPAL_AGENT_SERIAL`, or the tree's own `org/mcp/sessions/<session>.serial`, before the shared root). Repair the fixture
to declare its serial that way (export `OPAL_AGENT_SERIAL`, or write a session serial file in its temp tree), with no
`.agent_context` reference left. Do not change the gate itself.

**(b) proof-of-spec-check's re-commit warning (round-6 L8 packet section 6.5).** When an instance that already exists
at HEAD is re-committed and still carries `PENDING-THIS-COMMIT` rows, the commit re-dates those rows and the instance
reads INVALID (CCX) afterwards. In `.tools/proof-of-spec-check.py` (the pending handling near `:393` and `:447`),
print a `WARN:` naming each pending row when the instance being checked already exists at HEAD. A first commit stays
silent. Test `.tools/tests/test_pos_recommit_warning.py`, offline in a temp git repo: re-committed instance with
pending rows -> WARN naming them; first commit -> no WARN; all rows pinned -> no WARN.

**(c) The aws shim's UTF-8 output (row Z-S75).** `.tools/aws` (`:131`, `:136`) and `.tools/aws.cmd` (`:25-31`) launch
the AWS CLI with no encoding set, so non-ASCII in a response (e.g. `systemctl status`'s bullet in SSM output) raises
`'charmap' codec can't encode` under cp1252 and the read comes back empty. Export `PYTHONUTF8=1` (and/or
`PYTHONIOENCODING=utf-8`) in BOTH shims -- both or neither. Test `.tools/tests/test_aws_shim_utf8.sh`: show the failure
arm (a Python child printing a non-ASCII glyph to a pipe under the shim's environment WITHOUT the setting fails, or
the test prints why that arm cannot be reproduced on this device) and the fixed arm (with the shim's environment it
prints cleanly). Read the shim to find how to get its environment without calling AWS.

**Ruled by the issuer, NOT in this cell:** the two "stale" MCPINDEX tests (Z-W21-S15). `test_mx_s15_dataset_registered`
failed only in a sparse worktree (the issuer's drain re-runs it in the full tree). `test_schwab_host_inputs.py` exists
only on the gateway release lineage, not on CLOUD; it is carried to the next gateway release cut.

## 2. BOUNDS

1. Tests are offline. No AWS call, no deploy.
2. Every changed script keeps its existing interface for current callers. A caller you would break is a BLOCKING row.
3. Nothing under `data/cot/`. No push. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
.tools/test-haltgt-recipient-scoping.sh
.tools/proof-of-spec-check.py
.tools/tests/test_pos_recommit_warning.py
.tools/aws
.tools/aws.cmd
.tools/tests/test_aws_shim_utf8.sh
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~27/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W27-S<k>`; re-read the file for the next free k at commit time;
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`.

## 4. PROOF OF SPEC (literal; run from your worktree root)

<proof_of_spec>
  <expected_criteria>AC1,AC2,AC3</expected_criteria>
  <criterion id="AC1" cell_refs="MX-x-5" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round7/checks/x5.AC1.sh; echo "exit=$?"</invocation><expect>the scoping test passes with 0 failed; .agent_context references in the fixture: 0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-x-5" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round7/checks/x5.AC2.sh; echo "exit=$?"</invocation><expect>pytest passes with 0 failed (re-commit with pending rows warns; first commit and all-pinned stay silent) -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MX-x-5" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round7/checks/x5.AC3.sh; echo "exit=$?"</invocation><expect>the shim test exits 0 with both arms printed -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~27/NFRA_MCPINDEX.TO-MX-x-5.haltgate-fixture-recommit-warning-aws-utf8.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the proof instance at the `<instance_path>`. Report once, naming every existing caller of the changed scripts
you checked.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round-7 item 5, the batch repair cell (worker-light, C7 trial). Battery dry-run at
base: x5.AC1 FAIL as expected (2 passed, 6 failed; 1 `.agent_context` reference); x5.AC2 FAIL as expected (test
absent); x5.AC3 FAIL as expected (test absent).

<status>complete</status>
<round>7</round>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
