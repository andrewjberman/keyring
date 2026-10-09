# ADVI_FIRMBKTS task order -- `FB-t-2` -- THE MAPPING TABLE AND THE READING LIST

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP.md</decomp_doc>
<owned_cells>FB-t-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_FIRMBKTS~1</issued_to>
<issued_by>2.0.0_SA_COO~F1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- thread round; no cron, rule, schedule or cadence is added or changed.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change and no AWS act; the cell reads census.json and the builders.
comp-adversary: RUN by the issuer (2.0.0_SA_COO~F1) on dell1 -- r1_mapping.py 0 of 5 at base (files absent); 5 of 5 on a reference table over the issuer's reference census; 3 of 5 with one address typed by hand (negative control: the builder arm and the reading-list arm both refuse it).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `FB-t-2` (round 1, THE THREAD for FWD-1; decomposition v1)

This is the thread's second and third hops. You place every class of the census by ONE table, build each new location
with the builders, and write the list of locations two other workers will read. `FB-t-1` (earlier in your queue) wrote
the census: `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/census.json`. Read it, never edit it.

FWD-2's rule, which binds this table: *every piece lands in exactly one destination and nothing is left unplaced, and
anything the table cannot place is a fault in the table rather than a decision for whoever is holding it.* You apply
the table below; you do not decide.

### 1a. The key string (ruled; PRD CONTRACTS)

`{source}/{scope}/{tier}/{table}/{partition}`, the bucket as its container and the object as its leaf.
- `{source}` is the PRODUCING system: a product for derived tiers (`advi`, `irpt`, `mdpf`), a vendor for pass-through
  data (`blackdiamond`, `schwab`, `orion`, `eclipse`, `smartx`).
- `{scope}` in a firm bucket is that bucket's own firm in the LONG form: `opal-data-bd` -> `49financial`,
  `opal-data-inf` -> `inflection`, `opal-data-cot` -> `cottonwood`.
- `{tier}` in a firm bucket is `gold`, `platinum`, `state` or `code`. Bronze and silver never live in a firm bucket:
  they go HOME to `opal-data-assets`, and `address()` homes them there.
- `{partition}` is `date=YYYY-MM-DD`, a named leaf, or an entity partition `{entity}={id}` (`org/standards/NAMING_SCHEMA.json`
  `key.partition`). **A LEGACY served path keeps its bytes** below `{source}/{scope}/platinum/` (the table, a bare
  entity-id segment, the file name; `key.legacy_served_path`), and a path is legacy only if
  `org/missions/D14/LGIC/LGIC_NAMING/deliverables/LEGACY_SERVED_PATHS.json` lists it.
- Code: `{source}/{scope}/code/{built_tier}/{file}` (`key.code`).
- **Every new location comes from `lib/opal_naming.py` `address(source, scope, tier, table, partition, object=None)`,
  never typed.** A builder refusal is a FAULT row (1c), never a hand-spelled string.

### 1b. The table (brief IV.6 restated in the five segments; the PRD ratifies it as FWD-2's rule, DEC-2)

