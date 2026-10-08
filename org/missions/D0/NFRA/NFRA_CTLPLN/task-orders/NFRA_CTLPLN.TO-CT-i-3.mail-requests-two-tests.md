# TO NFRA_CTLPLN.TO-CT-i-3 -- workstream INBOUND round 1 CT-i-3: mail to Andrew is read for requests for work under his two tests, before any model sees a message

<to_id>NFRA_CTLPLN.TO-CT-i-3</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~31</issued_to>
<issued_by>2.0.0_SA_COO~R</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>INBOUND</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-i-3` (`decompositions/NFRA_CTLPLN_DECOMP.inbound1.md`) | **outcome_ref:** FWD-20 |
**depends_on:** `CT-i-1` (`assist.work_request` and the text shape of `assist.offer_text`), drained before this order starts

---

## WORKER FACE

### THE CELL

`CT-i-3`, contract C-SEATS clause 9, verbatim: "**9. Mail.** Only his own mailbox, through the gateway. A message is considered
ONLY when both hold: its sender's domain is one of the five he named (Cottonwood, Inflection, 49 Financial, Alongside, and Opal
for internal), each domain string read from the estate's firm records and never typed; and its body names "Andrew". A message
failing either test is not passed to any model."

Andrew, 2026-10-07 ~21:4xZ: "Yeah i need it for both teams and outlook".

The gateway is the only sanctioned read of his mailbox. The existing mail code is `data/transcripts/scripts/outlook/`
(`gateway_mail.py` is the caller of the gateway's headless route; `pull.py` and `criterion.py` read mail for one other
purpose). The Teams agent is `data/transcripts/scripts/teams_chat/` (`tenant.py`, `assist.py`); after `CT-i-1` it has
`assist.work_request(...)` and a text that says `WORK REQUESTED by ...` with a recommendation.

### AMENDMENT 1 (issuer; do this FIRST, before the build below)

Rows NFRA_CTLPLN-W31-S1 and S2 (ARMED, disarm owner the issuer) name three cases of
`data/transcripts/scripts/tests/test_teams_chat_jobs.py` that pin the contract `CT-i-1` changed:
`test_open_offers_to_every_device_and_sets_the_award_alarm`, `test_both_bids_award_at_once_to_the_lighter_box` and
`test_complete_texts_a_draft_for_the_requester_and_1_sends_it_to_the_chat`. That file is now in your `<paths>`. Bring those
three cases to the new contract: the offer goes to every box of `NAMES["bus_devices"]` (derive the count, type no box
name the file does not already use), the early award needs a bid from every offered box, and a completion carries `coo`
and a PASS `grade` by a `3.0.0_SA_CVO` serial. Remove no case and weaken no assertion that still holds; touch no other
case. Commit that repair as its own commit. In your final report give the exact command you used to run the seven
teams-chat and End of Day test files and its last line, which must show 0 failed; rows S1 and S2 are disarmed by it.

### BUILD, IN THIS ORDER

1. **Measure first.** In your deliverables folder, `MAIL_ROUTE_MEASURED.md`, from READING the code and the documents it cites
   (make no request): what the gateway's headless mail route allows today (which paths, whether it can LIST messages, whether
   it returns a body, which senders it admits), with file and line for each; what a read of his mailbox for requests under
   clause 9 needs that the route does not give; and where the estate records each of the five firms' mail domains (path,
   key, and the value's claim: measured, held or absent). If any of the five has NO recorded mail domain, that is a surprise
   row, class BLOCKING for that firm only: you build the rest, the missing firm's mail is not considered, and you type no
   domain.
2. `data/transcripts/scripts/teams_chat/mail_requests.py` (standard library plus what `assist.py` already imports):
   - `firm_domains()` returns {firm: [domains]} read from the records step 1 found; no domain string is typed in this file or
     in any test that runs against the real records.
   - `considered(message, domains)` returns (bool, reason): True only when the sender address's domain (case-folded, exact
     match on the registered domain or a sub-domain of it) is one of the five's AND the body, as plain text, names "Andrew" as
     a whole word (any case). `reason` is one of "ok", "sender_domain", "body_no_andrew", "no_sender", "no_body".
   - `on_mail_messages(ctx)`: the handler for a payload {`messages`: [...]}. For each message it calls `considered` FIRST. A
     message that fails is counted by reason and dropped: neither its body nor its subject is passed to any function that
     calls the model, logged, or kept in state. A message that passes goes through `assist.work_request`; when `is_work` is
     True it becomes ONE text to Andrew through the same `offer` path a chat uses, kind "mail", the head line reading
     `#<tag> Mail - <sender name>, <firm>`; when False nothing is texted. It returns a string like the other handlers and
     keeps in state only counts by reason and the pending item.
   - `ROUTE = ("mail.messages", on_mail_messages)`: the one entry the issuer adds to `tenant.ROUTES` at the merge. Do NOT edit
     `tenant.py`, `assist.py` or anything under `data/transcripts/scripts/outlook/`.
