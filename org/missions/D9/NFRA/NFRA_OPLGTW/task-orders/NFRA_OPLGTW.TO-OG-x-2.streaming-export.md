# NFRA_OPLGTW task order -- `OG-x-2` -- ROUND 2 (E5, build half): the streaming export -- refuse before allocating, one representation, the row cap counted once, wired end to end

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-x-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~11</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a local code change; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM operation, policy, principal or role; local build only.
comp-adversary: DECLARED-NOT-APPLICABLE -- the remedy is ruled (R-4 on R-OG-22 and S57) and the defect measured at the bytes (row Z-S8 @b6727f8cee).
EGRESS CLASS, declared: the PyPI download for the venv below only -- development egress permitted to this project's COO and its workers (Andrew-direct ~21:2xZ, record @7bfa5811c6). No AWS call, no deploy.
</preflight>

## 1. THE CELL -- `OG-x-2` (decomposition addendum R2-E, item E5, build half)

**Make the Schwab CSV export's memory stop being a function of the export's size, refuse an over-cap export before it
allocates, and make the production export path work at all.** Build only: nothing is deployed by this cell (`OG-x-3`
ships it). PRD `org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md` v1.1; contract
`org/standards/NFRA_OPLGTW_CONTRACT.json` (limits unchanged, ruling R-4). Outcomes served: FWD-4, FWD-5, FWD-7.

**What the code does today, read at the issuance base (paths under `infra/aws/ec2/opal-gateway/`):**

1. **The export is BROKEN end to end today, not only expensive (row `NFRA_OPLGTW-Z-S8`).**
   `app/integrations/schwab/engine.py:686-695`: for `kind == "export"` the child writes the whole Arrow result to
   `export.csv` with `pyarrow.csv.write_csv` and reads the WHOLE file back as `result["csv"]` (bytes), pickled to the
   parent over the pipe. It never sets `result["rows"]`. But `app/integrations/schwab/integration.py:898-905`
   (`SchwabService.export_query`) calls `self._engine.run_export(...)` and then requires `value.get("rows")` to be a
   list, else it raises `ServiceError(INTERNAL_ERROR, "scan_incomplete")`. So on the real engine every export ends
   `INTERNAL_ERROR`. The tests do not see it: `tests/test_schwab_export.py:132` aliases `run_export = run_query`, and
   `tests/acceptance/conftest.py:139` does the same. `tests/test_schwab_engine.py:738` asserts the `csv` bytes shape.
2. **The result is materialised whole, up to four times.** In the child: `engine.py:674` `fetch_arrow_table()` (every
   row up to `limit = cap + 1`), then the CSV file, then the file read back into bytes (`:691-692`), then the pickled
   copy in the parent. In `export_query`, had rows arrived: `rows` (:902), `prepared` (:923-929) and `rendered` (:930),
   all live at once (row `NFRA_OPLGTW-S57`).
3. **The row cap is enforced AFTER the allocation it bounds.** The plan is built with `limit=cap + 1` (:890-891);
   `matched > cap` is checked at `integration.py:911-914`, after `run_export` has returned. The child already knows
   `matched` BEFORE it fetches: `engine.py:673` runs `count_sql` first, then `:674` fetches. The cap value is read from
   the contract at `integration.py:871`.
4. **The writer is already row-at-a-time.** `app/integrations/schwab/export.py:203-215` `write_csv` iterates `rows` and
   never indexes or `len()`s it (row `NFRA_OPLGTW-S59`). `generate_csv` (`export.py:257-268`) calls `export_query`, then
   `write_csv`, then `len(rows)` (:268 -- that `len` must go when rows become an iterator).
5. **The MCP response's 500-row cap counts every row twice** (row `NFRA_OPLGTW-W5-S6`). `app/integrations/schwab/envelope.py:174-184`
   `measure()` adds the `structuredContent` rows to the rows of each duplicate JSON text block, so a page never carries
   more than 250 rows although `page_size` accepts 500. `tests/test_schwab_query.py:780-800` (`test_ogq2_ac16`) asserts
   that doubling (`measured["rows"] == 2 * doc["returned_count"]`) and must change with it.

**What to build (the outcome is fixed; the shape inside it is yours):**

- **Wire it end to end.** The real `run_export` result is what `export_query` consumes; both test aliases
  (`run_export = run_query`) are removed from the export tests so they exercise the branch production takes.
