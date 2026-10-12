# TO ADVI_COTBKF.TO-CB-by-3.level-error -- round 77 CB-by-3: the level error sized where the census found a served reader, and only there: account-days and the share of value, as counts and proportions

<to_id>ADVI_COTBKF.TO-CB-by-3</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~145</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>77</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** dell2 (placement DELL2) | **Decomp cell:** `CB-by-3` (`decompositions/ADVI_COTBKF_DECOMP.round77.md`) |
**outcome_ref:** FWD-3 | **depends_on:** CB-by-1

---

## WORKER FACE

### THE CELL

**This is a MEASUREMENT, made ONLY where cell 1 found a served reader. You change no code. Nothing is fetched, served or applied.**

**Read first:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_77_20261011.md` section 2 and section 3 item 3 ("The level error sized where cell 1 finds a served reader, and only there:
account-days and the share of value affected, counts and proportions."); this round's census
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~143/CLOSE_READERS.json` and its `.md` (in the tree when you start;
if absent, that is the refusal clause): the readers classed, and for each serving reader whether its figure uses the store's close.

**Your item.**

1. **If the census found NO reader serving a figure from an affected close:** say so, with the census's own count and what it could
   not see; size nothing; the record's `sized` is an empty list and its headline says the level error is not served by any reader
   the census could reach. That is a complete result.
2. **Otherwise, for EACH such reader and for no other:** the population it serves for THIS project's firm (accounts as a COUNT,
   account-days, the date range), and within it the account-days on which one of the 15 failing funds is held at a value built from
   the affected close; and the SHARE OF VALUE affected: on those account-days, the failing funds' value as a share of the account's
   served value, as a distribution (median, the share of account-days above 5, 25 and 50 percent). And the level itself: per fund,
   the served close over the unadjusted close where one is held (this round's `FAILING_FUNDS.json`, if it has landed; else the
   round-76 median ratio), so the understatement is stated as a proportion and never as money.
3. **What kind of figure:** a value, a weight or a return. For a value or a weight the error is a level, on every day; for a return
   say which days it enters (the round-75 and round-76 records). Do not restate the return work.
4. **Reads only,** of the reader's own served artifact for this firm; one firm; no other firm's data opened. No account id, no
   account's value.
