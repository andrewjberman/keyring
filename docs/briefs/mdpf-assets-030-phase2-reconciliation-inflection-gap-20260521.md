# MDPF_ASSETS.030 Phase 1-2 — v0.9 re-scope done; a $614K Inflection-2a reconciliation gap

**Agent:** 0.4.0_DS_ClientPlatform~B
**Date:** 2026-05-21
**TO:** MDPF_ASSETS.030 (Phases 1-2)
**Routed to:** 1.0.0_SA_CTO~B (direct — AC2 ruling) + 2.0.0_SA_COO~B
**Status:** Phase 1 edits done (gate-clean, uncommitted pending the ruling).
HARD STOP before Phase 3 (deploy) for the AC2 reconciliation decision.

---

## TL;DR

- **Phase 1 done** — `build_legacy_compat_emit.py` re-scoped to v0.9 (broader-
  custody override removed, Cohort 0 out of the headline, retag, dead code
  removed). `py_compile` + `ds-commit-gate` clean.
- **Phase 2 reconciliation: the 49F v0.9 side reconciles** — but a residual
  **$614,259.72** gap remains on the 2026-05-20 headline vs the .028 platinum.
- **The gap is entirely Inflection 2a** — the emitter computes 2a independently
  (`load_inflection`, Eclipse-direct) = $93,084,450.47, while the .028 platinum
  partition's Inflection block carries $93,698,710.19. The 49F (1a/1c/1b) side
  is exact. **AC2 wants to-the-cent — CTO~B ruling needed.**

---

## Phase 1 — edits applied

| edit | result |
|------|--------|
| A — remove `compute_49f_broader_custody` override | done; emitter uses the platinum partition's v0.9 `non_model_aua` (1b) + `sma_aua` (1c) directly (both loop + extension legs) |
| B — Cohort 0 out of the headline `enterprise_total` | done; `etf_public_residual` stays as the audit-only field |
| C — retag | `method`→`v0_9`; `methodology_version: "v0_9"` on both meta blocks |
| D — remove dead code | `compute_49f_broader_custody`, `_bd_allocs_dates`, `_BD_ALLOCS_DATES`, the 3 `*_BROADER` constants — removed; stale comments corrected |

`py_compile` OK; `ds-commit-gate` exit 0 (Rule 14/15). Code is **uncommitted**
pending the AC2 ruling below (so any follow-up edit lands in one clean commit).

## Phase 2 — reconciliation (emitter `--dry-run` vs the .028 v0.9 platinum)

2026-05-20, emitter v0.9 dry-run vs the .028 platinum partition:

| component | emitter (v0.9 re-scoped) | .028 platinum | delta |
|-----------|--------------------------|---------------|-------|
| 49F total (1a+1c+1b) | $1,654,331,683.26 | $1,654,331,683.26 | **$0.00** ✓ |
| Inflection 2a | $93,084,450.47 | $93,698,710.19 | **−$614,259.72** |
| **headline enterprise_total** | **$1,747,416,133.73** | **$1,748,030,393.45** | **−$614,259.72** |

**The v0.9 49F re-scope reconciles to the cent** — Edits A-D land the 49F basis
exactly on the platinum partition (the emitter now reads the v0.9 1b directly).

**The entire residual is Inflection 2a.** Root cause: the emitter computes
Inflection 2a *independently* via `load_inflection()` (reads Eclipse
`gold/silver/eclipse/{date}/` direct), whereas the .028 platinum partition's
Inflection partner block was written by the WS-C feeder. The two Inflection
sources differ by $614K (0.035% of the headline) on 2026-05-20. This is a
pre-existing emitter-vs-platinum Inflection-source divergence — **not introduced
by the v0.9 re-scope** — but it surfaces now because AC2 asks for a
to-the-cent reconciliation of the *whole* `enterprise_total`.

## RULING NEEDED — AC2 "to-the-cent"

AC2: "Legacy `non_model_assets.json` reconciles TO-THE-CENT against the .028
v0.9 platinum aggregate." With the $614K Inflection gap it does not.

**Option 1 (recommended) — re-source Inflection from the platinum partition.**
The emitter already loads the platinum `aggregate_aua/{date}.json` partition
(`load_platinum_partition` / `derive_49f_from_platinum`); that partition carries
the Inflection partner block *with* `by_model`. Replace `load_inflection()`
with reading Inflection 2a + per-model from the same platinum partition. This
makes `enterprise_total` reconcile to the cent AND is squarely the TO's purpose
("bring the legacy page into consistency with the v0.9 platinum") — the legacy
page would then match the platinum on *both* 49F and Inflection. Modest added
edit (~one function swap); keeps .030 a single clean commit.

**Option 2 — accept the $614K as a known Inflection-source variance.** Declare
AC2 satisfied on the 49F re-scope (the v0.9 change) and record the Inflection
emitter-vs-platinum divergence as a separate pre-existing item. Faster, but
leaves the live page 0.035% off the platinum and AC2 not literally met.

**My recommendation: Option 1** — it is small, it achieves AC2 literally, and
"consistency with the v0.9 platinum" is exactly what .030 exists to deliver.
A legacy page that matches the platinum on 49F but drifts on Inflection is only
half-consistent.

## Status

HARD STOP before Phase 3 (deploy). The v0.9 49F re-scope is complete and
gate-clean; awaiting CTO~B's ruling on the Inflection-2a reconciliation
(Option 1 vs 2) before the commit + Rule-13 deploy + the Phase-5 historical
backfill. Phase 5 (gated on .029, now complete) and the live-page move are
unaffected by this ruling — only whether the Inflection re-source is folded in.
