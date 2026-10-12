# TO NFRA_TRNSPT.TO-TR-sw23 -- the drafter posts its draft to the request's own ticket, and leaves a count of the ones that did not land

<to_id>NFRA_TRNSPT.TO-TR-sw23</to_id>
<project>NFRA_TRNSPT</project>
<issued_to>0.9.0_WK_NFRA_TRNSPT~1</issued_to>
<issued_by>2.0.0_SA_COO~T2</issued_by>
<issued_date>2026-10-12</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>23</round>
<workstream>routeswitch</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Decomp cell:** `TR-sw-23` (`decompositions/NFRA_TRNSPT_DECOMP_R23.md`, AMENDMENT 2) | **outcome_ref:** FWD-10 |
**depends_on:** none (the two upstream releases are live: the ticket route's request-id match, and the draft store's `ticket_id`)

---

## WORKER FACE

### THE CELL

`TR-sw-23`. Today, on the queue path, the commentary drafter stores its draft in IRPT's draft store and stops (`stage: draft_stored`).
Two things changed upstream, both live:
- IRPT's draft store now answers a first successful `put` with a top-level `ticket_id` beside `commentary_ref`, when the request's
  accepted record names a ticket (`infra/aws/lambda/investor-reporting/reports/commentary_draft_store.py`, docstring lines 12-13).
- Ticket Center serves `POST /api/scoped/tickets/{ticketId}/commentary-draft` for the drafter only. Body: EXACTLY two keys,
  `draft_commentary` and `request_id`. 200 = set. 403 = one deny for every reason. 409 with a `code`: `DRAFT_ALREADY_SET`,
  `DRAFT_WRONG_TICKET_TYPE`, `DRAFT_TICKET_COMPLETED`, `DRAFT_TICKET_CHANGED`. The ticket accepts the draft only if its own recorded
  request id equals the one in the body.

Make the drafter post its draft to that ticket, and make every post that did not land visible to a seat on demand.
Everything is in `data/transcripts/scripts/commentary/`. READ `lambda_handler.py` and `ticket_client.py` whole first.

**1. The store port carries the ticket id** (`lambda_handler.py`, `make_draft_store`). `persist_draft` returns the three stored fields as
today, plus `ticket_id` when the store's answer carries a top-level `ticket_id` that is a non-empty string matching
`^[A-Za-z0-9-]{1,64}$`. Anything else: no `ticket_id` key. `existing_draft` (the `get_ref` replay) is unchanged and never returns one.

**2. The post** (`ticket_client.py`, a NEW function; `write_draft_ticket`, `build_body` and `stub_post` are NOT changed).
`post_draft_to_ticket(draft, ticket_id, request_id, *, post, token_reader)`:
- path `/api/scoped/tickets/<ticket_id>/commentary-draft`; refuse (no HTTP) a `ticket_id` that fails the pattern above.
- body EXACTLY `{"draft_commentary": {"text", "model", "generated_at", "status": "DRAFT"}, "request_id": request_id}`: the same four
  `draft_commentary` members `build_body` builds (text cut at `MAX_TEXT`), nothing else.
- NEVER raises. Returns `{"outcome", "status", "code"}` with `outcome` one of:
  `POSTED` (200); `ALREADY_SET` (409 with code `DRAFT_ALREADY_SET`); `REFUSED` (403, 404, any other 409, 400);
  `FAILED` (any other status, or an exception from `post` or `token_reader`). `code` is the 409 body's `code` or `None`.
- ONE attempt. No retry loop.

**3. The handler** (`lambda_handler.py`, the queue path only: the run that today ends `STAGE_DRAFT_STORED`). After `persist` and the
ONE `commentary_ready` send, both unchanged and in today's order:
- the stored answer has a `ticket_id` -> call `post_draft_to_ticket` once with the run's `rid`, then log EXACTLY one line
  `COMMENTARY-POST request_id=<rid> outcome=<OUTCOME> status=<status or -> code=<code or ->` and append the result with stage
  `draft_posted` (POSTED or ALREADY_SET), `draft_post_refused` (REFUSED) or `draft_post_failed` (FAILED).
- no `ticket_id` -> log `COMMENTARY-POST request_id=<rid> outcome=NO_TICKET status=- code=-`; the stage stays `draft_stored`.
- The line carries the request id and nothing else of the request: no ticket id, no tenant, no draft text.
- **A failed or refused post is NOT handed back to the queue** (it adds no `batchItemFailures` entry). A redelivered message finds the
  draft already stored, and a replay carries no ticket id, so a redelivery could never post it; it would only start nothing, forever.
- **On a replay** (`existing_draft` true): unchanged. Stage `draft_exists`, no post, no `COMMENTARY-POST` line.
- The stream path (records that are not queue messages) is unchanged: it still ends in `write_draft_ticket`.

**4. The on-demand count** (a NEW file `post_census.py`; a seat runs it, nothing schedules it).
- `census(lines)`: given log lines, keep the `COMMENTARY-POST` ones; per request id take its LAST outcome; return
  `{"with_ticket": n, "posted": n, "unposted": n, "no_ticket": n, "unposted_request_ids": [...]}` where `with_ticket` counts request
  ids whose last outcome is POSTED, ALREADY_SET, REFUSED or FAILED, `posted` counts POSTED and ALREADY_SET, and `unposted` counts
  REFUSED and FAILED.
