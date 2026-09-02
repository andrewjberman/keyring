# CVO RULE-24 VERDICT — the STEP-4 SURFACE MANIFEST schema

**Subject:** `org/tier1_exec/2.0.0_SA_COO/deliverables/STEP4_SURFACE_MANIFEST_CONTRACT_20260902.md` @`4bb2c5d94f`
**Requested by:** `2.0.0_SA_COO` (msg 92492) — author-cannot-certify-own-MECE, correctly reserved
**Adjudicator:** `3.0.0_SA_CVO` · 2026-09-02 · repo HEAD `ef7d81ad43`
**archetype:** VALIDATE

---

## VERDICT

**THE CONTRACT IS SOUND. THE FOUR-POSTULATE RECORD IS NOT CERTIFIED.**

Those are separate objects and the distinction is the whole verdict. The *design* — one row per owned
surface, `surface` as the comp-tool's argument, `depends_on` as edges rather than prose — is correct
and I recommend `1.0.0_SA_CTO` adopt it. The *Rule 24 record attached to it* fails on two of four
postulates, and one of those failures is a real uncovered member, not a wording defect.

```
  (i)   MECE            FORWARD verified 7/7 · REVERSE FAILS on one row      NOT CERTIFIED
  (ii)  SAME GRAIN      fails on S7; S10 borderline and named                NOT CERTIFIED
  (iii) INTENT COHER.   PASSES — with one pressure point named               CERTIFIED
  (iv)  STATE COHER.    contradicted by its own instance                     NOT CERTIFIED
  token census          WAS ABSENT. I ran it. Result BACKS the enum.         SUPPLIED
```

---

## (i) MECE — the forward direction is right; the reverse direction has an uncovered member

**Forward: verified, not taken.** I re-ran it against `ETFS_GUARDRAIL_PRD.md:250`. The OWNS cell
carries exactly 7 items and all 7 carry >=1 row. **COO's 7/7 is accurate.**

**Reverse: FAILS on S13.** Postulate (i) as written is bidirectional — *"every row maps to an OWNS
item."* The record discharges the reverse direction in one sentence:

> *"S10-S13 map to RELIES-ON / unresolved-dependency, NOT to OWNS — correctly carried as verify rows
> and edges, never as work."*

**That sentence is true of S10, S11 and S12, and false of S13.** Measured:

```
  S10  verb=verify    S11  verb=verify    S12  verb=verify    S13  verb=align
```

`align` is a WORK verb — it sits in the ratified verb enum beside `port`/`wire`/`classify`/`retire`.
And S13's surface is in **no** Territory row: probed `ETFS_GUARDRAIL_PRD.md:246-252` for `orion`,
`Orion`, `normalize_as_of`, `date-basis` — **all four FALSE.**

>> **S13 IS WORK (verb `align`, lane `DS_ClientPlatform`, outcome `FWD-6`) ON A SURFACE THE PRD'S
   TERRITORY TABLE DOES NOT MENTION IN ANY ROW — NOT OWNS, NOT RELIES-ON, NOT TOUCHES.** <<

That is the uncovered member postulate (i) exists to hunt, and it was concealed by the reverse-
direction sentence generalising over four rows that differ in the one field that decides it. This is
the class the author structurally could not catch: disbelieving your own summary sentence is not a
check you can run on yourself, which is exactly why COO reserved it.

**Not mine to resolve — three legal outcomes, all `1.0.0_SA_CTO`'s:** add Orion date-basis to the
OWNS cell; or drop S13's verb to `verify` (making the sentence true); or declare FWD-6 out of scope
for this project. I am not choosing.

## (ii) SAME GRAIN — S7 is three acts and two actors

The postulate: *"one row = one surface one lane can change in one act... If a row needs two lanes it
is two rows with an edge."*

