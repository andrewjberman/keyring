# CVO CERT — `STI-inv-6`, THE SUMMATION ARM: **HOLDS**

**Author:** `3.0.0_SA_CVO` · **Rendered:** 2026-08-26 ~21:50Z
**Pre-registered shape:** msg 73680 (written before the arm was run, so it could not be tuned).
**Ruled IN and owned at this seat** per 73680, on `2.0.0_SA_COO`'s 73658 s.4 routing;
`0.4.0_DS_ClientPlatform~V` correctly declined to self-assign a CVO-class control.

---

## THE INVARIANT

> **`STI-inv-6` — FIRM + ACCOUNT-SET SEPARATION: 49F only; `08242234` rows are EVIDENCE, NEVER A
> SUBSTITUTE for `08335338`.**
> Oracle, two clauses: *(1)* no `08242234` key in any landed path or census input — **PATH arm, done
> previously**; *(2)* **"the two account sets never summed"** — **COMPUTATION arm, this cert.**

⚠ **`08335338` = ADVI Advisor Intelligence · `08242234` = MDPF Model Portfolios.** Distinct books.

---

## VERDICT: **HOLDS — AND ON A STRUCTURAL MECHANISM, NOT A GUARD**

>> **THE TWO ACCOUNT SETS ARE NEVER SUMMED BECAUSE ONE OF THEM IS NEVER PULLED INTO THE PRODUCER.**
`08335338` is not fetched by the daily emitter — that is **G2, sovereign-gated** (`lambda_function.py:36-37`).
The cohort that would require both (**cohort-8**) lands **`incomplete`** rather than substituting
`08242234` or summing across. **That is the invariant's own words — evidence, never a substitute —
holding by construction rather than by a check that could be bypassed.** <<

## THE INSTRUMENT, AND ITS CONTROLS

| | |
|---|---|
| **DENOMINATOR** | **34** `.py` files carry BOTH ids (63 carry `08242234`, 73 carry `08335338`) — the only files where a summation is even expressible |
| **DETECTOR** | both ids within a 3-line window **AND** a combining operator (`+`, `sum(`, `.union(`, `\|=`, `extend`, `update`, `append`, `concat`, `add`) |
| **HITS** | **6 of 34** |
| **POSITIVE CONTROL** | constructed summation `total = a + b` over the two ids → **FIRES** |
| **NEGATIVE CONTROL** | separated use, no arithmetic → **SILENT** |

**The instrument discriminates.** An arm that cannot fire is not a control — the estate's own lesson,
three seats, this evening.

### THE SIX, ADJUDICATED

| site | disposition |
|---|---|
| `test_silver_registry_identity_and_routing.py:30` | string concatenation building a **path**, not a set sum |
| `test_schwab_trn_nna_gold.py:44` | asserts `master_for('model_portfolios')=='08242234'` and `('advisor_intelligence')=='08335338'` — **an assertion OF SEPARATION; the opposite of a violation** |
| `opal-assets-daily-emitter:33` | **comment** describing cohort-8's incomplete state |
| `opal-assets-silver-schwab:3` | **docstring**, "TWO scope lanes" — describes separation |
| `test_incomplete_reachability.py:237` | the one live candidate — resolved below |
| `g4_build_ownership_rows_extension.py:48` | **draft deliverable**, comment, not production |

### THE LIVE CANDIDATE, RESOLVED AT SOURCE

`test_incomplete_reachability.py:237` feeds **both** masters into `emitter.build_total_rows`. That
function's contract (`lambda_function.py:1032`):
> *"The reconciled per-basis totals. **NO cross-basis total — by design.**"*

It sums only rows flagged `additive`, and the code states what that flag means:
> *"A total is NOT itself additive — summing it with its own contributors would double the book.
> `additive` marks the **disjoint INGREDIENTS**."*

**No sum reaches across the two books.**

## ⛔ THE CLAUSE I PRE-REGISTERED AND HONOURED

> *"A CLEAN RECONCILIATION IS NOT EVIDENCE. Do not accept 'the totals tie' as passing this arm — it
> is the failure's own signature."* (73680, and `~Q`'s near-miss: an unpadded-vs-zero-padded join with
> **zero true overlap** produced a perfect MECE census at 2,998+4,148=7,146 **of the wrong firm**.)

**This arm does NOT pass because anything reconciled.** It passes because **the arithmetic cannot
reach across** — one side is absent from the producer — **and the code says so in its own contract.**

## WHAT MAKES THIS STRONGER THAN "NO VIOLATION FOUND"

**1. The gap is pinned by a test written to FAIL when the world improves.**
`test_the_production_clearing_path_is_DEAD` — *"PINS A KNOWN GAP. This test asserts a DEFECT, on
purpose, so it cannot hide."* `08335338` is observable only via a marker mdpf emits **0 of 427**
times. *"WHEN THIS TEST GOES RED, THAT IS GOOD NEWS."*

**2. The code names the exact future act that would break the invariant.**
`lambda_function.py:116-124` — *"THE HAZARD IS THE OBVIOUS REPAIR: the next agent sees a
permanently-stuck `incomplete`, assumes the flag is broken, and hard-wires it to `fresh` —
**LAUNDERING THE EXACT UNDERCOUNT THE STATE EXISTS TO DISCLOSE.**"*
**The control is guarded against its own most likely repair.** That is rarer than the control.

## ⛔ WHAT THIS CERT DOES NOT COVER

- **NOT the PATH arm** — done previously (`0 of 931` / `0 of 7,921` / `0 of 7,283`, positive control
  17,378 keys). This cert is the **second** clause only.
- **NOT a claim that the invariant survives G2.** When `08335338` data actually flows, **the state
  will NOT clear on its own** and the summation question must be re-asked against a producer that
  pulls both. **This cert is true of the producer as it stands today, and its expiry is G2 landing.**
- **NOT a lint.** No mechanical carrier is added by this cert; if the path segment is later ruled not
  a scope boundary, `STI-inv-6`'s PATH arm loses its carrier and **this arm becomes the only one**.
