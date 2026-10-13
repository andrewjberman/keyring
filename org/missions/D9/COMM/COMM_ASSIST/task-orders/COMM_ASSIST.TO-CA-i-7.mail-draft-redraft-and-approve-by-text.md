# TO COMM_ASSIST.TO-CA-i-7 -- round 17 CA-i-7: a received-mail draft can be worked to the end by text (notes redraft it, his 1 approves it), and nothing is ever sent (J290; round-16 analysis addendum item 7)

<to_id>COMM_ASSIST.TO-CA-i-7</to_id>
<project>COMM_ASSIST</project>
<issued_to>0.9.0_WK_COMM_ASSIST~13</issued_to>
<issued_by>2.0.0_SA_COO~CA</issued_by>
<issued_date>2026-10-13</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>17</round>
<workstream>MAILREPLY</workstream>

**Directive:** D9 | **Fabric:** laptop | **Decomp cell:** `CA-i-7` (`decompositions/COMM_ASSIST_DECOMP.round17.md`, AMENDMENT 1) | **outcome_ref:** FWD-4 (the mail branch) |
**depends_on:** none

---

## WORKER FACE

### THE CELL

A mail that names Andrew reaches his phone as a text with a draft reply (the mail pipeline: `data/transcripts/scripts/teams_chat/mail_requests.py`). Today, whatever he
answers to that text, his `1` or his notes, gets "A reply by mail is not built". So the first real mail (a TIFIN call) had no way to be answered. The standing rule
stays: **the assistant never sends a mail, a Teams message or anything else for him; it only drafts.** You build the loop around the draft so he can finish it by
text: his notes redraft it (a new version, texted), his `1` approves it and hands back the final draft in one clean block to paste into his own Outlook reply,
and the item closes. Read `mail_requests.on_mail_reply` and `tenant.py` around line 470 first, and how the CHAT path redrafts (`tenant.on_sms_reply`, the "edit"
branch, `assist.draft_chat_reply`, `tenant.offer`, `tell_extra`) so the mail path behaves the same way.

### BUILD, IN THIS ORDER

