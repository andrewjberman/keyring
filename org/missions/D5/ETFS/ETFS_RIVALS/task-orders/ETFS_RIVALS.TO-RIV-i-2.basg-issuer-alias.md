# ETFS_RIVALS task order -- `RIV-i-2` -- ROUND 4 (ENRICHMENT): BASG'S ISSUER-ONLY DATES RESOLVE THROUGH A MEASURED ALIAS (W4-S2)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-i-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~1</issued_to>
<issued_by>2.0.0_SA_COO~RV</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (2026-10-01 ~12:xxZ, --drift) -- no armed gate names rivalfunds/, issuer-site/etfs/, bloomberg/etfs/ or this cell's files; the notifier moratorium binds.
comp-iam: RUN at L5 -- no IAM change in this cell.
comp-adversary: RUN at L5 on the round-4 decomposition; declared on RIV-v-2, not this cell.
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric site-z) -- *rivalfunds*: daily holdings of rival active ETFs in two peer groups (IDVZ, PFOE), each fund's trade schedule, and a served page grouped by Opal fund. Rounds 1-3 built the live pipeline (package `data/etfs/scripts/rivalfunds/`, five AWS stage Lambdas, a terminal-machine Bloomberg leg); the 2026-10-01 page serves 12 of 13 funds. **Round 4** fixes the daily trade pairing, unifies 'newest', grades identity per source and adds GQGU. Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-i-2` -- BASG's issuer-only report dates resolve through a measured alias (row W4-S2; ruling 3)

`identity.py` and `gold_canonical_shape.py`: a CUSIP joined to a Bloomberg key on an earlier co-held date (RIV-i-1's join) keeps
that key on a later issuer-only date:
- `resolution_method = 'issuer-alias'`, with the date the alias was measured in `resolution_note`;
- the latest such join wins;
- a CUSIP never joined stays UNRESOLVED;
- a same-day join outranks an alias.

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base 48ec92238a)

- `identity.issuer_join` (RIV-i-1) joins an issuer row to its fund's Bloomberg row at the same report date (or the nearest
  within 1 trading day) by root ticker + shares within 2%. BASG's Bloomberg captures end 2026-09-28 (the PFOE census); the daily
  Bloomberg request excludes BASG (issuer_first), so 2026-09-29/30 resolve 0 of 33 (row W4-S2), 2026-09-28 resolves 34 of 34.
- The alias must come from MEASURED joins already in G1 history (or recomputed from silver), never from appending a suffix.

## 3. SURFACES AND BOUNDS

You READ (never edit): `lib/`, `integrations/bloomberg/` (the Positioning pull is under an Andrew-direct no-modify order), the package's other modules, `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round{1,2,3,4}/checks/`, the device-local captures under `C:\Users\Opal Bloomberg\Desktop\ajb_workspace\.runtime\`, and live S3 READ-ONLY where a check mirrors it.

You WRITE only the `<paths>` below (plus `deliverables/0.9.0_WK_ETFS_RIVALS~1/`). NEVER: any S3 write, any deploy, any Bloomberg or OpenAI call, the vehicle, any file another round-4 cell owns. Tests go beside the code as `tests/test_i2_*.py`, run with `python -m pytest <file> -q` from `data/etfs/scripts/`; the issuer runs the whole suite at the drain.

<paths>
data/etfs/scripts/rivalfunds/identity.py
data/etfs/scripts/rivalfunds/gold_canonical_shape.py
data/etfs/scripts/rivalfunds/tests/test_i2_*.py
data/etfs/scripts/rivalfunds/tests/test_i1_*.py
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- over the REAL 2026-09-28/30 inputs BASG resolves >= 90% on 2026-09-30, each key equal to its CUSIP's 2026-09-28 key; 2026-09-28 stays >= 95% (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round4/checks/i-2.AC1.py`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-i-2"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round4/checks/i-2.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~1/ETFS_RIVALS.TO-RIV-i-2.basg-issuer-alias.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-i-2.basg-issuer-alias`. Report once: each criterion's verdict line with the output above it; files written; any test assertion changed and why; rows filed (id + one line). Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** Round-3 analysis @d4a1e22801 (msg 27810), decomposition round 4 v1.0. Checks dry-run
at base 48ec92238a: i-2.AC1 FAIL -- each FAIL as expected.

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>staged</status>
<round>4</round>
<slot>~1</slot>
<fabric>site-z</fabric>
