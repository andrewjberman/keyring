# MDPF REMEDIATION PLAN — a functioning daily pipeline for all four scopes

**Andrew-direct 2026-08-10.** Author `1.0.0_SA_CTO`. **For `2.0.0_SA_COO` to decompose into TOs.**
**Evidence base:** `org/projects/MDPF_PIPELINE_TRUTH.json` @5ba751ed88 — 7 pipelines × 37 identical
fields, **253 MEASURED / 3 INFERRED / 3 UNMEASURED**, 24 defects, 5 of 9 holes closed.

**THE DELIVERABLE IS ANDREW'S, VERBATIM: *"a functioning daily pipeline for all scopes."*** Not a
finding count. A cycle that emits for 49financial, inflection, cottonwood and global, on schedule,
with correctly-labelled dates.

---

## 0 · THE ORDERING CONSTRAINT — read before sequencing anything

⛔ **SOME REPAIRS SILENCE A GUARD WITHOUT FIXING THE DEFECT IT GUARDS. ORDER IS CORRECTNESS, NOT
PREFERENCE.**

**D-19, measured:** move the floor later (or the pulls earlier) *on its own* and the frontier becomes
2026-08-07, **which eclipse has**. 08-06 stops being the frontier, both legs go `None`, they agree,
**and limb (v) stops firing.** Under the run-date ruling that cycle then **publishes one trading day
mislabelled instead of refusing.**

⇒ **THE LABEL OFFSET (W1) MUST LAND BEFORE OR WITH THE CADENCE FIX (W3). NEVER W3 ALONE.**

---

## 1 · WHERE EACH SCOPE IS BROKEN — traced path, then the break

### 49FINANCIAL
`SmartX → smartx/platform/bronze (13:36:31Z) → silver (13:40:47Z) → in-run gold → platinum`
`Schwab CRS → schwab/08242234/bronze (10:15:59Z) → silver (10:16:06Z, +7s)` ✅ healthiest leg in the estate
- **D-21** ingest ran **dirty** today (`DirtyRunError`, resolver 3278 ≠ living 3281); the retry returned clean by **skipping all 9,762 objects**
- **D-20** weekend partitions are **not T+1** — Sat and Sun both carry Thursday
- **D-5** its gate PASS is **limb-(v)-SKIPPED** (205 disagreements across 33 dates, printed and unchecked)
- **D-22** serves 08-07 on account-distribution beside 08-06 on two other surfaces

### INFLECTION
`Eclipse → opal-data-inf → mirror 22:30Z → eclipse/inflection/bronze (22:31:02Z) → silver (+5s)`
`Orion → opal-data-inf → mirror 14:15Z → orion/inflection/bronze (14:15:55Z) → silver (+10s)`
- **D-1** ⛔ **axis frontier imported from 49financial** — the violation
- **D-4 / D-10** **both legs served one trading day late.** Served Wednesday 08-05 = **$209,431,383.43**, which is **Tuesday 08-04's** custody — and the artifact declares `lag_vs_as_of_days: 0`
- **D-11** eclipse has **7 missing partitions of 57 post-launch (12.3%)**, not one
- **CURRENTLY REFUSING TO BUILD**

### COTTONWOOD ✅ the only compliant axis
`Black Diamond → opal-data-cot + blackdiamond/cottonwood/bronze (06:00:44Z) → silver (06:00:53Z, +9s) → gold`
- **D-3 REMEDIED** @dadd5d64f9 — point-in-time collision fix, deployed, COO-accepted
- **OPEN** custody leg shows a real **~24h silver-precedes-bronze inversion**, unexplained, began between data dates 08-04 and 08-05
- gold not written since 08-07 while the publisher re-serves 08-06

### GLOBAL
composes the three on the shared axis
- **D-18** dependency **exceeds** the permitted "most recent date": unions all three firms' full ~440-date axes, **pins** cottonwood into the headline, **rolls it forward** across every no-delivery date
- **all-zero aggregate emitted daily since 08-09 with `reconciliation: PASS`** — because `0 == 0+0+0`
- `_aggregate_aua` missing 08-07 (a **Friday**) and 08-08 entirely

---

## 2 · THE WORKSTREAMS

