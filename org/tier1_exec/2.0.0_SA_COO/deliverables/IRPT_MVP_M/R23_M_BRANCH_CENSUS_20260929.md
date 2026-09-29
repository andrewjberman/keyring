# R23 ~M irpt-m-* branch census (row S208, cell IB-mr-231)

Measured 2026-09-29T16:38:00Z against live CLOUD head `75b5cdcba2` (CLOUD advanced twice during this
census, from `a11debe552` to `37cabd144d` to `75b5cdcba2` -- neither intervening commit touched a
census file except one append to the shared INVESTIGATION_v1.md, re-verified). Full evidence per file
in `R23_M_BRANCH_CENSUS_20260929.json`. Nine `irpt-m-*` branches exist live (`git branch --list
'irpt-m-*'`), not the ten the issuer's 15:3xZ read named -- see surprise row IRPT_BCKEND-W81-S1.

- **irpt-m-b01b-skip** -- DRAIN. 2 files, both CARRY (S141's B_01b skip-list fix; its landing
  condition -- CTO sign-off on the COT-new write -- is now satisfied at `ab4a2e41bb`, not reversed).
- **irpt-m-comparison-consumer** -- WORLD-DONE. 2 files, both PRESENT (byte-identical to CLOUD,
  landed independently at `65957b8afc`/`15b9f85eb3`). Omitted entirely from the issuer's preamble.
- **irpt-m-cot-b1** -- DRAIN. Tip identical to irpt-m-cot-cash-line (duplicate branch). 2 files
  PRESENT (Holdings cash-line rule cherry-picked to CLOUD at `a82a01a8ed`), 4 files CARRY (COT-gold
  half explicitly HELD pending S173's re-point, CTO ruling S188 `7ba9384e7d`).
  - CARRY: `data/cot/scripts/gold/C_06.client_mix_timeseries.py`,
    `data/cot/scripts/gold/D_03.composition_artifacts.py`,
    `data/cot/scripts/gold/D_04.client_portal_summary.py`,
    `data/cot/scripts/gold/tests/test_other_admission.py`
- **irpt-m-cot-cash-line** -- DRAIN. Same tip hash as irpt-m-cot-b1 (`0da4449e1f`) -- literally the
  same commits under a second branch name; same 2 PRESENT / 4 CARRY as above.
- **irpt-m-cot-cash-line-act** -- DRAIN. Strict ancestor of cot-b1 (one commit short: the structured/
  commodities addition). 2 files PRESENT (the exact branch a82a01a8ed names as its Holdings
  cherry-pick source), 4 files CARRY (the cash-line-only, narrower COT-gold half, same S173 hold).
- **irpt-m-s125-20260924** -- WORLD-DONE. 2 files, both PRESENT (`fecbf0dc43` landed the deployed
  fix onto CLOUD, which otherwise would have rolled the directory-refresh cadence fix back).
- **irpt-m-s125-publish** -- DRAIN. `refresh.py` + test + the change-management record are PRESENT
  (`fecbf0dc43`, `3a906e2672`); `lambda-source-map.json` is SUPERSEDED (CLOUD's registry has moved on
  through ~20 later independent CI deploy-record commits); the terraform `CHANGELOG.json` entry for
  this branch's own deploy is CARRY -- genuinely missing from CLOUD's 21 current (all P-lineage)
  entries, and append-only so it cannot conflict.
- **irpt-m-s152** -- DRAIN. 0.4.0_DS_ClientPlatform~X's work-order output (structured/commodities
  admission, 49F/BD/COT). Its surprise row collided with ~M's own numbering and was renumbered
  S152->S155 by CTO 101771; S155 is still ARMED (open, undisarmed) on ~M. 15 files CARRY (tied to
  S155), 1 file (`data/cot/scripts/gold/lib/mix_views.py`) is SUPERSEDED -- CTO+CRO signed a
  narrower, different re-cut of the SAME file "ALONE" (`c1862baf18`/`b5bb9430e7`), which is exactly
  irpt-m-s152-cloud's fix. 1 file (`INVESTIGATION_v1.md`) is PRESENT -- its 4 rows landed on CLOUD
  under the renumbered ids S153-S156 (verified by direct grep).
- **irpt-m-s152-cloud** -- DRAIN. ~M's own SIGNED S152 re-cut (CTO 101688/101700, CRO 101686,
  final "ALONE ff63895521 stands" ruling) -- fully approved, yet still not an ancestor of CLOUD, whose
  live `mix_views.py` still lacks `cash`/`other`. Both files CARRY: this is the authoritative version
  the s152 branch's wider cut was ruled against, and it is itself the thing still missing.

## Duplicates / non-independent branches found
`irpt-m-cot-b1` and `irpt-m-cot-cash-line` are the same commit (`0da4449e1f`) under two branch names.
`irpt-m-cot-cash-line-act` is a strict ancestor of both. Draining once (from any of the three) covers
all three; the other refs are stale pointers for cleanup, not a second drain.

## CARRY files, by branch (for the drain act)
- irpt-m-b01b-skip: `B_01b.classify_new_securities.py`, `tests/test_other_admission.py`
- irpt-m-cot-b1 / irpt-m-cot-cash-line: `C_06.client_mix_timeseries.py`,
  `D_03.composition_artifacts.py`, `D_04.client_portal_summary.py`, `tests/test_other_admission.py`
  (all under `data/cot/scripts/gold/`)
- irpt-m-cot-cash-line-act: same 4 paths, narrower (cash-line-only) content
- irpt-m-s125-publish: `infra/aws/terraform/investor-reporting/CHANGELOG.json` (one append)
- irpt-m-s152: 15 files across `comp-constants.config.yaml`, `data/assets/scripts/gold/runners_49f/*`,
  `data/black_diamond/scripts/gold/*`, `data/cot/scripts/gold/runners_cot/d08_cot_mix_summary.py`,
  `data/cot/scripts/gold/tests/test_b1_class_admission_cot.py`, and 4 deliverable files under
  `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.4.0_DS_ClientPlatform~X/` -- ALL still tied to
  ARMED row S155, not yet disposed
- irpt-m-s152-cloud: `data/cot/scripts/gold/lib/mix_views.py`,
  `data/cot/scripts/gold/tests/test_s152_mix_views_cash_other.py`

Full per-file evidence (commit hashes, diff results, ruling citations): see the JSON.
