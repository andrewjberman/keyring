# DEPLOY LEDGER — billing WINDOW FIX + the coupled FLAG ACT — 2026-08-11

**Status:** CLOSED -- all legs proven, scheduled-fire verification DISCHARGED 2026-08-12 ~15:05Z. Re-stamped 2026-08-26 by `2.0.0_SA_COO`.

> **This entry carried no top-level `**Status:**` line, and the first status-shaped string a reader meets is the PRESERVED SUPERSEDED HEADER further down -- *"Original: legs (a)+(c) CLOSED ~1730Z; (b)+(d) OPEN at COO."* That line is deliberate provenance and is CORRECTLY kept; it is also what made this read OPEN for 338 hours.**
>
> **ACTUAL STATE, from the body:** LEG 1 CLOSED 08-11 ~1712Z, deploy verified, own tie-out 1,869/1,869 to the cent. LEG 2 **ALL LEGS CLOSED ~1815Z** -- including the completion amendment that caught the missed `validate_api_dims.py:96` touch on re-read. **SCHEDULED-FIRE VERIFICATION DISCHARGED 08-12, ALL CHECKS PASS** (structural 4/4, value 3/3 in band, served == silver book $209,225,005.59 delta 0.00).
>
> ⛔ **I CHECKED THE ONE THING THAT WOULD HAVE MADE THIS RE-STAMP A BURIAL, BECAUSE IT NAMES MY OWN SEAT:** leg (d) was *"base-held file, sequenced via COO (owner: COO to schedule; not silently dropped)."* **It was executed** -- *"(d-extended) + (b) window executed per COO 175403Z"*, all four repoints VERIFIED ON RE-READ before (b). **Nothing is owed by this seat, and a status line stamped without reading for that would have closed a COO obligation by accident.**
>
> Owner `0.4.0_DS_ClientPlatform~A` is not live. Record correction only; **no deploy state, no leg, and no superseded text was altered.**

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

## LEG 2 — THE FLAG ACT (Andrew instruction #2): **ALL LEGS CLOSED ~1815Z — INSTRUCTION #2 COMPLETE**

**(d-extended) + (b) window executed per COO 175403Z (transfer extended, C_09 repoint ruled,
WINDOW_DAYS held 365). Order honored: all four repoints VERIFIED ON RE-READ before (b).**
- Repoints @9eeecd154d, deploys all md5-TIED: D_02 4a61f28c / D_00c a88c5997 / D_00f
  d769a8f7 / C_09 faf9e9cd / lib(amended: upper date bound + asof-series) 52005d2b.
  Verifications: D_02/D_00c/D_00f each EXACT vs lib (771 of 908); C_09 97-partition
  longitudinal stack spot-verified 3/3 dates (606/730/771 -- real history, no flicker).
  Surfaced: C_09 is PARKED (Path C.1 ratified 2026-05-25) -- repointed as ruled, parked
  disposition untouched.
- (b) retirement deployed, md5 TIE 9a25fe0dc8e0: _derive_is_fee_earning + column + fee-split
  prints removed from silver; registry yaml grounding amended; tests unchanged by disposition
  (they assert reader behavior on fixture columns). Window-fix outputs verified INTACT
  post-retirement (908/908, $209,476,279.36, own-tie 1,869/1,869).
- Rollbacks all stashed pre-first-write: 55c69984 / dfd73226 / a3029cf2 / e3932b4a / be954ebd.
- **COMPLETION AMENDMENT ~1817Z:** the ruled `validate_api_dims.py:96` touch was MISSED in
  the first close (caught on re-read of the window order against the executed set) --
  billing `required_columns` still demanded the retired column and the next validation run
  would have FAILED LOUD on the healed dim. Fixed + deployed, re-download md5 TIE
  777c62aec667. The close report to COO carries the correction explicitly.
- **THE ESTATE NOW HAS EXACTLY ONE ANSWER TO "DOES THIS ACCOUNT EARN FEES"**
  (lib/fee_classification.py). Both billing files RETURN TO BASE at this close.

*(superseded header of this section preserved below for provenance)*
Original: legs (a)+(c) CLOSED ~1730Z; (b)+(d) OPEN at COO

**Legs (a)+(c) executed + deployed (commit 7c6043a883):**
- (a) `lib/fee_classification.py` MINTED — the single gold-home derivation (ledger basis,
  both lag edges declared in-function, WINDOW_DAYS=365 ruled tunable). Deployed FIRST-MINT
  (explicit) to `s3://opal-data-inf/code/gold/lib/fee_classification.py`, re-download md5
  TIE **62cfa5f388762614103971ef392a7415**.
- (c) INF_D_04's local derivation RETIRED → thin delegate. Deployed (sentinel-lifted
  artifact; repo file keeps the sentinel — the AoR hold is untouched), re-download md5 TIE
  **eaae8fb4a8c526ea4907c84e45875408**; rollback stash of the prior deploy = 49712671… .
- CONTROLS: IDENTITY lib==retired-local EXACT (771 fee-active / 851 observed, both
  derivations, same input); determinism stable; window mutant 365→30d dropped 241 accounts
  (tunable live); edges demonstrated with live specimens (19 lag-in, 8 lag-out accounts);
  D_04 delegate path byte-identical.
- Served figures unchanged by construction (identity control) — no serve event in this act.

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

## SCHEDULED-FIRE VERIFICATION: **DISCHARGED 2026-08-12 ~15:05Z -- ALL CHECKS PASS**

Both standing watches read on the FIRST post-fix scheduled run (chain complete advanced
08-11 14:59:31Z -> 08-12 15:02:12Z; serve generated_at 14:58:54Z, data_as_of 08-11 = T-1,
calendar resolved first). Deployed code re-verified 4/4 md5 TIE BEFORE the fire.
Interpretation table PRE-REGISTERED before the evidence existed (`PREREG_...md` @committed).

- STRUCTURAL 4/4: `ending_mv_source` 908/908 roster-sourced · retired `is_fee_earning`
  absent · **908/908 populated, ZERO source-absent** · **own tie-out 554/554 TO THE CENT**
  (coverage changed, meaning did not -- the load-bearing control).
- VALUE 3/3 in band: silver book **$209,225,005.59** (-0.12% vs QA pin) · served fee-earning
  **$203,216,860.04** (+0.19%) · served **non-fee-earning $6,008,145.55** (band $6-8M).
- Rescued class MEASURED: 354 of 908 rows, **$68,676,268.78** previously suppressed to zero
  (pre-fix book was $140,717,260.47).
- Cross-plane: served `total.aua` == silver book == **$209,225,005.59**, delta 0.00;
  `unclassified_aua` 0.0. (Bucket identity is by-construction; the served/silver equality is
  the independent fact. Mechanism INFERRED, not source-confirmed.)
- Andrew instruction #1 + #2 now verified IN PRODUCTION on a scheduled run: non-fee-earning
  serves at $6.01M against his ~$8M expectation and the $60M+ that started it.
- Full record + the self-caught instrument error: `org/tier2_senior/0.4.0_DS_ClientPlatform~A/
  logs/2026-08-12/RESULT_first_post_fix_scheduled_fire.md`.

**Placement-crossing note (surfaced twice, proceeding on the architecture seat's ruling):**
COO's letters say "re-derive in silver"; CTO twice ruled the GOLD home on Rule-17 grounds.
Executing on CTO's placement; COO objection reopens the shape, not the mechanics.
