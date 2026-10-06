# ETFS_RIVALS task order -- `RIV-fe-1` -- ROUND 13 (ENRICHMENT): EVERY MENTION IN FUND F'S PANEL OPENS A MODAL WITH F'S ENGAGEMENT; THE PAGE COUNTS IT; THE TREND'S TICKER-NAMED KEYS GET NAMES

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-fe-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~2</issued_to>
<issued_by>2.0.0_SA_COO~RV</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule, cron or trigger is added or moved by this cell
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell (the gateway's read policy already covers the page prefix)
comp-adversary: DECLARED-NOT-APPLICABLE the validator-context composer profiles RETURNED work for the L8/L9 packet; at the cut nothing is returned, and the issuer's evidence context is this order's check files
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric site-z) -- *rivalfunds*: a daily research page on rival active ETFs (13 funds, two peer groups), published to S3 by the package `data/etfs/scripts/rivalfunds/` (five AWS stage Lambdas) and served signed-in by the opal-gateway (Starlette app under `infra/aws/ec2/opal-gateway/app/`) at `mcp.opalinvest.dev/rivalfunds`. Andrew's word: "Any mention of a security by ticker should be hyperlinked to the modal popup for that fund's engagement with that security" and "1.) Pull audit off the page 2.) Get those linking schemas up and running 3.) Make an audit gateway after 2.) is done". Round 12 took the audit trail off the page into a daily `audit.html` and linked every ticker. **Round 13** (main workstream): the audit route and link, and every mention opening its fund's engagement. Nothing here deploys, merges or calls a vendor. Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-fe-1` -- every mention in fund F's panel opens a modal with F's engagement; the page counts it; the trend's ticker-named keys get names (round-11 analysis rulings 1, 2, 5: C-S47 + Z-S50 + C-S36)
- Measured on the served 10-06 page (CVO census, C-S47): 15 mentions (3 securities, 2 funds) open a modal with no section for the
  linking fund -- Nebius (two keys; pk-1 + al-1), Alphabet (a share-class name crossing to the other listing), SpaceX (a fresh
  GQGU entry with no contribution row and no YTD trend row, so `_sec_dialogs` writes no GQGU section). Four securities still read
  in ticker form (C-S36): 8053 JP, RBLX US (rankings / AI text), 9433 JP, 000270 KS (trend only) -- the names stage reads only
  holding_contribution keys.
- Interface: a name mention inside fund F's panel links to the key F holds or traded among the keys carrying that name (a name two
  listings share resolves by F's own holdings, Z-S50; when F holds none, the page-wide rule applies). `_sec_dialogs` writes a
  `section data-fund=<_fid(F)>` for EVERY fund F with a contribution row OR a trend row (any period) for that key -- a trend-only
  fund's section states its buying. `render.fund_section_census(html) -> {"buttons", "with_section", "missing"}` over every
  `data-sec` button inside a `data-fund-panel`; `publish_page` puts it in the manifest (`fund_sections`) and prints a line starting
  `FAIL: fund sections missing` when missing > 0. `security_names` asks for the ticker-named keys of the newest holding_contribution
  AND buying_trend objects.
- **Organic trigger:** the 07:00 ET marker publish; the names stage on the vehicle's daily run.

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD 365f0a59e1)

- The check files' docstrings are the exact interface they read: read `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round13/checks/fe-1.AC1.py`, `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round13/checks/fe-1.AC2.py` and `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round13/checks/_common.py` before you build.
- Name resolution: `render._collect_names`, `_collect_aliases`, `_resolve_names` (~1360) and the two-pass in `_render_doc` / `_render_page` (round 9 RIV-ln-1, round 12 au-1) decide which key a name links to page-wide (`_NAME_KEYS`, `_NAME_AMBIG`); a mention renders through `_sec_button` (~694). The fund context of a mention is the panel being rendered (`_fund_panel(ctx, f)`, ~1600): F's own keys are its contribution rows, trend rows and trades.
- Dialog sections: `_sec_dialogs` (~1638) builds `contrib` from holding_contribution rows and `trend` from `_trend_rows(ctx, fund, "YTD")` only -- a trend row in another period, or a fund with neither, gets no section.
- `publish_page.handler_entry` already prints `FAIL: holding dialogs off ...` and writes `holding_dialogs` into the manifest (round 12): add `fund_sections` the same way.
- `security_names.handler_entry` (~133) reads the newest holding_contribution within LOOKBACK_DAYS; read the newest buying_trend the same way.
- You run fe-1 FIRST; lk-1 follows on the same branch.
- AMENDMENT 1 (issuer, 2026-10-06 ~20:5xZ; CTO half @2f44b42430, the Alphabet case 1): the order is REOPENED with a third criterion, AC3. Measured on the served 10-06 page after your build: WCMG's account text "Alphabet Inc" (citing `WCMG|R30|GOOGL_US_Equity`; WCMG holds GOOGL, page name "Alphabet Inc") renders as a button to GOOG_US_Equity reading "Alphabet Inc-Cl C" -- 2 of the 10 fund-section misses. Cause read in `render._collect_aliases`: a row names GOOG with a casing variant of "Alphabet Inc", the alias "alphabet inc" maps to GOOG's page name, and the second loop's `setdefault` keeps it over GOOGL's own page name, so the text is rewritten before your fund-aware rule sees it. Read `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round13/checks/fe-1.AC3.py` (its docstring is the interface): inside fund F's panel a name or alias that resolves to several keys' names links to the key F holds or traded and reads THAT key's page name; the cited key breaks a remaining tie. Work in the NEW worktree your issuer names (based on CLOUD, WITHOUT lk-1); AC1 and AC2 must still PASS.

