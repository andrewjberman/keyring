# TO ADVI_COTBKF.TO-CB-bz-2.store-unadjusted-field -- round 78 CB-bz-2: for each of the 15 funds, the store's field that holds the unadjusted close, and whether it is present for every date the back-fill reads

<to_id>ADVI_COTBKF.TO-CB-bz-2</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~149</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-12</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>78</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** dell2 (placement DELL2) | **Decomp cell:** `CB-bz-2` (`decompositions/ADVI_COTBKF_DECOMP.round78.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**This is a READ of code, of local copies, and of ONE store object's schema and rows for this firm. You change no code. Nothing is
fetched from a vendor; nothing is written to any bucket.**

**Read first:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_78_20261012.md` section 3 item 2 ("For each of the 15 funds, the store's field that holds the unadjusted close, and whether
it is present for every date the back-fill reads: counts and date ranges per fund, the denominator printed. 14 of 15 already
reproduce the price paid from the cache; the fifteenth is named with what it lacks.") and the sentence after the list (the addendum
it serves "names the price basis per fund class, makes the minted table carry its basis in a field a reader can reject on"); the
round-77 records `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~144/FAILING_FUNDS.json` (the 15; each holds an unadjusted close in the LOCAL VENDOR CACHE, 2020-06-29 to 2026-10-08; 14 pass
against the price paid, VGHAX too few) and `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~143/CLOSE_READERS.json` (the store: the firm's silver canonical prices, key = ticker, its address as
the code names it, its writer `data/cot/scripts/gold/build_canonical_prices_v2.py`, unscheduled).

**The question.** The cache is a file on one box. The STORE is what a build reads. Does the store itself hold an unadjusted close for
these funds, in which field, and for which dates; or does it hold only the adjusted series, so that a corrected basis has to come
from somewhere the store does not have?

**Your item.**

1. **The store's fields, from its writer and from the store.** From the writer's code, with file and line: which vendor field
   becomes the store's price for a mutual fund (an adjusted close? an unadjusted one?), which other fields it writes, and what the
   `source` values mean. From the store itself: its schema (every column and type) -- from the local copy if it carries the schema,
   else from ONE read of the store object for this firm (its footer and the rows of the 15 tickers only). State which you read and
   the object's last-modified time.
2. **Is an unadjusted close in the store?** For each of the 15 funds: the field (if any) that holds it; the dates it is present
   on (count, first, last); and, set beside the local vendor cache's unadjusted close on common dates, whether it IS that series
   (the share of dates equal within 0.1 percent). If the store has no such field, say so in one sentence and name the fields it
   does have.
3. **The dates the back-fill reads.** For each fund: its held dates in the build (the dates the served table values it), with the
   count; of them, the dates on which an unadjusted close is present (a) in the store's field, if there is one, and (b) in the
   local vendor cache; the first and last uncovered date and the count uncovered, split into non-trading days the build
   interpolates and trading days. The denominator printed per fund and in total.
4. **The fifteenth:** VGHAX, named with what it lacks (a field, dates, or trades to test it on), from the records and your reads.
5. **Where the Tier-2 input lands,** as a pointer only: which upstream landing the writer reads the vendor series from (file and
   line), and whether that landing keeps the unadjusted field even if the store drops it. A code read; open no landing.
6. Write the record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~149/STORE_UNADJUSTED_FIELD.json`, a `.csv` (columns: cusip, ticker, store_field, store_dates, store_first, store_last, held_dates,
   held_covered_by_store, held_covered_by_cache, uncovered_trading_days, first_uncovered, last_uncovered; CUSIPs only in the
   column named exactly `cusip`) and a short `.md`. Top-level keys, exactly: `store` (`{"address_as_named_in_code", "schema",
   "read_from", "last_modified"}`), `writer` (`{"file_line", "vendor_field_for_a_fund", "fields_written"}`),
   `store_holds_an_unadjusted_close` (true, false or `not_established`), `funds` (15), `with_a_store_field`, `by_fund` (a list of
   15), `held_dates_total`, `covered_by_store_total`, `covered_by_cache_total`, `uncovered_trading_days_total`, `the_fifteenth`,
   `upstream_landing`, `headline`, `not_established`.

### ACCEPTANCE

<criterion id="CB78bz2-AC1" cell_refs="CB-bz-2"><invocation>python -c "import json;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~149/STORE_UNADJUSTED_FIELD.json',encoding='utf-8'));print('STORE-FIELD funds=%d listed=%d store_holds_an_unadjusted_close=%s with_a_store_field=%d schema_columns=%d read_from=%s held_dates_total=%d covered_by_store_total=%d covered_by_cache_total=%d uncovered_trading_days_total=%d the_fifteenth=%s'%(d['funds'],len(d['by_fund']),d['store_holds_an_unadjusted_close'],d['with_a_store_field'],len(d['store']['schema']),str(d['store']['read_from'])[:40],d['held_dates_total'],d['covered_by_store_total'],d['covered_by_cache_total'],d['uncovered_trading_days_total'],str(d['the_fifteenth'])[:60]))"</invocation><expect>STORE-FIELD funds=15 listed=15</expect></criterion>
`CB78bz2-AC1` -- the store's schema is read and each of the 15 funds carries its store field (or none), its held dates and what
covers them. The issuer reads whether the store holds an unadjusted close at all.

<criterion id="CB78bz2-AC2" cell_refs="CB-bz-2" judgment="true"/>
`CB78bz2-AC2` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9 and never self-graded: the store's fields are read from the store and its
writer, not inferred from the cache; "present" is counted against the dates the back-fill reads, with the denominator; a field
that exists and does not match the unadjusted series is said to be that; the cache is not called the store; no account id appears
and no other firm's data is opened.

<expected_criteria>CB78bz2-AC1,CB78bz2-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below (your deliverables folder and your own NEW channel row) and the file of this order.
- **You change no code, test, config, manifest or registry.**
- **AWS: at most ONE read, read-only, of the one store object for THIS project's firm** (its schema and the rows of the 15 tickers),
  and only if the local copy does not carry the schema. No listing, no write, no delete, no serve.
- **Another firm's data is never opened.** No account id: this cell reads prices, dates and tickers only.
- After your commit run `env -u COTBKF_SWEEPS_CONFIG python -m pytest data/assets/scripts/silver/tests/test_cotbkf_no_account_ids.py -q -s`;
  keep CUSIPs in CSV columns named exactly `cusip` and tickers elsewhere; report its DENOMINATOR line.
- **NEVER `--apply`, `--remint`, `--overwrite`, a serve, or any S3 write or delete against a real bucket.** No push. No `--refresh`.
  **No vendor call and no fetch** (no Yahoo, no Bloomberg, no gateway series pull): what is on disk is read, never refreshed. The
  one store read is a read of an Opal artifact, not of a vendor.
- A commonwealth script you run carries `COTBKF_SWEEPS_CONFIG=C:/dev/_cotbkf_private_evidence_20261009/config/commonwealth_sweeps.json` in its command line. Do not open or print anything else under that folder.
- Run outputs go under your own worktree `.scratch/` (never committed); nothing under `C:/dev/ajb_workspace/.scratch/advi_cotbkf` is modified.
- **Never print** an account id or an account's value, flow, quantity, share balance or return. Counts, dates, CUSIPs, tickers, a
  security's price or per-share distribution, ratios and reason codes only.
- **No gate override** of any kind and no `--force`. Do not weaken, delete, xfail or skip a test.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row with id
  `ADVI_COTBKF-D2-W149-S<k>` (k from 1), `"fabric": "dell2"`, `surfaced_at` read from the clock, APPENDED to the channel file with
  `open(path, 'a', encoding='utf-8', newline='\n')`; `git diff --numstat` must show added lines only. Never open the channel file with
  an editing tool.

<paths>
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round78.md</decomp_doc> (round 78), cell `CB-bz-2`.
<owned_cells>CB-bz-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB78bz2-AC1, CB78bz2-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~149/ADVI_COTBKF.TO-CB-bz-2.store-unadjusted-field.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB78bz2-AC1,CB78bz2-AC2` BEFORE the flip. Mechanical: CB78bz2-AC1. A judgment criterion is recorded as PENDING-ADJUDICATION, never PASS. An artifact already committed and not changed
in the flip commit is pinned to the commit that carried it, never left `PENDING-THIS-COMMIT`.
</proof_of_spec>

**REPORT:** the store's schema and where it was read from, with the object's last-modified time; the writer's vendor field for a fund, with file and line; whether the store holds an unadjusted close at all, in one sentence; per fund, the field, its dates, and the coverage of the held dates by the store and by the cache, with the denominators; the uncovered trading days; the fifteenth fund and what it lacks; the upstream landing as a pointer; the `STORE-FIELD` line; the account-id scan's DENOMINATOR line; every remote read made; what is not established; commits; every gate refusal and hook denial, verbatim.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a read of code, local copies and at most one store object; nothing is scheduled or served.
comp-iam: DECLARED-NOT-APPLICABLE no lens was run: at most one read-only call on one object of this firm under the existing role; no write, delete or serve.
comp-adversary: RUN -- the store's fields are read from the store and its writer, never inferred from a cache on one box; a field that exists and does not match the unadjusted series is said to be that; present is counted against the dates the back-fill reads, with the denominator; BLIND: deployed writer code that differs from the repository's copy, and an upstream landing that is named and not opened.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-78 analysis @e5d2fc8e59 (msg 6229), section 3 item 2; `3.0.0_SA_CVO` REMEDIATION_v46 @d389aa8f85.
