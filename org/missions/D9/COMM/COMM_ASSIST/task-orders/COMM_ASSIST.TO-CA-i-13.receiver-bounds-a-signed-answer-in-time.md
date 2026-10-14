# TO COMM_ASSIST.TO-CA-i-13 -- round 17 CA-i-13: a signed muse answer is only good for a bounded time (CVO row COMM_ASSIST-C-S6)

<to_id>COMM_ASSIST.TO-CA-i-13</to_id>
<project>COMM_ASSIST</project>
<issued_to>0.9.0_WK_COMM_ASSIST~18</issued_to>
<issued_by>2.0.0_SA_COO~CA</issued_by>
<issued_date>2026-10-14</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>17</round>
<workstream>FRESH</workstream>

**Directive:** D9 | **Fabric:** laptop | **Decomp cell:** `CA-i-13` (`decompositions/COMM_ASSIST_DECOMP.round17.md`, AMENDMENT 5) | **outcome_ref:** FWD-7 |
**depends_on:** CA-i-10 (merged `8a480805e5`, live `eH3nihM...`)

---

## WORKER FACE

### THE CELL

The assistant's receiver (`data/transcripts/scripts/teams_chat/tenant.py`, `on_muse_reply`) now refuses a signed muse answer that is replayed or aimed at the wrong draft. A reviewer found one smaller gap: a draft with no `seq` (an End of Day draft, whose tag is `E` plus
month and day and repeats each year; a mail draft, whose tag `M000-M999` is reusable) is bound only by tag, version and a 200-entry hash window. A year-old signed End of Day `send` at version 1 would verify against that day's new draft. The signed payload already
carries `signed_at` (the time muse signed). You bound the answer in time, which closes every tag-reuse case at once.

### BUILD, IN THIS ORDER

1. Constants near `MUSE_ACTED`: `MUSE_MAX_AGE = datetime.timedelta(hours=24)` and `MUSE_SKEW = datetime.timedelta(minutes=5)` (use the module's existing `datetime` import).
2. `_muse_fields`: the signed payload MUST carry `signed_at` as a string that `assist.parse_ts` reads as a UTC time (the form `2026-10-13T22:00:00Z`); a missing or unparsable value is refused with reason `bad-payload`. Return the parsed time in the fields.
3. In `on_muse_reply`, after the signature verifies and the payload parses, and BEFORE the replay and seq checks, compare `signed_at` with the receiver's OWN clock `ctx.now()` (never the sender's envelope time): if `ctx.now() - signed_at` is more than `MUSE_MAX_AGE`, or `signed_at` is more than
   `MUSE_SKEW` after `ctx.now()`, refuse with reason `stale-signature`. A refusal is recorded as today (`state["muse_refusals"]`), sends nothing, texts nobody and changes no draft; it returns `"muse-refused"`.
4. Update the tests in `data/transcripts/scripts/tests/test_teams_chat_tenant.py` and `test_muse_verify.py`: every signed payload in a test now carries a `signed_at` near the test context's clock; add tests for `stale-signature` (too old, too far in the future), a missing `signed_at`, an unparsable one, and a payload just inside the bound.
   Existing tests must still pass. The text path (`sms.reply`) is untouched.
5. No non-ASCII. No AWS call, no network, no change outside `<paths>`.

### RULES

- Edit nothing but the files in `<paths>`. Code change with tests; NOT deployed here (a later cell deploys it under change management).
- Refuse a criterion you cannot satisfy as written and report the refusal with its measurement; do not repair or widen it.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CAi13-AC1" cell_refs="CA-i-13"><invocation>python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r17/checks/check_i13_fresh.py"</invocation><expect>I13-FRESH ok=True arms=6 of 6</expect></criterion>
`CAi13-AC1` -- the issuer's check (read it; do not edit it): real `ssh-keygen -Y sign` signatures against the receiver's clock. One hour old and 23h59m old act; 25 hours old and 10 minutes in the future are refused `stale-signature`; a missing and an unparsable `signed_at` are refused `bad-payload`; nothing is sent and the draft is untouched on a refusal. It prints ok=False at the base (2 of 6: the two controls).

