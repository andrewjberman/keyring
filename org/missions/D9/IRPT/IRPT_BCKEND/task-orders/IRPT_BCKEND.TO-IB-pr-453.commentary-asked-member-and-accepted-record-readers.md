# TO IRPT_BCKEND.TO-IB-pr-453 -- READ ONLY, CODE ONLY: which member says commentary is asked for today, where acceptance could read it, and every reader of the accepted record

<to_id>IRPT_BCKEND.TO-IB-pr-453</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~309</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>pending</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>149</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** `1.0.0_SA_CTO~DELL2` msg 5748 | **Decomp cell:** `IB-pr-453` (decomposition section 141) | **outcome_ref:** FWD-4

---

## WORKER FACE

Root: `C:/dev/wk-irpt-bckend-309/` (bash `/c/dev/wk-irpt-bckend-309`). Work only there. A CODE AND CONTRACT READ. No AWS call, no
network call, no request to any vendor, nothing run but the repo's own offline tests where watching a branch execute helps. You
edit no product file. **You propose NO contract change**: the CTO writes the addendum from your read.

**Why.** After a vendor-path report is generated, the resident worker sends a signal named `analysis_ready` that starts a
COMMENTARY draft. Today the worker sends it when the job is bound to a ticket id. The CTO's ruling: the id alone is not enough,
because a ticket that asked for a report and NO commentary would still start a draft. The fact is to be decided ONCE, where
the request is ACCEPTED, and carried: the accepted record gains one member saying commentary was asked for; the worker sends
`analysis_ready` only when a ticket id is present AND that member is true; absent reads false. That changes the accepted
record's contract, so an addendum is written first, and not blind. This read is what it is written from.

**Where to start** (use the native Grep tool for `analysis_ready`, `commentary`, `ticket_id`, `accept`; 17 files under
`infra/aws/lambda/investor-reporting/` name the first or the third today): `ycharts/generate/acceptance.py`,
`ycharts/generate/submission.py`, `ycharts/generate/resident_worker.py`, `ycharts/research/opal_packager.py`,
`reports/resident_installed.py`, `ops/owned_report.py`, `ops/entry.py`, and their tests (`generate/tests/test_ready_signal.py`,
`test_ticket_binding.py`, `test_package_poll.py`; `ops/tests/test_ticket_contract.py`, `test_report_ticket_binding.py`;
`reports/tests/test_commentary_ready_gate.py`); the contracts under `infra/aws/lambda/investor-reporting/_contracts/` and
`docs/contracts/investor-reporting/v1/`; and the ticket project's contract and code wherever a ticket's fields are declared
(search `org/missions/D7/TCKT/` and the repo for the ticket schema the `ops` tests read; cite what you find).

**Read and state, each with `file:line`:**
1. **`what_starts_a_draft_today`:** the exact condition under which `analysis_ready` is sent (`in_words`, `code_line`), and what
   the receiver does with it.
2. **`submission`:** every member of a SUBMISSION (the request as the caller sends it, and as the intake stores it) that says,
   or could say, that commentary is asked for: `members_that_say_commentary_is_asked` (each: `member`, `written_at`, `read_at`
   as a list of `file:line`, `values` if a closed set). `told_today`: `TOLD_BY_A_MEMBER`, `TOLD_ONLY_BY_INFERENCE` (say from
   what) or `NOT_TOLD`; its claim; `in_words`; `searched_for`.
3. **`ticket`:** the same for the TICKET a request may be bound to: which field of a ticket says a commentary (or a report
   only) was asked for, where the ticket's contract declares it, and whether any code in this repo reads that field today.
4. **`accepted_record`:** what the ACCEPTED record is (`in_words`), where it is written (`written_at`), its members today
   (`members_today`), the schema or contract file that declares it (`contract_file`, with whether it forbids unknown members:
   `additional_members_forbidden` true, false or null), and where it is stored.
