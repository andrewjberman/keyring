# NEWS TREND-ANALYSIS CONCEPTS — originated by `3.0.0_SA_CVO~Z`

**Andrew-direct 2026-08-11:** *"later, news trend-analyses concepts."* · **PRD §517** sequences these inside the W3b certifier role, so they ride the certification hand-back.
**Substrate:** `news-subsystem/20260811T2330Z`, **certified by me at 0352Z** — 4 entities, 722 keys reconciled exactly, one plant detected. **Every number below is measured, not estimated, and each carries where it came from.**

> ⛔ **CONCEPTS ONLY. Nothing here is built, scheduled, or proposed for build.** No alert, alarm, SNS, SES, freshness checker or monitor appears in any concept — the standing moratorium is absolute and these ideas are exactly the kind that tempt one.

---

## 0. THE ONE FACT THAT SHOULD DRIVE EVERY DECISION HERE

**We already own a keyword-level sentiment time series. It is 720 files, 58 write dates, 2026-01-05 to 2026-04-07 — and it stopped because a scheduled job is switched off.**

**Not broken. Not missing. Not expensive. Switched off**, on a Lambda that still exists (`opal-keyword-drilldown-generator`, py3.12, `DAYS_BACK=14`) reading a DynamoDB table that is still there.

>> **SO THE HONEST HEADLINE IS NOT "WE SHOULD BUILD NEWS TREND ANALYSIS." IT IS: WE BUILT IT, IT RAN FOR THREE MONTHS, AND NOBODY NOTICED IT STOP.** Four months of silence, and the finding surfaced only because a decomposition run enumerated the prefix key by key. Every concept below is cheap **if that cron comes back** and largely hypothetical if it does not. **The decision is Andrew's; I am putting the price on the table, not choosing.** <<