- CLI `python post_census.py --live --since <ISO8601>` reads the function's log group (name from the commentary `NAMES.json`
  lambda name, `/aws/lambda/<name>`; `filter_log_events` with EVERY page followed) and prints ONE line
  `POST-CENSUS since=<iso> lines=<n> with_ticket=<n> posted=<n> unposted=<n> no_ticket=<n>` then one request id per unposted line.
  `--from-file <path>` reads lines from a file instead (the tests use this). It reads only; it writes nothing and sends nothing.

**Tests**, in a NEW file `data/transcripts/scripts/tests/test_commentary_route_switch.py` (fakes only; no AWS, no HTTP, no model):
- `test_persist_answer_carries_ticket_id_when_the_store_names_one` (and none when the store's answer has none or an ill-formed one)
- `test_post_goes_to_the_named_ticket_with_exactly_two_body_keys`
- `test_no_ticket_id_means_no_post`
- `test_refused_post_is_logged_and_not_handed_back_to_the_queue` (a 403: stage `draft_post_refused`, one log line, no batch failure)
- `test_replay_of_a_stored_draft_posts_nothing`
- `test_census_counts_unposted_drafts` (last outcome wins; a later POSTED clears an earlier FAILED)

### ACCEPTANCE

<criterion id="TR23-sw23-AC1" cell_refs="TR-sw-23"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T2/R23_CHECKS/r23_checks.py sw23</invocation><expect>R23-SW23-OK</expect></criterion>
`TR23-sw23-AC1` -- the six named tests exist and every commentary test file passes together.

<expected_criteria>TR23-sw23-AC1</expected_criteria>

Dry-run at the base: `R23-SW23-FAIL absent: data/transcripts/scripts/tests/test_commentary_route_switch.py` -- FAIL as expected.

## BOUNDS

- **Grant.** The paths below, this order's file, your deliverables folder.
- **LOCAL.** No AWS or HTTP call, no model call, no deploy, no Terraform, no change to `drafter.py`, `entry.py` or anything under
  `infra/`. The ticket API base is an environment value and is NOT this order's (the deploy cell changes it). ASCII only.
- Run ONLY the acceptance check and the commentary test files it names; do NOT run the whole tests directory (another test there
  rewrites a tracked fixture). If `git status` shows a path outside your grant modified, restore it with `git checkout -- <path>`.
- An existing test that pins the queue path's results may need its expected stage or log lines updated; change only what this cell
  changes, and name each edit in your report.
- If the handler cannot do step 3 without changing the order of `persist` and the `commentary_ready` send, or without touching the
  stream path, file a surprise row (`NFRA_TRNSPT-D2-W1-S<k>`, next unused across every document under `surprise-channel/`; recent
  rows are single-object json fenced blocks appended to INVESTIGATION_v1.md) naming why, and stop.

<paths>
data/transcripts/scripts/commentary/lambda_handler.py
data/transcripts/scripts/commentary/ticket_client.py
data/transcripts/scripts/commentary/post_census.py
data/transcripts/scripts/tests/test_commentary_route_switch.py
data/transcripts/scripts/tests/test_commentary_live_ports.py
data/transcripts/scripts/tests/test_commentary_seam.py
org/missions/D9/NFRA/NFRA_TRNSPT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant (your deliverables folder is granted by the tree convention). Everything else named here you READ.
The two existing test files are granted only so a test that pins the old queue-path result can be updated.

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_TRNSPT/decompositions/NFRA_TRNSPT_DECOMP_R23.md</decomp_doc> (round 23, AMENDMENT 2), cell `TR-sw-23`.
<owned_cells>TR-sw-23</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: TR23-sw23-AC1. Instance at `org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/0.9.0_WK_NFRA_TRNSPT~1/NFRA_TRNSPT.TO-TR-sw23.drafter-posts-draft-to-the-requests-ticket.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> TR23-sw23-AC1` BEFORE the flip. Commit first, then pin.
</proof_of_spec>

**REPORT:** the functions changed and added with their line ranges; the exact body the post sends; each outcome and what the
handler does with it; the six test names with pass or fail; every existing test edited and why; the check line; commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a repo build; the deploy (code plus the ticket base's move to the front door) is cell TR-sa-23 under its own pair.
comp-iam: DECLARED-NOT-APPLICABLE -- no new AWS call in the function (the census CLI reads a log group as the seat that runs it).
comp-adversary: RUN -- sources: CTO msgs 5832, 5854, 5934, 5988, 5992, 6034, 6204; IRPT_BCKEND PRD v0.45 (the store's answer); 2.0.0_SA_COO~V2 msg 5985 (the route as live). Traps: a ticket id used unchecked in a URL path (the pattern, refused before any HTTP); a third body key (the route answers 400 to any other key; a test pins exactly two); a refused post redelivered forever (not handed back; stated why); the draft text or the ticket id in a log line (the line carries the request id only; tests assert it); a count that is a monitor (a CLI a seat runs; nothing schedules it). BLIND: the live route's answers (every arm is UNEXERCISED by V2's own word) and the front door's handling of the service bearer -- the deploy cell's driven proof measures both.
lane: the paths block.
</preflight>

Source: the CTO's release msg 6204; decomposition round 23 AMENDMENT 2, cell TR-sw-23.
