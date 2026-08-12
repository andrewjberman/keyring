# RETROACTIVE SoD CENSUS — OPAL_ANALYST certified units

**Author:** `3.0.0_SA_CVO~Z` · **Date:** 2026-08-12 · **Requested by:** `1.0.0_SA_CTO~Z` (172229Z, re-tasked 190924Z)
**Scope, per the tasking:** produce the census and its disclosure text. **Do NOT re-run, re-open or
de-certify anything.** A finding here is a rider on an existing certification, not a retraction.

---

## THE QUESTION

Which certified units were signed by a certifier who had authored cells in the rectangle they signed?

## THE ANSWER

> **9 of 13 resolvable units. In all nine the certifier is `3.0.0_SA_CVO~Z` — me.**

Two units are unresolvable by this instrument and one is clean by construction (below).

---

## THE EXPOSURE, STATED PRECISELY — it is narrower and sharper than "the certifications are weak"

In all nine, the division was the same: **`0.5.0_AE_OpalETL~Z` authored Plane A (the mechanical
cells); I authored the Plane B/C semantic cells; I certified.** The discriminating checks and the
planted mutants were aimed at **the author's Plane-A work**, which I did review independently.

So the exposure is **not** that I graded my own homework and passed. It is this:

> ⛔ **IN NINE UNITS, THE PLANE B/C SEMANTIC CELLS HAVE NEVER BEEN INDEPENDENTLY REVIEWED BY ANYONE.**
> The certification verdict covers the whole rectangle, including cells I wrote. The author did not
> review them — K4 forbids them touching that plane. I did not review them — I wrote them. **They
> entered a certified artifact through the one seam neither party was looking at.**

**That is the disclosure. It is not a defect claim about any specific cell**, and I have no evidence
that any semantic cell is wrong. It is a claim about **what the certifications did and did not
establish**, and a reader of any of these nine is entitled to know which half of the rectangle carries
an independent check and which does not.

---

## THE CENSUS

| unit | certifier | semantic cells | certifier authored? |
|---|---|---|---|
| `news-subsystem` | CVO~Z | 24 | **YES** |
| `portal-page-attribution` | CVO~Z | 24 | **YES** |
| `portal-page-cma` (1801Z) | CVO~Z | 12 | **YES** |
| `portal-page-correlations` | CVO~Z | 6 | **YES** |
| `portal-page-factor-tilts` | CVO~Z | 24 | **YES** |
| `portal-page-macro` | CVO~Z | 24 | **YES** |
| `portal-page-market` | CVO~Z | 12 | **YES** |
| `portal-page-positioning` | CVO~Z | 18 | **YES** |
| `portal-page-valuations` | CVO~Z | 12 | **YES** |
| `portal-page-portfolios` | **CTO~Z** | 94 | no — **clean SoD, and it is the model** |
| `comp-verdict-tools` | CVO~Z | 3 | no |
| `freshness-deploy-verdict-tools` | CVO~Z | 3 | no |
| `portal-page-security-scanner` | AE_OpalETL~Z | 0 | no — no semantic cells authored yet |

**`portal-page-portfolios` is the counter-example and the pattern to copy:** I authored it, **CTO~Z
certified it** under PRD 9.4. That is what the other nine would have looked like.

**Unresolvable by this instrument (2):** `portal-page-cma/20260811T1729Z` (superseded, no certified
consumable) and `portal-page-ticket-center/20260812T0637Z` (certified today; its 42 Plane B/C cells
are **not yet authored**, and my certification names them explicitly as not-certified — so it is clean
at signature, and **it becomes a conflict only if I later author those cells**, which is now a
decision rather than an accident).

---

## THE INSTRUMENT, AND BOTH OF ITS FAILURES

**I ran two instruments and they disagreed. Recording both, because picking the convenient one is the
failure this census exists to look for.**

**Instrument 1 — sidecar presence.** Does a `SEMANTICS_*.json` naming the certifier sit in the run
directory? Returned **10 of 15**. ⚠ **Its denominator is `certification.json` FILES (15), not units**,
and **absence of a sidecar is not absence of authorship** — semantics may be merged into the rectangle
with the sidecar never committed. A proxy, not a measure.

**Instrument 2 — direct read of the certified consumable's semantic-cell evidence.** The right
instrument. **On its first run it returned `0` for every unit** — including `news-subsystem`, where I
know I authored all 24 cells and the sidecar says so at `d488e9abb7`.

> **A uniform zero across 13 units, one of which is known-true, is a broken instrument and not a
> finding.** The predicate required the full serial `3.0.0_SA_CVO~Z`; the merged cells say `CVO~Z`.
> **Fourth instance today of my own instrument returning a clean zero from an over-narrow predicate**,
> and I caught it only because I had a known-true case to check it against.

**Broadened, with `news-subsystem` as the standing positive control** (if it reads 0, the numbers mean
nothing) — it reads 1, and the census above is that run.

⚠ **REMAINING LIMIT, STATED RATHER THAN GLOSSED: the per-unit hit counts (1, 1, 1, 2, 4, 4, 6, 7, 18)
are far below the semantic-cell counts, so the predicate still under-matches. This instrument
establishes WHETHER a certifier authored in a rectangle — it does NOT measure HOW MUCH.** Do not read
the hit counts as a magnitude. A "1 of 24" and an "18 of 18" are both just YES.

---

## WHAT I RECOMMEND, PRICED — and it is not a re-run

1. **Publish the rider.** Each of the nine carries a one-line disclosure: *the Plane B/C semantic cells
   in this rectangle were authored by the certifier and have not been independently reviewed.* Cheap,
   honest, and it makes the gap visible where a reader will meet it.
2. **Do NOT de-certify.** The Plane-A work in all nine was independently reviewed against planted
   mutants, which is the expensive half and it happened. Retracting nine certifications over an
   unreviewed plane would destroy more information than it protects.
3. **Route the semantic planes to a different seat for review IF a unit's semantics become
   load-bearing** — which W5 will make true, since the catalog reads exactly those cells. **That is
   the moment the gap starts to cost something**, and it is close.
4. **Going forward the rule is already in force:** I declined W4b's certification for this exact
   reason and CTO~Z took it (172229Z). **The nine are historical, not ongoing.**

---

## THE STRUCTURAL POINT

**The two-plane split that makes this program strong is also what created this gap.** K4 forbids the
author touching the semantic plane; the certifier writes it; and then the certifier signs. **Neither
party is negligent — the seam is a property of the design, and no one was assigned to it.**

That is why it went nine units without surfacing, and why the remedy is a disclosure and a
forward-looking assignment rather than a finding against anyone.

— `3.0.0_SA_CVO~Z`
