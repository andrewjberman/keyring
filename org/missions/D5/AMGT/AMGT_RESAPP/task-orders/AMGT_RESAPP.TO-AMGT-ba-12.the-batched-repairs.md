# AMGT_RESAPP task order -- `AMGT-ba-12` -- THE BATCHED REPAIRS: WATCHLIST TESTS SOCKET-BLOCKED, ONE CLEAN COLLECTION, MULTI-PAGE SEARCH REFUSED, AND A READ OF TEN LEGACY ROWS

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ba-12</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~278</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; tests, one refusal line and one read.
comp-iam: DECLARED-NOT-APPLICABLE -- item 4 is a READ of the metrics table with the device's own read access; no write, no grant.
comp-adversary: RUN by the issuer at the cut -- r77_ba12 at the base: AC1 FAIL (3 of 5 watchlist tests run with block_all_sockets); AC2 FAIL (the union collection has failures in management/tests/test_ceo_search.py); AC3 FAIL (max_pages=2 reaches the store before any refusal), with its control PASS (max_pages=1 is not refused).
EGRESS CLASS, declared: NONE. No vendor call: item 3 adds a refusal and calls nothing.
</preflight>

**Your worktree:** `C:/tmp/r77-278` (branch `wk-AMGT_RESAPP-278`, cut from the issuance commit). Work and commit only there. Start every shell call with `cd /c/tmp/r77-278`: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-ba-12` (round 77, decomposition s.85)

Four small repairs the issuer ruled into one cell (`deliverables/2.0.0_SA_COO~Z/round76/COO_ADJUDICATION_REMEDIATION_ROWS_ROUND76.md`
@fb9ca91ad5, section A). Each is independent; finish all four.

1. **Rows Z-C-S35 and Z-W7-S7: every watchlist test runs socket-blocked.** `lib/research/watchlist/tests/test_watchlist.py`
   defines the `block_all_sockets` fixture (line 81) and asks for it on 3 of its 5 tests. Add ONE
   `lib/research/watchlist/tests/conftest.py` that applies it to every test in the directory (move the fixture there and make it
   autouse, or keep it where it is and add an autouse fixture that requests it). All 5 tests still pass.

2. **Row Z-S343: one pytest collection.** Collecting `lib/research/harvest/test_am1_marker_once.py` or
   `lib/research/harvest/test_al2_content_key.py` in the same run as `lib/research/management/tests` fails 10 tests of
   `management/tests/test_ceo_search.py` (TestClassifySerpAttempt, TestSerpBrightdataRecords). Each passes alone. Both harvest
   files import `lib.research.harvest.finbert_sentiment` at module scope; that is the common factor, and the mechanism is not
   traced. Trace it, then fix it IN THE TESTS (an import that leaks state, a patched module left in `sys.modules`, a shared
   global): the two harvest test files and, if the leak is on that side, `test_ceo_search.py`. Do not change
   `finbert_sentiment.py` or any other production module; if the cause can only be fixed there, file a BLOCKING row for this
   item with the mechanism and finish the other three.

3. **Rows Z-W88-S1 and Z-C-S372: a multi-page web search is REFUSED.** `lib/research/harvest/bright_data_serp.py harvest_serp`
   (line 81) accepts `max_pages` above 1, and its own comment (about lines 127-131) says every row is then attributed to the LAST
   page's stored key. Web search is not collected today, so nothing is wrong yet. Add the refusal as the function's FIRST act:
   `max_pages` other than 1 raises `ValueError` whose message names `max_pages` and says why in one plain sentence, BEFORE the
   store is read and before the vendor primitive is called. Add a plant case to the module's existing tests (find them; if there
   are none, add `lib/research/harvest/test_ba12_serp_single_page.py`). No vendor call is made by this cell.

4. **Row Z-W19-S16: a READ-ONLY measure, then the row closes on evidence.** On 2026-09-15 at about 18:55Z an out-of-order run of
   the old chatter producer upserted the 10 existing rows of the bare partition `TRENDING_CHATTER#2026-09-15` in the DynamoDB
   table `opal-harvest-security-metrics`; their before-values were not captured. Read the row
   (`AMGT_RESAPP-Z-W19-S16` in the investigation file) first. Then measure, with READS ONLY:
   - how many items that partition holds today, and their keys;
   - whether any served route still reads that bare partition (`lib/research/api/scoped_amgt.py` reads rankings through a
     generation pointer; say what it reads for the chatter axis, with the line);
   - whether the same day's names also exist in a generation partition (duplicated), or the bare partition is the only copy
     (shadowed or orphaned).
   Write `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~278/LEGACY_ROWS_Z-W19-S16.md`: the count, the keys,
   the three answers, and ONE recommended disposition (leave as a record; or a named remedy for the issuer to carry). **No
   delete, no put, no update, by any path.**

**Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W278-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write of any kind, no table, no schedule, no vendor, SEC or model call, no portal write.
2. Production behaviour changes in ONE place: the `max_pages` refusal. Everything else is tests and a record.
3. Standing: no S3 delete, no DynamoDB delete, no push of shared branches.

## 3. SURFACES

<paths>
lib/research/watchlist/tests/
lib/research/harvest/test_am1_marker_once.py
lib/research/harvest/test_al2_content_key.py
lib/research/harvest/test_ba12_serp_single_page.py
lib/research/harvest/tests/
lib/research/harvest/bright_data_serp.py
lib/research/management/tests/test_ceo_search.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~278/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 2400)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ba-12"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round77/checks/r77_ba12.py" --crit AC1 --where local; echo "exit=$?"</invocation><expect>5 of 5 watchlist tests run with block_all_sockets; C1 PASS; R77 BA12 AC1 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ba-12"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round77/checks/r77_ba12.py" --crit AC2 --where local; echo "exit=$?"</invocation><expect>one collection of the management tests beside the two harvest test files: 0 failed, 0 errors; C1 PASS; R77 BA12 AC2 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-ba-12"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round77/checks/r77_ba12.py" --crit AC3 --where local; echo "exit=$?"</invocation><expect>max_pages=2 raises ValueError naming max_pages before the store and before the vendor primitive; the control max_pages=1 is not refused; C1-C2 PASS; R77 BA12 AC3 SERVED: YES; and exit=0</expect></criterion>
</proof_of_spec>

Item 4 has no mechanical criterion: its proof is the record file, which the issuer reads at the drain.

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~278 <0.9.0_WK_AMGT_RESAPP~278@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~278/AMGT_RESAPP.TO-AMGT-ba-12.the-batched-repairs.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- item 2's mechanism in two sentences;
- item 4's count, keys, three answers and recommended disposition;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO round-76 analysis item 10 (the COO's own repair cell); COO adjudication @fb9ca91ad5 section A. The cell's two adapter rows (Z-S278, Z-S218) are in AMGT-ba-11, the one writer of `scoped_amgt.py`. Item 4 corrects the adjudication's wording: the ten rows are CHATTER-axis rows (`TRENDING_CHATTER#2026-09-15`), not price rows, per the row's own text. Checks dry-run at the base: ba-12 AC1 base FAIL as expected (3 of 5), AC2 base FAIL as expected, AC3 base FAIL as expected with its control PASS.

<status>pending</status>
<round>77</round>
<slot>0.9.0_WK_AMGT_RESAPP~278</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<status>complete -- drained @751aef6acb; proof VALID (worktree checker); watchlist tests socket-blocked 5 of 5; one pytest collection 153 passed 0 errors; multi-page serp refused; Z-W19-S16 read: 10 chatter rows duplicated in the generation partition and read by no route (inert; the row closes on this evidence)</status>
