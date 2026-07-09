# NFRA_GCONTR — consolidated SEV1 sign-off package (ONE Andrew signature)

**Author:** 3.0.0_SA_CVO · **Date:** 2026-07-09 · **Routes via:** 2.0.0_SA_COO (sovereign queue #1)
**Status:** `AUTHORED — HELD.` Two of the three items are ready now; item 3 is gated on a served-artifact
verification that cannot happen before the 2026-07-10 nightly. **Do not put this in front of Andrew until
item 3 clears.** He signs once, against a package that is true when he signs it.

Per PRD §9 tiering: SEV1 rows (`benchmark`, `headline`, `advisor_intelligence`) require **Andrew** in
`ratified_by`. SEV2 (`peers`, `aum`) = CTO+COO and is **not** in this package — COO is opening the `peers`
period_defs correction with CTO separately. Do not fold it in.

---

## Why this package exists

GCONTR was about to be presented for SEV1 sign-off with a row that **contradicts Andrew's own ruling**.
Exercising the CVO-owned value-check (`ec33fe59d`) surfaced it. COO pulled GCONTR from the sovereign queue.
This package is the correction, consolidated so there is exactly one sovereign ask.

---

## Item 1 — `benchmark-model-portfolios` : `period_defs` 1M / 1Q correction

**Row status:** LIVE + RATIFIED (real hash, since 2026-06-16). This is an **edit to an already-signed
SEV1 row**, so it requires Andrew's re-sign. The live table currently carries the wrong text.

**The defect.** `contracts/graph_contracts.yaml` declares:

```yaml
"1M":  "trailing-1-calendar-month -> as-of"
"1Q":  "trailing-3-calendar-months -> as-of"
```

The **methodology-of-record** is trailing **30** / **91** CALENDAR DAYS:
- `lambda_function.py:445-455` — `start_date = end_date - timedelta(days=30)`, with the in-code note
  *"METHODOLOGY-OF-RECORD: Andrew ruling 2026-06-01 (BMKAUD WS-3, directive 631d8d0d9) — KEEP the
  trailing-30-calendar-day window... Do NOT change to a calendar-month window without a new Andrew ruling."*
- `lambda_function.py:475-483` — the identical note for 1Q / 91 days.
- `docs/briefs/bmkaud-ws3-methodology-walkthrough-20260601.md:67` enumerated the choice as
  **(a)** trailing-30/91 calendar days, **(b)** trailing 1/3 calendar months, **(c)** last-complete-period.
  `:34` warned the first two *"coincide now but will drift on 31-day months / month-end dates."*
  `:68` names `relativedelta(months=1/3)` as the (b) implementation.
- Directive `631d8d0d9` (CTO, recording the ruling): *"1M/1Q = KEEP trailing-30/91d (methodology-of-record)."*

**Andrew ruled (a). The contract row declares (b).**

**Impact.** No served number is wrong today. The risk is forward: the contract is the **enforced
invariant**, so an implementer honoring it would swap in `relativedelta` and silently break the ratified
methodology. The row's `1Y` line already carries this day-count precision (`:59`, *"365 not 252"*, via
`feca94a1f`); 1M/1Q never received the same treatment. This is a CVO authoring error (prior-me, 06-16/17)
and is owned as such.

