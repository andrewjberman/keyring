# TO COMM_ASSIST.TO-CA-m-1 -- round 9 CA-m-1: a mail poller feeds the assistant from the gateway's domain mail route

<to_id>COMM_ASSIST.TO-CA-m-1</to_id>
<project>COMM_ASSIST</project>
<issued_to>0.9.0_WK_COMM_ASSIST~2</issued_to>
<issued_by>2.0.0_SA_COO~R</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>9</round>

**Directive:** D9 | **Fabric:** laptop | **Decomp cell:** `CA-m-1` (`decompositions/COMM_ASSIST_DECOMP.round9.md`) | **outcome_ref:** FWD-4 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

`CA-m-1`. Andrew's assistant (a Lambda; code in `data/transcripts/scripts/teams_chat/`; its minute clock is `tenant.ingress`) has a
mail handler (`mail_requests.on_mail_messages`, kind `mail.messages`) but NOTHING feeds it: no code reads mail. The Opal gateway
(another project's, being released separately) serves a mail route under its own bearer, and this cell builds the poller against
it. Read `infra/aws/ec2/opal-gateway/app/mail_route.py` (the docstring and the listing handler, ~lines 1-45 and ~380-435, and
`_window`) for the exact parameters:

- `GET /hx/mail/messages?sender_domain=<domain>&<window>&page_size=<1..50>[&page_token=...]` -> `{"rows": [minimal rows],
  "count", "next_page_token"}`; exactly one of `sender` / `sender_domain`; the window at most 31 days; a page may be short or
  empty with a next token; a domain not on the gateway's table is 403.
- `GET /hx/mail/messages/{message_id}` -> one message with its body (allow-by-key).
- Bearer: `MAIL_BEARER` (not the Teams bearer).

Use from `mail_requests.py` (read it): `firm_domains()` (the five firms' domains from the estate's records; NEVER type a domain),
`considered()` (the two tests). `assist.py` has the pattern for a gateway client (`Gateway`, `_call`, `_seg`, `secret()`,
`gateway()`), the state store (`get_json`, `put_json`, `state_key`), `log`, `now_utc`, `iso`. `ldo.send(object_id, kind, payload,
event_id=...)` queues an event; the event id de-duplicates. How tests inject fakes: `data/transcripts/scripts/tests/test_teams_chat_tenant.py`
and `test_inbound_mail.py`.

### BUILD, IN THIS ORDER

1. `assist.py`: a `MailGateway` client beside `Gateway` (same `fetch` injection, same error type), base path `/hx/mail`, methods
   `list_domain(domain, start, end, page_token=None, page_size=50)` and `message(message_id)`, its bearer from a NEW secret name
   constant `MAIL_BEARER_SECRET` read from an environment variable of that name (no value is baked), and `mail_gateway()`.
   Nothing else in `assist.py` changes.
2. NEW `data/transcripts/scripts/teams_chat/mail_poll.py` with `poll(mg, now) -> dict`:
   - runs its listing at most once every `MAIL_EVERY_S = 300` seconds (a stamp in state `mail_poll.json`) and makes at most
     `MAX_CALLS = 20` gateway calls per run, round robin over the domains;
   - per domain, its own cursor (the newest received time seen) in `mail_poll.json`; the window is `[cursor - LAG_MARGIN_S (900),
     now]`, never over 31 days; the first run (no cursor) records now and sends nothing;
   - follows `next_page_token` until none, within the call budget; a domain cut short keeps its old cursor;
   - for each listed message id not yet seen (a set of recent ids kept in state, bounded to the last 500), fetches it by id and
     sends `ldo.send("mail:<message id>", "mail.messages", {"messages": [<that row, unchanged>]}, event_id="mail-<message id>")`.
     It does NOT run `considered` (the handler does, first); it never logs a subject, body or address;
   - a 403 on a domain (not on the gateway's table yet) or any `GatewayError` is counted per reason and stops nothing;
   - returns and logs `assist.log("mail_poll", domains=, listed=, fetched=, sent=, calls=, refused=, failed=)`, counts only.
3. NEW `data/transcripts/scripts/tests/test_inbound_mail_poll.py` (a plain script, no network; fakes injected). Arms, each printing
   `ARM <name> ok=<True|False>`:
   - `first_run`: no cursor -> nothing sent, every domain gets a cursor.
   - `new_mail`: one new message on one domain -> one event, object `mail:<id>`, event id `mail-<id>`, payload the by-id row
     unchanged. **Difference control in the same arm:** the same message already in the seen set -> no event.
   - `pages`: a domain listing over three pages (one empty with a token) -> every message fetched once.
   - `budget`: five domains with many messages -> no run over `MAX_CALLS`; a domain cut short keeps its cursor and finishes next run.
   - `cadence`: a second call inside 300 s makes no gateway call.
   - `refused`: a 403 on one domain is counted as refused and the others are read.
   - `no_content_logged`: the log line carries counts only (no subject, body, address or domain string).
   - `domains_not_typed`: the poller's domains come from `firm_domains()`; the test patches it and the poller lists exactly those.
   LAST line `MAIL-POLL ok=<True|False> arms=<passed>/<total>`.

### RULES FOR THIS CELL

- **Nothing you run leaves this machine**: no gateway, Graph, S3, model or text call. Everything is injected.
- Edit nothing but the files in `<paths>`. Do NOT edit `tenant.py` (the issuer adds the minute-clock step at the merge; name the
  line it needs in your report) or `mail_requests.py` (another cell of this round changes it).
- No real mail, person's, client's or firm's name or domain in any file you write. No non-ASCII. Bake no absolute path or secret.
- Refuse a criterion you cannot satisfy as written and report the refusal with its measurement; do not repair or widen it.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CAm1-AC1" cell_refs="CA-m-1"><invocation>python data/transcripts/scripts/tests/test_inbound_mail_poll.py</invocation><expect>MAIL-POLL ok=True</expect></criterion>
`CAm1-AC1` -- the built behaviour and its difference control in one run: eight arms; a seen message sends nothing.

<criterion id="CAm1-AC2" cell_refs="CA-m-1"><invocation>python "org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/2.0.0_SA_COO~R/checks/check_agent_suites.py"</invocation><expect>AGENT-SUITE ok=True</expect></criterion>
`CAm1-AC2` -- the cell's bound (the issuer's check; read it, do not edit it): the agent's existing suites still pass with the new `assist.py` client.
</proof_of_spec>

<expected_criteria>CAm1-AC1,CAm1-AC2</expected_criteria>

Each invocation runs under `timeout 120`. Write the proof instance to
`org/missions/D9/COMM/COMM_ASSIST/deliverables/0.9.0_WK_COMM_ASSIST~2/COMM_ASSIST.TO-CA-m-1.mail-poller.proof_of_spec.json`, validate
it with `python .tools/proof-of-spec-check.py <instance> CAm1-AC1,CAm1-AC2`, and flip `<status>` to `complete` only when both pass and
the instance is VALID. Your surprise rows are `COMM_ASSIST-W2-S<k>`; append lines only to the investigation file and keep its
existing line endings.

<decomp_ref>
<decomp_doc>org/missions/D9/COMM/COMM_ASSIST/decompositions/COMM_ASSIST_DECOMP.round9.md</decomp_doc>
<owned_cells>CA-m-1</owned_cells>
</decomp_ref>

<paths>
data/transcripts/scripts/teams_chat/mail_poll.py
data/transcripts/scripts/teams_chat/assist.py
data/transcripts/scripts/tests/test_inbound_mail_poll.py
org/missions/D9/COMM/COMM_ASSIST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE the poller runs inside the existing minute clock, at most once in 300 s, at most 20 calls.
comp-iam: DECLARED-NOT-APPLICABLE -- denominator: 0 policies and 0 AWS calls in this cell. BLIND: the agent's access to the mail bearer's secret is a later grant under a pair, after site Z's release.
comp-adversary: RUN -- a first-run flood of old mail (first run sends nothing, arm `first_run`); a duplicate text for one mail (seen set plus event id, arm `new_mail` control); content in logs (arm `no_content_logged`); a typed domain (arm `domains_not_typed`); a gateway hammered every minute (arms `cadence`, `budget`); a domain not yet admitted breaking the rest (arm `refused`). BLIND: the by-id row's exact keys are read from the route code and stubbed, not from a live call; the seam is probed after site Z's release.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: PRD `prd/COMM_ASSIST_PRD.md` v0.2 (ADMITTED, `805fec22c5`), FWD-4, C-MAIL; `1.0.0_SA_CTO` msg 107513.
