# ETFS_RIVALS task order -- `RIV-s-6` -- ROUND 5 (ENRICHMENT): THE G4 PRODUCER NEVER WRITES A CURRENT-VALUE PULL UNDER A PAST DATE (W3-S15)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-s-6</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~5</issued_to>
<issued_by>2.0.0_SA_COO~RV</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (2026-10-01 ~23:xxZ, --drift) -- no armed gate names rivalfunds/, issuer-site/etfs/, bloomberg/etfs/ or this cell's files; the notifier moratorium binds.
comp-iam: RUN at L5 -- no IAM change in this cell.
comp-adversary: RUN at L5 on the round-5 decomposition; declared on RIV-b-2 and RIV-l-1, not this cell.
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric site-z) -- *rivalfunds*: daily holdings of rival active ETFs in two peer groups (IDVZ, PFOE), each fund's trade schedule, and a served page grouped by Opal fund (13 funds, package `data/etfs/scripts/rivalfunds/`, five AWS stage Lambdas, a terminal-machine Bloomberg leg run by the vehicle from the CLOUD working tree). **Round 5** bounds G1, fixes three trade-inference method defects (CTO hop-9 rulings), makes the issuer floor per fund, and builds the v0.8 Bloomberg leg inert. Nothing in round 5 deploys. Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-s-6` -- the G4 as-of guard (W3-S15; ruling 4)

`enrichment_bloomberg`'s market pull never writes current values under a past partition.
- **Past date.** A date before the run date (ET) uses a historical request through a new hook `_blp_historical_data(securities,
  fields, start, end, ...)` (wrapping `integrations/bloomberg/mcp/blp_client.historical_data`). Its rows carry `as_of` = that date
  and `as_of_source` = `historical`.
- **No historical answer.** If the historical request answers nothing, nothing is written under the past date, and the result says
  so.
- **Run date.** A pull for the run date carries `as_of_source` = `pull`.

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base 9e201639c3)

- `enrichment_bloomberg._market_pull` (~388-425) uses the event `date` as the partition; the pull is a current-value
  `_blp_reference_data` (~250-254, ~404); `market_rows` (~280-294) stamps `"date": as_of, ..., "as_of": as_of` with as_of = the
  event date. The CLI default date is the previous trading day ET (~602-604), so the DAILY run is itself a past-date pull.
- No historical request exists in enrichment; `integrations/bloomberg/mcp/blp_client.historical_data(securities, fields,
  start_date, end_date, periodicity="DAILY", ...)` (~239-260) is the BDH equivalent. READ_HERE.md section 4: HistoricalDataRequest
  returns zero rows for DERIVED fields -- an empty historical answer must land nothing, never a current value.
- Consumer: G1 `_g4_for` (`gold_canonical_shape.py` ~614-642) takes the greatest G4 partition <= the report date.
- This file is ALSO run by the terminal vehicle from the CLOUD tree (the 08:03 enrichment step, Z-S10): the run-date pull must
  keep landing.

## 3. SURFACES AND BOUNDS

You READ (never edit): `lib/`, `integrations/bloomberg/` (the Positioning pull is under an Andrew-direct no-modify order), the package's other modules and tests, `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round{3,4,5}/checks/`, the CTO rulings `org/missions/D5/ETFS/ETFS_RIVALS/ledger/CTO_RULING_20261001_HOP9_METHOD_DEFECTS.md` and `org/missions/D5/ETFS/ETFS_RIVALS/ledger/ROUND_ANALYSIS.round4.md`, the device-local captures under `C:\Users\Opal Bloomberg\Desktop\ajb_workspace\.runtime\`, and live S3 READ-ONLY where a check reads it.

You WRITE only the `<paths>` below (plus `deliverables/0.9.0_WK_ETFS_RIVALS~5/`). NEVER: any S3 write, any deploy, any Bloomberg or OpenAI call (stub every vendor hook in tests), the vehicle, any file another round-5 cell owns. Tests go beside the code as `tests/test_r5s6_*.py`, run with `python -m pytest <file> -q` from `data/etfs/scripts/`; run the whole package suite before you report (it must read 0 failed).

<paths>
data/etfs/scripts/rivalfunds/enrichment_bloomberg.py
data/etfs/scripts/rivalfunds/tests/test_r5s6_*.py
data/etfs/scripts/rivalfunds/tests/test_s4_security_market.py
data/etfs/scripts/rivalfunds/tests/test_e1_enrichment_bloomberg.py
data/etfs/scripts/rivalfunds/tests/test_v2_enrichment_cli.py
data/etfs/scripts/rivalfunds/tests/test_v2_revision_contract.py
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

**AMENDMENT 1 (issuer ruling on rows Z-W5-S29 and Z-W5-S30 (ARMED), 2026-10-02).** (a) `tests/test_v2_revision_contract.py::test_new_g4_objects_are_named_with_their_capture_time` runs a past-date `market` pull against a current-value stub -- the behaviour this cell retires: pin `eb._run_date_et` to the test's own date there (as in test_s4 and test_e1); no assertion changes. (b) S30: the vehicle's daily G4 targets the PREVIOUS trading day, so under refuse-unless-historical it becomes a historical request, and READ_HERE section 4 says that answers nothing for derived fields (GICS among them) -- the daily G4, and the served G1 GICS that reads it, would stop. CTO ruling 4 reads 'refuses OR LABELS'. Ruling: for a past-date pull, a security whose historical answer covers EVERY requested field lands as historical (`as_of` the past date, `as_of_source` historical); every other security lands from the current-value pull LABELLED with its true as-of -- `as_of` the RUN date (ET), `as_of_source` pull -- under the requested partition, never claiming the past date. A failed historical request falls to the same labelled current pull (no historical answer at all). The run-date path is unchanged. AC1 is unchanged and still holds under this ruling (no row under the past date claims that date from a current-value pull). Append resolution rows for S29 and S30.

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- a past-date pull with no historical answer writes no row claiming that date; with one it lands rows as_of that date, as_of_source historical; control: the run-date pull lands, as_of_source pull (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round5/checks/s-6.AC1.py`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-s-6"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round5/checks/s-6.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~5/ETFS_RIVALS.TO-RIV-s-6.g4-as-of-guard.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-s-6.g4-as-of-guard`. Report once: each criterion's verdict line with the output above it; files written; any test assertion changed and why; rows filed (id + one line). Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** Round-4 analysis @6dcb0074e4 (msg 28075), decomposition round 5 v1.0. Checks dry-run
at base 9e201639c3: s-6.AC1 FAIL -- each FAIL as expected, each control PASS.

<risk>SERVED</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<round>5</round>
<slot>~5</slot>
<fabric>site-z</fabric>
