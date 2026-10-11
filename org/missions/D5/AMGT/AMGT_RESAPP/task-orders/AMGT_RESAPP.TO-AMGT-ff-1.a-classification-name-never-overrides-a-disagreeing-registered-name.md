# AMGT_RESAPP task order -- `AMGT-ff-1` -- A CLASSIFICATION NAME NEVER OVERRIDES A REGISTERED COMPANY NAME THAT DISAGREES WITH IT (THE BARE-TICKER COLLISION: SANOFI SERVED AS BANCO SANTANDER)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ff-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~387</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-ff-1.a-classification-name-never-overrides-a-disagreeing-registered-name</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a name-chain rule and its tests, no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- r94_name_census.py reads the crosswalk, the classifications table and stored model blocks with the caller's own credentials (GET only).
comp-adversary: RUN at the cut -- r94_display_name.py FAILs D1 at the base and PASSes D2-D6, and PASSes 6 of 6 against a throwaway candidate; r94_name_census.py --where local reads 2 DIFFERENT companies at the base (SAN_FP_Equity 'Banco Santander S.A.' for Sanofi, CSL_AU_Equity 'Carlisle Cos Inc' for CSL Ltd), 243 of 243 judged against a reference name, and 0 against the candidate which flips exactly those two served names and no other of 243. Cause read: the classifications table is looked up by the BARE Bloomberg ticker (`SAN FP` -> `SAN`); `SAN` is Madrid's Santander and Paris's Sanofi.
EGRESS CLASS, declared: NONE (S3 GETs by the census; no vendor, SEC or model call).
</preflight>

