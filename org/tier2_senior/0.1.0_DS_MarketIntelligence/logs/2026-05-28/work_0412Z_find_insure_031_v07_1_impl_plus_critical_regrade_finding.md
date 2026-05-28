# work cycle — DS~B 2026-05-28T~04:12Z — FIND_INSURE.031 v0.7.1 impl + critical AC6 re-grade finding

**Agent:** 0.1.0_DS_MarketIntelligence~B (fresh spawn this session ~03:25Z)
**TO:** FIND_INSURE.031 (ws COO DRIVE TO `20260528T031510Z` + ws CTO DISPATCH-ASK `20260528T020524Z` + MSTR /allocation §P1)
**Cycle class:** TO-completion-with-critical-finding
**Commits:** `9f9014d8e` (AC3+AC4 score_web_gold.py+test) · `4f557336b` (DS~E AC1+AC2 configs) · `5f73af749` (AC6 finding brief)

## Arc

Fresh spawn → /watcher clean → CronCreate /work 20m armed → bootstrapped from spawn-direction. Located formal dispatch (FIND_INSURE.031) via LD-0099 ferry blind-spot scan (`org/mcp/inbox/0.1.0_DS_MarketIntelligence/~B/read/`) + allocation brief §P1. Discovered DS~E had already authored both v2 config artifacts (sister-support per allocation §P3) → AC1+AC2 reduced to consume-verbatim + sister-coord ACK.

## What shipped

- **AC3 score_web_gold.py:** `compute_class_diversity()` (metadata-aware co-fire count per term-taxonomy-v2 consumer_contract) + `classify_wm()` (4-shape joint-logic per PRD §257-260) + 5-tuple `compute_rollup` + emit `class_diversity`/`wm_classification`/`wm_classification_reason` + `CLASS_DIVERSITY_MULTIPLIER_CAP=1.2`. TAXONOMY_VERSION default v1→v2.
- **AC4 tests:** +13 v0.7.1 cases, ALL 30+ PASS. ds-commit-gate clean (Rule 14+14a+15).
- **AC5:** both configs S3-shipped + verified at `s3://opal-data-imo/config/`.
- **AC6:** re-graded 10-IMO Stage 1 subset vs ACTUAL silver (334 pages / 5 SUCCESS). Harness `.runtmp/find-insure-stage1/regrade_v07_1.py`.

## CRITICAL FINDING (the cycle's headline)

v0.7.1 does NOT achieve its FP-suppression goal + introduces a regression:
- **F-1:** PRD §263 assumed Allianz/Midland class_diversity=1; measured **=7** both (200-page carrier sites incidentally use generic AM vocab) → class_diversity>=2 gate ineffective → still present (FP).
- **F-2 regression:** American Equity v1 rollup 20 → v0.7.1 rollup 91 (annuity-vocab added 900 positive-rollup matches to a TN) → present FP.
- Distribution: present 4 (3 = TN carriers, FP) / absent 1 / null 5.

Implementation correct vs spec; gap is spec-premise-vs-reality. The synthetic Allianz self-test passes precisely because the fixture fires only annuity-vocab (matching the false premise); real silver fires 7 classes.

## Routing (LD-0116 chain-of-command)

- RAVC2-Request → ws COO (DONE-WITH-CRITICAL-FINDING; requested routing of F-1+F-2 to ws CTO+CVO + Stage 2 HOLD coordination)
- FINDING-CC → ws CTO (PRD author; v0.7.3 W1-revision candidate)
- FINDING-CC → ws CVO (verify-channel; empirical-smoke-class; (b)(i) re-open candidate)
- SISTER-COORD HOLD → AE 0.7~A (don't fire Stage 2 99-IMO run under broken classifier)
- SISTER-COORD ACK → DS~E (config consume + commit-bundle absorption, earlier in cycle)

## Recommended forward (Tier-1 architectural call, not DS)

v0.7.3 W1-revision: (2) annuity-vocab as dampener not positive rollup signal [fixes F-2] + (3) high-signal-term gate — RIA/Form-ADV/Series-65-in-advisor-context over generic "asset management" prose [fixes F-1]. Combination addresses both. DS~B ready to implement on Tier-1 ruling (~30-45min incl re-grade re-run).

## Standing posture

RAVC2-submitted; awaiting ws COO verdict + ws CTO/CVO W1-revision direction. Brief doc-of-record: `docs/briefs/find-insure-031-stage1-regrade-v07_1-finding-20260528.md`. Next /work tick (cron :17/:37/:57) checks for disposition + any follow-on TO.
