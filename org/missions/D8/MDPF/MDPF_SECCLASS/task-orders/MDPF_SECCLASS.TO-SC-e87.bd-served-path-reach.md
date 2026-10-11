# TO MDPF_SECCLASS.TO-SC-e87 -- round 20 SC-e-87: BD's three served classify sites reach the ticker-no-row NAME:: fallback

<to_id>MDPF_SECCLASS.TO-SC-e87</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~77</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>20</round>
<workstream>~M1</workstream>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `SC-e-87` (`decompositions/MDPF_SECCLASS_DECOMP_R20.md`) |
**outcome_ref:** FWD-1 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`SC-e-87`, row MDPF_SECCLASS-D1-S26. Round 16 (SC-e-79) taught the shared lib
`data/black_diamond/scripts/gold/lib/etf_classifier.py` `ETFClassifier.classify_with_identity(ticker, asset_name, cusip)` to resolve a
position whose ticker is non-blank but has NO row by its `NAME::` row (identity hop `ticker-no-row-name-key`). The lib is served and does
that when called. But Black Diamond's three SERVED classify sites call `classify_with_identity` ONLY for a BLANK ticker, so for a
ticker-no-row position the branch never runs, and the 23 such securities ($966,285) still serve `unclassified`:

| site | file and function | today |
|---|---|---|
| D_04 | `data/black_diamond/scripts/gold/D_04.client_portal_summary.py` `_classify_with_canonical(ticker, name, classifier, cusip='')` (:146-175) | `classifier.classify(t, n)`; on a miss, `classify_with_identity('', n, c)` only `if not t.strip()`; otherwise cash-keyword or `unclassified` |
| C_06 | `data/black_diamond/scripts/gold/C_06.client_mix_timeseries.py` `classify_series(ticker_series, name_series)` (:201-265) | `classifier.classify(ticker, name)`; on a miss, `classify_with_identity('', name)` only when the ticker is blank |
| D_03 | `data/black_diamond/scripts/gold/D_03.composition_artifacts.py` `classify_series(ticker_series, name_series, cusip_series=None)` -> inner `_classify` (:119-166) | same shape; `classify_with_identity('', asset_name, cusip)` only when blank |

