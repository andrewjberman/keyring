# TO COMM_ASSIST.TO-CA-i-6 -- round 17 CA-i-6: the assistant's agentbus sends carry from_tailnet=ldo-001 (Andrew-direct ~22:3xZ; round-16 analysis addendum item 6)

<to_id>COMM_ASSIST.TO-CA-i-6</to_id>
<project>COMM_ASSIST</project>
<issued_to>0.9.0_WK_COMM_ASSIST~12</issued_to>
<issued_by>2.0.0_SA_COO~CA</issued_by>
<issued_date>2026-10-13</issued_date>
<status>complete</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>17</round>
<workstream>LDO001FIX</workstream>

**Directive:** D9 | **Fabric:** laptop | **Decomp cell:** `CA-i-6` (`decompositions/COMM_ASSIST_DECOMP.round17.md`, AMENDMENT 1) | **outcome_ref:** FWD-8 (agentbus honesty), the item-6 line of the round-16 analysis |
**depends_on:** none

---

## WORKER FACE

### THE CELL

Andrew's assistant (LDO-001) sends messages onto the agent bus (job offers, awards, closes) from `bus_send` in
`data/transcripts/scripts/teams_chat/assist.py`. Every message on the bus is meant to carry a message attribute `from_tailnet` naming the sender's tailnet
name; the boxes' consumer checks it against the device register (`org/devices/DEVICES.json`, the `senders` list) and today prints
`WARN agentbus unstamped sender=LDO-001` because the assistant sends no such attribute. The register now holds the sender `ldo-001`.
You make the assistant stamp its sends. Nothing else changes.

### BUILD

1. In `bus_send` (assist.py, near line 989) add a message attribute `from_tailnet` with `StringValue` the lower-case of `BUS_FROM` (`ldo-001`; derive it from
   `BUS_FROM`, do not type the name) and `DataType` `String`, beside the existing `from` and `sent_at` attributes. The existing attributes, the body and the
   group id stay exactly as they are.
2. Add a small test file `data/transcripts/scripts/tests/test_bus_stamp.py` (plain pytest, no network): `bus_send` through a recording stand-in for the SQS
   client sends exactly one message whose attributes include `from_tailnet` equal to `ldo-001`, and `ldo-001` is a name `lib/devices.py` `held_tailnet_names`
   reports for the repository's register.
3. Edit nothing else. No non-ASCII.

### RULES

- Edit nothing but the files in `<paths>`. This is a code change with a test; it reaches AWS only when a later cell rebuilds and deploys the assistant.
- Refuse a criterion you cannot satisfy as written and report the refusal with its measurement; do not repair or widen it.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CAi6-AC1" cell_refs="CA-i-6"><invocation>python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r17/checks/check_i6_stamp.py"</invocation><expect>I6-STAMP ok=True</expect></criterion>
`CAi6-AC1` -- the issuer's check (read it; do not edit it): the message the assistant sends is classified `deliver` by the agentbus consumer's own rule against this checkout's register, and the control (a name the register does not hold) is `refused`. It prints ok=False at the base (`unstamped`).

<criterion id="CAi6-AC2" cell_refs="CA-i-6"><invocation>python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r17/checks/check_i2_regression.py"</invocation><expect>I2-REGRESSION ok=True</expect></criterion>
`CAi6-AC2` -- the bound, a control that PASSES at the base and must still pass: the assistant's flow tests.
</proof_of_spec>

<expected_criteria>CAi6-AC1,CAi6-AC2</expected_criteria>

Each invocation runs from the worktree root under `timeout 120`. Write the proof instance to
`org/missions/D9/COMM/COMM_ASSIST/deliverables/0.9.0_WK_COMM_ASSIST~12/COMM_ASSIST.TO-CA-i-6.ldo001-stamps-its-agentbus-sends.proof_of_spec.json`, validate it by
running the WORKTREE'S OWN `.tools/proof-of-spec-check.py` from inside the worktree: `python .tools/proof-of-spec-check.py <instance> CAi6-AC1,CAi6-AC2`, and flip
`<status>` to `complete` only when both pass and the instance is VALID. Your final report names the exact lines you changed. Your surprise rows are
`COMM_ASSIST-W12-S<k>`; append only to the investigation file and keep its existing line endings; `surfaced_at` = `date -u +%FT%TZ` at filing. Commit with
`.tools/safe-commit.sh` as your serial.

<decomp_ref>
<decomp_doc>org/missions/D9/COMM/COMM_ASSIST/decompositions/COMM_ASSIST_DECOMP.round17.md</decomp_doc>
<owned_cells>CA-i-6</owned_cells>
</decomp_ref>

<paths>
data/transcripts/scripts/teams_chat/assist.py
data/transcripts/scripts/tests/test_bus_stamp.py
org/missions/D9/COMM/COMM_ASSIST/task-orders/COMM_ASSIST.TO-CA-i-6.ldo001-stamps-its-agentbus-sends.md
org/missions/D9/COMM/COMM_ASSIST/deliverables/0.9.0_WK_COMM_ASSIST~12/
org/missions/D9/COMM/COMM_ASSIST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no grant moves; no AWS call is made here.
comp-adversary: RUN -- a stamp typed as a literal (refused: derive from BUS_FROM); a stamp the register does not hold (refused: AC1 asks the consumer's own rule); a changed existing attribute (refused: AC1 compares from); a stamped send that the real consumer would drop (refused: the control arm shows the consumer does refuse an unheld name). BLIND: the real bid delivered with no WARN is read after the deploy, not here.
lane: the <paths> block IS the grant (worker RULING 1). DIRECT-ACT: one cell, a few lines, LOCAL; it runs no L8-L10 and its close is the issuer's one real run.
</preflight>

Base: CAi6-AC1 base: FAIL as expected (unstamped); CAi6-AC2 base: PASS as expected (control, 19 passed at the issuance, 46 with the round-17 tests). AC1 green arm: PASS as expected against a scratch reference stamp.
Source: Andrew-direct ~22:3xZ via 0.0.0_AB_MSTR msg 108965; CTO msg 108970 and the round-16 analysis addendum item 6 (`ledger/ROUND_ANALYSIS.round16.md`, commit e6e0464bbc); `.tools/agentbus-consumer.py` lines 70-110.
