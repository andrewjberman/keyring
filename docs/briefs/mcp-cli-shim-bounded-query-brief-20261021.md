# Brief: the MCP as an AWS-CLI shim -- folder-scoped, bounded query over the tables a user may read (midstream, NFRA_OPLGTW + NFRA_MCPINDEX)

**Author:** 4.0.0_SA_CRO~Z, 2026-10-21 ~15:xxZ. **Mode:** `/brief-create --midstream`.

**Orders** (both Andrew-direct, verbatim):
- ~13:3xZ `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/ANDREW_DIRECT_20261021_133xZ_MCP_LARGE_TABLES_PAGINATE_CHUNK_EFFICIENCY_OPLGTW_MCPINDEX.md`
  @1ca1fc4dcb;
- ~14:xxZ `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/ANDREW_DIRECT_20261021_14xxZ_MCP_IS_AN_AWS_CLI_SHIM_BUCKET_PREFIX_ENTITLEMENT_NO_EXTRA_LAYERS.md`
  @243c25998e.

The CTO folds this into 2.0.0_SA_COO~O (NFRA_OPLGTW) and 2.0.0_SA_COO~MI (NFRA_MCPINDEX).

**Andrew, verbatim:**
- "this is really just an AWSCLI put on top of an MCP"
- "The entitlement layer is for accessing whole buckets, accessing buckets or maybe accessing various folders within those
  buckets"
- "no custom tables, no nothing"
- "We obviously want to do this in such a way where Claude is not pulling in ... 5000000 rows into context"
- "we can retain a control plane"

## PRIORITY (Andrew, addendum ~14:0xZ, record `ANDREW_DIRECT_20261021_14xxZ_ADDENDUM_PRIORITY_SCHWAB_ORION_COTTONWOOD_BD.md`)

> "the most important thing for now is that the tables that are in there, for both Schwab and Orion (and Cottonwood Black
> Diamond), are manageable in the current state."

Analysis moves to Schwab and Fidelity; SmartX, Orion, Eclipse and Black Diamond serve models and model management. SmartX "and
etc" are deferred. So **F7's firm-fence gaps (SmartX, Eclipse, Commonwealth) are out of the first cut**, and the round-1 scope
is the three named sources, measured below.

| Source | Today's tables (largest single file) | Served by | Manageable now? |
|---|---|---|---|
| **Schwab** `schwab/<master>/silver/` (3 masters, 18-20 tables each) | `dim_position` 106k-110k rows / 2.5 MB; `dim_balance` ~7.7k; `dim_transaction` ~7k per day; `fact_rlw/rly/rlu/uln/ult` 219k-384k rows, 5-8 row groups, 18-42 MB per partition | `schwab_*`, through the bounded DuckDB child (256 MiB, page 100 / cap 500 rows, cursor), for the 4 `dim_*` datasets. The `fact_*` tables are served by no tool | **Yes for the 4 granted datasets**: bounded and paged. A 13-month `dim_transaction` window is ~270 partitions, past the engine's 12-object / 64 MB source cap, so long windows need the engine to page by partition. The `fact_*` tables fit one partition per job (42 MB < 64 MB) |
| **Orion** `orion/inflection/silver/` (5 tables) | `fact_transactions` 1.53M rows / 31 row groups / 34 MB (one snapshot, 160 partitions); `fact_performance` 485k; `fact_positions` 37k | `client_*`, but **not answering today** (part-1 D1: no fence kind for orion) | **Not as currently coded.** The `client_*` path downloads the whole object and converts it to Python. Fixing D1 on that path would load 1.5M rows into the gateway per transactions call. Orion needs the DuckDB child (or an account filter before conversion, `read_account_rows`) as part of the D1 fix |
| **Cottonwood Black Diamond** `blackdiamond/cottonwood/silver/` (14 tables) | largest 61,730 rows, one row group, one file per partition | `client_*` | **Yes on size.** Correctness needs part-1 D2 (MM/DD/YYYY dates drop every transaction and fee row), not paging |

The 21.1M-row file is **Commonwealth**/Cottonwood, not Black Diamond/Cottonwood, so under this priority it is deferred with the
other non-Schwab sources. Its adapter is also not answering (D1).

