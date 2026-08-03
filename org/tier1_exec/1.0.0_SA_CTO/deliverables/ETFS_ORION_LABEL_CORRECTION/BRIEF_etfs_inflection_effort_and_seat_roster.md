# BRIEF — the ETFS tracking effort, the inflection work, and who worked what

**For:** Andrew · **From:** `1.0.0_SA_CTO` · **2026-08-03**
**Window:** 2026-08-01 ~1330Z → 2026-08-03 ~1315Z (continuous)
**Subject:** ETFS_AVGCAP — the partner-rebate basis.

---

## 1. WHERE WE ARE, IN ONE PARAGRAPH

The Aug-1 month-end email delivered on time with three partner CSVs. Everything downstream of it
turned out to be wrong in a way nothing was reporting. Chasing "a rollback that didn't work" led to
a broken CDN invalidation, then to eight missing inflection days, then to a producer with no
schedule, then to holdings values repeating across trading days — and finally to the real mechanism:
**Orion returns the prior day's SETTLED close and stamps it with the RUN date.** The portal/gold
chain corrects for that. **The rebate chain does not.** Inflection's July basis is understated
**$424,062.91 (0.891%)**, and the deeper problem is that inflection sits on a T-1 basis while
49financial and cottonwood sit on T — **inside the same monthly file that decides what each partner
is paid.**

## 2. WHAT IS FIXED AND VERIFIED

| thread | state | evidence |
|---|---|---|
| Emergency-rollback CDN invalidation | **CLOSED** | invalidated `/api/public/*`, dead since the 2026-02-25 rename (api/public=0 behaviors, api/general=6). Fixed + a fail-loud coverage gate. Proved itself twice, second time on a real repair |
| Portal serving the 7/27 vintage | **CLOSED** | etag `a8cb00d8…` / 19221 B; Andrew visually confirmed; 3 independent oracles |
| inflection producer had NO schedule | **CLOSED** | only trigger was an event-pattern on the INF sentinel. Now `cron(0 15)`, event dependency deleted, structurally identical to its two siblings |
| inflection trading-day gaps | **CLOSED** | was 14/22 July. **Now zero gaps across the entire production history** |
| 49F + cottonwood → `opal-data-assets` | **CLOSED** | cottonwood 07-20 corrected off a stale roll-forward: 48,391,202.69 → **50,292,778.58** |
| `lib/trading_calendar.py` had 4 unguarded copies | **CLOSED** | parity CI landed; caught BEFORE drift |
| Corrected figures emailed | **DELIVERED** | SES Send=1 / Delivery=1, 3 attachments |

## 3. THE INFLECTION FINDING — the actual mechanism

Orion returns the latest **settled** close (prior trading day); `asOfDate` **echoes the run date**.
Sealed in the estate 2026-07-02 at `data/inf/scripts/silver/_orion_vendor_asof.py`.

**Refinement we established:** the docstring blames a *pre-open* pull. The puller now fires
**09:37 ET, post-open** — moved by **your own directive `b2f61bed83` (07-01)** *"to avoid pulling
before Orion settles prior-day close."* So the mechanism is **the pull deliberately targets the
prior settled close**, not pre-open timing. Same conclusion, correct premise.

**ORACLE TEST — run, with its control:**
```
published 07-18 AND 07-20  -> true 07-17   identical values  => the repeat is CORRECT
published 07-25/26/27      -> true 07-24   identical         => CORRECT
CONTROL   07-14 / 07-16    -> 07-13 / 07-15  DIFFERENT       => instrument discriminates
```

**THE FIGURES** (22 trading-day observations per basis, no gaps):

| ticker | published avg | true-settled avg | delta | % |
|---|---|---|---|---|
| DIVZ | 17,213,181.28 | 17,372,480.95 | +159,299.67 | 0.925% |
| IDVZ | 13,303,299.68 | 13,425,779.03 | +122,479.35 | 0.921% |
| PFDE | 10,855,741.97 | 10,949,981.15 | +94,239.18 | 0.868% |
| PFOE | 6,236,133.97 | 6,284,178.68 | +48,044.71 | 0.770% |
| **TOTAL** | **47,608,356.91** | **48,032,419.82** | **+424,062.91** | **0.891%** |

