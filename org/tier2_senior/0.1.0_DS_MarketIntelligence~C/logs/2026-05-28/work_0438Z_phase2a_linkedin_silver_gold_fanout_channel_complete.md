# /work — Phase 2A LinkedIn channel silver→gold fan-out (channel #2 complete)

**Agent:** 0.1.0_DS_MarketIntelligence~C
**Cycle:** /work substantive tick (~04:37Z → ~04:38Z author; ~15min wall)
**Archetype:** IMPLEMENT (STANDING-PARALLEL readiness scaffold, stage 2 of 2)
**Trigger:** ws COO RAVC2-ACCEPT-CLOSE + DRIVE `20260528T0437Z` (LinkedIn bronze readiness ACCEPTED → complete the channel)

## Context

LinkedIn bronze dispatch readiness (`dcf65dc06`) ACCEPTED. COO DRIVE'd completion of the FULL channel-#2 fan-out (mirroring AE 0.7~A's web-scrape bronze→silver→gold) so the 99-IMO LinkedIn pipeline is instant-fire-ready end-to-end, not just bronze.

## Deliverables (added to `.runtmp/find-insure-linkedin-stage2/`)

| Artifact | Stage | Lambda | Event |
|---|---|---|---|
| `dispatch_linkedin_orgchart.sh` (prior) | bronze | find-insure-crawl-linkedin | {slug, run_date, domain, seniority_filter} |
| `dispatch_linkedin_silver.sh` (NEW) | silver | find-insure-parse-linkedin | {slug, run_date, bronze_prefix} |
| `dispatch_linkedin_gold.sh` (NEW) | gold | find-insure-score-linkedin | {slug, run_date, silver_prefix} |
| `dispatch_linkedin_channel.sh` (NEW) | orchestrator | — | runs bronze→silver→gold sequentially |

Silver/gold build per-IMO events inline via jq from the shared manifest (slug + run_date) — no extra payload files needed (events are trivial vs bronze's domain+filter complexity).

## Validation

- Silver dry-run: 99 events, prefix `corp/{slug}/bronze/...` → `corp/{slug}/silver/...`
- Gold dry-run: 99 events, prefix `corp/{slug}/silver/...` → `corp/{slug}/gold/...`
- Channel orchestrator dry-run: chains all 3 (99+99+99 staged), prints CHANNEL DONE, exit 0
- All `--execute` without gate → exit 3 BLOCKED; orchestrator `--execute` → ABORTS at bronze stage (chain halts)
- Git-Bash-3.6.7-safe (Rule 16): bash/sed/grep/comm/jq/aws/date/tr/sleep only; same CRLF `tr -d '\r'` discipline

## Auto-chain gap (documented per COO §3)

The 3 stages are NOT EventBridge-wired (no S3-PutObject→next-stage trigger at v0.x). `dispatch_linkedin_channel.sh` is the MANUAL sequential fan-out — the channel-#2 analog of AE 0.7~A's web-scrape Stage 2 precedent (dispatch tier, settle window, dispatch next). If AE 0.7 later wires S3→EventBridge→Lambda, the orchestrator collapses to just the bronze dispatch (silver+gold auto-fire). Settle window default 90s (`--settle N`); per-IMO completion polling left as a v0.x TODO (async invokes return immediately).

## Gating (all stages)

Same gate as bronze: `--execute` requires `.PHASE2A_GO` marker (Phase 1 close + Andrew Phase-2A GO) + deployed Lambda; audited `--force-gate-ack` bypass. `--subset <file>` for Andrew Q1 cut, forwarded through the orchestrator to all 3 stages.

## Channel #2 status: instant-fire-ready END-TO-END

Bronze + silver + gold dispatch infra all staged + validated. On Phase-2A-GO, `dispatch_linkedin_channel.sh --execute` runs the full 99-IMO LinkedIn org-chart pipeline in one sequence. Org-chart-only discipline (per .034) carries through — reveal deferred; the gold tier scores the org-chart leadership (named-individuals + Series-license + AUM per ~B's `6457f6861` AC3).

## LD-0116 routing

RAVC2-Request → ws COO; CC ws CTO + ws CVO. No MSTR direct.

## Next Steps

1. **[ws COO]** RAVC2-ACCEPT channel-#2 full fan-out; channel #2 instant-fire-ready end-to-end.
2. **[AE 0.7]** 3 LinkedIn Lambdas deploy (crawl + parse + score via imo-pipeline-vX.Y.Z) = the other half of fire-readiness; optional S3→EventBridge auto-chain wiring collapses the manual orchestrator.
3. **[Andrew Phase-2A GO]** bundled package (LinkedIn ToS/cost + Q1 subset-cut + Phase-2A-authorization) per COO §2 — fires `.PHASE2A_GO` marker.
4. **[~C self-loop]** /work cron next tick; .024 held on Andrew Q1.

— 0.1.0_DS_MarketIntelligence~C 2026-05-28T04:38Z
