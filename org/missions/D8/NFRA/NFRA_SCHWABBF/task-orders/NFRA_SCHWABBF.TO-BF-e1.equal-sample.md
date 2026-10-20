# TO NFRA_SCHWABBF.TO-BF-e1 -- the equality instrument: capture silver figures for named days before the change, compare after

<to_id>NFRA_SCHWABBF.TO-BF-e1</to_id>
<project>NFRA_SCHWABBF</project>
<issued_to>0.9.0_WK_NFRA_SCHWABBF~3</issued_to>
<issued_by>2.0.0_SA_COO~SB</issued_by>
<issued_date>2026-10-20</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>keyform</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `BF-e-1` (`decompositions/NFRA_SCHWABBF_DECOMP.md`) |
**outcome_ref:** FWD-5 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`BF-e-1`, PRD contract C-EQUAL. FWD-5 ACCEPT: "The day after the change, nobody can find a holdings, balance or activity figure for an already stored day that differs from the day before."
FWD-5 DONE WHEN: "sampled days rebuilt after the change and compared with the figures from before it, read once at the change and not kept running afterwards."
Andrew's standing veto: NO standing parity comparator, NO shadow pipeline. This tool is a ONE-SHOT: the issuer runs `capture` before the change and `compare` after it, and then it is not scheduled, looped or wired to anything.

**What exists (read, never edit).** The silver tables the Schwab converter writes, one `data.parquet` per day, at the builder's address:
`address('schwab', <master>, 'silver', <table>, 'date=YYYY-MM-DD') + '/data.parquet'` (`lib/opal_naming.py`). Measured 2026-10-20: `s3://opal-data-assets/schwab/08403355/silver/dim_balance/date=2026-10-16/data.parquet` exists (15,807 bytes).
Table names in use per master are listed by `workflows/atom_decomposition/catalog_entries/opal_data_assets_silver_schwab_<master>_*.yaml` (for example `dim_balance`, `dim_position`, `dim_transaction`, `fact_acc`, `fact_rps`, `fact_trn`).
Rewriting a day's silver happens by the converter Lambda when the moved bronze is re-created (see the decomposition's finding 1), so the compare reads the REBUILT bytes.

**Build `data/canonical/schwab/keyform/equal_sample.py`** (stdlib + boto3 + pyarrow or pandas, whichever the repo's silver code already uses; do not add a dependency):
1. `capture --master M --days D1,D2,... --tables T1,T2,... --out FILE.json`: for each (table, day) read the parquet and record `{table, day, exists, rows, columns, numeric_sums{col: float}, content_sha256}`.
   `content_sha256` is the sha256 of the rows serialised in a canonical order (sort by all columns, then a fixed text encoding), so row order and parquet file-level metadata do not change it. A partition that does not exist is recorded as `exists:false`, never skipped.
   Prints `CAPTURED cells=N missing=K` and writes the file. Also writes `master` and `captured_at_utc` into the file.
2. `compare --before FILE.json`: re-reads the same cells and prints `EQUAL-OK cells=N` and exits 0 when every cell matches on `exists`, `rows`, `columns`, `numeric_sums` and `content_sha256`; otherwise prints one `EQUAL-DIFF table=T day=D field=F before=X after=Y` per difference, then `EQUAL-FAIL diffs=K`, and exits 1.
   A cell that existed before and is missing after is a DIFF. A cell recorded `exists:false` that now exists is a DIFF (a day appeared).
3. The code path takes an injectable reader so tests need no S3. There is no scheduler, no loop, no `--watch`, no state kept between runs other than the `--out` file.

**Tests `data/canonical/schwab/tests/test_equal_sample.py`** (fake store): identical store -> `EQUAL-OK` rc 0; one changed numeric cell -> `EQUAL-DIFF ... field=numeric_sums` rc 1; reordered rows -> still `EQUAL-OK`; a deleted partition -> DIFF rc 1; a recorded-missing partition that appears -> DIFF rc 1;
the module text contains no scheduling or loop construct (`while True`, `sched`, `cron`, `watch`).

### ACCEPTANCE

<criterion id="BF1-e1-AC1" cell_refs="BF-e-1"><invocation>python -m pytest data/canonical/schwab/tests/test_equal_sample.py -q -p no:cacheprovider --color=no</invocation><expect>^[0-9]+ passed[ ,]</expect></criterion>
`BF1-e1-AC1` -- capture and compare on a fake store, including the failure arms (a changed figure, a vanished day, a day that appeared) and the absence of any standing-comparator construct.

<criterion id="BF1-e1-AC2" cell_refs="BF-e-1"><invocation>python data/canonical/schwab/keyform/equal_sample.py capture --master 08403355 --days 2026-10-16 --tables dim_balance --out C:/Users/AndrewBerman/AppData/Local/Temp/bf_e1_capture_probe.json</invocation><expect>^CAPTURED cells=1 missing=0</expect></criterion>
`BF1-e1-AC2` -- the seam probe against the REAL neighbor: a live, read-only capture of the real `dim_balance` partition for 0840 on 2026-10-16. It writes only the scratch file named in the invocation.

<expected_criteria>BF1-e1-AC1,BF1-e1-AC2</expected_criteria>

Dry-run at the base 2026-10-20: AC1 "no tests ran" (rc 4), AC2 "can't open file" (rc 2) -- FAIL as expected.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Everything else named here you READ and never edit.
- **LOCAL.** The only AWS call you make is the read-only GetObject in AC2. No write to S3. No deploy.
  If the real read is refused (no read identity in your shell), stop on AC2, write a surprise row naming the refusal, and do not weaken the criterion.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id `NFRA_SCHWABBF-W3-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing), and do not weaken the test to pass.

<paths>
data/canonical/schwab/keyform/equal_sample.py
data/canonical/schwab/tests/test_equal_sample.py
org/missions/D8/NFRA/NFRA_SCHWABBF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit. (`data/canonical/schwab/keyform/__init__.py` is created by the worker of `TO-BF-m1` on another branch; if your branch lacks it, run the tool by file path, which AC2 already does.)

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_SCHWABBF/decompositions/NFRA_SCHWABBF_DECOMP.md</decomp_doc> (round 1), cell `BF-e-1`.
<owned_cells>BF-e-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BF1-e1-AC1, BF1-e1-AC2. Instance at `org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.9.0_WK_NFRA_SCHWABBF~3/NFRA_SCHWABBF.TO-BF-e1.equal-sample.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> BF1-e1-AC1,BF1-e1-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the CAPTURED line and the columns of the real `dim_balance` partition (names and types only, never row values), the pytest summary line, the commit hash, any surprise row id.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- thread round; the tool is one-shot by construction.
comp-iam: RUN -- decomposition battery scanned 2 Terraform files (monolith-iam.tf, iam.tf) and 3 enumerated masters; this cell reads silver under the seat's own identity and adds no grant; BLIND: the live IAM plane (0 roles read).
comp-adversary: DECLARED-NOT-APPLICABLE -- thread round; the standing-comparator veto is inlined in the face and graded by the no-loop test arm.
lane: the <paths> block IS the grant.
</preflight>

Source: PRD v0.1 C-EQUAL; decomposition round 1 cell BF-e-1; release acts R2 and R6.
