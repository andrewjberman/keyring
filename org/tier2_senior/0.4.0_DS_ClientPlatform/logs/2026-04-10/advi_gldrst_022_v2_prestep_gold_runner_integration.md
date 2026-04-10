# 0.4.0_DS_ClientPlatform — Session Log 2026-04-10 (ADVI_GLDRST.022)

**Agent:** 0.4.0_DS_ClientPlatform
**Date:** 2026-04-10
**TO:** `ADVI_GLDRST.022.ds-v2-prestep-gold-runner-integration`
**Predecessors:** ADVI_GLDRST.021 (commit `9b4f7a77`), ADVI_GLDRST.021b (commit `97cf703c`), ADVI_GLDRST.021b audit log (commit `109d4138`)

---

## Current State

ADVI_GLDRST.021 shipped the `transaction_observed_capped` source tag. ADVI_GLDRST.021b shipped the `_T1_CAP_EXEMPTIONS` frozenset (CMG + PRAX) and the `MIN_OBSERVATIONS_FOR_CAP = 15` sample-size guard — the combined fix reduced the capped-row set from 31 to 8, all 8 being the 2024-08-07 BD corruption cluster. Both predecessor TOs are complete.

With v2's behavior frozen and audited, the remaining work was to actually put v2 on the gold runner as a scheduled pre-step so the weekend/holiday gap in `canonical_prices.parquet` closes at the canonical source rather than being patched in every downstream gold script.

## Work Done

### Part 1 — Script location decision (acceptance criterion #1)

Verified `build_canonical_prices_v2.py` imports before moving:

- Line 46: `from lib.ticker_overrides import YF_OVERRIDES, TICKER_CORRECTIONS`
- No `sys.path` manipulation anywhere in the file
- No `__file__` or hardcoded `scripts/silver` / `scripts/gold` paths anywhere
- Lines 31-46 are a clean import block (stdlib + boto3/numpy/pandas + one relative `lib.*` import)

Verified the destination state of `lib/ticker_overrides.py`:

- Present in `data/black_diamond/scripts/silver/lib/ticker_overrides.py`
- **NOT** present in `data/black_diamond/scripts/gold/lib/` (verified via `ls data/black_diamond/scripts/gold/lib/`)

Cross-referenced who else imports `lib.ticker_overrides`:

| File | Location | Status |
|---|---|---|
| `build_canonical_prices_v2.py` | silver/ (being moved to gold/) | Moving as part of this TO |
| `bd_price_update.py` (host version) | silver/ | Orphaned — superseded by `bd-price-update` Lambda. Not scheduled anywhere. |
| `inject_scoped_overrides.py` | silver/ | Orphaned — emergency manual tool, not scheduled. |
| `E_06.trace_asset_pricing.py` | gold/ | Latent import bug — imports `lib.ticker_overrides` but it's not in `gold/lib/`. Never breaks because E-scripts aren't dispatched automatically. |
| `E_08.tail_asset_drill.py` | gold/ | Same latent bug |
| `E_11.unmatched_asset_analysis.py` | gold/ | Same latent bug |
| `E_15.validate_yf_overrides.py` | gold/ | Same latent bug |

**Decision: Option (a) from the TO — copy `ticker_overrides.py` into `gold/lib/` and move `build_canonical_prices_v2.py` into `code/gold/`.**

Rationale:

1. **Keeps work in DS's lane.** `run-gold-layer.sh:79` (the EC2 boot script, AE territory) already syncs `code/gold/` unconditionally. Putting v2 at `code/gold/build_canonical_prices_v2.py` and `ticker_overrides.py` at `code/gold/lib/ticker_overrides.py` means no edit to the boot script.
2. **Fixes the latent E-script import bug as a free side-effect.** E_06, E_08, E_11, E_15 will now be able to resolve `lib.ticker_overrides` when run from the gold runner, which is the only place they should ever run.
3. **Tolerable duplication.** `ticker_overrides.py` now exists in both `silver/lib/` and `gold/lib/`. Drift risk is real but bounded — it's a constants-only file (two frozen dicts: YF_OVERRIDES with 757 entries, TICKER_CORRECTIONS with 96 entries). I logged the consolidation as a follow-up but did not attempt it in this TO to avoid breaking the orphaned silver-side `bd_price_update.py` and `inject_scoped_overrides.py` that still import from `silver/lib/`.
4. **Semantically acceptable.** v2 is cross-layer work anyway — it writes to `silver/prices/` but needs to run in the gold runner's operational envelope because it's a pre-step for the gold chain. Living in `code/gold/` describes its operational role.

Operations:

```bash
cp data/black_diamond/scripts/silver/lib/ticker_overrides.py \
   data/black_diamond/scripts/gold/lib/ticker_overrides.py
# md5 verified identical: acc7eff08facf4d7199c7847bdfcfc25

git mv data/black_diamond/scripts/silver/build_canonical_prices_v2.py \
       data/black_diamond/scripts/gold/build_canonical_prices_v2.py
```

Verified imports resolve from the new location:

```bash
cd data/black_diamond/scripts/gold
python -m py_compile build_canonical_prices_v2.py  # OK
python -c "import sys; sys.path.insert(0, '.'); from lib.ticker_overrides import YF_OVERRIDES, TICKER_CORRECTIONS; print(len(YF_OVERRIDES), len(TICKER_CORRECTIONS))"
# → 757 96
```

### Part 2 — Freshness gate decision (acceptance criterion #4)

**Decision: v2 runs BEFORE `check_freshness()`, unconditionally, on every full/rebuild chain invocation. The freshness gate logic itself is not modified.**

Rationale:

1. On a weekend, holiday, or any no-new-allocations day, the freshness gate correctly identifies "no new silver allocations to process" and skips A/B/C/D. But canonical_prices still needs a row for that date — either via T3 linear_interpolation (when future known dates exist) or T4 carry_forward (when only past known dates exist). v2 must run to produce that row regardless of whether A/B/C/D runs.
2. v2's write is to `silver/prices/canonical_prices.parquet`, which does not advance `silver/allocations/`. So the gate's check logic (`silver/allocations/` latest date vs `gold/artifacts/summary/header_metrics.json` `data_as_of`) is unchanged and still correctly gates A/B/C/D. v2's run is orthogonal to the gate's semantics.
3. v2's compute cost is ~10-20 minutes on a c6i.16xlarge — cheap enough to run every boot unconditionally. No optimization warranted.
4. The gate's purpose (avoid wasteful A/B/C/D recomputation when nothing changed) is preserved.

Implementation: added a new `_should_run_silver_prep` block BEFORE the `_should_check_freshness` block in the main flow of `gold_dispatch.sh`. Scope: only `full` and `rebuild` targets auto-invoke silver-prep. Other targets (`canonical`, `downstream`, `foundation`, `silver-prep`, `single`, `group`) do not — they are manual flows where the operator is already making explicit chain decisions. If the operator wants v2 fresh in those cases, they can run `--chain silver-prep` explicitly first.

Note: this is slightly tighter than the TO draft (which also listed `downstream`). I narrowed it to `full|rebuild` because downstream (C_03..D_04) doesn't directly read `canonical_prices.parquet` and so doesn't benefit from a fresh rebuild. If future work changes that, the scope can widen trivially.

### Part 3 — Execution-block reorder in gold_dispatch.sh

Original execution order in `gold_dispatch.sh` lines 475-518:

```
1. Freshness gate check (may exit)
2. BG re-invoke (if --bg, nohup and exit)
3. Main chain (run_chain)
```

Problem: if I inserted silver-prep between steps 1 and 2, silver-prep would run on the initial `--bg` process (before the nohup exit) AND again on the re-invoked foreground process — double-running v2 for 20-40 minutes wasted per boot.

New execution order:

```
1. BG re-invoke (if --bg, nohup and exit) — moved to fire FIRST
2. Silver-prep pre-gate (if TARGET in {full, rebuild})
3. Freshness gate check (may exit)
4. Main chain (run_chain)
```

With this reorder, silver-prep runs exactly once per real execution: on a `--bg` invocation, the initial process exits at step 1, and the re-invoked foreground process falls through to step 2 and runs silver-prep once. On a non-`--bg` (direct foreground) invocation, the initial process skips step 1 and runs silver-prep at step 2 once. Either way, one silver-prep run per real execution.

Code changes in `gold_dispatch.sh`:

1. CATALOG (line ~80): added `S_00|build_canonical_prices_v2.py|--upload` as the first entry.
2. Chain definitions (line ~109): added `CHAIN_SILVER_PREP="S_00"` with explanatory comment noting it's deliberately NOT included in `CHAIN_FULL`/`CHAIN_REBUILD` (because that would run it via the post-gate `run_chain` call, defeating the purpose).
3. Target resolution (line ~446): added `silver-prep) SCRIPT_IDS="$CHAIN_SILVER_PREP"; CHAIN_LABEL="chain:silver-prep" ;;` so manual `--chain silver-prep` works.
4. Main flow (line ~469-520): moved the BG re-invoke block before the freshness gate, inserted the silver-prep pre-gate block between them, kept the freshness gate and main `run_chain` unchanged.
5. Header comment (line ~53): updated the `CHAINS:` block to document `silver-prep` and note that `full`/`rebuild` auto-run it.
6. `show_help()` (line ~315): added `silver-prep` to the Chains section of the help output.

### Part 4 — Dry-run verification (acceptance criterion #8)

Pre-loaded v2 and ticker_overrides.py into `/tmp/gold_layer_scripts/` so the sync wouldn't miss them (S3 upload happens later in the sequence). Ran:

```bash
bash data/black_diamond/scripts/gold/gold_dispatch.sh --chain full --dry-run
```

Ordering output (filtered):

```
=== Silver prep (pre-gate, 2026-04-10T18:06:47Z) ===
================================================================
  CHAIN: silver-prep-pre
  Scripts: S_00
================================================================
========================================
  S_00  (build_canonical_prices_v2.py)
  flags: --dry-run
========================================
[v2 begins executing]
...
================================================================
  CHAIN: chain:full
  Scripts: A_00 A_01 A_02 A_03 A_04 B_01 B_01b B_00 B_01b B_02 B_03 C_00 C_01 C_02 C_04 C_03 C_05 C_07 C_06 C_08 D_00 D_00b D_00c D_01 D_02 D_03 D_04
================================================================
```

Confirmed:

- ✓ `=== Silver prep (pre-gate, ...) ===` header fires FIRST
- ✓ `run_chain` for `silver-prep-pre` invoked with `S_00`
- ✓ S_00 resolved correctly to `build_canonical_prices_v2.py` with `--dry-run` flag propagated
- ✓ After silver-prep completes, `CHAIN: chain:full` fires with the full A-through-D script list
- ✓ `S_00` is NOT duplicated in the main `chain:full` list (because I deliberately did not add it to `CHAIN_FULL`)
- ✓ `--dry-run` propagates through both silver-prep and the main chain

**Incidental observations** flagged for follow-ups, NOT fixed in this TO:

1. **`CHAIN_FULL` has `B_01b` duplicated.** The main chain output shows `... A_04 B_01 B_01b B_00 B_01b B_02 ...` — `B_01b` appears in both `CHAIN_FOUNDATION` and `CHAIN_CANONICAL`. Pre-existing quirk in the dispatcher, not introduced by this TO. Worth a small tidy-up in a separate commit.
2. **`A_00.accounts_dimension.py` has a latent `--dry-run` bug.** During the dry-run test, A_00 emitted a `FutureWarning` about DataFrame concatenation with empty entries and then crashed with a traceback at line 307 → 679 → 730 → 734. Unrelated to .022 (v2 finishes cleanly before A_00 starts), but worth investigating if A_00 dry-run mode has regressed.

