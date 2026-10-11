# CTO ROUND-2 ANALYSIS -- TCKT_VNEXT -- answering the round-1 L10 slug (2026-10-11 ~03:4xZ)

**Author:** 1.0.0_SA_CTO~DELL2. **Answers:** `org/missions/D7/TCKT/TCKT_VNEXT/ledger/L10_SLUG_R1.md` @23e3126092 (2.0.0_SA_COO~V2 msg 3963).
**Reviewer's grade read:** `org/tier1_exec/3.0.0_SA_CVO/deliverables/TCKT_VNEXT_SA_R1B_L9_GRADE_20261010.md` @771737f0a6.
**PRD:** `org/missions/D7/TCKT/TCKT_VNEXT/prd/TCKT_VNEXT_PRD.md`. **No PRD addendum:** FWD-1's ACCEPT text does not change, so no
half re-opens.

## 1. Where the project stands

**FWD-1 is NOT REALIZED. The thread is not built yet, so round 2 is still a thread round.** The seat-arm run filed a
ticket and submitted an analysis, then never read a request: its runner polled the idempotency token it had sent
(`sar1b-<24 hex>`), and the read plane accepts `REQ-<24 hex>` only. 61 of 61 reads were refused. No render ran. The ticket
stored the token as its `report_ref`, so the report cannot open from the ticket. The reviewer's grade stands as written,
including its correction of the packet's stated cause.

FWD-2 to FWD-9: none graded. FWD-9 and C-PACKAGE moved with IRPT_ANLREQ (ADDENDUM 2).

## 2. Rulings on the slug's open items

| slug item | ruling |
|---|---|
| 5. Fee default (row D2-W1-S1) | **No number is invented.** The `advisory_fee` field stays with no default (da43155418) and is required of the filer. The contract's "default stated" is satisfied only by a value Andrew or Alyssa gives; that is an input, listed in section 5, and nothing in round 2 waits on it. |
| 9. data-refresh admission (rows D2-W6-S2 ARMED, S12, S16, S17) | **W6-S2 DISARMS.** Its hazard was a one-firm filer token with no `userType` reaching data-refresh. Row S16 measured the routed fix live: the gate admits `Dev` or an Opal-internal principal, so a one-firm token is refused. What remains is S17: an Opal-internal principal is admitted whatever its `userType`. That is the gate's intent for staff, and the only residue is a TEST token minted as internal. It is bounded by this rule, which round 2's pair carries: **no internal-tier test token is minted outside a signed pair that names data-refresh in its blast radius, with a zero-call read after.** S17 stays with the data-refresh owner (my msg 3619) and leaves this project's list. 2.0.0_SA_COO~V2 files the disposition row citing this section. |
| 6. Firm pick-list (S3), second reader of a filed report (S4) | Not this project's. Carried to IRPT_ANLREQ's backlog as candidates; 2.0.0_SA_COO~V2 sends the two row ids to 2.0.0_SA_COO~Y2. No cell here. |
| 10. svc-commentary read grant reaches dell1 as well as dell2 (S9); rotation runbook (S8) | Round 3. The remediation row is the reviewer's. |
| `round-close-check --round 1` read MAY-CLOSE while a JUDGMENT criterion was NOT MET | A tool gap: the check did not see the SA-r-1b grade. 2.0.0_SA_COO~V2 files one row (`spec_asserts`: the check counts every graded judgment criterion of the round; `world_is`: it printed judgment=1 graded=1 with a second grade on file). The round did not close on it; the slug is correct. |

## 3. One dependency round 2 must respect (not a wait)

**The re-run of the journey needs irpt-status at the IB-pr-416 build.** Live irpt-status is revision 3
(`t6OJTCcm...`), which lacks release 1's reader members. The one-tree build `6idtFvAm...` is signed (CTO half
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/1.0.0_SA_CTO~DELL2/NEVER_WIDEN_IB_pr_416_THREE_FUNCTIONS_ONE_TREE_CTO_HALF.md`
@81cba68056, section A3) and is applied by 2.0.0_SA_COO~Y2's TO-APPLY-Y1 AMENDMENT 8. Round 2's build cells do not wait
on it. Only the WORLD run does, and its precheck reads the live CodeSha256: `6idtFvAm...` proceeds, anything else is a
STOP that names the apply still owed.

## 4. ENRICHMENT LIST for round 2 (cut in ONE issuance, in this order)

1. **Thread repair, the runner (LOCAL build).** The runner takes the request id from the submission's answer, or from the
   firm's request list when the answer carries none. It never polls a value it sent. It polls that `REQ-<24 hex>` id,
   reads `stage` from the contract field until GENERATED or RELEASED, records the id on the ticket, and opens the report
   from the ticket. The request record is read through the API with the run's token. No `kms:Decrypt` grant is added for
   any seat principal.
2. **`report_ref` shape (SERVED; its own never-widen pair).** `POST /api/scoped/tickets/{ticketId}/report` refuses a
   `request_id` that does not match `REQ-[0-9a-f]{24}`. Both arms tested: a well-formed id stored, a malformed one
   refused with a typed code. Lands before item 3's run, so a wrong id cannot be stored again.
3. **Thread re-run (WORLD; a re-signed pair).** One seat-arm journey end to end on DEV with item 1's runner, after items
   1 and 2 and after the section 3 precheck. Graded on FWD-1's ACCEPT by the reviewer: the report is made from the filed
   file, and it opens from the same ticket. The pair names data-refresh in its radius with a zero-call read that has a
   positive control (the round-1 zero had `searched_log_streams: 0`). Before the run, every live worktree's
   `.open_deploys/` is read and unioned with the per-tree denominator printed; the slug read the shared tree only.
   Test ticket `TCK-20261009-67ab7f27` is closed or marked in the same run (slug item 11).
4. **Andrew's "crawl that instead" (open call `-fbb1`).** A seat claims then completes `TCK-20261009-a1052909` on the DEV
   board through the browser crawler; the board is read after. The call closes on that read.
5. **Stub SES and the users-table reads in the ticket_center tests (rows D2-W1-S4, D2-W7-S1; LOCAL).** A test never
   reaches a real send. This is the standing fix behind the procedural disarm.

Each build order carries at most three mechanical criteria. Items 1, 4 and 5 are independent; 2 precedes 3; 1 precedes 3.

**Not in round 2, carried to the round-3 list unless round 2 changes them:** FWD-3's one-account check (S5); FWD-6
"same ticket" (remediation row S6, which also needs NFRA_TRNSPT's FWD-10 drafter); FWD-2's other-firm refusal; FWD-5's
queue type and age; slug item 10.

## 5. Acts and inputs only Andrew or Alyssa can give (none gates round 2)

- **The default advisory fee** the Analysis Request form should state, or his word that there is none. Citation: PRD
  C-ANALYSIS-REQUEST "advisory fee (default stated)"; no source in the repo carries the value.
- **Alyssa's one Analysis request on portal DEV** (open call `-3cb1`), the organic arm of FWD-1. His word of 2026-10-10:
  "later".

## 6. What this analysis did not measure

It rests on the slug's table and the reviewer's grade as filed. This seat re-read neither the live logs nor the trace
file. The dependency in section 3 rests on the IB-pr-416 packet's statement that revision 3 lacks the reader members.

-- 1.0.0_SA_CTO~DELL2
