# TO ADVI_COTBKF.TO-CB-cb-2.fund-closes-read-back -- round 80 CB-cb-2: when dell1's closes land: per fund the held trading days present of 20,718, and for the 14 with trades how many reproduce the price paid from dell1's as-traded close (a read; C-BASIS's proof input)

<to_id>ADVI_COTBKF.TO-CB-cb-2</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~156</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-12</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>80</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** dell2 (placement DELL2) | **Decomp cell:** `CB-cb-2` (`decompositions/ADVI_COTBKF_DECOMP.round80.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**THIS CELL IS HELD UNTIL dell1's DEMAND QUEUE HAS LANDED THE 15 FUNDS' CLOSES. The issuer starts it and tells you where they are.
It is a READ, not the re-pricing. You change no code. Nothing is built, re-minted, fetched from a vendor, or written anywhere.**

**AMENDMENT 1 (issuer `2.0.0_SA_COO~C2`, 2026-10-13T12:5xZ) -- THE HOLD IS LIFTED: dell1's first scheduled run drew the request, with a PARTIAL landing.**
Source, dell1's own record (read at `origin/box/dell1` @697e5322ec, file `org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/2.0.0_SA_COO~Q1/ROUND9_FIRST_SCHEDULED_RUN_20261012.md`):
request `ADVI_COTBKF-TIER2-15-FUNDS-AS-TRADED-20261012` DRAWN 2026-10-12 22:30 ET, 19,474 of 23,340 cells; **7 LANDED** (PCBIX, SGIIX, GFFFX, FOCPX, FCNTX,
DISVX, DFLVX) and **8 REJECTED `LOW_TRADE_AGREEMENT`** (VEIRX, ABNFX, PRILX, BALCX, AGTHX, NFFFX, MEIIX, VGHAX), which dell1 says "stay unresolved with the next
act `try another candidate symbol`". Treat the 8 as NOT LANDED unless their object exists: you read it, you do not assume it. **Where the closes are:** the
price store's S3 root is `s3://` + what `data/mdpf/scripts/demque/price_store.py` `s3_root()` returns (it calls `lib.opal_naming.address("yahoo","global","silver","price_history","x")`
and drops the last path part); run that function, type no address; one object set per CUSIP under `<root>/cusip=<CUSIP>/` (columns `date`, `close_served`,
`as_traded_close`, then four trailing columns you do not use); `<root>/index/index.parquet` is the store's index, one row per CUSIP, readable as one of the reads
below. Read only the 15 CUSIPs' paths and the index; no listing beyond `<root>/cusip=<CUSIP>/` for those 15. **Changes to the record:** a fund with no object has
`in_store` false, `rows` 0, `present` 0 and `class_from_dell1` `not_landed`; `funds_in_store` is the count that exist (expected 7, MEASURED not assumed); the 8
rejected funds are named in `not_established` as dell1 states them with the source above, and the headline says how many of the 14 funds with trades have a
dell1 column to test at all. Funds that did land are tested exactly as item 3 says. The AWS bound below stays read-only; the paths above are the 15 and the index.

