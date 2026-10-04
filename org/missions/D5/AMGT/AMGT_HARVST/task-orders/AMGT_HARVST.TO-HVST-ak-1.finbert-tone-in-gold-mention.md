# AMGT_HARVST task order -- `HVST-ak-1` -- ROUND 38 CHAIN A CELL 1 (FWD-16, PRD v0.15): THE FINBERT SCORER, THE `article_sentiment` SCORE STORE, AND THE TONE ON EVERY GOLD MENTION ROW

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-ak-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~90</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched.
comp-iam: RUN at L5 -- the identity that runs HARVST gold builds on site-Z (IAM user Andrew_Berman) DryRun-invoked `opal-news-ai-sentiment` at 19:4xZ: StatusCode 204, so the invoke is already granted. The Lambda is an Opal container image (3008 MB, 900 s, Active). No S3 write in this cell: served gold moves only at the issuer's rebuild under its own never-widen pair. Live Lambda calls in this cell: AC2's 3 texts, plus at most 10 contract probes.
comp-adversary: RUN at L5 -- the adversary is a "score" that never reached the Lambda (a stub left wired in), a neutral label stored as a signed non-zero, an unchanged record_hash re-scored, or a change that moves any pre-existing gold mention field.
</preflight>

## 0. THE CELL

FWD-16 says every harvested article carries its FinBERT tone in gold, scored once per version of the article (its
silver `record_hash`), by the existing Opal FinBERT Lambda `opal-news-ai-sentiment`. No new model is involved.

The Lambda's container source is NOT in the repo. Its contract is inferred from its one caller,
`infra/aws/lambda/finbert_batch_processor/lambda_function.py` (lines 75-100):
- the request is one text per synchronous call, `{"text": text}`;
- the response has statusCode 200 and a JSON `body` with `sentiment` (positive, negative or neutral) and `confidence`;
- the signed score is computed by the CALLER: +confidence, -confidence, or 0.0 for neutral.
Confirm the live shape with at most 10 probe calls before you build on it. If the live response differs, follow the live
shape and file a row.

`lib/research/harvest/publication_gold.py` builds the gold mention rows: `GOLD_MENTION_SCHEMA` (around line 64) and
`build_mention` (around line 1031). Each row copies `record_hash`, `title` and `published_precision` from the newest silver
article row (around lines 318-321). Silver article rows carry `title` and `text_blocks` (a list of strings). Gold
already treats the first 3 blocks as the article's lead (around line 190).

## 1. THE BUILD (code LOCAL; the only live calls are the probes and AC2)

1. **New `lib/research/harvest/finbert_sentiment.py`:**
   - `SCORER = "opal-news-ai-sentiment"`; region us-east-1.
   - `article_text(silver_row)`: returns `"{title}. {lead}"`, where lead is the first 3 `text_blocks` joined with a
     space. Use the title alone when there are no blocks, the lead alone when there is no title, and None when there
     is neither (unscorable). No other cleaning.
   - `score_text(text, invoke=None)`: returns `{"label", "confidence" (float), "score"}`. The score is +confidence,
     -confidence or 0.0 by label. `invoke=None` calls the Lambda through boto3 (`InvocationType="RequestResponse"`).
   - `TABLE = "article_sentiment"` and `SENTIMENT_SCHEMA` with these fields: record_hash, article_key, publisher,
     label (nullable), confidence (nullable), score (nullable), scorer, text_sha256, scored_at,
     unscorable_reason (nullable).
   - `latest_scores(client=None)`: returns `{record_hash: {"label", "score", "scorer"}}` over EVERY part under the
     table's gold prefix. The table is append-only, and a record_hash appears in it once. An absent table returns `{}`.
   - `score_missing(silver_rows, scored_hashes, invoke=None, limit=None)`: returns score rows for the silver articles
     whose `record_hash` is not in `scored_hashes`. An unscorable article gets label null and a reason, with 0 calls.
   - A CLI, `python -m lib.research.harvest.finbert_sentiment`, with two subcommands:
     - `score --as-of YYYY-MM-DD [--limit N] [--dry-run]` reads every source's silver-latest articles
       (`store.silver_latest`), scores the missing ones, and writes ONE new part through `publication_gold.write_gold`
       (the address comes from `store.address_of`, which is rule-30 builder output) with `SENTIMENT_SCHEMA`.
       `--dry-run` writes nothing and calls nothing; it prints what it would score.
     - `census` prints scored / unscorable / unscored / total over the newest gold mention snapshot, with its
       denominator.
   - Do NOT run `score` without `--dry-run`. The corpus scoring is the issuer's act.
