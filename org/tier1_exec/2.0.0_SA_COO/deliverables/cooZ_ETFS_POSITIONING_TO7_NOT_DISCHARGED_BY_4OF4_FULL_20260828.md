# FINDING: `ETFS_POSITIONING.TO-7` is **NOT** discharged by the 4/4-FULL measurement — the defect is a DESIGN property that is merely MASKED today

**Author:** `2.0.0_SA_COO~Z` · 2026-08-28 ~01:2xZ · measured at `HEAD f4f557eafd`
**Class:** finding, routed. **Not a ruling.**

---

## 1. WHY THIS EXISTS

`1.0.0_SA_CTO~Z` measured the live planes (msg 11371) and reported **4 books / 4 FULL / 0 SHELL**,
correctly retiring a three-day-stale "GOLD HAS NEVER RUN". On that basis Andrew's promote **condition
(i)** — *"until data pipeline is complete with full data structure for daily bloomberg data for all
ETFs"* — was read as **discharged on the DATA plane**. That reading is reasonable and I am not
disputing it.

⛔ **BUT THE SAME 4/4-FULL NUMBER READS AS DISCHARGING `ETFS_POSITIONING.TO-7`, AND IT DOES NOT.**

## 2. WHAT TO-7 ACTUALLY SAYS

`TO-7` is **ANDREW-DIRECT** (~23:5xZ, relayed by `1.0.0_SA_CTO~Z`, msg 5918), VERBATIM:

> *"It is not a problem if we are showing 08-21 data and not 08-24, the issue is that we have data for
> PFDE and PFOE being presented but we are not presenting DIVZ and IDVZ data ... We should be able to
> display data for all 4 ETFs every day"*

⭐ **NOTE WHAT HE TOOK OFF THE TABLE: *"It is not a problem if we are showing 08-21 data and not
08-24."* STALENESS IS NOT THE COMPLAINT. ABSENCE IS.**

## 3. THE DEFECT, MEASURED AT SOURCE THIS TURN

`data/etfs/scripts/gold/etf_positioning_gold.py` @ `f4f557eafd`:

```
:425   def resolve_as_of(now, frontier_override, ...)      -> ONE as_of for the whole run
:972   def build_tables(as_of: dt.date, universe: list[str], holdings, ...)
:1009      for code in universe:
:1013          rows = holdings[holdings["fund_ticker"] == code]
:1014          is_full = len(rows) > 0
```

⛔ **ONE `as_of` GOVERNS ALL FOUR FUNDS.** A fund whose data has not landed at that single date
produces `len(rows) == 0` → `is_full = False` → **it renders as a SHELL**, rather than being shown at
**its own most-recent** as-of.

>> **THAT IS PRECISELY THE STATE ANDREW REJECTED.** He said stale-but-present is fine. The design
converts *"this fund's data is a day behind"* into *"this fund has no data"* — **it trades the
condition he accepts for the condition he refuses.**

⚠ **METHOD NOTE, because I nearly recorded a false absence here.** My first probe for a per-fund
resolution (`per_fund|as_of_by|fund_as_of|...`) returned empty and printed `rc=0` — **but the `rc` was
`head`'s, not `grep`'s, because a pipe resets `$?`.** A hand-written pattern returning clean-empty is
the exact shape of a matcher written against a format never read. **The verdict above rests on READING
`:972`–`:1014`, not on that grep.**

## 4. WHY IT LOOKS DISCHARGED AND IS NOT

```
TODAY   all four funds happen to have rows at the same as_of  ->  4 FULL, 0 SHELL, symptom ABSENT
DESIGN  one as_of for all four funds                          ->  UNCHANGED at HEAD
```

⛔ **THE SYMPTOM IS ABSENT BECAUSE THE INPUTS HAPPEN TO AGREE TODAY, NOT BECAUSE THE DEFECT WAS
FIXED.** This is the *"an absence check cannot tell a fix from a refactor"* class in its sharpest form
— here it cannot even tell a fix from **a lucky Tuesday.** The next day any one issuer lags, a fund
drops to a shell again and Andrew's complaint returns verbatim.

⭐ **AND THE CONVERSE IS THE HONEST HALF:** a 4/4-FULL reading is **genuinely good evidence for
condition (i)** — the shells did upgrade and the pipeline does produce full books. **Condition (i) and
`TO-7` are different claims over the same number.** One asks *does the pipeline produce full data*;
the other asks *what happens when one fund lags*. **The measurement answers the first and is silent on
the second.**

## 5. STATE OF THE TO

```
issued        2026-08-25T00:00Z by 2.0.0_SA_COO~Z          basis: ANDREW-DIRECT
assignee      NONE -- the open-TO index shows it UNASSIGNED, age 3d
executor      DS (producer) + DE (serving surface) -- two lanes, sequenced
cells         ETFS-d-1 (projection producer) · ETFS-e-2 (artifact contract) · ETFS-f-1 (mode switch)
status tag    (none on the face)
```

⛔ **AN ANDREW-DIRECT TO HAS SAT UNASSIGNED FOR THREE DAYS AND APPEARS IN NO HANDOFF.** It is not
blocked on a decision — it is blocked on nobody having been given it.

## 6. WHAT I AM AND AM NOT CLAIMING

- **I am NOT claiming condition (i) is undischarged.** `1.0.0_SA_CTO~Z` scoped that reading to the
  DATA plane and it stands on its own evidence.
- **I am NOT claiming the pipeline is broken.** It is working; the four books are full.
- **I AM claiming that `TO-7` is undischarged, that its design defect is present at `HEAD`, and that
  the number most likely to be cited as closing it does not close it.**
- **I have not measured the DE half** (the serving surface / mode switch cells). This finding is about
  the producer.

## 7. ROUTED

- **`0.0.0_AB_MSTR~Z`** — `TO-7` needs a **DS-class** seat (producer half first; the DE half is
  sequenced behind it). ⚠ **Do not fold it into an existing DS instance: Rule 27, and every live DS
  lane is on another project** (`~L` ETFS_SATELLITES, `~Q` ETFS_INGEST).
- **`1.0.0_SA_CTO~Z`** — the remedy shape (per-fund as-of resolution vs. a stated fallback) is an
  architecture call, not the issuer's.
- **`3.0.0_SA_CVO~Z`** — surprise channel, class **OBSERVATION**, standing **INERT**: nothing breaks
  today, and it arms on the first day an issuer lags.

⛔ **THIS BEARS ON D4's COMPLETION SET.** D4 completes on `ETFS_POSITIONING` + `ETFS_INGEST`. An
Andrew-direct, unassigned, undischarged TO sits inside the first of those. **It does not change D4's
bar — that remains his smoke test — but it does change how close D4 is to meeting it.**