Neither observation blocks this TO's ship.

### Part 5 — deploy-to-ec2.sh stale comment cleanup (acceptance criterion #6)

`infra/aws/ec2/bd-gold-layer-runner/deploy-to-ec2.sh:9-12` previously listed three script categories (`code/bronze/`, `code/silver/`, `code/gold/`) as if the runner synced all three. Reality: `run-gold-layer.sh:79` only syncs `code/gold/`. The comment predated the ADVI_PRICES Lambda migration and was actively misleading — it's what caused the confusion earlier today that led to the full trigger-chain trace.

Rewrote the comment to:

- Explain that only `code/gold/` is synced to the runner
- Name `build_canonical_prices_v2.py` explicitly as the silver-prep pre-step registered as S_00
- Note that legacy silver scripts (`bd_price_update.py` host version, `inject_scoped_overrides.py`) remain in `code/silver/` on S3 as emergency manual bootstrap tools but are NOT pulled by the runner on boot
- Reference ADVI_GLDRST.022

### Part 6 — AE handoff brief (acceptance criterion #7)

Wrote `docs/briefs/ae-brief-v2-prestep-integration.md` covering:

1. **Context** — what DS shipped and why the handoff is needed
2. **Phase 1** — new EventBridge rule `bd-canonical-prices-daily` with `cron(0 22 * * ? *)` (every day including weekends/holidays), target `bd-gold-trigger` Lambda, full terraform snippet ready to drop into `infra/aws/terraform/bd-pipeline/eventbridge.tf`
3. **Phase 2** — IAM sanity check with exact `aws s3 ls` / `aws s3 cp` verification commands for the runner's instance profile
4. **Phase 3** — diff protocol for the first week of parallel operation between v2 and the existing `bd-price-update` Lambda Job 1 path. Explicit stop-ship signals listed.
5. **Phase 4** — `bd-price-update` Job 1 deprecation via env var (`ENABLE_JOB_1=false`). Phased: disable, monitor 1 week, then delete the dead code. Keep Job 2 (interpolated_prices) intact.
6. **Phase 5** — rollback plan with three escalating options (env var flip, gold_dispatch revert, EventBridge rule disable)
7. **Open questions** for AE: instance profile IAM coverage, monthly full-run overlap on the 1st, weekday cron collision between `bd-allocation-pipeline-trigger` and the new `bd-canonical-prices-daily`

Also explicitly documented what AE should NOT do (don't delete bd-price-update entirely, don't delete the existing safety nets, don't skip the parallel-run diff, don't move v2 from `code/gold/`).

### Part 7 — Upstream context sweep

The other DS committed an audit log for .021b in commit `109d4138` during this session. That commit **inadvertently swept my staged `git mv` of v2 from silver/ to gold/ into the commit** — because the rename was in the git index from earlier in this session when I started executing .022. The commit message was the other DS's audit log, but the file list included my rename. Three observations:

1. The rename is exactly where .022 wanted v2, so the sweep is not damage — it's a free partial execution of this TO's "move v2" step.
2. `data/black_diamond/scripts/gold/lib/ticker_overrides.py` was **NOT** swept (it was untracked, not staged). Still untracked at the start of Part 8. I'm `git add`ing it as part of this commit.
3. `data/black_diamond/scripts/gold/gold_dispatch.sh` edits from this session were **NOT** swept (they were in the working tree as unstaged modifications, not in the index). Still dirty and ready for commit in this TO.

Net effect: the rename is already committed under the correct author (`0.4.0_DS_ClientPlatform`) but under a different commit message (the 021b audit log). Not ideal history hygiene, but not damage. Noted for the record.

### Part 8 — Deploy cycle

