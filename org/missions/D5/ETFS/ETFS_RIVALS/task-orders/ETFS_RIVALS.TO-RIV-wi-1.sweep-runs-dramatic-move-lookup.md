# ETFS_RIVALS task order -- `RIV-wi-1` -- WORKSTREAM 3: THE 13:00Z SWEEP RUNS THE DRAMATIC-MOVE LOOKUP BEFORE PUBLISH

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-wi-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~32</issued_to>
<issued_by>2.0.0_SA_COO~V1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule, cron or trigger is added or moved by this cell
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell; no S3 or deploy act
comp-adversary: DECLARED-NOT-APPLICABLE the validator-context composer profiles RETURNED work; at the cut nothing is returned, and the evidence context is this order's two check files (dry-run at the base: FAIL as expected)
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric dell1) -- *rivalfunds*: a daily research page on rival active ETFs (13 funds, two
peer groups): rankings, buying trend, AI accounts, a security dialog per holding with a price chart, and an audit page.
Code: `data/etfs/scripts/rivalfunds/` (run from `data/etfs/scripts`, package `rivalfunds`); tests:
`data/etfs/scripts/rivalfunds/tests/` (pytest from `data/etfs/scripts`).

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-wi-1` -- the 13:00Z sweep runs the dramatic-move lookup before publish, so a split found on the web adjusts the served history (row D1-S10; CTO ruling ADDENDUM 6) -- APPENDED 2026-10-09, revision 1.26
- Placement: `ledger/CTO_RULING_WORKSTREAM2_SPLIT_ADJUST_TRADE_LIST_SCOPE_20261009.md` ADDENDUM 6 @04214e638c
  (1.0.0_SA_CTO~DELL1 msg 2508). Its own cell and its own deploy pair; WS2/WS3 ship first.
- Measured (row D1-S10 @0d4f7cc409): no Lambda calls `dramatic_move`; no Lambda carries `BRIGHT_DATA_API_KEY`;
  `rivalfunds_package.STAGED` (7 paths) does not stage `data/find/dualbiz/scripts/serp.py`, and `serp_search` finds it
  only at the repository layout (`pathlib.Path(__file__).resolve().parents[4]`). `price_series._actions` READS gold
  `corporate_actions`; `dramatic_move.write_rows` is its only writer. Andrew-direct comment 1: "there should be a google
  search for corporate action and an automatic refactoring of historical prices by the split multiple".
- Interface:
  1. `dramatic_move.run_for_day(day, sink, *, g4=None, actions=None, search=None, cap=MAX_LOOKUPS_PER_RUN, names=None)
     -> dict`. With `g4`/`actions` None it reads the stored closes (G4) and the stored corporate actions from `sink` for
     the 30 days before `day`; it runs `detect`, searches at most `cap` candidates (`lookup`), writes every find with
     `write_rows` (one object, source_url per row), and returns a report `{candidates, searched, calls, written, failed,
     capped, uri}`. It PRINTS one line naming the cap and the counts. A search that raises is counted in `failed` and the
     run goes on; `run_for_day` itself never raises for a search or write failure. A name with no discontinuity draws 0
     searches. `MAX_LOOKUPS_PER_RUN` is a module constant (8).
  2. `sweep.run_sweep` calls `dramatic_move.run_for_day(date, sink)` after the canonical / trade-schedule stages and
     before the day's publish, inside a `try` that records the failure and does not re-raise (a failed lookup never
     blocks publish; the price stays unadjusted and the chart's gap flag stays).
  3. The key: `serp_search` takes `BRIGHT_DATA_API_KEY` from the environment, else reads the Secrets Manager secret named
     by `RIVALFUNDS_SERP_SECRET` (one `GetSecretValue`, cached per process). With neither, the search raises (counted as
     failed by item 1).
  4. `infra/aws/lambda/etfs-pipeline/rivalfunds_package.py` `STAGED` stages `data/find/dualbiz/scripts/serp.py`, and
     `serp_search` finds it in a Lambda tree (a `_serp_dir()` that tries the staged destination first, then the
     repository layout).
- Out of bounds: Terraform, IAM, the Lambda environment and any deploy (the deploy pair's applier sets
  `RIVALFUNDS_SERP_SECRET` and the one-ARN read); `price_series.py`, `publish_page.py`, `render.py`,
  `enrichment_bloomberg.py`; no live search, no S3.
- Checks: `ws3_item8_prep/wi1_lookup_run_check.py` (AC1; base FAIL: run_for_day absent) and
  `ws3_item8_prep/wi1_wiring_check.py` (AC2; base FAIL 3). Acceptance (the pair's read, CTO ADDENDUM 6): Tokio Marine
  adjusted on the served page; a name with no discontinuity makes 0 calls.

### The workstream's guards (verbatim)

GUARDS on every cell: (1) no deploy and no served write before both round-28 J1 reads (tw-1 at the 2026-10-09 11:00Z
vehicle run, aw-1 at the 13:00Z sweep); (2) no edit to `data/etfs/scripts/rivalfunds/enrichment_bloomberg.py` (a cell that
finds it must, files a row and stops); (3) every deploy or served write goes under its own never-widen pair.

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base box/dell1)

- Read both checks before you build. Each FAILS at the base and is your target; do not edit them.
  `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~V1/ws3_item8_prep/wi1_lookup_run_check.py` calls
  `run_for_day` on a LocalSink with scripted closes and a scripted search (arms A-D);
  `.../ws3_item8_prep/wi1_wiring_check.py` reads `sweep.run_sweep` with `ast`, imports `rivalfunds_package.STAGED`, and
  reads `serp_search`'s path logic.
- `dramatic_move.py`: `detect(g4, actions)` (~105) yields candidates `{security_id, date, prior_date, prior_close, close,
  security_name?}`; `lookup(candidate, search, names)` (~265) returns ONE row or None; `serp_search(query)` (~299) imports
  `serp` from `parents[4]/data/find/dualbiz/scripts`; `write_rows(s, rows, day)` (~330) writes one object per call.
  Where G4 closes and stored corporate actions live: `price_series.py` (`_CA_PREFIX`, `_actions`, `load`) and
  `homes.py` -- read them, do not edit them.
- `sweep.py`: `run_sweep(date, sink, runners, *, mode="daily", markers=None)` (~147); the graph runs
  canonical -> coverage / trade-schedule -> publish-page; after the graph the sweep publishes the day's page when no
  publish-page marker exists. Put the lookup where its rows are stored before any publish of the day reads them.
- `infra/aws/lambda/etfs-pipeline/rivalfunds_package.py`: `STAGED` is `(source, destination)` pairs; a file copies to
  its destination under each Lambda's tree.

## 3. SURFACES AND BOUNDS

You READ (never edit): every file not in your `<paths>`, including `lib/`, `integrations/`, `price_series.py`,
`publish_page.py`, `render.py`, `enrichment_bloomberg.py`, Terraform, the decomposition and the PRD
`org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md`.

You WRITE only the `<paths>` below (plus `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~32/`).
NEVER: any S3 read or write outside a LocalSink or memory sink, any deploy, gateway release or Terraform, any vendor call
(Bloomberg, OpenAI, Bright Data or any live web search -- inject `search`), any Secrets Manager call (mock boto3 in a test),
any environment gate flip outside a test. A row you file goes in the investigation file below with id
`ETFS_RIVALS-D1-W32-S<k>`, `"fabric": "dell1"`.

<paths>
data/etfs/scripts/rivalfunds/dramatic_move.py
data/etfs/scripts/rivalfunds/sweep.py
infra/aws/lambda/etfs-pipeline/rivalfunds_package.py
data/etfs/scripts/rivalfunds/tests/
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.dell1.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- `run_for_day`: TKM searched and one row with its source_url; 0 searches for a flat name; the cap holds and
  prints; a failing search never raises and writes nothing.
- **AC2** -- the sweep calls it inside a non-raising `try`; serp.py is staged; `serp_search` finds it in a Lambda tree.
- **J1** -- the pair's read on the served page (Tokio Marine adjusted), not yours.

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-wi-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~V1/ws3_item8_prep/wi1_lookup_run_check.py</invocation><expect>WI1 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="AC2" cell_refs="RIV-wi-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~V1/ws3_item8_prep/wi1_wiring_check.py</invocation><expect>WI1 WIRING RESULT: PASS 0 failures</expect></criterion>
  <criterion id="J1" cell_refs="RIV-wi-1" judgment="true"/>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Run the rivalfunds suite (`python -m pytest -q rivalfunds/tests` from `data/etfs/scripts`) and report its final line.
Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~32/ETFS_RIVALS.TO-RIV-wi-1.sweep-runs-dramatic-move-lookup.proof_of_spec.json`
with `to_id` `ETFS_RIVALS.TO-RIV-wi-1.sweep-runs-dramatic-move-lookup`. Report once: AC1's and AC2's verdict lines with
the output above them; J1 left UNVERIFIABLE-BY-INSTRUMENT; files written; where in `run_sweep` the call sits and why
there; how `run_for_day` reads G4 and the stored actions (prefixes and date span); the environment variable and secret
contract the applier must set; the suite's final line; every existing test assertion changed and why; rows filed (id +
one line); anything the issuer must do at the merge. Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L6, 2.0.0_SA_COO~V1):** The production hookup of RIV-wb-1 (row D1-S10 @0d4f7cc409), placed by
1.0.0_SA_CTO~DELL1 ruling ADDENDUM 6 @04214e638c (msg 2508): its own cell and its own deploy pair (the secret read is one
ARN, a WORLD limb in that pair); WS2/WS3 ship first. Decomposition revision 1.26. Cell id and slot listed before naming
(0 hits for RIV-wi-1, slot ~32, workstream 3g). Checks dry-run at the base: wi1_lookup_run_check FAIL 1 (run_for_day
absent); wi1_wiring_check FAIL 3 ((a), (b), (c)). Disjoint write set from RIV-wh-1 (ai_accounts.py): two chains.

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>28</round>
<workstream>3g</workstream>
<slot>~32</slot>
<fabric>dell1</fabric>
