# TO IRPT_ANLREQ.TO-AR-y-357.resident-package-refusal-source-read -- the resident packaging refusal read: what raises ReportRefused with no code on the commentary_ready path, whether a RESERVED retention row of the draft causes it, who leaves a row RESERVED, what CurrentAuthorityRefused ACTOR_NOT_FOUND reads, and the smallest fix; READ ONLY, one record, no source change

<to_id>IRPT_ANLREQ.TO-AR-y-357</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~155</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>40</round>
<workstream>ZZ18</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL (a read of source and a record; nothing is changed, called or deployed)
**Decomp cell:** `AR-y-357` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** FWD-1 | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~155`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-155` (branch `wk-IRPT_ANLREQ-155`), provisioned by the issuer. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~155 <0.9.0_WK_IRPT_ANLREQ~155@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form `IRPT_ANLREQ-D2-W155-S<k>` (take the next free `<k>`). The workspace worktree shows ` M portal` (and may show a modified `.parquet` fixture): never commit either. Every `.py` you add passes `bash .tools/commit-gate.sh <file>`. No non-ASCII in what you add.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`; every non-PASS row carries a `status_reason`. No live call, NO PUSH, no AWS call of any kind, no edit of any source file. Scratch outside the product tree.

### THE CELL (`AR-y-357`, inlined) -- a READ. The product tree is not edited.

*Context. FWD-1 window 2 (applier record `org/tier2_senior/0.7.0_AE_CloudOps~AQ2/deliverables/irpt_anlreq_r31/A_RUN_FWD1_R2.txt`) filed a ticket and the live intake ACCEPTED the request (`commentary_requested` true). The chain then stopped at the resident's PACKAGING step (the applier's read of the resident host journal, `org/tier2_senior/0.7.0_AE_CloudOps~AQ2/deliverables/irpt_anlreq_r31/A_READ_FWD1R2_STALL.txt`, read it first): the resident (unit `irpt-analysis-resident`, root `0485393f3a-r31`) RECEIVED the `commentary_ready` message at 17:01:54Z and its packager step logged `IRPT_RESIDENT_PACKAGE retained_for_retry class=ReportRefused code=-` at 17:01:54Z and 17:17:02Z, then `class=CurrentAuthorityRefused code=ACTOR_NOT_FOUND` at 17:32:10Z (about 12 minutes after the synthetic user's row was removed); the message then went to the dead-letter queue (maxReceiveCount 3); the packager's secret was never read; the ticket carries only `attachment.input_id` and `upload_id`. The facts the applier measured: the request item holds `commentary_ref` (artifact `ART-229ea94e...`, 2968 bytes, written 17:01:54Z by the drafter), the report PDF is retained (225463 bytes), and the draft artifact's RETENTION row read state `RESERVED` at about 17:25Z while another retention row of the same principal read `ACCEPTED`. The release-31 resident source is the issuer's build input (the resident package is built from `infra/aws/lambda/investor-reporting/`; read it in your worktree, where `infra/` may be skip-worktree: read blobs with `git show HEAD:<path>`). The issuer must know, from SOURCE, what raises `ReportRefused` with no code on the packaging path, so the fix can be cut. You make no AWS call and read no live state.*

Answer these six questions from SOURCE, each with `file:line` evidence (print the lines you cite; a line you did not read is not cited):

1. **Q1, the path.** Trace the resident's handling of a `commentary_ready` message to the `IRPT_RESIDENT_PACKAGE` journal line: start at the poll in `ycharts/generate/resident_worker.py` (about the `commentary_ready` consumer and the line that prints `IRPT_RESIDENT_PACKAGE retained_for_retry`) through `ycharts/research/opal_packager.py` `handle_commentary_ready` and every read it makes (the request item, the report, the commentary draft, the retained PDF, the ticket). List each call in order with `file:line`, the exception it can raise, and which of them can raise `ReportRefused` (class in `reports/repository.py`) or `CurrentAuthorityRefused`.
2. **Q2, what raises ReportRefused with no code.** For each site that can raise `ReportRefused` on that path (a name search over `infra/aws/lambda/investor-reporting/` for `raise ReportRefused` and `ReportRefused(`), give the message text, the condition, and whether the exception carries a `code` (the journal printed `code=-`, so find where the journal line gets `code`). In particular: does reading a draft or report artifact whose retention row is `RESERVED` (not `ACCEPTED`) raise it (`reports/retention.py`, `reports/repository.py`, `reports/commentary_draft_store.py`, `reports/commentary_composition.py`)? State which retention states a reader admits.
3. **Q3, who leaves a retention row RESERVED.** Trace how the drafter's store writes the commentary draft artifact and its retention row (`reports/commentary_draft_store.py` and `reports/retention.py`): the reserve step and the accept step, where each runs and what runs after the draft is written. Can the store return with the row left `RESERVED` (an accept that is a later step, a failed accept that is swallowed, an accept that waits on a signal)? Say what would move a RESERVED row to ACCEPTED, and whether anything in the resident's packaging path does it or expects it done.
4. **Q4, the actor.** What is `CurrentAuthorityRefused code=ACTOR_NOT_FOUND`: where it is raised, what it reads (the users table row of the request's owner), and whether the FIRST two refusals (while the owner's row existed) could be the same family of check failing for another reason (the owner is a synthetic principal `fwd1-staff-r41a@opal.invalid` of class OPAL_GLOBAL; read how the resident decides an owner's authority for a package).
5. **Q5, the dead-letter message (the CTO's addendum, msg 8534).** From source only: where a `commentary_ready` message moves to its DLQ (the queue's redrive policy is declared in `infra/terraform/transcripts/commentary.tf` or the module it calls: maxReceiveCount), what consumes or ignores the DLQ, and WHAT A REDRIVE WOULD DO if someone moved that message back (the resident re-handles it: does the handler tolerate a second delivery, is it idempotent, would it hit the same refusal). Name who may redrive. You recommend a disposition (leave it, redrive after the fix, or discard after a ruling); nothing is redriven or deleted by anyone without the CTO's ruling.
6. **Q6, the owner of the RESERVED retention row (the CTO's addendum).** From source only: which principal and service write a retention row in the RESERVED state and which may move it to ACCEPTED or release it (`reports/retention.py` `_service_allows`, the writers and readers sets, `SERVICE_WRITERS`, `SERVICE_READERS`), whether a RESERVED row expires or is garbage-collected (a TTL, a sweeper), and what the commentary draft's retention policy revision is. Name the OWNER (the service principal that holds the row) and whether the owner is the drafter, the resident or the retention service.

End with ONE line (after answering all six): `CAUSE: RETENTION_RESERVED` or `CAUSE: AUTHORITY` or `CAUSE: BOTH` or `CAUSE: UNDETERMINED <what is missing>`, and the ONE source fact that decides it, then the smallest change you would cut (file and function) and whether it rides the resident release or the Lambda release. You recommend; the issuer and the CTO rule.


### Deliverable and ACCEPTANCE

Write `C:/dev/wk-irpt-anlreq-155/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~155/r41/PACKAGE_REFUSAL_READ.json` with keys: `base` (the sha your branch started from), `q1` {`steps` (a list of {order, call, file, line, can_raise}), `report_refused_sites` (a list of {file, line, message}), `evidence` (list of {file, line, text})}, `q2` {`sites` (a list of {file, line, message, condition, has_code (true|false)}), `reserved_row_raises` (`yes`|`no`|`unknown`), `admitted_retention_states` (a list of strings), `journal_code_source` {file, line, text}, `evidence`}, `q3` {`reserve_site` {file, line, text}, `accept_site` {file, line, text}, `can_leave_reserved` (`yes`|`no`|`unknown`), `what_moves_to_accepted` (string), `packaging_path_expects_accepted` (`yes`|`no`|`unknown`), `evidence`}, `q4` {`actor_not_found_site` {file, line, text}, `reads` (string), `first_two_refusals_same_family` (`yes`|`no`|`unknown`), `owner_authority_rule` (string), `evidence`}, `q5` {`dlq_move_site` {file, line, text}, `redrive_policy` (string), `redrive_would` (string), `idempotent` (`yes`|`no`|`unknown`), `who_may_redrive` (string), `recommended_disposition` (`leave`|`redrive_after_fix`|`discard_after_ruling`), `evidence`}, `q6` {`owner` (string), `owner_kind` (`drafter`|`resident`|`retention_service`|`unknown`), `who_may_accept` (string), `expires` (`yes`|`no`|`unknown`), `policy_revision` (string), `evidence`}, `cause` (`RETENTION_RESERVED`|`AUTHORITY`|`BOTH`|`UNDETERMINED`), `deciding_fact` (string), `smallest_change` {file, function, change, rides} , `evidence`, and `not_read` (what you did not read: the live system, the deployed bytes). Then write `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~155/shape_check.py` and `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~155/cite_check.py` named below. Every cited `{file, line, text}` is a path relative to the worktree root.

<criterion id="AR357-y-AC1" cell_refs="AR-y-357"><invocation>python C:/dev/wk-irpt-anlreq-155/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~155/shape_check.py</invocation><expect>^SHAPE-OK </expect></criterion>
`AR357-y-AC1`: `shape_check.py` loads `r41/PACKAGE_REFUSAL_READ.json` and prints `SHAPE-OK <keys>` only when every key above is present with an allowed value (`q2.reserved_row_raises`, `q3.can_leave_reserved`, `q4.first_two_refusals_same_family`, `cause` in their enums) and every answer block has at least one evidence item; otherwise `SHAPE-BAD <why>`, exit 1.

<criterion id="AR357-y-AC2" cell_refs="AR-y-357"><invocation>python C:/dev/wk-irpt-anlreq-155/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~155/cite_check.py</invocation><expect>^CITES-OK </expect></criterion>
`AR357-y-AC2`: `cite_check.py` re-opens every `{file, line, text}` of the record and prints `CITES-OK <n> of <n>` only when each cited line number exists and the cited `text` is a substring of that line (after stripping); a miss prints `CITES-BAD <file>:<line>` and exits 1. It prints the denominator n.

<criterion id="AR357-y-AC3J" cell_refs="AR-y-357" judgment="true"/>
`AR357-y-AC3J` (judgment, graded at L9, never by you): the answers follow from the cited lines, a "not found" is said plainly with what was searched, and the recommendation is the one the evidence supports.

<expected_criteria>AR357-y-AC1 AR357-y-AC2 AR357-y-AC3J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~155/` and this order's file (status flip only). You edit NO source file; the product tree is READ ONLY.
- If a cited file does not exist at the path named, find the file that now holds the function (a name search), cite that, and say so in the record.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-357</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~155/IRPT_ANLREQ.TO-AR-y-357.resident-package-refusal-source-read.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-357`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR357-y-AC1,AR357-y-AC2,AR357-y-AC3J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a read of source and one record; nothing is changed, deployed or called.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call, no policy change.
comp-adversary: RUN -- by reading the cell against the answer shape; the lens: an answer asserted without a read line, a 'not found' said without a search, a binding assumed set because a name exists, a recommendation that widens beyond the cell. The cell requires cited lines checked by script, a stated search for every absence, and a stated recommendation. NOT seen (blind): the live system, the deployed bytes, the resident's runtime state and the DLQ message body (only source at the worktree HEAD is read); denominator: 4 questions, 5 resident or report modules, 2 retention files, 1 packager module.
</preflight>

---

## RECORD FACE

- Cut on AQ2's chain-stall read (msg 8529; the attachment chain stays this seat's, `~P2` msg 8521). Workstream `ZZ18` of round 40. Risk LOCAL. Base: `AR357-y-AC1` and `AC2` FAIL as expected (no record, no checker files).
- Its output decides the fix cell for the resident's packaging step; nothing is changed by this cell.
