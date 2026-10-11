# MDPF_CANON task order -- `CN-e-1` -- THE AUM-TIMESERIES INSTRUMENT READS THE CANONICAL GOLD ARTIFACT (M4, third slice, FWD-5)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_CANON/decompositions/MDPF_CANON_DECOMP.md</decomp_doc>
<owned_cells>CN-e-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_MDPF_CANON~15</issued_to>
<issued_by>2.0.0_SA_COO~D1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence is added or changed; the script is run on demand from a repo checkout and nothing in the dispatch chain or the Lambda package calls it (measured: no caller).
comp-iam: DECLARED-NOT-APPLICABLE -- reads only, one global partition at the builder's address; no grant is added.
comp-adversary: RUN by the issuer (2.0.0_SA_COO~D1) on DELL1 at box/dell1 -- r5_cn_e_1.py reader 0 of 5, seam 0 of 1 and r5_cn_e_1_census.py 1 of 4 at base (arm C4 is a control); a reference implementation reads 5 of 5, 1 of 1 (2958 cells DELTA=0 on the real partition) and 4 of 4 (the arms can pass).
EGRESS CLASS, declared: NONE (the worker writes no AWS).
</preflight>

## 1. THE CELL -- `CN-e-1` (round 5, decomposition v5)

`data/mdpf/scripts/gold/dim_mdpf_aum_timeseries.py` is a read-only identity instrument (read its module docstring first): `main` loads the global
aggregate, builds the served-shape aum-timeseries document with `build_aum_timeseries`, validates its internal identity, and prints. Its staging
write is RETIRED and `--upload` only logs a SKIP. It still reads the aggregate from the OLD staging tree through `load_aggregate()`, key
`AGG_GLOBAL_KEY = "gold/mdpf_revamp/global/aggregate_aua_timeseries.json"`. The same artifact is written, one partition per day, at the builder's
address. Repoint the instrument to read that, and change nothing else about what it computes. It moves no served output: it prints and exits.

The builder's address for the global scope and one day is wrapped by a sibling module in the same folder, `mdpf_gold_parquet.py`
(`partition_uri(scope, artifact, date)`; read it, do NOT edit it):

```
partition_uri("global", "aggregate_aua_timeseries", "2026-10-08")
  -> s3://opal-data-mdpf/mdpf/global/gold/aggregate_aua_timeseries/date=2026-10-08/data.parquet      (the builder's output; type no bucket or key)
```

The parquet is WIDE: one row per axis date (493 rows at 2026-10-08, the newest partition carries the whole axis). Columns: `date`, flat series, and
one column per nested series named by joining keys with a dot, e.g. `by_model.opal_short_term.model_value` and
`by_model.opal_short_term.account_count`. A null is NaN. There is NO `cohort_class` column.

What `build_aum_timeseries(agg)` consumes, and what your loader must therefore return:

```
{"dates": ["2024-11-01", ..., "2026-10-08"],                       # str(x)[:10] of the date column, in row order
 "by_model": {"<model_key>": {"cohort_class": "model",             # from the producer's registry, see step 4
                              "model_value":   [100.0, None, ...], # NaN -> None, else float
                              "account_count": [3, None, 5, ...]}},# NaN -> None, else int
 "gold_partition": "2026-10-08"}                                   # the partition date read
```

Steps (the file keeps its line endings; read it first, and the sibling `mdpf_revamp_count_source_audit.py` whose `latest_gold_artifact` is the
pattern this cell follows):

1. Imports. Add `import io`, `import re`, `from urllib.parse import urlsplit` and `import pandas as pd`; and, in the style of the other
   sibling imports in the repo's gold scripts, `from mdpf_gold_parquet import partition_uri  # noqa: E402` and
   `from mdpf_revamp_model_crosswalk import entry_for_key  # noqa: E402`. (The script is run from a checkout, never on the runner.)
2. Constants. Delete `AGG_GLOBAL_KEY` and `STAGING_KEY`. Leave `SERVED_BUCKET`, `SERVED_KEY` and `S3_REGION` as they are. Add
   `GOLD_ARTIFACT = "aggregate_aua_timeseries"`, `GOLD_SCOPE = "global"` and
   `_WIDE = re.compile(r"^by_model\.(?P<key>.+)\.(?P<field>model_value|account_count)$")`.
3. Add `latest_gold_aggregate() -> dict` (and a small `_split_uri(uri) -> (bucket, key)` with `urlsplit`):
   - list the global scope's dated partitions: take the bucket and key from `partition_uri(GOLD_SCOPE, GOLD_ARTIFACT, "2000-01-01")`, cut the key
     at `"/date="` and add a trailing `/` for the listing prefix, list it with `Delimiter="/"`, and collect the `date=<D>` tokens;
   - keep tokens that start with `20`, take the greatest, and RAISE `SystemExit` naming the scope if there is none (no fallback to any other
     place, ever);
   - read that partition's `data.parquet` from `partition_uri(GOLD_SCOPE, GOLD_ARTIFACT, <D>)` into a DataFrame and build the dict above.
   - ALL S3 access goes through the file's existing `_s3()` (the issuer's check replaces it with a fake; a direct `boto3.client` call would reach
     the network and fail the offline arms).
