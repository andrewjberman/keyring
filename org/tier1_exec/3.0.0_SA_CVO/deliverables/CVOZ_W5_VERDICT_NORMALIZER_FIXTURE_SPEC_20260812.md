# W5 VERDICT-NORMALIZER — FIXTURE CORPUS SPECIFICATION

**Author:** `3.0.0_SA_CVO~Z` · **Date:** 2026-08-12 · **Status:** W5 PREP — findings and a fixture
specification. **No normalizer built, no catalog widening, no acts.**
**Against:** CTO~Z's ruling (20260812T171723Z) that W5 carries a verdict normalizer — str-or-dict in,
a token from a closed set out, **RAISING on an unrecognised shape rather than defaulting** — and that
⛔ **the normalizer is itself an instrument and gets its own negative control: it must go RED on the
VOID attempt-1 files.**

---

## WHY THIS DOCUMENT EXISTS

**A fixture set invented by the person writing the normalizer tests the shapes they thought of.** That
is the undiscriminating-instrument class one layer down, and it is what the ⛔ was aimed at. **This
corpus is measured from the tree**, so the normalizer is tested against what exists rather than what
was imagined.

---

## THE MEASURED CORPUS

**Denominator: 18 `certification*.json` files** under `workflows/atom_decomposition/runs/*/*/`.

```
container type:   str 13   |   dict 4   |   NoneType 1
VOID-by-filename:  2
distinct tokens:  PASS · PASS-WITH-REFUSAL · CERTIFIED
```

### ⚠ THERE ARE THREE CONTAINER SHAPES, NOT TWO — AND I CREATED THE THIRD

`portal-page-ticket-center/certification.addendum1.json` **has no `verdict` key at all** (`NoneType`).
**I wrote that file an hour ago, while documenting the problem of two container shapes.** A normalizer
built to the "str or dict" spec would hit it and, depending on its guard, either raise on a legitimate
file or silently return None.

> **The corpus grew a shape during the very session that measured it.** Any normalizer must treat
> "shapes I have seen" as a floor, and its raise-on-unrecognised branch is the load-bearing part —
> not a defensive nicety.

---

## THE NEGATIVE CONTROL SET — and its two members fail DIFFERENTLY

**This is the part a hand-built fixture set would get wrong**, because the obvious move is two
instances of one shape. **These two exercise opposite mechanisms.**

### NC-1 · `portal-page-portfolios/20260811T1640Z/certification.attempt1.VOID.json`

```
container : str, 206 chars
head      : "VOID. THE CERTIFIER MISSED THE PLANTED MUTANT. ..."
"VOID"    : present, index 0        <- the text is honest
"PASS"    : present, index 123      <- inside "...and the pass is void."
"CERTIFIED"/"SOUND" : absent
```

**FAILURE MODE: a substring matcher for `PASS` hits a word inside a sentence that says the opposite.**
The verdict is textually honest and still defeats naive matching. **A normalizer that scans for tokens
anywhere in the string accepts this file.**

### NC-2 · `portal-page-security-scanner/20260812T0158Z/certification.attempt1.VOID.json`

```
container : dict, 986 chars serialised
verdict["certification"]  = "CERTIFIED WITH REFUSAL CORRECTIONS OWED"
verdict["plane_a_values"] = "SOUND. All 16 MEASURED cells re-grounded..."
"VOID"    : ABSENT ENTIRELY from the verdict object
```

**FAILURE MODE: the void is FILENAME-ONLY. A normalizer reading `verdict["certification"]` — which is
the correct, structured, non-naive thing to do — returns `CERTIFIED` for a voided attempt.** The
disciplined implementation fails here, not the sloppy one.

> ⛔ **THE TWO CONTROLS TOGETHER PROVE THE NORMALIZER CANNOT BE A TEXT PROBLEM.** NC-1 defeats
> substring matching; NC-2 defeats structured field reading. **Nothing that reads only the verdict —
> by any method — can classify both correctly.** The void state is not fully carried in the verdict,
> and W5's F-3 rule ("keys off the verdict field of the file named EXACTLY `certification.json`; a
> glob is prohibited") is therefore **load-bearing rather than stylistic**: it is the only thing
> standing between the lift and NC-2.

---

## REQUIRED FIXTURE SET, with expected outcomes

| # | fixture | container | expected |
|---|---|---|---|
| P-1 | `portal-page-attribution` | str, `PASS — ...` | `PASS` |
| P-2 | `portal-page-cma/1729Z` | str, `PASS-WITH-REFUSAL — ...` | `PASS-WITH-REFUSAL` |
| P-3 | `news-subsystem` | dict, `certification: CERTIFIED` | `CERTIFIED` |
| P-4 | `portal-page-security-scanner` (live) | dict, `PASS-WITH-REFUSAL` | `PASS-WITH-REFUSAL` |
| P-5 | `portal-page-portfolios` (live) | str, `PASS -- CERTIFIED WITH ONE REFUSED CELL` | `PASS` — ⚠ **contains `CERTIFIED` in its own text; must not classify as `CERTIFIED`** |
| **N-1** | **portfolios VOID** | str | **RED / refuse** — defeats substring matching |
| **N-2** | **security-scanner VOID** | dict | **RED / refuse** — defeats structured field reading |
| **R-1** | `certification.addendum1.json` | **no `verdict` key** | **RAISE**, not `None` |
| R-2 | a synthetic `{"verdict": 42}` | int | **RAISE** |
| R-3 | a synthetic unrecognised token | str, `"MAYBE"` | **RAISE**, never a default |

**P-5 is the sharpest positive fixture and it is easy to miss:** the live portfolios verdict reads
`PASS -- CERTIFIED WITH ONE REFUSED CELL`. **A normalizer that scans for `CERTIFIED` classifies a
`PASS` as `CERTIFIED`** — and both are valid tokens, so the error is silent and produces a
well-formed wrong answer rather than a failure.

---

## WHAT THIS SPEC DOES NOT SETTLE

- **How the void state should be represented going forward.** NC-2 shows it is filename-only in one of
  two cases; AM's remedy fixed portfolios and not security-scanner. **That is a schema act and it is
  not mine** — flagged, not designed.
- **The token set is a floor, not a closed world.** Three tokens exist across 18 files today; the
  corpus grew a container shape during this session.
- **I have not built or tested a normalizer.** This is the corpus and the expected outcomes.

## THE ONE-LINE VERSION

> **Do not build the normalizer's fixtures from imagination. NC-1 and NC-2 fail by opposite
> mechanisms, and no reader of the verdict alone classifies both correctly — which is why F-3's
> exact-filename rule carries the weight and not the parser.**

— `3.0.0_SA_CVO~Z`
