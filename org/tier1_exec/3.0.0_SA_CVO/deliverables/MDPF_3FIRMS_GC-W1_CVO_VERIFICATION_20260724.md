# GC-W1 — CVO INDEPENDENT VERIFICATION

    verifier:      3.0.0_SA_CVO (main-fabric CVO)
    subject:       MDPF_3FIRMS_GC-W1_global_count_composition_measurement_20260724.md @b078877020
    author:        0.4.0_DS_ClientPlatform~A · TO MDPF_3FIRMS.GC-W1 @939376b88 (amended @157278cb3)
    verdict:       **PASS — VALIDATED.** Every acceptance criterion independently reproduced on the
                   served bytes. Two SHARPENINGS recorded; neither blocks W-2.
    method:        Re-measured, not reviewed. I pulled the four served artifacts myself and computed
                   every headline figure from scratch. Where I agree, two instruments agree.
    artifact pin:  global key ETag `55a8b379fb22a9c1ed02db1eef5d2a18`, 254,419 B,
                   LastModified **2026-07-23T21:18:53Z** — byte-identical to the ETag DS~A measured on,
                   so we are provably on the same vintage.
    consequence:   Andrew re-pointed MDPF counts PRIMARY-through-to-VALIDATED (~1432Z). CTO rules W-2
                   off this measurement; W-3 and W-6 gate behind that.

---

## 1. WHAT I REPRODUCED INDEPENDENTLY — all of it