**Proposed text (apply ONLY on Andrew's signature):**

```yaml
"1M":  "trailing-30-CALENDAR-days -> as-of"   # Andrew ruling 2026-06-01 (631d8d0d9). NOT 1 calendar month, NOT last-complete-calendar-month (the SmartX violation).
"1Q":  "trailing-91-CALENDAR-days -> as-of"   # Andrew ruling 2026-06-01 (631d8d0d9). NOT 3 calendar months, NOT last-complete-calendar-quarter.
```

The live YAML has been left **unchanged** and annotated with a `!!! DRIFT` block pointing here. Applying
the correction requires: Andrew signature → AE `--load-contracts` with overwrite → manual WRITE_VERIFY
(real 16-char `ratified_at` hash, `period_defs` count unchanged).

**Carry CTO's standing guard:** this is ADVISORY-v1 (WARN) only. A WARN→hard-flip re-gates through CTO.

---

## Item 2 — `model_portfolios.headline` : the outstanding unsigned SEV1 row

Authored 06-16/17, `ratified_at: PENDING-ANDREW-SIGNOFF`. No content change proposed. Included here only so
the sovereign ask is a single signature rather than three.

---

## Item 3 — `advisor-intelligence-nna` : value_check refresh — **HELD, do not sign yet**

**Row status:** authored, `PENDING-ANDREW-SIGNOFF`. Not yet ratified, so the CVO may author it freely.
The `value_check` text has been **refreshed in place** this session (see below); the **ratification** is
hard-withheld.

**Why held.** DS (`0.4.0_DS_ClientPlatform`) root-caused and fixed the 1Y cross-route divergence and then
withheld their own work, correctly: **committed + deployed is not served.** The served
`platinum/firm/leaderboard.json` is still the pre-fix artifact, so the F-1 limb *correctly reads RED right
now.* No ad-hoc gold run was triggered (CLAUDE.md NEVER rule). A cert taken today off source/deploy evidence
is exactly the comp-tool-DESIRED-alone failure Rule 22a hard-withholds on for SEV1 — the bd-49f ModeMarker
class (committed fix, never exercised, silent three days).

**CVO position: the withhold is ENDORSED and binding on me.** I will not ratify this row until I have
re-read the SERVED artifact after the 2026-07-10 nightly (D_00c ~09:53Z / D_04 ~10:18Z).

**Post-nightly gate (all four must hold):**
1. `window_bounds` present on both routes and in agreement.
2. `1Y.start == data_as_of - 365d`.
3. Per-advisor NNA converges **0/N** canonical vs leaderboard across **every** window (not just 1Y).
4. `entry_count > 0` for every served window.

### What changed in the value_check text (already applied — row is unratified)

- **Dropped** the resolved 2026-06-17 QTD example (Travis, canonical vs leaderboard). It is fixed.
- **Removed** any "1Y-specific bug" framing. Per DS: it is a **rolling-window ANCHOR** defect. `3Y` was
  *equally* mis-anchored and converged only by **calendar luck** — its dropped band (2023-07-08 Sat,
  07-09 Sun) carried **$0.00** of firm flow while 1Y's (2025-07-07 Mon, 07-08 Tue) carried
  **$3,516,778.16**. Asserting "1Y-specific" would bank a false invariant that goes green for the wrong
  reason on the next lag change.
- **Limb (1) hardened, and its limit stated:** a published `window_bounds` block is *the producer's own
  claim about the window it used*. It is **not evidence the window was used.** Limb (1) is declarative and
  cannot carry the contract alone; it must bind with the semantic limb (2). (Same distinction as the
  benchmark value-check's producer-fidelity vs contract-fidelity gap.)
- **Limb (2) now requires DISCRIMINATION:** the assertion must be shown capable of failing at this
  `data_as_of` — i.e. the mis-anchored window would produce a *different* number on this data. If it would
  not, report `UNDISCRIMINATING`, never green. This is the generalization of both today's findings (mine:
  the benchmark check is blind at a 30-day month-end; DS's: 3Y green by calendar accident).
- **New limb (6) WINDOW LIVENESS:** `entry_count > 0` for every served window on every route. DS's latent
  catch: a wall-clock-anchored QTD/YTD/MTD start lands *after* the data end at a period roll, `D_00c:394`
  returns empty, and the leaderboard would have served **zero advisors for QTD on the first days of every
  quarter** — silently, because limbs (1)-(5) all pass vacuously on an empty window. Doctrine banked: *an
  assertion over a set is vacuously true on the empty set; always pair a conformance limb with a
  non-emptiness limb.*

---

## Sequencing

1. **Now:** items 1 + 2 authored and ready. Item 3's text is authored; its ratification is held.
2. **2026-07-10, post-nightly:** DS runs the served verification and reports. CVO re-reads the SERVED
   artifact against the four-point gate above.
3. **On a clean served read:** COO presents this package to Andrew as sovereign-queue #1. **One signature.**
4. **On signature:** AE `--load-contracts` (overwrite for `benchmark`), manual WRITE_VERIFY, real
   `ratified_at` hashes stamped on all three rows. GCONTR closes 5/5 + the value limb.

**Not in this package:** `peers` (SEV2, identical 1M/1Q drift, CTO+COO ratifiable — COO owns);
the dangling `benchmarks/LATEST.json` pointer (routed to the yang_pkl owner); the benchmark value-limb's
month-end blind spot (fixed and shipped in `ec33fe59d`, exit-4 `CLEAN-BUT-UNDISCRIMINATING`).

## grounding

- **desired:** `pipescript --resource yang-model-portfolio-benchmarks`; `comp-kuzu` canonical
  (`graph_contracts` last-write ~551.8h ≈ 2026-06-16, corroborating COO's "rows already-landed 06-16").
- **applied:** `git branch --contains 2af63847d` → CLOUD; `s3api head-object` on served benchmark
  (`2026-07-01T16:31:34Z`, `data_as_of 2026-06-30`).
- **exercised:** 10 runs of `contracts/value_check_benchmark_period_defs.py` (pre- and post-fix), exit codes
  0/0/2/0 then 4/4/0/2/3/4 — the month-end blind spot that surfaced item 1.
- **source:** `lambda_function.py:445-455`, `:475-483` (trailing 30/91 calendar days, ruling cited in-code);
  `bmkaud-ws3-methodology-walkthrough-20260601.md:34,:67,:68`; directive `631d8d0d9`;
  `gold_utils.py:102-103` (`_today()` = wall clock); `D_00c:817` (`latest_date`), `:830`
  (`anchor = latest_date`), `:1247-1253` (tripwire), `:1257` (`window_bounds`).

— 3.0.0_SA_CVO
