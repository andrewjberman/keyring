# MDPF_CANPLAT.G2 — Verification Instruments (R7 / R1 / R2 / R12)

**Seat:** `3.0.0_SA_CVO~Z` · **TO:** `MDPF_CANPLAT.G2.regression-comparator-and-acceptance` @f123fbf6e
**Governing:** PRD @24d3eb2f8 §5.5 (Guard 2) · CONTRACT @a3106d585 (§B = the closed field-path list; §E rows R1/R2/R7/R12)

> ⛔ PRD §0 binds: SHAPE project, correct-and-live business logic, no error-hunting. A comparator diff
> is a REGRESSION REPORT to `2.0.0_SA_COO~Z` — DS~Z/AE~Z fix under their TOs; this seat never fixes.
> Run-and-read per verification event. **No standing comparator service.**

## The instruments

| File | Rubric row | What it does |
|---|---|---|
| `pin_baseline.py` | R7 limb 3 | Pins the served platinum surface to explicit S3 VersionIds + ETags + sha256 at a stamped instant. Re-pins are NEW manifests, never edits. |
| `r7_comparator.py` | R7 (all five limbs) | Value-identity per JSON path vs the pinned baseline, under the declared canonicalisation, consuming `sectionB_field_paths.json` as the closed exemption list. Also carries the three-state selftest. |
| `g2_instruments.py` | R1 / R2 / R12 | `r1` = EXISTENCE (never freshness) of the 12 canonical keys. `r2` = key-set identity per artifact type across the four scopes (set-diff = empty is PASS). `r12` = both standalone extras still present (retirement is Andrew's act, never this program's). |
| `sectionB_field_paths.json` | R7 limb 5 | The CLOSED field-path list, extracted from CONTRACT §B. Only `exemptions` entries can excuse a diff; `decision_pending` and `path_pending` excuse NOTHING. |

**R7, quoted as the row (CONTRACT §E):** *"REGRESSION TEST — all five limbs. PASS iff value-identical
per JSON path · declared canonicalisation · mutation shown to FAIL and LOCALISE · baseline pinned to
VersionIds at a stamped instant · absent≠null≠zero."*

**No PASS from the comparator is citable until its mutation exercise is on the record.** The comparator
enforces this mechanically: without `--mutation-record <path>` pointing at an existing record file, every
report is stamped `PASS-NOT-CITABLE`.

## THE DECLARED CANONICALISATION (Guard 2 limb 1 — cited by G2 and P1-1)

Confirmed jointly with `0.4.0_DS_ClientPlatform~Z` (P1-1), msg `20260807T000529Z`, as proposed:

1. **Strict JSON parse.** Objects compare as **unordered maps** (key order irrelevant).
2. **Arrays are ORDER-SIGNIFICANT** — `dates[]` and every parallel array carry meaning by position.
3. **Numbers compare by mathematical value** via `Decimal` parse of the raw literal: `5 == 5.0`,
   `0.1 == 0.10`. A pure int/float literal change is not a business diff (emitter fact on record:
   gold counts may emit int where a prior producer emitted float, or vice versa, after the port).
   `NaN`/`Infinity` are rejected as non-JSON (emitter obligation on record: P1-1 sets
   `allow_nan=False` so a NaN dies loud at the emitter, never absorbed here).
4. **Strings: exact unicode codepoint equality.** No NFC/NFD normalisation, no case folding — a
   normalisation difference is a REAL diff and surfaces.
5. **ABSENT vs NULL vs ZERO are THREE DISTINCT STATES** and produce three distinct verdicts. Absent is
   never zero; null is never absent. (Containers report as OBJECT/ARRAY states, so `null -> {…}` is one
   localised diff at its path, not a spray of child diffs.)
6. **Paths are dotted JSON paths** with `[i]` array indices; literal dots in keys are escaped `\.`.

**Newly-present subtree note:** a subtree excused wholesale by a named `absent_to_present` /
`fold_in_new` exemption becomes value-guarded from the next re-pin onward (once present in the
baseline, every subsequent change is guarded). The Guard-3 `null -> 0` class on EXISTING baseline
arrays is fully guarded from day one (`null_to_nonzero_value_only`).

## Run protocol (run-and-read; per verification event)

```
python pin_baseline.py                      # writes baseline_manifest_<UTCSTAMP>.json (new file each pin)
python g2_instruments.py r1                 # EXISTENCE 12/12 (never reported as freshness)
python g2_instruments.py r2                 # key-set identity per type across scopes
python g2_instruments.py r12                # both extras still present
python r7_comparator.py selftest-three-state --record   # three-state fixture verdicts, on the record
python r7_comparator.py compare --manifest <manifest> --candidate-dir <dir> [--live] \
       --mutation-record records/MUTATION_EXERCISE_<date>.md
```

**Vintage discipline (protocol, not instrument):** the comparator answers value-parity vs the pinned
baseline; it does not adjudicate whether the candidate SHOULD tie the baseline. A same-data-day
candidate (the port's output for the baseline's data day) is the valid comparison; the report header
prints both sides' `as_of_last` / `n_dates` / `last_updated` so vintage skew is visible, and skew
diffs land as regression-classified diffs for COO~Z adjudication — the instrument never silently
excuses appended dates.

## Records

- `records/MUTATION_EXERCISE_<date>.md` — the FAIL + LOCALISE exercise (business-value mutant + the
  DS~Z-requested Guard-3 `null -> 0` parallel-array mutant), verbatim outputs.
- `records/THREE_STATE_<date>.md` — absent/null/zero producing three distinct verdicts.
- `records/R1_R2_R12_first_run_<date>.md` — first exercised run of the three instruments, denominators printed.

— 3.0.0_SA_CVO
