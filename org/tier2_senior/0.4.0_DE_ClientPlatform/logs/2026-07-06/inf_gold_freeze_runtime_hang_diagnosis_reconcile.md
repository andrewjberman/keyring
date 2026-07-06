# INF gold FREEZE runtime-hang diagnosis + reconcile (Andrew-facing AUM-stale question)

**archetype:** DIAGNOSE
**secondary_archetypes:** COORDINATE, VALIDATE

Serial: 0.4.0_DE_ClientPlatform | Window: 2026-07-06 13:44Z (last log 4ce2af4bd) -> 15:50Z | Andrew-live-driven.

## Summary

Andrew asked what AUM we present for Inflection in PartnerAnalytics.tsx (answer: header_metrics.json
total.aua = $201,689,909.65), then flagged Orion shows $202.58M with no morning update. Traced it
to the INF gold chain being FROZEN@07-02, root-caused the runtime break to a hung dispatcher wrapper,
reconciled a conflicting read with 0.6.1, and handed COO a single reconciled read + fix sequence. No
code commits this window -- diagnostic + coordination; 0.6.1 executed the fix (COO-signed-off).

## What I did (grounded)

1. **AUM number (grounded on served artifact):** PartnerAnalytics.tsx:243 `auaDonutTotal` = primary
   `headerMetrics.total.aua` (getHeaderMetrics('inflection') -> s3://opal-data-inf/platinum/firm/
   header_metrics.json). Live value = **201689909.65** (raw JSON literal, 2 decimals; float64 display
   noise != real precision). Cross-confirmed identical by total_aua (top-level), partner_analytics
   fallback views.aua.current.metrics.aua, and certified donut.total. data_as_of 07-02.

2. **Freeze localization:** comp-freshness chain inf -- SILVER/Orion morning pull RAN + fresh
   (~13:33-13:44Z today, PASS: orion_api performance/activity/billing, silver transactions/positions/
   accounts_v2); GOLD chain FROZEN@07-02 (INF_A_00 accounts_dimension -> B -> C -> D, all ~92-93h FAIL);
   platinum served all 07-02. So today's 202.58M is in silver; gold->platinum never propagated.

3. **Runtime root-cause (SSM on inf-gold-layer-runner i-0ed5afded2ebd4ed4):** EC2 launched 13:33:25Z
   off the EVENT trigger `inf-gold-full-on-bronze-complete` (ENABLED; inf-gold-incremental-daily cron
   DISABLED) -- so event LAUNCH works; the break is RUNTIME POST-INSTANTIATION. `--chain full` procs
   (PID 3252 13:33 + 18632 14:37 retry) were state=S, wchan=do_wait, 0% CPU, ~115m/42m, ONLY child a
   `sleep 30` telemetry-sync bg loop (script L814-821); zero gold written. Script SELF-DOCUMENTS the
   class (L809-813: `run_chain | tee log` do_wait deadlock, "chain #28 hung 10min ... SSM-killed
   2026-05-13"). SELF-CORRECTED my own first read (grepped "chain-full" hyphen, real is "--chain full"
   space -> initially missed the chain proc; corrected to COO immediately).

4. **Reconcile with 0.6.1 (conflicting read -> single reconciled read for COO):** 0.6.1 read the chain
   ABORTED at INF_API_SILVER_PERF (exit=1) + lock self-released; I read HUNG (do_wait). Reconciled:
   BOTH true in sequence -- perf STEP errored (a CONTENT-vs-mtime staleness gate: perf silver file
   fresh-mtime 13:33Z but data-vintage behind the 07-06 frontier after the holiday gap), then the
   wrapper LEAKED (main()'s final wait() blocked on the never-reaped telemetry child) = do_wait linger.
   **0.6.1 corrected my over-call:** lock was NOT held (self-released, confirmed absent, re-invoke
   acquired fresh lock) -- benign wrapper-process leak, not a functional block. My process-state read
   (HUNG wrapper) held; my "blocks re-trigger" consequence was wrong.

5. **Fix in flight (0.6.1 executed, COO-signed-off):** killed the 4 leaked wrappers -> lock free ->
   re-invoked inf-gold-trigger full with ceiling=10 (defers the perf content-staleness gate). Verified
   the fresh run PID 31251 is PROGRESSING: child python3 pull_inflection_transactions_rest.py state=R
   8.9% CPU under a `timeout -k 30 600` wrapper. So it's past the perf gate + actively running gold.

## Compiler Tools

| Tool | Run | Result | Note |
|---|---|---|---|
| comp-freshness | chain inf (x3) | FAIL(gold)/PASS(silver) | localized freeze: silver fresh 07-06, gold+platinum frozen 07-02 |
| comp-which | "what is the inf gold layer runner doing / progress" | routed | surfaced comp-freshness/comp-pipescript/comp-platinum; ran comp-freshness |
| (rail gate) | aws s3 ls gold/dimensions/ | GATED->re-routed | Rule-21 hook gated raw s3-ls freshness; correctly re-ran via comp-freshness |

**What worked:** comp-freshness chain inf cleanly split silver-fresh vs gold-frozen -- the localization
that scoped the whole investigation. **What failed:** none. **Gap found:** none new (the comp-rail
correctly caught my raw s3-ls freshness eyeball). Grounding note: the runtime root-cause required raw
SSM (ps state/wchan/child-tree, /proc, script source) -- process-level truth the comp-tools don't
surface; operational SSM/aws, off-rail.

## Current State

- **AUM presented (inf PartnerAnalytics):** $201,689,909.65 (header_metrics.json total.aua, data_as_of
  07-02). STALE vs Orion 202.58M because gold->platinum frozen.
- **INF gold freeze:** ROOT = perf CONTENT-staleness gate abort (exit=1) + a wrapper-process reap LEAK
  (do_wait on unreaped telemetry sleep-30 child). Lock self-releases correctly (benign leak, not held).
- **Fix in flight:** 0.6.1 killed leaked wrappers + re-invoked (PID 31251, ceiling=10) -- PROGRESSING
  past perf, running gold steps at ~15:50Z. 0.6.1 watcher keys on INF_A_00 -> 07-06 (~15:55-16:00Z).
- **Durable fixes (0.6.1 lane, accepted):** (a) reap telemetry child + fix run_chain|tee teardown, (b)
  dispatch-lock TTL / hung-holder detect, (c) bound silver steps with timeout, (d) perf gate should key
  on content-vintage + a sane post-holiday ceiling (WS-4 content-vs-mtime class).
- **WS-4 AC-2 intersect:** my per-dim oracle + DS~A's 3 emits are in-path; they serve on the SAME
  gold->platinum completion -> this un-freeze also unblocks the AC-2 close.

## Next Steps

- **[0.6.1_AE_PartnerETL]** own the re-invoke watch (INF_A_00 -> 07-06) + the 4 durable fixes; ping me
  if PID 31251's WRAP-UP hangs (gold produced but wrapper won't exit) -> I py-spy/lsof the tee pipe FDs
  to name the holder = teardown root for durable (a).
- **[2.0.0_SA_COO]** holds the go/no-go; has the reconciled read + fix sequence; relaying the watch outcome.
- **[0.4.0_DE, me]** SERVING VERIFY on gold->platinum completion: confirm platinum flip (AUM 201.69M
  -> 202.58M) + the WS-4 as_of_by_dim maps land on all 3 emits -> then support CVO AC-2 re-cert. Report
  the number-flip to Andrew.