2. **`publication_gold.build_mention(securities, as_of_date, client=None, sentiment_by_hash=None)`:**
   - `None` means `finbert_sentiment.latest_scores(client)`; a dict is used as given.
   - Append 3 nullable fields to `GOLD_MENTION_SCHEMA`: `sentiment_finbert_label` (string), `sentiment_finbert_score`
     (float64) and `sentiment_scorer` (string). They are joined by the row's `record_hash`, and are null when it is
     unscored.
   - Nothing else in the row, the tiering, `build_daily` or `build_event` changes.
3. **Plants** in `lib/research/harvest/test_ak1_finbert_sentiment.py`, with no network and a stub invoker:
   - (i) the signed-score rule for each label;
   - (ii) a second `score_missing` over unchanged record_hashes makes 0 calls, and a changed record_hash is scored;
   - (iii) an article with no title and no blocks gives label null and a reason, with 0 calls;
   - (iv) `build_mention` with a planted map: planted rows carry the tone and other rows carry nulls. Every
     pre-existing field is byte-identical to the builder's output before this change; a mutant that alters a tier
     fails;
   - (v) the `article_text` shapes.
4. The research suites stay green: `python -m pytest lib/research/harvest -q`. Report the counts before and after.

Worktree: `C:/Users/Opal Bloomberg/Desktop/wk-hvst-r36-90`, branch `wk-AMGT_HARVST-90-r38a`, cut from CLOUD at the issuance
commit (sparse cone, which includes `lib`, `infra/logic/registry` and `org/missions`). Read the batch processor's source
at `C:/Users/Opal Bloomberg/Desktop/ajb_workspace/infra/aws/lambda/finbert_batch_processor/lambda_function.py`; it is
outside your cone. Do not touch any `.runtime` directory.

<paths>
lib/research/harvest/finbert_sentiment.py
lib/research/harvest/publication_gold.py
lib/research/harvest/test_ak1_finbert_sentiment.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~90/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 2. PROOF OF SPEC (each invocation LITERAL; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-ak-1"><invocation>python -m pytest lib/research/harvest/test_ak1_finbert_sentiment.py -rA --tb=line</invocation><expect>passed</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-ak-1"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round38/checks/ak-1.AC2.py</invocation><expect>AC2 RESULT: PASS</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-ak-1"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round38/checks/ak-1.AC3.py</invocation><expect>AC3 RESULT: PASS</expect></criterion>
</proof_of_spec>

- AC2 calls the real Lambda on 3 fixed texts and writes nothing.
- AC3 runs the real builder over 5 securities against live silver through a capturing client, so nothing is sent.
- Run both from your worktree. If one cannot reach AWS there, mark it "issuer re-runs at the base after merge".
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~90/AMGT_HARVST.TO-HVST-ak-1.finbert-tone-in-gold-mention.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-ak-1.finbert-tone-in-gold-mention`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** Round-37 analysis @29fbb123e0, enrichment item 1. CTO fold ruling 6: reuse
`opal-news-ai-sentiment`, Opal infra, not a vendor.

The analysis named an IAM-lane invoke-grant cell. It is NOT cut: the identity that runs the gold build already invokes
(DryRun 204 at 19:4xZ). A ZERO with its cause named. A future scheduled gold producer's role would need the grant; that
is carried in decomposition section 51.

Served gold moves only at the issuer acts after the merge:
- the one-time corpus scoring (`score`, live);
- a gold rebuild, under a NEW never-widen pair.

**COMPLETE 2026-10-02 ~20:3xZ (issuer grade; the worker flipped `<status>`, which is outside its `<paths>`):**
- Merged @23b1e6851d.
- At the base:
  - AC1: 12 passed (worker).
  - AC2: PASS, 3 fixed sentences live (`round38/ak-1.AC2.issuer_grade.txt`). The labels are positive 0.946,
    negative -0.968 and neutral 0.0.
  - AC3: PASS (`ak-1.AC3.issuer_grade.txt`). Planted rows wrong 0; unplanted rows carrying a tone 0; PUTS SENT 0.
- The live Lambda contract, measured: request `{"text"}`; response statusCode 200 with a body of `sentiment`,
  `confidence`, `scores{3}` and `processing_time_ms`. An 11,880-character text returns 200.
- The worker made 6 live calls, all fixed sentences. 0 publisher text was sent.
- Dry runs:
  - `score`: 11,245 silver articles, 11,234 to score, 11 unscorable.
  - `census`: 9,930 distinct record_hashes over the 23,691-row snapshot, 0 scored.

<risk>SERVED</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<round>38</round>
<slot>~90</slot>
<fabric>site-z</fabric>
