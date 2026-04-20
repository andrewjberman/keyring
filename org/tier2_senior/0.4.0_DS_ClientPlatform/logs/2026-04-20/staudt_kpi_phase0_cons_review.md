# Session Log — STAUDT.KPI Phase 0 + STAUDT.CONS Review/ACK
**Agent:** 0.4.0_DS_ClientPlatform~C
**Date:** 2026-04-20 (evening ET)
**TOs:** ADVI_STAUDT.KPI, ADVI_STAUDT.CONS
**Commit:** (none yet — TO-file edits uncommitted; validator/diagnostic build is Phase 1)
**Status:** KPI Phase 0 complete, awaiting COO GO for Phase 1. CONS ACK'd, Phase 0 queued.

---

## Session Resume Context

Fresh ~C session launched by Andrew after the prior ~C session closed at ADVI_STAUDT.C commit b687ff47 (~13:30Z). While that session was offline, 6 MCP messages accumulated on the ~C channel:

| # | From | Subject | Time (Z) |
|---|---|---|---|
| 1 | 2.0.0_SA_COO | DISPATCH STAUDT.KPI | 20260420T174904 |
| 2 | 2.0.0_SA_COO | KPI TO extended — identity-assertion sentinel (1b) added | 20260420T182951 |
| 3 | 2.0.0_SA_COO | NUDGE — KPI 3hr radio silence | 20260420T183604 |
| 4 | 2.0.0_SA_COO | PUSH — KPI 3.5hr, second nudge | 20260420T18XX |
| 5 | 2.0.0_SA_COO | GO STAUDT.CONS — 4 review edits incorporated | 20260420T19XX |
| 6 | 2.0.0_SA_COO | CONS broken-ref fix (missed first pass) | 20260420T19XX |

Both dispatches were real (GO-means-GO per feedback memory); the 3.5-hour silence was a session-gap artifact (no live process on the ~C lane channel). Startup protocol (register + check_inbox + get_agent_status + inbox-watch + .agent_context) surfaced all 6 immediately on the new session's first turn.

---

## CONS TO Review (before ACK)

Andrew asked for a review of `ADVI_STAUDT.CONS.ds-small-account-threshold-user-input-investigation.md` before the GO arrived. Review delivered verbally in-chat; COO incorporated all 4 substantive edits into commit 4a901692 + a second commit for the missed `parent-project` ref:

| # | Review item | COO disposition |
|---|---|---|
| 1 | Broken `<ref>project_bd_is_ground_truth.md` — file does not exist in repo (lives only in COO+CTO auto-memory) | Replaced with `<ref type="principle">` inline note describing the operating principle |
| 2 | No `<deadline>` block (P2 without timebox is hard to sequence) | Added `<deadline>24-36hr, target 2026-04-21 evening to 2026-04-22 morning ET</deadline>` |
| 3 | Missing coordination with 0.4.0_DE_ClientPlatform (portal-side wiring is DE's lane) | Added `<ref type="dependency-consult">0.4.0_DE_ClientPlatform</ref>` + acceptance criterion requiring DE consult evidence in briefing |
| 4 | Aggregate-recompute not a distinct trade-off dimension | Added 8th dimension "Aggregate blast (what else must recompute)" — separates A (precompute every rollup per bucket) vs B (recompute per request) vs C (client slider but server rollups static = mismatch risk) |
| 5 (bonus) | Option A bucket selection ($10k/$25k/$40k/$75k/$100k/$250k) is arbitrary | Reframed as Phase 0 deliverable — ground in account-AUA distribution via `comp-platinum reverse` OR ask Andrew for preferred breakpoints |
| 6 (bonus) | Acceptance criteria missing `org/compiler-tools-log.md` append line | Added per TO_COMPILER_GATE.md standard |

Status flipped `dispatched` -> `pending` in-place; Phase 0 queued behind KPI Phase 0.

---

## KPI Phase 0 Work

**Goal:** determine the sentinel pattern (config-native vs standalone validator) for codifying firm AUA 50bps accuracy + flow-vs-snapshot identity as regression sentinels in `gold_validate_config.yaml`.

### Evidence-file-trace

1. **Read `gold_validate_config.yaml`** (Lines 1-184). Declared check types: `key_present`, `count_min`, `field_nonzero`, `sum_approx`, `no_null_numeric`, `threshold_pct`, `script_check`. All config-native types operate on a single artifact via JSON-path. There is no native cross-source-comparison type.
2. **Read `org/modules/graph/validate_cli.py`** (213 lines total). Lines 176-185 dispatch to `data/black_diamond/scripts/validators/validate_{id}.py` when extras supplied or `--artifact` missing. Transparent subprocess invocation, exit-code preservation. This is the pass-through path.
3. **Surveyed existing standalone validators:**
   - `validate_nna_atomic.py` — 5 ratified invariants on parquet artifact, schema-only mode via `--schema`.
   - `validate_role_aua.py` — 6 invariants INCLUDING `I3 cross-advisor additivity` via `--cross-check account_performance.parquet`. **This is the closest existing precedent to KPI's cross-source requirement.**
4. **Read `data/black_diamond/diagnostics/STAUDT/engine_accuracy_2026-04-20.md`** — ~A's manual ground-truth report. Firm gap $48.3M (-284bps). 5-mechanism loss decomposition (bd_stale overreach $38.6M / Schwab undershoot $19.5M / non-Schwab dropped $18.5M / non-Schwab overshoot -$16M / Schwab-mapped dropped $7.8M / canonical-only adds -$2M). Cohort: Schwab -181bps, non-Schwab -1094bps. **This is the parity target for the diagnostic script's 2026-04-16 reproduction.**
5. **Date-alignment check on firm_composition.json producer:**
   - `D_03.composition_artifacts.py` writes `s3://opal-data-bd/gold/views/firm_composition.json` (singleton — NOT date-partitioned in the S3 key).
   - D_03.py L264-279: firm total is sourced from `account_performance.parquet` via `ap['date'].max()`. Implicit as-of date = latest account_performance snapshot.
   - `silver/allocations` IS date-partitioned: `silver/allocations/{date}.parquet`.
   - `canonical/holdings` IS date-partitioned: `gold/canonical/holdings/{date}.parquet`.
   - **Conclusion:** validator takes `--date YYYY-MM-DD` explicitly. Reads canonical + silver parquets directly by that date. Does NOT trust firm_composition.json's implicit date — (a) avoids metadata drift risk; (b) matches ~A's manual methodology which read canonical/holdings.parquet for the 2026-04-16 ground truth.

### Pattern decision — standalone validator

Chosen pattern: **`data/black_diamond/scripts/validators/validate_engine_accuracy.py`** dispatched via comp-validate's pass-through path (L176-185 of validate_cli.py).

**Rationale:**
- Config-native types are single-artifact; cross-source comparison not natively expressible.
- Standalone-validator precedent exists (2 live examples).
- `validate_role_aua.py` already implements cross-artifact invariants — direct skeleton reuse.
- Scope stays tight: no `extract_validate.py` changes, no new check type.

**DISABLED-initially mechanism:** commented-out YAML block in gold_validate_config.yaml with enablement procedure documented in block header. Enablement = uncomment + `comp-validate engine_accuracy --artifact /tmp/... --date YYYY-MM-DD` returning exit 0. Tied to ~A's BFIX1+BFIX2 RAVC4 close. Rejected alternative: introducing an `enabled: true/false` flag in config schema — scope creep into `extract_validate.py`.

### Planned invariants (6)

| ID | Name | Formula | Severity |
|---|---|---|---|
| I1 | BD-anchored firm AUA (1a) | `abs(canonical_firm_aua - silver_firm_mv) / silver_firm_mv < 50bps` | ERROR; WARN @ 25bps |
| I2 | Identity flow-vs-snapshot (1b) | `abs(sum(canonical_nna.aua_residual[d])) / sum(canonical_nna.aua_current[d]) < 50bps` | ERROR; WARN @ 25bps |
| I3 | Schwab-cohort accuracy | same ratio, schwab-mapped subset | ERROR |
| I4 | Non-Schwab cohort accuracy | same ratio, non-schwab subset (currently -1094bps) | ERROR |
| I5 | Account count parity | `canonical_account_count >= silver_account_count - 5` | WARN |
| I6 | Schema presence | required columns in canonical/nna + canonical/holdings | ERROR |

### Planned file layout

| File | Role |
|---|---|
| `data/black_diamond/scripts/validators/_lib_engine_accuracy.py` | Shared compute lib — 5-mechanism loss decomposition + cohort split + cross-source ratio |
| `data/black_diamond/scripts/validators/validate_engine_accuracy.py` | 6-invariant validator. CLI: `--artifact`, `--date`, `--silver`, `--schema`. Skeleton mirrors validate_role_aua.py |
| `data/black_diamond/scripts/diagnostics/engine_accuracy_diagnostic.py` | Markdown report generator. CLI: `--date`, `--output`. Default output: `diagnostics/STAUDT/engine_accuracy_{date}.md`. Imports shared lib |
| `data/black_diamond/scripts/gold/gold_validate_config.yaml` | New **commented-out** `engine_accuracy:` block with `script_check` type + enablement procedure in header |
| `data/black_diamond/diagnostics/STAUDT/KPI/kpi_evidence.md` | Phase 0 pattern evidence + Phase 1 parity check + dry-run log + enablement procedure |

### Phase 0 gate MCP

Sent to 2.0.0_SA_COO at 20260420T195325Z (msg `20260420T195325Z_0.4.0_DS_ClientPlatform_C_STAUDT.KPI_Phase_0___pattern_chosen__sta.md`). Includes pattern choice, evidence, DISABLED mechanism, date alignment, invariant list, file layout, Phase 1 plan. Awaiting GO.

---

## Files Modified (this session, uncommitted)

| File | Change |
|------|--------|
| org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/ADVI_STAUDT.KPI.ds-engine-accuracy-50bps-sentinel.md | `<status>` flipped dispatched -> pending; annotation extended with 20260420T1829Z 1b extension + fresh-session ACK |
| org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/ADVI_STAUDT.CONS.ds-small-account-threshold-user-input-investigation.md | `<status>` flipped dispatched -> pending; annotation notes GO after 4a901692 + broken-ref fix + queued behind KPI Phase 0 |
| .comp-graph/.agent_context | SERIAL=0.4.0_DS_ClientPlatform~C, TO_ID=ADVI_STAUDT.KPI |

**No code written yet.** No gold-script edits, no validator/diagnostic scaffolding — those are Phase 1 after COO GO.

---

## Compiler Tools

| Tool | Command | Result | Notes |
|---|---|---|---|
| grep (Grep tool) | `small_account\|40_?000` on C_08.advisor_fee_efficiency.py | MATCH L72 `SMALL_ACCOUNT_AUA_THRESHOLD_USD = 40_000` | CONS TO premise verified — $40k is a module constant, not a function arg or config |
| grep (Grep tool) | `firm_composition` in gold/ | 5 files touched; D_03.composition_artifacts.py is producer | KPI date-alignment evidence |
| grep (Grep tool) | `firm_composition` in D_03.py | L6 S3 destination, L264-279 loads firm total from account_performance via `ap['date'].max()` | KPI date-alignment confirmed — firm_composition.json is singleton, implicit date = latest account_performance snapshot |
| git show | `f2ec98d1` (B9) | Confirms "SMALL_ACCOUNT_AUA_THRESHOLD_USD = 40_000 module constant" | CONS TO premise verified |
| git show | `bb426933` (B10) | Confirms small_account_avg_aua at (advisor, role) + advisor grain | CONS TO premise verified |

No comp-* tools executed yet — KPI Phase 0 is a CONFIG+SOURCE audit (gold_validate_config.yaml + validate_cli.py + validators/); no graph queries needed. Phase 1 will run comp-pipescript io on canonical/holdings + canonical/nna producers + comp-validate dispatch dry-run. CONS Phase 0 will run the full compiler triad (io, blast, routes, schema-check, pii, cache) per TO spec.

---

## Current State

- **STAUDT.KPI:** Phase 0 complete. Pattern = standalone validator + commented-out config entry. Awaiting COO GO for Phase 1 (build validator + diagnostic + shared lib).
- **STAUDT.CONS:** ACK'd. Phase 0 queued behind KPI. 4 substantive review edits + 2 bonus items incorporated by COO before GO.
- Pending coordination with ~A BFIX1+BFIX2 RAVC4 for KPI sentinel enablement timing.
- ~C inbox empty as of 20260420T1953Z. inbox-watch live (bash bb36qa6vx).

---

## Next Steps

1. **[2.0.0_SA_COO]** GO on KPI Phase 1 plan (pattern + file layout + invariant list).
2. **[0.4.0_DS_ClientPlatform~C]** On COO GO — build `_lib_engine_accuracy.py` + `validate_engine_accuracy.py` + `engine_accuracy_diagnostic.py` + commented-out config entry. Parity-check diagnostic against ~A's 2026-04-16 manual report (within 5%).
3. **[0.4.0_DS_ClientPlatform~C]** Commit KPI work as a single scoped commit (author=~C, `--only`) with paths: validators/, diagnostics/engine_accuracy_diagnostic.py, gold_validate_config.yaml, diagnostics/STAUDT/KPI/.
4. **[0.4.0_DS_ClientPlatform~C]** After KPI Phase 1 commit — update `.agent_context` TO_ID to `ADVI_STAUDT.CONS` and start CONS Phase 0 (compiler triad: io C_08, blast small_account_*, routes /Books, schema-check Consolidation component, pii audit, cache collisions).
5. **[0.4.0_DS_ClientPlatform~A]** Reference KPI sentinel enablement procedure in BFIX1+BFIX2 RAVC4 close ("flip KPI commented-out config to enabled when firm AUA within 50bps post-fix").
6. **[0.4.0_DE_ClientPlatform]** Consult tap pending CONS Phase 0 portal-side questions (React component name, query key, Option C/C' client-side filter cost).

---

## Pending

- KPI Phase 1 build (gated on COO GO).
- CONS Phase 0 compiler triad (queued behind KPI Phase 1 commit).
- compiler-tools-log.md append — will happen automatically via `.comp-graph/.agent_context` auto-log on Phase 1 comp-* runs.
- Session log commit (this file — will go in with KPI Phase 1 commit bundle, or separately if Phase 1 is delayed).
