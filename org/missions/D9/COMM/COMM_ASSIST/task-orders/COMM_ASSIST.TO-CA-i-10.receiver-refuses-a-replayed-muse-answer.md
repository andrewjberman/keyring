# TO COMM_ASSIST.TO-CA-i-10 -- round 17 CA-i-10: a signed muse answer cannot be replayed against a later draft (CVO row COMM_ASSIST-C-S5)

<to_id>COMM_ASSIST.TO-CA-i-10</to_id>
<project>COMM_ASSIST</project>
<issued_to>0.9.0_WK_COMM_ASSIST~16</issued_to>
<issued_by>2.0.0_SA_COO~CA</issued_by>
<issued_date>2026-10-14</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>17</round>
<workstream>REPLAY</workstream>

**Directive:** D9 | **Fabric:** laptop | **Decomp cell:** `CA-i-10` (`decompositions/COMM_ASSIST_DECOMP.round17.md`, AMENDMENT 4) | **outcome_ref:** FWD-7 |
**depends_on:** CA-i-2 (merged @eac776ff43)

---

## WORKER FACE

### THE CELL

The assistant's receiver (`data/transcripts/scripts/teams_chat/tenant.py`, `on_muse_reply`, `_muse_fields`) acts on a muse answer when its signature verifies against muse's pinned key. A reviewer found a hole: a chat's tag
(`C123`) is stable, and after a draft is sent the NEXT draft under that chat starts again at version 1, so an old signed answer `{"tag":"C123","action":"send","version":1}` still verifies against a LATER draft Andrew never
saw, and `_muse_fields` accepts an answer that carries no version at all. Signed answers will sit in a folder the dell2 agents' account can read, and that account can put a `muse.reply` on the queue itself. You close the hole
in the receiver. Every chat draft carries `seq` (`assign_seq`, tenant.py around line 119): a number that never repeats on its chat. A job or End of Day draft carries no seq (its tag is unique).

### BUILD, IN THIS ORDER

1. `_muse_fields`: the signed payload MUST carry `version` as a whole number (not a bool) for every action; without it the answer is refused with reason `bad-payload`. It may carry `seq` (a whole number or null).
2. In `on_muse_reply`, after the signature verifies and the payload parses, BEFORE the answer is run through `on_sms_reply`, in this order:
   - **Replay record.** Compute `h = sha256( payload_text + "\n" + signature_text )` (hex). If `h` is in `ctx.state["muse_acted"]`, refuse with reason `replayed`.
   - **Seq binding.** Let `pending` be `ctx.state.get("pending")`. If `pending` exists and carries a `seq`, the answer's `seq` must be equal to it; a missing or different `seq` is refused with reason `seq-mismatch`. If `pending` carries
     no `seq`, the answer is not seq-checked (a job or End of Day draft, or a draft made before seq existed).
3. A refusal is recorded exactly as today (`ctx.state["muse_refusals"]`, last 50, the new reasons included), sends nothing, texts nobody and changes no draft; it returns `"muse-refused"`.
4. After the delegated call, if it ACTED (its result is one of the words that mean the draft moved: `sent`, `dropped`, `redrafted`, `approved`, `posted`, `mail-approved`, `job-opened`; read `on_sms_reply` and `mail_requests.on_mail_reply` for the
   full set), append `h` to `ctx.state["muse_acted"]`, keeping the last 200. A result that did not act (`unseen`, `nothing-open`, `asked`, a refusal) records nothing.
5. Update `data/transcripts/scripts/tests/test_teams_chat_tenant.py` and `test_muse_verify.py`: any test whose signed payload lacks `version` now expects `bad-payload`; add tests for `replayed`, `seq-mismatch`, a seqless pending, and an answer
   that carries `seq`. Existing tests must still pass. The text path (`sms.reply`) is untouched.
6. No non-ASCII. No AWS call, no network, no change outside `<paths>`.

### RULES

