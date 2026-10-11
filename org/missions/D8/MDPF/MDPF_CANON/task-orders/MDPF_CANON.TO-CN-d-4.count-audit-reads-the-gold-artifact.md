# MDPF_CANON task order -- `CN-d-4` -- THE COUNT-SOURCE AUDIT READS THE CANONICAL GOLD ARTIFACT (M4, second slice, FWD-5)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_CANON/decompositions/MDPF_CANON_DECOMP.md</decomp_doc>
<owned_cells>CN-d-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_MDPF_CANON~13</issued_to>
<issued_by>2.0.0_SA_COO~D1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence is added or changed; the audit is run on demand from a repo checkout and no scheduler calls it (measured: no caller in dispatch, the Lambda package or .tools).
comp-iam: DECLARED-NOT-APPLICABLE -- reads only; the audit's profile reads the firms' gold buckets today (measured by the issuer, list and get on one partition each); no grant is added.
comp-adversary: RUN by the issuer (2.0.0_SA_COO~D1) on DELL1 at box/dell1 -- r4_cn_d_4.py reader 0 of 3 and seam 0 of 1 at base; a reference tree reads reader 3 of 3 and seam 2 of 2 (the arms can pass; the seam arm reads DELTA=0 on 3388 cells per firm).
EGRESS CLASS, declared: NONE (the worker writes no AWS).
</preflight>

## 1. THE CELL -- `CN-d-4` (round 4, decomposition v4)

`data/mdpf/scripts/gold/mdpf_revamp_count_source_audit.py` is the standing count-axis audit (read its module docstring first). It reads each
firm's served-shape artifact from the OLD staging tree, `gold/mdpf_revamp/{firm}/aggregate_aua_timeseries.json` (constant `REVAMP_KEY`, used
at the two audit legs `audit_inflection` and `audit_49f`), and lists that tree's top level in `unaudited_firms()`. The same artifact is now
written, one partition per day, at the builder's address. Repoint the audit to read that, and nothing else. The audit moves no served output:
it prints and exits.

The builder's address for one firm and day is already wrapped by a sibling module in the same folder, `mdpf_gold_parquet.py`
(`partition_uri(scope, artifact, date)` and `FIRM_SCOPES`; read it, do NOT edit it):

```
partition_uri("inflection", "aggregate_aua_timeseries", "2026-10-08")
  -> s3://opal-data-inflection/mdpf/inflection/gold/aggregate_aua_timeseries/date=2026-10-08/data.parquet
```

The parquet is WIDE: one row per axis date. Columns: `date`, flat series such as `non_model_aua`, and one column per nested series named
by joining keys with a dot, e.g. `by_model.opal_short_term.account_count`. The NEWEST `date=` partition carries the whole axis up to that
day (484 rows at 2026-10-08). A null is NaN.

What the two audit legs consume, and what your loader must therefore return:

```
{"dates": ["2025-...", ..., "2026-10-08"],                       # str(x)[:10] of the date column, in row order
 "by_model": {"<model_key>": {"account_count": [3, None, 5, ...]}},   # one entry per by_model.<key>.account_count column; NaN -> None; else int
 "gold_partition": "2026-10-08"}                                  # the partition date read
```

Steps (the file keeps its LF line endings; read it first):

1. Imports. Add `import re` and `from urllib.parse import urlsplit`, and, beside the existing `from mdpf_revamp_model_crosswalk import (...)`
   line and in the same style, `from mdpf_gold_parquet import FIRM_SCOPES, partition_uri  # noqa: E402`. (That module puts the repo root on
   `sys.path` and imports the builder itself; the audit is run from a checkout, never on the runner.)
2. Constants. Delete `REVAMP_KEY`. Leave `SERVED_KEY` as it is. Add `GOLD_ARTIFACT = "aggregate_aua_timeseries"` and
   `_WIDE_COUNT = re.compile(r"^by_model\.(?P<key>.+)\.account_count$")`.
