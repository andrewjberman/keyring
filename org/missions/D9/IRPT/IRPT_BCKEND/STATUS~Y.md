# IRPT_BCKEND~Y (Analysis) -- status

Seat `2.0.0_SA_COO~Y` (CLAUDE). Mode FAST: lease `IRPT_BCKEND~Y` re-armed 2026-10-01T11:52Z until 19:52Z on Andrew's word
(record `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261001_042xZ_SELF_DRIVE_60M_LAPTOP_FABRIC_FINAL_SAY_CLOSER_DRIVE_IRPT_FIRST.md`).
Loop `/canonical-drive IRPT_BCKEND` 10m (LIVE_ARMS RELAUNCH row). Way forward: CTO rulings batches 61, 62, 65, 70, 72,
76 and 83 in `org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/RULINGS.md`. Reviewer `3.0.0_SA_CVO`
(grades pins after the fact). As of 2026-10-01T13:0xZ.

## Pins

| What | Value |
|---|---|
| Worktree | branch `coo-y-r30` at `C:/Users/AndrewBerman/Desktop/coo-y-r30`, merged into CLOUD at `9ac9b56d3c` |
| Items 1 to 13 on CLOUD | 1 to 6 (`62535e0fdc`, `b75e571a74`, `ec4dddd69b`, `0ad0e6867d`, `efde229443`, `e118089403`); 7 and 9 `ffb94090dc`; 8 `25c32c3b58`; 10 `1253002a2f`; 11 and 12 `2775cae84b` (merge `a3b35fd376`); 13 `82cdfe9802`, the settings-row reader takes the vendor's cut name (merge `9ac9b56d3c`) |
| SERVED: the resident | `/opt/irpt-resident/9ac9b56d3c-st8` since 11:58:05Z (ledger `irpt-resident-st8-20261001` CLOSED). The whole tree at 9ac9b56d3c: every item above. Host capture library `9511060e04f45b51..` (st7's, with the sign-in reason tokens) |
| SERVED: `irpt-ycharts-generate` | `arC65KbDPPssn2UX..` since 06:51:12Z (whole bundle at 21eca74f40) |
| SERVED: `irpt-status` | `2V7xV1+zII4+g6tV..` since 06:59:55Z (whole bundle at 21eca74f40) |
| NOT served | the catalogue route (no API route is published for it); items 6 to 13 in the two Lambda bundles (none of them is on a Lambda's path except the catalogue filter, which rides the next generate build) |
| Stored YCharts session | the version of 2026-10-01T08:21:20Z (fence 21), stored by one operator sign-in; read LIVE at 12:12Z; it carried three jobs |
| Push state | LOCAL; origin/CLOUD `0abf99fcd4` (ls-remote read 12:5xZ). CLOUD is pushed by `0.0.0_AB_MSTR` only |

## Live thread

**The upload lane ran end to end on served code at 12:31Z, back end only.** `REQ-a69e5751d42c374f1d2354f9` (Cottonwood,
one CSV upload, an Overview, submitted by the service principal) is READY with certified report
`RPT-ec30778a867a59f3805be6e7f07d35cb`; the sections route serves it; the case trace reads 22 links, 20 MATCH, 0
MISMATCH. **NOT yet called live:** hop 10, the page walk of this request, is asked of `2.0.0_SA_COO~D` (12:50Z), and
`3.0.0_SA_CVO` grades the outcome on the artifact (CTO half, item 10).

Six windows today, each with both halves and a closed ledger:

| window | what it showed | file under `IRPT_MVP_Y/` |
|---|---|---|
| hop 7 (07:33Z) | stored session EVICTED; the resident's own re-login `AUTH_FAILED` | `HOP7/J2_OUTCOME_20261001.md` |
| second (08:21Z) | an operator sign-in as the resident's user AUTHENTICATED; the upload's lookup then refused 4 of 4 | `HOP7B/OUTCOME_20261001.md` |
| lookup diagnostic (08:42Z) | the ticker lookup answers 200 JSON with the session and with none | `HOP3/OUTCOME_20261001.md` |
| third (08:55Z) | the job ran through the PDF download; refused at the printed-type check, PDF not kept | `HOP7C/OUTCOME_20261001.md` |
| hop 8 on st7 (10:47Z) | the same refusal, NAMED by st7's census and kept PDF: the vendor prints the name cut with an ellipsis | `HOP8/OUTCOME_20261001.md` |
| hop 8 on st8 (12:12Z) | READY; `TOLERANCE_TYPE type=Static as_of=Custom name=cut` | `HOP8B/OUTCOME_20261001.md` |

Two resident releases today, each a whole tree at one commit under a never-widen packet with both halves: st7
(`ST7/`, the diagnostics and the sessionless lookup) and st8 (`ST8/`, the reader's repair).

## Next

1. `2.0.0_SA_COO~D`'s walk of `REQ-a69e5751d42c374f1d2354f9` on the page; on a clean walk the CTO calls the thread.
2. The next resident build, when one is due, carries row S253's repair (the receipt's vendor request ledger).
3. Batch 61's order after the thread: one job per remaining arm (Multi-Comp, Target Weight, 49 Financial,
   Inflection), each an Analysis attempt under a window packet; the catalogue route, served from a read that is not
   a full-table Scan per request; the resolve concurrency fix; the vendor PDF link; the Analysis export; the email lane.

## Rows this lane holds

| Row | State |
|---|---|
| S230 | OPEN. The resident's OWN sign-in fails `AUTH_FAILED` 4 of 4 and is unnamed; the same wrapper run by an operator as the resident's user signs in. Not met again today (one operator sign-in carried three jobs). st7's reason token names the step at its next occurrence. Until then a job that meets a displaced session ends ATTENTION and an operator sign-in under a packet is the way back |
| S253 | OPEN, inert (this seat's, 12:55Z): the READY receipt of a resident job carries no `vendor_requests` ledger; IB-yr-291 writes it in `job.py`, which the resident's worker does not use |
| S231 | DONE on served code; for the CVO to close |
| W88-S2 | reader served in the generate bundle; grant applied; the route is not published |
| W94-S2, W91-S1, W92-S1 | repaired or read; for the CVO to close |
| W91-S2 | NOT repaired: `_contracts/tests/test_seam_paired.py` is held by the open order IRPT_DASHBD TO-DB-b-4 |
| W92-S4 | one read of a report whose blob is absent is still owed |

## Enrichment candidates this day measured, none built

- Each job loses 15 minutes: the first receive's second status poll, about 17 seconds after the portfolio is
  created, draws a 202 read challenge (3 of 3 jobs today) and the message waits out its 900-second visibility.
- The words a user reads for `RESOLVE_RETRY_EXHAUSTED` say other work was in flight (`2.0.0_SA_COO~D`, batch 72 item
  13; the refusal class now exists to word it from).
- A name with no request id is accepted by the cut-name rule on its three-quarter prefix alone (st8 half, item 1).
- The vendor cuts a 49-character portfolio name at 47; a shorter name would never be cut. Not changed: batch 83
  keeps the name and makes the reader an identity check.

## Write claims

`infra/aws/lambda/investor-reporting/ycharts/**`; `infra/aws/ec2/investor-reporting-ycharts/**` (the library file by the
exact-file grant of batch 74, lane IRPT_BCKEND_FAST_Y_HOST); `docs/contracts/investor-reporting/v1/routes.json`; this
file; `deliverables/2.0.0_SA_COO~Y/**`; `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/**`; the rows of
`irpt-status` and `irpt-ycharts-generate` in `infra/aws/lambda/ci/lambda-source-map.json`. NOT this seat's:
`infra/aws/terraform/investor-reporting/**`, `reports/**`, `_contracts/tests/**`.

## Parked, each with its owner and the condition that un-parks it

- The two source-map rows' `deployed_code_sha256` and `last_deployed_*` fields still describe 2026-09-24. Owner this
  seat; un-parks with the pipeline's next recorded deploy.
- Request history lists the same requests under any selected client. Owner `2.0.0_SA_COO~D` for the label; whether
  history filters by client is a product call for `1.0.0_SA_CTO`.
- Three test-path defects in files that are `2.0.0_SA_COO~P`'s (`reports/tests/test_resident_installed.py` alone: 10
  passed, 1 failed; `test_generate_installed.py` at collection; `_authz/tests`, row W98-S1).
- The node of `ycharts/session/tests/test_host_capture.py` that runs a real wrapper needs a POSIX host. Owner this
  seat; un-parks at the first resident-run capture on st7 or later, whose stderr file is the live read.
- One kept artifact in Cottonwood's partition that nothing references, under the 30-day rule: the refused PDF of
  `REQ-7c7a9e45` (`ART-58f132884b3f5dc8..`). Owner this seat; it is the fixture's source and needs nothing.
- The FAST notice to `3.0.0_SA_CVO` is carried by this file.

## Limits

No sign-in has run on the st7 capture library (`9511060e..`). The resident's own sign-in is unrepaired. Every
certified report so far is Cottonwood's, from this lane's test upload; no other firm, variant or real client file
has run. The page has not yet shown the READY request of 12:31Z. At the vendor each attempt leaves an upload record,
a model portfolio and, when it gets that far, a generated report: five attempts today, of which three reached the
vendor's upload (three upload records, three model portfolios, three generated reports).

## Standing directives (carried)

- No firm id typed in code or JSON; run `.tools/naming-gate.py --diff <diff> --enforce` explicitly in a worktree.
- A password is read BY NAME from its store into memory and never printed; an output file is read for values before
  it is committed.
- Vendor egress is on Andrew's standing words (2026-09-23 for the host's own calls, 2026-09-27 for Analysis attempts),
  each use inside a packet with both halves; no sign-in is made from the host outside one. A served move needs both
  never-widen halves. "Nobody runs AC8 again"; do not remove the `wk-nfra-oplgtw-og-v-4-p1` worktree.
- Read safe-merge's exit code and its "tree check" line on every merge, and build nothing on a merge that did not
  land (a build this afternoon was made at the wrong commit that way and discarded before any gate).
