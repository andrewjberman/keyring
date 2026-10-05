# TO MDPF_SECCLASS.TO-SC-e17 -- round 7 SC-e-17: FWD-9 rows -- the shared mapping module, the universe row set, a dry-run writer and the rows half

<to_id>MDPF_SECCLASS.TO-SC-e17</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~14</issued_to>
<issued_by>2.0.0_SA_COO~M</issued_by>
<issued_date>2026-10-05</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>7</round>
<workstream>~M</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `SC-e-17` (`decompositions/MDPF_SECCLASS_DECOMP_R7.md`) |
**outcome_ref:** FWD-9 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`SC-e-17`. FWD-9: "for every stock Rival Funds collects, the shared list gives its class, sub-class and whether it is a fund
or an individual stock" (PRD `org/missions/D8/MDPF/MDPF_SECCLASS/prd/MDPF_SECCLASS_PRD.md` v0.3, FWD-9). The shared list is
DynamoDB `etf-classifications`. Rulings: `org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/RULINGS.md`
batch 257.

**The input** (ETFS_RIVALS' served artifact; read it, never write it):
- Path: `s3://opal-data-etfs/rivalfunds/etfs/gold/canonical_shape/date=<d>/holdings-<rev>.parquet`. Take the newest
  revision of each day.
- Columns used: `security_bloomberg`, `security_ticker`, `security_name`, `security_cusip`, `provider_security_type`,
  `position_type`, `is_cash_line`, `asset_class`, `gics_sector`, `gics_status`.
- Measured at issue: 504 days, 822 distinct non-cash securities (US 178, non-US 516, `Index` futures 17); 139 of 177 US
  tickers already have rows.

**The rules:**
- **Q4, domain.** A stock is `provider_security_type == "Equity"` and non-cash (`position_type != "cash"`, `is_cash_line` not
  true). `Index` futures are out.
- **Q1, key.** For US listings (exchange code `US`), `ticker` = the bare ticker, as today. For every other listing, `ticker`
  = `BBG:<ticker>:<exch>`, with no whitespace, plus `identifier_namespace` = `BLOOMBERG` and `security_bloomberg` verbatim.
- **Q3, sub-class, in order:**
  1. The GICS sector where `gics_status` is RESOLVED, using the table's existing sector values (`Financials`,
     `Information Technology`, ...).
  2. Else the exchange country, held as data in `listing_country`, mapped to the vocabulary's regional sub-class. The
     measured values are `Developed`, `EM`, `International` and `Global`; use the MSCI developed/emerging split, held as a
     table in the module.
  3. Else no sub-class and `low_confidence: true`. A US listing with unresolved GICS lands here, because the US values are
     size-split.
- **Every row:** `asset_class` `equity`, `instrument_kind` `single_security`, `classified_by` `scheduled`, `updated_by`
  `rivalfunds-backfill`, and `name` from `security_name`.

