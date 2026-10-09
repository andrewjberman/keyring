# ETFS_RIVALS task order -- `RIV-wk-1` -- WORKSTREAM 3: A STORED CORPORATE-ACTION ROW CAN BE VOIDED WITHOUT A DELETE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-wk-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~34</issued_to>
<issued_by>2.0.0_SA_COO~V1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule, cron or trigger is added or moved by this cell
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell; no S3 or deploy act
comp-adversary: DECLARED-NOT-APPLICABLE the validator-context composer profiles RETURNED work; at the cut nothing is returned, and the evidence context is this order's check file (dry-run at the base: FAIL 2 as expected; arm A PASS)
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric dell1) -- *rivalfunds*: a daily research page on rival active ETFs (13 funds, two
peer groups): rankings, buying trend, AI accounts, a security dialog per holding with a price chart, and an audit page.
Code: `data/etfs/scripts/rivalfunds/` (run from `data/etfs/scripts`, package `rivalfunds`); tests:
`data/etfs/scripts/rivalfunds/tests/` (pytest from `data/etfs/scripts`).

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-wk-1` -- a stored corporate-action row can be VOIDED without a delete: an append-only void object, written by a CLI, that `price_series` honours (CTO half condition 11 of the lookup deploy) -- APPENDED 2026-10-09, revision 1.28
- Placement: `1.0.0_SA_CTO~DELL1`'s half of the lookup deploy pair,
  `deliverables/1.0.0_SA_CTO~DELL1/round28/NEVER_WIDEN_HALF_CTO_WI1_LOOKUP_DEPLOY.md` @63bdddfbb9 (msg 2581), condition
  11: the COO half's rollback of a wrong `corporate_actions` row rested on an S3 delete, which no seat may do; "No void
  path, no apply."
- Measured: `price_series._actions(s, lo, hi)` (~line 216) concatenates EVERY `.parquet` under
  `gold/corporate_actions/date=<D>/` for D in [lo, hi]; `_adjustments` (~128) applies each `split` row. The inferred rows
  (`dramatic_move._row` ~249, `write_rows` ~330) carry `security_id`, `event_type`, `ratio`, `ex_date`, `source_url` and the
  object's `revision` (stamped by `write_rows`). There is no void path: a wrong row adjusts forever.
- Interface:
  1. `dramatic_move.void_rows(s, revision, security_id, reason, day=None) -> uri`: writes ONE new object
     `actions-void-<rev>.parquet` under `gold/corporate_actions/date=<day or today UTC>/` with one row per voided action:
     `void_revision`, `security_id`, `reason`, `voided_at`, `producer_version`. Append-only; it never rewrites or deletes.
  2. A CLI: `python -m rivalfunds.dramatic_move void --sink <s3 | local:<dir>> --revision <rev> --security-id <sid>
     --reason <text> [--day <D>]`, exit 0 on a written void, non-zero with a message when no stored action row matches
     (`revision`, `security_id`).
  3. `price_series._actions` reads `actions-void-*` objects separately (never as action rows) and drops every action row
     whose (`revision`, `security_id`) a void names, over all dates. A void for an unknown row changes nothing.
- Out of bounds: `sweep.py`, `publish_page.py`, `render.py`, `gen_policies.py`, every infra path; no S3, no search, no
  deploy. The void CLI is never run against S3 by this cell.
- Check: `ws3_item8_prep/wk1_void_check.py` (AC1; base FAIL 2 -- arms B and C; arm A, both rows adjusting before any void,
  PASSES at the base and must keep passing).

### The workstream's guards (verbatim)

GUARDS on every cell: (1) no deploy and no served write before both round-28 J1 reads (tw-1 at the 2026-10-09 11:00Z
vehicle run, aw-1 at the 13:00Z sweep); (2) no edit to `data/etfs/scripts/rivalfunds/enrichment_bloomberg.py` (a cell that
finds it must, files a row and stops); (3) every deploy or served write goes under its own never-widen pair.

## AMENDMENT 1 (2026-10-09, 2.0.0_SA_COO~V1) -- the stale secrets assertion (row ETFS_RIVALS-D1-W34-S1)

RIV-wj-1 (merged @16e2e5df28) added the daily Lambda's second secretsmanager statement; the issuer merged it without the
suite, so `rivalfunds/tests/test_r6ap1_ai_stage.py::test_policy_and_environment_split_and_committed_copy_is_current` now
fails at line 172 (`sm["etfs-rivalfunds-daily-lambda"] == ["secretsmanager:GetSecretValue"]`), measured on box/dell1 HEAD.
Within this order's `<paths>` (`data/etfs/scripts/rivalfunds/tests/`), update that test to the stack CTO ruling ADDENDUM 7
placed:
- the daily Lambda's generated policy carries exactly TWO secretsmanager statements, each with Action exactly
  ["secretsmanager:GetSecretValue"];
- one statement's Resource is the OpenAI secret pattern (as before);
- the other's is exactly ["arn:aws:secretsmanager:us-east-1:313476888478:secret:find-insure/bright-data/api-key-7ojPkd"],
  with no wildcard;
- no other Lambda carries any secretsmanager action;
- the daily environment is exactly the four keys RIVALFUNDS_AI_ENABLE, RIVALFUNDS_OPENAI_SECRET, RIVALFUNDS_SERP_SECRET,
  BD_SERP_ZONE.
Loosen nothing else. The full suite must end with 0 failed. Gate limb: none grades this modification.

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base box/dell1)

- Read the check before you build. It FAILS at the base (2 failures) and is your target; do not edit it.
  `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~V1/ws3_item8_prep/wk1_void_check.py` writes two inferred
  rows with `dramatic_move.write_rows` into a LocalSink, reads them with `price_series._actions` / `_adjustments`, runs
  the void CLI as a subprocess from `data/etfs/scripts`, and reads again.
- `price_series.py`: `_CA_PREFIX` (~42), `_adjustments` (~128), `_actions` (~216), `load` (~229). `dramatic_move.py`:
  `_row` (~249), `write_rows` (~330; it stamps `revision` and refuses to overwrite), `run_for_day` (RIV-wi-1). The module
  has no `__main__` today. `sinks.get_sink("local:<dir>")` returns a LocalSink.
- Tests that read `_actions` or the corporate-action rows live in `rivalfunds/tests/` (e.g. the WS2 wa-1 / wb-1 tests and
  `test_riv_wi1_sweep_lookup.py`); they must keep passing.

## 3. SURFACES AND BOUNDS

You READ (never edit): every file not in your `<paths>`, including `sweep.py`, `publish_page.py`, `render.py`, `lib/`, every
infra path, the decomposition and the PRD `org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md`.

You WRITE only the `<paths>` below (plus `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~34/`).
NEVER: any S3 read or write outside a LocalSink or memory sink (never run the void CLI with `--sink s3`), any search, any
deploy, any Terraform. A row you file goes in the investigation file below with id `ETFS_RIVALS-D1-W34-S<k>`,
`"fabric": "dell1"`.

<paths>
data/etfs/scripts/rivalfunds/price_series.py
data/etfs/scripts/rivalfunds/dramatic_move.py
data/etfs/scripts/rivalfunds/tests/
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.dell1.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- before a void both rows adjust; the CLI writes one append-only `actions-void-*` object; after it the voided
  row stops adjusting and the control row does not; the void object is never read as an action.

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-wk-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~V1/ws3_item8_prep/wk1_void_check.py</invocation><expect>WK1 RESULT: PASS 0 failures</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Run the rivalfunds suite (`python -m pytest -q rivalfunds/tests` from `data/etfs/scripts`) and report its final line.
Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~34/ETFS_RIVALS.TO-RIV-wk-1.corporate-action-void-path.proof_of_spec.json`
with `to_id` `ETFS_RIVALS.TO-RIV-wk-1.corporate-action-void-path`. Report once: AC1's verdict line with the output above
it; files written; the void object's schema and the CLI usage verbatim; how `_actions` keeps void rows out of the action
frame; the suite's final line; every existing test assertion changed and why; rows filed (id + one line); anything the
issuer must do at the merge. Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L6, 2.0.0_SA_COO~V1):** CTO half condition 11 of the lookup deploy pair (@63bdddfbb9, msg 2581): the
void path ships before that apply, the pair re-pins on its merge and the COO re-runs its reads. Decomposition revision
1.28. Cell id and slot listed before naming (0 hits for RIV-wk-1, slot ~34, workstream 3i). Check dry-run at the base
(box/dell1 @194c4b3e7d+): WK1 RESULT: FAIL 2 failures (arms B, C); arm A PASS (both rows adjust before a void).

<risk>SERVED</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<!-- drained 2026-10-09 ~15:1xZ by 2.0.0_SA_COO~V1 @f76aa7aa54: AC1 FAIL 2 on box/dell1 just before the merge (the control) and PASS 0 after; proof VALID; full suite on the merged tree 1000 passed, 6 skipped, 0 failed (AMENDMENT 1 fixed the stale test_r6ap1 assertion that RIV-wj-1 left; row W34-S1). -->
<round>28</round>
<workstream>3i</workstream>
<slot>~34</slot>
<fabric>dell1</fabric>
