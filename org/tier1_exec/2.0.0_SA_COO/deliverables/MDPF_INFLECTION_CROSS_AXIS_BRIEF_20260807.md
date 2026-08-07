# MDPF INFLECTION CROSS-AXIS REFUSAL — the freshness-qualification defect

**Author:** `2.0.0_SA_COO` · 2026-08-07 ~2320Z · **For:** `1.0.0_SA_CTO`
**Status:** ANDREW-DIRECT NEXT-HIGHEST PRIORITY. **His hypothesis is CONFIRMED by the gate's own
error text**, below.
**Grounding:** every figure re-derived at the COO seat in TRUE UTC (`list-objects-v2` LastModified,
never `aws s3 ls` — that renders local EDT and is a 4-hour trap). Source citations are `file:line`
at HEAD 2026-08-07.

---

## 0 · ANDREW'S CALL, VERBATIM

> *"I suspect based on what youre saying that its some kind of issue about the qualification of the
> freshness (that D+0 D+1 logic), will need to comprehensively look over it"*

**He is right, and the gate says so in its own words.** `dim_mdpf_aggregate_aua_timeseries.py:1583`
raises with the literal string:

> *"signature of a roster imported from a different day than the values on this date"*

The defect is a **DATE-ALIGNMENT DISAGREEMENT BETWEEN TWO AXES** — exactly the D+0/D+1 qualification
question. This brief is the grounding for the comprehensive pass, not the fix.

---

## 1 · WHAT THE GATE ACTUALLY CHECKS — source-confirmed, two limbs

`data/mdpf/scripts/gold/dim_mdpf_aggregate_aua_timeseries.py:1569-1594`

**LIMB (v) — PRESENCE DISAGREEMENT.** Per date `i`, fails when
`(model_value[i] is None) != (account_count[i] is None)`.
*One axis has data for a date and the other does not.*

**LIMB (vi) — FOREIGN-DAY ROSTER.** Walks `total account_count` across consecutive dates and fires on
a **round-trip excursion**: `a -> b -> c` where `out` and `back` have opposite signs and
`min(|out|,|back|) > |net|`. The code's own gloss:

```
"the round-trip excursion exceeds the net drift: signature of a roster
 imported from a different day than the values on this date"
```

It deliberately does NOT fire on: a flat series, a persisting move (a real change), or a monotone
trend. **It fires only on a bump-and-return — the shape a wrong-day roster makes.**

**⚠ AND THE CHECK IS NOT UNIFORM ACROSS FIRMS.** `:1562-1567` records that for one firm the
cross-axis check is **SKIPPED** because *"count axis reads the legacy served import, not the value's
feed — RETAINED STRUCTURAL EXPOSURE (49F decouple is a PREREQUISITE for cross-axis coverage here),
not a clean result."* It even measures and prints the exposure it is not checking.
⇒ **49financial is EXEMPT FROM THE CHECK THAT INFLECTION IS FAILING.** Any comparison between the
two firms' outcomes must account for that or it is comparing a checked axis to an unchecked one.

---

## 2 · THE MEASURED TIMELINE — and it inverts the obvious remedy

All UTC.

| when | what |
|---|---|
| `2026-08-07T03:52:16Z` | inflection + global A4 written, **data date 2026-08-05** — the last successful inflection build |
| `2026-08-07T13:00Z` | scheduled floor fires. Morning error list = `['cottonwood','global']`. **No inflection A4 write at this time** — see §4 |
| `2026-08-07T22:31:10Z` | eclipse + orion inflection silver **data 2026-08-07 LANDS** |
| `2026-08-07T22:46:43Z` | `mdpf-gold-lambda` fired ad hoc (Andrew-direct QA) |
| `2026-08-07T22:47:19Z` | **inflection REFUSES on the cross-axis gate.** 49F + cottonwood A4 written, data 08-06 |

**INFLECTION HAD 16-MINUTE-OLD DATA WHEN IT REFUSED.**

> ### ⛔ THE INVERSION, AND IT IS THE MOST IMPORTANT LINE IN THIS BRIEF
> This morning at 13:00Z the newest inflection silver was **2026-08-05 — two days stale** (08-06 is
> missing, 08-07 had not landed). Inflection was **NOT** in the morning error list.
> Tonight at 22:47Z it had **16-minute-old** data and **FAILED**.
> **IT PASSES ON STALE DATA AND FAILS ON FRESH DATA.**
> ⇒ **Moving the floor LATER gives inflection FRESHER data and will surface this failure MORE
> OFTEN, not less.** The W1-5 re-time is still worth doing — it converts an accidental head start
> into a stated contract — but it is NOT the fix and must not be reported as one.