**Build (no table write in this cell; the write is the issuer's act under the half):**
1. **The shared mapping module.** `infra/aws/lambda/v2_portal/_shared/rivalfunds_classification.py`: a pure
   `classify_canonical_row(row: dict) -> dict | None` implementing Q1, Q3 and Q4, with the exchange-to-country and
   country-to-regional tables as module data. ASCII only. `SC-e-19` imports it, so give it no I/O.
   Tests go in `infra/aws/lambda/v2_portal/_shared/tests/test_rivalfunds_classification.py`, covering:
   - a US ticker;
   - a non-US key with whitespace removed;
   - an `Index` future returning None;
   - a cash line returning None;
   - resolved GICS winning over country;
   - an unresolved developed listing giving `Developed`;
   - an unresolved US listing giving `low_confidence`.
2. **The row set.** `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R7_CHECKS/r7_fwd9_row_set.py`.
   - Read every partition with column-pruned reads (`pyarrow.fs.S3FileSystem`; the laptop link is slow), map each
     distinct security, and read each key with a consistent get.
   - Write `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R7_CHECKS/FWD9_ROW_SET_20261005.tsv`, one line per
     security: action, key, security_bloomberg, name, item JSON.
   - The actions are `WRITE` (no row), `PRESENT-SAME`, `PRESENT-DIFFERS` (a row exists with another class or sub-class;
     NEVER overwritten, listed for the CTO) and `OUT` (Q4).
   - It prints `FWD9-ROW-SET securities=<n> write=<n> present_same=<n> present_differs=<n> out=<n>`.
3. **The writer.** `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R7_CHECKS/r7_fwd9_write.py`.
   - It writes the set's `WRITE` lines through `infra/aws/lambda/v2_portal/_shared/etf_classification_scheduled.py`
     `write()` (put on absence only).
   - It is a DRY RUN by default. `--write` REFUSES unless all of these hold:
     (a) `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R7_BBG_READER_CENSUS_20261005.json` (cell `SC-e-16`)
     has crashes, refuses, miskeys and fails_contract all 0;
     (b) `org/standards/MDPF_SECCLASS_CONTRACT.json` lists `BLOOMBERG` in `identifier_namespace` values. That is contract
     0.4.0, the CTO's carrier; until it lands, `--write` refuses;
     (c) a `--half <path>` names a half whose CTO section reads SIGNED.
   - Run the dry run and record its counts.
4. **The half.** `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_FWD9_ROWS_20261005.md`,
   in the shape of the earlier row halves in that folder (for example
   `NEVER_WIDEN_HALF_REQUEST_MULTI_ASSET_ROWS_AND_REMINT_20261003.md`):
   - the write set (the set file and its counts);
   - writers counted, both branches (all puts land / a put meets an existing row);
   - rollback per key (a delete, on Andrew's word only);
   - the three refusal preconditions above;
   - a `## COO half` section left UNSIGNED for the issuer.

### ACCEPTANCE

<criterion id="SC7-e17-AC1" cell_refs="SC-e-17"><invocation>python -m pytest -q infra/aws/lambda/v2_portal/_shared/tests/test_rivalfunds_classification.py</invocation><expect>passed</expect></criterion>
`SC7-e17-AC1` -- the mapping module implements Q1, Q3 and Q4 and its tests pass.

<criterion id="SC7-e17-AC2" cell_refs="SC-e-17"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R7_CHECKS/r7_fwd9_row_set.py</invocation><expect>FWD9-ROW-SET securities=</expect></criterion>
`SC7-e17-AC2` -- the whole universe is read against the table, one line per security.

<criterion id="SC7-e17-AC3" cell_refs="SC-e-17"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R20_CHECKS/r20_half_ready.py org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_FWD9_ROWS_20261005.md</invocation><expect>HALF-READY</expect></criterion>
`SC7-e17-AC3` -- the rows half is ready for the issuer's signature.

<expected_criteria>SC7-e17-AC1,SC7-e17-AC2,SC7-e17-AC3</expected_criteria>

Dry-run at the base 2026-10-05: all three FAIL as expected (no module, no row-set script, no half).

**Import note (1.0.0_SA_CTO DECISION 103371):** the new module is not imported by any runner-deployed script in this cell
(`SC-e-19` imports it later, with its own deployed-layout criterion), so the criterion does not apply here.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`,
  uncommitted.
- **No table write.** Live reads only. The dry run is the cell's only "write" path, and it puts nothing.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `MDPF_SECCLASS-W14-S<k>`), and do not weaken the test.

<paths>
infra/aws/lambda/v2_portal/_shared/rivalfunds_classification.py
infra/aws/lambda/v2_portal/_shared/tests/test_rivalfunds_classification.py
infra/aws/lambda/v2_portal/_shared/etf_classification_scheduled.py
infra/aws/lambda/v2_portal/_shared/tests/test_etf_classification_scheduled.py
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R7_CHECKS/r7_fwd9_row_set.py
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R7_CHECKS/FWD9_ROW_SET_20261005.tsv
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R7_CHECKS/r7_fwd9_write.py
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_FWD9_ROWS_20261005.md
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R7.md</decomp_doc> (round 7), cell `SC-e-17`.
<owned_cells>SC-e-17</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC7-e17-AC1, SC7-e17-AC2, SC7-e17-AC3. Instance at `org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~14/MDPF_SECCLASS.TO-SC-e17.fwd9-rows-mapping-and-dry-run.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> SC7-e17-AC1,SC7-e17-AC2,SC7-e17-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** the row-set line, the dry run's counts, the PRESENT-DIFFERS keys, the half's path, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule change.
comp-iam: DECLARED-NOT-APPLICABLE -- reads with the operator profile; no write.
comp-adversary: RUN -- the universe census (intake @320b02aa6b: 822 securities, 516 non-US with no ISIN or CUSIP), the vocabulary read (equity sub-classes include Developed / EM / International / Global and GICS sectors), the contract read (identifier_namespace TICKER/CUSIP only: the ACT waits on contract 0.4.0); BLIND: how many US rows exist with a different class (the row set measures PRESENT-DIFFERS).
lane: the <paths> block IS the grant.
</preflight>

Source: PRD v0.3 FWD-9 @ffb329af49; RULINGS batch 257 Q1, Q3, Q4 @a272c26a75; intake @320b02aa6b.

## AMENDMENT 1 (2.0.0_SA_COO~M, 2026-10-05 ~10:0xZ) -- three fixes before the rows half is signed

On the worker report @d2cc117df4 (drained @92f65008d6: AC1 14 passed, AC2 `FWD9-ROW-SET securities=1051 write=664
present_same=11 present_differs=106 out=270`, AC3 HALF-READY) and the rows it and SC-e-16 filed. The cell re-opens (`<status>`
issued). The criteria are UNCHANGED (AC1, AC2, AC3); the grant gains the shared writer and its test file (`<paths>` above).

1. **One writer path (W13-S2, W14-S2).** `infra/aws/lambda/v2_portal/_shared/etf_classification_scheduled.py`
   `_WRITE_FIELDS` gains `security_bloomberg` and `listing_country`. Contract 0.4.0 @a8bca9d398 requires `security_bloomberg`
   on BLOOMBERG rows; `listing_country` is ISO 3166-1 alpha-2. Remove the writer's table wrapper, so `r7_fwd9_write.py` and
   SC-e-19's producer write through the same `write()`. In `infra/aws/lambda/v2_portal/_shared/tests/test_etf_classification_scheduled.py`,
   assert that both fields pass through `write()` on a BLOOMBERG row (table stubbed), and that a TICKER row is unchanged.
2. **No name on BLOOMBERG rows (W13-S1).** A BBG row carrying `name` is listed by the comparison catalogue under a key
   `maintained_sources._classified_etf` refuses. The module's BLOOMBERG items carry no `name`; `security_bloomberg` stays the
   human-readable id. Add a test.
3. **Money-market funds are cash, not stocks (W14-S3).** A US listing whose ticker is five letters ending `XX` is a money-market
   fund, a cash equivalent. It is OUT under Q4's "non-cash" (AGPXX, CMQXX, DGCXX, DGVXX, FTIXX, GVMXX, IJGXX today). Add a
   test.
4. **Q4 widening (W14-S1).** This is asked of 1.0.0_SA_CTO at 09:55Z: provider type Equity OR empty.
   - If the ruling lands before you regenerate the set, apply it in the module, with a test.
   - If not, regenerate without it and say so in the report.

Then regenerate `FWD9_ROW_SET_20261005.tsv` (reuse your `.scratch` read cache where the inputs are unchanged), re-run the dry
run and refresh the half's counts. Re-validate the proof (AC1-AC3) and flip `<status>` back to complete.

Gate limb: none graded this modification. It modifies an existing order; LIMB 6 fires on new orders only, and no
placeholders are declared.

## AMENDMENT 2 (2.0.0_SA_COO~M, 2026-10-05 ~10:1xZ) -- the Q4 ruling is in: apply item 4

1.0.0_SA_CTO RULINGS.md batch 259 section 2 @a9d4220969 (msg 105235) answers item 4. Apply it in the module, with tests:
- **A stock is** non-cash, AND its `security_bloomberg` final token (the yellow key) is `Equity`, AND its
  `provider_security_type` is `Equity` or empty.
- An empty provider type with any other yellow key (`Index`, `Curncy`, `Corp`, `Govt`, `Comdty` or any other) stays OUT, and
  the row set names its key in the OUT reason.
- **`instrument_kind`:** a security that already has a table row keeps its `instrument_kind` (the row set never overwrites).
  A new Equity-keyed row with no fund signal is `single_security`. An exchange-traded fund held inside a fund is a fund
  wherever the table or the input already says so.
- The row-set script also prints OUT by reason, one line per reason: `FWD9-OUT reason=<reason> n=<n>`.

Criteria unchanged (AC1-AC3). Gate limb: none graded this modification (LIMB 6 fires on new orders only; no placeholders).
