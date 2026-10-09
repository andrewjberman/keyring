# TO COMM_ASSIST.TO-CA-c-1 -- round 8 CA-c-1: one verdict line says whether a day's Teams messages all reached Andrew's phone

<to_id>COMM_ASSIST.TO-CA-c-1</to_id>
<project>COMM_ASSIST</project>
<issued_to>0.9.0_WK_COMM_ASSIST~1</issued_to>
<issued_by>2.0.0_SA_COO~R</issued_by>
<issued_date>2026-10-08</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>8</round>

**Directive:** D9 | **Fabric:** laptop | **Decomp cell:** `CA-c-1` (`decompositions/COMM_ASSIST_DECOMP.round8.md`) | **outcome_ref:** FWD-3 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

`CA-c-1`. Andrew's Teams assistant (a Lambda; code in `data/transcripts/scripts/teams_chat/`) texts him a draft for each Teams
message that wants a reply. Outcome FWD-3: "for one full working day, the count of messages that came in matches the count of
texts he got or updates to texts he already had, with nothing unexplained and no refusal that failed silently".

The reader `data/transcripts/scripts/teams_chat/inbound_count.py` already counts, for one US Eastern day: received messages per
chat (from S3 bronze), `ldo_event` lines per chat, outcomes from the `tenant` log line (`{"event": "tenant", "kind", "result",
"object"?}`), `ldo_event_failed` lines, and `sms_sent` lines (`{"event": "sms_sent", "tag", "parts"}`), all as TOTALS. Read it
and its test `data/transcripts/scripts/tests/test_inbound_count.py` first. Its gap is the one that hid a real failure: a chat
outcome `texted` whose text was never sent (on 2026-10-08, 14 such outcomes; the totals showed `sms_sent=4` beside `texted=9`,
`updated=5`, and nothing flagged it).

**How the log lines relate** (read `tenant.py` `offer()`, `dispatch()`, `chat_tag()`): one chat event runs in ONE handler invocation.
If a draft is texted, `assist.send_sms` logs `sms_sent` with the chat's tag (`C` + 3 digits) BEFORE `dispatch` logs the `tenant`
line, in the same CloudWatch log stream. Other tags: `E####`/`T####` End of Day, `J###` job, `K###` confirmation, `M###` mail,
`mention`, `owner`. CloudWatch `filter_log_events` returns each event with `logStreamName`, `timestamp` and `message`. A Lambda
stream also carries `START RequestId: <id>` and `END RequestId: <id>` lines around each invocation.

### BUILD, IN THIS ORDER

1. In `inbound_count.py`, add a per-invocation pairing:
   - Read the handler's events with their `logStreamName` and `timestamp`, including the `START RequestId` and `END RequestId`
     lines (add them to the filter); group lines into invocations by stream and START/END.
   - For each `tenant` line of kind `teams.messages` whose result is `texted` or `updated`: `paired` when the SAME invocation holds
     an `sms_sent` line with a `C`-tag, else `texted_without_sms`.
   - `refusals_told` = `eod_refused` lines plus `tenant` lines with result `redraft-refused`; `failed` = `ldo_event_failed` lines
     (all kinds).
   - Print, after the existing last line, ONE verdict line, and make it the new LAST line:
     `FWD3 day=<d> received=<n> chat_events=<n> texted=<n> paired=<n> texted_without_sms=<n> unexplained=<n> failed=<n> refusals_told=<n> adds_up=<True|False>`.
     `adds_up` is True only when `texted_without_sms == 0`, `unexplained == 0` and `failed == 0`.
   - A day with no invocation boundaries readable (no START/END lines) prints `adds_up=UNKNOWN` with a reason field, never True.
   - Keep every existing count and the existing line unchanged. Print no message text.
