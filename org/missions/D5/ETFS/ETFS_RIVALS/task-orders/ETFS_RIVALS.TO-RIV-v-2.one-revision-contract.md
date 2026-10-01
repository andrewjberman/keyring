# ETFS_RIVALS task order -- `RIV-v-2` -- ROUND 4 (ENRICHMENT): ONE REVISION CONTRACT FOR G1, G4 AND THE TRADE SCHEDULE -- NEWEST BY CAPTURE TIME, PER FUND

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-v-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~1</issued_to>
<issued_by>2.0.0_SA_COO~RV</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (2026-10-01 ~12:xxZ, --drift) -- no armed gate names rivalfunds/, issuer-site/etfs/, bloomberg/etfs/ or this cell's files; the notifier moratorium binds.
comp-iam: RUN at L5 -- no IAM change in this cell.
comp-adversary: RUN at L5 on the round-4 decomposition and DECLARED on this cell: the revision contract is what every reader rides; its checks plant the measured case (the 2026-09-29 QA G4 import named after the live pull) and a second issuer fund.
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric site-z) -- *rivalfunds*: daily holdings of rival active ETFs in two peer groups (IDVZ, PFOE), each fund's trade schedule, and a served page grouped by Opal fund. Rounds 1-3 built the live pipeline (package `data/etfs/scripts/rivalfunds/`, five AWS stage Lambdas, a terminal-machine Bloomberg leg); the 2026-10-01 page serves 12 of 13 funds. **Round 4** fixes the daily trade pairing, unifies 'newest', grades identity per source and adds GQGU. Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-v-2` -- ONE revision contract for G1, G4 and the trade schedule (rows W4-S5, W1-S11, W1-S19, W1-S25)

`revision.py` (new):
- `capture_time(uri_or_revision)` and `newest(candidates)`, where a candidate is a URI or a {uri, provenance} record;
- newest = latest capture time;
- an `import:` provenance never outranks a live object of the same date;
- a hash never orders.

Every multi-object reader uses it:
- `gold_canonical_shape`: issuer silver PER FUND (the issuer prefix holds `basg-*` and, after RIV-q-1, `gqgu-*` objects), Bloomberg
  silver per fund, and the G4 pick;
- `gold_trade_schedule`: the G1 pick per date and its own G5/G6 objects;
- `publish_page`: the G1/G5/G6 picks;
- `enrichment_bloomberg`: new G4 objects named with their capture time.

The G1 revision forms of W1-S19 and W1-S25 (the `h`/`j` letter suffixes) are replaced by the contract. A reader of an existing
object keeps working.

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base 48ec92238a)

- Today: `gold_canonical_shape` picks ONE issuer silver object per date (`max(issuer_uris, key=_revision)`, ~line 696),
  `_bbg_latest` (newest Bloomberg capture per fund by id string), `_g4_for` (newest G4 by object name); `gold_trade_schedule`
  `_canonical_by_date` / `_revision`; `publish_page._by_date` / `_revision`. Revision strings: issuer/Bloomberg `<UTC ts>-<sha12>`;
  G1 `<ts16>-<sha12>`, `<ts16>-h...`, `<ts16>-j<date>-<sha8>` (rows W1-S19, W1-S25); G4 `market-<YYYYMMDD>-<sha12>` (no time).
- The measured defect (row W4-S5): `rivalfunds/etfs/gold/security_market/date=2026-09-29/` holds
  `market-20260929-afcd903ad844` (172 rows, `source` = `import:bbg/2026-09-29/characteristics.parquet`, produced_at 10:59:32Z)
  and `market-20260929-53bc393958bd` (434 rows, `source` = `blp_client.reference_data`, produced_at 11:10:34Z); by name the
  import wins.
- `revision.newest(candidates)` is ALSO read by the issuer's live check d-5.AC3 (`from rivalfunds import revision`;
  `revision.newest([s3 uris])` -> the newest uri) -- keep that signature.
- After RIV-q-1 the issuer silver prefix holds `gqgu-<capture_id>.parquet` beside `basg-...`; G1 must read each issuer fund's
  own newest object (GQGU is `issuer_first` in the map).

## 3. SURFACES AND BOUNDS

You READ (never edit): `lib/`, `integrations/bloomberg/` (the Positioning pull is under an Andrew-direct no-modify order), the package's other modules, `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round{1,2,3,4}/checks/`, the device-local captures under `C:\Users\Opal Bloomberg\Desktop\ajb_workspace\.runtime\`, and live S3 READ-ONLY where a check mirrors it.

You WRITE only the `<paths>` below (plus `deliverables/0.9.0_WK_ETFS_RIVALS~1/`). NEVER: any S3 write, any deploy, any Bloomberg or OpenAI call, the vehicle, any file another round-4 cell owns. Tests go beside the code as `tests/test_v2_*.py`, run with `python -m pytest <file> -q` from `data/etfs/scripts/`; the issuer runs the whole suite at the drain.

