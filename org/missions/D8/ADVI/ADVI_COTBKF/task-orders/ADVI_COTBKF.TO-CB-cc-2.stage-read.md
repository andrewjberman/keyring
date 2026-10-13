# TO ADVI_COTBKF.TO-CB-cc-2.stage-read -- round 81 CB-cc-2: five securities, one served day each: the value at every stage that touches it (vendor Close, store row, build price, minted copy, served row), and the first stage where the ratio leaves 1.0

<to_id>ADVI_COTBKF.TO-CB-cc-2</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~159</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>81</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** dell2 (placement DELL2) | **Decomp cell:** `CB-cc-2` (`decompositions/ADVI_COTBKF_DECOMP.round81.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**This is a READ on local copies and, for one object, of the price store in S3. You change no code. Nothing is built, served, corrected or fetched from a vendor.**

**Read first:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_81_20261013.md` whole, section 2 ruling 2, word for word: "Cause, by stage, not by ratio. A whole split ratio was the wrong lens: 0.150 and 0.50 are
what the served value is AFTER some stage. For each of the five securities, on one served day each, read the value at every stage that touches it: vendor Close, store row, build price, minted copy,
served row. The first stage where the ratio leaves 1.0 is the cause's address." and section 3 item 2: "Counts and ratios only, with no account value." Then round 80's record
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~155/THREE_EQUITIES.json` (the five: APH, CTVA, HON, KLAC, SCCO; the `day` it chose for each; the ratios it found) and its channel rows
`ADVI_COTBKF-D2-W155-S1`, `-S2`, `-S3`, `-S4`. You read the record to find the securities and the days; you READ EVERY STAGE AGAIN FROM ITS SOURCE and never copy a value from that record.

**The stages and where each is read (all read-only):**

| stage | source |
|---|---|
| vendor Close | `C:/dev/ajb_workspace/.scratch/advi_cotbkf/yahoo_census/` (one file per ticker: Date, Close, Adj Close; no split column): read what is on disk, fetch nothing |
| store row | `s3://opal-data-cot/silver/prices/canonical_prices.parquet`, version `76.rgWIXYdLNsXSwrXvyuEmaEtfr9y98` (97,443,387 bytes, last modified 2026-10-09T13:41:04Z; named in `deliverables/0.9.0_WK_ADVI_COTBKF~153/STORE_WRITER.md`): ONE `get-object` for that key and version into your worktree's `.scratch/`; check the byte length before use; columns date, asset_name, ticker, price, source. State the row's `source` value on the day |
| build price | `C:/dev/ajb_workspace/.scratch/advi_cotbkf/r34/after/security_day_price.parquet` (cusip, date, price, store) |
| minted copy | `C:/dev/ajb_workspace/.scratch/advi_cotbkf/fwd3_serve_r34/` (the `account_day_value` table: the close column; report counts of accounts as a COUNT, never an id) |
| served row | what is served: the minted tables' S3 prefixes (`s3://opal-data-assets/commonwealth/cottonwood/silver/{daily_returns,account_day_value,month_grades}/date=2026-06-23/`: one `list-objects-v2 --max-items 5` each, to say whether anything is served) and, for a day in 2026-04-22 to 2026-06-07, the served holdings partition read the way `deliverables/0.9.0_WK_ADVI_COTBKF~145/NO_SNAPSHOT_BRANCH.json` says it was read (this firm's own gold holdings, read-only, those dates, the rows for these names only; match by `asset_name` where the ticker column is empty) |
| price paid | the custodian's trades `C:/dev/ajb_workspace/.scratch/advi_cotbkf/tx_cache/trade_year=*/*.parquet` (price paid = amount over units on a buy or sell; CUSIP, Symbol); the nearest trade to the day; say which and how far |

**Your item.**

1. **The day.** Per security, start from round 80's `day` for it and keep it if the minted copy holds the security that day; otherwise choose the nearest day it is held and say why. A day on which a stage does not exist
   is recorded as that stage `absent` with the reason (KLAC and SCCO are held on no day the build or store covers: report exactly that and read the earliest and latest day each stage DOES cover instead).
2. **Per security, per day, the value at each of the five stages, and the price paid** (a price, a ratio, never a dollar value of a holding). Then the ratio of each stage to the PREVIOUS stage and to the price paid.
3. **The first stage where the ratio leaves 1.0** (outside 0.5 percent of the previous stage, and say the tolerance): named as one of `store_row_vs_vendor`, `build_vs_store`, `minted_vs_build`, `served_vs_minted`, `none_before_price_paid`, or `not_established`.
   For that stage give the next fact that would name the cause (a file and line of the code that writes that stage, read, not run), without opining on a fix.
