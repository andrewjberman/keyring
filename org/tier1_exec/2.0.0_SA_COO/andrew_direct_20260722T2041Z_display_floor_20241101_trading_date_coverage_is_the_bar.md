# ANDREW-DIRECT 2026-07-22 ~20:41Z — THE BAR IS CORRECT-DATE CONSISTENCY + FULL TRADING-DATE COVERAGE, NOT DEPTH. Display floor is 2024-11-01. Short histories are EXPECTED, not defects.

**Channel:** Andrew direct at the `2.0.0_SA_COO` terminal (this session), 2026-07-22 ~20:41Z.
**Context:** delivered mid-turn while MDPF_3FIRMS lanes were executing, in response to depth findings
surfaced from 3F-B2 (SmartX) and 3F-S2 (DS's 49F bronze-vs-silver head-gap).
**Recorded same-turn per `org/XXX.md`.** Broadcast: MCP to `1.0.0_SA_CTO` + `0.0.0_AB_MSTR`, and
propagated to the affected lanes (`0.6.2_AE_PartnerETL~A`, `0.4.0_DS_ClientPlatform`).

---

## VERBATIM (do not paraphrase — the phrasing IS the ruling)

> "We only display 11-01-2024 onward anyway in the MDPF aum-timeseries chart element, so its not a huge
> priority to get super ancient stuff. I don't believe that we even have full model data before November
> 2024, I think the first model recording that appeared in smartx is sometime in September. We just want
> to make sure we have consistent and validated values on the correct dates, and full coverage on
> trading dates. Some firms are not going to have that much history. Inflection only started migrating
> models on May 15 2026, and anything before is inherently non-model; the interest in their validation
> is a function of checking those July dates. Cottonwood we don't even have the means to do Backfill at
> this state, all we can do is get aum-metrics and the bell curve distribution from them."

---

## What it establishes (surfacing, NOT adjudicating — carrier/TO amendments are CTO's)

1. **A DISPLAY FLOOR OF 2024-11-01.** The MDPF aum-timeseries chart renders 2024-11-01 onward. Depth
   below that floor is **"not a huge priority"** — explicitly deprioritized, not forbidden.

2. **THE ACTUAL BAR, IN HIS WORDS: "consistent and validated values on the CORRECT DATES, and FULL
   COVERAGE ON TRADING DATES."** This is a **CORRECTNESS + COVERAGE** standard, not a depth standard.
   **Restated: depth is not the goal; a right value on a right date, with no trading day missing, is.**

3. **SHORT HISTORIES ARE EXPECTED AND ACCEPTABLE.** "Some firms are not going to have that much
   history." A shallow series is a fact about a firm, **not a defect to be repaired**.

4. **INFLECTION: MODELS BEGAN 2026-05-15. ANYTHING BEFORE IS INHERENTLY NON-MODEL.** This is a
   **KNOWLEDGE CLAIM ABOUT THE WORLD, not a data-availability statement** — and it directly answers an
   open TO question (see below).

5. **THE POINT OF INFLECTION VALIDATION IS THE JULY DATES.** "the interest in their validation is a
   function of checking those July dates" — i.e. **3F-B7 IS the Inflection deliverable**; deep
   Inflection backfill is not.

6. **COTTONWOOD: NO MEANS TO BACKFILL AT THIS STATE.** "all we can do is get aum-metrics and the bell
   curve distribution from them" — which is **exactly 3F-G8's scope**, and confirms current-state-only.

---

## Direct consequences for live TOs (routed to CTO; COO does not amend the PRD)

| TO | Consequence |
|---|---|
| **3F-B1** (49F depth) | DS measured a contiguous head-gap **2024-01-12..2024-05-23** (bronze 632 dates vs silver 540). **That entire gap sits BELOW the 2024-11-01 display floor.** Deprioritized. The live half of B1 — zero missing TRADING days in the served window — is the part that matters. |
| **3F-B4** (eclipse) | The TO asks to "determine vendor depth pre-05-15." **ANSWERED BY ANDREW: models began 2026-05-15, so there is no pre-05-15 model history to find.** The silver floor at 2026-05-15 is **CORRECT, not a gap.** The remaining live question is the **07-01/13/14/15 recoverability verdict** — inside the July window he cares about. |
| **3F-B6** (COT temporal probe) | "we don't even have the means to do Backfill at this state" is consistent with the probe's purpose being **evidence**, not enablement. ⚠ CTO's cascade explicitly ruled the probe EXECUTES; this does not countermand that — but its PRIORITY relative to B5/G8 is now a CTO question. |
| **3F-B7** (INF July) | **ELEVATED AND CONFIRMED as the Inflection deliverable.** Already Andrew-priority; this restates why. |
| **3F-G8** (COT current-state) | **CONFIRMED as the correct and complete Cottonwood scope.** |
| **3F-S2** (DS census) | Denominators should be read against the **trading-date** standard and the display floor, not maximal depth. A pre-floor absence is not an unexplained gap. |

---

## ⚠ AN OPEN DESIGN QUESTION THIS CREATES — ROUTED TO CTO, NOT DECIDED HERE

**"anything before [2026-05-15] is inherently non-model" is a statement that Inflection's model_aum was
ZERO before that date — not that it is UNKNOWN.**

That distinction is load-bearing and it collides with a settled rule:
- **PRD §1.1:** where only one side exists for a date, `non_model` is **"not computable and renders as
  absent — never fabricated, never rolled silently."**
- **But if model_aum is KNOWN to be 0 pre-05-15**, then `non_model = total_aua − 0 = total_aua` **is**
  computable, and the Inflection non-model series could extend back as far as Orion's `fact_assets`
  (which reaches **2020-04-28**) rather than starting at 2026-05-15.

**This is precisely the knowing-zero vs missing-data line, and getting it backwards in either direction
is a defect:** writing 0 where data is merely absent is fabrication; rendering absent where we *know*
the value was zero throws away real, correct history the chart could show from the display floor onward.

**COO does not decide this.** It interacts with settled ruling #3 (2-term non_model), §1.1's
absent-not-fabricated rule, and the Cottonwood additive/self-extending constraint. **CTO's call.**

---

## What this does NOT change (stated so nobody over-reads a deprioritization as a lift)

- **Full trading-date coverage IS still required** — he named it explicitly as the bar. Deprioritizing
  ancient depth is not deprioritizing coverage.
- **NEVER#1** — the trading calendar still resolves before any absence is called a gap.
- **17a / Rule 17 / no-ad-hoc-gold-runs / the eclipse `--date` ban / LD-0333's single path** — all
  untouched.
- **Cottonwood backfill remains the DEVELOPING SUBJECT**; this reinforces it rather than closing it.

-- `2.0.0_SA_COO`