## 3. SURFACES AND BOUNDS

You READ (never edit): `lib/`, `integrations/bloomberg/` (Andrew-direct no-modify order), every file not in your `<paths>`, the round-8..13 check folders under `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/`, the decomposition `org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md`, and `org/missions/D5/ETFS/ETFS_RIVALS/ledger/ROUND_ANALYSIS.round11.md`.

You WRITE only the `<paths>` below (plus `deliverables/0.9.0_WK_ETFS_RIVALS~2/`). NEVER: any S3 read or write, any deploy or gateway release, any Terraform, any Bloomberg or OpenAI call (stub every vendor hook), any environment gate flip outside a test, any file under `integrations/`. New tests as `data/etfs/scripts/rivalfunds/tests/test_r13fe1_*.py` beside the code's tests; run the code's whole test suite before you report: 0 failed. A check you cannot satisfy without leaving your `<paths>` is a surprise row in the investigation file (`surfaced_at` = `date -u +%FT%TZ` at filing), never an edit outside them.

<paths>
data/etfs/scripts/rivalfunds/render.py
data/etfs/scripts/rivalfunds/publish_page.py
data/etfs/scripts/rivalfunds/security_names.py
data/etfs/scripts/rivalfunds/tests/
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- per-button census (missing 0, equal to `render.fund_section_census`); SpaceX (trend-only) opens a modal with TXUE's section; 'Alphabet Inc' in IDVZ's AI text links to the listing IDVZ holds; control: Apple in IDVZ's panel (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round13/checks/fe-1.AC1.py`)
- **AC2** -- the names stage asks for the rankings' and the trend's ticker-named keys; control: a G4-named key is never asked (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round13/checks/fe-1.AC2.py`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-fe-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round13/checks/fe-1.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="AC2" cell_refs="RIV-fe-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round13/checks/fe-1.AC2.py</invocation><expect>AC2 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="AC3" cell_refs="RIV-fe-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round13/checks/fe-1.AC3.py</invocation><expect>AC3 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="J1" cell_refs="RIV-fe-1" judgment="true"/>
</proof_of_spec>

J1 (graded by 3.0.0_SA_CVO~RV at L9 on the issuer's real render, never self-graded): on the served page, the 15 C-S47 mentions open a modal with their fund's section, the manifest's fund_sections.missing reads 0, and the C-S36 control set (8053 JP, 9433 JP, RBLX US, 000270 KS) reads real names after the next names run.

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~2/ETFS_RIVALS.TO-RIV-fe-1.every-mention-opens-its-funds-engagement.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-fe-1.every-mention-opens-its-funds-engagement`. Report once: each mechanical criterion's verdict line with the output above it; each judgment criterion left UNVERIFIABLE-BY-INSTRUMENT for the CVO; files written; every existing test assertion changed and why; the suite's final line; rows filed (id + one line); the hookups you need the issuer to add at the merge. Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER AMENDMENT 1 (2.0.0_SA_COO~RV, 2026-10-06 ~20:5xZ):** REOPENED (never re-cut): criterion AC3 added on the CTO half @2f44b42430 (Alphabet case 1: WCMG holds exactly one Alphabet listing, GOOGL; measured on the served rv-publish-1006r13 page). fe-1.AC3 dry-run at CLOUD 98de9868ce: FAIL (2; control (c) PASS) as expected. Four mechanical criteria would exceed the diet's three only if AC3 were new work; it is the SAME built behaviour (rule 1) on the real name shape -- stated here as the one-line reason. No gate limb grades a modification (LIMB 6 fires on new orders).

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** ROUND_ANALYSIS.round11.md @3ae96d6bc7 section 3; decomposition v1.3 (round 13 appended). Chain `~2`, slot `~2`, position 1 of 2. Checks dry-run at base: fe-1.AC1 FAIL (3: SpaceX 3 buttons missing TXUE's section, census function absent, Alphabet unlinked; control (d) PASS) as expected; fe-1.AC2 FAIL (1: asks only BBB; control (b) PASS) as expected.

<risk>SERVED</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>13</round>
<slot>~2</slot>
<fabric>site-z</fabric>
<status>complete</status>
<status>in_progress</status>
