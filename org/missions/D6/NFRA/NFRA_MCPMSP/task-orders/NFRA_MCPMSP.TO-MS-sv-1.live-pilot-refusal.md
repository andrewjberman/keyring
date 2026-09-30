# NFRA_MCPMSP task order -- `MS-sv-1` -- ROUND 2, E2: the live arm -- an opalinvest.com sender is refused and gets no reply

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPMSP/decompositions/NFRA_MCPMSP_DECOMP.md</decomp_doc>
<owned_cells>MS-sv-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_MCPMSP~6</issued_to>
<issued_by>2.0.0_SA_COO~MS</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- reads the host audit over SSM with existing access.
comp-adversary: DECLARED-NOT-APPLICABLE -- AC2's control (the session DID ask) is the read against a silent session.
EGRESS CLASS, declared: none.
</preflight>

## 1. THE CELL -- `MS-sv-1` (decomposition v2, R2.2; PRD C3/C4, FWD-3)

With the gateway release live (`MSP_CALLING_IDENTITIES` set to the MSP calling identity) and the supervised `Opal_MSP`
session running, Andrew sent ONE Teams message from `opalinvest.com` to the MSP calling identity. The session called
`opal_asker_query`; the gateway refused it `asker_pilot_scope`; the agent-side hook blocked any reply. This order's
AMENDMENT (issuer) names: `t0`, `t1` (ISO UTC, the window), `chat_id`, and `msp_identity` (the calling email).

1. Write `org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/0.9.0_WK_NFRA_MCPMSP~6/r2_e2v_run.json` = `{"t0", "t1",
   "chat_id", "msp_identity"}` from the amendment.
2. Run AC1 and AC2 (both read `/opt/opal-gateway/audit.jsonl` on instance `i-07dccb1615503ac99` over SSM; entries
   `ts`, `user`, `tool`, `args`, `outcome`).
3. For AC3 (the CVO's), write `r2_e2v_evidence.md` in your deliverables: the refusal entry's fields (no text -- there
   is none), the count of sends by the MSP identity in the window (zero), and the `opal_asker_query` entry's verdict.
If the amendment is absent, STOP with a BLOCKING row.

## 2. BOUNDS

1. Read-only on the host. No send of any message. No push, no vendor call. REFUSE a criterion you cannot meet.

## 3. SURFACES

<paths>
org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/0.9.0_WK_NFRA_MCPMSP~6/**
org/missions/D6/NFRA/NFRA_MCPMSP/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

Read, never write: `infra/aws/ec2/opal-gateway/app/audit.py`,
`org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/2.0.0_SA_COO~MS/round2/checks/`. Rows: `INVESTIGATION_v1.Z.md`, id
`NFRA_MCPMSP-Z-W6-S<k>`, `disarm_owner` `2.0.0_SA_COO~MS`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MS-sv-1"><invocation>bash org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/2.0.0_SA_COO~MS/round2/checks/e2v.AC1.sh; echo "exit=$?"</invocation><expect>ssm status=Success; refusal entries in window>=1 matching chat+asker_pilot_scope+opalinvest.com>=1 with text=0 verdict=OK -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MS-sv-1"><invocation>bash org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/2.0.0_SA_COO~MS/round2/checks/e2v.AC2.sh; echo "exit=$?"</invocation><expect>ssm status=Success; msp identity calls>=1 asker_queries>=1 sends_any_target=0 verdict=OK -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MS-sv-1" judgment="true"/>
</proof_of_spec>

AC3 (JUDGMENT, Rule J; graded by `3.0.0_SA_CVO~O` at L9, never self-graded): from the refusal entry and the absent
reply, the refusal came from the gate, not from the Analyst declining. Record it `UNVERIFIABLE-BY-INSTRUMENT` with
`status_reason` naming the CVO.

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/0.9.0_WK_NFRA_MCPMSP~6/NFRA_MCPMSP.TO-MS-sv-1.live-pilot-refusal.proof_of_spec.json`.
Report once, with: the two check lines; the evidence file path; the commit hash; any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** HELD (join): G-MSPID, MS-d-2 live with `MSP_CALLING_IDENTITIES` set, MS-sh-1 merged, and MS-rn-1's
session; then Andrew's one message. Queued on slot `~6` after MS-rn-1 (same session). Checks dry-run at base: AC1 FAIL
as expected, AC2 FAIL as expected (no run file). AC2 counts sends to ANY target: `send_chat_message` is absent from
`audit._ARGS_ALLOWLIST`, so its chat_id is never logged (measured at the cut).

<status>staged</status>
<round>2</round>
<slot>~6</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
