# MDPF_TAXSMA -- status (FAST lease, /closer-drive)

Seat `4.0.0_SA_CRO` (CLAUDE). Contract `org/standards/MDPF_TAXSMA_DATA_CONTRACT.json` version 0.5.0 (0.6.0 in flight). Reviewer `3.0.0_SA_CVO`.
As of 2026-09-30T14:5xZ. Lease: FAST MDPF_TAXSMA seat 4.0.0_SA_CRO until 17:41Z (`org/mcp/drive-mode.log`).
Authority: `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260930_142xZ_TAXSMA_CLOSER_DRIVE_GO_RIA_COLUMN_WORKBOOK_FALLBACK.md` @d55b7066ba.

## Pins

| What | Value |
|---|---|
| Working branch / worktree | `wk-mdpf_taxsma-cro` at `C:/Users/AndrewBerman/Desktop/wk-taxsma-cro` |
| Workspace candidate pin | d55b7066ba (record only; no engine change yet) |
| Portal candidate pin | n/a |
| Deployed artifact pin | mdpf-gold-lambda CodeSha256 5aKNH5WB.. (bundle 2026-08-29, NO taxsma module) -- NOT DEPLOYED |
| Push state | LOCAL (ls-remote not read since 13:4xZ) |

## Live thread

State: NOT LIVE. Last trace: the deep dive @8cdcc2aba9. First failing hop: 1 (the Gold Lambda bundle carries no Tax module; the served `tax` leaf reads `aum: null`).
Hops: workbook (Gateway capability) -> Bronze/Silver -> membership -> reconcile (per RIA: Schwab 0833 | Black Diamond) -> dated assets (custodian value | workbook AUM (Mn) fallback) -> aggregate overlay -> consolidator -> publisher -> served category-views -> portal leaf.

## Acceptance IDs (decomp cells; state = this lane's read, CVO grades the pin)

| ID | State | Evidence |
|---|---|---|
| TX-p-1, v-1, g-1, g-2, b-1, b-2, m-1, m-2, m-3, m-4, a-1, a-2 | COMPLETE (round 1, drained by COO~T) | position record @cbfeeef31f |
| E1 engine: RIA firm axis + custodian-per-firm + workbook fallback + S19 fixture repair | IN PROGRESS | this lane |
| TX-k-1 gold package (+ `lib/opal_naming` member, S5) | NOT STARTED | |
| TX-u-1 / TX-u-2 publisher | NOT STARTED | |
| TX-i-3 / TX-i-1 / TX-i-2 IAM applies | BLOCKED (Terraform roots claimed by NFRA_IAMROLES202609 IAM-t-3) | see Dependencies |
| TX-c-1 / TX-c-2 / TX-c-3 portal | NOT STARTED (c-2's component under DSGN_IRPTV1 lease) | |
| TX-v-2 / TX-v-3 / TX-o-1 | NOT STARTED | |
| TX-r-1 / TX-r-2 / TX-r-3 | NOT STARTED (G-O grade, G-W, G-P ahead) | |

Offline-only work grades nothing until the live thread is live.

## Write claims

`infra/aws/ec2/opal-gateway/app/taxsma_workbook.py` (EXPECTED_HEADERS, PROJECTED_COLUMNS), `infra/aws/ec2/opal-gateway/tests/test_taxsma_workbook.py`;
`data/mdpf/scripts/silver/taxsma_workbook.py` (BUSINESS_COLUMNS); `data/mdpf/scripts/gold/taxsma_membership.py` (firm from RIA);
`data/mdpf/scripts/gold/taxsma_reconcile.py` (custodian per firm); `data/mdpf/scripts/gold/taxsma_assets.py` (basis + fallback);
`data/mdpf/scripts/gold/mdpf_gold_consolidator.py::run_taxsma_prelude`; `data/mdpf/tests/taxsma/*`; `org/standards/MDPF_TAXSMA_DATA_CONTRACT.json` (0.6.0).

## Next proof

The TAXSMA suite green (149 of 149 today's count, plus the new firm/fallback arms), then ONE real run of the prelude against the 2026-09-28 partitions (0833 fact_rps_s2/fact_acc, Black Diamond fact_holdings) and the live workbook snapshot, reproducing 12 measured 49F accounts + 2 measured Cottonwood accounts + 2 workbook-stated 49F accounts.

## Dependencies

| Needs | From (owner) | Interface / pin | State |
|---|---|---|---|
| Terraform roots `infra/aws/terraform/{mdpf-pipeline,opal-assets,opal-gateway}` free of another live claim | NFRA_IAMROLES202609 IAM-t-3 (`<paths>` infra/aws/terraform/) | lease `arm` refusal 14:2xZ | BLOCKED until IAM-t-3 closes or Andrew holds it |
| `portal/src/components/CategoryViewTree.tsx` | 2.0.0_SA_COO~D (DSGN_IRPTV1 FAST lease) | lease ends / component released | AWAITED |
| G-O grade of OG-r-1 readback @e2f11d1e3d | issuer (was COO~T; now this lane under Andrew's word) | TX-r-2 first line | AWAITED |
| G-W never-widen halves | 1.0.0_SA_CTO + a COO | TX-r-3 | AWAITED |
| G-P consumer promotion | Andrew | TX-r-3 | AWAITED |

## Parked

| Question (off-thread) | Owner | Un-parks when |
|---|---|---|
| S5 EC2 Stage 6 import (`lib.opal_naming` not on the runner tree) | this lane (disarm owner was COO~T) | TX-k-1 fixes the Lambda member; the runner sync of `lib/` is one line in `mdpf-daily-dispatch.sh` (AE~V's tree) |
| S6 Gateway deploy ships four projects | this lane | TX-r-2 cut NARROW at 1764e54a16 + TX-g-1's three commits + this lane's projection commit |
| IRPT's 09-23 edits to Silver/membership (COO~M) | this lane | absorbed: the S19 census check matches the Gateway's `used_rows` (header included); the consolidator fixture was stale |
| A traded row with a blank Account Number | Andrew | stays INVALID_ACCOUNT / unresolved (no fallback), unless Andrew says the workbook value counts for it too |

## Limits

Nothing deployed, nothing served, no apply run, no Gateway deploy. PRD v0.5 A04 "workbook estimate rejected" is amended by Andrew's word for the absent-from-custodian case only; the served value will carry `basis` per row and a measured/workbook split on the leaf so FWD-5 still holds. TX-v-1's expected cases for A02/A04 must be re-cut to the amended rule before TX-v-2 grades anything. No product ID is PASS until the CVO says so on a pinned candidate.