3. `data/transcripts/scripts/tests/test_inbound_mail.py`, run as a plain script, the model and every send faked, invented
   senders and invented domains injected for the unit cases:
   - a message from a listed domain whose body names Andrew and asks for work yields one text beginning with its tag and
     `Mail -`, containing `WORK REQUESTED by`;
   - the difference control: the same message from an unlisted domain, and the same message with no "Andrew" in its body,
     each yield no text AND the fake model records ZERO calls for them; "Andrews" and "andrew" inside another word do not
     count as naming him, "ANDREW," does;
   - a passing message that asks for nothing yields no text;
   - a sub-domain of a listed domain passes; a look-alike (the listed domain as a prefix of a longer one) does not.
   LAST line `INBOUND-MAIL-TEST ok=<True|False> cases=<passed>/<total> model_calls_on_failed=<n>` (`ok=True` needs that last
   count to be 0).
4. `python data/transcripts/scripts/teams_chat/mail_requests.py --check-domains` prints one line per firm with its domain
   count and NO domain string, then LAST `MAIL-DOMAINS ok=<True|False> firms=<f>/5 typed=0`. `ok=True` needs every firm that
   has a recorded domain to load, and the count of firms with none to equal the count of BLOCKING rows you filed (pass it as
   `--expect-missing <n>`, default 0).

### RULES FOR THIS CELL

- **Nothing you run leaves this machine.** No gateway call, no mail read, no model call, no text, no AWS call. No real
  message, subject, address or person's name appears in any file you write; test messages are invented.
- A message that fails either test must never reach the model: that is the cell.
- Reply by mail is NOT built here; `MAIL_ROUTE_MEASURED.md` says in one paragraph what telling a mail requester the outcome
  would need.
- No non-ASCII in any file you write. Bake no absolute path.
- Refuse a criterion you cannot satisfy as written and report the refusal with its measurement; do not repair or widen it.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTi3-AC1" cell_refs="CT-i-3"><invocation>python data/transcripts/scripts/tests/test_inbound_mail.py</invocation><expect>INBOUND-MAIL-TEST ok=True</expect></criterion>
`CTi3-AC1` -- the two tests with their difference control: a message failing either reaches no model; one passing both and asking for work becomes one text.

<criterion id="CTi3-AC2" cell_refs="CT-i-3"><invocation>python data/transcripts/scripts/teams_chat/mail_requests.py --check-domains --expect-missing 2</invocation><expect>MAIL-DOMAINS ok=True</expect></criterion>
`CTi3-AC2` -- the seam with the real neighbour: the five firms' domains load from the estate's real records and none is typed. If you filed BLOCKING rows for firms with no recorded domain, record the run with `--expect-missing <n>` beside this one in your report and leave this criterion FAIL: the issuer rules it.
`CTi3-AC2`, AMENDMENT 2 (issuer ruling on rows W31-S4 and W31-S5): Alongside and Opal have no mail domain in the estate's firm
records, measured by the cell; no domain is typed to fill the gap. The criterion is run with `--expect-missing 2`: the three
recorded firms load, the two unrecorded ones are named and their mail is NOT considered until the firm records carry them. The
two record rows are asked of `1.0.0_SA_CTO` by the issuer. Re-run it, record the new output in the instance as PASS,
re-validate, and flip `<status>` to `complete`.
</proof_of_spec>

<expected_criteria>CTi3-AC1,CTi3-AC2</expected_criteria>

Each invocation runs under `timeout 120`. Write the proof instance to
`org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~31/NFRA_CTLPLN.TO-CT-i-3.mail-requests-two-tests.proof_of_spec.json`,
validate it with `python .tools/proof-of-spec-check.py <instance> CTi3-AC1,CTi3-AC2`, and flip `<status>` to `complete` only when
every criterion passes and the instance is VALID.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.inbound1.md</decomp_doc>
<owned_cells>CT-i-3</owned_cells>
</decomp_ref>

<paths>
data/transcripts/scripts/teams_chat/mail_requests.py
data/transcripts/scripts/tests/test_inbound_mail.py
data/transcripts/scripts/tests/test_teams_chat_jobs.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell adds a handler, not a clock; the mail poll's clock is set by the deploy order after the drain.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call and no policy.
comp-adversary: RUN -- mail content from an unlisted sender reaching a model (considered runs first; the fake model counts zero calls on a failed message; a criterion); a typed domain drifting from the firm records (domains are read, the check prints typed=0); a look-alike domain admitted (exact or sub-domain match only, tested); a failed message kept in state or logs (only counts by reason are kept); a firm with no recorded domain silently skipped (a BLOCKING row and an expected-missing count). BLIND: the gateway's route is not called, so whether it can list and return bodies today is a READ of its caller and contract, stated as such in the measured file; the real read is after the drain and may need NFRA_OPLGTW.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: PRD `prd/NFRA_CTLPLN_PRD.md` v0.18 @55e2de3227 (ADMITTED), ADDENDUM v0.18 item 1 (C-SEATS clause 9); Andrew-direct
~21:4xZ at the 2.0.0_SA_COO~R terminal (record @4f53112d76); CTO ruling msg 106585.
