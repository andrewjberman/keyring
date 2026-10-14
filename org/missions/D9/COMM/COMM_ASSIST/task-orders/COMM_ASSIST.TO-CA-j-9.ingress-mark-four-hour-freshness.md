# TO COMM_ASSIST.TO-CA-j-9 -- round 18 CA-j-9: the ingress mark stays valid for 4 hours, and the single-use record holds every mark inside that window (CTO ruling on call 847f)

<to_id>COMM_ASSIST.TO-CA-j-9</to_id>
<project>COMM_ASSIST</project>
<issued_to>0.9.0_WK_COMM_ASSIST~23</issued_to>
<issued_by>2.0.0_SA_COO~CA</issued_by>
<issued_date>2026-10-14</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>18</round>
<workstream>FRESHMARK</workstream>

**Directive:** D9 | **Fabric:** laptop | **Decomp cell:** `CA-j-9` (`decompositions/COMM_ASSIST_DECOMP.round18.md`, AMENDMENT 6) | **outcome_ref:** FWD-7 |
**depends_on:** CA-j-1 (merged `0ca94ce0b6`); the CTO ruling `CTO_RULING_20261014_104xZ_COMM_ASSIST_MARK_FRESHNESS_4H.md` (msg 109095)

---

## WORKER FACE

### THE CELL

The assistant (LDO-001, `data/transcripts/scripts/teams_chat/tenant.py`) marks every event it makes for Andrew's texts with an HMAC (`ingress_mark.py`) and its handler checks the mark in the mode `INGRESS_MARK_MODE` gives. Today a mark is valid for 15 minutes and the handler keeps the last 100 marks it accepted, to refuse a replay. The mailbox queue redelivers a failed event an hour later, and again an hour after that (visibility timeout 3600 s, max receive count 3), so in `enforce` mode a retried genuine text would be refused as stale and deleted. The CTO ruled: the mark stays valid for **4 hours**; and so a mark cannot be replayed inside the wider window, the single-use record must hold **every** mark younger than the window (pruned by age, never by a count cap). A refusal must record the event's kind and tag so a lost text can be found and resent. This cell changes the code and its tests. It is NOT deployed here (a later cell does that).

### BUILD, IN THIS ORDER

1. `ingress_mark.py`: `MAX_AGE_S` becomes `4 * 3600`. Update the comment beside it (why 4 hours: the queue redelivers a failed event after 3600 s, twice). `MAX_AHEAD_S` stays 5 minutes. Nothing else in the module changes.
2. `tenant.py`, in `_mark_refused` (and the constants above it):
   - `state["marks_seen"]` holds one entry per accepted mark with the mark's own time, for example `{"mark": <mark>, "at": <mark_at>}`. At every check, entries older than `ingress_mark.MAX_AGE_S` (measured from `ctx.now()` against the entry's `at`) are DROPPED; entries inside the window are ALL kept. Remove the count cap (`MARKS_KEEP` and its `del`). A mark already held is `"replayed-mark"` exactly as today.
   - Tolerate a legacy entry (a bare mark string, as CA-j-1 wrote): treat it as held, dated now, so it ages out four hours later. No crash on either shape.
   - A refusal appended to `state["mark_refusals"]` records `{"at": <iso now>, "reason": <reason>, "kind": ctx.kind, "tag": <the payload's "tag" if it is a string, else None>}` and NOTHING else from the payload (never the notes or text, a mark, or the secret). Keep `REFUSALS_KEEP`.
   - The modes, the reasons, the return `"unmarked-refused"`, the `unmarked_seen` counter and `dispatch` are otherwise unchanged.
3. Tests: update `data/transcripts/scripts/tests/test_ingress_mark.py` for the new bound and record (the 15/16-minute window test, the 105-marks-cap test, the refusal-reasons test), and add: a mark replayed at 3h59m is refused `replayed-mark`; a mark 4h01m old is `stale-mark`; 150 marks inside the window are all held and the first replayed is refused; a mark older than the window is no longer held after a later delivery; a refusal carries kind and tag and not the payload's note. Existing tests must still pass.
4. No non-ASCII. No AWS call, no network, no change outside `<paths>`.

### RULES

- Edit nothing but the files in `<paths>`. This is a code change with tests; it is NOT deployed here.
- Refuse a criterion you cannot satisfy as written and report the refusal with its measurement; do not repair or widen it.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CAj9-AC1" cell_refs="CA-j-9"><invocation>python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r18/checks/check_j9_fresh.py"</invocation><expect>J9-FRESH ok=True arms=7 of 7</expect></criterion>
`CAj9-AC1` -- the issuer's check (read it; do not edit it): the window edges (3h59m ok, 4h01m stale, six minutes ahead stale, four ahead ok); a first delivery 3h59m after the mark acts; a replay at 3h59m is `replayed-mark`; 150 marks in the window are all held and the first replayed is refused (no count cap); a mark older than the window is no longer held after a later delivery; a refusal records kind and tag and never the payload's note; and the CA-j-1 check still reads 9 of 9. It prints 1 of 7 at the base.

