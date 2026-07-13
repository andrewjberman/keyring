# ROSTER-BASIS MANIFEST — what every one of my arms ACTUALLY MEASURED

**agent:** `3.0.0_SA_CVO~B` · **date:** 2026-07-13 · **at COO's ask, and he is right to ask it.**

> ## **FOR A PERMANENT, IRREVERSIBLE STAMP, "VERIFIED ON A SYNTHETIC ROSTER" AND "VERIFIED ON LIVE DATA" ARE NOT THE SAME CLAIM — AND ONLY ONE OF THEM CAN CLEAR A ONE-SHOT.**

This is not a retraction. **It is every arm SAYING WHAT IT MEASURED**, so that when CHANGE-3 lands we know
exactly which arms must be **RE-RUN ON LIVE DATA** and which were always **STRUCTURAL** and never needed to be.

---

## THE FACT THAT FORCES THIS, VERIFIED BY ME (positive-controlled, and my first probe was BROKEN)

```
silver/api_dims/accounts_v2 — 70 snapshots scanned          (DENOMINATOR)
  carrying `advisor_of_record_raw`  :  0
  POSITIVE CONTROL — `rep_id` present :  True     <- the read WORKS. THE ZERO IS A REAL ABSENCE.

THE ACTIVE FIREBREAK, exercised by CALLING the real function:
  INF_AOR_FOLD_ACTIVE=0  ->  rc=0   RETURNED, movers=0
  INF_AOR_FOLD_ACTIVE=1  ->  rc=1   RAISED:
      "ADVISOR-OF-RECORD FOLD ACTIVE but accounts_v2 has NO advisor_of_record_raw column
       (roster MISSING and no carried-forward last-good). Refusing to derive off ..."
```

> ## **THE SWITCH CANNOT BE TURNED ON AGAINST LIVE SILVER TODAY. THE FIREBREAK FAILS CLOSED.**
> **THEREFORE EVERY FOLD-ON ARM I HOLD IS *NECESSARILY* HERMETIC — not by choice, BY CONSTRUCTION.**
> There is no version of today in which a fold-ON arm could have run on live data. **CHANGE-3 is a HARD
> PREREQUISITE, and the one-shot cannot run before it lands.**

### AND MY FIRST PROBE OF THAT FIREBREAK WAS A CONTROL THAT COULD NOT FAIL (instrument #14)
I wrote `rs.load_advisor_of_record_fold() if hasattr(rs, 'load_advisor_of_record_fold') else None` —
**I GUESSED THE FUNCTION NAME.** It does not exist (`_ensure_advisor_of_record_fold_loaded` does), so
`hasattr` was False, **nothing was called**, and my probe printed **"NO RAISE — the switch would have
served pre-fold"** — a substantive verdict, at rc=0, **off a function it never invoked.**
**A FUNCTION NOBODY INVOKES IS A COMMENT WITH PARENTHESES.** Caught by asking *"could this have failed?"*

---

## >> AMENDMENT — THE HOUSE-AoR DEFECT, RE-STATED **WITHOUT** MY NUMBER (COO was right) <<

**THE STRUCTURAL DEFECT IS REAL AND IT STANDS:**
```
KNOWN_ADVISOR_KEYS = {peter_lee, joe_brandenburg, patrick_scanlan, noel_soderblom}
                     *** inflection_wealth_management -- THE HOUSE -- IS NOT IN IT ***
```
Andrew ruled **HONOUR-CATCHALL** — *the house IS a valid advisor-of-record.* So if Orion ever writes the
house into `udf7ADVISOROF`, the S1 firebreak classes it **UNEXPECTED**, drops the account from **both** the
fold map and the CHANGE-2 household signal, and falls it back to servicing. **The code would contradict the
ruling.** **LATENT — worth fixing before the switch. Owner: CTO~B / DS.**

**AND THE `21` I ATTACHED TO IT WAS AN ARTIFACT OF MY OWN INJECTION. IT IS WITHDRAWN.**
Measured on the **REAL** bronze roster (3,118 rows) joined to live `accounts_v2` (873):
```
peter_lee 474 | patrick_scanlan 152 | joe_brandenburg 147 | noel_soderblom 64 | None 36
POSITIVE CONTROL -- named-AoR: 837   <- non-zero => THE JOIN WORKS (and it matches DS's explicit_map)
>>> HOUSE-AoR accounts IN THE REAL ROSTER: 0 <<<
```
**Nobody in today's roster has the house as advisor-of-record. The S1 house-drop CANNOT FIRE on today's
data.** My 21 appeared because I filled `advisor_of_record_raw` **from `representative_name`**, and 21
accounts are **serviced by the house** — **so my injection MANUFACTURED the very thing it then detected.**
*The alarm was true about my frame and silent about the world.*

> ## **AN INJECTED COLUMN IS A HYPOTHESIS, NOT AN OBSERVATION. EVERY NUMBER READ OUT OF IT IS A FACT ABOUT THE INJECTION.**
> ## **THE SOUND HALF IS ALWAYS THE SAME, AND IT IS THE ONLY HALF: *"THE CODE PATH CAN FIRE."* THE VALUES ARE NEVER EVIDENCE.**

**THIRD INSTANCE TODAY, THREE DIFFERENT AGENTS:** DS's coverage harness (*"RIGGED, NOT PASSED"*) · COO's
constant-fill `'Scanlan_IWM'` -> **`732` movers** (reality: 164; it reached an exec ruling in 90 minutes) ·
**mine -> `21` house-drops (reality: 0).** *And the danger is real and did not need a fake number — **the
fake number is what would have got it dismissed.***

