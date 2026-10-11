# ADVI_FIRMBKTS round 3 -- act 2 precondition: the census of readers of the 11 served legacy prefixes outside the 14 writers

**Author:** `2.0.0_SA_COO~B1` | **Date:** 2026-10-11 ~09:2xZ | **Asked by:** the CTO half of act 2 (msg 3673: "ONE census of
reads of the 11 classes' legacy prefixes over data/ and infra/aws/lambda (denominator printed), classed
producer-or-server / QA / router; the first class is routed through the seam or the act waits") | **Instruments:**
(1) `comp-find` literal census of the 11 prefixes over `data/black_diamond` and `infra/aws/lambda`; (2)
`deliverables/2.0.0_SA_COO~B1/round3/checks/r3_readers_outside.py` (AST, one hop through local helpers); (3) the dispatcher
and its configs read by hand. Neither (1) nor (2) alone is complete (see "What this census does not see").

## Denominators

- (1) `comp-find` over `data/black_diamond infra/aws/lambda`: 464 hits across 5,868 files scanned (1,581 binary not searched);
  45 distinct files after the band split (HEAD 9, DEF 8, SURFACED 21, CONFIG 2, TEST 3, DOC 2).
- (2) AST over every `.py` of those two trees except the 14 writers and the 8 lib modules `r3_reads.py` grades: 3,222 files,
  355 with an S3 data call; call sites SERVED 38, NOT-SERVED 630, UNRESOLVED 1,201 (dynamic keys); 11 files with a SERVED call.
  Of the 120 files that name the BD bucket or its layout, 103 carry UNRESOLVED calls (260 sites): those are NOT shown to read
  no served key, only not shown to read one.

## The readers, classed

| # | reader | what it reads (legacy prefix) | class | disposition proposed |
|---|---|---|---|---|
| 1 | `data/black_diamond/scripts/gold/gold_dispatch.sh:249` `gold_as_of` (the chain's freshness gate, read live: the key was last modified 2026-10-11T05:24Z, so a current writer writes it) | `gold/artifacts/summary/header_metrics.json` `data_as_of` (1 key, in the F7 manifest) | PRODUCER (the chain's own gate) | route through the seam (a one-line python read of the seam inside the shell function): under `canonical` it reads a frozen `data_as_of`, finds gold older than silver, and the chain runs on every trigger instead of skipping when fresh (cost, not data) |
| 2 | `data/black_diamond/scripts/gold/gold_freshness_config.yaml` (`s3_key_prefix: s3://opal-data-bd/...` for served keys) read by `bd-served-vintage-alarm`, `infrastructure_monitor` and `compdiff/freeze_monitor.py` (comp-find, 5 files) | LastModified / vintage of served keys | QA / MONITOR (existing alarms) | follow-up for act 4's pair: the monitors' key list follows the router's map; between act 2 and act 4 the alarm reading the legacy home is CORRECT (the served home is stale by design) |
| 3 | `infra/aws/lambda/exec-summary-generator/` (`platinum_reader.py`, `config.py`, `exec_summary/*`) | `platinum/advisors/` listing and `summary.json` reads | SERVER (generates user-facing summaries) | a Lambda deploy act with the seam in its package, or it serves frozen legacy |
| 4 | `infra/aws/lambda/v2_portal/partners/lambdas/opal-partners-data/lambda_function.py` (16 SERVED call sites; the bucket is read per firm from DynamoDB `s3Bucket`) | `gold/artifacts/snapshots/aua_by_*.json`, `gold/artifacts/filters/dimensions.json`, `gold/artifacts/clients/*` | SERVER (client-facing partners API) | the firm's DynamoDB bucket/prefix mapping moves with act 4, or it serves frozen legacy: a data change with its own pair |
| 5 | `infra/aws/lambda/bd-pipeline/bd-incrparity-trigger/incrparity_cli.py` | `gold/views/mix_daily_summary.json` (map `C_06`) | QA / monitor (incremental-parity trigger) | follow-up; after the move it compares a frozen object |
| 6 | `data/black_diamond/scripts/gold/validate_platinum_consistency.py` (6 SERVED), `gold_validate_config.yaml` | `platinum/firm/dashboard.json`, `platinum/firm/clients_tab.json`, `platinum/advisors/` | QA (not in the dispatcher catalog) | follow-up; reads the legacy home |
| 7 | `E_20`, `E_21`, `E_22`, `E_25`, `gldrst/preflight_snapshot.py`, `gldrst/verify_migration.py`, `diag_verify_cliff_fix.py`, `C_01b.role_aua_backfill.py` (the last is a manual backfill, not in the catalog) | `gold/views/*`, `gold/artifacts/*`, `platinum/*` | QA / ad hoc | follow-up; `C_01b` reads `gold/views/account_team.parquet` |
| 8 | the Lambda@Edge router `shared-advisor-router` and the guard | the served-key map and class list | ROUTER | act 4 |
| 9 | `infra/aws/lambda/inf-portal-publisher`, `inf-portal-advisor-publisher`, `inf-*`, `cot-*` | `opal-data-inf` / `opal-data-cot` (their own buckets; `BD_DATA_BUCKET` defaults to `opal-data-cot` in `bd-cot-freshness-probe`) | OTHER FIRM | excluded with the bucket as the evidence (CLAUDE.md: never another firm's data) |

## What this census does not see (stated)

- A reader whose key is built from a name defined in another module (the AST resolves `s3_layout`/`config` and the file's own
  constants; `exec-summary-generator/config.py` constants were found only by the literal instrument).
- Non-Python readers other than the two shell and YAML files read by hand: `.mjs`/`.js`/`.ts` Lambda sources, other `.sh`,
  Terraform and Athena/Glue definitions were not walked by instrument (2). The literal instrument (1) covers them for the
  eleven literal prefixes only.
- 103 BD-named files with dynamic keys. Their reads are not shown to touch a served key.

## The ruling this needs

The producer-or-server class (rows 1, 3, 4) is not routed. Row 1 is code in the gold runner's tree and can be a dormant
phase A4 under the same worker pattern; row 2 is monitors, not a gate, and rides act 4. Rows 3 and 4 are deployed services outside the gold runner: each is its own deploy act
with its own pair (and, for rows 3 and 4, may be a Lambda that the Dell identity may or may not deploy). The act-2 pair's
precondition therefore does not clear this window unless the CTO rules one of: (a) A4 for rows 1 and 2 now, and rows 3 and 4
sequenced as acts of this window with their own pairs; (b) rows 3 and 4 accepted as reading the frozen legacy home until a
round-4 act, stated to Andrew as a client-facing staleness; (c) another order.

## ADDENDUM 1 (2026-10-11 ~10:0xZ) -- the BD-named dynamic-key files, classed by how each composes its key (the CTO's act-4 condition, msg 3713)

**Instrument:** `r3_readers_outside.py --dynamic` (AST, def-use through up to 3 local assignments in the call's function,
sibling-module constants resolved; no AWS). Population: every `.py` of `data/black_diamond` and `infra/aws/lambda` except the
14 writers and the 8 lib modules `r3_reads.py` grades, that names `opal-data-bd`, `BD_S3_BUCKET`, `s3_layout`, `lib.config` or
`from lib import`, and carries an S3 data call whose key has no static prefix.

| class | sites | reading |
|---|---|---|
| SERVED-REACHING (a name feeding the key resolves under a served prefix) | **0** | class (i): none to route |
| NON-SERVED (every feeding name resolves outside every served prefix) | 63 | not a served reader |
| PARAM (the key is a function parameter; its callers decide) | 151 | graded at the callers by the one-hop pass: the 11 files with a SERVED call, already classed above |
| UNKNOWN (no feeding name resolves) | 46 | listed by file and line in the instrument's output; `latest_key`, `latest_file`, `key=prefix`-style lookups of a listing under a bronze, silver, gold-canonical, config or `investor-reporting/` prefix |

Of the 46 UNKNOWN sites, 45 carry no served-prefix literal anywhere in their own function and the one that does is
`data/black_diamond/scripts/diag_verify_cliff_fix.py:20` (a diagnostic reading `gold/views/*.parquet`: class ii, QA, already
in the table). Four lambdas read a bucket other than `opal-data-bd` for their keys (`mdpf-freshness-checker`: `opal-data-portal-v2`
by environment; `bd-cot-freshness-probe`: `opal-data-cot`; the investor-reporting lambdas: their directory bucket map;
`bd-49f-etf-ownership-daily-canonical`: `gold/canonical/holdings/` in, `daily/49financial/` out, both outside the served
classes).

**Not shown, stated:** the 45 UNKNOWN sites are not PROVEN to read no served key: the instrument sees a name it cannot
resolve, not the value the name holds at run time. The evidence is the absence of a served-prefix literal in any of their
functions and the directory each file sits in. Class (i) found: 0. Act 4's condition reads "class (i) routed or act 4 waits":
there is nothing to route, and the residual above is carried to the CTO's reading rather than closed by inference.
