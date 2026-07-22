# MDPF Item 1 — ALL inflection AUA spikes enumerated, and how many the reclass mechanism explains

**Verifier:** 3.0.0_SA_CVO · **Date:** 2026-07-22 · **Trigger:** Andrew-direct (~1205Z, via MSTR
@c66272d82): *"figuring out why Inflection's model numbers are jumping around july 6 july 7 **with some
other odd spikes in the daily trend timeseries**."*

**This supersedes my own @88851665d on scope.** That verdict answered ONE spike and stated no denominator.
Andrew's "other odd spikes" were never inside the evidence it ran. This establishes the denominator.

---

## HEADLINE — the count Andrew asked for

**6 spikes in the artifact he is actually served. My @88851665d mechanism explains 2 cleanly, 3 at most.
It does NOT explain 3.**

But the enumeration found something better than an attribution table: **5 of the 6 are ONE defect**, and it
is not the reclassification at all.

> ## THE LEGACY DATE AXIS IS NOT A TRADING-DAY AXIS.
> **It publishes 21 datapoints on days the market was closed (16 holidays + 5 weekends) and omits 20 real
> trading days.** The revamp axis is **427 / 427 trading days, zero holidays, zero weekends.**
> Every spike except one is that defect posting real moves onto wrong days, or collapsing several days of
> movement into a single print where days are missing.

Only **2026-06-03** is a genuine business event. The rest is the calendar.

---

## A. ENUMERATION — denominator first (verification-law 10)

**Population:** LEGACY `s3://opal-data-portal-v2/json/mdpf/inflection/aggregate-aua-timeseries.json` — the
artifact Andrew is served. **429 dates · 428 day-over-day transitions evaluated · 0 nulls.**
**Criterion:** |DoD| >= 5% on `model_aua` **OR** `non_model_aua` (I ran 5% / 2% / $3M absolute; the 6 below
are the >=5% set — the 2% and $3M passes add only ordinary market drift, no new structural events).

| # | Legacy date | What Andrew sees | dModel / dNonModel / dTotal | Explained by the 07-10 reclass? |
|---|---|---|---|---|
| 1 | **2026-05-18** | model cohort appears, 0 -> $93.6M | launch | **NO** — launch date; revamp dates it **05-15** |
| 2 | **2026-06-03** | +17.5% model | +16,961,432 / −16,894,760 / **+66,672** | **NO** — a *separate, larger, correctly-dated* reclass |
| 3 | **2026-06-09** | −7.3% non-model | +3,648,485 / −6,608,033 / −2,959,549 | **NO** — axis omits 06-08; two days collapse into one print |
| 4 | **2026-07-06** | +12.0% model, then | +14,632,452 / −14,001,633 / +630,819 | **YES** — the mislabel |
| 5 | **2026-07-07** | −9.7% model (the revert) | −13,296,913 / +14,662,452 / +1,365,539 | **YES** — same event, down-leg |
| 6 | **2026-07-16** | +10.1% model | +12,606,200 / −12,382,090 / +224,110 | **PARTLY** — same 07-10 reclass, mis-dated a *second* way |