4. `cohort_class` comes from the producer's own registry, never from the parquet: for each `by_model` key set
   `node["cohort_class"] = entry_for_key(key).cohort_class`, and `None` where the registry does not know the key (`UnknownModelError`). This is
   the one substitution this cell makes and the CVO grades it: the FATAL guard in `build_aum_timeseries` that reads `cohort_class` keeps its meaning
   and its raise. Do not edit `build_aum_timeseries`.
5. `load_aggregate()` returns `latest_gold_aggregate()`. `load_served()` is unchanged (it reads the served comparator).
6. Remove EVERY remaining occurrence of the text `gold/mdpf_revamp` in the file, in code, log strings, help text and comments (the module
   docstring's last line names the old staging object, the `--upload` help and the SKIP log name it). Say "the gold tier" instead and keep the
   retirement note's meaning. After your edit `grep -c "gold/mdpf_revamp" <the file>` must print 0.
7. Do not change anything else: `MODEL_ORDER`, `SERVED_MODEL_NAME`, `build_aum_timeseries`, `validate_internal`, `verify_field_identity`,
   `self_test`, the printed lines and the exit codes. Run `python <the file> --self-test` yourself and report its result (not a criterion).
8. **The census.** `org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~4/READER_CENSUS.md` (a prior worker's deliverable, in your
   `<paths>`) has two rows that name this script. Edit only these two rows:
   - the row whose first cell begins `gold/mdpf_revamp/ -- dim_mdpf_aum_timeseries.py` (about line 15): replace it with
     `| gold tier at the builder address -- dim_mdpf_aum_timeseries.py (repointed by CN-e-1; reads the newest global aggregate_aua_timeseries partition through partition_uri; its staging write stays retired) | reader | data/mdpf/scripts/gold/dim_mdpf_aum_timeseries.py:<L1>; data/mdpf/scripts/gold/dim_mdpf_aum_timeseries.py:<L2> | live |`
     where `<L1>` is the line of `def latest_gold_aggregate` and `<L2>` the line of the `partition_uri(GOLD_SCOPE, GOLD_ARTIFACT, latest)`-style
     read, in the file AS YOU LEAVE IT. The new row must not contain the text `gold/mdpf_revamp/`;
   - the row whose first cell begins `json/portfolios/aum-timeseries.json -- dim_mdpf_aum_timeseries.py SERVED_KEY` (about line 53): its first
     citation `...dim_mdpf_aum_timeseries.py:56` follows the line of `SERVED_KEY = ...` in the file as you leave it. Change only that number.
   If the census's own header counts rows, leave the count (one row is replaced, none added).

## 2. BOUNDS

1. **No AWS write of any kind**: no put, no copy, no delete, no invoke, no apply. Read-only `get`/`head`/`list` is allowed (the seam arm of the
   issuer's check reads one partition and the old JSON). No install, no push. REFUSE, do not rescue.
2. Only the files in section 3 change (plus your deliverables and the surprise channel). Do not edit `mdpf_gold_parquet.py`,
   `mdpf_revamp_model_crosswalk.py`, `lib/opal_naming.py` or the issuer's checks.
3. **Never** (PRD DEC-14) add a fallback to the old tree, a dual read, a comparison against the old JSON, or any standing comparator: the
   instrument reads the canonical artifact only. The old tree and its writers are not touched (their retirement is another cell).
4. **Every address comes from the builder** through `partition_uri`. Type no bucket and no key. A refusal from a gate (the commit-time naming
   limb, or `ds-precommit` over a cross-firm reference) is a BLOCKING row with the gate's text and a stop on that criterion: never a workaround.
5. **CLIENT DATA:** the instrument prints per-model aggregates as it does today; never print an account id.
6. No non-ASCII. Use the Edit tool. Keep each file's line endings as you find them (read them first).
7. If an item cannot be met within your paths, file a row and stop on that criterion.

## 3. SURFACES

<paths>
data/mdpf/scripts/gold/dim_mdpf_aum_timeseries.py
org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~4/READER_CENSUS.md
org/missions/D8/MDPF/MDPF_CANON/task-orders/MDPF_CANON.TO-CN-e-1.aum-timeseries-reads-the-gold-artifact.md
org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~15/
org/missions/D8/MDPF/MDPF_CANON/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository, in particular `data/mdpf/scripts/gold/mdpf_gold_parquet.py` (`partition_uri`),
`data/mdpf/scripts/gold/mdpf_revamp_model_crosswalk.py` (`entry_for_key`), the sibling loader named in the steps, and the issuer's checks
`org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round5/checks/r5_cn_e_1.py` and `r5_cn_e_1_census.py` (never edit them; read what
each arm asserts).

## 4. PROOF OF SPEC (literal; timeout 120 per invocation)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CN-e-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round5/checks/r5_cn_e_1.py" reader; echo "exit=$?"</invocation><expect>ROUND 5 READER: 5 of 5 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="CN-e-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round5/checks/r5_cn_e_1.py" seam; echo "exit=$?"</invocation><expect>ROUND 5 SEAM: 1 of 1 arms -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="CN-e-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round5/checks/r5_cn_e_1_census.py"; echo "exit=$?"</invocation><expect>ROUND 5 CENSUS: 4 of 4 arms -- and exit=0</expect></criterion>
  <criterion id="AC4" cell_refs="CN-e-1" judgment="true"/>
</proof_of_spec>

AC4 is JUDGMENT, graded at the round-5 close (never self-graded): `/seams` on the instrument-to-artifact seam, grounded on the artifact at the
builder's address -- MECHANICAL (the instrument run end to end with `--out` reads the newest global partition and prints its identity line),
DECLARATIVE (the module docstring, the log strings, the help text and the census row name the gold tier, not the staging tree), SEMANTIC (the
document built from the gold partition equals the document built from the legacy staging JSON at the same vintage, cell for cell, and the
`cohort_class` the guard reads is the registry's, not the parquet's).

## 5. WHEN YOU ARE DONE

Write the instance at
`org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~15/MDPF_CANON.TO-CN-e-1.aum-timeseries-reads-the-gold-artifact.proof_of_spec.json`
(beside the order's own file stem, which is the name the pipeline gate searches for), with AC4 UNVERIFIABLE-BY-INSTRUMENT and status_reason
"graded at the round-5 close". **Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the order file is in your
paths), and only when every mechanical criterion passes.

A row id on this project carries the dell1 infix: `MDPF_CANON-D1-W15-S<k>`, with `surfaced_at` taken from `date -u +%FT%TZ` at filing.
Report once: the diff (one line per file), the output line of every criterion, the census rows before and after, the commit hash, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 5 = `org/missions/D8/MDPF/MDPF_CANON/ledger/ROUND_ANALYSIS.round4.md` @c902dcb1b5 section 3 item 5 (M4, the next reader).
- **The census row:** `READER_CENSUS.md` row 15, `gold/mdpf_revamp/ -- dim_mdpf_aum_timeseries.py` (reader; `dim_mdpf_aum_timeseries.py:53,54,291`).
- **Why this one, said plainly:** the candidate the analysis expected, `verify_mdpf_revamp_conditions.py`, cannot be repointed without a logic
  change: four of the cells its conditions read (`cohort_provenance`, `meta.latest_cross_section.partner_custody_total`,
  `by_model.<sma>.count_as_of`, `meta.count_coverage_end`) are not columns of the wide parquet at the builder's address, and adding them is a change
  to the one gold writer `mdpf_gold_parquet.py` (its `write_partition` returns "conflict" on an existing date whose bytes differ). That is the CTO's
  to rule, not a cell: `deliverables/2.0.0_SA_COO~D1/round5/CN_E_1_CANDIDATE_READ.md`. Every other remaining reader feeds a served key and takes a
  never-widen pair. This instrument is the one reader that moves no served output; it is retired-as-writer and read-only, so it is also the
  smallest honest supply, and whether a never-canonical instrument deserves a repoint at all versus deletion is named to the CTO in the round-5
  message, not decided here.
- **Measured at the cut (issuer, 2026-10-11):** the loader, run against the real global partition (2026-10-08, 493 rows), builds a document equal to
  the one built from the staging JSON, 2958 of 2958 cells, 5 models, DELTA=0.
- **The one named substitution:** `cohort_class` has no parquet column; the registry supplies it (step 4) and AC4 grades it.
- **Hazards:** none expected (`global` only, no firm bucket literal; `partition_uri` types none). The naming gate's two WARNs on CN-d-4 came from
  firm-name literals, which this cell does not carry.
- **Risk and class:** LOCAL (no `infra/` path, no deploy verb; the file is not shipped in the Lambda package or the runner chain, measured: no
  caller). `worker-light`: about 45 lines added, 8 changed.
- **Fanout:** one cell, one chain, slot ~15; independent of the CloudOps orders. Base box/dell1.

<status>pending</status>
<round>5</round>
<to_id>MDPF_CANON.TO-CN-e-1</to_id>
<slot>~15</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
