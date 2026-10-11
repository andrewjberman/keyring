# TO IRPT_BCKEND.TO-IB-pr-458 -- READ ONLY, CODE ONLY: the commentary draft store's persist answer -- its members, where its shape is declared, every consumer, and what it knows of the ticket id

<to_id>IRPT_BCKEND.TO-IB-pr-458</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~314</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>pending</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>154</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** `1.0.0_SA_CTO~DELL2` msg 5993 | **Decomp cell:** `IB-pr-458` (decomposition section 146) | **outcome_ref:** FWD-4

---

## WORKER FACE

Root: `C:/dev/wk-irpt-bckend-314/` (bash `/c/dev/wk-irpt-bckend-314`). Work only there; `git rev-parse HEAD` before your first
commit is `base_commit` (state it; it is the trunk at the cut and contains the ticket gate and the `commentary_requested`
member). A CODE AND CONTRACT READ: no AWS call, no network call, no vendor request; the repo's own offline tests may be run
only to watch a branch execute. You edit no product file. **You propose NO contract change**: the CTO writes the addendum.

**Why.** The commentary DRAFTER writes its draft into the report's own store by invoking the DRAFT STORE's persist operation
under the drafter's own identity, and must then file the draft on the request's TICKET. The drafter has no ticket read and does
not hold the ticket id. The CTO ruled where it learns it: the draft store's PERSIST ANSWER carries the ticket id, read from the
accepted record the store already reads. The id is only a pointer: the ticket route's own request-id match decides whether
the draft lands. That changes the persist answer, a contract, so an addendum is written first, from this read.

**Where to start:** `infra/aws/lambda/investor-reporting/reports/commentary_draft_store.py` (the store and its handler),
`reports/commentary_composition.py`, `reports/resident_installed.py`, their tests under `reports/tests/`; the drafter under
`data/transcripts/scripts/commentary/` (`lambda_handler.py`, `ticket_client.py` and whatever invokes the store); the accepted
record's writer `ycharts/generate/acceptance.py` (`DynamoAcceptance.get` returns only the `record` attribute; the draft store
sets `commentary_ref` as a SEPARATE attribute of the same item); contracts under
`infra/aws/lambda/investor-reporting/_contracts/` and `docs/contracts/investor-reporting/v1/`. Use the native Grep tool.

**Read and state, each with `file:line` and a claim:**
1. **`persist_answer`:** `entry_point` (the handler and the operation name that persists a draft), `how_it_is_called` (a direct
   Lambda invoke, a route, a queue: and by which identity), and `outcomes`: EVERY distinct answer the operation returns (the
   first persist, a replay of the same draft, each refusal with its code), each with `outcome`, `members` (every key of the
   returned object, nested keys written `a.b`), and `built_at` (the line that builds it). `shape_declared`: is that answer's
   shape declared in any schema or contract file (`declared`, `where`, `additional_members_forbidden` true, false or null), or
   only by the code and its tests (name the tests that pin it, and whether any pins the EXACT key set).
2. **`who_invokes_persist`:** every caller (each: `caller`, `code_line`, `identity` = the role or principal it runs as, as the
   code or Terraform states it; cite the Terraform line for the invoke permission if you find it).
3. **`consumers_of_the_answer`:** by subtraction: `files_naming_the_persist_operation` (`total`, each file placed as
   `consumers`, `producers` or `neither`), then `list` (each: `consumer`, `code_line`, `kind`, `members_read` = exactly which
   members of the answer it reads, `on_an_unknown_member` = ignores, refuses or raises, with the line that decides it),
   `by_kind`, `searched_for`, `not_searched`. Search the drafter's tree and the whole repo, not only the store's folder.
4. **`accepted_record_at_persist`:** does the persist path read the accepted record (`read_at_persist`, `code_line`,
   `members_taken`: which members of the record it uses, and for what), or does it read only the request item's other
   attributes? If it reads the item and not the `record` attribute, say exactly what it reads and whether `ticket_id` is
   reachable from what it already holds without a new read (`ticket_id_reachable_without_a_new_read`: true, false or null).