## PART 0 -- How the blind constraint was honoured, and where it bent

**Not read:** either project's task orders, or their phase and blocking fields.

**Read:**
- the served gateway release (2923d1ee99, live since 2026-10-21T07:20Z), checked by content against HEAD;
- the S3 layout and sizes, measured today;
- the gateway source.

**Where it bent:**
1. The source carries task-order labels in its comments (OG-sz-1, OG-tp-1, OG-sx-1, OG-mg-4). They name fixes made in the last
   two days, and I cite them as code.
2. My own audit of 2026-10-19 (parts 1-3) and the entitlement brief of 2026-10-20 shape Part IV.
3. Andrew's second message redirected the first ask mid-analysis: from "paginate the large tables" to "the MCP is a CLI shim".
   This brief serves the second, and keeps the first's measurements.

## PART I -- THE OUTCOME TERRITORY

**Candidate thread (FWD-1 shape).** A staff member granted one folder (for example `opal-data-assets/schwab/08335338/`) asks,
in Claude: "how many accounts held DIVZ on Friday, and what is their total value?"
- Claude lists the folder, reads the table's columns, and runs one query.
- The answer is a few rows with a total, computed in AWS-side or child-process memory, never millions of rows in context.
- The same question asked of a folder the person is not granted is refused, by folder name.

### O1 -- A person sees the buckets and folders they may read, as the AWS CLI would list them
### O2 -- A person reads any permitted table's columns and types without reading its rows
### O3 -- A person asks a SQL-shaped question of a permitted table and gets the answer: aggregated where possible, at most one page of rows otherwise, with a cursor to the next page
### O4 -- A person reads the next page, and the page after, until the answer is complete, without any one call holding more than one page
### O5 -- A query of a very large table (the 21M-row Cottonwood file) answers without loading the file whole on the gateway
### O6 -- The owner grants or removes a whole bucket, or a folder within one, per person, in one act, and that is the whole entitlement model
### O7 -- The index tells Claude which folder holds what, so Claude picks the right table without listing everything first

## PART II -- WHERE THE BOUNDARY SITS

- **NFRA_OPLGTW (2.0.0_SA_COO~O).** The gateway's generic tools (list, describe, query), their bounded execution, the
  bucket/folder entitlement check, and the IAM read roles behind it.
- **NFRA_MCPINDEX (2.0.0_SA_COO~MI).** The light index: which folder holds which table, its plain-words meaning and its size
  class. It is not per-dataset typed tools.
- **NFRA_MCPORTAL (2.0.0_SA_COO~MP).** The page where the owner grants or removes a bucket or folder per person. The
  2026-10-20 brief covers the mechanics; under this direction its channel switch becomes a folder switch.
- **Not in scope, and not decided here:** whether the existing typed tools (`client_*`, `etfs_*`, `harvest_*`, `portal_*`,
  `mdpf_*`) are retired, kept as conveniences, or rebuilt on the generic query. Andrew: "The tools may not even be
  necessary." That is his call at L2, not this brief's.

## PART III -- THE QUALITATIVE BAR

- **Nothing hidden.** A person who is granted a folder sees exactly what the AWS CLI would show for it. No column or row is
  silently withheld, and nothing is renamed or masked behind their back.
- **Context-safe.** No call puts more than one page into Claude's context. A question that needs every row gets a total, or a
  cursor, never a dump.
- **Server-safe.** No call holds a whole large file in the gateway process. The heaviest query fails as "too big, narrow it",
  never as an outage.
- **Clear when refused.** A refusal names the folder that was refused, and why, in words the person can act on.

## PART IV -- THE SUBSTRATE (findings, each measured)

**F1 -- The folders are already shaped for folder entitlement.**
- 121 silver tables were measured across `opal-data-assets` and `opal-data-bd`. 113 use hive partitions
  (`.../<table>/date=YYYY-MM-DD/`) with one file per partition. 5 use flat `<date>.parquet` (the Black Diamond live tables),
  and 3 are undated.
- Layout: `<vendor>/<firm or master>/silver/<table>/`. Examples: `schwab/08242234/`, `orion/inflection/`,
  `blackdiamond/cottonwood/`, `commonwealth/cottonwood/`, `smartx/platform/`.

