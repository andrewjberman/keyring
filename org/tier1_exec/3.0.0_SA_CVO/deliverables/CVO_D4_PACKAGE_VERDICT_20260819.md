# CVO VERDICT — D4 package (ETF Positioning Variant)

**Reviewer:** `3.0.0_SA_CVO` · **Date:** 2026-08-19 · **archetype:** VALIDATE
**Package scored, vintage-pinned:**
- `docs/architecture/D4_ETF_POSITIONING_VARIANT_PRD.md` @8d662d5f1f (187 lines)
- `org/tier1_exec/1.0.0_SA_CTO/deliverables/D4_ATOMDECOMP/run_20260819.md` @8d662d5f1f (54 lines)

**Verdict: ACCEPT — 0 P0, 2 P1.** Both P1s are things I MEASURED rather than inferred, and one of them
may save a sovereign egress ask. Four things this package does right, stated first because they are the
counter-examples to defects I filed elsewhere tonight:

- **§5.3 records the run FALSIFYING a pre-authoring assumption** — *"the 'no composition data'
  assumption was WRONG and corrected pre-authoring"* — turning a build-from-nothing backend into
  extend-coverage-and-project. **A major descope, caught by the chain, before decomposition.**
- **§4.2 specifies the producer as SCHEDULED (cron)**, citing production-pipelines-must-be-scheduled
  explicitly. **Direct contrast with D7's agent-loop trigger** (my D7 P1-1) — same author, same night,
  the rule applied correctly here.
- **§4.2's missing-day handling applies NEVER#1 correctly** — prior `data_as_of` + explicit staleness
  field, *"weekends per trading calendar"* — rather than treating a weekend gap as a defect.
- **§4.3's failure mode is VISIBLE** — *"ETF artifacts absent -> ETF mode disabled with dark-text
  notice"*. **Direct contrast with D1's invisible fallback** (my D1 unknown-unknown). A user can tell.

---

## P1-1 — For CTO. §2 generalizes a one-day absence into a standing property. I ran the series census: your conclusion is CORRECT, and it now has 67 observations instead of 1.

Run R7 is carefully scoped: *"COVERAGE = PFDE (90 rows) + PFOE (24 rows) ONLY **on 2026-08-18**; DIVZ +
IDVZ ABSENT"* — one date, and it says so. **§2 then drops the scoping:** *"covering PFDE + PFOE ONLY;
DIVZ + IDVZ **have no holdings rows**"* — stated as a property of the plane. That generalization
motivates backend atom (1), TO-D4b (1–3 sessions), and Q1's contemplated **vendor-egress ask to
Andrew**, which is a sovereign act.

**The asymmetry is the tell:** TO-D4b's *acceptance* correctly demands *"4/4 universe tickers present in
silver/holdings for **3 consecutive days**"* — the author is alert to one-day flukes at acceptance time,
while the state claim that motivates the whole workstream rests on n=1.

**Measured this session (denominators printed):** `silver/holdings/` holds **67 objects**, sizes
**16,292 – 16,973 B**, a **4% spread**, against the known anchor of 16,957 B = 114 rows (PFDE 90 + PFOE
24) on 08-18. **No object is materially larger**, so no date carries a substantially larger row count —
two additional funds' holdings could not hide in a 4% band. **Your conclusion holds across the whole
series, not just 08-18.**

**Stated caveat, because it is a proxy:** object size is not a row count — parquet compresses, and a
column-level change could move bytes. A per-file groupby would be definitive. But a 4% spread across 67
files against a known-row anchor is strong support, and it is 66 more observations than the claim had.

**Recommend:** re-scope §2's sentence to the series with this denominator, or cite R7's date. The
finding is methodological, not factual: **an n=1 absence that motivates a multi-session workstream and
a possible sovereign egress ask should carry its series check** — and here the check was two commands.

**Bonus, partially closing U3** (*"holdings history completeness May-18..08-18 — TO-time census"*): 67
objects across a ~92-calendar-day span is consistent with a business-day cadence with no material gaps.
The TO-time census is now cheap and pre-framed.

---

## P1-2 — For CTO. The estate ALREADY HOLDS DIVZ and IDVZ holdings, in the shape you need. TO-D4b is aimed at a feed and a possible vendor ask without checking what we have.

TO-D4b Phase 1 is scoped as *"trace `etf_netassets_watch` (comp-find + comp-pipescript io; where does
filepoint deliver, what funds can it deliver)"*, and §7 Q1 escalates: *"if a NEW vendor/feed is
required, that is a **vendor-egress word for Andrew** (standing law)."*

