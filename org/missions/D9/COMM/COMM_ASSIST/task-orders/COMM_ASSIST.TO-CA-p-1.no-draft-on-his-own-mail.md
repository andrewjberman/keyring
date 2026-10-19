# TO COMM_ASSIST.TO-CA-p-1 -- round 22 CA-p-1: the mail handler never drafts for mail Andrew sent (his own mailbox is refused before anything else runs)

<to_id>COMM_ASSIST.TO-CA-p-1</to_id>
<project>COMM_ASSIST</project>
<issued_to>0.9.0_WK_COMM_ASSIST~33</issued_to>
<issued_by>2.0.0_SA_COO~CA</issued_by>
<issued_date>2026-10-19</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>22</round>
<workstream>SELFMAIL</workstream>

**Directive:** D9 | **Fabric:** laptop | **Decomp cell:** `CA-p-1` (`decompositions/COMM_ASSIST_DECOMP.round22.md`) | **outcome_ref:** FWD-2 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

`data/transcripts/scripts/teams_chat/mail_requests.py` reads mail sent to Andrew and drafts a reply for him. A message is
"considered" (function `considered`) when its sender's domain is one of five parties' (Opal's own domain is one) and its body
names "Andrew". Nothing excludes Andrew's OWN mailbox, so a mail Andrew sent (a reply chain that names him) is drafted and
texted back to him. You make `on_mail_messages` refuse a message whose sender address is Andrew's own, before anything else
runs for it. The cached identity `a.me()` (module `assist`, imported in the file as `a`) returns a dict with the key `mail`
(his mailbox address, any letter case) beside `id` and `display_name`.

### WHAT TO BUILD (in `mail_requests.py`, these changes only)

1. `REASONS` gains a sixth value, `"from_andrew"`, last: `("ok", "sender_domain", "body_no_andrew", "no_sender", "no_body", "from_andrew")`.
2. A new function above `considered`:
   ```python
   def _my_addresses() -> set:
       """Andrew's own mailbox addresses, lowercase, from the cached /me answer. Unknown raises: the event retries and nothing is drafted."""
       mail = str(a.me().get("mail") or "").strip().lower()
       if not mail:
           raise RuntimeError("me-without-mail")
       return {mail}
   ```
3. `considered(message, domains, mine=None)`: after the `no_sender` return and BEFORE the domain test, add
   `if mine and addr.strip().lower() in mine: return False, "from_andrew"`. Update its docstring's reason list. The two-argument
   call `considered(message, domains)` must keep working and behave as before.
4. `on_mail_messages`: right after `domains = firm_domains()` add `mine = _my_addresses()`, and call
   `considered(message, domains, mine)`. Nothing else in the function changes (a refused message is counted by reason and skipped:
   no model call, no text, no state beyond the count).

### THE TEST EDITS (in `data/transcripts/scripts/tests/`, these four changes only)

- `test_inbound_mail_draft.py`, `test_inbound_mail_reply.py` and `test_inbound_mail.py`: each has exactly ONE line
  `        mr._lookup = lambda ns, key: None` inside its `World.__init__` (8 spaces). Add directly after it this line:
  `        a.me = lambda: {"id": "u-me", "display_name": "Andrew Invented", "mail": "andrew.invented@house-zero.test"}   # CA-p-1: his mailbox, invented`
- `test_inbound_mail.py`, the case `a_mixed_batch_texts_only_the_passing_work_request`: its counts literal
  `{"ok": 1, "sender_domain": 1, "body_no_andrew": 1, "no_sender": 0, "no_body": 0}` becomes
  `{"ok": 1, "sender_domain": 1, "body_no_andrew": 1, "no_sender": 0, "no_body": 0, "from_andrew": 0}`.
Change no other test, name or assertion.

### THE CONTRACT

`org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r22/checks/check_p1_self_mail.py` (READ it, do not edit it): six arms --
his mail is refused with no text and no model call and counted `from_andrew`; the same in other letter cases under another display
name; a colleague's mail at the same domain still texts (difference control); a mixed batch texts only the colleague; the reason
and the old two-argument call; and an unknown mailbox (`a.me` raising, or no `mail`) makes `on_mail_messages` raise with nothing
drafted.

### RULES

- Edit nothing but the files in `<paths>`. No non-ASCII. The files use LF line endings: keep them (do not rewrite a file whole).
  Do not change the event shape, `ROUTE`, `firm_domains`, or any text sent to Andrew. Never log message text or an address.
- Refuse a criterion you cannot satisfy as written and report the refusal with its measurement; do not repair or widen it.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CAp1-AC1" cell_refs="CA-p-1"><invocation>python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r22/checks/check_p1_self_mail.py"</invocation><expect>P1-SELFMAIL ok=True arms=6 of 6</expect></criterion>
`CAp1-AC1` -- the built behaviour: the issuer's six arms. It prints 1 of 6 at the base (only the difference control passes) and 6 of 6 against a 14-line reference.

<criterion id="CAp1-AC2" cell_refs="CA-p-1"><invocation>python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r22/checks/check_p1_mail_suite.py"</invocation><expect>P1-MAILSUITE ok=True tests=4 of 4</expect></criterion>
`CAp1-AC2` -- the bound, a control that PASSES at the base: the four existing mail test files (17/17, 15/15, 22/22, 8/8 arms). Without the four test edits above the reference build reads 16/17, 14/15, 4/22 and 8/8, so the edits are part of the cell.

<criterion id="CAp1-AC3" cell_refs="CA-p-1"><invocation>python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r17/checks/check_i2_regression.py"</invocation><expect>I2-REGRESSION ok=True</expect></criterion>
`CAp1-AC3` -- the bound, a control that PASSES at the base: the assistant's flow tests.
</proof_of_spec>

<expected_criteria>CAp1-AC1,CAp1-AC2,CAp1-AC3</expected_criteria>

Each invocation runs from the worktree root, by that RELATIVE path, under `timeout 280`. Commit the edits FIRST. Then write the proof
instance to
`org/missions/D9/COMM/COMM_ASSIST/deliverables/0.9.0_WK_COMM_ASSIST~33/COMM_ASSIST.TO-CA-p-1.no-draft-on-his-own-mail.proof_of_spec.json`,
modelled on `org/missions/D9/COMM/COMM_ASSIST/deliverables/0.9.0_WK_COMM_ASSIST~32/COMM_ASSIST.TO-CA-n-1.read-replies-of-recent-threads.proof_of_spec.json`,
recording each invocation EXACTLY as the criterion text (no `timeout` prefix) and pinning each artifact row to the commit that
carried it. Flip `<status>` to `complete` only when all three pass. Validate with the WORKTREE'S OWN `.tools/proof-of-spec-check.py`
from inside the worktree AFTER your last commit: `python .tools/proof-of-spec-check.py <instance> CAp1-AC1,CAp1-AC2,CAp1-AC3`; its
LAST line must be `VALID (rc=0)` at the final head. Your final report names each function you changed and the arm counts. Your
surprise rows are `COMM_ASSIST-W33-S<k>`; append only to the investigation file and keep its existing line endings; `surfaced_at` =
`date -u +%FT%TZ` at filing. Commit with `.tools/safe-commit.sh` as your serial; write the commit message file with your Write tool
(never a shell heredoc), ending with the attribution line the harness gives you.

<decomp_ref>
<decomp_doc>org/missions/D9/COMM/COMM_ASSIST/decompositions/COMM_ASSIST_DECOMP.round22.md</decomp_doc>
<owned_cells>CA-p-1</owned_cells>
</decomp_ref>

<paths>
data/transcripts/scripts/teams_chat/mail_requests.py
data/transcripts/scripts/tests/test_inbound_mail_draft.py
data/transcripts/scripts/tests/test_inbound_mail_reply.py
data/transcripts/scripts/tests/test_inbound_mail.py
org/missions/D9/COMM/COMM_ASSIST/task-orders/COMM_ASSIST.TO-CA-p-1.no-draft-on-his-own-mail.md
org/missions/D9/COMM/COMM_ASSIST/deliverables/0.9.0_WK_COMM_ASSIST~33/
org/missions/D9/COMM/COMM_ASSIST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing (the mail poller's cadence is unchanged).
comp-iam: DECLARED-NOT-APPLICABLE no grant moves; `a.me()` is the handler's existing cached read (state object me.json, already read by the chat path).
comp-adversary: RUN -- a fix that matches his display name instead of his address (refused: `case_and_name` uses another name with his address, and the control uses his name only through the address); a fix that drops every Opal-internal mail (refused: `colleague_control`, same domain texts); a fix that drafts when his mailbox is unknown (refused: `fail_closed`, three unknown shapes); a fix that changes the old call shape (refused: `reasons_and_api`, two-argument call). BLIND: an alias or second mailbox of his that is not the cached `mail` is not refused; a mail whose sender is a shared mailbox he sends from is not refused; the thread-latest half of the rule cannot be built here (each mail is its own event, one message).
naming: no name is created (CLAUDE.md rule 30 non-application).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Base: CAp1-AC1 base: FAIL as measured (1 of 6; `colleague_control` passes). Green arm 6 of 6 against a scratch reference implementation (14 added lines, 3 replaced; the scratch folder is outside the repository). CAp1-AC2 base: PASS as measured (4 of 4). CAp1-AC3 base: PASS as measured (control, 64 passed).
Source: Andrew's word 2026-10-19 ~16:26Z (`org/tier1_exec/2.0.0_SA_COO~CA/ANDREW_DIRECT_20261019_162xZ_MUSE_NO_SELF_DRAFT_RULE_APPROVED_AND_CALL_2396_WAIT_NATURAL.md` @8eb8c7408a), CTO go msg 109839; the live state read of M741 and M044 (`mail_log` rows from "Andrew Berman", domain opalinvest.com).
