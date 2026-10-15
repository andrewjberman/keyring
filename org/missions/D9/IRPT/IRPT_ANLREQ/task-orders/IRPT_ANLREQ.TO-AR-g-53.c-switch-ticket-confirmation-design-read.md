# TO-AR-g-53 -- C-SWITCH, the ticket-confirmed switch: a READ that settles WHERE a ticket_id is confirmed against the ticket table, what each placement needs to read, and the smallest change set; READ ONLY, one record, no source change

<to_id>IRPT_ANLREQ.TO-AR-g-53</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~172</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>7</round>
<workstream>~G</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~G (ENGINE) | **Decomp cell:** `AR-g-53` (`decompositions/IRPT_ANLREQ_DECOMP_R7_G.md`) |
**outcome_ref:** FWD-1 (C-SWITCH, hop 8) | **depends_on:** none.

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~172`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-172` (branch `wk-IRPT_ANLREQ-172`), provisioned by the issuer. Work only there.
- Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~172 <0.9.0_WK_IRPT_ANLREQ~172@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool. Do not pre-`git add`. The workspace worktree may show ` M portal` and a modified `.parquet` fixture: never commit either.
- A row id has the form `IRPT_ANLREQ-D2-W172-S<k>` (take the next free `<k>`); `surfaced_at` of any row = `date -u +%FT%TZ` at filing.
- No live call, NO PUSH, no AWS call of any kind, NO edit of any source file. Scratch outside the product tree. Use the native Grep, Glob and Read tools; a recursive shell grep over the repo is denied by a hook.

### THE CELL (`AR-g-53`, inlined) -- a READ. The product tree is not edited.