**Measured this session:**

```
research_transcripts/analysis/source_divz_holdings_20260731.csv   2,790 B   30 rows (29 + header)
research_transcripts/analysis/source_idvz_holdings_20260731.csv   4,010 B
```

Header: `Date,Account,Stock Ticker,CUSIP,Security Name,Shares,Price,Market Value,Weightings,Net Assets`
Row 1: `7/31/2026,DIVZ,SALXX,857492656,STATE STREET INST U.S. GOVERNMENT MMKT ADMN CLASS,5986373.08,100,5986373.08,2,299025342`

**Compare against R7's parquet schema** (`holding_ticker / cusip / security_name / shares / price /
market_value / weight_pct / fund_net_assets`): **the CSV carries the same eight fields, matched by
content** — `Stock Ticker`→`holding_ticker`, `Weightings`→`weight_pct`, `Net Assets`→`fund_net_assets`,
with `Account` as the fund key. **This is DIVZ and IDVZ holdings data in the shape the ETF silver plane
needs, and it is already in the repo.**

**What this does and does not establish — stated precisely, because the distinction is the whole
finding.** It does **NOT** solve the source: a one-off 07-31 CSV is not a daily feed, and its provenance
is unknown. It **DOES** establish that **someone obtained DIVZ+IDVZ holdings on 2026-07-31**, so the
question *"does a source exist at all"* is answered YES, and TO-D4b's first act should be *"where did
these come from"* rather than *"can filepoint deliver them."* **If that provenance is an existing
entitlement, the contemplated vendor-egress ask to Andrew may be unnecessary** — and an unnecessary
sovereign ask is not free.

**This is BUILD LADDER rung 2 across a PRD boundary**, and it is invisible to protocol §6: that check
asks whether *the file you are declaring NEW* already exists, not whether *the data you are about to
source* is already in the estate. **Recommend adding one line to TO-D4b Phase 1** — establish the
provenance of `source_{divz,idvz}_holdings_20260731.csv` before scoping a feed extension or an egress
request.

---

## Explicit deferrals

- **§3b ETFS_CANON reconciliation** — the siblings ruling (ownership plane vs composition plane) is
  correct against R8/R9, and it **explicitly names the one-word-two-things collision** *"so no wave lane
  conflates them."* That collision is a live estate hazard with its own memory record; naming it in the
  ruling is the right handling. Five DE defaults accepted as orthogonal — verified they are, all
  ownership-plane. **No finding.**
- **Verdict vocabulary undeclared** (uses MEASURED / "MEASURED (record)" / "MEASURED (08-18, same
  seat)") — sixth variant across eight packages; covered by your @36a7fbd70e family ruling, conform at
  absorption. R3's reuse of 08-18 rectangle cells **states its vintage**, which is the part that
  matters.
- **TO-D4b acceptance derives from R5** (universe = exactly the four, MEASURED), not from a
  record-sourced row. **No illegal derivation** — checked specifically.
- **Q2 attribution scope lever** — correctly framed as Andrew's scope choice with a proposed default,
  not an assumption.

---

## What you should have asked but did not

**One unestablished source now underpins TWO of your ten PRDs, and neither one owns it.**

The `source_{divz,idvz}_holdings_20260731.csv` files I found are not incidental — **they are D5's
analytical basis.** D5 §4 states the alt-research queue's ETF weight side *"refreshes when new holdings
snapshots land (sources: `source_{divz,idvz}_holdings` CSVs)"*, and §7 Q1's activation default is
*"top-5 by firm weight"* computed from them.

So the same two files are simultaneously:

- **D5's** materiality-ranking input, feeding a build queue that activates on Andrew's word; and
- **the only DIVZ/IDVZ holdings data in the estate**, which D4 is about to spend 1–3 sessions and a
  possible sovereign egress ask to re-source.

**Neither PRD names an owner for them, and neither knows the other depends on them.** D4 does not
mention them at all; D5 treats them as a given input with no producer. **Nobody owns the refresh**,
which is exactly why D5's weights are frozen at 07-31 (my D5 unknown-unknown) — and it means the D4
workstream, if it succeeds, would *solve D5's staleness as a side effect nobody planned or would
notice.*

**Recommend, cheap and once:** TO-D4b's provenance finding is reported to **both** D4 and D5, and
whichever program lands a standing DIVZ/IDVZ holdings feed declares itself the owner, with the other
consuming it. Otherwise the likely outcome is two sources for one fact — the two-homes defect D3 named
by name, arrived at from opposite directions.

— 3.0.0_SA_CVO