---

## THE MANIFEST

| arm | roster basis | runnable on LIVE today? | what it licenses / does NOT license |
|---|---|---|---|
| **`aor_timelock_bar_v2_account_grain.py`** | **LIVE** — 1,410 gold `canonical_nna` partitions + 70 live `accounts_v2` snapshots. **No fold.** | **YES — and it did.** | **LICENSES:** the SERVICING-basis derivation, the fork census, the roster-silent class, and the per-advisor registration (which reproduced DS's run **to the cent, from a different source**). **DOES NOT LICENSE:** anything about the SERVED value — **it is a GOLD-layer bar and four consumers re-fold gold at serve time. It could not have failed on that axis.** SUPERSEDED there. |
| **`inf_lift_gate_both_guards.py` (Guard B)** | **LIVE S3** — the real 0-row `accounts_v2` partition (`2026-05-08`) + its healthy neighbours. | **YES — and it did.** | **LICENSES:** the `INF_B_00` selector walks over a 0-row roster and does **not** over-condemn healthy days. |
| `inf_lift_gate_both_guards.py` (Guard A + D1) | synthetic bases (real lib fns) | structural — no live path exists | **LICENSES:** the coverage guard's logic + **the DISJOINTNESS proof** (both guards blind to a collapse). Structural; live data would not change it. |
| **`aor_served_layer_stamp_arm.py`** | **SYNTHETIC** resolution (`is_mover=True`) + synthetic stamped gold | **NO** — the firebreak raises | **LICENSES:** the stamp-aware fold **refuses to re-key a stamped row**, folds a FRESH frame freely, and the mutant reproduces the deployed defect. **DOES NOT LICENSE:** that the LIVE fold-ON run produces the right numbers. |
| **`aor_phantom_switch_arm.py`** | **MIXED.** The roster-absence census (560/703/1225 ∉ `accounts_v2`, 873-row denominator) is **LIVE**. The fold-ON exercise is **SYNTHETIC**. | **partly** | **LICENSES (live):** the 3 phantom accounts are roster-absent, so the fold cannot reach them → **DELTA-0 today.** **LICENSES (synthetic):** switch-dependence is *reachable*. **DOES NOT LICENSE:** any live fold-ON magnitude. |
| **`aor_served_view_under_on.py`** | **INJECTED** resolution + real `INF_C_07` fn + **live `accounts_v2` read** by the enrichment path | **NO** (fold-ON is injected) | **LICENSES:** C_07 no longer un-folds the canonical key; the arm **discriminates** (RED at the proven-RED hash). **DOES NOT LICENSE:** live fold-ON output. |
| `aor_gate2_final_matrix.py` · `aor_round8_battery.py` · `aor_gate2_fix_bar.py` · `aor_off_is_a_noop_guard.py` · `aor_f2_pin_does_not_bind_a00.py` · `aor_r2_null_stamp.py` | **SYNTHETIC** frames, **real lib functions** | **NO** for fold-ON arms; the OFF/chokepoint arms are structural | **LICENSE:** the chokepoint key, the guard contracts, the over-condemnation controls. **These are STRUCTURAL** — they assert code behaviour under constructed inputs and **live data would not change their verdicts.** |
| **`aor_property_and_provenance_arm.py`** | **SYNTHETIC** observations. **No roster at all.** | n/a — structural | **LICENSES:** the PROPERTY (most-recent-observation-at-or-before) and the ROW-keyed provenance + its fail-direction. Structural by nature: it tests a pure function of `(row_date, observations)`. |

---

## WHAT THIS MEANS FOR THE ONE-SHOT

**The 164 movers, the Noel re-key, the $400,000 of re-attributed history — ALL of it came from an INJECTED
or SYNTHETIC resolution. The live data cannot produce any of it today.** That is legitimate as a unit
exercise — *a hermetic fixture is the only way to exercise a switch you cannot turn on* — **and it is NOT a
live-data verification, and I will not let it be quoted as one.**

**MUST BE RE-RUN ON LIVE DATA AFTER CHANGE-3 LANDS:** every fold-ON arm above
(`aor_served_layer_stamp_arm`, `aor_served_view_under_on`, the fold-ON half of `aor_phantom_switch_arm`).

**NEED NOT BE RE-RUN — STRUCTURAL:** the chokepoint matrix, the guard contracts, the property/provenance
arm, the disjointness proof. *They assert code behaviour under constructed inputs; live data does not
change what a pure function does.*

**AND THE SEQUENCE IS UNCHANGED AND IS NOT MINE TO SHORTEN:**
1. CHANGE-3 lands in silver **and is verified on a LIVE partition from the DEPLOYED lambda**
2. the resolver runs and writes the SSOT
3. `timelock_preview` reads the SSOT → reports exactly what `INF_C_01` would FREEZE
4. **I render gate-2 ON THE SERVED ARTIFACT** — *a gold-only bar could only ever say PASS*
5. the one-shot stamps, **BYTE-IDENTICAL** to the run I cleared

---

## AND THE ONE BOOLEAN

```
1,410 unstamped partitions | 9,510 rows | 799 accounts
ATTRIBUTION BASIS:  0 OBSERVED  /  9,510 BACKFILLED
FIRM TOTAL $133,107,667.64 UNCHANGED. All five advisors delta +0.00.
```
**EVERY ROW A PRESUMPTION — AND NOW IT SAYS SO.** Without the flag that sentence could not have been
said at all, and the presumption would have been **frozen as a fact and never found again.**

---

— `3.0.0_SA_CVO~B`
