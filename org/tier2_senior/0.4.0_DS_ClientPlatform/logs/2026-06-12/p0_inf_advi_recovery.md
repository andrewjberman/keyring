# 0.4.0_DS_ClientPlatform — ANDREW-TIMED P0: inf ADVI staleness recovery (4-layer)
**archetype:** DIAGNOSE
**secondary_archetypes:** DEPLOY, COORDINATE
**Window:** 2026-06-12 ~20:36Z -> ~21:30Z (since 2b6d1a491)

## Summary

Andrew-direct P0 (GO 20:37Z via CTO trace): ADVI inf served 06-11/$202M vs Orion $204.6M.
Recovery lane executed in full; doc-of-record = `docs/briefs/inf-advi-staleness-p0-recovery-20260612.md`
@ a3f53eeb7 (complete clock + root-cause + follow-ups a-h). Compressed here:

- **L1 (CTO's trace):** `code/bronze-runner/` stale (May-8 7-dim orchestrator). Plus my find: the
  on-instance `inf-bronze-fetch.sh` (bootstrap-baked May-1) lays scripts at `data/orion/` while the
  current orchestrator resolves `data/inf/` — orchestrator-only sync would have failed every dim.
  Fixed: 9 files repo->S3 (ETag-verified) + on-instance refresh; EC2 txn re-fire landed
  `bronze/orion-api/2026-06-12/transactions.csv` 20:52:59Z. (1 retry: `jwt_freshness.py` missing on
  the prefix — my import pre-scan had silently failed on conflicting grep -E/-P flags; re-scanned
  via python AST-free regex, jwt_freshness = the only non-stdlib import.)
- **L2:** `inf-api-txn` (the canonical txn leg) fired today as always but its date DEFAULT = now-1d ->
  today's run completed YESTERDAY's quorum; `_silver_complete/2026-06-12/` sat 8/9 (8 same-day dim
  lambdas + the D-1 laggard). Direct-invoked `{"date":"2026-06-12"}` -> 200 -> quorum 9/9 ->
  `_AGGREGATOR_FIRED` -> inf-gold-trigger 21:07:16Z.
- **L3 (the morning-crash cause):** gold chain died INSTANTLY both at 13:00Z (scheduled; held the
  dispatch lock 8.1h, no log, no alarm) and at my 21:07Z dispatch — `sync_scripts()` basename-collision
  FATAL: `_orion_api_silver_lib.py` + `build_assets_dim.py` in `code/gold/` (May) vs `code/silver/`
  (06-11 16:08 cutover uploads) with different content. Fixed per the guard's own prescription:
  verified repo==code/silver canonical (md5==ETag), overwrote the code/gold twins, byte-identical
  verified. Cleared the dead lock (`NO-CHAIN-PROCESS` evidence, lock-full-5288d152539c) — the
  trigger's own stale-clear path executed early instead of burning 80min TTL. Re-dispatched 21:18:14Z;
  chain verified ALIVE past the guard (REST txn pull, 864 accounts).
- **L4 (CTO scope extension):** Eclipse dark at 06-11; MP model leg rides it; mdpf auto-fires on
  `pipeline-complete.json`. Ground truth: eclipse = the gold chain's POST-SENTINEL block (not the
  bronze-runner bundle) -> it rode L3 down. Pre-landed `--chain eclipse` concurrent (no self-lock,
  verified): bronze+silver+gold/eclipse/2026-06-12/ + sentinel at 21:25:01Z, ~1h43m before
  pipeline-complete. **NEAR-MISS:** the eclipse completion armed the runner 2-min auto-shutdown under
  the live full chain — cancelled via SSM with ~60s margin (follow-up h).

Also in window: ADVI_COTSNP.P0 TO ACK'd (tomorrow-AM queue, zero tonight action) + TO #5 interface
constraints delivered to AE 0.7 (4 constraints from the live forensics: FATAL fires on-instance
pre-log-upload via AWS-native primitive; lock-state resolution not just alerting; alert-before-
shutdown-arm; quorum-deadline RED for the silent-partial class).

## Deployment Sequence + Verification (S3 artifact model; all content = already-committed repo files)

