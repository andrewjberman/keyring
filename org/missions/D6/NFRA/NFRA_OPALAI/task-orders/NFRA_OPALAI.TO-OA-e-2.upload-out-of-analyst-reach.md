# NFRA_OPALAI task order -- `OA-e-2` -- ROUND 2, E2: the upload drops out of the Analyst's reach

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_OPALAI/decompositions/NFRA_OPALAI_DECOMP.md</decomp_doc>
<owned_cells>OA-e-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPALAI~11</issued_to>
<issued_by>2.0.0_SA_COO~AI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- nothing reaches AWS.
comp-adversary: DECLARED-NOT-APPLICABLE -- the fence's deny arm and its pass control are the adversary read.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OA-e-2` (round 2, decomposition section R2.1)

The Opal Analyst is a Teams-facing agent that will run as a separate Windows account, `Opal_Agent`, from a read-only
checkout of the `opal_ai` repository. Its product files live in `opal_ai/opal/agent/`. The gateway tool
`opal_data_refresh_upload` fires the Bloomberg data pipeline. It is the OPERATOR's duty: a daily scheduled script
(`publish_to_portal.py`) does the upload off the gateway, and the gateway already admits the tool to the operator's own
OAuth client only. The Analyst must never hold it (Andrew's option 2 and his call-6 answer; rows Z-S18/Z-S19). Two
places still give it to the Analyst, and this cell removes both:

1. **The runtime fence** `opal_ai/opal/agent/hooks/concierge-gate.sh` (a Claude Code `PreToolUse` hook; it denies with
   the JSON `"permissionDecision":"deny"` and exit 0). Its G4 block denies email and site writes on
   `mcp__opal-gateway-bbg__*` but has NO line for the upload. Add `mcp__opal-gateway-bbg__opal_data_refresh_upload` to G4
   as a DENY, with a plain reason (the upload is the operator's daily script, never the Analyst's). Add a deny arm for it
   to `opal_ai/opal/agent/hooks/test_concierge_gate.sh` (its `run DENY ...` form). G1, G2 and G3, and every other G4
   line, are unchanged.
2. **The Analyst's runbook** `opal_ai/opal/agent/refs/RELAUNCH.md`. Line 81 lists `opal_data_refresh_upload` among the
   seat's six "hot gateway tools", and lines 124-128 ("DAILY UPLOAD GUARDRAIL DUTY") give the seat a fallback
   `/terminal-upload` and call the upload row its capability. Rewrite those lines so that:
   - no line names `/terminal-upload`;
   - every line that still names `opal_data_refresh_upload` says it is NOT the Analyst's (the word `never` or `not` on
     that line);
   - the upload is named as the operator's daily script `publish_to_portal.py`, and a missed run is reported to Andrew,
     never repaired by the Analyst.
   Change nothing else in the file.

## 2. BOUNDS

1. **`opal_ai` is a nested repository** at `<worktree>/opal_ai`, on its own branch off `opal_ai` `fd8ab8a57f` (origin
   PROD at the cut). Commit your nested files there with `git -C opal_ai commit --author "0.9.0_WK_NFRA_OPALAI~11
   <0.9.0_WK_NFRA_OPALAI~11@opal.agent>" -F <msgfile> -- <nested paths>`, the msgfile written with the Write tool.
   Commit your deliverables in the parent with `safe-commit.sh` as usual.
2. Not yours: `opal_ai/opal/agent/prompt.md` (its hard lines), `REQUEST_CATALOG.md`, every other ref, and the gateway.
3. Standing: no push, no install, no vendor call, no AWS. REFUSE a criterion you cannot meet as written, and report the
   refusal with its measurement. Never repair a criterion, widen it, or meet it by a route this face does not name.

## 3. SURFACES

<paths>
opal_ai/opal/agent/hooks/concierge-gate.sh
opal_ai/opal/agent/hooks/test_concierge_gate.sh
opal_ai/opal/agent/refs/RELAUNCH.md
org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~11/**
org/missions/D6/NFRA/NFRA_OPALAI/surprise-channel/investigations/**
</paths>

Rows: `org/missions/D6/NFRA/NFRA_OPALAI/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, id
`NFRA_OPALAI-Z-W11-S<k>` (next free k for W11).

## 4. PROOF OF SPEC (literal; run from your worktree root, after BOTH repos are committed)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OA-e-2"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~AI/round2/checks/e2.AC1.sh; echo "exit=$?"</invocation><expect>upload=DENY read_chat_messages=PASS send_email=DENY; fence test names upload>=1; fence test 'RESULT: N passed, 0 failed ...' -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OA-e-2"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~AI/round2/checks/e2.AC2.sh; echo "exit=$?"</invocation><expect>/terminal-upload=0; upload lines without never/not=0; publish_to_portal.py>=1 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OA-e-2"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~AI/round2/checks/e2.AC3.sh; echo "exit=$?"</invocation><expect>files changed outside the cell's three=0; fence lines removed outside G4=0 -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~11/NFRA_OPALAI.TO-OA-e-2.upload-out-of-analyst-reach.proof_of_spec.json`.
Report once: what you changed and where (the new G4 line and the RELAUNCH.md lines, before and after), the commit hashes
in BOTH repos, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** E2 (rows Z-S18/Z-S19; Andrew's option 2, call 6). Chain B head; the slot continues with OA-t-3 (the
cutover fence is graded after this deny lands). A cutover precondition, belt-and-braces to OA-f-2's server-side client
binding. The nested branch merges into `opal_ai` DEV at the cutover window (decomp R2.4), before G-PUSH.

SPAWN ONLY WHEN: at the cut (no precondition). Slot `~11`, nested worktree `--nested opal_ai=fd8ab8a57f`.

Dry-run at base (main tree, CLOUD `c8df03c408`; `OA_NESTED_REF=fd8ab8a57f` reads the worker's true nested base):
- e2.AC1 base: FAIL as expected (HEAD: fence absent at the stale gitlink 90ca424; fd8ab8a57f: `upload=PASS
  read_chat_messages=PASS send_email=DENY; fence test names upload=0; 27 passed, 0 failed` -- the fence does NOT deny
  the upload today, row Z-S19 reproduced).
- e2.AC2 base: FAIL as expected (fd8ab8a57f: `/terminal-upload=1; upload lines=2, of which without never/not=2;
  publish_to_portal.py=0`).
- e2.AC3 base: PASS as expected at fd8ab8a57f (bound: 0 files changed); FAIL at the stale gitlink HEAD, which is not
  the worker's base.

<status>pending</status>
<round>2</round>
<slot>~11</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