- Edit nothing but the files in `<paths>`. This is a code change with tests; it is NOT deployed here (a later cell deploys it under change management).
- Refuse a criterion you cannot satisfy as written and report the refusal with its measurement; do not repair or widen it.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CAi10-AC1" cell_refs="CA-i-10"><invocation>python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r17/checks/check_i10_replay.py"</invocation><expect>I10-REPLAY ok=True arms=6 of 6</expect></criterion>
`CAi10-AC1` -- the issuer's check (read it; do not edit it): real `ssh-keygen -Y sign` signatures. A correct answer acts once; the same signed bytes replayed are refused `replayed`; an old signature aimed at a NEW draft under the same tag is refused and the new draft is untouched; a payload with no version is refused `bad-payload`; a payload with no seq against a draft that has one is refused `seq-mismatch`; a draft with no seq still works (control). It prints ok=False at the base (2 of 6: the two controls).

<criterion id="CAi10-AC2" cell_refs="CA-i-10"><invocation>python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r17/checks/check_i2_receiver.py"</invocation><expect>I2-RECEIVER ok=True arms=7 of 7</expect></criterion>
`CAi10-AC2` -- the bound, a control that PASSES at the base and must still pass: round 17's own seven receiver arms (the check now signs the draft's seq too).

<criterion id="CAi10-AC3" cell_refs="CA-i-10"><invocation>python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r17/checks/check_i2_regression.py"</invocation><expect>I2-REGRESSION ok=True</expect></criterion>
`CAi10-AC3` -- the bound, a control that PASSES at the base: the assistant's flow tests, the text path included.
</proof_of_spec>

<expected_criteria>CAi10-AC1,CAi10-AC2,CAi10-AC3</expected_criteria>

Each invocation runs from the worktree root under `timeout 120`. Write the proof instance to
`org/missions/D9/COMM/COMM_ASSIST/deliverables/0.9.0_WK_COMM_ASSIST~16/COMM_ASSIST.TO-CA-i-10.receiver-refuses-a-replayed-muse-answer.proof_of_spec.json`, validate it by running the WORKTREE'S OWN
`.tools/proof-of-spec-check.py` from inside the worktree: `python .tools/proof-of-spec-check.py <instance> CAi10-AC1,CAi10-AC2,CAi10-AC3`, and flip `<status>` to `complete` only when all three pass and the instance is VALID. Your final
report names the exact reasons returned and the set of result words you treated as "acted". Your surprise rows are `COMM_ASSIST-W16-S<k>`; append only to the investigation file and keep its existing line endings; `surfaced_at` =
`date -u +%FT%TZ` at filing. Commit with `.tools/safe-commit.sh` as your serial.

<decomp_ref>
<decomp_doc>org/missions/D9/COMM/COMM_ASSIST/decompositions/COMM_ASSIST_DECOMP.round17.md</decomp_doc>
<owned_cells>CA-i-10</owned_cells>
</decomp_ref>

<paths>
data/transcripts/scripts/teams_chat/tenant.py
data/transcripts/scripts/tests/test_teams_chat_tenant.py
data/transcripts/scripts/tests/test_muse_verify.py
org/missions/D9/COMM/COMM_ASSIST/task-orders/COMM_ASSIST.TO-CA-i-10.receiver-refuses-a-replayed-muse-answer.md
org/missions/D9/COMM/COMM_ASSIST/deliverables/0.9.0_WK_COMM_ASSIST~16/
org/missions/D9/COMM/COMM_ASSIST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no grant moves and no AWS call is made.
comp-adversary: RUN -- an old signature acting on a later draft under the same tag (refused: AC1 arm 3); the same signed bytes sent twice (refused: AC1 arm 2); an answer that drops version or seq to dodge the binding (refused: AC1 arms 4 and 5); a guard that breaks a seqless draft (refused: AC1 control arm); a guard that records a refusal as "acted" (the build records only on a result that moved the draft). BLIND: the assistant's state row growing by 200 hashes is not measured here; each is 64 characters.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Base: CAi10-AC1 base: FAIL as expected (2 of 6 arms: the two controls; the four build arms fail). CAi10-AC2 base: PASS as expected (control, 7 of 7). CAi10-AC3 base: PASS as expected (control). AC1 green arm: PASS as expected (6 of 6) against a scratch reference guard.
Source: CVO half `deliverables/3.0.0_SA_CVO~L/NEVER_WIDEN_HALF_CVO_COMM_ASSIST_R17_DEPLOY_20261014.md` ("Carried": row COMM_ASSIST-C-S5, ARMED, disarm owner the issuer); issuer rulings R-7 (`r17/ISSUER_RULINGS.md`); tenant.py `assign_seq`, `chat_tag`.