- **Refuse before allocating.** An export whose matched count exceeds the contract's `limits.export_rows` is refused
  `LIMIT_EXCEEDED`, reason `export_rows_limit`, with the same suggestion text as today, BEFORE any result row is fetched.
  The cap travels from the contract (read as today at `integration.py:871`) into the job; it is never a new literal.
- **One representation at a time.** The rows move from the child to the CSV file in bounded batches. The parent never
  receives the whole result over the pipe, and nothing holds `rows`, `prepared` and `rendered` side by side. A shape
  that meets this: the child writes the projected result to a file in the export directory (never the job `workdir`,
  which `submit()` deletes at `engine.py:1162`), returns its path and `matched_rows`; the parent reads it back in
  record batches, applies the account reference (`aref.account_ref`) and rendering (`env.render_rows`) per batch, and
  feeds an iterator to `write_csv`. The keyring stays in the parent; the child never receives it.
- **Keep every existing guarantee:** the grant revision is re-read before emission (`integration.py:910`); the UTF-8
  byte cap refuses and removes the file (`export.py:212-214`); formula prefixes are escaped; every local export file
  is removed on success, failure, cancellation and startup cleanup (PRD C5).
- **Count a row once.** `envelope.measure()` counts a row once however many blocks carry it (the largest per-block
  count, not the sum). The codepoint and UTF-8 byte measures still cover the whole serialized result. Correct
  `test_ogq2_ac16`'s doubling assertion; keep its three-cap assertion.

The PRD's C5, verbatim: *"Generate and validate a bounded CSV completely before starting its response; then reauthorize
and stream without buffering it on the event loop. At most 250,000 rows and 50 MiB UTF-8, within the export job deadline
and shared source/resource caps. Over-limit exports fail and ask for narrower scope, never silently truncate."*
"Completely before responding" constrains ORDER, not residency (row S59). C4, verbatim: *"Limit the entire serialized
MCP result to 500 rows, 100,000 Unicode codepoints and 131,072 UTF-8 bytes, including all content blocks,
structuredContent and duplicated text."* The round analysis rules the reading: the 500-row cap is counted once.

**Read:** the PRD's C4 and C5; the contract's `limits`; `engine.py` (`_plan_job`, `submit`, `run_export`),
`integration.py` (`export_query`), `export.py`, `envelope.py`, `download_routes.py` (the caller of `generate_csv`), and
the three test modules above.

**New test module** `tests/test_schwab_export_stream.py` carries `test_ogx2_ac01` and `test_ogx2_ac02`;
`tests/test_schwab_query.py` gains `test_ogx2_ac03`. Each test must finish inside its invocation's `timeout 110`.

## 2. BOUNDS

- **Grant.** Your write surface is the `<paths>` block below. A path you need that is not named is a BLOCKING surprise
  row -- never an override.
- **Worktree.** You work in the worktree named in your identity line. Never push, merge, rebase, `checkout --`,
  `stash` or `clean`.
- **Interpreter.** Build `.venv-og` at your worktree root ONCE:
  `python -m venv --system-site-packages .venv-og && .venv-og/Scripts/python -m pip install -r infra/aws/ec2/opal-gateway/requirements.txt moto pytest`.
  This PyPI download is permitted development egress (Andrew-direct ~21:2xZ, record @7bfa5811c6). Site Z has no
  `py -3.12`; `python` is 3.11. It serves every invocation. Never commit `.venv-og/` or `.scratch/`. Every pytest run
  sets `AUDIT_PATH` to a temporary file first.
- **Contract numbers do not move** (ruling R-4): 250,000 rows, 50 MiB, the 256 MiB job cap. A test lowers a cap only
  through a contract OVERLAY fixture, never by editing `org/standards/NFRA_OPLGTW_CONTRACT.json`.
- **Synthetic data only.** No Schwab object, no AWS call, no deploy.
- **The rest of the Schwab suite stays green at your close:** `tests/test_schwab_export.py`, `test_schwab_engine.py`,
  `test_schwab_query.py`, `test_schwab_wiring.py` and `tests/acceptance/test_local_acceptance.py`. A test that
  asserts the OLD behaviour (the `csv` bytes shape at `test_schwab_engine.py:738`, the doubling at
  `test_schwab_query.py:799`, the `run_export = run_query` aliases) is corrected, and each correction is named in your
  result file. Record the suite's pass/fail counts; this is drain hygiene, not a criterion.
