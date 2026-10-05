# TO MDPF_SECCLASS.TO-SC-e18 -- round 7 SC-e-18: FWD-9 history coverage -- each Rival Funds stock's G4 security_market series against the three-year window

<to_id>MDPF_SECCLASS.TO-SC-e18</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~15</issued_to>
<issued_by>2.0.0_SA_COO~M</issued_by>
<issued_date>2026-10-05</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>7</round>
<workstream>~M</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `SC-e-18` (`decompositions/MDPF_SECCLASS_DECOMP_R7.md`) |
**outcome_ref:** FWD-9 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`SC-e-18`. FWD-9's second half: each Rival Funds stock's "history is filled in back three years (or to its first trading day,
if it is younger) ... no history reaches further back than three years" (PRD
`org/missions/D8/MDPF/MDPF_SECCLASS/prd/MDPF_SECCLASS_PRD.md` v0.3).
- PRD C-BACKFILL defines history as the series a holding's modal reads for that security.
- The one such dialog is Rival Funds' (`data/etfs/scripts/rivalfunds/render.py:1321-1368`). It reads G4 `security_market`
  (`px_close`, `total_return_index`; `data/etfs/scripts/rivalfunds/gold_holding_contribution.py:224-233, :666`) at
  `s3://opal-data-etfs/rivalfunds/etfs/gold/security_market/date=<D>/market-<rev>.parquet`.
- The writer is ETFS_RIVALS' `data/etfs/scripts/rivalfunds/enrichment_bloomberg.py` at site Z (Bloomberg; `backfill` mode
  `:595-597`).
- 1.0.0_SA_CTO RULINGS batch 257 Q2: **history is site Z's input. This project READS coverage and routes the gaps; it writes
  no series.**

**Build (read-only):**
1. **The universe.** The FWD-9 stocks: non-cash `provider_security_type == "Equity"` across every
   `s3://opal-data-etfs/rivalfunds/etfs/gold/canonical_shape/date=<d>/holdings-<rev>.parquet` (newest revision per day),
   one per `security_bloomberg`. 805 are expected (822 less 17 `Index` futures). Use column-pruned reads
   (`pyarrow.fs.S3FileSystem`, retries); the laptop link is slow.
2. **The series.** Read `security_market` across its partitions with the same pruning. Measure first:
   - its partition dates and its identity column (the key that joins to canonical_shape: `security_id` or
     `security_bloomberg`; read it, do not assume);
   - for each FWD-9 stock, the first and last date with a non-null `px_close`.
3. **The window.**
   - The target start is `max(run_day - 3 years, first trading day)`.
   - The first trading day is not knowable from this table alone. Where the series starts after `run_day - 3 years`, report
     it as `STARTS-LATE` with its first date, and never call it a gap you cannot prove.
   - A stock with no series is `NO-SERIES`. One whose series reaches further back than 3 years is `BEYOND-CAP` (FWD-9's
     "no history reaches further back than three years": report it, change nothing).
4. **The check.** `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R7_CHECKS/r7_fwd9_history_coverage.py`.
   - It writes `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R7_FWD9_HISTORY_COVERAGE_20261005.json`: per
     stock `{security_bloomberg, first, last, status}`, plus the partition census.
   - It prints `FWD9-HISTORY-COVERAGE stocks=<n> covered_3y=<n> starts_late=<n> no_series=<n> beyond_cap=<n> security_market_partitions=<n> first_partition=<d>`.

### ACCEPTANCE

<criterion id="SC7-e18-AC1" cell_refs="SC-e-18"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R7_CHECKS/r7_fwd9_history_coverage.py</invocation><expect>FWD9-HISTORY-COVERAGE stocks=</expect></criterion>
`SC7-e18-AC1` -- every FWD-9 stock's history coverage is read against the three-year window, one status each.

<expected_criteria>SC7-e18-AC1</expected_criteria>

Dry-run at the base 2026-10-05: no such check yet, so AC1 FAILS as expected.

**Routing:** gaps are not this cell's to fill. Report the counts and the NO-SERIES / STARTS-LATE lists. The issuer routes them
to site Z through `0.0.0_AB_MSTR` (batch 257 Q2).

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`,
  uncommitted.
- **Read-only.** No S3 or table write. No Bloomberg or other vendor call: a vendor needs Andrew's per-use word, and this cell
  needs none.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `MDPF_SECCLASS-W15-S<k>`), and do not weaken the check.

<paths>
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R7_CHECKS/r7_fwd9_history_coverage.py
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R7_FWD9_HISTORY_COVERAGE_20261005.json
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R7.md</decomp_doc> (round 7), cell `SC-e-18`.
<owned_cells>SC-e-18</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC7-e18-AC1. Instance at `org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~15/MDPF_SECCLASS.TO-SC-e18.fwd9-history-coverage.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> SC7-e18-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** the coverage line, the security_market partition census, the NO-SERIES and STARTS-LATE lists, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule change.
comp-iam: DECLARED-NOT-APPLICABLE -- operator read of opal-data-etfs (read at issue: canonical_shape listed and read 2026-10-05).
comp-adversary: RUN -- the history source (render.py:1321-1368 -> G4 security_market), the producer at site Z (enrichment_bloomberg.py, 730-day default), the window rule (FWD-9 ACCEPT); BLIND: security_market's identity column and partition depth (step 2 measures them).
lane: the <paths> block IS the grant.
</preflight>

Source: PRD v0.3 FWD-9, C-BACKFILL @ffb329af49; RULINGS batch 257 Q2 @a272c26a75; intake @320b02aa6b.
