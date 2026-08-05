# DOCTRINE DRAFT — THE FIVE DENOMINATOR ERRORS

**Status:** DRAFT for `docs/doctrine/`. **Authored in the CVO lane; NOT landed** — `docs/doctrine/`
is outside this seat's commit authority. Routed to `1.0.0_SA_CTO` to land or amend.
**Source:** Andrew-direct, CVO terminal, 2026-08-05 ~1615Z, stated as an EXISTING list
(*"which we historically listed as"*).
**Andrew approved recording it as doctrine + making it operational**, same session.

## ⛔ RETRACTED — MY ABSENCE CLAIM WAS FALSE. THE TAXONOMY HAS EXISTED SINCE 2026-07-24.

**This file originally asserted:** *"NOT FOUND IN THE SEARCHABLE RECORD UNDER THESE NAMES. `comp-grep`
scanned 22,307 of 24,239 files... This is the first durable record."*

**That is FALSE and the claim is withdrawn.** Found by `4.0.0_SA_CRO`, verified at source by me:

> `infra/system/ontology/ARCHETYPAL_LEARNING_LOOP.md` §2 — created **`977e1251e9`, `1.0.0_SA_CTO~Z`,
> 2026-07-24 10:21**, and `git log -S"SEMANTIC REDIRECT"` confirms the string entered **in that
> creating commit**: `1 NEW AXIS · 2 GRAIN SHIFT · 3 SEMANTIC REDIRECT · 4 VOCABULARY POVERTY ·
> 5 MERGE / SPLIT`. Same five, same order, same names but POVERTY/MISSING. **Twelve days before mine.**

### The mechanism — and it is NOT the one CRO diagnosed

CRO attributed the miss to searching the wrong token *(they live under "the five orthogonal shapes")*.
**Measured, that is not it.** My pattern was `"Semantic Redirect|Grain Shift|New Axis|Vocab Missing"` —
**mixed case. The source file is ALL CAPS: `SEMANTIC REDIRECT`.** `comp-grep` uses Python `re`,
case-sensitive by default. **I searched the RIGHT tokens in the WRONG CASE**, and a case-sensitive
regex over an all-caps heading returns exactly what an absent concept returns: zero.

*(Control: the same mixed-case pattern now returns 24 hits in 3 files — my own artifacts and CRO's,
written today in mixed case. The all-caps original is still invisible to it.)*

### ⚠ THE PART THAT MAKES THIS THE WORST INSTANCE OF THE DAY: THE TOOL TOLD ME

`comp-grep`'s own output said, verbatim:

> `0 hits in the 22307 file(s) actually searched. This is NOT a confirmation of absence -- widen the
> pattern, or check git check-ignore.`

**The instrument printed the correct warning and I published the absence anyway** — and I cited the
denominator (22,307) as if a large denominator *validated* the claim, when the tool was telling me the
denominator was irrelevant to it. **A denominator makes a zero AUDITABLE; it does not make it TRUE.**
Then CTO landed it into `docs/doctrine/DENOMINATOR_ERRORS.md`, so a false provenance claim reached
doctrine — routed for correction the moment it was found.

**This is instance #15 of `THE RETRIEVAL IS THE DEFECT` (@ccdaa06e7), committed inside the very
document that catalogues the class, in its central provenance claim, after the tool warned me.**

### What is TRUE, restated

Three surfaces of ONE taxonomy, carrying **different intents** — which is Rule 24 (iii) failing
*across* documents, and worse than a duplicate because each is correct about its own subject:

| surface | date | intent |
|---|---|---|
| `ARCHETYPAL_LEARNING_LOOP.md` §2 (CTO~Z) | 07-24 | shapes of **CHANGE an enumerator cannot see** — a **DETECTION** taxonomy |
| CRO's denominator doctrine §9 | 08-05 | the same five, carried forward + audited |
| **this file** | 08-05 | ways a semantic **LENS misreads a substrate** — a **DIAGNOSIS** taxonomy |

**This file is SUBORDINATE and cross-linked, not a peer.** Its one non-duplicative contribution is the
**operational** half: *classify before you remedy, because the class determines the remedy.* The
authoritative-surface decision is Andrew's; CRO is holding the fold until he rules.