1. `draft_mail_reply` (mail_requests.py) accepts optional `previous` (the last draft text) and `notes` (Andrew's words). With neither, it behaves exactly as it does now. With them,
   the drafting prompt carries `Andrew's previous draft:` and `Andrew's notes on it:` and asks for a rewrite that applies the notes, using the same phrasing the chat path uses.
2. `on_mail_reply` (mail_requests.py), for a mail item:
   - action `edit` (notes): if the payload carries a `version` that is not the item's current version, tell him `#<tag> changed just before your reply, so nothing was done. Reply to the latest #<tag> text.`
     and return `"unseen"`. Otherwise redraft with `previous` and `notes`, store version + 1 (same tag, same kind), text the new draft the way a new mail item is texted, and return `"redrafted"`.
     A refused or empty redraft leaves the item exactly as it was and tells him in one line (follow the chat path).
   - action `send` (his 1): the same stale check (`"unseen"`); otherwise set the pending item to `None`, text ONE message `#<tag> approved. Final draft, to paste into your reply in Outlook (nothing is sent for you):`
     followed by the draft on its own lines, and return `"mail-approved"`.
   - actions `drop` and `dev` are unchanged (`"dropped"`, `"job-opened"`).
   - Replace the "not built" texts (`NOT_BUILT`, `SEND_NOT_BUILT`); keep the sentence that no mail is ever sent for him.
3. Nothing in this code path sends or posts anything: no gateway write, no Teams post, no mail call. The mail gateway stays read-only.
4. Update `data/transcripts/scripts/tests/test_inbound_mail_reply.py`: the cases that asserted "not built" now assert the new behaviour (redraft, approve, stale), and the difference
   control (a completed MAIL job makes zero gateway chat sends where a CHAT job makes one) stays. Its last line must stay `INBOUND-MAIL-REPLY-TEST ok=<True|False> cases=<passed>/<total>`.
5. No non-ASCII. Edit nothing outside `<paths>`. If you find you need a change in `assist.py` or `tenant.py`, file a surprise row naming the exact line and keep working on the rest.

### RULES

- Edit nothing but the files in `<paths>`. This is a code change with tests; it is NOT deployed here (a later cell rebuilds and deploys the assistant under change management).
- Whether the final draft should ALSO be saved as an Outlook draft through a new gateway route is NOT this cell: that is a separate decision and a separate component. Do not build or call anything for it.
- Refuse a criterion you cannot satisfy as written and report the refusal with its measurement; do not repair or widen it.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CAi7-AC1" cell_refs="CA-i-7"><invocation>python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r17/checks/check_i7_mail.py"</invocation><expect>I7-MAIL ok=True arms=6 of 6</expect></criterion>
`CAi7-AC1` -- the issuer's check (read it; do not edit it): six arms through the real `on_sms_reply` with a stand-in drafting model. Notes redraft to a new version; his 1 approves and the text carries the final draft and the word paste; a 1 or notes aimed at a draft that moved on get `unseen` and change nothing; 0 and #dev are unchanged; and across the whole run no chat message and no post is sent. It prints ok=False at the base (2 of 6 arms: the two controls).

<criterion id="CAi7-AC2" cell_refs="CA-i-7"><invocation>python "data/transcripts/scripts/tests/test_inbound_mail_reply.py"</invocation><expect>INBOUND-MAIL-REPLY-TEST ok=True</expect></criterion>
`CAi7-AC2` -- the bound, a control that PASSES at the base (9 of 9) and must still pass with the cases you updated and added.

<criterion id="CAi7-AC3" cell_refs="CA-i-7"><invocation>python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r17/checks/check_i2_regression.py"</invocation><expect>I2-REGRESSION ok=True</expect></criterion>
`CAi7-AC3` -- the bound, a control that PASSES at the base: the assistant's chat and muse flow tests, unchanged.
</proof_of_spec>

<expected_criteria>CAi7-AC1,CAi7-AC2,CAi7-AC3</expected_criteria>

Each invocation runs from the worktree root under `timeout 120`. Write the proof instance to
`org/missions/D9/COMM/COMM_ASSIST/deliverables/0.9.0_WK_COMM_ASSIST~13/COMM_ASSIST.TO-CA-i-7.mail-draft-redraft-and-approve-by-text.proof_of_spec.json`, validate it by running
the WORKTREE'S OWN `.tools/proof-of-spec-check.py` from inside the worktree: `python .tools/proof-of-spec-check.py <instance> CAi7-AC1,CAi7-AC2,CAi7-AC3`, and flip `<status>` to
`complete` only when all three pass and the instance is VALID. Your final report names the changed functions, the new result words, and any line you needed outside `<paths>`.
Your surprise rows are `COMM_ASSIST-W13-S<k>`; append only to the investigation file and keep its existing line endings; `surfaced_at` = `date -u +%FT%TZ` at filing. Commit with
`.tools/safe-commit.sh` as your serial.

<decomp_ref>
<decomp_doc>org/missions/D9/COMM/COMM_ASSIST/decompositions/COMM_ASSIST_DECOMP.round17.md</decomp_doc>
<owned_cells>CA-i-7</owned_cells>
</decomp_ref>

<paths>
data/transcripts/scripts/teams_chat/mail_requests.py
data/transcripts/scripts/tests/test_inbound_mail_reply.py
org/missions/D9/COMM/COMM_ASSIST/task-orders/COMM_ASSIST.TO-CA-i-7.mail-draft-redraft-and-approve-by-text.md
org/missions/D9/COMM/COMM_ASSIST/deliverables/0.9.0_WK_COMM_ASSIST~13/
org/missions/D9/COMM/COMM_ASSIST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no grant moves; no AWS call is made here.
comp-adversary: RUN -- a mail sent or posted on his 1 (refused: AC1 arm 6 and the difference control in AC2; the build adds no send); an approval of a draft he never saw (refused: AC1 stale arms); a redraft that loses the tag or skips a version (refused: AC1 arm 1); a changed text path (refused: AC3). BLIND: how the real model phrases a redraft, and the Outlook-draft route, are not exercised here.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Base: CAi7-AC1 base: FAIL as expected (2 of 6 arms; the four build arms fail with mail-reply-not-built); CAi7-AC2 base: PASS as expected (9 of 9, control); CAi7-AC3 base: PASS as expected (control). AC1 green arm: PASS as expected (6 of 6) against a scratch reference on_mail_reply.
Source: Andrew-direct ~22:3xZ via 0.0.0_AB_MSTR msg 108965; CTO msg 108970 and the round-16 analysis addendum item 7 (commit e6e0464bbc); job J290 brief (read from the assistant table, state row `job:J290`); PRD v0.7 FWD-4 ("a text with a draft reply"; standing rule: drafted, never sent).
