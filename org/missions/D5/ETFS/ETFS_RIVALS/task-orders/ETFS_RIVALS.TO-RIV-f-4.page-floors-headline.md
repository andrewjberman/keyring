# ETFS_RIVALS task order -- `RIV-f-4` -- ROUND 5 (ENRICHMENT): THE PAGE CELL: PER-FUND ISSUER FLOORS, THE HEADLINE, REFUSED AND KEY-RESOLUTION DISPLAYS

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-f-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~4</issued_to>
<issued_by>2.0.0_SA_COO~RV</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (2026-10-01 ~23:xxZ, --drift) -- no armed gate names rivalfunds/, issuer-site/etfs/, bloomberg/etfs/ or this cell's files; the notifier moratorium binds.
comp-iam: RUN at L5 -- no IAM change in this cell.
comp-adversary: RUN at L5 on the round-5 decomposition; declared on RIV-b-2 and RIV-l-1, not this cell.
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric site-z) -- *rivalfunds*: daily holdings of rival active ETFs in two peer groups (IDVZ, PFOE), each fund's trade schedule, and a served page grouped by Opal fund (13 funds, package `data/etfs/scripts/rivalfunds/`, five AWS stage Lambdas, a terminal-machine Bloomberg leg run by the vehicle from the CLOUD working tree). **Round 5** bounds G1, fixes three trade-inference method defects (CTO hop-9 rulings), makes the issuer floor per fund, and builds the v0.8 Bloomberg leg inert. Nothing in round 5 deploys. Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-f-4` -- the page cell: per-fund issuer floors, the headline, the REFUSED and key-resolution displays (rulings 3, 7; b and d's page halves)

**Per-fund issuer floors.** `guardrails.resolved_floor()` accepts per-fund entries under `issuer` (`{"issuer": {"BASG": x, "GQGU":
y}}`, like `home_funds`).
- An issuer fund the table does not name is held to the strictest issuer floor, and the reason names it.
- The shipped config is not changed by this cell.

**Headline.** The manifest's top-level `status` means "page published".
- The headline states "`<n>` of `<m>` funds current", from the manifest's counts.
- It names each lagging fund with its reason.
- Failed figures still never publish (FWD-9).

**REFUSED windows.** A G6 row whose `status` is REFUSED renders as "not inferred" with its reason, never as an empty window.

**Key resolution.** Where G5 carries `key_resolution`, the page shows it where it showed UNRESOLVED.

**Column-optional.** Every column read here is optional.

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base 9e201639c3)

- `guardrails.resolved_floor` (~187-202): a dict value -> `home_funds[fund]` only for `home_producer`; else `float(v[source])`
  -- a per-fund dict under `issuer` crashes there today; an unknown source gets the strictest floor. `identity_coverage` (~205-229).
  Shipped config: issuer 0.23 (set by GQGU 0.2368), so BASG (1.0) is held to 0.23 (row Z-S13).
- Page status: `publish_page` ~484-549: `agg = guardrails.rollup(...)`; manifest `"status": "not-updated" if agg_failed else
  "published"` -- one stale fund flips the whole page word. Headline `render.py` ~354-357 ("`<n>` of `<m>` funds updated");
  per-fund banner ~267; status table ~341.
- The round-5 G6 columns `status`/`reason` (RIV-h-5) and the G5 column `key_resolution` (RIV-h-6) are built concurrently on
  another slot: read both as OPTIONAL columns (present -> render; absent -> today's page).
- Test fixtures to reuse: `tests/test_p2_page_grouped_by_fund.py` (`_put`, `_book`, `_ev`, `_g6_row`, `_block`),
  `tests/test_f3_identity_floors.py` (`_reports`).

## 3. SURFACES AND BOUNDS

You READ (never edit): `lib/`, `integrations/bloomberg/` (the Positioning pull is under an Andrew-direct no-modify order), the package's other modules and tests, `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round{3,4,5}/checks/`, the CTO rulings `org/missions/D5/ETFS/ETFS_RIVALS/ledger/CTO_RULING_20261001_HOP9_METHOD_DEFECTS.md` and `org/missions/D5/ETFS/ETFS_RIVALS/ledger/ROUND_ANALYSIS.round4.md`, the device-local captures under `C:\Users\Opal Bloomberg\Desktop\ajb_workspace\.runtime\`, and live S3 READ-ONLY where a check reads it.

You WRITE only the `<paths>` below (plus `deliverables/0.9.0_WK_ETFS_RIVALS~4/`). NEVER: any S3 write, any deploy, any Bloomberg or OpenAI call (stub every vendor hook in tests), the vehicle, any file another round-5 cell owns. Tests go beside the code as `tests/test_r5f4_*.py`, run with `python -m pytest <file> -q` from `data/etfs/scripts/`; run the whole package suite before you report (it must read 0 failed).

<paths>
data/etfs/scripts/rivalfunds/guardrails.py
data/etfs/scripts/rivalfunds/publish_page.py
data/etfs/scripts/rivalfunds/render.py
data/etfs/scripts/rivalfunds/tests/test_r5f4_*.py
data/etfs/scripts/rivalfunds/tests/test_p1_page_and_guardrails.py
data/etfs/scripts/rivalfunds/tests/test_p2_page_grouped_by_fund.py
data/etfs/scripts/rivalfunds/tests/test_f3_identity_floors.py
data/etfs/scripts/rivalfunds/tests/test_r3_repairs.py
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- with one planted lagging fund the manifest reads `published` and the headline states '<n> of <m> funds current' naming the laggard with its reason (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round5/checks/f-4.AC1.py`)
- **AC2** -- per-fund issuer floors: BASG 0.5 FAILs its 0.95, GQGU 0.3 PASSes its 0.23, an unnamed issuer fund takes the strictest; control bloomberg as before (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round5/checks/f-4.AC2.py`)
- **AC3** -- a planted G6 row of status REFUSED renders 'not inferred' with its reason; control: a fund without one does not (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round5/checks/f-4.AC3.py`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-f-4"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round5/checks/f-4.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>

  <criterion id="AC2" cell_refs="RIV-f-4"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round5/checks/f-4.AC2.py</invocation><expect>AC2 RESULT: PASS 0 failures</expect></criterion>

  <criterion id="AC3" cell_refs="RIV-f-4"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round5/checks/f-4.AC3.py</invocation><expect>AC3 RESULT: PASS 0 failures</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~4/ETFS_RIVALS.TO-RIV-f-4.page-floors-headline.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-f-4.page-floors-headline`. Report once: each criterion's verdict line with the output above it; files written; any test assertion changed and why; rows filed (id + one line). Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** Round-4 analysis @6dcb0074e4 (msg 28075), decomposition round 5 v1.0. Checks dry-run
at base 9e201639c3: f-4.AC1 FAIL, f-4.AC2 FAIL, f-4.AC3 FAIL -- each FAIL as expected, each control PASS.

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>5</round>
<slot>~4</slot>
<fabric>site-z</fabric>
