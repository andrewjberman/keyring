# AMGT_HARVST task order -- `HVST-ak-2` -- ROUND 38 CHAIN B CELL 1 (FWD-17, PRD v0.15): PER-NAME ROLLING 30 / 90 / 365-DAY TONE, VOTERS AND COUNTS, ENDING AT T-1

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-ak-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~92</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched.
comp-iam: RUN at L5 -- LOCAL code and plants. No S3 write: the served window table is first written at the issuer's rebuild under its own never-widen pair. AC2 reads the SERVED gold mention snapshot read-only.
comp-adversary: RUN at L5 -- the adversary is a neutral label counted as a voter, a confidence threshold added (none is permitted), an all-neutral name reading tone 0.0 instead of null, a window ending today instead of at T-1, or a 365-day window that silently serves less than it says.
</preflight>

## 0. THE CELL

FWD-17 (PRD v0.15) says each covered name's tone and article count are in gold for rolling 30, 90 and 365-day windows,
and that FinBERT not being sure is not a vote. Its DONE WHEN is per name per window ending at the last trading day
(T-1, `lib/trading_calendar.py`), and gold carries three figures:
- `articles_total`;
- `voters`: articles whose FinBERT label is not neutral, with NO confidence threshold;
- a tone aggregate over the voters only.
Where the store is shorter than the window, the served window start is stored. No history before 2026-01-01 is pulled.
A name whose articles are all neutral reads voters 0 and tone null, never 0.0.

The tone per article comes from a sibling cell's score store, which merges separately. Code against this interface
only:
- `lib.research.harvest.finbert_sentiment.latest_scores(client=None)` returns
  `{record_hash: {"label": "positive"|"negative"|"neutral", "score": float, "scorer": str}}`;
- the score is signed: +confidence, -confidence, or 0.0 for neutral;
- a missing hash means unscored.
Import it lazily, inside the CLI path only. Your tests and AC2 inject the map.

The gold mention rows (`lib/research/harvest/publication_gold.py`) carry `security_key`, `article_key`, `published_utc`
(a timezone-aware datetime) and `record_hash`. The served snapshot reader is
`publication_gold._latest_gold_snapshot_rows(table, client=None)`; the writer is
`publication_gold.write_gold(table, rows, as_of_date, run_stamp, schema=..., client=None)`. The writer's address is
rule-30 builder output.

## 1. THE BUILD (LOCAL)

1. **New `lib/research/harvest/window_tone.py`:**
   - `WINDOWS = (30, 90, 365)`, `STORE_START = date(2026, 1, 1)`, `TABLE = "chatter_window"`.
   - `GOLD_WINDOW_SCHEMA` fields:
     - security_key;
     - window_days (int32);
     - window_end, window_start_requested and window_start_served (date32);
     - articles_total, scored and voters (int64);
     - tone (float64, nullable);
     - as_of (date32);
     - scorer (string, nullable).
   - `build_window_rows(mention_rows, sentiment_by_hash, window_end)` builds one row per window for each security
     present in `mention_rows`:
     - `window_start_requested` = window_end minus (N - 1) days;
     - `window_start_served` = max(requested, STORE_START);
     - the population is the DISTINCT `article_key` values of that security whose UTC publication day is in
       [window_start_served, window_end];
     - `articles_total` = the population size;
     - `scored` = articles with a label;
     - `voters` = labels other than neutral;
     - `tone` = the mean signed score over the voters, or None when there are 0 voters.
   - `build_window(securities, as_of_date, client=None, sentiment_by_hash=None)`:
     - window_end = `trading_calendar.prev_trading_day(as_of_date)`;
     - it reads the served mention snapshot;
     - `None` means `finbert_sentiment.latest_scores`, imported lazily;
     - it writes ONE snapshot part with `GOLD_WINDOW_SCHEMA` and returns a summary dict.
   - A CLI, `python -m lib.research.harvest.window_tone build --securities-json PATH --as-of YYYY-MM-DD [--dry-run]`.
     `--dry-run` writes nothing. Do NOT run it without `--dry-run`: the first served write is the issuer's.
2. **Plants** in `lib/research/harvest/test_ak2_window_tone.py`, with no network:
   - (i) an all-neutral name gives voters 0 and tone None in every window;
   - (ii) a 365-day window has `window_start_served` = 2026-01-01 and requested earlier;
   - (iii) as_of on a Monday gives window_end on the prior Friday, and as_of after a holiday skips it;
   - (iv) an article published on window_end is in, and one on the day after is out;
   - (v) an unscored article counts in articles_total but not in scored;
   - (vi) two mention rows with one article_key count once;
   - (vii) the tone is the mean over voters only: neutrals do not dilute it.
3. Do not edit `publication_gold.py`. The research suites stay green: `python -m pytest lib/research/harvest -q`.
   Report the counts before and after.

Worktree: `C:/Users/Opal Bloomberg/Desktop/wk-hvst-r38-92`, branch `wk-AMGT_HARVST-92-r38b`, cut from CLOUD at the issuance
commit (sparse cone per decomposition section 50). Do not touch any `.runtime` directory.

<paths>
lib/research/harvest/window_tone.py
lib/research/harvest/test_ak2_window_tone.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~92/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 2. PROOF OF SPEC (each invocation LITERAL; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-ak-2"><invocation>python -m pytest lib/research/harvest/test_ak2_window_tone.py -rA --tb=line</invocation><expect>passed</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-ak-2"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round38/checks/ak-2.AC2.py</invocation><expect>AC2 RESULT: PASS</expect></criterion>
</proof_of_spec>

- AC2 reads the served gold mention snapshot read-only, plants a tone per record_hash, and recomputes every window row
  independently.
- Run it from your worktree. If it cannot reach AWS there, mark it "issuer re-runs at the base after merge".
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~92/AMGT_HARVST.TO-HVST-ak-2.window-tone-30-90-365.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-ak-2.window-tone-30-90-365`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** Round-37 analysis @29fbb123e0, enrichment item 2. PRD v0.15 rules: a voter is a non-neutral label
with no added threshold, and windows end at T-1. CTO fold ruling 7: a STATED START, with no back-collection.

Build ladder: the analysis points at `chatter_daily`'s trailing sums. They count MENTIONS per day, while voters and
tone need per-ARTICLE labels. Keeping all three counts on one population (distinct articles from the mention rows)
holds SAME GRAIN (taxonomy law ii). `articles_total` is reconciled against the `chatter_daily` window sum at the
issuer's real run.

The first served write is at the issuer's rebuild #6, after ak-1's corpus scoring.

**COMPLETE 2026-10-02 ~20:1xZ (issuer):**
- AC1 PASS: 9 passed. A mutant that counts neutrals as voters fails plants (i) and (vii).
- Merged @f175fbeb99.
- AC2 re-run at the base PASSES (`deliverables/2.0.0_SA_COO_H/round38/ak-2.AC2.issuer_grade.txt`): 715 mention rows over
  5 securities, window_end 2026-10-01, 15 of 15 rows equal the independent recompute. The all-neutral `2317_TT_Equity`
  reads voters 0 and tone None at 30d (3 articles), 90d (10) and 365d (37).
- The research suite at the base reads 294 passed and 3 failed. All 3 failures are in
  `tests/test_timeline_day_read_path.py`, which pins the silver read path that RESAPP am-1 removed by design
  (@59c2ef1b23); row Z-S68. None was caused by this cell.
- The CLI was not run: `finbert_sentiment` lands with ak-1.

<risk>SERVED</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<round>38</round>
<slot>~92</slot>
<fabric>site-z</fabric>
