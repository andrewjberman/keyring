# CVO~C REVIEW — SCRIPT I/O ONTOLOGY SPEC (the S-layer)

**Reviewer:** `3.0.0_SA_CVO~C` (Andrew-named)
**Artifact:** `org/tier1_exec/4.0.0_SA_CRO/deliverables/SCRIPT_IO_ONTOLOGY_SPEC_20260806.md`
**Vintages read:** REV 1 `@72279a7c2` (488 ln) · REV 2 `@785ed481f` (576 ln)
**Date:** 2026-08-07
**Author of artifact:** `4.0.0_SA_CRO` · **Parallel arch read:** `1.0.0_SA_CTO~D` `@56edc2738`

**THIS IS NOT A GATE.** No approval step, hold, or co-sign is proposed or implied. Per Andrew-direct
2026-08-06 that is not mine to create. Findings are findings; the driver drives.

---

## VERDICT IN ONE PARAGRAPH

The layer is worth building and the central claim of §1 holds: **the estate has line-level knowledge
and no line-level ontology.** That survives everything below. But the **axis-independence claim in §4
FAILS** — not on the pair CRO nominated, on a different one, by three independently-derived routes —
and **S0 is not net-new**: the site primitive it specifies is already landed, wired, and fail-closed
validated in `comp_recognizer_sdk.py`. Both are structural. Both are cheap to fix *now* and expensive
after a naming act. Everything else is P1/P2 and none of it threatens the layer's existence.

**Two P0, three P1, two P2 — plus one P1 RETRACTED (P1-5, refuted by `1.0.0_SA_CTO~D`; I was wrong,
the second "SDK" is a re-export and the retraction is written into that section rather than deleted).**
The ranking is real — if it were all P0 I would have failed at ranking.

---

## P0-1 — AXIS INDEPENDENCE FAILS. Axis 3 (`resolution`) is not a peer axis; it is a META-axis.

**Verdict on the claim as stated in §4/§4.1: FALSIFIED.**

CRO nominated direction×identity as the suspect pair and told me it was the weaker test because he
chose it. He was right about that. I tested all ten pairs. The break is at **3×{1,2,5}**.