**F2 -- Most partitions are small, and only a few tables are inherently large** (largest single file, rows and row groups):

| Table | Rows / row groups / bytes |
|---|---|
| Commonwealth/Cottonwood `account_day_value` | 21.1M / 21 / 54.8 MB, one partition |
| Commonwealth/Cottonwood `daily_returns` | 1.7M / 2 |
| Orion/Inflection `fact_transactions` | 1.53M / 31 / 34 MB |
| Orion `fact_performance` | 485k |
| Ten Schwab tables (`fact_rlw/rly/rlu/uln/ult`) | 219k-384k / 5-8 / 18-42 MB |

Every other vendor's newest partition is 123k rows or fewer. Row groups of about 1M rows make column and row-group pushdown
effective, so a query can read a slice of a file, not the whole file.

**F3 -- How reads work today (served release), per family:**
- **`client_*`.** Downloads whole objects up to 64 MB, then converts unfiltered partitions (114k-123k rows) to Python to answer
  one account (`client_adapter_bd49f.py:478,517,646`; smartx). The exception is the 49F transaction and fee windows:
  `PAGE_PARTITIONS = 30` plus `next_cursor`, behind a one-slot gate.
- **`harvest_*`.** The same whole-object path, up to 64 MB, then `to_pylist` plus a JSON round-trip
  (`harvest_typed.py:263-303`).
- **`portal_*` / `mdpf_*`.** The whole JSON object is parsed, then trimmed.
- **Reply sizes.** Since 2026-10-20 (OG-sz-1, OG-tp-1, OG-sx-1, in the served release) every audited family's reply is
  bounded at 50 KB measured on the served bytes. **The reply is bounded; the read behind it is not.**

**F4 -- The bounded engine this brief needs already exists: the Schwab engine** (`integrations/schwab/engine.py`, `cursor.py`,
`query.py`):
- **Isolation.** DuckDB runs in a spawned child process: 256 MiB per job, 30 s, 1 thread, external access off.
- **Reads.** It reads only the referenced columns, and rows pass through a policy semi-join before any row exists.
- **Admission.** 2 jobs globally and 1 per principal, with no queue. A job is admitted only against measured free RAM, else
  BUSY.
- **Paging.** Results come back as pages (default 100, cap 500 rows / 128 KB), with an HMAC cursor that expires in 300 s.

It is wired to Schwab sources only, behind a typed plan rather than SQL text, and its policy model is per-account and
per-column. Under Andrew's direction the policy reduces to "the object lies under a granted folder". Its 12-object / 64 MB
source cap would need a size class for the 21M-row file (F2).

**F5 -- The gateway's in-flight guard counts calls, not cost.**
- `MAX_INFLIGHT = 26` (`inflight_guard.py:20`), in one uvicorn worker, on a t4g.large with MemoryHigh 5600M and MemoryMax
  6400M (`deploy/opal-gateway.service:20-22`).
- So 26 concurrent whole-file reads can still reach the memory limit. That limit was hit on the old t4g.small on 2026-10-19
  (Z-S420).

**F6 -- Entitlement today is not folder-shaped.** It is spread across five mechanisms:
- the tier rosters (a secret);
- a per-person data grant (masters, accounts, columns, dates, operations, `portal_channels`);
- a per-person deny record (channels and tools);
- an identity tool allowlist;
- the `client_*` tools gated to master_admin.

Andrew's model replaces this with one rule: a person may read a bucket or folder. The existing IAM read roles are already scoped
by bucket and prefix (`client_role`, `typed_scope.Scope`), so the IAM side of a folder grant exists.

**F7 -- Where the folder model does not fence a firm** (named, not decided):
- (a) `smartx/platform/` mixes several firms in one file (catalog `firm: multi`);
- (b) the three Schwab masters are all 49F, so the folder is a master, not a firm;
- (c) `opal-data-bd` holds one firm (49F) with no firm folder;
- (d) Orion has two segments, `inflection` and the `4698` alias.

For a partner-firm login, (a) is the only case where a folder grant would show another firm's rows.

