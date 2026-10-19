# NFRA_OPLGTW task order -- `OG-en-33` -- the both-orders check keeps the forward pytest text, and its first-run flake is reproduced cold and named (round 44; row `Z-S399`; round-43 analysis item 4)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-en-33</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-en-33</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~159</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a check script; no deploy, no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change; no AWS call is needed.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the CTO's round-43 analysis, item 4 (keep the forward text, reproduce it cold, name the cause, fix the check).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-en-33` (decomposition addendum R3-T.121, round 44, workstream ENRICH-R44-A)

WHY. The shared check `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/_bothorders.sh` runs a list of gateway test files in the given order and in the reverse order and passes only when both orders pass the same count. Row `Z-S399`: on the FIRST run after a change to the tree (a checkout or a merge) its forward order has read `passed 0; failed 0` (RESULT FAIL), or a partial count (68 of 71, 69 of 71), and every later run reads `71 of 71`; the applier saw it in 3 of 8 runs and the issuer in 1 of 4. The script discards the forward output (`run()` keeps only `tail -1` and the caller never saves the rest), so the failing text is not on record. Read the script first (about 25 lines).

DO, IN THIS ORDER:
1. REPAIR THE SCRIPT (this is the point; many orders use it). Keep every existing behaviour and output line. Add:
   - env `BOTHORDERS_PYTEST` (default `python -m pytest -q -p no:cacheprovider`): the runner, called as `( cd "$GW" && timeout 280 $BOTHORDERS_PYTEST <files> )` (unquoted on purpose so a multi-word runner works);
   - env `BOTHORDERS_OUT` (default a fresh `mktemp -d`): the FULL runner output (stdout and stderr, colour codes stripped) of each order is written to `<BOTHORDERS_OUT>/<label>.forward.txt` and `<label>.reverse.txt` (the existing `tail -1` parse reads the same text);
   - when an order's last line carries no `N passed`, print `<label> <order>: NO PASS LINE; saved <path>` (order = `forward` or `reverse`; path = the saved file) followed by the last 15 lines of that file, and the verdict is FAIL. The existing lines `<label> forward: passed N; failed F` and `<label> reverse: passed M; failed G` and `RESULT: PASS`/`RESULT: FAIL` stay exactly as they are.
   Test it against its own control: `bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r44/checks/en33.AC1.sh` (read it: it builds two stub runners, one that prints a traceback for the forward order, one that prints `3 passed`, and checks both arms).
2. REPRODUCE THE FLAKE COLD. The load is the issuer's 18-file window set (the same files, in this order):
   `tests/test_og_en13.py tests/test_og_en15.py tests/test_og_en17.py tests/test_og_en18.py tests/test_og_en19.py tests/test_og_en20.py tests/test_og_en21.py tests/test_og_en22.py tests/test_og_en23.py tests/test_og_en24.py tests/test_og_cl2.py tests/test_og_rv2.py tests/test_og_db3.py tests/test_og_en9.py tests/test_og_sv2.py tests/test_og_pr1.py tests/test_og_pr5.py tests/test_og_sec2.py`
   Run `bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/_bothorders.sh cold<n> <that list>` EIGHT times (at least), each time after making the tree COLD: alternate between (a) removing every `__pycache__` folder under `infra/aws/ec2/opal-gateway/` and (b) touching every file in that folder (`touch`, no content change) and (c) both. Each run takes about 35 seconds; run them one per command (the 120-second limit applies to each command), with `BOTHORDERS_OUT` set to a scratch folder OUTSIDE the repository so the forward text of every run is kept.
3. NAME THE CAUSE. Write `W/BOTHORDERS_COLD.json` (exact shape in the header of `r44/checks/en33.AC2.sh`; read it first): one `runs` row per run with `how_cold`, the last three lines of the forward and reverse text, and the two counts; then `cause`. If ANY run read a forward count that differs from the reverse count (zero, or partial), `cause` names what the saved text shows (a collection error, an import error on a missing `.pyc`, a timeout, a test that reads a file mid-write, a plugin warning, a port in use) and `cause_evidence` QUOTES that run's `forward_tail`. If NO run differed in at least 8 cold runs, `cause` starts with `NOT_REPRODUCED` and says how many runs and what you varied; the repaired script stays (it now keeps the text the next time it happens).
4. If the cause is a defect in the script itself (for example the parse of the last line when a warning follows the summary, or `timeout 280` cutting the run), fix THAT in the script too, under the same control.

## 2. BOUNDS

- Write only `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/_bothorders.sh`, `W/BOTHORDERS_COLD.json`, your scratch folder (outside the repository) and, if a row is needed, the channel. NO gateway file (`app/`, `tests/`), no other check, no release, no deploy. Touching files for the cold runs changes their modification time only; commit none of them.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; print a secret, an email address or a client value.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/_bothorders.sh
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~159/` (the tree convention grants it). Rows: id `NFRA_OPLGTW-Z-W159-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`; a row's `disposition` is one of `UNDER_INVESTIGATION`, `GRADUATED`, `DISMISSED_WITH_REASON` (the last needs a `dismissal_reason`), `DECOMP_INVALIDATING`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-en-33"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r44/checks/en33.AC1.sh; echo "exit=$?"</invocation><expect>(?s)arm A \(forward prints a traceback\): NO PASS LINE reported 1 \(want 1\); the saved forward text holds the traceback 1 \(want 1\); RESULT: FAIL printed 1 \(want 1\); exit 1 \(want 1\).*arm B \(both orders print 3 passed\): forward line 1 \(want 1\), reverse line 1 \(want 1\), RESULT: PASS printed 1 \(want 1\); exit 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-en-33"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r44/checks/en33.AC2.sh; echo "exit=$?"</invocation><expect>(?s)cold runs recorded \d+ \(want >= 8\), each with its forward and reverse text and counts: ok; runs where forward differs from reverse: \d+.*consistent with the runs; email-shaped strings 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the repaired script keeps and reports the forward text (control with two stub runners, both arms). `AC2`: at least eight cold runs are recorded with their text, and the named cause agrees with them.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-en-33.round-44-the-both-orders-check-keeps-its-forward-text.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if both PASS, and report once (commit hash, the AC lines, how many cold runs and how many differed, the cause in one sentence).

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 44, workstream ENRICH-R44-A. Source: the CTO's round-43 analysis (`ledger/ROUND_ANALYSIS.round43.md` @d35c913755, msg 35841), list item 4: "keep the forward pytest text in a file when its tail has no `passed`; reproduce it cold, name the cause, and fix the check; the check is shared by many orders, so the fix is the point."
- The issuer's own control runs after the drain read forward 0 once, then 71 of 71 six times; the issuer's runs of the same script (3 more) were all 71. The cause is unproven.
- Two mechanical criteria. `AC1` base FAIL as expected (the unrepaired script has no stub support: arm A reports no `NO PASS LINE`). `AC2` base FAIL as expected (record absent); a synthetic record of 8 identical runs with `NOT_REPRODUCED` passes it and a record with one differing run but a `NOT_REPRODUCED` cause fails it.
- Risk `LOCAL`: the one product-adjacent file is the issuer's own check script.

<status>complete</status>
<round>44</round>
<workstream>ENRICH-R44-A</workstream>
<slot>~159</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
