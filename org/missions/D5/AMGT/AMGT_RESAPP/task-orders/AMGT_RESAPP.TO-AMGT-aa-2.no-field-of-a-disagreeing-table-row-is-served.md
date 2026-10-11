# AMGT_RESAPP task order -- `AMGT-aa-2` -- NO FIELD OF A TABLE ROW WHOSE NAME DISAGREES WITH THE REGISTERED NAME IS SERVED FOR THE SECURITY

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-aa-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~391</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-aa-2.no-field-of-a-disagreeing-table-row-is-served</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a serve-time rule and its tests, no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- r95_classification_census.py --where local reads the crosswalk, the classifications table (GetItem) and the handler's own stored reads with the caller's own credentials (GET only).
comp-adversary: RUN at the cut -- r95_classification_census.py --where deployed FAILs K1, K2, K3 at the live base (SAN FP's row 67 of both PRICE lists, both rank series and the three collected-chatter windows serve 'Health Care'; CSL AU serves 'US Large Cap' where listed) and PASSes K4, K5; against a throwaway candidate (--where local) 5 of 5 with 2 rows, 2 series and 3 chatter rows withheld and 186 and 186 control rows unchanged; r94_display_name.py 12 of 12 and r94_name_census.py YES are unchanged at the base.
EGRESS CLASS, declared: NONE (S3 and DynamoDB GETs by the census; no vendor, SEC or model call).
</preflight>

**Your worktree:** `C:/dev/wk-resapp-391` (branch `wk-AMGT_RESAPP-391`, cut from the issuance commit). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-391`; a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout and answers for the wrong tree.

## 1. THE CELL -- `AMGT-aa-2` (round 95, decomposition s.103)

CTO~DELL1 round-94 analysis item 2 (row `D1-S26`, ARMED). The classifications table is keyed by the BARE Bloomberg ticker. `CSL` is Carlisle (the row's name is 'Carlisle Cos
Inc', sub-asset class 'US Large Cap') while the security `CSL_AU_Equity` is CSL Ltd, so its classification is another company's; `SAN`'s row is named 'Banco Santander S.A.
ADR' under Sanofi's ticker. Round 94 made the NAME the registered company's (`names_read.names_disagree`, `AMGT-ff-1`). The same test now governs the row's other fields:

> When the table row's name DISAGREES with the security's registered name, NO field of that row is served for the security. `classification` is null, `sector` is null, and
> the page says why in plain words: `classification not available for this listing`.

Do exactly this, in three places that each read the table by ticker and that `AMGT-ff-1` already made name-aware (do NOT touch `_classification_for_ticker`, the table read or
its cache; do NOT touch `names_read.py`):

1. `scoped_amgt.py`: add the constant `CLASSIFICATION_WITHHELD_REASON = "classification not available for this listing"`. In `_drop_disagreeing_table_names(rows)` (a ranked
   row whose `name_source` is the classifications table and whose `names_disagree` is True), besides what it does now also set that row's `classification` to None, `sector` to
   None and `sector_reason` to the constant.
2. `scoped_amgt.py`: in `_rank_series_names(tickers)` a disagreeing entry also gets `classification` None and `classification_reason` set to the constant (its `name`/`name_state`
   rule is unchanged); `read_rank_series` copies `classification_reason` onto the series object when the entry carries one (an additive key, present only on a withheld series).
3. `monthly_chatter.py`: a collected-chatter row (the call of `_classification_fields(ticker, served)` that builds each row) whose served table name disagrees with the row's
   registered name (`names_read.names_disagree(served name, registered name of the row's security_key, ticker)`) serves `classification` None and `classification_reason` the
   same constant. `_crosswalk_names()` is read at most once per request.

No per-security route (overlay, thesis, peers, coverage, compare, timeline) serves a subject classification today (`r95_classification_census.py` K4 guards that); the peers' members carry their own companies' sectors and are not touched. The classification is served only by the three list routes above.
Note for the reader of the census: `SAN FP`'s table row is `classified_by: legacy` 'Health Care' under a Santander name (the census prints both rows whole); under the rule as
written its classification is withheld too, because its row disagrees. That is the rule, and the pair's table will list it before any served change.

Add `lib/research/api/tests/test_classification_withheld.py` (pure, no network; fixtures replace `_crosswalk_names`, `_classification_for_ticker` and
`_covered_bloomberg_index` as `r94_display_name.py` does): one test per place and a control that an agreeing row keeps its classification byte-equal.

### 1b. AMENDMENT 1 -- two existing assertions pin the round-94 reading "a withheld series keeps its classification" (the issuer's ruling on rows `AMGT_RESAPP-D1-W391-S1` and `S2`)

Your reading of both rows is right and your production code stands. Round 94's arm D10 of `r94_display_name.py` and the test of the same arm in
`lib/research/api/tests/test_names_read_agreement.py` (`test_d10_a_rank_series_whose_table_name_disagrees_serves_the_registered_name`, the line
`assert got["SAN FP"]["classification"] == table["SAN FP"]["classification"]`) were written for the rule BEFORE this cell and assert that a series whose name is replaced keeps
its table classification: this cell changes exactly that. The issuer has changed the check file (`r94_display_name.py` D10 now asserts `classification` None and a
`classification_reason` containing "not available for this listing"; it is on your branch at the commit that carries this order). You change the test: in that one test
replace the classification assertion by `assert got["SAN FP"]["classification"] is None` and `assert "not available for this listing" in got["SAN FP"]["classification_reason"]`, and
change nothing else in that file (`status` stays asserted equal). The file joins `<paths>`. Re-run AC1-AC3 and rewrite the instance; the two rows are ruled by this amendment.

### 1c. AMENDMENT 2 -- the rank series resolves a ticker only through the COVERED universe, and `CSL_AU_Equity` is not in it (the issuer's measurement after your merge)

The census read `CSL AU` asked for BY TICKER on the rank timeseries after your merge @b12a5c865b: it still serves 'Carlisle Cos Inc' (name) and 'US Large Cap'
(classification), because `_rank_series_names` finds a ticker's security key with `_covered_bloomberg_index()` (the 95 covered names) and `CSL_AU_Equity` is a MEASURED crosswalk
subject outside that universe. K2 judged only the series of tickers a ranked list holds (CSL AU is on none), so it passed without seeing it; the new arm K6 asks for every
disagreeing ticker by ticker. The close the CTO set is that CSL AU serves no Carlisle field on the rank timeseries. Do exactly this in `scoped_amgt.py`:

1. Add `_measured_ticker_index() -> Dict[str, str]`: ticker -> security_key over every crosswalk record whose `resolution` is `MEASURED` and that has a `security_key`, the ticker
   taken from `resolve_identity(key)["bloomberg"]` (as `_covered_bloomberg_index` takes it); `setdefault` so the first record wins; `crosswalk.load_crosswalk()` is read once.
2. In `_rank_series_names(tickers)` build the lookup as `{**_measured_ticker_index(), **_covered_bloomberg_index()}` (the covered entry wins where both name a ticker) and use it
   instead of `_covered_bloomberg_index()` alone; a failed read of either leaves every answer as the table's (the existing `try`). Change nothing else: the ranked join and the
   collected-chatter rows already carry the security key and are not touched.
3. Add to `test_classification_withheld.py` one test: a ticker that is in the measured index and not in the covered index, whose table name disagrees, is withheld with the reason
   and its name replaced (the arm D10's shape), and an agreeing measured ticker is returned byte-equal.

AC1's census now has six arms (K1-K6). The issuer's measurement: the arm reads FAIL at the merged base (K6: CSL AU 'Carlisle Cos Inc' / 'US Large Cap') and 6 of 6 against a
throwaway candidate that widens the lookup exactly so.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W391-S<k>`, `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no schedule, no SEC, vendor, model or Bloomberg call.
2. No `bun`, `npm` or `pip install`. The checks' S3 and DynamoDB reads (GET only) are permitted; nothing else is fetched.
3. Standing: no S3 delete, no push of shared branches.
4. Edit the named product files minimally: do not reformat them and touch no function the cell does not name.
5. `names_read.py` and `_classification_for_ticker` are not touched; no field is withheld for a row that AGREES with the registered name or has no registered name.

## 3. SURFACES

<paths>
lib/research/api/scoped_amgt.py
lib/research/api/monthly_chatter.py
lib/research/api/tests/test_classification_withheld.py
lib/research/api/tests/test_names_read_agreement.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~391/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-aa-2"><invocation>cd C:/dev/wk-resapp-391 &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round95_prep/checks/r95_classification_census.py" --where local; echo "exit=$?"</invocation><expect>two disagreeing table rows listed (CSL_AU_Equity, SAN_FP_Equity) with their rows whole; PASS K1 (ranked rows withheld, with the reason), PASS K2 (rank series), PASS K3 (collected chatter, three windows), PASS K4, PASS K5 (186 ranked rows and 186 series unchanged), PASS K6 (every disagreeing ticker asked for by ticker); arms passed 6 of 6; R95 CLASSIFICATION CENSUS: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-aa-2"><invocation>cd C:/dev/wk-resapp-391 &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round94_prep/checks/r94_display_name.py" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round94_prep/checks/r94_name_census.py" --where local; echo "exit=$?"</invocation><expect>the names are unmoved: R94 DISPLAY NAME: YES (12 of 12) and R94 NAME CENSUS: YES (C1, C3, C4 at 0 different); and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-aa-2"><invocation>cd C:/dev/wk-resapp-391 &amp;&amp; PYTHONPATH="$(pwd)" python -m pytest lib/research/api/tests --ignore=lib/research/api/tests/test_print_format_rich.py -q -p no:cacheprovider; echo "exit=$?"</invocation><expect>the control: the new test file and every other test of lib/research/api/tests pass (no failed, no error; about 950 passed); and exit=0</expect></criterion>
</proof_of_spec>


<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO~DELL1 round-94 analysis item 2: "D1-S26: no field of a disagreeing table row is served. When the registered name disagrees with the table row's name for the bare ticker, no field of that row is served for the security, and the page says why ('classification not available for this listing'). Close: CSL AU serves no Carlisle field on the overlay, the ranked join or the rank timeseries. SAN FP's classification row is read and shown to be Sanofi's, beside a control whose classification is unchanged. It is a served change: its redeploy is under its own pair, measured route by route as ff-4 was." READ: the rule withholds SAN FP's too (its row's name disagrees); the census prints SAN's row (a legacy 'Health Care' under a cleaned Santander name) and the control arm K5 is the 'unchanged' control. The CTO is asked to confirm that reading (message with the issuance); the pair's table lists SAN FP's change either way. The overlay arm K4 is a guard (the subject's own classification is not served there today). aa-4 follows on this slot's queue (same file).

<status>complete -- 2026-10-11T17:20Z by the issuer (2.0.0_SA_COO~R1): AMENDMENTS 1 and 2 merged (b12a5c865b, then wk-AMGT_RESAPP-391 @5fd5f992f3, code @b6ebfa196e, merged @fe7175efde), proof instance VALID; issuer re-run on the merged tree: AC1 R95 CLASSIFICATION CENSUS YES (6 of 6: K1 2 ranked rows, K2 2 rank series, K3 3 chatter rows withheld with the reason, K4 no per-security route carries a classification, K5 186 and 186 control rows unchanged, K6 every disagreeing ticker asked for by ticker serves neither the table row's name nor its classification), AC2 R94 DISPLAY NAME YES (12 of 12) and R94 NAME CENSUS YES, AC3 lib/research/api/tests 956 passed. scoped_amgt.py: `_measured_ticker_index` and the series lookup `{**measured, **covered}`. Worker rows W391-S3 (an empty portal submodule skips two tests in a re-seated worktree) and S4 (the order's literal worktree path) INERT. Served change: NONE until AMGT-aa-5.</status>
<round>95</round>
<slot>0.9.0_WK_AMGT_RESAPP~391</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
