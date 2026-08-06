# CALL LAYOUT — Kimi subdivision (implementation lane)

**From:** `1.0.0_SA_CTO~B` (runner + design owner) · **To:** `3.0.0_SA_CVO` (contract verification),
`1.0.0_SA_CTO` (architecture gate).
**Authority:** Andrew-direct 2026-08-06 ~1414Z, VERBATIM: ***"No bridge, move to the subdivision now."***
Preceded by: *"I thought we already established that this should be broken up into multiple calls,
where I would imagine that each call would have its prompt in a step function manner."*
**Answers:** SPEC `@58505c291` §8 — the lane CVO explicitly did not specify (API layout, chunking,
retry semantics, runner structure).
**Status: LAYOUT FOR VERIFICATION. NO CODE WRITTEN.** Per my commitment to CVO: the layout comes
first so it is verified against the pre-registered contract, not a post-hoc bar.

---

## 0. THE THING THAT CHANGED TODAY AND IS NOT YET IN THE SPEC

**SPEC §7 parameter 3 says cost/egress is "DEFERRED TO MEASUREMENT — tomorrow's 13:00Z fire is
instrumented for real token counts; the subdivision is priced from those."**

**That fire produced no token counts.** It timed out, and the instrument was response-conditional, so
it went dark on exactly that path. **The stated basis for resolving parameter 3 no longer exists**,
and §7 currently reads as though it does. I am not proposing a substitute here — I am flagging that
one of three "no longer assumptions" has quietly reverted to an assumption, and a spec that says a
question is *answered by a measurement that never happened* is the map-not-territory shape §5a warns
about, occurring inside the document that warns about it.

What we DO have is CVO's Andrew-authorised probe (~13:55Z) — the first real token data on this
endpoint: **31-char prompt -> 3.4s, prompt_tokens 92, completion_tokens 51, of which 35 REASONING.**
**~69% reasoning overhead on a request whose answer was "OK."** That single datum constrains §5 of
this document more than anything else we hold.

---

## 1. THE DESIGN CLAIM I MOST WANT VERIFIED

**Subdivision silently converts a BINARY into a FRACTION, and the spec's own §5 law then binds the
call layer.**

Today the AI half is one call: PRESENT or ABSENT, and "ABSENT" is honest because nothing ran. With
N calls, a run where 5 of 7 succeed has no honest binary. **If we emit `ai_section: PRESENT` over a
partial run, we have rebuilt `degraded_sources: []` one layer up** — the exact shape §5 forbids and
that CVO caught this morning: presence as the only predicate, byte-identical to health.

**Therefore the call layer inherits the stratum contract:**

```
ai_section: PRESENT | PARTIAL | ABSENT
ai_coverage:
  calls_planned:   <N>        # the DENOMINATOR, known before any call fires
  calls_succeeded: <k>
  calls_failed:    [{call_id, role, group, reason, elapsed_s, prompt_chars}]
  groups_absent:   [<group>]  # a DETECT group that produced nothing because it FAILED,
                              # explicitly distinguished from one that ran and found zero
```

**`groups_absent` vs "found zero" is the load-bearing distinction** and it is the same one twice: a
DETECT call that fails and a DETECT call that returns zero candidates are byte-identical downstream
unless we separate them. Zero candidates is a RESULT. A failed call is an ABSENCE OF MEASUREMENT.
Adjudicating a day as "nothing drifted" when a group never ran would be a false negative with a
sovereign-looking number on it.

---

## 2. CALL GRAPH, WAVES, AND CONCURRENCY

```
CALL 0  DETERMINISTIC COMPILATION  (no model)
        comp-tools -> strata, each with contract (SPEC 5): question, tool+args,
        vintage, denominator, rows. Group A rungs 1-3 + Group C uncited queue
        render as LISTS -- they never enter a prompt.
                    |
        +-----------+------------------------------------------+
        |                                                      |
   WAVE 1 (parallel, 5 calls, no interdependence)              |
        |                                                      |
   CALL 1 NARRATE          CALLS 2..5 DETECT (one per group A/B/C/D)
   in:  stratum summaries  in:  that group's stratum + corpus nuggets
        + headline changes      + CURRENT PROSE of the entities named
   out: plain-English brief out: {entity, field, why_suspect, evidence_ref}
        (Andrew audience)       CANDIDATES ONLY, NO PROSE
        |                                                      |
        |                       runner-side HARD FILTER: entity MUST be a
        |                       D-canon entity. A candidate naming a compiled
        |                       fallback label is REJECTED BY THE RUNNER.
        |                                                      |
        +-----------+------------------------------------------+
                    |
   WAVE 2 (parallel, 0..N calls -- fires ONLY on surviving candidates)
   CALLS 6..N AUTHOR+JUSTIFY, ONE PER CANDIDATE
   in:  that ONE entity's current prose + the specific evidence row + bearing nuggets
   out: {proposed_text, rationale, evidence_cited}
   runner-side HARD FILTER: evidence_cited must resolve to a real stratum row or nugget id.
```

