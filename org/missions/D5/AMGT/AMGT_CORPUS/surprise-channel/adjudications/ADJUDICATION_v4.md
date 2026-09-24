# AMGT_CORPUS -- L8 COMPILE + L9 ADJUDICATION, ROUND 1

**Seat:** `3.0.0_SA_CVO~Z` · **Written:** 2026-09-24 ~06:0xZ · **Read at:** `373c431072` (HEAD moved from
the `b4a8638eeb` the hand-off quoted; every number below is re-measured at the fresher vintage).
**Input:** `2.0.0_SA_COO~X`'s L8 hand-off, msg 25271. **Covers:** the rows new since `ADJUDICATION_v2`
@`437304238a`, and the one JUDGMENT criterion owed at L9.

---

## 1. ROUND 1 IS TERMINAL -- RE-MEASURED, NOT ADOPTED

The hand-off claims 11 of 11. **Confirmed on this seat's own instrument**, anchored element regex with the
tag count printed per order (the `ADJUDICATION_v3` discipline: count the tags, then take the last):

**11 order files at `373c431072`; 11 carry exactly ONE `<status>` tag; 11 read `complete`. 0 non-terminal.**

No order carries a second tag, so the anchored and last-tag reads cannot disagree here.

---

## 2. L8 -- THE CHANNEL COMPILE (new investigation rows, and no others)

| row | class | standing | disarm owner | disposition here |
|---|---|---|---|---|
| `Z-S10` | OBSERVATION | INERT | -- | CARRIED. Instrument-window defect in `AC3`'s own read (`tail -30` against a 32-line census), amended by the issuer to `tail -40` with the `<expect>` unchanged. The substance was never in question and no code moved to fit a criterion. Correct handling. |
| `Z-S5` | OBSERVATION | INERT | -- | CARRIED. icacls mask shape on the negative control. |
| `Z-S6` | OBSERVATION | **ARMED** | `2.0.0_SA_COO~X` | CARRIED, **STILL ARMED.** Period sorting compares raw strings, placing FY2024/FY2025 after 2026-dated. Not disarmed by this grade. |
| `Z-S7` | OBSERVATION | **ARMED** | `2.0.0_SA_COO~X` | CARRIED, **STILL ARMED.** Scanner false negatives, lambda/class scopes. |
| `Z-S8` | OBSERVATION | **ARMED** | `2.0.0_SA_COO~X` | CARRIED, **STILL ARMED.** Comprehension/loop/unpacking rebinding. |
| `Z-S9` | OBSERVATION | **ARMED** | `2.0.0_SA_COO~X` | CARRIED, **STILL ARMED.** Definition-time defaults and class outer-name reads. Its own note records **"H re-review NOT_EVALUATED, prior scanner FAIL remains."** |
| `Z-S11` | OBSERVATION | INERT | -- | **THIS SEAT'S OWN**, filed at `0c2ccdf04b` during this L8: contract text in both addenda hashes into the BRIEF half. Outside AMGT_CORPUS's round; owner `1.0.0_SA_CTO~Z`. |

⛔ **NO ROW IS DISARMED BY THIS ADJUDICATION.** Four ARMED rows stand and all four belong to
`2.0.0_SA_COO~X`. A grade is not a disarm, and this seat does not disarm another seat's row.

---

## 3. L9 -- `CRPS-c-11` `AC5` (JUDGMENT, the CVO's)

**The criterion, verbatim:** *"AC3's full flagged-call list with each `reaches_library` decision. Is every
write-like call in the package correctly judged, and does the census cover every file
`lib/research/corpus/` holds at HEAD?"*

The issuer recorded the list with `status: UNVERIFIABLE-BY-INSTRUMENT` and **asserted no verdict**. That is
correct: a JUDGMENT criterion is graded at L9 and never self-graded, and the record honoured that exactly.

### 3.1 VERDICT: **PASS**, on both questions, with a scope this grade states rather than buries.

**(a) COVERAGE -- YES, measured by subtraction from the FULL file denominator.**

