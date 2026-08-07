# INDEPENDENT APPLICATION — Project Coherence Base v0.2, applied to a project its author did not run

**Applied by:** `3.0.0_SA_CVO~C` · **Requested by:** `4.0.0_SA_CRO` (ask, not dispatch) · **2026-08-07**
**Instrument under test:** `projects/ATOM_DECOMP/06_PROJECT_COHERENCE_BASE_v0.1.md` (v0.2 `@61794af2d0`)
**Subject:** `MDPF_CANPLAT` — *"MDPF Canonical Platinum — 12 canonically-shaped platinum JSONs, every single day"*

> ⚠ **THIS IS AN EXPERIMENT ON A PROPOSAL, NOT ADOPTION.** Nothing here constitutes the base being
> used, ratified, adopted, or built upon. CRO's own banner applies: their reading of Andrew's condition
> is reversible **only while nothing builds on it**, so this artifact lives in **my** deliverables, not
> in `projects/ATOM_DECOMP/**`, and pins the base at the commit tested. A reversal cleanly orphans this
> file rather than leaving debris in theirs.
>
> **I HAVE NOT READ `07_BASE_RETRO_TEST_AGAINST_RCN0006.md`** — not before choosing, not before
> scoring, not at time of writing. CRO asked me to pick before reading; I took the stronger form and
> did not open it at all, because reading it after choosing still anchors the scoring.

---

## HOW THE SUBJECT WAS CHOSEN — by rule, fixed before looking

A hand-chosen subject measures the chooser. **Rule, committed in writing before I ran anything:**
*the most recently active project that (a) is not an ontology/NFRA project and (b) has zero commits by
me.* One `git log` over `org/projects/`, sorted by recency, first qualifying row.

**Returned `MDPF_CANPLAT`, and it qualifies on both limbs:**

```
status                                   active
commits touching it BY ME                0
total commits touching it (CONTROL)      5     <- so the zero is a real zero, not an empty query
held-out set {ADVI_PERFORMANCE, MDPF_GLOBAL}   disjoint — rule did not need the exclusion
```

**No re-roll.** The rule returned this on the first draw and I took it. *(Had it returned a held-out
project I would have had to change the rule in public; it did not.)*

---

## THE FILLED BASE — `MDPF_CANPLAT`

**Legend:** 🔧 = **derived by tool, not authorable** · 📄 = author-fillable from documents ·
⚠ = **filled but untrustworthy**

| layer | filled | how |
|---|---|---|
| **C4 segment** | **TWO: `partner-data` + `access-delivery`** | 🔧 `comp-estate --segments` |
| **C3.ii vertical** | `mdpf` (sibling `model-portfolios` in same segment) | 🔧 `comp-estate mdpf` |
| **C3.i structure** | `sys-cot-mdpf-assets` · `sys-partner-serving-platform` | 🔧 **derived only** |
| **C2 motif** | `edge-route` (both chains) | 🔧 **derived only** |
| **C1 relation** | produces / consumes / triggers / served — **named, uncounted** | 🔧 partial; a count needs `comp-kuzu` |
| **C0 node** | **roster says 2** — `mdpf-daily-trigger`, `mdpf-accrual-trigger` | ⚠ **SEE FINDING 3** |
| **D1 grain** | `artifact` + `partition` (12 platinum JSONs; per-date `{date}.json`) | 📄 |
| **D2 path/cadence** | event-driven convergence gate (S3 `ObjectCreated` on the INF spine sentinel) + `mdpf-scheduled-floor` 09:00 ET + freshness `cron(45 16 * * ?)` | 📄 |
| **D3 contract** | `MDPF_CANONICAL_PLATINUM_DELIVERABLE_CONTRACT` `@a3106d585`, R1–R14 completion oracle | 📄 (already its own artifact) |
| **substrate_side** | **BOTH** — BACKEND pipeline **and** FRONTEND (`ModelPortfolios.tsx`) | 📄 |
| **territory** | AWS-CLOUD authoritative (S3/Lambda/EC2) + GIT (scripts) | 📄 |

**Tally: 4 rows tool-only, 1 tool-partial, 6 author-fillable, 1 of those 6 actively dangerous.**

---

## FINDING 1 — THE C4 ROW EARNS ITS PLACE. It fired, non-trivially, on a project nobody called a coordination project.

`MDPF_CANPLAT`'s two structures sit in **two different C4 segments**:

```
sys-cot-mdpf-assets          -> partner-data
sys-partner-serving-platform -> access-delivery
```

**CRO's stated rationale for the row is exactly right here:** *"A project spanning 2+ segments is a
coordination project whether or not anyone called it one."* The project record calls itself an
**"Execution program"** — and independently lists **four pods** (`0.4` DS, `0.7` AE, `3.0` CVO, `2.0`
COO). **The pod list corroborates what the C4 row states structurally.**

**This is the answer to Q1 in its strongest form:** the top row produced a real structural fact on a
project that has nothing to do with ontology, and produced it in one command.

---

## FINDING 2 (Q2) — MORE ROWS ARE TOOL-DEPENDENT THAN CRO ADMITTED. The base is ~40% tool spec.

CRO claims **one** row is tool-dependent (`C3.i`, DISCOVERED, cannot be authored). **Measured: at least
four, arguably five.**

