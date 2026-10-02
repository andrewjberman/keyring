# MDPF_TAXSMA -- status (FAST lease, /closer-drive)

Seat `4.0.0_SA_CRO` (CLAUDE). Contract `org/standards/MDPF_TAXSMA_DATA_CONTRACT.json` version 0.6.0 (amendment 3). Reviewer `3.0.0_SA_CVO`.
As of 2026-10-01T20:2xZ. **LIVE. TX-r-3 is done and Andrew validated it himself on PROD, verbatim "It works, i just smoked on PROD and looks great." Tax is ENABLED in mdpf-gold-lambda (pin 0f1a67e196, CodeSha256 wKfgTBeq..; the four TAXSMA_ settings applied 18:55Z) and the publisher's `TAXSMA_ROLLOUT_SWITCH` is ON (19:26:50Z). Served, valued 2026-09-30: Global Tax 24,813,815.93 (SMA 45,590,911.70), 49financial Tax 18,768,213.65, Cottonwood SMA 6,045,602.28. Ledgers CLOSED: `mdpf-taxsma-activation-20261001` (4/4), `mdpf-gold-taxsma-urllib-20261001` (3/3; the runtime had no httpx), `mdpf-taxsma-serve-today-20261001` (5/5; nine Sep 30 Gold documents delete-marked on Andrew's word, prior versions intact). Still OPEN: `mdpf-gold-healgap-hookup-20261001` leg V2 on the 2026-10-02 13:30Z run (record `deliverables/4.0.0_SA_CRO/V2_RECORD_TAXSMA_SERVE_TODAY_20261001.md`). Portal: the Tax-Managed SMA takes the alternatives vermilion (d79b9934), promoted to PROD as portal-v2.1.192 (f2731ad3, all of DEV on Andrew's choice, CI 36918344456 success). Push state: CLOUD LOCAL @ed0410908b over origin 0abf99fcd4 (ls-remote 20:0xZ); MSTR carries it.** The pins table below is the 15:1xZ vintage except where this paragraph supersedes it.
Parked (owner 4.0.0_SA_CRO, un-parks on Andrew's rulings): Cottonwood shows Custom $0 and ETF SMA $0 -- the auto-Custom Opal models (~$24.1M) are routed to Other AUA, and Anna Thiessen's "DIVZ SMA" sleeve is dropped by the Opal-name filter. Read in the 20:2xZ session reply; not this project's scope. Lease: FAST MDPF_TAXSMA seat 4.0.0_SA_CRO, re-armed 09:19Z on NAMED FILES instead of all of `data/mdpf` (CTO batch 75 item 6; `org/mcp/drive-mode.log`), laptop-only surfaces (the Gateway surfaces are site Z's).
Order faces: 9 of the 9 world-done orders are terminal (`superseded`, each with its artifact and a read: TX-i-1, i-2, i-3, k-1, u-1, u-2, c-1, c-3, r-1; CTO batch 74 item 4). Still open: TX-c-2, o-1, r-2, r-3, v-2, v-3. The five BLOCKING or ARMED rows are read in `deliverables/4.0.0_SA_CRO/ARMED_ROWS_READ_20261001.md`.
Authority: `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260930_142xZ_TAXSMA_CLOSER_DRIVE_GO_RIA_COLUMN_WORKBOOK_FALLBACK.md` @d55b7066ba;
priority `ANDREW_DIRECT_20260930_202xZ_TAXSMA_PRIORITY_THROUGH_MDPF_ALONGSIDE_DROPPED.md` @733b28e890 (Tax SMA through MDPF to every relevant surface);
placement `ANDREW_DIRECT_20261001_033xZ_TAXSMA_TAX_PORTFOLIOS_ARE_SMAS_NOT_MODELS_SMA_CATEGORY.md` @fc06bf47d6 (the Tax portfolios are SMAs, not models; SMA category).

## Pins

| What | Value |
|---|---|
| Working branch / worktree | `wk-mdpf_taxsma-cro` at `C:/Users/AndrewBerman/Desktop/wk-taxsma-cro`, fully merged, nothing uncommitted |
| Workspace candidate pin | The Gold function is DEPLOYED at 8ade880fad, which contains 1e5e13d223 (Cottonwood's Tax into Global), 46d04eb7b6 (Cottonwood's tree shows the Tax leaf under SMA) and dfe374adfb (the valuation-date defect fixed). The publisher is deployed at e8994f23af; its code has not changed since |
| Portal candidate pin | 370d2fe8 on origin/DEV (accessor + page caption); origin/DEV head 970d5c75 at 01:01Z; PROD untouched |
| Deployed artifact pin | mdpf-gold-lambda CodeSha256 eZ6Rtm+2.. (S3 version O09x_Btrx4EEuu_fI2uwz5Jkf8YlV8xL, zip sha256 799e91b6.., deployed 2026-10-01T15:00:26Z from pin 8ade880fad, 41 entries, Tax DISABLED: no TAXSMA_ env); publisher CodeSha256 pj+Jat96.. (S3 version Deg26fXt.., deployed 02:21Z from e8994f23af, `TAXSMA_ROLLOUT_SWITCH = OFF`) |
| Rollback | Gold artifact prior S3 version U4JsC9gYCgaKgm8kRbF1dL.2JgIPESxk (code 7hI4flW5.., pin e8994f23af); publisher prior version ZLaQC2nGuQ2hP72JpdTA4RWfciYhFoql (code 7X50uR1H..): copy that version onto the key with its `content-sha256`, restore the commit pin, plan, `safe-apply`. If the catch-up has already run, its five objects are restored first (`2.0.0_SA_COO~M`'s ledger) |
| Push state | origin/CLOUD 0abf99fcd4 (ls-remote read 15:07Z) carries this seat's work through the 02:45Z session log 171bcc4da8; everything after it is LOCAL, including the Terraform pin of an APPLIED deploy (@dae8267e31). The push is `0.0.0_AB_MSTR`'s on Andrew's word |

## Live thread

State 2026-10-01T19:28Z: LIVE end to end -- Gateway route (site Z release 3a7d6a7dc8) -> Gold prelude COMPLETE -> served platinum documents -> Model Portfolios page, validated by Andrew on PROD. The rest of this section is the 15:1xZ vintage, kept for the record.
State at 15:1xZ: NOT LIVE. Nothing serves Tax (by design of this release: Tax DISABLED, switch OFF). The Tax CODE is now deployed in both functions. Live tonight: the IAM the thread needs (two scoped prelude roles, the Gold role's
assume + control write, the publisher's control read). Hops 2-7 exercised offline on real data (E2a/E2b). The Tax-off
release is proven a zero business delta offline (16 of 16 bodies, deployed bundle vs new bundle, `qa_local`).
First failing hop: 1 (the Gateway workbook route is not on the host; its release is now site Z's, requested in `org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/4.0.0_SA_CRO/SITEZ_GATEWAY_RELEASE_REQUEST_TX-r-2.md`). The secret exists, with no value.
Trace: `org/tier1_exec/4.0.0_SA_CRO/deliverables/TAXSMA_MODEL_PORTFOLIOS_END_TO_END_GAP_BRIEF_20261001.md` (9 hops: 3 MISSING, 5 INCOMPLETE, 1 WORKS at 01:27Z; hop 2's secret has since been created).

## Acceptance IDs (decomp cells; state = this lane's read, CVO grades the pin)

| ID | State | Evidence |
|---|---|---|
| TX-p-1, v-1, g-1, g-2, b-1, b-2, m-1, m-2, m-3, m-4, a-1, a-2 | COMPLETE (round 1, drained by COO~T) | position record @cbfeeef31f |
| E1 engine (RIA firm axis, custodian per firm, workbook fallback, loaders) | CANDIDATE @62fa52fa6f + f4c4614f33 | real run on Yang's corrected sheet: 49F 11 of 11 = 17,034,745.40 (measured 12,584,745.40 + workbook-stated 4,450,000.00); Cottonwood 2 of 2 = 6,041,791.65 |
| E2a production wiring | CANDIDATE @0e1d37e80b + bd2e9a1181, re-wired per firm @338665c1b1 | 216 of 216 |
| E2b served fold | CANDIDATE @faf88511b9 + 3f03d42024 | real served spines 09-29: 49F 1,761,000,294.98 on timeseries, category tree and aum-metrics alike; Global 2,083,972,030.82 to the cent |
| E2c Cottonwood's Tax added to Global once, with an overlap control on Cottonwood's model-assigned accounts | CANDIDATE @1e5e13d223; NOT deployed | 223 of 223; real run on 09-29 data, zero writes: Global 2,066,937,285.42 base + 24,817,481.13 Tax (49F 18,768,112.35 + Cottonwood 6,049,368.78) = 2,091,754,766.55, fee-basis components sum to the cent, category tree SMA > ALT Strategies 24,817,481.13, frontier cell 13 of 13 covered; control: the assignment reader returns 0 keys, and 47 (both Tax accounts inside) with the `--` filter lifted |
| E2d Cottonwood's own tree shows the Tax leaf under SMA, as a carve-out of Client; the SMA basis is declared per firm where it differs | CANDIDATE @46d04eb7b6; NOT deployed | 226 of 226; Gold suite 94 passed, 3 failed (the S1 baseline three); real run on 09-29 data: Cottonwood SMA 0.00 -> 6,049,368.78, Client 362,884,540.60 -> 356,835,171.82, total 541,913,026.79 both ways; Rule 24 record `deliverables/4.0.0_SA_CRO/RULE24_SMA_BASIS_BY_SCOPE.md` |
| E2e DEFECT FIXED: the prelude's default valuation date was TODAY (`expected_last_trading_day`), but a custodian partition for business date D lands on D+1, so the 13:30Z run would have read SOURCE_UNAVAILABLE on every trading day. Now the prior completed session (`prev_trading_day`) | DEPLOYED in the Gold function since 2026-10-01T15:00Z (pin 8ade880fad contains dfe374adfb) | found by running the prelude on the real clock; landing times measured for 09-25, 09-28, 09-29 (Schwab 0833 at 09:46Z, Black Diamond at 11:46Z, the next day); test first, 227 of 227 |
| TX-r-3 never-widen request (the blast radius, measured) | WRITTEN, awaiting the CTO and a COO: `deliverables/4.0.0_SA_CRO/NEVER_WIDEN_REQUEST_TX-r-3.md` | Tax on moves 9 of the 16 Gold documents, not the two the order names; probe `deliverables/4.0.0_SA_CRO/probes/tx_r_3_blast_radius.py` |
| TX-i-1 scoped prelude roles | APPLIED 2026-10-01T00:03:55Z, ledger CLOSED @14670cf66c | 5 added; re-plan No changes; SIMULATION 30 of 30; exercise owed at TX-r-3. TWO roles (49f, cot), not one: each firm bucket admits only its own short token |
| TX-i-2 publisher control read | APPLIED 2026-10-01T00:16:59Z, ledger CLOSED @73ef80ab94 | 1 added; re-plan No changes; SIMULATION 10 of 10; exercise owed at TX-r-3 |
| TX-i-3 capability secret + Gateway read | APPLIED 2026-10-01T01:52:55Z from the `mdpf-pipeline` root, ledger CLOSED @c3d2237872 | 2 added; re-plan No changes; EXERCISED from the Gateway host 01:56:15Z (new secret admitted with no value; a secret not held AccessDenied). Not applied from `opal-gateway`: that root still has appliers whose commits are not on origin (rows S7, S10), and Andrew ruled it is applied from site Z only |
| TX-k-1 gold package | DEPLOYED 2026-10-01T02:17Z (built at e8994f23af, sidecar @75a4076b90) | deployed CodeSha256 equals the built zip; 39 modules |
| TX-u-1 / TX-u-2 publisher extension + package | DEPLOYED 2026-10-01T02:21Z (built at e8994f23af, sidecar @75a4076b90) | deployed CodeSha256 equals the built zip; switch OFF on the applied plane |
| TX-c-1 / TX-c-3 portal accessor + page caption | CANDIDATE portal 370d2fe8 on origin/DEV | 10 bun arms; tsc 0; no signed-in render (no served Tax yet) |
| TX-c-2 tree leaf | NOT STARTED (component under the DSGN_IRPTV1 lease; the tree already renders the tax member's served amount) | |
| TX-r-1 backend release, Tax off | CLOSED 2026-10-01T14:32Z, ledger `mdpf_taxsma-tx-r-1` 6 of 6 legs (@62301c017b); the order face is superseded | leg V2: both scheduled runs clean, 16 of 16; the probe read 12 of 16 and the four differing time-series documents were traced outside the release (`deliverables/4.0.0_SA_CRO/TX_R_1_LEG_V2_READ_20261001.md`); `1.0.0_SA_CTO` closed the leg (batch 91) |
| Gold function at 8ade880fad (E2c + E2d + E2e, Tax off, plus the HEALGAP catch-up hookup) | APPLIED 2026-10-01T15:00:26Z; ledger `mdpf-gold-healgap-hookup-20261001` OPEN, 4 of 5 legs closed (@c469f61a65); packet signed by `1.0.0_SA_CTO` with four conditions | CodeSha256 equals the built zip; re-plan No changes; the deployed dry run before (14:15Z) and after (15:02Z) both green 16 of 16, 16 documents compared, process-time only 16, other 0. Leg V2 = the 2026-10-02 13:30Z run. The catch-up itself is exercised by no leg yet |
| TX-r-2 Gateway release, capability off | **NO OWNER since 04:00Z, Andrew's call.** Site Z will not act on the request (relay 103435: Andrew to `1.0.0_SA_CTO~O` ~03:4xZ, "do not touch any MDPF_TAXSMA, that is out of your scope"); his 02:0xZ word keeps gateway releases at site Z | the route and its module are on origin/CLOUD, so any ordinary Gateway deploy carries them capability-off; the deploy script still lacks the two `.env` lines (row S11), and activation needs one more deploy after the bearer has a value |
| TX-r-3 activation | NOT STARTED, held on G-W and G-P | see Dependencies |
| TX-v-1 re-cut / TX-v-2 / TX-v-3 / TX-o-1 | NOT STARTED (this seat builds, the CVO grades each changed case) | 102 expected cases written for 0.5.0 |

## Write claims

`data/mdpf/scripts/gold/{taxsma_*.py, mdpf_gold_consolidator.py (Tax blocks), dim_mdpf_aum_metrics.py (Tax blocks)}`,
`data/mdpf/tests/taxsma/*`, `org/standards/MDPF_TAXSMA_DATA_CONTRACT.json`,
`infra/aws/terraform/mdpf-pipeline/iam.tf` (the TX-i-1 block), `infra/aws/terraform/opal-assets/mdpf_egress_publisher.tf` (the TX-i-2 block),
the two package sidecars.
The ledger entry `mdpf-gold-healgap-hookup-20261001` and its sentinel (OPEN until its leg V2, 2026-10-02 13:30Z).

## Next proof

1. **Leg V2 of `mdpf-gold-healgap-hookup-20261001`, after the 2026-10-02 13:30Z run:** every scope green; the
   Cottonwood family report carries a `catchup` block; no served change outside the five Cottonwood dates
   (2026-08-18, 08-20, 08-21, 09-23, 09-24) and Global's same five. Anything else is a SAME-DAY ROLLBACK (CTO
   condition 3): the five objects first (`2.0.0_SA_COO~M`'s ledger), then this function per the Pins row. The five
   builds themselves are read by `2.0.0_SA_COO~M`.
   Before then, if it can be had: Global's fold exercised offline on the five restored points, result reported.
1a. **The V2 probe restated before the next release's V2** (CTO batch 91 item 3): its history assertion allows the
   prior frontier date and an input restatement shown in the input; its shape assertion ignores date-keyed maps.
2. Andrew's word on who runs the Gateway deploy (see Dependencies). This seat's recommendation: it writes the two
   `.env` lines into `infra/aws/ec2/opal-gateway/deploy-to-ec2.sh` here, and site Z runs its ordinary Gateway deploy.
3. Activation (TX-r-3) once Andrew's items exist: the opalbloomberg sign-in at the Gateway and the never-widen sign-off.
4. Unblocked meanwhile, this seat: the 0.6.0 re-cut of the expected cases (TX-v-1) and the journey harness
   (TX-v-2); per-firm isolation of the source loader (see Parked).
5. DONE for the Gold function at 15:00Z (pin 8ade880fad carries E2c, E2d and E2e, so the valuation-date defect
   is no longer deployed). The publisher's code is unchanged since e8994f23af and needs no release for these.

## Dependencies

| Needs | From (owner) | Interface / pin | State |
|---|---|---|---|
| A Gateway deploy carrying the Tax route capability-off, then a second one at activation (the bearer is read into `.env` at deploy time) | **Andrew: who runs it.** Site Z was told ~03:4xZ not to touch MDPF_TAXSMA; the laptop was told 02:0xZ that gateway releases are site Z's | the request file's four acceptance results; relay `org/tier0_exec/0.0.0_AB_MSTR/deliverables/RELAY_20261001_0400Z_SITEZ_CTO_O_TX_R_2_NOT_ACTED_ON_NO_TAXSMA_AT_SITEZ_FOR_CRO.md` | BLOCKED on Andrew since 04:00Z |
| The opalbloomberg@opalinvest.com account signed in at the Gateway, so its tid/oid resolves and the first controlled read can run (G-A) | Andrew | TX-r-3 AC2, AC5, AC6 | AWAITED -- access is believed, UNMEASURED |
| G-W never-widen halves for activation | `1.0.0_SA_CTO` + a COO | the request is written: `deliverables/4.0.0_SA_CRO/NEVER_WIDEN_REQUEST_TX-r-3.md` (9 of 16 documents move, not the two the order names) | AWAITED; not yet sent to either seat |
| G-P consumer promotion (portal DEV to PROD) | Andrew | TX-r-3 AC4 | AWAITED |
| G-O grade of OG-r-1 readback @e2f11d1e3d | this lane under Andrew's word | TX-r-2 first line | AWAITED |
| `portal/src/components/CategoryViewTree.tsx` | `2.0.0_SA_COO~D` (DSGN_IRPTV1 FAST lease) | lease ends / component released | AWAITED |

## Parked

| Question (off-thread) | Owner | Un-parks when |
|---|---|---|
| FIRST-DAY RULE: an account counts only for valuation dates on or after its first Gateway observation (`taxsma_membership.resolve_date_status`), so Tax first appears on the scheduled run ONE TRADING DAY AFTER activation | Andrew | he accepts the one-day lag, or rules that the first observation also covers the prior business day **RULED 2026-10-02 ~17:0xZ, Andrew "All recs approved" (record org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261002_020xZ_EOD_UPDATE_AUTOMATION.md): the one-day lag is accepted; no change** |
| WEEKEND RUNS: Black Diamond's Friday holdings land on Monday (measured: 09-25's partition landed 09-28 11:46Z), and one missing source fails the whole prelude, so a Saturday or Sunday run carries Thursday's Tax for both firms even though 49 Financial's Friday data is there | this lane | per-firm isolation in `taxsma_sources.load_sources` (a missing Cottonwood source fails Cottonwood only), or Andrew accepts the weekend carry |
| The registry's new per-firm row types the firm id `cottonwood` by hand (naming gate WARN, 1 graded) beside the three already there (`CLIENT_L1_RULE`) | the registry's LGIC migration (R19) | the registry reads its firm ids through `lookup()` |
| aum-metrics `non_model_assets_detail` (W-6) is built before the Tax step, so its enterprise_total stays pre-Tax | this lane | the page is shown to read it; else leave |
| Outside 49F's 17.03M: workbook row 9 (Traded=No, awaiting a transfer, 2.30M on 0833) and two 0833 accounts labelled Opal Tax SMA 145 with no workbook row (1.03M + 0.96M), UNCONFIRMED candidates | Yang (workbook rows) / Andrew | two rows added with Traded=Yes; the transfer settling |
| STRATEGY_CONFLICT valued (workbook SMA 145 vs custodian SMA 200 on 2 accounts): `taxsma_assets.IDENTITY_STATUSES_VALUED` | Andrew (reverse by one tuple edit) | if he wants a label conflict to withhold value **RULED 2026-10-02 ~17:0xZ, Andrew "All recs approved" (record org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261002_020xZ_EOD_UPDATE_AUTOMATION.md): a label conflict keeps its value counted; no change** |
| CORRECTED 03:5xZ: the 937 of 984 Black Diamond accounts that form no key are NOT masked; their numbers are in other custodian formats (nine digits, eleven digits, hyphenated). Only the 47 eight-digit numbers form a key, which is the format every Tax claim has. A Cottonwood Tax claim outside those 47 falls to the workbook value | this lane | a Cottonwood Tax account appears at a custodian whose numbers are not eight digits |
| The contract's N+1 category Gold copies are not written (surprise S9) | `1.0.0_SA_CTO` at the round analysis | strike the two artifacts, or re-point the publisher to them as one migration |
| S5 EC2 Stage 6 import (`lib.opal_naming` not on the runner tree): NOT a live hazard today (Stage 6 was red before the Tax import and is not the writer of any key read today); this seat recommends AGAINST the `lib/` sync, which could make the runner a second writer of the staged spines | `1.0.0_SA_CTO` (placement) | Stage 6 is retired, or what still needs it is named |
| The probe `tx_r_1_served_delta.py` asserts two things this pipeline never satisfies (history unchanged at a baseline date; shape unchanged). It read 12 of 16 on a clean release | this lane | restated before the next release's V2 (CTO batch 91 item 3; Next proof 1a) |
| S6 Gateway deploy ships four projects | this lane | TX-r-2 cut NARROW at 1764e54a16 + TX-g-1's three commits + 030cef41b5 |
| A traded row with a blank Account Number | Andrew | stays INVALID_ACCOUNT (no fallback) unless he says the workbook value counts **RULED 2026-10-02 ~17:0xZ, Andrew "All recs approved" (record org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261002_020xZ_EOD_UPDATE_AUTOMATION.md): it stays INVALID_ACCOUNT; Yang fills the account number; no change** |
| The Gateway `.env` wiring for the Tax bearer and identity (row S11) | site Z, inside the release requested above | the release reply shows both `TAXSMA_WORKBOOK_` keys in `.env` |

## Limits

Nothing serves Tax (the deployed Tax code is DISABLED). The E2c fold is exercised on real data offline only, under
this seat's own credentials, not the function's role. The two IAM applies are verified by SIMULATION only; no session of the new
roles has been opened (they trust only the Gold function and Lambda). The Tax-off zero-delta proof is a local `qa_local` run
on Python 3.12 against the Lambda's Python 3.11 runtime and layers; the deployed `qa_local` invoke at TX-r-1 is the real-runtime
arm. The first-run read of a missing dispositions object under a prefix-conditioned ListBucket is unexercised. No product ID is
PASS until the CVO says so on a pinned candidate.
