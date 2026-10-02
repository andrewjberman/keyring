# ETFS_RIVALS task order -- `RIV-ui-1` -- ROUND 6 (ENRICHMENT): PAGE HEADER AND CHROME (RFW-U01, RFW-U17, RFW-U15)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-ui-1</owned_cells>
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

### `RIV-ui-1` -- page header and chrome (RFW-U01, RFW-U17, RFW-U15; the absence sentences)
- The current-funds count appears once, and the sentence names only lagging funds (absent when none lag).
- A fund header reads "Latest report 30 Sep", a source chip and a separate current/late chip.
- No SVG bar has a negative width (clamped >= 0).
- An absence reason starts with a capital letter ("No AI account. The ...", "Input census not available. The ...").

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD bdbd7a257b (rv-fast; render.py unchanged since the deployed 722f0db291))

- The DOM hooks the checks read: `data-headline` appears only when a fund lags (`data-lagging` stays as it is); one chip per fund header with `data-freshness="current|late"` beside the existing `data-source` badge; the header date reads like "30 Sep"; no `<rect>` with a negative width or height (`_svg_bars` drew -5.0/-4.0, the holdings list -0.5).
- Keep round 5's contracts: the KPI tile keeps its "funds current" label (round-5 f-4.AC1 reads "n of m funds current"); the page still opens on MTD when MTD ranks (round-5 pg-1.AC1).
- The absence sentences start with a capital letter ("No AI account. The ...", "Input census not available. The ..."): the round-5 r-6.AC1 limb moved to this cell; its tests are yours.
- Shared helper: `round6/checks/_ui.py` builds the page offline from fixtures.
- render.py is this chain's ONE write set across five orders; the next four orders build on what this one leaves.

## 3. SURFACES AND BOUNDS

You READ (never edit): `lib/`, `integrations/bloomberg/` (the Positioning pull is under an Andrew-direct no-modify order), the package's other modules and tests, `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round6/checks/` and round 5's `.../round5/checks/`, the PRD `org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md` (v0.12), the walk brief `docs/briefs/rivalfunds-ui-data-walk-20261002.md` and its register `docs/briefs/rivalfunds-ui-data-findings-20261002.json`, and live S3 READ-ONLY where a check reads it.

You WRITE only the `<paths>` below (plus `deliverables/0.9.0_WK_ETFS_RIVALS~6/`). NEVER: any S3 write, any deploy, any Bloomberg or OpenAI call (stub every vendor hook in tests), the vehicle, any file another round-6 chain owns, and none of the merge hookups the decomposition names (the issuer adds them). Tests go beside the code as `tests/test_r6ui1_*.py`, run with `python -m pytest <file> -q` from `data/etfs/scripts/`; run the whole package suite before you report (it must read 0 failed). A check you cannot satisfy without leaving your `<paths>` is a surprise row in the investigation file, never an edit outside them.

<paths>
data/etfs/scripts/rivalfunds/render.py
data/etfs/scripts/rivalfunds/tests/test_r6ui1_*.py
data/etfs/scripts/rivalfunds/tests/test_p1_page_and_guardrails.py
data/etfs/scripts/rivalfunds/tests/test_p2_page_grouped_by_fund.py
data/etfs/scripts/rivalfunds/tests/test_r5f4_page_floors_headline.py
data/etfs/scripts/rivalfunds/tests/test_home_producer_source.py
data/etfs/scripts/rivalfunds/tests/test_render_one_sector_rule.py
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- the current-funds count appears once; the headline sentence names only lagging funds and is absent when none lag (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round6/checks/ui-1.AC1.py`)
- **AC2** -- each fund header reads 'Latest report 30 Sep' with the source chip and ONE data-freshness chip (current|late) (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round6/checks/ui-1.AC2.py`)
- **AC3** -- no SVG rect has a negative width or height; positive bars keep their widths (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round6/checks/ui-1.AC3.py`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-ui-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round6/checks/ui-1.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="AC2" cell_refs="RIV-ui-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round6/checks/ui-1.AC2.py</invocation><expect>AC2 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="AC3" cell_refs="RIV-ui-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round6/checks/ui-1.AC3.py</invocation><expect>AC3 RESULT: PASS 0 failures</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~6/ETFS_RIVALS.TO-RIV-ui-1.page-header-and-chrome.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-ui-1.page-header-and-chrome`. Report once: each mechanical criterion's verdict line with the output above it; each judgment criterion left UNVERIFIABLE-BY-INSTRUMENT for the CVO; files written; any existing test assertion changed and why; rows filed (id + one line). Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** Round-5 analysis @56c99763bb (msg 28485) section 4 + PRD v0.12 @afc2bed44f
(RFW register, msg 28535); decomposition round 6 v1.0; Andrew-direct "/canonical-drive with max parallelization on
subagents" (cooRV record 141xZ). Chain `~6`, slot `~6`, position 1 of 5 (ui-1 -> ui-2 -> ui-3 -> ui-4 -> ui-5). Checks dry-run at base CLOUD bdbd7a257b (rv-fast; render.py unchanged since the deployed 722f0db291):
ui-1.AC1 FAIL (3; controls PASS) as expected; ui-1.AC2 FAIL (4; source chip control PASS) as expected; ui-1.AC3 FAIL (2; positive-bar and 128-rect sweep controls PASS) as expected.

<risk>SERVED</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>6</round>
<slot>~6</slot>
<fabric>site-z</fabric>
