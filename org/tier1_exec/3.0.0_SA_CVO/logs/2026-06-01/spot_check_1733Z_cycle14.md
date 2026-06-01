# /spot-check cycle 14 — 1733Z 2026-06-01 — 1 ledger-completeness note routed to AE

14 commits triaged (15 delta − 1 own). Active cycle: 2 Andrew-flagged FE data fixes deployed + Schwab re-derive PRE-EMIT map + FIND_INSURE wrong-entity gate institutionalization + Andrew visual review.

DEPLOY-ALIGNMENT (yang-pipeline yang-v2.4.10, deployed 2026-06-01T17:07:04Z):
- Macro fix (a0b18e305 values_ym YYYY-MM keying, fixes May-blank/June-filled wraparound; verified vs PKL; ws CTO GO Option-b) + Positioning VUG fix (f981f6ae6 ETF_NAME_OVERRIDES, Andrew-flagged, DE-traced 44dc78db7/e8b5ea5f2) BOTH recorded: source-map + CHANGELOG (98f0c3c52/d4e53216b). CHANGELOG confirmed newest-first convention (idx0=v2.4.10, NOT an ordering anomaly). functions_updated=[macro, positioning, benchmarks].
- FINDING ROUTED TO AE (CC COO): v2.4.10 BUNDLED a re-deploy of yang-model-portfolio-benchmarks (the BMKAUD-audited surface). BENIGN — source-map artifact_sha256 STILL IYrvZ0zN (identical to WS-5-verified revert); no code drift, WS-5 deployed-parity HOLDS post-v2.4.10; deploy!=invoke + schedule upload-held => no run/no quarantine violation. BUT AE's WS-4 ledger (4fd0f447b) "ONE deploy today" is now mechanically-stale (v2.4.10 = 2nd deploy touching the audited surface). Asked AE to append it for "every-change-to-the-minute" completeness + confirm no benchmark run fired. (Verifier ledger-truth maintenance; non-blocking, doesn't change WS-5 PASS or un-quarantine GO.)

SCHWAB RE-DERIVE: DS~B PRE-EMIT exact-vs-estimate MAP (5ae318a65) per CTO hard gate — 1/16-5/17 custody+1a MEASURED, 1c ~$25M bandaid ESTIMATE (label), pre-1/16 OLD-BASIS non-canonical (flag@1/16). MATCHES my primed 5-point verify (164639Z). Emit HELD pending CTO+Andrew confirm — I fire on re-emit-done ping.

VISUAL GATE: RD~B briefed Andrew's per-firm Daily AUA visual-review findings to CTO (4bb7a0ecc) — the portal visual smoke gate RAN (Andrew). Connects to my recurring visual-gate flag.

FIND_INSURE: rep-BD-disjoint wrong-entity gate institutionalized at pull-time (9f137abf9 standing gate MIN_HARD_DISJOINT=3 + 96018e109 wired into enrichment pull path, CTO GO); eagle-strategies CONFIRMED over-scope (NY Life PARENT id) -> REVIEW; midland LOW_CONF. Catches PMA/#79 class for all IMOs at pull-time, not manual audit.

Substance-meta: Macro wraparound (bare-month-key collision) = real bug, root-caused+fixed+PKL-verified; $25M 1c estimate-labeled (honest); no magnitude anomalies. No Tier-0 ledger. Checkpoint -> 96018e109.
