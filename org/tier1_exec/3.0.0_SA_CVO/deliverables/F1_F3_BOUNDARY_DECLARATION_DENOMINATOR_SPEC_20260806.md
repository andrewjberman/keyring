# F1-F3 BOUNDARY_DECLARATION + DENOMINATOR SPEC — the friction battery's soundness layer

**Owed under** `OPAL_KIMIPIPELINE_STATE_FRICTION_DESIGN.md` §5 and §9 row 4 —
*"Denominator spec per instrument (F1–F3 boundary_declarations) — `3.0.0_SA_CVO` + this seat
(Andrew named the collaboration)"*, **blocked on: nothing, startable now.**
**Status:** DRAFT for `1.0.0_SA_CTO~B` co-sign. **Joint by Andrew's naming — not landed unilaterally.**
**F4 is deliberately out of scope** (§9 row 5: base `1.0.0_SA_CTO`, segment-fit ruling).

## 0. The frame this is written to — and it is not the obvious one

Andrew, at the CTO~B terminal 2026-08-06, on what the battery is FOR — **verbatim**:

> *"the idea is that we effectively use this information from the Friction axes in conjunction with
> the user input data that is already designed, to step by step create an analysis that bridges c3.i
> and c3.ii to identify risk surfaces on the semantic plane."*

**The battery is a RISK-SURFACE DETECTOR, not a change report.** The question each axis answers is
*where is the MEANING of a business function going unreliable* — before it surfaces as a broken
number. F1 is literally the c3.ii → c3.i bridge.

> ⚠ **THIS BINDS `failure_direction` AND CHANGES WHAT THIS DOCUMENT IS.** The field is NOT *"what
> does this figure get wrong."* It is **"what RISK SURFACE does this axis fail to raise, or falsely
> raise."** A denominator spec written against *is the number right* and one written against *would
> this miss an eroding boundary* are different documents. **This is the second one.** (Framing owed
> to `1.0.0_SA_CTO~B`, who supplied it before I wrote the first one and wasted the draft.)

**The four-part form** (§1, ratified): every Friction figure carries `intent_denominator` +
`denominator_grain` + a `boundary_declaration` of
`address_space / traversal_residue / presentation_residue / failure_direction`.

