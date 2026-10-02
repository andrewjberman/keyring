# IRPT_BCKEND~Y (Analysis) -- status

Seat `2.0.0_SA_COO~Y` (CLAUDE), relaunched 2026-10-02 ~01:5xZ on Andrew's word (record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261002_014xZ_BRING_EVERYONE_BACK_ONLINE_PER_REBOOT_RECORDS.md`).
Mode FAST: lease `IRPT_BCKEND~Y` re-armed 04:33Z until 08:33Z after the withdrawn wind-down (MSTR 104039; CTO 103946
terms, under Andrew-direct 2026-10-01 ~04:2xZ).
Loop `/canonical-drive IRPT_BCKEND` 10m (LIVE_ARMS RELAUNCH row). Way forward: CTO rulings batches 61, 62, 65, 70, 72,
76, 83, 88, 89, 93, 97, 98, 100 and 105 in `org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/RULINGS.md`.
Reviewer `3.0.0_SA_CVO` (grades pins after the fact). As of 2026-10-02T07:3xZ.

## Pins

| What | Value |
|---|---|
| Worktree | branch `coo-y-r30` at `C:/Users/AndrewBerman/Desktop/coo-y-r30`, head `3ad9306bf9`, merged into CLOUD at `87f9b3afab` |
| Items 1 to 17 on CLOUD | 1 to 14 as before (st9 carries them); 15 `3921492913` (the 900 s calculating release, the WAF header token); 16 `7122afefc1` (row S253, the job row's `vendor_requests` ledger); 17 `8c4398e32a` (E7, the request read names the chosen comparisons); 19 `951afdf4e6` (st11, merge `4f68a17d3a`, SERVED in the resident; its words ride the next generate and irpt-status bundles); 18 `3ad9306bf9` (the catalogue reads `etf-classifications` once per 300 s warm window, not per request; condition 11 of the whole-bundle packet), merge `87f9b3afab`, NOT served |
| SERVED: the resident | `/opt/irpt-resident/4f68a17d3a-st11` since 2026-10-02T07:18:54Z (ledger `irpt-resident-st11-20261002` CLOSED; both halves, CTO batch 122): items 1 to 19, and `irpt-ycharts-runner-role` holds `sqs:SendMessage` on `irpt-generation`. Rollback root `b1db201025-st10` on the host |
| SERVED: `irpt-status` | `2V7xV1+zII4+g6tV..` since 2026-10-01T06:59:55Z (read 2026-10-02 ~02:2xZ) |
| SERVED: `irpt-ycharts-generate` | `E+FqSWwETrwJ9Gd1..` since 2026-10-02T05:54:19Z (whole bundle at `97eaff05ff`, item 18; ledger `irpt-generate-catalogue-20261002` CLOSED). Rollback: S3 version `J52XmUEj..` (code `arC65KbD..`) |
| SERVED: catalogue route | `GET /api/scoped/investor-reporting/analysis/comparisons`, route `bh7ynom` on `7k3ed8px20` behind `naqxlm`, since ~06:00Z. V1: 341 entries for cottonwood, `FIRM_BINDING` outside reach, 720 ms with the Scan then 221-260 ms |
| UPLOADED, NOT APPLIED | `irpt-status.zip` version `gqIQUc_Z..` (sha `iYgp8301..`, E7) is its key's LATEST version. CTO batch 115 item 3: no untargeted apply of the ops or ycharts roots while it is held |
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
3. E6 MEASURED (@3fdf23d545, `IRPT_MVP_Y/E6_TIMING/OUTCOME_E6_20261002.md`): the page's status read is 193 AWS calls for 22
   distinct keys (5.7 s warm, 9.8 s cold in region); the list 280 for 129 (8.9-9.3 s at 18 items, about 0.5 s per
   listed request, timeout 15 s). The CTO's call on the change was asked 03:54Z (recommended: a per-request read memo
   that keeps the deliberate `_final` re-reads, as a new irpt-status packet).
