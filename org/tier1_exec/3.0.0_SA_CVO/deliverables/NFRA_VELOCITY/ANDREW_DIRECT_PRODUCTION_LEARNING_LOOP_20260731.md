# ANDREW-DIRECT -- THE PRODUCTION LEARNING LOOP, and the INTENT / FRICTION axes

**Recorded by:** `3.0.0_SA_CVO` per `org/XXX.md` -- an Andrew-direct instruction is recorded DURABLY and
broadcast SAME TURN, VERBATIM, with channel + time. Never a paraphrase.
**Channel:** Andrew -> `3.0.0_SA_CVO` session terminal, DIRECT (no relay hops).
**Time:** 2026-07-31, ~1655-1700Z. Two of the three arrived MID-TURN.
**Scope:** NFRA_VELOCITY_ESTATE. Not a carve-out; this is the ESTATE PRD's own spine made explicit.

---

## 1. ANDREW, VERBATIM AND IN ORDER

> **(1)** "Yes is this persisted anywhere? this concept is effectively the production learning loop"

> **(2)** *(mid-turn)* "i like the AXIS of Intent and Friction"

> **(3)** *(mid-turn)* "I think blast-radius is a way to potentially check overlap, in essence if
> something has highly overlapping blast radius and is doing the same function, that is very high
> friction, and needs to be assessed"

**THREE DISTINCT SOVEREIGN ACTS, and they are not the same kind of act:**
**(1) is a NAMING ACT** -- "the production learning loop" is now the name of the thing.
**(2) is a RATIFICATION** of the INTENT / FRICTION decomposition of WS-E3's decision.
**(3) is a NEW MECHANISM** -- it does not restate (2), it EXTENDS the friction axis with a detector.

---

## 2. WHAT PROMPTED IT, so the record is re-derivable

Andrew read a CVO diagram of the ESTATE workstreams, and CORRECTED IT IN TWO PLACES:

- **He struck VIEW 3 as ad hoc** -- "just an ad hoc thing between you and I in the context of this
  project, not a real process." **CORRECT, and CVO conceded it**: the `/draw` template demands a
  query view, and CVO filled it with "Andrew asks CVO, CVO re-derives," which is a CONVERSATION, not
  a mechanism. *The form dictated a claim.* The genuine standing read is the Kimi review cycle,
  already present in VIEW 2.
- **He read VIEW 1 as a CYCLE where CVO had drawn a static census.** CVO drew four rows (verb ->
  workstream -> artifact -> status) because it was answering *where are we*. Andrew read *how does it
  work*, and the PRD §0 verbs close into a loop. **His read was better than the drawing.**

---

## 3. THE LOOP (Andrew's name, CVO's rendering)

```
        ┌─────────┐   contracts + lifecycle   ┌─────────┐
   ┌───►│   SAY   │──────────────────────────►│  FIRE   │
   │    │  WS-E1  │   declared order, cadence │  WS-E2  │
   │    └─────────┘                           └────┬────┘
   │         ▲                                     │ runs; emits telemetry
   │         │ new + changed assets re-declare     ▼
   │    ┌─────────┐                           ┌─────────┐
   └────│  SHED   │◄──────────────────────────│ MEASURE │
        │  WS-E3  │  what no longer has       │ WS-E4/5 │
        └─────────┘  intent behind it         └─────────┘
```

**PRD §0 states the four verbs as a SENTENCE. It does not state them as a LOOP.** The loop is
Andrew's reading, ratified here, and it is the difference between a scope list and an operating cycle.

---

## 4. SHED TAKES TWO AXES -- and only one was ever instrumented

| | **AXIS 1 -- INTENT** | **AXIS 2 -- FRICTION** |
|---|---|---|
| the question | "is this still wanted?" | "what does it cost to remove -- and what to keep?" |
| carried by | `lifecycle_class`, PRODUCER-ASSERTED, never observer-inferred | blast radius, live gates, writer/reader census, unit-of-retirement |
| instrument | **NONE EXISTED.** Nothing ever ASKED a producer; all 14 WS-E1 subjects read `UNDECLARED` | **INSTRUMENTED AND WORKING** -- this is the axis E3.0 used |
| the fix | the C3 labeling walk (spec v0.2, CVO-reviewed) IS the missing sensor | extended by Andrew act (3) -- see §5 |

**THE MEASURED CONSEQUENCE, and it is why SHED sits at zero:** E3.0's safe slice closed at **0
retirements, 6/6 KEEP-DORMANT** (@`2da40ba711`), and the P1 baseline §3c records why in terms:
**THE SAFE SLICE AND THE CLEARABLE SLICE DO NOT OVERLAP.** The population with zero blast radius
(axis 2 clean) was also the population with no intent evidence (axis 1 unknown).

> **THE ESTATE HAS BEEN TRYING TO MAKE A TWO-AXIS DECISION ON ONE AXIS, AND THE HONEST ANSWER ON ONE
> AXIS IS ALWAYS "DO NOT TOUCH IT."** That is not caution; it is the only sound verdict available.

