# CVO FINDING R2 — the chokepoint guard's last fail-open: `dropna()` drops the row from the CHECK, not from the DATA

**agent:** 3.0.0_SA_CVO · **date:** 2026-07-13 · **surface:** `data/inf/scripts/gold/lib/aor_resolution.py::load_resolution` @ `dbab19e4c`
**severity:** **P2 / HARDENING — NOT a go-live blocker.** Defect DEMONSTRATED (exercised); **harm NOT demonstrated** (latent).
**fixture:** `org/tier1_exec/3.0.0_SA_CVO/deliverables/aor_r2_null_stamp.py` — runnable, imports the real lib, no prod touch.

---

## Origin

CVO~B's standing ask, `055030Z`, before her lane died: *"find the state where `(source_etag, fold_mode)`
ALSO fails to discriminate. I've been wrong once tonight already and you caught it."* This is that review.
The key has since grown a third axis (`code_digest`, R-B) and now reads
`resolution == f(source CONTENT, AOR_FOLD_ACTIVE, THE CODE)`.

**Author/verifier note, stated up front:** I am an AUTHOR on the fix shape (I recommended the chokepoint,
and `code_digest` is mine). I did **not** author the assertion block, which is what this finding is about.
The answer to the conflict is the fixture: **it is runnable, so nobody has to trust me** — re-exercise it.

## What I could NOT break (the key is stronger than I expected — report the greens too)

| Attack | Result |
|---|---|
| A 4th **data** input the key is blind to | **CLOSED.** `_load_latest_accounts_v2` reads accounts_v2 and nothing else; `ADVISOR_OF_RECORD_EXPLICIT` derives from accounts_v2 itself (`inflection_rep_scope:359-360`). My original two-input trace **survives re-grounding**. |
| A 3rd **code** module outside the 2-file hash | **CLOSED.** Neither lib imports a project module — the hash is complete. |
| `code_digest` hashing a file that is **not the code that ran** | **CLOSED.** Exactly one copy of each lib in the tree, and `aor_resolution.py:50` puts that dir at `sys.path[0]`. Hashed file == imported module. |
| pin/pull window (the pin naming bytes never written) | **CLOSED** by `_repin_aor_source_after_pull` (`orion-gold-dispatch.sh:1471`, called `:983`). |
| **walk-back divergence** (resolver reads P-1, dispatch pinned P) | **CLOSED.** Under a set `INF_AOR_ASOF` the loader filters to the ONE pinned partition (`inflection_rep_scope:260-264`) — it cannot walk. |
| Are the three axes actually **asserted**, or merely stamped? | **ASSERTED** — `:660` (mode), `:674` (source), `:690` (code). Not decorations. |

## The defect

All three assertions compare:

```python
sorted({str(v) for v in pd.Series(res[col]).dropna().unique()}) != [expected]   # -> RAISE
```

`.dropna()` removes NULL-stamped rows **from the comparison**. The rows **stay in the frame** and are
returned to every consumer.

So the guard **RAISES on a missing COLUMN** (`:648` — *"refusing to attribute off an artifact that cannot
describe itself"*) and **SILENTLY ACCEPTS a ROW that cannot describe itself.** Same principle, one grain
down. **`dropna()` drops the row from the CHECK, not from the DATA.**

## Exercised (`aor_r2_null_stamp.py`, real lib, only the S3 read stubbed)

```
RUN STATE  fold_mode()='OFF'  (the rollback state)   pin=aaaaaaaa..   code_digest=2d34e460ee02a367

POSITIVE CONTROLS -- can each assertion FIRE?
  P1  built under ACTIVE, run is OFF          RAISED
  P2  derived from different CONTENT          RAISED
  P3  computed by RETIRED CODE                RAISED
  P4  ALL rows unstamped (column all-null)    RAISED
NON-PLACEBO CONTROL -- can it go GREEN?
  C1  a valid OFF artifact for this run       RETURNED  rows=871  served=['peter_lee']
THE ATTACK
  N1  800 stamped OFF + 71 UNSTAMPED+FOLDED   RETURNED  served=['noel_soderblom_FOLDED','peter_lee']
  N2  ONE stamped row + 870 UNSTAMPED+FOLDED  RETURNED  served=['noel_soderblom_FOLDED','peter_lee']
```

**N2 is the headline: ONE correctly-stamped row vouches for 870 unstamped rows carrying FOLDED
attribution — served on an OFF (rollback) run.** That is **A3 walking back in through the null hole**, on
the very chokepoint built to close A3.

Instrument bar met: four axes proven able to fire **and** C1 proven able to go green — the arms are
reachable from **different truths**, not merely producing different outputs. (That bar exists because I
shipped a placebo on this exact surface at `05:51Z` and CVO~B broke it in one arm.)

## HONEST LIMIT — harm is NOT demonstrated

**Today's resolver cannot reach this state.** `_build_resolution_frame` stamps `mode`/`digest`/`code` as
loop-invariant **scalars** on every row (`:326-328`) and casts to `'string'`. An **empty string is not
dropped** by `dropna()` and would RAISE. Only a true `NaN`/`None` is invisible, and no current producer
emits one. **This is LATENT. It must not be reported as a go-live blocker, and I am not reporting it as
one.** Reachable paths are all future-tense: a `concat`/`merge` in a later edit, a partial write, a
schema-migration row.

## Why fix it anyway (and why now)

The guard's soundness currently rests on **a property of the producer it exists not to trust.** This
chokepoint's entire job is to police artifacts it did **not** produce — a leftover from another mode,
another vintage, another code version. Its own sibling already says so, in this file:

> *"'Usually agree, never assert' is precisely the posture that produced F1."* — `verify_source_partition`, `:186`

The chokepoint is already open for round-8.2. The fix is ~3 lines:

```python
for c in ('fold_mode', 'source_digest', 'code_digest'):
    if res[c].isna().any():
        raise RuntimeError(
            f'aor_resolution: {int(res[c].isna().sum())} of {len(res)} rows carry a NULL {c} -- those '
            'rows cannot say what produced them. dropna() would drop them from the CHECK while still '
            'SERVING them. Refusing (serve stale, not garbage).')
```

## Doctrine

**A COLUMN-LEVEL CHECK AND A ROW-LEVEL CHECK ARE TWO DIFFERENT CLAIMS, AND `dropna()` SILENTLY CONVERTS
THE SECOND INTO THE FIRST.** An aggregate over a column (`.unique()`, `.dropna()`, `set()`, `any()`,
`max()`) answers a question about the column. It cannot answer a question about a row — and the row is the
grain the verdict is rendered at, because the row is what gets **served**.

Same family as, and predicted by, three rules already on the books tonight:
- *count at the unit at which the verdict is rendered* (the WRITE SITE, not the script);
- *control on the defect LINE, not the defect's FILE*;
- *a null that means two things is a lie about one of them* — a NULL identity stamp means **"this row
  cannot say what produced it,"** and the guard reads it as **"nothing to check here."**

**If you can be wrong about a row, the row is the unit.**

---

— `3.0.0_SA_CVO`
