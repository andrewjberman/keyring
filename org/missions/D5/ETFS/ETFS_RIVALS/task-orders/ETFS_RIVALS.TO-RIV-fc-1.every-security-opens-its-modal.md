# ETFS_RIVALS task order -- `RIV-fc-1` -- ROUND 8 WORKSTREAM C (ENRICHMENT): EVERY SECURITY NAMED ON THE PAGE OPENS ITS ONE MODAL, WITH ITS HISTORY OR A NOT-YET-BACKFILLED NOTE (FWD-21)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-fc-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~2</issued_to>
<issued_by>2.0.0_SA_COO~RV</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L6 (2026-10-04 ~21:1xZ, --drift) -- WITHIN BUDGET, 6 of 6 carriers scanned (C1=29 C2=32 C3=12 C4=21 C5=334 C6=1); 1 gate armed, not on this project; the notifier moratorium binds.
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell
comp-adversary: DECLARED-NOT-APPLICABLE the validator-context composer profiles RETURNED work for the L8/L9 packet; at the cut nothing is returned, and the issuer's evidence context is this order's check files
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric site-z) -- *rivalfunds*: daily holdings of rival active ETFs in two peer groups (IDVZ, PFOE), each fund's trade schedule, the A1 rankings, buying trend, input census and AI accounts, and a served page grouped by Opal fund (13 funds, package `data/etfs/scripts/rivalfunds/`, five AWS stage Lambdas, a terminal-machine Bloomberg leg the vehicle runs from the CLOUD working tree). **Round 8, workstream C** (Andrew-direct 2026-10-05 ~03:3xZ; PRD v0.16 @646ce7f4b8, FWD-21): every security named on the page opens its one modal, and the modal shows its history or says it is not yet backfilled. Nothing in round 8 deploys, merges or flips a gate from a worker. Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-fc-1` -- every security named on the page opens its one modal (FWD-21)
- Measured at the rn-1 build: only the YTD rankings and the trend open a holding dialog (`render._name_button`, one dialog
  per fund x holding, `_holding_dialogs`); the trade log, the R30/QTD rankings and the AI text name securities as plain text.
  The served page is 1.89 MB of the gateway's 2,097,152 B cap.
- Issuer ruling at the cut: ONE dialog per security page-wide, keyed by its security key and reused by every mention, so the
  page grows by one dialog per distinct security, never per mention or per fund.
- Interface: every security mention in the rankings tables, the trend tables, the trade log and the AI text is a
  `<button data-sec="<key>" popovertarget="<id>">`; each target is exactly one element carrying `data-sec-dialog="<key>"`;
  a security with no history rows reads "History not yet backfilled" (`data-history="none"`); no script.
- **Organic trigger:** the 07:00 ET marker publish and the 09:00 ET sweep publish; the page must stay under DIALOG_SOFT_CAP
  with every dialog, or fall back as today.

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base branch wk-ETFS_RIVALS-2 at the amended rn-1 build 280b8dc66a)

- AMENDMENT (2026-10-05 ~04:4xZ, issuer): your first build (cb67f943a6, 57f7403405) is on your branch and passes AC1. Its
  own report named the gap AC2 now closes: a display name written exactly as the page spells it in AI prose stays plain
  text. Link every whole-word occurrence of a `_NAMES` display name in the AI text; keep `.rf-cite` keys as text.
- The check files' docstrings are the exact interface they read: read `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round8/checks/fc-1.AC1.py` and `fc-1.AC2.py` before you build. On
  this branch it reads FAIL 3 at the start (control OK).
- Andrew, verbatim (2026-10-05): "anytime a stock/ticker is mentioned, it should be clickable to the modal, and we should be
  able to see backfill on it."
- The modal's content today: contribution by period with rank, the year's net buying, the labelled months (CRO~RV layout,
  `_holding_dialogs`). Merge the per-fund content into the one security dialog (a section per fund that holds it). History
  rows for a security (its price and holdings history) arrive with the backfill routed to 1.0.0_SA_CTO (the ETFClassifier
  ingest); until a history table exists in the page context, every dialog reads "History not yet backfilled".
- Keep every inherited check passing on this branch: an-1.AC1, rw-1.AC1..AC3, rn-1.AC1..AC3 (all under `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round8/checks/`).
- Size: the holding dialogs are the page's largest part; keep `DIALOG_SOFT_CAP` and its fallback. Report the fixture page's
  bytes before and after.

## 3. SURFACES AND BOUNDS

