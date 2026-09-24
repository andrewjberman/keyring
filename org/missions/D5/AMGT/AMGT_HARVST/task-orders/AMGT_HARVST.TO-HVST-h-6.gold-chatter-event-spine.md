# AMGT_HARVST task order -- `HVST-h-6` -- H6: gold `chatter_event`, the company's news events as clustered runs of UTC days, each with its lead headline and its articles, by the working rule (tier A+B >= 2 from >= 2 publishers, gaps <= 1 day); rebuildable from silver

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-h-6</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~6</issued_to>
<issued_by>2.0.0_SA_COO~Y</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- 0 armed gates on any harvest surface (C1=23 C2=7 C3=12 C4=21 C5=334); a gold snapshot at a new prefix is not a deploy.
comp-iam: RUN at L5 on the DESIRED plane only; the S3 write under amgt/harvest/gold/ is measured by AC4's own conditional PUT.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification, not a produced artifact.
</preflight>

**You are `0.9.0_WK_AMGT_HARVST~6`.** Work ONLY in the worktree whose absolute path is in your spawn prompt.
- **Your first act** prints `git rev-parse --abbrev-ref HEAD` and `git rev-parse --show-toplevel`, and tests that `org/`,
  `.tools/`, every EXISTING path in section 3, and `lib/research/harvest/tests/test_publication_gold_daily.py` exist.
  - That last file is the predecessor's. If it is absent, STOP with a BLOCKING row.
- Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_HARVST~6;`.
- **NEVER RUN AN INSTALL. NEVER CALL A PUBLISHER.** AWS is allowed only as S3 reads of `opal-data-harvest`, and
  conditional writes under `amgt/harvest/gold/`.

## 1. THE CELL, inlined in full -- `HVST-h-6` (manifest row H6, outcome FWD-6)

**The contract, verbatim** (PRD v0.2 @9102ccfe81, `C-HV-EVENT-SPINE`):
- The gold `chatter_event` table (`s3://opal-data-harvest/amgt/harvest/gold/chatter_event/date=2026-09-22`, builder
  output) holds clustered runs of UTC days for one security.
- The working rule: tier A+B articles >= 2, from >= 2 publishers, merged across gaps of <= 1 day.
- Each event carries its lead headline and its articles.

**Also binding:** `C-HV-GOLD-REBUILDABLE` (a rebuild from the same silver gives identical rows), `C-HV-ABSOLUTE-ONLY`,
and `C-HV-KEY` (`security_key`, and `composite_figi` where held).

**Outcome FWD-6, DONE WHEN:** *"the timeline for the validation security shows at least the event runs the stored
articles support, each with its lead headline, and opening one lists its articles"*. This cell builds the table; the
timeline shows it after `HVST-h-8`'s spec is approved.

**THE STATE you start from** (read at your branch HEAD):
- `lib/research/harvest/publication_gold.py` holds `mention_rows` and `write_gold` (by `HVST-h-4`) and `daily_rows` (by
  `HVST-h-5`).
- The newest `article_security_mention` snapshot is under `amgt/harvest/gold/article_security_mention/`. Read the newest
  `date=` and its newest part.
- The securities list is `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~4/securities.json`.

**RULED -- what you build** (extending `publication_gold.py`, never changing `HVST-h-4`'s or `HVST-h-5`'s behaviour):
1. **`event_rows(mention_rows, min_articles=2, min_publishers=2, max_gap_days=1)`** is PURE and works per security:
   - (a) A QUALIFYING day is a UTC day, by `published_utc`, carrying tier A or B mention rows whose count is at least
     `min_articles` and whose distinct publishers number at least `min_publishers`.
   - (b) Consecutive qualifying days whose gap (the non-qualifying days between them) is at most `max_gap_days` merge
     into ONE event.
   - Each event row carries:
     - `event_id` = sha256 of `security_key` + first day + last day;
     - `security_key`, and `composite_figi` where held;
     - `first_day` and `last_day`;
     - `days_span`, `articles_total`, `tier_a` and `tier_b`;
     - `publishers_distinct`;
     - `lead_article_key` and `lead_headline`. The lead is the highest tier, then the earliest `published_utc`, then the
       lowest `article_key`, so it is deterministic.
     - `article_keys`: every tier A or B article in the event's days, ordered by tier and then `published_utc`.
   - The thresholds are working defaults at the top of the module, named so.
2. **A CLI `build-event --securities-json FILE --as-of YYYY-MM-DD`** writes a `chatter_event` snapshot through
   `write_gold` and prints `{"securities", "events", "events_per_security", "key"}`.
3. **New test file `lib/research/harvest/tests/test_publication_gold_event.py`.** Exactly eight arms:
   - `test_single_publisher_burst_is_not_an_event`
   - `test_two_publishers_two_articles_is_an_event`
   - `test_gap_of_one_day_merges`
   - `test_gap_of_two_days_splits`
   - `test_tier_c_and_d_do_not_qualify`
   - `test_lead_headline_is_deterministic`
   - `test_event_lists_its_articles`
   - `test_rebuild_identical`

