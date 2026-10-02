# ETFS_RIVALS task order -- `RIV-h-6` -- ROUND 5 (ENRICHMENT): KEY RESOLUTION IS ITS OWN G5 COLUMN, OUT OF THE CONFIDENCE PRECEDENCE (HOP-9 d)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-h-6</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~3</issued_to>
<issued_by>2.0.0_SA_COO~RV</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (2026-10-01 ~23:xxZ, --drift) -- no armed gate names rivalfunds/, issuer-site/etfs/, bloomberg/etfs/ or this cell's files; the notifier moratorium binds.
comp-iam: RUN at L5 -- no IAM change in this cell.
comp-adversary: RUN at L5 on the round-5 decomposition; declared on RIV-b-2 and RIV-l-1, not this cell.
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric site-z) -- *rivalfunds*: daily holdings of rival active ETFs in two peer groups (IDVZ, PFOE), each fund's trade schedule, and a served page grouped by Opal fund (13 funds, package `data/etfs/scripts/rivalfunds/`, five AWS stage Lambdas, a terminal-machine Bloomberg leg run by the vehicle from the CLOUD working tree). **Round 5** bounds G1, fixes three trade-inference method defects (CTO hop-9 rulings), makes the issuer floor per fund, and builds the v0.8 Bloomberg leg inert. Nothing in round 5 deploys. Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-h-6` -- key resolution is its own G5 column (hop-9 ruling d; after h-5 on `~3`)

- **New column.** G5 gains `key_resolution` in {`RESOLVED`, `ALIAS`, `UNRESOLVED`}. ALIAS is a resolved key whose G1
  `resolution_method` is `issuer-alias`.
- **Confidence.** `confidence` grades the inference only (flow factor, event cleaning, price band). It is no longer overridden by
  `UNRESOLVED`.
- **Additive.** `key_resolved` is still written.

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base 9e201639c3)

- G5 schema `gold_trade_schedule.py` ~147-162. `label()` ~467-473 -> `security_key_kind`, `key_resolved` (~483);
  `_resolved = resolution_status == "RESOLVED"` (~264).
- `conf()` ~498-505: CORP-ACTION, then `if not resolved: return "UNRESOLVED"`, then STALE-WIDENED, then FLOW-WINDOW/CLEAN -- so an
  unresolved key hides the inference grade.
- ALIAS is invisible today: G1 alias rows are `resolution_status` RESOLVED with `resolution_method` `issuer-alias`
  (`gold_canonical_shape.py` ~274-278); G5 never reads `resolution_method`.
- The page reads `key_resolved` (`render.py` ~104-107) -- render is RIV-f-4's; keep `key_resolved` written.

## 3. SURFACES AND BOUNDS

You READ (never edit): `lib/`, `integrations/bloomberg/` (the Positioning pull is under an Andrew-direct no-modify order), the package's other modules and tests, `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round{3,4,5}/checks/`, the CTO rulings `org/missions/D5/ETFS/ETFS_RIVALS/ledger/CTO_RULING_20261001_HOP9_METHOD_DEFECTS.md` and `org/missions/D5/ETFS/ETFS_RIVALS/ledger/ROUND_ANALYSIS.round4.md`, the device-local captures under `C:\Users\Opal Bloomberg\Desktop\ajb_workspace\.runtime\`, and live S3 READ-ONLY where a check reads it.

You WRITE only the `<paths>` below (plus `deliverables/0.9.0_WK_ETFS_RIVALS~3/`). NEVER: any S3 write, any deploy, any Bloomberg or OpenAI call (stub every vendor hook in tests), the vehicle, any file another round-5 cell owns. Tests go beside the code as `tests/test_r5h6_*.py`, run with `python -m pytest <file> -q` from `data/etfs/scripts/`; run the whole package suite before you report (it must read 0 failed).

<paths>
data/etfs/scripts/rivalfunds/gold_trade_schedule.py
data/etfs/scripts/rivalfunds/tests/test_r5h6_*.py
data/etfs/scripts/rivalfunds/tests/test_g2_trade_schedule.py
data/etfs/scripts/rivalfunds/tests/test_i1_trade_stable_key.py
data/etfs/scripts/rivalfunds/tests/test_r5h4_id_change_identifier_relation.py
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- unresolved key: confidence FLOW-WINDOW and key_resolution UNRESOLVED; resolved -> RESOLVED, issuer-alias -> ALIAS; control: key_resolved still written (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round5/checks/h-6.AC1.py`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-h-6"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round5/checks/h-6.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~3/ETFS_RIVALS.TO-RIV-h-6.key-resolution-column.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-h-6.key-resolution-column`. Report once: each criterion's verdict line with the output above it; files written; any test assertion changed and why; rows filed (id + one line). Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** Round-4 analysis @6dcb0074e4 (msg 28075), decomposition round 5 v1.0. Checks dry-run
at base 9e201639c3: h-6.AC1 FAIL -- each FAIL as expected, each control PASS.

<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<status>pending</status>
<!-- AMENDMENT 1 (issuer, 2026-10-02 ~02:5xZ, row Z-W3-S18): <paths> gains tests/test_r5h4_id_change_identifier_relation.py; those 4 tests assert the retired UNRESOLVED confidence. -->
<round>5</round>
<slot>~3</slot>
<fabric>site-z</fabric>
