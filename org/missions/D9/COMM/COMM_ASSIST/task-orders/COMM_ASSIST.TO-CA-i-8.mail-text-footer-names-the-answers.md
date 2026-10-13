# TO COMM_ASSIST.TO-CA-i-8 -- round 17 CA-i-8: the text that carries a mail draft tells Andrew how to answer it (worker row W13-S1)

<to_id>COMM_ASSIST.TO-CA-i-8</to_id>
<project>COMM_ASSIST</project>
<issued_to>0.9.0_WK_COMM_ASSIST~14</issued_to>
<issued_by>2.0.0_SA_COO~CA</issued_by>
<issued_date>2026-10-13</issued_date>
<status>pending</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>17</round>
<workstream>MAILFOOT</workstream>

**Directive:** D9 | **Fabric:** laptop | **Decomp cell:** `CA-i-8` (`decompositions/COMM_ASSIST_DECOMP.round17.md`, AMENDMENT 2) | **outcome_ref:** FWD-4 (the mail branch), J290 |
**depends_on:** CA-i-7 (merged @d555e412c1)

---

## WORKER FACE

### THE CELL

A mail that names Andrew is texted to him with a draft (`_mail_text` in `data/transcripts/scripts/teams_chat/mail_requests.py`). Cell CA-i-7 taught the assistant to act on his answers:
his notes redraft the draft, his `1` approves it and hands back the final draft to paste into Outlook, `0` drops it, `#dev [notes]` opens a job. But the text still ends
`Reply #dev [notes] to open a job / 0 drop`, so he is never told that `1` and notes work. You change that one closing line and its test. Nothing else.

### BUILD

1. In `_mail_text`, replace the closing line with one that names all four answers in plain English, short enough for a text: `1` approves and returns the final draft to paste into Outlook
   (nothing is sent for you); notes redraft; `0` drops; `#dev [notes]` opens a job. For example:
   `Reply 1 to approve (you get the draft to paste; nothing is sent) / notes to redraft / 0 drop / #dev [notes] to open a job`. Keep it one line, ASCII only.
2. In `data/transcripts/scripts/tests/test_inbound_mail_reply.py` update any case that asserts the old closing line, and add one assertion that the text names `1`, `notes`, `0` and `#dev`.
   Its last line stays `INBOUND-MAIL-REPLY-TEST ok=<True|False> cases=<passed>/<total>`.
3. Edit nothing else. No change to any logic, any other text or any other file.

### RULES

- Edit nothing but the files in `<paths>`. Code change with a test; not deployed here.
- Refuse a criterion you cannot satisfy as written and report the refusal with its measurement; do not repair or widen it.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CAi8-AC1" cell_refs="CA-i-8"><invocation>python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r17/checks/check_i8_footer.py"</invocation><expect>I8-FOOTER ok=True</expect></criterion>
`CAi8-AC1` -- the issuer's check (read it; do not edit it): the last line of the text names `1` (with what it does: approve, paste, or both), notes (redraft), `0` and `#dev`. It prints ok=False at the base.

<criterion id="CAi8-AC2" cell_refs="CA-i-8"><invocation>python "data/transcripts/scripts/tests/test_inbound_mail_reply.py"</invocation><expect>INBOUND-MAIL-REPLY-TEST ok=True</expect></criterion>
`CAi8-AC2` -- the bound, a control that PASSES at the base (15 of 15) and must still pass with your assertion added.
</proof_of_spec>

<expected_criteria>CAi8-AC1,CAi8-AC2</expected_criteria>

Each invocation runs from the worktree root under `timeout 120`. Write the proof instance to
`org/missions/D9/COMM/COMM_ASSIST/deliverables/0.9.0_WK_COMM_ASSIST~14/COMM_ASSIST.TO-CA-i-8.mail-text-footer-names-the-answers.proof_of_spec.json`, validate it by running the
WORKTREE'S OWN `.tools/proof-of-spec-check.py` from inside the worktree: `python .tools/proof-of-spec-check.py <instance> CAi8-AC1,CAi8-AC2`, and flip `<status>` to `complete` only when both
pass and the instance is VALID. Your final report names the exact line you wrote. Your surprise rows are `COMM_ASSIST-W14-S<k>`; append only to the investigation file and keep its existing
line endings; `surfaced_at` = `date -u +%FT%TZ` at filing. Commit with `.tools/safe-commit.sh` as your serial.

<decomp_ref>
<decomp_doc>org/missions/D9/COMM/COMM_ASSIST/decompositions/COMM_ASSIST_DECOMP.round17.md</decomp_doc>
<owned_cells>CA-i-8</owned_cells>
</decomp_ref>

<paths>
data/transcripts/scripts/teams_chat/mail_requests.py
data/transcripts/scripts/tests/test_inbound_mail_reply.py
org/missions/D9/COMM/COMM_ASSIST/task-orders/COMM_ASSIST.TO-CA-i-8.mail-text-footer-names-the-answers.md
org/missions/D9/COMM/COMM_ASSIST/deliverables/0.9.0_WK_COMM_ASSIST~14/
org/missions/D9/COMM/COMM_ASSIST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no grant moves; no AWS call is made here.
comp-adversary: RUN -- a footer that promises a send (refused: AC1 requires the words paste or approve and the text says nothing is sent); a footer that drops #dev or 0 (refused: AC1 needs all four answers); a logic change riding the edit (refused: THE CELL; AC2 keeps the 15 cases). BLIND: how the line reads on his phone is not graded here.
lane: the <paths> block IS the grant (worker RULING 1). DIRECT-ACT: one line, LOCAL; no L8-L10; its close is the issuer's one real run.
</preflight>

Base: CAi8-AC1 base: FAIL as expected (has_one=False has_notes=False); CAi8-AC2 base: PASS as expected (control, 15 of 15). AC1 green arm: PASS as expected against a scratch footer.
Source: worker row COMM_ASSIST-W13-S1 (the footer names only #dev and 0); CA-i-7 merged @d555e412c1; job J290.