### W1 · LABEL CORRECTNESS — *served numbers are wrong today* · **OWNER `0.4.0_DS_ClientPlatform`** · **FIRST**
Apply the vendor label offset so a served date means the day it claims.
- **orion**: `orion_normalize_as_of = prior_trading_day` **exists, is SEALED (2026-07-02), and is never called** — zero occurrences in the 2,734-line gold builder
- **eclipse**: run-date key, T−1 offset, **four independent derivations** (producer source · weekday census · value tie-out · DS's TWR-factor ratio at 0.07bp vs 101bp for same-day)
- ⚠ **schwab and blackdiamond labels are ACCURATE — the normalizer is explicitly Orion-only. Do not apply an offset there.**
- **ACCEPTANCE (exercised, not config-read):** a served point labelled D contains D's close, tied out against the vendor artifact for D. **And `lag_vs_as_of_days` must stop asserting 0 when it isn't.**

### W2 · CROSS-FIRM UNLINK — **OWNER `0.4.0_DS_ClientPlatform`** · with or after W1
**The fix is two lines.** `:2682-2683` hands 49F's `dates` to `build_inflection_artifact`. `_model_leg_eclipse:889-895` **already self-derives** when passed `axis=None`, and cottonwood's `self_derived_axis` is the ratified pattern.

> **THE SEMANTIC RULING, because Andrew asked and it decides the shape:** the **CALENDAR** is legitimately shared — `canonical_trading_axis()` → `lib/_trading_day_calendar`, NYSE days, a library not a firm. **The FRONTIER is the violation** — read live from 49F's own vendor data, so 49F's *content* decides where inflection's series ends. **Each firm derives its OWN frontier from its OWN legs, then feeds the SAME canonical calendar.** Canonical shape kept; data link severed.

- **ACCEPTANCE:** a standalone `--firm inflection` build produces the same axis as the consolidated one, and **no read of `smartx/**` occurs in an inflection build** (exercised, not asserted).

### W3 · CADENCE — **OWNER `0.7.0_AE_CloudOps`** · ⛔ **GATED ON W1**
Current order is backwards: the floor reads at 13:00Z, four of its inputs land after.
```
06:00  cottonwood silver          ✅ before
10:16  schwab silver              ✅ before
13:00  ===== FLOOR READS =====
13:40:47  smartx silver  (AXIS SOURCE)   +40m
14:16:05  orion silver                   +1h16m
22:31:08  eclipse silver                 +9h31m
```
**THE BOTTLENECK IS THE MIRRORS, NOT THE VENDORS.** Eclipse data exists in `opal-data-inf` by ~14:48Z and waits **~7.5h** for the 22:30Z mirror.
**Proposed:** mirrors to ~13:45Z (after the pulls land) → eclipse/orion silver ~13:46Z; **floor to 14:00Z**; bridge and publisher shift behind it.
**The smartx leg needs no new trigger** — it is chained to the pull's `OnSuccess`, so **moving the pull moves the conversion** (G-1a).
- **ACCEPTANCE:** every consumed silver partition's C1 precedes the floor's read, measured on one scheduled cycle.

### W4 · NAMING — **OWNER `0.7.0_AE_CloudOps`** · ⛔ **DECISION AT ANDREW FIRST**
Andrew ordered `opal-assets-ingest-mirror-{firm}-{channel}-daily`. **It cannot be applied as specified: there is one mirror function with NO firm selector** (`event` never read in 469 deployed lines), and **both schedules have been observed writing the other firm's tree.**
**Two routes:** (a) name by cadence (`pass1`/`pass2`); (b) **add the firm selector, then the firm names become true.** ⇒ **RECOMMEND (b)** — it also lets firms be re-timed independently, which W3 wants anyway.

### W5 · INSTRUMENT INTEGRITY — *we cannot currently see failures* — **OWNER `0.7.0_AE_CloudOps`**
- **D-16** the mirror has **hard-failed every invocation for 14 days** (81 raises) on an ALIEN SURPLUS of 687 keys, because `cot-rebalancer-runner` writes into the mirror's own dst_prefix. **Signal destruction: a genuine new failure is indistinguishable from the standing one.** Narrow the assertion — **never disable the guard.**
- **D-5** the 49F limb-(v) skip
- **D-21/D-24** ⚠ **CORRECTED FRAMING — see §3.** The smartx leg is the **only** silver converter with no S3-object trigger.
- **global's zeroed-but-PASS aggregate** — an identity check that cannot fail on an empty artifact

### W6 · UPSTREAM — **NOT OURS** — route to the site-Z / INF fabric
**D-15** the 08-06 gap has **two unrelated causes**: orion's raw producer skipped a day while its parquet producer ran (**our Rule-17a guard correctly refused the parquet**); eclipse's producer missed the day outright. **D-11** the 12.3% eclipse gap rate.

### W7 · BACKFILL — **OWNER `0.2.0_DS_PortfolioAnalytics`** · **AFTER the pipeline is functional**
Andrew: *"after the remediation is complete and the pipeline is functional moving forward, we will want to explore a robust targeted solution for backfill — which is the point of that emitter."* **The emitter is strategic infrastructure, not a one-off for 08-05.** Ratification in §4.

---

## 3 · ⚠ CORRECTION TO MY OWN D-24 — Andrew's architectural read is right

I filed D-24 as *"the axis source has no working scheduled fallback,"* implying a NEVER#4 defect.
**Andrew: *"Aren't all silver mechanisms working this way? This methodology is what makes silver easily processed without a bunch of extra scheduling hassle."*** **He is right, and I measured it:**

**8 of 8 S3 notification configs on `opal-data-assets` are silver converters firing on bronze
object-creation.** Event-driven silver **is** the estate pattern, it is deliberate, and it is good —
conversion follows data arrival instead of a guessed clock. **A scheduled converter would be the
defect, not the fix.** D-24's framing is withdrawn.

**WHAT SURVIVES IS NARROWER AND SHARPER — and it is a DEVIATION FROM THE PATTERN, not the pattern:**

| leg | trigger predicate |
|---|---|
| eclipse · orion · schwab · blackdiamond · etf | **an OBJECT WAS CREATED** in bronze |
| **smartx** | **A PROCESS RETURNED CLEAN** (`OnSuccess` destination; **no S3 notification exists for smartx**) |

**Those are different predicates with different failure modes, and today the difference decided the
outcome:** the pull's first attempt **wrote 5,222,424 B of bronze at 13:36:31Z and then raised
`DirtyRunError`. Under the estate's normal S3-object pattern that landing would have triggered
conversion. Under `OnSuccess` it did not** — silver was produced only by the retry that returned clean
**by skipping all 9,762 objects.**

⇒ **THE REMEDY IS TO BRING SMARTX ONTO THE ESTATE PATTERN, not to add a schedule anywhere.**
*(Note `cot-rebalancer-runner` carries an `OnSuccess` to blackdiamond **in addition to** its S3
notification — belt and braces. SmartX has only the belt.)*
*(All six silver converters do carry `OnFailure → opal-assets-silver-dlq`, so a failure path exists.)*

---

## 4 · DS's RECONSTRUCTION PREFIX — RATIFIED, with two conditions

`s3://opal-data-assets/eclipse/inflection/reconstructed/vintage=2026-08-05/reconstruction.json`

**RATIFIED.** It meets every property I ruled: distinct (occupies the medallion slot, **is** none of
them), self-naming, **opt-in by construction** (0 existing read paths glob it — a measured claim), and
grammar-conformant (new segment, not a new root, so Rule 17b is untouched). `vintage=` rather than
`date=` is a deliberate and correct choice — **no consumer globbing `date=` can pick it up by
accident.**

**CONDITION 1 — the labels live in the ARTIFACT BODY, not only in the gate.** `point_class:
"reconstructed"`, method version, tie-out error, and the fwd/bwd residual must travel **with the data**.
A consumer that reads the object without reading the gate must still learn it is derived.

**CONDITION 2 — DO NOT FREEZE THE GATE THRESHOLDS ON THE DAY YOU CALIBRATE.** The proposal freezes
from the calibrated flow-adjusted known-day run and then measures against it — **that is fitting the
test to the data**, the class Andrew ruled on 2026-08-06 (*"a fix only your test set can see is a tune,
not a fix"*). **Calibrate on one known day, validate on a different one.**

**UNCHANGED:** the 136bp `opal_long_term_conservative` cell must come under the bar or **the gate fails
and that is a finding, not a threshold to relax** — DS's own words, and correct. Nothing serves from
this without a separate ruling.

---

## 5 · COMPLETION BAR — unchanged, and it is not negotiable later

**Not when a cause is named.** When the **mechanism is established at source**, the remedy lands, **the
SCHEDULED cycle emits** (ad-hoc is QA, never production evidence), and served
`meta.generated_at` / `as_of_last` **advance — never the S3 mtime**, which is rewritten daily and looks
fresh while carrying stale content.

**PER-SCOPE, the bar is: 12/12 A4 objects built on one unattended scheduled cycle, with each firm's
served dates carrying the vintage they claim.**

## 6 · WHAT IS STILL OPEN

`G-3a` orion-silver normalisation · `G-3c` **Schwab date semantics — the only custody feed with no
measured vintage, anchored solely on a docstring in another vendor's module** · `G-2` bronze
provenance on remaining feeds · `G-4` roll-forward policy per firm · the cottonwood-custody ~24h
inversion. **None blocks W1–W3.**
