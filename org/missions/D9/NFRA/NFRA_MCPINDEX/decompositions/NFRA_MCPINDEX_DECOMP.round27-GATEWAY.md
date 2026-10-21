# NFRA_MCPINDEX -- decomposition addendum, ROUND 27, workstream GATEWAY (2.0.0_SA_COO~MI)

**archetype:** COORDINATE

Companion to `NFRA_MCPINDEX_DECOMP.round26-GATEWAY.md`. One issuer, one round, ONE issuance (workstream GATEWAY, round 27). Spec-frozen once issued.

Source: the CTO's round-26 analysis `ledger/ROUND_ANALYSIS.round26.md` @4f85c8cf6a (`1.0.0_SA_CTO~Z`, msg 36269), the round-26 evidence (`deliverables/2.0.0_SA_COO~MI/round26/evidence/`, esp. `ROUND26_REPORT.md` @e81a0e5a3c7 and `PER_VENDOR_RUN_20261021.json`), PRD v0.19 @7c42c0c743. Round 26 closed on the CTO's analysis (the close check refuses only for the absent reviewer seat while the broker is down). Rulings in force: the `platform_not_source_label` refusals are NOT graded as tool faults until a run uses the labels the tools accept; the 33 graph and 9 integration tools with no second client are PARKED (owner this seat; un-park condition: a seat holding a direct second client for that surface) and drop off the round list; the Commonwealth gap (newest partition 2026-06-23, 83 trading days) is a data-freshness finding, no fix in this project; the sheets' site is HELD for Andrew; candidate e (catalog md5 03d2dbbae1f07b8d4fa5f0eaa73355d6) is NOT served and serving it is ordered to `2.0.0_SA_COO~O`.

Reading of the adapters at the cut (read-only, `infra/aws/ec2/opal-gateway/app/client_adapter_*.py`): the `platform` argument of the `client_*` tools is a CUSTODIAN label read from the data partition, never a vendor or contract name (`client_adapter_schwab.py:12,47,100`: "a contract label (SmartX, BlackDiamond) passed as a platform" is refused; `client_adapter_orion.py:186,206,231` and `client_adapter_eclipse.py:156`: "not a custodian label in this partition"; `client_adapter_bdcottonwood.py:192,283,448`; `client_adapter_commonwealth.py:96`; `client_adapter_smartx.py:85`). The round-26 per-vendor run passed vendor names as platforms; those refusals were input errors of that run.

Nothing in this round touches the gateway, a grant, the live catalog, or sends anything. Every worker cell writes local files; the live chains, the served-md5 routing run and the battery are the issuer's drain acts (R27.4).

## R27.1 INPUTS (all under `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/`, read-only to workers)

- `2.0.0_SA_COO~MI/round26/evidence/PER_VENDOR_RUN_20261021.json` (the chains and codes), `ROUND26_REPORT.md`; `4.0.0_SA_CRO~Y/ADVISOR_TABLES_PER_VENDOR_BRIEF_20261020.md` (section 4 per vendor: tables, columns, freshness; 4.7 Commonwealth) and `4.0.0_SA_CRO~Y/census.json` (newest partition per table).
- the gateway source `infra/aws/ec2/opal-gateway/app/` (`client_adapter_*.py`, `client_core.py`, `tools.py`), the catalog `infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml`, `workflows/gateway_battery/` (`cheatsheet.py` and tests), the round-24 sheets `2.0.0_SA_COO~MI/round24/sheets/`, and the infrastructure and ETL sources under `infra/` and `data/` (read-only).
- the Eclipse copier file `0.9.0_WK_NFRA_MCPINDEX~91/eclipse_copier.json` (the model for a producer, schedule and owner finding).

## R27.2 THE CELLS (three independent chains)

| cell | analysis item | class | deliverable | slot |
|---|---|---|---|---|
| `MX-u-1` | 2 platform labels read from source | data | `deliverables/0.9.0_WK_NFRA_MCPINDEX~94/platform_labels.json` | ~94 |
| `MX-u-2` | 3 Commonwealth freshness producer, schedule, owner + one surprise row | data | `deliverables/0.9.0_WK_NFRA_MCPINDEX~95/commonwealth_producer.json` | ~95 |
| `MX-u-3` | 2 platform labels into the per-employee sheets | code | edit `workflows/gateway_battery/cheatsheet.py` + `tests/test_cheatsheet_labels.py` | ~96 |

Items 1 and 4 (routing and battery on candidate e once served; the per-vendor re-run after NFRA_OPLGTW round 48) are event-gated and are the issuer's drain acts. The parked tools need no cell.

## R27.3 FROZEN CONTRACTS

