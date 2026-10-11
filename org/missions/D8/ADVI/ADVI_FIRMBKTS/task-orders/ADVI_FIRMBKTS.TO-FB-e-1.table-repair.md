# ADVI_FIRMBKTS task order -- `FB-e-1` -- THE MAPPING TABLE'S REPAIR

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R2.md</decomp_doc>
<owned_cells>FB-e-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_FIRMBKTS~4</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, rule, schedule or cadence is added or changed.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change; the only AWS acts are read-only list_objects_v2 calls by the box's existing identity.
comp-adversary: RUN by the issuer (2.0.0_SA_COO~B1) on dell1 -- r2_mapping.py structure 0 of 5 and repair 0 of 4 at base (mapping_v2.json absent); 5 of 5 and 4 of 4 on a reference table; mutants: no owner 4 of 5, typed address 3 of 5, a round-1 row disturbed 3 of 5, an unruled collision 3 of 4.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `FB-e-1` (round 2, enrichment item 2; decomposition v2)

Round 1 placed 209 of the 444 census classes. 226 are FAULT in `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/mapping.json`.
FWD-2 reads each as a fault in the TABLE, never a decision for whoever holds it: you do not decide a class. You apply
the REPAIR RULES in section 1c, which are the issuer's rulings, and a class they do not place stays FAULT with a named
owner. You write the repaired table as a NEW file; round 1's `mapping.json` and `census.json` are read-only.

### 1a. The key string (ruled; PRD CONTRACTS)

`{source}/{scope}/{tier}/{table}/{partition}`, the bucket as its container and the object as its leaf.
- `{scope}` in a firm bucket is that bucket's own firm in the LONG form: `opal-data-bd` -> `49financial`,
  `opal-data-inf` -> `inflection`, `opal-data-cot` -> `cottonwood`. Write it `{F}` below.
- `{tier}` is `gold`, `platinum`, `state`, `bronze` or `silver`. Bronze and silver never live in a firm bucket: `address()`
  homes them in `opal-data-assets` itself.
- **Every new location comes from `lib/opal_naming.py` `address(source, scope, tier, table, partition, object=None)`,
  never typed.** A builder REFUSAL is a FAULT row (reason `builder refused: <its message>`), never a hand-spelled string.
- `{V}`, the vendor of a pass-through key: the path contains `eclipse` -> `eclipse`; contains `orion` -> `orion`; starts
  `smartx/` -> `smartx`; contains `schwab/` -> `schwab`; starts `blackdiamond/` -> `blackdiamond`; otherwise the
  bucket's feed: `opal-data-bd` and `opal-data-cot` -> `blackdiamond`, `opal-data-inf` -> `orion`.
  The product source of a derived tier is `advi`; `investor-reporting/` is `irpt`.

### 1b. What you keep

Every round-1 row whose disposition is MOVE, HOME, RETIRE or DECISION is copied into `mapping_v2.json` UNCHANGED (all its
fields). The check proves it (the difference control). Only the 226 FAULT classes are worked. THE ONE EXCEPTION is
section 1e's: a round-1 MOVE or HOME class whose MEASURED destination-key overlap with another class is above 0
becomes a FAULT row (its `dest`, `address` and `dest_pattern` are dropped), reason `destination-key overlap <n> of <m>
keys with <the other class>`, owner `1.0.0_SA_CTO~DELL1`; the check admits that change only with that reason text.

### 1c. THE REPAIR RULES -- ordered; the FIRST rule a class matches decides it

Match on the class's `prefix` (and, for a re-gridded child, its own prefix). `<seg1>`, `<seg2>` are the path segments
of the sample key after the matched prefix, `<rest>` the remainder after them, `<file>` the key's last segment.

