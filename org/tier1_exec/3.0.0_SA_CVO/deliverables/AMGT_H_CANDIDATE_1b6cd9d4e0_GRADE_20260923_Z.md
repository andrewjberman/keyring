# CVO GRADE -- H pinned candidate `1b6cd9d4e0` (`2.0.0_SA_COO~Y`)

**Reviewer** `3.0.0_SA_CVO~Z`. **2026-09-23.** Under closer CONTRACT v1.0 s.5. Branch
`closer/amgt-h-y-20260923`, LOCAL. Supersedes the `621bf1d5d7` and `56621b4949` handoffs.

## VERDICT

| boundary | grade |
|---|---|
| **Source/offline: the R5 inversion is closed** | **PASS** (exercised) |
| **Amendment 4 `no_coverage` semantic counter** | **NOT MET -- correctly self-reported as owed** |
| **H-a: `mention_score` dropped for `NO_COVERAGE`** | ⛔ **NEW FINDING, unnamed by any seat** |
| **H1-H4 acceptance IDs** | **NOT_EVALUATED** -- no `B00`/`E0`, per s.2 LIVE FIRST |
| Deploy / cutover acceptance | **NOT CLAIMED, NOT GIVEN** |

## 1. ANCESTRY -- EVERY CLAIM VERIFIED

`git merge-base --is-ancestor`, run here:

- `0e9ed7b1d8` (the 996-commit integration merge) -> **YES.** The candidate is built on the integrated
  tree, not the stale base. This was a live risk named by `0.0.0_AB_MSTR~Z` and it is cleared.
- `621bf1d5d7` and `56621b4949` -> **YES, both.** The explicit-state H writer chain is carried.
- `dd9df4305c` (amendment 4 + R8, the ratified PRD) -> **NO**, and that is expected and correct: the
  candidate branch predates the ratified text, so it **cannot** have been built against amendment 4's
  `no_coverage` clause. `2.0.0_SA_COO~Y` states this itself rather than letting it pass.

## 2. THE R5 INVERSION IS CLOSED -- EXERCISED, WITH A DISCRIMINATING CONTROL

The candidate modifies `lib/research/coverage/pool_reader.py` (+33/-3) and adds an allowlist guard
ahead of the map lookup:

```python
if (status not in (GOLD_DAY_COMPLETE, GOLD_DAY_PARTIAL, GOLD_DAY_DENIED)
        or not math.isfinite(score) or score < 0
        or isinstance(row.get("mention_score"), bool)):
    counters["malformed"] += 1
    continue
```

Because `malformed` is in `STATE_NAMES` it is summed into `incomplete`, so an unrecognised status can
no longer reach the `.get()` miss. Driven directly at the pin, one row, only `data_status` varying:

| `data_status` | `states` | `complete` | score kept |
|---|---|---|---|
| `COMPLETE` | `{}` | **True** | yes |
| `DENIED` (positive control) | `denied=1` | False | yes |
| `PARTIAL` | `partial=1` | False | yes |
| `NO_COVERAGE` | `malformed=1` | **False** | **no** |
| `UNKNOWN_VALUE` | `malformed=1` | False | no |
| `None` | `malformed=1` | False | no |

**`COMPLETE` still returns `complete=True`, so the check discriminates** -- this is not a reader that
calls everything incomplete. **The defect this seat refused the PRD over cannot occur at this pin.**
`2.0.0_SA_COO~Y`'s claim is confirmed.

⚠ **INSTRUMENT, stated because it matters:** this seat did **not** re-run that lane's 214 focused
tests. Re-running their suite would be repetition of their method. The exercise above is a **different
instrument** on the same object, which is why it found section 3.

## 3. ⛔ H-a -- NEW FINDING. THE MIGRATION WOULD SILENTLY DROP 1,595 DAYS' SCORES FROM THE SERVED SERIES

**No seat has named this, including this one until now.**

`counts` is the `{date: mention_score}` series the reader returns. Today a `DENIED` day **keeps its
score in `counts`** -- the module's own docstring is explicit: *"A day graded PARTIAL or DENIED is
counted in `states` ... and **STILL carries its `mention_score` in `counts`** -- the state block, not a
silent zero in the series, is what tells a caller the day was not a clean read."*

Under this candidate a `NO_COVERAGE` day takes the `malformed` branch, which **`continue`s before
`counts[day_str] = score`**. Measured above: score kept for `DENIED`, **dropped for `NO_COVERAGE`**.

⛔ **So when the ratified migration relabels 1,595 of 1,596 rows, those days stop contributing to
`counts` entirely** -- not merely re-labelled, **removed from the series**. That is the precise
behaviour the docstring says the state block exists to avoid, arrived at from the other direction: the
first defect served a silent *clean read*, this one serves a silent *gap*.

⭐ **IMPLEMENTING AMENDMENT 4 PROPERLY ALSO FIXES THIS, which is the argument for doing it rather than
keeping the `malformed` bucket as a stopgap:** a `no_coverage` counter puts the day on the counted
path, where the score is written exactly as `DENIED`'s is. **REQUIREMENT: the `no_coverage`
implementation preserves `mention_score` in `counts`, matching `DENIED`'s treatment and the module's
own stated contract.** The implementation is `2.0.0_SA_COO~Y`'s; this seat names the obligation only.

## 4. WHY `malformed` IS A STOPGAP AND NOT THE REMEDY

Verified at the pin: `STATE_NAMES` is `('missing_body', 'malformed', 'denied', 'partial')` --
**no `no_coverage`** -- and `_GOLD_DAY_STATE_MAP` still carries **only** `DENIED` and `PARTIAL`.

Amendment 4 ratifies `NO_COVERAGE` as a **legal member** of the daily enum. Grading a legal member as
`malformed` tells a caller **the producer emitted a schema-invalid row**, when the truth is a
well-formed row saying no enabled publisher covered that day. That is a different assertion about a
different subject, and it is the same conflation amendment 3 retired `DENIED` to end.

**It does satisfy amendment 4's clause that an unrecognised `data_status` "raises or is counted and is
never silently skipped"** -- it is counted. **The safety half is met; the semantic half is not.**
Amendment 4 clause 4's ordering still holds: `publication_gold.py:579` still writes `"DENIED"`, so no
producer emits `NO_COVERAGE` yet and nothing is re-opened.

## 5. WHAT IS NOT GRADED, AND IS NEVER AN IMPLIED PASS

`H1`-`H4` stand **NOT_EVALUATED**. s.2 LIVE FIRST governs: offline closures grade nothing until
`B00`/`E0` passes, and `E0` is UNGRADED for want of a captured trace. Also ungraded here: the Price
migration handback under R-9 (`lib/research/price/**` returned to `2.0.0_SA_COO~Z`, a surface this
seat has not measured); the five injected-I/O controls; the CLI nonzero-return modes; and the
claim of no live writes. **This seat's silence on any of these is not consent.**

**No relabelling of producer or retained rows has occurred** -- confirmed at HEAD, where
`publication_gold.py:579` still assigns `"DENIED"`.

## 6. SUMMARY FOR THE INTEGRATOR

The candidate is **sound on the safety property and honest about what it does not do.** The lane
self-reported the amendment-4 gap rather than letting a `complete=False` result stand in for the
ratified remedy, which is the correct behaviour and is the reason this grade is a PASS on its stated
boundary. **H-a is the one thing that should not reach a build**: the `no_coverage` implementation must
preserve the score, or the migration trades a false clean read for a silent gap in the served series.
