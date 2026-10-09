# TO NFRA_TRNSPT.TO-TR-e12 -- FWD-10 hop H2: the READY event becomes one abstract request (+ the READY-event contract draft)

<to_id>NFRA_TRNSPT.TO-TR-e12</to_id>
<project>NFRA_TRNSPT</project>
<issued_to>0.9.0_WK_NFRA_TRNSPT~1</issued_to>
<issued_by>2.0.0_SA_COO~T2</issued_by>
<issued_date>2026-10-08</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>12</round>
<workstream>communications</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Decomp cell:** `TR-e-12` (`decompositions/NFRA_TRNSPT_DECOMP_R12.md`) |
**outcome_ref:** FWD-10 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`TR-e-12`: hop H2 of FWD-10 ("When someone generates an analysis report in Investor Reporting, a draft commentary in Opal's voice appears
for an Opal person to review, without slowing the report"; `org/missions/D9/NFRA/NFRA_TRNSPT/prd/NFRA_TRNSPT_PRD.md:76-81`). H1 (owned by
IRPT_BCKEND, not you) will deliver a READY event when a report is READY; you turn it into ONE abstract request for the slicer and drafter.

**Contracts to honor:** C-KIMI (`prd :117`): the model sees "abstract fields (variant, model names, account type, themes, holdings as
category weights; no client identity, no account ids)". C-SLICE (`prd :116`): the request carries `yc_variant` (1/2/3 from models referenced
0/1/2+), `comparison_keys`, `account_type`. C-TRIGGER (`prd :120`): the hook is a DynamoDB stream on `irpt-requests` filtered to `REPORT#`
items; "the commentary must never block or fail the report".

**Read (do not edit):** `infra/aws/lambda/investor-reporting/reports/request_composition.py` (the retained composition; `browser` carries
`comparison_keys`, see :179-191), `infra/aws/lambda/investor-reporting/ops/owned_requests.py:105-120` (the frozen `comparison_keys` and
catalogue names), `data/transcripts/scripts/outlook/slicer.py` (what the slicer consumes as a request).

**Build:**
1. `data/transcripts/scripts/commentary/__init__.py` (empty) and `data/transcripts/scripts/commentary/entry.py`:
   - `abstract_request(ready_event, composition_reader) -> dict` with exactly: `request_id`, `yc_variant` (1 when 0 comparison keys, 2 when
     1, 3 when 2+), `comparison_keys` (catalogue model names, as `owned_requests` derives them), `account_type`, `themes` (list of theme
     labels only, no figures tied to a client), `holdings_categories` (category -> weight, rounded to whole percent, no tickers of the
     client's own positions), `requester` (the Opal person's display name only). `composition_reader(request_id)` is injected (tests use a
     fake; no AWS call in this cell).
   - It NEVER emits: client name, firm name, account number or id, advisor email, household, any free text from the client. A whitelist of
     output keys, not a blacklist.
   - `ticket_context(ready_event, composition_reader) -> dict`, a SEPARATE output for the ticket write (H6) only, never passed to the
     model: `report_request_id`, `advisor`, `firm`, `household`, `report_type` (Overview | Comparison | Multi-Comp), `comparison_model`,
     `upload_id`, `input_id`, `requester_email`, `requester_name` -- the fields of the agreed ticket-write contract's body
     (`org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/FWD10_H6_H5_TICKET_WRITE_CONTRACT.md` v0.1 @a8410fcca3, section 2).
     Ticket Center is internal-only
     (C-TICKET), so these may appear there; they must never appear in `abstract_request`.
   - `handler(event, context, reader=None)` -- a Lambda-shaped entry: for each record in a DynamoDB-stream-shaped event whose key starts with
     `REPORT#` and whose new image is READY, build the request; any exception is caught, logged with the request id only, and returned in a
     `failed` list (never raised -- the report path must not fail).
