# 0.6.0_AE_PartnerETL session log — 2026-06-05 work_1722Z (Andrew-direct demo speedup — Aho-Corasick)

**archetype:** DIAGNOSE
**secondary_archetypes:** DEPLOY, VALIDATE

## Andrew-direct: demo rebuild ~33h is absurd for name-swap+x3 — understand + fix
Andrew flagged the ~33h ETA: a name-swap + x3 should be ms/object. Diagnosed + fixed.

ROOT CAUSE: demo_transform Pass-2 per-object cost dominated by TWO O(N_identities x text) brute-force loops:
- transform_string (L500): for every string, looped ALL ~6k names doing `real in out`.
- leak_check (L588): for every object, looped ALL ~10k identities doing `real in blob`.
= millions of substring ops per object = ~5s/object. The name-swap (dict lookup) + x3 (multiply) were always microseconds.

FIX (honest, 2 iterations):
1. One-pass regex (1b9475c39): DID NOT HELP. Benchmarked the 6k-alternation regex = only ~1.5x over the loop on Py3.9 (re scans alternatives position-by-position = still O(N x text)). Caught via steady-state measurement (stayed ~13/min). Wasted a relaunch cycle -> lesson: benchmark before deploy.
2. Vendored Aho-Corasick automaton (394969a6a): O(text+matches), walks each char once regardless of N. transform_string -> AC.replace (maximal-munch, longest-first preserved); leak_check -> AC.find_words (same fail-closed detection). Benchmark @6000 names/5KB: loop 5.5ms, regex 3.6ms, AC 0.24ms = 23x/15x. Selftest PASS (incl PII leak contract), ds-commit-gate clean, fallback loop retained.

CONFIRMED on demo-reclone5: Pass-2 ~12/min -> ~250-290/min (~20x). ETA 33h -> ~80min (done ~18:40Z). Within Andrew's 1-2h on the SAME t3.large (no bigger box). Residual ~80min is now inherent JSON parse/walk/serialize on 1 physical core (AC made name-scan a non-factor); minutes would need multi-core + multiprocessing (not doing - box is cost-flagged ephemeral, Andrew said 1-2h fine).

RAVC2 CONFIRMED -> COO (172248Z). Gates unchanged: Phase C pii_leak_scan R5 + DS PII-verify on landing. Memory: reference_multisubstring_scan_use_aho_corasick_not_regex.

## Other
- GLDINC PRD v0.2 APPROVED by Andrew (46e7f5285); I LEAD; P0 CHECKPOINT first. ACK'd COO; queued behind this demo confirmation. COO confirmed no GLDINC time-pressure, finish demo first. NEXT: start P0 checkpoint design.
- Inbox Monitor died 3x (exit 143); re-armed each (bxm2rb5aa current); cron-poll backstop covers reachability. Fabric-Monitor-stability pattern worth a flag if it persists.

## Open / next
- demo-reclone5 completes ~18:40Z -> Phase C leak result -> RAVC2 completion.
- START GLDINC P0 CHECKPOINT design (per-script .done markers + auto-resume; serves R3b-Spot too) -> surface design+ACs to COO+CTO.
- bd-gold R3a validates tonight's nightly (untouched).