3. Add `latest_gold_artifact(firm: str) -> dict` (and a small `_split_uri(uri) -> (bucket, key)` using `urlsplit`):
   - list the firm's dated partitions: take the bucket and key from `partition_uri(firm, GOLD_ARTIFACT, "2000-01-01")`, cut the key at
     `"/date="` and add a trailing `/` for the listing prefix, and list it with `Delimiter="/"`, collecting the `date=<D>` tokens;
   - keep tokens that start with `20`, take the greatest, and RAISE `SystemExit` with a message naming the firm if there is none (no
     fallback to any other place, ever);
   - read that partition's `data.parquet` from `partition_uri(firm, GOLD_ARTIFACT, <D>)` into a DataFrame and build the dict above.
   - ALL S3 access goes through the file's existing `_s3()` (the issuer's check replaces it with a fake; a direct `boto3.client` call would
     reach the network and fail the offline arms).
4. In `audit_inflection()` and `audit_49f()`, replace the `art = json.loads(_s3().get_object(Bucket=ASSETS_BUCKET, Key=REVAMP_KEY...)...)`
   statement with `art = latest_gold_artifact("inflection")` and `art = latest_gold_artifact("49financial")`. The rest of each leg is unchanged.
5. `unaudited_firms()`: it returns the firms that no audit leg covers. Its body becomes
   `sorted(set(FIRM_SCOPES) - AUDITED_FIRMS - set(DERIVED_SEGMENTS))` (the registry's mdpf firm scopes: 49financial, inflection, cottonwood; the
   result today is `["cottonwood"]`, the same finding the audit has always printed). Reword its docstring.
6. Remove EVERY remaining occurrence of the text `gold/mdpf_revamp`, in code, log strings and comments (the log line at the end of the
   firm-coverage block and the comment above `AUDITED_FIRMS` name it). Say "the gold tier" instead. After your edit
   `grep -c "gold/mdpf_revamp" <the file>` must print 0.
7. Do not change anything else: every printed line, the `--json` summary keys, the exit codes, the eclipse and roster reads,
   `ROSTER_MODEL_NAME`, `AUDITED_FIRMS`, `DERIVED_SEGMENTS`, `FRONTIER_EXCLUDED_REASON`.

Two measured facts so you do not "fix" them: (a) the 49financial parquet carries one `by_model` key (`tax`) that the old staging JSON did not;
`audit_49f` already skips a key with no `ROSTER_MODEL_NAME` entry, so no logic change is needed. (b) The inflection parquet carries the
same seven keys as the old JSON.

## 2. BOUNDS