---

## 3 · THE FEED ANOMALY — the likely proximate cause

eclipse `fact_model_composition` + orion `fact_positions`, true UTC writes:

```
data 2026-08-01 -> 2026-08-02T03:30:30Z   T+1 03:30
data 2026-08-02 -> 2026-08-03T03:30:30Z   T+1 03:30
data 2026-08-03 -> 2026-08-04T03:30:30Z   T+1 03:30
data 2026-08-04 -> 2026-08-05T03:30:30Z   T+1 03:30
data 2026-08-05 -> 2026-08-06T14:16:05Z   OFF-PATTERN
data 2026-08-06 -> ** MISSING FROM BOTH FEEDS **      <- 2026-08-06 was a THURSDAY
data 2026-08-07 -> 2026-08-07T22:31:10Z   OFF-PATTERN, SAME-DAY
```

**Both feeds agree on coverage** — identical date sets, both missing 08-06. So this is **NOT** an
eclipse-vs-orion disagreement; the incoherence is between the **VALUE axis and the COUNT axis**
within inflection.

**A MISSING TRADING DAY IN THE MIDDLE OF A SERIES IS EXACTLY WHAT LIMB (vi) DETECTS.** If the count
axis carries 08-06 (from a different source or a carry) while the value axis does not, or if the
roster for 08-07 is joined to values from 08-05, the account_count series makes a bump-and-return —
the foreign-day signature.

**⚠ NOT CLAIMED:** I have not read the actual failing per-date output. The above is the mechanism the
gate is built to catch matched against the anomaly present. **It is a HYPOTHESIS, not a diagnosis**,
and it cannot authorise a fix (Rule 22).

**⚠ AND CHECK THE CALENDAR FIRST.** 08-06 is a Thursday, so a weekend does not explain it — but the
comprehensive pass must resolve the trading calendar before calling any date missing. `T-1` is the
default for every AUM/holdings pipeline unless it explicitly qualifies otherwise.

---

## 4 · THE UNRESOLVED FACT — flagged rather than papered

**Inflection's A4 was last written `2026-08-07T03:52:16Z`. There is NO inflection write at the 13:00Z
scheduled fire.** That is in tension with the morning error list naming only `cottonwood` and
`global`.

Two readings, and they are materially different:
- (a) inflection **also failed at 13:00Z** and it was not logged → **a second failure nobody saw**
- (b) the consolidator **skips a rebuild when the data date has not advanced** → benign

**I cannot discriminate these from outside and I am not guessing.** Resolving it is step one of the
comprehensive pass, because under (a) the morning error list is not trustworthy as a record.

---

## 5 · WHAT "COMPREHENSIVE" HAS TO COVER

1. **The D+0/D+1 qualification itself** — for each axis (value, count, roster), which DAY's data does
   it read, and is that stated anywhere or emergent? Andrew's named suspicion.
2. **Resolve §4** — did inflection fail silently at 13:00Z, or does the consolidator no-op a
   non-advancing date?
3. **The 08-06 gap** — why both feeds skipped a Thursday, and whether the two off-pattern writes
   (08-05 late, 08-07 same-day) share a cause. Trading calendar resolved FIRST.
4. **The 49F exemption** (`:1562`) — one firm is exempt from the check another is failing. Is that
   still warranted, and is the "49F decouple" prerequisite still open?
5. **Read the actual failing per-date rows** — limb (v) prints up to 5 presence disagreements and
   limb (vi) prints up to 5 roster excursions. **Nobody has read them yet.** That is the cheapest
   next measurement and it likely names the defect outright.

---

## 6 · WHAT IS NOT WRONG, so the pass does not re-derive it

- **The gate is not miscalibrated.** It is refusing to emit rather than emitting a wrong number, and
  it prints its evidence. Treat it as the instrument working.
- **Global is not separately broken.** `mdpf_gold_consolidator.py:792-802` requires ALL THREE firm
  legs; global skips whenever any one fails. **Every `6/12` is ONE firm plus global riding behind
  it.**
- **Cottonwood is currently fine** — it failed this morning on a `value_date` collision (register
  row R-18, the vintage race, firing exactly as predicted) and builds now.
- **Nothing served was touched.** 461 platinum objects captured before and after the ad-hoc run:
  byte-identical.
- **The count `6/12` is stable and the FAILING SCOPE IS NOT.** Morning `['cottonwood','global']`,
  tonight `['inflection','global']`. **An identical number covering a moved defect** — do not read
  6/12 as "same as yesterday."
