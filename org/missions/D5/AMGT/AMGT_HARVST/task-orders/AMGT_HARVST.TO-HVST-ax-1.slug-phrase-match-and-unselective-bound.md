# AMGT_HARVST task order -- `HVST-ax-1` -- ROUND 51 (round-49 analysis ADDENDUM 2; CTO @a246fcd07f; rows Z-S90, Z-S91): A SITEMAP CANDIDATE MATCHES THE COMPANY'S WORDS AS WORDS, AND AN UNSELECTIVE JOB ENDS

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-ax-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~101</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched.
comp-iam: RUN at L5 -- LOCAL code, plants, and an OFFLINE replay over files already on disk. NO publisher host is contacted (wsj is signed out and stopped; bbg and sa legs are live), no collector or backfill_driver is run, no S3 call. `.runtime` is READ ONLY and only at the two paths named in section 0; never write there and never open a browser profile.
comp-adversary: RUN at L5 -- the adversary is a matcher that still passes a substring (`sse` inside `assets`), a matcher that drops a real hit (`boeings-...` for Boeing, `at-t-...` for AT&T), a bound that fires on a job that would have accepted, a bound that stops the LEG instead of ending the JOB, or a replay that fetches.
</preflight>

## 0. THE CELL

The wsj and bbg legs list candidates from monthly sitemaps (`lib/opal_data_harvest/discovery.py`). `discover()` yields a
sitemap item when `_matches(url, query)` is true, and `query` is `slug_query(security["company"])` (the company name with
legal suffixes dropped; `lib/opal_data_harvest/publishers.py:258`). Today (`discovery.py:65-67`):

```python
def _matches(url, query):
    slug = url.rsplit("/", 1)[-1].lower()
    return all(word in slug for word in re.findall(r"[a-z0-9]+", (query or "").lower()))
```

`word in slug` is a SUBSTRING test. Measured (rows AMGT_HARVST-Z-S90, Z-S91):
- **T US Equity** (company AT&T -> words `at`, `t`): one wsj job fetched 502 articles in 3 h 03 min, accepted 0; 431 were
  rejected `company_not_mentioned`. Fetched slugs include `oil-little-changed-as-traders-weigh-...`,
  `kkr-strikes-deal-to-buy-private-capital-...`.
- **SSE LN** (word `sse`): two jobs fetched 482 and 280, accepted 0. Fetched slugs include
  `teresa-margolles-dissects-tragedy-...`, `ithaca-energy-to-buy-offshore-canada-oil-assets-...`,
  `ai-token-spending-businesses-...`.
- Across 260 finished wsj jobs: 127 fetched 0, 92 fetched 1-10, 24 fetched 11-25, 17 fetched more than 25. Of the 68 jobs
  with at least one accepted article, the largest fetched 116.

Read-only inputs on disk (absolute; they are NOT in your worktree):
- run records: `C:/Users/Opal Bloomberg/Desktop/ajb_workspace/.runtime/opal-data-harvest-wsj/runs/*.json` (per job: `ticker`,
  `status`, `fetched_keys`, `accepted`, `rejected`, `fetch_outcomes`);
- stored wsj sitemaps: `C:/Users/Opal Bloomberg/Desktop/ajb_workspace/.runtime/opal-data-harvest-wsj/harvest_listing/*.xml`
  (18 files, 16 MB).

## 1. THE BUILD (LOCAL)

1. **The matcher** (`discovery.py`, `_matches`). Split the slug on `-` into tokens, and join the query's words into one
   string `q` (`at t` -> `att`, `eli lilly` -> `elililly`, `mcdonald s` -> `mcdonalds`). The slug matches when some run of
   CONSECUTIVE whole slug tokens, joined, equals `q` or `q` + `s` (`at`+`t`; `boeings` for `boeing`; `mcdonalds` for the
   words `mcdonald`, `s`). A run never starts or ends inside a token, so `sse` does not match `assets`. An empty query
   matches nothing. A trailing hash token (the last token of a wsj slug, e.g. `40b9`, `6785f907`) is an ordinary token and
   needs no special case. Name `HVST-ax-1` in a comment.
