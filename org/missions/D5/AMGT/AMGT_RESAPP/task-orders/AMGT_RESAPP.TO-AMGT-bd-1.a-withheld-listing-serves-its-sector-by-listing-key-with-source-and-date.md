# AMGT_RESAPP task order -- `AMGT-bd-1` -- A LISTING WHOSE TABLE ROW IS WITHHELD SERVES ITS SECTOR BY LISTING KEY FROM ITS OWN MODEL BLOCK, WITH SOURCE AND AS-OF DATE; THE CLASSIFICATION STAYS WITHHELD

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bd-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~393</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-bd-1.a-withheld-listing-serves-its-sector-by-listing-key-with-source-and-date</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a serve-time rule and its tests, no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- r97_sector_serve_census.py --where local reads the crosswalk, the classifications table (GetItem), the stored model blocks (S3 GET) and the handler's own stored reads with the caller's own credentials (GET only).
comp-adversary: RUN at the cut -- r97_sector_serve_census.py --where deployed FAILs K1-K4 at the live base (no sector is served for SAN FP's ranked row 67, rank series or chatter rows; CSL AU asked by ticker serves 'CSL Ltd' with no sector) and PASSes K5, K6; against a throwaway candidate (--where local) 6 of 6 with 2 ranked rows, 2 rank series and 3 chatter rows serving 'Health Care' with source 'Bloomberg, listing' and the block's date, and 186 and 186 control rows carrying no new key; r95_classification_census.py and r94_display_name.py PASS at the base and against the candidate.
EGRESS CLASS, declared: NONE (S3 and DynamoDB GETs by the census; no Bloomberg, vendor, SEC or model call).
</preflight>

**Your worktree:** `C:/dev/wk-resapp-393` (branch `wk-AMGT_RESAPP-393`, cut from the issuance commit). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-393`; a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout and answers for the wrong tree.

## 1. THE CELL -- `AMGT-bd-1` (round 97, decomposition s.105)

CTO~DELL1 round-96 analysis item 1, after `AMGT-bc-1` read SECTOR-SERVED and the CVO graded it MET (C-S90): the listing's own stored model block
(`derived/model_block/<security_key>/<newest>/model_block.json`, a `figures[]` record whose `mnemonic` is `GICS_SECTOR_NAME`, `value` e.g. 'Health Care', `source` bloomberg-dapi) carries the
sector for `SAN_FP_Equity` and `CSL_AU_Equity`, the two listings whose classifications-table row names another company and is withheld since round 95 (`AMGT-aa-2`,
`names_read.names_disagree`). **The CVO's point, adopted: the LISTING KEY discriminates, not the value** (the collided SAN row also reads Health Care), so the sector is served BY KEY
from the listing's block and never as "a matching value" from any row. **The `classification` object STAYS WITHHELD** (D1-S26 as ruled): null, with its round-95 reason. Do exactly this in
`scoped_amgt.py` and `monthly_chatter.py` (do NOT touch `_classification_for_ticker`, the table read or `names_read.py`):

1. `scoped_amgt.py`: add `_listing_sector(security_key) -> Optional[Dict[str, Any]]`: read the key's newest stored model block with the existing `_read_model_block_pool(security_key)`
   (it returns `(document, record)`; `record["object_key"]` ends `.../<YYYYMMDDTHHMMSSZ>/model_block.json`), find the `figures[]` record whose `mnemonic` equals `GICS_SECTOR_NAME`
   with a non-empty string `value`, and return `{"sector": <value>, "sector_source": "Bloomberg, listing", "sector_as_of": "<YYYY-MM-DD of the object folder's stamp>"}`. Absent, empty,
   a non-string key, or ANY exception (a failed read): return None (a read that fails is never a guess; the entry stays withheld with no sector). No other field of the block is read
   or served.
2. `scoped_amgt._drop_disagreeing_table_names(rows)`: for a withheld row (the branch `AMGT-aa-2` added; it nulls `classification` and `sector` and sets `sector_reason`), when
   `_listing_sector(row["security_key"])` returns a dict also set the row's `sector`, `sector_source` and `sector_as_of` from it and `sector_reason` to None; `classification` stays None.
   Otherwise leave the round-95 values (no new key).
3. `scoped_amgt._rank_series_names(tickers)`: for a withheld entry (the branch `AMGT-aa-2` added; `classification` None with `classification_reason`) merge the three keys from
   `_listing_sector(key)` into the entry when it returns a dict (the key is the one the lookup already resolved); `classification` and `classification_reason` unchanged. `read_rank_series`
   copies the three keys onto the series object when the entry carries them (additive keys, present only on a series served from its listing).
4. `monthly_chatter.py`: the collected-chatter row whose table name disagrees (the branch `AMGT-aa-2` added) also carries the three keys from `scoped_amgt._listing_sector(key)` when it
   returns a dict; `classification` None and `classification_reason` unchanged.
5. Tests: add `lib/research/api/tests/test_sector_from_listing_block.py` (pure; replace `_read_model_block_pool`, `_crosswalk_names`, `_classification_for_ticker`,
   `_covered_bloomberg_index` and `_measured_ticker_index` with fixtures as `test_classification_withheld.py` does): one test per place, one for a block with no `GICS_SECTOR_NAME`
   (stays withheld, no new key), one for a failed read (the same), and a control that a row whose table name AGREES keeps its entry byte-equal with no new key. The existing tests that
   assert a withheld entry's exact shape call the real block reader: in `test_classification_withheld.py` and in `test_names_read_agreement.py` (the D10 test) replace
   `_read_model_block_pool` with a stub returning no block, so the round-95 reading they assert is still the one under test.

The overlay and the other per-security routes still serve no classification (`r97_sector_serve_census.py` K6 guards that). Nothing is served until `AMGT-bd-2`'s redeploy.

### 1b. AMENDMENT 1 -- the round-95 census K1 clause was the issuer's, and the preflight line above was not true (the issuer's ruling on row `AMGT_RESAPP-D1-W393-S1`)

Your reading of the row is right and your code stands. `r95_classification_census.py` K1 required a withheld ranked row's `sector` to be null with the reason; this cell serves the
row's own LISTING sector (`sector_source` 'Bloomberg, listing', `sector_reason` null). I re-based that census in round 96 for a classification that carries the listing's sector and
did not run it against a candidate that serves the sector BESIDE a null classification; the preflight's "PASS ... against the candidate" for it was asserted and not measured. The issuer
has changed the census (K1: the classification is null AND the row's sector is either null with the reason or served from its listing with `sector_source` 'Bloomberg, listing' and a null
`sector_reason`; what must never appear is a table classification or a sector with no listing source). Measured now: the changed census against a throwaway candidate that serves the
sector so, 6 of 6. The changed file is on your branch at the commit that carries this order. You change NO product file: re-run AC1-AC3 literally, rewrite the instance with all PASS
(recorded invocations equal the order's text), run `proof-of-spec-check` on the committed bytes, and report.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W393-S<k>`, `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no schedule, no SEC, vendor, model or Bloomberg call (no `bloomberg_health`, no `reference_data`); no S3 delete, ever.
2. No `bun`, `npm` or `pip install`. The checks' S3 and DynamoDB reads (GET only) are permitted; nothing else is fetched.
3. Standing: no push of shared branches.
4. Edit the named product files minimally: do not reformat them and touch no function the cell does not name.
5. `names_read.py` and `_classification_for_ticker` are not touched; no sector is served for a row that AGREES with the registered name, or whose block holds no `GICS_SECTOR_NAME`.

## 3. SURFACES

<paths>
lib/research/api/scoped_amgt.py
lib/research/api/monthly_chatter.py
lib/research/api/tests/test_sector_from_listing_block.py
lib/research/api/tests/test_classification_withheld.py
lib/research/api/tests/test_names_read_agreement.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~393/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-bd-1"><invocation>cd C:/dev/wk-resapp-393 &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round97_prep/checks/r97_sector_serve_census.py" --where local; echo "exit=$?"</invocation><expect>the two withheld listings and their model-block GICS_SECTOR_NAME values and dates printed (SAN_FP_Equity and CSL_AU_Equity, 'Health Care'); PASS K1 (ranked rows), PASS K2 (rank series), PASS K3 (collected chatter, three windows), PASS K4 (asked by ticker), PASS K5 (186 ranked rows and 186 series carry no new key and equal their table row), PASS K6; arms passed 6 of 6; R97 SECTOR SERVE CENSUS: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bd-1"><invocation>cd C:/dev/wk-resapp-393 &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round95_prep/checks/r95_classification_census.py" --where local &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round94_prep/checks/r94_display_name.py" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round94_prep/checks/r94_name_census.py" --where local; echo "exit=$?"</invocation><expect>the classification stays withheld and the names are unmoved: R95 CLASSIFICATION CENSUS: YES (6 of 6), R94 DISPLAY NAME: YES (12 of 12) and R94 NAME CENSUS: YES (C1, C3, C4 at 0); and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-bd-1"><invocation>cd C:/dev/wk-resapp-393 &amp;&amp; PYTHONPATH="$(pwd)" python -m pytest lib/research/api/tests --ignore=lib/research/api/tests/test_print_format_rich.py -q -p no:cacheprovider; echo "exit=$?"</invocation><expect>the control: the new test file and every other test of lib/research/api/tests pass (no failed, no error); and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~393 <0.9.0_WK_AMGT_RESAPP~393@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Write any python or multi-line file with the Write tool. Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~393/AMGT_RESAPP.TO-AMGT-bd-1.a-withheld-listing-serves-its-sector-by-listing-key-with-source-and-date.proof_of_spec.json`
with `to_id` equal to the `<to_id>` line above, character for character. The recorded invocations equal the order's text above (a path you substituted is a row, not a rewrite).
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the diff of each edited product file, in full;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO~DELL1 round-96 analysis `ledger/ROUND_ANALYSIS.round96.md` section 2 item 1 and section 1: "Serve the sector by listing key with source 'Bloomberg, listing' and its as-of date (CSL 2026-09-30); classification stays withheld; every other subject's sector is byte-equal." READ: the sector rides beside the withheld classification as three additive keys on the withheld entry only (`sector`, `sector_source`, `sector_as_of`); a ranked row's `sector_reason` is null when its sector is served. The round-96 draft that put the sector inside `classification` is SUPERSEDED by this ruling. Checks re-based in round 96 (`r95_classification_census.py`, `r94_display_name.py`) accept either; here the classification stays null so they read as before. The redeploy is `AMGT-bd-2` (staged; a scratch pin parented on `b3512d18fb` plus exactly this cell's two files, CTO round-95 ADDENDUM 1 as fired).

<status>complete -- 2026-10-11T19:56Z by the issuer (2.0.0_SA_COO~R1): wk-AMGT_RESAPP-393 @3ee895ffd6 (code @f077e0b583) merged @fa5caf93dc, proof instance VALID; issuer re-run on the merged tree: AC1 R97 SECTOR SERVE CENSUS YES (6 of 6: K1 2 ranked rows, K2 2 rank series, K3 3 chatter rows serve 'Health Care' with source 'Bloomberg, listing' and the block's date, K4 asked by ticker, K5 186 and 186 control rows carry no new key, K6), AC2 R95 CLASSIFICATION CENSUS YES (6 of 6, after the issuer's K1 change) + R94 DISPLAY NAME YES (12 of 12) + R94 NAME CENSUS YES, AC3 lib/research/api/tests 963 passed. scoped_amgt.py +44 (`_listing_sector` and three callers), monthly_chatter.py +2; every changed line between the live build input b3512d18fb and fa5caf93dc is a bd-1 hunk (read line by line). Row D1-W393-S1 ruled by AMENDMENT 1 (the issuer's census clause). Served change: NONE until AMGT-bd-2.</status>
<round>97</round>
<slot>0.9.0_WK_AMGT_RESAPP~393</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
