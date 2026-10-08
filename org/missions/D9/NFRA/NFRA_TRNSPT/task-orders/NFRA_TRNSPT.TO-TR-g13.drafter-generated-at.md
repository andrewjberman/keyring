# TO NFRA_TRNSPT.TO-TR-g13 -- row D2-S6: the drafter emits generated_at; the H4 -> H6 seam test

<to_id>NFRA_TRNSPT.TO-TR-g13</to_id>
<project>NFRA_TRNSPT</project>
<issued_to>0.9.0_WK_NFRA_TRNSPT~1</issued_to>
<issued_by>2.0.0_SA_COO~T2</issued_by>
<issued_date>2026-10-08</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>13</round>
<workstream>communications</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Decomp cell:** `TR-g-13` (`decompositions/NFRA_TRNSPT_DECOMP_R13.md`) |
**outcome_ref:** FWD-10 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`TR-g-13` (CTO round-12 analysis @a090c5ea23, E1; row NFRA_TRNSPT-D2-S6): "the drafter emits `generated_at`, matching ~V2's ticket contract
... the H6 contract test passes; the trace reaches H6 without a dead letter." The round-12 journey trace stopped at H6:
`write_draft_ticket` returned `action: dead_letter`, error "missing required value: 'generated_at'", because `drafter.draft()` returns
`request_id, draft_text, provenance, status` and ~V2's contract
(`org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/FWD10_H6_H5_TICKET_WRITE_CONTRACT.md` section 2) requires
`draft_commentary.generated_at` (ISO-8601 UTC).

**The code:** `data/transcripts/scripts/commentary/drafter.py` (`draft()`), `data/transcripts/scripts/commentary/ticket_client.py`
(`write_draft_ticket`, `stub_post`; read how it reads `generated_at` and `model` from the draft), `data/transcripts/scripts/commentary/entry.py`
and `data/transcripts/scripts/tests/test_commentary_entry.py` (the `stream_event()` / `composition()` fixtures).

**Build:**
1. `drafter.py`: `draft()` adds `generated_at` = the UTC time of the model call, ISO-8601 with a trailing `Z` (e.g.
   `2026-10-08T23:01:02Z`), taken from an injectable `now` (default `datetime.now(timezone.utc)`) so tests are deterministic. Keep every other
   output key unchanged. Fix ONLY the drafter: the ticket client already follows the contract.
2. `data/transcripts/scripts/tests/test_commentary_seam.py` (new), at least: `test_draft_carries_generated_at` (with a fixed `now`, the exact
   string); `test_drafter_output_writes_ticket_via_stub` -- the real chain on synthetic data: `entry.handler(stream_event(), reader=...)` ->
   `drafter.draft(abstract_request, [], model=<fake>, wipe_gate_passed=True)` -> `ticket_client.write_draft_ticket(draft, ticket_context,
   post=ticket_client.stub_post, token_reader=lambda: "t")` returns `ok` True, `action` "done", the stub ticket id. Import the entry fixtures
   from `test_commentary_entry.py` (by path if needed).
3. Keep `test_commentary_drafter.py`, `test_commentary_entry.py` and `test_commentary_ticket_client.py` green.

### ACCEPTANCE

<criterion id="TR13-g13-AC1" cell_refs="TR-g-13"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T2/R13_CHECKS/r13_checks.py g13</invocation><expect>R13-G13-OK</expect></criterion>
`TR13-g13-AC1` -- `generated_at` is emitted, and the drafter's real output writes a ticket through the stub with `action: done`.

<expected_criteria>TR13-g13-AC1</expected_criteria>

Dry-run at the base (box/dell2 b75b0669f1): `R13-G13-FAIL absent` -- FAIL as expected. The real Kimi call is the issuer's.

## BOUNDS

- **Grant.** The paths below, this order's file, your deliverables folder. `ticket_client.py`, `entry.py` and the contract are READ only.
- **LOCAL.** No model, AWS, HTTP or gateway call; fake model only. Do not edit another order's proof instance; no bulk edits.
- **Refusal clause.** If the seam needs a change outside `drafter.py` to reach `done`, stop and file a surprise row (id `NFRA_TRNSPT-D2-W1-S<k>`,
  next unused across every document under `surprise-channel/`) naming the field.

<paths>
data/transcripts/scripts/commentary/drafter.py
data/transcripts/scripts/tests/test_commentary_seam.py
data/transcripts/scripts/tests/test_commentary_drafter.py
org/missions/D9/NFRA/NFRA_TRNSPT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant (your deliverables folder is granted by the tree convention). Everything else named here you READ.

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_TRNSPT/decompositions/NFRA_TRNSPT_DECOMP_R13.md</decomp_doc> (round 13), cell `TR-g-13`.
<owned_cells>TR-g-13</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: TR13-g13-AC1. Instance at `org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/0.9.0_WK_NFRA_TRNSPT~1/NFRA_TRNSPT.TO-TR-g13.drafter-generated-at.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> TR13-g13-AC1` BEFORE the flip. Commit code first, then pin each artifact to a
commit that actually contains it.
</proof_of_spec>

**REPORT:** the generated_at format, the seam test's result line, the three related suites, the check line, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a one-field fix and a seam test.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call.
comp-adversary: RUN -- 4 sources read (drafter.py, ticket_client.py, ~V2's contract section 2, the round-12 trace); BLIND to the live H5 route (stubbed). Traps: fixing the client instead of the drafter, a non-UTC or naive timestamp, a seam test that uses fakes on both sides; the face fixes the drafter, pins UTC with Z, and runs the real entry -> drafter -> client chain.
lane: the drafter, two tests, the investigation file.
</preflight>

Source: CTO round-12 analysis @a090c5ea23 E1; row NFRA_TRNSPT-D2-S6; decomposition round 13 cell TR-g-13.
