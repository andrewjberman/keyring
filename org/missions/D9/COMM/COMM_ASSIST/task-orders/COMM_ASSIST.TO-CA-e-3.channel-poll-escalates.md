# TO COMM_ASSIST.TO-CA-e-3 -- round 13 CA-e-3: channel_poll names its failure and raises it, and the live failure is ruled

<to_id>COMM_ASSIST.TO-CA-e-3</to_id>
<project>COMM_ASSIST</project>
<issued_to>0.9.0_WK_COMM_ASSIST~7</issued_to>
<issued_by>2.0.0_SA_COO~ZZ</issued_by>
<issued_date>2026-10-10</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>13</round>

**Directive:** D9 | **Fabric:** site-z | **Decomp cell:** `CA-e-3` (`decompositions/COMM_ASSIST_DECOMP.round13.md`) | **outcome_ref:** FWD-3 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

`CA-e-3`. Andrew's assistant runs an ingress Lambda once a minute (`teams-global-chat-assist-ingress-lambda`, us-east-1). Each
run calls several steps through `_safe(step, fn)` in `data/transcripts/scripts/teams_chat/tenant.py` (read lines 1169-1199): a
step that RAISES is logged as `ingress_step_failed` with its error; a step that returns is not.

The `channels` step is `poll()` in `data/transcripts/scripts/teams_chat/channel_mentions.py` (read the whole file, 206 lines).
It catches every `a.GatewayError` (defined in `data/transcripts/scripts/teams_chat/assist.py`), adds 1 to `failed`, and returns
normally. Live, every invocation logs `{"event": "channel_poll", "failed": 1, "channels": 0, "mentions": 0, "read": 0}`
(63 of 63 in the hour before 2026-10-09 18:33Z, and continuing). So channel @mentions of Andrew are not being read, the log
never says why, and the failure never escalates.

### BUILD, IN THIS ORDER

1. `channel_mentions.py` only:
   - every caught `GatewayError` records a short error description (the failing call, the status, the error code or message
     from the exception's own attributes; at most 200 characters; NEVER any message content);
   - the `channel_poll` log line gains a field `error`: the first failure's description, or absent/empty when `failed` is 0;
   - after the cursors are saved and the `channel_poll` line is logged, if `failed > 0` the function RAISES an exception whose
     text is that description, so `_safe` logs `ingress_step_failed` with step `channels`. Work done before the raise (events
     sent, cursors of channels read successfully) is kept. A healthy poll raises nothing and returns as today.
2. Update `data/transcripts/scripts/tests/test_inbound_channel_mentions.py` ONLY where an existing arm asserted the old
   return-on-failure behaviour; keep every other arm as it is.
3. READ the live failure (read-only; no write to AWS): the last hour of `/aws/lambda/teams-global-chat-assist-ingress-lambda`
   (us-east-1) filtered on `channel_poll`, with the count of lines and the count with `failed` = 1 (print the denominator).
   Use the `.tools/aws` shim (`bash .tools/aws logs filter-log-events ...`, bounded with `--start-time` and `--max-items`).
   Then read the gateway's channel routes in `infra/aws/ec2/opal-gateway/app/` (which routes serve `teams`, `channels` and
   `channel_messages`, and whether they exist there) to name which call most plausibly fails.
4. Write `CHANNEL_POLL_RULING.md` in your deliverables folder: the live counts with their denominator; the failing call as far
   as the evidence goes, and how sure (the deployed code logs no error text, so say what the new `error` field will show after
   the next deploy); whether a fix is inside COMM's own code or depends on the gateway (another project); and the outcome
   that depends on the step: FWD-3's "every Teams message reaches his phone" for channel @mentions. Then append ONE surprise
   row `COMM_ASSIST-W7-S1` (class OBSERVATION, hazard_standing INERT, disarm_owner `2.0.0_SA_COO~ZZ`) whose `world_is`
   names that dependent outcome and cites `COMM_ASSIST-Z-S6`. Copy an existing row's field set from the investigation file;
   do not invent field names.

### RULES FOR THIS CELL

