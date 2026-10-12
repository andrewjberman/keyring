# ETFS_RIVALS task order -- `RIV-xd-1` -- A MOVE THE LOOKUP FINDS IS ADJUSTED ON THE PAGE OF THE SAME DAY (OFFLINE RENDER OF A PLANTED DISCONTINUITY)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-xd-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~35</issued_to>
<issued_by>2.0.0_SA_COO~V1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule, cron or trigger is added or moved by this cell
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell; no S3 or deploy act
comp-adversary: DECLARED-NOT-APPLICABLE the validator-context composer profiles RETURNED work; at the cut nothing is returned, and the evidence context is this order's check file(s) (dry-run at the base: FAIL as expected)
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric dell1) -- *rivalfunds*: a daily research page on rival active ETFs (13 funds, two
peer groups): rankings, buying trend, AI accounts, a security dialog per holding with a price chart, and an audit page.
Code: `data/etfs/scripts/rivalfunds/` (run from `data/etfs/scripts`, package `rivalfunds`); tests:
`data/etfs/scripts/rivalfunds/tests/` (pytest from `data/etfs/scripts`).

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-xd-1` -- a move the lookup finds is adjusted on the page of the SAME day, shown by an offline render of a planted discontinuity (round 28 analysis section 2.8) -- APPENDED 2026-10-12, revision 1.29
- Placement: `ledger/ROUND_ANALYSIS.round28.md` section 2.8 and section 3 item 5 (msg 4558); CVO ADDENDUM 12 (row D1-C-S13).
- Measured (this seat, `WI1_SCRATCH_WALK_20261012.md` and the dry-run of the check below): `sweep.run_dag` calls
  `dramatic_move.run_for_day(day, sink)` with `day` = the page day; `run_for_day` writes the find with `write_rows(s, rows,
  day)`, so the object lands in `gold/corporate_actions/date=<page day>/`; but the page's charts read the series with
  `price_series.load(s, keys, lo, asof)` where `asof = gold_holding_contribution.as_of(day)` (the previous trading day), and
  `_actions` reads only partitions `lo <= date <= asof`. A find on page day D is therefore invisible to page D's chart and
  appears one trading day late. Measured: the same row read with a window ending 2026-10-07 gives `adjustment == []`, ending
  2026-10-12 gives the INFERRED split.
- Interface: `dramatic_move.run_for_day` writes with the partition day `gold_holding_contribution.as_of(day)` instead of
  `day` (`uri = write_rows(s, rows, <as_of(day)>)`); every other behaviour is unchanged: the candidate window (30 days up to
  `day`, which includes that partition), the report, the printed line, the idempotence (a second run reads the stored row
  and searches nothing). Where an existing test pins the partition date of a lookup row, change that assertion to the
  as-of date and say so in the report.
- Out of bounds: `price_series.py`, `publish_page.py`, `render.py`, `sweep.py`, `write_rows`'s own signature, `void_rows`,
  everything the retry cell (RIV-xb-1) changes in `serp_search` (it lands first, on the same file: yours is the one call
  site); no S3, no live search.
- Checks: `round29/checks/xd1_planted_render_check.py` (AC1 and AC2; base FAIL 2, its control PASSES at the base and must
  keep passing). The organic case (no name with a discontinuity) is the negative arm, read when it occurs.

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base box/dell1)

- Read the check before you build: `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~V1/round29/checks/xd1_planted_render_check.py`. At the base: AC1 and AC2 FAIL (the find is written
  and not read), its control PASSES. It is your target; do not edit it. It plants closes in a LocalSink, runs
  `dramatic_move.run_for_day` with an injected search, then reads the series (`price_series.load`, the call
  `publish_page._build_charts` makes) and the published `charts/TXUE.json`.
- `run_for_day` (about line 470) ends with `uri = write_rows(s, rows, day)`; `write_rows(s, rows, day, revision=None)` puts
  the object under `gold/corporate_actions/date=<day>/`. The page's charts read partitions up to `as_of(day)` only:
  `from . import gold_holding_contribution as hc; hc.as_of(day)` is the previous trading day.
- Run RIV-xb-1's change first: you inherit it in the same worktree (the issuer continues you). Do not touch `serp_search`.
- Existing tests that read a lookup row's partition: `tests/test_ws2_wb1_dramatic_move.py`, `tests/test_riv_wi1_sweep_lookup.py`:
  change only an assertion the new partition falsifies and name it in the report.
## 3. SURFACES AND BOUNDS

You READ (never edit): every file not in your `<paths>`, including `lib/`, `integrations/`, Terraform, the decomposition and
the PRD `org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md`.

You WRITE only the `<paths>` below (plus `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~35/`).
NEVER: any S3 read or write outside a LocalSink or memory sink, any deploy, gateway release or Terraform, any vendor call
(Bloomberg, OpenAI, Bright Data or any live web search -- inject `search` or the client), any Secrets Manager call, any
environment gate flip outside a test. A row you file goes in the investigation file below with id
`ETFS_RIVALS-D1-W35-S<k>`, `"fabric": "dell1"`.

<paths>
data/etfs/scripts/rivalfunds/dramatic_move.py
data/etfs/scripts/rivalfunds/tests/test_riv_xd1_same_page_find.py
data/etfs/scripts/rivalfunds/tests/test_ws2_wb1_dramatic_move.py
data/etfs/scripts/rivalfunds/tests/test_riv_wi1_sweep_lookup.py
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.dell1.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from the repository root)

- **AC1** -- the series the page's chart reads carries the INFERRED split on the page day it was found, continuous against its
  gapped control, and a second run searches nothing; the published chart object carries it too.
- **AC2** -- the existing lookup tests green after you correct only the assertions the partition falsifies.
<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-xd-1"><invocation>cd data/etfs/scripts; python -m pytest -q -p no:cacheprovider ../../../org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~V1/round29/checks/xd1_planted_render_check.py</invocation><expect>3 passed</expect></criterion>
  <criterion id="AC2" cell_refs="RIV-xd-1"><invocation>cd data/etfs/scripts; python -m pytest -q -p no:cacheprovider rivalfunds/tests/test_ws2_wb1_dramatic_move.py rivalfunds/tests/test_riv_wi1_sweep_lookup.py</invocation><expect>all passed, 0 failed</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Run the rivalfunds suite (`python -m pytest -q rivalfunds/tests` from `data/etfs/scripts`) and report its final line.
Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~35/ETFS_RIVALS.TO-RIV-xd-1.planted-render-same-page-find.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-xd-1.planted-render-same-page-find`. Report once: each criterion's verdict line with the output above it;
files written; every existing test assertion you changed and why; rows filed (id + one line); anything the issuer must do at
the merge. Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L6, 2.0.0_SA_COO~V1):** Round 29 of ETFS_RIVALS, ONE issuance on `ledger/ROUND_ANALYSIS.round28.md` section 3
(msg 4558). Decomposition revision 1.29. Check file(s) dry-run at the base before the cut. Chain A, second order (slot ~35, after RIV-xb-1 on the same file).

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<!-- drained 2026-10-12 by 2.0.0_SA_COO~V1 @afb5fa2ba6: AC1 3 passed (control gap passes at base), AC2 30 passed, instance VALID; suite 1032 passed, 6 skipped after the merge. The fix is write_rows(s, rows, hc.as_of(day)) in run_for_day (_partition_day). -->
<round>29</round>
<workstream>4</workstream>
<slot>~35</slot>
<fabric>dell1</fabric>