**Copies and run output -- RETIRE** (moves nothing, deletes nothing; removal is a later cell's, after a reader census):

| rule | the prefix (any bucket) contains or starts | reason to write |
|---|---|---|
| RA | `GOOD_RUN_`, `_rollback/`, `_regen_backup_`, `_pre_rebuild_backup/`, `backup/`, `_compare/`, `_rebuild/`, `_rebuild_status/`, `_quarantine_`, `_parity-snapshot/`, `v4_output/`, `runs/`, `.bak-`, `_backup_` | backup, rollback, quarantine, rebuild-staging or parity-snapshot copy; no destination (R17, R18) |
| RB | `logs/`, `diagnostics/`, `diagnostic/`, `debug/`, `qa-scratch/`, `_scratch/`, `_toolprobe_scratch/`, `tmp/`, `temp/`, `ssm-output/`, `gldrst/preflight/`, `_diag/`, `_perm_probe_`, `_DIAGNOSTIC_ARTIFACT`, `platinum/firm/_meta/`, a first segment `qa/` | log, diagnostic, scratch, probe or QA output; no destination (R17, R18) |
| RC | a key that ends in `/` (a zero-byte directory marker) | zero-byte directory-marker key; no destination |

**Operational state -- MOVE, tier `state`** (R21; the 1b rows for `otp/state.json` and the trigger-mode files are the analogs):

| rule | the class | address(...) arguments |
|---|---|---|
| RS1 | `gold/.checkpoints/` | `advi`, `{F}`, `state`, `checkpoints`, `<seg1>`, object `<rest>` |
| RS2 | `silver/` files named `*manifest*.json` (not `.bak-`) | `advi`, `{F}`, `state`, `manifests`, `<file>` |
| RS3 | `status/` | `advi`, `{F}`, `state`, `status`, `<file>` |
| RS4 | a file whose name matches `_*COMPLETE*.json` or `*_complete.json`, or under `_silver_complete/`, `_complete/` or a `_meta/` dir | `{V}` (else `advi`), `{F}`, `state`, `complete`, `<seg1>`, object `<rest>` |
| RS5 | `orion/backfill_progress_*.json` | `orion`, `{F}`, `state`, `backfill-progress`, `<file>` |
| RS6 | `orion/rate_limit_state_*.json` | `orion`, `{F}`, `state`, `rate-limit`, `<file>` |
| RS7 | `orion/jwt/trigger-mode.json` | `orion`, `{F}`, `state`, `session`, `trigger-mode.json` |
| RS8 | `orion/browser-profile/`, `eclipse/browser-profile/` | the segment before `browser-profile`, `{F}`, `state`, `browser-profile`, `<file>` |
| RS9 | `gold/meta/pull-complete.json`, `gold/meta/pipeline-failed.json`, `gold/dispatch-lock.json`, `gold/meta/schemas/`, `gold/meta/valgate-baseline/` | `advi`, `{F}`, `state`, `meta`, `<seg1>`, object `<rest>` |
| RS10 | `forwardfill_v2/_retry_net/` | `blackdiamond`, `{F}`, `state`, `retry-net`, `<file>` |

**Ingest data -- HOME** (R4, R9; the 1b HOME row is the analog; `address()` returns an `opal-data-assets` address):

| rule | the class | address(...) arguments |
|---|---|---|
| RH1 | `smartx/raw/<t>/<date>/<file>` | `smartx`, `{F}`, `bronze`, `<t>`, `<date>`, object `<file>` |
| RH2 | `forwardfill_v2/<kind>/<file>`, `backfill_v2/<kind>/<file>` | `{V}`, `{F}`, `bronze`, `<kind>`, `<file>` |
| RH3 | `forwardfill_v2/<name>.xlsx` (a root file) | `{V}`, `{F}`, `bronze`, `transactions` if the name starts `TXN_`, else `unplaced`, `<file>`; a name that is not `TXN_*` is FAULT |
| RH4 | `bronze/<child>/...`, `silver/<child>/...` where `<child>` is a data directory (not a marker per RS4, not market-price silver below) | `{V}`, `{F}`, `bronze` or `silver` by the first segment, `<child>`, `<seg2>`, object `<rest>` |

**Served and analytical -- MOVE** (R5, R11, R12; the 1b `gold/` rows are the analogs):

| rule | the class | address(...) arguments |
|---|---|---|
| RG1 | `gold/<name>.json` (a root JSON file) | `advi`, `{F}`, `platinum`, `artifacts`, `<file>` (R12: served JSON is platinum whatever it was called) |
| RG2 | `gold/<name>.parquet` (a root parquet) | `advi`, `{F}`, `gold`, `<name>`, `<file>` |
| RG3 | `gold/<dir>/` whose sample is `*.json`, for `<dir>` in `advisors`, `clients`, `client_timeseries`, `partner_analytics`, `perf_history`, `snapshots`, `summary`, `filters`, `cohorts`, `nna`, `aua_certification`, `canonical/nna_validation` | `advi`, `{F}`, `platinum`, `<dir with / as ->`, `<seg1>`, object `<rest>` (omit object when `<rest>` is empty) |
| RG4 | `gold/<dir>/` whose sample is `*.parquet` named by a date, for `<dir>` in `holdings_lots`, `daily/positions`, `consolidated`, `timeseries/<t>` | `advi`, `{F}`, `gold`, `<dir with / as ->`, `date=<date>`, object `data.parquet` |
| RG5 | a root parquet under `gold/timeseries/` | `advi`, `{F}`, `gold`, `<name>`, `<file>` |
| RP1 | inf `platinum/clients/` outside `_quarantine_*` | the same destination the bd class `platinum/clients/` has in `mapping.json` (copy its `dest_pattern`; build with `address()`) |
| RI1 | `investor-reporting/<seg1>/...` | `irpt`, `{F}`, `platinum`, `investor-reporting`, `<seg1>`, object `<rest>` |

**Stay FAULT, with these named owners** (a class no rule above places, or one `address()` refuses, keeps its FAULT row; write
`fault_owner` as shown and the reason in words):

| the class | `fault_owner` | reason |
|---|---|---|
| market-price silver: `silver/historical_prices*.parquet`, `silver/historical_dividends.parquet`, `silver/interpolated_prices*`, `silver/prices/`, `canonical/silver/` | `1.0.0_SA_CTO~DELL1` | the {vendor} is not derivable from the key and is not the bucket's feed vendor |
| `lambda-deploy/`, `lambda-layers/`, `lambda-packages/` | `1.0.0_SA_CTO~DELL1` | Lambda deployment artifacts: R16 is not applied to them (PRD CONTRACTS); the home is not ruled |
| `smartx/jwt/`, any key whose basename is `current.json` under a `jwt/` dir | `1.0.0_SA_CTO~DELL1` | a live credential: moving it breaks the chain that refreshes it (FWD-8's class) |
| `scripts/`, a first segment `/` (leading-slash keys), `telemetry/` | `1.0.0_SA_CTO~DELL1` | code, an empty first segment no builder accepts, or runtime telemetry whose reader is unnamed |
| anything else no rule places | `1.0.0_SA_CTO~DELL1` | no repair rule places it |

### 1d. Re-gridding a MIXED class

A class the census marks MIXED (its `reason` in `mapping.json` begins `MIXED`), or one whose objects match two rules,
is split by a live read-only listing (`list_objects_v2` on that class's prefix, `Delimiter="/"` one level at a time) into
CHILD classes: one per sub-directory, one per root file, or one per group named by an `exclude_prefixes` list (for example
inf `platinum/clients/` = the child `platinum/clients/` with `exclude_prefixes ["platinum/clients/_quarantine_scope_bug_20260424/"]`
plus the child `platinum/clients/_quarantine_scope_bug_20260424/`). Each child is then worked by 1c.
- A child row carries `parent` (the census prefix it came from) and, when it excludes sub-prefixes, `exclude_prefixes`.
- `mapping_v2.json` has NO row for the parent; it has an entry in `regrids`:
  `{"bucket", "parent", "children": [prefixes], "parent_objects": <live count under the parent>,
  "children_objects": <sum over the children>, "listed_at": "<UTC ISO>"}`. The two counts MUST be equal.
- Never re-grid a class round 1 placed; only FAULT classes are split.

### 1e. Collisions

After the repair, group the MOVE and HOME rows by `(bucket, dest.source, dest.scope, dest.tier, dest.table)`. Every group
with two or more classes is a collision. For each, list both classes' keys (read-only), compute each key's destination key
(`dest_pattern` with the key's tail) and count the keys the two classes would write to the SAME destination key.
- Overlap 0: record `{"bucket","source","scope","tier","table","classes":[prefixes],"verdict":"merge","reason":"<why one
  table is right: same product, same tier, disjoint keys, counts printed>","overlap_keys":0}` in `collisions`.
- Overlap above 0: the classes cannot share the table. Make EVERY class of the group a FAULT row, `fault_owner`
  `1.0.0_SA_CTO~DELL1`, reason `destination-key overlap <n> of <m> keys with <the other class>`; they then leave the group.
  This applies to a class round 1 placed as much as to a new one: round 1's cot `gold/positions_cube/` and
  `gold/timeseries/positions_cube/` are the known case (342 of 342 keys shared), and both become FAULT rows.

## 2. FILE SHAPES

1. **`org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/mapping_v2.json`** (`indent=1`, `ensure_ascii=True`, LF):
   ```json
   {"census_listed_at": "<census.json listed_at, copied>", "supersedes": "mapping.json",
    "rows": [{"bucket", "prefix", "class", "disposition", "rule", "dest", "address", "dest_pattern"}],
    "regrids": [], "collisions": []}
   ```
   - One row per census class that round 1 placed (copied) or that you placed or left FAULT, and one per child class;
     a re-gridded parent has none.
   - `rule` quotes the repair rule id and its row (for example `RA: backup copy ... (R17, R18)`).
   - MOVE and HOME rows carry `dest` {source, scope, tier, table, partition, object?}, `address` (exactly `address()`'s
     output) and `dest_pattern`. RETIRE rows carry `reason`. FAULT rows carry `reason` and `fault_owner`.
   - There is NO new DECISION row: the two round-1 DECISION rows are copied; everything else is FAULT with an owner.
2. **`org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/MAPPING_TABLE_v2.md`**: counts per disposition with the census
   denominators (444 classes, 238,861 objects), then per bucket the classes you changed (prefix, disposition, rule), the
   remaining FAULT rows grouped by owner and reason, the regrids and the collisions with their overlap counts.

## 3. BOUNDS

1. AWS: read-only `list_objects_v2` on `opal-data-bd`, `opal-data-inf`, `opal-data-cot` (re-grid and overlap) by the
   box's own identity, with `boto3.client("s3")`. No write, no delete, no other service.
2. **CLIENT DATA:** an entity id inside a key is the only client datum you handle; in `MAPPING_TABLE_v2.md` write `{id}`.
3. Only the files in section 4 change. Never edit `census.json`, `mapping.json`, the checks, the PRD or the builders.
4. No non-ASCII; LF line endings.
5. A rule you cannot apply as written is a FAULT row with its reason, never a reinterpretation. If an item cannot be met
   within your paths, file a surprise row and stop on that criterion.

## 4. SURFACES

<paths>
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/mapping_v2.json
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/MAPPING_TABLE_v2.md
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~4/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/census.json` and `mapping.json`, `lib/opal_naming.py`,
`org/standards/NAMING_SCHEMA.json`, `org/missions/D14/LGIC/LGIC_NAMING/deliverables/LEGACY_SERVED_PATHS.json`,
`infra/logic/registry/`, the PRD, and the issuer's checks under
`org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round2/checks/` (never edit them).

## 5. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~4/ADVI_FIRMBKTS.TO-FB-e-1.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-e-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round2/checks/r2_mapping.py" --arms structure; echo "exit=$?"</invocation><expect>ROUND 2 MAPPING STRUCTURE: 5 of 5 arms</expect></criterion>
  <criterion id="AC2" cell_refs="FB-e-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round2/checks/r2_mapping.py" --arms repair; echo "exit=$?"</invocation><expect>ROUND 2 MAPPING REPAIR: 4 of 4 arms</expect></criterion>
</proof_of_spec>

AC1 is the seam against the real neighbour: it rebuilds every MOVE and HOME address through `address()` and refuses one
typed by hand, and its fifth arm is the difference control (round 1's placed rows are unchanged). Both invocations are
bounded: they read three JSON files and call the builder; neither calls AWS.

## 6. WHEN YOU ARE DONE

Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~4/ADVI_FIRMBKTS.TO-FB-e-1.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance**, only when AC1 and AC2 pass. A row
id on this project carries the dell1 infix and your slot: `ADVI_FIRMBKTS-D1-W4-S<k>`, with `surfaced_at` from
`date -u +%FT%TZ` at filing. Report once: the files (one line each), counts per disposition with the census
denominator, the FAULT rows remaining by owner, the regrids and collision verdicts, the output lines of AC1 and AC2,
the commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 2 over PRD v1.3 @30d612d5e5 (ADMITTED), decomposition v2, issuer `2.0.0_SA_COO~B1`. The repair
rules are the issuer's rulings under the CTO's "no worker decides them" (ROUND_ANALYSIS.round1.md section 2): every class
a rule does not place stays FAULT with `1.0.0_SA_CTO~DELL1` as its named owner (the CTO's "0 FAULT or each remaining
one with a named owner"). RETIRE is a classification, not a removal. The 2 DECISION classes the analysis names are the
two round-1 DECISION rows (FWD-7, FWD-8); no worker adds a third.

# pipeline-override: the one refusal is LIMB PRD_HEADER.fabric='laptop' vs the register's 'dell1'. The register row is the authority since 1.0.0_SA_CTO's L3 re-placement @8afcb0f851; the PRD header repair is the CTO's. Every other limb passed in the issuer's dry run.
<status>pending</status>
<round>2</round>
<to_id>ADVI_FIRMBKTS.TO-FB-e-1</to_id>
<slot>~4</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
