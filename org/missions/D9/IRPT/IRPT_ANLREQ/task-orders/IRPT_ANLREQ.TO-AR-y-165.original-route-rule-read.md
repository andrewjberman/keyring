# TO IRPT_ANLREQ.TO-AR-y-165 -- a READ: the original-file route's rule, owner check and trusted headers, and which instrument can shape a caller as another firm's client

<to_id>IRPT_ANLREQ.TO-AR-y-165</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~54</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-12</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>16</round>
<workstream>Y</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL (a read of code and committed records; no live call, no product file changed)
**Decomp cell:** `AR-y-165` (`decompositions/IRPT_ANLREQ_DECOMP_R16_Y.md`) | **outcome_ref:** FWD-5 of this project (another firm refused each package file); TCKT_VNEXT FWD-2; CTO msg 6012 | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~54`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-54` (branch `wk-IRPT_ANLREQ-54`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~54 <0.9.0_WK_IRPT_ANLREQ~54@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `IRPT_ANLREQ-D2-W54-S<k>` (take the next free `<k>`). The worktree shows ` M portal` (and may show a modified `.parquet`
  fixture): never commit either. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` before its commit.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`;
  every non-PASS row carries a `status_reason`.

### THE CELL (`AR-y-165`, inlined) -- A READ. You change no product file and make no live call.

*The original-file route of `irpt-status`: its rule, its owner check, its trusted headers, and which instrument can shape a caller.*

Why. An outcome asks that someone signed in for a DIFFERENT FIRM is refused a request's files. One live arm has been run by another
lane: an Opal-INTERNAL caller with a firm list was refused the original-file route for two other firms. That is not the arm the
outcome names: no caller shaped as another firm's CLIENT has asked for the original of a REAL request, and no arm has reached a
real record, so the route's OWNER check has never run. The CTO ordered that arm (F2) and its twin (the record's own owner gets the
signed link's presence only, never written or followed) under a pair, and said: "Read the route's rule and trusted headers first
and say which instrument they allow." This cell is that read. The arm itself is not yours.

1. `route`: the original-file operation in `docs/contracts/investor-reporting/v1/routes.json` (find it: the route that returns the
   uploaded original of an analysis request) and its handler in `infra/aws/lambda/investor-reporting/ops/` (`entry.py`, `owned_report.py`'s original path):
   `{"operation": "...", "path": "...", "handler_file_function": "...", "owner_check_file_line": "<the line that compares the
   caller with the record's owner, and what it compares>", "firm_fence_file_line": "<the line that refuses another firm before
   any record is read>", "order_of_checks": "<fence, then record read, then owner check? with lines>", "what_each_refusal_is_served_as":
   {...}}`.
2. `trusted_headers` and `how_a_caller_is_shaped`: how the service learns WHO the caller is -- which request members or headers
   it trusts, set by what (the API gateway's authorizer? a verified token's claims? `_authz/served.py` and `_authz/loaders.py`),
   with lines; what distinguishes an Opal-internal caller from a firm's client in those members; and whether a DIRECT INVOKE of
   the function (bypassing the gateway) lets the invoker state those members itself.
3. `instruments`: every way a seat could present itself to this route as ANOTHER FIRM'S CLIENT, each `{"instrument": "<a direct
   invoke with a constructed event; a signed-in test user of that firm; a token minted by ...>", "can_shape_another_firms_client":
   true|false, "writes_anything": true|false, "what_it_writes_or_logs": "...", "who_can_use_it_today": "<identity; with the
   evidence: an earlier apply record under org/tier2_senior/ or a policy line>", "evidence": "..."}`. Read the earlier arm's record
   to see the instrument it used: `org/missions/D7/TCKT/TCKT_VNEXT/deliverables/` (the F1 arm; search that folder for the
   original-file route's name with the Grep tool).
4. `arms`: `{"other_firm_client": "<the exact request a seat would make and the refusal the code says it gets, with the line>",
   "owner_twin": "<the same for the record's own owner: what comes back, and that only the link's PRESENCE is recorded>",
   "what_is_never_written": "the signed link; any body content; a real request's id beyond the one already on the order",
   "what_a_real_request_is_needed_for": "<why a nonexistent id proves nothing here: which check it never reaches>"}`.
5. `not_read`: a list. Write `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~54/r16/ORIGINAL_ROUTE_RULE_READ.json`;
   commit it.

### ACCEPTANCE

<criterion id="AR165-y-AC1" cell_refs="AR-y-165"><invocation>python C:/dev/wk-irpt-anlreq-54/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r16/ar16_checks.py y165-read --root C:/dev/wk-irpt-anlreq-54</invocation><expect>Y165-READ-OK</expect></criterion>
`AR165-y-AC1`: the record names the route, its handler and its owner-check line, the trusted headers and how a caller is shaped,
at least one instrument with whether it can shape another firm's client and whether it writes, both arms, and what was not read.
It grades the record's form.

<expected_criteria>AR165-y-AC1</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~54/` and this order's
  file (status flip only).
- READ only: everything else. No live call, no push, no deploy, no upload, no apply, no invoke. No non-ASCII in what you add.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R16_Y.md</decomp_doc>
<owned_cells>AR-y-165</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR165-y-AC1. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~54/IRPT_ANLREQ.TO-AR-y-165.original-route-rule-read.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-165`. Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> AR165-y-AC1`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: RUN -- by reading 1 CTO message (6012: F1 used an internal caller with a firm list, was refused for two other firms, and no arm reached a real record) and 1 rollback record of this lane on the same function (release 5: its entry refuses any query member but selected_tenant at ops/entry.py:164-165); NOT seen: the original-file handler and the authorizer's trusted members (the worker reads them). comp-routes: DECLARED-NOT-APPLICABLE -- no route is added or called by this cell. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger; 0 scheduled readers of what this cell writes. comp-iam: RUN -- by reading 0 policies; the cell READS how a caller's identity reaches the function and which seat has invoked it before, and changes nothing; an instrument that needs a new grant is recorded as such, never used.
comp-adversary: RUN -- by reading 1 outcome sentence (someone signed in for a different firm) against the F1 arm; the lens: an arm that stops at the firm fence and is reported as the owner check. The face makes the order of checks and 'what a real request is needed for' required members. NOT seen: any live answer.
lane: the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on PRD v0.4 @4b1447e2cc ROUND-16 item 4 and CTO msg 6012 ("Read the route's rule and trusted headers first").
  `AR165-y-AC1` base: FAIL as expected (no record).
- The arm F2, its twin and their pair are the issuer's, written on this record and sent to the CTO.
- Seating: slot ~54 is reused; its earlier order is terminal.
