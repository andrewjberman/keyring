# NFRA_MCPMSP task order -- `MS-a-3` -- ROUND 1, hop 4 live: the `Opal_MSP` account on the site-Z box

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPMSP/decompositions/NFRA_MCPMSP_DECOMP.md</decomp_doc>
<owned_cells>MS-a-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_MCPMSP~4</issued_to>
<issued_by>2.0.0_SA_COO~MS</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- a Windows local account; nothing reaches AWS.
comp-adversary: DECLARED-NOT-APPLICABLE -- thread round; the boundary probe (AC2) is the adversary read.
EGRESS CLASS, declared: none.
</preflight>

## 1. THE CELL -- `MS-a-3` (decomposition section 2)

Create the partner runtime's dedicated local account on this box with the harness `MS-t-3` built (earlier in your
queue; merged, with its nested opal_ai commit):

1. Write the REAL config OUTSIDE every repo at `C:\opal_runtime_msp\runtime.msp.config.json`, from
   `opal_ai/opal/runtime-msp/provision/runtime.msp.config.example.json` (`account_name` `Opal_MSP`,
   `checkout_dir` `C:\opal_runtime_msp\opal_ai`, `state_dir` `C:\opal_runtime_msp\state`, the workspace probe file,
   `prod_ref` `PROD`).
2. `provision-account.ps1 -Config C:\opal_runtime_msp\runtime.msp.config.json -Plan`, then the same WITHOUT `-Plan` in
   an ELEVATED session. **Elevation is G-ADMIN (Andrew):** if your shell is not elevated, the script prints
   `ELEVATION REQUIRED` and does nothing; then file ONE BLOCKING row naming G-ADMIN, record the `-Plan` output, and
   stop -- never try to elevate yourself.
3. Read AC1 and AC2. `launch-gate.ps1` needs the opal_ai PROD checkout, which waits on G-PUSH (opal_ai DEV -> PROD,
   `0.0.0_AB_MSTR~Z` on Andrew's word); it is NOT a criterion here and runs at the close.

## 2. BOUNDS

1. One local account and its two directories and ACLs, by the script. `Opal_Agent`, its directories and its credential
   are untouched (AC1 prints its existence beside yours).
2. The credential is DPAPI-protected in the OPERATOR profile, never printed, never committed.
3. No push. REFUSE a criterion you cannot meet as written, with its measurement.

## 3. SURFACES

<paths>
org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/0.9.0_WK_NFRA_MCPMSP~4/**
org/missions/D6/NFRA/NFRA_MCPMSP/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

Off-repo, on this box: `C:\opal_runtime_msp\` (config, checkout dir, state dir) and the operator profile's
`.opal_runtime\opal_msp_cred.xml`. Read, never write: `opal_ai/opal/runtime/**`, `opal_ai/opal/runtime-msp/**`,
`org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/2.0.0_SA_COO~MS/round1/checks/`. Rows: `INVESTIGATION_v1.Z.md`, id
`NFRA_MCPMSP-Z-W4-S<k>`, `disarm_owner` `2.0.0_SA_COO~MS`.

## 4. PROOF OF SPEC (literal; run from your parent worktree root)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MS-a-3"><invocation>bash org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/2.0.0_SA_COO~MS/round1/checks/a3.AC1.sh; echo "exit=$?"</invocation><expect>exists=True enabled=True admin=0 codex=0 opal_agent_exists=True -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MS-a-3"><invocation>bash org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/2.0.0_SA_COO~MS/round1/checks/a3.AC2.sh; echo "exit=$?"</invocation><expect>verify-boundary (msp config): BOUNDARY: DENIED-OK -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/0.9.0_WK_NFRA_MCPMSP~4/NFRA_MCPMSP.TO-MS-a-3.opal-msp-account.proof_of_spec.json`.
Report once, with: the `-Plan` lines; the two check lines; whether G-ADMIN was needed; any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-1 issuance (CTO msg 26985); WORLD: a device account. Checks dry-run at base: AC1 FAIL as
expected (`exists=False`, `opal_agent_exists=True`); AC2 FAIL as expected (the script is absent at the parent's
opal_ai gitlink). G-ADMIN is Andrew's; G-PUSH for the launch gate is `0.0.0_AB_MSTR~Z`'s.

<status>staged</status>
<round>1</round>
<slot>~4</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
