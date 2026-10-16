# NFRA_OPLGTW task order -- `OG-en-6` -- harvest chatter states its lag in trading days (round 38 E6; CVO v30 enrichment)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-en-6</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-en-6</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~120</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- gateway code and offline tests; no deploy, no schedule. The release is a later applier order.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change; reads only what `harvest_get_chatter` already reads.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the CTO's round-37 analysis (`ledger/ROUND_ANALYSIS.round37.md` @afa8003488, E6: "harvest chatter states its lag in trading days (enrichment)").
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-en-6` (decomposition addendum R3-T.93, round 38 item E6, workstream ENRICH-R38, FWD-22)

THE GAP. `harvest_get_chatter(security_key, from_day, to_day)` in `app/harvest_press.py` answers chatter rows for a window but does not say how many TRADING days behind T-1 its newest chatter is, which the project's rule requires of every freshness claim (calendar days mislead on a Monday). The other harvest answers already carry it: `app/harvest_identity.py` has `_behind(last_modified, t1, cal)` (it returns `(trading_days_behind_t1, absent_reason)`) and a `t1` frontier from `lib/trading_calendar.py`; `app/news_typed.py` has `_freshness(kind, newest)`.

THE FIX (code only). In `app/harvest_press.py`, make the chatter answer carry, in its body: `trading_days_behind_t1` (int, the newest returned chatter day measured against T-1 by `lib/trading_calendar.py`), `newest_chatter_day` (ISO date), and `lag_absent_reason` (null, or one sentence when no row carries a date or the calendar cannot place it; then `trading_days_behind_t1` is null). Reuse the existing helper pattern (import or mirror `harvest_identity._behind` and the `t1` computation; do NOT write a new calendar and do NOT use calendar-day arithmetic). An empty chatter window carries `trading_days_behind_t1: null` and `lag_absent_reason`. Change no other tool and no admission.

TESTS (new file `tests/test_og_en6.py`; read the nearest existing chatter test, `tests/test_og_hv1.py` or `tests/test_og_gt4.py`, for the fixture style):
- `test_ogen6_ac01`: chatter whose newest day is the previous trading day answers `trading_days_behind_t1` 0 and names `newest_chatter_day`.
- `test_ogen6_ac02`: the Monday case: with today a Monday and the newest chatter on the Friday, the lag is 0 (Friday IS Monday's T-1); with newest chatter on the Thursday it is 1. Patch the module's `_today`-style clock the way the existing tests do.
- `test_ogen6_ac03`: an empty window and a calendar that cannot be imported each give `trading_days_behind_t1: null` with a `lag_absent_reason`, and no exception.
If an existing test pins the exact key set of a chatter answer, update it to the new truth with the smallest edit and name it; never weaken it.

## 2. BOUNDS

- Write only the files in `<paths>`. No release, no deploy, no IAM, no registry change.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; weaken a test; print a person's name or a secret.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/harvest_press.py
infra/aws/ec2/opal-gateway/tests/test_og_en6.py
infra/aws/ec2/opal-gateway/tests/test_og_hv1.py
infra/aws/ec2/opal-gateway/tests/test_og_gt4.py
infra/aws/ec2/opal-gateway/tests/test_og_gt5.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

You WRITE `app/harvest_press.py`, `tests/test_og_en6.py` and, only to follow the new truth, the existing chatter tests listed; the rest you only READ. `W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~120/`. Rows: id `NFRA_OPLGTW-Z-W120-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`; a row's `disposition` is one of `UNDER_INVESTIGATION`, `GRADUATED`, `DISMISSED_WITH_REASON` (the last needs a `dismissal_reason`), `DECOMP_INVALIDATING`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-en-6"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/_named.sh tests/test_og_en6.py test_ogen6_ac01 test_ogen6_ac02 test_ogen6_ac03; echo "exit=$?"</invocation><expect>(?s)pytest rc=0; named tests passed 3 of 3; failed/error lines 0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-en-6"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/_wkbound.sh 0.9.0_WK_NFRA_OPLGTW~120 '^infra/aws/ec2/opal-gateway/(app/harvest_press\.py|tests/test_og_(en6|hv1|gt4|gt5)\.py)$'; echo "exit=$?"</invocation><expect>(?s)write-set bound for 0\.9\.0_WK_NFRA_OPLGTW~120: files touched [1-9]\d*; product files [1-9]\d*; outside the allowed set 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the three named tests pass. `AC2`: the commits of this serial touch only `harvest_press.py` and the chatter tests.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-en-6.chatter-lag-in-trading-days.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if both PASS, and report once (commit hashes, the two AC lines, each existing test you had to update and why).

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 38 (CTO round-37 analysis, E6), workstream ENRICH-R38 (decomposition addendum R3-T.93). Risk WORLD by the L6 floor (a gateway infrastructure path), no deploy in this cell; rides the next batched gateway release with E4, E5 and E8.
- Pre-cut: AC1 base FAIL as expected (the test file is absent); AC2 base FAIL as expected (no commit of this serial yet).

<status>complete</status>
<round>38</round>
<workstream>ENRICH-R38</workstream>
<slot>~120</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
