# FIND_INSURE — Alias-Recall Empirical Findings & Disposition

**Author:** 0.4.0_DS_ClientPlatform~C
**Date:** 2026-06-01
**Directive:** ws COO 2026-06-01 (162013Z) — "scribe the brief; record the empirical finding + the empirical-only alias policy; prevents anyone re-attempting the broad-recall dead-end."
**Status:** FINDINGS BRIEF v1.0 — DECISION OF RECORD: broad alias-recall SHELVED; empirical-only alias policy binding.

---

## 1. Question

The FINRA BrokerCheck enrichment over the 24 Option-B IMOs (run_date 2026-05-27, 661 contacts)
leaves **478 / 661 (72%) at disposition `NO_FIRM_MATCH`**. The premise to test: is the 72% a
recoverable recall miss — i.e., would an IMO→registered-BD alias map (`firm-aliases-v1.json` +
`--reenrich-no-firm-match`) lift `NO_FIRM_MATCH → ENRICHED` and meaningfully raise IR-product
coverage? (Originally framed by COO as "the biggest lever on coverage.")

## 2. Disposition baseline (24 IMOs, run_date 2026-05-27)

| disposition | count | % | meaning |
|---|---|---|---|
| ENRICHED (firm+name matched) | 79 | 12% | carries series-license data |
| NO_FIRM_MATCH | 478 | 72% | name found in BrokerCheck, but no candidate's current-employment firm token-matched the company name |
| NO_MATCH | 104 | 16% | no BrokerCheck record at all |
| series-licensed leaders (gold-scored) | 73 | — | the (b)-depth discriminator |

NB: the earlier "636 enriched" figure was records **processed/attempted** (FINRA field attached),
NOT matched. The matched/value figure is 79 (→ 73 series-licensed after gold dedup/scoring).

## 3. Method

1. **Offline (0 GETs):** tallied ENRICHED reps' observed BrokerCheck `matched_firm` (the
   registered-BD current-employment firm_name) across all 24 IMOs from existing bronze.
2. **Two deep samples (free GETs):** re-queried the ACTUAL candidate firms of the NO_FIRM_MATCH
   reps at lincoln-investment (18) + gradient-financial-group (30). Required because
   `enrich_person` discards the candidate firms on a NO_FIRM_MATCH — it stores only `name_hits`
   (the count) at `data/find/imo/scripts/_util/brokercheck_client.py:135-138`.

## 4. Finding — the 72% is mostly PRECISION-CORRECT rejection, not a recall miss

The NO_FIRM_MATCH reps **scatter across many unrelated national firms; they do NOT cluster under
the IMO's affiliated BD**:

- **lincoln-investment** (18 NO_FIRM_MATCH): Charles Schwab ×7, Merrill Lynch ×4, Fidelity ×4,
  PFS Investments ×4, Edward Jones ×4, Morgan Stanley, LPL, J.P. Morgan, Daiwa, Allstate, NYLIFE…
  — 12+ unrelated wirehouses/IBDs, no dominant affiliated entity.
- **gradient-financial-group** (30 NO_FIRM_MATCH): **0 of 30** at any `Gradient-*` entity; same
  scatter (Schwab, Merrill, Osaic, Morgan Stanley…).

Interpretation: these are **name-collisions** (a different person with the same name registered at
a wirehouse) + **LinkedIn-current-company ≠ FINRA-current-employment** (former reps, or LinkedIn
title noise). Both are *correct rejections* under Andrew's firm+name-match rule — not recall misses.

An affiliated-BD alias keyed on this scatter (e.g. adding "Charles Schwab" as a lincoln alias)
would falsely match unrelated reps — exactly the over-match failure-mode that produced the
`preferred-marketing-associates` collision and that CTO banned. **Broad alias-recall trades
precision for ≈zero true recall.**

## 5. Decision of record (ws COO 162013Z)

- **SHELVE broad alias-recall.** Do NOT build a broad alias map. Do NOT run a full
  `--reenrich-no-firm-match` pass.
- **Banked (do not build now — FIND_INSURE parallel/secondary, near-zero yield):**
  - *Surgical cluster-detection:* enhance `enrich_person` to store NO_FIRM_MATCH candidate firms,
    then add an empirical alias ONLY for an IMO whose unmatched reps demonstrably **cluster** under
    one distinctive affiliated BD (cluster = true miss; scatter = correct reject). Expect FEW
    qualifying IMOs.
  - *Preferred future depth-lever:* a **name-match-strength / "FINRA-current-employment-elsewhere"
    signal** that splits name-collision from true-no-FINRA inside NO_FIRM_MATCH. Higher value than
    alias recall; the one to revisit if FIND_INSURE depth gets more investment.

## 6. Empirical-only alias population policy (CTO 131406Z + COO, binding)

Populate a `firm-aliases-v1.json` entry **ONLY** from a name-matched rep's **OBSERVED** BrokerCheck
current-employment `firm_name`. **NEVER** guess an alias from a shared abbreviation or name pattern.
Require distinctive multi-token registered names; reject single generic tokens
(Advisors / Public / Trust / Investments over-match). The stripped
`preferred-marketing-associates → [PMA Securities / Prudent Man Advisors / PMA Asset Management /
Public Trust Advisors / PTMA]` seed was an abbreviation collision and is the canonical
counter-example. The empty map = honest pre-alias precision-first behavior. (Policy is also recorded
inline in `data/find/imo/config/firm-aliases-v1.json:_population_policy`; seed-strip commit
`f9804fde7`.)

## 7. Related discovery — `preferred-marketing-associates` is a wrong-entity (separate RAVC2)

The same probe surfaced that the `preferred-marketing-associates` slug's bronze (0.858 / 29
series-licensed, #1-tier IR headline) is **PMA Financial Network** (muni/public-finance,
pmanetwork.com / Lusha id 57838758), NOT the insurance IMO. Root cause = upstream source-list
(safemoneybroadcasting 99-IMO list) position #79 pairs "Preferred Marketing Associates" with
domain `pmanetwork.com`. Pipeline propagated faithfully; source data wrong. Tracked separately —
RAVC2 to COO+CTO 2026-06-01 162318Z/162337Z; A/B disposition (relabel-as-PMA-Financial-Network vs
out-of-scope-drop) + a name↔domain spot-audit of the other 98 entries pending COO/CTO call.

## 8. Artifacts

- Seed-strip: commit `f9804fde7` (`firm-aliases-v1.json` → empty map + policy note).
- Provenance-honesty fix (unrelated, same cycle): commit `a75965d33` (contacts-target v1.2).
- Probe scripts were ad-hoc/read-only (not persisted); methodology in §3 is reproducible from
  existing bronze + `brokercheck_client.search_individual`.
