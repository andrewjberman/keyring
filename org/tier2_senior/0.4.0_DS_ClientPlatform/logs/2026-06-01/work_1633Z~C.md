# work 1633Z — 0.4.0_DS_ClientPlatform~C — PMA off-slot relabel (COO GO)

**Tick:** /work 2026-06-01 ~1633Z. **Project:** FIND_INSURE Phase 2A (parallel/secondary).
**Trigger:** COO [DRIVE] split-ruling GO — off-slot relabel is a binding data-correctness fix (NOT Andrew-gated); only universe-DEFINITION A/B waits on Andrew.

## Done this tick
1. **PMA relabeled OFF the #1 insurance-IMO slot** (CTO ruling 162518Z + COO off-slot GO), data preserved:
   - `build_contacts_target.py` v1.3: config-driven out-of-universe segregation — `out_of_insurance_imo_universe` slugs move to a new `adjacent_wm_targets` array (relabeled to `true_identity`, data+score preserved), excluded from the ranked insurance-IMO `companies` array. Source of truth = `source-list-corrections-v1.json` (also read by `extract_source_list`).
   - Live `serving/contacts-target-2026-05-27.json` rebuilt + verified: 24→23 IMOs, `adjacent_wm_targets_count=1` (PMA Financial Network), PMA not in `companies`.
   - Ranked brief `find-insure-024-ranked-target-list-20260529.md`: PMA off #1 → **lincoln-investment #1** of 23; separate adjacent-WM section; revision note; IMO-universe series-licensed corrected to 44 (73−29); `no_firm_match` note updated (v2 alias map SHELVED per empirical findings).
2. **#79 re-sourced → UNRESOLVED**: two web searches found no distinct insurance-IMO "Preferred Marketing Associates" web presence; marked `real_imo_domain_status=UNRESOLVED`, kept flagged `WRONG_DOMAIN` + `out_of_universe` so a re-pull excludes it (never silently resolves pmanetwork.com). #92 preserved.
3. 98-pairing spot-audit: already delivered (RAVC2 163657Z) — 1/24 (only PMA); eagle #31 review; no new clear errors.

## Gate / verify
- ds-commit-gate clean; `test_build_contacts_target.py` 3 pass (default no-op preserved); live serving artifact verified (PMA segregated).

## Commits
- `62fd126c4` (PMA off-slot relabel: serving v1.3 + brief + config) — pushed origin/CLOUD.
- (this tick builds on `4fe0a7cb2`/`0382a23bd` corrections layer.)

## RAVC2
- COO 164844Z (primary) + CTO 164856Z (CC). Universe-DEFINITION A/B left with Andrew; off-slot fix implements the COO+CTO keep-PMA-separate lean either way (one config flag reverses if Andrew expands the universe).

## Open / pending senior decisions
- rep-BD-disjoint standing pull-time gate: bank-or-GO (COO).
- Universe-DEFINITION A/B: Andrew.
