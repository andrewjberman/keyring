# TO ADVI_COTBKF.TO-CB-cb-1.three-equities -- round 80 CB-cb-1: row D2-W152-S1: the equities whose build price is a fraction of the store row -- held and served days, four ratios to the price paid, the split dates, the cause

<to_id>ADVI_COTBKF.TO-CB-cb-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~155</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-12</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>80</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** dell2 (placement DELL2) | **Decomp cell:** `CB-cb-1` (`decompositions/ADVI_COTBKF_DECOMP.round80.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**This is a READ on local copies and, for one question only, of this firm's own served holdings partitions. You change no code.
Nothing is built, fetched from a vendor, or written to any bucket.**

**Read first:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_80_20261012.md` whole (46 lines): section 3 item 1, word for word: "Row D2-W152-S1, first. For each of the three equities,
counts and dates only, no account value: is it held on any day of the 47 served early partitions (2026-04-22 to 2026-06-07), and on
any day the minted table covers; on one held day each: the build's price, the store's row, the vendor's Close, and the price paid
on the nearest trade, as four ratios to the price paid; the vendor's split dates for it, and which side of each the wrong ratio
begins. A held, SERVED day carrying a split-sized error comes to this seat the same hour, before the rest of the table." and its
paragraph "Why the three equities matter beyond themselves". Then row ADVI_COTBKF-D2-W152-S1 in the channel (APH, CTVA, KLAC: the
build's price on the last store day at 0.5, 0.15 and 0.1 of the store's row, where 1,258 of 1,263 sit at 1.0), the PRD's
`## ADDENDUM v0.10` (find the heading in `org/missions/D8/ADVI/ADVI_COTBKF/prd/ADVI_COTBKF_PRD.md`: this build's split step is NOT applied to a point already split-undone), and
the round-79 record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~152/BASIS_VALUE_AGAINST_SPLIT_SCALING.json` (where the split scaling runs: `split_plan`, `apply_splits`).

**Local data:** the build's prices `C:/dev/ajb_workspace/.scratch/advi_cotbkf/r34/after/security_day_price.parquet` (cusip, date, price, store); the price store
object `C:/dev/wk-cotbkf-84/.scratch/w149/store/` (date, asset_name, ticker, price, source; read it there, do not download it); the vendor cache
`C:/dev/ajb_workspace/.scratch/advi_cotbkf/yahoo_census/` (one file per ticker with Close, Adj Close and, where the file has them, split events: read what is on
disk, fetch nothing; if a ticker has no file, say so); the custodian's trades `C:/dev/ajb_workspace/.scratch/advi_cotbkf/tx_cache/trade_year=*/*.parquet` (the
price paid = amount over units on a buy or sell; CUSIP, Symbol); the served minted copy `C:/dev/ajb_workspace/.scratch/advi_cotbkf/fwd3_serve_r34/` (which
securities and days the minted table covers); the build's split plan and repairs in `C:/dev/ajb_workspace/.scratch/advi_cotbkf/r34/after/` (list the folder: the
plan of applied splits per CUSIP, the suspect rows).

**Your item.**

1. **The three, identified:** ticker, kind as the custodian types it, and whether the 0.5, 0.15 and 0.1 of the row reproduce (the
   build's price over the store's row on the last store day). If more than these three sit far from 1.0, list them all (the row
   says 5 of 1,263 are not at 1.0): this cell covers every one of them.
2. **Held and SERVED?** For each: (a) is it held on any day the minted table covers (the served copy; first and last held day, the
   count of held days, the count of holding accounts as a COUNT); (b) is it held on any day of the 47 served early holdings
   partitions, 2026-04-22 to 2026-06-07: the round-77 record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~145/NO_SNAPSHOT_BRANCH.json` says how those partitions were read and where; use the
   same read (this firm's own gold holdings, read-only, those dates only, the rows for these tickers only) and report days held
   as a count. (c) On those days, which price does the served partition carry for it: the store's, the build's, another?
3. **One held day each, four ratios to the price paid:** pick the held day nearest a trade of that security (say which, and how
   far). Report the price paid (as 1.0), and the build's price, the store's row and the vendor's Close each divided by it.
4. **The vendor's split dates** for each (from the cache file's split events if present; else from the split store's entries the
   build's plan lists; say which source), and **on which side of each split the wrong ratio begins:** compute build over store by
   date across the whole held range and report the dates at which it steps, with the step size, against the split dates and
   ratios.
5. **The cause, one of:** `double_scaling` (this build's split step applied to a store row that is already split-undone or
   as-traded: the step in build/store equals a split ratio and the STORE's row matches the price paid while the build's does
   not), `store_row_unscaled_build_right` (the build's price matches the price paid and the store's does not), `other` (say
   what), or `not_established`. Per security. The price paid decides which of the two is right; say so with the numbers.
6. **THE SAME-HOUR CLAUSE.** If any of them is held on a SERVED day (the minted table or the 47 partitions) with a split-sized error
   in the price that is served there, put that FIRST in your report, with the ticker, the count of served days and of holding
   account-days (counts), so the issuer can carry it to the CTO at once.
7. Write the record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~155/THREE_EQUITIES.json` and a short `.md`. Top-level keys, exactly: `not_at_one` (the count of securities whose build/store
   ratio on the last store day is off 1.0, of how many), `equities` (a list, one per such security: `{"ticker", "kind",
   "ratio_build_over_store", "held_minted_days", "held_served_partition_days", "served_price_is", "day", "ratios": {"price_paid":
   1.0, "build", "store", "vendor_close"}, "vendor_splits", "steps", "cause"}`), `served_day_with_split_sized_error` (true, false
   or `not_established`), `served_error_account_days` (an integer), `cause_overall`, `widens_c_basis` (true, false or
   `not_established`: true only if a cause is `double_scaling`), `headline`, `not_established`.

### ACCEPTANCE

<criterion id="CB80cb1-AC1" cell_refs="CB-cb-1"><invocation>python -c "import json;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~155/THREE_EQUITIES.json',encoding='utf-8'));e=d['equities'];print('THREE-EQUITIES listed=%d not_at_one=%s with_four_ratios=%d held_minted=%d held_served_partitions=%d served_day_with_split_sized_error=%s served_error_account_days=%d causes=%s widens_c_basis=%s'%(len(e),d['not_at_one'],sum(1 for x in e if all(k in x['ratios'] for k in ('price_paid','build','store','vendor_close'))),sum(1 for x in e if x['held_minted_days']),sum(1 for x in e if x['held_served_partition_days']),d['served_day_with_split_sized_error'],d['served_error_account_days'],json.dumps(sorted(str(x['cause']) for x in e)),d['widens_c_basis']))"</invocation><expect>THREE-EQUITIES listed=</expect></criterion>
`CB80cb1-AC1` -- every security off 1.0 is listed with its four ratios, its held and served days and a cause. The issuer reads
whether a served day carries a split-sized error and whether the contract widens.

<criterion id="CB80cb1-AC2" cell_refs="CB-cb-1" judgment="true"/>
`CB80cb1-AC2` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9 and never self-graded: the price paid decides which of the build and the
store is right, with the numbers shown; "served" is read from what is served (the minted copy and the 47 partitions), not from
what is built; a cause is named only where the step equals a split ratio on the split's date, and `not_established` otherwise;
no account id or amount appears.

<expected_criteria>CB80cb1-AC1,CB80cb1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below (your deliverables folder and your own NEW channel row) and the file of this order.
- **You change no code, test, config, manifest or registry.**
- **AWS: READ-ONLY, this firm's own gold holdings partitions dated 2026-04-22 to 2026-06-07, the rows for these tickers,** read the
  way the round-77 record says they were read; nothing else; no write, delete or serve. If that read is refused, record the exact
  error and mark the served-partition answers `not_established`.
- **No rebuild of any partition and no consumer attached to the minted table** (the ruling on row D2-S131).
- **Another firm's data is never opened.** No account id and no account's value: counts, tickers, dates, prices and ratios only.
- Searches go through the estate's tools; a recursive shell search of the repository is denied by a hook and is not retried another way.
- After your commit run `env -u COTBKF_SWEEPS_CONFIG python -m pytest data/assets/scripts/silver/tests/test_cotbkf_no_account_ids.py -q -s`;
  keep CUSIPs in CSV columns named exactly `cusip` and tickers elsewhere; report its DENOMINATOR line.
- **NEVER `--apply`, `--remint`, `--overwrite`, a serve, or any S3 write or delete against a real bucket.** No push. No `--refresh`.
  **No vendor call and no fetch** (no Yahoo, no Bloomberg, no gateway series pull): what is on disk is read, never refreshed.
- A commonwealth script you run carries `COTBKF_SWEEPS_CONFIG=C:/dev/_cotbkf_private_evidence_20261009/config/commonwealth_sweeps.json` in its command line. Do not open or print anything else under that folder.
- Run outputs go under your own worktree `.scratch/` (never committed); nothing under `C:/dev/ajb_workspace/.scratch/advi_cotbkf` is modified.
- **Never print** an account id or an account's value, flow, quantity, share balance or return. Counts, dates, CUSIPs, tickers, a
  security's price or per-share distribution, ratios and reason codes only.
- **No gate override** of any kind and no `--force`. Do not weaken, delete, xfail or skip a test.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row with id
  `ADVI_COTBKF-D2-W155-S<k>` (k from 1), `"fabric": "dell2"`, `surfaced_at` read from the clock, APPENDED to the channel file with
  `open(path, 'a', encoding='utf-8', newline='\n')`; `git diff --numstat` must show added lines only. Never open the channel file with
  an editing tool.

<paths>
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round80.md</decomp_doc> (round 80), cell `CB-cb-1`.
<owned_cells>CB-cb-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB80cb1-AC1, CB80cb1-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~155/ADVI_COTBKF.TO-CB-cb-1.three-equities.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB80cb1-AC1,CB80cb1-AC2` BEFORE the flip. Mechanical: CB80cb1-AC1. A judgment criterion is recorded as PENDING-ADJUDICATION, never PASS. An artifact already committed and not changed
in the flip commit is pinned to the commit that carried it, never left `PENDING-THIS-COMMIT`.
</proof_of_spec>

**REPORT:** FIRST, if it exists: a held, SERVED day with a split-sized error in the served price -- the ticker, the served days and holding account-days as counts. Then: every security off 1.0 with its ratio; per security the held and served days, which price the served partitions carry, the one day with its four ratios to the price paid, the split dates and their source, the dates and sizes of the steps in build over store, the cause with the numbers that decide it; whether C-BASIS widens; every remote read made; the `THREE-EQUITIES` line; the account-id scan's DENOMINATOR line; what is not established; commits; every gate refusal and hook denial, verbatim.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a read of local copies and of served partitions; nothing is scheduled or served.
comp-iam: DECLARED-NOT-APPLICABLE no lens was run: read-only calls on Opal data under the existing role, as the bounds list them; no write, delete or serve, and no new permission.
comp-adversary: RUN -- the price paid is the referee between the build and the store, with the numbers shown; served is read from what is served; a cause needs the step to equal a split ratio on the split date; every security off 1.0 is covered, not only the three named; BLIND: a security with no trade near any held day.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-80 analysis @7bfd7c4664 (msg 6406), section 3 item 1; `3.0.0_SA_CVO` REMEDIATION_v48 @222ab69461.
