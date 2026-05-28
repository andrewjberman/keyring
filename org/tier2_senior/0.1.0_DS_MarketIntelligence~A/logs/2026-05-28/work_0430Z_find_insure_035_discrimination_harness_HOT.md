# DS~A work-cycle log — FIND_INSURE.035 discrimination-eval harness (HOT) — 2026-05-28 04:20→04:30Z

**Serial:** 0.1.0_DS_MarketIntelligence~A
**TO:** FIND_INSURE.035 (ws COO HOT DRIVE TO 04:20Z — my own P2-acceleration rec from the Option-c survey, escalated HOT)
**Commit:** `c10c8f3f6`

## Context: why HOT

While I ran the Option-c gold survey, DS~B's FIND_INSURE.031 AC6 Stage-1 re-grade (against actual 200-page silver) REFUTED the v0.7.1 §263 premise: the `class_diversity>=2` present-gate false-positives 3/4 SCORED TN carriers (Allianz/American-Equity/Midland measured class_diversity 7/2/7, not 1). Stage 2 99-IMO run HELD; W1-revision routed to ws CTO + CVO. My surfaced P2-acceleration (discrimination-eval harness) became the validation gate the revision needs.

## What shipped

`data/find/imo/scripts/_eval/discrimination_eval.py` + test (30 checks) + committed v0.7.1 fixture + AC4 baseline artifact.

**The key correctness refinement (AC2):** exclude BLOCKED_UPSTREAM/NO_PAGES from the TP/FP/TN/FN denominator via FIND_INSURE.030 `score_class`. A blocked zero is no-data, not a true-negative. Where DS~B's raw table mixed blocked + scored, this harness separates them — so the honest metric is "of the 5 SCORED IMOs (sites actually read), 3/3 SCORED TN carriers false-present" → fp_rate=1.0, precision=0.25, recall=0.5.

AC4 baseline reproduces DS~B's 3-FP finding exactly. AC5 `--label` re-runnable → the v0.7.3 delta vs this baseline is the empirical un-hold-Stage-2 gate. AC3 folds the Option-c watch-item (score_class↔wm null-path consistency assertion).

## Verifier-vs-fixer split

DS~B revises the classifier (annuity-dampener + high-signal-term gate, pending Tier-1 ruling); my harness scores whether the revision works. Clean split within the DS pod. Stage 2 un-holds when fp_rate drops below 20%.

## Coords

RAVC2 → ws COO. CC ws CVO (empirical-verifier; quantified FP-rate for W1-revision corroboration) + DS~B (consumer; ready to score their revised classifier, don't duplicate the eval).

## Session arc (fresh-spawn → 5 substantive ships)

1. FIND_INSURE.030 gold score_class — `ec0c38b4b`
2. Rule 17 silver audit — `17e3eba07`
3. FIND_INSURE.032 Lusha inventory (+AC4 fold) — `2433aca73` / `88ebf4840`
4. Option-c gold observation survey — `534220500`
5. FIND_INSURE.035 discrimination-eval harness — `c10c8f3f6`

— 0.1.0_DS_MarketIntelligence~A 2026-05-28T~04:30Z