<criterion id="CAj9-AC2" cell_refs="CA-j-9"><invocation>python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r17/checks/check_i2_regression.py"</invocation><expect>I2-REGRESSION ok=True</expect></criterion>
`CAj9-AC2` -- the bound, a control that PASSES at the base and must still pass: the assistant's flow tests, the text path included.

<criterion id="CAj9-AC3" cell_refs="CA-j-9"><invocation>python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r17/checks/check_i13_fresh.py"</invocation><expect>I13-FRESH ok=True arms=6 of 6</expect></criterion>
`CAj9-AC3` -- the bound, a control that PASSES at the base and must still pass: muse's signed-answer path (its own gate, untouched by the mark).
</proof_of_spec>

<expected_criteria>CAj9-AC1,CAj9-AC2,CAj9-AC3</expected_criteria>

Each invocation runs from the worktree root under `timeout 120` (the first may need up to `timeout 250`). Commit the code and tests FIRST. Then write the proof instance to
`org/missions/D9/COMM/COMM_ASSIST/deliverables/0.9.0_WK_COMM_ASSIST~23/COMM_ASSIST.TO-CA-j-9.ingress-mark-four-hour-freshness.proof_of_spec.json`, modelled on `org/missions/D9/COMM/COMM_ASSIST/deliverables/0.9.0_WK_COMM_ASSIST~19/COMM_ASSIST.TO-CA-j-1.ingress-mark-on-the-text-driven-events.proof_of_spec.json`, pinning each artifact row to the commit that carried it (a row left as pending-this-commit goes INVALID the moment a later commit lands), and flip `<status>` to `complete` only when all three pass. Validate by running the WORKTREE'S OWN `.tools/proof-of-spec-check.py` from inside the worktree AFTER your last commit: `python .tools/proof-of-spec-check.py <instance> CAj9-AC1,CAj9-AC2,CAj9-AC3`, and read the LAST line: it must be `VALID (rc=0)` at the final head. Your final report names the changed lines, the new state shape, every existing test you changed, and the whole flow-test count (`python -m pytest data/transcripts/scripts/tests -q -p no:cacheprovider` from the worktree root). Your surprise rows are `COMM_ASSIST-W23-S<k>`; append only to the investigation file and keep its existing line endings; `surfaced_at` = `date -u +%FT%TZ` at filing. Commit with `.tools/safe-commit.sh` as your serial.

<decomp_ref>
<decomp_doc>org/missions/D9/COMM/COMM_ASSIST/decompositions/COMM_ASSIST_DECOMP.round18.md</decomp_doc>
<owned_cells>CA-j-9</owned_cells>
</decomp_ref>

<paths>
data/transcripts/scripts/teams_chat/ingress_mark.py
data/transcripts/scripts/teams_chat/tenant.py
data/transcripts/scripts/tests/test_ingress_mark.py
org/missions/D9/COMM/COMM_ASSIST/task-orders/COMM_ASSIST.TO-CA-j-9.ingress-mark-four-hour-freshness.md
org/missions/D9/COMM/COMM_ASSIST/deliverables/0.9.0_WK_COMM_ASSIST~23/
org/missions/D9/COMM/COMM_ASSIST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no grant moves and no AWS call is made; the deploy is a later cell with its own pair.
comp-adversary: RUN -- a count cap that lets a mark be replayed inside the wider window (refused: AC1 `nocap` arm, 150 marks then the first replayed); a wider bound that weakens single use (refused: AC1 `replay` arm at 3h59m); the window growing without end (refused: AC1 `prune` arm); a refusal record that leaks the payload (refused: AC1 `refusal-fields` arm; the notes never appear); the CA-j-1 modes and reasons disturbed (refused: AC1 `regress` arm and AC2); a state written by the CA-j-1 code (bare mark strings) crashing the new code (refused: BUILD step 2 tolerates both shapes; none exists in production today, `check_j5_obs` read 0 rows carrying mark counters). BLIND: a real redelivered event after a real handler failure is read only live, after the deploy cell; the queue's retry timing (3600 s, 3 receives) is a read of the live queue on 2026-10-14 ~10:4xZ, not exercised here.
naming: no name is created (CLAUDE.md rule 30 non-application).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Base: CAj9-AC1 base: FAIL as expected (1 of 7: only the CA-j-1 regress arm holds). CAj9-AC2 base: PASS as expected (control). CAj9-AC3 base: PASS as expected (control). AC1 green arm: PASS as expected (7 of 7) against a scratch reference (the two edited files in a throwaway worktree, removed); a negative control that restores a count cap reads 6 of 7 (`nocap` fails). The CA-j-1 check was amended to stale its mark at 5 hours so it reads 9 of 9 before and after this cell.
Source: CTO ruling on call 847f (`CTO_RULING_20261014_104xZ_COMM_ASSIST_MARK_FRESHNESS_4H.md`, msg 109095); round-18 decomposition AMENDMENT 5 (the live queue read); `ingress_mark.py`, `tenant.py` `_mark_refused`.
