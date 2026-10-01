# MDPF_TAXSMA -- status (FAST lease, /closer-drive)

Seat `4.0.0_SA_CRO` (CLAUDE). Contract `org/standards/MDPF_TAXSMA_DATA_CONTRACT.json` version 0.6.0 (amendment 2). Reviewer `3.0.0_SA_CVO`.
As of 2026-10-01T02:1xZ. RESUMED on Andrew's `/closer-drive MDPF_TAXSMA` at this terminal (02:04Z), after the 02:03Z checkpoint; the reboot waits for the next checkpoint. Lease: FAST MDPF_TAXSMA seat 4.0.0_SA_CRO until 2026-10-01T05:06Z (`org/mcp/drive-mode.log`), laptop-only surfaces (the Gateway surfaces are site Z's).
Authority: `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260930_142xZ_TAXSMA_CLOSER_DRIVE_GO_RIA_COLUMN_WORKBOOK_FALLBACK.md` @d55b7066ba;
priority `ANDREW_DIRECT_20260930_202xZ_TAXSMA_PRIORITY_THROUGH_MDPF_ALONGSIDE_DROPPED.md` @733b28e890 (Tax SMA through MDPF to every relevant surface).

## Pins

| What | Value |
|---|---|
| Working branch / worktree | `wk-mdpf_taxsma-cro` at `C:/Users/AndrewBerman/Desktop/wk-taxsma-cro`, fully merged, nothing uncommitted |
| Workspace candidate pin | e8994f23af (both packages are built from it); the checkpoint commit is the one carrying this file |
| Portal candidate pin | 370d2fe8 on origin/DEV (accessor + page caption); origin/DEV head 970d5c75 at 01:01Z; PROD untouched |
| Deployed artifact pin | mdpf-gold-lambda CodeSha256 5aKNH5WB.. (S3 version 8eu2ppmBW1z1.., LastModified 2026-09-22T15:19Z, 24 members, NO taxsma module); publisher MDPF_PUBLISHER_COMMIT c0902245b0 -- Tax code NOT DEPLOYED |
| Built, not uploaded | mdpf-gold-lambda zip sha256 ee12387e55b94597.. (39 modules); publisher zip sha256 a63f896adf7ab797.. |
| Push state | origin/CLOUD 68e15a70df (ls-remote read 01:39Z) carries this seat's work through 75a4076b90; everything after it is LOCAL |

## Live thread