<paths>
data/etfs/scripts/rivalfunds/revision.py
data/etfs/scripts/rivalfunds/gold_canonical_shape.py
data/etfs/scripts/rivalfunds/gold_trade_schedule.py
data/etfs/scripts/rivalfunds/publish_page.py
data/etfs/scripts/rivalfunds/enrichment_bloomberg.py
data/etfs/scripts/rivalfunds/tests/test_v2_*.py
data/etfs/scripts/rivalfunds/tests/test_g1_canonical_shape.py
data/etfs/scripts/rivalfunds/tests/test_g12_*.py
data/etfs/scripts/rivalfunds/tests/test_g6_*.py
data/etfs/scripts/rivalfunds/tests/test_p2_*.py
data/etfs/scripts/rivalfunds/tests/test_s4_*.py
data/etfs/scripts/rivalfunds/tests/test_hp1_home_producer.py
data/etfs/scripts/rivalfunds/gold_holdings_coverage.py
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

**AMENDMENT 1 (issuer ruling on rows Z-W1-S30 and Z-W1-S31, 2026-10-01).** Two repairs join this cell; no criterion is added.
(a) `tests/test_hp1_home_producer.py` `test_the_revision_with_home_rows_sorts_after_the_other_sources_revision_at_the_same_ts` asserts the retired `-h` letter form. Rewrite it to the one revision contract: a G1 build with home rows at a capture time already taken is ordered by `revision.newest` after the earlier build (the `-b<NN>` sequence), and a home-only build carries its own capture time; no letter form.
(b) `gold_holdings_coverage.py` `g1_sources` picks the newest G1 by object name; route it through `revision.newest(objs)`.
The drain runs the whole `data/etfs/scripts/rivalfunds/tests/` suite and must read 0 failed.

**AMENDMENT 2 -- REOPEN (issuer ruling on row ETFS_RIVALS-Z-S9, 2026-10-01).** `gold_canonical_shape.py` stamps every issuer row `source_channel` with the constant `SOURCE_CHANNEL = "issuer-site:basg"` (line 105, written at `build_rows`), so GQGU's rows read as BASG's channel. An issuer row's `source_channel` is `issuer-site:<source>`, where `<source>` is the source token of the silver object the row came from (`gqgu-...parquet` -> `issuer-site:gqgu`; `basg-...` -> `issuer-site:basg`, unchanged). Add a test beside the code (`tests/test_v2_*.py`). One criterion is added: AC3.

**AMENDMENT 3 -- REOPEN (issuer ruling on row ETFS_RIVALS-Z-S10, ARMED, 2026-10-01).** The vehicle's enrichment step runs `python -m rivalfunds.enrichment_bloomberg --mode daily` and branches on 0 landed / 1 unreachable / 2 partial / 3 nothing written (`integrations/bloomberg/pipeline/scheduled_daily_pull.cmd` :470-485, READ only, never edit it), but `enrichment_bloomberg.py` has no `__main__`: it imports, exits 0, and the vehicle logs "landed" with nothing pulled. Give `enrichment_bloomberg.py` the collector's CLI shape (`collector_bloomberg.py` `exit_code` + `main` + `if __name__ == "__main__": sys.exit(main())`): `--mode` passes through to `handler_entry` unchanged (daily included), plus `--date`, `--sink` (default s3), `--batch-id`; print the result as JSON; exit by the collector's contract (OK 0; detail.unreachable 1; PARTIAL 2; anything else 3). NEVER run it against Bloomberg or S3: tests stub `handler_entry`. Add a test (`tests/test_v2_*.py`). A FOURTH criterion is added, AC4 -- reason: an ARMED row whose remedy lies in this cell's write set (`enrichment_bloomberg.py`) and has no other open cell this round.

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- over the REAL 2026-09-29 inputs, G1's GICS sources name only the live G4 53bc393958bd, never the import (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round4/checks/v-2.AC1.py`)
- **AC2** -- with a later-named second issuer fund's object planted on BASG's date, G1 holds BOTH funds' rows (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round4/checks/v-2.AC2.py`)
- **AC3** (amendment 2) -- on the same planted date, G1's GQGU rows carry `source_channel` `issuer-site:gqgu`; control: BASG's stay `issuer-site:basg` (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round4/checks/v-2.AC3.py`)
- **AC4** (amendment 3) -- `python -m rivalfunds.enrichment_bloomberg --help` prints a usage naming --mode, and main() maps a stubbed handler's results to the collector's exit contract with --mode daily passed through (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round4/checks/v-2.AC4.py`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-v-2"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round4/checks/v-2.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>

  <criterion id="AC2" cell_refs="RIV-v-2"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round4/checks/v-2.AC2.py</invocation><expect>AC2 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="AC3" cell_refs="RIV-v-2"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round4/checks/v-2.AC3.py</invocation><expect>AC3 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="AC4" cell_refs="RIV-v-2"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round4/checks/v-2.AC4.py</invocation><expect>AC4 RESULT: PASS 0 failures</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~1/ETFS_RIVALS.TO-RIV-v-2.one-revision-contract.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-v-2.one-revision-contract`. Report once: each criterion's verdict line with the output above it; files written; any test assertion changed and why; rows filed (id + one line). Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** Round-3 analysis @d4a1e22801 (msg 27810), decomposition round 4 v1.0. Checks dry-run
at base 48ec92238a: v-2.AC1 FAIL, v-2.AC2 FAIL -- each FAIL as expected.

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<round>4</round>
<slot>~1</slot>
<fabric>site-z</fabric>
