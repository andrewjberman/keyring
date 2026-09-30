# NFRA_MCPMSP task order -- `MS-sh-1` -- ROUND 2, E2: the agent-side gate -- no reply unless the gateway served the asker

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPMSP/decompositions/NFRA_MCPMSP_DECOMP.md</decomp_doc>
<owned_cells>MS-sh-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_MCPMSP~6</issued_to>
<issued_by>2.0.0_SA_COO~MS</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- a local hook.
comp-adversary: DECLARED-NOT-APPLICABLE -- the three blocking fixture cases are the adversary read.
EGRESS CLASS, declared: none.
</preflight>

## 1. THE CELL -- `MS-sh-1` (decomposition v2, R2.2; PRD C3 -- the agent sends no reply to a refused message)

Your worktree carries the nested repo `opal_ai` checked out at its local `DEV` (`61841f5`). The supervised MSP runtime is
`opal_ai/opal/runtime-msp/`; its `.claude/settings.json` today registers ONE PreToolUse hook (matcher `*`, command
`bash "$CLAUDE_PROJECT_DIR/../agent/hooks/concierge-gate.sh"`, timeout 15) -- keep it.

Build:
1. **`opal_ai/opal/runtime-msp/hooks/sender-gate.sh` (new):** a Claude Code PreToolUse hook. It reads the hook JSON on
   stdin (`tool_name`, `tool_input`, `transcript_path`). For a send tool (`mcp__opalgateway__send_chat_message`,
   `mcp__opalgateway__send_channel_message`) it ALLOWS (exit 0) only when the transcript's most recent
   `opal_asker_query` tool call whose input `chat_id` equals the send's target `chat_id` returned a result WITHOUT
   `asker_scope_denied` (a served answer); otherwise it BLOCKS (exit 2, reason on stderr: which case). Any other tool:
   exit 0. Parse JSON with `python` (no jq dependency); fail CLOSED on an unreadable transcript for a send tool.
2. **`opal_ai/opal/runtime-msp/hooks/test_sender_gate.sh` (new):** builds fixture transcripts and hook inputs in a temp
   dir, runs the hook, and prints one line per case -- `PASS: <case>` or `FAIL: <case>` -- for
   `served_answer_allows_send`, `denied_answer_blocks_send`, `no_query_blocks_send`, `other_chat_served_blocks_send`,
   then `RESULT: PASS` only when all four pass (else `RESULT: FAIL`, exit 1).
3. **`opal_ai/opal/runtime-msp/.claude/settings.json`:** add a second PreToolUse entry, matcher
   `mcp__opalgateway__send_.*`, command `bash "$CLAUDE_PROJECT_DIR/hooks/sender-gate.sh"`, timeout 15.
4. Commit INSIDE `opal_ai` on your worktree's nested branch (author as in your definition; never push); report the
   nested commit hash -- the issuer fast-forwards opal_ai's local `DEV` at the drain.

## 2. BOUNDS

1. Write surface: exactly the `<paths>` below. `runtime-msp/record/**`, `runtime-msp/provision/**`, `opal/agent/**` and
   the launcher are others'. No push, no vendor call. REFUSE a criterion you cannot meet.

## 3. SURFACES

<paths>
opal_ai/opal/runtime-msp/hooks/sender-gate.sh
opal_ai/opal/runtime-msp/hooks/test_sender_gate.sh
opal_ai/opal/runtime-msp/.claude/settings.json
org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/0.9.0_WK_NFRA_MCPMSP~6/**
org/missions/D6/NFRA/NFRA_MCPMSP/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

Read, never write: `opal_ai/opal/runtime-msp/**` (others), `opal_ai/opal/agent/hooks/concierge-gate.sh`,
`org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/2.0.0_SA_COO~MS/round2/checks/`. Rows: `INVESTIGATION_v1.Z.md`, id
`NFRA_MCPMSP-Z-W6-S<k>`, `disarm_owner` `2.0.0_SA_COO~MS`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MS-sh-1"><invocation>bash org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/2.0.0_SA_COO~MS/round2/checks/e2h.AC1.sh; echo "exit=$?"</invocation><expect>hook fixture cases: served_answer_allows_send=1 denied_answer_blocks_send=1 no_query_blocks_send=1 other_chat_served_blocks_send=1; final RESULT: PASS lines>=1 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MS-sh-1"><invocation>bash org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/2.0.0_SA_COO~MS/round2/checks/e2h.AC2.sh; echo "exit=$?"</invocation><expect>pretooluse entries=2 sender_gate=True concierge_fence=True verdict=OK -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/0.9.0_WK_NFRA_MCPMSP~6/NFRA_MCPMSP.TO-MS-sh-1.agent-sender-hook.proof_of_spec.json`.
Report once, with: the nested opal_ai commit; the two check lines; the parent commit hash; any row. Then STOP: this
slot continues with MS-rn-1 when its gates clear.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-2 issuance (E2, agent half). Worktree provisioned with `--nested opal_ai=61841f5`. Checks
dry-run at base (main tree's opal_ai checkout is not at DEV, so AC2 was also read on the DEV blob): AC1 FAIL as expected
(test absent); AC2 FAIL as expected (DEV settings: 1 entry, sender_gate=False, concierge_fence=True).

<status>pending</status>
<round>2</round>
<slot>~6</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