**U1 PLATFORM LABELS** `platform_labels.json`, schema `gateway_platform_labels/1`: `{"schema","items":[{"tool","adapter","firm","accepts_platform":true|false,"platform_meaning":str,"label_source":{"table":str,"column":str}|null,"omit_means":str,"refusals":[{"code":str,"when":str}],"cite":"<path>:<line>","evidence":[str,...]}]}`. One item for each pair (tool, adapter) over the five `client_*` tools (`client_resolve_account`, `client_get_holdings`, `client_get_allocation`, `client_get_fees`, `client_get_transactions`) and every client adapter file `client_adapter_*.py` that handles a `platform` argument (read `client_core.py` and `tools.py` for the dispatch to find which adapter answers which firm); items sorted by (tool, adapter). `platform_meaning` (at least eight ASCII words) states what a valid `platform` is for that adapter, read from the code (for example a custodian label read from a named column of the vendor's own table, or "no platform label: the argument is ignored or refused"); `label_source` names the table and column the accepted values come from when the code reads them from data, else null; `omit_means` (at least eight ASCII words) states what the adapter does when `platform` is omitted; `refusals` lists the refusal codes the adapter raises about `platform` with the condition in at least five words; `cite` and every `evidence` entry are `<path>:<line>` of a file that exists with at least one `evidence` entry that is a different line from `cite`. No account number, name or data value appears anywhere in the file.

**U2 COMMONWEALTH PRODUCER** `commonwealth_producer.json`, schema `gateway_commonwealth_producer/1`: `{"schema","feed":{"bucket","prefix"},"newest_partition":str,"trading_days_behind":int,"producer":{"kind":"lambda"|"script"|"glue"|"ecs-task"|"terraform-only"|"manual"|"other","name":str,"cite":"<path>:<line>"},"schedule":{"expression":str,"cite":"<path>:<line>"},"owner":str,"gap_cause":str,"evidence":[str,...]}`. `feed` is the Commonwealth silver feed `opal-data-assets` `commonwealth/cottonwood/silver/` (read the catalog rows and the CRO brief section 4.7 and `census.json`); `newest_partition` and `trading_days_behind` come from the CRO files and the round-26 report (2026-06-23, 83 trading days at 2026-10-21); find in the repository the job that writes that feed and its schedule (Lambda, script, Glue job, scheduled task, or a manual upload with its runbook) and the project that owns it (`owner` is a project code that exists in `org/projects/`). `gap_cause` is at least twelve ASCII words explaining, from the code and the schedule, why no partition after 2026-06-23 exists, or says what cannot be established from the repository and why. All `cite` and `evidence` entries resolve (at least two evidence entries); when no producer is found the `producer.kind` is `manual` or `other` with `name` `none-found` and at least three evidence entries naming what was searched. The cell ALSO files ONE surprise row on the project's channel (`surprise-channel/investigations/INVESTIGATION_v1.md`): class OBSERVATION, hazard INERT, `disarm_owner` `2.0.0_SA_COO~MI`, `one_line` stating the measured gap (newest partition 2026-06-23, 83 trading days behind), `grounding` GROUNDED with the cites. No fix in this project.

**U3 SHEETS LABELS SECTION** `cheatsheet.py gen-all` gains `--platform-labels FILE` (optional; absent = the round-25 behavior byte for byte). The file is a `gateway_platform_labels/1` document (shape of U1). When given, every written sheet that lists at least one `client_*` tool gets, after the tool list, a section headed `Platform labels` (ASCII) that states in one line per listed `client_*` tool: the tool name, then `platform: ` followed by the item's `platform_meaning` (when several adapters answer a tool, one line per adapter, sorted by adapter), then `omit: ` followed by `omit_means`. A sheet with no `client_*` tool is unchanged. A malformed file (wrong schema, an item missing a field, an unknown tool name, a non-ASCII character) exits 2 before anything is written. The section holds no data value and no account identifier. Two runs give byte-identical sheets; `--upload-manifest` continues to carry the sheets as written (the new section included) and keeps its guards.

## R27.4 THE ISSUER'S REAL RUN AT THE DRAIN (not worker cells)

1. U1: read the accepted custodian label values per adapter from the vendor tables (list-only S3 reads and distinct-value counts, no account data), re-run the Schwab chain (both masters) and the Eclipse chain with valid labels (counts and codes only, two gateway calls at a time), and ask COO~O one line per tool naming the accepted labels if the tool descriptions do not state them.
2. U3: regenerate the 17 sheets with `--platform-labels`; they stay local (the site is held for Andrew).
3. U2: relay the Commonwealth producer and owner to the owner MSTR to MSTR.
4. When candidate e is served: re-run the routing table on the new served md5 and commit it with that md5 (target link 0), then the battery; record the result as the input to the CVO's re-grade of MCPORTAL MP-z-6 AC2.
5. After NFRA_OPLGTW round 48 lands: re-run the per-vendor chains and record each changed result against the round-26 table.
6. `round-close-check --round 27`, then the L10 slug to `1.0.0_SA_CTO~Z`.

## R27.5 WHAT THIS CUT DOES NOT CLAIM

It does not change a grant or a tool, upload a sheet, serve the catalog, or realize FWD-23, FWD-24 or FWD-25 by itself. The live runs and the numbers come from the drain.