---

## 5. ANDREW ACT (3) -- BLAST-RADIUS OVERLAP AS A DUPLICATION DETECTOR

**This is the genuinely new content and it changes what the friction axis IS.**

CVO's framing had friction as a COST (what breaks if I remove this). Andrew's adds a second sense:

> **HIGH BLAST-RADIUS OVERLAP + SAME FUNCTION = HIGH FRICTION = ASSESS.**

**Why it matters: it makes axis 2 GENERATIVE rather than merely gating.** Previously axis 2 could
only price a candidate someone else proposed. Under act (3) it can **PROPOSE** candidates: two assets
whose blast radii heavily overlap and whose function is the same are probably one asset wearing two
names, and the duplication is itself the cost -- paid continuously, by everyone downstream.

**THE ESTATE ALREADY HAS THE SPECIMEN, AND IT IS ANDREW'S OWN, CONDEMNED IN HIS OWN WORDS**
(AWS_ESTATE_CENSUS RULINGS_LEDGER, 2026-07-30, verbatim): *"yeah this whole bucket is garbage, this
is agents just making duplicate resources... prime example of cruft and agentic slop."* The census
classed it **`estimate-shadowing-exact`**: *an agent built an ESTIMATOR for a quantity the estate
already measures EXACTLY.* **Two things, one function -- and the estate had no mechanism that would
have noticed.** Act (3) is that mechanism. Sibling class already on the books:
`canon-bypass-creation` (a resource created beside the declared canonical location).

**FENCE, stated before anyone builds it:** this is an ANALYSIS over the existing dependency graph
(`comp-blast` already computes blast radius) producing **CANDIDATES FOR HUMAN ASSESSMENT** --
Andrew's own word is *"needs to be assessed."* **IT IS NOT AN ALARM, A MONITOR, OR A DETECTOR THAT
PAGES.** The standing moratorium binds; a finding lands as a candidate list a person reads, never a
notification. Anyone reaching for SNS/SES/CloudWatch here has misread the instruction.

**OPEN DESIGN QUESTION, NOT RULED HERE:** "doing the same function" is not mechanically decidable
from the graph alone -- overlap is computable, FUNCTION-SAMENESS is a semantic judgement. So act (3)
plausibly needs the C3.ii vertical labels (axis 1's own output) to make the second half of the test.
**If so, the two axes are not independent: FRICTION-AS-DUPLICATION READS INTENT'S OUTPUT.** Routed
to COO (E3/E5 design) and CTO (arch), not settled by CVO.

---

## 6. IS IT PERSISTED? -- MEASURED, NOT ASSERTED

Andrew's question (1) was literal, and the answer is **NO**.

| probe | result | reading |
|---|---|---|
| `"production learning loop"` | **0 hits / 24,771 files scanned** | the NAME did not exist before this record |
| `"SHED what it no longer intends"` (POSITIVE CONTROL) | **2 hits** | the instrument DISCRIMINATES -- the zero above is a measurement, not a broken search |

**WHAT *IS* PERSISTED:** the four verbs, as a SENTENCE, in ESTATE PRD §0 (canonical + one staged
copy). **WHAT IS NOT:** the LOOP shape, the INTENT/FRICTION decomposition, the
one-axis-instrumented diagnosis, and act (3)'s overlap detector. **The components sat in three
separate documents** -- the PRD's retirement-forbidden-against-UNDECLARED clause, the P1 baseline's
measured non-overlap, and the C3 spec's problem statement -- **and nothing composed them.**

> **THE SYNTHESIS WAS NOT WRITTEN DOWN ANYWHERE, AND IT EMERGED FROM ANDREW READING A DIAGRAM AND
> DISAGREEING WITH IT.** That is worth its own line in the record: the estate's own material,
> composed by the one reader who was outside the measurement -- the same shape as the 07-30 specimen
> where the corrective question came from the party who had never handled the claim.

---

## 7. ROUTING (CVO surfaces; CVO does not adjudicate scope)

| to | what | why |
|---|---|---|
| `0.7.0_AE_CloudOps~B` | §4 + §5 **before v0.3 lands** | the two-axis framing is the sharpest available justification for the C3 layer -- it names precisely WHAT the walk is a sensor FOR |
| `1.0.0_SA_CTO` | §3 + §4 as a **PRD §0 amendment candidate** | the PRD is arch-gated; CVO does not amend it. The loop is the PRD's own sentence made structural |
| `2.0.0_SA_COO` | §5 as an **E3 / E5 design input** | E3's TO is theirs, and act (3) is a new candidate-generation mechanism for a workstream currently INERT |
| `0.0.0_AB_MSTR` | the record | seam + cross-fabric visibility (CORE's C3.ii labels are the input act (3) may need) |

**NOT DONE HERE:** no build, no TO issued, no PRD edit, no detector. This record exists so the naming
act and the two new mechanisms are durable and verbatim before they are relayed -- and so nobody
rebuilds them from memory.
