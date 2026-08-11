# 49F GOLD ANALYTICS RUNNER -- GROUP A SPEC (DIMENSIONS / REFERENCE / BOUNDARY)

**Author:** 3.0.0_SA_CVO · **2026-08-11 ~0730Z** · **archetype:** IMPLEMENT (design)
**Commission:** Andrew-direct @5e4b8dda98 ("design a spec for Group A, then B, then C, then D up to
the emitters, for 49 Financial"); sequential delivery, this is GROUP A, for CTO review.
**Governing law:** GIPS standard (the .rtf, requirements verbatim -- sections cited as sec-N) ·
pattern spec v1.0 @d272021791 (9 atoms + the 5-member exception set) · shape-transposition
doctrine @6e180df78e (this spec IS the shape inflection/cottonwood instantiate) ·
CRO-confirmed data layer @a876ee6ae9 + @5bb3b2626d · feasibility @e323c1cfac.
**Substrate census (live, 07:2xZ):** `opal-data-assets/schwab/08335338/silver/` = **20 tables**
(4 `dim_*` + 16 `fact_*`); existing partial runner corpus `data/assets/scripts/gold/runners_49f/`
(a00/a01 + c00-c04 + fit harness) = the quality-extraction input per instruction 4.

---

## 0. WHAT GROUP A IS, AND THE ONE RULE THAT ORDERS EVERYTHING

Group A is everything the standard requires to exist BEFORE a single transaction is classified or
a single value summed: **sec2 verbatim -- "The calculation boundary must be defined before any
transaction is classified."** Group A therefore owns: the account dimension, the
family/household dimension, the PERFORMANCE-PORTFOLIO BOUNDARY as a versioned artifact, the
security master, the calendar frame, the transaction-classification reference, and the identity
crosswalk. Group A produces NO analytics and NO valuations -- it produces the frame that makes
B/C/D deterministic. Every Group A output carries the pattern's provenance columns
(`source_pipeline`, `_ingested_at` -- atom 9) and lands under ONE product root (atom 1).

**Naming law, binding on every script here: COLUMNS ARE NAMED BY CONTENT, NEVER BY VENDOR LABEL**
(the 2a registry rule; measured cost: the map table's `account_id` column carries a SmartX UUID and
its `account_number` carries the Schwab digits -- three live specimens in one night, one of them
mine). Where a vendor field is passed through under a content-true name, the vendor's original
name rides in a `_src` suffix column comment, never as the serving name.

## 1. THE SEVEN GROUP A ARTIFACTS (script -> output contract)

Home (DECISION-FOR-REVIEW, stated in §3): `{PRODUCT_ROOT}/dimensions/{artifact}/date={D}/data.parquet`
+ `{PRODUCT_ROOT}/_manifests/{data-as-of}/{process-ts}.json` (atom 3).

| # | Script | Inputs (silver) | Output artifact | The contract, in one line |
|---|---|---|---|---|
| A_00 | `a00_dim_account.py` (EXTRACT from existing corpus -- survives instruction-4's partition) | `fact_acc` (95 cols, 7,239 accounts at date=2026-08-07) | `dim_account` | One row per account_id (10-digit, content-verified digit-rate 1.00): registration/type/status, open/close dates, custodian branch, managed-program fields -- sec2's identity bullet, passthrough-clean |
| A_01 | `a01_dim_relationship.py` (EXTRACT; absorb the fact_fam parse) | `fact_fam` (7,186 rows, positional: col_4 = 8-digit account -> zfill(10), col_1 = 19 grouping ids, col_5 = names -- feasibility cell 2) | `dim_relationship` | Account -> family/grouping map at HOUSEHOLD grain; the sec2 "parent, household, registration, subaccount relationships" surface; unlocks household composites (C-group consumes) |
| A_02 | `a02_dim_boundary.py` (NEW -- the spec's center) | `dim_account` + `dim_relationship` + `fact_trn` FRM-credit legs | **`dim_boundary` (VERSIONED)** | The performance-portfolio boundary: per account -- IN_CLIENT_BOOK / COLLECTION_ACCOUNT / EXCLUDED_OTHER + effective dates + `boundary_version` (content hash). Sec10's lineage field "portfolio-boundary version" is MINTED HERE and nowhere else |
| A_03 | `a03_dim_security.py` (NEW) | `fact_sec` (2,313 assets; 112 rate-bearing by `interest_rate` nonzero -- NEVER `maturity_date`, which is sentinel-populated on all rows) | `dim_security` | Stable security identifier (sec3): cusip/symbol/type, rate-bearing flag + accrual inputs (interest_rate, 1st_cpn_date, dividend_interest_frequency, next_pay_date) for Group B's cell-4 decision |
| A_04 | `a04_dim_calendar.py` (NEW, tiny) | the `dim_balance` partition tree (525 daily partitions 2024-07-08..2026-08-07, T-1) | `dim_calendar` | The partition tree IS the trading calendar (c00_runner's own proven convention); emits trading-day sequence + prev-day resolution + the gap census (feasibility's INFERRED-continuous cell becomes MEASURED here, once, for everyone) |
| A_05 | `a05_ref_txn_classification.py` (PROMOTE, not rebuild) | `SCHWAB_TRANSACTION_CODE_CLASSIFICATION_20260811.json` @a876ee6ae9 (187 code rows over 2,982,720 txns, full 525-partition universe) | `ref_txn_classification` (VERSIONED) | The classification table AS DATA in the product root (atom 6: config never lives in the code store -- partner_roster's violation, not repeated). First-match rule list; unknown codes fail LOUD to UNRESOLVED; TPFEE/SMFEE rows carry their VERIFIED grade @5bb3b2626d |
| A_06 | `a06_dim_identity_crosswalk.py` (NEW) | `smartx/platform/silver/fact_allocation_account_map` + `dim_account` | `dim_identity_crosswalk` | allocation_id -> schwab_account_number -> zfill(10) -> account_id; columns named BY CONTENT (`smartx_allocation_uuid`, `smartx_account_uuid`, `schwab_account_number`); the two-derivation lockstep PRECONDITION printed in the manifest (bronze-listing vs registry-filter universes -- coincidence, not construction); coverage denominators carried per run (99.86% feed->map / 99.65% end-to-end at spec time) |

## 2. THE BOUNDARY DIM (A_02) -- THE ONLY GENUINELY NEW DESIGN, SPECIFIED TIGHT

Sec2 requires, verbatim, before classification: account_id · parent/household/registration/
subaccount relationships · inception/opening/closing/termination dates · base currency ·
included sleeves · discretionary status · cash/sweep/money-market/settlement accounts ·
short/margin/derivative/liability accounts. Mapping to measured truth:

- **IN_CLIENT_BOOK** default for the 7,239-account universe (`fact_acc` roster).
- **COLLECTION_ACCOUNT** by the measured discriminator @5bb3b2626d: an account receiving
  TPFEE/MGFEE **FRM-{client} CREDIT legs** is an advisor/firm collection account, mechanically
  identified (38,187 FRM legs measured). One groupby, re-derived per run -- a PREDICATE, never a
  hand roster (the predicate-not-roster law).
- **EXCLUDED_OTHER** carries its reason enum (closed-before-window, non-discretionary if a
  discretionary flag emerges from fact_acc's 95 cols at build, boundary-ruled exclusions with the
  ruling cited). **Absence of a discretionary flag is recorded as ABSENT-with-shape** per
  @6e180df78e -- not guessed.
- **Cash/sweep/MM are INSIDE the boundary** (the standard's own rule; the 680K sweep rows are
  INTERNAL -- the classification table already encodes this).
- **`boundary_version`** = sha256 over the sorted (account_id, class, effective_from) set. Every
  downstream artifact that consumed a boundary STAMPS this version (sec10 lineage). A boundary
  CHANGE with an unchanged version is structurally impossible; a version change is a visible event.
- **Base currency: USD BY CONSTRUCTION** (zero FX columns across all 8 pulled tables --
  feasibility boundary). Documented as a constant in the dim's manifest, not a column.

## 3. DECISIONS-FOR-REVIEW (CTO adjudicates at this group's review; the spec proceeds on the stated default)

1. **PRODUCT ROOT.** Default per pattern atom 1: `opal-data-assets/portal/gold/advi/49financial/`
   (the advi product root does not exist yet -- this group MINTS it; `{scope}` = firm x advisor
   arrives with the D-group's advisor projections). The existing corpus writes
   `schwab/08335338/gold/` parallel-by-construction -- treated as the QA/dev vintage to PORT FROM
   (build-correct-then-port, no shadow: the old prefix gets a dated tombstone at cutover, never a
   parallel life). If CTO rules the vendor-tree home (`schwab/08335338/gold/`) canonical instead,
   only the table's Home line changes -- every contract survives.
2. **A_00/A_01 extraction depth.** Default: EXTRACT the existing a00/a01 (they are clean
   passthroughs with a fit harness) and re-home; rewrite only where a column name violates
   name-by-content.
3. **`dim_asset` vs `fact_sec` as the security-master source** -- one content diff at build
   decides; the contract (A_03) is source-agnostic.

## 4. WHAT GROUP A DOES NOT DO (boundaries, stated)

No valuations (B), no flow ledger or TWR (C), no serving (D). No schedule design here beyond the
atom-5 requirement that every leg WILL carry a clock floor -- the floor lands with the runner
wiring, not the dims. The existing c00-c04 corpus is NOT adjudicated here (it is B/C-group input).
Advisor-grain scope (`{scope}` = firm x advisor) is D-group's projection; Group A carries the
advisor ATTRIBUTION inputs (A_01/A_02) without projecting them. fact_slm/uln/ult/upn/upt/rl*/rt*
are deliberately untouched by Group A -- they are attribution/validation-family inputs (canonical
decision 4: validation inputs, never return inputs) and enter at C's validation battery.

## 5. ACCEPTANCE (per artifact, machine-checkable -- the TO decomposition inherits these)

- Row-count identity vs source (A_00: 7,239 == fact_acc distinct account_id on the same partition;
  denominators printed).
- A_02: collection-account set NONEMPTY and disjoint from IN_CLIENT_BOOK; boundary_version stable
  across two same-input runs (determinism control); a mutated input flips it (the mutant control).
- A_04: gap census printed with the trading-calendar frame (weekends/holidays are NOT gaps --
  the T-1 law); any true gap NAMED.
- A_05: every fact_trn code on the freshest partition resolves through the table or lands
  UNRESOLVED-LOUD (0 silent rows); the 187-row table's census key re-derives.
- A_06: coverage ratios printed with BOTH denominators (map-side and feed-side); the lockstep
  precondition line present in the manifest.
- Every artifact: provenance cols present; manifest written (atom 3); py gate + `from __future__
  import annotations` (Rule 15).

-- 3.0.0_SA_CVO
