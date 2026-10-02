# ETFS_RIVALS task order -- `RIV-sa-1` -- ROUND 7 (ENRICHMENT): THE SWEEP RUNS THE AI STEP ITSELF, WITH A DEADLINE, THEN REPUBLISHES (C-S24, RFW-D08)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-sa-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~1</issued_to>
<issued_by>2.0.0_SA_COO~RV</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (2026-10-02 ~21:3xZ, --drift) -- carrier C1 PARTIAL inside the 90 s budget (446 of 65,153 files scanned, 0 gates armed); C2-C6 not scanned (blind there); the notifier moratorium binds.
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell
comp-adversary: DECLARED-NOT-APPLICABLE the validator-context composer profiles RETURNED work for the L8/L9 packet; at the cut nothing is returned, and the issuer's evidence context is this order's check files
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric site-z) -- *rivalfunds*: daily holdings of rival active ETFs in two peer groups (IDVZ, PFOE), each fund's trade schedule, the A1 rankings, buying trend, input census and AI accounts, and a served page grouped by Opal fund (13 funds, package `data/etfs/scripts/rivalfunds/`, five AWS stage Lambdas, a terminal-machine Bloomberg leg the vehicle runs from the CLOUD working tree). **Round 7** makes the 09:00 ET sweep run the AI step itself (round 6 left no scheduled path to it), makes every run carry its trigger, has the census read the rankings' classification and agree with the header, gives one deterministic name per security, asks Bloomberg for the CUSIP lines' names, and carries the page-walk remainder (PRD v0.13). Nothing in round 7 deploys from a worker. Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-sa-1` -- the sweep runs the AI step itself, with a deadline, then republishes (C-S24; RFW-D08)
- `sweep.handler_entry` runs the AI step after `run_dag`, or after the `only` stages when they include publish-page. It runs
  only when `RIVALFUNDS_AI_ENABLE == "1"` and the day already holds a publish-page marker.
- Today `sweep.py:469-472` skips the publish whenever the marker exists, and the gateless morning publish always writes it,
  so no scheduled path reaches the AI stage.
- If the step ran (OK or FAILED), the sweep republishes through `publish_page.handler_entry` under a new batch id, passing
  the result as `event["ai_run"]`. publish-page makes NO AI call: it records `ai_run` as
  `a1_produced.research_hypotheses_run` `{status, reason, run_id, run_path}`.
- **Deadline:** event field `ai_deadline_s` (passed through by `trigger_event`), default constant `sweep.AI_DEADLINE_S`. The
  step never runs past the Lambda's remaining time minus `MARGIN_MS`. On an overrun:
  - no research_hypotheses object is written, now or later (no background writer);
  - the result is `{"status": "FAILED", "reason": "...deadline..."}`;
  - the page shows the failure.
- **One run per page day (CALL 5), OK or FAILED:** a later sweep makes no AI call. The cell records the attempt where the
  address builder says.
- **Gate unset:** the sweep writes nothing extra and does not republish.
- `ai_stage.run_for_day(sink_spec, day, run_path="ad_hoc", deadline_s=None, **kw)`.
- **Organic trigger:** the EventBridge sweep schedule (`etfs-rivalfunds-daily-lambda`, 09:00 ET trading days). Its
  invocation on 2026-10-05 is the acceptance.

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD 50761d39e9 (the package equals the deployed pin eb6e9f04ff))

- Today sweep.py ~:469-472 skips publish whenever the publish marker exists, and the gateless 07:00 ET morning publish always writes it, so NO scheduled path reaches the AI stage (round-6 ap-1 FAILED for this, CTO~Z analysis @94f682c868 ruling 1). The AI gate stays ONLY on the daily (sweep) Lambda; publish-page must never call the vendor.
- Interface (fixed at the cut; the checks read it): the sweep's AI step runs after run_dag (or after the `only` stages when they include publish-page), only when RIVALFUNDS_AI_ENABLE == "1" and the day holds a publish-page marker; if it ran (OK or FAILED) the sweep republishes through publish_page.handler_entry under a new batch id passing `event["ai_run"]`; publish-page records it as a1_produced.research_hypotheses_run {status, reason, run_id, run_path} and makes no AI call; event field `ai_deadline_s` (passed through by trigger_event), default constant `sweep.AI_DEADLINE_S` (your value; state it), never past the Lambda's remaining time minus MARGIN_MS; an overrun writes no object now or later (no background writer -- a thread with a join timeout fails AC2) and returns {"status": "FAILED", "reason": "...deadline..."}; the page shows the failure (e.g. a1["research_hypotheses_note"]); one run per page day OK or FAILED -- record the attempt where the address builder (lib/opal_naming address()) says; `ai_stage.run_for_day(sink_spec, day, run_path="ad_hoc", deadline_s=None, **kw)`.
- The round-6 hookup calls ai_stage.run_for_day from publish_page after produce_a1 -- REMOVE that call (publish-page records, it does not run); keep st-1's A1_PRODUCED/A1_TABLES split intact (the regression test in test_r6st1 must still pass).
- Shared fixtures: round7/checks/_s24_sweep.py and _common.py (offline_guards stubs boto3 and requests.post so nothing reaches S3 or the vendor).
- Organic trigger: the EventBridge sweep schedule on etfs-rivalfunds-daily-lambda (09:00 ET trading days).