4. **If a stage's ratio drifts rather than steps** (CTVA's served level moved 0.1603 to 0.1500 across fifteen small steps in round 80), report the ratio on three days across the held range, so the drift is visible.
5. Write the record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~159/STAGE_READ.json` and a short `.md`. Top-level keys, exactly: `store_object` (`{"key", "version", "bytes", "bytes_match"}`), `served_prefixes` (a list of 3:
   `{"prefix", "objects_seen", "listing_limit"}`), `securities` (a list of 5: `{"ticker", "kind", "day", "day_reason", "stages": {"vendor_close", "store_row", "build_price", "minted_copy", "served_row", "price_paid"}, "ratios": {"store_over_vendor", "build_over_store",
   "minted_over_build", "served_over_minted", "stage_over_price_paid"}, "first_stage_off_1", "tolerance", "writer_to_read_next", "drift"}`), `stages_found_absent` (a list), `headline`, `not_established`. A value is a number or the string `absent`.

### ACCEPTANCE

<criterion id="CB81cc2-AC1" cell_refs="CB-cc-2"><invocation>python -c "import json;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~159/STAGE_READ.json',encoding='utf-8'));s=d['securities'];print('STAGE-READ securities=%d with_six_stage_keys=%d with_a_first_stage=%d served_prefixes=%d store_bytes_match=%s'%(len(s),sum(1 for x in s if all(k in x['stages'] for k in ('vendor_close','store_row','build_price','minted_copy','served_row','price_paid'))),sum(1 for x in s if x['first_stage_off_1']),len(d['served_prefixes']),d['store_object']['bytes_match']))"</invocation><expect>STAGE-READ securities=5 with_six_stage_keys=5</expect></criterion>
`CB81cc2-AC1` -- the five securities each carry every stage (a number or `absent`) and a first stage off 1.0; the store object matched its byte length. The issuer reads where each leaves 1.0.

<criterion id="CB81cc2-AC2" cell_refs="CB-cc-2" judgment="true"/>
`CB81cc2-AC2` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9 and never self-graded: every stage is read from its own source (not copied from round 80's record); "served" is read from what is served (the prefixes and the early partitions), not from what is built; the first stage off 1.0 is named
only where the ratio shows it and `not_established` otherwise; an absent stage is said to be absent, not filled; no account id or amount appears.

<expected_criteria>CB81cc2-AC1,CB81cc2-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below (your deliverables folder and your own NEW channel row) and the file of this order.
- **You change no code, test, config, manifest or registry.**
- **AWS: READ-ONLY, the ONE price-store object above (`get-object`, that key and version, into your `.scratch/`); one `list-objects-v2 --max-items 5` on each of the three served prefixes; and this firm's own gold holdings partitions dated 2026-04-22 to 2026-06-07, the rows for these names,** read the way the
  round-77 record says they were read; nothing else; no write, delete or serve. If a read is refused, record the exact error and mark that stage `absent` with the error.
- **No rebuild of any partition and no consumer attached to the minted table** (the ruling on row D2-S131).
- **Another firm's data is never opened.** No account id and no account's value: counts, tickers, dates, prices and ratios only.
- Searches go through the estate's tools; a recursive shell search of the repository is denied by a hook and is not retried another way.
- After your commit run `env -u COTBKF_SWEEPS_CONFIG python -m pytest data/assets/scripts/silver/tests/test_cotbkf_no_account_ids.py -q -s`; keep CUSIPs in CSV columns named exactly `cusip` and tickers elsewhere; report its DENOMINATOR line.
- **NEVER `--apply`, `--remint`, `--overwrite`, a serve, or any S3 write or delete against a real bucket.** No push. No `--refresh`. **No vendor call and no fetch** (no Yahoo, no Bloomberg, no gateway series pull): what is on disk is read, never refreshed.
- A commonwealth script you run carries `COTBKF_SWEEPS_CONFIG=C:/dev/_cotbkf_private_evidence_20261009/config/commonwealth_sweeps.json` in its command line. Do not open or print anything else under that folder.
- Run outputs go under your own worktree `.scratch/` (never committed); nothing under `C:/dev/ajb_workspace/.scratch/advi_cotbkf` is modified.
- **Never print** an account id or an account's value, flow, quantity, share balance or return. Counts, dates, CUSIPs, tickers, a security's price, ratios and reason codes only.
- **No gate override** of any kind and no `--force`. Do not weaken, delete, xfail or skip a test.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row with id `ADVI_COTBKF-D2-W159-S<k>` (k from 1), `"fabric": "dell2"`, `surfaced_at` read from the clock (`date -u +%FT%TZ`),
  APPENDED to the channel file with `open(path, 'a', encoding='utf-8', newline='\n')`; `git diff --numstat` must show added lines only. Never open the channel file with an editing tool.

<paths>
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round81.md</decomp_doc> (round 81), cell `CB-cc-2`.
<owned_cells>CB-cc-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB81cc2-AC1, CB81cc2-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~159/ADVI_COTBKF.TO-CB-cc-2.stage-read.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB81cc2-AC1,CB81cc2-AC2` BEFORE the flip. Mechanical: CB81cc2-AC1. A judgment criterion is recorded with status `UNVERIFIABLE-BY-INSTRUMENT` and a `status_reason` that begins `PENDING-ADJUDICATION`, never PASS. An artifact already committed and not changed
in the flip commit is pinned to the commit that carried it, never left `PENDING-THIS-COMMIT`.
</proof_of_spec>

**REPORT:** FIRST, if it exists: a served stage (the prefixes or the early partitions) carrying a value off 1.0 against the stage before it, with the ticker and the counts of days and accounts. Then: per security the day, the value at each stage, the ratios, the first stage off 1.0 and the writer to read next; the stages found absent; the drift where one is seen; every remote read made; the `STAGE-READ` line; the account-id scan's DENOMINATOR line; what is not established; commits; every gate refusal and hook denial, verbatim.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a read of local copies, one S3 object and three listings; nothing is scheduled or served.
comp-iam: DECLARED-NOT-APPLICABLE no lens was run: read-only calls on Opal data under the existing role, as the bounds list them; no write, delete or serve, and no new permission.
comp-adversary: RUN -- every stage is read from its own source and not copied from round 80; the served stage is read from what is served; a stage that does not exist is `absent`, never filled; the first stage off 1.0 is named by the ratio; BLIND: a security with no trade near any held day (KLAC, SCCO) and a stage whose source file is missing from this box.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-81 analysis @ab1112493b (msg 7078), section 2 ruling 2, section 3 item 2; `3.0.0_SA_CVO` REMEDIATION_v49 @7aceb5d4a1.
