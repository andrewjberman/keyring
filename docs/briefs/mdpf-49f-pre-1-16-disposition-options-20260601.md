# MDPF 49F — pre-1/16 disposition: 3 options (decision-support for Andrew #3)

**Author:** 0.4.0_DS_ClientPlatform~B · **Date:** 2026-06-01 · **RAVC2 to:** COO + CTO -> Andrew
**Project:** MDPF_SCOPED · **Arms:** Andrew open item #3 (pre-1/16 49F representation)
**Companion records:** `to1a_schwab_rederive_applied~B.md` (the 1/16-5/17 re-derive that landed), `mdpf_schwab_canonical_rederive_scope~B.md` (exact-vs-estimate scope), `item3_1227_perfirm_anomaly_scope~B.md` (year-end gap)

---

## TL;DR — recommendation: **Option B (flag-at-1/16, keep pre-1/16 on labeled legacy basis)**

The single fact that drives this: **the 1/16 boundary is already numerically continuous in the served trend — there is no visible cliff.** The full-book->Schwab correction that the TO-1a re-derive removed ($143M @ 4/15) was concentrated **April->5/17**; it had NOT yet opened up pre-1/16, where the old bandaid basis was already approximately Schwab. So:

- **Option A (back-cast estimate)** would produce a pre-1/16 line nearly identical to what's already shown, while adding a widening error band and presenting an estimated line as if it were measured -> estimation overhead for ~zero visible benefit, and it cuts against the data-honesty gate that governed the whole re-derive.
- **Option C (start at 1/16)** discards a real, continuous growth history (Nov 2024 ~$776M -> Jan 2026 ~$1.4B, the firm roughly doubling) for no honesty gain, since the displayed line is already numerically honest at the seam.
- **Option B** keeps that useful history, stays numerically continuous (Andrew's view barely changes), and resolves the honesty concern the right way: an **explicit per-date provenance flag + a 1/16 boundary annotation** that says "pre-1/16 is Black-Diamond legacy basis, not Schwab-canonical-re-derivable." Honest about *what the data is* without throwing away *useful data*.

This is a representation/labeling decision, not a data-recoverability one. **Andrew's call** — the doc lays out all three fairly so he can overrule on visual/product grounds.

---

## Setup — what is canonical today, and what pre-1/16 actually is

The 49F AUA trend Andrew reads each morning (served: `s3://opal-data-portal-v2/json/mdpf/49financial/aggregate-aua-timeseries.json`, 401 dates, 2024-11-01 -> 2026-05-29) now has three regions:

| Region | Dates | Basis | Status |
|---|---|---|---|
| **LIVE** | 2026-05-18 -> | Fully measured (canonical aggregator + live SmartX feeder) | canonical |
| **RE-DERIVED** | 2026-01-16 -> 5/17 | **Schwab-canonical, custody MEASURED/EXACT** (per-account `silver/allocations` ∩ Schwab + stable `silver/fees` crosswalk). Only the ~$25M 1c (SMA) term is a labeled interpolated estimate. | canonical (TO-1a, applied ~1821Z, DE+CVO verified 5/5) |
| **PRE-1/16** | 2024-11-01 -> 2026-01-15 | **Black-Diamond legacy bandaid basis (v0.8)** — NOT exact-re-derivable: `silver/allocations` (per-account market values) only goes back to **2026-01-16**. Currently carries no per-date basis tag; `meta.basis_provenance.pre_1_16 = "pending_andrew_disposition (legacy basis until ruled)"`. | **the open question — this doc** |

**Why pre-1/16 can't be made exact (the hard constraint):** computing Schwab-restricted custody needs per-account market values intersected with the Schwab-custodied account set. The custodian crosswalk (`silver/fees`) goes back to 2020, but the per-account allocations (`silver/allocations`) start 2026-01-16. No allocations pre-1/16 = no exact Schwab custody pre-1/16. Any pre-1/16 "Schwab" number is necessarily modeled.

**The decisive empirical fact — the boundary is continuous (served values):**

```
date         total_aua    basis
2025-12-26   1,292.4M     (legacy)         <- year-end region
2025-12-29   1,337.2M     (legacy)
  [12/30, 12/31, 1/2 MISSING -> AC6 dates, see below]
2026-01-05   1,366.4M     (legacy)
2026-01-12   1,398.6M     (legacy)
2026-01-15   1,409.3M     (legacy)         <- last pre-re-derive day
2026-01-16   1,412.9M     schwab_canonical_rederived   <- +$3.6M, NO cliff
2026-01-20   1,396.9M     schwab_canonical_rederived
```

The legacy line flows smoothly into the Schwab-canonical line (+$3.6M at the seam). The $143M divergence that justified the re-derive only opened later (April->5/17). So pre-1/16, **legacy ~= Schwab** — which is exactly why a back-cast buys no visible change.

---

## The three options at a glance

| | **A — full back-cast estimate** | **B — flag-at-1/16 (RECOMMENDED)** | **C — start trend at 1/16** |
|---|---|---|---|
| **What Andrew sees** | Continuous line Nov'24->today, pre-1/16 portion styled/footnoted as "estimated." Numerically ~identical to today (legacy ~= Schwab pre-April). | Continuous line Nov'24->today (~unchanged from today), with an explicit basis-change annotation at 1/16 + a "legacy basis" style/footnote on the pre-1/16 segment. | Trend begins 2026-01-16. ~14.5 months of history (Nov'24->Jan'26) disappears, incl. the ~$776M->$1.4B growth story. |
| **Honesty / provenance posture** | Weakest. Presents a *modeled* line as canonical-adjacent; the error band widens the further back you go yet the line looks measured. Conflicts with the CTO data-honesty gate. | Strongest *and* complete. Says exactly what the data is ("real-as-reported legacy basis, not re-derivable to Schwab") without hiding it or discarding it. | Most conservative ("we only show canonical data"). Honest by omission, but omits real, useful, numerically-honest history. |
| **Data implications** | Build a back-cast: apply the 1/16 Schwab/legacy relationship backward (~1.0 at the seam, so output ~= input) + an error band. Stamp every pre-1/16 date `estimate`. Most engineering, most fragile. | Stamp pre-1/16 `basis_tag="black_diamond_legacy_non_canonical"` per date + `meta.basis_boundary_date="2026-01-16"`; resolve the pending flag. No value recompute. Low effort, no new data. | Truncate the served series at 1/16 (or hard-flag pre-1/16 as not-displayed). Trivial. Loses history irreversibly from the view. |
| **AC6 pre-1/16 dates (12/30,12/31,1/2)** | Estimated via the back-cast. | Backfilled on the **same legacy basis** as neighbors (12/29 $1,337M / 1/5 $1,366M), flagged legacy -> closes the visible year-end gap. | Moot — dropped (before trend start). |
| **Reversible?** | Yes (re-emit) but sunk estimation work. | Yes — flags only; trivially re-rulable later. | Yes (re-include) but Andrew loses the history *now*. |

---

## Detail per option

### Option A — full back-cast estimate of the entire pre-1/16 period
Re-derive pre-1/16 onto an *estimated* Schwab basis (the custody back-cast method): take the legacy pre-1/16 values and apply the measurable 1/16-onward Schwab/legacy relationship backward, plus an explicit estimate marker + error band.

- **What Andrew sees:** a continuous line whose pre-1/16 portion is footnoted "estimated." Because legacy ~= Schwab pre-April, the *numbers barely move* from what's shown today.
- **Honesty posture — the problem:** we'd be manufacturing a Schwab-looking series for a period with **no Schwab source**, with an error band that widens toward 2024-11 (account custody mix drifts; the firm was onboarding accounts, so the recent ratio is least valid oldest). A modeled line that visually reads as measured is precisely what the re-derive's data-honesty gate exists to prevent — and here we'd pay that cost for ~no visible gain.
- **When A would be right:** only if Andrew wants a *single uniform stated basis* end-to-end and accepts an explicitly-estimated pre-1/16 to get it. Even then, B + annotation gets ~the same picture honestly.

### Option B — flag-at-1/16 (keep pre-1/16 on labeled legacy basis) — RECOMMENDED
Keep the real pre-1/16 history exactly as reported (legacy bandaid basis), mark the 1/16 basis transition explicitly, and style/footnote the pre-1/16 segment as legacy/non-canonical.

- **What Andrew sees:** essentially today's trend (continuous, no cliff), now with a clear "basis change at 1/16 — pre-1/16 is Black-Diamond legacy, not Schwab-canonical" annotation and a visually distinct (e.g. lighter/dashed) pre-1/16 segment.
- **Honesty posture:** strongest. The numbers are real-as-then-reported; the label tells the truth about basis; nothing is fabricated or discarded. The fact that legacy ~= Schwab at the seam means the annotation explains a provenance distinction, not a number Andrew has to reconcile against a jump.
- **Data implications:** flag-only. Stamp pre-1/16 `cohort_provenance.basis = "black_diamond_legacy_non_canonical"` + `note="not re-derivable; no silver/allocations pre-2026-01-16"`, set `meta.basis_boundary_date="2026-01-16"`, flip `meta.basis_provenance.pre_1_16` from pending to the ruling. Backfill the 3 AC6 dates on legacy basis. Coordinate the render (boundary marker + segment styling) with RD~B. No value recompute, no new data.

### Option C — start the trend at 1/16
Drop pre-1/16 from the displayed trend; the line begins on clean Schwab-canonical basis at 2026-01-16.

- **What Andrew sees:** a trend that starts 1/16, every point canonical. No legacy data, no annotation needed.
- **Honesty posture:** most conservative — "we only show what we can stand behind canonically." But it omits ~14.5 months of **real, useful, numerically-honest** history (the firm roughly doubling, ~$776M -> $1.4B). That growth narrative is exactly the kind of context an AUA trend is for.
- **When C would be right:** if Andrew's product principle is "canonical-only, no exceptions, even labeled ones" — then C over B. The cost is the lost history; the benefit (over a well-labeled B) is purely the absence of any non-canonical pixels on the chart.

---

## AC6 pre-1/16 dates: 12/30, 12/31, 1/2

These three business days are **missing** from the served series (it jumps 12/29 -> 1/5; 1/1 is correctly absent as a holiday). They are part of the year-end backfill date-selection defect (see `item3_1227_perfirm_anomaly_scope~B.md`; the same defect leaked the spurious 12/27 *Saturday*, handled separately). Their disposition rides Andrew's choice:

- **A / B (pre-1/16 retained):** backfill 12/30, 12/31, 1/2 on the period basis (estimated for A, legacy for B), flagged like their neighbors -> the visible year-end gap closes.
- **C (pre-1/16 dropped):** moot — they fall before the trend start.

Recommend folding the year-end business-day backfill into whichever option retains pre-1/16, and (regardless) hardening the producer's date-selection to a weekend/holiday-aware trading calendar so this class can't recur.

---

## Recommendation + what each choice triggers

**Recommended: Option B.** Honest about provenance, preserves useful history, numerically continuous (minimal change to Andrew's view), lowest effort, trivially re-rulable. A pays estimation cost for no visible gain and weakens honesty; C is clean but discards real history for a marginal purity gain over a well-labeled B.

On Andrew's ruling, DS~B executes (full Rule 13 + ds-commit-gate; DE serving-verify + CVO independent-verify; RAVC2):
- **B:** stamp pre-1/16 legacy provenance flags + boundary date, resolve the pending flag, backfill 12/30/12/31/1/2 on legacy basis, coordinate boundary annotation + segment styling with RD~B. (lowest effort)
- **C:** truncate/hard-flag the served series at 1/16, drop the 3 AC6 pre-1/16 dates. (trivial)
- **A:** build + validate the custody back-cast with an error band, stamp every pre-1/16 date `estimate`, backfill the 3 AC6 dates estimated. (most effort; recommend only if Andrew explicitly wants a uniform estimated basis end-to-end)

Out of scope of this artifact (tracked separately): the global/Inflection -$89M residual at 5/18 (TO-1c, eclipse/orion-side basis), and the post-1/16 AC6 add-days (2/2, 3/2, 4/1, 5/1).
