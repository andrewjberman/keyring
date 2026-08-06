# CONSOLIDATION — the staged-run substrate

**Author:** `1.0.0_SA_CTO~B` (leading, Andrew-direct) · **Validator:** `3.0.0_SA_CVO` (as I go, **not
a gate**).
**Andrew-direct 2026-08-06, VERBATIM:** *"the task here is to figure out how to consolidate the best
pieces of these mechanics, simplify it down, and get rid of the rest. You lead the way on it, then
get CVO to validate as you go."*
**Preceded by:** *"make sure that we assemble the finished product from the pieces available."*

---

## 1. THE FINDING THAT SIZES THE WHOLE JOB

**It is not two systems to merge. It is ONE system missing TWO PROPERTIES.**

`deck_generation/engine/orchestrator.py` already records every stage as
`StageRecord(stage, kind, status, detail)` with `kind ∈ {deterministic, inferential}`, emitted to
`<name>.run_bundle.json` — *"Full audit trail: stages, resolutions, deterministic vs inferential"*
(`RUNTIME.md:38`). That is the STATE_FRICTION shape, already built, in another domain.

**But `stages` is a JOURNAL, not a LEDGER.** It is an append-only narration of what happened. It is
not keyed, so it cannot be asked *"is step X done?"* — and therefore it cannot decide what to run
next. **Everything CVO's rig genuinely adds is a consequence of that one absence.**

So the job is not "port a runner." It is: **give the existing record a KEY and a PREDICATE, and two
other properties fall out.**

## 2. THE SIMPLIFICATION — CVO's six mechanics collapse to THREE

Their six were correctly identified as absent from the estate. They are not six independent things:

| CVO's mechanic | collapses into |
|---|---|
| resume: skip completed steps from cache | **(1) ONE PREDICATE** — a step runs iff its deps are |
| gate: step blocked until dependency complete | complete and its own output is not. Gate and resume |
| | are the SAME condition read in two directions. |
| failure != zero (INSTRUMENT_FAILED / DETECT_FAILED) | **(2) ONE RULE** — a stage's outcome is a |
| per-call budget + starvation detection | STATUS, never a bare value. Starvation is `status=error` |
| | with a reason; it is not a separate mechanism. |
| runner-side rejection of model output | **(3) ONE HOOK** — a stage may declare a validator. |
| (canon universe + evidence citation) | Rejected output is DROPPED, with a reason, and COUNTED. |
| per-call prompt + response persisted individually | **not a mechanic — a LAYOUT RULE** (§4) |

**Six become three plus a layout rule.** That is the simplification, and it is not cosmetic: three
mechanisms have three failure modes to reason about, not six.

## 3. THE SUBSTRATE — additions only, no new system

**KEEP VERBATIM from the deck orchestrator** (this is the estate's existing vocabulary and it wins):
- `StageRecord(stage, kind, status, detail)`
- `kind ∈ {deterministic, inferential}`
- the artifact name **`run_bundle.json`**
- the dry-run convention (deck: `--no-assemble`)

**ADD, and only these:**

**(1) KEY + PREDICATE.** The run gains a lookup by stage id and exactly one decision function:

```
should_run(id, deps) = all(complete(d) for d in deps) and not complete(id)

complete(id) = ledger[id].status == "ok" AND the step's output artifact EXISTS
```
**Two conditions deliberately** — CVO's design, kept: the output file is written FIRST and the status
SECOND, so a crash between them re-runs the step. **A half-written file can never be mistaken for a
finished one, and the failure direction is re-do rather than skip.**

**(2) STATUS, EXTENDED — NOT REPLACED.** The deck already has `status ∈ {ok, error, started}`. Add
the missing states rather than inventing a parallel enum:
```
ok | error | started | skipped_deps_unmet | not_run
```
> **THE RULE: A STAGE'S ABSENCE, OR A BARE ZERO, IS NEVER A RESULT.** Zero candidates is a RESULT;
> a failed or unrun stage is an ABSENCE OF MEASUREMENT. They must not be renderable as the same thing.

**(3) OUTPUT CONTRACT.** A stage may declare `validate(output) -> (kept, dropped_with_reasons)`.
Drops are COUNTED and reported, never silent. This is where the canon-universe rejection and the
evidence-citation control live — as *instances of one hook*, not as bespoke code.

## 4. LAYOUT RULE — per-step artifacts beside the bundle

```
<run_dir>/
  run_bundle.json          <- the aggregate audit trail (deck's name, deck's shape)
  <stage>.prompt.txt       <- what was sent
  <stage>.response.json    <- what came back, raw
  <stage>.out.json         <- what was parsed/kept
```
The aggregate bundle alone cannot be walked call-by-call. **This layout is what let Andrew inspect
an inferential step in isolation, and it is the difference between an audit trail and an
inspectable one.**

## 5. GET RID OF — the explicit delete list

| delete | because |
|---|---|
| `GROUPS` / the A-B-C-D strata taxonomy | a parallel taxonomy over the ratified F1-F4 intent. Rule 24 (iii). Dead. |
| `run.json` / "ledger" as artifact NAMES | **`run_bundle.json` already exists.** Three names for one artifact is how a fourth gets built. |
| "Call 0 deterministic / Calls 1..N model" | **`kind: deterministic \| inferential` already exists.** Same split, worse words. |
| four-part contract attached at the STRATUM layer | wrong layer — it belongs at the battery layer (ruled 2026-08-06). |
| the vetoed timeout-bridge instrumentation | superseded: per-stage telemetry is a property of the substrate, not a patch on a monolith. |
| porting `kimi_pipeline.py` wholesale | carries the dead taxonomy in `step0_compile` and the parallel vocabulary throughout. **CVO reached this independently; both of us say do not port it.** |

## 6. WHAT THIS IS NOT

- **NOT a library extracted from `deck_generation`.** The deck code is deck-specific — architect,
  fitter, assembler and brand sit beside the orchestrator. **The PATTERN and the VOCABULARY
  transfer; the code does not.** Someone writes the generic version.
- **NOT a new abstraction layer.** If the substrate cannot be stated in the four pieces above, it has
  grown past its warrant.
- **NOT a gate on anyone.** CVO validates as I go, per Andrew. Findings land loudly and do not hold.

## 7. THE RISK I AM NAMING BEFORE IT HAPPENS

**The estate has now produced three names for one artifact and two vocabularies for one split — and
every one was written by an agent who believed they were building something new.** The tell, in
CVO's own words, is that the duplicated parts *"felt generic while I wrote them."*

> **A FOURTH DIALECT WILL BE WRITTEN WHILE BUILDING THE GENERIC VERSION, BY WHOEVER BUILDS IT,
> UNLESS THE NAMES ARE FIXED BEFORE THE CODE IS.**

That is why §3 leads with KEEP VERBATIM and §5 names the deletions explicitly. **The naming decision
is the load-bearing half of this consolidation; the code is the easy half.**

## 8. OPEN — for CVO's validation pass, not decided here

1. Does `should_run` need an explicit FORCE/invalidate path (re-run a completed step when its INPUT
   changed), or is deleting the run dir sufficient? My lean: sufficient, and an invalidation
   mechanism is where this design would start growing past §6.
2. Should the substrate live in `.tools/` as a comp-registered module, or beside the runner? It has
   two consumers already, which argues for shared — but a shared home implies a registration and an
   output contract. Not mine alone to decide.
3. Does the deck orchestrator ADOPT the additions, or only donate the vocabulary? Deck generation is
   a live product with its own owner; **this consolidation does not touch it without that owner.**
