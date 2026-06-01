# ws CTO session wrap — 2026-06-01 (~2148Z)

**Agent:** 1.0.0_SA_CTO (ws CTO) · **Loop:** /ws-charter 30m cron · **Mode:** Andrew-direct + autonomous in-lane
**Headline:** A deployment-integrity day. Everything Andrew raised is code-complete + verified; the entire remaining critical path collapses to ONE step — the AE CloudOps smartx-exporter Docker rebuild — which is SAFE-HELD pending Andrew's Docker Desktop + a MSTR respawn (his push-vs-ride tempo call).

---

## 1. Directives handled this session (Andrew-direct)

| # | Directive | Outcome |
|---|---|---|
| BMKAUD | Quarantine Benchmark + Peers tabs; Yang PKL = source of truth; audit all changes/terraform "to the minute"; full team | RESOLVED. Benchmark vindicated (CVO 40/40 vs raw Yang); Peers UST-1M = FE falsy-zero bug (fixed, live PROD v2.1.107/109). SmartX lock-down plan authored (AE, held for Andrew ratify — rec: NO break-glass). |
| Redeploy + invalidate | Redeploy portal+data, invalidate CloudFront, "make certain correct numbers display" | DONE — AE reran lambdas + invalidated; correct data confirmed on localhost + opalinvest.dev (DS log 1345Z). |
| Cohort 1c | Historical 1c; FE rolls 1b+1c in Daily AUA; backend keeps split; cohorts were "backwards" | Taxonomy corrected: 1a=SmartX model, 1c=SmartX SMA, 1b=plug (Schwab−1a−1c). Folded into the 49F re-derive PRD. |
| VUG casing | Positioning all-caps "VANGUARD GROWTH ETF" → in-pattern fix | DONE (per-ticker full-name override map; DE-caught source was all-caps AND truncated). |
| Macro anomaly | May-blank / June-filled despite Yang 5/29; "does it lag that much?"; YALP_MACRO | ROOT-CAUSED. May-blank = GENUINE release-lag (monthlies end April, May unreleased — verified per-indicator). June-filled = bare-month-key collision (fixed values_ym; live PROD v2.1.109). Andrew's lag skepticism was correct. |
| Yield-curve | 1Y-ago missing {1M,3Y,20Y,30Y}; "find exactly what changed, maybe TF modules, artifact/path flux" | ROOT-CAUSED + GO'd. NOT a TF/path swap (hypothesis REFUTED): latent FRED partial-overwrite bug (no retry → empty-tenor → clobbers prior good artifact), exposed by the May-21 runner revival. The {1M,3Y,20Y,30Y} vs {1M,3Y,10Y} "mismatch" = different S3 versions (set varies daily). Fix = retry+merge-preserve (data-honest; historical tenors immutable). Validated 10/10 pre-deploy (921a80ac3); code → AE deploy. |
| comp-aws | Batch compiler over ALL AWS (TF/lambda/EC2/Dynamo/S3/"everything"); hand-audit until "categorized, typed, perfect"; gzipped-tarball shape archive each run | PRD authored (d425e072f) + comp-lambdamap PRD (f9e70457a). Timing RULED by Andrew (via COO): HOLD schema build until 3 co-primaries clear → full fabric redirect. Schema-design lane stands ready. EC2-edge scope enriched empirically (see §3). |
| Bell-curve footer | Lineage for "Excludes N unfunded" footer (Global 14 / 49F 201 / Inflection 6639); Inflection "not the correct intent"; write PRD → COO | PRD authored (c7ec02f76) + 4 amendments. Root cause = cross-grain SCOPE bug (global metrics − per-firm distribution). DATA-LAYER fix COMPLETE all 3 firms (6639→5; 49F→2; global 6838; by_model reconciled). See §2. |

---

## 2. Bell-curve durable fix — the session's biggest data deliverable

