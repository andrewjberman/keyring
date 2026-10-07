# TO ADVI_COTBKF.TO-CB-d-1 -- round 4 CB-d-1: the price census complete over every bucket, graded USABLE / BARRED, legacy stores read only through the registry

<to_id>ADVI_COTBKF.TO-CB-d-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~12</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-07</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>4</round>
<workstream>~C</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `CB-d-1` (`decompositions/ADVI_COTBKF_DECOMP.round4.md`) | **outcome_ref:** FWD-3 |
**depends_on:** none (the six legacy registry rows landed @4991b8b11b)

---

## WORKER FACE

### THE CELL

`CB-d-1`, FWD-3: before any price is pulled for the Commonwealth securities, Opal knows which of its own stores already price them -- and
which stores it may not touch. Round 2's census (`data/assets/scripts/analysis/commonwealth_price_coverage.py`) read stores in 10 of the 40
buckets, read two other firms' price files, and missed a third firm's position table. You rebuild it to be COMPLETE and LAWFUL. You write
NOTHING to S3.

**The law (CTO rulings 1 and 2, `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_ADVI_COTBKF_R2_R3_20261007.md`):**
- A Cottonwood pipeline never reads another firm's store, for prices or anything else, even though a closing price is public.
- A new script reads an address only as builder output: `lib/opal_naming.address(...)` for canon stores, and for a store that predates
  the canon, `lib/opal_naming.legacy_address(<key>, **params)` (rows in `infra/logic/registry/legacy_addresses.json`). A file under `org/`
  is evidence, never configuration: the script's `--stores` read of
  `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~6/PRICE_COVERAGE_STORES_20261006.json` is REMOVED.

**The file.** Build the census as a NEW script `data/assets/scripts/analysis/commonwealth_price_census.py` and DELETE
`commonwealth_price_coverage.py` and its test `data/assets/scripts/analysis/tests/test_commonwealth_price_coverage.py` in the same commit
(move the matching functions and the tests you keep into the new files; one script, never two -- no shadow).

**The grading (every bucket, derived, never typed):** list every bucket in the account (`s3.list_buckets()`; 40 at the cut). Read the
firms from `infra/logic/registry/scopes.json`: every scope with `class == "FIRM"`, its `bucket`, and every alias whose `planes` include
`bucket` (today: `49financial` -> `opal-data-49financial`, `opal-data-bd`; `inflection` -> `opal-data-inf`; `cottonwood` ->
`opal-data-cottonwood`, `opal-data-cot`). A bucket of a FIRM other than `cottonwood` is **BARRED**: listed by name, its known price or
position stores named (at least `opal-data-49financial` `gold/advi/canonical/canonical_positions/date=<d>/data.parquet`, which the CVO
found and round 2 missed, and the bd/inf `canonical_prices` and `historical_prices` files), and **never opened -- no List, Head or Get
under it**. Every other bucket is **USABLE**: Cottonwood's own, or no firm in its address.

**The USABLE price stores read (the six legacy rows, exact calls):**
`legacy_address('cottonwood-silver-canonical-prices')`, `legacy_address('cottonwood-gold-canonical-holdings', date='YYYY-MM-DD')` (a
custodian mark on a held position is a close for that security on that day), `legacy_address('rivalfunds-etfs-gold-security-market')`
(prefix), `legacy_address('etfs-bbg-testpull-ticker-history', ticker=...)`, `legacy_address('etfs-bbg-fund-daily', date=...)`,
`legacy_address('portal-canon-return-daily-values')` (prefix). A USABLE bucket with no price store gets one line saying what it holds
(listing its top-level prefixes is enough). Keep round 2's matching (CUSIP first, ticker second, a reused symbol not credited) and its
universe (`address('commonwealth', <cottonwood scope via lookup>, 'silver', 'transactions', 'date=2026-06-23')`, 4,634 CUSIPs).

