# TO MDPF_SECHIST.TO-SH-t2 -- round 1 SH-t-2: Positioning gold computes every window from a year of rows carried in one daily partition

<to_id>MDPF_SECHIST.TO-SH-t2</to_id>
<project>MDPF_SECHIST</project>
<issued_to>0.9.0_WK_MDPF_SECHIST~2</issued_to>
<issued_by>2.0.0_SA_COO~H1</issued_by>
<issued_date>2026-10-07</issued_date>
<status>pending</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>

**Directive:** D8 | **Fabric:** laptop (placement dell1) | **Decomp cell:** `SH-t-2` (`decompositions/MDPF_SECHIST_DECOMP.md`) |
**outcome_ref:** FWD-1 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`SH-t-2`. FWD-1: a security an Opal ETF bought yesterday reads every return window a year of history supports on the Positioning page.

**The hop.** A sibling cell changes the site Z ETF daily pull so that, for a new security, the day's
`s3://opal-data-etfs/bbg/<asof>/history_topup.parquet` carries a YEAR of that security's rows (dates from about `asof - 372 days` to `asof`), not
only the as-of day. This cell proves Positioning gold computes all eight windows (1D, WTD, MTD, 1M, QTD, 1Q, YTD, 1Y) from such a partition.

**The code, read at the base.** `data/etfs/scripts/gold/etf_positioning_gold.py`:
- `load_history(as_of, bucket)` (line 731) lists `bbg/` date prefixes, reads `history_topup.parquet` for each prefix date within
  `HISTORY_LOOKBACK_DAYS` (400) of `as_of`, appends the frozen `bbg-testpull/tickers/` CSV rows (`_load_backfill_history`), keys rows by the first
  token of `security` into `tkr`, and de-duplicates (populated beats null, then daily partition beats CSV). It reads S3 through `_s3()` (line 361)
  and `_read_parquet`. It does NOT filter a partition's rows by the partition date.
- `compute_returns(tkr, as_of, hist)` (line 855) compounds `DAY_TO_DAY_TOT_RETURN_GROSS_DVDS` (percent) over the observations present; a window is
  computed only when there is an observation ON `as_of` and the series starts at or before the window's start.
- The sibling tests in the same folder (`test_etf_positioning_upgrade_forward.py` and others) import `etf_positioning_gold` bare, run offline with
  fixtures, and use no S3.

**Build (a test; code only on a measured defect):**
1. NEW file `data/etfs/scripts/gold/test_etf_positioning_backfill_rows.py`, pytest-collectable, offline: replace `_s3()` (monkeypatch the module
   attribute) with a fake client that serves `list_objects_v2` and `get_object` from an in-memory dict, so the real `load_history` runs unchanged.
   Tests, exact names:
   - `test_backfill_rows_in_topup_fill_all_windows`: as_of 2026-10-06 (a Tuesday). One partition `bbg/2026-10-06/history_topup.parquet` holds
     the security `NEWX US Equity` with one row per weekday from 2025-09-29 to 2026-10-06, a small non-zero `DAY_TO_DAY_TOT_RETURN_GROSS_DVDS` and
     a `PX_LAST`; no CSV object. `compute_returns("NEWX", as_of, load_history(as_of))` returns a non-null value for EVERY key of
     `RETURN_WINDOWS`; assert also that the 1D value equals that day's return.
   - `test_single_row_only_1d_control`: the same partition with only the 2026-10-06 row: 1D non-null, every other window null. This is the
     difference control: the only change between the two tests is the rows present.
2. If `test_backfill_rows_in_topup_fill_all_windows` fails on the real code, find the cause, fix it in `etf_positioning_gold.py` with the smallest
   change, keep the sibling tests passing (`python test_etf_positioning_upgrade_forward.py` and the other `test_etf_positioning_*.py` in that
   folder, each run from the folder), and file a surprise row naming the defect. If it passes, change no production code.

### ACCEPTANCE

<criterion id="SH1-t2-AC1" cell_refs="SH-t-2"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECHIST_H1/R1_CHECKS/sh_t2_gold_tests.py</invocation><expect>GOLD-TESTS-OK</expect></criterion>
`SH1-t2-AC1` -- both named tests pass against the real `load_history` and `compute_returns`: a year of rows in one partition yields all eight windows, one row yields 1D only.

<expected_criteria>SH1-t2-AC1</expected_criteria>

Run the invocation from the worktree root. It FAILS at the base (2026-10-07): `GOLD-TESTS-BAD rc=4` (no test file).

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **No S3 read or write, no gold run, no deploy.** The test is offline.
- `etf_positioning_gold.py` is in your grant ONLY for a defect the first test measures; any edit there names the failing assertion in your report.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id `MDPF_SECHIST-W2-S<k>`,
  `surfaced_at` = `date -u +%FT%TZ`) in the investigation file below, and do not weaken the test.

<paths>
data/etfs/scripts/gold/test_etf_positioning_backfill_rows.py
data/etfs/scripts/gold/etf_positioning_gold.py
org/missions/D8/MDPF/MDPF_SECHIST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECHIST/decompositions/MDPF_SECHIST_DECOMP.md</decomp_doc> (round 1, the thread), cell `SH-t-2`.
<owned_cells>SH-t-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SH1-t2-AC1. Instance at `org/missions/D8/MDPF/MDPF_SECHIST/deliverables/0.9.0_WK_MDPF_SECHIST~2/MDPF_SECHIST.TO-SH-t2.gold-reads-backfill-rows.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> SH1-t2-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** the test file, its output, whether any production code changed (and why), commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE thread round; no schedule.
comp-iam: DECLARED-NOT-APPLICABLE no IAM; the test is offline.
comp-adversary: DECLARED-NOT-APPLICABLE thread round; the lens runs on the enrichment round that touches its surface.
risk: LOCAL -- a test file; a gold edit only on a measured defect, deployed by the issuer under Rule 13 at the drain if one lands.
direct_act: true -- one cell, under 300 lines, LOCAL.
</preflight>

Source: PRD v0.1 @b4b995dc14 section 2 (THREAD); decomposition round 1, hop H4.
