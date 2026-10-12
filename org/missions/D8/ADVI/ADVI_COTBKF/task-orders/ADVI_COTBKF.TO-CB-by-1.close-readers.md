# TO ADVI_COTBKF.TO-CB-by-1.close-readers -- round 77 CB-by-1: who reads the affected closes: the store and key of the 15 failing funds, every reader in the workspace and the portal classed, and one read per serving reader

<to_id>ADVI_COTBKF.TO-CB-by-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~143</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>77</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** dell2 (placement DELL2) | **Decomp cell:** `CB-by-1` (`decompositions/ADVI_COTBKF_DECOMP.round77.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**This is a CENSUS of code and one read per serving reader. You change no code. Nothing is fetched, served, applied or written
to any bucket.**

**Read first:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_77_20261011.md` whole, and above all section 2 ("A close at three quarters of the traded price is a LEVEL error. Every value
and every weight built from that close for those funds is low by the same proportion on every day it applies, not only on trade days.
... is a value or a weight built from the affected close SERVED to anyone, and where." and "This project's own table is read by nothing
released. That says nothing about the PRICE STORE the closes sit in, which this project did not build and does not own alone.") and
section 3 item 1; the round-76 records `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~140/FUNDS_BY_TRADES.json` (the 15 failing funds, key `named`) and `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~139/PRICE_PAID.json` (the price-paid instrument; the
build's `store` column says which price store each close came from); the build's own list of the price stores it reads,
`data/assets/scripts/analysis/commonwealth_price_census.py` lines 50 to 80, and `data/assets/scripts/silver/commonwealth_daily_valuation.py`
(how a close reaches the build, and by which key).

**Your item.**

1. **The store and the key.** For each of the 15 failing funds: the price store its closes are read from in the build (the `store`
   column of `C:/dev/ajb_workspace/.scratch/advi_cotbkf/r34/after/security_day_price.parquet`), the key it is read by (a ticker or a CUSIP), and the address of that
   store as the code names it (quoted from the code, with file and line; you type no address of your own). How many of the 15 sit
   in each store.
2. **The census of readers, with its denominator.** Every reader of that store (and of any store carrying the same closes
   downstream: say how you established "downstream") in the WORKSPACE and in the PORTAL (`portal/`). Use the estate's own search
   tools (`comp-find`, `comp-which`, the dependency graph's query calls named in `org/modules/graph/graph-call-manifest.yaml`), and
   PRINT the denominator of each sweep (files or nodes scanned, the corpus scope) beside its hits; before a zero is read as an
   absence, run the tool's census verb on the path. A reader is a script, a job, a query, a view or a page that takes a price from
   the store. State what the census CANNOT see (a reader outside the two checkouts; a consumer of an export).
3. **Each reader classed:** `serves_a_value`, `serves_a_weight`, `serves_a_return`, `serves_nothing` (a build, a test, an analysis
   script, a dormant or unscheduled path), or `not_established`; with WHAT it serves (the surface: a table, an endpoint, a page),
   TO WHOM (which firm's logins can open it; a staff-only page is said to be staff-only), whether it is scheduled or live, and its
   OWNER (the project code and seat that owns the reader, from the tree, not from memory).
4. **For each reader that serves: ONE READ.** For one failing fund on one day, does the reader's figure use the store's close, or
   another price (a custodian price, a vendor price, a different store)? Read it from the reader's code path first; where the code
   leaves it open, read ONE served value from the artifact the reader produces (a read of one object or one row; reads only) and
   set it beside the store's close and the fund's unadjusted close for that day. Say which of the two you did. No account value is
   written: the figure compared is a PRICE or a ratio.
5. **A reader that serves a figure from an affected close is filed THE SAME HOUR as a surprise row naming its owner,** before you
   finish the rest: one row per such reader, class `OBSERVATION` unless the figure is in front of a client firm today, in which case
   say so plainly in the row's first sentence. You do not message anyone; the row is the carrier, and your report names every row.
6. Write the record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~143/CLOSE_READERS.json` and a short `.md`. Top-level keys, exactly: `failing_funds` (15), `stores` (a list of `{"store",
   "key", "address_as_named_in_code", "funds"}`), `census` (`{"instruments", "denominators", "cannot_see"}`), `readers` (a list of
   `{"reader", "plane", "owner", "class", "serves", "to_whom", "scheduled_or_live", "uses_the_store_close", "one_read"}`),
   `serving_readers`, `serving_from_an_affected_close`, `rows_filed` (a list of row ids), `headline`, `not_established`.

### ACCEPTANCE

<criterion id="CB77by1-AC1" cell_refs="CB-by-1"><invocation>python -c "import json;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~143/CLOSE_READERS.json',encoding='utf-8'));r=d['readers'];c=['serves_a_value','serves_a_weight','serves_a_return','serves_nothing','not_established'];print('CLOSE-READERS failing_funds=%d stores=%d funds_placed=%d readers=%d classed=%d serving=%d one_read=%d serving_from_an_affected_close=%d rows_filed=%d denominators=%d by_class=%s'%(d['failing_funds'],len(d['stores']),sum(x['funds'] for x in d['stores']),len(r),sum(1 for x in r if x['class'] in c),d['serving_readers'],sum(1 for x in r if x['class'].startswith('serves_a') and x['one_read']),d['serving_from_an_affected_close'],len(d['rows_filed']),len(d['census']['denominators']),json.dumps({k:sum(1 for x in r if x['class']==k) for k in c},sort_keys=True)))"</invocation><expect>CLOSE-READERS failing_funds=15</expect></criterion>
`CB77by1-AC1` -- every failing fund is placed in a store; every reader found carries one class (`classed` equals `readers`); every
serving reader has its one read (`one_read` equals `serving`); a row is filed for each reader serving from an affected close.

<criterion id="CB77by1-AC2" cell_refs="CB-by-1" judgment="true"/>
`CB77by1-AC2` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9 and never self-graded: each sweep prints its denominator and a zero is not
read as an absence without the census verb; what the census cannot see is stated; a reader's class and owner are read from the
tree; the one read says whether it came from code or from a served value; a reader serving from an affected close is filed as a
row the same hour and named in the report; no account value appears and no other firm's data is opened.

<expected_criteria>CB77by1-AC1,CB77by1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below (your deliverables folder and your own NEW channel row) and the file of this order.
- **You change no code, test, config, manifest or registry, in the workspace or in the portal.** You read code in both.
- **AWS: READS ONLY, and only the ONE read per serving reader** that step 4 names (one object or one row), plus a read of the graph.
  No list of a bucket the graph holds; no write, no delete; no serve; no `--apply`.
- **Another firm's data is never opened.** Where a reader of the store serves another firm, you record that it exists, its class
  and its owner from the CODE, and you do not read its data or name its accounts. The one read of step 4 is made for THIS project's
  firm only.
- Searches go through the estate's tools (`comp-find`, `comp-which`, the graph's query calls); a recursive shell search of the
  repository is denied by a hook and is not retried another way.
- After your commit run `env -u COTBKF_SWEEPS_CONFIG python -m pytest data/assets/scripts/silver/tests/test_cotbkf_no_account_ids.py -q -s`;
  keep CUSIPs in CSV columns named exactly `cusip` and tickers elsewhere; report its DENOMINATOR line.
- **NEVER `--apply`, `--remint`, `--overwrite`, a serve, or any S3 write or delete against a real bucket.** No push. No `--refresh`.
  **No vendor call and no fetch** (no Yahoo, no Bloomberg, no gateway series pull): what is on disk is read, never refreshed. The
  one read per serving reader is a read of an Opal artifact, not of a vendor.
- A commonwealth script you run carries `COTBKF_SWEEPS_CONFIG=C:/dev/_cotbkf_private_evidence_20261009/config/commonwealth_sweeps.json` in its command line. Do not open or print anything else under that folder.
- Run outputs go under your own worktree `.scratch/` (never committed); nothing under `C:/dev/ajb_workspace/.scratch/advi_cotbkf` is modified.
- **Never print** an account id or an account's value, flow, quantity, share balance or return. Counts, dates, CUSIPs, tickers, a
  security's price or per-share distribution, ratios and reason codes only.
- **No gate override** of any kind and no `--force`. Do not weaken, delete, xfail or skip a test.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row with id
  `ADVI_COTBKF-D2-W143-S<k>` (k from 1), `"fabric": "dell2"`, `surfaced_at` read from the clock, APPENDED to the channel file with
  `open(path, 'a', encoding='utf-8', newline='\n')`; `git diff --numstat` must show added lines only. Never open the channel file with
  an editing tool.

<paths>
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round77.md</decomp_doc> (round 77), cell `CB-by-1`.
<owned_cells>CB-by-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB77by1-AC1, CB77by1-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~143/ADVI_COTBKF.TO-CB-by-1.close-readers.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB77by1-AC1,CB77by1-AC2` BEFORE the flip. Mechanical: CB77by1-AC1. A judgment criterion is recorded as PENDING-ADJUDICATION, never PASS. An artifact already committed and not changed
in the flip commit is pinned to the commit that carried it, never left `PENDING-THIS-COMMIT`.
</proof_of_spec>

**REPORT:** FIRST, before anything else: every reader that serves a figure from an affected close, with its owner, what it serves, to whom, and the row id filed; or the plain statement that none was found. Then: the store, the key and the address as the code names it, per failing fund; each sweep with its instrument and its denominator; what the census cannot see; every reader with its class, what it serves, to whom, scheduled or live, and its owner; for each serving reader the one read, and whether it came from code or from a served value; the `CLOSE-READERS` line; the account-id scan's DENOMINATOR line; what is not established; commits; every gate refusal, verbatim.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a census of code and at most one read per serving reader; nothing is scheduled or served.
comp-iam: DECLARED-NOT-APPLICABLE no lens was run: the cell makes only single reads of an Opal artifact under the existing role; no write, delete or serve, and no new permission.
comp-adversary: RUN -- every sweep prints its denominator, and a zero is not an absence until the census verb has run on the path; what the census cannot see is stated; class and owner are read from the tree; the one read says whether it came from code or from a served value; a reader serving from an affected close is filed as a row the same hour; BLIND: a reader outside the two checkouts, and a consumer of an export the tree does not name.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-77 analysis @1101e06fcd (msg 6154), section 3 item 1; `3.0.0_SA_CVO` round-76 grade file @d299fd357a.
