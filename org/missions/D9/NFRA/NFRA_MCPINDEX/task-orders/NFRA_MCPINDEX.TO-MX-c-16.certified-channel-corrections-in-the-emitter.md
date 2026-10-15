# NFRA_MCPINDEX task order -- `MX-c-16` -- the emitter's three certified-channel corrections: re-rule the frozen aum-metrics row to deny, drop the legacy mdpf row, state the news channel's measured size and its EMPTY and frozen markers

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.md</decomp_doc>
<owned_cells>MX-c-16</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPINDEX.TO-MX-c-16</to_id>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~40</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- the emitter and its tests only; no AWS call.
comp-adversary: DECLARED-NOT-APPLICABLE -- the base dry-run plus nine planted arms are the control (decomposition R16.3a).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `MX-c-16` (round 16)

Work in your own worktree (cut from `box/sitez`; its portal folder is provisioned because the emitter reads it). Every path below is relative to its root. The one catalog writer is
`workflows/atom_decomposition/emit_catalog_v02.py`; you change ONLY it and its tests. The catalog it writes is `infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml`: you REGENERATE it in YOUR worktree to grade the checks, and you do NOT commit it (the issuer regenerates and lands it at the drain).

**Why.** These are corrections to channel text that the CVO certified, each changing what the catalog tells the gateway. The CVO read them (READ-OK) on two conditions that the checks make mechanical: nothing may move from deny to serve for any firm principal, and the news text change touches no gate field. Do exactly the three changes below and nothing else.

### Change (a) -- re-rule the frozen aum-metrics row to DENY

The catalog row with key `json/portfolios/aum-metrics.json` (map entity `pos.03.portfolios-aum-metrics`, which carries the twins `att.03` and `ft.04`) is today `serve-with-caveat`. The artifact is frozen 58 trading days behind T-1 (period 2026-07-22) and no PROD page reads it any more (consumer gone), so the row becomes `verdict_class: deny`, `verdict_state: ruled`.
- Add a module constant `VERDICT_OVERRIDE = {"pos.03.portfolios-aum-metrics": ("deny", "ruled", "<reason text>")}` beside `EMISSION_MAP`.
- At the row writer, right after `vc, vstate = verdict_class(sv)`, apply it: `if eid in VERDICT_OVERRIDE: vc, vstate = VERDICT_OVERRIDE[eid][0], VERDICT_OVERRIDE[eid][1]`.
- The row's quotable refusal reason (the gate prints the row's `serve_verdict_with_caveats` text when it denies) must begin `DENY (re-ruled in round 16, G3 contract portfolios_legacy):` and then state, in one sentence, that the artifact is frozen 58 trading days behind T-1 with period 2026-07-22 and that no PROD page reads it. Find where the writer emits `serve_verdict_with_caveats` for the row and use the override reason for an overridden entity.

### Change (b) -- drop the legacy mdpf row

Remove the `EMISSION_MAP` entry `mp.15.json-mdpf-legacy` (key `json/mdpf/**`) and its two entries in `VINTAGE_FIELD` and `VINTAGE_GRAIN`-style tables (search the file for `mp.15`). Add `"mp.15.json-mdpf-legacy": "SUPERSEDED legacy tree: 0 keys at the G3 measurement (2026-10-14), platinum is primary; dropped from the routable catalog (the objects and the live json/mdpf/{firm}/account-distribution.json portal object are not touched)"` to the `UNMAPPED` dictionary, so the drop is named and never silent. Leave the `never_serve` text lines as they are.
The `mdpf_model_portfolios` channel then has exactly one artifact row fewer than before (8 become 7).

### Change (c) -- the news channel text

The `news` channel is a preserved v0.1 fragment (the writer function `emit_v01_fragment` copies it and has per-channel patches, e.g. for `market_regime_trending` and `correlations_factors`). Add a patch for `ch == "news"` that changes ONLY these texts and no other key:
1. `tables.articles`: replace `(298K items; one day ~350 items)` with `(381,261 items measured 2026-10-14; about 1,000 a weekday, 985 to 1,229 over 2026-09-25 to 2026-10-13)`, keeping the rest of that string.
2. `hazards`: append two strings. One must contain the words `opal-harvest-articles` and `EMPTY` (for example `opal-harvest-articles EMPTY: 0 items since it was created on 2026-09-11 -- do not serve`). The other must contain the words `frozen` and `2026-04-13` (for example `the Seeking Alpha scraper output (bucket opal-data-news-av) is frozen since 2026-04-13 -- serve only with that vintage stated`).
3. The `news` channel gains NO `artifacts`, NO `verdict_class`, `allowlist`, `firm` or `firm_resolution`. It changes no gate field.

