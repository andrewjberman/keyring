# TO COMM_ASSIST.TO-CA-j-1 -- round 18 CA-j-1: the assistant marks every event it makes for Andrew's texts, and the handler refuses (or records) an unmarked one (row COMM_ASSIST-W10-S2)

<to_id>COMM_ASSIST.TO-CA-j-1</to_id>
<project>COMM_ASSIST</project>
<issued_to>0.9.0_WK_COMM_ASSIST~19</issued_to>
<issued_by>2.0.0_SA_COO~CA</issued_by>
<issued_date>2026-10-14</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>18</round>

**Directive:** D9 | **Fabric:** laptop | **Decomp cell:** `CA-j-1` (`decompositions/COMM_ASSIST_DECOMP.round18.md`) | **outcome_ref:** FWD-7 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

Andrew answers his assistant (LDO-001, `data/transcripts/scripts/teams_chat/tenant.py`) by text. Each text becomes an event on the assistant's queue, of kind `sms.reply` (an answer to a draft) or `owner.text` (natural language), and the handler acts on it as Andrew's own word. A reviewer found that any identity
that can write to the queue can put such an event there, and the handler cannot tell it from a real one. The fix: the assistant marks each event it makes for a text with a mark that only the assistant's two functions can compute, and the handler checks it. The mark is an HMAC keyed by a secret held in Secrets Manager (the assistant's execution role already reads its secrets); an identity that can only write to the queue cannot make
one. To roll out safely, the handler checks in one of three MODES from an environment variable, so a text already in flight from the old code is never dropped by surprise.

### THE CONTRACT (fixed by the issuer; the check and the Terraform cell pin their halves)

- A new module `data/transcripts/scripts/teams_chat/ingress_mark.py`, standard library only (`hmac`, `hashlib`, `json`, `datetime`):
  - `stamp(secret, object_id, kind, payload, now)` returns a COPY of `payload` with `mark_at` (the UTC time of `now`, like `2026-10-14T03:00:00Z`) and `mark` (hex HMAC-SHA256, key = the secret, over `object_id`, `kind`, `mark_at` and the canonical JSON of the payload without `mark`: sorted keys, compact separators). The inputs are not mutated.
  - `verify(secret, object_id, kind, payload, now)` returns `"ok"`, `"no-mark"` (no `mark` or `mark_at`), `"bad-mark"` (the HMAC does not match; compare in constant time) or `"stale-mark"` (`mark_at` more than 15 minutes before `now`, or more than 5 minutes after).
  - `KINDS = ("sms.reply", "owner.text")`.