4. E5 (row S230 at its next natural failure; no session is displaced on purpose).
5. **The catalogue is SERVED** (above). `2.0.0_SA_COO~D` wires the composer (interface sent 06:05Z).
   **Hop 3 -- window CLOSED, NOT fixed on st10** (`IRPT_MVP_Y/HOP3_PROOF/OUTCOME_HOP3_PROOF_20261002.md` @3743f5a084): an
   upload during another job's generation is refused `PROVIDER_READ_UNAVAILABLE:OPERATION_BUSY` and exhausts. CTO batch 120
   ruled the remedy as **st11**: a BUSY receive re-sends a fresh message delayed by the lease's retry-after (<= 900 s) and
   deletes the received one; a 60-minute wall deadline; a busy end reads a busy code with a retry action, never
   `REPLACE_FILE`. **st11's code is BUILT and MERGED** (item 19 `951afdf4e6`, IAM `85240e4c82`, merge `4f68a17d3a`): the
   re-send, the deadline from the row's `requested_at`, `RESOLVE_PROVIDER_BUSY` with action `CORRECT` and its words; 3 new tests
   (one proves a resolve busy for its whole deadline never reaches the dead-letter queue), negative control, every suite green.
   **st11 is SERVED** (07:18:54Z; ledger CLOSED @861b9bf176). Its live proof (an upload during another job's generation reads
   NORMALIZED after it) is the next window's, after Andrew's YCharts sign-in. The `RESOLVE_PROVIDER_BUSY` words ride the next
   generate and irpt-status bundles (until then the code shows with action `CORRECT`; CTO half item 1).
   **Hop 11 RULED as recommended** (CTO batch 123): `GET analysis/requests/{requestId}/pdf` on irpt-status, an Opal-signed 300 s
   URL plus sha256; `irpt-status-policy` gains `vendor_documents` in `ops/iam.tf` (this seat's lane).
   **THE irpt-status QUEUE (batch 123 item 4):** every irpt-status bundle now carries E7, so E7, then E6's memo, then hop 11 land
   in that order, one packet each, once the tolerant parser is on every deployed build incl. PROD (row S261). Build now, apply
   none before the gate, and upload no new irpt-status artifact before E7 applies (E7's step 2 stops on a replaced key).
   **E6 memo:** design `IRPT_MVP_Y/E6_TIMING/E6_MEMO_DESIGN_20261002.md` @8e128269d0; two of its lines are in
   `reports/status_installed.py` (`2.0.0_SA_COO~P`'s lane); placement asked of the CTO 07:28Z.
6. Batch 61's order after that: one job per remaining arm (Target Weight, 49 Financial, Inflection), each under a window
   packet; the resolve concurrency fix; the vendor PDF link; the Analysis export; the email lane. E6's memo follows E7's
   apply (CTO batch 111). A client-scoped history route is an enrichment item at the next round analysis (CTO batch 110 item 4).

## The YCharts session -- DEAD; only Andrew can restore it

Leg A of the hop-3 window (06:26Z) read EVICTED 71 s after a probe read LIVE; the resident's refresh met
`CHALLENGE_CAPTCHA_UNSUPPORTED` (row S230's cause, named). CTO batch 120 item 7: a sign-in that answers a CAPTCHA is a
person's act on Andrew's YCharts login; no seat attempts one. Until he signs in, no Analysis attempt can produce a report.
Batch 120 item 6 (the probe's cookie rotation) is read at the next window, which waits on that sign-in.

## Rows this lane holds

| Row | State |
|---|---|
| S263 | FIXED on CLOUD @6c4ac61088 (CTO batch 114, this seat's lane IRPT_BCKEND_FAST_Y_TFPOLICY): five roots select the policy by revision; core, export, performance plan no changes, ops and ycharts one held Lambda code move each. For the CVO to close |
| S261 | OPEN, BLOCKING (2026-10-02 02:41Z): the page parser rejects E7's third key. Disarm owner `2.0.0_SA_COO~D` (parser on DEV `281b03c6`; PROD promote on Andrew's word); this seat holds E7's D1 |
| S230 | OPEN, CAUSE NAMED 2026-10-02T06:26:18Z: the resident's own sign-in meets a CAPTCHA (`CAPTURE_FAILED:UNEXPECTED_CHALLENGE:CHALLENGE_CAPTCHA_UNSUPPORTED`). Only Andrew's own sign-in restores the session (CTO batch 120 item 7) |
| S253 | SERVED on st10 and READ LIVE: job `REQ-93441e4e..` carries 2 `vendor_requests` records, one per receive (hop-3 outcome). For the CVO to close |
| S231 | DONE on served code; for the CVO to close |
| W88-S2 | reader served in the generate bundle; grant applied; the route is not published |
| W94-S2, W91-S1, W92-S1 | repaired or read; for the CVO to close |
| W91-S2 | NOT repaired: `_contracts/tests/test_seam_paired.py` is held by the open order IRPT_DASHBD TO-DB-b-4 |
| W92-S4 | READ 05:5xZ: S213's path answers INVALID_INPUT (named; the route takes a request id), the same report by request serves 76 sections, served `owned_report.py` carries ReportBundleAbsent. Disarm proposed to the CVO 07:28Z (also S213) |

## Ledgers this seat holds open

- `irpt-status-e7-20261001`: U1 closed; HELD (external gate: row S261 and the PROD promote). Nothing applied.

## Enrichment candidates (the measured list is `IRPT_MVP_Y/ENRICHMENT_CANDIDATES_20261001.md`)

- The read challenge after a job's first receive: item 15's journal token names the header's action at the next one.
- The request history list grows about 0.5 s in region per listed request against a 15 s timeout; a cold first page
  reaches it at about 22 Cottonwood requests (inferred, E6). Each Analysis attempt adds one.
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

- The api root's `CHANGELOG.json` entry for route `bh7ynom`: outside this seat's write surface (no lane names the
  api directory; earlier entries are `2.0.0_SA_COO~P`'s). The closed ledger entry holds the record. Un-parks with an
  exact-file grant or that lane's next entry.
- `record-terraform-deploy.sh investor-reporting` is not run while E7 is held: it stamps every function of the pipeline
  as deployed at HEAD, `irpt-status` included.

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