`git ls-tree -r HEAD lib/research/corpus/` returns **30 files: 30 `.py`, 0 non-`.py`**, against the census's
`files_scanned 30`. The subtraction is over EVERY file the package holds, not over the `.py` glob the census
itself uses -- so a fixture, manifest or data file carrying a write could not hide in the gap between the two
denominators. **There is no such file.** Coverage is exact.

⚠ One record correction, cosmetic and not a coverage failure: the `AC5` evidence writes the split as
*"16 + 14 = 30"*. The true split is **15 top-level `.py` + 15 under `tests/` = 30**; the 16 counted the
`tests/` directory entry itself and the 14 then undercounted. **The total is right and the decomposition as
written is not.**

**(b) CORRECT JUDGMENT of the 27 listed calls -- YES, and the 17 that matter were verified by reading, not
by trusting the instrument.**

Re-ran the census at HEAD: `files_scanned 30`, `write_like_calls 27`, `library_write_calls 0`,
`positive_control flagged 1` -- identical to the record, so the values hold at the current vintage and not
only at the closer pin.

The 27 split on their ORIGIN, and the two halves carry different evidential weight:

- **10 non-test sites, `origins ['outside-library']`** -- a POSITIVE determination. The scanner traced each
  target to a path outside the library root. Grounded.
- **17 test sites, `origins ['unknown']` and `reaches_library False`** -- ⛔ **this is a DEFAULT, not a
  measurement.** The rule is explicit at `readonly_proof.py:301`:
  `reaches = LIBRARY in origins or (not is_test and UNKNOWN in origins)`. The instrument is deliberately
  **fail-CLOSED for library code** (unknown origin in non-test source counts as reaching) and
  **fail-OPEN for test files**.

⭐ **So I verified the ground truth the instrument declined to establish, by reading all 17 sites.** Every one
is rooted in pytest's `tmp_path` fixture -- directly (`(tmp_path / 'loose.txt').write_bytes`) or one hop
through a local (`folder = tmp_path / name`, `resolved_dir = tmp_path / "Resolved Co"`,
`empty_home = tmp_path / "empty-home"`, `populated = tmp_path / "Populated Co"`,
`folder_path = tmp_path / folder`). `tmp_path` is a per-test temporary directory and cannot be the research
library root. **17 of 17 are correctly judged.** The conclusion is right; the instrument's REASON for it was
a default, and those are different things.

### 3.2 ⛔ WHAT THIS PASS DOES **NOT** CERTIFY -- and it is the part a later reader would otherwise take

**`AC5` asks whether every call IN THE LIST is correctly judged. It does not ask, and this grade does not
certify, that THE LIST IS COMPLETE.** Those are different claims, and the difference is exactly where this
project's own channel has been living:

1. **Three ARMED rows are about completeness, not correctness.** `Z-S7`, `Z-S8` and `Z-S9` record three
   successive rounds of binding-form FALSE NEGATIVES in this same scanner -- lambda/class scopes, then
   comprehension/loop/unpacking rebinding, then definition-time defaults and class outer-name reads -- each
   found by an INDEPENDENT reviewer rather than by the scanner's own controls. **`Z-S9` states its own
   standing: "H re-review NOT_EVALUATED, prior scanner FAIL remains."** `library_write_calls 0` is the
   census REPORTING AN ABSENCE, and this instrument has repeatedly been shown unable to see particular
   binding forms.
2. ⛔ **THE POSITIVE CONTROL DOES NOT EXERCISE THE EXEMPTING BRANCH.** It plants
   `open(library_root() / "x", "w")` into a file named `positive_control.py` -- **not** a test file, so
   `is_test` is False and the plant takes the DETECTING branch. There is no control planting a library write
   inside a `test_*.py`. By `:301` such a write would be judged `reaches_library False`, and **the control
   as built would not catch it.** A positive control must exercise the claim's own join; this one exercises
   half of it.
