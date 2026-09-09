# SPEC — Kimi call subdivision + deterministic insight strata

**For:** `1.0.0_SA_CTO~B` (runner + design owner). **From:** `3.0.0_SA_CVO`.
**Authority:** Andrew-direct, CVO terminal, 2026-08-05 — subdivide the call layout; feed the model
the high-signal deterministic strata our own tools already compute, *"not just obvious stuff."*
**Sequencing:** Andrew ruled v3 State/Friction is sorted FIRST; this spec is the input to that work,
not a parallel track.

**Grounding vintage:** all `estate_report_runner.py` line cites are `@a254104b34` (tip for the file,
deployed 2026-08-05T14:56:59Z, md5 `a110981492b461e19fb9be7848b9ad09`).

---

## 1. The measured problem this replaces

| Fact | Evidence |
|---|---|
| **It is ONE call doing everything** | `:1072` — single `call_kimi(build_prompt(resources, window_desc), ...)` |
| **The corpus NEVER reaches the model** | nuggets computed `:1058`, stored `:1096`, **never passed** — `build_prompt(resources, window_desc)` `:806` has no corpus parameter |
| **The git payload is silently truncated mid-structure** | `:826` `[:60000]`. Today: 69,495 chars → **9,495 dropped (14%)**, cut mid-string at `"area:data-scripts": {\n "resource": "area` |
| ~~**89% of paths land in fallback labels**~~ ⛔ **COMPOSITE — SEE §1a** | ~~today's run: 10 of 357 chain-resolved, 318 area-bucketed~~ |

### 1a. CORRECTION 2026-08-06 — THE "89% FALLBACK" IS TWO DIFFERENT THINGS ADDED TOGETHER

*Measured by `1.0.0_SA_CTO~B` @6a20a5d42 across two independent days. **I found the same split myself
in `S1_attribution_denominator_finding_20260805.md` @ccef4eba5 and NEVER PROPAGATED IT INTO THIS
DOCUMENT** — see the propagation note below.*

| | 2026-08-05 | 2026-08-06 |
|---|---|---|
| changed paths, total | 357 | 217 |
| **governance-class** (`org/`, `docs/`, `.claude/`) | **234 (65.5%)** | **135 (62.2%)** |
| non-governance (the real resource axis) | 123 | 82 |
| chain rate **AS REPORTED** | 2.8% | 7.4% |
| chain rate **ON THE CORRECTED DENOMINATOR** | **8.1%** | **19.5%** |

**The single number was hiding two populations:**
1. **GENUINE RESOLVER MISSES** — `area:infra-other`, `area:data-scripts`, `area:tooling`,
   `UNRESOLVED`. Real resources that should have chained and did not. **A real defect.**
2. **STRUCTURALLY UNRESOLVABLE RECORDS** — `org/`, `docs/`, `.claude/`. **No producer emits these;
   an agent wrote them. They can NEVER chain.** Not a resolver failure at all.

**~Two thirds is category 2, and no resolver improvement can move it.** On the corrected denominator
the resolver is ~2.4–2.6× better than this document recorded — still weak, but **weak in a fixable
way**, which is a different engineering problem from the one §21 described.

**AND IT EXPLAINS THE REJECTED PROPOSALS BETTER THAN "THE RESOLVER IS BAD" DOES.** `area:governance`
is the **largest entry on the resource axis both days** — 118 paths on 08-06, **5.6× the next-largest
real resource and 118× the median producer.** The model proposing against it is **not reaching for a
fallback; it is correctly picking the biggest thing in front of it.**

> ⚠ **THIS ALSO CORRECTS §D's SEQUENCING ARGUMENT BELOW.** That argument says *"if 89% of subjects are
> named `area:*`, D sits underneath everything."* **D gives real names to RESOURCES — and ~62% of the
> axis is not a resource to be named.** Had we gone straight to D on the uncorrected number, we would
> have built it, watched the fallback rate barely move, and **concluded D was broken.**
> *(This is Rule 24 postulate **(iv) STATE COHERENCE** — the remedy test names which values do NOT
> move — catching what the other three postulates missed.)*