**Battery-layer attachment** (CTO~B's ruling, adopted): instruments stay GENERIC; the BATTERY WRAPS.
`comp-blast`, `comp-heat --json`, `comp-cochange` are consumed as-is. The contract attaches at the
battery layer, the only layer that knows which vertical's paths, which scan scope, what residue.
*(My proving rig violated this by attaching contracts at the instrument layer. Corrected here.)*

---

## F1 — BLAST OVERLAP · the c3.ii → c3.i bridge

**Figure:** which of the 14 c3.i deterministic structures this vertical's in-window change radius
touches, and its breadth against the vertical's own trailing baseline.

```yaml
intent_denominator: "of the vertical's C0 nodes changed in-window, how many resolve into the
                     c3.i structure partition, and how many of the 14 structures are touched"
denominator_grain:  "C0 node, scoped to ONE c3.ii vertical. NOT repo paths, NOT commits."
boundary_declaration:
  address_space:        "the vertical's CHANGED C0 nodes in-window, resolved chain -> c3.i.
                         Explicitly NOT the vertical's full node set: an unchanged node is
                         out of address space, not a zero."
  traversal_residue:    "changed paths that do not resolve to a C0 node -- COUNTED and NAMED,
                         never folded into the touched/untouched split.
                         PLUS the §8.3 case: verticals wholly or partly on UNASSIGNED-RESIDUE
                         (7 today) have NO discovered structure, so F1 is UNCOMPUTABLE for
                         them -- HEAT-ONLY friction with the blindness DECLARED per report."
  presentation_residue: "ZERO BY CONSTRUCTION and asserted as such: the K-of-14 figure is
                         complete because 14 is small enough to enumerate in full. If a
                         display cut is ever introduced this line becomes false and must be
                         rewritten -- it is an assertion about the renderer, not a hope."
  failure_direction:    "MISSES A BOUNDARY ERODING.
                         >> The instrument is BLINDEST EXACTLY WHERE THE RISK IS HIGHEST. <<
                         Erosion means a vertical's footprint spreading into territory it never
                         owned -- and new territory is disproportionately territory the chain
                         does not yet map. So the spreading edge lands in traversal_residue and
                         the breadth figure UNDER-REPORTS precisely as the boundary gives way.
                         A rising residue count with flat breadth is the erosion signature and
                         must be readable as such.
                         FALSE RAISE: a mechanical sweep (rename, lint, header insertion) touches
                         many structures with zero semantic spread. Breadth alone cannot tell a
                         sweep from a real widening."
```

### F1 on day one — three fields, emitted separately

Trailing baselines do not exist on the first run (§3: the daily report IS the persistence layer).
**Emit; never suppress.** Suppressing rebuilds `degraded_sources: []` — a silent absence
indistinguishable from *no blast overlap*.

| field | day-one value | why |
|---|---|---|
| `structures_touched` | `K of 14` | a FACT. True on day one. Needs no baseline. |
| `baseline` | `ABSENT (0 of N days)` | declared, with its denominator |
| `direction` | **`UNCOMPUTABLE`** | **NOT null. NOT omitted. NEVER `STABLE`.** |

> **`direction` IS THE TRAP, NOT THE BREADTH FIGURE.** A null or absent direction reads as *no
> divergence* to the next consumer — **and "no divergence" is a FINDING.** `UNCOMPUTABLE` is the only
> value that cannot be mistaken for a verdict. Same law as `DETECT_FAILED` vs `0 candidates`, one
> field lower. *(Ruling: CTO~B, adopting my emit-lean and correcting the field I was watching.)*

---

## F2 — HEAT TRAJECTORY · is this vertical's attention rising or dying

**Figure:** `comp-heat` recency SCORE distribution over the vertical's paths + day-over-day delta.

```yaml
intent_denominator: "of the vertical's tracked paths, how many were scored, and what is the
                     mean-score delta against the trailing window"
denominator_grain:  "path, scoped to ONE vertical. half_life_days DECLARED ON EVERY FIGURE --
                     a score without its half-life is not a number, it is a number-shaped
                     string (the horizon IS the meaning)."
boundary_declaration:
  address_space:        "the vertical's TRACKED paths as of the vertical join."
  traversal_residue:    "paths in the vertical not scanned -- untracked, gitignored, submodule-
                         interior -- counted. NOTE the asymmetry: untracked work is invisible to
                         F2 and is exactly where new/experimental effort lives, so a vertical
                         can be genuinely hot and read cold."
  presentation_residue: "SCORES ONLY. BANDS EXCLUDED -- Andrew-ruled 2026-08-04 ~2020Z at the
                         CTO~B terminal ('bands are useless for us then, F2 should be
                         scores-only'), on the CH-3 dial finding @1a02a8b3f: bands are fixed
                         7d/30d cutoffs, non-configurable, INDEPENDENT of --half-life.
                         DECLARED, NOT SILENT: the instrument still emits bands and cold_frac;
                         the battery deliberately does not consume them. An undeclared exclusion
                         is indistinguishable from a field that does not exist."
  failure_direction:    "MISSES ABANDONMENT AS READILY AS HEATING.
                         >> A COOLING VERTICAL AND A FINISHED VERTICAL PRODUCE THE IDENTICAL
                         FALLING SCORE. << The score measures write-recency; it cannot see
                         intent. On the risk plane those are opposite states -- one is a
                         function going unmaintained, the other is a function that shipped --
                         and F2 cannot separate them ALONE. Separation requires F3 (did the
                         operator stop talking about it, or declare it done) and the ratified
                         lifecycle_value. F2 MUST NOT be cited alone for a RETIRED/DORMANT
                         shift proposal.
                         FALSE RAISE: bulk/mechanical churn (archive sweeps, mass reformat)
                         lifts scores estate-wide with no change in attention.
                         AND THE HALF-LIFE IS ITSELF A FAILURE MODE: a half-life longer than
                         the phenomenon makes a real trajectory invisible and returns a
                         confident flat line. The declared half_life_days is therefore part of
                         the CLAIM, not part of the configuration."
```

---

## F3 — OPERATOR SIGNAL · is this meaning contested in practice

**Figure:** Andrew's in-window language, classified against a versioned rubric.

> ⛔ **F3 HAS NO DATA SOURCE TODAY.** Its feed is the B6 capture uploader (§5), **NOT BUILT**, owner
> `0.7.0_AE_CloudOps~B`, **no AE seat live** (§9 row 2). The interim store
> (`kimi_svp_f3_interim/`) is partial by construction. **F3 CANNOT BE BUILT AT ALL UNTIL B6 LANDS**
> — and F3 is the axis Andrew named first. This spec is written so it is ready when the feed is,
> and so the gap is a declared blindness rather than a silent zero.

### The rubric FAILS RULE 24 as written — the two-field split

The §8.2 draft enum is `directed | corrective | exploratory | erratic | thrashing`. It fails on
**three** postulates (CTO~B's analysis, adopted in full — I had flagged only the grain mix):

| postulate | failure |
|---|---|
| **(ii) SAME GRAIN** | `directed`/`corrective`/`exploratory` are properties of ONE UTTERANCE. `thrashing` is unambiguously a property of a SEQUENCE. **`erratic` is worse — it is AMBIGUOUS between the two, which is how the mix hides.** |
| **(iii) INTENT COHERENCE** | two questions on one axis: *what is this utterance DOING* vs *what is the PATTERN of this sequence*. |
| **(i) MECE** | an utterance can be DIRECTED **and** part of a THRASHING sequence simultaneously. Not mutually exclusive — so the enum cannot classify it. |

**REMEDY — the two-field split (the pattern Rule 24 names; type specimen RCG charters v1→v2):**

```yaml
utterance_class:  directed | corrective | exploratory     # ONE utterance. MECE.
sequence_pattern: steady | oscillating | thrashing        # a DECLARED WINDOW over a sequence.
```

- **`erratic` does not survive as written.** It was reaching for the sequence question;
  `oscillating` covers it. Dropped rather than relocated.
- **`thrashing` is RELOCATED, never dropped.** Repeated reversal on one vertical is among the
  strongest risk-surface signals in the battery — **it is *the meaning is contested in practice*
  stated in data.** It simply is not an utterance property.

### The declaration

```yaml
intent_denominator: "TWO, one per field, never summed:
                     utterance_class  -- utterances classified of utterances CAPTURED
                     sequence_pattern -- sequences evaluated of sequences CONSTRUCTIBLE
                     (a sequence needs >= N utterances on one vertical in the declared window;
                      verticals below N are NOT 'steady', they are UNEVALUABLE)"
denominator_grain:  "DIFFERENT PER FIELD, which is the whole reason they are two fields:
                     utterance_class  = one utterance
                     sequence_pattern = a declared window over utterances sharing a vertical.
                     Rubric version PINNED on every classification record."
boundary_declaration:
  address_space:        "in-window operator language from CHANNEL 1 ONLY (raw capture store).
                         Channel 2 ratification acts are OUT of address space by the §8.2
                         non-mixing rule -- a ruling's authority travels via its landed canon
                         record, never via the capture store."
  traversal_residue:    "TWO KINDS, and the second is the dangerous one:
                         (a) captured but unclassifiable -- counted, normal.
                         (b) NOT CAPTURED AT ALL -- and pre-B6 THE CAPTURE COVERAGE IS ITSELF
                             UNKNOWN. Andrew types into terminals no capture path reaches.
                             >> F3's denominator is 'of CAPTURED', and the ratio of CAPTURED to
                             SPOKEN IS UNMEASURED AND MAY BE UNMEASURABLE. << That must be
                             declared on every F3 figure, permanently, not only pre-B6. A
                             denominator over a partial universe is honest ONLY if the
                             partiality is stated."
  presentation_residue: "AGGREGATE ONLY -- counts, classes, denominators. NEVER quoted content
                         as authority (§8.2 non-mixing, which prevents the loop eating its own
                         tail). Verbatim may be captured; it may not be cited as warrant."
  failure_direction:    "MISSES A MEANING CONTESTED IN PRACTICE -- the operator repeatedly
                         re-deciding a vertical while every mechanical axis reads calm. F1/F2/F4
                         are all blind to it BY CONSTRUCTION: contested meaning need not move a
                         single file. F3 is the ONLY axis that can raise it, which makes its
                         absence today a REAL HOLE IN THE BATTERY, not a missing nice-to-have.
                         FALSE RAISE, and it is the one to fear:
                         >> F3 CLASSIFIES THE SOVEREIGN'S OWN LANGUAGE. A false `thrashing` is
                         not a wrong number -- it is a claim about Andrew's process, feeding a
                         state proposal about his business. << Exploratory language on a genuinely
                         open question is INDISTINGUISHABLE from oscillation by shape alone; a
                         rubric that cannot tell thinking-in-progress from churn will label the
                         former as the latter. BLAST RADIUS DECLARED BEFORE IT RUNS, not after:
                         sequence_pattern is ADVISORY, is never sole warrant for a lifecycle
                         shift, and its rubric version is pinned so a re-classification under a
                         new rubric is visibly a different claim."
```

---

## Cross-cutting laws (all three axes)

1. **A FAILED INSTRUMENT IS NOT A ZERO.** `INSTRUMENT_FAILED` with its error is a distinct state from
   `rows: 0`. A tool that errored and a tool that found nothing are byte-identical otherwise, and the
   model narrates both with equal confidence. *(Measured live 2026-08-06: three strata reported
   INSTRUMENT_FAILED under a real fault; a starved detect call at a 12,000 ceiling reported
   `candidates_raw: 0` while emitting 0 bytes — the same class one layer up.)*
2. **AN UNCOMPUTABLE DIRECTION IS NOT STABILITY.** Applies to F1 baselines, F2 trajectories, F3
   sequences alike. Emit `UNCOMPUTABLE`; never null, never omitted, never a calm-sounding default.
3. **SILENCE IS NEVER A VERDICT** (§3, already legislated): quiet verticals are listed explicitly as
   NO-SHIFT **with their denominators**.
4. **A DEGRADED UPSTREAM MUST NOT BECOME A CONFIDENT ZERO.** `load_attribution_maps` degrades
   gracefully per hop by design; when its resolver hop failed on 2026-08-06 the canon universe went
   386 → 0 and every downstream call reported a clean-looking zero. **The vertical join depends on
   that same resolver**, so the battery inherits this exposure directly. Every figure declares its
   join health or it is not sound.
5. **THE HALF-LIFE / WINDOW IS PART OF THE CLAIM**, not part of the config — for F2's
   `half_life_days` and F3's sequence window equally.

## Open, and NOT decided here

- **Fan-out unit** — §3 computes F1-F4 per vertical with in-window changes, so DETECT fans out per
  VERTICAL carrying four figures, not per axis. **Confirmation owed from CTO~B**; my proving rig
  currently inverts this axis.
- **Whether the detect/author split survives at all** — §3's flow is R1 narrative → R2 state
  proposal, TWO model layers. The split is MY addition and is not in the ratified design.
- **F4's declaration** — base `1.0.0_SA_CTO`, out of scope here by §9 row 5.
- **`N` for F3's minimum sequence length**, and the sequence window duration. Both need the B6 feed
  to size against real data; setting them now would be inventing a number ahead of the measurement.

-- `3.0.0_SA_CVO`, drafted to `1.0.0_SA_CTO~B` for co-sign