## The problem it names

The estate holds a **deterministic truth state** — stable, measurable. Reading it requires a
**semantic lens**, and the lens is where it goes wrong: identifying the correct axis, or conflating
axes, or shifting grain. These five are the recurring ways the lens misreads a stable substrate.

## The five

| # | Error | What it is |
|---|---|---|
| **1** | **New Axis** *(Case C)* | The thing being described belongs to a **different axis** than the one it was recorded on. Two axes occupying one field. |
| **2** | **Grain Shift** | Values on one axis sit at **incompatible grains** — a file-level value beside a cohort-level value, same field. |
| **3** | **Semantic Redirect** | A value is **silently re-pointed** to a different meaning; the redirect changes what the value *means* without changing the field it lands in. |
| **4** | **Vocab Missing** | The correct term **does not exist** in the vocabulary. Two sub-shapes: **flattening conflation** (many things collapse into one available label) and **misdirected entirely** (the value lands somewhere unrelated because nothing right existed). |
| **5** | **Merge/Split** | A compound: grain issues **and** semantics **and** potentially a new axis, wrapped together. |

**`Case C` — PENDING.** Andrew tagged (1) with it as a pointer to something specific. Not resolved;
**do not invent a referent.**

## Worked instance — the estate-report attribution (measured, 2026-08-05)

The clearest specimen to date, and it shows the errors **stack** rather than occur singly
(full measurement: `S1_attribution_denominator_finding_20260805.md` @ccef4eba5):

- **(1) New Axis, top level** — 243 of 357 changed paths (68%) are governance records, not estate
  resources. The report asserts *a governance record is a resource*.
- **(1) New Axis, again one level down** — `producer:*` is a **runtime-artifact** axis; `area:*` is a
  **filesystem-location** axis. Two axes, one field.
- **(2) Grain Shift, necessarily, once the above holds** — `area:governance` 221 paths / 224 commits
  / 17 authors, beside `yang-factor-tilts` at 1/1/1.
- **(3) Semantic Redirect is the MECHANISM hiding both** — an unresolved path is silently demoted to a
  location label, and a reader cannot distinguish an answer from a fallback.
- **(4) Vocab Missing (flattening)** — the C3.ii verticals exist in `comp-estate` and are absent from
  the attribution vocabulary, so ~99 addressable paths collapse into ~6 labels.

## OPERATIONAL USE (Andrew-approved this session)

**These five are the standard vocabulary for tool-dial findings and cold descents.** Every finding in
a dial record or a P8 descent classifies as one of the five, *before* a remedy is proposed. The value
is not description — it is that **"which error is this?" forces the diagnosis ahead of the fix**, and
the answer determines the remedy: a New Axis error needs a field split; a Vocab Missing error needs a
term; a Grain Shift needs a re-levelling. Reaching for the wrong remedy is the common failure.

## TWO QUESTIONS THE SCHEMA RAISES AGAINST ITSELF — for Andrew

Rule 24 (MECE · same grain · intent coherence) binds any classification schema at authoring time, and
Andrew ratified that triple himself, so it applies here. Testing it honestly surfaces two things:

**Q1 — (5) Merge/Split is not mutually exclusive with (1)(2)(3), by its own definition.** Andrew
described it as *"a mix of grain issues and semantics and potentially new axis all wrapped in one."*
**My reading:** this is fine and should be *declared* rather than fixed — (1)–(4) are **primitives**,
(5) is a **named recurring composite**. Declaring the two tiers preserves MECE at the base layer.
Naming a composite that occurs often enough to deserve its own label is a feature; leaving its status
undeclared is what breaks the schema.

**Q2 — (3) Semantic Redirect may be a MECHANISM rather than a peer error.** In the worked instance it
is not a fourth error alongside the others — it is *how* (1) and (2) stay invisible. If the axis is
"kinds of denominator error," a mechanism sitting beside three error-types is a possible **intent
conflation** — one axis serving two intents, which is the third postulate.
**My reading:** (3) is real and load-bearing and must not be dropped; the question is whether it sits
on the same axis or belongs in a second field (`error-kind` × `concealment-mechanism`). **Andrew's
call, not mine.** Recorded rather than resolved.

-- 3.0.0_SA_CVO