**Tally: 2 of 6 cleanly (#4, #5). 3 of 6 if #6 is credited to the same underlying reclass. 3 of 6 not
explained at all (#1, #2, #3).**

**Proof for #4/#5 — value-match, not inference.** `136,859,722.32` appears in **both** artifacts: dated
**2026-07-06** in legacy, **2026-07-10** in revamp. Same number, different day. Legacy posts the real 07-10
move onto 07-06, so the series jumps and falls back — Andrew's *"jumping around july 6 july 7."*

**Why #6 is the same event, not a third one.** Legacy's axis goes **07-08 -> 07-16 directly**, omitting
07-09, 07-10, 07-13, 07-14, 07-15 — five consecutive trading days. The 07-10 reclass has nowhere to land, so
it surfaces at 07-16 as a fresh +$12.6M step. Same fingerprint as 07-10: total flat (+$224K against
+$12.6M model), **all 7 bands up together**, accounts +70.

---

## B. WHAT MY @88851665d GOT WRONG

**1. "ONE-TIME" is FALSIFIED.** 2026-06-03 carries the identical signature — +$16.96M model / −$16.89M
non-model / **total flat at +$67K** / **7 of 7 bands up together** / +44 accounts — five weeks earlier and
**larger than the event I wrote the verdict about**. DS has since source-confirmed the mechanism runs
*continuously in small batches* (eclipse `modelId` re-assignment on existing portfolios), not as one event.

**2. The scope error.** I explained one spike and let the finding stand for the whole complaint. Andrew
asked again *because the verdict was silent on the rest* — a right answer generalized past its evidence.
That is the wrong-axis failure with a correct instrument on it.

**What survives:** the *mechanism* (legacy date-mislabel of a real eclipse reclassification), and *"not real
AUM, not a revamp bug"* — total custody stays flat through every one of these.

---

## C. THE 06-03 CLEARANCE RESTS ON THE WRONG AXIS (correction to a live ruling)

CTO cleared 06-03 as a real event on **+44 account_count**; COO held a residual that this "establishes the
EVENT not the DATE." **COO's residual is correct, and the producer source proves why.**

`account_count` in the revamp is **not computed** — it is imported from the LEGACY served artifact by a
plain date-string join:

- `data/mdpf/scripts/gold/dim_mdpf_aggregate_aua_timeseries.py:476-498` @`78f25db36` —
  `load_served_account_count()` reads `SERVED_BUCKET = "opal-data-portal-v2"`, key
  `json/mdpf/{firm}/aggregate-aua-timeseries.json` (**the legacy artifact**).
- `:501-505` — `_account_count_series()` = `[counts_for_key.get(d) for d in dates]` — a **join on the date
  string**.

So account counts sit on **the very axis under suspicion**. They cannot corroborate a *date* for any event.

**The conclusion still holds, on different evidence: the revamp's VALUE axis is eclipse-anchored and
independently places the step at 06-03** (both artifacts carry `113,657,096.43` on 06-03 — a same-date
match, unlike 07-06). **06-03 is real and correctly dated. The +44-account evidence should be struck from
the ruling, not the ruling.** Right answer, unsound support — and the support is unsound in exactly the way
this whole item is about.

---

## D. INDEPENDENT THIRD LIMB — the count-axis defect inside the frozen-9

Reached from the artifact side before reading DS's or CTO's work; **converges with DS @`0e77885a2` and
CTO's reproduction.** Recording it as an independent limb, not a re-report.

The same date-join above imports legacy's *mislabeled* counts onto the revamp's *corrected* axis, so one
artifact reads its two axes from two different days:

| revamp date | `opal_intermediate` value | `opal_intermediate` accounts | |
|---|---|---|---|
| 2026-07-02 | $70.39M | 189 | coherent (pre-reclass) |
| **2026-07-06** | **$70.76M** (pre-reclass) | **207** (post-reclass) | **INCOHERENT — a row that never existed** |
| 2026-07-07 | $71.16M | 189 | coherent |
| 2026-07-10 | $76.12M (post-reclass) | **None** | value correct, count missing |
| 2026-07-16 | $76.14M | 207 | coherent |

Firm-level, the frozen-9 renders accounts **474 -> 540 -> 474** across Jul 6/7 — **a phantom 66-account
round-trip that never happened, reproducing Andrew's exact complaint on the count view.** Legacy was
wrong-but-coherent; the revamp is right-on-value-but-incoherent-in-the-row.

**This is a design defect, not an implementation bug** — the docstring states the intent ("imported ==
served EXACT"). You cannot both correct the date axis for values and exact-tie counts to the uncorrected
axis. **The fix is a ruling, not a patch.** Concur with the CTO ruling: fix-before-flip; *parity with a
known defect is not a virtue.*

---

## E. WHAT THE FLIP FIXES (on the value axis)

The revamp resolves **5 of the 6** as rendered values: #4/#5/#6 collapse into one correctly-dated 07-10
step, #3 resolves to 06-08, #1 moves to the true 05-15 launch. It does **not** change #2 (06-03) — **and it
should not: 06-03 is honest.** Residual business question, unchanged and now larger in scope: *are these
eclipse re-mappings into Opal-crosswalk models correct at the business level?* The pipeline faithfully
reflects whatever eclipse assigns; that is a mapping decision, not a data defect.

---

## F. GROUNDING

| Claim | Layer | Evidence |
|---|---|---|
| Andrew is served LEGACY | **exercised/live** | `EVTSA9VEHNZVH` = `opalinvest.dev`, **24 behaviors / 7 origins** — pre-flip (the flip is 24->33, @328248c13). Independently run, not taken from CTO. |
| Both artifacts, byte-exact | **applied** | own `ListObjectsV2`: inflection `cec5a0d6fe749aae77735f9297edbb71` size 153160 == bytes downloaded. Pin unmoved. |
| Spike population = 6 | **measured** | 429 dates / 428 transitions / 0 nulls; thresholds 5%, 2%, $3M all run |
| 07-06 == 07-10 same value | **measured** | exact value match `136,859,722.32` across artifacts |
| Axis defect 21 non-trading / 20 omitted | **measured** | full-axis classification vs weekends + US market holidays; revamp 427/427 clean |
| `account_count` imported from legacy by date-join | **SOURCE-CONFIRMED** | `dim_mdpf_aggregate_aua_timeseries.py:476-505` @`78f25db36` |
| 06-03 is a real reclass | **measured** | same-date value match both artifacts; 7/7 bands; total flat |
| *Whether eclipse's re-mapping is business-correct* | **UNRESOLVED** | mapping decision, owned by business/Eclipse — not a pipeline defect |

**Read-only throughout. Zero writes to the frozen-9. No producer change made by me.**

---

## G. WHAT I DID NOT COVER

- **Global and 49F.** This is inflection-only, as Andrew scoped it. COO's ~8 unattributed non-model
  NET-MOVEs (largest 2025-09-30->10-01 +$49.5M, month/quarter boundaries) are a separate population I have
  not attributed.
- **Pre-2026-05-15.** `by_model` bands carry values on only **38 of 427 dates**; band-level structure before
  the launch is not observable in these artifacts.
- **The count-axis sweep for 49F/global** is DS's, in flight.
