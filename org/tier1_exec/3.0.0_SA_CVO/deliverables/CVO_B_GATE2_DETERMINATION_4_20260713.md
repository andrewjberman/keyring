# GATE-2 DETERMINATION #4 -- **CLEARED** at `59d70b95e`

**agent:** `3.0.0_SA_CVO~B` (Andrew-direct dedicated validation lane, LD-0277) · **date:** 2026-07-13
**determination:** **GATE-2 CLEARED.** Both withholds from determination #3 are **DISCHARGED**, verified at the
committed hash by three independent instruments, and **the over-condemnation controls stayed green.**
**supersedes:** determination #3 (`d3826ceb3`, WITHHELD at `59c24b46e`).

> # >> CLEARING GATE-2 DOES **NOT** AUTHORIZE GO-LIVE. NOTHING IN THIS FILE DOES. <<
> Still required and **NOT MINE**: **CHANGE-2** - the **never-widen co-sign** (NEVER#2) - the **INF hold-lift**
> - **Andrew's GO** - and the **V4 served-verify on the first nightly**, which remains an **EXPLICIT GAP**.
> Nothing served. Switch OFF. SERVE-HELD.

---

## 1. BOTH WITHHOLDS DISCHARGED -- against the bar I PRE-REGISTERED before the fixes existed

The bar (`aor_gate2_fix_bar.py` @ `294965d79`) was written **before** DS's fixes, precisely so they could not be
graded on a moving target. **It is now 5/5.**

| bar | at `59c24b46e` | at `59d70b95e` |
|---|---|---|
| **B1** null-stamped rows carrying FOLDED attribution -> must RAISE | RED (returned + served) | **PASS -- RAISES** |
| **B2** [OVER-CONDEMNATION] healthy OFF resolution -> must RETURN | PASS | **PASS (stayed green)** |
| **B3** [OVER-CONDEMNATION] healthy ACTIVE resolution -> must RETURN | PASS | **PASS (stayed green)** |
| **B4** an absent account's loss is DISCLOSED, never SILENT | RED | **PASS** |
| **B5** [OVER-CONDEMNATION] healthy run -> guard must not fire | PASS | **PASS (stayed green)** |

**The three over-condemnation controls staying green is the load-bearing half of this clearance.** A
fail-closed fix that fires on a legitimate run is the disease it was sent to cure, and that hazard was not
hypothetical -- the "wipe the whole firm's `advisor_key` under OFF" defect existed **only in a ruling** and died
because someone exercised it before building it.

**R2 is confirmed independently of me:** base CVO's own falsifier (`aor_r2_null_stamp.py`) now RAISES on both
attacks (N1, N2) while its non-placebo control C1 still RETURNS. **Her arm, her fixture, my re-run.**

Full battery at `59d70b95e`: **10 live arms, 9 GREEN, 1 expected RED** (the phantom -- see §3).
Reproducible in one command: `python aor_gate2_runner.py`.

---

## 2. >> AND I HAVE TO CORRECT A SCOPE ERROR *I* INTRODUCED, OR THIS CLEARANCE IS GOALPOST-MOVING <<

**Determination #3 listed V4 as one of three gate-2 withholds. That was a CATEGORY ERROR, and it was mine.**

**V4 verifies the FIRST NIGHTLY *AFTER* the switch flips.** It is a **POST-cutover delivery check**. It is
structurally impossible to run before go-live -- you cannot verify the served output of a switch that has not
been turned on. **It therefore cannot be a precondition of a PRE-cutover gate**, and my own determination #2 had
said so correctly (*"still required and NOT mine: ... V4 served-verify on the first nightly"*). I then contradicted
myself in #3 and made it a withhold.

**I am naming this rather than quietly reclassifying it, because quietly reclassifying a withhold in order to
clear is exactly how a gate stops meaning anything.** MSTR's own instruction is the check on me here, and it
agrees: *"Gate-2 can still advance on everything upstream of that step. Sequence it so the served-verify is the
LAST thing outstanding, and say plainly that it is parked on an infrastructure control, not on your analysis."*

**SO, PRECISELY:**
- **V4 = `WITHHELD -- NOT RUN`. An EXPLICIT GAP. NEVER a PASS. NO fixture green in my battery closes it.**
- It is parked on an **infrastructure control**, not on my analysis: the INF gold chain **dies at step zero**
  (`sync_scripts()` FATAL, basename collision -- I exercised the predicate: `build_assets_dim.py` is the **sole**
  in-scope collision, a **single keystone**, no second layer).
- **AoR go-live is serialized behind the hold-lift, and the lift is gated on the coverage assertion -- not on my
  gate.** **The pressure to "lift the hold just so CVO can run her V4" is the single most likely way this control
  gets defeated. I will not accept that trade, and I am recording in advance that I will refuse it.**

---

## 3. THE PHANTOM: RED on the served spine, and **NOT** a gate-2 blocker -- exercised, not assumed

The served `advisor_nna_canonical.json` carries **5 advisor keys, one of which is not an advisor**:
`inflection_unmapped_rep`, **$52,604.80** -- and it is **a real advisor's money** (Patrick Scanlan, short since
2026-07-09).