2. **The bound.** A wsj job that has FETCHED K articles and accepted none ends there with status
   `candidate_set_unselective`.
   - K is contract data: `contracts.json`, wsj, `"unselective_after": <K>`. A publisher without the key has no bound (bbg,
     barrons, sa, ft are unchanged).
   - Derive K with a script, `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~101/ax-1.k_derivation.py`,
     over the run records named above: for every finished wsj job with at least one accepted article, the number of
     articles fetched BEFORE its first accepted one if the record's order gives it, else its total fetched. K = that
     maximum, rounded UP to the next multiple of 10. Print the denominator (jobs read, jobs with an accept, which of the two
     measures was used) and K; write the output beside it as `ax-1.k_derivation.out`.
   - Enforce it where acceptance is decided (`lib/opal_data_harvest/worker.py`, the job loop that sets
     `no_acceptable_new_articles` near line 661): the job stops consuming candidates, and its run record carries
     `status: candidate_set_unselective` and the count fetched.
   - `lib/opal_data_harvest/backfill_driver.py`: `candidate_set_unselective` is NOT a stop status. The pair is recorded
     done in the checkpoint with that status and the leg goes on to the next name.
3. **Plants** in `lib/opal_data_harvest/test_ax1_slug_phrase_and_bound.py` (no network):
   - (i) matcher refusals: query `sse` against `teresa-margolles-dissects-tragedy-at-moma-ps1-airdigital-1a2`,
     `ithaca-energy-to-buy-offshore-canada-oil-assets-from-suncor-x1` and `ai-token-spending-businesses-431ee94a`; query
     `at t` against `oil-little-changed-as-traders-weigh-mideast-crude-export-data-6785f907`;
   - (ii) matcher hits: `sse` against `sse-raises-profit-guidance-ab12`; `at t` against
     `at-t-to-buy-spectrum-licenses-9f3c` and `why-at-ts-fiber-bet-matters-11aa`; `boeing` against
     `boeings-new-chief-faces-a-test-77de`; `mcdonald s` against `mcdonalds-sales-rise-on-value-meals-5e2a`; `eli lilly` against `how-eli-lilly-won-the-weight-loss-race-0c1d`, and NOT
     against `eli-manning-and-lilly-pulitzer-22bb`;
   - (iii) the mutant: the old substring rule makes (i) fail;
   - (iv) the bound: a planted wsj job whose candidates are all rejected ends `candidate_set_unselective` after exactly K
     fetches (set K small through a planted contract), and a planted job that accepts one before K runs to the end;
   - (v) the driver: a `candidate_set_unselective` result is recorded done with that status and the next pair runs.
4. **Existing tests** that pin the substring rule or the driver's status sets may be updated, and only for that reason; list
   each file and assertion you changed in your report.
5. **The offline replay** `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~101/ax-1.replay.py`. It parses
   the stored wsj sitemap XML files (no request) and, per name, counts the URLs the OLD rule and the NEW rule admit:
   - `T US Equity` (query `AT T`) and `SSE LN` (query `SSE`): print `<name>: old <n> new <m>`;
   - three CONTROL names: the three finished wsj jobs with the most accepted articles in the run records. For each, print
     `<name>: accepted <a>, still admitted <b>` where `b` counts the job's accepted article URLs that the NEW rule admits
     (read the URL from each accepted entry, or from the matching fetched key);
   - print `REPLAY OK` only if both `new` counts are at or below K AND every control has `b == a`. Otherwise print
     `REPLAY FAIL` and the failing line.
   - Write its output beside it as `ax-1.replay.out`.
   - If a control loses an accepted URL, do NOT loosen the matcher to make it pass: record the URL and the slug, file a
     surprise row, and report.
6. The harvest suite stays green: `python -m pytest lib/opal_data_harvest -q -p no:cacheprovider`. Report the count.

