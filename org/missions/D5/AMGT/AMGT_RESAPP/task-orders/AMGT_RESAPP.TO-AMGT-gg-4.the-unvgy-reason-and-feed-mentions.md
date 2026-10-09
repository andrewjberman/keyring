# AMGT_RESAPP task order -- `AMGT-gg-4` -- TWO SERVED FIXES IN ONE MODULE: UNVGY'S NO-FORECAST REASON NAMES THE MISSING PERIOD-END DATES; EACH FEED ITEM CARRIES ITS MENTIONS

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-gg-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~326</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; one module and one test.
comp-iam: DECLARED-NOT-APPLICABLE -- both fields read what the function already reads; no grant.
comp-adversary: RUN at the cut (round82_prep/GROUP_API_NOTES.md) -- live: UNVGY_US_Equity's forecast reason is the false 'raw stamp ... carries no bestdata.json (pulled before C-MODEL-FORECASTS)'; AMD/BA/NVDA feed items carry no mentions while the gold rows carry mention_count (463 of 463 for AMD). Both checks FAIL at the base.
EGRESS CLASS, declared: NONE.
</preflight>

**Your worktree:** the spawn names it (branch `wk-AMGT_RESAPP-326`, cut from the issuance commit). Work and commit only there. Start every shell call with `cd` into that path: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-gg-4` (round 82, decomposition s.90)

Two fixes, both in `lib/research/api/scoped_amgt.py` (so one cell). Read
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round82_prep/GROUP_API_NOTES.md` items 3 and 4b whole first.

1. **UNVGY's no-forecast reason** (`read_model`, ~:5174-5187): when every unresolved forecast entry is per-period ("no
   BEST_PERIOD_END_DATE for this period"), serve ONE sentence built from those entries that names the missing period-end dates,
   instead of falling through to the 'pulled before C-MODEL-FORECASTS' text. If the per-period reasons differ, name each distinct
   one once. The fall-through stays for the case it was written for (no forecast file at all).
2. **Feed mentions** (`read_feed`, ~:5355-5421, served on `/overlay`): carry each item's `mentions` from the gold row's
   `mention_count` (the field `top_band.py:115` already serves), and name the ordering basis that is actually measured. No item is
   dropped or re-ordered by this change.
3. New test `lib/research/api/tests/test_r82_reason_and_mentions.py`: both fixes on plants, plus a name whose reason and feed are
   unchanged.

Run `lib/research/api/tests/` before your commit and report its last line.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W326-S<k>` (dell1's registered coordinate is D1), `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no schedule, no SEC, vendor, model or Bloomberg call.
2. No `bun`, `npm` or `pip install` of any kind. Nothing is fetched from the internet.
3. Standing: no S3 delete, no push of shared branches.
4. You edit `scoped_amgt.py` at `read_model`'s reason and `read_feed` only, and add the one test file.

## 3. SURFACES

<paths>
lib/research/api/scoped_amgt.py
lib/research/api/tests/test_r82_reason_and_mentions.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~326/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-gg-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round82_prep/checks/r82_unvgy.py" --crit AC1 --where local; echo "exit=$?"</invocation><expect>UNVGY_US_Equity's served forecast reason names the period-end-date absence and no longer carries 'pulled before C-MODEL-FORECASTS'; R82 UNVGY AC1 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-gg-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round82_prep/checks/r82_feed.py" --crit AC1 --where local; echo "exit=$?"</invocation><expect>every feed item served for the named names carries mentions from its gold row and the ordering basis is named; R82 FEED AC1 SERVED: YES; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~326 <0.9.0_WK_AMGT_RESAPP~326@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~326/AMGT_RESAPP.TO-AMGT-gg-4.the-unvgy-reason-and-feed-mentions.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the test folder's last line (api folder on this box: 2 failed at the base, both `No module named 'pypdf'` -- name them, file no row);
- anything your read of the code found that this order did not say;
- any row.
- the hookup the redeploy must carry, or that none is needed.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO~DELL1 round-81 analysis enrichment items 3 and 4b (msgs 1772, 1880). The round's only writer of scoped_amgt.py besides the issuer's one timeline wiring line at gg-5's merge. Checks dry-run at the base: AC1 (r82_unvgy) base FAIL as expected; AC2 (r82_feed) base FAIL as expected. Served only through AMGT-gg-7.

<status>pending</status>
<round>82</round>
<slot>0.9.0_WK_AMGT_RESAPP~326</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>complete -- drained @df9568bf85 (build 7ed6e1de21, proof 4aa0085247 VALID rc=0; mutant control restores the false text). Re-run by the issuer on the branch: R82 UNVGY AC1 SERVED: YES ("no forecast figure is served: no BEST_PERIOD_END_DATE for this period (FY1, FY2, FY3)"), R82 FEED AC1 SERVED: YES (AMD 22 of 22, BA 75 of 75 items with integer mentions; basis named; order unchanged, newest first). ISSUER RULING on the worker's finding: mentions is None (not 0) where the gold row stores no count, and the ABSENT basis text stays for a feed with no counts. api folder 2 failed (pypdf absent on dell1), 880 passed. Served only through AMGT-gg-7.</status>
