# ETFS_RIVALS task order -- `RIV-ui-2` -- ROUND 6 (ENRICHMENT): THE RANKING PANELS (RFW-U02, RFW-U03, RFW-U04, RFW-U16 render half, rk-2's refusal display)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-ui-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~6</issued_to>
<issued_by>2.0.0_SA_COO~RV</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (2026-10-02 ~15:2xZ, --drift) -- carrier C1: 31 sentinels scanned, 12 gates armed, none names rivalfunds/, etfs-rivalfunds or this cell's files; C2-C5 not scanned inside the 90 s budget (blind there); the notifier moratorium binds.
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell
comp-adversary: DECLARED-NOT-APPLICABLE the validator-context composer profiles RETURNED work for the L8/L9 packet; at the cut nothing is returned, and the issuer's evidence context is this order's check files
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric site-z) -- *rivalfunds*: daily holdings of rival active ETFs in two peer groups (IDVZ, PFOE), each fund's trade schedule, the A1 rankings, buying trend, input census and AI accounts, and a served page grouped by Opal fund (13 funds, package `data/etfs/scripts/rivalfunds/`, five AWS stage Lambdas, a terminal-machine Bloomberg leg the vehicle runs from the CLOUD working tree). **Round 6** makes the A1 tables follow their inputs, puts the AI accounts into the scheduled path, adds the plausibility guard, fixes dividend currency and exit pricing, gives the census three states and the page real names, and carries the 33-item page walk (PRD v0.12). Nothing in round 6 deploys from a worker. Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-ui-2` -- the ranking panels (RFW-U02, RFW-U03, RFW-U04, RFW-U16 render half; rk-2's refusal display)
- The default period is the shortest that ranks at least one holding for the fund; an empty period's switch shows its state.
- A fund-period with 0 ranked renders ONE empty-state line with its reason and the count without a price.
- Each block carries a one-line count chip; the method text appears once per page, behind an info element.
- "Unclassified" is never a ranked row: it is a footnote with its share.
- A refused fund-period (rk-2) shows "Rankings refused" with its bound, marked `data-refused`, and no table.

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD bdbd7a257b (rv-fast; render.py unchanged since the deployed 722f0db291))

- DOM hooks: one `data-empty-state` line per 0-ranked panel carrying the count of unpriced holdings; the refused panel carries `data-refused` and the words "Rankings refused" with its bound (the rk-2 cell writes the producer's refused row: axis "refused", bucket = the bound name, contribution = the offending value); one footnote `data-unclassified-share="<fraction>"` (the absolute share, the same measure `_sectors_hidden` uses) with a % in its text; the checked `rf-period-*` radio as in AC3.
- At base a refused panel CRASHES `_rank_panel` (IndexError): handle a panel whose rows are one refused row.
- The sx-1 cell makes the producers write Unclassified with rank NULL; until it merges, today's data ranks it. Never re-rank sectors in render: drop the Unclassified row from the ranked list and footnote its share.
- Round-5 pg-1.AC1 (the page opens on MTD) stays true whenever MTD ranks.

## 3. SURFACES AND BOUNDS

You READ (never edit): `lib/`, `integrations/bloomberg/` (the Positioning pull is under an Andrew-direct no-modify order), the package's other modules and tests, `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round6/checks/` and round 5's `.../round5/checks/`, the PRD `org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md` (v0.12), the walk brief `docs/briefs/rivalfunds-ui-data-walk-20261002.md` and its register `docs/briefs/rivalfunds-ui-data-findings-20261002.json`, and live S3 READ-ONLY where a check reads it.

You WRITE only the `<paths>` below (plus `deliverables/0.9.0_WK_ETFS_RIVALS~6/`). NEVER: any S3 write, any deploy, any Bloomberg or OpenAI call (stub every vendor hook in tests), the vehicle, any file another round-6 chain owns, and none of the merge hookups the decomposition names (the issuer adds them). Tests go beside the code as `tests/test_r6ui2_*.py`, run with `python -m pytest <file> -q` from `data/etfs/scripts/`; run the whole package suite before you report (it must read 0 failed). A check you cannot satisfy without leaving your `<paths>` is a surprise row in the investigation file, never an edit outside them.

<paths>
data/etfs/scripts/rivalfunds/render.py
data/etfs/scripts/rivalfunds/tests/test_r6ui2_*.py
data/etfs/scripts/rivalfunds/tests/test_p1_page_and_guardrails.py
data/etfs/scripts/rivalfunds/tests/test_p2_page_grouped_by_fund.py
data/etfs/scripts/rivalfunds/tests/test_render_one_sector_rule.py
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- a 0-ranked fund-period renders ONE data-empty-state line with its count and no table shells; a refused fund-period shows 'Rankings refused' with data-refused and no table (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round6/checks/ui-2.AC1.py`)
- **AC2** -- Unclassified is never a ranked row: one data-unclassified-share footnote with its % (accepts today's data shape and sx-1's) (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round6/checks/ui-2.AC2.py`)
- **AC3** -- the checked period is the first of MTD/QTD/YTD that ranks at least one holding for the opening fund, else MTD (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round6/checks/ui-2.AC3.py`)
- **J1** (JUDGMENT, graded by 3.0.0_SA_CVO~RV at L9 on the served page) -- RFW-U04 (one count chip per block; the method text once per page behind an info element) and U02's second half (an empty period's switch shows its state); positive control: the served 2026-10-02 page (batch rv-publish-1002g), where the method text repeats in every block and an empty period renders four table shells

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-ui-2"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round6/checks/ui-2.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="AC2" cell_refs="RIV-ui-2"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round6/checks/ui-2.AC2.py</invocation><expect>AC2 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="AC3" cell_refs="RIV-ui-2"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round6/checks/ui-2.AC3.py</invocation><expect>AC3 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="J1" cell_refs="RIV-ui-2" judgment="true"/>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~6/ETFS_RIVALS.TO-RIV-ui-2.ranking-panels.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-ui-2.ranking-panels`. Report once: each mechanical criterion's verdict line with the output above it; each judgment criterion left UNVERIFIABLE-BY-INSTRUMENT for the CVO; files written; any existing test assertion changed and why; rows filed (id + one line). Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** Round-5 analysis @56c99763bb (msg 28485) section 4 + PRD v0.12 @afc2bed44f
(RFW register, msg 28535); decomposition round 6 v1.0; Andrew-direct "/canonical-drive with max parallelization on
subagents" (cooRV record 141xZ). Chain `~6`, slot `~6`, position 2 of 5 (ui-1 -> ui-2 -> ui-3 -> ui-4 -> ui-5). Checks dry-run at base CLOUD bdbd7a257b (rv-fast; render.py unchanged since the deployed 722f0db291):
ui-2.AC1 FAIL (3; ranked-panel control PASS) as expected; ui-2.AC2 FAIL (2; sx-1-shape control PASS) as expected; ui-2.AC3 FAIL (1; MTD-ranks control PASS) as expected.

<risk>SERVED</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<round>6</round>
<slot>~6</slot>
<fabric>site-z</fabric>