**THE CORRECTION IS A RE-AXIS, NOT A FILTER:** two axes, one intent each. **RESOURCES**
(`producer:*`, genuine `area:*`, `UNRESOLVED`) — chain-resolvable, and its rate finally measures the
resolver **and only the resolver**. **RECORDS** (`org/`, `docs/`, `.claude/`) — not chain-resolvable
**by construction**, which is not a defect. **No path is discarded**; the records axis carries its own
declared denominator per §5. *A silently excluded path is the same defect facing the other way.*

**⚠ PROPAGATION NOTE, and it is mine.** I measured this split myself on 08-05 (S1 @ccef4eba5: 243 of
357 non-resources) and **recorded it in a separate artifact that carries ZERO references to this
document.** This spec went on asserting the uncorrected number for a day, and the D-first argument was
built on it. **Two of my own documents disagreed and the newer one did not know about the older.**
Same class as §7a — *a finding that does not reach the document it corrects has not landed* — and the
second instance today, both caught by CTO~B rather than by me.
*(Minor: their governance-class count is 234 vs my 243; the delta is `rcg/`, which they classify
outside governance-class. Two derivations, same shape, one directory's classification differing.)*

**The causal chain, and it is not a model-quality problem:** the model is asked a *semantic* question
(has this prose drifted?) using *mechanical* evidence (which files moved), with the semantic evidence
withheld and 14% of the mechanical evidence silently missing. It can only propose against vocabulary
it was given — which is why both 08-04 proposals and 5 of 9 today target `area:*` compiled fallback
labels, and why Andrew has rejected that output class twice.

---

## 2. Organizing principle — GIVE IT CONTRADICTIONS, NOT MEASUREMENTS

A single-signal fact is a metric; the model can only restate it. **Insight lives where two
independent deterministic signals disagree.** Every stratum below is a pre-computed tension between
two reads that *should* agree. That is a task a language model is good at — explain the
contradiction, say which side is likely wrong, say what it implies. It is bad at manufacturing one
from a bucket list, which is what we ask today.

---

## 3. The four strata groups (Andrew-regrouped 2026-08-05: by QUESTION, not by tool)

Authored under CLAUDE.md Rule 24 — one intent per axis, one grain, mutually exclusive. Each group
asks a distinct question about how belief and reality diverge.

### GROUP A — DID WHAT WE WROTE ACTUALLY TAKE EFFECT?
A propagation **ladder**; one purpose, four layers, a different tool per rung.

| Rung | Tool | The gap |
|---|---|---|
| written → committed | `comp-heat drift` | uncommitted work (invisible risk in a shared tree) |
| committed → deployed | `comp-pipescript deployed` | committed-but-never-deployed (a named CLAUDE.md class) |
| deployed → served | md5/size vs the repo vintage | deployed artifact ≠ intended vintage |
| served → current | `comp-freshness` (**trading-day aware**) | served output stale behind its frontier |

*Hit twice today on this very pipeline. The trading-day basis is mandatory — a flat-hours read
false-alarms every Monday.*

### GROUP B — ARE OUR RELATIONSHIPS WHAT WE THINK?
Same question at three depths: what is wired, what actually moves, which way it trends.

- structural: `comp-blast --overlap-sweep`, `comp-pipescript overlap A B`
- behavioral: `comp-cochange matrix|pair` (`--grain type|serial`)
- temporal: `comp-heat compare` → CONVERGING / DIVERGING / PARALLEL **+ half-life**

**The rows that matter are the disagreements**, not the agreements:
- **coupled but only ONE side changed** → the silent-breakage leading indicator
- **co-moved with NO dependency edge** → hidden coupling / duplicated logic / undeclared contract
- **diverging with a rate** → a fork forming, an ownership split, or a quiet abandonment.
  *The rate is what makes it a forecast rather than a snapshot.*

### GROUP C — IS OUR LIFECYCLE PICTURE TRUE?
`comp-heat freshness` cold subtrees × citation/reachability (`comp-estate --fe-reachability`,
`--orphans-only`, `--debt`).
- **cold AND cited** → dangerous to archive. *This is the exact cell that reversed the dated-briefs
  archive decision on 08-04, after citations were found in production Lambda source.*
- **cold AND uncited** → the safe-archive queue.

### GROUP D — DO THINGS HAVE THEIR REAL NAMES?  ← **SUBSTRATE, NOT A PEER**
`comp-estate` C3.ii semantic verticals vs the compiled `AREA_BUCKETS` fallback.

**D sits UNDERNEATH A, B and C.** They all describe *subjects*; if 89% of subjects are named
`area:docs`, every insight above is phrased about a bucket. **Fixing D lifts all three at once, and
it is the direct fix for the rejected-proposal class.**

**Sequence D first.** New questions become *askable* only once subjects have real names — a vertical
that changed while its declared owner never touched it; two verticals whose co-movement suggests they
are one; a vertical with no changes but open work claiming it. Those are not new tools; they are the
same three questions finally asked about real things.

---

## 4. The call architecture

**Today:** five cognitive acts in one call, competing for one shared budget —
**R1** comprehend · **R2** narrate · **R3** detect drift · **R4** author prose · **R5** justify.
`max_tokens: 32000` is shared between `reasoning_content` and `content` (`:855-863`) — raising it
from 4000 fixed the starvation but **did not unbundle the contention**.

### CALL 0 — DETERMINISTIC COMPILATION (no model)
The comp-tools produce every stratum. **The model never computes a stratum, only interprets one.**
Each stratum is emitted with its contract (§5). Group A rungs 1–3 and Group C's uncited queue are
**LISTS, not insights** — they render in the report body and are NOT sent to a narration call.

### CALL 1 — NARRATE (R2)  ·  audience: **Andrew**
- **in:** stratum *summaries* + headline changes. Not raw payloads.
- **out:** the plain-English brief. No jargon, no serials, no hashes.
- **no** allowlist, **no** proposals. Judged on clarity alone.

### CALLS 2..5 — DETECT (R3), ONE PER GROUP  ·  audience: **the canon**
- **in:** that group's stratum + **the corpus nuggets** + the *current prose* of the entities named.
- **out:** `{entity, field, why_suspect, evidence_ref}` — **CANDIDATES ONLY, NO PROSE.**
- **HARD:** `entity` MUST be a canon entity from D. A candidate naming a compiled fallback label is
  **rejected by the runner, not by asking the model nicely** (`:26` — prompt discipline is not a
  control). This is the structural fix for the rejected-proposal class.
- Separating detect from author makes the funnel visible: we can see how many candidates were found
  vs authored vs adopted, per group, per day.

### CALLS 6..N — AUTHOR + JUSTIFY (R4+R5), **ONE PER CANDIDATE**
- **in:** that ONE entity's current prose + the specific evidence row + the nuggets bearing on it.
- **out:** `{proposed_text, rationale, evidence_cited}`.
- **HARD:** `evidence_cited` must reference a stratum row or nugget id. A proposal that cannot cite
  what it saw is discarded — this stops prose inventing its own warrant.
- Small prompt, small output, own budget. Fires **only** on R3 hits, so a zero-candidate day costs
  nothing.

**Why this removes the failure mode rather than mitigating it:** each call gets its own 32k budget,
so narration and proposal no longer compete; each call's evidence is scoped to its job, so nothing
needs a 60KB dump; and detection is constrained to real entities, so the output class Andrew rejected
cannot be produced.

---

## 5. THE STRATUM CONTRACT — non-negotiable, and the reason is specific

**Every stratum entering a prompt MUST carry its own denominator and its own input vintage.**

```
stratum: <name>
question: <the contradiction it encodes>
tool: <tool> <subcommand> <args>          vintage: <input freshness / commit-ish>
denominator: scanned N of M <units>       rows: <k>
[rows...]                                  # k may be 0 — that is a RESULT, not an absence
```

**Why this is load-bearing, not hygiene:** a stratum computed by a tool that returned clean zeros is
**byte-identical** to a stratum with genuinely nothing to report. Kimi cannot distinguish "no
coupling violations today" from "the coupling tool was pointed at the wrong universe and found
nothing," and **it will narrate either with equal confidence.** We are deliberately throwing every
angle at the wall (Andrew, 2026-08-05), which means shipping strata whose tools I have dialed and
found imperfect — several returned clean zeros for whole classes of question on 08-04. **A
high-signal stratum computed by a broken instrument produces CONFIDENT WRONG INSIGHT, which is
strictly worse than today's obvious-but-harmless output.**

Same law as the corpus defect found this morning: `degraded_sources: []` was the strongest possible
all-clear precisely because presence was the only predicate. **Do not rebuild that shape one layer up.**

### 5a. AMENDMENT — VINTAGE IS NOT A QUALITY SIGNAL. THE SECOND HEAD.

*(Added 2026-08-05 ~1540Z. Source: `4.0.0_SA_CRO` via `3.0.0_SA_CVO~B`, banked verbatim as theirs.)*

§5 requires every stratum to carry its **input vintage**. That requirement stands — but it creates a
hazard the same paragraph must close, because a model reading a freshness field will treat recent as
reliable, and **it is not**:

**RULING — Andrew-direct, CVO terminal, 2026-08-05 ~1550Z. This SUPERSEDES CRO's phrasing, VERBATIM:**

> **"treat recent output as the last agent's understanding of state, not a settled baseline"**

His correction of CRO's original — *"'recent output as a live error source' is true, but it gists too
heavily in favor of guilt"* — and the distinction is **not cosmetic; it changes what the contract must
require.**

- *Live error source* implies **down-weight recent rows** — a suspicion heuristic. Under it, the
  correct move is to trust new evidence less.
- *The last agent's understanding of state* implies something different and more useful: a recent row
  is **not suspect, it is UNSETTLED.** It carries **a viewpoint, and an author**, not a verdict.

**So the requirement is POSITIVE, not defensive:** a stratum row does not get discounted for being
recent — it must **carry whose understanding it is and whether anything ratified it.** The question a
reader (human or model) must be able to answer is *"who understood this, when, and has it been
adjudicated?"* — never *"is this new, and therefore shaky?"*

*Original observation and the incident behind it remain CRO's; the frame is Andrew's.*

#### TWO RENDERINGS OF THE SAME RULING — recorded separately ON PURPOSE

**(i) DIRECT, at this terminal, ~1550Z — what I heard myself, and what §5a is bound to:**
> *"treat recent output as the last agent's understanding of state, not a settled baseline"*

**(ii) FULLER, relayed by `4.0.0_SA_CRO` via `3.0.0_SA_CVO~B` (1700Z) — same ruling, more of it:**
> *"treat recent agentic artifacts as the last agent's understanding of state, not a settled
> baseline. It is not necessarily an error, but it is neither an absolute truth, it is a
> representation, a map, not the territory, and should be handled with a 'go and fetch for yourself'"*

**I am NOT overwriting (i) with (ii).** (i) is primary evidence from my own terminal; (ii) is a
relayed rendering, which XXX.md says I accept without challenging provenance — and I do. They agree
on the load-bearing clause. **(ii) carries two things (i) does not, and both change the spec:**

**A — "a map, not the territory" replaces a FALSIFIABLE justification with an unfalsifiable one.**
*(~B's derivation, and it is better than mine.)* CRO's retracted phrasing rested on an **empirical
claim about a population** — recent rows are error-prone. That is falsifiable, and a run of perfectly
good recent rows (the normal case) would leave the rule looking unmotivated. Andrew's form is a claim
about **what kind of thing a row IS**: a representation of one agent's understanding at a vintage.
A run of good rows cannot falsify it, because it was never a claim about error rates.
**Consequence: "recent = reliable" and "recent = suspect" are the SAME error.** CRO's phrasing ruled
out one; Andrew's rules out both. The vintage field's real job is to tell a consumer **which map it
is holding.**

**B — "go and FETCH FOR YOURSELF" is an operational directive, and it is now binding on the strata.**
Where a stratum row is **load-bearing** for a proposal, the consumer does not perform a trust
calculation on the row's age in either direction — **it fetches the territory.** In practice: a
proposal's `evidence_cited` must reference something re-derivable, and the detect/author calls must
be able to reach ground truth rather than reason from the stratum's summary of it. A stratum is a
map of the estate; it is never the estate.

*Provenance note kept deliberately: ~B relayed CRO's in-flight framing to me as settled, I banked it,
and its author revised it 40 minutes later — **the map-not-territory failure occurring inside the
message that warned about it.** ~B named that themselves. The relay was correct (it bore on my
stake); treating a 40-minute-old peer framing as durable was not. Both of us did it.*

Live instance, same day: `4.0.0_SA_CRO` landed a repair and **self-retracted half of it ~25 minutes
later**, after a label was flipped on coherence reasoning when a ratified prior adjudication had
already ruled that path on a grounded search nobody reproduced. **The retracted half was, for those
25 minutes, the freshest row in the tree.** Any stratum ranking or weighting by recency would have
scored it highest exactly while it was wrong.

**These are two heads of one disease and the contract must close both:**

| Head | The false inference | Instance |
|---|---|---|
| **presence ≠ health** | "all sources present" ⇒ healthy | `degraded_sources: []` over a six-day-frozen corpus |
| **recency ≠ correctness** | "newest row" ⇒ most reliable | a self-retracted repair, freshest for 25 minutes |

**THEREFORE — binding on every stratum:** vintage is emitted as a **fact about the input**, never as
a **rank, weight, confidence, or sort key**. No stratum may order its rows by recency or present
newness as a quality signal, and no prompt may invite the model to prefer recent evidence. Where
recency genuinely matters (Group B half-life), it is the **subject of the measurement**, never a
proxy for trust in it.

### 5b. APPLICABILITY CONDITION — where "go and fetch for yourself" BINDS

*(Added 2026-08-06. Source: `1.0.0_SA_CTO~B`, the only seat that must consume this in running code.
Andrew-directed convergence; full record `CONVERGENCE_..._20260806.md` @b5bcc1115.)*

§5a made *"go and fetch for yourself"* binding on load-bearing rows. **It carried no applicability
condition, and that was a defect in the contract, not in the principle.**

> **A CONTRACT THAT DOES NOT SAY WHERE IT APPLIES WILL BE APPLIED WHERE IT CANNOT HOLD, AND THEN
> ABANDONED WHOLESALE.**

**Measured, not argued.** Affordable at a batch call site: the estate-report runner is a once-daily
job on a transient box, whole run **3m24s**; a vertical join over a day's ~357 changed paths is ≈36s
serialised, seconds parallelised. **But it is affordable because of a property of that CONTEXT — daily
batch, transient box, no latency SLA, nobody waiting — not a property of this contract.** At a
request-serving call site (a 256MB Lambda behind API Gateway serving a live page) per-row ground-truth
fetch is a latency **and** cost failure, and the holder **will quietly ignore the contract.**

| consumer class | how it satisfies FETCH-THE-TERRITORY |
|---|---|
| **BATCH / ANALYTIC** | **Fetches directly.** The obligation binds as written. |
| **SERVING / REQUEST-PATH** | **Fetches AT PRODUCTION TIME and carries the vintage forward** — the fetch happens once, in the batch; the serving path inherits a **stamped** value rather than re-deriving it. |

This keeps Andrew's ruling intact where it is affordable and **gives the serving side a way to HONOUR
it rather than a reason to ignore it.** A rule only the comfortable half of the estate can follow is a
rule the other half learns to route around — and a routed-around rule teaches that rules are optional,
which corrodes the ones that bind.

**AND: NO SILENT TRUNCATION.** `[:60000]` must not survive into any call. A payload exceeding budget
is chunked with a declared denominator, or the call fails loud. A model cannot know it was handed
14% less than the day.

---

### 5c. AMENDMENT 2026-09-05 -- THE `reproduce` KEY. The contract shape gains one OPTIONAL, ADDITIVE field, and the specification catches up with the code rather than the other way round

**Trigger:** NFRA_OUTSET row W2-S20 (0.9.0_WK_NFRA_OUTSET~2, 2026-09-05T11:00Z, disarm_owner 3.0.0_SA_CVO). Building
O11-AC1 (traceability on deterministic lines) required every deterministic stratum row to carry the tool and the vintage
that reproduce it, and that lives in the stratum shape. The worker's order granted the runner's code and not this
document, so the code moved first: `_stratum()` in `infra/aws/ec2/estate-report-runner/estate_report_runner.py` (:1248 at
HEAD @f2ef16d70a) now returns a `reproduce` key, optional, additive, no change to the status vocabulary, no existing caller
altered. The worker recorded the divergence instead of leaving it for a later reader, which is the correct act; closing it
is the CVO's, and this section closes it.

**The shape, amended.** Section 5's block gains one line, and the line is optional:

```
stratum: <name>
question: <the contradiction it encodes>
tool: <tool> <subcommand> <args>          vintage: <input freshness / commit-ish>
denominator: scanned N of M <units>       rows: <k>
reproduce: tool=<tool> claim=<rail-reproducible | host-reproducible | not-reproducible>   # OPTIONAL, ADDITIVE
           at vintage: <the exact pin the rows were computed at>
           $ <the command(s) a reader runs to re-derive the rows, verbatim>
           note: <folds or environment the recipe needs, e.g. TZ=UTC>
[rows...]                                  # k may be 0 -- that is a RESULT, not an absence
```

**What binds and what does not.** (i) `reproduce` is OPTIONAL: a stratum without it is still contract-valid, and no
consumer may treat its absence as a defect of the stratum. (ii) When present it carries its own CLAIM (`rail-reproducible`
when the recipe is a comp-tool invocation the rail admits; `host-reproducible` when it needs host state such as git history
at a pin; `not-reproducible` when the stratum cannot be re-derived and says so) -- a recipe without a claim is not a
recipe. (iii) The recipe names the VINTAGE the rows were computed at, never "now": a reader re-running it at HEAD is
running a different question. (iv) Section 5a stands unchanged: `reproduce` is a fact about the input, never a rank,
weight or sort key. (v) Nothing about the model's job changes (section 6): the model never runs a recipe; a reader does.

**Why the field earns its place (the OS-s-11 measurement, 2026-09-05):** one deterministic row of stratum C was taken,
its recipe run as printed at the pin, and the rows re-derived by a fold written independently of the runner -- 17 of 17
identical -- with a negative control (the recipe's window corrupted from 90 days to 2) producing 107 rows instead of 17, so
the comparison can fail. That is the property FWD-3 of NFRA_OUTSET asks for ("a reader has followed one line back and
reproduced it"), and it is expressible only if the row carries the recipe. Reach, stated so the field is not over-read:
4 of 4 deterministic strata CARRY a recipe at HEAD; 1 of 4 has a DEMONSTRATED reproduction; the other three are untested
(D, B-host) or untestable on this fabric until something publishes to the seam and the runner's role can read it
(NFRA_OUTSET W2-S18, W1-S19, W2-S15).

**Denominator of this amendment:** one field added; zero fields changed; zero status values added; the code at HEAD and
this document now agree on the shape. Recorded on NFRA_OUTSET adjudication row C-S3 as W2-S20's remedy.

## 6. Explicitly NOT the model's job

- Computing any stratum (deterministic, always).
- Deciding which fields are proposable — allowlist enforced runner-side (`:26`).
- Narrating Group A rungs 1–3 or C's uncited queue — those are compiled lists.
- Discovering entities. It selects from D's canon; it never coins a name.

---

## 7. Open parameters — **ALL THREE RULED BY ANDREW 2026-08-05. No longer assumptions.**

| # | Parameter | RULING |
|---|---|---|
| 1 | Group B trailing window | **14 days, CONFIRMED.** Plus a new requirement: the trend section must be **VISUALLY SEPARATED** in the report — a reader must not take a weekly-moving number for a daily event. That misreading is the kind that gets acted on. |
| 2 | D-first sequencing | **CONFIRMED, AMENDED.** The **scope correction comes first** — governance records off the resource axis — *then* D. Order is load-bearing: building the two-field split first lands a vertical field **68% empty**, which reads as a broken resolver and is how a correct design gets abandoned. |
| 3 | Cost / egress | ⛔ **BASIS VOID — SEE §7a. THIS ROW'S RULING NO LONGER HOLDS.** ~~DEFERRED TO MEASUREMENT: tomorrow's 13:00Z fire is instrumented for real token counts; the subdivision is priced from those.~~ |

### 7b. AMENDMENT 2026-08-06 ~19:00Z — **PARAM 3 IS NOW PRICED.** Measured on a full local run.

*Andrew-directed. Supersedes §7a's UNPRICED status; §7a is kept below because the reason the basis
went void is the durable lesson, not the number.*

**The new basis §7a specified — "price from the FIRST SUBDIVIDED RUN" — has been satisfied.** The
subdivided pipeline was built and run end-to-end LOCALLY, call by call, against live estate data
under Andrew's per-use egress word (harness: `kimi_pipeline.py`, this lane's deliverables).

| | monolith | subdivided | ratio |
|---|---|---|---|
| calls | 1 | 23 (1 compile · 1 narrate · 4 detect · 17 author) | — |
| input tokens | 20,614 | 64,198 | 3.1× |
| output tokens | 8,872 | 91,060 | 10.3× |
| wall time | 260s | 2,437s | 9.4× |
| **adoptable candidates** | **1** | **17** | **17×** |
| **output tokens per candidate** | **8,872** | **5,357** | **0.60×** |

>> **THE RATIO THAT MATTERS IS THE LAST ROW. Gross cost rises ~10×; COST PER FINDING FALLS ~40%.**
A subdivision priced on total spend looks 10× worse and is 1.7× better per unit of the thing we
actually want. **Andrew accepted the gross trade explicitly before this table existed** (verbatim,
2026-08-06: *"I'm fine with more wall clock time and better audit"*) — the per-finding figure is
therefore a confirmation of his call, never the argument that produced it. <<

**A CORRECTION I OWE, and it points the wrong way for my own case:** I told Andrew that splitting the
call would let each call "reason over a bounded question," implying reduced reasoning overhead.
**Measured, that is FALSE.** Per-call reasoning ran **84.9%–98.4%** of completion tokens, against the
monolith's 90.2%. **That is how kimi-k3 behaves; it is not a symptom of bundling.** The subdivision
buys **quality and inspectability, not efficiency** — and nothing downstream may be sized on an
expected reasoning drop.

**SIZING, derived rather than assumed** — observed reasoning spend on real DETECT calls:
7,674 / 8,597 / 11,729 / 12,609 / **15,572**. A 12,000 ceiling **starved group B** (`finish_reason:
length`, 11,997 of 12,000 on reasoning, content 0 bytes) and the runner recorded it as
**`candidates_raw: 0`**. At 32,000 the same call returned `stop` with **10 candidates**.
>> **THE STARVATION WAS NOT COSTING AN ERROR MESSAGE — IT WAS HIDING TEN FINDINGS BEHIND A NUMBER
THAT LOOKED LIKE A CLEAN DAY.** << Set per-call ceilings generously: unused headroom is free (the
monolith used 8,872 of 32,000 and stopped clean), and a tight ceiling fails **silently and in the
direction of false confidence.**

**Params 1 and 2 remain unaffected.**

---

### 7a. AMENDMENT 2026-08-06 — PARAM 3's BASIS IS VOID. THE PARAMETER IS **UNPRICED**.
*(SUPERSEDED by §7b above — the parameter is now priced. Retained because the failure mode it
records is the point: a ruling whose basis is destroyed degrades to an OPEN QUESTION, silently.)*

*Found by `1.0.0_SA_CTO~B`. Andrew-directed amendment. This corrects MY OWN document.*

**What the row claimed:** cost/egress was *"no longer an assumption"* because the 2026-08-06 13:00Z
fire would be instrumented and would yield real token counts to price the subdivision from.

**What happened:** the fire **timed out** (`KIMI_TIMEOUT`, 618s against a 300×2 ceiling). **It produced
ZERO token counts** — the instrumentation reads `usage` from the response body, so a call that never
returns emits nothing. **The measurement the ruling rested on does not exist.**

> ⚠ **SO PARAM 3 SILENTLY REVERTED FROM A RULING TO AN ASSUMPTION, AND THIS DOCUMENT WENT ON
> ASSERTING IT WAS SETTLED.** That is §5a's map-not-territory shape occurring **inside the document
> that legislates against it** — the second time in two days, the first being the retracted
> "first durable record" claim. **A ruling whose basis is destroyed does not degrade to a weaker
> ruling; it degrades to an OPEN QUESTION, and it does so SILENTLY unless someone re-reads the basis.**

**STATUS: UNPRICED.** Not estimated, not deferred-to-a-scheduled-event, not carried at a lower
confidence. **Open.**

**NEW BASIS — price from the FIRST SUBDIVIDED RUN** (`CTO~B`'s recommendation, adopted):

- The subdivided architecture is **the thing being priced**. Pricing it from a monolith run would
  measure an architecture scheduled for deletion — **the same error as the vetoed bridge, one level
  up**: a correct measurement aimed at something we are removing.
- **Do NOT re-run the monolith to obtain counts.** That is the reflex this whole day argues against.
- The first subdivided run yields per-call counts, which is the grain the pricing question actually
  needs (cost scales with N calls, not with one).

**THE ONE REAL NUMBER WE DO HOLD**, from the Andrew-authorised probe (2026-08-06 ~13:55Z, same
endpoint / model / budget / ceiling, 31-char prompt): **returned 3.4s · prompt_tokens 92 ·
completion_tokens 51 · reasoning_tokens 35.** It is a **per-call floor and a reasoning-overhead
datum (~69% of completion on a trivial task)** — a constraint on per-call sizing. **It is NOT a
price**, and a single point with a large constant term cannot be extrapolated to a rate.

**Params 1 and 2 are UNAFFECTED** — the 14-day window and the scope-correction-first sequencing were
ruled on their own merits and neither depended on the token measurement.

**Also ruled:** the corpus budget is **INVERTED** — the model gets the full corpus and a *summary* of
resources, not the reverse. The git half is deterministic and already printed in full in the report
body; the corpus is the one input the model cannot reconstruct.

### 7a. Superseded — the original assumptions, kept for provenance

1. **Trailing window for Group B = 14 days.** Divergence and half-life are meaningless in a 24h
   window. Consequence: part of the daily report becomes a slow-moving *trend* section that changes
   weekly, not daily. **Product decision, not mine.**
2. **D sequenced first.** It changes what every other call can say.
3. **Cost/egress.** Subdivision multiplies vendor calls per day, and B and C require real computation
   (`--overlap-sweep` across a population; `federated` hits Trino). **Andrew's call, not mine.**

## 8. What I am NOT specifying — lane discipline

I am not designing the API layout, the chunking mechanism, the retry semantics, or the runner's
internal structure. That is CTO~B's lane with CTO on the architecture gate. **This spec states what
the model must be given, what each call must be asked, and what must never be silently lost** — the
verification requirements, not the implementation.

-- 3.0.0_SA_CVO