Worktree: given in your spawn prompt (cut from CLOUD at the issuance commit).

<paths>
lib/opal_data_harvest/discovery.py
lib/opal_data_harvest/worker.py
lib/opal_data_harvest/backfill_driver.py
lib/opal_data_harvest/contracts.json
lib/opal_data_harvest/test_ax1_slug_phrase_and_bound.py
lib/opal_data_harvest/test_af4_discovery_hookup.py
lib/opal_data_harvest/test_af4_sitemap_listing.py
lib/opal_data_harvest/test_ae4_backfill_driver.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~101/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 2. PROOF OF SPEC (each invocation LITERAL; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-ax-1"><invocation>python -m pytest lib/opal_data_harvest/test_ax1_slug_phrase_and_bound.py -rA --tb=line -p no:cacheprovider</invocation><expect>passed</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-ax-1"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~101/ax-1.replay.out</invocation><expect>REPLAY OK</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-ax-1"><invocation>python -m pytest lib/opal_data_harvest -q -p no:cacheprovider</invocation><expect>passed</expect></criterion>
</proof_of_spec>

- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~101/AMGT_HARVST.TO-HVST-ax-1.slug-phrase-match-and-unselective-bound.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-ax-1.slug-phrase-match-and-unselective-bound`. Pin every artifact row to the commit that
  carries it.
- Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Round-49 analysis ADDENDUM 2 @a246fcd07f; decomposition section 64; rows AMGT_HARVST-Z-S90 @2b959b20e9, Z-S91 @27de0728f6.
- **Where the cut departs from ADDENDUM 2 item (1), and why:** the addendum has the wsj query switch from the symbol to the
  crosswalk company name for short or common-word symbols. Read at the cut, the wsj query is ALREADY the company name
  (`slug_query(security["company"])`, `publishers.py:700,762`); the symbol is never queried. The measured defect is the
  matcher's substring test (`discovery.py:67`), so the cell fixes the matcher for every name, which serves the same outcome
  (items 2 and 3 are cut as written; the replay is offline because wsj is signed out). No gate limb graded this departure;
  it is stated here and in the issuance commit for the CTO's round-51 read.
- `_matches` is shared with the bbg sitemap leg, which is live: its next job after the merge lists on the new rule.
- The close run is the issuer's: after Andrew's wsj sign-in, the leg resumes from `r46_wsj_checkpoint.json`
  (`--clear-stop wsj`) and the T US Equity pair re-runs under the new rule.

**COMPLETE 2026-10-07 ~00:5xZ (issuer):**
- **Built:** worker ~101 @d19b06f397 + @5dcce98469; merged @a02b56aaa5 (12 files, dropped 0, foreign 0).
- **AC1 PASS:** 21 of 21. **AC2 PASS:** REPLAY OK over 18 stored wsj sitemap files (26,907 unique URLs): T US Equity old 8,758
  new 11; SSE LN old 501 new 0; controls Netflix 65/65, Visa 25/25, BP 23/23. **AC3 PASS:** 693 passed on the branch; issuer
  re-run on merged CLOUD 695 passed, 1 skipped.
- **K = 100** (`contracts.json` wsj `unselective_after`): 260 run records read, 68 with an accept (55 by fetch order, 13 by
  total fetched); the maximum was 93 (AAPL US Equity).
- **Existing tests changed:** none.
- **Rows:** AMGT_HARVST-Z-W101-S1 (OBSERVATION, INERT): the run record carries no company or query, so the replay read each
  control's query from `progress.sqlite3` `harvest_listing_outbox`; K counted the 1-based position of the first accept.
- **Close run:** OWED. It needs Andrew's sign-in in the wsj profile; then the leg resumes from `r46_wsj_checkpoint.json`
  (`--clear-stop wsj`) and the T US Equity pair re-runs under the new rule. bbg's next job lists on the new matcher.

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>issued</status>
<status>complete</status>
<round>51</round>
<slot>~101</slot>
<fabric>site-z</fabric>