**Why NARRATE is in wave 1 and not after DETECT:** SPEC §105-108 gives it stratum *summaries* and
headline changes, explicitly not proposals, and judges it on clarity alone. It has no data dependency
on detection. Putting it in wave 1 costs nothing and removes it from the critical path.
**Consequence to accept deliberately:** Andrew's brief will not mention that day's proposals. If the
narration SHOULD summarise what was found, it becomes wave 3 and the critical path grows by one call.
**That is a product question, not mine — flagging rather than silently choosing.**

**Zero-candidate day = 5 model calls.** Wave 2 is empty and costs nothing (SPEC §124).

---

## 3. CHUNKING — killing `[:60000]`

SPEC §5b: *"NO SILENT TRUNCATION. `[:60000]` must not survive into any call."*

**It does not survive, and mostly it becomes unnecessary rather than replaced.** The monolith needed
a 60KB dump because one call carried every group's evidence. Each DETECT call now carries ONE
group's stratum; each AUTHOR call carries ONE entity's prose plus one evidence row. The payloads are
small by construction. **The step function is the chunking mechanism** — that is what Andrew's
phrasing means operationally, and any residual chunker is a backstop, not the design.

For the backstop, where a single group's stratum still exceeds its call budget:

| | behaviour |
|---|---|
| **NEVER** | slice mid-structure; slice mid-row; emit a payload whose recipient cannot tell it was cut |
| **ALWAYS** | split on ROW boundaries only, and stamp EVERY chunk with the declared denominator: `rows k of M, chunk i of n` |
| **FAIL LOUD** | if rows cannot be split without breaking the contract (e.g. one row alone exceeds budget) -> that group emits `groups_absent` with reason `STRATUM_UNCHUNKABLE`, and the run continues |

The model must never be able to receive a truncated payload and believe it is whole. A chunk that
declares `rows 40 of 137, chunk 1 of 4` is honest; `[:60000]` is not, and today it silently dropped
14% mid-string.

---

## 4. RETRY SEMANTICS — per call CLASS, not one global rule

The terminal-on-timeout argument from the vetoed bridge belongs here, where it is a per-call decision
rather than a patch on a monolith.

| failure | retry? | why |
|---|---|---|
| **TIMEOUT** | **NO** | Structural. Same payload/endpoint/ceiling cannot go differently. On 08-06 the retry burned 5 minutes to reproduce the same nothing. |
| **5xx / reset / DNS** | **YES, once** | Genuinely transient; a second try is real work. |
| **MALFORMED body** | **YES, once** | Observed once as a formatting flake; twice is a prompt defect, not a retry case. |
| **LENGTH_STARVED** (`finish_reason: length`) | **NO** | Retrying an output-budget failure at the same budget is the definition of futile. Raise that CALL's `max_tokens` in the next vintage; the discriminated record already says so. |
| **Rejected by a runner-side hard filter** | **NO** | Not a transport failure. The model produced a real answer that violated the contract; that is a RESULT, recorded as a drop with its reason, and it is signal about the prompt. |

**A failure NEVER aborts the run.** It is confined to its own call, recorded in `calls_failed`, and
the surviving calls proceed. This is the mechanism behind §1's PARTIAL: one bad group must not cost
the day.

---

## 5. BUDGETS AND TIMEOUTS — sized against INDUCED GENERATION, never against `max_tokens`

**This section is written specifically to avoid repeating today's error, and CVO's correction is the
governing rule:**

> `max_tokens` **IS A CEILING, NOT A TARGET.** Size a call's timeout against the generation *its own
> prompt induces* — never against `max_tokens` in the abstract.

Proof that the abstract form is wrong, and it is why the bridge was misconceived: the probe ran the
SAME `max_tokens=32000` under the SAME 300s ceiling and **returned in 3.4s**. The pair is not
inconsistent; the pair *plus a 72k-char prompt* is.

**What we can honestly derive today: almost nothing, and I will not pretend otherwise.** Three data
points, two of them censored:

| prompt | outcome | usable? |
|---|---|---|
| 31 chars | 3.4s, 51 completion (35 reasoning) | yes — but a trivial task |
| ~60k chars, no corpus (08-05) | ~195s, ~2,146 content tokens | partly — content only, reasoning unknown |
| 72,344 chars (08-06) | >300s, TIMED OUT | **censored — tells us only "more than 300"** |

**So budgets are set by the OUTPUT CONTRACT, which we control, not by a fitted curve we do not have:**

| call | output contract bounds it to | `max_tokens` | first-run timeout |
|---|---|---|---|
| NARRATE | one plain-English brief | generous | generous |
| DETECT | a candidate LIST, no prose | moderate | moderate |
| AUTHOR | ONE field's prose + rationale | small task, **NOT a small budget** | short |

**Deliberately NO NUMBERS IN THIS TABLE.** Naming them now would be the bridge's mistake in new
clothing: a number invented ahead of the measurement, then defended. **The first subdivided run is
the measurement** — every call is instrumented (§6), and the numbers are DERIVED from it in a
follow-up vintage. I would rather ship one over-generous run that returns real per-call data than a
tuned run that returns another argument.

**The one hard constraint that IS derivable, from the probe:** *35 of 51 completion tokens were
reasoning for an answer of "OK."* **Do not size AUTHOR calls tight because their job is small.** A
call that writes one field still reasons first, and a tight budget starves content exactly the way
4000 starved the monolith on 07-30. **Small task does not mean small budget** — that inference is
the KIMI_EMPTY defect waiting to be re-derived per call, N times instead of once.

---

## 6. TELEMETRY — the one piece of the vetoed commit that carries forward

The `KIMI_CALL` / `KIMI_ATTEMPT` instrumentation (committed `1b925859a`, deliberately NOT deployed)
carries into this build per CVO's recommendation, now **per call**, because N calls need it more than
one did: **a failure in call 4 of 7 must be locatable from the MANIFEST**, without an engineer
opening an EC2 log — which is exactly what two seats had to do today.

Emitted for every call, on every path including the ones that return no body:
`call_id · role (NARRATE|DETECT|AUTHOR) · group · prompt_chars · prompt_tokens_est · max_tokens ·
timeout_s · elapsed_s · outcome · usage{...} when a body exists`

Design rule inherited from today's defect, and it is the reusable line:
> **An instrument that only fires when the call works cannot report the call not working.**
> *(3.0.0_SA_CVO, 2026-08-06 — kept verbatim, it is the most transferable thing produced today.)*

Everything above is known BEFORE the call or measured on our own clock, so none of it is
response-conditional.

---

## 7. SEQUENCING — what I intend to build first, and it is NOT wave 1

SPEC §7 parameter 2, Andrew-amended: **scope correction FIRST (governance records off the resource
axis), THEN D.** Order is load-bearing — building the two-field split first lands a vertical field
**68% empty**, which reads as a broken resolver and is how a correct design gets abandoned.

So the build order is:
1. **Scope correction** — governance records off the resource axis.
2. **D (canon entities)** — SPEC §86: *"Sequence D first"* among the groups. D is substrate, not a
   peer; until subjects have real names, every other call is phrased about `area:*` buckets and
   produces the output class Andrew has now rejected three times.
3. **Call 0** — deterministic strata with the §5 contract (denominator + vintage, no recency ranking
   per §5a).
4. **Wave 1** (narrate + detect) with per-call telemetry.
5. **Wave 2** (author) + the runner-side hard filters.

**Nothing in waves 1-2 is worth building before step 1-2 land.** That is the same trap as today at a
larger scale: building the mechanism correctly against subjects that do not yet have real names.

---

## 8. OPEN — I am NOT deciding these

| # | question | whose |
|---|---|---|
| 1 | **SPEC §7 param 3 (cost/egress) has lost its stated basis** — the instrumented fire returned no counts. Re-run to price, or price from the first subdivided run? | CVO to re-open with Andrew; I recommend pricing from the first subdivided run, since it is the thing being priced |
| 2 | **Does Andrew's brief need to mention the day's proposals?** If yes, NARRATE moves to wave 3 and the critical path grows one call. | Product — Andrew |
| 3 | **PARTIAL adjudication contract**: is a PARTIAL day adjudicable, or does any `groups_absent` make the day non-adjudicable like today's ABSENT? | CVO — this is the verdict contract, not the mechanism |
| 4 | **Interim runs before subdivision lands** stay AI-dark (08-07 onward). Accepted; recorded so it is not re-raised as a fire. | recorded, no action |

**Not built, not deployed, no code written.** No alert/alarm/SNS/SES/checker/monitor.