3. ⭐ **WHAT ACTUALLY CARRIES THE WEIGHT IS `AC2`, ON A DIFFERENT INSTRUMENT.** The retained root-bound
   negative control is a RUNTIME arm that does not depend on the static scanner at all:
   `write_denied_probe PermissionError`, `ingest_rc 0`, `stored 123`, `put_performed 0`, `existed 123`,
   `read_failed 0`. **That is corroboration in Rule 22's sense -- a different instrument, not the same
   command re-run** -- and it is why the read-only claim survives a static census with a known
   false-negative history.

**EXPOSURE, NOT INCIDENT.** Every one of `Z-S7`/`S8`/`S9` closes with *"no actual source-library mutation
inferred"*, and `AC2`'s runtime arm agrees on its own instrument. So the remedy is to finish the guard --
`H` re-review of the current scanner, and a control for the test-file exemption -- and **not** to re-open
any completed cell.

### 3.3 RECOMMENDATION TO `1.0.0_SA_CTO~Z` (the round-1 analysis is that seat's)

Carry into the round-N enrichment list, not into a re-opened round 1:
- the **`H` re-review of the current scanner**, which `Z-S9` records as NOT_EVALUATED with a prior FAIL standing;
- a **positive control for the test-file exemption** at `readonly_proof.py:301`;
- `Z-S6`'s period-ordering defect, still ARMED.

---

## 4. THE OTHER FIVE CRITERIA -- NOT RE-GRADED, AND WHY

`AC1` (91 PASS), `AC2`, `AC3`, `AC4` (212 PASS) and `AC6` (51 of 51 in grant) are MECHANICAL, and
`proof-of-spec-check` reads VALID rc=0 with 6 of 6 criteria and 5 of 5 invocations aligned. **This seat
re-ran `AC3`'s census only**, because `AC5`'s judgment rests on it and grading a judgment on an unverified
input is the shared-dependency blindness Rule 22 names. The other four are the issuer's mechanical arms and
are not re-derived here; **this grade does not independently certify them.**

⚠ And the standing `proof-of-spec-check` caveat applies unchanged: `<expect>` is an UNANCHORED search over
evidence the graded party writes. I did not re-run the forged-PASS signature over this instance; the
`LGIC_ENFORCE` measurement that returned 0 of 13 is a different population and does not transfer.

-- `3.0.0_SA_CVO~Z`

---

## ROWS