**What this cell does NOT change:**
- the mention and daily functions and snapshots;
- silver;
- `store.py`;
- the chatter axis;
- any served object.

## 2. WHERE THIS CAME FROM
Round 1, decomposition v1.0 @9fbf337a74, chain A position 8 of 9. After `HVST-h-5`.

## 3. SURFACES -- what you may read and write

<paths>
lib/research/harvest/publication_gold.py
lib/research/harvest/tests/test_publication_gold_event.py
lib/research/harvest/tests/test_publication_gold_mention.py
lib/research/harvest/tests/test_publication_gold_daily.py
lib/research/harvest/store.py
lib/research/identity/crosswalk.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~4/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~6/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_HARVST/task-orders/AMGT_HARVST.TO-HVST-h-6.gold-chatter-event-spine.md
</paths>

- **Only `publication_gold.py` and your new test file may change.** AC3 fails otherwise.
- Scratch goes in `<your worktree>/.scratch/hv6/`.
- **Committing:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_HARVST~6 <0.9.0_WK_AMGT_HARVST~6@opal.agent>" -F <msgfile> -- <paths>`.

## 4. BOUNDS
- **The code and tests come first**; the live build after.
- **Pure ASCII.** A refused PUT is a BLOCKING row.
- **Zero events for a security is a RESULT,** reported with the qualifying-day count that produced it.
- **Surprise rows:** `AMGT_HARVST-Z-W6-S<k>`, with `disarm_owner` `2.0.0_SA_COO~Y`.

## 5. PROOF OF SPEC (each invocation LITERAL; timeout 600)

Write `.scratch/hv6/check.py`. It reads the snapshot key AC4 printed, recomputes `event_rows` from the newest mention
snapshot, and prints:
- `events_written <w> events_rederived <r> symmetric_difference <d>`;
- `events_violating_rule <v>` (any event with fewer than 2 tier A or B articles or fewer than 2 publishers);
- `events_without_headline <h>`.

<proof_of_spec>
  <criterion id="AC0" cell_refs="HVST-h-6"><invocation>cd "$(git rev-parse --show-toplevel)" && for t in test_publication_gold_mention test_publication_gold_daily; do echo "$t :: $(python -m pytest lib/research/harvest/tests/$t.py -q --color=no -p no:cacheprovider 2>&1 | tail -1)"; done</invocation><expect>BEFORE any edit: "12 passed" and "10 passed" (the predecessors' bars)</expect></criterion>
  <criterion id="AC1" cell_refs="HVST-h-6"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/research/harvest/tests/test_publication_gold_event.py -v --color=no -p no:cacheprovider 2>&1 | tail -12</invocation><expect>"8 passed" and no "failed" -- the eight arms named in section 1 item 3</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-h-6"><invocation>cd "$(git rev-parse --show-toplevel)" && for t in test_publication_gold_mention test_publication_gold_daily; do echo "$t :: $(python -m pytest lib/research/harvest/tests/$t.py -q --color=no -p no:cacheprovider 2>&1 | tail -1)"; done</invocation><expect>equal to AC0: "12 passed" and "10 passed"</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-h-6"><invocation>cd "$(git rev-parse --show-toplevel)" && git diff --name-only "$(git merge-base HEAD SITEZ)" HEAD -- lib && git status --porcelain -- lib && echo "--- end"</invocation><expect>before "--- end", ONLY lib/research/harvest/publication_gold.py and lib/research/harvest/tests/test_publication_gold_event.py, and nothing else under lib</expect></criterion>
  <criterion id="AC4" cell_refs="HVST-h-6"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m lib.research.harvest.publication_gold build-event --securities-json org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~4/securities.json --as-of "$(date -u +%Y-%m-%d)"</invocation><expect>a JSON line with events_per_security naming every security in the list (zero allowed) and a key beginning "amgt/harvest/gold/chatter_event/date="</expect></criterion>
  <criterion id="AC5" cell_refs="HVST-h-6"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/hv6/check.py</invocation><expect>"symmetric_difference 0", "events_violating_rule 0" and "events_without_headline 0"</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR.** No judgment criterion.

## 6. WHEN YOU ARE DONE
1. Write the instance to
   `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~6/AMGT_HARVST.TO-HVST-h-6.gold-chatter-event-spine.proof_of_spec.json`.
2. Grade it with `python .tools/proof-of-spec-check.py <instance> AC0,AC1,AC2,AC3,AC4,AC5`, which must return rc 0.
3. Flip only on all PASS.
4. Commit with `--only`.
5. Report once, with Lenovo's events (days and lead headline).

**MUTATION DISCIPLINE:** snapshot the working-tree bytes to `.scratch/hv6/` first. Never `git checkout --`, `stash` or
`git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6):**
1. **The contract's "gap <= 1 day" is read as at most one non-qualifying day between qualifying days.** That is the
   reading under which "merged across gaps" means anything; the reading is stated so the CTO can amend it.
2. **The lead tie-break is fixed,** so a rebuild cannot change a headline.

<status>complete</status>
<round>1</round>
<slot>~6</slot>
<fabric>site-z</fabric>