```
code/bronze-runner/: orchestrator.py + inf-bronze-fetch.sh + 7 manual_api scripts + jwt_freshness.py
  -> all md5==ETag MATCH (verified per file post-upload)
code/gold/: _orion_api_silver_lib.py + build_assets_dim.py overwritten with canonical
  -> IDENTICAL across code/gold + code/silver (ETag== verified)
SSM: txn re-fire (473461eb retry after 0699d592 jwt-miss) -> [transactions] OK exit=0;
     bronze csv landed 20:52:59Z 1.2MB (head-object verified)
Lambda: inf-api-txn {"date":"2026-06-12"} -> 200 {"empty_day": false}; sentinel verified
Lambda: inf-gold-trigger -> SSM de221d6c, lock-full-816b520f05ad; chain log tail shows
     [200/864] REST pull progressing
Eclipse: --chain eclipse SSM 8e5a3781 -> CHAIN COMPLETE 21:25:01Z; gold_complete sentinel verified
```

## Compiler Tools

None run this window — live-AWS P0 incident forensics (S3 head-object/ls, SSM, Lambda invoke, CW
logs/metrics); Rule-20 dependency assessment was CTO's graph trace (2 comp-kuzu queries, cited in the
GO), and per F5 my own changes were verified against live AWS state, never the graph. Note: follow-up
(c) extends comp-pipescript deployed-checks to the bronze-runner prefixes this incident exposed.

## Briefs Written (DS)

| Brief | Path | Commit | Status |
|---|---|---|---|
| P0 recovery report (4-layer root cause + clock + follow-ups a-h) | docs/briefs/inf-advi-staleness-p0-recovery-20260612.md | a3f53eeb7 | R4 served-verify pending chain completion |

## MCP Traffic

~8 substantive (excl. re-surfaces): CTO P0 GO -> my PROGRESS 1/2/3 (quorum+gold dispatch; collision
root-cause; eclipse landed + near-miss) -> CTO direction (inf-api-txn lane + 2 corrections) -> CTO
scope extension (eclipse/mdpf) -> COO COTSNP.P0 TO cut + my ACK -> AE 0.7 TO #5 kickoff + my
constraints reply.

## Blockers

None. Remaining work is event-gated (chain completion ~23:08Z), not blocked.

## Current State (zero-context handoff)

- **Gold chain RUNNING** on i-0ed5afded2ebd4ed4 (dispatched 21:18:14Z, SSM de221d6c,
  lock-full-816b520f05ad; ETA ~23:08Z per 06-11 precedent 1h49m). On completion it writes
  `s3://opal-data-inf/gold/meta/pipeline-complete.json` -> mdpf-daily-trigger auto-fires -> mdpf
  Stage 0.5 resolves TODAY's eclipse gold sentinel (landed 21:25:01Z) -> MP refreshes.
- **Monitor armed** (task bsuilrlqn): fires when `platinum/firm/partner_analytics.json` LastModified
  moves off the 06-11 14:48:20 GMT baseline, or on gold-SSM terminal failure.
- **R4 on fire:** verify BOTH pages — ADVI platinum (partner_analytics + header_metrics_fresh,
  AUA ~$204.6M) AND Model Portfolios (fresh mdpf partition ~205M + eclipse model leg). Then R5 final
  stamps to CTO/COO/Andrew.
- All deploys = repo-committed content; zero repo code changes were needed; bronze-runner instance
  self-stops via watchdog.
- DEFERRED EXPLICITLY: tonight's 02:00Z cot baseline untouched by all of this (inf-side only).

## Next Steps

1. ON MONITOR FIRE: R4 both-pages served-verify + R5 timestamps -> CTO/COO ([1.0.0_SA_CTO],
   [2.0.0_SA_COO]); close the P0.
2. Structural follow-ups a-h -> [2.0.0_SA_COO] TO cuts (interface constraints already with
   [0.7.0_AE_CloudOps] for TO #5).
3. Tomorrow AM (unchanged): ADVI_COTSNP.P0 (qt3/qt4 review -> TABLE_CONFIG deploy -> holdings.json
   parity) + NFRA_COT_RULE15 pending COO drive.
