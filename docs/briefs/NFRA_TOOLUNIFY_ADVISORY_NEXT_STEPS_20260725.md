<!-- 1.0.0_SA_CTO~Z · 2026-07-25 · feedback + advisory answering the 6 open questions in NFRA_TOOLUNIFY_STATUS_FOR_REVIEW_20260725.md -->

# NFRA_TOOLUNIFY — Feedback & Advisory: Next Steps

**Author:** `1.0.0_SA_CTO~Z` · **Date:** 2026-07-25 · **Audience:** internal (Andrew + build lane) — the
answer-side of the outward-facing [`NFRA_TOOLUNIFY_STATUS_FOR_REVIEW_20260725.md`](NFRA_TOOLUNIFY_STATUS_FOR_REVIEW_20260725.md).
**Grounding:** census closed + CVO~Z-verified; REC-1 predicate-exercise **DELIVERED + verified, closed**
(`REC1_EXERCISE.md`, 5/92 v1 sample, both acceptance anchors held). This doc is placed ADJACENT to the
external status doc, not over it — that one is colleague-facing and deliberately omits internal detail;
this is the internal ruling-side. Say the word to merge.

---

## 0. Where we actually are (grounded, not remembered)

Two facts drive everything below, and both are settled, not in-flight:

1. **The register is built and the exercise method is proven.** WS-1/WS-2 shipped (92 rows, zero UNKNOWN
   in binding/eval/failure_mode). REC-1 then did the thing that mattered most: it **exercised** the
   `failure_mode` column instead of trusting the AST-derived value — and the headline case
   (`comp-stitch-refresh`'s only consumer discards its exit-2 alarm and always reports success) proves the
   census's silent-controls finding *by direct exercise, one layer down.* That is the domain census and
   the first predicate-side probe, both landed.
2. **The census produced a program, not a cleanup list.** Six independent instances of *a correct
   instrument whose verdict reaches no one*, plus a 93%-undeclared graph vocabulary. Those are not
   consolidation details; they are the two most valuable things the audit surfaced.

Everything that follows is a ruling on the six open questions, in the doc's order.

---

## 1. Q1 — Scope: "tool consolidation" or "silent controls" as the primary program?

**Ruling: neither reframes, and do not rename reactively. Consolidation is the DELIVERABLE; silent
controls is the DISCOVERY; they share one denominator and stay one project.**

The silent-controls finding is genuinely the more valuable output — and it is not a coincidence, it is a
*named class*: **a control that runs and produces a correct verdict that never reaches a consumer is
predicate-blindness at estate scale** — the same class as the SYSPARITY parity check that read 100% while
blind. But renaming the project to chase the shinier finding would (a) undersell the consolidation payload
Andrew explicitly asked for ("unified set, clear denominators, clear coverage disclaimers"), and (b) split
one denominator into two, which is the exact anti-pattern this program exists to close.

**What to do instead:** keep NFRA_TOOLUNIFY as the container; make **"controls that do not reach the
runtime" a named, first-class WORKSTREAM within it** (call it the *reachability* workstream), with its own
denominator and its own gate. The consolidation and the reachability findings are the same audit seen from
two sides — the register tells you *what a tool reads*; the exercise tells you *whether its verdict lands*.
One project, two lenses, one denominator.

---

## 2. Q2 — How far to take "exercise, don't infer"?

**Ruling: not "sample vs sweep" — RANK by consumer-criticality and exercise the critical tier
exhaustively, sample the rest. The v1 result already tells you where the line is.**

The register carries `role_flags[]` (GATE-BLOCKING / PRODUCER / ADVISORY / TEST). Use it:

- A `SILENT-EMPTY` on an **ADVISORY** tool is cosmetic — a human reads the prose, no automated consumer is
  fooled. Sample these.
- A `SILENT-EMPTY` or a swallowed-`LOUD` on a **GATE-BLOCKING** or **PRODUCER** tool is the catastrophic
  class — precisely the `comp-stitch-refresh` case REC-1 found. **Exercise every one of these.**

So the exhaustiveness question resolves to a *filter*, not a *volume*: exercise the gate-blocking +
producer tier exhaustively (that is a small subset of 92, and it is where the harm lives), and sample
advisory/test. That is defensible, bounded, and it puts the spend exactly where a false verdict costs
something. **Do not run all 92 exhaustively** — it spends manual-inspection-depth effort on tools whose
worst failure mode is a human squinting at prose.

*One control carries forward from REC-1:* the six through-line instances are the positive-control set —
if a widened exerciser cannot re-find those six, the exerciser is broken, not the estate.

---

## 3. Q3 — The 86.5%-undeclared graph vocabulary: author it, or leave it outside by design?

**Ruling: author vocabulary ONLY where the undeclared node participates in a JOIN or a CONTROL. Everything
else gets a DECLARED "outside-ontology-by-design" label with its own denominator — never forced into the
41-class vocab, and never left silently undeclared either.**

This is the two-plane ruling made concrete. The 86.5% is the code-level + M365 plane; it is real, it is
large, and most of it has no AWS existence to crosswalk to. Authoring 41-class vocabulary for 17,000
code/M365 nodes speculatively would be inventing a schema for a population nobody queries — the inverse
waste of leaving it undeclared.

The discriminator is materiality, and materiality is *not* an agent's guess — it is: **does anything join
to it, or does any control depend on it?**
- **6.8% naming-mismatch** → cheap, do it: an alias table, one mutant per alias. This is Class-1 pure.
- **The join entities** (Lambda, S3 key, Component, Endpoint — the four that exist in both planes) → author
  the crosswalk with a conformance suite, per WS-4. This is where the vocabulary *earns* extension.
- **The rest of the 86.5%** → a single declared record: *"this plane is modeled as node properties, not
  as first-class ontology types, by design; denominator = N; it is not a coverage defect, it is a scope
  boundary."* That sentence is the coverage disclaimer Andrew asked for, applied to the graph itself.

**Do not commit to authoring the whole 86.5%.** Route it through materiality: extend where something
depends on it, declare-and-bound the rest. Undeclared-and-silent is the defect; undeclared-and-*declared*
is a legitimate scope boundary.

---

## 4. Q4 — Formalize a PRD now, or keep iterating?

**Ruling: PRD the FRAME now; keep the IMPLEMENTATION iterating. Write the constitution, not the details.**

What is settled enough to lock, and *should* be locked because a PRD is what makes the denominator visible:
- the two-plane ruling (source + deployed, joined by a tested crosswalk — not "one graph");
- the reachability workstream as a first-class scope (Q1);
- the exercise-don't-infer method and its criticality-ranked scope (Q2);
- the persistence gate (WS-7) as the exit mechanism;
- the coverage-disclaimer standard (a tool with a SILENT vintage or an unprintable denominator fails).

What is NOT settled and must stay out of the PRD: which specific tools get re-pointed, which vocabulary
gets authored, the order of the repairs. PRD those and you freeze decisions the census is still feeding.

**The rule this follows:** *canonization is not complete until the denominator can see it.* A PRD that
locks the frame makes the whole program a declared denominator; a PRD that locks the details freezes a
moving target. Do the first now.

---

## 5. Q5 — The silent-controls findings: fix now, or wait for the design phase?

**Ruling: SPLIT by reversibility. Make silent things LOUD now (cheap, reversible, stops daily harm); DEFER
the substantive producer repairs until the shape is settled.**

Two different actions are being bundled as one question:

- **Visibility / alerting (do NOW):** the 83-night-silent pipeline and the 476-message un-alerted queue are
  accruing harm *every day* precisely because they are silent. Making them **loud** — wire the missing SNS
  subscription, make the health check's failure reach a human — is cheap, reversible, and it converts an
  invisible failure into a visible one without touching the thing that is failing. There is no reason to
  wait, and waiting is itself the harm.
- **Substantive repair (DEFER):** *fixing the producer* is a different act and the census already warned
  against rushing it — `comp-stitch-refresh` needs a **working producer to exist**, not merely "finish the
  retirement," and its `EXTERNAL_ENDPOINT=0` must be investigated in parallel with the baseline **not
  recalibrated over the unresolved zero** (recalibrating bakes the defect in and blinds the sentinel). That
  is design-phase work; picking at it now risks laundering a broken state as fixed.
- **The two path bugs (FIX NOW):** the hardcoded-path hook failure (4/4 sessions) blinds the census
  instrument *itself* and is mechanical. Fix it — a broken measurement instrument corrupts everything
  downstream, and it is the cheapest high-leverage fix on the board.

**One-line policy:** loud-not-fixed is always safe and often urgent; fixed-but-unsettled is neither. Make
everything loud now; repair on the design phase's schedule.

---

## 6. Q6 — Sequencing against the larger effort; what is "done enough"?

**Ruling: the larger effort is TOOLUNIFY's own L3 phase, not a separate project — and "done enough" has a
concrete, definable exit bar. Define it now.**

The "more ambitious self-improving version" is GRAPHLEARNS, and per the level analysis it is the **growth
phase of this same program** (it absorbed the CANON/CANON2 lineage; it grows the crosswalk this census
produces). Standing it up as a separate project would re-split the denominator. Keep it as the successor
phase under the same lanes and the same verification.

**The exit bar — two mechanical conditions, both checkable, define "done enough":**
1. **The crosswalk conformance suite exists and passes** (WS-4): source ↔ deployed join at the four shared
   entities, one mutant per settled mapping. *Reason:* the growth phase grows the crosswalk; you cannot
   grow onto a schema whose own grain is unsettled.
2. **The register is a control** (WS-7): a new/renamed tool cannot land unregistered, a new floating
   artifact cannot land unwatched — demonstrated by exercise (a deliberately unregistered tool is
   *rejected*), not asserted. *Reason:* the growth phase will add tools; if the register is maintained by
   care rather than a gate, it decays exactly like the artifacts this project is about.

When those two are green, the larger effort may start. Not before — and the bar is definable *now* because
both conditions are mechanical, not judgment calls. **Do not leave "done enough" to a later feel.**

---

## 7. The forward sequence (one page)

```
NOW (parallel, all grounded + ready):
  A. VISIBILITY fixes -- wire the missing SNS sub, make the 83-night pipeline's failure LOUD,
     fix the hardcoded hook-path bug (blinds the census instrument itself). Reversible, urgent.
  B. WIDEN REC-1 by CRITICALITY -- exercise the GATE-BLOCKING + PRODUCER tier exhaustively;
     sample advisory/test. Positive control = the 6 through-line instances.
  C. WS-4 crosswalk build -- source+deployed, 4 shared entities, per-mapping mutant. Inputs exist.
  D. PRD the FRAME (Q4) -- two-plane ruling, reachability workstream, exercise method, gate, disclaimers.
     NOT the implementation details.

THEN:
  E. Vocabulary: alias table for the 6.8% mismatch; DECLARE-and-bound the 86.5% as scope boundary;
     author only where a join/control depends on it.
  F. WS-5 substantive repair -- stitch (working producer required; do NOT recalibrate over the zero),
     comp-iam self-producer role_flag, comp-residue registration (still behind the self-route gate,
     NFRA_TOOLARCH.GATEBOUND).
  G. WS-6 packaging + coverage disclaimers (the consolidation payload Andrew asked for).
  H. WS-7 register-as-control -- the persistence gate. THIS + WS-4 = the exit bar for the larger effort.

THEN (gated on WS-4 + WS-7 green):
  I. GRAPHLEARNS -- the L3 growth phase, same lanes, same verification. Not a new project code.

INDEPENDENT of all of the above (currency axis, not coverage):
  the version-pin remedy, NFRA_SYSPARITY.DENOM.
```

---

## 8. The one framing to hold

The census set out to consolidate tools and instead proved the program's own thesis on live estate: **the
domain side (what a tool reads, what the graph covers) can be built and mostly is; the predicate side (does
a correct verdict actually reach anyone) is where the real, invisible failures live, and it is only ever
found by EXERCISE, never by reading.** REC-1 demonstrated that in one case by direct probe. The next moves
are: make the silent things loud (now), exercise the critical tier (now), and lock the frame in a PRD (now)
— then grow. One project, one denominator, cleanup and vision unified.

**Related:** [`NFRA_TOOLUNIFY_STATUS_FOR_REVIEW_20260725.md`](NFRA_TOOLUNIFY_STATUS_FOR_REVIEW_20260725.md)
(the questions) · `org/tier1_exec/1.0.0_SA_CTO/deliverables/NFRA_TOOLUNIFY_CENSUS/CONSOLIDATED_ESTATE_MAP.md`
(the audit) · `REC1_EXERCISE.md` (the predicate-exercise) ·
`infra/system/ontology/IMPLEMENTATION_LEVELS_AND_SEQUENCING.md` (the level stack this maps onto).

---

## 9. Review before merge (`1.0.0_SA_CTO~Z`, this session) — HOLD on one item

Found this doc untracked/uncommitted on disk; did not author it this session, so reviewing rather than
adopting wholesale — same discipline as grading the pre-crash fork's REC-proposal.

**Q1, Q3, Q4, Q5 — sound, grounded, no conflict with anything on the record. Adopting.**

**Q2 — mechanism spot-checked against the live register, holds.** `grep role_flags D.md` confirms
`GATE-BLOCKING`, `PRODUCER`, `TEST` are real values in the shipped 92-row register (not invented). The
criticality-ranked exercise plan is buildable as described.

**Q6 — HOLDING, does not get executed as written.** This ruling ("the larger effort is TOOLUNIFY's own L3
phase... not a new project code... GRAPHLEARNS — same lanes, not a new project code") is exactly REC-2 from
the pre-crash fork review, which I explicitly declined to affirm — because it reverses Andrew's own
verbatim ruling: *"This is a separate project than GRAPHLEARNS and ARCHTOOL, we will return to those
later."* Andrew's most recent word on sequencing (this session, recorded in `CONSOLIDATED_ESTATE_MAP.md`
§8) keeps them **separate but sequenced** — COMPLEARNS starts *after* TOOLUNIFY, not *as* TOOLUNIFY's WS-8/L3.
A colleague-advisory, however well-reasoned, is not the authority that reverses a sovereign ruling — that's
Andrew's call, surfaced not adjudicated, same as before.

**Practical effect:** §7's steps A/E/F/G/H (visibility fixes, vocabulary, WS-5/6/7) don't depend on Q6 and
are fine to sequence as internal TOOLUNIFY work once explicitly greenlit. **Step I (GRAPHLEARNS as L3) does
depend on Q6 and is NOT authorized by this doc alone.** Also holding B/C/D (widen REC-1, start WS-4, PRD the
frame) at their CURRENT scope — Andrew's explicit instruction this session was "start with REC1," and I've
been treating that as the active scope boundary; this advisory recommending a wider parallel push doesn't
by itself widen Andrew's own authorization. Flagging both back to him rather than self-authorizing.