July's file actually spans **06-30 → 07-30** — one June day in, true 07-31 out.
⚠ **BASIS, not payment.** Simple-mean assumption; the real AVGCAP aggregation is unconfirmed.
⚠ **MEASUREMENT, not a restatement.** Nothing restated, no partner notified.

## 4. THE THREE OPEN DECISIONS (yours)

1. **Build the normalization?** `ETFS_ORION_LABEL_NORMALIZATION.md` @`8f0e32a642` — specced, not started.
2. **Restate any partner figure?** Requires confirming AVGCAP aggregation first.
3. **Fix the cross-partner date basis?** inflection T-1 vs 49F/cottonwood T. **I would do this one
   regardless of 1 and 2** — it makes the partners non-comparable in the paying artifact.

Plus two unowned residuals: **true 07-13 / true 07-15 identical to the cent** (normalization does not
explain it; your "raw fact" ruling binds), and the **`dev@test.com` attribution gap** — any direct
invoker of the data-refresh handler can self-assert an arbitrary identity string on a live mutation.

## 5. SEAT ROSTER — who worked what

| serial / lane | thread | outcome |
|---|---|---|
| **`0.7.0_AE_CloudOps`** (base) | Aug-1 ETFS month-end fire watch | DELIVERED. Cleared two instrument traps (`SendQuota` unchanged across a real send; empty log grep) that would each have raised a **false red-alert on a pipeline that had already paid three partners** |
| **`0.7.0_AE_CloudOps~C`** | rollback CDN invalidation fix; 7/27 portal repair | CLOSED. AC1-AC8. Its AC1 test displaced the served vintage — caught, ruled, repaired. Found a way to stamp a real actor identity instead of `dev@test.com` |
| **`0.7.0_AE_CloudOps~E`** | inflection scheduled floor + catch-up; 49F/cottonwood repoint; vendored-copy parity CI; correction email | CLOSED (×4). **Falsified three of my specs before implementing them** |
| **`0.7.0_AE_CloudOps~A`** | named Aug-1 fire owner | NOT REGISTERED at fire time; base took the watch |
| **`0.0.0_AB_MSTR`** | spawned `~C` + `~E`; integration/push; owns the INF-gold-canon cluster | Owned a 50-min spawn delay explicitly |
| **`1.0.0_SA_CTO`** (me) | specs, arch-gates, validation, the oracle | 3 specs falsified; 1 detector broken; the oracle test |
| `2.0.0_SA_COO` / `2.1.0_SA_COO` | ESTATE / CORE fabrics | not on this thread |
| `3.0.0_SA_CVO`, `4.0.0_SA_CRO` | verification / research | not on this thread |

## 6. THE PART WORTH KEEPING

**Every defect that mattered was caught by someone verifying a premise they were handed, not by the
person who wrote it.**

- `~E` refused to implement my layer table and **falsified it** — my hash used snake_case drop names
  against a camelCase schema, so the date columns I "excluded" were inside it. **It failed toward
  "clean" twice.**
- `~E` found AC2 and AC7 could not both hold, and that my cited 92.3% skipped an existing partition.
- `~E` refused to delete a correct S3 object to manufacture a test gap, and refused to override an
  owned-paths gate.
- `~C` owned an unchecked premise that changed live client-facing data, then read state first on the repair.
- Base `~AE` refused two instruments that read "no send" on a send that had happened.

**And the reverse: my own first probe of the calendar defect PASSED and proved nothing** — my
environment had the dependency the Lambdas lack. I had to force the failing path to see it.

**The one thing that went wrong went wrong because a premise was not checked before acting on
production.** Everything else held because someone stopped.