- Edit nothing but the files in `<paths>`. AWS: the one `logs filter-log-events` read only; no deploy, no apply, no other call.
- Never put message content in a log field, a file or a row.
- No non-ASCII. Bake no absolute path.
- Refuse a criterion you cannot satisfy as written and report the refusal with its measurement; do not repair or widen it.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CAe3-AC1" cell_refs="CA-e-3"><invocation>python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~ZZ/r13/checks/check_e3_channel_poll_escalates.py"</invocation><expect>E3-ESCALATES ok=True</expect></criterion>
`CAe3-AC1` -- the issuer's check (read it; do not edit it): a forced gateway failure puts a non-empty `error` on the `channel_poll` line and `_safe` logs `ingress_step_failed` for `channels`; the control, a healthy poll, logs failed=0 and raises nothing. It prints ok=False at the base.

<criterion id="CAe3-AC2" cell_refs="CA-e-3"><invocation>python data/transcripts/scripts/tests/test_inbound_channel_mentions.py</invocation><expect>CHANNEL-MENTIONS ok=True</expect></criterion>
`CAe3-AC2` -- the bound: the channel-mention arms still pass (an arm changed under BUILD 2 is named in your report).

<criterion id="CAe3-AC3" cell_refs="CA-e-3" judgment="true"/>
`CAe3-AC3` -- JUDGMENT, never self-graded: `CHANNEL_POLL_RULING.md` and row W7-S1 name the dependent outcome, carry the live counts with their denominator, and say plainly what is and is not established about the failing call.
</proof_of_spec>

<expected_criteria>CAe3-AC1,CAe3-AC2,CAe3-AC3</expected_criteria>

Each invocation runs under `timeout 120`. Record `CAe3-AC3` with NO verdict (status `UNVERIFIABLE-BY-INSTRUMENT`, the reason
naming `3.0.0_SA_CVO`). Write the proof instance to
`org/missions/D9/COMM/COMM_ASSIST/deliverables/0.9.0_WK_COMM_ASSIST~7/COMM_ASSIST.TO-CA-e-3.channel-poll-escalates.proof_of_spec.json`,
validate it with `python .tools/proof-of-spec-check.py <instance> CAe3-AC1,CAe3-AC2,CAe3-AC3`, and flip `<status>` to `complete`
only when both mechanical criteria pass and the instance is VALID. Your surprise rows are `COMM_ASSIST-W7-S<k>`; append only to
the investigation file and keep its existing line endings.

<decomp_ref>
<decomp_doc>org/missions/D9/COMM/COMM_ASSIST/decompositions/COMM_ASSIST_DECOMP.round13.md</decomp_doc>
<owned_cells>CA-e-3</owned_cells>
</decomp_ref>

<paths>
data/transcripts/scripts/teams_chat/channel_mentions.py
data/transcripts/scripts/tests/test_inbound_channel_mentions.py
org/missions/D9/COMM/COMM_ASSIST/task-orders/COMM_ASSIST.TO-CA-e-3.channel-poll-escalates.md
org/missions/D9/COMM/COMM_ASSIST/deliverables/0.9.0_WK_COMM_ASSIST~7/
org/missions/D9/COMM/COMM_ASSIST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing (the ingress keeps its 1-minute clock).
comp-iam: DECLARED-NOT-APPLICABLE no grant moves; one read-only logs call under the seat's existing identity.
comp-adversary: RUN -- a raise before the cursors are saved (refused: BUILD 1 orders it after put_json and the log line); message content in `error` (refused); a raise on a healthy poll (AC1's control arm); a change to tenant.py (not in <paths>). BLIND: whether the gateway serves the channel routes is another project's state; the cell rules on it in writing and fixes nothing there.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Base `a89f5575b1`: CAe3-AC1 base: FAIL as expected (error_field=None, ingress_step_failed=0; control PASS); CAe3-AC2 base: PASS as expected (7/7).
Source: CTO round-12 analysis `ledger/ROUND_ANALYSIS.round12.md` @82f10ddf63 E3; row `COMM_ASSIST-Z-S6`; CVO C-S3 (Z-S6 graduated).