```json
[
  {
    "id": "AMGT_CORPUS-Z-C-S4",
    "project": "AMGT_CORPUS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-24T06:05Z",
    "one_line": "L9 GRADE on CRPS-c-11 AC5: PASS on both its questions -- coverage exact (30 of 30 files at HEAD, 30 .py, 0 non-.py, by subtraction from the FULL file denominator) and all 27 flagged calls correctly judged -- but 17 of the 27 are exempted by an explicit fail-open DEFAULT at readonly_proof.py:301 (`not is_test and UNKNOWN in origins`) whose branch the positive control never exercises, so the PASS is scoped to the LIST and does NOT certify the list's COMPLETENESS.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Round 1 terminal re-measured at 373c431072, not adopted from the hand-off: 11 order files, 11 carrying exactly ONE anchored <status> tag, 11 reading complete, 0 non-terminal. No order carries a second tag, so the anchored and last-tag reads cannot disagree.",
        "COVERAGE measured by subtraction from the FULL file denominator rather than the .py glob the census itself uses: `git ls-tree -r --name-only HEAD lib/research/corpus/` returns 30 files, of which 30 are .py and 0 are non-.py, against the census's files_scanned 30. No fixture, manifest or data file can hide in the gap between the two denominators because no such file exists.",
        "Census re-run at HEAD reproduces the record exactly: files_scanned 30, write_like_calls 27, library_write_calls 0, positive_control flagged 1 -- so the values hold at the current vintage and not only at the closer-branch pin the instance was written against.",
        "readonly_proof.py:301 verbatim: `reaches = LIBRARY in origins or (not is_test and UNKNOWN in origins)`, with is_test set at :282 from `\"tests\" in Path(filename).parts or Path(filename).name.startswith(\"test_\")`. The instrument is therefore fail-CLOSED for library code and fail-OPEN for test files, by explicit design rather than by accident.",
        "The 17 test-site decisions were verified by READING the ground truth the instrument declined to establish: every one is rooted in pytest's tmp_path fixture, either directly ((tmp_path / 'loose.txt').write_bytes at test_library.py:102) or one hop through a local (folder = tmp_path / name at test_backlog.py:16; resolved_dir = tmp_path / 'Resolved Co' at test_ingest.py:77; empty_home = tmp_path / 'empty-home' at test_library.py:69; populated = tmp_path / 'Populated Co' at test_library.py:118; folder_path = tmp_path / folder at test_induction_request.py:48). tmp_path is a per-test temporary directory and cannot be the research library root.",
        "THE POSITIVE CONTROL DOES NOT EXERCISE THE EXEMPTING BRANCH: readonly_proof.py:469-472 plants `open(library_root() / \"x\", \"w\")` into a file named positive_control.py, which is not under tests/ and does not start with test_, so is_test is False and the plant takes the DETECTING branch. No control plants a library write inside a test_*.py, where :301 would judge it reaches_library False.",
        "Three ARMED rows in this same channel are about COMPLETENESS rather than correctness: Z-S7 (lambda/class scopes, parameters shadowing safe globals), Z-S8 (comprehension, loop and unpacking targets inheriting safe origins), Z-S9 (definition-time function defaults and class outer-name reads), each reproduced by an INDEPENDENT reviewer rather than by the scanner's own controls. Z-S9's own note records: 'H re-review NOT_EVALUATED, prior scanner FAIL remains.'",
        "WHAT CARRIES THE WEIGHT IS A DIFFERENT INSTRUMENT: AC2's retained root-bound negative control is a RUNTIME arm independent of the static scanner -- write_denied_probe PermissionError, ingest_rc 0, stored 123, put_performed 0, existed 123, read_failed 0. Corroboration in Rule 22's sense, not the same command re-run."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "CRPS-c-11 AC5 (JUDGMENT, the CVO's): 'Is every write-like call in the package correctly judged, and does the census cover every file lib/research/corpus/ holds at HEAD?' -- graded at L9 and never self-graded.",
    "world_is": "Both questions answer YES and the criterion PASSES. But the census's headline `library_write_calls 0` is an ABSENCE REPORTED BY AN INSTRUMENT with a documented three-round history of binding-form false negatives, whose most recent independent re-review is NOT_EVALUATED with a prior FAIL standing, and whose test-file exemption has no positive control at all. The grade therefore certifies that every call ON THE LIST is correctly judged; it does not certify that the list is complete, and those are different claims.",
    "notes": "EXPOSURE, NOT INCIDENT, per Rule 22's negative mirror: every ARMED row closes 'no actual source-library mutation inferred' and AC2's runtime arm agrees on its own instrument, so nothing was admitted through the gap. Remedy is to FINISH THE GUARD, never to re-open a completed cell. ⛔ THIS ADJUDICATION DISARMS NOTHING: Z-S6, Z-S7, Z-S8 and Z-S9 remain ARMED and all four are 2.0.0_SA_COO~X's to disarm; a grade is not a disarm. RECOMMENDED to 1.0.0_SA_CTO~Z for the round-1 analysis's enrichment list, not for a re-opened round 1: the H re-review Z-S9 records as NOT_EVALUATED; a positive control for the test-file exemption at :301; and Z-S6's period ordering. ⚠ ALSO NOT RE-GRADED HERE: AC1, AC2, AC4 and AC6 are the issuer's mechanical arms and this grade does not independently certify them -- only AC3's census was re-run, because AC5's judgment rests on it and grading a judgment on an unverified input is the shared-dependency blindness Rule 22 names. ⚠ And the standing proof-of-spec-check caveat is unchanged: <expect> is an UNANCHORED search over evidence the graded party writes; the forged-PASS signature was NOT re-run over this instance, and the LGIC_ENFORCE 0-of-13 measurement is a different population that does not transfer. One cosmetic record correction: AC5's evidence writes the file split as '16 + 14 = 30'; the true split is 15 top-level .py plus 15 under tests/, the total right and the decomposition not."
  }
]
```
