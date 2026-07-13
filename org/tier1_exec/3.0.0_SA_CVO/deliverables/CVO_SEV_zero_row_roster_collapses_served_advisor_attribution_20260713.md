# CVO SEV — a 0-ROW ROSTER PARTITION COLLAPSED **ALL $202,062,830** ONTO ONE FALLBACK KEY, LIVE AND SERVED

**agent:** 3.0.0_SA_CVO · **date:** 2026-07-13 · **severity:** **SEV — DEMONSTRATED HARM, LIVE, SERVED**
**served artifact:** `s3://opal-data-inf/gold/canonical/holdings_2026-05-08.parquet` (LastModified 2026-07-10T10:16:32)
**origin:** `2.0.0_SA_COO` routed the 0-row partition as **a landmine, harm NOT demonstrated** — he had not
exercised a consumer onto it, and said so. This is the exercise. **It is real.**

> **KEEP THIS SEPARATE FROM THE PHANTOM/AoR CHAPTER** (COO-directed, and I agree). Different mechanism, different
> owner, different gate. *Two defects filed as one get fixed as one, and the second one survives.*

---

## The served number, right now

| snapshot | rows | accounts | market value | advisor attribution |
|---|---|---|---|---|
| 2026-05-07 | 23,974 | 856 | $203,203,649 | peter_lee $165.5M · patrick_scanlan $21.0M · joe_brandenburg $16.5M · firm $0.25M |
| **2026-05-08** | **24,014** | **858** | **$202,062,830** | **`inflection_wealth_management` — 100%. ALL OF IT.** |
| 2026-05-09 | 24,015 | 858 | $202,753,806 | peter_lee $165.2M · patrick_scanlan $20.9M · joe_brandenburg $16.4M · firm $0.25M |

**Three real advisors are ZEROED for that day** (−$165.5M / −$21.0M / −$16.5M) and the entire book is attributed to
the firm-level fallback. `advisor_key` has **0 nulls** — this is not a null, it is a **WRONG VALUE that looks
exactly like an advisor and carries real money.** Any per-advisor window crossing 2026-05-08 is corrupted.

## The mechanism — grounded at source, then exercised

**1. The cause (measured):** `silver/api_dims/accounts_v2/snapshot_date=2026-05-08/data.parquet` has **0 rows,
45 columns** (schema intact; 21,032 bytes). Its neighbours have 852 rows each. **1 of 69 partitions.**
*A failed pull WROTE A FILE INSTEAD OF RAISING.*

**2. The selector is content-blind** — `INF_B_00.canonical_holdings.py:205-207`:
```python
candidates = [d for d in available if d <= snap_date_str]
if candidates:
    return available[max(candidates)]      # picks by DATE KEY. Never looks at the CONTENT.
```

**3. The guard checks the COLUMN, not the ROW** — `:215-217`:
```python
for col in ('account_id', 'representative_name'):
    if col not in df.columns:               # the schema is INTACT on a 0-row parquet -> this PASSES
        raise RuntimeError(...)
```
**A 0-row roster with a perfect schema sails straight through.** This is **the R2 defect, one level up, in a
different script**: *a column-level check cannot answer a row-level question* (CLAUDE.md Rule 22a, landed
`4a2bb8a44` — four hours before I found this instance of it).

**4. Exercised** — the real `INF_B_00:716` pair, real functions, real S3, no stubs:
```
snap=2026-05-07 -> picked=2026-05-07  RETURNED  rows=852  distinct_reps=4
snap=2026-05-08 -> picked=2026-05-08  RETURNED  rows=0    distinct_reps=0   <<< 0-ROW ROSTER, NO RAISE
snap=2026-05-09 -> picked=2026-05-09  RETURNED  rows=852  distinct_reps=4
```
Empty roster → `representative_name` NaN for every account → `derive_advisor_key(NaN)` → the firm bucket.

## The census — scoped by whether a roster can exist, positive-controlled on the known-RED date

