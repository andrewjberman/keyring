# TO NFRA_TRNSPT.TO-TR-t12 -- FWD-10 hop H6: the ticket-write client to ~V2's agreed contract, with its stub

<to_id>NFRA_TRNSPT.TO-TR-t12</to_id>
<project>NFRA_TRNSPT</project>
<issued_to>0.9.0_WK_NFRA_TRNSPT~3</issued_to>
<issued_by>2.0.0_SA_COO~T2</issued_by>
<issued_date>2026-10-08</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>12</round>
<workstream>communications</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Decomp cell:** `TR-t-12` (`decompositions/NFRA_TRNSPT_DECOMP_R12.md`) |
**outcome_ref:** FWD-10 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`TR-t-12`: hop H6 of FWD-10. Put a DRAFT commentary into a Ticket Center ticket of the new type `analysis_request` for the person who
generated the report (C-TICKET, `org/missions/D9/NFRA/NFRA_TRNSPT/prd/NFRA_TRNSPT_PRD.md:118`: "A new ticket type `analysis_request`; the
draft text in the ticket and the report as an ATTACHMENT; requester name and firm on the ticket ... The Ticket Center is internal-only";
until the attachment work lands "the ticket carries text and a report link", `:119`). The ticket TYPE and requester-claim are built by
TCKT_VNEXT (`2.0.0_SA_COO~V2`), not you; you write against a contract and a fake.

**THE CONTRACT YOU CODE TO (agreed by the issuer, msg to ~V2):** `org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/FWD10_H6_H5_TICKET_WRITE_CONTRACT.md`
v0.1 @a8410fcca3 -- READ it in full. Section 2 is the ONE call (`POST {api_base}/api/scoped/tickets`, `Authorization: Bearer <svc-commentary
token>`) and its exact body (`ticket_type: "analysis_request"`, `title`, `source: "commentary:<request_id>"`, `answers{advisor, firm,
household, report_type, comparison_model, add_commentary: true}`, `attachment{upload_id, input_id}`, `report_request_id`,
`draft_commentary{text <= 8000 chars, model, generated_at, status: "DRAFT"}`, optional `requester_email`, `requester_name`). Section 4 is
the responses and what H6 does (201 done; 400/403 dead-letter, NO retry; 5xx/timeout transient -> retry via the DLQ policy). Section 5 is the
stub: assert the body against section 2 and return a synthetic 201 `ticket_id = "TCK-00000000-stub0000"`. Issuer ruling on O3: draft for
EVERY READY report (FWD-10's DONE WHEN carries no condition); `add_commentary` is sent `true`.

**Build:**
1. `data/transcripts/scripts/commentary/ticket_client.py`: `write_draft_ticket(draft, ticket_context, *, post, token_reader) -> dict`.
   `draft` is the drafter's output (`request_id`, `draft_text`, `provenance`, `status: "DRAFT"`); `ticket_context` is H2's separate ticket
   output (`report_request_id`, `advisor`, `firm`, `household`, `report_type`, `comparison_model`, `upload_id`, `input_id`,
   `requester_email`, `requester_name`). `post(path, headers, body) -> (status, json)` and `token_reader() -> str` are injected (no HTTP, no
   secret read in this cell). Build the section-2 body exactly (truncate the draft text to 8000 chars and say so in the result), POST it, and
   map section 4: return `{"ok", "ticket_id", "status", "action": "done" | "dead_letter" | "retry", "error"}`. ANY failure (exception, non-2xx,
   timeout) is caught and returned -- it NEVER raises (the report path must not fail: C-TRIGGER).
   Also `stub_post(path, headers, body)` -- section 5's stub: validates the body against section 2 (required keys, `ticket_type`,
   `draft_commentary.status == "DRAFT"`, text length) and returns `(201, {"ticket": {"ticket_id": "TCK-00000000-stub0000"}})` or `(400, ...)`.
2. `data/transcripts/scripts/tests/test_commentary_ticket_client.py`, at least: `test_writes_analysis_request_ticket` (with `stub_post`: the
   body passes the stub, `ok` true, `ticket_id` the stub id, `add_commentary` true, the draft text and status DRAFT present);
   `test_failure_never_raises_into_report_path` (a `post` that raises, one returning 500 -> `action: "retry"`, one returning 400 ->
   `action: "dead_letter"`; nothing raised); a test that an over-8000-char draft is truncated and flagged.

### ACCEPTANCE

<criterion id="TR12-t12-AC1" cell_refs="TR-t-12"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T2/R12_CHECKS/r12_checks.py t12</invocation><expect>R12-T12-OK</expect></criterion>
`TR12-t12-AC1` -- the named tests pass against the contract's stub.

<expected_criteria>TR12-t12-AC1</expected_criteria>

Dry-run at the base (box/dell2 846cbbe61e): `R12-T12-FAIL absent` -- FAIL as expected.

## BOUNDS

- **Grant.** The paths below, this order's file, your deliverables folder. `ticket_center` code is READ only.
- **LOCAL.** No AWS, HTTP or gateway call. Synthetic drafts only.
- **Refusal clause.** If the contract's section 2 cannot be built from the draft and ticket context as given, do not invent a value: file a surprise row (id `NFRA_TRNSPT-D2-W3-S<k>`, next unused across every document under `surprise-channel/`).

<paths>
data/transcripts/scripts/commentary/ticket_client.py
data/transcripts/scripts/tests/test_commentary_ticket_client.py
org/missions/D9/NFRA/NFRA_TRNSPT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant (your deliverables folder is granted by the tree convention). Everything else named here you READ. If
`data/transcripts/scripts/commentary/__init__.py` is absent in your worktree, import `ticket_client` by path in tests; do not create it.

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_TRNSPT/decompositions/NFRA_TRNSPT_DECOMP_R12.md</decomp_doc> (round 12), cell `TR-t-12`.
<owned_cells>TR-t-12</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: TR12-t12-AC1. Instance at `org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/0.9.0_WK_NFRA_TRNSPT~3/NFRA_TRNSPT.TO-TR-t12.commentary-ticket-client.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> TR12-t12-AC1` BEFORE the flip. Commit code first, then pin each artifact to a
commit that actually contains it.
</proof_of_spec>

**REPORT:** the result shape, the test names, the check line, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a client and a contract draft; no deploy.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS or HTTP call.
comp-adversary: RUN -- 2 sources read (PRD C-TICKET/C-TRIGGER, ~V2's contract v0.1 @a8410fcca3); BLIND to the svc-commentary token (contract O1, not minted) and the live write (no live write until H5's deploy closes). Traps: a ticket write that raises into the report path, a field the submit seam refuses, the draft reading as sent; the face fixes each.
lane: one commentary module, one test, the investigation file.
</preflight>

Source: Andrew-direct @a4fdb78bbe; CTO msgs 1763, 1780; decomposition round 12 cell TR-t-12.
