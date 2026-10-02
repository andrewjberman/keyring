# IRPT_BCKEND~Y (Analysis) -- status

Seat `2.0.0_SA_COO~Y` (CLAUDE), relaunched 2026-10-02 ~01:5xZ on Andrew's word (record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261002_014xZ_BRING_EVERYONE_BACK_ONLINE_PER_REBOOT_RECORDS.md`).
Mode FAST: lease `IRPT_BCKEND~Y` re-armed 02:25Z until 06:25Z (CTO 103946, under Andrew-direct 2026-10-01 ~04:2xZ).
Loop `/canonical-drive IRPT_BCKEND` 10m (LIVE_ARMS RELAUNCH row). Way forward: CTO rulings batches 61, 62, 65, 70, 72,
76, 83, 88, 89, 93, 97, 98, 100 and 105 in `org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/RULINGS.md`.
Reviewer `3.0.0_SA_CVO` (grades pins after the fact). As of 2026-10-02T03:2xZ.

## Pins

| What | Value |
|---|---|
| Worktree | branch `coo-y-r30` at `C:/Users/AndrewBerman/Desktop/coo-y-r30`, head `9ada3e8b02`, merged into CLOUD |
| Items 1 to 17 on CLOUD | 1 to 14 as before (st9 carries them); 15 `3921492913` (the 900 s calculating release, the WAF header token); 16 `7122afefc1` (row S253, the job row's `vendor_requests` ledger); 17 `8c4398e32a` (E7, the request read names the chosen comparisons). One pin for both releases: `b1db201025` |
| SERVED: the resident | `/opt/irpt-resident/b1db201025-st10` since 2026-10-02T03:19:51Z (ledger `irpt-resident-st10-20261002` CLOSED; both halves, CTO batch 106): items 1 to 17. Rollback root `481166a8f2-st9` on the host |
| SERVED: `irpt-status` | `2V7xV1+zII4+g6tV..` since 2026-10-01T06:59:55Z (read 2026-10-02 ~02:2xZ) |
| SERVED: `irpt-ycharts-generate` | `arC65KbDPPssn2UX..` since 2026-10-01T06:51:12Z |
| UPLOADED, NOT APPLIED | `irpt-status.zip` version `gqIQUc_Z..` (sha `iYgp8301..`, E7) is the key's LATEST version |
| Stored YCharts session | the version of 2026-10-01T08:21:20Z (fence 21) |
| Push state | LOCAL @5946fe3945; origin/CLOUD `0257976705` (ls-remote read 02:5xZ). CLOUD is pushed by `0.0.0_AB_MSTR` only |

## Live thread

**The Analysis thread is LIVE** (CTO batch 88) on the Overview `REQ-a69e5751d42c374f1d2354f9`. The Multi-Comp
`REQ-a1d9abc0bc037ea3d9e4a7ed` is READY, graded PASS and walked, and is NOT live until E7 is served (batch 98).

**E7 -- both halves SIGNED, apply HELD on row S261.** Packet
`IRPT_MVP_Y/E7_STATUS/NEVER_WIDEN_SIGNOFF_PACKET_IRPT_STATUS_E7_20261002.md` (blob `cc3ecd9fbb`); CTO half
`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_HALF_IRPT_STATUS_E7_20261002.md` (batch 105), conditional on step 1. The
page's `readOwnedRequest` accepted exactly two keys, so serving `comparisons` first would break every request the page
opens. `2.0.0_SA_COO~D` landed a tolerant parser on portal DEV `281b03c6` (msg 104011); the only deployed build calling
the route is PROD `b3a1d8a638`, still strict. **The apply waits on a portal PROD promote, which is Andrew's word**
(`2.0.0_SA_COO~D` is putting it to him). Census: 20 of 20 accepted requests derive (16 `[]`, 4 name one or two), 0 refuse.

**st10 -- SERVED 03:19:51Z.** Packet `IRPT_MVP_Y/ST10/NEVER_WIDEN_SIGNOFF_PACKET_RESIDENT_ST10_20261002.md` (blob
`cf517d1b39`), CTO half batch 106. V1: every digest equals the packet's; unit active and polling; queue 0/0
(`ST10/INSTALL_OUTPUT_20261002.txt`). Items 15 and 16 are offline-proven only until the next job: its journal is read for
`IRPT_RESIDENT_VENDOR_REQUESTS` and, if challenged, `WAF_READ`, and the ledger's records are compared with the requests
made (CTO half item 1).

## Next

1. The next job on st10 (natural or under its own window packet): read items 15 and 16 live (CTO batch 106 item 1).
2. On Andrew's PROD promote of `281b03c6` (named by `2.0.0_SA_COO~D`): E7's D1 (one targeted apply) and V1; then
   `2.0.0_SA_COO~D` shows the names and re-walks; the CTO calls the Multi-Comp arm live.
3. E6 (batch 93 item 8): the status list's 15.7 s and a status read's 2.3 to 13.6 s, timed by hop before any change.
4. E5 (row S230 at its next natural failure; no session is displaced on purpose).
5. Batch 61's order after that: one job per remaining arm (Target Weight, 49 Financial, Inflection), each under a window
   packet; the catalogue route from a read that is not a full-table Scan per request; the resolve concurrency fix; the
   vendor PDF link; the Analysis export; the email lane.

## Rows this lane holds

| Row | State |
|---|---|
| S261 | OPEN, BLOCKING (2026-10-02 02:41Z): the page parser rejects E7's third key. Disarm owner `2.0.0_SA_COO~D` (parser on DEV `281b03c6`; PROD promote on Andrew's word); this seat holds E7's D1 |
| S230 | OPEN. The resident's OWN sign-in fails `AUTH_FAILED` 4 of 4 and is unnamed; an operator sign-in as the resident's user works. st7's reason token names the step at its next occurrence |
| S253 | SERVED on st10 (03:19:51Z); first live read is the next job; for the CVO to close after it |
| S231 | DONE on served code; for the CVO to close |
| W88-S2 | reader served in the generate bundle; grant applied; the route is not published |
| W94-S2, W91-S1, W92-S1 | repaired or read; for the CVO to close |
| W91-S2 | NOT repaired: `_contracts/tests/test_seam_paired.py` is held by the open order IRPT_DASHBD TO-DB-b-4 |
| W92-S4 | one read of a report whose blob is absent is still owed |

