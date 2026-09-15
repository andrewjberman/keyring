# Tax SMA workbook-to-custodian pipeline audit

Author: `1.0.0_SA_CTO~A`. Measured 2026-09-15, principally 04:35–04:52 UTC.
Purpose: ground the commissioned D8 brief before endpoint projection or registration.
Disposition: measured gaps; not an implementation certification.

## Finding

The current workbook is not a list of exclusively live accounts. It includes eight marked traded, two numbered accounts explicitly not traded and three prospects without account numbers. The eight marked traded are the expected cohort to reconcile, not eight independently verified live feed records. Six have exact 0833 records and long/short holdings at the observed date. Two remain unmatched.

The current manual ETL roster and July BD report do not cover that expected cohort. Existing daily Schwab canonical valuation is a usable source for the six matched accounts, but it cannot repair missing identity or business-status evidence. The new project needs complete expected membership and explicit reconciliation before a total can be trusted.

## Method and privacy

SharePoint was read through the live **Opal Gateway MCP** endpoint `https://mcp.opalinvest.dev/mcp/`: MCP initialization/tool discovery, `find_sharepoint_site`, scoped listings/searches, `read_site_workbook`, `read_document`, and `read_site_file`. Existing authorized OAuth access was refreshed without displaying credentials. No direct Graph substitute was used. `read_document` returned converted PDF bytes for local text inspection.

The Shared site is `https://opalinvest.sharepoint.com/sites/Shared`, ID `opalinvest.sharepoint.com,9332c03f-2ad0-4b84-97fe-7bcd2c9cb90a,18b7f31c-c878-41ea-9b7e-0c103bcb5679`.

AWS checks used read-only object listing and reads, plus Lambda configuration and direct classic EventBridge target lookup. No Lambda invocation, Black Diamond request, enrollment, workbook edit, S3 write or trading operation was performed.

All account joins used complete normalized account numbers, never the endings displayed below. Full account numbers, names, raw workbook responses, parquet downloads and authentication material remain in private seat scratch. Committed evidence contains redacted account labels, counts, source metadata and hashes. Endings are display labels only and are not a proposed primary key.

## Workbook population

Live source: `TAX/Tax SMA Accounts.xlsx`, item `01L6LHKFXVVTRR73M6KZGIHM4FY2ATNK4U`, modified **2026-09-14T18:33:00Z**, 19,062 bytes, eTag `{1FE3ACF5-9EED-4C56-83B3-85C68136AB94},208`. Gateway read at 04:36:55Z: Sheet1 **A1:N22**, all 22 rows and 14 columns, `truncated:false`.

| Workbook population | Count | Treatment |
|---|---:|---|
| Ready Yes / Traded Yes, complete account number | 8 | Expected traded cohort; reconcile to source evidence |
| Ready No / Traded No, complete account number | 2 | Excluded from live Tax SMA valuation |
| Prospects without account number | 3 | Await opening; excluded |
| Blank indexed slots | 7 | Not accounts |
| Displayed total | 33.33 million | Includes sales prospects; not daily live assets |

The important columns are Account Number, Strategy, Leverage, Ready, Inception Date, Last Trade Date and Traded. A state model must distinguish business activation from technical ingestion and from funding. Existing positions are corroboration, not a substitute for the business activation designation: an account may be funded before its first Tax SMA trade, and an active strategy need not trade daily.

## Reconciliation matrix

Source date for all custodian rows below: **2026-09-11**, latest present when measured. `Positions` counts position rows, not trades or clients. `Active` and `Pending` refer to the existing ETL roster, not business activation. `Canonical` means exact rows in the existing canonical daily valuation output.

| Workbook index / ending | Ready / Traded | 0833 account rows | Positions | ETL roster | Canonical rows | Disposition |
|---|---|---:|---:|---|---:|---|
| 1 / 5115 | Yes / Yes | 1 | 374 | Active | 1 | Traded claim corroborated; workbook 145 vs custodian 200 conflict |
| 2 / 3310 | Yes / Yes | 1 | 349 | Active | 1 | Traded claim corroborated; workbook 145 vs custodian 200 conflict |
| 3 / 0058 | Yes / Yes | 1 | 367 | Pending resolution | 1 | Traded claim corroborated; BD resolution is a technical gap |
| 4 / 9710 | Yes / Yes | 1 | 357 | Active | 1 | Traded claim corroborated |
| 5 / 9812 | Yes / Yes | 1 | 354 | Pending resolution | 1 | Traded claim corroborated; BD resolution is a technical gap |
| 6 / 8743 | Yes / Yes | 1 | 432 | Absent | 1 | Traded claim corroborated; missing from ETL roster |
| 7 / 4809 | Yes / Yes | 0 | 0 | Absent | 0 | Workbook-traded claim not corroborated in observed 0833 sources |
| 8 / 5591 | Yes / Yes | 0 | 0 | Absent | 0 | Workbook-traded claim not corroborated in observed 0833 sources |
| 9 / 4632 | No / No | 1 | 1 | Absent | 1 | Funded single-security account; not admitted as traded Tax SMA |
| 10 / 4702 | No / No | 1 | 0 | Absent | 1 | Zero balance; not admitted as traded Tax SMA |
| Unlisted / 4282 | Unconfirmed | 1 | 0 | Absent | 1 | Zero balance; discovery candidate, not proven live |
| Unlisted / 0650 | Unconfirmed | 1 | 0 | Absent | 1 | Zero balance; discovery candidate, not proven live |
| Unlisted / 4992 | Unconfirmed | 1 | 0 | Absent | 1 | Zero balance; discovery candidate, not proven live |