**And the reason nobody noticed is itself the most reusable lesson:** `json/sentiment/` contains 2 keys written hours ago beside 720 dead four months. **A prefix-grain freshness read returns HEALTHY on 2 of 722.** *(This is W3a's K12 at 720× scale — and it is a reason freshness must be artifact-grain **when it is measured at all**, not a reason to build something that measures it.)*

---

## 1. WHAT EXISTS TODAY, AND THEREFORE WHAT AN ANALYST CAN ACTUALLY SAY

| asset | state | what it supports |
|---|---|---|
| `fear-greed-index.json` | **LIVE**, 2×/day, cron ENABLED | today's market mood, one composite number |
| `keyword-sentiments.json` | **LIVE**, written 2026-08-11 | today's mood **by topic** (FinBERT, per keyword) |
| 360 × history-summary | **FROZEN** 2026-04-07 | per-keyword sentiment **trend**, through early April only |
| 360 × history-articles | **FROZEN** 2026-04-07 | the **articles behind** each score — the "why" |

**The gap this exposes is not a data gap, it is a TIME gap: we can say what mood is, and we cannot say what mood is DOING.** Every concept below is an attempt to answer *doing*.

⛔ **THE STANDING TRAP, and it is the one I would guard hardest:** joining a live point to the frozen series to manufacture a trend line. **It produces a chart that is false in exactly the way a reader cannot detect** — a smooth curve with a four-month hole rendered as continuity. *Any concept that touches both populations states its end date in the same sentence.*

---

## 2. THE CONCEPTS

### C-1 · SENTIMENT DIVERGENCE — *the one I would do first*
**Question:** which topics are moving **against** the market's overall mood?
**Mechanism:** per-keyword sentiment vs. the fear-greed composite, same day. A keyword deteriorating while the index is greedy is a *specific* thing to look at.
**Why first:** it is the only concept that is **fully live today** — both inputs are current, no frozen data touched, nothing to re-enable. **It also needs no history at all**, because divergence is a cross-sectional question, not a longitudinal one.
**Honest limit:** a divergence is a *pointer*, never a signal. It says *look here*, and it does not say *why* — the "why" lives in the frozen article tier.

### C-2 · TOPIC PERSISTENCE — *the cheapest thing the revived cron would unlock*
**Question:** is this topic's sentiment a **spike or a trend**?
**Mechanism:** how many consecutive days a keyword has held its sentiment direction. The existing summary files already carry exactly the shape this needs.
**Why it matters:** it separates *the market panicked about this for one afternoon* from *this has been getting worse for three weeks* — **which is the single most common question a human asks after being shown a sentiment number**, and today we cannot answer it at all.
**Precondition:** the cron. Nothing else. *The Jan–Apr data already proves the shape works.*

### C-3 · KEYWORD EMERGENCE
**Question:** what is being talked about now that **was not** three months ago?
**Mechanism:** set difference between today's live keyword set and the frozen historical keyword set.
**Peculiar property, and it is the reason I like it:** **this one gets BETTER the longer the cron stays off**, because the frozen set is a clean, dated baseline. It is the only concept that turns the freeze into an asset rather than a loss — **and that is precisely why it must never be used as an argument for leaving the cron off.**

### C-4 · SENTIMENT-TO-POSITION PROXIMITY — *highest value, highest risk, and the risk is not technical*
**Question:** are the topics moving sentiment ones **we hold exposure to**?
**Mechanism:** keyword set against holdings/sector exposure.
**Why it is the most valuable:** it is the only concept that connects news to the book. Everything else is market colour.
**⛔ WHY IT IS THE MOST DANGEROUS, and it is a semantics problem rather than a data problem:** a keyword is **not** a ticker and **not** a sector. "banking" is not a bank position. **The join is a HEURISTIC and any output must say so in the artifact, not in a footnote** — because this is exactly the output that gets screenshotted into a client conversation, and a proximity score reads as a risk measure to anyone who did not build it. *This concept needs a semantics ruling before it needs an implementation.*

### C-5 · ARTICLE-BACKED EXPLANATION
**Question:** *why* is sentiment on this topic where it is?
**Mechanism:** the Tier-2 article lists are already the citation layer under every score.
**Status: BLOCKED, and precisely.** The articles are four months old. This concept is **not** waiting on design — it is waiting on the same cron as C-2. **It is worth naming because it is the concept that makes every other one defensible:** a sentiment number nobody can trace back to an article is a number an analyst cannot stand behind in a room.

---

## 3. THE ORDERING, AND WHY IT IS NOT THE OBVIOUS ONE

**C-1 is buildable today. C-2, C-3 and C-5 all reduce to ONE DECISION about ONE EventBridge rule.**

>> **So the sequencing question is not "which concept first." It is: DO WE WANT THE KEYWORD SENTIMENT HISTORY OR NOT?** Answer yes and three of five concepts become cheap at once. Answer no and the 720 keys are residue, C-2/C-3/C-5 are hypothetical, and C-1 is the whole product. **Nothing here should be built until that is answered, because building C-1 alone and then reviving the cron would mean designing the same surface twice.** <<

**And the decision has a fact missing from it that I could not supply and did not invent:** *the run measured **when** the cron was disabled as `NOT_MEASURABLE` with a named discriminator, and **why** is unknown.* **A cron switched off deliberately for a recorded reason and a cron switched off by accident lead to opposite answers**, and nobody currently knows which this was. **That question is cheaper to answer than any concept here and it gates all of them.**

---

## 4. WHAT I AM NOT DOING

- **Not building anything**, not proposing a schedule, not touching a cron. Rule 9 and the moratorium both.
- **Not choosing** between retire and revive. That is Andrew's, routed via CTO~Z, and I have priced it rather than pre-empted it.
- **Not treating C-4 as ready.** It needs a semantics ruling on what a keyword↔holding join is permitted to claim, and that ruling is arguably Andrew's too.
- **Not claiming this list is complete.** These are the concepts the *measured substrate supports*. A concept requiring data we do not have is not on it, and its absence is not evidence that nothing else is worth doing.

— `3.0.0_SA_CVO~Z`, 2026-08-12 ~0358Z · substrate: `news-subsystem/20260811T2330Z`, certified 0352Z
