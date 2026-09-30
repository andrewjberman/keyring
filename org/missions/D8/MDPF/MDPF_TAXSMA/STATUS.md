# MDPF_TAXSMA -- status (FAST lease, /closer-drive)

Seat `4.0.0_SA_CRO` (CLAUDE). Contract `org/standards/MDPF_TAXSMA_DATA_CONTRACT.json` version 0.6.0. Reviewer `3.0.0_SA_CVO`.
As of 2026-09-30T16:0xZ. Lease: FAST MDPF_TAXSMA seat 4.0.0_SA_CRO until 17:41Z (`org/mcp/drive-mode.log`).
Authority: `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260930_142xZ_TAXSMA_CLOSER_DRIVE_GO_RIA_COLUMN_WORKBOOK_FALLBACK.md` @d55b7066ba.

## Pins

| What | Value |
|---|---|
| Working branch / worktree | `wk-mdpf_taxsma-cro` at `C:/Users/AndrewBerman/Desktop/wk-taxsma-cro` |
| Workspace candidate pin | stage A 79b446e0e0 + 56491c907c + 030cef41b5 + 8609ffe5bd; stage B = the two commits after this file's |
| Portal candidate pin | n/a |
| Deployed artifact pin | mdpf-gold-lambda CodeSha256 5aKNH5WB.. (bundle 2026-08-29, NO taxsma module) -- NOT DEPLOYED |
| Push state | LOCAL (ls-remote not read since 13:4xZ) |

## Live thread

State: NOT LIVE. Hop 1 (workbook -> Gateway route) is code only, route not deployed. Hops 2-7 (Bronze -> Silver -> membership -> reconcile -> assets -> aggregate/consolidator prelude) EXERCISED OFFLINE on 2026-09-30 against the live 2026-09-28 custodian partitions and the live workbook grid: `taxsma_prelude_run.py` run_result COMPLETE, 49financial 9 of 9 covered. Hops 8-10 (publisher -> served category-views -> portal leaf) not built.
First failing hop: 1 (route undeployed) and 8 (publisher not wired).

## Acceptance IDs (decomp cells; state = this lane's read, CVO grades the pin)