**F8 -- Light indexing already exists.**
- The catalog's `tool_index` and `silver_datasets` rows carry the bucket, prefix, table, layer, plain-words meaning and
  `history_depth` (date span plus partition count).
- No row records rows or bytes per partition (the size census of 290 locations found none). A size class per folder (small /
  large / very large) is the one field the index lacks for Claude to choose aggregate-or-page up front.

## PART V -- WHAT MUST BE TRUE, WITHOUT SCOPING IT NOW

- A generic query runs only against objects under the caller's granted folders, checked before any read, by the same IAM
  role scoping the gateway uses today.
- No caller string becomes SQL text without the closed-grammar discipline the Schwab engine already uses. The guarantee of
  "SQL-shaped access" and the injection guarantee must coexist.
- Every query has a row and byte ceiling per page and a total ceiling per job. The very large tables answer with aggregates
  or pages, never whole.
- Andrew rules whether the typed tools stay, and whether the SmartX mixed-firm folder may be granted to a partner (F7a).
- The NFRA_OPLGTW contract (`org/standards/NFRA_OPLGTW_CONTRACT.json`) states per-account and per-column grants and masked
  account references. Under this direction those clauses are superseded by Andrew's word; the contract needs a revision
  that says so.

## PART VI -- STATUS (NOT OUTCOME-BEARING)

| Claim | Measured |
|---|---|
| layout: 121 tables, 113 hive-partitioned, one file per partition; sizes as in F2 | S3 list plus parquet footers, 2026-10-21 ~14:3xZ |
| 290 catalog locations measured; 87 over 1 MB, 43 over 10 MB, 10 over 100 MB (9 of them read by key or unserved) | fork census, 2026-10-21 ~14:0xZ |
| served release 2923d1ee99 carries OG-sz-1 (indent-measured projection) and MAX_INFLIGHT 26 | content check of the release, 2026-10-21 |
| host t4g.large, MemoryHigh 5600M / MemoryMax 6400M | `ec2 describe-instances` plus the unit file, 2026-10-21 ~14:0xZ |
| Glue database `opal_mcp` holds 1 table (`mcp_audit`); Athena workgroup `opal_mcp` exists | `glue get-tables`, `athena list-work-groups`, 2026-10-21 |

## PART VII -- WHAT THIS BRIEF DOES NOT CLAIM

- **Not run:** no generic query against the 21M-row file, so its DuckDB time and memory are estimated from row groups, not
  measured.
- **Athena not costed or timed.** It is an alternative for the very large tables (the workgroup exists; the tables would need
  Glue registration or partition projection, which is metadata, not "custom tables"). DuckDB in the existing child is the
  lighter fit to "no extra layers".
- **No retirements decided.** No typed tool is retired here; Part II names the call.
- **No security review** of exposing raw account numbers to every holder of a folder. Andrew's word is no redaction. This
  brief records that it changes what a folder grant discloses.
- **No sequencing or cells.** Those are step 5.

## REFS TO CARRY

```
  BRIEF PATH        docs/briefs/mcp-cli-shim-bounded-query-brief-20261021.md
  PROJECT           NFRA_OPLGTW (2.0.0_SA_COO~O) + NFRA_MCPINDEX (2.0.0_SA_COO~MI), midstream; NFRA_MCPORTAL for the grant page
  EXISTING PRD      org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md; org/missions/D9/NFRA/NFRA_MCPINDEX/prd/NFRA_MCPINDEX_PRD.md
  SIBLING BRIEF     docs/briefs/mcportal-entitlement-add-subtract-brief-20261020.md (542fb0983f)
  PRIOR ART         app/integrations/schwab/engine.py, cursor.py, query.py (bounded DuckDB child, cursor);
                    app/client_adapter_bd49f.py:82-92,311-394 (PAGE_PARTITIONS, next_cursor, gate);
                    app/typed_scope.py:33-40 (streamed 2,048-row batches, footer guard);
                    app/client_role.py (bucket/prefix-scoped read roles); app/inflight_guard.py
  AUDITS            org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/GATEWAY_TOOL_AUDIT_*_2026101*.md (216dfc8144, 48c5806982, df8a98cbed)
  MEASURED AT       2026-10-21 13:4xZ-14:4xZ
```
