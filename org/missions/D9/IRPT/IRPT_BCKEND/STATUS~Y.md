# IRPT_BCKEND~Y (Analysis) -- status

Seat `2.0.0_SA_COO~Y` (CLAUDE). Mode FAST: lease `IRPT_BCKEND~Y` armed 2026-10-01T04:33Z until 12:33Z on Andrew's word
(record `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261001_042xZ_SELF_DRIVE_60M_LAPTOP_FABRIC_FINAL_SAY_CLOSER_DRIVE_IRPT_FIRST.md`,
CTO 103441). Loop `/canonical-drive IRPT_BCKEND` 10m (LIVE_ARMS RELAUNCH row). Way forward: CTO rulings batches 61, 62 and
65 in `org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/RULINGS.md`, ruled on the trace
`org/tier1_exec/4.0.0_SA_CRO~X/deliverables/ANALYSIS_END_TO_END_GAP_BRIEF_20261001.md`. Reviewer `3.0.0_SA_CVO` (grades
pins after the fact). As of 2026-10-01T07:3xZ. The version before FAST is at @5c19dcc1fe.

## Pins

| What | Value |
|---|---|
| Worktree | branch `coo-y-r30` at `C:/Users/AndrewBerman/Desktop/coo-y-r30` |
| Items 1 to 6 on CLOUD | 1 `62535e0fdc` (permanent authority refusal ends the job); 2 `b75e571a74` (certification handed the comparisons); 3 `ec4dddd69b` (generate tests green, routes.json notes); 4 `0ad0e6867d` (etf-classifications reader); 5 `efde229443` (list serves named rows only); 6 `e118089403` (a model-written row is never listed), merged `89c304eaeb` |
| SERVED: the resident | `/opt/irpt-resident/36dfa80058-st6` since 06:02:56Z (ledger `irpt-resident-head-st6-20261001` CLOSED @d70857d3ce). The whole tree at 36dfa80058: items 1 and 2, IB-yr-293, IB-yr-291. Host capture library `0fec0ca910ee5fb1..` |
| SERVED: `irpt-ycharts-generate` | `arC65KbDPPssn2UX..` since 06:51:12Z, S3 version `J52XmUEj..` (ledger `irpt-analysis-whole-bundle-20261001` CLOSED @7153ec83fd). The whole bundle at 21eca74f40: items 1 to 5, the HEAD profile reader, the fail-closed `served.py` |
| SERVED: `irpt-status` | `2V7xV1+zII4+g6tV..` since 06:59:55Z, S3 version `m1LolBKF..` (same ledger). The whole bundle at 21eca74f40 |
| NOT served | item 6 (rides the next generate build); the catalogue route (no API route is published for it) |
| Push state | LOCAL; origin/CLOUD `0abf99fcd4` (ls-remote read 07:2xZ). CLOUD is pushed by `0.0.0_AB_MSTR` only |

## Live thread

NOT LIVE end to end. Hops 6 and 10 are read live on the code served today; hops 3 and 4 (upload, submission) were last
exercised on the earlier generate build and are next exercised by the hop-7 attempt, as is hop 7 itself (the YCharts
session, where the last 3 of 3 jobs died). The thread is the upload lane: one Cottonwood CSV upload, an Overview, a READY
report read on the page (batch 61 item 1).

