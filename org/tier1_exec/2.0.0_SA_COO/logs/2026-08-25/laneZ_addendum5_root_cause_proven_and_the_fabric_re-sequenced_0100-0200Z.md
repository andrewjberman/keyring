# 2.0.0_SA_COO~Z — ADDENDUM 5: the root cause PROVEN, and the fabric re-sequenced off it (0100–0200Z)

**archetype:** MIXED · **secondary:** DIAGNOSE, VALIDATE, COORDINATE, SCRIBE
Continues `laneZ_addendum4_...md`. **~5 further commits (43 this session).** **Zero crons, whole session.**

---

## 1. ⛔ THE ROOT CAUSE — PROVEN BY EXECUTION, NOT ARGUED

`0.7.0_AE_CloudOps~Z` ran `build_tables()` (**verified PURE, zero I/O**) twice, identical `as_of`,
universe, netassets, characteristics, fund_daily, history. **One variable: the holdings frame.**

```
A: silver/holdings/2026-08-21.parquet  114 rows -> 2 full, 2 SHELL   <- REPRODUCES THE LIVE PORTAL
B: silver/holdings/2026-08-24.parquet  187 rows -> 4 FULL, 0 shell
                                                   DIVZ 29 · IDVZ 44 · PFDE 90 · PFOE 24
Nothing written. Nothing published.
```
⭐ **The CONTROL is what makes it proof** — frame A shows the apparatus can reproduce the failure,
and frame B fills anyway, **with tonight's code and tonight's characteristics.**

### The one line

```
lambda_function.py:1375   filename = run_date      (WHEN WE RAN)
lambda_function.py:1210   column   = data_as_of    (WHAT THE DATA IS)
etf_positioning_gold.py:794-795   gold OPENS BY FILENAME
```
**Nothing syncs them; nothing errors when they diverge — the reader just gets a different,
well-formed set.** 73 correctly-stamped TrueShares rows sit in a file gold never opens.
⭐ **`ETFS_INGEST.TO-7`'s stamp fix WORKED. The rows are in the wrong FILE.**

---

## 2. ▶ RE-SEQUENCED — AND THIS IS THE ENTRY A SUCCESSOR NEEDS MOST

⛔ **THE SALXX/FXFXX THREAD CANNOT MAKE DIVZ/IDVZ APPEAR.** `@0c03c359f2`, the STOP, the 164-row
census, the sentinel set, the vocabulary amendment — **all real work about how two rows RENDER once
they arrive. Six seats, two hours, on the thing that is not between Andrew and four filled books.**
**Not dropped. Behind `:1375`.**
⭐ **AE~Z's framing, kept: *"we have been fixing the rendering of rows that never arrive."***

---

## 3. ⭐ THE APPARENT CONFLICT WITH ANDREW'S RULING DISSOLVED — TONIGHT'S LESSON ONE LEVEL UP

DS~Z warned that keying the partition on `data_as_of` puts **two provider semantics in one key**
(Rule 24 same-grain). AE~Z's *"prior trading day of capture, identically for both providers"*
resolves it, and **it does not violate Andrew's 23:0xZ provenance ruling:**
```
PARTITION KEY    = an OPERATIONAL LOCATOR   uniform, derived, provider-agnostic   -> AE~Z's rule
PROVENANCE STAMP = a ROW FIELD              per-provider, the provider's assertion -> ANDREW's rule
```
>> **They conflict only if ONE FIELD CARRIES BOTH — which is exactly the `is_cash` defect DS~Z
>> diagnosed tonight, reappearing at the partition key instead of at a boolean.** ✅ **And it removes
>> DS~Z's stated blocker: the key stops depending on what the providers mean.**

---

## 4. MEASUREMENTS I CONTRIBUTED THIS STRETCH

- **`is_cash` occurs 0 times in the SERVED artifact** (positive controls `asset_class` 114,
  `sub_asset_class` 114; negative control 0). **It never leaves gold** — so DS~Z's "unmeasurable
  external consumer population" is EMPTY, and their `:671` choice rests on merit not caution.
  ⚠ **`alloc_cash` and `alloc_fixed_income` are ALSO 0 there** — so I could NOT confirm the
  aggregation defect reaches a client. **Gap stated, not resolved.**
- **`alloc_fixed_income` EXISTS at `:718`, hardcoded `0.0`** — contradicting the premise DS~Z partly
  stopped on. Not a schema addition; a hardcoded zero becoming a computed value.
- **The weekend "impossible future date" fits a rule 14/14 over two weekends** — but **AE~Z's
  mechanism (filepoint stamps the CURRENT BUSINESS DAY, forward-rolling) is better than my fitted
  curve**, and their line *"nothing that can be a future date is an as-of"* **closed a sovereign fork
  I had raised.** Withdrawn for filepoint; it survives for TrueShares, which does publish a page as-of.

---

## 5. ⛔ MY DEFECTS — AND ALL THREE WERE IN ONE VERIFICATION

| # | defect | caught by |
|---|---|---|
| 21 | **Reported 2-of-4 FAIL on a correct, RATIFIED commit** — `classify()` gained a third arg `cash_sentinel=True`; I called it with two, so FXFXX took the default and read as broken | re-reading the signature |
| 22 | **My four cells listed SALXX as MUST-PASS** when the ruling deferred that half — **the check would have FAILED A CORRECT BUILD** | the ruling's own text |
| 23 | **I pre-wrote a VERDICT into the measurement script** — *"the constants are DECLARED AND UNREFERENCED"* — **while the data printed directly above it showed `:573` referencing both** | reading my own output |

⛔ **AND THE ONE THAT MATTERS MOST: MY FOUR-CELL CHECK WOULD HAVE PASSED THE DEFECTIVE BUILD DS~Z
STOPPED.** It exercises `classify()`; the defect is in the three aggregations that consume it
(`:691` `cash_w`, `:692` `eq_w`, `:697` sector map, all keyed on the RAW flag). **Rule 22a's layer
rule — a unit read is not a behavioural read — and my check sat on the wrong layer.** Marked
INSUFFICIENT on the TO face; sufficient form named (read the emitted book) and **deliberately not
written**, since the aggregations are about to change.
> **Three structural corrections to one check in one night: a wrong VALUE, a wrong SIGNATURE, a wrong
> LAYER. Each was real and each was caught by a different seat.**

---

## 6. STATE FOR A SUCCESSOR

```
ACT 2      HELD on bbg/2026-08-24/ (absent). Release is a MEASUREMENT any seat can make -- see the
           TO-5 face. Do NOT fire while the prefix is absent.
L1         DO NOT RE-RUN BEFORE 04:00Z -- before local midnight it lands on the WRONG KEY and
           OVERWRITES the 170-row characteristics artifact (intact at b752f5c7).
@0c03c359f2  LOCAL, NOT DEPLOYED, STOPPED by its own author. Deployed package verified clean
           (Ultra Short Duration 0 · Fixed Income 0 · cash_sentinel 0, neg control fired).
THE FIX    partition key on a UNIFORM derived date, NOT run_date. DS~Z's plane. Live-data change
           over 73 partitions; interacts with the dedup on (date, key).
```
⭐ **And the night's through-line, `3.0.0_SA_CVO~Z`'s words: *a TRUE ADJACENT FACT SUBSTITUTED FOR THE
ONE ACTUALLY ASKED.* The remedy every time was the same and cheap: EXECUTE THE PREDICATE, DO NOT READ
AROUND IT.** *(And I did execute it, and still got it wrong three ways, because I executed the wrong
call. Executing is necessary, not sufficient — read the signature and the layer first.)*
