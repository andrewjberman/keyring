# NFRA_OPLGTW task order -- `OG-en-5` -- a coverage floor beside an empty news answer (round 38 E5; ap-19 AC3 enrichment, CVO v30)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-en-5</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-en-5</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~119</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- gateway code and offline tests; no deploy, no schedule. The release is a later applier order.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change; reads only the news tables the tools already read.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the CTO's round-37 analysis (`ledger/ROUND_ANALYSIS.round37.md` @afa8003488, E5: "a coverage floor beside an empty news answer: 'no articles in window W, newest article at T'") on the CVO's v30 reading of the ap-19 answers.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-en-5` (decomposition addendum R3-T.93, round 38 item E5, workstream ENRICH-R38, FWD-22)

THE GAP. `news_search_articles` (and its siblings in `app/news_typed.py`) answer an empty window as `items_matched 0` plus `absent_reason "no article matched the window and filters"`. A reader cannot tell a quiet window from a store that stopped: the answer does not say how recent the newest article is. The CVO asked for a floor beside every empty answer.

THE FIX (code only). In `app/news_typed.py`, where a tool of that file returns an empty result (read `news_search_articles`, `_search_core`, `news_trending_topics`, `news_keyword_intelligence` and `_serve`; the helper `_newest_day(table, attr, index)` already finds a table's newest day, and `_freshness(kind, newest)` already measures a trading-day lag): add to the body of an EMPTY answer a key `coverage_floor` = `{"window": [<from ISO date>, <to ISO date>], "newest_article_at": "<the newest article's ISO date or timestamp in the table, or null when the table is empty>", "newest_article_trading_days_behind_t1": <int or null>, "message": "no articles in window <from>..<to>, newest article at <T>"}`. The message text is exactly that sentence form with the real dates (and `newest article at none` when the table has none). A NON-empty answer is unchanged (no `coverage_floor` key). Use the existing helpers; no new table read beyond the one `_newest_day` call per empty answer; if `_newest_day` fails, the floor carries `newest_article_at: null` and a `floor_absent_reason` and the answer still returns (never raise). Change no other tool and no admission.

TESTS (new file `tests/test_og_en5.py`; read `tests/test_og_nw1.py` or the nearest news test for the fake-table fixture style):
- `test_ogen5_ac01`: an empty window on `news_search_articles` carries `coverage_floor` with the window dates, a `newest_article_at` taken from the fake table's newest day, and the exact message sentence.
- `test_ogen5_ac02`: a non-empty answer has NO `coverage_floor` key and is otherwise byte-equal to the pre-change answer for the same inputs.
- `test_ogen5_ac03`: an empty window over an EMPTY table gives `newest_article_at: null` and the message ends `newest article at none`; a failing `_newest_day` gives `floor_absent_reason` and no exception.
If an existing test pins the exact key set of an empty answer, update it to the new truth with the smallest edit and name it in your report; never weaken it.

## 2. BOUNDS

- Write only the files in `<paths>`. No release, no deploy, no IAM, no registry change.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; weaken a test; print a person's name or a secret.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/news_typed.py
infra/aws/ec2/opal-gateway/tests/test_og_en5.py
infra/aws/ec2/opal-gateway/tests/test_og_nw1.py
infra/aws/ec2/opal-gateway/tests/test_og_nw2.py
infra/aws/ec2/opal-gateway/tests/test_og_nw3.py
infra/aws/ec2/opal-gateway/tests/test_og_gt8.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

You WRITE `app/news_typed.py`, `tests/test_og_en5.py` and, only to follow the new truth, the existing news tests listed; the rest you only READ. `W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~119/`. Rows: id `NFRA_OPLGTW-Z-W119-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`; a row's `disposition` is one of `UNDER_INVESTIGATION`, `GRADUATED`, `DISMISSED_WITH_REASON` (the last needs a `dismissal_reason`), `DECOMP_INVALIDATING`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-en-5"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/_named.sh tests/test_og_en5.py test_ogen5_ac01 test_ogen5_ac02 test_ogen5_ac03; echo "exit=$?"</invocation><expect>(?s)pytest rc=0; named tests passed 3 of 3; failed/error lines 0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-en-5"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/_wkbound.sh 0.9.0_WK_NFRA_OPLGTW~119 '^infra/aws/ec2/opal-gateway/(app/news_typed\.py|tests/test_og_(en5|nw[0-9]+|gt8)\.py)$'; echo "exit=$?"</invocation><expect>(?s)write-set bound for 0\.9\.0_WK_NFRA_OPLGTW~119: files touched [1-9]\d*; product files [1-9]\d*; outside the allowed set 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the three named tests pass. `AC2`: the commits of this serial touch only `news_typed.py` and the news tests.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-en-5.news-coverage-floor.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if both PASS, and report once (commit hashes, the two AC lines, each existing test you had to update and why).

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 38 (CTO round-37 analysis, E5), workstream ENRICH-R38 (decomposition addendum R3-T.93). Risk WORLD by the L6 floor (a gateway infrastructure path), no deploy in this cell; rides the next batched gateway release with E4, E6 and E8.
- Pre-cut: AC1 base FAIL as expected (the test file is absent); AC2 base FAIL as expected (no commit of this serial yet).

<status>staged</status>
<round>38</round>
<workstream>ENRICH-R38</workstream>
<slot>~119</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
