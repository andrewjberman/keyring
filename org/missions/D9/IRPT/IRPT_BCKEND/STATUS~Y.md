# IRPT_BCKEND~Y (Analysis) -- status

Seat `2.0.0_SA_COO~Y` (CLAUDE). Mode FAST: lease `IRPT_BCKEND~Y` armed 2026-10-01T04:33Z until 12:33Z on Andrew's word
(record `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261001_042xZ_SELF_DRIVE_60M_LAPTOP_FABRIC_FINAL_SAY_CLOSER_DRIVE_IRPT_FIRST.md`).
Loop `/canonical-drive IRPT_BCKEND` 10m (LIVE_ARMS RELAUNCH row). Way forward: CTO rulings batches 61, 62, 65, 70, 72 and
76 in `org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/RULINGS.md`. Reviewer `3.0.0_SA_CVO`
(grades pins after the fact). As of 2026-10-01T10:1xZ.

## Pins

| What | Value |
|---|---|
| Worktree | branch `coo-y-r30` at `C:/Users/AndrewBerman/Desktop/coo-y-r30`, equal to CLOUD at the merge below |
| Items 1 to 12 on CLOUD | 1 to 6 as before (`62535e0fdc`, `b75e571a74`, `ec4dddd69b`, `0ad0e6867d`, `efde229443`, `e118089403`); 7 and 9 `ffb94090dc` (service actor with no firm list refused; resolve-phase refusal ends by name; the lookup's refusal class); 8 `25c32c3b58` (sign-in reason tokens; kept stderr); 10 `1253002a2f` (sessionless ticker lookup); 11 and 12 `2775cae84b` (tolerance row census; refused PDF kept as evidence). Merge `a3b35fd376`, 16 of 16 files |
| SERVED: the resident | `/opt/irpt-resident/36dfa80058-st6` since 06:02:56Z. Host capture library `0fec0ca910ee5fb1..` |
| BUILT, not installed | `a3b35fd376-st7`: tar sha256 `c12a37d6..`, install script `ad9f91d5..`, gate PASS; packet `IRPT_MVP_Y/ST7/NEVER_WIDEN_SIGNOFF_PACKET_RESIDENT_ST7_20261001.md` @9b1ff6fb28, COO half signed, CTO half asked 10:09Z; ledger `irpt-resident-st7-20261001` OPEN (U1 closed) |
| SERVED: `irpt-ycharts-generate` | `arC65KbDPPssn2UX..` since 06:51:12Z (whole bundle at 21eca74f40) |
| SERVED: `irpt-status` | `2V7xV1+zII4+g6tV..` since 06:59:55Z (whole bundle at 21eca74f40) |
| Stored YCharts session | version of 2026-10-01T08:21:20Z (fence 21), stored by the operator sign-in of the second window; read LIVE at 08:55Z and used by a job at 09:13Z |
| Push state | LOCAL; origin/CLOUD `0abf99fcd4` (ls-remote read 10:0xZ). CLOUD is pushed by `0.0.0_AB_MSTR` only |

## Live thread

NOT LIVE end to end. The upload lane (one Cottonwood CSV, an Overview, a READY report read on the page) now runs on
served code through hop 7 and stops at **hop 8, the check of the portfolio type the vendor prints in the PDF**.

Four windows today, each with both halves and a closed ledger:

| window | what it showed | file |
|---|---|---|
| hop 7 (07:33Z) | stored session EVICTED; the resident's own re-login `AUTH_FAILED`; job ATTENTION `SESSION_REFRESH_ALREADY_USED` | `IRPT_MVP_Y/HOP7/J2_OUTCOME_20261001.md` |
| second (08:21Z) | an operator sign-in as the resident's user AUTHENTICATED and stored a fresh session; the job's upload then met `PROVIDER_READ_UNAVAILABLE` 4 of 4 | `IRPT_MVP_Y/HOP7B/OUTCOME_20261001.md` |
| lookup diagnostic (08:42Z) | the ticker lookup answers 200 JSON with the session AND with none | `IRPT_MVP_Y/HOP3/OUTCOME_20261001.md` |
| third (08:55Z) | session read LIVE; `REQ-602834fd` passed upload, portfolio, read-back, report and PDF download; ATTENTION `TOLERANCE_REQUIRES_STATIC` (`type=- as_of=-`) | `IRPT_MVP_Y/HOP7C/OUTCOME_20261001.md` |

Three failures today were unreadable because the fact that names them was discarded by design (the sign-in step, the
lookup's status, the refused PDF's row). The st7 build makes each of them print its cause.

## Next

1. **Install st7** on the CTO half (`ST7/install_fetch_and_run.sh` through Systems Manager; V1 read-back closes the
   ledger). No vendor call.
2. **ONE job attempt** under a new window packet (batch 76 item 5): a liveness read first, then one upload and one
   Overview. A refusal at hop 8 now prints the row census and keeps the PDF, so the reader's repair has its fixture.
3. After hop 8: `2.0.0_SA_COO~D` walks the READY request (hop 10 on a service-principal request); then batch 61's
   order: one job per remaining arm, the catalogue route (not a full-table Scan per request), the resolve concurrency
   fix, the vendor PDF link, the Analysis export, the email lane.

## Rows this lane holds

| Row | State |
|---|---|
| S230 | OPEN. The resident's own sign-in fails `AUTH_FAILED` 4 of 4; the same wrapper run by an operator as the resident's user signs in. The reason token (st7) names the step at the next occurrence. By the CTO's trace the session is displaced by another sign-in on the shared seat, not aged out |
| S231 | DONE on served code (both dead-lettered jobs ended ATTENTION `ACTOR_NOT_FOUND` at 06:04Z); for the CVO to close |
| S238, S244 | S238 disarmed in the CTO's row S248; S244's resident half closed in row S246 |
| W88-S2 | reader served in the generate bundle; grant applied; the route is not published |
| W94-S2, W91-S1, W92-S1 | repaired or read; for the CVO to close |
| W91-S2 | NOT repaired: `_contracts/tests/test_seam_paired.py` is held by the open order IRPT_DASHBD TO-DB-b-4 |
| W92-S4 | one read of a report whose blob is absent is still owed |

## Write claims

`infra/aws/lambda/investor-reporting/ycharts/**`; `infra/aws/ec2/investor-reporting-ycharts/**` (the library file by the
exact-file grant of batch 74, lane IRPT_BCKEND_FAST_Y_HOST); `docs/contracts/investor-reporting/v1/routes.json`; this
file; `deliverables/2.0.0_SA_COO~Y/**`; `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/**`; the rows of
`irpt-status` and `irpt-ycharts-generate` in `infra/aws/lambda/ci/lambda-source-map.json`. NOT this seat's:
`infra/aws/terraform/investor-reporting/**`, `reports/**`, `_contracts/tests/**`.

## Parked, each with its owner and the condition that un-parks it

- The words a user reads for `RESOLVE_RETRY_EXHAUSTED` say other work was in flight. Owner `2.0.0_SA_COO~D` (batch
  72 item 13); un-parks when st7 is served and the refusal class exists to word it from.
- The two source-map rows' `deployed_code_sha256` and `last_deployed_*` fields still describe 2026-09-24. Owner this
  seat; un-parks with the pipeline's next recorded deploy.
- Request history lists the same requests under any selected client. Owner `2.0.0_SA_COO~D` for the label; whether
  history filters by client is a product call for `1.0.0_SA_CTO`.
- Three test-path defects in files that are `2.0.0_SA_COO~P`'s (`reports/tests/test_resident_installed.py` alone: 10
  passed, 1 failed; `test_generate_installed.py` at collection; `_authz/tests`, row W98-S1).
- The node of `ycharts/session/tests/test_host_capture.py` that runs a real wrapper needs a POSIX host. Owner this
  seat; un-parks at the first st7 capture, whose stderr file is the live read.
- The FAST notice to `3.0.0_SA_CVO` is carried by this file.

## Limits

No sign-in has run on the st7 capture library. The sessionless lookup has not run through the resident's own child
process. Every certified report so far is Cottonwood's; the resident-side refusal of a foreign-firm job is proven by
the installed digest and offline nodes, not by a live job. At the vendor each attempt leaves an upload record, a
model portfolio and, when it gets that far, a generated report.

## Standing directives (carried)

- No firm id typed in code or JSON; run `.tools/naming-gate.py --diff <diff> --enforce` explicitly in a worktree.
- A password is read BY NAME from its store into memory and never printed; an output file is read for values before
  it is committed.
- Vendor egress is on Andrew's standing words (2026-09-23 for the host's own calls, 2026-09-27 for Analysis attempts),
  each use inside a packet with both halves; no sign-in is made from the host outside one. A served move needs both
  never-widen halves. "Nobody runs AC8 again"; do not remove the `wk-nfra-oplgtw-og-v-4-p1` worktree.
- Read safe-merge's exit code and its "tree check" line on every merge.