| legacy class (in `opal-data-{bd,inf,cot}`) | IV.3 class | disposition | destination | rule |
|---|---|---|---|---|
| `platinum/**` | a | MOVE | `advi/{firm}/platinum/**` (same tail) | R6 |
| `gold/artifacts/**.json`, `gold/entities/**.json`, `gold/platinum/**`, `gold/views/*.json` | a | MOVE | `advi/{firm}/platinum/{artifacts,entities,firm,views}/**` | R12: served JSON is platinum whatever it was called |
| `gold/canonical/{t}/...`, `gold/timeseries/{t}/...`, `gold/dimensions/*`, `gold/holdings/*`, `gold/lots/*`, `gold/positions_cube/*`, `gold/views/*.parquet`, `gold/cache/*`, `gold/account_gains/*` | b | MOVE | `advi/{firm}/gold/{t}/date={D}/data.parquet` | R5, R11 |
| `gold/_state/**`, `gold/_parity/**`, `gold/meta/*_watermark.json`, `gold/manifests/**`, `gold/canonical/watermarks.json`, `silver/meta/gap_manifest.json` | c | MOVE | `advi/{firm}/state/{watermarks,parity,manifests}/**` | R21 |
| `config/*` | c | MOVE | `advi/{firm}/state/config/*` | R21 |
| `otp/state.json` (inf) | c | MOVE | `orion/inflection/state/otp/state.json` | R21 |
| `blackdiamond/{49f,cot}/session-trigger-mode.json` | c | MOVE | `blackdiamond/{firm}/state/session/trigger-mode.json` | R21 |
| `gold/eclipse/{*}/_meta/gold_complete.json`, `silver/eclipse/{*}/_meta/silver_complete.json` | c | MOVE | `eclipse/inflection/state/complete/**` | R21 |
| `bronze/**`, `silver/**`, `schwab/silver/**` | d | HOME | `opal-data-assets/{vendor}/{firm}/{bronze,silver}/**` | R4, R9 |
| `code/gold/**` (and `code/{bronze,silver}/**`) | f | MOVE | `{source}/{firm}/code/{built_tier}/{file}` | R16, `key.code` |
| `gold/validation/**`, `gold/holdings_lots_v2_dryrun/**`, `gold/timeseries/holdings_lots_shadow/**`, dated singletons | e | RETIRE | none | R17, R18 (removal is a later cell's, after a reader census) |
| `gold/meta/pipeline-complete.json` (inf) | - | DECISION | none; `decision_ref` `FWD-7` | Door 6, ruled by Andrew 2026-09-14 ~13:4xZ: retired with its watcher |
| `orion/jwt/current.json` (inf) | - | DECISION | none; `decision_ref` `FWD-8` | B2, ruled by Andrew 2026-09-14 ~13:4xZ: stays; the bucket stays open for it |

A class matches a row by what it IS, not only by its first segment (IV.3: "move gold is not a move, it is a sort").
Investor-reporting keys (`investor-reporting/...`) are `irpt`'s; a product slice keeps its product as `{source}`.

### 1c. What to build

1. **`org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/mapping.json`**, exactly this shape (AC1 binds it):
   ```json
   {"census_listed_at": "<census.json listed_at, copied>",
    "rows": [{"bucket": "opal-data-bd", "prefix": "<census class prefix>", "class": "a",
              "disposition": "MOVE", "rule": "<the 1b row's legacy cell and rule, quoted>",
              "dest": {"source": "advi", "scope": "49financial", "tier": "platinum", "table": "...", "partition": "...", "object": "..."},
              "address": "<address(...) for the class's sample_key>",
              "dest_pattern": "<the class's destination with {placeholders}>",
              "reading_ids": {"canonical": "<id>", "legacy": "<id>"}}]}
   ```
   - One row per census class, every class, nothing extra.
   - `disposition` is one of `MOVE`, `HOME`, `RETIRE`, `DECISION`, `FAULT`.
   - MOVE and HOME rows carry `dest`, `address`, `dest_pattern` and `reading_ids`. `dest` is built for the class's
     `sample_key` (its date, its entity id, its file), and `address` is exactly what `address()` returns for it (`object`
     may be omitted when the partition is the leaf).
   - RETIRE rows carry `reason`. DECISION rows carry `decision_ref`.
   - **FAULT** is a class no row of 1b places, or one `address()` refuses. File ONE surprise row that lists every FAULT
     class with the reason, and set each FAULT row's `fault_row` to that row's id. Logs, backups, rollback copies and
     leading-slash keys are FAULT unless a 1b row places them. Never stretch a row to fit.
2. **`org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/reading_list.json`**: `{"locations": [{"id": "...", "location": "..."}]}`.
   - For every MOVE and HOME row, two entries: the canonical `address` (`reading_ids.canonical`) and the legacy
     `s3://<bucket>/<sample_key>` (`reading_ids.legacy`).
   - Each entry carries ONLY `id` and `location`. Ids are opaque: 8 random hex characters (no `/`, never the word `opal`).
   - Shuffle the list with a fixed seed so the two arms are interleaved. Nothing in the list says which arm an entry is.
3. **`org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/MAPPING_TABLE.md`**: the human view. Counts per disposition with the
   census denominator, then one table per bucket (class, IV.3 class, disposition, `dest_pattern`, rule), then the FAULT
   classes and their row id.

## 2. BOUNDS

1. **No AWS act** of any kind; the census is your only view of the buckets.
2. **CLIENT DATA:** an entity id inside a sample key is the only client datum you handle. It appears in `mapping.json`
   and `reading_list.json` only as part of a key; in `MAPPING_TABLE.md` write `{id}`.
3. Only the files in section 3 change. Never edit `census.json`, the checks, the PRD or the builders.
4. No non-ASCII; LF line endings; JSON written with `indent=1` and `ensure_ascii=True`.
5. If an item cannot be met within your paths, file a row and stop on that criterion.

## 3. SURFACES

<paths>
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/mapping.json
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/reading_list.json
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/MAPPING_TABLE.md
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~1/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/census.json`, `lib/opal_naming.py`,
`org/standards/NAMING_SCHEMA.json`, `org/missions/D14/LGIC/LGIC_NAMING/deliverables/LEGACY_SERVED_PATHS.json`,
`infra/logic/registry/` (read only), the PRD and the brief (IV.3, IV.5, IV.6), and the issuer's checks under
`org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~F1/round1/checks/` (never edit them).

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
  <criterion id="AC1" cell_refs="FB-t-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~F1/round1/checks/r1_mapping.py"; echo "exit=$?"</invocation><expect>ROUND 1 MAPPING: 5 of 5 arms -- and exit=0</expect></criterion>
</proof_of_spec>

AC1's builder arm is the seam probe against the real neighbour: it rebuilds every MOVE and HOME address through
`address()` and refuses one typed by hand.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~1/ADVI_FIRMBKTS.TO-FB-t-2.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance**, only when AC1 passes. A row id
on this project carries the dell1 infix: `ADVI_FIRMBKTS-D1-W1-S<k>`, with `surfaced_at` from `date -u +%FT%TZ` at
filing. Report once: the files (one line each), the counts per disposition with the census denominator, the FAULT row
id, the output line of AC1, the commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 1 = THE THREAD (FWD-1) over PRD v1.3 @30d612d5e5 (ADMITTED). The PRD's two HELD families
(entity-keyed served files, code) are placed because LGIC_NAMING ruled S6/S7/S8 at v1.3 (L5_FACTS section 2); round 1
writes no object. Spawned in slot ~1 by continuing the FB-t-1 worker.

# pipeline-override: the one refusal is LIMB PRD_HEADER.fabric='laptop' vs the register's 'dell1'. The register row is the authority since 1.0.0_SA_CTO's L3 re-placement @8afcb0f851; the PRD header repair is the CTO's (msg 3113: a PRD commit is refused until it gains a KEY SURFACES section). Every other limb passed in the issuer's dry run.
<status>pending</status>
<round>1</round>
<to_id>ADVI_FIRMBKTS.TO-FB-t-2</to_id>
<slot>~1</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
