# TO ADVI_COTBKF.TO-CB-bv-4.fetch-held-27 -- round 74 CB-bv-4: the one permitted fetch: unadjusted daily closes for the 27 held fund series with no cached close, each asked once, into a new folder

<to_id>ADVI_COTBKF.TO-CB-bv-4</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~130</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>issued</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>74</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** dell2 (placement DELL2) | **Decomp cell:** `CB-bv-4` (`decompositions/ADVI_COTBKF_DECOMP.round74.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**This cell makes ONE PERMITTED FETCH. It is the only cell of the project that asks a vendor for anything. You change no code.**

**Read first:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_74_20261011.md` section 2 item 5 and section 3 item 4, word for word: "The 27 held series with no cached close: a fetch is
permitted, once. Unadjusted daily closes from the source the cache already uses, tickers counted before fetching, each asked once, into
the project's own cache; not Bloomberg. The 94 unheld series are not fetched." Then the round-73 record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~126/NO_CACHE_HELD_COUNT.json` and its `.csv` (the
121 with no cached close; 27 held, 94 not; all with a ticker); and how the existing cache was pulled:
`data/assets/scripts/silver/commonwealth_price_basis_census.py` (READ it, do NOT run it: which library and call it uses, with which
arguments, so that the file it writes has an unadjusted `Close` and an `Adj Close`; the file format and name per ticker) and two
files of `C:/dev/ajb_workspace/.scratch/advi_cotbkf/yahoo_census/` as the format to match.

**Your item.**

1. **Count before fetching.** Rebuild the 27 held tickers from the round-73 `.csv` and print them with the count. Confirm none has a
   usable file in `C:/dev/ajb_workspace/.scratch/advi_cotbkf/yahoo_census/` (the one with a marker and no bars is named). Write the list of tickers you WILL ask to a
   file in your scratch, with a clock timestamp, BEFORE the first request. The 94 unheld are not on it.
2. **Fetch, each ticker asked ONCE,** from the same source by the same call the existing cache used, unadjusted closes with the
   adjusted close beside them, over the same span the existing files cover or wider. One request per ticker; a pause between
   requests; NO retry of a ticker that returns nothing or errors: it is recorded as `empty` or `error` with the message, and left.
   Not Bloomberg, and no other vendor, gateway or source.
3. **Where it lands.** A NEW folder `C:/dev/ajb_workspace/.scratch/advi_cotbkf/yahoo_census_fetch_r74/`, one file per ticker in the existing cache's format. You do NOT write into
   `C:/dev/ajb_workspace/.scratch/advi_cotbkf/yahoo_census/` and you overwrite nothing: the served table was reproduced against that folder as it stands, and a
   pinned re-build must still find it unchanged. This is the one write you make outside your worktree; say so in your report with
   the file count. Print the count of files in `C:/dev/ajb_workspace/.scratch/advi_cotbkf/yahoo_census/` before and after (equal).
4. **What came back,** per ticker: rows, first and last date, whether `Close` and `Adj Close` differ anywhere (a fund that paid
   nothing in the window cannot show an adjustment), a sha256 of the file. And beside the build: the BUILD's close for that fund
   (`C:/dev/ajb_workspace/.scratch/advi_cotbkf/r34/after/security_day_price.parquet`) over the fetched unadjusted close on the dates they share: dates shared, the
   share below 0.98, the lowest ratio, and whether the ratio rises toward the present. A reading per fund: `looks adjusted`, `looks
   unadjusted`, `too few dates`, with the words NOT CUSTODIAN-VALIDATED beside every one: none of these funds has a reinvestment row,
   so the custodian's price cannot confirm the fetched close.
