# ETFS_RIVALS task order -- `RIV-m-2` -- ROUND 5 (ENRICHMENT): THE BLOOMBERG COLLECTOR'S CAPTURE DEDUP IS LINEAR (W5-S21)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-m-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~2</issued_to>
<issued_by>2.0.0_SA_COO~RV</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (2026-10-01 ~23:xxZ, --drift) -- no armed gate names rivalfunds/, issuer-site/etfs/, bloomberg/etfs/ or this cell's files; the notifier moratorium binds.
comp-iam: RUN at L5 -- no IAM change in this cell.
comp-adversary: RUN at L5 on the round-5 decomposition; declared on RIV-b-2 and RIV-l-1, not this cell.
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric site-z) -- *rivalfunds*: daily holdings of rival active ETFs in two peer groups (IDVZ, PFOE), each fund's trade schedule, and a served page grouped by Opal fund (13 funds, package `data/etfs/scripts/rivalfunds/`, five AWS stage Lambdas, a terminal-machine Bloomberg leg run by the vehicle from the CLOUD working tree). **Round 5** bounds G1, fixes three trade-inference method defects (CTO hop-9 rulings), makes the issuer floor per fund, and builds the v0.8 Bloomberg leg inert. Nothing in round 5 deploys. Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-m-2` -- the collector's capture dedup is linear (W5-S21; ruling 2)

`collector_bloomberg._existing_by_sha` re-lists and re-reads an acquisition partition's sidecars for every capture.
- Memoise the sidecar index per partition in the product sink for the run, or key the dedup on the sha, so a bulk import reads
  each sidecar a bounded number of times.
- `_issuer_has_bronze` (per issuer fund per day) gets the same memo.
- Idempotence across batch ids is unchanged.

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base 9e201639c3)

- `collector_bloomberg._existing_by_sha` (~139-145): `for u in s.list(bronze_prefix(acq) + "/")` and a `get` of every
  `.sidecar.json` until the sha matches -- called once per capture by `land_capture` (~157) from the import loop (~410-419) and the
  daily/backfill loop (~440-449); a bulk import in one acquisition partition does k sidecar GETs for the k-th capture (measured:
  60 captures -> 1830 GETs; 937 -> ~440,000, row W5-S21).
- `_issuer_has_bronze` (~241-254) lists all issuer bronze and GETs each sidecar, per (issuer_first fund, day) from `funds_for_day`.
- `sinks.get_sink` passes a sink object through, so a counting sink measures GETs.
- This file is ALSO run by the terminal vehicle from the CLOUD tree: behaviour must not change except the read count.

## 3. SURFACES AND BOUNDS

You READ (never edit): `lib/`, `integrations/bloomberg/` (the Positioning pull is under an Andrew-direct no-modify order), the package's other modules and tests, `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round{3,4,5}/checks/`, the CTO rulings `org/missions/D5/ETFS/ETFS_RIVALS/ledger/CTO_RULING_20261001_HOP9_METHOD_DEFECTS.md` and `org/missions/D5/ETFS/ETFS_RIVALS/ledger/ROUND_ANALYSIS.round4.md`, the device-local captures under `C:\Users\Opal Bloomberg\Desktop\ajb_workspace\.runtime\`, and live S3 READ-ONLY where a check reads it.

You WRITE only the `<paths>` below (plus `deliverables/0.9.0_WK_ETFS_RIVALS~2/`). NEVER: any S3 write, any deploy, any Bloomberg or OpenAI call (stub every vendor hook in tests), the vehicle, any file another round-5 cell owns. Tests go beside the code as `tests/test_r5m2_*.py`, run with `python -m pytest <file> -q` from `data/etfs/scripts/`; run the whole package suite before you report (it must read 0 failed).

<paths>
data/etfs/scripts/rivalfunds/collector_bloomberg.py
data/etfs/scripts/rivalfunds/tests/test_r5m2_*.py
data/etfs/scripts/rivalfunds/tests/test_b1_bloomberg_channel.py
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- a 60-capture bulk import reads <= 180 sidecars (today 1830); control: a re-import writes no new data object (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round5/checks/m-2.AC1.py`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-m-2"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round5/checks/m-2.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~2/ETFS_RIVALS.TO-RIV-m-2.collector-dedup-linear.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-m-2.collector-dedup-linear`. Report once: each criterion's verdict line with the output above it; files written; any test assertion changed and why; rows filed (id + one line). Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** Round-4 analysis @6dcb0074e4 (msg 28075), decomposition round 5 v1.0. Checks dry-run
at base 9e201639c3: m-2.AC1 FAIL -- each FAIL as expected, each control PASS.

<risk>SERVED</risk>
<worker_class>worker-light</worker_class>
<status>complete</status>
<round>5</round>
<slot>~2</slot>
<fabric>site-z</fabric>
