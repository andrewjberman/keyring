# NFRA_OPLGTW task order -- `OG-nf-1` -- `news_for_security` searches the company NAME as well as the ticker text, and a zero answer says why (H2, row Z-S414): `app/news_typed.py` and one test file (round 47; round-46 analysis item 8)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-nf-1</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-nf-1</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~172</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a code and test change; no deploy, no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change; the name lookup reads objects the harvest tools already read.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the CTO's round-46 analysis (`org/missions/D9/NFRA/NFRA_OPLGTW/ledger/ROUND_ANALYSIS.round46.md` @ad17495429), rank 8: "Y2, Y1/R1/T1 plus H2 (`news_for_security`), as one cell of small fixes"; H2 is its own order because it is the one repair that is behaviour, not a one-line change.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-nf-1` (decomposition addendum R3-T.124, round 47, workstream ENRICH-R47-A)

WHY (row Z-S414, the CRO's audit). `news_for_security(ticker="NVDA", window_days=7)` answered `0 mentions, fallback_rows 0, fallback_absent_reason null`, while `news_search_articles` found 35 "Nvidia" articles in the same days in the same store. Two causes: the primary index (`amgt/harvest/gold/article_security_mention/`, newest partition 2026-10-08) is stale, and the fallback searches the TICKER text ("NVDA"), which news prose rarely prints (it says "Nvidia"). The answer's only hint is `precision`, which says "a TEXT match of the ticker". A reader sees a zero for a heavily covered name with no reason.

READ FIRST (under `infra/aws/ec2/opal-gateway/`): `app/news_typed.py` `news_for_security` (about lines 576-637), `_search_core` (about 293), `_freshness`, `_serve`, and the constants `PRECISION`, `WINDOW_CAP_DAYS`, `LIMIT_MAX`; `app/harvest_identity.py` `harvest_resolve_security` (about line 374, the identity lookup the `harvest_resolve_security` tool uses: it resolves a ticker or key to the security's identity and display name); `tests/test_og_nw1.py` (how the existing news tests fake the index read and the search).

DO, in `app/news_typed.py` ONLY (plus the new test file):

1. **A name resolver, `_security_name(ticker_or_key) -> Optional[str]`** (new module function, imports `app.harvest_identity` lazily INSIDE the function). It returns the company name for the ticker (or the ticker part of a `security_key`) by calling the identity lookup, taking the display name only when the lookup answers ONE exact match for that ticker; for no match, several candidates, a refusal, or ANY exception it returns `None` (never raises, never calls the network). It makes no write.
2. **The fallback searches both terms.** In `news_for_security`, the fallback loop that today calls `_search_core(table, d0, d1, text_term, None, None, LIMIT_MAX)` once for the ticker text now runs it once for the ticker text and, when `_security_name(...)` returns a name that differs (case-insensitively) from the ticker text, once more for the name, in that order. Merge the results, listing a row once when both terms found it (compare the whole row dict). Every fallback row keeps its `match: "text"` key and gains `match_term`: the term that found it (the ticker text when both did). The body gains `fallback_terms` (the list of terms searched, ticker first) and `fallback_name_absent_reason` (a short string when no name was resolved, else `None`).
3. **A zero answer says why.** The body gains `mention_index_lag_days`: the calendar days between today (`_today()`) and the newest partition's date (the `date=` part of the key), or `None` when the key carries none. When there is no mention row AND no fallback row, `absent_reason` names the newest partition date and every term searched, for example `no mention row in the window (the mention index's newest partition is 2026-10-08, 8 days before today) and no text match for NVDA | Nvidia`. When a row is found, `absent_reason` stays `None`, as now. The `PRECISION` sentence is updated in one clause so it says the fallback matches the ticker text AND the company name.
4. **Nothing else changes:** the index read, the mention matching, the window clamp, the freshness block, the envelope and the 50 KB projection are as they are. The tool wrapper in `app/tools.py` is NOT edited.
5. **The new test file `tests/test_og_nf1.py`** with at least these tests (names fixed): `test_ognf1_name_term_found`, `test_ognf1_row_listed_once`, `test_ognf1_zero_reason_names_partition_and_terms`, `test_ognf1_name_unresolved`, `test_ognf1_resolver_never_raises`, `test_ognf1_index_mention_still_served`. Fakes only: replace the index read, `_security_name`, `_table`, `_search_core` and `_today` as `tests/test_og_nw1.py` does.

## 2. BOUNDS

- Write only `app/news_typed.py`, `tests/test_og_nf1.py`, `W/` and, if a row is needed, the channel. NO other product file, no other test, no release, no deploy, no Terraform, no AWS or network call.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; print an account number, email address or client value.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/news_typed.py
infra/aws/ec2/opal-gateway/tests/test_og_nf1.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~172/` (the tree convention grants it). Rows: id `NFRA_OPLGTW-Z-W172-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-nf-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r47/checks/nf1.AC1.sh; echo "exit=$?"</invocation><expect>(?s)name search found 2 rows although the ticker text found none: ok.*fallback_terms is the ticker then the name: ok.*rows found: no absent_reason: ok.*a row found by both terms is listed once: ok.*zero answer: absent_reason names the partition date and every term: ok.*zero answer: mention_index_lag_days is 8, fallback empty: ok.*name unresolved: terms are the ticker only, the reason is stated: ok.*control: an index mention is still served, absent_reason None: ok.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-nf-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r47/checks/nf1.AC2.sh; echo "exit=$?"</invocation><expect>(?s)new file tests/test_og_nf1.py: [1-9]\d* passed, 0 failed.*neighbours \(\d+\): [1-9]\d* passed, failed names \[\].*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the fallback's two terms, the dedupe, the zero reason and the unresolved-name case, probed with fakes. `AC2`: your test file and the three existing news test files.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-nf-1.round-47-news-for-security-searches-the-name-and-says-why-it-found-none.proof_of_spec.json`. Validate it after your last commit with `python3 -I .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>` (`python3`, not `python`: ruling msg 35901). Flip the ONE `<status>` tag to `complete` only if both PASS, and report once.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 47, workstream ENRICH-R47-A, `<risk>WORLD</risk>` is the gateway-path floor. Source: the CTO's round-46 analysis (msg 36165) rank 8 (H2, Z-S414). The stale index itself (Z-S415, the AMGT harvest producer on dell1) is not this cell's: this cell makes the zero honest and the fallback useful.
- READINGS DISCLOSED TO THE CTO: (1) the name comes from the gateway's own identity lookup, so a name it cannot resolve leaves the old ticker-only fallback, with the reason stated. (2) The fallback now makes up to twice the article reads (one per term), within the existing per-day caps. (3) `match_term`, `fallback_terms`, `fallback_name_absent_reason` and `mention_index_lag_days` are the issuer's field names.
- Pre-cut: `AC1` base FAIL as expected (only the index-mention control holds), `AC2` base FAIL as expected (no test file). The three neighbour files pass at the base (14 tests with `test_og_gt8`, which carries one red at the live ref and is left out).

<status>complete</status>
<round>47</round>
<workstream>ENRICH-R47-A</workstream>
<slot>~172</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