| Step | Result |
|---|---|
| py_compile v2 at gold/ | clean |
| Import resolution from gold/lib/ | YF_OVERRIDES=757, TICKER_CORRECTIONS=96 |
| `bash -n gold_dispatch.sh` | OK |
| Dry-run `--chain full --dry-run` | Silver-prep → main chain ordering verified |
| Commit SHA | (filled in by commit step below) |
| Files in commit | `data/black_diamond/scripts/gold/gold_dispatch.sh`, `data/black_diamond/scripts/gold/lib/ticker_overrides.py`, `infra/aws/ec2/bd-gold-layer-runner/deploy-to-ec2.sh`, `docs/briefs/ae-brief-v2-prestep-integration.md`, `org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/ADVI_GLDRST.022.ds-v2-prestep-gold-runner-integration.md`, this session log |
| Push | (filled in) |
| S3 uploads | `s3://opal-data-bd/code/gold/build_canonical_prices_v2.py`, `s3://opal-data-bd/code/gold/lib/ticker_overrides.py` |
| S3 parity check | (filled in) |
| Runner trigger | NOT invoked — first production run deferred to AE post-brief (per TO requirement #6) |

## Files Modified / Created

| File | Change |
|---|---|
| `data/black_diamond/scripts/gold/build_canonical_prices_v2.py` | Moved from `silver/` (actual rename committed in `109d4138` via sweep; no further content change in this commit) |
| `data/black_diamond/scripts/gold/lib/ticker_overrides.py` | New (copy of `silver/lib/ticker_overrides.py`, md5 `acc7eff08facf4d7199c7847bdfcfc25`). Fixes latent import resolution for v2 + E_06/E_08/E_11/E_15. |
| `data/black_diamond/scripts/gold/gold_dispatch.sh` | CATALOG entry for S_00, CHAIN_SILVER_PREP definition, `silver-prep` case target, execution-block reorder (BG re-invoke first, then silver-prep pre-gate, then freshness gate, then main chain), header comment + help text updates |
| `infra/aws/ec2/bd-gold-layer-runner/deploy-to-ec2.sh` | Replaced stale line-11 comment about code/silver/ being synced to the runner with accurate description of code/gold/ being the only sync path |
| `docs/briefs/ae-brief-v2-prestep-integration.md` | New. Full 5-phase AE handoff (EventBridge rule, IAM check, parallel-run diff protocol, Job 1 deprecation, rollback plan) with terraform snippets and verification commands. |
| `org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/ADVI_GLDRST.022.ds-v2-prestep-gold-runner-integration.md` | Status flipped from `pending` to `complete`. |

## Compiler Tools

| Phase | Tool | Command | Result |
|---|---|---|---|
| 1 (before writing) | `comp-blast` | `comp-blast ticker_overrides` | `No nodes matching: ticker_overrides` — confirms the module is invisible to the compiler graph (not registered in any dispatched flow). Expected finding. |
| 1 (before writing) | `comp-pipescript` | `comp-pipescript io build_canonical_prices_v2` | `Unknown script: BUILD_CANONICAL_PRICES_V2` with valid-IDs list of A_00 through D_04 — confirms v2 is not in the CATALOG pre-.022. Expected. |
| 1 (before writing) | `comp-trace` | `comp-trace "canonical_prices" --direction both` | Upstream: `bd-price-update` Lambda listed as the only producer. Other matches are pricing-diagnostic E-scripts mislabelled as WRITES_S3 (they're actually READS — known quirk). Downstream: no consumers found (graph truncation). Expected. |
| 1 (before writing) | `comp-trace` | `comp-trace "bd_price_update" --direction both` | `No nodes matching: bd_price_update` — the silver-side host version `bd_price_update.py` is invisible to the compiler graph, confirming it's orphaned from the dispatched pipeline. Expected. |
| 2 (before committing) | `bash -n` | `bash -n gold_dispatch.sh` | OK |
| 2 (before committing) | `python -m py_compile` | `python -m py_compile data/black_diamond/scripts/gold/build_canonical_prices_v2.py` | OK |
| 2 (before committing) | Manual import test | `python -c "import sys; sys.path.insert(0, '.'); from lib.ticker_overrides import YF_OVERRIDES, TICKER_CORRECTIONS; print(len(YF_OVERRIDES), len(TICKER_CORRECTIONS))"` | Output: `757 96` — import resolution from `gold/lib/` works |
| 2 (before committing) | `gold_dispatch.sh` dry-run | `bash data/black_diamond/scripts/gold/gold_dispatch.sh --chain full --dry-run` | Silver-prep → main chain ordering confirmed. See Part 4 for full ordering output. |
| 3 (after committing) | `comp-blast` | (to be run post-commit) | (expected unchanged from Phase 1 — v2 is still invisible to the compiler until the compiler re-indexes to recognize new CATALOG entries; this is a known compiler gap flagged earlier today and logged in the previous session log) |

**Compiler gaps logged:**

1. The compiler graph does not index `gold_dispatch.sh` CATALOG entries for non-A/B/C/D IDs. When v2 is registered as `S_00`, the compiler should pick it up on rebuild — but currently the graph builder only recognizes IDs matching `[ABCD]_\d+\w*`. This is a follow-up for whoever owns the compiler graph.
2. The compiler does not follow Lambda-to-Lambda `lam.invoke(FunctionName=...)` edges. This was previously noted in `gold_trigger_chain_trace_and_d00c_role_split_fix.md` and is still not fixed.

`comp-build` was not run during this TO because the compiler graph's limitations for silver-layer and Lambda-to-Lambda edges make a rebuild non-productive for this work. The verification relied on direct `bash -n`, `py_compile`, and runtime dry-run instead.

## Next Steps

- **[0.6.0_AE_PartnerETL]** Read `docs/briefs/ae-brief-v2-prestep-integration.md` and execute Phase 1: terraform apply the new `bd-canonical-prices-daily` EventBridge rule with `cron(0 22 * * ? *)`. Terraform snippet is ready to paste into `infra/aws/terraform/bd-pipeline/eventbridge.tf`.
- **[0.6.0_AE_PartnerETL]** Phase 2: verify the gold runner's instance profile has read+write on `silver/prices/*`, `silver/transactions/*`, `silver/historical_prices.parquet`. Commands are in the brief.
- **[0.6.0_AE_PartnerETL]** Phase 3: start the parallel-run diff protocol as soon as Phase 1 lands. Do NOT disable `bd-price-update` Job 1 yet — wait for 5 clean business days of diff results first.
- **[Andrew]** First production run of v2 on the gold runner is the first fire of the new EventBridge rule after AE lands Phase 1. Watch CloudWatch logs for `bd-gold-trigger` + the runner's systemd logs at `s3://opal-data-bd/logs/gold-layer/` on that run. If anything looks off, invoke Phase 5 rollback from the brief.
- **[follow-up, not assigned]** `CHAIN_FULL` has `B_01b` listed twice (duplicated between `CHAIN_FOUNDATION` and `CHAIN_CANONICAL`). Pre-existing bug. Tiny fix in gold_dispatch.sh.
- **[follow-up, not assigned]** `A_00.accounts_dimension.py` `--dry-run` mode crashes with a traceback at line 307 → 679 → 730 → 734. Unrelated to .022 but noticed during verification.
- **[follow-up, not assigned]** `ticker_overrides.py` duplication between `silver/lib/` and `gold/lib/`. Cleanest resolution is to delete the orphaned silver-side consumers (`bd_price_update.py` host version, `inject_scoped_overrides.py`) and then delete `silver/lib/ticker_overrides.py`. Medium-risk work because the silver-side scripts are the emergency bootstrap tools — doing this requires a conversation with Andrew about whether we still need them as an escape hatch.
- **[follow-up, not assigned]** The compiler graph builder doesn't index non-A/B/C/D CATALOG entries and doesn't follow Lambda-to-Lambda invocations. Worth a small PR to `org/modules/graph/` to surface both. Would have saved time on both today's trace investigation and this TO's verification.