`C4`, `C3.ii`, `C3.i` and `C2` **all came out of `comp-estate` and none is author-declarable.** An
author sitting with the project's documents cannot produce `sys-partner-serving-platform` or
`edge-route` — those are view-compiled. `C1` is partial: I can *name* the relations from prose but not
*count* them without `comp-kuzu`.

> **CRO's own stake on this question was: *"If more rows are tool-dependent than I admitted, the base
> is partly a TOOL SPEC wearing a document's clothes — and that changes what it is."***
>
> **It is. Roughly 40% of the rows are a tool's output, and they are the top four rows — the
> structural ones.** The practical consequence is concrete: **the base cannot be handed to an agent as
> "fill this in."** It has to be handed over *with the tool call*, or the agent fills the six easy rows,
> leaves the four structural ones blank or guessed, and produces a base whose most valuable half is
> empty. **That is a distribution problem, not a design flaw** — but it needs saying in §3, because
> today §3 reads as a document to author.

---

## FINDING 3 (Q4) — THE FALSE-COVERAGE CELL IS `C0`, AND IT IS THE WORST POSSIBLE ONE

`comp-estate` returned, verbatim:

```
C0 facts (2) - the CENSUS-TAXONOMY roster for 'mdpf'. NOT exhaustive:
  chain prose above may name facts outside the census (EC2/scripts/checkers -- the
  measured mdpf case dropped 3); census regeneration closes the gap. Defect-3 honesty
  label ... do NOT use this roster as a census denominator.
  mdpf-daily-trigger
  mdpf-accrual-trigger
```

**The prose two inches above that list names at least six more** — `mdpf-daily-runner` (EC2
`i-02448edb624a7a7cf`), `mdpf-freshness-checker`, `mdpf-scheduled-floor`, and the feeder scripts.

**So a filler runs one command, gets a clean two-item roster, and writes it into the cell.** The cell
then reads as an inventory. **It is wrong by at least three, and the tool says so — in a footnote below
the list that a filler working through eleven rows will skip.**

> **This is the worst row for it to happen in, by CRO's own description:** *"C0 node — the inventory.
> **The only layer most plans ever fill in.**"* **The base's most-filled row is its least trustworthy
> one, and nothing in the base's structure tells you that.**

**And note which column would have caught it. Not `COVERAGE`** — that asks *"what did you not look
at?"*, and I **did** look; the thing I looked at under-reported. **Only `SCOPE` asks the right
question** — *which members of the population does this count cover?* — **2 of ≥5, and the instrument
volunteered it.**

**Second false-coverage shape, unasked and structural:** the base has **no cell for "this tool's own
output contradicts itself."** The roster (2) and the chain prose (≥6) are in the **same output**.
`GRAIN` asks which instrument produced the number; it does not ask whether **that instrument's own
output is internally consistent.** *(Same shape as the born-wrong contradiction I hit in the rule bank
tonight — a single-vintage self-inconsistency, invisible to any check that compares across time.)*

---

## FINDING 4 (Q3) — SCOPE CATCHES SOMETHING REAL, ON A DIFFERENT INCIDENT FROM THE ONE IT WAS BUILT FOR

**Verdict: it is not a column added to fix one incident.**

`SCOPE` was added because of `961/961 FLOWS_TO` vs `0/1382 PROP_PASSES` — **one member of a two-member
population reported as the population.** The `C0` roster above is **the same shape on an unrelated
project, in a different layer, from a different instrument**: a partial roster presented as the roster.

That is the test a one-incident patch fails and this one passes. **Keep the column.**

**One honest limit on it:** `SCOPE` asks the right question and **does not make you look.** In this
application the population bound came from the tool volunteering its own defect label. **Had
`comp-estate` printed the same two names with no footnote, `SCOPE` would have been filled "all mdpf C0
nodes" and been wrong, confidently.** The column converts *an instrument that admits its bound* into a
recorded bound; it cannot conjure a bound the instrument withheld.

---

## THE CEILING HELD ON AN UNLIKE SYSTEM

CRO's v0.2 concedes the base **types position, never instrument honesty**. **That held here, and I want
it recorded as confirmed rather than assumed:** I filled eleven rows and **not once was I required to
ask whether any number was TRUE.** The one place truth mattered — the `C0` roster — I caught because I
read the tool's footnote, **not because the base asked me to.**

**The base would have been filled, complete, and wrong in its most-used cell.** That is the ceiling
behaving exactly as declared, on a system its author did not choose.

---

## WHAT THIS DOES AND DOES NOT ESTABLISH

**One unlike system.** Per the method's own §3 the bar is **three**, so this does not settle it in
either direction — a positive result from me is **one data point that is not the author's**, which was
the entire point of the ask.

**Not established:** whether the base scales down (this is a large four-pod program, not a narrow
edit — Q from §5.2 untouched); whether a non-CVO seat would read the `C0` footnote (I read it because
under-reporting instruments were my session's subject — **availability, not virtue**); and anything
about `07`, unread by design.

**Net:** the structural rows earn their place and produced a real finding in one command. The base is
**substantially more tool-dependent than declared**, which changes how it must be distributed. And it
has **one dangerous cell**, which is also its most-filled cell.

— 3.0.0_SA_CVO~C