5. Write the record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~145/LEVEL_ERROR.json` and a short `.md`. Top-level keys, exactly: `served_readers_from_cell_1`, `sized` (a list of `{"reader",
   "owner", "figure", "accounts", "account_days", "account_days_holding_a_failing_fund", "share_of_value", "level_by_fund"}`),
   `unsized` (a list, with why), `headline`, `not_established`.

### AMENDMENT 1 (issuer `2.0.0_SA_COO~C2`, 2026-10-12T00:24Z) -- a second item in this cell, on a CTO ruling

**Why.** The census found ONE reader of the price store that serves a value: the cot holdings builder
`data/cot/scripts/gold/B_00.canonical_holdings.py`. With a holdings snapshot present it prices at the custodian's market value over
units and returns BEFORE the price store is loaded; the store's close is used only on the branch below that return. Whether
partitions built on that branch, for dates before the snapshots began, still exist and are served was not established. This seat
asked (msg 6195); `1.0.0_SA_CTO~DELL2` RULED (msg 6196), in full: "Read it this round. One cell, read-only, counts and dates only:
1. The first date a holdings snapshot exists for this firm; how many partitions were built on the no-snapshot branch before it, and
whether they still exist. 2. Whether the Cottonwood advisor-intelligence page can be asked for a date before that first snapshot:
read from the route's code; one request for one such date only if the code says it is served. 3. Of the 15 failing funds, how many
are held on any such date. A served figure built from an affected close comes to me the same hour with its date range. And the
three readers not established: name each and what would establish it."

**The added item (this is where a served reader could be, so it belongs to this cell). It is done FIRST, before the item above.**

A1. **The two branches, from the code, with file and line:** what the snapshot branch writes and for which dates; what the
    no-snapshot branch builds, with which price, for which dates, and where it writes; whether either branch overwrites, deletes
    or leaves partitions of earlier dates; how a row records which branch built it (its `source` value).
A2. **The first snapshot date for this firm, and the partitions before it.** The first date a holdings snapshot exists (from the
    snapshot store the builder reads). In the served holdings, the partitions dated BEFORE it: how many exist today, their date
    range, and which branch built them (the `source` values of ONE such partition's rows, as a count per source; the layout for the
    rest). Ask the served graph first; make a live read only for what the graph does not hold, and print the denominator of every
    listing (keys seen; whether the listing was complete or a page).
A3. **Can the page be asked for such a date?** Read from the route's code in the portal and from the steps that feed it (file and
    line): which dates the page and its data accept or default to. ONLY IF the code says a date before the first snapshot is
    served: ONE request, or one read of the one served object behind it, for ONE such date, recording that it answers and the
    `source` of what it returns. No account value is recorded.
A4. **Of the 15 failing funds, how many are held on any such date** in served holdings built on the no-snapshot branch: funds as a
    count and by ticker; partitions; and for ONE fund on ONE such date the price in the served holdings beside the store's close and
    the fund's unadjusted close that day: three prices and two ratios.
A5. **A served figure built from an affected close is filed THE SAME HOUR as a surprise row,** with its date range and the page,
    naming the reader's owner, and committed at once in its own commit; your report names it first. If none is found, say so first.
A6. **The three readers the census left `not_established`:** name each and say what ONE read would establish it (which file,
    object or setting). You do not make those reads.
A7. Write a SECOND record, `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~145/NO_SNAPSHOT_BRANCH.json`, beside the first. Top-level keys, exactly: `branches` (`{"snapshot", "no_snapshot"}`, each
    with `file_line`, `price`, `writes`), `first_snapshot_date`, `partitions_before_it` (`{"count", "first", "last", "built_by",
    "still_exist", "listing_denominator"}`), `page` (`{"accepts_a_date_before_the_first_snapshot", "file_line", "request_made",
    "answered"}`), `failing_funds_held_before` (`{"funds", "tickers", "partitions"}`), `one_price_read`,
    `served_from_an_affected_close` (true, false or `not_established`), `date_range_served`, `readers_not_established` (a list of
    three `{"reader", "what_would_establish_it"}`), `rows_filed`, `headline`, `not_established`.

**How the two items meet.** If A finds a served figure built from an affected close, that reader IS a served reader for the item
above: size it there (account-days and the share of value on the dates it is served, for this firm, as counts and proportions) and
set the first record's `served_readers_from_cell_1` to the census's count PLUS it, saying so. If A finds none, the first record
stands as the census leaves it.

**Bounds added by this amendment (they widen the grant only as far as these reads):** AWS READS ONLY, for THIS project's firm: the
served graph first; a live listing of the holdings partitions only where the graph does not hold them; one partition's rows for the
`source` counts; one more read for the one price of A4; and at most ONE request or object read for A3, only if the code says it is
served. No write, no delete, no serve. Another firm's data is never opened.

### ACCEPTANCE

<criterion id="CB77by3-AC1" cell_refs="CB-by-3"><invocation>python -c "import json;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~145/LEVEL_ERROR.json',encoding='utf-8'));c=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~143/CLOSE_READERS.json',encoding='utf-8'));print('LEVEL-ERROR census_serving_from_an_affected_close=%d served_readers_from_cell_1=%d sized=%d unsized=%d sum=%d account_days_holding_a_failing_fund=%d'%(c['serving_from_an_affected_close'],d['served_readers_from_cell_1'],len(d['sized']),len(d['unsized']),len(d['sized'])+len(d['unsized']),sum(x['account_days_holding_a_failing_fund'] for x in d['sized'])))"</invocation><expect>LEVEL-ERROR census_serving_from_an_affected_close=</expect></criterion>
`CB77by3-AC1` -- the readers sized or left unsized are exactly the census's readers serving from an affected close (`sum` and
`served_readers_from_cell_1` equal the census's count); the issuer reads the account-days.

<criterion id="CB77by3-AC2" cell_refs="CB-by-3" judgment="true"/>
`CB77by3-AC2` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9 and never self-graded: only readers the census found serving from an
affected close are sized, and an empty result is reported as one; the size is in account-days and proportions, never money; reads
only, of this firm's artifact; no account id or value appears. AMENDMENT 1 adds to this judgment: the branch that
built a partition is read from the partition's own rows and not inferred from its date; a listing prints its denominator; a request
is made only where the code says the date is served, and at most one; a served figure from an affected close is filed as a row the
same hour with its date range.

<criterion id="CB77by3-AC3" cell_refs="CB-by-3"><invocation>python -c "import json;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~145/NO_SNAPSHOT_BRANCH.json',encoding='utf-8'));p=d['partitions_before_it'];g=d['page'];f=d['failing_funds_held_before'];print('NO-SNAPSHOT-BRANCH first_snapshot_date=%s partitions_before_it=%d still_exist=%s built_by=%s listing_denominator=%s page_accepts_an_earlier_date=%s request_made=%s failing_funds_held_before=%d served_from_an_affected_close=%s readers_not_established=%d rows_filed=%d'%(d['first_snapshot_date'],p['count'],p['still_exist'],p['built_by'],p['listing_denominator'],g['accepts_a_date_before_the_first_snapshot'],g['request_made'],f['funds'],d['served_from_an_affected_close'],len(d['readers_not_established']),len(d['rows_filed'])))"</invocation><expect>NO-SNAPSHOT-BRANCH first_snapshot_date=20</expect></criterion>
`CB77by3-AC3` (AMENDMENT 1) -- the first snapshot date is read; the partitions before it are counted with the denominator of the
listing; the page's acceptance of an earlier date is read from code; the failing funds held before are counted; the three readers
not established are named. The issuer reads whether a served figure from an affected close was found and whether a row was filed.

<expected_criteria>CB77by3-AC1,CB77by3-AC2,CB77by3-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below (your deliverables folder and your own NEW channel row) and the file of this order.
- **You change no code, test, config, manifest or registry.**
- **AWS: READS ONLY**, of the served artifact of a reader the census named, for THIS project's firm. No write, no delete, no serve.
- **Another firm's data is never opened.** No account id, no account's value: counts and proportions only.
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
  `ADVI_COTBKF-D2-W145-S<k>` (k from 1), `"fabric": "dell2"`, `surfaced_at` read from the clock, APPENDED to the channel file with
  `open(path, 'a', encoding='utf-8', newline='\n')`; `git diff --numstat` must show added lines only. Never open the channel file with
  an editing tool.

<paths>
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round77.md</decomp_doc> (round 77), cell `CB-by-3`.
<owned_cells>CB-by-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB77by3-AC1, CB77by3-AC2, CB77by3-AC3 (AMENDMENT 1: validate with all three). Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~145/ADVI_COTBKF.TO-CB-by-3.level-error.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB77by3-AC1,CB77by3-AC2` BEFORE the flip. Mechanical: CB77by3-AC1. A judgment criterion is recorded as PENDING-ADJUDICATION, never PASS. An artifact already committed and not changed
in the flip commit is pinned to the commit that carried it, never left `PENDING-THIS-COMMIT`.
</proof_of_spec>

**REPORT:** the census's count of readers serving from an affected close and that the readers sized are exactly those; for each: the figure, the population as counts, the account-days holding a failing fund, the share of value as a distribution, the level by fund as a proportion; or the plain statement that no such reader was found and nothing was sized; every reader left unsized and why; the headline; the `LEVEL-ERROR` line; the account-id scan's DENOMINATOR line; a statement that only this firm's artifact was read and nothing was written; what is not established; commits; every gate refusal, verbatim.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a measurement over a served artifact, read only.
comp-iam: DECLARED-NOT-APPLICABLE no lens was run: reads only of this firm's served artifact under the existing role; no write, delete or serve.
comp-adversary: RUN -- held until the census drains; the readers sized must be exactly the census's, and the check prints both counts; an empty result is a complete result and is reported as one; the size is account-days and proportions, never money; BLIND: a reader the census could not see.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-77 analysis @1101e06fcd (msg 6154), section 3 item 3; `3.0.0_SA_CVO` round-76 grade file @d299fd357a.
