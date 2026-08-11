# BRIEF — THE `ending_mv` VALUATION-BASIS QUESTION: A LONGITUDINAL INVESTIGATION

**Commissioned:** Andrew-direct, 2026-08-11 ~0840Z ("investigate key accounts under Patrick over several
weeks/months and use that dynamic to come to a sharper conclusion").
**Author:** `2.0.0_SA_COO` · **Status:** brief for hand-off · **Assignee:** TBD by Andrew
**Deliverable form:** a schema-valid `PROOF_OF_SPEC` instance (canonized ~0821Z @bddd6554ce) —
`org/standards/PROOF_OF_SPEC.schema.json`, validated by `python .tools/proof-of-spec-check.py <instance>`.

---

## 1 · THE QUESTION

**When a client-facing surface displays "non-fee-earning assets," what does `ending_mv` actually represent,
and is it a legitimate basis for that display?**

This is NOT a request for a recommendation on which basis to serve — **that ruling is Andrew's.** This
investigation exists to make that ruling decidable on measured mechanism instead of inference.

## 2 · WHY IT MATTERS

Patrick's advisor surface shows **$695,956.41** non-fee AUA (current-AUA basis). The reviewed figure is
**$127,852.75** (`ending_mv` basis). A 5.4× disagreement on a client-facing number.

**And the exposure is larger than one advisor.** The ratified firm-level derivation sums `ending_mv`:
- `fee_earning_aua = SUM(ending_mv WHERE is_fee_earning)` → **$137.2M**
- `non_fee_earning_aua` (classified form) → **$3.6M**
- residual gap surfaced as `unreconciled_aua` → **$68.3M**

**If `ending_mv` is systematically absent or stale, those firm figures are understated on the same
mechanism and the $68.3M is largely an artifact rather than a reconciliation gap.** That decomposition is
currently marked **INFERRED, not certified.**

⚠ **What is NOT at stake: the ratified fix itself.** Andrew ratified replacing a subtract-and-clamp residual
with a classified sum. **That form is correct on any basis** (CTO adjudication). This investigation decides
what *values* feed it, not whether the mechanism was right. **Nothing here justifies unwinding anything.**

## 3 · WHAT IS ALREADY MEASURED — DO NOT REDO

From `0.4.0_DS_ClientPlatform`, who replicated the served `book.json` computation exactly (reproducing the
served 144/15 counts and the fee sum to the cent against billing snapshot 2026-08-11):

| fact | value |
|---|---|
| Patrick's non-fee accounts, **all with billing rows** | **12 of 12** |
| Non-fee accounts at `ending_mv = 0.00` | **9 of 12** — while holding **$568,103.66** of current assets |
| Non-fee accounts with nonzero `ending_mv` | **3** — and they **match current AUA to the cent** |
| **Fee-earning** accounts at `ending_mv = 0.00` | **63 of 144** — accounts that WERE billed |
| Zero-rows across his whole billing set | **72 of 156** |
| No-billing-match accounts (the conflation class) | **3, holding $0.00** — worth nothing today |

**Source mechanism, read from `data/inf/scripts/silver/build_billing_dim.py`:**
- `ending_mv` ← Orion Billing report column **`"Activity: Ending Market Value"`**
- rows carry **`Billing Period Start` / `Billing Period End`** → it is a **period figure, not a daily mark**
- `is_fee_earning` is a **documented workaround for Orion's broken "Included In Billing" flag**:
  `(fee_schedule_name != '0 Fee Schedule Names') AND (fee_amount > 0)` (PATH_DISCOVERY §1.6)
- the builder's own docstring specifies the mixed-basis derivation:
  `non_fee_earning_aua = total_aua − fee_earning_aua` — **a live total minus a period-end fee base**
- guards exist: `if df["ending_mv"].sum() == 0` and `apply_aua_guard(df, "ending_mv", "billing")`
- `fee_assessed_on_zero_balance` is an **already-named state** at `D_02:1629`

## 4 · WHAT IS NOT KNOWN

1. **Inflection's actual billing cadence** — quarterly? monthly? per-account-varying? This sets the
   staleness ceiling and nobody has measured it.
2. **What the 72 zeros MEAN** — unclosed period · genuinely zero balance · new account · parse/ingest loss.
   **Four different meanings, four different remedies.**
3. **Whether populated values stay flat or track AUA** — i.e. whether this is staleness or absence.
4. **Whether `is_fee_earning` is stable per account over time**, given it rides a workaround.

## 5 · THE FIVE HYPOTHESES AND THEIR DISCRIMINATING SIGNATURES

⚡ **This is the core of the brief. Each hypothesis predicts a DIFFERENT longitudinal signature, so the time
series discriminates between them. Do not go looking for evidence of one — run the series and see which
signature appears.**

| # | hypothesis | predicted longitudinal signature | implied remedy |
|---|---|---|---|
| **H1** | **UNCLOSED-PERIOD ABSENCE** — zero until a period closes | zeros for a run of days, then a **STEP** to nonzero on a period boundary; **boundaries ALIGNED across accounts**; value at population ≈ current AUA that day | the display must not subtract an unclosed period |
| **H2** | **STALE PERIOD-END CARRY** — populates at close, then sits | nonzero but **FLAT across many days**, **progressively diverging** from current AUA, **resetting** at the next boundary | the display compares two different moments |
| **H3** | **GENUINELY ZERO BALANCE** | zero across **ALL** dates **AND** current AUA ≈ 0 / account closed or transferred | the number is already right |
| **H4** | **OUR-SIDE CLASSIFICATION OR PARSE DEFECT** | `is_fee_earning` **flips** across days with no underlying change; or the vendor CSV carries a value our parse drops (`parse_dollar` on `ending_mv_str`) | fix the workaround / the parse |
| **H5** | **PURE MIXED-BASIS ARITHMETIC** — no absence at all | `ending_mv` **well-populated**, and the gap tracks the **GROWTH of current AUA since the last close** | the specified derivation is the defect |

**They are not mutually exclusive** — the honest outcome may be "H1 for 40 accounts, H3 for 12, H5 residual."
**Report the partition, with counts.**

## 6 · THE DATA — IT IS ALL AT REST. NO EGRESS REQUIRED

```
s3://opal-data-inf/silver/api_dims/billing/snapshot_date=YYYY-MM-DD/data.parquet
```
- ✅ **1,597 snapshot partitions**, earliest **2020-01-31**, **current through 2026-08-11 (today)**
- **102 partitions dated 2026**
- bronze raw: `data/inf/manual_api/pulls/{YYYYMMDD}_billing.csv`; puller
  `data/inf/manual_api/orion_billing_dim.py`

⛔ **THE DENOMINATOR TRAP, AND IT WILL BITE:** **102 partitions in 2026 against ~223 elapsed days.** The
series is **NOT complete-daily.** Anyone computing "days since populated" or "consecutive zero-days" on an
assumed-daily grid will produce confident nonsense. ** CHARACTERIZE THE ACTUAL PARTITION CADENCE FIRST AND
PRINT ITS DENOMINATOR BESIDE EVERY DERIVED INTERVAL. **

**No vendor call is needed for the core work.** If a genuine Orion-side question survives the at-rest read
(e.g. what Orion's own period-close semantics are), that is a **separate, per-use egress ask to Andrew** —
do not assume the standing lifts cover it, and note the session-scoped blanket lift **does not survive
session end**.

## 7 · THE METHOD (Andrew's, made concrete)

1. **Pick the cohort from the measured sets, not at random:**
   - the **9** non-fee accounts at `ending_mv = 0` holding **$568,103.66**
   - a sample of the **63** zero-valued **fee-earning** accounts (the `fee_assessed_on_zero_balance` cohort)
   - ⚡ **the 3 nonzero non-fee accounts that match current AUA to the cent — THESE ARE THE POSITIVE
     CONTROL.** They show what "working" looks like. **An investigation without them cannot tell a broken
     account from a broken instrument.**
2. **Pull the per-account time series** across a window long enough to contain **at least two candidate
   period boundaries** (≥ 6 months, given a possible quarterly cadence). Fields: `ending_mv`,
   `period_start`, `period_end`, `fee_amount`, `fee_schedule_name`, `is_fee_earning`, `snapshot_date`.
3. **Join current AUA per account per date** from the positions/AUA side, so divergence is measurable rather
   than inferred.
4. **Plot / tabulate per account:** `ending_mv` vs current AUA over time, with `period_start`/`period_end`
   marked. **The step-vs-flat-vs-absent shape is the answer.**
5. **Test cross-account boundary alignment** — do period boundaries coincide? That alone separates H1 from H3.
6. **Report the cohort partition** with counts per hypothesis.

## 8 · WHAT WOULD MAKE THE CONCLUSION SHARP

- The **measured billing cadence**, stated with its denominator.
- A **per-account classification** into H1–H5 with counts, not a single verdict.
- For H1/H2: **the measured lag distribution** — "as of any given day, `ending_mv` reflects a close a median
  of N days old, p95 M days."
- ⚡ **A restatement of the $68.3M firm-level gap decomposed by hypothesis** — that converts my
  currently-INFERRED decomposition into a measured one, and it is the single most valuable output.
- **A plain-English answer to: "when a human reads 'non-fee-earning assets,' which number answers that
  question?"** — as *input to Andrew's ruling*, explicitly not the ruling.

## 9 · TRAPS AND CONTROLS

- ⛔ **RUN THE POSITIVE CONTROL** (the 3 matching accounts). A finding that cannot distinguish a real defect
  from a measurement artifact is not a finding.
- ⛔ **PRINT DENOMINATORS.** Partition coverage, accounts examined / accounts in cohort, dates with data /
  dates in window. An absence verdict without its denominator is indistinguishable from a failed retrieval.
- ⛔ **`ending_mv` IS PARSED** from `ending_mv_str` via `parse_dollar`. **Check whether any zeros are
  PARSE losses rather than vendor zeros** — read the bronze CSV for a sample. This is H4 and it is cheap to
  exclude.
- ⛔ **DO NOT ASSUME DAILY PARTITIONS** (§6).
- ⛔ **NAME the mechanism, do not infer it.** "Probably a quarterly close" is not a finding; the period
  boundary read off `period_start`/`period_end` is.
- ⛔ **The trading-calendar rule applies** — weekends and holidays are not staleness.

## 10 · OUT OF SCOPE

- **Do NOT rule the basis.** That is Andrew's, and CTO's exec read is already with him.
- **Do NOT re-cut D_02 or D_04.** A basis re-cut is a change to a ratified form — Andrew's and CTO's.
- **Do NOT touch serving.** No republish, no field changes. This is a read.
- **Do NOT fold this into the CPR-6 window.** CPR-6 is a class closure worth $0.00 today and its scoping is
  already on the record.

## 11 · POINTERS

- Mechanism source: `data/inf/scripts/silver/build_billing_dim.py` · puller
  `data/inf/manual_api/orion_billing_dim.py` · `PATH_DISCOVERY.md` §1.6 (the broken vendor flag)
- Named state: `D_02:1629` `fee_assessed_on_zero_balance`
- DS's measurement + the inversion: `05_PATRICK_696K_MECHANISM.md` (amended @9a7229495d), CPR-6 @c55e0d6fcc
- CTO's adjudication (form stands, basis separable): the seventh single-homing face —
  **one producer AND one basis per quantity**
- My register: `CANONICAL_PATTERN_STAFFING_AND_ROUTING_20260811.md` §4ad
