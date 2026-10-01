# ETFS_RIVALS task order -- `RIV-g-6` -- ROUND 3 (ENRICHMENT): `canonical_shape` JOINS G4 -- GICS, AND SUB_ASSET_CLASS IS THE SECTOR

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-g-6</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~1</issued_to>
<issued_by>2.0.0_SA_COO~RV</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (2026-10-01 ~06:4xZ, --drift) -- 2 armed gates fabric-wide, none names rivalfunds/.
comp-iam: RUN at L5 -- no IAM change; the canonical-shape Lambda's read of gold/security_market/ is measured by RIV-d-4 before the deploy.
comp-adversary: RUN at L5 on the round-3 decomposition (3 of 3 cited commits verified); declared on RIV-i-1, not this cell.
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric site-z) -- *rivalfunds*. The master holdings table (G1 `canonical_shape`) must carry, per
position, Opal's classification and the GICS hierarchy as separate fields (C-SHAPES). RIV-s-4 built G4 (`security_market`) and RIV-i-1
gave positions their keys; **this cell joins them.** It follows RIV-i-1 on your slot; your worktree has CLOUD (with s-4 and i-1)
merged in first. Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-g-6` -- `canonical_shape` joins G4: GICS, and sub_asset_class IS the GICS sector for equities (C-SHAPES v0.7)

For each non-cash G1 row with a `security_id` present in the newest G4 dated on or before the report date: `gics_sector`,
`gics_industry_group` (+ codes), and `gics_industry`/`gics_sub_industry` where G4 has them; `gics_status = RESOLVED`, `gics_source`
naming the G4 revision. For an equity row with `gics_status = RESOLVED`, `sub_asset_class = gics_sector` and
`sub_asset_class_status = RESOLVED` (the ratified vocabulary, `etf_positioning_gold.SUB_ASSET_CLASS_VOCAB`). A row outside G4 stays
UNRESOLVED; a finer GICS level never stands in for a sub-asset class.

## 1b. ISSUER AMENDMENT 1 (2026-10-01 ~08:1xZ, 2.0.0_SA_COO~RV) -- repair your row W1-S22 first (the suite must be green)

The drain of RIV-i-1 read the package suite at 225 passed / 2 FAILED. Two RIV-hp-1 tests in `tests/test_hp1_home_producer.py`
(`test_an_unreadable_producer_file_raises_and_is_never_guessed`, `test_g1_fails_loud_when_the_producer_address_is_unreadable`)
assert the runtime read of `etf_constituents_pull.py` that i-1's amendment removed. Both files are granted to you:
- **`tests/test_hp1_home_producer.py`:** delete those two tests. The drift test in `tests/test_i1_home_producer_address.py` now
  carries the guarantee they guarded.
- **`gold_holdings_coverage.py`:** fix the stale comment near line 448 that still names `ProducerAddressError`. Comment only;
  no behaviour change.
- Then `python -m pytest data/etfs/scripts/rivalfunds/tests -q` must read 0 failed. Say so in your report, and record the
  repair as row W1-S22's resolution.

## 2. THE CONTRACT (PRD v0.7 C-SHAPES, the amended line, verbatim)

"**A finer GICS level (industry group, industry, sub-industry) never stands in for a sub-asset class; for an equity row the
`sub_asset_class` IS its GICS sector, per the ratified vocabulary (`etf_positioning_gold.py` `SUB_ASSET_CLASS_VOCAB`), both fields
carried and agreeing by construction** (v0.7, CTO ruling on row ETFS_RIVALS-Z-S1, round-2 analysis ruling 5) ... A value that cannot
be resolved is carried with a status, never guessed."

## 3. WHAT YOU NEED TO KNOW (measured at the cut, base 78167bb8fc)

- G1 already has the columns: `asset_class`, `asset_class_status`, `sub_asset_class`, `sub_asset_class_status`,
  `classification_source`, `gics_sector`, `gics_sector_code`, `gics_industry_group`, `gics_industry_group_code`, `gics_industry`,
  `gics_industry_code`, `gics_sub_industry`, `gics_sub_industry_code`, `gics_status`, `gics_source` (all NULL / UNRESOLVED today;
  `NO_GICS_SOURCE` is the current classification_source). Equity rows get `asset_class` from `epg.classify(False, None)`.
- G4 is at `address('rivalfunds','etfs','gold','security_market','date=<D>','market-<rev>.parquet')` with `security_id`,
  `gics_sector`, `gics_industry_group`, `gics_industry_group_code`, `gics_industry`, `gics_industry_code`, `gics_sub_industry`,
  `gics_sub_industry_code`, `revision`, `as_of` (RIV-s-4's output; read its module after the merge).
- Overlap measured at the cut: of the 2026-09-28 holdings, BASG 13/36, WCMG 5/49, TSEL 15/29, ETFT 14/30, PCLG 19/30 ids are in the
  Positioning `bbg/2026-09-28/characteristics.parquet` (the G4 import the check uses) -- 66 rows.
- `etf_positioning_gold.py` (READ ONLY; G1 loads it by path, see `gold_canonical_shape.py` ~line 127) defines the vocabulary.

## 4. SURFACES AND BOUNDS

You READ (never edit): `data/etfs/scripts/gold/etf_positioning_gold.py`, `enrichment_bloomberg.py`, `identity.py`, the package's
other modules, `lib/`, `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round{1,2,3}/checks/`, live S3 READ-ONLY for
`bbg/<D>/characteristics.parquet`, the device-local captures under `C:\Users\Opal Bloomberg\Desktop\ajb_workspace\.runtime\`.

You WRITE only the `<paths>` below (plus `deliverables/0.9.0_WK_ETFS_RIVALS~1/`). NEVER: any S3 write, any deploy, any Bloomberg or
OpenAI call, any file another round-3 cell owns. Tests: `tests/test_g6_*.py`.

<paths>
data/etfs/scripts/rivalfunds/gold_canonical_shape.py
data/etfs/scripts/rivalfunds/tests/test_g6_*.py
data/etfs/scripts/rivalfunds/tests/test_g1_canonical_shape.py
data/etfs/scripts/rivalfunds/tests/test_hp1_home_producer.py
data/etfs/scripts/rivalfunds/gold_holdings_coverage.py
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

## 5. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- with G4 imported from the real characteristics file, at least 40 G1 rows carry G4's GICS (RESOLVED, sourced to the G4
  revision); every resolved equity row's sub_asset_class equals its sector; no finer level stands in; rows outside G4 stay
  UNRESOLVED (`.../round3/checks/g-6.AC1.py`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-g-6"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round3/checks/g-6.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>
</proof_of_spec>

## 6. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~1/ETFS_RIVALS.TO-RIV-g-6.canonical-shape-gics-join.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-g-6.canonical-shape-gics-join`. Report once: the verdict line with the output above it; files written; rows filed. Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** Round-2 analysis item 5 / ruling 5 (G1 half). Depends on RIV-s-4 (G4) and RIV-i-1 (keys);
handed to slot ~1 after both merge. Check dry-run at base 78167bb8fc: g-6.AC1 FAIL (G4 imported 0 rows) -- FAIL as expected.

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<completion_note>2026-10-01 drain by 2.0.0_SA_COO~RV: worker 0.9.0_WK_ETFS_RIVALS~1 @16f0e97741 (builds 0dce4474db S22 repair, b789e6ae5a G4 join); proof instance VALID; g-6.AC1 PASS (66 rows keyed into G4, all GICS RESOLVED and sourced, sub_asset_class == sector on 66/66, 102 outside G4 UNRESOLVED); package 241 passed 2 skipped 0 failed; rows W1-S24 (S22 resolved), W1-S25 (revision letter-suffix ordering, carried to round 4's revision contract W1-S11).</completion_note>
<round>3</round>
<slot>~1</slot>
<fabric>site-z</fabric>
