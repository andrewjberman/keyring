# TO COMM_ASSIST.TO-CA-m-2 -- round 9 CA-m-2: every admitted client mail reaches Andrew as a text with a draft reply, the client flagged

<to_id>COMM_ASSIST.TO-CA-m-2</to_id>
<project>COMM_ASSIST</project>
<issued_to>0.9.0_WK_COMM_ASSIST~3</issued_to>
<issued_by>2.0.0_SA_COO~R</issued_by>
<issued_date>2026-10-09</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>9</round>

**Directive:** D9 | **Fabric:** laptop | **Decomp cell:** `CA-m-2` (`decompositions/COMM_ASSIST_DECOMP.round9.md`) | **outcome_ref:** FWD-4 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

`CA-m-2`. Andrew's assistant (a Lambda; code in `data/transcripts/scripts/teams_chat/`) has a mail handler,
`mail_requests.on_mail_messages` (kind `mail.messages`; one event per mail on object `mail:<message id>`, payload
`{"messages": [<the gateway's by-id row>]}`). It runs his two tests FIRST (`considered`: the sender's domain is one of the five
firms', read from the estate's records; the body names "Andrew" as a whole word). A mail failing either is dropped before any
model call. Keep that exactly.

The outcome it must meet (FWD-4): "an email from one of the five firms whose body mentions Andrew arrives as a text with a draft
reply, the client is flagged as a client, and mail that does not name him does not text him". Contract: mail is DRAFTED, NEVER
SENT. Andrew's word: "it always has to say andrew in the body text somewhere, otherwise i dont care".

What it does today (read `on_mail_messages`, `_mail_text`, `on_mail_reply`): it texts a considered mail ONLY when the model reads it
as a work request (`a.work_request`), with `draft: ""`. A client mail that asks for nothing never reaches him, and no mail ever
carries a draft reply. `on_mail_reply` answers `1` / notes with "a reply by mail is not built"; `#dev` opens a job; `0` drops.

Read `assist.py` for `kimi(system, user)`, `voice_md()` (the voice file, organised by kind of act, including a mail-reply kind),
`draft_chat_reply` (the pattern for a draft prompt in his voice), `sms_safe`, `sms_free`. Do NOT edit `assist.py` (another cell of
this round changes it); call it.

### BUILD, IN THIS ORDER

1. In `mail_requests.py`:
   - EVERY considered mail is texted once, whatever `work_request` says.
   - The text carries: the flag line `CLIENT <firm>` for a client firm, or `Opal` for Opal's own domain; the sender; up to
     `BODY_CAP` characters of the mail; and `Draft:` with a draft reply.
   - When the model reads a request for work, the existing `WORK REQUESTED` / `Recommend` lines are added.
   - The last line lists only the actions `on_mail_reply` supports.
   - The draft is ONE model call, `mail:draft:<key>` under `ctx.once`, written as Andrew in the first person from the voice
     file's mail-reply section and the mail; a helper in this file, prompt beside it. Put it through `sms_free`.
   - If the draft call fails (`KimiError`), the mail is STILL texted, with `Draft: (not available: <error class>)`. Nothing is
     silent.
   - The pending item keeps the draft (`pending["draft"]`), so a later redraft path can use it.
   - Nothing sends a mail or a Teams message.
2. `on_mail_reply`: `1` answers one line that sending by mail is not built and that the draft is in the text to paste into
   Outlook; the item stays open. `#dev` and `0` are unchanged.
3. NEW `data/transcripts/scripts/tests/test_inbound_mail_draft.py` (a plain script, no network; fake `kimi`, fake `send_sms`, fake
   `ctx` with `once` keeping records). Arms, each printing `ARM <name> ok=<True|False>`:
   - `client_no_request`: a client mail that names Andrew and asks for nothing -> ONE text with `CLIENT <firm>` and a `Draft:`.
     **Difference control in the same arm:** the BASE handler (`git show 416b9c1260:data/transcripts/scripts/teams_chat/mail_requests.py`
     loaded into a temp module) sends NO text for the same mail.
   - `client_request`: a work request -> one text with both the draft and the `WORK REQUESTED` lines.
   - `opal_flag`: an Opal-domain sender -> flagged `Opal`, not `CLIENT`.
   - `not_named`: the body lacks "Andrew" -> no model call and no text.
   - `draft_fails`: the draft call raises `KimiError` -> still one text, saying the draft is not available.
   - `once`: the same event twice -> one draft call and one text.
   - `never_sent`: no gateway send or reply verb is called in any arm.
   LAST line `MAIL-DRAFT ok=<True|False> arms=<passed>/<total> base_texts_client_no_request=<n>`.