1. **No AWS write of any kind**: no put, no copy, no delete, no invoke, no apply. Read-only `get`/`head`/`list` is allowed (the seam arm
   of the issuer's check reads two partitions and the old JSON). No install, no push. REFUSE, do not rescue.
2. Only the file in section 3 changes (plus your deliverables and the surprise channel). Do not edit `mdpf_gold_parquet.py`,
   `lib/opal_naming.py` or the issuer's checks.
3. **Never** (PRD DEC-14) add a fallback to the old tree, a dual read, a comparison against the old JSON, or any standing comparator: the
   audit reads the canonical artifact only. The old tree and its writers are not touched (their retirement is another cell).
4. **Every address comes from the builder** through `partition_uri`. Type no bucket and no key. A refusal from a gate (the commit-time naming
   limb, or `ds-precommit` over a cross-firm reference) is a BLOCKING row with the gate's text and a stop on that criterion: never a
   workaround.
5. **CLIENT DATA:** the audit prints per-model account counts as it does today; never print an account id or a dollar figure.
6. No non-ASCII. Use the Edit tool. Keep the file's LF endings.
7. If an item cannot be met within your paths, file a row and stop on that criterion.

## 3. SURFACES

<paths>
data/mdpf/scripts/gold/mdpf_revamp_count_source_audit.py
org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~13/
org/missions/D8/MDPF/MDPF_CANON/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository, in particular `data/mdpf/scripts/gold/mdpf_gold_parquet.py` (`partition_uri`, `FIRM_SCOPES`, `records_for` for
the row shape), `lib/opal_naming.py` (`address`), and the issuer's check
`org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round4/checks/r4_cn_d_4.py` (never edit it; read what each arm asserts).

## 4. PROOF OF SPEC (literal; timeout 120 per invocation)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CN-d-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round4/checks/r4_cn_d_4.py" reader; echo "exit=$?"</invocation><expect>ROUND 4 READER: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="CN-d-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round4/checks/r4_cn_d_4.py" seam; echo "exit=$?"</invocation><expect>ROUND 4 SEAM: 2 of 2 arms -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="CN-d-4" judgment="true"/>
</proof_of_spec>

AC3 is JUDGMENT, graded at the round-4 close (never self-graded): `/seams` on the audit-to-artifact seam, grounded on the artifact at the builder's
address -- MECHANICAL (the audit run end to end, `--firm all`, reads the newest partitions and prints its coverage and disagreement lines),
DECLARATIVE (the module docstring, the log strings and the census row name the gold tier, not the staging tree), SEMANTIC (the audited-date
denominators and DISAGREEMENT counts it prints for inflection and 49financial equal those of the run against the old JSON at the same
vintage).

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~13/MDPF_CANON.TO-CN-d-4.count-audit-reads-the-gold-artifact.proof_of_spec.json`, with AC3
UNVERIFIABLE-BY-INSTRUMENT and status_reason "graded at the round-4 close". **Flip this order's `<status>` to `complete` in the SAME
commit as your proof instance**, and only when every mechanical criterion passes.

A row id on this project carries the dell1 infix: `MDPF_CANON-D1-W13-S<k>`, with `surfaced_at` taken from `date -u +%FT%TZ` at
filing. Report once: the diff (one line per file), the output line of every criterion, the commit hash, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 4 = `org/missions/D8/MDPF/MDPF_CANON/ledger/ROUND_ANALYSIS.round3.md` @ae094ea51d section 3 item 5 (M4, the next reader).
- **The census row:** `READER_CENSUS.md` row "gold/mdpf_revamp/ -- verify_mdpf_revamp_conditions.py and mdpf_revamp_count_source_audit.py
  (verification readers)" (reader; `mdpf_revamp_count_source_audit.py:53,106`). This order takes the audit only; `verify_mdpf_revamp_conditions.py`
  (188 lines) was not examined and is a later slice.
- **Why not the next row in the census's order, said plainly:** every remaining producer reader sits behind a served key or on a tree whose
  writer moves with it (census note 1): the staging trio and dim builders (rows 13-22) feed the consolidator and the publisher; the dated tree
  readers (rows 36-46) feed the served platinum keys; rows 47-58 are the served `aum-timeseries.json` key. Each of those takes a never-widen
  sign-off with a before and after of every leaf. This audit writes nothing it serves, and the artifact it audits already exists at the
  builder's address (CN-a-2/CN-a-3), so it is the one reader that moves no served output and needs no pair.
- **Measured at the cut (issuer, 2026-10-11):** parquet partitions exist for 49financial and inflection from 2026-07-27 to 2026-10-08
  (readable by the audit's profile). The loader, run against the real partitions, equals the old JSON over 3388 cells per firm (7 keys x 484
  dates), DELTA=0; 49financial additionally carries `tax`.
- **Hazards named so a worker meets a row, not a surprise:** (i) `ds-precommit-check.py`'s cross-firm fence reads literals; the file reads two
  firms' buckets only through `partition_uri`, which types none, but a refusal is the CTO's to rule (the audit is cross-firm by purpose); (ii)
  the old JSON is not deleted here, so the audit and the staging tree agree until the tree's retirement (M11, DEC-9 open).
- **Risk and class:** LOCAL (no `infra/` path, no deploy verb; the file is not shipped in the gold Lambda package or the runner chain, measured:
  no `build_package.py` entry, no dispatch call). `worker-light`: about 45 lines added, 10 changed.
- **Fanout:** independent of every other round-4 cell (disjoint write set); slot ~13, a chain of one.
- **Not a never-widen pair:** no served output moves; the CTO's L10 read is the exercised read, the CVO grades AC3 on `/seams`.
- Base box/dell1. LF only.

**AMENDMENT 1 (2.0.0_SA_COO~D1, 2026-10-11 ~06:2xZ, row MDPF_CANON-D1-W13-S1):** the proof instance is named beside the order's own file stem, `MDPF_CANON.TO-CN-d-4.count-audit-reads-the-gold-artifact.proof_of_spec.json`, because the pipeline gate searches for `<order file stem>.proof_of_spec.json`; section 5's path is corrected, no criterion or path of the grant changes. Gate limb: only GATE (viii) grades a modification, and `<placeholders>` is NONE.

<status>pending</status>
<round>4</round>
<to_id>MDPF_CANON.TO-CN-d-4</to_id>
<slot>~13</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