5. Write the record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~130/FETCH_HELD_27.json`, a `.csv` (columns: cusip, ticker, asked, outcome, rows, first_date, last_date, sha256, dates_shared,
   share_below_0_98, min_ratio, reading; CUSIPs only in the column named exactly `cusip`) and a short `.md`. Top-level keys,
   exactly: `permitted_by` (the analysis line, quoted), `source`, `call`, `list_written_at`, `held` (27), `asked`, `asked_more_than_once`
   (0), `returned`, `empty`, `errors`, `unheld_asked` (0), `bloomberg` (false), `landed_in`, `existing_cache_files_before`,
   `existing_cache_files_after`, `readings` (counts by reading), `custodian_validated` (0), `headline`, `not_established`.

### ACCEPTANCE

<criterion id="CB74bv4-AC1" cell_refs="CB-bv-4"><invocation>python -c "import json;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~130/FETCH_HELD_27.json',encoding='utf-8'));print('FETCH-HELD held=%d asked=%d asked_more_than_once=%d returned=%d empty=%d errors=%d outcome_sum=%d unheld_asked=%d bloomberg=%s cache_before=%d cache_after=%d custodian_validated=%d readings=%s'%(d['held'],d['asked'],d['asked_more_than_once'],d['returned'],d['empty'],d['errors'],d['returned']+d['empty']+d['errors'],d['unheld_asked'],d['bloomberg'],d['existing_cache_files_before'],d['existing_cache_files_after'],d['custodian_validated'],json.dumps(d['readings'],sort_keys=True)))"</invocation><expect>FETCH-HELD held=27</expect></criterion>
`CB74bv4-AC1` -- the 27 held tickers were counted before fetching and each asked once (`outcome_sum` equals `asked`); no unheld
ticker and no other vendor was asked; the existing cache folder holds the same number of files before and after.

<expected_criteria>CB74bv4-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below (your deliverables folder and your own NEW channel row), the file of this order, and the ONE
  new folder `C:/dev/ajb_workspace/.scratch/advi_cotbkf/yahoo_census_fetch_r74/` outside the repository.
- **You change no code, test, config, manifest or registry.** You do not run the price-basis census script.
- **The fetch is the 27 held tickers, once each, from the source the cache already uses. Nothing else is asked of anyone:** not the
  94, not Bloomberg, not a gateway, not a second vendor, not a retry.
- After your commit run `env -u COTBKF_SWEEPS_CONFIG python -m pytest data/assets/scripts/silver/tests/test_cotbkf_no_account_ids.py -q -s`;
  keep CUSIPs in CSV columns named exactly `cusip` and tickers elsewhere; report its DENOMINATOR line.
- **NEVER `--apply`, `--remint`, `--overwrite`, a serve, or any S3 write or delete against a real bucket.** No push. No `--refresh`.
  **The one fetch this order permits is the only vendor call;** no Bloomberg, no gateway series pull, nothing else refreshed.
- A commonwealth script you run carries `COTBKF_SWEEPS_CONFIG=C:/dev/_cotbkf_private_evidence_20261009/config/commonwealth_sweeps.json` in its command line. Do not open or print anything else under that folder.
- Run outputs go under your own worktree `.scratch/` (never committed); nothing under `C:/dev/ajb_workspace/.scratch/advi_cotbkf` is modified except the one new folder this order names.
- **Never print** an account id or an account's value, flow, quantity, share balance or return. Counts, dates, CUSIPs, tickers, a
  security's price or per-share distribution, ratios and reason codes only.
- **No gate override** of any kind and no `--force`. Do not weaken, delete, xfail or skip a test.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row with id
  `ADVI_COTBKF-D2-W130-S<k>` (k from 1), `"fabric": "dell2"`, `surfaced_at` read from the clock, APPENDED to the channel file with
  `open(path, 'a', encoding='utf-8', newline='\n')`; `git diff --numstat` must show added lines only. Never open the channel file with
  an editing tool.

<paths>
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round74.md</decomp_doc> (round 74), cell `CB-bv-4`.
<owned_cells>CB-bv-4</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB74bv4-AC1. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~130/ADVI_COTBKF.TO-CB-bv-4.fetch-held-27.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB74bv4-AC1` BEFORE the flip. Mechanical. An artifact already committed and not changed
in the flip commit is pinned to the commit that carried it, never left `PENDING-THIS-COMMIT`.
</proof_of_spec>

**REPORT:** the 27 tickers as counted and the timestamp of the list written before the first request; the source and the call; per ticker asked, the outcome; asked, returned, empty, errors; that no ticker was asked twice, no unheld ticker asked and no other vendor asked; where the files landed and the existing cache's file count before and after; the readings, each not custodian-validated; the headline; the `FETCH-HELD` line; the account-id scan's DENOMINATOR line; what is not established; commits; every gate refusal, verbatim.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE one hand-run fetch into a local folder.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call; one vendor, the one the cache already uses, permitted by the CTO for this round, once.
comp-adversary: RUN -- the list is written before the first request; each ticker is asked once and an empty answer is recorded, not retried; the 94 unheld and every other vendor are out; the files land in a NEW folder so the cache the served table was reproduced against is unchanged, by a file count before and after; every reading says it is not custodian-validated; BLIND: a vendor that returns an adjusted series under an unadjusted label cannot be caught here, since none of these funds has a reinvestment row.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-74 analysis @42390144c0 (msg 5758), section 3 item 4; `3.0.0_SA_CVO` REMEDIATION_v44 @edbfc928ca.