The funded-but-not-traded case has one DELL position in the inspected feed. This is a concrete negative case for the user's instruction: account existence, assets and the Tax SMA custodian label must not override Traded No. The six corroborated traded accounts each have both long and short positions. No aggregate of those six is asserted to be the complete eight-account value.

Across the full **7,469-row** 0833 account table, Tax SMA strategy labels identify **11 unique accounts**: eight labeled 145 and three labeled 200, all with open status and Opal Capital LLC as manager. Eight of the ten numbered workbook accounts match exactly; six of the eight workbook-traded accounts match. The three custodian-only candidates above are all zero-balance/zero-position cases.

The full **7,384-row** 0824 account table for the same business date contains **zero exact matches for all ten numbered workbook accounts**. This supports the observed separation of the named cohort from that base population; it does not prove absence from every master or justify an eternal hardcoded additive assumption.

## Source and producer evidence

| Plane | Observed source | Measurement |
|---|---|---|
| Manual ETL membership | `s3://opal-data-assets/blackdiamond/49f/_ops/taxsma_roster.json` | Modified 2026-08-27T22:48:18Z; 5 accounts, 3 active, 2 pending |
| Custodian identities | `s3://opal-data-assets/schwab/08335338/silver/fact_acc/date=2026-09-11/data.parquet` | 7,469 rows; entire latest object read |
| Custodian positions | Same 0833 silver root, `fact_rps/date=2026-09-11/data.parquet` | 105,074 rows; exact account comparisons |
| Custodian balances | Same root, `dim_balance/date=2026-09-11/data.parquet` | 7,469 rows; source of canonical account assets |
| Canonical daily value | `s3://opal-data-49financial/gold/advi/canonical/canonical_valuation/date=2026-09-11/data.parquet` | 7,468 rows; 549 parquet objects enumerated; same six traded accounts covered |
| Cross-master control | `s3://opal-data-assets/schwab/08242234/silver/fact_acc/date=2026-09-11/data.parquet` | 7,384 rows; zero exact workbook-account matches |
| BD identity crosswalk | `s3://opal-data-assets/blackdiamond/49f/silver/dim_account_xref/date=2026-09-11/data.parquet` | 6,202 rows; only one exact match within the compared population |
| BD Tax SMA report | `s3://opal-data-assets/blackdiamond/49f/gold/dim_taxsma_report/` | Exactly one parquet object, ending 5115, dated 2026-07-17; 45 quarterly/window rows |

The ETL membership version was `lNH3od2BprexiXQDjAxntCJjcNB_MK5t`, eTag `8462a2e7a994df410225af72efd2e073`. Among eight workbook-traded accounts its split is **3 active / 2 pending / 3 absent**. The current crosswalk's absence does not by itself invalidate manually pinned existing BD identifiers; no vendor resolution was retried.

Canonical valuation was modified 2026-09-14T12:47:35Z, eTag `f82e6ff4d860901e9199f762ad932486`, SHA-256 `899133db30f5cf66f631a5fee6b77c03b3927c19650811d32c4219caba1df170`. Its business date is September 11. Its value basis is `net_mv_plus_cash`; it retains balance components, `accrual_status`, `boundary_version`, `schema_version` and `source_pipeline`. Do not equate this silently with gross exposures or `eqty_incl_option`, which differs when margin balances are present. Accrued income remains an explicit upstream limitation.

The inspected Lambda `opal-assets-bd49f-reporting-pull` was Active with LastUpdateSuccessful and last modified 2026-08-30T09:14:51Z. A direct classic EventBridge target lookup found zero rules targeting its exact ARN. This is not an exhaustive census of EventBridge Scheduler, state machines or indirect invocation. No producer run or provider call was made. The single historical gold object is the direct evidence that this prefix is not a current all-account daily output.

## SharePoint prior art

