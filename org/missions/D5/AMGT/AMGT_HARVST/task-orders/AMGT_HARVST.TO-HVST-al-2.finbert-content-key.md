# AMGT_HARVST task order -- `HVST-al-2` -- ROUND 39 CHAIN B (PRD v0.17 FWD-16; row Z-S67; round-38 analysis ruling 1): FINBERT TONE KEYED TO A CONTENT HASH OF THE EXACT TEXT SCORED

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-al-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~90</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched.
comp-iam: RUN at L5 -- LOCAL code and plants. 0 FinBERT Lambda calls of any kind: FWD-16 is HELD on the publisher-terms card and no publisher text reaches the scorer. No S3 write. AC2 and AC3 read live silver read-only through a capturing client that sends no put.
comp-adversary: RUN at L5 -- the adversary is a key that still moves on a re-silvering (it hashes run_stamp, fetched_at or anything other than the scored text), a key computed from different text than the scorer receives, a window join left on record_hash, or a `score` run that sends publisher text while the card is open.
</preflight>

## 0. THE CELL

`lib/research/harvest/finbert_sentiment.py` keys the FinBERT score store (`article_sentiment`) to silver's `record_hash`.
- Silver's `record_hash` hashes every column but bronze_key, fetched_at and record_hash, and `run_stamp` is one of them
  (`lib/research/harvest/store.py:330-334`). So every re-silvering of an unchanged article makes a new key, and the
  article would be re-scored.
- PRD v0.17 FWD-16 requires the tone to be keyed to a CONTENT hash of the exact text scored, so that a changed article is
  re-scored and an unchanged one never is.
- `article_text(silver_row)` already produces the scored text, and `SENTIMENT_SCHEMA` already has `text_sha256`.

`lib/research/harvest/publication_gold.py` `build_mention` joins the tone by `record_hash` through its
`sentiment_by_hash` parameter. `lib/research/harvest/window_tone.py` `build_window_rows` joins it the same way, from
the mention rows.

## 1. THE BUILD (LOCAL; no Lambda call)

1. **In `finbert_sentiment.py`:**
   - add `content_key(text)`: sha256 hex of `text.encode("utf-8")`, and None for None;
   - the store is keyed by `content_key(article_text(row))` (the `text_sha256` column);
   - `latest_scores(client=None)` returns `{content_key: {"label", "score", "scorer"}}`;
   - `score_missing` scores only the articles whose content key is not already scored, so a re-silvered unchanged
     article makes 0 calls;
   - `record_hash` stays in the row as provenance, but it is NOT a key.
2. **In `publication_gold.build_mention`:**
   - rename the parameter to `sentiment_by_key`;
   - append the nullable `sentiment_content_key` (string) to `GOLD_MENTION_SCHEMA`;
   - each row carries `content_key(article_text(<its silver article row>))`, or null when unscorable;
   - the 3 tone fields are joined by that key.
   Nothing else in the row changes.
3. **In `window_tone.build_window_rows` and `build_window`:** join the tone by each mention row's
   `sentiment_content_key`. The parameter is `sentiment_by_key`.
4. Update `test_ak1_finbert_sentiment.py`, `test_ak2_window_tone.py` and `test_ak4_ft_quarantine.py` wherever they plant
   by `record_hash`.
5. **Plants** in `lib/research/harvest/test_al2_content_key.py`, with no network and a stub invoker:
   - (i) an article re-silvered with a new run_stamp and record_hash but the same text keeps its key and makes 0 calls;
   - (ii) a changed body gets a new key and is scored;
   - (iii) `content_key` equals the sha256 of the exact `article_text` the invoker receives;
   - (iv) build_mention joins by the content key;
   - (v) the window rows join by the content key;
   - (vi) a quarantined (ft) article still makes 0 calls.
6. Do NOT run `finbert_sentiment score` without `--dry-run`. Make 0 Lambda calls.
7. Both suites stay green: `python -m pytest lib/research/harvest -q` and `python -m pytest lib/opal_data_harvest -q`.
   Report the counts before and after.

Worktree: `C:/Users/Opal Bloomberg/Desktop/wk-hvst-r39-90`, branch `wk-AMGT_HARVST-90-r39b`, cut from CLOUD at the issuance
commit (sparse cone per decomposition section 50). Do not touch any `.runtime` directory.

<paths>
lib/research/harvest/finbert_sentiment.py
lib/research/harvest/publication_gold.py
lib/research/harvest/window_tone.py
lib/research/harvest/test_ak1_finbert_sentiment.py
lib/research/harvest/test_ak2_window_tone.py
lib/research/harvest/test_ak4_ft_quarantine.py
lib/research/harvest/test_al2_content_key.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~90/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 2. PROOF OF SPEC (each invocation LITERAL; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-al-2"><invocation>python -m pytest lib/research/harvest/test_al2_content_key.py -rA --tb=line</invocation><expect>passed</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-al-2"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round39/checks/al-2.AC2.py</invocation><expect>AC2 RESULT: PASS</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-al-2"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round39/checks/al-2.AC3.py</invocation><expect>AC3 RESULT: PASS</expect></criterion>
</proof_of_spec>

- AC2 and AC3 build the gold mention rows over 5 securities from live silver through a capturing client. They send no
  put and call no Lambda.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~90/AMGT_HARVST.TO-HVST-al-2.finbert-content-key.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-al-2.finbert-content-key`.
- Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** Round-38 analysis @3da5563fd8, ruling 1 and enrichment item 2; PRD v0.17; row Z-S67. It is built, NOT
run on publisher text, while the publisher-terms card @8d20bc24c8 is open. Served gold gains `sentiment_content_key`
only at a later rebuild under its own pair.

<risk>SERVED</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>39</round>
<slot>~90</slot>
<fabric>site-z</fabric>