**Your worktree:** `C:/dev/wk-resapp-387b` (branch `wk-AMGT_RESAPP-387`, cut from the issuance commit). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-387` (or the portal path named below); a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout and answers for the wrong tree.

## 1. THE CELL -- `AMGT-ff-1` (round 94, decomposition s.102)

CTO~DELL1 round-93 analysis item 1 (row D1-S23, ARMED; breach of FWD-13). `lib/research/api/names_read.py::display_names(keys, classifications)` names each
key: the classifications table's name looked up by the key's BARE Bloomberg ticker, else the crosswalk's registered name, else the stored model-block name, else
the display ticker. A bare ticker is not a company: the table's `SAN` row names Banco Santander, so `SAN_FP_Equity` (Sanofi) serves "Banco Santander S.A." on the
overlay and the peers subject, and the held-name index (`scoped_amgt._held_name_index`, built from the same chain) carries Santander's name under Sanofi's key;
`CSL_AU_Equity` (CSL Ltd) serves "Carlisle Cos Inc" the same way.

Add ONE rule inside `display_names`, where the classification name is about to be served: when the crosswalk has a registered name for the key (non-empty and
not just the bare ticker, case-insensitive) and the two names DISAGREE, serve the REGISTERED name (cleaned by `scoped_amgt._clean_display_name`) with source
`crosswalk`, instead of the classification name. Two names AGREE when the token sets of `numeric_tickers.name_token(scoped_amgt._clean_display_name(name))`,
each with the GENERIC words {com, stk, cl, class, cos, holdings, holding, group, del, new, and, corp, co, inc, ltd} removed, share at least one token of two or
more characters. No registered name, or a registered name that is only the bare ticker: the chain is unchanged. Nothing else in the chain moves (the order, the
source labels, the model-block and ticker fallbacks, the batching), and `monthly_chatter.py`, `scoped_amgt.py` and every route are untouched: the held-name
index and every route follow from the chain.

Add `lib/research/api/tests/test_names_read_agreement.py` (pure, no network; replace `scoped_amgt._crosswalk_names` and `scoped_amgt.resolve_identity` with
fixtures as `r94_display_name.py` does): one test per arm D1-D6.

### 1b. AMENDMENT 1 -- the same rule at the two other places the table's name is served (the issuer's miss: the first cut changed ONE of three paths)

The chain above (`names_read.display_names`) serves the peers subject's name and the held-name index. The page HEADER prints the overlay's own name
(`scoped_amgt._overlay_name`), and a ranked list prints each row's `name` (`scoped_amgt._join_ranked_rows`); both read the same table by the same bare ticker on their
own paths. Measured on the merged first cut (live function against the merged handler, 243 subjects, overlay and peers routes): only `peers.subject.display_name`
moved (2 subjects); the overlay's `display_name` still reads 'Banco Santander S.A.' for `SAN_FP_Equity`. Make the SAME rule apply there, with one shared helper:

1. `names_read.py`: add `names_disagree(served_name, registered_name, bare_ticker)`: True when `registered_name` is non-empty, is not just the bare ticker
   (case-insensitive), `served_name` is non-empty, and `names_agree(served_name, registered_name)` is False. `display_names` may use it (behaviour unchanged).
2. `scoped_amgt._overlay_name(identity, security_key, ticker)`: where the classification branch would return the table's name, first read the crosswalk's registered
   name for `security_key` (`_crosswalk_names()`); when `names_disagree(...)` is True skip that branch exactly as when the table holds no name (so the existing
   crosswalk branch serves the registered name with `display_name_source` `crosswalk`). Otherwise unchanged.
3. `scoped_amgt._join_ranked_rows(served, route)`: between `_join_covered_identity(rows)` and `_fill_names_from_crosswalk(...)`, add one small step: for every row
   whose `name_source` is the classifications table, with a `security_key` and a registered name for it, when `names_disagree(row["name"], registered, ticker's bare
   form)` is True, set that row's `name` to None, `name_source` to None and `name_state` to `ABSENT` (the existing crosswalk fill then serves the registered name,
   `name_source` `crosswalk`). Every other row is byte-equal. One `_crosswalk_names()` read for the step.

`r94_display_name.py` gains arms D7-D9 for exactly these two paths and `r94_name_census.py --where local` now reads the overlay's name path. Add tests for D7-D9
to `lib/research/api/tests/test_names_read_agreement.py`. Edit `scoped_amgt.py` minimally: do not reformat it and touch nothing else in it.

### 1c. AMENDMENT 2 -- one existing test pins the superseded precedence (the issuer's ruling on row `AMGT_RESAPP-D1-W387-S3`)

`lib/research/api/tests/test_lead_list_names_and_places_moved.py::test_name_from_ranked_source_keeps_its_label_and_crosswalk_fills_the_rest` registers the sentinel name
"SHOULD NOT WIN" for `BA_US_Equity` against the table's "Boeing Co" and asserts the table's name is kept: it pins the OLD precedence for a DISAGREEING pair, which is
exactly what this cell changes (the CTO's ruling: the registered name wins on disagreement). Your reading of S3 is correct and the production code is right. The test's intent
is the precedence for an AGREEING pair. Change that ONE fixture value in that file from `"SHOULD NOT WIN"` to `"BOEING CO SHOULD NOT WIN"` (it shares the token `boeing` with
"Boeing Co", so the names agree and the table's name still wins; the sentinel still proves the precedence), and change nothing else in that file. The file joins `<paths>`.
Re-run AC1-AC3 and rewrite the instance with AC3 PASS; the new D9 arm and your D7-D9 tests already cover the disagreeing case.

### 1d. AMENDMENT 3 -- the rank timeseries is a FOURTH path (found by the issuer's read of the live function after your first merge; `AMGT_RESAPP-D1-S25`)

`scoped_amgt.read_rank_series` (the `/lead-panel/timeseries/{movement}/{subject}?tickers=...` route) serves each series' `name`, `classification` and `name_state`
straight from `_classification_for_ticker(ticker)`: the table's answer for the BARE ticker, with no security key and no registered-name check. Live read, 2026-10-11:
`SAN FP` -> 'Banco Santander S.A. ADR'. The same rule applies here. Do this in `scoped_amgt.py`:

1. Add `_rank_series_names(tickers) -> Dict[str, Dict[str, Any]]` beside `read_rank_series`: for each DISTINCT ticker of `tickers` (input order kept) the table's
   answer `_classification_for_ticker(ticker)`; then, only when at least one answer carries a `name`, read `_crosswalk_names()` once and `_covered_bloomberg_index()`
   once (the SAME exact-ticker match `_join_covered_identity` uses); for each ticker whose answer carries a `name` whose covered security key has a registered name
   and `names_read.names_disagree(answer["name"], registered, ticker)` is True, replace that ONE entry by `dict(answer, name=_clean_display_name(registered),
   name_state="ABSENT")` (a crosswalk-filled ranked row's precedent; `classification`, `status` and `reason` untouched). Every other entry is the table's answer
   object, untouched.
2. In `read_rank_series` replace the per-ticker `served_names` loop by `served_names = _rank_series_names(tickers)`; nothing else in that function changes.
   A failure of `_covered_bloomberg_index()` or `_crosswalk_names()` leaves every entry as the table's answer (a read that fails is never a guess): catch and return.
3. Add tests D10-D12 (mirrored by the check's arms) to `lib/research/api/tests/test_names_read_agreement.py`.
4. Measure and report in your final message the wall time of `python -c` calls of `_covered_bloomberg_index()` (once) in this tree; if one call takes over 2 seconds,
   file a row naming the number (do not change the design).

AC1 now reads 12 arms (D1-D12). AC3 is the WHOLE `lib/research/api/tests` directory but the print-format file (it reads the portal fixture, absent here), so the
control covers every test that touches the three paths.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W387-S<k>`, `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no schedule, no SEC, vendor, model or Bloomberg call.
2. No `bun`, `npm` or `pip install`. `r94_name_census.py`'s S3 GETs are permitted; nothing else is fetched.
3. Standing: no S3 delete, no push of shared branches.
4. Edit `names_read.py` and `scoped_amgt.py` minimally: do not reformat them and do not touch `monthly_chatter.py`, `numeric_tickers.py` or any other function of `scoped_amgt.py`.

## 3. SURFACES

<paths>
lib/research/api/names_read.py
lib/research/api/scoped_amgt.py
lib/research/api/tests/test_names_read_agreement.py
lib/research/api/tests/test_lead_list_names_and_places_moved.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~387/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ff-1"><invocation>cd C:/dev/wk-resapp-387b &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round94_prep/checks/r94_display_name.py"; echo "exit=$?"</invocation><expect>PASS D1 (a classification name that disagrees with the registered name is not served), PASS D2, PASS D3, PASS D4, PASS D5, PASS D6, PASS D7 (the overlay), PASS D8, PASS D9 (a ranked row), PASS D10 (a rank series), PASS D11, PASS D12; arms passed 12 of 12; R94 DISPLAY NAME: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ff-1"><invocation>cd C:/dev/wk-resapp-387b &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round94_prep/checks/r94_name_census.py" --where local; echo "exit=$?"</invocation><expect>judged 243 of 243 subjects, UNJUDGED 0, DIFFERENT company 0, the spelling variants listed; PASS C1; the ranked lists read 188 rows with 126 judged and DIFFERENT company 0 (PASS C3); the rank timeseries of those tickers reads DIFFERENT company 0 over a non-zero judged count (PASS C4); R94 NAME CENSUS: YES; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-ff-1"><invocation>cd C:/dev/wk-resapp-387b &amp;&amp; PYTHONPATH="$(pwd)" python -m pytest lib/research/api/tests --ignore=lib/research/api/tests/test_print_format_rich.py -q -p no:cacheprovider; echo "exit=$?"</invocation><expect>the control: the new test file and every other test of lib/research/api/tests pass (no failed, no error; about 940 passed); and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~387 <0.9.0_WK_AMGT_RESAPP~387@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~387/AMGT_RESAPP.TO-AMGT-ff-1.a-classification-name-never-overrides-a-disagreeing-registered-name.proof_of_spec.json`
with `to_id` equal to the `<to_id>` line above, character for character.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the diff of each edited product file, in full;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO~DELL1 round-93 analysis @bfa6b04c8c item 1: "A classification name never overrides a registered company name that disagrees with it, and the held-name index carries ONE company per key. Close: a census of every served subject whose display name differs from its crosswalk company, count printed: 0 wrong companies, spelling variants listed. It is a served change, under its own pair." The census (`r94_name_census.py`) judges each of the 243 MEASURED subjects against every reference name its record holds (registered identity name 68, `legal_name` 211, research folder 96, model-block header 100); 0 are unjudged. The base reads 2 wrong companies, not the 1 the packet named (CSL_AU_Equity served as Carlisle Cos Inc). 35 are spelling variants and are listed, not defects. Producer-side code; the served change is `AMGT-ff-4` (staged, its own pair).