- **Root cause:** the footer count is an FE subtraction `metrics.account_count − distribution.account_count`; metrics is GLOBAL-only, distribution is PER-FIRM → every per-firm footer computed global−firm (Inflection 6639 = 7039−400; 49F's 201 was masked-wrong too; only Global's 14 was right).
- **Durable fix (option b):** producers emit `excluded_unfunded_count` directly at accounts-grain. PROVEN: 6639→5 (Inflection), 49F→2; reconciled Σ(by_model)=total on all firms.
- **CTO rulings:** (i) per-model footer L1009 IS in-scope (`by_model` field required — same bug class, compounded for Inflection's client-grained model distribution); (ii) PRODUCER CORRECTION — the footer reads `account-distribution.json` from `compute_per_firm_account_distribution.py` (49F+inf) + `compute_account_distribution.py` (global), NOT `09/INF_09.generate_partner_analytics` (DE-caught before propagation); (iii) §2 = run the unified per-firm producer in the smartx daily DAG (option a) with fail-soft + edge-track guardrails, defer the standalone-MDPF-pipeline split.
- **Status:** AC1-AC4 (DATA) COMPLETE all 3 firms incl per-model (3445d7f23). Workers executed: DAG-wiring (016a763c8), by_model (f201e7485), §3c drift-guard (79568df53). Remaining = EC2 redeploy (durability) + RD FE read-direct cutover + AC5 visual.

## 3. smartx deployment-integrity finding (CTO architecture territory) — the day's structural catch

- **Finding (AE-surfaced, COO-escalated):** "what we commit ≠ what runs in prod." The smartx-exporter daily run executes a Docker-baked bundle copy; the deployed **ECR image is Jan-14 — ~4.5 months stale** (older than even the Feb-20 repo bundle). Every smartx-exporter change since Jan-14 (incl. 2 Jan-21 "CRITICAL" AUM fixes) never reached prod via the image.
- **Blast-radius (my RAVC2s):** the DAILY-RUN DAG is CLEAN post-AE-sync — the scary divergences (compute_non_model_assets 357-line [retired], aggregate_to_timeseries 175, etc.) are all OUTSIDE the daily DAG. Contains the incident to "structural hazard + one file," NOT 4.5mo of corrupted daily output.
- **Key catch:** `config.py` divergence is INTENTIONAL env-specialization (bundle = EC2 Docker `/opt/...` paths; canonical = Lambda+Windows-local) → a naive "canonicalize + copy" would CLOBBER the EC2 paths and BREAK the daily run. The durable fix MUST be env-aware.
- **Re-derive dependency (don't-assume-safe → RESOLVED safe):** flagged that the just-closed Schwab re-derive could sit on stale-exporter output. Workers confirmed (1308043ab): 49F `1a` reads raw SmartX daily-export CSVs (bypasses the aggregation layer), INSULATED → stays closed.
- **Durable architecture (my call, folds into comp-aws):** (a) build-time sync logic scripts FROM canonical; (b) env-detecting `config.py` (add IS_EC2 branch); (c) interim CI drift-guard — SHIPPED (79568df53, 0 drift). The EC2 declared-vs-deployed edge is a THREE-STATE reconcile: image(ECR) < bundle(repo Docker-source) < canonical(edited tree), env-specialization-aware. Empirically strengthens the comp-aws thesis (2nd "commit≠runs" class after lambda-source-map).

## 4. Owned-paths ruling (CTO territory)

MDPF distribution producers are DS-authored but live in `data/smartx/**` (Andrew-direct-ruled AE lane 2026-05-15). Ruled: relocate is OUT (deployed smartx-pipeline components); recommend (b) co-own the 2 files (AE+DS) via narrow `.owned-paths.yaml` entry — **Andrew-confirm-gated** (narrows his direct ruling). Interim AE-commit-handoff holds.

---

## 5. Current state (end of session)

- **Single remaining critical-path step:** AE CloudOps smartx-exporter Docker rebuild + redeploy → lands BOTH the bell-curve durable-close (permanent global fix + closes 4.5mo staleness) AND the yield-curve lambda. **SAFE-HELD + deadline-free** (daily-trigger held = no overnight revert; live global correct; yield-curve dropout pre-existing-intermittent).
- **Blocker:** the AE pod session-wrapped (f5c64a9ca); a respawn alone is insufficient because the env Docker daemon is down — needs Andrew's Docker Desktop + a MSTR CloudOps respawn. = Andrew push-vs-ride tempo call (COO surfacing, safe default = ride).
- **CVO:** conditional global cert STANDS unsatisfied until the actual deploy + next-daily-run proof (ship≠deploy — correct discipline).

## 6. Andrew decision queue (all non-blocking)

1. **push-vs-ride TONIGHT** — start Docker Desktop + "push" to close bell-curve+yield-curve tonight, or ride to next session (safe default = ride).
2. SmartX lock-down apply-ratify (rec: NO break-glass).
3. pre-1/16 disposition — rec B (flag-as-legacy/honest); CTO+DS~B concur.
4. FIND_INSURE universe A/B.
5. Macro current-month UX (blank vs latest-labeled) + Positioning/Macro visual eyeball.
6. owned-paths confirm (co-own the 2 MDPF-distribution files AE+DS).
- comp-aws kickoff = RULED (hold-then-redirect on 3-coprimary-clear) — off queue.

## 7. ws CTO commit ledger (this session, representative)
914faabd5 (BMKAUD brief) · d425e072f (comp-aws PRD) · f9e70457a (comp-lambdamap PRD) · c7ec02f76 + 29b310e4f + dcc23f4c0 + 4294cc6ee + d62717074 (bell-curve PRD + amendments) · MDPF 49F re-derive PRD amendments · cycle logs (9b6ad9279 / 8bfdd3228 / a4b3790ef) · ws-charter-cycle 0023/0024 tags.

## 8. Next-session pickup
- Watch for: AE respawn + Docker Desktop → bell-curve durable-close (EC2 redeploy + daily-run proof) + yield-curve deploy + verify (10/10 tenors) + RD FE cutover + AC5 visual → CVO lifts conditional cert.
- On 3-coprimary-clear: COO fires comp-aws redirect → I author the node/edge schema (EC2 three-state reconcile + cross-pipeline edge + env-aware, per §3).
- Andrew queue items above.
