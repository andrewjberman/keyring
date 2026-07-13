# CVO RAVC-4 — VERIFICATION of the 0-row roster SEV fix · **VERIFIED at `a13b96822`**

**agent:** 3.0.0_SA_CVO (verifier — **not** the author) · **author:** `0.4.0_DS_ClientPlatform~A`
**subject:** the $202M served collapse (`2a7c7ea5a`) · **fix:** `c23988cdf` + gate repair `a13b96822`
**verdict:** **VERIFIED — CORRECT-ON-NEXT-DERIVE.** *The defect is still SERVED.*

> **VINTAGE:** verified at **`a13b96822`**, not `c23988cdf`. My tree was already there when I ran the arms —
> **timing luck, not discipline**, and it is recorded as luck. The `c23988cdf → a13b96822` delta is
> **prose-only** (no executable line changed), so the functional verification carries.

---

## Arms (real `INF_B_00:811` path, real S3, no stubs — I did not take the author's exercise on report)

| arm | result |
|---|---|
| **DEFECT** — 2026-05-08 (was RED: rows=0, ALL $202M on the firm bucket) | **rows=852, reps=4 — REPAIRED** (walk-back engaged) |
| controls — 05-07, 05-09 | rows=852, reps=4 — unchanged |
| **OVER-CONDEMNATION** (CTO mandate) — 2026-07-09 · 2026-06-15 · 2026-04-28 · 2019-01-01 (pre-roster) | **ZERO false raises** (870 · 864 · 850 · 850) |
| **DIRECT-CALLER** — `load_accounts_v2` straight onto the poison | **RAISES `EmptyRosterError`** — fails CLOSED |
| **RENAME BLAST** — old `accounts_v2_key_for_snap` | no orphaned callers |
| **SUITE** — gold + lib | **212/212** · F10 census **6 passed, 6 SELECTED** · SEV fixture **12/12** |

**The over-condemnation arm is the one that mattered.** A fail-closed fix that fires on a legitimate zero *is
the disease it was sent to cure*. It does not fire.

**And a test that does not RUN is not a pass** — so I checked the F10 census's *selection count* (6 selected),
not merely the exit code.

### Two errors of my own, inside the verification

1. **My first suite run said 131, the author said 212.** I did **not** report that as a discrepancy in his
   claim — **I went and found the right denominator.** I had run `gold/tests/` and missed `gold/lib/tests/`.
   *Two counts that disagree usually mean two different UNITS.* His number was right; my scope was wrong.
2. **I suspected the mtime skip-gate would strand the fix** (output 07-10 > input 05-11 → skip → the collapsed
   artifact never recomputed). **Wrong:** `INFINC_PHASE1=0` by default, the gate is a no-op (`dispatch:1163`).
   I checked the **enable condition**, because my local env could only ever have returned `COMPUTE` — *a control
   that cannot fail is not a control*, and that includes a control I run against myself.

## The author's two corrections to my SEV — **both accepted; the first is a real error of mine**

**(1) LAYER 1 (ROOT) WAS ALREADY CLOSED. I PRESCRIBED A PRODUCER FIX WITHOUT OPENING THE PRODUCER.**
The 0-row guard already exists — `convert_orion_api_to_silver.py` (ADHC_BUGB, `6010ea93a`). **I verified the
vintage myself:**

```
guard   2026-05-13T16:03:49Z      poison   2026-05-11T15:41:20Z      -> the guard POSTDATES the poison by 2 days
```

**And the guard's own comment describes my file:** *"silently produced 21KB schema-only parquet writes."* The
poison is **21,032 bytes.** Somebody had already found this exact class and closed it. **2026-05-08 is a
PRE-GUARD RELIC, not a live producer defect** (69 partitions, exactly 1 empty; ~60 written since the guard,
zero empty).

> **This is CTO's amendment with the sign flipped.** He read the consumer and declared the producer
> *irrelevant*; **I read the consumer and declared the producer *broken*.** Neither of us opened it. Had the
> builder obeyed me, he would have shipped a second guard whose green told him nothing.

**(2) "TWO PATHS TO WHICH-accounts_v2" IS SEVEN.** A function-level census — *each file OPENED*, because a grep
scores a docstring as an implementation. `INF_B_00` is the **only per-snap VINTAGE selector**, hence the only
path that can *select* the relic. The `INF_D_*` trio lack a row guard but read **latest** (kept non-empty by the
root guard) → **LATENT, not live.** He did **not** blanket-fix them. *A blanket fix across an ungrounded blast
introduces defects into correct scripts.*

## ⚠ THE THING THAT WILL BE MISREAD — **THE DEFECT IS STILL SERVED**

```
gold/canonical/holdings_2026-05-08.parquet   (LastModified 2026-07-10)
    inflection_wealth_management   $202,062,830.31     n_advisors = 1
```

**The fix repairs the DERIVATION. It does not repair the ARTIFACT.** The served number changes only on a
re-derive — and the re-derive is **HELD**. *An "ON" control that measures the producer's output is not a control
on the SERVED value* (the C_07 lesson). **Nobody may read "SEV fixed" as "the number is right."**

## And the composition — why this fix is a PRECONDITION, never a trigger

**The re-derive that REPAIRS 05-08 is the same re-derive that DELETES $439,326.22** of Class-B NNA from three
named advisors — and `sum(advisors) == firm_total` **ties to the cent through it** (exercised, `3a1459644`).
**You cannot repair 05-08 without firing the deletion.**

```
coverage guard (F7) lands + is EXERCISED  ->  THEN re-derive  ->  05-08 repairs AND the 14 are caught
```

**Do not cite `c23988cdf` / `a13b96822` as licence to rebuild.**

## Credit where it is owed

The author **turned a real gate RED with a comment** (a docstring spelled the banned symbol; the F10 census is a
grep-by-token and scored the *mention* as a *call*), **self-reported it before I could find it**, and **did not
weaken, exempt, or touch the gate to go green** — the single most tempting shortcut available to a builder.
He found it *only* because he ran the **whole** suite: his own 12 were green, his fix was correct, and the thing
he broke was 200 tests away. **A fixture that only runs its own file would have shipped it.**

*Knowing a failure mode by name does not immunize you against writing it* — now demonstrated by five agents in
one night. He is the only one who caught his own instance first.

---

— `3.0.0_SA_CVO`
