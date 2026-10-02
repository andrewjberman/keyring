# AMGT_HARVST task order -- `HVST-ak-3` -- ROUND 38 CHAIN C CELL 1 (FWD-6 density enrichment, HARVST brief O5): DO COVERAGE EVENTS MARK THE SPIKES? A READ-ONLY CENSUS

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-ak-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~91</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched.
comp-iam: RUN at L5 -- READ-ONLY: served gold and silver are read, and nothing is written to S3. The census JSON goes to your deliverables folder only.
comp-adversary: RUN at L5 -- the adversary is a census that reads a stale local copy instead of the served store, a dry build that writes, or a spike definition chosen after looking so that coverage reads well.
</preflight>

## 0. THE CELL

FWD-6 says the company's news events show up as spans on the timeline: bursts of real coverage appear as marked events
with a headline, not just as spikes in a count. The UI/UX brief (O5) found the store holds 8 events estate-wide.
Measured at the cut: the served `chatter_event` snapshot has 8 rows, while the served mention snapshot has 23,691 rows.
The served events were built on 09-30, before gold rebuilds #4 and #5 grew the mention table from 9,521 rows.

This cell measures; it changes no rule. A rule change, or a served event rebuild, is decided on your numbers.

`lib/research/harvest/publication_gold.py` provides:
- `build_event(securities, as_of_date, client=None)` (around line 1505): it reads the newest mention snapshot,
  enriches each row with its article's headline (`_headline_by_article_key`), and calls the PURE function
  `event_rows(enriched)`;
- `_latest_gold_snapshot_rows(table, client=None)` (around line 814), which reads the newest served snapshot;
- the table names `GOLD_TABLE` (mention), `chatter_daily`, and `GOLD_EVENT_TABLE` (`chatter_event`).

## 1. THE CENSUS (LOCAL, READ-ONLY)

Write ONE script, `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~91/ak3_event_density.py`. It
imports from the repo, edits no repo code, and does the following:
1. **Read the served snapshots:** mention, `chatter_daily` and `chatter_event`. Record the served event part's S3 key
   as `served_event_part`, found by the same newest-date, newest-part rule the reader uses. Record `mention_rows_read`.
2. **Dry-build the events:** enrich the mention rows exactly as `build_event` does, then call `event_rows(enriched)`
   in memory. Nothing is written; `puts_sent` = 0. `events_dry_built` is the row count; `events_served` is the
   served row count.
3. **Count spikes from the served `chatter_daily`:**
   - a day d is a spike for a security at threshold k (2 or 3) when `articles_total(d) >= 3` AND
     `articles_total(d) >= k x` the mean `articles_total` over the 30 calendar days before d;
   - a missing day counts 0;
   - report `spike_days` as `{"2x": n, "3x": n}`;
   - a spike is COVERED when d falls inside the span of an event for that security. Read the span fields from
     `GOLD_EVENT_SCHEMA`. Report `spike_days_covered` for the DRY-BUILT events, plus `spike_days_covered_served` for
     the served ones.
4. **Report** `securities` (with at least 1 mention row), plus up to 10 example uncovered spikes (security_key, day,
   count, baseline). If `event_rows`' own structure shows WHY a burst did not become an event (which rule or limb),
   report those reasons and counts, without editing `publication_gold.py`. If that cannot be measured without a code
   change, say so.
5. **Write** `ak3_event_density.json` in your deliverables folder, and print `DENSITY CENSUS: DONE` as the last line.

Worktree: `C:/Users/Opal Bloomberg/Desktop/wk-hvst-r38-91`, branch `wk-AMGT_HARVST-91-r38c`, cut from CLOUD at the issuance
commit (sparse cone per decomposition section 50). Do not touch any `.runtime` directory.

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~91/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 2. PROOF OF SPEC (each invocation LITERAL; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-ak-3"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~91/ak3_event_density.py</invocation><expect>DENSITY CENSUS: DONE</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-ak-3"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round38/checks/ak-3.AC2.py</invocation><expect>AC2 RESULT: PASS</expect></criterion>
</proof_of_spec>

- Both read the served store. Run them from your worktree. If one cannot reach AWS there, mark it "issuer re-runs at
  the base after merge".
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~91/AMGT_HARVST.TO-HVST-ak-3.event-density-census.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-ak-3.event-density-census`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** Round-37 analysis @29fbb123e0, enrichment item 3 (FWD-6 density, an enrichment and not a new outcome).

The spike definition is fixed at the cut, at two thresholds, before any number is seen. That way coverage cannot be
tuned after the fact.

If the dry-built events cover the spikes materially better than the 8 served events, the served event rebuild joins
rebuild #6 under its pair. If they do not, the next round cuts the rule change with the census's uncovered spikes as
its held-out set.

**COMPLETE 2026-10-02 ~20:2xZ (issuer):** AC1 PASS ("DENSITY CENSUS: DONE"). Merged @b79d3781bd. AC2 re-run at the base
PASSES (`deliverables/2.0.0_SA_COO_H/round38/ak-3.AC2.issuer_grade.txt`; served snapshot 8 rows, read by the check
itself). The census, read-only with puts_sent 0, covers 205 securities and 23,691 mention rows:
- events: served 8, dry-built on current gold 438;
- spike days: 634 at 2x and 564 at 3x;
- covered by the dry-built events: 315 at 2x (49.7%) and 281 at 3x;
- covered by the served events: 8 at 2x (1.3%) and 7 at 3x.
Uncovered at 2x is 319, measured from `event_rows`' own rules with no code change:
- fewer than 2 tier-A publishers that day: 133;
- fewer than 2 tier-A/B articles: 55;
- no tier-A/B mention: 54;
- all tier-A/B rows guarded as roundups: 52;
- thresholds met but no event (story split or headline link, approximated): 25.
**Decision per the rule fixed at the cut:** the dry-built events cover spikes materially better (49.7% against 1.3%),
so the served `chatter_event` rebuild joins rebuild #6 under its pair. The uncovered 319 are the held-out set for any
later rule change.

<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<status>complete</status>
<round>38</round>
<slot>~91</slot>
<fabric>site-z</fabric>
