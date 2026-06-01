# /ws-charter event-driven action — 2026-06-01 ~2102Z

**CLASS:** FIX (DRIVE_ESCALATION from COO → deployment-architecture blast-radius assessment; my territory per CLAUDE.md Rules 7-12)

## Trigger
- **2.0.0_SA_COO [DRIVE]** (205101Z): STRUCTURAL deployment-integrity finding (AE-surfaced during bell-curve TO-B global fix). The smartx-exporter EC2 daily run executes the **Docker-baked bundle copy** at `infra/aws/ec2/smartx-exporter/smartx-workspace/scripts/` (Dockerfile L62-63), a SEPARATE COPY from canonical `data/smartx/scripts/` where edits land. They DIVERGED → "what we commit ≠ what runs in prod." Asks: (1) blast radius (what else diverged), (2) durable architecture (canonicalize / build-sync).

## Finding (RAVC2 to COO, 210234Z)
- **DAILY-RUN DAG is CLEAN post-AE-sync (low prod risk now):** run_smartx_pipeline.py @14:16Z invokes only consolidate / aggregate_by_transaction_dates / compute_account_distribution (SAME — AE ported 9dfb66dcb) / generate_timeseries + pipeline_monitor + config. All SAME except config (env-specialized).
- **Diverged files are OUTSIDE the daily DAG** (no silent daily-run corruption): compute_non_model_assets 357-line (RETIRED 51ffcbf65), aggregate_to_timeseries 175, precompute_views 62, validate_canonical_aum 45, aggregate_to_daily 24, + 4 trivial 2-line. CANON-ONLY (never bundled): compute_per_firm_account_distribution.py (the TO-B per-firm producer!), backfill_non_model_assets, pull_model_monthly, sxpl_probe, validate_non_model_reconcile.
- **§2 trace handed to DS~B/AE:** compute_per_firm is CANON-ONLY + NOT in the daily DAG (DAG calls compute_account_distribution = global only) → how does per-firm (49F/inf) bell-curve data regenerate recurringly? Confirm before calling bell-curve durable-closed.
- **CRITICAL durable caveat:** config.py divergence is INTENTIONAL env-specialization (bundle = EC2 Docker `/opt/...` paths; canonical = Lambda + Windows-local). A naive canonicalize+copy would CLOBBER the EC2 paths and BREAK the daily run. So durable architecture must be env-aware: (a) build-time sync logic scripts FROM canonical (Dockerfile COPY from data/smartx/scripts/), (b) make config.py fully env-detecting (add IS_EC2 branch), (c) interim CI/verify-ec2.sh diff-guard. This is the **EC2-bundle analog of the lambda-source-map drift** → folds into **comp-aws** EC2 node + declared-vs-deployed edge (empirically strengthens the comp-aws thesis).

## Disposition
- AE doing the immediate fix (port + Docker redeploy before tomorrow 14:16Z) — correct + sufficient for THIS file.
- Durable (a/b/c) → COO decomposes; the categorical check folds into comp-aws EC2 scope (fires post 3-coprimary-clear).
- Andrew heads-up delivered (deployment-integrity).

## Follow-on
- DS~B/AE: confirm per-firm bell-curve regen path (§2).
- comp-aws EC2 edge: declared(canonical)-vs-deployed(Docker bundle) drift, categorical — banked into comp-aws scope.