**Why it does not block THIS gate, by exercise:** `INF_C_01:463` floors to the phantom and `:474` runs
`apply_resolution_fold` **on those same rows** -- so the switch and the phantom touch the same rows in sequence,
and nobody had asked whether the switch moves the money. The fold re-keys **iff the account is a MOVER** -> a
mover must be in the resolution -> the resolution is built from `accounts_v2`. **Grounded LIVE** (roster
`snapshot_date=2026-07-12`, **873 rows**; positive control: account 42 IS found): accounts **560/703/1225 are ALL
ROSTER-ABSENT** -> the fold **cannot reach them** -> **DELTA-0 across the switch.**

> **BUT SWITCH-DEPENDENCE IS REACHABLE, AND THE GREEN IS DATA-DEPENDENT, NOT STRUCTURAL.**
> "Roster-absent" (`accounts_v2`) and "null `rep_id` on the txn row" (`transactions`) are facts about **TWO
> DIFFERENT SOURCES, and NOTHING COUPLES THEM.** A roster-**PRESENT** account with a null txn `rep_id` is floored
> to the phantom **and is eligible to be a mover** -- exercised: the fold re-keys it and **moves money out of the
> phantom bucket at go-live.** Same shape as "dormant because coverage is 849/849": **armed, not fixed.**

Its fix is **blocked** by the INF hold (no `canonical_nna` re-derivation). **Separate chapter, deliberately kept
separate** (COO-directed): *two defects filed as one get fixed as one, and the second one survives.*

**And the reconciliation identity cannot detect this class in either direction:** `sum(advisors) == firm_total`
ties to **0.00 BECAUSE the phantom is counted as an advisor** (green in the defective state), **and it stays
green through the DELETION mode** (both sides lose the money at the same instant). Ruling (iii)'s
`sum(advisors) + unattributed == firm_total` inherits the blindness: it catches SUPPRESSION and is **blind to
DELETION**. **The deletion mode needs a coverage/denominator assertion -- which is the F7 detector that was
deleted. F7 and the deletion mode are the same hole.**

---

## 4. RESIDUAL, NAMED HONESTLY -- disclosed, not a blocker

The F2 fix makes the loss **VISIBLE** (`INF_09:188` firm total is unfiltered; `:193` per-advisor is filtered, so
`sum(advisors) < firm_total` and the residual is reconcilable -- **verified at source**). **But the residual is
VISIBLE, not ASSERTED:** nothing raises on `sum(advisors) + unattributed != firm_total`. **A WARN IN A LOG IS NOT
A GATE.**

**Not a blocker because:** the absent set is empty by construction today (the pin + source-digest assertion mean
the resolver and every consumer read the **same `accounts_v2` bytes**, so the account sets are identical),
`INF_A_00:302` **RAISES** and runs **first** in the chain, and the incoherent shape (non-null `advisor_key` +
null `rep_bucket`) is **refused unconditionally**. It is defence-in-depth for the day that invariant breaks.

---

## 5. THE FIX I ASKED FOR WAS WORSE THAN THE FIX I GOT -- and my bar was grading OBEDIENCE

My B4 demanded *"all three full-attach call sites must RAISE on absent."* **That was MY REMEDY, not the
PROPERTY.** DS chose a better shape: floor `rep_bucket` to an explicit `'unresolved'` (so the exclusion is a
**DECISION**, not a dtype-dependent artifact of `NaN != 'individual'`), **exclude** the row from per-advisor
rollups (**never fabricate attribution**), **leave** it in the firm total (so the residual is visible), **alarm**
by account, and **raise unconditionally** on the incoherent shape. **A raise at C_07 would abort the chain where
a disclosure suffices.**

> **A BAR THAT ENCODES A REMEDY GRADES THE FIXER ON OBEDIENCE, NOT ON CORRECTNESS.** Rewritten to assert the
> property: *an absent account's loss must never be SILENT.*

**And my F2 arm ASSERTED THE DEFECT.** It demanded `rep_bucket` stay `<NA>` -- the very thing that silently drops
the row -- so a **good fix broke my test** (`FAIL: rep_bucket = 'unresolved'`), and the tempting repair was to
revert the code. **CTO~B warned me about this exact class ONE MESSAGE before it happened**, having just found the
mirror-image error in his own gate-1 arm A (it demanded the absent row **survive** into per-advisor NNA -- which
demands **fabricated attribution**, the phantom sin in reverse; DS refused it and was right).

> **THREE OF US WROTE A TEST THAT DEFENDED THE BUG IT WAS WRITTEN TO CATCH, IN ONE DAY.** It is not coincidence.
> **It is what happens when you write the assertion from the SHAPE OF THE DEFECT instead of from the PROPERTY YOU
> WANT.** Write it from the property.

---

-- `3.0.0_SA_CVO~B`
