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

**Post-nightly gate (all four must hold) — now a DELIVERY gate, since the value limb passed:**
1. `window_bounds` present on both routes and in agreement.
2. `1Y.start == data_as_of - 365d`.
3. Per-advisor NNA converges **0/N** canonical vs leaderboard across **every** window (not just 1Y).
4. `entry_count > 0` for every served window.

**Per-window discrimination must be reported, never a blanket green (limb 2a).** Measured at
`data_as_of = 2026-07-07` (wall-clock `2026-07-09`):
- **[A] STRUCTURALLY undiscriminating — MTD / QTD / YTD / MAX.** The mis-anchored and correct windows are
  *identical* (both anchors share month/quarter/year). Zero power, and always will be **except at a period
  roll**. Remedy: the suite must carry a period-roll as-of — re-running at a normal as-of can never bite.
  This is exactly DS's latent period-roll defect, and it is invisible to any number of ordinary runs.
- **[B] CONTINGENTLY undiscriminating — 3Y.** Windows differ (`2023-07-10` vs `2023-07-08`) but the delta
  band is a Sat+Sun carrying **$0.00**. Coincides by calendar luck. Remedy: re-measure every run.
- **[C] DISCRIMINATING — 1Y.** Windows differ; the band carries **$3,516,778.16**; pre-fix code yields
  65/158 divergent on this exact data.

Only **[C]** licenses a green. Conflating *"the check passed"* with *"the check could have failed"* is the
defect this contract exists to prevent.

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

---

## Item 4 — the `ratified_at` field in this YAML is a STALE PROXY on all five rows

Folded in here at COO's direction (2026-07-09, `/drive` cycle 5) rather than opened as a separate thread:
*the YAML is a claim about the table; the table is the truth.*

Every row in `contracts/graph_contracts.yaml` reads `PENDING-*-SIGNOFF`:

| row | YAML `ratified_at` | LIVE table (AE in-VPC `contract_engine` read, COO 150336Z) |
|---|---|---|
| `benchmark` | `PENDING-ANDREW-SIGNOFF` | **RATIFIED**, Andrew-signed, real 16-char hash, since 06-16 |
| `peers` | `PENDING-CTO-COO-SIGNOFF` | **RATIFIED**, CTO+COO |
| `aum` | `PENDING-CTO-COO-SIGNOFF` | **RATIFIED**, CTO+COO |
| `headline` | `PENDING-ANDREW-SIGNOFF` | genuinely unsigned |
| `advisor_intelligence` | `PENDING-ANDREW-SIGNOFF` | genuinely unsigned |

**A reader of this file concludes 0/5 ratified. The live table says 3/5.** The loader stamps `ratified_at`
in the LIVE table on in-VPC write and never writes back to the YAML, so this field can only ever be stale —
it is structurally incapable of being correct. It is not a status; it is a default string.

**Consequence, and it already fired:** prior-CVO bound TO-3's status to this field on 2026-07-09, concluded
the rows were unauthored, and re-authored all five rows that already existed (deliverable removed in
`d39ae51d9` — including an `aum` row with the wrong `canonical_writer`). One row-set nearly overwrote a
correct, ratified one because a proxy was read as the property.

**Remediation (no Andrew signature required — mechanical):**
1. A blocking header comment now sits at the top of the YAML directing readers to the live table. *(landed)*
2. Recommend AE make `--load-contracts` **write `ratified_at` back** into the YAML after an in-VPC write, or
   else **remove the field from the YAML entirely** so it cannot be misread. A field that can only be stale
   should not exist in the authoring source. **Routing note: this is an AE/CTO call, not a CVO edit** — the
   loader is not my lane.
3. Until then: **ground ratification on `globgrph.graph_contracts`, never on this file.**

---

---

## !! DISPOSITION CHANGE 2026-07-09 ~23:35Z — SOVEREIGN OUT-OF-SCOPE. Item 3's gate can never clear. !!

**Andrew, 2026-07-09T22:33Z:** *"i do not want to deal with 49 right now, their data and setup is ambiguous and
a fucking mess, it is not our problem and not something that we should pursue unless i explicitly ask for it."*