**Leg A — `opaque` nullifies three other axes (my derivation, from the spec's own value table).**
Axis 3's `opaque` is defined `@785ed481f` §4 as *"call not in the recognizer set at all."* If the call
was never recognized, then **`direction`, `grain`, and `identity` are not merely unknown — they are
unassertable.** You cannot know a site is `ingress` rather than `egress`, at `field` rather than
`artifact` grain, if you did not recognize the call. Only Axis 4 (`condition`) survives, because it is
computed from syntactic nesting rather than from recognition. **An axis whose extreme value voids the
assertability of three others is not orthogonal to them — it qualifies them.**

**Leg B — the front-end capability bound (CRO's own, handed to me mid-review).** A site cannot be
`folded` if the front-end tier serving it cannot resolve across files. Verified at source: the tier
enum is real and ordered — `RAW_TEXT=0 / LEXICAL_AST=1 / RESOLVED_SEMANTIC=2`
(`org/modules/graph/comp_recognizer_sdk.py:66-69` @HEAD `72279a7c27`), and dispatch is gated on
`tree.capability >= recognizer.requires` (`:64-65`). So Axis 3's achievable values are a function of
`(site, extractor)`, not of the site.

**Leg C — the estate already models this, at the right grain, and it is landed.**
`comp_recognizer_sdk.py:84-90` defines `Coverage{attempted, resolved, unresolved:[(locus, reason)]}`,
described in its own header comment as *"the no-silent-Unknown channel ... so a weak recognizer cannot
silently under-report while the parity gate passes."* **That is Axis 3's entire stated purpose**
(§4 Axis 3: *"the anti-fabrication axis ... SILENCE IS THE DEFECT"*) — already built, already
fail-closed, and carried at **run/recognizer grain with a per-locus reason**, not as a peer attribute
on a site record.

**Why three legs and not one:** they do not share a derivation. Leg A is from the spec's own text, Leg
B from the extractor's type system, Leg C from a landed dataclass. A tie between instruments that
share a derivation is one observation counted three times; these do not, so the convergence is
evidence.

**Consequence, and it is the Rule 24 one:** Axis 3 answers *"how much do you trust the other axes?"*
while Axes 1/2/5 answer *"what is the value?"* Those are two intents on one plane —
**Rule 24 (iii) INTENT COHERENCE**, the RCG charter-v1 defect the taxonomy law cites as its own type
specimen. It also fails **Rule 24 (iv) STATE COHERENCE**: improving the recognizer set moves every
Axis-3 value together, and moves **no** Axis-1 value at all. One remedy does not move the axis set
together, which is exactly the stability-frame test.

**RECOMMENDED SHAPE (not drafted — CRO's to author):** demote `resolution` from an axis to a
**per-binding confidence qualifier** carried alongside the four axes, whose non-`literal` values
explicitly mark which other axes are unasserted; and bind it to the existing `Coverage` channel rather
than re-implementing it. Four orthogonal axes plus a declared confidence qualifier is a stronger
schema than five axes one of which is secretly about the other four.

---

## P0-2 — S0 IS NOT NET-NEW. The site primitive is landed, wired, and validated.

**§3.3 specifies S0 as a new record. It already exists.**

`org/modules/graph/comp_recognizer_sdk.py:76-81` (31,832 bytes, landed 2026-07-07):

```
@dataclass
class Site:
    source: str      # repo-relative file
    locus: str       # "L{n}" or "L{a}-{b}"      <- covers §3.3's line AND end_line
    evidence: str    # the LITERAL bytes at that locus (comp_ladder C0 style)
    payload: dict
```

Header comment `:73`: *"Site -- one located lexical match a recognizer found; carries the file:line
provenance the CSE needs."* It is imported by **6 modules**
(`comp_recognizers_{code,config,ticket,tsx}.py`, `comp_promote_materializer.py`, plus the SDK's own
self-test) — a printed denominator, not an impression.

**And it already aggregates upward.** `emit_cse(verb, subject, edges, provenance, ...)` at `:162-186`
emits CSE **C0+C1** with a deterministic `event_id` hashed from provenance (`:168-169`) and
`validate_or_raise` fail-closed on provenance-less CSE (`:186`). `comp_recognizers_code.py:3` states it
plainly: *"each recognizer emits CSE C0+C1 with file:line provenance."*

**This falsifies two of the four limbs of §2.1.** That section asserts of the existing surfaces:
*"None of them shares a record ... none is addressable from a C-ladder or D-rail query."* For the
COMPILERKIT surface **both are false** — `comp_recognizer_sdk` **is** the shared record, and CSE C0+C1
**is** C-ladder addressability. The other two limbs (*"no two can be joined"*, *"none is registered in
SYSTEM_DEFINITIONS.yaml"*) still stand, and the §1 claim stands with them.

**This is the same defect CRO just corrected in §6, one level deeper.** He fixed *"build new language
adapters"* → *"recognizers on the existing SDK"* (BUILD LADDER rung 2). §3.3 still says *build a new
site record*. The correction has not reached it.

> **ADDENDUM — S0 AND S1 ARE IN TWO DIFFERENT STATES, AND THE NAMING ACT SHOULD SAY SO.**
> `1.0.0_SA_CTO~D` verified this finding at their own seat before letting it anchor a naming act, and
> found a half neither of us had stated. **Their finding, re-derived at mine with a positive control
> run first:**
>
> | sweep (`org/modules/graph` + `infra/system/sdk`) | count |
> |---|---|
> | `class Site` — **positive control, must be ≥1 or the sweep is broken** | **2** |
> | `class Binding` / `class Bindings` | **0** |
> | landed object carrying all five S1 axes | **0** (`resolution` 0, `identity` 0) |
> | nearest landed edge object — `RelationshipDelta`, `cse_schema.py:208` | a CSE relationship, **not** an intra-node binding; carries none of the five axes |
> | `vintage`/`commit`/`sha` in the `Site` span | **0** (control: `locus` hits 2 in the same span) |
>
> **So S0 is a landed dataclass needing ONE ADDITIVE FIELD; S1 is a GREENFIELD BUILD.** That is
> **Rule 24 postulate (iv) STATE COHERENCE**, whose own instruction is to **name which values do not
> move**: one remedy delivers S0 and structurally cannot deliver S1.
>
> **This strengthens the finding rather than qualifying it** — the reason S0 is well-founded is exactly
> the reason S1 is not yet. **It is not a blocker and does not change the tokens or the ordering**; it
> changes what Andrew is told the naming act COSTS. Naming both is still available — `forward: true` is
> the bank's ratified way to carry a declared-but-unpopulated half, which is what S1 would be.

**What is genuinely net-new, after this:** the **five axes**, the **field grain**, and **`vintage`** —
which `Site` does **not** carry (grep for `vintage|sha|commit` returns the provenance uplift at `:142`
noting compiler #1's Node has `file_path+sha` but **no line**; the Site itself carries no commit-ish).
So §3.3's insistence that *"an S0 record without `vintage` is malformed, not merely incomplete"* is
**correct, and lands as a one-field additive amendment to a live dataclass** rather than a new
primitive. That is a much cheaper and much stronger version of the same point.

---

## P1-3 — AXIS 1 FAILS ITS OWN STATED INTENT TEST. Two of six values, three range types.

§4 sets the test itself: *"Each axis below states its intent in one line. If a proposed value does not
answer that question, it belongs on a different axis."* Axis 1's intent is
***"what does this site do to the VALUE?"***

- `control` is defined *"invokes/triggers another node, **carries no payload**."* It does nothing to a
  value; there is no value.
- `guard` is defined *"site gates whether another site executes."* It acts on **execution**, not on a
  value.

By the axis's own test, both belong elsewhere. The deeper form is that Axis 1 mixes **three range
types** on one axis — `ingress`/`egress`/`roundtrip` relate a site to an **external target**, `derive`
relates it to an **in-node value**, `control` to a **node**, `guard` to **another site**. That is
Rule 24 (ii) SAME GRAIN.

**It also propagates as totality holes.** `direction=control` has no `grain` and no `identity` (there
is no value to be grained or named), so the five-axis cross-product contains **structurally empty
cells**. Those must be **declared in the schema**, not discovered by the first consumer that reads a
null as "artifact grain."

This subsumes CRO's §9.3 (*"does `guard` belong on DIRECTION at all?"*) — the answer is no, and
`control` has the same problem, which §9.3 does not ask about.

---

## P1-4 — `roundtrip` DECOMPOSES. Its own cited precedent argues against it when read at source.

**CRO's evidence, read at the source rather than at the citation:**
`org/modules/graph/extract_pipeline.py:51-53`, verbatim:

```
# FUNC keys that appear in both reads and writes: likely rolling-window prior-run reads.
# Removed from read_keys/reads to avoid false circular-dep edges; surfaced as warnings.
rolling_window_candidates: list[str] = field(default_factory=list)
```

Three grain mismatches from a single site-level binding, all in two lines of comment:

1. **`prior-run`** — the read is of the **previous run's** output. That is a **temporal** dependency
   (read at t−1, write at t), not one site doing two things.
2. **`keys ... in both reads and writes`** — the match is computed over **artifact-key sets aggregated
   across an entire script**, never at a line.
3. It is a **suppression** (`Removed from ... to avoid false circular-dep edges`) — a de-duplication
   applied *because* two genuinely distinct sites collided at key grain.

**So the precedent establishes that the phenomenon is real and worth naming. It does not establish a
site-level primitive — it is positive evidence for the opposite.**

The definition confirms it independently: §4 Axis 1 defines `roundtrip` as *"same target both read and
written at **one site or one loop**."* **"One loop" is definitionally two sites.** S0 is per-site and
S1 is site→target, so a one-loop roundtrip **cannot be a single S1 binding**. The value places a
site-grain fact and a multi-site fact on one axis — Rule 24 (ii) again.

**This is the outcome CRO named as the worst available: naming it would ratify an aggregation artifact
as an ontological category.** Recommended home: a **derived finding over a set of bindings** — the R4
shape the spec already has — not an Axis-1 value.

---

## ~~P1-5 — THERE ARE **TWO** RECOGNIZER SDKs~~ — **RETRACTED 2026-08-07. I WAS WRONG.**

**RETRACTED IN FULL.** `1.0.0_SA_CTO~D` refuted this and they are right. `gensdk/recognizer_sdk` is a
**RE-EXPORT of `comp_recognizer_sdk`, not a second SDK.** Verified at source myself before accepting:

- `infra/system/sdk/gensdk/recognizer_sdk/__init__.py:18-19` — *"The engine lives with the other
  comp-tools (exec-locked; **imported, never forked**)"*; `:28-29` `from comp_recognizer_sdk import *`
  with `__all__ = list(_ENGINE_ALL)`.
- **Discriminating count:** `class FrontEndCapability` is defined **exactly once estate-wide** —
  `org/modules/graph/comp_recognizer_sdk.py:66`. Zero definitions in gensdk.

**So the enums are not "byte-identical" — they are THE SAME OBJECT, imported, and cannot drift by
construction.** There is no "which SDK" architecture call; there is one exec-locked ENGINE plus one
tenant AUTHORING SURFACE. My claim that *"gensdk has the richer front-end lineup and none of that"* was
false on its second half: gensdk gets `Site`, `Coverage` and `emit_cse` through the star-import. This is
not a BUILD LADDER rung-2 duplication — **it is that rule being obeyed, in writing.** REV 2 is not
under-determined and CRO should not restructure §6 around a fork that does not exist.

> **HOW I GOT IT WRONG, because the method matters more than the finding.** I compared **symbol
> tables** — same three tier names, same ordering, shared `EnrichedTree` — and concluded *fork*. **A
> symbol-table comparison cannot distinguish a fork from a re-export: both produce identical symbols.**
> That is an instrument that could not have said otherwise, which is the exact failure class I applied
> to CRO's spec in P0-1 and did not apply to my own check. The disambiguating evidence was in a
> **docstring**, not the symbol table. Caught by CTO~D, `@fff88d612`.

**WHAT SURVIVES, narrowly:** the front-end *implementations* (`python_ast.py`, `python_resolved.py`,
`raw_text.py`, `tree_sitter_stub.py`) do live under `gensdk/frontends/` while the engine lives in
`org/modules/graph/` — so "where do S-layer front-ends go" is still a placement question, just not a
*which-SDK* one. And §10.5's resolved-tier passability remains open — **one** open question, not two.
Neither CTO~D nor I has exercised it; both reads are DESIRED-plane.

---

## P1-6 — THE FENCE: the obligation CRO did not quote, and why I declined his method.

**On the method first, because it matters more than the finding.** CRO asked me to hunt for an
"ADVI-shaped fingerprint" in the design, calling it the highest-value finding available. **I declined
that method, and the fence itself is why.** `NFRA_ONTOLOGY_RULE_BANK.yaml:275-277`:

> `verifiable_without_breaching:` *"A FENCE MUST BE VERIFIABLE WITHOUT READING THE FENCED SURFACE. A
> fence whose enforcement requires the enforcer to breach it is not a fence (3.0.0_SA_CVO~Z, Amendment
> 1 corollary). **Check a declared shaping corpus against a schema, never against ADVI_PERFORMANCE or
> MDPF_GLOBAL.**"*

To recognize an ADVI fingerprint I would have to know what ADVI looks like. **The review target as
phrased invites the reviewer to breach the fence in order to check it** — and the fence anticipated
exactly that and prescribed the alternative. I used the prescribed method.

**The prescribed method returns a finding.** `:271-274`:

> `obligation_on_every_author:` *"**PUBLISH YOUR SHAPING CORPUS** — the denominator you drew from — so
> a later reader can verify the two held-out projects are absent. **AN UNNAMED SHAPING CORPUS IS
> INDISTINGUISHABLE FROM A BREACHED ONE.** This is not a courtesy; it is the only way the fence is
> CHECKABLE by anyone other than the author it binds."*

**REV 1 §11 declared the corpus unbounded** (*"the denominator of tools I did not examine is not zero
and I have not bounded it"*). Under the clause above, an unbounded corpus **does not discharge the
obligation** — so REV 1's §8.1 fence-compliance claim was unverifiable *by the fence's own standard*,
and REV 2's census correction is therefore **not only a census fix, it is a partial fence discharge.**
CRO filed these as two separate targets (#3 and #4). **They are one finding.**

**What is still open, and it is cheap:** REV 2 bounded the tool census, but the *shaping corpus* is a
different set — it includes the live graph figures (`Field 4969`, `FLOWS_TO 961`, `PROP_PASSES 1382`,
`RENDERS 2447`), which are **estate-wide counts from a graph that contains ADVI**. I do **not** call
that a breach: those are aggregates, not surfaces-as-vocabulary-examples, and the rule bank's own
`graph_evidence` uses the same estate-wide census — the fence's authors already treat that as
compliant. **The remedy is to state the corpus positively** — "exactly these N files at these
vintages, plus the estate-wide comp-kuzu census @2026-07-23T14:52Z" — which is checkable, rather than
"seven that I found" plus a residue.

**Separation that matters:** §8.1's three-readings conflict (does the fence bind the S-layer at all?)
is **Andrew's** and CRO is right not to adjudicate it. The corpus-publication obligation is **not**
Andrew's — it binds every rail author, CRO can discharge it himself today, and it should not wait
behind the sovereign question. He bundled them; they separate cleanly.

**Verified accurate in §8.1, for the record:** the fence quote, the `why_it_is_the_most_dangerous_item`
no-failure-channel text (`:266-270`), and the ADVI_PERFORMANCE/MDPF_GLOBAL naming are all verbatim
correct at `:261-279`.

---

## P2-7 — THE `S` TOKEN. Collision confirmed and wider than flagged; **not fatal to the letter.**

CRO's `.owned-paths.yaml:745` citation is **verified verbatim** (*"DS placed S0 (heat_map.py) + O1
(object_freshness.py) here"*). CTO~D independently found more, and my own sweep hit one of his
before I read his message: `org/modules/graph/comp-coverage-map.yaml:3,12,21-25,36` uses **both**
`S0` and `S1` as NFRA_COMPUNIFY workstream-stage codes — **inside the target directory.**

**My verdict, since CRO asked for it: NOT fatal, and I would not rename.** The colliding uses are
**workstream/TO stage codes in prose and lane descriptions**; the proposed uses are **ontology terms in
a term registry**. Those are different key spaces and no mechanical resolver crosses them —
`SYSTEM_DEFINITIONS.yaml` currently defines **no** S-numbered term (verified: zero matches for
`^\s*S[0-9]:`), so the registry's own space is clean.

**ADDENDUM 2026-08-07 — CTO~D's counter-argument for a rename, TESTED AND FALSIFIED at its strict
reading.** They argued the collision count is irrelevant because the registry's term space is 51 terms
of which 10 are letter-number codes, and *"ALL TEN CODES DECLARE A LADDER POSITION in `sits_at` —
ten of ten, no counterexample"*, making a non-rung code a category error at any collision count. I
re-derived it. **The parse confirms 51 terms / 10 codes / 41 words — and 8 of 10, not 10 of 10:**

| code | `sits_at` | ladder position? |
|---|---|---|
| C0–C4 | `ladder rung 0..4` | yes (5) |
| D1–D3 | `rail between Cx and Cy` | yes (3) |
| **C3.i** | `C3 grain, deterministic projection; view-compiled` | **NO** |
| **C3.ii** | `C3 grain, semantic projection; view-compiled` | **NO** |

**`C3.i` and `C3.ii` are the counterexample, and they are the structurally relevant kind**: codes for
things that are *not rungs* but are positioned *relative to* a rung's grain — which is exactly what
`S0`/`S1` with `sits_inside: C0` would be. The registry already admits non-rung letter-number codes.

**In fairness, the charitable reading of their claim survives**: all ten codes are positioned
*relative to the ladder*, and that reading is true at 10/10. **But it does not support a rename
either — because `sits_inside: C0` satisfies it.** Both readings fail to make S0/S1 a category error:
the strict one has counterexamples, the charitable one is satisfied. **My P2 verdict therefore stands
and is now positively argued rather than merely permissive.**

**RESOLVED — CTO~D conceded in full `@a21b44580`, and handed over a precedent STRONGER THAN MY OWN
COUNTEREXAMPLE. Credit where it belongs: this is their argument, against their own position.**
**`D1–D3` is the governing precedent and it is decisive.** `D` is a **new letter series introduced for
a new structural relation** — *rails between rungs, which are themselves not rungs.* So `S` for
"inside a node" **follows that precedent rather than breaking it**: the registry has already minted a
non-rung letter series once, deliberately. That is a positive warrant for `S`, where C3.i/C3.ii were
only a counterexample to the prohibition. **We are one position, not two — Andrew sees one
recommendation on this.**

**Scope note on the one live argument that does NOT fall with the category claim:** CRO separately
raises an **occupancy** argument (the two-character token space is crowded — `N0=177, N1=1287, K1=90,
K0=3`). **That is a different basis and my verdict does not answer it.** Mine is that `S0`/`S1` are
**not a category error and not fatal**. Occupancy is a design-cost argument about collision density,
not a correctness one — **if CRO prefers words on that basis I do not oppose it**, and I am not
extending a correctness verdict to cover a cost judgement that is the author's to make.

**And their serving-path argument remains the strong form — I concur with it:**
`SYSTEM_DEFINITIONS.yaml:4` declares the file is served by `comp-estate --definitions` with **fuzzy
match on term + aliases**, so a post-landing query for `S0` returns the ontology term while 13 estate
uses mean a build stage. That is a **consumer-confusion** cost, not a correctness one. **P2:
disambiguate in the definition text** (state explicitly that `S0`/`S1` are ontology strata and are
unrelated to NFRA_COMPUNIFY/NFRA_HEATMAP stage codes) rather than renaming the letter.

---

## P2-8 — ACCEPTANCE TESTS: three can pass while the layer is broken, and the central discipline has NO test.

CRO asked precisely the right question. Answers per test (§10):

| # | Can it pass while broken? | Mechanism |
|---|---|---|
| 1 Round-trip | **YES** | *"every C1 edge **over a covered node**"* — the denominator is self-selected. If "covered" means "nodes where we found sites," the test runs over exactly the set where it works. Shrink coverage, pass harder. **Gate the PRECONDITION (what counts as covered) not the OUTPUT.** |
| 2 Negative control | **YES** | *Who picks the file?* A hand-chosen no-I/O file measures the author, not the instrument. Must be **generated** from the corpus, not nominated. |
| 3 Mutation | no | Genuinely discriminating. **But it exercises `identity` only** — a green mutation test on one axis reads as "the layer was mutation-tested." |
| 4 Anti-fabrication | **YES** | *"inherit it, do not re-derive it."* An inherited battery tests `script_io_ast`'s folding. If the S-layer re-implements or extends folding on a different SDK, **the inherited assertions may not execute the new path at all** — pass count unchanged, coverage silently zero. |
| 5 Cross-language join | **YES** | **N=1.** One hand-picked field can be made to work while the other 4,968 `Field` nodes cannot. (Also blocked-or-not per P1-5.) |
| 6 Known-negative | no | The strongest of the six. Keep it as the load-bearing one. |

**Three gaps, and the first is the serious one:**

- **NO TEST FOR THE LAYER'S OWN CENTRAL DISCIPLINE.** §4 Axis 3 states *"`unresolved` and `opaque`
  must be EMITTED, never dropped ... SILENCE IS THE DEFECT."* **No acceptance test asserts it.** Test 2
  covers the *all-zero* case; the actual failure mode of an under-reporting instrument is
  **partial** — some sites resolved, the opaque ones quietly absent — and nothing in §10 fires on
  that. The landed `Coverage.unresolved` channel (P0-1 Leg C) is the ready-made assertion surface.
- **No test for Axis 4 (`condition`)** at all.
- **No test for R4's second direction** — *"edges with no sites"* — which §5 itself calls *"the more
  valuable one."* The spec names it as the thing the estate currently cannot ask, then does not test
  that it can now ask it.

---

## DEFERRALS — stated explicitly, because a silent non-answer is worse

- **CRO's nominated pair (§9.1, `derive` vs identity's passthrough/rename): REAL, but the WEAKEST of
  the four breaks, and the mechanism is not the one he suspected.** Verified: `derives-from` binds up
  `[FLOWS_TO, PROP_PASSES]` and **carries** `EdgeKind(passthrough|rename|recompute_guarded)`
  (`NFRA_ONTOLOGY_RULE_BANK.yaml:139`). So Axis 1's `derive` selects the *relation* and Axis 5
  populates a *property carried by* that relation. That is **parameter-of**, not co-variance — Axis 5
  is only defined when Axis 1 ∈ {ingress, egress, derive, roundtrip}, i.e. **conditional on Axis 1**,
  which is a weaker defect than P0-1's nullification. **P2, fix alongside P1-3.** *His instinct that
  self-nomination produces the weaker test was correct, in both directions: right pair, wrong
  mechanism, and not the worst break.*
- **Axis 2×4 coupling — flagged, not ranked.** Axis 4's own value table says `iterated` *"implies
  multiplicity, **relevant to grain**."* That is a conceded coupling to Axis 2 sitting inside the
  axis table, and it appears on **no** suspect list. It is not a functional dependency (a loop can
  write rows or whole artifacts), so it does not break independence — but either state how it is
  relevant to grain, or delete the clause. **Ranking it P2 rather than P1 is a judgement call I could
  be wrong about.**
- **§9.4 (materialize vs view-time) — I am ANSWERING it, against CTO~D's read, which he invited.** His
  claim is that `view_time_compiled` (`SYSTEM_DEFINITIONS.yaml:181`) binds C3-and-below to *"computed
  at invocation ... NEVER served from a hand-written document,"* so S0/S1 instances can never be a
  document. **I read the law as narrower than he does.** It prohibits a **hand-written** document; it
  does not prohibit a **materialized vintaged projection**. The estate already materializes 20,398
  C0/C1 nodes in comp-kuzu and treats that as legal precisely because it carries a vintage and
  auto-refreshes on HEAD-advance. **So §9.4 resolves as: materialize as a vintaged projection, never
  as a hand-authored record — and S0's mandatory `vintage` field is exactly what makes that legal.**
  CTO~D's direction is right; his stated strength overshoots the text. Flagging to him, not
  adjudicating over him.
- **`comp-iam`-style DESIRED/APPLIED discipline in R5 — NO FINDING, and it deserves saying.** §5 R5
  (*"an S-layer claim is never evidence that a line runs in production"*) is correct, is the right
  lesson from the right incident, and is the single most likely clause to be dropped as obvious.
  **Keep it verbatim.**

---

## WHAT YOU SHOULD HAVE ASKED BUT DID NOT

**You asked me to test whether the five axes are independent of each other. You did not ask what the
axes are independent OF — and the answer is that at least one of them is not a property of the
subject at all.**

Axis 3 is a property of `(site, extractor, extractor's tier)`. You found half of that yourself
mid-review and handed it to me. But the general question it opens is the one nobody has asked:
**which of the other four axes are also secretly two-place?**

At least one more is. **Axis 2 (`grain`) is a property of `(site, recognizer)` too** — `field` grain
is only observable if the recognizer subscripts dataframe columns; the *same line of code* reads as
`artifact` grain to `script_io_ast.py` and `field` grain to a column-aware recognizer. §4 Axis 2 makes
this the layer's headline contribution — *"a site is where grain is actually OBSERVABLE"* — and that
sentence is **precisely the admission that grain is observer-relative**, written as though it were
observer-independent. The spec then builds R2 on it (*"the edge's grain is the COARSEST grain among
its sites"*), which silently assumes every site was measured by an equally capable observer. **Run
two recognizers of different tiers over one file and R2 returns a different edge grain for the same
code** — with no field anywhere in S0 or S1 recording which observer produced the reading.

**The structural question, which is bigger than any single axis:** the S-layer as specified has **no
place to record who measured a site and with what capability.** `comp_recognizer_sdk` already carries
`Provenance{source, locus, recognizer}` (`:168`) — it records the *recognizer* on every emission,
because COMPILERKIT already learned this. Your S0 record (§3.3) has `node_id, file, line, end_line,
col, symbol, vintage` — **`vintage` answers "when," and nothing answers "by whom, at what tier."**

You made `vintage` mandatory because `file:line` without it resolves at every vintage to different
code. **The same argument applies one axis over: `file:line@vintage` without an observer resolves to
different *grains* and different *resolutions* depending on who looked.** A site record without an
observer field is under-determined in exactly the way you correctly refused to let it be
under-determined in time.

That is one additive field, it is free today, and after a naming act it is a ratification change.

---

*Grounding note: every source citation above was read at `HEAD 72279a7c27` (CLOUD, 0 behind origin)
and every count printed with its denominator. Nothing here rests on an exercised run — I read source
and live YAML, not behavior. **No claim in this review is a behavioral or GREEN claim, and none should
be read as one.** Where passability is at issue (§10.5, P1-5) I have said explicitly that it needs an
exercise and that mine is not it.*

*Self-correction, on the record: I briefly measured §5 as CHANGED between revisions. That was a
retrieval artifact — my `sed` range terminated on the §6 heading, which did change. §5's body is
byte-identical and CRO's "what did not move" list is accurate. The control that caught it was reading
the actual diff instead of trusting the hash.*

— 3.0.0_SA_CVO~C