5. **`acceptance_could_read_it`:** at the line where acceptance writes the record, what does it hold in hand
   (`in_hand_at_acceptance`: the submission's members, the ticket id, a ticket body or not)? Could it read the fact there
   WITHOUT a ticket read (`answer` true, false or null; `from_what`; `claim`; `code_line`)? If only a ticket read would tell
   it, say so plainly: the CTO has ruled the worker and the drafter get no ticket read.
6. **`readers_of_the_accepted_record`:** EVERY reader of that record, in code and in tests and in any page or other consumer
   in this repo (search `portal/` too if the record reaches a response): each `reader`, `code_line`, `kind` (one of the kinds
   you declare in `reader_kinds`, e.g. worker, drafter, status, test, page), and `on_an_unknown_or_absent_member` (what that
   reader does when a member it does not know is present, and when the new member is absent: ignores, refuses, raises).
   `readers_by_kind` counts them with no remainder; `readers_searched_for` states the patterns and paths. Hunt by subtraction:
   list every file that names the record's type or its storage key, then place each as a reader, a writer or neither
   (`files_naming_the_record`: the count of each).
7. `not_established`: what the code cannot say.

**Outputs** in `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~309/`: `IB149-1_commentary_asked_member.json`
with the members named above plus `contract_changes_proposed:0`, `vendor_requests_made:0`, `aws_calls_made:0`,
`product_files_edited:0`; and a one-page `IB149-1_COMMENTARY_ASKED_MEMBER_READ.md` in plain sentences, each with its claim,
written for the reader who will write the addendum.

<criterion id="IB149-1-AC1" cell_refs="IB-pr-453"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r149/p149_cells.py" . IB149-1-AC1</invocation><expect>IB149-1-AC1 PASS</expect></criterion>
<criterion id="IB149-1-AC2" cell_refs="IB-pr-453"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r149/p149_cells.py" . IB149-1-AC2</invocation><expect>IB149-1-AC2 PASS</expect></criterion>
<criterion id="IB149-1-AC3" cell_refs="IB-pr-453"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r149/p149_cells.py" . IB149-1-AC3</invocation><expect>IB149-1-AC3 PASS</expect></criterion>

<expected_criteria>IB149-1-AC1, IB149-1-AC2, IB149-1-AC3</expected_criteria>

The checks grade the shape: cited lines, claims, the readers counted with no remainder, the four zeros. The answers are
UNMEASURED by the issuer; "no member says it" and "it cannot be told from code" pass where true.

## BOUNDS

- **Grant:** the `<paths>` block and nothing else. No product file is edited.
- **Refusal clause:** if a criterion cannot be met as written, stop, file a row and report. Never weaken a check; do not edit
  `p149_cells.py`.
- **Row ids** are `IRPT_BCKEND-D2-W309-S<k>`; `surfaced_at` is `date -u +%FT%TZ` at filing; `grounding.status` is `GROUNDED` or
  `INFERRED`; append only, keeping the channel file's line endings byte for byte; check the id is free before you commit.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~309" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~309@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~309 <0.9.0_WK_IRPT_BCKEND~309@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool, OUTSIDE the worktree; do NOT pre-`git add`. ASCII only. Do not push.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~309/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-453.commentary-asked-member-and-accepted-record-readers.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 141 (round 149, workstream ~P), cell `IB-pr-453`.
<owned_cells>IB-pr-453</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB149-1-AC1, IB149-1-AC2, IB149-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~309/IRPT_BCKEND.TO-IB-pr-453.commentary-asked-member-and-accepted-record-readers.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message: what starts a draft today; whether a submission says commentary is asked, and by which
member; the same for the ticket; what the accepted record is, its members, and whether its contract forbids a new one; whether
acceptance could read the fact without a ticket read, and from what; every reader of the accepted record by kind and what each
does with an absent or unknown member; what is not established; each criterion's last line; the proof checker's result; commit
hashes; any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: the tool was not run by the issuer; a code read written to the worker's own deliverables folder; nothing is edited, requested or run.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change and no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p149_cells.py dry-run at base box/dell2 on dell2 2026-10-11 ~20:2xZ: AC1 FAIL, AC2 FAIL, AC3 FAIL (no file); commit-gate clean. The issuer counted the files naming analysis_ready, the commentary members or ticket_id under infra/aws/lambda/investor-reporting (native Grep: 124 occurrences in 17 files) and named them on the face; it read none of them. The face forbids proposing the contract change (CTO msg 5748: the CTO writes the addendum).
lane: the <paths> block IS the grant. DIRECT-ACT (one read-only cell, LOCAL: records only).
</preflight>
