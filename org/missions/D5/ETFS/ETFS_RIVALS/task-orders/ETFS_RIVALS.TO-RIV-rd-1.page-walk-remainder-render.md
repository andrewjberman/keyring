# ETFS_RIVALS task order -- `RIV-rd-1` -- ROUND 7 (ENRICHMENT): THE PAGE-WALK REMAINDER IN render.py (RFW-D12, U09, U13, U14, U16)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-rd-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~2</issued_to>
<issued_by>2.0.0_SA_COO~RV</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (2026-10-02 ~21:3xZ, --drift) -- carrier C1 PARTIAL inside the 90 s budget (446 of 65,153 files scanned, 0 gates armed); C2-C6 not scanned (blind there); the notifier moratorium binds.
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell
comp-adversary: DECLARED-NOT-APPLICABLE the validator-context composer profiles RETURNED work for the L8/L9 packet; at the cut nothing is returned, and the issuer's evidence context is this order's check files
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric site-z) -- *rivalfunds*: daily holdings of rival active ETFs in two peer groups (IDVZ, PFOE), each fund's trade schedule, the A1 rankings, buying trend, input census and AI accounts, and a served page grouped by Opal fund (13 funds, package `data/etfs/scripts/rivalfunds/`, five AWS stage Lambdas, a terminal-machine Bloomberg leg the vehicle runs from the CLOUD working tree). **Round 7** makes the 09:00 ET sweep run the AI step itself (round 6 left no scheduled path to it), makes every run carry its trigger, has the census read the rankings' classification and agree with the header, gives one deterministic name per security, asks Bloomberg for the CUSIP lines' names, and carries the page-walk remainder (PRD v0.13). Nothing in round 7 deploys from a worker. Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-rd-1` -- the page-walk remainder in render.py (RFW-D12, U09, U13, U14, U16)
- **The name-map shadow (found at the cut):** a second `def _render_page` at `render.py:1457` replaces the wrapper at :1446.
  The wrapper fills `_NAMES`, so `render_page` never fills it. U14 (one display name per security) has been dead since
  95af466e67. Rename the body and keep the wrapper.
- D12: a buying-trend line built from ONE window reads "Single trade", not BET or TILT (`render.py` ~:970).
- U09: the account text's stored reading keys display as labels. That includes multi-word keys and bare family names
  (`fear_greed`, `"middle" east oil`; the label regex ~:1072). The face's vintage line shows no raw table names.
- U13: the holdings table reads plain words ("UNRESOLVED" ~:436, identifier types, "source policy ..." ~:399), each with
  its code in a title tooltip, as the trade log does.
- U14: the holdings-table name (~:438) reads through the page's one name map (no case-only clashes).
- U16: the buying trend's no-sector row becomes a footnote with its share, like the rankings' data-unclassified-share.
- **Organic trigger:** the 07:00 ET marker publish and the 09:00 ET sweep publish. The page they write is the evidence.

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD 50761d39e9 (the package equals the deployed pin eb6e9f04ff))

- ROOT CAUSE for U14 (found at the cut): render.py defines `_render_page` TWICE (~:1446 and ~:1457). The second replaces the wrapper that fills `_NAMES`, so render_page's page-wide name map is always empty (since CRO~RV's layout pass 95af466e67). Rename the body (e.g. `_render_page_body`), keep the wrapper calling it. tests/test_r6ui5_census_and_audit_trail.py:85-94 sets _NAMES by hand, so it never saw this -- make your test go through render_page.
- Interfaces (the checks read them): D12 -- a line with n_windows == 1 reads 'Single trade', neither text nor hover says BET or TILT; 2+ windows keep '<Reading>, <n> trades'. U16 -- the trend's sector tables drop Unclassified; one `data-unclassified-share` element outside the table rows; share = Unclassified gross traded / all sectors' gross traded (`_traded_of`, the measure `_sectors_hidden` uses), text states the %. U09 -- a whole stored key becomes a label whose `title` is exactly the key; a bare family name reads e.g. 'Fear & Greed' with title `fear_greed`; the `data-vintage` line names tables in words with the code in a title. U13 -- the trade log's rule: code in a title ('Key resolution: UNRESOLVED', 'Identifier type: cusip'), policy in words with `bloomberg_primary` in a title. U14 -- the holdings name equals the face name ('Intuit Inc'), one casing on the page.
- Keep the round-6 contracts and CRO~RV's layout (test_crorv_layout.py): data-excluded-ca, data-excluded-income, one details.trace per trade, the holding dialogs and DIALOG_SOFT_CAP.
- Left out (not this cell): the status section's 'Source policy' column and the cited-row table names.
- Organic trigger: the 07:00 ET marker publish and the 09:00 ET sweep publish; the page they write is the evidence.