| Item | Live identity / vintage | What it establishes |
|---|---|---|
| `TAX/Tax SMA Accounts.xlsx` | Item `01L6LHKFXVVTRR73M6KZGIHM4FY2ATNK4U`, modified Sep 14 | Current mixed live/prospect workbook and eight traded claims |
| `TAX/Literature/Tax SMA Accounts 20260805.xlsx` | Item `01L6LHKFQHQXJ4JSVIBVDIK3HCX6UPDPK7`, modified Aug 5 | Historical schema and masked identities; not a full-number identity baseline |
| `TAX/Tax Aware Capital Gains - SOP.docx` | Item `01L6LHKFT3OMLCT6QRK5DLQKQYKNMIEEAP`, modified Jul 27 | Onboarding readiness; no explicit pipeline completeness handoff |
| `TAX/Literature/Portfolio Margin Approval Process.docx` | Item `01L6LHKFR6TBK7KBN7UVCL4DT4FCB6WOC5`, modified Apr 14 | Firm and client margin approvals are readiness actions |
| `TAX/src/convert_cost_basis.py` | Item `01L6LHKFW2VXZXE4BICNBZHD24GQQBXPBO`, modified Sep 10, eTag version 28 | Ready-only lookup over existing input files; no complete traded-account denominator |

Exact SOP item ID: **`01L6LHKFT3OMLCT6QRK5DLQKQYKNMIEEAP`**, modified 2026-07-27T13:28:22Z, 29,341 bytes. The Gateway returned a three-page PDF for reading. It describes a Firm Tax FA master, money manager Opal Capital LLC under **BT master 0804-4932**, 145/200 strategy selection, portfolio margin and options approval. That onboarding master is a different role from reporting feed **08335338** and base feed **08242234**. The SOP does not define a machine-verifiable workbook-to-registry or 0833 coverage handoff.

The live cost-basis converter reads the workbook and removes dashes from account identifiers, checks Ready Yes, and then loops over cost-basis CSV files already present in the date folder. It does not check Traded for that workflow and does not enumerate missing expected files. It also contains weekday-only prior-date logic and a specific cost-basis override. It was inspected as prior art, not executed or edited. A D8 ingestion/reconciliation contract should not inherit those omissions merely because the converter already exists.

The August workbook has a title row, different headers and masked `XXXX-last4` account cells. The current workbook has its header in row one and complete identifiers. No exact newly-added-account claim is made from that historical comparison. Schema drift and masked identifiers need explicit refusal/disposition in the pipeline.

## Checked-in gearing

- `infra/aws/lambda/opal-assets/opal-assets-bd49f-reporting-pull/taxsma_registry.py`: versioned, conditionally written S3 roster; active/pending distinction; no workbook reconciliation. Its normalizer pads digit strings without enforcing the full identifier's minimum length. A production full-identity contract must reject suffix-only inputs rather than relying on padding.
- Adjacent `taxsma_resolver.py`: exact crosswalk lookup and duplicate refusal; documented infeasibility of the masked fallback; new provider egress is separately gated. The daily valuation recommendation avoids making that unavailable BD resolution path a prerequisite for already identified Schwab values.
- Adjacent `lambda_function.py`: discovery includes only active roster entries. Pending BD resolution therefore drops those accounts from pulls even when the workbook calls them traded.
- `data/assets/scripts/gold/build_dim_taxsma_report.py`: historical per-account report projection; multiple report windows, not the new daily all-account asset basis.
- `data/assets/scripts/gold/runners_49f/b00_canonical_valuation.py` and `runner_common.py`: existing canonical valuation reads 0833 balance and boundary data, takes V from `net_mv_plus_cash`, preserves decomposition and writes the live gold plane above. Reuse this engine's value contract and separately validate Tax SMA membership.
- `data/mdpf/scripts/gold/mdpf_category_registry.py`: existing `tax` member under SMA / ALT Strategies, additive basis. Historical five-account comments do not define today's live population.
- `data/mdpf/scripts/gold/mdpf_gold_consolidator.py`: source-carried versus registry-declared basis check; additive source basis required; Client subtracts only carve-outs; category total increases by the additive leg. The missing work is a correctly scoped, complete daily contribution and its honest failure/coverage propagation, including Global exactly once.

## Limits and interpretation

The latest September 11 source partition was observed before the September 15 morning delivery window. No lateness conclusion is drawn from wall-clock age alone. Source date, expected delivery and workbook effective dates must be reconciled explicitly.

The complete named workbook and relevant TAX, Literature and src folder listings were read; broader SharePoint searches returned 200 results and continuation links. This was not a tenant-wide exhaustive search. `comp-estate taxsma` had no matching corpus subject, and the B00 `comp-dataflow` trace extracted no reads because the actual I/O is imported: neither compiler result is evidence of absent live data. Direct source reads and object evidence supply the stated findings.

No cause has yet been proven for the two missing workbook-traded accounts or the two strategy-label conflicts. No live asset total is asserted for an incomplete cohort. No production valuation change, account-status correction, enrollment or rollout is implied by this audit. These are the explicit gaps and prior-art facts the brief and later PRD must carry.