- **Commits.** `.tools/safe-commit.sh` under your serial; every `.py` you touch passes `.tools/commit-gate.sh`.
- **Spec frozen; REFUSE what you cannot meet as written.** Anything off-spec is one surprise row, and you keep working.
- **Numbers** in this order are context, never acceptance values, except where a criterion states one.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/integrations/schwab/engine.py
infra/aws/ec2/opal-gateway/app/integrations/schwab/integration.py
infra/aws/ec2/opal-gateway/app/integrations/schwab/export.py
infra/aws/ec2/opal-gateway/app/integrations/schwab/envelope.py
infra/aws/ec2/opal-gateway/app/download_routes.py
infra/aws/ec2/opal-gateway/tests/test_schwab_export_stream.py
infra/aws/ec2/opal-gateway/tests/test_schwab_export.py
infra/aws/ec2/opal-gateway/tests/test_schwab_engine.py
infra/aws/ec2/opal-gateway/tests/test_schwab_query.py
infra/aws/ec2/opal-gateway/tests/acceptance/conftest.py
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~11/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: `org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md`, id
`NFRA_OPLGTW-Z-W11-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="OGX2-AC1" cell_refs="OG-x-2"><invocation>timeout 110 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_export_stream.py::test_ogx2_ac01 -q -s -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
  <criterion id="OGX2-AC2" cell_refs="OG-x-2"><invocation>timeout 110 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_export_stream.py::test_ogx2_ac02 -q -s -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
  <criterion id="OGX2-AC3" cell_refs="OG-x-2"><invocation>timeout 110 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_query.py::test_ogx2_ac03 -q -s -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
</proof_of_spec>

- `OGX2-AC1` (`test_ogx2_ac01`) -- through the REAL engine (a spawned child, no `run_export` alias) and `generate_csv`,
  a 100,000-row export's peak memory (the child's peak RSS as `JobResult.peak_child_rss_bytes` reports it, plus the
  parent's `tracemalloc` peak during `generate_csv`) is at most 1.2 times a 10,000-row export's; both CSVs are written
  with the right row count; the test prints both sizes and all four numbers.
- `OGX2-AC2` (`test_ogx2_ac02`) -- with a contract overlay setting `limits.export_rows` to 1,000 and a request matching
  5,000 rows, the real-engine export is refused `LIMIT_EXCEEDED` / `export_rows_limit` with zero result rows fetched (a
  count the child reports and the test prints), and no file remains in the export directory.
- `OGX2-AC3` (`test_ogx2_ac03`) -- a `schwab_query` page with `page_size` 500 over 700 matched short rows (bytes and
  codepoints well inside their caps) returns 500 rows, `truncated` true with a cursor, and `envelope.measure()` reports
  500 rows.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~11/NFRA_OPLGTW.TO-OG-x-2.streaming-export.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance>` BEFORE the `complete` flip. Result file
`streaming-export.result.md` beside it: the four AC1 numbers, the AC2 fetched-row count, the suite counts, and every
corrected test named. Flip `complete` only when every criterion PASSES by output. Report once, in your final message.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Slot ~11, queue position 1 (then `OG-x-3`, the narrow release, then `OG-r-3`, the on-host measurement).
- Rows carried: `S57` (materialisation + post-allocation refusal), `S59` (writer already streams), `W5-S6` (cap counted
  twice), and `Z-S8` @b6727f8cee (the export cannot return a CSV today; the aliases hid it). `onhost_bench.py:366-371`'s
  comment refers to a round-1 row for the same mismatch that no channel row carries by id; Z-S8 is the carrier.
- AC1's sizes are the issuer's choice: 10,000 and 100,000 rows (one order of magnitude apart, both under the cap), sized
  so the real-engine test fits the worker's 120 s bound; the 1.2 ratio stands. Contract scale is `OG-r-3`'s, on the host.
- Write set is disjoint from E7/E9 (slot ~12) and from `OG-r-3`. `OG-h-1` (the batch cell) edits two of these test files
  and is therefore handed only after this order drains.
- `<risk>` WORLD is GATE (xii)'s floor (an `infra/` path); the cell deploys nothing.

<status>complete</status>
<round>3</round>
<slot>~11</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
