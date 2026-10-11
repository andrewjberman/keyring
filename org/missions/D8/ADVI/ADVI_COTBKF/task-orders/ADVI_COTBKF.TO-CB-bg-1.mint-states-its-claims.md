# TO ADVI_COTBKF.TO-CB-bg-1.mint-states-its-claims -- round 59 CB-bg-1: the manifest carries the vocabulary note, the sidecar and the method row; the mint path can write and read back all three

<to_id>ADVI_COTBKF.TO-CB-bg-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~86</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>issued</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>59</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** dell2 (placement DELL2) | **Decomp cell:** `CB-bg-1` (`decompositions/ADVI_COTBKF_DECOMP.round59.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**RULE (CTO containment ruling @0e8209c33c, item 6): no client account id, balance, fee or flow in ANY tracked file.** Counts, sha256,
addresses and reason codes only, in code, tests, the manifest, your report, commit messages and rows. Every value in a test is
SYNTHETIC. The sidecar holds account ids: it NEVER enters the repo; the repo carries its sha256 and row count.

**Why (CTO round-58 analysis `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_58_20261011.md` section 4
item 5, and msg 4170).** Before Cottonwood's `account_return_daily` is minted, the sign-off pair must state, each as a fact a reader
can check: what `NO_HOLDINGS_ROW` means on these rows; where the blank-day reasons live; and which method row the rows are stamped
with. Today the adapter can mint the day files only. This cell makes the manifest say those things and makes the mint able to write
and read back the two extra objects. **You do NOT run the mint.**

**Your item, all in `data/assets/scripts/silver/commonwealth_account_return_daily.py`.** No S3 call of any kind; tests fake S3.

1. **A stamp mode.** Add `--stamp-manifest --manifest <tracked manifest> [--days-dir <dir>]`. It rewrites the tracked manifest IN
   PLACE, changing nothing but these three top-level fields, and prints one last line:
   - `vocabulary_notes`: an object with one key, `NO_HOLDINGS_ROW`, whose text says: on these rows it means no holdings row exists
     UNDER THIS ACCOUNT ID FORM; the two id forms were not joined on any of the 75 neighbour days; the holdings cross-check therefore
     graded 0 of 1,691,729 rows; a reader must not take it as "the account held nothing". Carry the two counts as numbers too
     (`neighbour_days_joined`: 0 of 75; `rows_graded_by_holdings_cross_check`: 0 of the manifest's `rows`).
   - `reasons_sidecar`: keep what is there and make sure it carries `address` (the output of `lib/opal_naming.py` `address()` under
     Cottonwood's own tenancy, built in code, never typed; if the builder REFUSES, stop: that is the refusal clause, not a
     workaround), `sha256` and `rows` of the local sidecar file `<days-dir>/ard_cottonwood_blank_reasons.parquet`, and
     `carrier_of`: `blank_reason` and `exception_class` per NOT_MEASURABLE account-day.
   - `method_row`: `method_version` 3; `address` of Cottonwood's `dim_return_method` row 3 as the PRODUCER computes it (call its own
     function; do not type it); `thresholds`: the five values null; `threshold_claims`: each of the five `absent`; `src`: the name of
     the `_commonwealth_delivery` entry.
   - Before writing it re-hashes every day file against the manifest's `day_files` and refuses if one differs. `day_files` is not
     touched.
   - Last line: `ARD-COTTONWOOD-MANIFEST-STAMP days=<d> day_hashes_equal=<e>/<d> note=present sidecar_rows=<n> method_version=3`.
2. **The mint path writes the two extra objects.** In `apply_days`, after the bond count and BEFORE any write: the sidecar key and the
   method-row key are read, and ANY existing key (a day key, the sidecar, the method row) refuses the whole run. Then, in this order:
   the day files exactly as now; the sidecar (re-hashed against the manifest's `reasons_sidecar.sha256` first); the method row through
   the producer's own `emit_method_row(..., upload=True, src=<the entry>)` with the thresholds of the manifest's `method_row`. Print one
   `LANDED <key>` line per object written, so a partial run is visible. There is still no delete path.
3. **Read-back.** `verify_served` also compares the served sidecar's sha256 with the manifest's and reads the method row back,
   checking `method_version` 3 and the five `*_claim` columns `absent`. Its last line keeps its `ARD-COTTONWOOD-VERIFY days=... match=...`
   start and gains `sidecar=<match|differ|absent> method_row=<match|differ|absent>`.
4. **Tests alone first.** Add `data/assets/scripts/silver/tests/test_commonwealth_ard_mint_claims.py`, committed ALONE first; report
   its red line. On synthetic frames and a faked S3 it asserts: the stamp writes the three fields and leaves `day_files` byte-equal;
   the stamp refuses when a day file's hash differs; `apply_days` refuses, with zero writes, when the sidecar key or the method-row
   key exists; on a clean faked bucket it writes days, then the sidecar, then the method row, and the method row's thresholds are
   five nulls claimed `absent`; `verify_served` reports `sidecar=match method_row=match` after that write and `differ` after one
   byte of the faked sidecar changes.
5. **Run the stamp on the real tracked manifest** with the CB59bg1-AC2 invocation and commit the stamped manifest. Report its old and
   new sha256.

**Inputs.** The real day files and the real sidecar are in the BASE checkout, read-only: `C:/dev/ajb_workspace/.scratch/advi_cotbkf/ard_cottonwood_r47`. Read
`data/assets/scripts/gold/irpt_reporting/account_return_daily.py` (`emit_method_row` at line 1948, `threshold_claims_of` at 1896) to
call it correctly; do NOT edit it. If `emit_method_row` refuses row 3 for Cottonwood on a faked bucket, stop and report its refusal
text: that is another project's contract, not yours to change.

### ACCEPTANCE

<criterion id="CB59bg1-AC1" cell_refs="CB-bg-1"><invocation>env -u COTBKF_SWEEPS_CONFIG python -m pytest data/assets/scripts/silver/tests/test_commonwealth_ard_mint_claims.py -q</invocation><expect>passed</expect></criterion>
`CB59bg1-AC1` -- the stamp, the mint's refusals and write order, and the read-back behave as step 4 lists; 0 failed, 0 skipped.

<criterion id="CB59bg1-AC2" cell_refs="CB-bg-1"><invocation>python data/assets/scripts/silver/commonwealth_account_return_daily.py --stamp-manifest --manifest org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~79/ard_cottonwood_manifest.json --days-dir C:/dev/ajb_workspace/.scratch/advi_cotbkf/ard_cottonwood_r47</invocation><expect>ARD-COTTONWOOD-MANIFEST-STAMP days=3325 day_hashes_equal=3325/3325 note=present sidecar_rows=1584413 method_version=3</expect></criterion>
`CB59bg1-AC2` -- the real tracked manifest carries the three fields and its 3,325 day hashes equal the local files. Running it a
second time changes no byte of the manifest.

<criterion id="CB59bg1-AC3" cell_refs="CB-bg-1"><invocation>env -u COTBKF_SWEEPS_CONFIG python -m pytest data/assets/scripts/silver/tests -q</invocation><expect>passed</expect></criterion>
`CB59bg1-AC3` -- the silver suite passes with the variable unset: 0 failed, 0 errors, 12 skipped as before this order. This includes
both account-id tests and the manifest hash-field test on the stamped manifest.

<expected_criteria>CB59bg1-AC1,CB59bg1-AC2,CB59bg1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, your deliverables folder and the file of this order.
- **Do NOT touch:** anything under `data/assets/scripts/gold/` or `lib/` or `infra/` (other lanes), any other test, the manifest's
  `day_files`, anything under `C:/dev/ajb_workspace/` (read only), `surprise-channel/` except your own NEW row.
- **Do NOT run `--apply` or `--verify-served`.** No AWS or S3 call of any kind. No push.
- **No gate override** of any kind and no `--force`. If a gate refuses a commit and the fix is not an ordinary code correction inside
  your grant, stop and report its exact refusal line.
- **Do not open or print** anything under `C:/dev/_cotbkf_private_evidence_20261009/`. Read the sidecar only for its sha256 and row
  count; never print a row of it.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report (counts only) and a NEW surprise row
  (id `ADVI_COTBKF-D2-W86-S<k>`, `"fabric": "dell2"`, carrying no account id). Do not weaken a test.

<paths>
data/assets/scripts/silver/commonwealth_account_return_daily.py
data/assets/scripts/silver/tests/test_commonwealth_ard_mint_claims.py
data/assets/scripts/silver/tests/conftest.py
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~79/ard_cottonwood_manifest.json
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round59.md</decomp_doc> (round 59), cell `CB-bg-1`.
<owned_cells>CB-bg-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB59bg1-AC1, CB59bg1-AC2, CB59bg1-AC3. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~86/ADVI_COTBKF.TO-CB-bg-1.mint-states-its-claims.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB59bg1-AC1,CB59bg1-AC2,CB59bg1-AC3` BEFORE the flip. All three are
mechanical.
</proof_of_spec>

**REPORT (counts only):**
- the red pytest line of the test-alone commit; the three acceptance lines, with the full `ARD-COTTONWOOD-MANIFEST-STAMP` line;
- the manifest's sha256 before and after the stamp, and the result of the second run (bytes equal or not);
- the two addresses as the builders printed them (the sidecar's and the method row's), and which function produced each;
- the order of writes in `apply_days` and the full list of keys it reads before writing, in two sentences;
- commits, with the test-alone commit first; every gate refusal, verbatim; anything you could not run or verify.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE one hand-run adapter, its tests and one tracked manifest; nothing scheduled runs the adapter (row ADVI_COTBKF-D2-S84).
comp-iam: DECLARED-NOT-APPLICABLE no AWS call; the apply and verify paths are extended and exercised on faked S3 only.
comp-adversary: RUN -- the test alone first, red at the base; the stamp re-hashes every day file and has a refusing arm; the mint's two new refusals assert zero writes; the read-back has a differ arm; addresses come from the builders and a builder refusal stops the cell; BLIND: the real IAM grant for the sidecar and method-row keys, and whether the producer's contract admits row 3 on the real bucket, are not exercised here.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-58 analysis @1c27ce4263 (msg 4153) section 4 items 4 and 5; msg 4170 (item 4 re-ruled); `2.0.0_SA_COO~D2` msg 4140 (contract 0.4.0, threshold claims); rows ADVI_COTBKF-D2-W66-S2 and D2-W66-S3.