CTO `231239Z` ruled **`data/black_diamond/` IS 49 Financial** — one firm, three names (`opal-data-bd`,
`bd-49f-*`, `data/black_diamond/`) — and placed `data/black_diamond/`, `schwab/`, `opal-data-bd`,
`opal-data-schwab` **OUT OF SCOPE: no writes, pushes, deploys, ad-hoc runs, ledger closes, or VERIFIES.**
COO `231641Z` retracted the competing carve-out. Both execs agree.

**Item 3's delivery-limb acceptance is a read of `s3://opal-data-bd/platinum/firm/leaderboard.json`. That read
is prohibited. There is no 10:30Z verify. There will not be one until Andrew explicitly asks.**

**Disposition: `WITHHELD — VERIFY NOT RUN, sovereign out-of-scope`. Recorded as an EXPLICIT GAP. NEVER a PASS.**

- **APPLIED:** `2af63847d` (D_00c anchor + `window_bounds`) and `3ea2bdbf9` (D_04 propagation), sha256-verified
  `repo == s3://opal-data-bd/code/gold/` on 07-09, **before** the ruling.
- **EXERCISED-CLEAN:** the value limb (1Y 0/158, bounds match, `entry_count>0` on all nine, tripwire silent).
- **UNVERIFIED AND UNVERIFIABLE:** the delivery limb. *A prohibition stops agents; it does not stop crons* — so
  the legs are applied with **no assurance, by sovereign design.**

**This is not "no divergence found."** A negative from a *prohibited* sweep is indistinguishable from a
negative from a complete one. **Could-not-verify is a finding, never a clean bill** (Rule 22a — the
committed-not-applied failure mode). Do not "just check."

**The only two honest exits:** (a) Andrew explicitly reopens 49F/bd and the served re-read runs; or (b) the row
is ratified on the value limb alone with the delivery gap recorded verbatim in `ratified_by`. **I do not
recommend (b) and I will not sign it.**

Surfaced by `0.4.0_DS_ClientPlatform~B`, who is `BLOCKED-SOVEREIGN`, wrote zero files under any 49F path, and
routed it *"because you are holding a gate on a condition that cannot be satisfied, and nobody else was going to
tell you."* Correct, and the right call.

**Items 1 and 2 are unaffected** — `benchmark` and `headline` are `model_portfolios` / `opal-data-portal-v2`,
not bd. They remain authored and ready. **Item 4 (the `ratified_at` stale proxy) is unaffected.**

---

## Sequencing

0. **Item 3 is HELD INDEFINITELY, as an explicit gap.** It does not gate items 1, 2, 4.
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
  **Item 3 VALUE limb EXERCISED 2026-07-09 ~21:0xZ** (DS 0.4.0, real deployed-identical `D_00c`, real S3
  inputs, read-only): 1Y **0/158 divergent** vs served canonical (was 65/158); `window_bounds` match canonical
  on all five; `entry_count > 0` on all nine windows; tripwire silent. CVO independently source-verified the
  no-write property (`_save_json` is called from `main():1360` **only**, never from
  `build_employee_leaderboard():798`, and is the sole write call in `D_00c` — `put_object` is *unreachable*
  from that path, a structural guarantee, not a `dry_run` flag) and the runner's pull-at-runtime property
  (`run-gold-layer.sh:88-90`, `gold_dispatch.sh:526` — `aws s3 sync`, nothing baked).
  **Correction on the record:** this grounding block previously read `exercised: (deferred by design)`. That
  was false — the value limb was **un-attempted**, not un-exercisable. Triggering the production gold run is
  forbidden; running the fixed code locally read-only never was. **A cert record that calls a limb
  un-exercisable when it was merely un-attempted is the same defect this package exists to catch.**
  **The DELIVERY limb remains genuinely un-exercised, by design, until the nightly.**
- **source:** `lambda_function.py:445-455`, `:475-483` (trailing 30/91 calendar days, ruling cited in-code);
  `bmkaud-ws3-methodology-walkthrough-20260601.md:34,:67,:68`; directive `631d8d0d9`;
  `gold_utils.py:102-103` (`_today()` = wall clock); `D_00c:817` (`latest_date`), `:830`
  (`anchor = latest_date`), `:1247-1253` (tripwire), `:1257` (`window_bounds`).

— 3.0.0_SA_CVO
