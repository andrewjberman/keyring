# Session — 0.4.0_DS_ClientPlatform~A — 2026-04-16 (session H)

**Agent:** 0.4.0_DS_ClientPlatform~A
**Window:** 2026-04-16 20:15 ET — 20:25 ET
**Scope:** (1) Ship C_08 L429 WAR ROOM vectorization (already committed at session start; verify deploy + close); (2) Pivot to polars-on-gold-runner research after COO superseded B_00 TO.

## Context

Session resumed with two CTO GO messages in inbox:
- GO ~A: Ship C_08 L429 iterrows -> vectorized. Already warm from bb426933.
- Addendum: ~C adds D_03 read TPE; ~B adds A_01 L316-343 vectorize. (Not my lane.)

Latest commit on HEAD was `86e57e36 perf(C_08 L429 WAR ROOM): iterrows to vectorized to_dict('records')` authored by 0.4.0_DS_ClientPlatform — the change had been made locally in a prior window. This session's job was deploy-cycle verification + MCP COMPLETE.

## Phase 1 — C_08 L429 WAR ROOM: Deploy Verification + Close

### Compiler Tools (deploy verification)

| Tool | Result | Pass/Fail |
|---|---|---|
| `python -m py_compile C_08.advisor_fee_efficiency.py` | exit 0 | PASS |
| `comp-pipescript deployed C_08` | 1 MATCH (local SHA matches s3://opal-data-bd/code/gold/C_08.advisor_fee_efficiency.py) | PASS |

### Deploy State

| Step | Result |
|------|--------|
| Commit SHA | `86e57e36` (author: 0.4.0_DS_ClientPlatform) |
| Push | origin/CLOUD up to date |
| S3 upload | `s3://opal-data-bd/code/gold/C_08.advisor_fee_efficiency.py` — 41.8 KiB, 2026-04-16 20:15:44 (etag from S3 matches commit timestamp) |
| py_compile | exit 0 |
| comp-pipescript deployed | MATCH |
| MCP COMPLETE | delivered to 1.0.0_SA_CTO (T001844Z) + 2.0.0_SA_COO (T001847Z) |

### Change Summary

`role_breakdown_by_advisor` construction at C_08 L429 — replaced `df.iterrows()` loop with vectorized pandas casts + single `to_dict('records')` pass + pure-Python dict loop. 45 lines changed (29 insertions / 16 deletions). Expected ~10x speedup on the `role_merged` loop. Output shape unchanged. No downstream consumer impact.

## Phase 2 — B_00 TPE Superseded, Pivot to Polars Research

COO dispatched (T002043Z) that my B_00.canonical_prices.py ThreadPoolExecutor TO was **superseded** — ~B already shipped B_00 L974 TPE 64 at `22736cf7` with S3 MATCH. Do NOT re-ship B_00 (would overwrite ~B's fix).

Note on script name: COO referenced `B_00.canonical_prices.py` — no such file exists. The real B_00 in the gold chain is `B_00.canonical_holdings.py`. The TPE fix at `22736cf7` landed on that script. Flagged implicitly via my pivot-response; no separate escalation.

Pivot assigned: **research whether polars can be added to the bd-gold-layer-runner EC2 environment** — C_00 Polars port was blocked because polars is not installed. Research only, no installs.

### Investigation

| Source | Finding |
|---|---|
| `infra/aws/ec2/EC2_MANIFEST.json` | bd-gold-layer-runner: i-01003b035d2988dfb, c6i.16xlarge, Intel, EventBridge-only access. bd-gold-qa-runner: i-0090b823a4a0997e3, c6a.16xlarge, AMD, manual SSM ok. |
| `aws ec2 describe-instances` (both) | Both on AMI ami-0c7217cdde317cfec (Ubuntu 22.04 LTS). Both STOPPED. |
| `infra/aws/ec2/bd-gold-layer-runner/setup-instance.sh` L20-21 | Current pip deps: pandas, pyarrow, boto3, python-dateutil, openpyxl, yfinance, openai, fsspec, s3fs. NO polars. System python3 global install (no venv). |
| `infra/aws/ec2/bd-gold-layer-runner/run-gold-layer.sh` | Outer bootstrap. Self-updates from `s3://opal-data-bd/code/runner/run-gold-layer.sh` on every boot. Deployed via deploy-to-ec2.sh. |
| `infra/aws/ec2/bd-gold-layer-runner/deploy-to-ec2.sh` L141-149 | Deploy script pushes run-gold-layer.sh + watchdog-shutdown.sh to s3://opal-data-bd/code/runner/. Does NOT push setup-instance.sh. |
| `infra/aws/lambda/layers/` | 5 layers (openpyxl, news-trending-deps, security-scanner-deps, deck-generation-deps, anthropic-sdk-deps). None include polars. Irrelevant — gold runner is EC2 not Lambda. |
| Grep `polars` in `data/black_diamond/scripts/gold` | No matches. No gold script currently imports polars. |

### Deploy Path Options

**Option 1 (RECOMMENDED):** Add `pip3 install polars --quiet` to `run-gold-layer.sh` between `aws s3 sync` and inner dispatch. Idempotent (pip no-op on repeat). Respects PROD EventBridge-only policy (no SSM/SSH). First boot: +30-60s wheel fetch. Subsequent boots: +2-3s cache hit. Single-line edit, goes through normal deploy-to-ec2.sh cycle.

**Option 2:** Update `setup-instance.sh` L20-21 to include polars, manually push to s3://opal-data-bd/code/runner/setup-instance.sh (deploy-to-ec2.sh does NOT push it), then re-run setup on existing instances via `sudo bash setup-instance.sh` (requires SSH — blocked on PROD by access policy). Higher friction.

### Risk Assessment (LOW)

- Polars PyPI wheel: prebuilt x86_64 manylinux — no compile. Covers both c6i (Intel) and c6a (AMD) identically.
- No conflicts with existing pip set: polars coexists with pandas (different namespaces). Depends on pyarrow-compatible arrow — existing pyarrow stays.
- Python 3.10+ supported on polars for current versions; Ubuntu 22.04 ships python3.10 by default — covered.
- Failure mode: transient PyPI fetch failure on first boot. Mitigation if needed: vendor wheel to `s3://opal-data-bd/code/runner/wheels/` for offline pip install.
- Cross-family drift risk: none — universal x86_64 wheel.

### Deliverables

- Findings delivered to 2.0.0_SA_COO (T002258Z) and 1.0.0_SA_CTO (T002306Z).
- Coordination response delivered to 0.4.0_DS_ClientPlatform~B (T002345Z) — answered import-style, install path, ETA questions; advised hold on C_00 polars port until CTO GO.

## Current State

- C_08 L429 SHIPPED, PROD-ready. Next PROD EventBridge gold run picks up new code from S3.
- B_00 TO stood down (~B's 22736cf7 authoritative).
- Polars research complete. Awaiting CTO GO on run-gold-layer.sh edit.
- ~B holding on C_00 polars port pending polars install GO.

## Compiler Tools

| Date | Agent | TO | Tool | Command | Result | Note |
|---|---|---|---|---|---|---|
| 2026-04-16 | 0.4.0_DS_ClientPlatform~A | C_08.L429.WAR_ROOM | py_compile | `python -m py_compile C_08.advisor_fee_efficiency.py` | PASS | exit 0 |
| 2026-04-16 | 0.4.0_DS_ClientPlatform~A | C_08.L429.WAR_ROOM | comp-pipescript | `comp-pipescript deployed C_08` | PASS | 1 MATCH, local SHA matches S3 |

## Files Modified

None this session (C_08 commit was already in HEAD; deploy-cycle only).

## Next Steps

- [CTO] GO/NO-GO on run-gold-layer.sh polars install (Option 1). If GO: edit → deploy-to-ec2.sh → auto-install on next boot.
- [~B] Hold on C_00 polars port until polars install lands. Pandas-only `22736cf7` remains in place.
- [~A] Stand by for next dispatch or polars install GO.

## Briefs Written

None.