### Steps

1. Make the three changes. Update or add tests under `workflows/atom_decomposition/tests/` for them (a unit test for the override, for the dropped row and for the news patch), and fix any existing test there that pinned the old counts (for example a family-axis census that counted the dropped row).
2. Run the unit tests of that folder: `python -m pytest -q -p no:cacheprovider workflows/atom_decomposition/tests` (all must pass).
3. Regenerate the catalog in your worktree: `python workflows/atom_decomposition/emit_catalog_v02.py` (it must end with the HARVEST ROWS and SILVER lines and no EMIT REFUSED line). Do NOT commit `DATA_CATALOG.yaml`.
4. Run the three criteria in section 4.

## 2. BOUNDS

1. You change only the files in `<paths>`. No `catalog_entries/` row, no registry file, no `DATA_CATALOG.yaml` commit, no gateway app or test file, no portal file, no tool, grant, route, role, `.env` or AWS change. No deploy. No push.
2. No firm or product name may be typed as a whole-string literal in code (the naming gate refuses a NEW hand-kept firm or product token); the reason strings above are prose with spaces and are fine.
3. The checks are `deliverables/2.0.0_SA_COO~MI/round16/checks/c16.AC1.sh`, `c16.AC2.sh`, `c16.AC3.sh` (python `c16_check.py`). Read `c16_check.py` for exactly what is graded. Do not edit them.
4. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
workflows/atom_decomposition/emit_catalog_v02.py
workflows/atom_decomposition/validate_catalog_v02.py
workflows/atom_decomposition/tests/
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~40/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W40-S<k>`;
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`;
- `surfaced_at` written as a full UTC timestamp.

## 4. PROOF OF SPEC (literal; run from your worktree root, after step 3)

<proof_of_spec>
  <expected_criteria>AC1,AC2,AC3</expected_criteria>
  <criterion id="AC1" cell_refs="MX-c-16" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round16/checks/c16.AC1.sh; echo "exit=$?"</invocation><expect>CHECK ok on all five lines: the aum-metrics row is deny + ruled; no json/mdpf/ artifact row and the mdpf channel lost exactly one row (8 -> 7); the news articles text carries 381,261 and not 298K; the EMPTY and frozen hazards are present -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-c-16" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round16/checks/c16.AC2.sh; echo "exit=$?"</invocation><expect>the DENOMINATOR line (65 keys x 6 principals = 390 pairs) and deny->serve=0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MX-c-16" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round16/checks/c16.AC3.sh; echo "exit=$?"</invocation><expect>every news and sentiment_news_mood line reads unchanged (verdict_class, allowlist, firm, firm_resolution before and after) and the news channel keeps no artifacts -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~40/NFRA_MCPINDEX.TO-MX-c-16.certified-channel-corrections-in-the-emitter.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

1. Write the proof instance.
2. APPEND `<status>complete</status>` only if all three criteria PASS (if the commit gate refuses the flip, leave it and say so).
3. Commit your files together through `.tools/safe-commit.sh` (never `DATA_CATALOG.yaml`).
4. Report once, with:
   - the three changes by function or constant;
   - the AC2 DENOMINATOR line and the AC3 table, verbatim;
   - the unit-test count and your commit sha.

The issuer then merges, regenerates the catalog, runs the gateway suite by failing-ID delta and lands the catalog through the lane that owns the gateway folder.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round 16, worker ~40, parallel to `MX-c-17` (no shared file). Source: G3 contract `portfolios_legacy` (ft.04 re-rule, mp.15 gone), G6 (news sizes and markers), R14.6, and the CVO's pre-issue read `deliverables/3.0.0_SA_CVO~Z/R16_MX-c-16_PRE-ISSUE_READ_20261014.md` @2a8a025031 (READ-OK; its two conditions are `c16.AC2` and `c16.AC3`). Battery and planted arms: decomposition R16.3a. Base dry-runs 2026-10-15: AC1 FAIL, AC2 PASS, AC3 PASS, all as expected.

<status>issued</status>
<round>16</round>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
