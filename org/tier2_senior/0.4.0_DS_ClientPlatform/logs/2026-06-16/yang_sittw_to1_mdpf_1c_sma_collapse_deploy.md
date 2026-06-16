# Session — YANG_SITTW.TO-1: MDPF 1c/SMA cohort collapse into 1b' (producer leg a — implemented + deployed + never-widen verified)

**archetype:** MIXED
**secondary_archetypes:** IMPLEMENT, DIAGNOSE, VALIDATE, DEPLOY, COORDINATE

Serial: 0.4.0_DS_ClientPlatform~A (lane A). Base author on commits.
Window: ~18:08Z startup -> ~18:40Z. Spawned for YANG_SITTW.TO-1 (Andrew "YANG up first"). Event-driven: spawn-confirm -> COO GO -> Phase-1 investigation -> implement -> Phase-2 never-widen -> CTO+COO co-sign -> DEPLOY-GO -> deploy + Phase-3 -> RAVC close. Leg (a) done; leg (b) FE handed to COO to sequence.

## Summary

1. **Producer cohort-collapse implemented + deployed.** `build_aggregate_aua_timeseries.py`: fold `sma_aua` (1c) into `non_model_aua` (1b' = Schwab_total - 1a) + drop the `sma_aua` field, at aggregate + per-firm. Commit `935d3ba79`. Re-derived + deployed all 3 served slices.
2. **Never-widen verified TWICE = $0.0000 movement** (Phase-2 local re-derive + Phase-3 on the DEPLOYED artifact), all 413 dates x 3 slices (global / 49financial / inflection): TOTAL + model + combined Non-Model band unmoved; `sma_aua` removed; `by_model` identical. CTO+COO joint never-widen co-sign GRANTED on the evidence; CTO binding-AC (verify on deployed result) satisfied.
3. **The fabrication, root-caused.** The served `sma_aua` carried a fabricated non-zero interpolated estimate pre-launch ($19.67M @ 2024-11-01) while the REAL SMA detail (by_model sleeves) was honestly null — see root-cause note below. Because 1b is a plug, the fabricated 1c was double-entered (added to sma, subtracted from nm), so the fold cancels it exactly → never-widen-safe by construction.
4. **Deploy FINISHED in-session, no stranded leg.** Deploy-completion ledger `yang-sittw-to1-mdpf-1c-collapse` opened at start, all 4 legs proven, CLOSED. Added a DURABILITY leg the COO's 2 steps omitted: uploaded the new rollup to the runner code-prefix `s3://opal-data-mdpf/code/scripts/backfill/` so the next nightly Stage-4 runs new code (else it reverts the collapse).
5. **Consumer-safety surfaced + verified (if_mismatch).** The FE DOES read `sma_aua` directly (ModelPortfolios.tsx L831/L893) — but it folds `nm+sma` via `?? 0` / `lastNonNull(undefined)→0`, and the Global view doesn't read it at all → dropping the field renders IDENTICALLY, no live break. Surfaced to COO/CTO; both independently re-verified.
6. **Transparency:** my "held local" commit reached origin EARLY (carried by another agent's shared-branch push b2cd5138d) — benign (mdpf is push-"check-only"; no served move until the post-co-sign `--upload`); never-widen gate NOT pre-empted. Same class as my GLDINC P1 note.

## Work done

### Phase-1 investigation (read-only, pre-GO)
- Read the producer: confirmed `build_aggregate_aua_timeseries.py` is a ROLLUP — it READS `sma_aua`/`non_model_aua` from the per-date partitions (`art["aggregate"].get(m)`, `p.get(series)`); the carve-out arithmetic lives in the partition-builders, NOT the rollup. → the surgical fix is a rollup-fold, never-widen-safest.
- Ground-truthed the served data (`aws s3 cp` global/49f/inflection slices + a 2024-11-01 partition):
  - Partition aggregate: `partner_aua_subtotal (924.4M) = 1a+1c+1b`; `opal_aggregate_aua (776.2M) = subtotal − cohort_2b_audit (148.2M = inflection custody pre-onboarding)`. So "Schwab_total" = `partner_aua_subtotal`, and `1b' = Schwab_total − 1a = 1b + 1c`.
  - `sma_aua` fabricated non-zero at ALL 413 dates ($19.67M @ 2024-11-01); by_model SMA sleeves (`opal_div_sma`, `opal_growth_sma`) honestly NULL pre-launch, real (==sma_aua) only from ~2026-05-18. ← the fabrication is isolated to the top-level field.
- Consumer enumeration (precise grep, since comp-pipescript io is mdpf-unsupported): only ModelPortfolios.tsx reads `sma_aua`/`non_model_aua`, all undefined-safe; Global view uses by_model(!=sma) + getNonModelAssets. → backward-compatible.

### Implementation (build_aggregate_aua_timeseries.py)
- Added `_fold_sma_into_nonmodel(series)`: `non_model_aua' = non_model_aua + sma_aua` element-wise, None-safe (both-None→None, else None treated as 0), then `del sma_aua`. Applied to the aggregate dict + every partner after assembly. Removed the `sma_aua` emit from `slice_per_firm`. Updated the docstring + the served `meta` (cohort0_historical_backfill leads with the collapse; basis_provenance gains `sma_collapsed_into_1b`).
- `data_contract.xml`: added `<mdpf_global_timeseries>` recording producer + served shape + the sma_aua removal + the FE-backward-compat note (commit 935d3ba79).

### Phase-2 never-widen (local re-derive before/after)
- Ran the producer `--out` (no upload) → diffed served BEFORE vs re-derived AFTER. GLOBAL + 49FINANCIAL + INFLECTION: TOTAL $0.0000, model $0.0000, combined band (before nm+sma vs after nm) $0.0000, by_model identical, sma_aua dropped, dates identical. Only delta = sma_aua removed + nm relabeled to 1b' (rises by old sma: global first +$19.67M / last +$24.22M = the internal relabel, not a widen).

### Deploy (on COO DEPLOY-GO; CTO+COO never-widen co-sign granted)
- L1 git: 935d3ba79 confirmed on origin/CLOUD (`git diff origin/CLOUD HEAD` on file = empty).
- L2 s3-prefix (durability): `aws s3 cp` the new producer → `s3://opal-data-mdpf/code/scripts/backfill/build_aggregate_aua_timeseries.py` (ETag 818d3049…, fold present in deployed runner code).
- L3 activation: producer `--upload` re-emitted 7 objects (platinum + json/ mirrors × global/49f/inflection + non-sliced global), all rc=0, no AccessDenied.
- L4 verify (CTO binding AC): re-pulled the DEPLOYED `json/mdpf/{firm}/aggregate-aua-timeseries.json` → $0.0000 TOTAL/model/combined-band movement all 3 slices, sma_aua absent, by_model identical, deployed mtime 18:37:13Z > commit. Never-widen holds on the DEPLOYED result.
- Ledger closed (4/4 legs proven).

### Coordination
- Spawn-confirm + RAVC2 (before/after) → COO; FYI evidence → CTO. CTO co-sign GRANTED (+ binding AC: verify on deployed). COO co-sign + DEPLOY-GO GRANTED (independently re-grepped the consumer safety). RAVC-close leg (a) → COO, CC CTO.
- Wrote FE-leg handoff brief `docs/briefs/ds-brief-yang-sittw-to1-fe-leg-handoff-20260616.md` (deployed shape + exact FE touch-points: type cleanup, redundant `+sma_aua` removal, x-axis extend to 2024-11-01, estimate-tail demarcation 2024-11-01→2026-01-15). Flagged COO to sequence DE 0.4.0 + RD 0.4.1.

## Root-cause note — why item-(d)'s `1c=$0` didn't ship in v0.9 (TO acceptance)

There are TWO partition-builders. `build_mdpf_process_backfill.py` correctly emits `sma_aua: None` ("rejected weekly-document-interpolated build_mdpf_v0_bandaid_backfill.py … the value is an explicit null — never interpolated, never carried as if real"; 1c a non-additive sub-slice of 1b) — that IS item-(d)'s `1c=$0`, implemented. BUT the **v0.9 schwab_canonical rederive** (MDPF_ASSETS.029 rps_calibrated + .031 2024depth; `basis_provenance.interpolated_1c=True`) — the basis the ENTIRE served history sits on — **re-introduced an interpolated aggregate 1c**, superseding the correct null. So the recommendation shipped in process_backfill but was overwritten by the later canonical-rederive's interpolation step. Evidence: the served by_model SMA sleeves are honestly null pre-launch (item-(d) honored) while the served top-level `sma_aua` is interpolated non-zero (the rederive's override). The collapse (`1b' = Schwab_total − 1a`) removes any need for an aggregate 1c estimate — SMA lives inside the plug to its real by_model extent — so the class can't recur regardless of which builder runs.

## Compiler Tools

| Tool / check | Run | Observed output | vs `<expect>` | Verdict |
|---|---|---|---|---|
| `comp-pipescript io build_aggregate_aua_timeseries` | yes | "Script not found … Did you mean: build_interpolated_prices, build_tax_dim?" | enumerate sma_aua consumers | **GAP** — io is bd/inf-only; mdpf silently unsupported ([[reference_comp_pipescript_io_postdeps_bd_only_silent_unknown]]). Did consumer enum via precise grep instead → found FE reads sma_aua but is undefined-safe/backward-compat. NOT counted as clean. |
| `comp-transform schema-check ModelPortfolios` | yes | "[WARN] types-resolution: no types.ts found near ModelPortfolios.tsx" (exit 1) | no field MISSING after sma_aua removal | **TOOL-LIMIT** — component types live in portal-proxy.ts (not a co-located types.ts). Did manual type-reconcile: `MdpfPerFirmTimeSeries.sma_aua` declared required → FE leg makes optional/removed; runtime-safe via `?? 0`. Handed to FE leg in the brief. |
| `comp-pipescript deployed` / `postdeps` (mdpf) | no | — | deploy/post-step verify | mdpf is "check-only" / bd-only for these (memory); they return Unknown for mdpf. Substituted a STRONGER direct check: runner-code ETag + fold-present grep + Phase-3 served-artifact re-verify ($0 on deployed). |
| Phase-2 never-widen diff (custom, served BEFORE vs local AFTER) | yes | TOTAL/model/combined-band = $0.0000, all 413d × 3 slices; sma_aua dropped; by_model identical; dates identical | TOTAL + Non-Model band UNCHANGED | **PASS** (the never-widen evidence) |
| Phase-3 served-verify (custom, DEPLOYED vs BEFORE) | yes | $0.0000 all 3 slices; sma_aua absent; mtime 18:37:13Z > commit; by_model identical | $0 on the deployed artifact (CTO binding AC) | **PASS** |
| `ds-commit-gate.sh build_aggregate_aua_timeseries.py` | yes | "All checks passed! OK: pre-commit gate clean" | py_compile + AST clean | **PASS** |
| `deploy_ledger.py open/close-leg/close` | yes | OPENED 4 legs → all closed → CLOSED (sentinel removed) | deploy-completion discipline | **PASS** (no stranded leg) |

Why no comp-validate: the MDPF rollup is a backfill/aggregator, not a gold-dispatch script with a comp-validate config; the served-artifact never-widen before/after IS the value-validation here, run directly.

## Files Modified
- `data/mdpf/scripts/backfill/build_aggregate_aua_timeseries.py` — the collapse (commit 935d3ba79; deployed to runner code-prefix + served artifact).
- `org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/data_contract.xml` — `<mdpf_global_timeseries>` shape record (935d3ba79).
- `docs/briefs/ds-brief-yang-sittw-to1-fe-leg-handoff-20260616.md` — FE-leg handoff (new).
- `org/critical_paths/change_management/20260616T1835Z_yang-sittw-to1-mdpf-1c-collapse_deploy_completion.md` — ledger (opened+closed).

## Next Steps
- **[2.0.0_SA_COO]** — sequence the FE leg (b): 0.4.0_DE_ClientPlatform (FE wiring) + 0.4.1_RD_ModelPortfolios (component, spawn-on-demand) against the deployed shape, per the handoff brief. Deploy-first done; FE-backward-compatible so no race.
- **[0.4.0_DE_ClientPlatform]** — on COO GO: type cleanup + redundant `+sma_aua` removal + x-axis extend to 2024-11-01 + estimate-tail demarcation (Global only; per-firm unchanged). `comp-transform schema-check` caveat noted in brief.
- TO-1 stays `pending` until leg (b) lands; I'm available to support the FE wiring (shape questions, provenance boundaries for the demarcation).
- Separate: GLDINC P1 ledger L4 verify remains in-window, gated on the 6/17 nightly (not a strand).