## 3. SURFACES AND BOUNDS

You READ (never edit): `lib/`, `integrations/bloomberg/` (the Positioning pull is under an Andrew-direct no-modify order), the package's other modules and tests, `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round7/checks/` and rounds 5-6's `.../round5/checks/`, `.../round6/checks/`, the PRD `org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md` (v0.13), the round-6 analysis `org/missions/D5/ETFS/ETFS_RIVALS/ledger/ROUND_ANALYSIS.round6.md`, the walk brief `docs/briefs/rivalfunds-ui-data-walk-20261002.md` and its register `docs/briefs/rivalfunds-ui-data-findings-20261002.json`, and live S3 READ-ONLY where a check reads it.

You WRITE only the `<paths>` below (plus `deliverables/0.9.0_WK_ETFS_RIVALS~2/`). NEVER: any S3 write, any deploy, any Bloomberg or OpenAI call (stub every vendor hook in tests), the vehicle, any file another round-7 chain owns, and none of the merge hookups the decomposition names (the issuer adds them). Tests go beside the code as `tests/test_r7rd1_*.py`, run with `python -m pytest <file> -q` from `data/etfs/scripts/`; run the whole package suite before you report (it must read 0 failed). A check you cannot satisfy without leaving your `<paths>` is a surprise row in the investigation file, never an edit outside them.

<paths>
data/etfs/scripts/rivalfunds/render.py
data/etfs/scripts/rivalfunds/tests/test_r7rd1_*.py
data/etfs/scripts/rivalfunds/tests/test_p1_page_and_guardrails.py
data/etfs/scripts/rivalfunds/tests/test_p2_page_grouped_by_fund.py
data/etfs/scripts/rivalfunds/tests/test_r6ui5_census_and_audit_trail.py
data/etfs/scripts/rivalfunds/tests/test_r6ui3_trend_card.py
data/etfs/scripts/rivalfunds/tests/test_r6ui4_ai_account_cards.py
data/etfs/scripts/rivalfunds/tests/test_crorv_layout.py
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- a one-window trend line reads 'Single trade' (no BET/TILT); the trend's sector tables drop Unclassified for one data-unclassified-share footnote with its % (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round7/checks/rd-1.AC1.py`)
- **AC2** -- every stored reading key (multi-word and bare family names) displays as its label with title = the key; the data-vintage line names tables in words (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round7/checks/rd-1.AC2.py`)
- **AC3** -- the holdings table reads plain words with codes in title tooltips (key resolution, identifier type, source policy); one name per security across the page via render_page (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round7/checks/rd-1.AC3.py`)
- **J1** (JUDGMENT, graded by 3.0.0_SA_CVO~RV at L9 on the served page) -- the served page after the deploy reads with no raw system word or code on any face and one name per security; positive control: the served 2026-10-02 page (rv-publish-1002r6): 58 'Bet, 1 trade', 4 bare fear_greed, 195 split labels, 94 UNRESOLVED cells, 45 case-only name clashes

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-rd-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round7/checks/rd-1.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="AC2" cell_refs="RIV-rd-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round7/checks/rd-1.AC2.py</invocation><expect>AC2 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="AC3" cell_refs="RIV-rd-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round7/checks/rd-1.AC3.py</invocation><expect>AC3 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="J1" cell_refs="RIV-rd-1" judgment="true"/>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~2/ETFS_RIVALS.TO-RIV-rd-1.page-walk-remainder-render.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-rd-1.page-walk-remainder-render`. Report once: each mechanical criterion's verdict line with the output above it; each judgment criterion left UNVERIFIABLE-BY-INSTRUMENT for the CVO; files written; any existing test assertion changed and why; rows filed (id + one line). Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** Round-6 analysis @94f682c868 (CTO~Z msg 28735) section 3 + the RFW register
graded against rv-publish-1002r6; decomposition round 7 v1.0; Andrew-direct max parallelization (cooRV record 141xZ). Chain `~2`, slot `~2`, position 1 of 1. Checks dry-run at base CLOUD 50761d39e9 (the package equals the deployed pin eb6e9f04ff):
rd-1.AC1 FAIL (3; control OK) as expected; rd-1.AC2 FAIL (3; control OK) as expected; rd-1.AC3 FAIL (3; control OK) as expected; each PASSES under the check writer's in-memory fix (scratchpad r7_rdcsnm/posarm.py).

<risk>SERVED</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>7</round>
<slot>~2</slot>
<fabric>site-z</fabric>