| ID | State | Evidence |
|---|---|---|
| TX-p-1, v-1, g-1, g-2, b-1, b-2, m-1, m-2, m-3, m-4, a-1, a-2 | COMPLETE (round 1, drained by COO~T) | position record @cbfeeef31f |
| E1 engine: RIA firm axis + custodian-per-firm + workbook fallback + loaders | CANDIDATE @62fa52fa6f + f4c4614f33 | 189 of 189; real run 2 on Yang's corrected sheet (Traded=Yes on rows 12-15): 49F expected 11 covered 11, 17,034,745.40 (measured 12,584,745.40 + workbook-stated 4,450,000.00); Cottonwood 2 of 2, 6,041,791.65 measured on Black Diamond |
| TX-k-1 gold package (+ `lib/opal_naming` subpackage + registry + schema + contract, S5) | CANDIDATE (the commit after f4c4614f33) | 39 of 39 members hash-equal to pin; closure OK; layer deps 0 FAIL; cold-start smoke from the extracted zip; Terraform plan NOT run (root claimed) |
| TX-u-1 publisher extension (switch default OFF) | CANDIDATE @96f7932f91 + 5f58087a79 | 9 harness arms; real category document published offline with the switch ON: one put, Tax leaf covered 11 of 11 |
| TX-u-2 publisher package | CANDIDATE (the commit after 5f58087a79) | 12 of 12 members hash-equal to pin 96f7932f91; sidecar declared; layer deps 0 FAIL (tool now reads the sidecar); Terraform env default and plan NOT done (root claimed) |
| TX-i-3 / TX-i-1 / TX-i-2 IAM applies | BLOCKED (Terraform roots claimed by NFRA_IAMROLES202609 IAM-t-3) | |
| TX-c-1 / TX-c-2 / TX-c-3 portal | NOT STARTED (c-2's component under DSGN_IRPTV1 lease) | |
| TX-v-2 / TX-v-3 / TX-o-1 | NOT STARTED; v-1's expected cases for A02/A04 must be re-cut to 0.6.0 | |
| TX-r-1 / TX-r-2 / TX-r-3 | NOT STARTED (G-O grade, G-W, G-P ahead) | |

## Write claims

`data/mdpf/scripts/gold/{taxsma_*.py, mdpf_gold_consolidator.py::run_taxsma_prelude, dim_mdpf_aggregate_aua_timeseries.py::tax_coverage_entry}`,
`data/mdpf/tests/taxsma/*`, `org/standards/MDPF_TAXSMA_DATA_CONTRACT.json`, `infra/aws/ec2/opal-gateway/app/taxsma_workbook.py` (+ its test).
Next claim: `infra/aws/lambda/mdpf-pipeline/mdpf-gold-lambda/build_package.py` + manifest (TX-k-1).

## Next proof

The consumer: TX-c-1 (`portal/src/api/endpoints/aum.ts` typed accessor for the 15 coverage fields and the two document fields, TTL at most five minutes, failed transport never cached, explicit refresh crosses both caches) proved by `bun test` in the portal, then TX-c-3 (`ModelPortfolios.tsx` honest affected totals); TX-c-2 waits for DSGN_IRPTV1 to release `CategoryViewTree.tsx`.
Deferred: the plan-only Terraform passes for TX-k-1 (mdpf-pipeline root) and TX-u-2 (opal-assets root: `TAXSMA_ROLLOUT_SWITCH = "OFF"` env default) -- both roots claimed by IAM-t-3.

## Dependencies

| Needs | From (owner) | Interface / pin | State |
|---|---|---|---|
| Terraform roots `infra/aws/terraform/{mdpf-pipeline,opal-assets,opal-gateway}` free of another live claim | NFRA_IAMROLES202609 IAM-t-3 (`<paths>` infra/aws/terraform/) | lease `arm` refusal 14:2xZ | BLOCKED until IAM-t-3 closes or Andrew holds it |
| `portal/src/components/CategoryViewTree.tsx` | 2.0.0_SA_COO~D (DSGN_IRPTV1 FAST lease) | lease ends / component released | AWAITED |
| G-O grade of OG-r-1 readback @e2f11d1e3d | issuer (this lane under Andrew's word) | TX-r-2 first line | AWAITED |
| G-W never-widen halves | 1.0.0_SA_CTO + a COO | TX-r-3 | AWAITED |
| G-P consumer promotion | Andrew | TX-r-3 | AWAITED |
| 2026-09-29 custodian partitions (0833 fact_rps_s2 last = 2026-09-28 at 13:3xZ) | Schwab CRS feed | T-1 frontier | AWAITED (trading-calendar: 09-29 is T-1 today, tdb 1, HEALTHY) |

## Parked

| Question (off-thread) | Owner | Un-parks when |
|---|---|---|
| TRADED-ONLY is the rule and Yang's sheet now reflects it (rows 12-15 flipped to Yes 2026-09-30 ~16:2xZ). Still outside 49F's 17.03M: row 9 (Traded=No, awaiting a transfer, 2.30M on 0833) and two 0833 accounts labelled Opal Tax SMA 145 with no workbook row (1.03M + 0.96M), reported as UNCONFIRMED candidates | Yang (workbook rows) / Andrew | two rows added with Traded=Yes; the transfer settling |
| STRATEGY_CONFLICT valued (workbook SMA 145 vs custodian SMA 200 on 2 accounts): decision at `taxsma_assets.IDENTITY_STATUSES_VALUED` | Andrew (reverse by one tuple edit) | if he wants a label conflict to withhold value |
| Black Diamond accounts whose Account Number is masked-only (937 of 984 on 09-28) can never match; a Cottonwood Tax claim on one falls to the workbook value | this lane | a BD field carrying the full number is found, or Andrew accepts the fallback for them |
| TX-v-1 expected cases (A02 "additional candidates", A04 "workbook estimate rejected") contradict 0.6.0 | this lane | TX-v-2 item re-cuts them under the amended rule |
| S5 EC2 Stage 6 import (`lib.opal_naming` not on the runner tree) | this lane | TX-k-1 packages `lib/`; the runner sync of `lib/` is one line in `mdpf-daily-dispatch.sh` (AE~V's tree) |
| S6 Gateway deploy ships four projects | this lane | TX-r-2 cut NARROW at 1764e54a16 + TX-g-1's three commits + 030cef41b5 |
| A traded row with a blank Account Number | Andrew | stays INVALID_ACCOUNT / unresolved (no fallback) unless he says the workbook value counts |

## Limits

Nothing deployed, nothing served, no apply run, no Gateway deploy, no S3 write by the harness. The real run's first pass is seeded (clock at 2026-09-27) so the membership history covers the valuation date; an unseeded fresh store reads TRADED_HISTORY_UNVERIFIED for every account, which is what production will show on its first day and clear on its second. Cottonwood's two workbook rows are Traded=No, so no Cottonwood population was exercised live (unit arms only). No product ID is PASS until the CVO says so on a pinned candidate.