2. `org/standards/NFRA_TRNSPT_READY_EVENT_CONTRACT.json` -- the DRAFT contract for H1 -> H2 that IRPT_BCKEND will agree: `{"version": 1,
   "producer": "IRPT_BCKEND (2.0.0_SA_COO~P2)", "consumer": "NFRA_TRNSPT (2.0.0_SA_COO~T2)", "transport": "...", "fields": {<name>:
   {"type", "required", "source"}}, "never_contains": [...], "failure": "async; DLQ + retry; never blocks the report"}`. Fields are the
   MINIMUM H2 needs from the event (e.g. the request id and status); everything else H2 reads from the retained composition by id.
3. `data/transcripts/scripts/tests/test_commentary_entry.py`, at least: `test_ready_event_to_abstract_request` (a stream-shaped fixture event
   + a fake composition -> the exact output keys and variant 3 for 2 keys); `test_abstract_request_carries_no_client_identity` (the fake
   composition plants a client name, firm, account number and an email; none appears anywhere in the JSON-serialised output); a test that a
   non-REPORT# record and a non-READY image are skipped; a test that a reader exception lands in `failed` and does not raise.

### ACCEPTANCE

<criterion id="TR12-e12-AC1" cell_refs="TR-e-12"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T2/R12_CHECKS/r12_checks.py e12</invocation><expect>R12-E12-OK</expect></criterion>
`TR12-e12-AC1` -- the contract draft parses with its fields, producer, consumer and version; the named tests pass.

<expected_criteria>TR12-e12-AC1</expected_criteria>

Dry-run at the base (box/dell2 846cbbe61e): `R12-E12-FAIL absent` -- FAIL as expected.

## BOUNDS

- **Grant.** The paths below, this order's file, your deliverables folder. IRPT code is READ only.
- **LOCAL.** No AWS, gateway, HTTP or model call. Synthetic fixtures only; synthetic names (e.g. `planted.client@example.test`).
- **Refusal clause.** If the retained composition cannot supply a field the contract needs, leave it nullable in the contract with a
  `source: "unknown -- producer to confirm"` and file a surprise row (id `NFRA_TRNSPT-D2-W1-S<k>`, next unused across every document under
  `surprise-channel/`). Never invent a source.

<paths>
data/transcripts/scripts/commentary/__init__.py
data/transcripts/scripts/commentary/entry.py
data/transcripts/scripts/tests/test_commentary_entry.py
org/standards/NFRA_TRNSPT_READY_EVENT_CONTRACT.json
org/missions/D9/NFRA/NFRA_TRNSPT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant (your deliverables folder is granted by the tree convention). Everything else named here you READ.

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_TRNSPT/decompositions/NFRA_TRNSPT_DECOMP_R12.md</decomp_doc> (round 12), cell `TR-e-12`.
<owned_cells>TR-e-12</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: TR12-e12-AC1. Instance at `org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/0.9.0_WK_NFRA_TRNSPT~1/NFRA_TRNSPT.TO-TR-e12.commentary-entry.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> TR12-e12-AC1` BEFORE the flip. Commit code first, then pin each artifact to a
commit that actually contains it.
</proof_of_spec>

**REPORT:** the contract's field list, the output keys, the test names, the check line, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a handler and a contract draft; no schedule, no deploy.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the stream subscription is H1's (IRPT_BCKEND).
comp-adversary: RUN -- 4 sources read (PRD C-KIMI/C-SLICE/C-TRIGGER, request_composition :179-191, owned_requests :105-120, slicer); BLIND to the live irpt-requests item shape (the producer agrees the contract). Traps: client identity leaking into the abstract request, an exception raised into the report path, an invented field source; the face whitelists keys, catches failures and forbids invention.
lane: a new commentary package file, one test, one contract draft, the investigation file.
</preflight>

Source: Andrew-direct @a4fdb78bbe; CTO msgs 1763, 1780; decomposition round 12 cell TR-e-12.