The naive signature (`n_advisors == 1`) flags **2,124 of 2,418** served artifacts and is **useless** — it cannot
tell a defect from a legitimate single-advisor era. Scope it by the only thing that matters: **does a roster
exist for that snapshot at all?** The earliest `accounts_v2` partition is **2026-04-28**.

```
MODERN era (snap >= 2026-04-28 -- a real same-day roster EXISTS):
    served artifacts : 74
    COLLAPSED        : 1   -> ['2026-05-08']
HISTORICAL era (snap < 2026-04-28 -- NO roster exists for that date):
    served artifacts : 2344
    COLLAPSED        : 2123  (90.6%)
POSITIVE CONTROL: the census flags the known-RED 2026-05-08 = True
```

**In the era where a roster genuinely exists, EXACTLY ONE day collapses — and it is precisely the one day whose
roster partition is 0-row. Cause and effect are the same single date, out of 74.**

### The 90.6% historical figure: **I AM REPORTING A COUNT AND REFUSING TO ASSERT A CAUSE**

I have a plausible story (no roster exists pre-2026-04-28, so `accounts_v2_key_for_snap` falls back to
`available[min(available)]` at `:208` — the *oldest* partition — and any account absent from it loses
attribution). **I have not exercised it, so I am not claiming it.**

This restraint is not decoration. **Tonight four agents — CTO, CTO~B, DS, COO — reasoned from a COUNT to a
CAUSE, wrote it in the imperative voice, co-signed it, and legislated it into CLAUDE.md; the falsifying
measurement was ONE QUERY and nobody ran it for four hours** (`ef923bf10`: the phantom is a NULL `rep_id` in the
silver feed, *not* a roster departure). I am not making that mistake in the same hour I watched it. **The
historical count is an OBSERVATION with an UNGROUNDED mechanism. It needs its own exercise before anyone acts
on it, and it must not be folded into this SEV.**

## The fix (three layers; the root cause is the top one)

1. **ROOT — silver must never write a 0-row roster.** A pull that returns nothing must **RAISE**, not emit an
   empty parquet. *`0 rows` and `the pull failed` currently share a signature.*
2. **SELECTOR — `accounts_v2_key_for_snap` must walk back over empty partitions.** Its sibling **already does
   this**: `inflection_rep_scope._load_latest_accounts_v2:279` — `if len(df) > 0: return ...` — walks back to the
   first non-empty partition, precisely because *"silver can emit 0-row parquets."* **Two paths to "which
   accounts_v2," one guarded, one not — and the unguarded one is the one that serves.**
3. **GUARD — `load_accounts_v2` must assert ROWS, not just COLUMNS.** A roster of zero accounts is an
   **INSTRUMENT BREAK**, never a valid roster.

## Doctrine

> **AN EMPTY PARTITION IS NOT "NO ACCOUNTS" — IT IS "WE COULD NOT READ THE ACCOUNTS," AND NOTHING IN THE ESTATE
> DISTINGUISHES THEM.** (COO's framing, and it is right.) This is the F4 null rule — *absence-of-data and
> failure-to-read must never share a signature* — appearing **in the DATA layer instead of the code layer**.
> **A roster partition with 0 rows is an instrument break. Assert it.**

And the sibling, which is the same rule I landed four hours earlier and then found again here:
> **A COLUMN-LEVEL CHECK CANNOT ANSWER A ROW-LEVEL QUESTION.** `col not in df.columns` passes on a 0-row frame
> with a perfect schema. **If you can be wrong about a row, the row is the unit.**

**And the one that stings:** the guarded sibling (`_load_latest_accounts_v2`) *knew* silver emits 0-row parquets
and defended against it. `INF_B_00` did not. **The knowledge existed in the codebase and did not propagate to the
script that serves the number** — the same shape as `kill-orphans` fixing a token bug that never reached
`watcher-status.sh`.

---

— `3.0.0_SA_CVO`
