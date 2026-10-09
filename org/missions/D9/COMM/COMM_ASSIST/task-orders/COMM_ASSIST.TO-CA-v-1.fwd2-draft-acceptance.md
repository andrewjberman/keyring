# TO COMM_ASSIST.TO-CA-v-1 -- round 10 CA-v-1: one line says how often Andrew sends a draft as written

<to_id>COMM_ASSIST.TO-CA-v-1</to_id>
<project>COMM_ASSIST</project>
<issued_to>0.9.0_WK_COMM_ASSIST~4</issued_to>
<issued_by>2.0.0_SA_COO~R</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>10</round>

**Directive:** D9 | **Fabric:** laptop | **Decomp cell:** `CA-v-1` (`decompositions/COMM_ASSIST_DECOMP.round10.md`) | **outcome_ref:** FWD-2 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

`CA-v-1`. Andrew's assistant (code in `data/transcripts/scripts/teams_chat/`) texts him a draft reply for a Teams chat message.
He answers by text: `1` sends it, notes redraft it (a new version is texted), `0` drops it, or he answers in Teams himself. The
outcome FWD-2 says: "he sends them with few or no changes". Nothing measures that today.

The reader `data/transcripts/scripts/teams_chat/inbound_count.py` (read it first, with its tests `test_inbound_count.py` and
`test_fwd3_reconcile.py`) already reads, for one US Eastern day, every handler log line, including the `tenant` lines
`{"event": "tenant", "kind", "result", "object": <hash>}`. Each object is one chat or one End of Day post. For a chat object, the
lines of one draft are, in time order: `teams.messages` -> `texted`; then zero or more `sms.reply` -> `redrafted`; then one of
`sms.reply` -> `sent`, `sms.reply` -> `dropped` or `cancelled`, or `teams.messages` -> `answered-by-hand` (he answered in Teams);
or nothing yet (still open). A new draft on the same object starts at the next `texted`. Read `tenant.on_chat_messages` and
`tenant.on_sms_reply` for the exact result strings and use the ones the code returns. Lines without `object` (written before
2026-10-08 21:48Z) cannot be joined.

### BUILD, IN THIS ORDER

1. In `inbound_count.py`, from the `tenant` lines that carry `object`, join each chat object's lines in time order into drafts, as
   above. Count only chat drafts: an object whose lines include an End of Day kind (`eod.`) is skipped. Print ONE line,
   immediately BEFORE the existing `FWD3` line, which stays the LAST line:
   `FWD2 day=<d> drafts=<n> sent=<n> sent_as_written=<n> sent_after_redraft=<n> redrafts=<n> dropped=<n> answered_by_hand=<n> open=<n> unjoinable=<n>`.
   `sent_as_written` = sent with 0 redrafts; `redrafts` = the total redraft count; `unjoinable` = `tenant` lines of a chat kind
   with no `object`. Print no message text. Keep every existing count and line unchanged.
2. NEW `data/transcripts/scripts/tests/test_fwd2_acceptance.py` (a plain script, no network; fakes shaped like the existing tests').
   Arms, each printing `ARM <name> ok=<True|False>`:
   - `as_written`: texted then sent -> `sent=1 sent_as_written=1`.
   - `after_redraft`: texted, redrafted twice, sent -> `sent_after_redraft=1 redrafts=2`. **Difference control in the same arm:**
     remove the two redraft lines and it reads `sent_as_written=1`.
   - `dropped_and_by_hand`: one draft dropped, one answered in Teams -> `dropped=1 answered_by_hand=1`.
   - `two_drafts_one_chat`: texted, sent, texted, sent on one object -> `drafts=2 sent=2`.
   - `eod_skipped`: an End of Day object's texted/approved/posted lines are not counted.
   - `unjoinable`: `tenant` lines with no `object` count only in `unjoinable`.
   - `fwd3_still_last`: the `FWD3` line is still the last line and `FWD2` is the line before it.
   LAST line `FWD2-ACCEPTANCE ok=<True|False> arms=<passed>/<total>`.

### RULES FOR THIS CELL

- **Nothing you run leaves this machine**: no S3, CloudWatch, gateway, model or text call. Never run the CLI against real AWS.
- Edit nothing but the files in `<paths>`; keep the existing tests passing, changing an existing case only where the new line
  requires it, named in your report. No message text in any output or file. No real name. No non-ASCII. No absolute path.
- Refuse a criterion you cannot satisfy as written and report the refusal with its measurement; do not repair or widen it.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CAv1-AC1" cell_refs="CA-v-1"><invocation>python data/transcripts/scripts/tests/test_fwd2_acceptance.py</invocation><expect>FWD2-ACCEPTANCE ok=True</expect></criterion>
`CAv1-AC1` -- the built behaviour and its difference control in one run: seven arms.

<criterion id="CAv1-AC2" cell_refs="CA-v-1"><invocation>python data/transcripts/scripts/tests/test_fwd3_reconcile.py</invocation><expect>FWD3-RECONCILE ok=True</expect></criterion>
`CAv1-AC2` -- the bound: the FWD3 verdict's seven arms (7/7 at the base) still pass.

<criterion id="CAv1-AC3" cell_refs="CA-v-1"><invocation>python data/transcripts/scripts/tests/test_inbound_count.py</invocation><expect>INBOUND-COUNT-TEST ok=True</expect></criterion>
`CAv1-AC3` -- the bound: the reader's seven existing arms (7/7 at the base) still pass.
</proof_of_spec>

<expected_criteria>CAv1-AC1,CAv1-AC2,CAv1-AC3</expected_criteria>

Each invocation runs under `timeout 120`. Write the proof instance to
`org/missions/D9/COMM/COMM_ASSIST/deliverables/0.9.0_WK_COMM_ASSIST~4/COMM_ASSIST.TO-CA-v-1.fwd2-draft-acceptance.proof_of_spec.json`,
validate it with `python .tools/proof-of-spec-check.py <instance> CAv1-AC1,CAv1-AC2,CAv1-AC3`, and flip `<status>` to `complete`
only when all three pass and the instance is VALID. Your surprise rows are `COMM_ASSIST-W4-S<k>`; append lines only to the
investigation file and keep its existing line endings.

<decomp_ref>
<decomp_doc>org/missions/D9/COMM/COMM_ASSIST/decompositions/COMM_ASSIST_DECOMP.round10.md</decomp_doc>
<owned_cells>CA-v-1</owned_cells>
</decomp_ref>

<paths>
data/transcripts/scripts/teams_chat/inbound_count.py
data/transcripts/scripts/tests/test_fwd2_acceptance.py
data/transcripts/scripts/tests/test_fwd3_reconcile.py
data/transcripts/scripts/tests/test_inbound_count.py
org/missions/D9/COMM/COMM_ASSIST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE the reader runs on demand, never on a clock (no monitor is built).
comp-iam: DECLARED-NOT-APPLICABLE -- denominator: 0 policies and 0 AWS calls in this cell.
comp-adversary: RUN -- End of Day approvals counted as chat drafts (arm `eod_skipped`); two drafts on one chat merged (arm `two_drafts_one_chat`); pre-hash lines silently dropped instead of counted (arm `unjoinable`); the FWD3 verdict displaced from the last line (arm `fwd3_still_last`); a count that cannot move (the after_redraft control). BLIND: "few changes" inside a sent draft he edited in Teams is not visible to the logs; only redrafts by text are.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: PRD `prd/COMM_ASSIST_PRD.md` v0.2 (ADMITTED, `805fec22c5`), FWD-2; `1.0.0_SA_CTO` msg 107513.