## Ledgers this seat holds open

- `irpt-status-e7-20261001`: U1 closed; HELD (external gate: row S261 and the PROD promote). Nothing applied.

## Enrichment candidates (the measured list is `IRPT_MVP_Y/ENRICHMENT_CANDIDATES_20261001.md`)

- The read challenge after a job's first receive: item 15's journal token names the header's action at the next one.
- The words a user reads for `RESOLVE_RETRY_EXHAUSTED` say other work was in flight (`2.0.0_SA_COO~D`, batch 72 item 13).
- A name with no request id is accepted by the cut-name rule on its three-quarter prefix alone (st8 half, item 1).
- A producer that adds `comparisons` only when the caller asks would remove E7's wait on a PROD promote (CTO half item 1);
  it would be a new packet.

## Write claims

`infra/aws/lambda/investor-reporting/ycharts/**`; `infra/aws/ec2/investor-reporting-ycharts/**` (the library file by the
exact-file grant of batch 74, lane IRPT_BCKEND_FAST_Y_HOST); `docs/contracts/investor-reporting/v1/routes.json`;
`docs/contracts/investor-reporting/v1/OwnedAnalysisRequest.schema.json`; `infra/aws/lambda/investor-reporting/ops/owned_requests.py`;
this file; `deliverables/2.0.0_SA_COO~Y/**`; `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/**`; the rows of
`irpt-status` and `irpt-ycharts-generate` in `infra/aws/lambda/ci/lambda-source-map.json`. NOT this seat's:
`infra/aws/terraform/investor-reporting/**`, `reports/**`, `_contracts/tests/**`, `portal/**`.

## Parked, each with its owner and the condition that un-parks it

- The two source-map rows' `last_deployed_*` fields. Owner this seat; un-parks with the pipeline's next recorded deploy
  (E7's D1 for `irpt-status`).
- Request history lists the same requests under any selected client. Owner `2.0.0_SA_COO~D` for the label; whether
  history filters by client is a product call for `1.0.0_SA_CTO`.
- Three test-path defects in files that are `2.0.0_SA_COO~P`'s (`reports/tests/test_resident_installed.py`;
  `test_generate_installed.py` at collection; `_authz/tests`, row W98-S1).
- The node of `ycharts/session/tests/test_host_capture.py` that runs a real wrapper needs a POSIX host. Owner this
  seat; un-parks at the first resident-run capture on st7 or later.
- One kept artifact in Cottonwood's partition that nothing references (the refused PDF of `REQ-7c7a9e45`). Owner this
  seat; it is the fixture's source and needs nothing.
- The FAST notice to `3.0.0_SA_CVO` is carried by this file.

## Limits

No sign-in has run on the st7 capture library (`9511060e..`). The resident's own sign-in is unrepaired. Every
certified report so far is Cottonwood's, from this lane's test upload: Overviews and one Multi-Comp; no other firm,
no Comparison or Target Weight on served code, and no real client file has run.

## Standing directives (carried)

- No firm id typed in code or JSON; run `.tools/naming-gate.py --diff <diff> --enforce` explicitly in a worktree.
- A password is read BY NAME from its store into memory and never printed; an output file is read for values before
  it is committed.
- Vendor egress is on Andrew's standing words (2026-09-23 for the host's own calls, 2026-09-27 for Analysis attempts),
  each use inside a packet with both halves; no sign-in is made from the host outside one, except under batch 88
  item 3's standing terms. A served move needs both never-widen halves. "Nobody runs AC8 again"; do not remove the
  `wk-nfra-oplgtw-og-v-4-p1` worktree.
- Read safe-merge's exit code and its "tree check" line on every merge, and build nothing on a merge that did not land.
- A consumer's parser is part of a served field's blast radius: read it at every deployed build before a served
  response gains a key (row S261).
