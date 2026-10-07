# TO ADVI_COTBKF.TO-CB-g-1 -- round 7 CB-g-1: a read-only scanner that lists a prefix to its leaves and finds per-security daily price stores

<to_id>ADVI_COTBKF.TO-CB-g-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~21</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>7</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL2) | **Decomp cell:** `CB-g-1` (`decompositions/ADVI_COTBKF_DECOMP.round7.md`) |
**outcome_ref:** FWD-3 (CB4d1-AC3) | **depends_on:** none

---

## WORKER FACE

### THE CELL

`CB-g-1`, FWD-3: before Opal pulls prices for the 4,634 Commonwealth securities, it must know whether a store it already owns holds a
per-security daily price. Round 4's census graded all 40 buckets but could not list two of them from this box. A two-level listing (run
on the laptop) shows `opal-data-cottonwood` holds `irpt/cottonwood/` and `mdpf/cottonwood/`. The remaining question is whether anything
under `irpt/cottonwood/` (reporting outputs) is a per-security daily price store.

You build `data/assets/scripts/analysis/commonwealth_price_store_scan.py`, a READ-ONLY scanner:
- `--bucket <name> --prefix <p>` (bucket and prefix are arguments; nothing typed in the script beyond argument defaults read from the
  registry -- default bucket = `opal_naming.lookup("cottonwood")["bucket"]`, default prefix `irpt/cottonwood/`);
- lists the prefix to its LEAVES with `list_objects_v2` paginated (no Get on anything but candidate stores' first object); prints the
  denominator: `objects=<n> prefixes=<k> bytes=<b>`;
- names a CANDIDATE price store: a leaf set whose objects are tabular (parquet/csv) and whose first object's columns include a security
  key (cusip or ticker or symbol) AND a date AND a price-like column (close, price, px, adj_close). For each candidate: the date span
  (from partition names or the date column of its first and last object) and the distinct security count of its first object;
- sizes candidates against the census need (`--need 9388961`, default that number) as `security_days_possible`;
- writes ONE JSON file to `--out` and prints as its LAST line exactly:
  `PRICE-STORE-SCAN bucket=<b> prefix=<p> status=<LISTED|DENIED> objects=<n> candidates=<c> security_days_possible=<s> need=<N>`;
- **a denied list is not an empty bucket:** on AccessDenied it prints `status=DENIED objects=0 candidates=0` and exits 3 -- never
  `status=LISTED objects=0`.

**Tests** `data/assets/scripts/analysis/tests/test_commonwealth_price_store_scan.py` (stub S3 client, no AWS): a stub tree with one price
store (cusip, date, close; two date partitions) and one non-price table finds exactly 1 candidate with its span and security count; a stub
that raises AccessDenied prints `status=DENIED` and exits 3 (the difference control against an empty-but-listed prefix, which prints
`status=LISTED objects=0` and exits 0).

On this box (dell2) the real bucket is denied to you; the criterion below proves the denied branch on the real bucket. The real listing
runs on the laptop after the drain (the issuer relays it).

### ACCEPTANCE

<criterion id="CB7g1-AC1" cell_refs="CB-g-1"><invocation>python -m pytest -q data/assets/scripts/analysis/tests/test_commonwealth_price_store_scan.py</invocation><expect>passed</expect></criterion>
`CB7g1-AC1` -- candidate detection and the denied-vs-empty control on stubs.

<criterion id="CB7g1-AC2" cell_refs="CB-g-1"><invocation>python data/assets/scripts/analysis/commonwealth_price_store_scan.py --out .scratch/advi_cotbkf/price_store_scan_dell2</invocation><expect>PRICE-STORE-SCAN bucket=opal-data-cottonwood prefix=irpt/cottonwood/ status=DENIED</expect></criterion>
`CB7g1-AC2` -- the real bucket from dell2: denied, and said so.

<expected_criteria>CB7g1-AC1,CB7g1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scratch under `.scratch/`, uncommitted.
- **Read-only.** No Put, no Delete, no policy read or change. Never try to widen a fence.
- **Rule 13:** a DS-lane script; your commit is a candidate.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `ADVI_COTBKF-W21-S<k>`), and do not weaken the test.

<paths>
data/assets/scripts/analysis/commonwealth_price_store_scan.py
data/assets/scripts/analysis/tests/test_commonwealth_price_store_scan.py
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round7.md</decomp_doc> (round 7), cell `CB-g-1`.
<owned_cells>CB-g-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB7g1-AC1, CB7g1-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~21/ADVI_COTBKF.TO-CB-g-1.price-store-scan.proof_of_spec.json`, validated with
`python .tools/proof-of-spec-check.py <instance> CB7g1-AC1,CB7g1-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the PRICE-STORE-SCAN line, the test names and count, the exact command the laptop should run, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a one-time read.
comp-iam: RUN -- the dell2 identity is denied List on opal-data-cottonwood (row S12, measured); denominator 1 bucket; BLIND: the laptop identity's grants (the relay runs there).
comp-adversary: RUN -- a denied list must never read as an empty store (the difference control); bucket from the registry; BLIND: stores outside S3.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-6 analysis @1c9c98e652, E1; rows S12, S15, W12-S2; CVO grade CB4d1-AC3.