**Output:** the JSON and markdown results in your deliverables folder (one row per bucket: name, grade, firm, stores read, securities
priced), and as the LAST stdout line exactly:
`PRICE-CENSUS buckets=<n> every_bucket_graded=<True|False> barred_read=<k> usable=<u> barred=<b> universe=<N> priced_any=<s> priced_fixed_income=<f> security_days_covered=<c> security_days_needed=<d>`
where `barred_read` counts S3 calls made under a BARRED bucket (it must be 0, counted by a wrapper around the client, not asserted).

**Tests** `data/assets/scripts/analysis/tests/test_commonwealth_price_census.py` (stub S3 client, no AWS): a fake registry with two firms
grades their buckets and aliases BARRED and a no-firm bucket USABLE; the run makes ZERO calls under a BARRED bucket while a USABLE one is
read (the difference control: the same stub counts calls under each); an unknown legacy key raises; no `--stores` argument remains.

**Run time.** The real run reads large price files: a cold read took 5 to 19 minutes in round 2. Warm a cache under `.scratch/` once (untimed),
then run the criterion within its 120 s; say so in the report.

### ACCEPTANCE

<criterion id="CB4d1-AC1" cell_refs="CB-d-1"><invocation>python -m pytest -q data/assets/scripts/analysis/tests/test_commonwealth_price_census.py</invocation><expect>passed</expect></criterion>
`CB4d1-AC1` -- the grading and the zero-calls-under-BARRED control on a stub.

<criterion id="CB4d1-AC2" cell_refs="CB-d-1"><invocation>python data/assets/scripts/analysis/commonwealth_price_census.py</invocation><expect>PRICE-CENSUS buckets=40 every_bucket_graded=True barred_read=0</expect></criterion>
`CB4d1-AC2` -- the real account: 40 of 40 buckets graded, no call under a BARRED bucket.

<criterion id="CB4d1-AC3" cell_refs="CB-d-1" judgment="true"/>
`CB4d1-AC3` -- JUDGMENT, graded by `3.0.0_SA_CVO` at L9: the census is complete (no unnamed store that holds a per-security daily price in
a USABLE bucket) and every BARRED grade is the registry's, not the seat's.

<expected_criteria>CB4d1-AC1,CB4d1-AC2,CB4d1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Caches under `.scratch/`, uncommitted.
- **No S3 write.** S3 reads of USABLE stores only; NOTHING under `opal-data-bd`, `opal-data-inf`, `opal-data-49financial` (or any other
  FIRM bucket but Cottonwood's) -- not a list, not a head.
- **No typed bucket or key** in the script: the naming gate refuses them, and the registry is the source.
- **Rule 13:** a DS-lane script; your commit is a candidate.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `ADVI_COTBKF-W12-S<k>`), and do not weaken the test.

<paths>
data/assets/scripts/analysis/commonwealth_price_census.py
data/assets/scripts/analysis/commonwealth_price_coverage.py
data/assets/scripts/analysis/tests/test_commonwealth_price_coverage.py
data/assets/scripts/analysis/tests/test_commonwealth_price_census.py
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round4.md</decomp_doc> (round 4), cell `CB-d-1`.
<owned_cells>CB-d-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB4d1-AC1, CB4d1-AC2, CB4d1-AC3 (judgment: UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming 3.0.0_SA_CVO; never PASS or
FAIL). Instance at `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~12/ADVI_COTBKF.TO-CB-d-1.price-census.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB4d1-AC1,CB4d1-AC2,CB4d1-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** the `PRICE-CENSUS` line, the BARRED list with the firm each belongs to, priced counts by asset type against round 2's, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a one-time measurement.
comp-iam: DECLARED-NOT-APPLICABLE no IAM change; reads under the laptop profile.
comp-adversary: RUN -- cross-firm (BARRED buckets never opened, counted by a client wrapper, not asserted); rule 30 (legacy_address only); BLIND: price stores outside S3 (Bloomberg at site Z, Yahoo) -- the sources Andrew approved for the pull, not this census.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: CTO analysis rulings 1-2 (msg 105940); CVO grade CB2b3-AC3 NOT MET; rows W6-S2, W6-S5; CRO legacy rows @4991b8b11b (msg 105953).