- Hop 6 (the job's identity): the service principal's firm limit is enforced on six of six tenant-selecting functions,
  read live (rows S238 disarmed in S248, S244 closed in S246). The resident's own arm is recorded NOT EXERCISED live
  (batch 65: no test upload into another firm's partition).
- Hop 10 (the page): `2.0.0_SA_COO~D` opened `REQ-7ea49c2d` on the page after the status move: Ready, sections on
  screen, no UNEXPECTED (103576, 07:11Z and 07:15Z).
- Hop 7: packet `IRPT_MVP_Y/HOP7/WINDOW_PACKET_HOP7_SOLO_JOB_20261001.md` @c3b046d0ef, COO half signed, CTO half asked
  (07:28Z). Ledger `irpt-hop7-solo-job-20261001` OPEN.

## Next

1. **The hop-7 attempt**, on the CTO half: `live_walk/hop7_run.sh` (one upload, one Overview, no retry). Then the three
   ledger legs: the two POSTs; the terminal state by name with the journal (this names row S230's cause or produces a
   report); no residue. If READY, `2.0.0_SA_COO~D` walks that request: the thread's last link.
2. **The next resident and generate builds carry three code items, none built yet:**
   a SERVICE actor whose row has no `allowedFirmIds` is refused in `decide()` (PRD v0.22 ruling 21); a permanent
   authority refusal at the RESOLVE phase ends by name (batch 65); item 6's reader projection.
3. After the thread, in batch 61's order: one job per remaining arm (Multi-Comp, Target Weight, 49 Financial,
   Inflection); the catalogue route, served from a read that is not a full-table Scan per request (the CTO's condition 11
   on the whole-bundle packet); the resolve concurrency fix; the vendor PDF link; the Analysis export; the email lane.

## Rows this lane holds

| Row | State |
|---|---|
| S231 | DONE on served code: the st6 resident ended `REQ-86f1ce70` and `REQ-3a1b73a8` ATTENTION `ACTOR_NOT_FOUND` at 06:04Z (`ST6/R1_REDRIVE_OUTPUT_20261001.txt`); for the CVO to close |
| S229 | restart conditions: the cause named (hop-7 attempt), the retained message handled (done, the redrive), the restart under a ledger (done twice: 09-30 and st6) |
| S230 | waits on the hop-7 attempt. From the journal so far: `EVICTED` at 03:36:10Z, then `CAPTURE_FAILED:AUTH_FAILED` 18 s later |
| W88-S2 | reader landed and SERVED in the generate bundle; grant applied (the Scan statement); the route is not published |
| W94-S2, W91-S1 | repaired by item 3; for the CVO to close |
| W91-S2 | NOT repaired: `_contracts/tests/test_seam_paired.py` is held by the open order IRPT_DASHBD TO-DB-b-4. Ready check `R30_checks/check_303_seam_handlers.py` |
| W92-S1 | READ: the portal never rendered a finding's `actions` (`tabs/analysis/ProspectComposer.tsx:309-319`, `InputReview.tsx:30-41`); for the CVO to close |
| W92-S4 | `irpt-status` now serves the NOT_READY answer; one read of a report whose blob is absent is still owed (the request this row names serves its 76 sections, so it is not that case) |

## Write claims

`infra/aws/lambda/investor-reporting/ycharts/**`; `infra/aws/ec2/investor-reporting-ycharts/**`;
`docs/contracts/investor-reporting/v1/routes.json`; this file; `deliverables/2.0.0_SA_COO~Y/**`;
`org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/**`; the rows of `irpt-status` and `irpt-ycharts-generate` in
`infra/aws/lambda/ci/lambda-source-map.json` (batch 62 lane grant). NOT this seat's: `infra/aws/terraform/investor-reporting/**`
(lane IRPT_COMPLETION_P; this seat applies, never commits there), `reports/**`, `_contracts/tests/**`.

## Parked, each with its owner and the condition that un-parks it

- The two source-map rows' `deployed_code_sha256` and `last_deployed_*` fields still describe 2026-09-24:
  `record-terraform-deploy.sh` writes them pipeline-wide and was not run. Owner this seat; un-parks with the pipeline's
  next recorded deploy, or a row-scoped writer.
- Request history lists the same 13 requests under any selected client, each labelled with that client's name
  (`2.0.0_SA_COO~D` 103576). Owner `2.0.0_SA_COO~D` for the label; whether history filters by client is a product call
  for `1.0.0_SA_CTO`.
- `ProspectComposer.tsx:311` tells the user to correct the file for every NEEDS_CORRECTION upload. Owner
  `2.0.0_SA_COO~D`.
- Three test-path defects in files that are `2.0.0_SA_COO~P`'s: `reports/tests/test_resident_installed.py` cannot
  import `extract` alone; `reports/tests/test_generate_installed.py` fails at collection after the catalogue tests;
  `_authz/tests` reads 6 failed (row W98-S1).
- The FAST notice to `3.0.0_SA_CVO` is not sent: no CVO seat is live. This file is its carrier.

## Limits

No capture has run on capture library `0fec0ca9`. The resident-side refusal of a foreign-firm job is proven by the
installed digest and five offline nodes, not by a live job. Every certified report so far is Cottonwood's.

## Standing directives (carried)

- No firm id typed in code or JSON; run `.tools/naming-gate.py --diff <diff> --enforce` explicitly in a worktree.
- Before any irpt-status or generate apply: the gates on the BUILT artifact (`zip_module_census --expect`,
  `zip_cold_start_smoke --owner-refusal`, `offline_submit_proof --live-env`, `bundle_vs_live_census --zip`, and
  `IRPT_MVP_P/served_import_closure.py` and `sibling_interface_check.py`).
- A password is read BY NAME from its store into memory and never printed.
- Vendor egress is on Andrew's standing word at this seat for Analysis attempts, each inside a window packet with both
  halves; a served move needs both never-widen halves. "Nobody runs AC8 again"; do not remove the
  `wk-nfra-oplgtw-og-v-4-p1` worktree.
- Read safe-merge's exit code and its "tree check" line on every merge.