State: NOT LIVE. Nothing serves Tax. Live tonight: the IAM the thread needs (two scoped prelude roles, the Gold role's
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
| TX-i-1 scoped prelude roles | APPLIED 2026-10-01T00:03:55Z, ledger CLOSED @14670cf66c | 5 added; re-plan No changes; SIMULATION 30 of 30; exercise owed at TX-r-3. TWO roles (49f, cot), not one: each firm bucket admits only its own short token |
| TX-i-2 publisher control read | APPLIED 2026-10-01T00:16:59Z, ledger CLOSED @73ef80ab94 | 1 added; re-plan No changes; SIMULATION 10 of 10; exercise owed at TX-r-3 |
| TX-i-3 capability secret + Gateway read | APPLIED 2026-10-01T01:52:55Z from the `mdpf-pipeline` root, ledger CLOSED @c3d2237872 | 2 added; re-plan No changes; EXERCISED from the Gateway host 01:56:15Z (new secret admitted with no value; a secret not held AccessDenied). Not applied from `opal-gateway`: that root still has appliers whose commits are not on origin (rows S7, S10), and Andrew ruled it is applied from site Z only |
| TX-k-1 gold package | CANDIDATE, built at e8994f23af, sidecar @75a4076b90 | 39 modules; import closure OK; `qa_local` green 16 of 16 from the extracted zip |
| TX-u-1 / TX-u-2 publisher extension + package | CANDIDATE, built at e8994f23af, sidecar @75a4076b90 | control read re-pointed to the global key @338665c1b1; harness arms in the 216 |
| TX-c-1 / TX-c-3 portal accessor + page caption | CANDIDATE portal 370d2fe8 on origin/DEV | 10 bun arms; tsc 0; no signed-in render (no served Tax yet) |
| TX-c-2 tree leaf | NOT STARTED (component under the DSGN_IRPTV1 lease; the tree already renders the tax member's served amount) | |
| TX-r-1 backend release, Tax off | READY TO RUN, not started | pre-proof: deployed vs new bundle, both `qa_local` green 16 of 16, every body difference a process-time path. Needs: upload both zips, two plans, two safe-applies, one deployed `qa_local` invoke, then the 13:50Z publisher fire for AC6 |
| TX-r-2 Gateway release, capability off | REQUESTED OF SITE Z (Andrew-direct 02:0xZ: gateway releases are site Z's) | request file above; includes the two `.env` lines the deploy script lacks (row S11) |
| TX-r-3 activation | NOT STARTED, held on G-W and G-P | see Dependencies |
| TX-v-1 re-cut / TX-v-2 / TX-v-3 / TX-o-1 | NOT STARTED (this seat builds, the CVO grades each changed case) | 102 expected cases written for 0.5.0 |

## Write claims

`data/mdpf/scripts/gold/{taxsma_*.py, mdpf_gold_consolidator.py (Tax blocks), dim_mdpf_aum_metrics.py (Tax blocks)}`,
`data/mdpf/tests/taxsma/*`, `org/standards/MDPF_TAXSMA_DATA_CONTRACT.json`,
`infra/aws/terraform/mdpf-pipeline/iam.tf` (the TX-i-1 block), `infra/aws/terraform/opal-assets/mdpf_egress_publisher.tf` (the TX-i-2 block),
the two package sidecars.
**In progress (claimed 2026-10-01T02:0xZ on Andrew's `/closer-drive MDPF_TAXSMA` at this terminal): TX-r-1** -- `infra/aws/terraform/mdpf-pipeline/gold-lambda.tf` (the commit pin), `infra/aws/terraform/opal-assets/mdpf_portal_publisher.tf` (the commit pin, the rollout switch OFF), both function artifacts, the ledger entry `mdpf_taxsma-tx-r-1`.

## Next proof

On resume, in order, each this seat's act under a re-armed lease:
1. TX-r-1: the Tax-off backend release. Set `MDPF_GOLD_COMMIT` and `MDPF_PUBLISHER_COMMIT` to
   e8994f23af282296037bd28bb539ac55cc9465dd and add `TAXSMA_ROLLOUT_SWITCH = "OFF"` on the publisher; upload the two
   zips (gold sha256 ee12387e55b94597.., publisher a63f896adf7ab797..) with `content-sha256` metadata; ledger; two
   plans; two `safe-apply`; one deployed `qa_local` invoke; AC6 at the 13:50Z publisher run. Rollback: the Gold
   artifact's prior S3 version 8eu2ppmBW1z1j2MOwTQc3G27uo9SbDXD.
2. Site Z's reply on the Gateway release, then activation (TX-r-3) once Andrew's three items exist.
Neither makes Tax visible alone; activation does, one trading day later by the current rule.

## Dependencies

| Needs | From (owner) | Interface / pin | State |
|---|---|---|---|
| The Gateway release carrying the Tax route, capability off | site Z NFRA_OPLGTW (`1.0.0_SA_CTO~O` / `2.0.0_SA_COO~O`), relayed by `0.0.0_AB_MSTR` | the request file; reply = release commit + host sha256 + four acceptance results | REQUESTED 02:0xZ |
| The opalbloomberg@opalinvest.com account signed in at the Gateway, so its tid/oid resolves and the first controlled read can run (G-A) | Andrew | TX-r-3 AC2, AC5, AC6 | AWAITED -- access is believed, UNMEASURED |
| G-W never-widen halves naming both served keys | `1.0.0_SA_CTO` + a COO (the CTO seat died 23:2xZ; relaunch pending) | TX-r-3 AC3 | AWAITED |
| G-P consumer promotion (portal DEV to PROD) | Andrew | TX-r-3 AC4 | AWAITED |
| G-O grade of OG-r-1 readback @e2f11d1e3d | this lane under Andrew's word | TX-r-2 first line | AWAITED |
| `portal/src/components/CategoryViewTree.tsx` | `2.0.0_SA_COO~D` (DSGN_IRPTV1 FAST lease) | lease ends / component released | AWAITED |

## Parked

| Question (off-thread) | Owner | Un-parks when |
|---|---|---|
| FIRST-DAY RULE: an account counts only for valuation dates on or after its first Gateway observation (`taxsma_membership.resolve_date_status`), so Tax first appears on the scheduled run ONE TRADING DAY AFTER activation | Andrew | he accepts the one-day lag, or rules that the first observation also covers the prior business day |
| Cottonwood's Tax ($6.04M on 09-28) is not added to Global: it would double-count if those accounts also carry a Cottonwood model assignment | this lane | a read of bd-rebalancer model assignments for the two accounts shows none, or Andrew rules |
| aum-metrics `non_model_assets_detail` (W-6) is built before the Tax step, so its enterprise_total stays pre-Tax | this lane | the page is shown to read it; else leave |
| Outside 49F's 17.03M: workbook row 9 (Traded=No, awaiting a transfer, 2.30M on 0833) and two 0833 accounts labelled Opal Tax SMA 145 with no workbook row (1.03M + 0.96M), UNCONFIRMED candidates | Yang (workbook rows) / Andrew | two rows added with Traded=Yes; the transfer settling |
| STRATEGY_CONFLICT valued (workbook SMA 145 vs custodian SMA 200 on 2 accounts): `taxsma_assets.IDENTITY_STATUSES_VALUED` | Andrew (reverse by one tuple edit) | if he wants a label conflict to withhold value |
| Black Diamond accounts whose Account Number is masked-only (937 of 984 on 09-28) can never match; a Cottonwood Tax claim on one falls to the workbook value | this lane | a BD field carrying the full number is found, or Andrew accepts the fallback |
| The contract's N+1 category Gold copies are not written (surprise S9) | `1.0.0_SA_CTO` at the round analysis | strike the two artifacts, or re-point the publisher to them as one migration |
| S5 EC2 Stage 6 import (`lib.opal_naming` not on the runner tree) | this lane | the runner sync of `lib/` is one line in `mdpf-daily-dispatch.sh` (AE~V's tree) |
| S6 Gateway deploy ships four projects | this lane | TX-r-2 cut NARROW at 1764e54a16 + TX-g-1's three commits + 030cef41b5 |
| A traded row with a blank Account Number | Andrew | stays INVALID_ACCOUNT (no fallback) unless he says the workbook value counts |
| The Gateway `.env` wiring for the Tax bearer and identity (row S11) | site Z, inside the release requested above | the release reply shows both `TAXSMA_WORKBOOK_` keys in `.env` |

## Limits

No Tax code is deployed and nothing serves Tax. The two IAM applies are verified by SIMULATION only; no session of the new
roles has been opened (they trust only the Gold function and Lambda). The Tax-off zero-delta proof is a local `qa_local` run
on Python 3.12 against the Lambda's Python 3.11 runtime and layers; the deployed `qa_local` invoke at TX-r-1 is the real-runtime
arm. The first-run read of a missing dispositions object under a prefix-conditioned ListBucket is unexercised. No product ID is
PASS until the CVO says so on a pinned candidate.