- The secret's name is a row in `data/transcripts/scripts/teams_chat/NAMES.json`: `"secrets": {"ingress_mark": "teams/global/ingress-mark"}` (the same grammar as the existing rows). The value is read with `assist.secret(assist.NAMES["secrets"]["ingress_mark"])`; type no value anywhere.
- The mode: environment variable `INGRESS_MARK_MODE`, read at CALL time, values `off` (unset or empty means off: no check at all, exactly today's behaviour), `record`, `enforce`.

### BUILD, IN THIS ORDER

1. Create `ingress_mark.py` and add the `NAMES.json` row.
2. **Stamp every producer.** In `tenant.py` there are FOUR places that send an `sms.reply` or `owner.text` event: in `_route_commands` (the ingress, two sends: `owner.text` and `sms.reply`) and in `on_owner_text` (the handler's own re-sends, two `ctx.send` of `sms.reply`; read the whole file, there may be others). Each passes its payload through ONE small helper (for example `_stamp(object_id, kind, payload)`
   returning `ingress_mark.stamp(a.secret(a.NAMES["secrets"]["ingress_mark"]), object_id, kind, payload, a.now_utc())`), with the object id and kind exactly as that send gives them. The check reads the source: every `.send(object_id, "sms.reply" | "owner.text", payload ...)` must pass a call whose name contains `stamp` as its third argument.
   Do not stamp `muse.reply` (it has its own signature) or any other kind.
3. **The gate.** In `dispatch(ctx)`, before the route runs, when the mode is not `off` and `ctx.kind` is in `KINDS`: compute `reason = verify(secret, ctx.object_id, ctx.kind, ctx.payload, ctx.now())`. If `reason` is `"ok"` and `ctx.payload["mark"]` is in `ctx.state["marks_seen"]`, the reason is `"replayed-mark"`. If the reason is `"ok"`, append the mark to `ctx.state["marks_seen"]` (keep the last 100).
   If the reason is not `"ok"`: append `{"at": <iso now>, "reason": <reason>}` to `ctx.state["mark_refusals"]` (keep the last 50), add 1 to `ctx.state["unmarked_seen"]`, and then: in `record` mode carry on and act as today; in `enforce` mode return `"unmarked-refused"` WITHOUT acting, texting or sending anything. Never log the secret, a mark or a payload.
4. Update `data/transcripts/scripts/tests/test_teams_chat_tenant.py`: the existing tests that assert the exact payload of an `sms.reply` or `owner.text` sent by the ingress (for example `test_route_text_only_from_the_owner_and_by_tag`, `test_several_tagged_replies_in_one_text`) now see `mark_at` and `mark`; update them to check the original fields and that the mark verifies. Add `test_ingress_mark.py` beside it: stamp/verify round trip, tamper, stale, replay in the gate, the three modes. Existing tests must still pass.
5. No non-ASCII. No AWS call, no network, no change outside `<paths>`.

### RULES

- Edit nothing but the files in `<paths>`. This is a code change with tests; it is NOT deployed here (later cells add the secret, set the mode and deploy it).
- If a commit gate refuses the `NAMES.json` row, file a BLOCKING row with the refusal text and stop on that criterion; do not widen.
- Refuse a criterion you cannot satisfy as written and report the refusal with its measurement; do not repair or widen it.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CAj1-AC1" cell_refs="CA-j-1"><invocation>python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r18/checks/check_j1_mark.py"</invocation><expect>J1-MARK ok=True arms=9 of 9</expect></criterion>
`CAj1-AC1` -- the issuer's check (read it; do not edit it): nine arms. The ingress's two events carry a mark that verifies; every producer site in `tenant.py` stamps; in `enforce` a marked event acts, an unmarked, a tampered, a stale and a replayed one are refused and recorded with their reasons and change nothing; in `record` an unmarked event acts and is counted; with the mode unset nothing changes. It prints ok=False at the base.

<criterion id="CAj1-AC2" cell_refs="CA-j-1"><invocation>python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r17/checks/check_i2_regression.py"</invocation><expect>I2-REGRESSION ok=True</expect></criterion>
`CAj1-AC2` -- the bound, a control that PASSES at the base and must still pass with your updated and added tests: the assistant's flow tests, the text path included.

<criterion id="CAj1-AC3" cell_refs="CA-j-1"><invocation>python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r17/checks/check_i13_fresh.py"</invocation><expect>I13-FRESH ok=True arms=6 of 6</expect></criterion>
`CAj1-AC3` -- the bound, a control that PASSES at the base and must still pass: muse's signed-answer path (its own gate, untouched by the mark).
</proof_of_spec>

<expected_criteria>CAj1-AC1,CAj1-AC2,CAj1-AC3</expected_criteria>

Each invocation runs from the worktree root under `timeout 120`. Write the proof instance to
`org/missions/D9/COMM/COMM_ASSIST/deliverables/0.9.0_WK_COMM_ASSIST~19/COMM_ASSIST.TO-CA-j-1.ingress-mark-on-the-text-driven-events.proof_of_spec.json`, validate it by running the WORKTREE'S OWN `.tools/proof-of-spec-check.py` from inside the worktree:
`python .tools/proof-of-spec-check.py <instance> CAj1-AC1,CAj1-AC2,CAj1-AC3`, and flip `<status>` to `complete` only when all three pass and the instance is VALID. Your final report names the four producer sites by function and line, the helper, the exact refusal reasons, and every existing test you changed. Your surprise rows are
`COMM_ASSIST-W19-S<k>`; append only to the investigation file and keep its existing line endings; `surfaced_at` = `date -u +%FT%TZ` at filing. Commit with `.tools/safe-commit.sh` as your serial.

<decomp_ref>
<decomp_doc>org/missions/D9/COMM/COMM_ASSIST/decompositions/COMM_ASSIST_DECOMP.round18.md</decomp_doc>
<owned_cells>CA-j-1</owned_cells>
</decomp_ref>

<paths>
data/transcripts/scripts/teams_chat/ingress_mark.py
data/transcripts/scripts/teams_chat/tenant.py
data/transcripts/scripts/teams_chat/NAMES.json
data/transcripts/scripts/tests/test_teams_chat_tenant.py
data/transcripts/scripts/tests/test_ingress_mark.py
org/missions/D9/COMM/COMM_ASSIST/task-orders/COMM_ASSIST.TO-CA-j-1.ingress-mark-on-the-text-driven-events.md
org/missions/D9/COMM/COMM_ASSIST/deliverables/0.9.0_WK_COMM_ASSIST~19/
org/missions/D9/COMM/COMM_ASSIST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no grant moves and no AWS call is made; the secret resource and the deploy are cells CA-j-2 and CA-j-3.
comp-adversary: RUN -- a mark that covers only the ingress and so makes the handler's own re-sends look forged (refused: the check reads every producer site); a mark that does not bind the payload, so an action can be changed after marking (refused: AC1 tamper arm); a captured mark replayed with a new event id (refused: AC1 stale and replayed arms); enforcement the moment it is deployed, dropping a text in flight (refused: the three modes; `off` is today's behaviour, `record` acts); a secret, mark or payload in a log (refused: build step 3). BLIND: whether the live secret can be read by the two functions' execution role (cell CA-j-2 adds it to `secret_arns`; the live read is cell CA-j-3's check).
naming: one NAMES.json row in the existing grammar {system}/{scope}/{purpose}; the secret resource is created in CA-j-2 from that row (CLAUDE.md rule 30).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Base: CAj1-AC1 base: FAIL as expected (no ingress_mark module). CAj1-AC2 base: PASS as expected (control). CAj1-AC3 base: PASS as expected (control, 6 of 6). AC1 green arm: PASS as expected (9 of 9) against a scratch reference built in a throwaway worktree (module, NAMES row, four stamped sites, the gate), then removed; the reference first scored 8 of 9 because it had stamped only three of the four producer sites, which is what the check's source-reading arm is for.
Source: CTO round-17 analysis `ledger/ROUND_ANALYSIS.round17.md` section 2 and item 1; CTO ruling `CTO_RULING_20261013_231xZ_COMM_ASSIST_SMS_FORGERY_AND_J290_DRAFTS.md`; worker row COMM_ASSIST-W10-S2; tenant.py `_route_commands`, `on_owner_text`, `dispatch`.