**Build (one change per site, nothing else):** where `classify()` returns no class and the ticker is NON-BLANK, call
`classifier.classify_with_identity(ticker, name, cusip)` and, if it returns a class, serve that class and sub-class with
`class_source` `'etf-classifications'` exactly as the blank-ticker branch already does. Keep, unchanged at every site:
1. a ticker that has a row (the ticker's row is never overridden);
2. a blank ticker (today's path);
3. a position with no ticker row and no `NAME::` row stays `unclassified` (the cash-keyword rule still decides `cash`);
4. C_06 passes no CUSIP today; pass none (its blank-ticker call has none); D_03 and D_04 pass the cusip they already hold.

Read `classify_with_identity` (`lib/etf_classifier.py:207-250`) first: for a non-blank ticker it already does the whole job, so each
site needs only to call it.

**Tests.** Add `data/black_diamond/scripts/gold/tests/test_served_path_reach_r20.py` (new file). With the table client stubbed (see
`tests/test_etf_classifier_name_key.py` for the stub shape) it drives each site's own function with a ticker-no-row position that has a
`NAME::` row, and asserts the class returned, plus the three kept behaviours above. No AWS call in the tests.

**The half request (the ship's carrier).** Write
`org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_BD_SERVED_PATH_REACH_20261011.md`, shaped
like `NEVER_WIDEN_HALF_REQUEST_SECCLASS_BD_NAME_TICKER_FALLBACK_20261009.md` in that folder (`## The act`, `## Blast radius`,
`## Rollback per key`). It must name:
- **the act:** deploy ONLY the three files `data/black_diamond/scripts/gold/D_04.client_portal_summary.py`,
  `data/black_diamond/scripts/gold/C_06.client_mix_timeseries.py` and `data/black_diamond/scripts/gold/D_03.composition_artifacts.py`
  to `s3://opal-data-bd/code/gold/`, with `bash .tools/safe-deploy.sh <the three paths>` (the deploy core ships only named files);
- **the blast radius:** the securities that move. Take the 23 ticker-no-row securities in
  `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/D1W66S3_TICKER_NO_ROW_LIST_20261009.json` (the 23 rows are under its
  `entries` key; read one first to see its fields). For each, call the NEW site code (D_04's `_classify_with_canonical`) against the LIVE `etf-classifications` table with
  `get_item` only, and print ticker, dollars, class from the table row (NAME:: row) and the class the new code returns; list by name any
  that stay `unclassified` and why (no NAME:: row). Print the totals: moved count and dollars, staying count and dollars;
- **both branches of the expected outcome**, read from the code you wrote: a ticker-no-row security WITH a NAME:: row moves from
  `unclassified` to that row's class; one WITHOUT stays `unclassified` and is listed by name;
- **the writers of the served `platinum/firm/mix_summary.json`:** count them with the Grep tool over `data/black_diamond/scripts/` and
  print N and each file:line;
- **the rollback per key:** the current served VersionId and ETag of each of the three keys, read with
  `bash .tools/aws s3api head-object --bucket opal-data-bd --key code/gold/<file>` (read-only).
Leave both halves (COO and CTO) unsigned.

### ACCEPTANCE

<criterion id="SC20-e87-AC1" cell_refs="SC-e-87"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R20_CHECKS/sc_r20_served_reach.py D_04</invocation><expect>SERVED-REACH site=D_04 ok=True</expect></criterion>
`SC20-e87-AC1` -- D_04's own served classify function places a ticker-no-row position through its NAME:: row; three controls hold.
<criterion id="SC20-e87-AC2" cell_refs="SC-e-87"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R20_CHECKS/sc_r20_served_reach.py C_06</invocation><expect>SERVED-REACH site=C_06 ok=True</expect></criterion>
`SC20-e87-AC2` -- C_06's own served classify function does the same.
<criterion id="SC20-e87-AC3" cell_refs="SC-e-87"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R20_CHECKS/sc_r20_served_reach.py D_03</invocation><expect>SERVED-REACH site=D_03 ok=True</expect></criterion>
`SC20-e87-AC3` -- D_03's own served classify function does the same.
<criterion id="SC20-e87-AC4" cell_refs="SC-e-87"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R20_CHECKS/r20_half_ready.py org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_BD_SERVED_PATH_REACH_20261011.md</invocation><expect>HALF-READY</expect></criterion>
`SC20-e87-AC4` -- the half request carries the act, the blast radius and the rollback per key. (A fourth criterion, with its reason: the
half request is the ship's only carrier and is the cell's deliverable beyond the three site checks.)

<expected_criteria>SC20-e87-AC1,SC20-e87-AC2,SC20-e87-AC3,SC20-e87-AC4</expected_criteria>

Dry-run at the base (dell1 box/dell1, 2026-10-11 ~03:3xZ):
- SC20-e87-AC1: FAIL, as expected (`SERVED-REACH site=D_04 ok=False target=('unclassified', '', '', 'unclassified') controls=3/3`).
- SC20-e87-AC2: FAIL, as expected (same, site=C_06).
- SC20-e87-AC3: FAIL, as expected (same, site=D_03).
- SC20-e87-AC4: FAIL, as expected (the half request is absent).

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`,
  uncommitted.
- **No package install and no download of any kind** (no pip, npm, bun add, bun install, curl or tool fetch, into any environment).
- **AWS is READ-ONLY** (get, list, head, scan, DynamoDB get_item): no write to any table or bucket, no deploy, no invoke, no model call.
  Never push. The deploy is NOT part of this cell.
- **Never edit** `lib/etf_classifier.py`, `.tools/`, or any test other than the new file. The BD gold suite must stay green.
- **Client data stays out.** The 23-security list is security-level (ticker, name, dollars). Print no relationship id, account id or
  client name anywhere in the half request or the tests.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and file a surprise row (id
  `MDPF_SECCLASS-D1-W77-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing). Do not weaken any test.

<paths>
data/black_diamond/scripts/gold/D_04.client_portal_summary.py
data/black_diamond/scripts/gold/C_06.client_mix_timeseries.py
data/black_diamond/scripts/gold/D_03.composition_artifacts.py
data/black_diamond/scripts/gold/tests/test_served_path_reach_r20.py
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_BD_SERVED_PATH_REACH_20261011.md
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R20.md</decomp_doc> (round 20), cell `SC-e-87`.
<owned_cells>SC-e-87</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC20-e87-AC1, SC20-e87-AC2, SC20-e87-AC3, SC20-e87-AC4. Write the instance at
`org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~77/MDPF_SECCLASS.TO-SC-e87.bd-served-path-reach.proof_of_spec.json`.
Validate it BEFORE the flip with `python .tools/proof-of-spec-check.py <instance> SC20-e87-AC1,SC20-e87-AC2,SC20-e87-AC3,SC20-e87-AC4`.
</proof_of_spec>

**REPORT:** what you read and changed (file:line per site), each criterion's output, the half request's moved/staying totals, commits, rows.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE the deploy is a later pair-gated act by a CloudOps lane, outside a BD gold run; this cell ships no key.
comp-iam: DECLARED-NOT-APPLICABLE no grant change (read-only get_item and head-object under the seat's role).
comp-adversary: RUN -- a ticker with a row overridden (control 1); a blank-ticker position moved off its identity chain (control 3); a function-level test standing in for the served function (round 16's AC1 did exactly that and passed while the served bytes did not move; AC1-3 drive each site's own function); a fourth call site missed (the half request's blast radius reads the three named sites; a grep for other classify_with_identity callers is the worker's census)
lane: the <paths> block IS the grant.
</preflight>

Source: CTO round-19 analysis section 3 item 1 (msg 3419); row D1-S26; DECOMP_R20.
