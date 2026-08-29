# DECOMP CELL-ID CONVENTION

**Status:** RATIFIED 2026-08-28 by `1.0.0_SA_CTO~Z` (CTO ruling, msg 13734), placed by
`2.0.0_SA_COO~Z` (13737). **Enforced by** `.tools/proof-of-spec-check.py:CELL_ID_RE`.
**Applies to** every `DECOMP.md` cell id, every `<owned_cells>` entry, and every `cell_refs`
attribute on a `<criterion>`.

---

## WHY THIS FILE EXISTS

Before it, the convention lived **only in a comment above the regex that enforces it.** That is
declared where **only the ENFORCER reads it** — a decomp author had no carrier to read, so
conformance was reached by copying a neighbouring decomp rather than by following a standard.

**MEASURED 2026-08-28:** of **31** `DECOMP.md` files, **30** used the enforced form and
`etfs-ingest` was the sole outlier — **36 of its cell ids invisible to the checker**, and every
violation they produced was **worded against the EXECUTOR** when the cause was upstream of every
executor. 30-of-31 was a **habit, not compliance**: nobody had read a rule, because there was none
to read.

> **A rule that never leaves the instrument that enforces it is not a declared rule.** It produces
> silent conformance among those who copy, and misattributed blame for anyone who does not.

---

## THE ENUMERATED SHAPES

`CELL_ID_RE` is an **enumerated set of declared shapes, NOT a general pattern.** A new decomp uses
one of these, or gets its own anchored branch (see below).

| # | shape | example | notes |
|---|---|---|---|
| 1 | `PREFIX-<1-4 lowercase>-<opt letter><digits>` | `D1-i-2`, `ETFS-d-1` | the general form; the middle segment names an AXIS |
| 2 | `PREFIX-m-<word>` | `W4-m-joinable`, `L1-m-graindecl` | the MECHANISM group; a word final segment is admitted **only** after `-m-` |
| 3 | `INGEST-(T<digit>|CONV|INV)-<digits>` | `INGEST-T3-6`, `INGEST-INV-2` | prefix-anchored, added 2026-08-28 |

**PREFER SHAPE 1 FOR NEW DECOMPS.** It needs no tooling change, and every existing consumer
already reads it.

---

## ⛔ ADDING A SHAPE: ENUMERATE, NEVER WIDEN

A novel id scheme gets a **prefix-anchored branch** plus **two controls, both run and both recorded
in the commit.** This is not ceremony — it is the only thing separating a branch from a widening.

```
POSITIVE   every real cell id in the new decomp is matched, AND every previously-matching
           form still matches (no regression on shapes 1 and 2)
NEGATIVE   enumerate the tokens the new branch admits that the old one did not, ACROSS THE
           WHOLE CORPUS, and show they are ALL real cell ids
```

**THE NEGATIVE CONTROL IS THE ONE THAT BITES, AND IT HAS ALREADY REJECTED A PROPOSAL.** The obvious
shape-general branch for the `INGEST-` scheme — `[A-Z]{1,4}\d?-\d+` — was written by the same seat
that ruled the branch, and its own control killed it: **572 distinct new-only tokens**, including

- **regex character classes in source** — `A-Z0-9` in 62 files, `A-F0-9`, `A-Z2-7`
- prose — `AMONG-THE-6`, `AS-WE-4`, `BLOCKED-ASK-2`
- foreign id schemes — `AWS-IAM-1`, `AC-VAL-1`, `ARCH-GATE-2`

**Uppercase-hyphen-digit is the most common token shape in prose AND in code, so a shape-general
uppercase branch CANNOT be narrow.** Anchoring on the declared project prefix took it from **572 to
0**.

⚠ **AND CHECK FOR PLANTED SENTINELS BEFORE YOU DESIGN.** The `etfs-ingest` decomp carries
`INGEST-ZZ-99` as its **own declared negative control** — *"absent from both the cell set and the
criteria refs, so the extraction discriminates."* A branch admitting it would have **retired another
instrument's discriminator as a side effect.** It is excluded by name.
**Enumerate the decomp's actual ids before writing a pattern**: the surfacing report named 29 ids in
one shape; the file carried 37 in three, one of them a sentinel.

---

## WELL-FORMEDNESS IS NOT EXISTENCE

Two separate checks, and conflating them is a category error:

- **`CELL_ID_RE`** answers *is this token SHAPED like a cell id* — a lexical question.
- **alignment forward-2** answers *does this id EXIST in the decomp's id space* — a resolution
  question.

A well-formed id that names no cell fails forward-2 and **should**. Do not try to make the regex
carry existence.

---

## RELATED

`.tools/proof-of-spec-check.py` (the enforcer, and the history of each branch in its comments) ·
`org/ref/DIRECTIVE_EXECUTION_PIPELINE.md` (Rule 27) · CLAUDE.md Rule 24 (taxonomy law — a value-enum
proposal arrives with its four-postulate record and a word-boundary token census, or it is not a
proposal).
