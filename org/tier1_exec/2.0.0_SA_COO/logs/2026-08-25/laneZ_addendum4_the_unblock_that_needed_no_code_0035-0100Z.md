# 2.0.0_SA_COO~Z — ADDENDUM 4: the unblock that needed no code (0035–0100Z)

**archetype:** COORDINATE
**secondary_archetypes:** DIAGNOSE, VALIDATE, SCRIBE

Continues `laneZ_addendum3_...md` @86aa8eefe0-chain. **2 further commits (~34 this session).**
**Zero crons, whole session. `/drive` never armed.**

---

## 1. ⛔ FOR A FRESH SEAT — THE ONLY THINGS THAT MATTER

| clock | state | owner |
|---|---|---|
| **~04:00Z** | local midnight. After it, the EXISTING code writes `bbg/2026-08-24/` correctly | anyone awake |
| **~11:00Z** | scheduled L1 pull — **already correct at that hour, no code change needed** | whoever is alive |
| **13:00Z** | `ETFS-TO5-AC7`, first scheduled producer fire | whoever is alive |

⛔ **ACT 2 IS HELD BY ME AND HAS NOT BEEN RELEASED.** Condition: **`bbg/2026-08-24/` exists.**
Verified ABSENT repeatedly through 01:00Z. **A producer run before then steps back to 08-21 for a
FOURTH time and adds a fourth ad-hoc decoy to a prefix already carrying three at one as-of.**
**Nobody fires on inference — the release is a measured prefix check, not a judgement.**

---

## 2. ⭐ THE DECISION: NO CODE CHANGE TONIGHT

Andrew's item (`DIVZ`/`IDVZ` absent from the page) was blocked on one missing input,
`bbg/2026-08-24/`. `0.0.0_AB_MSTR~Z` ran the L1 pull; it landed under **`bbg/2026-08-21/`** because
`pd.Timestamp.today()` is **LOCAL** and locally it was still Monday evening.

**A fix was ruled, then AE~Z and MSTR~Z found two independent traps in it within four minutes, and
MSTR~Z declined as named owner. I verified the load-bearing claim before sequencing:**

```
UTC       LOCAL (EDT)       BDay(-1)     writes
00:49Z    Mon 08-24 20:49   2026-08-21   WRONG   <- the actual run
03:59Z    Mon 08-24 23:59   2026-08-21   WRONG   <- control
04:01Z    Tue 08-25 00:01   2026-08-24   CORRECT
11:00Z    Tue 08-25 07:00   2026-08-24   CORRECT <- the scheduled run
```
>> **THE EXISTING CODE IS ALREADY CORRECT AT 04:00Z AND 11:00Z. The bug manifests ONLY before local
>> midnight.** The two WRONG rows are the controls — the computation discriminates.
**So the trade was: risk the one run that delivers Andrew's data, to buy ~3 hours over a gate that
needs no code. Declined.**

---

## 3. THREE FINDINGS THAT OUTLIVE TONIGHT

⛔ **The as-of tripwire has never been able to fire.** `:67` and `:68` compute `asof` and `expected`
from the **identical expression**; the refusal branch needs a midnight race between consecutive
lines. **The variable NAMES imply two independent derivations where the code has one** — `expected`
reads as an oracle and is a copy. **Its deadness had been masking a wrong `expected` nobody had to
think about.** *(AE~Z's catch; banked as `a-guard-that-compares-an-expression-to-itself`.)*
⭐ **CTO~Z's amended shape is right and survives the deferral: `asof` from the PARTITION (data),
`expected` from `lib/trading_calendar` on UTC (calendar) — two independent sources.**

⛔ **The overwritten manifest is unrecoverable.** `opal-data-etfs` has **no versioning** (checked —
the versioning I verified earlier was on `opal-data-portal-v2`, a **different bucket**; carrying that
property across would have produced a false "recoverable"). The 11:02Z **scheduled**-run record is
gone, including MSTR~Z's own Z-S5 criterion. **A `run_class` discriminator labels the survivor; it
does not restore the casualty.**

✅ **A5 WORKS.** `characteristics.parquet` 109 → **170** rows, `BBSEY`/`AMX`/`CPA`/`BNPQY` all
token-matched, `AAPL` positive control. **DS~Z's "full-looking books with blank analytics" branch —
the one outcome worse than tonight's honest shells — CANNOT HAPPEN.**
⚠ **But that discharges the pre-check's CAPABILITY half only** (*can Bloomberg resolve these?*), on
an **ad-hoc artifact at as-of 08-21**. The **INSTANCE** half (*did TODAY's scheduled run emit them at
today's as-of?*) is unanswered. **On the TO-5 face @2103a58512, because "discharged early" would
otherwise read as "skip it."**

---

## 4. ⛔ MY DEFECT THIS STRETCH — ONE, AND IT IS THE ROLE'S

**I ran the product check at 01:17Z, reported "three gold manifests, all `as_of 2026-08-21`", and
filed it as an AC7 evidence caveat.** CTO~Z read the same three numbers and saw that **every run was
at the one as-of where DIVZ/IDVZ cannot exist — i.e. that Andrew's top priority was unstarted.**
>> **I HAD THE MEASUREMENT AND MISSED ITS MEANING. I asked the question my thread was about, not the
>> question the project was about.**
⛔ **And I was the largest single contributor to the drift that made it necessary** — four
consecutive broadcasts on ack forensics and memory hygiene while `bbg/2026-08-24/` did not exist.
**Sequencing attention is the COO deliverable, so a drift I generate is a failure of the role.**
⭐ **The generalisable half: nobody was idle and nobody measured anything wrong. Each seat kept
measuring accurately INSIDE THE FRAME IT WAS ALREADY IN.** A frame does not announce itself, and
being rigorous inside it feels exactly like being rigorous.

---

## 5. Next

1. **[anyone, after 04:00Z]** re-run the L1 pull → writes `bbg/2026-08-24/`, a **NEW key, no
   overwrite**. Then tell me / a successor COO to release act 2.
2. **[whoever is alive 11:00Z]** the pre-check — **run it**; only its cheap failure mode is excluded.
   ⚠ **Match `BBSEY`/`AMX` on the ticker TOKEN** — `security` carries `AAPL US Equity` and a bare
   compare reads CLEAN ABSENT for every row.
3. **[whoever is alive 13:00Z]** `ETFS-TO5-AC7`. **An ad-hoc invoke can never discharge it.**
4. **[CTO~Z]** re-assign or defer the L1 as-of fix. **DS~Z is the named candidate** — they already
   solved the trading-day-partition trap once, in gold.
5. **[DS~Z / DE~Z]** `POS-TO7-AC7` (gold reads `data_as_of` from the rows) and TO-7 AC4 stand.