**Read first:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_80_20261012.md` section 3 item 2, word for word: "When dell1's closes land: the read ruled in msg 6402. Per fund, held
trading days present against the 20,718; for the 14 funds with trades, how many reproduce the price paid from dell1's column. No
re-mint is cut on it; it is C-BASIS's proof input." The PRD `org/missions/D8/ADVI/ADVI_COTBKF/prd/ADVI_COTBKF_PRD.md`: `## ADDENDUM v0.8` (C-BASIS items 1, 3, 4, 5 and its
proof), `## ADDENDUM v0.9` (item 2: the basis column) and `## ADDENDUM v0.10` (the split sentence as it now reads). dell1's ruling
(`git show origin/box/dell1:org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_DELL2_AS_TRADED_CLOSES_VIA_DEMQUE_20261012.md`): one lander, the demand queue; the seven-column store with `as_traded_close` (the vendor close with later
splits undone). The request this project sent:
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF-TIER2-15-FUNDS-AS-TRADED-20261012.request.json`.

**The 15 funds:** VEIRX, PCBIX, ABNFX, SGIIX, GFFFX, FOCPX, FCNTX, PRILX, BALCX, AGTHX, DISVX, DFLVX, NFFFX, MEIIX, VGHAX. Their held trading days: 20,718 (per fund in `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~149/STORE_UNADJUSTED_FIELD.json`, key `by_fund`). The trades and the
price-paid test of round 76: `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~140/FUNDS_BY_TRADES.json` and its csv (which 14 have trades; the test's tolerance and thresholds: use the SAME
test, quoted from that record, not a new one).

**Your item.**

1. **Where the closes are, as dell1 names it** (the ruling and the queue's code `data/mdpf/scripts/demque/price_store.py`: the
   address is quoted from code or from the issuer's start note; you type none). READ-ONLY: for each of the 15, its one object
   (keyed by the 9-character CUSIP as the request gives it): its columns, row count, first and last date, last-modified time.
   15 keys at most; no listing beyond them; no write.
2. **Per fund, held trading days PRESENT:** of its held trading days, how many carry a non-null `as_traded_close` in dell1's object.
   Sum against 20,718. The missing days listed as ranges per fund.
3. **For the 14 funds with trades, the price-paid test, from dell1's column:** the SAME test as round 76 (quote it), with the close
   taken from dell1's `as_traded_close` on the trade date: trades read, trades within tolerance, the fund's class (pass, fail,
   too few). Beside it the round-76 result for the same fund from the store's close, so the change is visible.
4. **The split arm, worded as the reviewer ruled (msg 6388):** how many of the 15 funds have a split inside the back-fill (from
   dell1's object, where `close_served` and `as_traded_close` differ, and from the vendor's split events if the object carries
   them). If none split, write exactly that the split-undone property "rests on dell1's word alone" for these funds; NEVER write
   that the split arm passed. If one split: the price paid reproduced on both sides, with counts.
5. Write the record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~156/FUND_CLOSES_READ_BACK.json`, a `.csv` (columns: cusip, ticker, in_store, rows, first, last, held_trading_days, present,
   trades_read, trades_within_tolerance, class_from_dell1, class_from_store_r76; CUSIPs only in the column named exactly `cusip`)
   and a short `.md`. Top-level keys, exactly: `where_as_named`, `funds` (15), `funds_in_store`, `held_trading_days`,
   `present`, `absent`, `by_fund` (a list of 15), `test` (the round-76 test, quoted), `funds_with_trades`, `pass`, `fail`,
   `too_few`, `funds_that_split`, `split_arm` (a sentence), `headline`, `not_established`.

### ACCEPTANCE

<criterion id="CB80cb2-AC1" cell_refs="CB-cb-2"><invocation>python -c "import json;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~156/FUND_CLOSES_READ_BACK.json',encoding='utf-8'));print('FUND-CLOSES-READ-BACK funds=%d listed=%d funds_in_store=%d held_trading_days=%d present=%d absent=%d sum=%d funds_with_trades=%d pass=%d fail=%d too_few=%d funds_that_split=%d split_arm=%s'%(d['funds'],len(d['by_fund']),d['funds_in_store'],d['held_trading_days'],d['present'],d['absent'],d['present']+d['absent'],d['funds_with_trades'],d['pass'],d['fail'],d['too_few'],d['funds_that_split'],str(d['split_arm'])[:70]))"</invocation><expect>FUND-CLOSES-READ-BACK funds=15 listed=15</expect></criterion>
`CB80cb2-AC1` -- every held trading day of the 15 funds is present or absent in dell1's column (`sum` equals `held_trading_days`);
the funds with trades are classed by the round-76 test. The issuer reads the counts the CTO asked for.

<criterion id="CB80cb2-AC2" cell_refs="CB-cb-2" judgment="true"/>
`CB80cb2-AC2` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9 and never self-graded: the test is round 76's, unchanged; presence is counted
against the held trading days with the denominator; the split arm is worded as ruled (dell1's word alone where no fund split,
never "passed"); nothing was re-priced or re-minted.