| claim | DS~A | mine | verdict |
|---|---|---|---|
| spine denominator | 447 | **447** | ✓ |
| `account_count_total` nulls | 40 of 447 | **40 of 447** | ✓ |
| nulls on the TRADING-day axis | 22 | **22** | ✓ |
| nulls on the WEEKDAY axis (CTO's 24) | 24 | **24** | ✓ |
| the 2 dates that differ | 06-19, 07-03 | **2026-06-19, 2026-07-03** | ✓ |
| trading axis / non-trading spine rows | 429 / 18 | **429 / 18** | ✓ |
| 49F @07-17 → @07-22 | 7,140 → 7,026 (−114) | **7,140 → 7,026 (−114)** | ✓ |
| INF @07-17 → @07-22 | 546 → 534 (−12) | **546 → 534 (−12)** | ✓ |
| COT @07-17 → @07-22 | absent → 442 (+442) | **absent → 442 (+442)** | ✓ |
| Σfirms / GLOBAL / residual @07-22 | 8,002 / 8,094 / +92 | **8,002 / 8,094 / +92** | ✓ |
| arithmetic identity | +442 −126 +92 = +408 | **= 408, and the served step IS 408** | ✓ |
| per-model residual split | +85 SMA, +7 roster | **+45 +40 = +85; −2−1+0+13−3 = +7** | ✓ |
| residual sweep | 406 clean of 407, sole exception 07-22 | **406 of 407, sole exception 07-22** | ✓ |
| `count_coverage_end` | 2026-07-18 | **2026-07-18** | ✓ |
| firm axis reconciliation | 429/429/447, cot covered 47 | **429/429/447, `n_cottonwood_covered`=47** | ✓ |
| `exempt_absorbed` served count | 38 | **38** | ✓ |
| §4A model-axis (b) | 0×26; 94 ✓; 255 ✓ | **0×26; 86×3 88×1 94×1 95×1 254×1 255×3 262×1 267×3** | ✓ exact |
| §4A INF zeros | 383 of 429, first non-zero 05-15 | **383 of 429, first non-zero 2026-05-15** | ✓ |
| §4A 49F concentration | 92.9% | **7,140 / 7,686 = 92.9%** | ✓ |
| §4A 49F absent on trading nulls | 21 of 22 | **21 of 22, sole exception 05-21** | ✓ |

**The 05-21 exercised case holds** — COO named it as the load-bearing proof and it is:

    model                          GLOBAL   49F   INF   COT
    opal_ultra_short_term            None   167  None  None
    opal_short_term                  None   660  None  None
    opal_intermediate                None  1567  None  None
    opal_long_term_conservative      None  2974  None  None
    opal_long_term_aggressive        None  1420  None  None

49F serves **6,788** real core accounts; Global publishes `None` on 5 of 5 core models. The
all-or-nothing is at the FIRM axis. This is EXERCISED, not inferred.

**The source swap is real.** `count_provenance` at the seam: 49F `measured` → **`frontier_stamp`**;
INF `measured` → `measured`; COT `source_absent` → `measured`; GLOBAL `band_2firm` → `frontier_stamp`.
**`frontier_stamp` occurs on exactly 1 of 447 dates.** So 49F's −114 is a source swap, not attrition —
confirmed at the bytes, not taken from the report.

**Mechanism source-confirmed at the pinned vintage** (`@3efc9dc6d`, positive control: file retrieves
1,926 lines at both vintages, so the comparison rests on a real read):
`:1656` `acct.append(None if (cgap or not cparts) else int(sum(cparts)))` — one contributing firm's
missing roster poisons the whole per-model cell. `:1657-1658` `acct[-1] = ad_frontier[mkey]` — the
frontier stamp overwrites the last axis position only.
**Vintage note verified:** the TO's `:1720-1741 @275b51aee` and the report's `:1716-1741 @3efc9dc6d`
are the same block, offset by 4 lines. DS~A's re-pin is correct.

---

## 2. THE FOUR SOFT JOINTS DS~A NAMED — my dispositions

DS~A asked to be hit on its own weak points first rather than the easy ones. Taken.

**#1 — the 2026 holiday set was never cross-checked externally. CLOSED.** 2026-06-19 is a **Friday**
(Juneteenth, an NYSE closure since 2022). 2026-07-04 falls on a **Saturday**, so the NYSE observes the
preceding **Friday 2026-07-03**. Both correction dates are unambiguous closures under the standard
observance rule. The resolver is externally right on exactly the two dates that carry the correction,
so the 24 → 22 correction stands and CTO's 24 is a weekday count.

**#2 — is the firm-sum mirroring the right comparison? CLOSED, and closed properly.** My first sweep
used DS~A's own predicate, which proves arithmetic, not the *choice*. So I re-ran under the
alternative (core keys only):

    ALL by_model keys (DS~A's choice)  -> 1 non-zero residual date: 2026-07-22 = +92
    CORE keys only    (alternative)    -> 1 non-zero residual date: 2026-07-22 = +7

**The finding is predicate-robust.** The date is the same under both; only the magnitude changes, and
the delta between them (+85) is exactly the SMA preserve decomposing out. The choice of predicate
does not manufacture the finding.

**#3 — could the 0/94/255 match be coincidence rather than reproduction? NARROWED, NOT CLOSED —
and it does not need to be closed.** All three values the producer's own comment pins
(`:1710-1712 @3efc9dc6d`) reproduce, *and* the full distribution shape matches DS~A's table
cell-for-cell (6 dates in the 86–95 band, 8 in the 254–267 band). Coincidence across three pinned
values plus the whole shape is implausible. But DS~A is right that it did not read the historical
client-side summing code, so this is **STRONG INFERENCE, not SOURCE-CONFIRMED**, and I grade it that
way. **It is not load-bearing:** the recommendation to take model-axis (b) off the table rests on
*26 of 40 dates publishing 0 against a true base of ~7,500* — which is measured outright, regardless
of whether the historical FE summed identically.

**#4 — are INF's zeros genuine, or absent-rendered-as-zero? CLOSED by the artifact itself.** All
**383** zero dates carry `count_provenance == "measured"`. They are genuine measured zeros. The
"firm-axis (b) publishes 0 on 8 dates" conclusion holds.

**Correctly NOT claimed:** why 49F's legacy import axis omits its 20 dates. The artifact self-labels
them *"UNCHECKED, not clean."* DS~A did not open the upstream import and did not assert a cause.
That restraint is right and I am not treating the gap as a defect in the measurement.

---

## 3. SHARPENING S-1 — the verdict line under-claims a refutation its own data supports

**Not a correction; the report contains the fact. The VERDICT LINE does not carry it, and that is what
downstream readers will quote.**

The claim under test, verbatim: *"the +408 is Cottonwood entering **via the frontier stamp**."*
DS~A's verdict answers the magnitude and the sufficiency. It does not answer the **mechanism clause**,
and the served bytes refute that too:

| firm | `count_provenance` @2026-07-22 |
|---|---|
| **cottonwood** | **`measured`** |
| 49financial | `frontier_stamp` |
| GLOBAL | `frontier_stamp` |

**Cottonwood does not enter via the frontier stamp. It enters as measured data.** The frontier stamp
is 49F's and Global's. The inherited claim fuses two different firms' mechanisms into one sentence,
and a W-2/W-3 reader who inherits it will go looking at the wrong code path — the frontier stamp is a
roster overwrite (`:1657-1658`) fed from a **separate staged artifact**
(`gold/mdpf_revamp/{firm_id}/account_distribution.json` → `meta.account_count_by_model_key`, `:604`),
which has nothing to do with Cottonwood's arrival.

**Recommend the verdict line read: CONFIRMED as to direction and dominant driver; REFUTED as to
magnitude, sufficiency, AND mechanism.** Three refutations, not two.

## 4. SHARPENING S-2 — "dominant driver": MEASURED for Σfirms, INFERRED for the served Global cells

COO asked the right question — *was the confirming half measured or absorbed?* My answer is neither
"absorbed" nor fully "measured," and the distinction is W-2 input rather than a defect.

**Measured:** Cottonwood's +442 is read directly from its own served artifact and is by far the
largest single mover. Σfirms moves +316 and the per-firm figures each trace to their own bytes. That
half is genuinely derived, not inherited — DS~A found −114 and −12 and +92, none of which appear in
CTO's attribution, which is what a real decomposition looks like.

**But it does not measure the provenance of the served Global number.** On 07-22 — the last axis
position — Global's core cells are **overwritten** by `ad_frontier` (`:1657-1658`). They are not the
firm sum at all. Σfirms lands within +7 of the stamped value, which is why the accounting identity
closes, but the causal path into the served core number runs through a separate artifact that DS~A
did not open. So `+442 Cottonwood` explains the **Σfirms** movement; the **served** core on the
frontier date is a different source that happens to agree to within 7.

**Why this matters more than it sounds:** W-2 is about to write a composition law for a number that,
on the frontier date, **is not composed — it is stamped.** Any rule expressed as "sum what is
present" has no effect on the one date where the value is an overwrite. CTO should know that before
ruling.

---

## 5. NOTES

**A predicate difference worth naming, since it bit us elsewhere today.** DS~A reports 49F serving
**6,788** accounts on 05-21; I first measured **6,882**. Neither is wrong: 6,788 is the five **core**
models, 6,882 includes the two SMA keys. DS~A's is the correct figure for the claim it supports (core
cells are what the poison gates on). **Print the predicate, not just the denominator** — the same
lesson that cost two wrong population figures in RV-0055 this morning.

**W-6 scope reduction independently confirmed.** `json/mdpf/aggregate-aua-timeseries.json` and
`json/mdpf/global/aggregate-aua-timeseries.json` carry the **identical ETag**
`55a8b379fb22a9c1ed02db1eef5d2a18` at 254,419 B (different write times, same bytes).
`json/portfolios/aum-timeseries.json` is genuinely different (`f96cfc43…`, 289,962 B). Two of the
three keys are one artifact — W-6 is a two-way reconcile plus a retire-or-repoint, not a three-way.

**Scope discipline held.** Measurement only: no producer edit, no gold run (NEVER#4 respected — I
confirmed the measurement is on served bytes, and I did not trigger one either), no SEV1 surface
touched. Fix-shaped content is confined to §4A/§5 as explicit W-2/W-3 input.

**On §4A generally:** it is the most decision-critical section and it was added *after* the
Andrew re-point. I verified it against the committed version @b078877020 — worth stating because I
had read an earlier 247-line draft and the file is now 310 lines; a verdict rendered on the draft
would have validated an artifact nobody is going to read.

---

## 6. WHAT SHOULD HAVE BEEN ASKED BUT WAS NOT

**Nothing in this wave measures whether the 07-22 frontier stamp is CORRECT — only that it is
different.** Every instrument here, mine included, treats `ad_frontier` as a given and reconciles the
firms to it. But `ad_frontier` is a second count source with its own `as_of`, explicitly *"NOT covered
by `count_coverage_end`"*, read from a staged artifact that must be written before this producer runs
(`:609` — *"account_dist MUST be staged first"*). The +7 is the only visible seam between those two
sources, and it is visible **only on the single date where both happen to be populated**. On every
other date the frontier stamp is invisible because it agrees, or because there is nothing to compare
it against.

So the question W-2 will not think to ask: **if the staged `account_distribution.json` were stale or
wrong, what in this system would say so?** The producer's own fallback is
*"`{}` if absent -> frontier stays honest-None"*, which is a sound answer for *absent*. There is no
equivalent answer for *present but stale* — a stale frontier stamp would silently overwrite the last
axis position of the served Global count with a confident, plausible number, on exactly the date a
reader is most likely to look at. **That is the same shape as this morning's grep defect: not a zero,
not an error — a plausible value from a source nobody re-checks.** I am not asserting it is stale; I
have not measured it. I am saying no instrument in W-1..W-7 as currently scoped would detect it, and
one cheap check (compare the staged `account_dist` `as_of` against `count_coverage_end` at publish
time) would close it.

**P2, non-blocking.** It does not touch this verdict — W-1 measured what it was asked to measure and
measured it correctly.

---

## VERDICT

**PASS — VALIDATED.** Every acceptance criterion is independently reproduced on the served bytes at a
provably identical vintage, with controls run (the residual sweep detects an injected discrepancy, so
it is not a broken instrument reporting silence) and with the central finding shown to be
predicate-robust. All four of DS~A's self-named soft joints are closed or correctly narrowed. The
report's restraint is as notable as its findings: it declines to claim the one cause it did not
profile, and it corrected the CTO on a number in his own brief with the axis named rather than the
person.

**AC-1 ✓ · AC-2 ✓ (24 → 22 correction upheld) · AC-3 ✓ · AC-4 ✓ (strengthen to three refutations
per S-1) · AC-5 ✓ · AC-6 ✓ (recipe reproduces `447 40 22` exactly).**

**W-2 may proceed on this measurement.** Two sharpenings for CTO to fold, neither gate-blocking:
S-1 the mechanism clause is refuted too, and S-2 the served core on the frontier date is stamped, not
composed — so a "sum what is present" law does not reach it.

— 3.0.0_SA_CVO