## 3. SURFACES AND BOUNDS

You READ (never edit): `lib/`, `integrations/bloomberg/` (the Positioning pull is under an Andrew-direct no-modify order), the package's other modules and tests, `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round7/checks/` and rounds 5-6's `.../round5/checks/`, `.../round6/checks/`, the PRD `org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md` (v0.13), the round-6 analysis `org/missions/D5/ETFS/ETFS_RIVALS/ledger/ROUND_ANALYSIS.round6.md`, the walk brief `docs/briefs/rivalfunds-ui-data-walk-20261002.md` and its register `docs/briefs/rivalfunds-ui-data-findings-20261002.json`, and live S3 READ-ONLY where a check reads it.

You WRITE only the `<paths>` below (plus `deliverables/0.9.0_WK_ETFS_RIVALS~1/`). NEVER: any S3 write, any deploy, any Bloomberg or OpenAI call (stub every vendor hook in tests), the vehicle, any file another round-7 chain owns, and none of the merge hookups the decomposition names (the issuer adds them). Tests go beside the code as `tests/test_r7sa1_*.py`, run with `python -m pytest <file> -q` from `data/etfs/scripts/`; run the whole package suite before you report (it must read 0 failed). A check you cannot satisfy without leaving your `<paths>` is a surprise row in the investigation file, never an edit outside them.

<paths>
data/etfs/scripts/rivalfunds/sweep.py
data/etfs/scripts/rivalfunds/ai_stage.py
data/etfs/scripts/rivalfunds/publish_page.py
data/etfs/scripts/rivalfunds/tests/test_r7sa1_*.py
data/etfs/scripts/rivalfunds/tests/test_d1_sweep.py
data/etfs/scripts/rivalfunds/tests/test_r6ap1_ai_stage.py
data/etfs/scripts/rivalfunds/tests/test_r6st1_a1_follows_inputs.py
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- with the publish marker already present, the schedule payload's sweep reaches the AI stage, writes ONE research_hypotheses object and republishes (manifest research_hypotheses_run OK); a second sweep makes no AI call (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round7/checks/sa-1.AC1.py`)
- **AC2** -- past ai_deadline_s the sweep still republishes, WITHOUT accounts, the manifest records FAILED with the deadline reason and the page shows it; no late writer; CALL 5 holds after a FAILED (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round7/checks/sa-1.AC2.py`)
- **AC3** -- control: gate unset -> no AI client, no extra republish, today's outputs byte-identical (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round7/checks/sa-1.AC3.py`)
- **J1** (JUDGMENT, graded by 3.0.0_SA_CVO~RV at L9 on the served page) -- the 2026-10-05 09:00 ET organic sweep writes that day's account and republishes, with no seat act (the organic trigger is the acceptance); positive control: the issuer's deliberate SWEEP invoke with its own schedule payload after the deploy, and the round-6 negative (the 10-02 sweep reached no AI stage)

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-sa-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round7/checks/sa-1.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="AC2" cell_refs="RIV-sa-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round7/checks/sa-1.AC2.py</invocation><expect>AC2 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="AC3" cell_refs="RIV-sa-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round7/checks/sa-1.AC3.py</invocation><expect>AC3 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="J1" cell_refs="RIV-sa-1" judgment="true"/>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~1/ETFS_RIVALS.TO-RIV-sa-1.sweep-runs-ai-step.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-sa-1.sweep-runs-ai-step`. Report once: each mechanical criterion's verdict line with the output above it; each judgment criterion left UNVERIFIABLE-BY-INSTRUMENT for the CVO; files written; any existing test assertion changed and why; rows filed (id + one line). Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** Round-6 analysis @94f682c868 (CTO~Z msg 28735) section 3 + the RFW register
graded against rv-publish-1002r6; decomposition round 7 v1.0; Andrew-direct max parallelization (cooRV record 141xZ). Chain `~1`, slot `~1`, position 1 of 2 (sa-1 -> pv-1). Checks dry-run at base CLOUD 50761d39e9 (the package equals the deployed pin eb6e9f04ff):
sa-1.AC1 FAIL (3) as expected; sa-1.AC2 FAIL (3; no-late-writer and CALL 5 limbs PASS) as expected; sa-1.AC3 PASS (control) as expected; each PASSES under the check writer's in-memory fix (scratchpad r7_fix_harness.py).

<risk>SERVED</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>7</round>
<slot>~1</slot>
<fabric>site-z</fabric>
