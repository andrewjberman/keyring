# ANDREW-DIRECT 2026-07-28 ~1743Z -- Part 2: the gold->platinum->portal serving bridge, its architecture, and eliminating DRIFT OPPORTUNITIES

**Recorded by:** `2.0.0_SA_COO` - **Channel:** Andrew directly at the COO terminal
**Received:** 2026-07-28T174328Z (read from `date -u`, not inferred)
**Recorded + broadcast:** same turn, per `org/XXX.md`
**Part 1 of the same initiative:** ~1741Z channel-trace directive @`db9b11524`

---

## VERBATIM

> "Once that is established, we need to identify what the mechanics are that bridge that gold table and the
> platinum serving layers that the portal consumes, and what is the architecture of that serving layer. I
> dont believe we have any client-side logic for this (we definitely should do this all server side, which I
> believe we do already). This is the second half of this initiative as you described, making sure we have
> full transparency and understnading on that architecture first, and then making sure that we dont have
> disorganized patterns, e.g. the issue whereby instead of jhust taking non-model assets from the 49
> generation, we are serverside aggregating "Global" aum-metrics separately. We do not want these drift
> opportunities, that is a major confound for all of us."

**NOT A PARAPHRASE. THE PHRASING IS THE RULING.**

---

## WHAT IT BINDS (surfaced, NOT adjudicated)

1. **SEQUENCED, and he sequenced it himself: *"Once that is established."*** Part 1 (channel -> feed ->
   schedule -> Gold DDB arrival) comes FIRST. This is the second half.
2. **TRANSPARENCY BEFORE REORGANISATION -- explicitly, and in that order:** *"full transparency and
   understanding on that architecture FIRST, and THEN making sure that we dont have disorganized patterns."*
   **Do not let a cleanup start before the map exists.** Same shape as his ~1725Z routes-before-monitoring
   ruling: understand the route, then make it canonical.
3. **THE TARGET IS A CLASS, NOT AN INSTANCE: "DRIFT OPPORTUNITIES."** The named example is one member.
   **The general form: any place a served value is RE-DERIVED instead of TAKEN from a single generation is a
   drift opportunity**, because the two derivations can disagree and nothing detects it.
4. **He states a BELIEF and flags it as one** -- *"I dont believe we have any client-side logic for this... which
   I believe we do already."* **That is a premise to VERIFY, not inherit.** Verified below; **it is FALSE for
   the Global headline.**

---

## ⚠ IMMEDIATE FINDING, MEASURED BEFORE THIS RECORD WAS COMMITTED: THERE **IS** CLIENT-SIDE AGGREGATION

**Source-confirmed, `portal/src/pages/ModelPortfolios.tsx:1164-1172`** (portal worktree on `DEV`, read
directly -- a React page component, i.e. **browser-side**):

```tsx
const totalAUMOrNull = effectiveFirmId !== 'global'
  ? (perFirmAumMetrics?.total?.aum ??
      (perFirmMdpfData ? lastRealPoint(readFirmAggregateSeries(perFirmMdpfData))?.value ?? null : null))
  : null
const totalAUM = effectiveFirmId !== 'global'
  ? (totalAUMOrNull ?? 0)
  : trendLastPoint
    ? trendLastPoint.aum + getNonModelAumForDate(nonModelData?.time_series, trendLastPoint.period)
    : modelAUM + (nonModelData?.latest?.non_model_aum || 0)
```

**THE ARCHITECTURE IS ASYMMETRIC, AND THE ASYMMETRY IS THE DEFECT:**
- **PER-FIRM** (`effectiveFirmId !== 'global'`): **TAKES a served total** -- `perFirmAumMetrics.total.aum`.
  One artifact, one generation, no arithmetic.
- **GLOBAL**: **COMPUTES, IN THE BROWSER**, by summing `trendLastPoint.aum` (the model series) with
  `getNonModelAumForDate(nonModelData...)` -- **a lookup into a SECOND, INDEPENDENTLY-PRODUCED artifact.**

**So Andrew's exact example is real, and it is one layer further out than he thought: Global aum-metrics
are not aggregated separately server-side -- they are aggregated separately CLIENT-side.**

**AND IT IS THE MECHANISM BEHIND TODAY'S $1.92B.** `0.2.0_DT` reproduced the rendered headline to the cent
as `1,924,186,044.47` = restored REVAMP model leg (`1,676,493,815.11`) + **un-restored LEGACY** non-model leg
(`247,692,229.36`), against a correct artifact headline of `1,951,676,164.42`. **The two legs come from two
producers with no arbitration, and the browser adds them.** Delta `27,490,119.95`, persistent for 2+ weeks.
**That is not a bug in either producer. It is the drift opportunity Andrew is naming, realised.**

**A NOTE ON THE CODE'S OWN COMMENT (`:1160-1163`)**, which makes this sharper rather than softer: it states
basis discipline explicitly -- *"it never sums across bases and never substitutes one labeled quantity for a
DIFFERENT rendered claim."* **That discipline is applied to the PER-FIRM branch and not to the GLOBAL
branch, in the same expression.** The rule was written, understood, and then not applied to the one branch
that sums.

**SCOPE OF THIS FINDING, stated so it is not over-read:** I read ONE file at ONE location. I have **not**
traced whether `nonModelData` is itself server-aggregated, nor swept the portal for other client-side
derivations, nor established that this is the only one. **The client-side sum at `:1171-1172` is measured;
"this is the only instance" is NOT claimed.** A portal-wide sweep for re-derivation sites is exactly the
Part-2 transparency work and it is not done.

---

## THE TRAP FOR PART 2, STATED BEFORE THE WORK STARTS

**A trace of how bytes DID arrive cannot enumerate what else COULD write, or what never ran.** That is
CTO's own diagnosis of why the 07-24 lineage trace (mine) produced five falsified premises. **Part 2 is a
lineage-trace-shaped task and will reproduce that failure unless it is built the other way: enumerate what
the RENDER CONSUMES and work backwards, not what a producer emits and work forwards.** The five-member
atomic set was found that way this afternoon; four-member was found the other way.

---

## STATUS AT TIME OF RECORD

Part 1 not started (recorded ~2 min earlier). Part 2 correctly sequenced behind it by Andrew's own
*"once that is established."* Broadcast to `1.0.0_SA_CTO` (PRD owner / arch gate), `0.0.0_AB_MSTR` (record
custody), CC `3.0.0_SA_CVO` + `0.2.0_DT_PortfolioAnalytics` (owns the portal surface and produced the
headline reproduction). **No writes; nothing dispatched; `/drive` OFF.**

-- `2.0.0_SA_COO`, 2026-07-28T174328Z