<status>pending</status>
<round>94</round>
<slot>0.9.0_WK_AMGT_RESAPP~387</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>complete -- issuer close 2026-10-11T12:59Z (2.0.0_SA_COO~R1): wk-AMGT_RESAPP-387 @05e912764e (code @fdc8659371) merged @dc40353618, proof instance VALID; issuer re-run in the worktree: AC1 R94 DISPLAY NAME YES (6 of 6), AC2 R94 NAME CENSUS YES (243 of 243 judged: registered name 68, legal_name 211, folder 96, model block 100; 0 unjudged; 0 different companies; 35 spelling variants listed), AC3 105 passed; drain checks py_compile rc 0, ruff clean, 540 passed over filings, peers and the names tests. names_read.py +26/-4: `names_agree` and the disagreement test inside `display_names`. The census flips exactly SAN_FP_Equity (Sanofi for Banco Santander) and CSL_AU_Equity (CSL Ltd for Carlisle Cos Inc) of 243. NOT SERVED until AMGT-ff-4. Worker rows ruled: S1 (the check's docstring said four letters, the order and census two characters: the code follows the order; docstring corrected) stands; S2 (ARMED: the channel header's one-fenced-block instruction would mis-append, the file holds one row per block; appended in the file's existing shape) stands, disarmed: no action is owed.</status>
<status>complete -- 2026-10-11T13:48Z by the issuer (2.0.0_SA_COO~R1): W387's AMENDMENT 1 and 2 merged @7e9d36c697 (branch tip 7213fcc909). Issuer re-run on the merged tree: r94_display_name.py 9 of 9 (R94 DISPLAY NAME YES); r94_name_census.py --where local 243 of 243 judged, DIFFERENT 0, C3 ranked rows 126 judged DIFFERENT 0 (R94 NAME CENSUS YES); AC3 158 passed; the whole lib/research/api/tests directory 939 passed, the same 3 print-format errors as at the base (no portal fixture), 0 new failures after the fixture edit. Row D1-W387-S3 RULED by AMENDMENT 2 (an existing test pinned the superseded precedence for a disagreeing pair; fixture value changed, production code stands). Proof instance VALID.</status>
<status>pending -- REOPENED AGAIN 2026-10-11T13:55Z by the issuer (2.0.0_SA_COO~R1): AMENDMENT 3 (section 1d): the rank timeseries series name is a fourth path (row D1-S25); the cell had been closed @48b8044b30 on the merge @7e9d36c697. Re-seat of slot ~387 in worktree C:/dev/wk-resapp-387b.</status>