5. **`ticket_id_in_the_answer_today`:** what the answer carries about the ticket today `when_the_record_carries_one` and
   `when_the_record_carries_none` (in words, with the line), and what the drafter does next in each case today
   (`drafter_next_step_today`).
6. `not_established`.

**Outputs** in `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~314/`: `IB154-1_draft_store_persist_answer.json`
with the members named above plus `base_commit`, `contract_changes_proposed: 0`, `aws_calls_made: 0`, `vendor_requests_made: 0`,
`product_files_edited: 0`; and a one-page `IB154-1_DRAFT_STORE_PERSIST_ANSWER_READ.md` in plain sentences, each with its claim.

<criterion id="IB154-1-AC1" cell_refs="IB-pr-458"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r154/p154_cells.py" . IB154-1-AC1</invocation><expect>IB154-1-AC1 PASS</expect></criterion>
<criterion id="IB154-1-AC2" cell_refs="IB-pr-458"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r154/p154_cells.py" . IB154-1-AC2</invocation><expect>IB154-1-AC2 PASS</expect></criterion>
<criterion id="IB154-1-AC3" cell_refs="IB-pr-458"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r154/p154_cells.py" . IB154-1-AC3</invocation><expect>IB154-1-AC3 PASS</expect></criterion>

<expected_criteria>IB154-1-AC1, IB154-1-AC2, IB154-1-AC3</expected_criteria>

The checks grade the shape: cited lines, claims, the subtraction's arithmetic, the four zeros. The answers are UNMEASURED by the
issuer; "no file declares it" and "it cannot be told from code" pass where true.

## BOUNDS

- **Grant:** the `<paths>` block and nothing else. No product file is edited.
- **Refusal clause:** if a criterion cannot be met as written, stop, file a row and report. Never weaken a check; do not edit
  `p154_cells.py`.
- **Row ids** are `IRPT_BCKEND-D2-W314-S<k>`; `surfaced_at` is `date -u +%FT%TZ` at filing; `grounding.status` is `GROUNDED` or
  `INFERRED`; append only, keeping the channel file's line endings byte for byte; check the id is free before you commit.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~314" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~314@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~314 <0.9.0_WK_IRPT_BCKEND~314@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool, OUTSIDE the worktree; do NOT pre-`git add`. ASCII only. Do not push.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~314/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-458.draft-store-persist-answer-read.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 146 (round 154, workstream ~P), cell `IB-pr-458`.
<owned_cells>IB-pr-458</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB154-1-AC1, IB154-1-AC2, IB154-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~314/IRPT_BCKEND.TO-IB-pr-458.draft-store-persist-answer-read.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message: the base; the persist answer's members per outcome and where its shape is declared; who
invokes persist and as what; every consumer and what each does with an unknown member; whether the store reads the accepted
record at persist and whether the ticket id is reachable without a new read; what the answer carries today with and without
a ticket id; what is not established; each criterion's last line; the proof checker's result; commit hashes; any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: the tool was not run by the issuer; a code read written to the worker's own deliverables folder; nothing is edited, requested or run.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change and no AWS call; the invoke permission is read from Terraform.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p154_cells.py dry-run at base box/dell2 on dell2 2026-10-11 ~22:4xZ: AC1 FAIL, AC2 FAIL, AC3 FAIL (no file); commit-gate clean. The issuer read none of the store's code; the starting files are from IB-pr-453's record (vintage 0bdd920114, row IRPT_BCKEND-D2-S99) and are given as starting points, with the face having the worker state its own base. The face forbids proposing the contract change (CTO msg 5993).
lane: the <paths> block IS the grant. DIRECT-ACT (one read-only cell, LOCAL: records only).
</preflight>