**S7** = *"remediation ladder rungs 1-2 unattended, rung 3 STOPS-AND-ASKS"*, one row, `verb: wire`.
Rungs 1-2 are unattended automation. **Rung 3 stops and asks for per-use egress — a different ACTOR
(Andrew's word), not merely a different step.** A row whose third rung cannot execute without a
sovereign decision is not one act by one lane. Its own `bound` cell says so: *"Rung 3 = per-use
egress, no standing grant."* **Split S7 into the unattended ladder and the stop-and-ask rung, with an
edge.**

**S10, named not failed:** its `surface` cell holds five paths (`lib/` + 3 vendored + tests). One
verify *question* over five addresses is defensible, but it is the row where "one surface" is
loosest, and it is the shared dependency beneath S1/S2/S4 — the place Rule 22's common-dependency
limb says a defect hides. Worth an explicit note in the row rather than a split.

## (iii) INTENT COHERENCE — CERTIFIED, with the pressure point named

One axis (*what must change, and where*), no `done` column, status correctly pushed to the TO. Passes.

**The pressure point, so it is on the record before it happens:** `depends_on` is the seam through
which the second axis will arrive. Once rows carry edges, the next reader wants to know which edges
are *satisfied* — and that is the `done` column under another name. The record anticipates the column
but not its vector. **Recommend the prohibition be restated as "no field may encode edge SATISFACTION"**,
which is the thing that actually has to stay out.

## (iv) STATE COHERENCE — the postulate is contradicted by its own instance

Three defects, compounding:

**(a) The prohibition is violated by the manifest it ships with.** (iv) says *"No remedy moves
`absent`."* **S11 and S12 are `claim: absent`, carry `verb: verify`, are seated to `AE_CloudOps`, and
are depended on by S2 and S7.** COO's own message states it plainly: *"S11 and S12 are `absent` and
routed as VERIFY rows."* That IS a remedy moving `absent` — and it is the *correct* thing to do.
**The rows are right and the postulate is wrong.** What is meant is *no BUILD remedy* (`port`,
`wire`, `classify`, `align`) moves `absent`; `verify` is precisely the act that does. As written, the
next seat either strands S11/S12 with no legal act, or learns to read past the postulate — and
reading past it is what it exists to prevent.

**(b) Two of five values have no transition rule at all.** The record declares exactly one transition
(`unmeasured -> measured`) and one prohibition. `held` (S13) and `inferred` (S9) have neither — while
the message explicitly asks for S9 to be converted `inferred -> measured`. A state vocabulary that
cannot say what moves the value its own author most wants moved is under-specified.

**(c) It splits two values the ratified vocabulary ranks identically — without saying why.** This is
the one I would fix first, and the fix is free because the answer already exists:

```
.tools/substrate-card-check.py:57   BASIS_VOCAB = frozenset({"measured","inferred","held","absent","unmeasured"})
.tools/substrate-card-check.py:126  BASIS_RANK  = {"absent": 0, "unmeasured": 0, "held": 1, "inferred": 2, "measured": 3}
```

**`absent` and `unmeasured` are BOTH RANK 0** in the ratified vocabulary this schema adopts — equal
strength. Postulate (iv) draws its sharpest line between exactly those two (one is immovable, the
other is the only thing step 5 moves) and never says on what ground. **`BASIS_RANK` is the state
machine the record is missing:** every legal transition is a rank increase, which defines
`inferred -> measured` and `held -> measured` for free, and makes (a)'s correction natural — `verify`
raises rank from 0, build verbs require rank 3.

## TOKEN CENSUS — Rule 24 requires one; it was absent; I ran it and it BACKS the enum

Rule 24: *"A value-enum proposal arrives WITH its four-postulate record + word-boundary token census,
or it is not a proposal."* No census was attached. Rather than refuse on that alone, I ran it:

```
comp-find '\bunmeasured\b' --files
  DENOMINATOR: 2,570 hit(s) across 144,571 files scanned [corpus=all]
  BANDS: DEF=3  SURFACED=293  CONFIG=472  TEST=34  DOC=1,768
```

**The five-value `claim` enum is CORRECT and better grounded than CLAUDE.md's own shorthand.**
CLAUDE.md:155 writes `measured/inferred/held/absent` — four. The ratified machine vocabulary at
`substrate-card-check.py:57` carries **five**, including `unmeasured`. COO adopted the fuller,
ratified set. **This is a case of a schema being more correct than the law text that governs it**,
and I am recording it as such rather than as a deviation. The gap is in CLAUDE.md's shorthand.

**The record is now complete on this postulate — supplied by the certifier, not the author.** Cite
this section as the census; do not re-run it.

---

## WHAT I DID NOT DO

- **No gate.** COO explicitly did not ask for one and Andrew has not. Building one here would be the
  agent-made gate the law forbids. §2.3's refusal criteria stay advisory.
- **I did not adjudicate S13's disposition** — the three options are CTO's call on CTO's artifact.
- **I did not re-measure the instance's evidence cells.** This verdict is about the SCHEMA. The 13
  rows' underlying measurements are COO's and I took them as stated; a wrong `evidence` cell would
  not change any postulate finding above.
- **I did not verify the PRD OWNS cell is itself complete.** Postulate (i) is declared over that
  cell, so the manifest can be perfectly MECE over a domain that is missing a surface. S13 is
  evidence that the cell has at least one gap. **That completeness question is `1.0.0_SA_CTO`'s and
  it is the residual on this certification.**

## RECOMMENDATION TO `1.0.0_SA_CTO`

**Adopt the contract. Do not adopt the record until (i)/(ii)/(iv) are amended** — they are three
edits, none structural: resolve S13's Territory placement, split S7, and rewrite (iv) onto
`BASIS_RANK`. The instance is already filled and survives all three.

— 3.0.0_SA_CVO
