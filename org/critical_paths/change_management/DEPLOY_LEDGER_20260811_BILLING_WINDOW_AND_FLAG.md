# DEPLOY LEDGER — billing WINDOW FIX + the coupled FLAG ACT — 2026-08-11

**Owner:** 0.4.0_DS_ClientPlatform~A (both halves re-homed: CTO 165818Z grant, COO 165850Z)
**Authorization:** joint CTO+COO window ruling (b) RAW portfolio-domain currentValue ·
Andrew-direct lineage ("get the fix deployed" + instruction #2 "fix the is_fee_earning flag
derivation too when the window fix lands") · base stand-off ACKed 160005Z (build_billing_dim)
+ extended to the window file (COO 165850Z).

## LEG 1 — WINDOW FIX: **CLOSED 2026-08-11 ~1712Z, deploy verified**

- Commit: window fix on `build_billing_dim.py` (~A author line; ending_mv := roster
  currentValue; window-semantics atom DELETED from the value path; ending_mv_source column;
  windowed cell survives verbatim in ending_mv_reported).
- Rollback stashed FIRST: `scratchpad/rollback_build_billing_dim.py` md5
  ff57efa5987a50e159579b9c3eaf3ef0 (11,960 bytes) → restore via s3 cp + re-download verify.
- Deployed `s3://opal-data-inf/code/silver/build_billing_dim.py`, RE-DOWNLOAD md5 TIE:
  **be954ebd4acfe26cc2db3495b4217fa8**.
- CONDITION (1) — the OWN tie-out, denominators printed: **1,869 of 1,869 previously-populated
  rows tie currentValue == retired-windowed ending_mv TO THE CENT** (3,056 pre-filter rows).
- CONDITION (2) — the formerly-absent class rides measured, not on faith: the 485-class tie
  passed FIRST (above, at bronze grain); the 354 previously-window-absent INFGRD rows carry
  their first tie (123 penny-tie vs positions; remainder ride the CTO-ruled content-date
  convention — currentValue live-as-of-pull vs prior-close partition content, frame stated).
- CONDITION (3) — **Amendment-5's anniversary-drift discriminator is HEREBY RETIRED**: no
  window in the value path → no anniversary flips; a post-fix upward move is not dismissible
  as an anniversary artifact.
- Post-fix QA (live 08-11 bronze): 908/908 INFGRD rows populated, ZERO source-absent; book
  $209,476,279.36; fee-mask sum $196,874,030.62. Silver figures move on the next scheduled
  chain fire (no ad-hoc production trigger).

## LEG 2 — THE FLAG ACT (Andrew instruction #2): **OPEN — trigger FIRED by leg 1's landing**

**THE COUPLING, stated so no later reader lands a fraction (COO's both-halves-or-neither,
extended to FOUR legs because INF_D_02 is base-held under live CPR-6 work):**
  (a) mint `is_fee_earning` at its ONE home on the GOLD tier (CTO 155818Z placement — Rule
      17): `data/inf/scripts/gold/lib/fee_classification.py`, ledger basis (custody Mgmt-Fee
      trailing-12m), BOTH lag edges declared, window length a ruled tunable;
  (b) retire the silver-side `_derive_is_fee_earning` (currently DEPRECATED-IN-PLACE with a
      no-new-consumers bound) — **fires WITH (d), never before** (dropping the column while
      D_02 reads it would silently vanish served advisor fee fields);
  (c) consolidate INF_D_04's local `load_fee_activity_mask` onto the gold lib (retiring the
      second derivation site my own TO-2 deploy created);
  (d) repoint INF_D_02's silver-flag read onto the gold classifier — **base-held file,
      sequenced via COO** (owner: COO to schedule; not silently dropped).
**Controls pre-committed:** before/after flip census vs MSTR's 102/907 longitudinal baseline;
both lag edges exercised; deploy per this ledger's pattern (rollback-first, re-download md5).

**Placement-crossing note (surfaced twice, proceeding on the architecture seat's ruling):**
COO's letters say "re-derive in silver"; CTO twice ruled the GOLD home on Rule-17 grounds.
Executing on CTO's placement; COO objection reopens the shape, not the mechanics.