<criterion id="CAi13-AC2" cell_refs="CA-i-13"><invocation>python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r17/checks/check_i10_replay.py"</invocation><expect>I10-REPLAY ok=True arms=6 of 6</expect></criterion>
`CAi13-AC2` -- the bound, a control that PASSES at the base and must still pass: the replay and seq arms (these signed payloads carry a `signed_at` one minute before the receiver's clock).

<criterion id="CAi13-AC3" cell_refs="CA-i-13"><invocation>python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r17/checks/check_i2_receiver.py"</invocation><expect>I2-RECEIVER ok=True arms=7 of 7</expect></criterion>
`CAi13-AC3` -- the bound, a control that PASSES at the base and must still pass: round 17's seven receiver arms.
</proof_of_spec>

<expected_criteria>CAi13-AC1,CAi13-AC2,CAi13-AC3</expected_criteria>

Each invocation runs from the worktree root under `timeout 120`. Write the proof instance to
`org/missions/D9/COMM/COMM_ASSIST/deliverables/0.9.0_WK_COMM_ASSIST~18/COMM_ASSIST.TO-CA-i-13.receiver-bounds-a-signed-answer-in-time.proof_of_spec.json`, validate it by running the WORKTREE'S OWN
`.tools/proof-of-spec-check.py` from inside the worktree: `python .tools/proof-of-spec-check.py <instance> CAi13-AC1,CAi13-AC2,CAi13-AC3`, and flip `<status>` to `complete` only when all three pass and the instance is VALID. Your final report names the exact reasons
returned and every test whose signed payload you had to change. Your surprise rows are `COMM_ASSIST-W18-S<k>`; append only to the investigation file and keep its existing line endings; `surfaced_at` = `date -u +%FT%TZ` at filing. Commit with `.tools/safe-commit.sh` as your serial.

<decomp_ref>
<decomp_doc>org/missions/D9/COMM/COMM_ASSIST/decompositions/COMM_ASSIST_DECOMP.round17.md</decomp_doc>
<owned_cells>CA-i-13</owned_cells>
</decomp_ref>

<paths>
data/transcripts/scripts/teams_chat/tenant.py
data/transcripts/scripts/tests/test_teams_chat_tenant.py
data/transcripts/scripts/tests/test_muse_verify.py
org/missions/D9/COMM/COMM_ASSIST/task-orders/COMM_ASSIST.TO-CA-i-13.receiver-bounds-a-signed-answer-in-time.md
org/missions/D9/COMM/COMM_ASSIST/deliverables/0.9.0_WK_COMM_ASSIST~18/
org/missions/D9/COMM/COMM_ASSIST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no grant moves and no AWS call is made.
comp-adversary: RUN -- a year-old signed answer against a recurring End of Day tag (refused: AC1 25h arm); a bound measured against the sender-written envelope time (refused: THE CELL says the receiver's own clock, and AC1 sets the envelope away from the signed time); a signed answer from the future (refused: AC1 future arm); a bound so tight it refuses a legitimate answer sent the next morning (the 24h window; AC1 just-inside arm). BLIND: muse's clock accuracy is not measured; a muse clock more than 5 minutes ahead refuses its own answers, which fails closed and visibly (the refusal is recorded).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Base: CAi13-AC1 base: FAIL as expected (2 of 6 arms: the two controls). CAi13-AC2 base: PASS as expected (control, 6 of 6). CAi13-AC3 base: PASS as expected (control, 7 of 7). AC1 green arm: PASS as expected (6 of 6) against a scratch reference guard.
Source: CVO half `deliverables/3.0.0_SA_CVO~L/NEVER_WIDEN_HALF_CVO_COMM_ASSIST_R17B_DEPLOY_20261014.md` ("Residual ... row COMM_ASSIST-C-S6"); tenant.py `eod_tag`, `mail_tag`; issuer ruling R-7 (`r17/ISSUER_RULINGS.md`).