2. NEW `data/transcripts/scripts/tests/test_fwd3_reconcile.py` (a plain script, no network; fake `logs` returning events with
   `logStreamName`, `timestamp` and `message`, across two pages; fake `s3` as in the existing test). Arms, each printing `ARM <name> ok=<True|False>`:
   - `adds_up`: two chat events texted, each with a `C`-tag `sms_sent` in its invocation -> `paired=2 texted_without_sms=0 adds_up=True`.
   - `s34_signature`: one texted outcome with no `sms_sent` in its invocation -> `texted_without_sms=1 adds_up=False`.
     **Difference control in the same arm:** add the `sms_sent` line to that invocation and it reads `adds_up=True`.
   - `other_tag_not_paired`: an `sms_sent` with tag `E1008` or `owner` in the invocation does not pair a chat outcome.
   - `failed`: one `ldo_event_failed` -> `adds_up=False`.
   - `refusal_told`: one `eod_refused` line and one `redraft-refused` tenant line -> `refusals_told=2`, and `adds_up` unaffected.
   - `streams_interleaved`: two streams whose lines interleave by timestamp pair within their own stream only.
   - `no_boundaries`: no START/END lines -> `adds_up=UNKNOWN`.
   LAST line `FWD3-RECONCILE ok=<True|False> arms=<passed>/<total>`.

### RULES FOR THIS CELL

- **Nothing you run leaves this machine**: no S3, CloudWatch, gateway, model or text call. Never run the CLI against real AWS; the
  issuer does, after the drain.
- Edit nothing but the files in `<paths>`. No message text in any output or file. No real message, person's, client's or firm's
  name in any file you write. No non-ASCII. Bake no absolute path, bucket or log group name.
- Refuse a criterion you cannot satisfy as written and report the refusal with its measurement; do not repair or widen it.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CAc1-AC1" cell_refs="CA-c-1"><invocation>python data/transcripts/scripts/tests/test_fwd3_reconcile.py</invocation><expect>FWD3-RECONCILE ok=True</expect></criterion>
`CAc1-AC1` -- the built behaviour and its difference control in one run: seven arms; S34's signature turns to `adds_up=True` when its text is added.

<criterion id="CAc1-AC2" cell_refs="CA-c-1"><invocation>python data/transcripts/scripts/tests/test_inbound_count.py</invocation><expect>INBOUND-COUNT-TEST ok=True</expect></criterion>
`CAc1-AC2` -- the cell's bound: the reader's seven existing arms (7/7 at the base, issuer's dry run) still pass. Where an existing arm asserts the old LAST line, change that arm only as far as the new last line requires and name it in your report.
</proof_of_spec>

<expected_criteria>CAc1-AC1,CAc1-AC2</expected_criteria>

Each invocation runs under `timeout 120`. Write the proof instance to
`org/missions/D9/COMM/COMM_ASSIST/deliverables/0.9.0_WK_COMM_ASSIST~1/COMM_ASSIST.TO-CA-c-1.fwd3-day-adds-up.proof_of_spec.json`,
validate it with `python .tools/proof-of-spec-check.py <instance> CAc1-AC1,CAc1-AC2`, and flip `<status>` to `complete` only when both
pass and the instance is VALID. Your surprise rows are `COMM_ASSIST-W1-S<k>`; append lines only to the investigation file and keep
its existing line endings.

<decomp_ref>
<decomp_doc>org/missions/D9/COMM/COMM_ASSIST/decompositions/COMM_ASSIST_DECOMP.round8.md</decomp_doc>
<owned_cells>CA-c-1</owned_cells>
</decomp_ref>

<paths>
data/transcripts/scripts/teams_chat/inbound_count.py
data/transcripts/scripts/tests/test_fwd3_reconcile.py
data/transcripts/scripts/tests/test_inbound_count.py
org/missions/D9/COMM/COMM_ASSIST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE the reader runs on demand, never on a clock (no monitor is built).
comp-iam: DECLARED-NOT-APPLICABLE -- denominator: 0 policies and 0 AWS calls in this cell; the issuer's real run uses the laptop's existing read identity, which read both log groups on 2026-10-08. BLIND: none claimed.
comp-adversary: RUN -- a verdict that reads True on a day the instrument could not see (no boundaries -> UNKNOWN, arm `no_boundaries`); an End of Day or owner text pairing a chat outcome (arm `other_tag_not_paired`); interleaved invocations paired across streams (arm `streams_interleaved`); a verdict that cannot move (the s34_signature arm's control); message text in output (forbidden). BLIND: a message the poll never read is invisible to this reader (the docstring already says so); the poll's own late-preview test covers it.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: PRD `prd/COMM_ASSIST_PRD.md` v0.2 (ADMITTED, `805fec22c5`), FWD-3; `1.0.0_SA_CTO` msgs 107436, 107481; row NFRA_CTLPLN-S34.
