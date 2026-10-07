# ETFS_RIVALS task order -- `RIV-ab-1` -- ROUND 14 (ENRICHMENT): AN AI ACCOUNT IS WRITTEN AGAINST THE BUILD THE PAGE SERVES, AND ITS BADGE SAYS SO WHEN IT IS NOT

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-ab-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~1</issued_to>
<issued_by>2.0.0_SA_COO~RV</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule, cron or trigger is added or moved by this cell (the sweep's own step order changes inside one invocation)
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell (the daily role already runs produce_a1 inside the publish step)
comp-adversary: DECLARED-NOT-APPLICABLE the validator-context composer profiles RETURNED work for the L8/L9 packet; at the cut nothing is returned, and the issuer's evidence context is this order's check files
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric site-z) -- *rivalfunds*: a daily research page on rival active ETFs (13 funds, two peer groups): rankings, buying trend, AI accounts per fund, and since round 12-13 a separate audit page; published to S3 by the package `data/etfs/scripts/rivalfunds/` (five AWS stage Lambdas; the 09:00 ET sweep runs the AI step and republishes) and served signed-in by the opal-gateway. **Round 14**: an AI account must agree with the panels beside it or say on its badge that it does not; the audit page gets its own size rule. Nothing here deploys, merges or calls a vendor (stub every OpenAI and Bloomberg hook). Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-ab-1` -- an AI account is written against the build the page serves, and its badge says so when it is not (row Z-S54; round-13 analysis ADDENDUM 1; Andrew: "not needed do a and c")
- Measured on the served 2026-10-06 page (2.0.0_SA_COO~RV): 22 of 26 accounts carry a figure that differs from the panel beside it;
  149 of 197 cited contribution figures moved (IDVZ direction verdict: "Petrobras ... +0.47%" against the rankings' +0.93%), each
  under a green "Grounded". The AI step ran at 13:00:20Z against the 11:03Z tables; `sweep.run_ai_step` (sweep.py ~589) runs
  `ai_stage.run_for_day` FIRST and only the republish after it (publish_page.produce_a1's stale rebuild) rebuilt
  holding_contribution and buying_trend, at 13:05-13:06Z. The only disclosure is a small "Written against earlier tables" line.
- Interface:
  - (A) `sweep.run_ai_step` calls `publish_page.produce_a1(<sink object>, <sink spec>, <date>)` BEFORE `ai_stage.run_for_day` and
    returns its result under `a1_refresh`; a refresh that raises is recorded and the AI step still runs; nothing is refreshed
    when the AI step does not apply. Each account already records the revision of every row it cites (`cited_rows[].revision`).
  - (C) the PASS badge is `<span class="rf-grounding-PASS" data-grade="PASS" data-build="served">Grounded</span>` when every
    revision the account's cited rows carry for a vintage table (holding_contribution, buying_trend) is a revision the page
    serves for that table, else `... data-build="earlier">Grounded on an earlier build</span>` -- the same element, place and
    weight. `render.grounding_census(html) -> {"served": n, "earlier": m}`; `publish_page` writes it into the manifest as
    `ai_grounding`. A FAIL badge is unchanged. NO account is re-run after a rebuild (Andrew: B is not needed).
- **Organic trigger:** the 09:00 ET sweep's AI step and its republish.

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD 330067f27b)

- The check files' docstrings are the exact interface they read: read `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round14/checks/ab-1.AC1.py`, `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round14/checks/ab-1.AC2.py` and `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round14/checks/_common.py` before you build.
- (A) `sweep.run_ai_step(ev, context, runners, markers=None)` (sweep.py ~589-621): today `ai_stage.run_for_day(sink, date, run_path=..., deadline_s=dl)` runs, then the publish-page runner republishes. `publish_page.produce_a1(s, sink_spec, day, refresh=False)` (publish_page.py ~322) rebuilds a table only when it is stale (`a1_stale`: a G1 or G4 input newer than its newest object) and SKIPS otherwise; call it through the module attribute (`publish_page.produce_a1`) so a test can stub it. Mind the deadline: the refresh spends time inside the same Lambda invocation -- compute the AI deadline AFTER the refresh, and state in your report what the refresh does to the time budget.
- (C) the PASS badge is written in `render` ~1536 (`rf-grounding-PASS`); `_written_revisions(rows)` and `_vintage_line(ctx, rows)` (~1465-1495) already compute, per table, the revisions an account's cited rows carry and the revisions the page serves (`_a1(ctx)[table]` rows' `revision`). Decide the badge per ACCOUNT from its own cited rows. Keep the existing "Written against earlier tables" line.
- The audit page (`render_audit_page`) carries the citations; the badge lives on the main page's AI card and inside its dialog -- both read the same.
- `publish_page` already writes `fund_sections` and `holding_dialogs` into the manifest (rounds 12-13): add `ai_grounding` the same way. No FAIL line for it (an earlier build is a state to show, not a publish failure).
- You run ab-1 FIRST; RIV-as-1 follows on the same branch.

## 3. SURFACES AND BOUNDS

You READ (never edit): `lib/`, `integrations/bloomberg/` (Andrew-direct no-modify order), every file not in your `<paths>`, the round-8..14 check folders under `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/`, the decomposition, and `org/missions/D5/ETFS/ETFS_RIVALS/ledger/ROUND_ANALYSIS.round13.md`.

You WRITE only the `<paths>` below (plus `deliverables/0.9.0_WK_ETFS_RIVALS~1/`). NEVER: any S3 read or write, any deploy, any OpenAI or Bloomberg call (stub every vendor hook), any environment gate flip outside a test, any file under `integrations/` or `infra/`. New tests as `data/etfs/scripts/rivalfunds/tests/test_r14ab1_*.py`; run the whole package suite (`python -m pytest rivalfunds/tests -q` from `data/etfs/scripts/`) before you report: 0 failed. A check you cannot satisfy without leaving your `<paths>` is a surprise row in the investigation file (`surfaced_at` = `date -u +%FT%TZ` at filing), never an edit outside them.

<paths>
data/etfs/scripts/rivalfunds/sweep.py
data/etfs/scripts/rivalfunds/render.py
data/etfs/scripts/rivalfunds/publish_page.py
data/etfs/scripts/rivalfunds/tests/
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- an account citing an older revision reads "Grounded on an earlier build"; one citing the served revision reads "Grounded"; the census counts both; control: both keep a PASS badge and their text (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round14/checks/ab-1.AC1.py`)
- **AC2** -- the table refresh runs before the AI step, then the republish; a failing refresh is recorded and the AI step still runs; control: gate off runs nothing (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round14/checks/ab-1.AC2.py`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-ab-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round14/checks/ab-1.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="AC2" cell_refs="RIV-ab-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round14/checks/ab-1.AC2.py</invocation><expect>AC2 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="J1" cell_refs="RIV-ab-1" judgment="true"/>
</proof_of_spec>

J1 (graded by 3.0.0_SA_CVO~RV at L9 on a real day's run, never self-graded): 26 of 26 accounts cite the served revision and a sample of cited figures equals the panel's (Petrobras in IDVZ among them); a late rebuild turns that fund's badge to "Grounded on an earlier build".

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~1/ETFS_RIVALS.TO-RIV-ab-1.ai-account-on-the-served-build-and-an-honest-badge.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-ab-1.ai-account-on-the-served-build-and-an-honest-badge`. Report once: each mechanical criterion's verdict line with the output above it; each judgment criterion left UNVERIFIABLE-BY-INSTRUMENT for the CVO; files written; every existing test assertion changed and why; the suite's final line; rows filed (id + one line); the hookups you need the issuer to add at the merge. Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** ROUND_ANALYSIS.round13.md @594d1be8f8; decomposition v1.4 (round 14 appended). Chain `~1`, slot `~1`, position 1 of 2. Checks dry-run at base: ab-1.AC1 FAIL (2; control (c) PASS) as expected; ab-1.AC2 FAIL (2; control (c) PASS) as expected. Andrew-direct @3e040ecbf2: B (a re-run) is NOT cut.

<risk>SERVED</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>14</round>
<slot>~1</slot>
<fabric>site-z</fabric>
<status>complete</status>