*Context.* An Opal staff user's Analysis Request must reach the Opal report engine, not the broken YCharts path. Today the resident chooses
the engine in `producer_for` (`infra/aws/lambda/investor-reporting/ycharts/generate/resident_worker.py` about line 175) from the accepted
record's `owner.principal_id` against a one-entry allow list, plus (since the FWD-1 run's widening) one synthetic test address. The CTO ruled the
real switch (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_DELL2_PIVOT_FIRST_ACTS_20261013.md`, Act 2, branch 3): the Opal producer is chosen
when the accepted record carries a `ticket_id` that the ticket table CONFIRMS is an `analysis_request` ticket; no human principal is added. A
prior read (`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~135/r41/C_SWITCH_READ.json`, read it first) found: the
principal is a staff member's sign-in email; `ticket_id` is set by the CLIENT (`submission.py` line 16 `PUBLIC_FIELDS`, lines 78-79, and
`acceptance.py` lines 136-137) and only pattern-checked; and NO Investor Reporting code reads the ticket table or the ticket service before the
producer is chosen. So the confirmation does not exist yet. You settle WHERE it should live.

Two placements are on the table:
- **A, at acceptance.** The accept step in `irpt-ycharts-generate` confirms the client's `ticket_id` against the ticket table and writes a
  SERVER-OWNED field on the accepted record (a name you propose, e.g. `ticket_confirmed`); `producer_for` then reads that field.
- **B, at the resident.** The resident reads the ticket (table or service) when it chooses the producer.

Answer these four questions from SOURCE (and from the Terraform under `infra/`, read only), each with `{file, line, text}` evidence read
from the worktree (print the lines you cite; a line you did not read is not cited):

1. **Q1, placement A reach.** Can the Lambda `irpt-ycharts-generate` read the ticket table TODAY? Find the table name, its key schema, the
   attribute that marks a ticket's type as `analysis_request`, and the attribute that names the filer (read them in
   `infra/aws/lambda/ticket_center/lambda_function.py` and `infra/aws/terraform/ticket-center/main.tf`); the exact `GetItem` a confirmation
   would make; and the Lambda's execution-role statements that exist today for DynamoDB (search `infra/` for the role of
   `irpt-ycharts-generate`; name the search terms). `can_read_today`: yes / no / unknown.
2. **Q2, placement B reach.** The same question for the RESIDENT's host role (`i-0167fd745ad906a66`'s instance role, read from the tracked
   Terraform or the resident package's IAM notes). `can_read_today` yes / no / unknown, with the same table, key, type and owner markers.
3. **Q3, the stamp.** For placement A: the server-owned field's name; where a client is refused from sending it (`submission.py`
   `PUBLIC_FIELDS` and the error at lines 51-52); the record schema that must admit it (find the accepted record's schema or writer in
   `acceptance.py` and name the file and line to change); and every reader that must agree (`producer_for`, the installer's second check about
   line 274 of `reports/resident_installed.py`, the producer choice about line 748 of `resident_worker.py`, and any test pinning the list).
4. **Q4, the change sets.** For EACH of A and B: the files and lines that change; the IAM statement that would be needed, written as the
   diff against the tracked Terraform (do NOT apply anything; write `NONE` if none); which seat or project owns each file (the ticket
   service is TCKT_VNEXT's, the Terraform for IAM is a CloudOps act); the tests that pin today's behaviour; and the **forgeability** of the
   confirmation: what stops a staff user from naming a real ticket that is not theirs (state the rule the confirmation must check: type is
   `analysis_request`, and the filer matches the accepted principal, or something else you can show).

**Recommendation.** Which placement, `A`, `B` or `NEITHER`, with ONE deciding fact and its evidence. Say plainly what is still needed from
another seat (an IAM grant, a ticket-service change) and whether it can be built in source before the grant exists.

### Deliverable and ACCEPTANCE

Write `C:/dev/wk-irpt-anlreq-172/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~172/r7/C_SWITCH_DESIGN.json` with these keys:

- `base` (the sha your branch started from), `cell` (`"AR-g-53"`), `not_read` (a list of strings: what you did not read and why).
- `q1` and `q2`, each `{"can_read_today": "yes"|"no"|"unknown", "table": str, "key_shape": str, "type_marker": str, "owner_marker": str, "role_evidence": [cite, ...], "evidence": [cite, ...]}`. A string field says `not found` plainly when it is; never leave it blank.
- `q3`: `{"field": str, "client_forbidden_evidence": [cite, ...], "schema_evidence": [cite, ...], "readers": [cite, ...]}`.
- `q4`: `{"A": {"files": [cite, ...], "iam_diff": str, "owner_seats": [str, ...], "pinning_tests": [cite, ...]}, "B": {same keys}, "forgeability": str}`.
- `recommendation`: `{"shape": "A"|"B"|"NEITHER", "deciding_fact": str, "evidence": [cite, ...]}`.
- A `cite` is `{"file": "<path under the repo root, forward slashes>", "line": <int>, "text": "<a substring of that line>"}`.

<criterion id="AR53-g-AC1" cell_refs="AR-g-53"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g_read_checks.py shape53 org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~172/r7/C_SWITCH_DESIGN.json</invocation><expect>^SHAPE-OK </expect></criterion>

<criterion id="AR53-g-AC2" cell_refs="AR-g-53"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g_read_checks.py cite org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~172/r7/C_SWITCH_DESIGN.json</invocation><expect>^CITES-OK </expect></criterion>

<criterion id="AR53-g-AC3J" cell_refs="AR-g-53" judgment="true"/>
`AR53-g-AC3J` (judgment, graded at L9, never by you): the answers follow from the cited lines, a "not found" is said plainly with what was searched, and the recommendation is the one the evidence supports.

<expected_criteria>AR53-g-AC1 AR53-g-AC2 AR53-g-AC3J</expected_criteria>

- AC1 loads the record and prints `SHAPE-OK` only when every key, enum and evidence list above is present; otherwise `SHAPE-BAD <why>`. At base it FAILs (no record).
- AC2 re-opens every cite in the record (the denominator is printed) and prints `CITES-OK <n> of <n>` only when each cited line exists and the cited text is a substring of it. At base it FAILs (no record).

## BOUNDS

- **Grant:** exactly the `<paths>` below. You edit NO source file; the product tree is READ ONLY.
- If a cited file does not exist at the path named, find the file that now holds the function (a name search), cite that, and say so in the record.
- Rows: APPEND a `## <id>` heading plus one fenced json block at the END of the channel file below; gate: `python .tools/surprise-row-gate.py --check <path>`.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~172/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-53.c-switch-ticket-confirmation-design-read.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R7_G.md</decomp_doc> round 7, workstream ~G, cell `AR-g-53`.
<owned_cells>AR-g-53</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR53-g-AC1, AR53-g-AC2, AR53-g-AC3J. Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~172/IRPT_ANLREQ.TO-AR-g-53.c-switch-ticket-confirmation-design-read.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_ANLREQ.TO-AR-g-53`.
- The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL).
- In `artifacts_produced`, name each file with the hash of the commit that holds it, never a placeholder: commit the record first, then the proof and the status flip.
- In each acceptance entry, `output_evidence` BEGINS with the check's OK line.
- Validate AFTER its commit with `python .tools/proof-of-spec-check.py <instance> "AR53-g-AC1,AR53-g-AC2,AR53-g-AC3J"`; flip `<status>` to `complete` only when it prints VALID.
- Shape: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~136/IRPT_ANLREQ.TO-AR-y-328.resident-release-bindings-read.proof_of_spec.json`.
</proof_of_spec>

**REPORT (final message):** each criterion's output lines; the recommendation in one sentence; commits and row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a read of source and one record; nothing is changed, deployed or called.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call, no policy change; any IAM statement is written as a diff in the record, never applied.
comp-adversary: RUN -- by reading the cell against the answer shape. Traps: an answer asserted without a read line; a "no" said without a search; a role assumed able to read a table because the table name appears in its code; a recommendation that widens beyond the cell; a confirmation that a staff user can satisfy with a ticket that is not theirs. NOT seen (blind): the live roles and the deployed bytes; denominator: 4 questions, each answered with cited lines.
</preflight>

- Cut on CTO msg 8377 (ENGINE lane) and the CTO's Act 2 (`CTO_DELL2_PIVOT_FIRST_ACTS_20261013.md`). Risk LOCAL: the cell reads source and writes one record. Base: `AR53-g-AC1` and `AC2` FAIL as expected (no record). The checker's green arm, mutant arm and absent-record arm were run by the issuer before the cut.
- Its output decides the build cell of the switch (and the IAM leg, which is a CloudOps act under its own pair); nothing is changed by this cell.