You READ (never edit): `lib/`, `integrations/bloomberg/` (the Positioning pull is under an Andrew-direct no-modify order), the package's other modules and tests, `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round8/checks/` and the earlier rounds' `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round{5,6,7}/checks/`, the PRD `org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md` (v0.16 @646ce7f4b8), the decomposition `org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md` (round 8, its WORKSTREAM C section), and live S3 READ-ONLY where a check reads it.

You WRITE only the `<paths>` below (plus `deliverables/0.9.0_WK_ETFS_RIVALS~2/`). NEVER: any S3 write, any deploy, any Bloomberg or OpenAI call (stub every vendor hook in tests), the vehicle, any environment gate flip outside a test, any file another round-8 chain owns. Tests go beside the code as `tests/test_r8fc1_*.py`, run with `python -m pytest <file> -q` from `data/etfs/scripts/`; run the whole package suite before you report (it must read 0 failed). A check you cannot satisfy without leaving your `<paths>` is a surprise row in the investigation file (`surfaced_at` = `date -u +%FT%TZ` at filing), never an edit outside them.

<paths>
data/etfs/scripts/rivalfunds/render.py
data/etfs/scripts/rivalfunds/tests/test_r8fc1_*.py
data/etfs/scripts/rivalfunds/tests/test_crorv_layout.py
data/etfs/scripts/rivalfunds/tests/test_r6ui2_ranking_panels.py
data/etfs/scripts/rivalfunds/tests/test_r6ui3_trend_card.py
data/etfs/scripts/rivalfunds/tests/test_r6ui4_ai_account_cards.py
data/etfs/scripts/rivalfunds/tests/test_r6ui5_census_and_audit_trail.py
data/etfs/scripts/rivalfunds/tests/test_p2_page_grouped_by_fund.py
data/etfs/scripts/rivalfunds/tests/test_r7rd1_page_walk_remainder.py
data/etfs/scripts/rivalfunds/tests/test_r8rw1_render_remainder.py
data/etfs/scripts/rivalfunds/tests/test_r8an1_ai_prose_one_name.py
data/etfs/scripts/rivalfunds/tests/test_r8rn1_period_switch.py
data/etfs/scripts/rivalfunds/tests/test_g83_cash_equiv_trades.py
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- every security mention in rankings, trend, trade log and AI text is a data-sec button opening its one page-wide dialog; no dialog key repeats; a security without history reads 'History not yet backfilled'; no script (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round8/checks/fc-1.AC1.py`)
- **AC2** -- the AI text links a security it names by the page's own display name ("Apple Inc"), not only by its key; a bare part of a name ("Inc") is not linked (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round8/checks/fc-1.AC2.py`)
- **J1** (JUDGMENT, graded by 3.0.0_SA_CVO~RV at L9 on the served page) -- on the served page after the deploy, clicking any security name anywhere opens its modal, and the page loads within the gateway cap; positive control: the served 2026-10-02 page (trade-log and AI names are plain text)

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-fc-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round8/checks/fc-1.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="AC2" cell_refs="RIV-fc-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round8/checks/fc-1.AC2.py</invocation><expect>AC2 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="J1" cell_refs="RIV-fc-1" judgment="true"/>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~2/ETFS_RIVALS.TO-RIV-fc-1.every-security-opens-its-modal.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-fc-1.every-security-opens-its-modal`. Report once: each mechanical criterion's verdict line with the output above it; each judgment criterion left UNVERIFIABLE-BY-INSTRUMENT for the CVO; files written; any existing test assertion changed and why; rows filed (id + one line). Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** Andrew-direct ~03:3xZ 2026-10-05 (record cooRV_ANDREW_DIRECT_20261005_03xxZ_RIVALFUNDS_BENCHMARKS_CLICKABLE_TICKERS_ETFCLASSIFIER_BACKFILL.md @41158af7f9, item 2), PRD v0.16 @646ce7f4b8 FWD-21 (CTO~Z msg 29442); decomposition round 8 WORKSTREAM C section. Chain `~2`, slot `~2`, position 4 of 4. Checks dry-run at base branch wk-ETFS_RIVALS-2 at the amended rn-1 build 280b8dc66a: fc-1.AC1 FAIL (3; control OK) at the rn-1 build 280b8dc66a, as expected. Bounds: no merge before the 2026-10-05 07:00 ET vehicle pull; no deploy before the 13:30Z grades.

**AMENDMENT 1 (2026-10-05 ~04:4xZ, issuer):** AC2 added (AI prose names by display name link too), from the first build's own reported gap. Dry-run at the first fc-1 build 57f7403405: AC2 FAIL 1 (control OK). Graded by: to-pipeline-gate on a modified order reads only GATE (viii) <placeholders> (NONE).

<risk>SERVED</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<round>8</round>
<workstream>C</workstream>
<slot>~2</slot>
<fabric>site-z</fabric>