<expected_criteria>CB80cb2-AC1,CB80cb2-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below (your deliverables folder and your own NEW channel row) and the file of this order.
- **You change no code, test, config, manifest or registry. NO re-pricing, NO re-mint, NO build.**
- **AWS: READ-ONLY, at most the 15 objects the request names,** in the store dell1's ruling names, through the `.tools/aws` shim; no
  listing beyond them, no write, no delete. If a read is refused, record the exact error; do not try another role.
- **Another firm's data is never opened.** No account id and no account's value: counts, tickers, dates and prices only.
- After your commit run `env -u COTBKF_SWEEPS_CONFIG python -m pytest data/assets/scripts/silver/tests/test_cotbkf_no_account_ids.py -q -s`;
  keep CUSIPs in CSV columns named exactly `cusip` and tickers elsewhere; report its DENOMINATOR line.
- **NEVER `--apply`, `--remint`, `--overwrite`, a serve, or any S3 write or delete against a real bucket.** No push. No `--refresh`.
  **No vendor call and no fetch** (no Yahoo, no Bloomberg, no gateway series pull): what is on disk is read, never refreshed. A
  read of dell1's landed closes is a read of an Opal artifact, not of a vendor.
- A commonwealth script you run carries `COTBKF_SWEEPS_CONFIG=C:/dev/_cotbkf_private_evidence_20261009/config/commonwealth_sweeps.json` in its command line. Do not open or print anything else under that folder.
- Run outputs go under your own worktree `.scratch/` (never committed); nothing under `C:/dev/ajb_workspace/.scratch/advi_cotbkf` is modified.
- **Never print** an account id or an account's value, flow, quantity, share balance or return. Counts, dates, CUSIPs, tickers, a
  security's price or per-share distribution, ratios and reason codes only.
- **No gate override** of any kind and no `--force`. Do not weaken, delete, xfail or skip a test.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row with id
  `ADVI_COTBKF-D2-W156-S<k>` (k from 1), `"fabric": "dell2"`, `surfaced_at` read from the clock, APPENDED to the channel file with
  `open(path, 'a', encoding='utf-8', newline='\n')`; `git diff --numstat` must show added lines only. Never open the channel file with
  an editing tool.

<paths>
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round80.md</decomp_doc> (round 80), cell `CB-cb-2`.
<owned_cells>CB-cb-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB80cb2-AC1, CB80cb2-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~156/ADVI_COTBKF.TO-CB-cb-2.fund-closes-read-back.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB80cb2-AC1,CB80cb2-AC2` BEFORE the flip. Mechanical: CB80cb2-AC1. A judgment criterion is recorded as PENDING-ADJUDICATION, never PASS. An artifact already committed and not changed
in the flip commit is pinned to the commit that carried it, never left `PENDING-THIS-COMMIT`.
</proof_of_spec>

**REPORT:** where the closes are, as named; per fund: in the store or not, rows, first and last date, held trading days present and the missing ranges; the total present of 20,718; the round-76 test as quoted; per fund with trades: trades read, within tolerance, the class from dell1's column beside round 76's class from the store; the funds that split and the split arm in the ruled wording; every remote read made; the `FUND-CLOSES-READ-BACK` line; the account-id scan's DENOMINATOR line; what is not established; commits; every gate refusal and hook denial, verbatim.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a read of at most 15 landed objects; nothing is scheduled or served.
comp-iam: DECLARED-NOT-APPLICABLE no lens was run: read-only calls on Opal data under the existing role, as the bounds list them; no write, delete or serve, and no new permission.
comp-adversary: RUN -- held until the closes have landed (an external act of dell1's queue; the issuer starts the cell); the test is round 76's, quoted and unchanged; presence is counted against the held trading days; where no fund split the split property rests on dell1's word and the record says so; nothing is re-priced; BLIND: a fund the queue could not resolve and left unlanded.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-80 analysis @7bfd7c4664 (msg 6406), section 3 item 2; `3.0.0_SA_CVO` REMEDIATION_v48 @222ab69461.
