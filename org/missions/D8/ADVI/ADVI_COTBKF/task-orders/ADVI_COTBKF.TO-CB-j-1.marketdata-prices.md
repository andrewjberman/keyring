# TO ADVI_COTBKF.TO-CB-j-1 -- round 10 CB-j-1: find marketdata's historical-price output and, if it is in a non-firm bucket, census it against the need

<to_id>ADVI_COTBKF.TO-CB-j-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~26</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>10</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL2) | **Decomp cell:** `CB-j-1` (`decompositions/ADVI_COTBKF_DECOMP.round10.md`) |
**outcome_ref:** FWD-3 (CB4d1-AC3) | **depends_on:** none

---

## WORKER FACE

### THE CELL

`CB-j-1`, FWD-3: the Commonwealth backfill needs daily prices for 4,634 securities over 9,388,961 security-days. Opal's six known price
stores cover 1,720 securities and 1,297,651 security-days; the Cottonwood firm bucket holds none. Opal also runs a `marketdata` system
whose registry rows (`infra/logic/registry/resources.json`, `"system": "marketdata"`) include `historical-prices-daily` (an EventBridge
rule), `historical-prices-yfinance` (a Lambda) and `historical-prices-fetcher` (an EC2 instance). Nobody has read where they write.

Build `data/assets/scripts/analysis/commonwealth_marketdata_prices.py`, read-only, which:
1. **Locates the output.** Read the Lambda `historical-prices-yfinance`'s configuration (`lambda.get_function_configuration`: env vars)
   and the repo source that builds it (find it by its name), and name the bucket and prefix it writes. **NEVER invoke the Lambda, run
   the fetcher, or call Yahoo or any vendor** -- that is egress off Opal infrastructure and needs Andrew's word. Read only.
2. **Grades the bucket** from `infra/logic/registry/scopes.json` exactly as round 4's census did: a bucket of a FIRM scope (or any of
   its `bucket`-plane aliases) is BARRED and is never listed, headed or read -- not once; any other bucket is USABLE. Count S3 calls under
   a BARRED bucket with a client wrapper (`barred_read`), never assert it.
3. **If USABLE, censuses it**: list the prefix (paginated, denominator printed), read the price store's security key (cusip, ticker or
   symbol) and dates, and match against the Commonwealth universe exactly as round 4's census does (reuse
   `data/assets/scripts/analysis/commonwealth_price_census.py`'s universe and matching functions by import; do not copy them):
   securities priced, security-days covered, and the GAIN over the six stores (securities and security-days not already covered).
4. Writes `MARKETDATA_PRICES.json` and a short `.md` to `--out`, and prints as its LAST line exactly:
   `MARKETDATA-PRICES writer=<function> bucket=<b> prefix=<p> grade=<USABLE|BARRED|NOT_FOUND> barred_read=<k> securities=<s> security_days=<d> gain_securities=<gs> gain_security_days=<gd> need=9388961`.
   If the output cannot be located from configuration and source, print `grade=NOT_FOUND` with zeros, and say what was read.

**Tests** `data/assets/scripts/analysis/tests/test_commonwealth_marketdata_prices.py` (stubs, no AWS): a stub function configuration
naming a non-firm bucket grades USABLE and censuses a stub store (2 securities, 3 dates) into the expected counts; one naming a FIRM bucket
(from a stub registry) grades BARRED with `barred_read=0` while the same stub counts a call under a USABLE bucket (the difference
control); a stub with no locatable output prints `grade=NOT_FOUND`.

### ACCEPTANCE

<criterion id="CB10j1-AC1" cell_refs="CB-j-1"><invocation>python -m pytest -q data/assets/scripts/analysis/tests/test_commonwealth_marketdata_prices.py</invocation><expect>passed</expect></criterion>
`CB10j1-AC1` -- locating, grading and the barred-call control on stubs.

<criterion id="CB10j1-AC2" cell_refs="CB-j-1"><invocation>python data/assets/scripts/analysis/commonwealth_marketdata_prices.py --out org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~26</invocation><expect>barred_read=0</expect></criterion>
`CB10j1-AC2` -- the real function and store: located and graded, nothing read under a firm bucket; the counts on the same line are
recorded, not presumed.

<expected_criteria>CB10j1-AC1,CB10j1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scratch under `.scratch/`, uncommitted.
- **Read-only.** No invoke, no S3 write, no vendor call, no Lambda or rule change. No read of any FIRM bucket.
- **No typed bucket or key** in the script: the bucket comes from the function's configuration or source, graded by the registry.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `ADVI_COTBKF-W26-S<k>`), and do not weaken the test.

<paths>
data/assets/scripts/analysis/commonwealth_marketdata_prices.py
data/assets/scripts/analysis/tests/test_commonwealth_marketdata_prices.py
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round10.md</decomp_doc> (round 10), cell `CB-j-1`.
<owned_cells>CB-j-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB10j1-AC1, CB10j1-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~26/ADVI_COTBKF.TO-CB-j-1.marketdata-prices.proof_of_spec.json`, validated
with `python .tools/proof-of-spec-check.py <instance> CB10j1-AC1,CB10j1-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the MARKETDATA-PRICES line, how the output was located (config key or source file:line), the grade's registry basis, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a one-time read; the schedule historical-prices-daily is read, never changed.
comp-iam: RUN -- reads Lambda configuration and S3 under the dell2 identity; FIRM buckets never read, counted by a client wrapper; denominator 1 function; BLIND: the EC2 fetcher's own output if it differs from the Lambda's.
comp-adversary: RUN -- no invoke and no vendor call (egress needs Andrew's word); the grade is the registry's; matching reused by import; BLIND: price stores outside AWS.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` analysis correction @283b15713f (msg 485); rows S17, S19, S20.