### RULES FOR THIS CELL

- **Nothing you run leaves this machine**: no gateway, Graph, S3, model or text call. Everything is injected.
- Edit nothing but the files in `<paths>`. Keep `considered` and the domain loading byte-unchanged in behaviour (they are the law
  of C-MAIL); keep every existing case passing, changing a case only where the new text requires it and naming it in your report.
- No real mail, person's, client's or firm's name or domain in any file you write. No non-ASCII. Bake no absolute path.
- Refuse a criterion you cannot satisfy as written and report the refusal with its measurement; do not repair or widen it.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CAm2-AC1" cell_refs="CA-m-2"><invocation>python data/transcripts/scripts/tests/test_inbound_mail_draft.py</invocation><expect>MAIL-DRAFT ok=True</expect></criterion>
`CAm2-AC1` -- the built behaviour and its difference control in one run: seven arms; the base texts nothing for a client mail that asks for nothing.

<criterion id="CAm2-AC2" cell_refs="CA-m-2"><invocation>python data/transcripts/scripts/tests/test_inbound_mail.py</invocation><expect>INBOUND-MAIL-TEST ok=True</expect></criterion>
`CAm2-AC2` -- the cell's bound on the two tests: the 15 existing mail cases (15/15 at the base) still pass, model calls on a failed message still zero.

<criterion id="CAm2-AC3" cell_refs="CA-m-2"><invocation>python "org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/2.0.0_SA_COO~R/checks/check_agent_suites.py"</invocation><expect>AGENT-SUITE ok=True</expect></criterion>
`CAm2-AC3` -- the agent's existing suites and the mail-reply script still pass (the issuer's check; read it, do not edit it).
</proof_of_spec>

<expected_criteria>CAm2-AC1,CAm2-AC2,CAm2-AC3</expected_criteria>

Each invocation runs under `timeout 120`. Write the proof instance to
`org/missions/D9/COMM/COMM_ASSIST/deliverables/0.9.0_WK_COMM_ASSIST~3/COMM_ASSIST.TO-CA-m-2.mail-text-with-draft.proof_of_spec.json`,
validate it with `python .tools/proof-of-spec-check.py <instance> CAm2-AC1,CAm2-AC2,CAm2-AC3`, and flip `<status>` to `complete` only
when all three pass and the instance is VALID. Your surprise rows are `COMM_ASSIST-W3-S<k>`; append lines only to the
investigation file and keep its existing line endings.

<decomp_ref>
<decomp_doc>org/missions/D9/COMM/COMM_ASSIST/decompositions/COMM_ASSIST_DECOMP.round9.md</decomp_doc>
<owned_cells>CA-m-2</owned_cells>
</decomp_ref>

<paths>
data/transcripts/scripts/teams_chat/mail_requests.py
data/transcripts/scripts/tests/test_inbound_mail_draft.py
data/transcripts/scripts/tests/test_inbound_mail.py
data/transcripts/scripts/tests/test_inbound_mail_reply.py
org/missions/D9/COMM/COMM_ASSIST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE -- denominator: 0 policies and 0 AWS calls in this cell.
comp-adversary: RUN -- a mail that fails the name test reaching a model (arm `not_named`, and AC2's zero model calls on failed); a draft failure going silent (arm `draft_fails`); a duplicate text or draft call on a retry (arm `once`); a mail sent in his name (arm `never_sent`; C-MAIL); a client mis-flagged as Opal or the reverse (arm `opal_flag`). BLIND: draft quality is a judgment for Andrew on the first real client mail (FWD-4's EXERCISED read).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: PRD `prd/COMM_ASSIST_PRD.md` v0.2 (ADMITTED, `805fec22c5`), FWD-4, C-MAIL, C-ONE-YES; Andrew-direct `c0a11edcc8`.
