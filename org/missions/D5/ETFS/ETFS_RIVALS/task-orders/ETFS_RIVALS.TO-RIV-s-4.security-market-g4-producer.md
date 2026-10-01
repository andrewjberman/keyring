# ETFS_RIVALS task order -- `RIV-s-4` -- ROUND 3 (ENRICHMENT): G4 `security_market` -- THE PRODUCER (GICS, PRICE, CURRENCY)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-s-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~3</issued_to>
<issued_by>2.0.0_SA_COO~RV</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (2026-10-01 ~06:4xZ, --drift) -- 2 armed gates fabric-wide, none names rivalfunds/ or bbg/<D>/characteristics; the Positioning pull is under an Andrew-direct no-modify order (read only). The vendor gate binds: no Bloomberg call by this worker (the Terminal is signed out).
comp-iam: RUN at L5 -- no IAM change in this cell; G4 is written by the terminal machine's identity, measured by RIV-d-4 with the IAM simulator before the first landing.
comp-adversary: RUN at L5 on the round-3 decomposition (3 of 3 cited commits verified); declared on RIV-i-1, not this cell.
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric site-z) -- *rivalfunds*: rival active ETFs in two peer groups, each fund's trade schedule,
and a served page. The master holdings table (G1) must carry Opal's classification AND the GICS hierarchy (C-SHAPES); its source is
G4 `security_market`, which does not exist yet. **This cell builds G4's producer.** Work ONLY in the worktree your spawn line names;
every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-s-4` -- G4 `security_market`: the producer (C-GOLD-MODEL G4; scripted Bloomberg, R-21)

`enrichment_bloomberg.py` gains three modes, all writing G4 at
`address('rivalfunds','etfs','gold','security_market','date=<D>','market-<revision>.parquet')` (never-overwrite; stage
`pull-enrichment`):
- **`plan-market`** -- offline (no session): the distinct non-cash Bloomberg securities of G1 at `date`, and the field list
  (GICS_SECTOR_NAME, GICS_INDUSTRY_GROUP_NAME, GICS_INDUSTRY_GROUP, GICS_INDUSTRY_NAME, GICS_INDUSTRY, GICS_SUB_INDUSTRY_NAME,
  GICS_SUB_INDUSTRY, PX_LAST, CRNCY, DAY_TO_DAY_TOT_RETURN_GROSS_DVDS);
- **`market`** -- the live scripted reference pull of that plan through `integrations/bloomberg/mcp/blp_client.py`; wired into
  `daily` mode after the dividends pull so the enabled vehicle leg runs it (no vehicle edit);
- **`import-market`** -- reads a Positioning `characteristics.parquet` as QA-class input (provenance `import:bbg/<D>/characteristics.parquet`).

G4 columns: `security_id` (the key grammar of `security_bloomberg`), `security_bloomberg`, `date`, `px_close`, `total_return_index`,
`currency`, `gics_sector`, `gics_industry_group`, `gics_industry_group_code`, `gics_industry`, `gics_industry_code`,
`gics_sub_industry`, `gics_sub_industry_code`, `source`, `as_of`, plus the C-GOLD-MODEL columns (`revision`, `produced_at`,
`producer_version`, `input_manifest`, `claim` = MEASURED). A field the response lacks is NULL, never guessed.

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base 78167bb8fc)

- **The key grammar:** spaces -> underscores, e.g. `'AAPL US Equity'` -> `'AAPL_US_Equity'` (the crosswalk's canonical key,
  `lib/research/identity/crosswalk.py` docstring: `<ROOT>_<CC>_Equity`). G1 rows carry the Bloomberg id in `security_bloomberg` (or,
  for a Bloomberg-sourced row whose crosswalk lookup missed, as `position_id`'s part before any `:<n>` suffix); `is_cash_line` marks
  cash. Use non-cash rows only.
- **The real fixture:** `s3://opal-data-etfs/bbg/2026-09-29/characteristics.parquet`, 172 rows, columns `security`, `NAME`,
  `GICS_SECTOR_NAME`, `GICS_INDUSTRY_GROUP_NAME`, `GICS_INDUSTRY_GROUP` (a float 4-digit code, e.g. 4520.0), `CNTRY_OF_DOMICILE`,
  `EQY_DVD_YLD_IND_NET`, `BETA_ADJ_OVERRIDABLE`, `CUR_MKT_CAP`, and fund-level fields; 164 of 172 carry a sector. It has NO price,
  industry or sub-industry: those are NULL in an imported G4 row. It is the Positioning pull's (`etf_daily_pull.py`, READ ONLY) --
  its field list there (~line 248) is the proven request shape for a per-security reference pull.
- **Existing modes** in `enrichment_bloomberg.py`: `daily`, `import` (dividends.json -> G3), `plan`; the G3 writer and marker
  pattern (`markers.write_marker`, stage `pull-enrichment`) is yours to reuse. `blp_client.py` is the shared client (READ ONLY).
- **No Bloomberg call by you:** the Terminal is signed out. The `market` mode is built and unit-tested with a stubbed client; its
  first live run is RIV-d-4's or the vehicle leg's.

## 3. SURFACES AND BOUNDS

You READ (never edit): `integrations/bloomberg/` (all of it), `lib/`, the package's other modules,
`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round{1,2,3}/checks/`, live S3 READ-ONLY for
`bbg/<D>/characteristics.parquet`, the device-local captures under `C:\Users\Opal Bloomberg\Desktop\ajb_workspace\.runtime\`.

You WRITE only the `<paths>` below (plus `deliverables/0.9.0_WK_ETFS_RIVALS~3/`). NEVER: any S3 write, any deploy, any Bloomberg or
OpenAI call, the vehicle `scheduled_daily_pull.cmd`, `gold_canonical_shape.py` (RIV-g-6 joins G4 into G1), any file another round-3
cell owns. Tests: `tests/test_s4_*.py`.

<paths>
data/etfs/scripts/rivalfunds/enrichment_bloomberg.py
data/etfs/scripts/rivalfunds/tests/test_s4_*.py
data/etfs/scripts/rivalfunds/tests/test_e1_enrichment_bloomberg.py
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- `import-market` over the real characteristics file writes G4: one row per input security, the key grammar, GICS sector
  and industry group (with the 4-digit code) on exactly the rows that carry them, the C-GOLD-MODEL columns, claim MEASURED
  (`.../round3/checks/s-4.AC1.py`)
- **AC2** -- `plan-market` over real G1 returns exactly G1's non-cash Bloomberg securities and the field list with the four GICS
  names, PX_LAST and CRNCY, without a session (`.../round3/checks/s-4.AC2.py`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-s-4"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round3/checks/s-4.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>

  <criterion id="AC2" cell_refs="RIV-s-4"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round3/checks/s-4.AC2.py</invocation><expect>AC2 RESULT: PASS 0 failures</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~3/ETFS_RIVALS.TO-RIV-s-4.security-market-g4-producer.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-s-4.security-market-g4-producer`. Report once: each verdict line with the output above it; files written; rows filed. Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** Round-2 analysis item 5 / ruling 5 (G4 half). Checks dry-run at base 78167bb8fc: s-4.AC1 FAIL
(G4 0 rows vs 172), s-4.AC2 FAIL (plan 0 vs 406 G1 non-cash; fields absent) -- each FAIL as expected.

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>3</round>
<slot>~3</slot>
<fabric>site-z</fabric>
