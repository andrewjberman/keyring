# CANONICAL FABRIC WORKFLOW — the ten steps, their owners, and where the gates actually are

**AUTHORED:** `1.0.0_SA_CTO`, 2026-09-01, at Andrew's instruction to persist this concretely.
**STATUS (2026-09-03 ~03:2xZ): THE STATE OF RECORD GOVERNS.** Andrew memorialized the canonical workflow as
**L1–L10 WITH ROLE EXCLUSIVITY PER STEP** -- L1 `4.0.0_SA_CRO` only; L2–L4 `1.0.0_SA_CTO` only (no COO, no CVO);
L5–L6 `2.0.0_SA_COO` only (no CVO); L7 Tier-2 workers ONLY; L8–L9 `3.0.0_SA_CVO`, its FIRST engagement; L10
routing ONLY after every task order is complete AND every investigation is CVO-checked; `0.0.0_AB_MSTR`
integrates and never works a project -- record `org/tier0_exec/0.0.0_AB_MSTR/deliverables/ANDREW_DIRECT_20260903_024xZ_CANONICAL_WORKFLOW_L1_L10_STATE_OF_RECORD.md`
@`716a9bc7ce` (LD-0521; the transcript verbatim in its s.2; the drawing he called *"completely correct"* in
s.3). **Where this file's text and that record's s.3 differ, s.3 governs.** This file is being REWRITTEN from
the atom-decomp water test of its own mechanisms (run `canonical-fabric-workflow-spec__20260903T0305Z`, CTO,
on his word *"running atom-decomp on the spec itself to water test every single ref, gate, transfer, handoff"*);
until that rewrite lands, the step sections below are the 2026-09-01 text with their known-stale clauses noted
in the run. **SIBLING:** `org/ref/DIRECTIVE_EXECUTION_PIPELINE.md` keeps its MECHANISMS (they are what the gates
cite); its clauses *"certifier of record = CVO"* and *"CTO runs the decomp on a dark COO"* are **VOID** by that
record (dated markers in place there). The 2026-09-01 sentence *"I do not know which governs"* is RETIRED.

**WHY IT EXISTS — Andrew's diagnosis, and it is the whole design constraint:** *whole projects were
becoming thrashing debug sessions with no hierarchy.* The measured instance is `ADVI_PERFRP` on
2026-09-01: five seats, one producer question, **nine hypotheses raised and nine dead**, no frame
holding them.

---

## THE TEN STEPS

```
  #   OWNER             STEP                                  ENFORCEMENT
  --------------------------------------------------------------------------------------
  1   4.0.0_SA_CRO      the brief                             binds by reading
  2   1.0.0_SA_CTO      endpoint alignment                    binds by reading
  3   1.0.0_SA_CTO      register + fabric key                 binds by reading (checked at 6)
  4   1.0.0_SA_CTO      THE PRD                               binds by reading
  5   2.0.0_SA_COO      decomp + comp-battery preflight       binds by reading (checked at 6)
  6   2.0.0_SA_COO      TASK-ORDER ISSUANCE               >>> THE ONLY GATE <<<
  7   the worker        execute; append surprise rows         binds by reading
  8   3.0.0_SA_CVO      compile the channel                   NOTIFIER, never a gate
  9   3.0.0_SA_CVO      disposition                           binds by reading
 10   3.0.0_SA_CVO      route + loop_target                   binds by reading
```

**The PRD is the handoff artifact** between CTO and COO. Andrew: *"that's what gets decomposed by COO."*

### Step 1 — the brief (CRO)

The grounding document. Everything downstream traces to a line in it; an outcome with no line to
cite cannot be emitted at step 2.

### Step 2 — endpoint alignment (CTO)

**Andrew:** *"before even writing the PRD, we need to define where we need to go."*

Instrument: `/endpoint --forward <brief>` — Phase 0 of `.claude/skills/endpoint/SKILL.md`. It reads
the **brief**, never the task-order register: at step 2 there are no task orders, and a skill that
enumerates the register returns an empty set and calls it an endpoint.

⛔ **THE OUTPUT IS QUALITATIVE BY RULING.** Andrew: *"This does not have to be a deliverable
contract. It can be qualitative because we will not know enough about the quantitative mechanics at
this point."* **Do not invent numbers here** — a number fabricated at step 2 is treated as ratified by
every later stage because it is sitting in a document.
**Qualitative is not vague. The test is DISPUTABILITY:** *"advisors find it useful"* fails, because
nobody can contest it; *"an advisor reads a figure here they would otherwise have opened Black
Diamond for"* passes, and contains no number.

### Step 3 — registration + fabric (CTO)

**Andrew:** *"when it is listed to directives.yaml, we need to discuss at that point if this is going
to be a laptop fabric project or a site Z fabric project."*

`fabric` enum: **`laptop` | `site-z`**. **Andrew 2026-09-01, on scope: *"every project at next TO"*** —
the key binds **every** project the next time a task order is cut against it, not only newly
registered ones. Measured 2026-09-01: **349 of 349 project JSONs carried no fabric key**; D2's ten
were set that day, leaving 339, each acquiring the key at the moment someone is already editing that
file.

### Step 4 — THE PRD (CTO)

**Andrew, verbatim:** *"Step 4 is the PRD, you need to write it, that's what gets decomposed by COO.
The premise is that we basically read the briefing from CRO and align on the endpoint, and the PRD is
the document that takes a briefing and converts it into a project arc with a defined outcome."*

⭐ **Two words in that are load-bearing.**
- **PROJECT ARC**, not specification. A PRD that lists requirements without an arc gives a decomp no
  shape to follow — **and work with requirements but no arc is the thrash this loop exists to prevent.**
- **DEFINED OUTCOME.** The step-2 endpoint lands *inside* the PRD as a named section, because
  **step 10's scope-change route reads it back.** The endpoint section is the seam between steps 2
  and 4, and both are CTO's.

### Step 5 — decomp + preflight (COO)

Every `<preflight>` disposition carries **a denominator or an explicit blindness statement, on its
own line**. Accepted evidence tokens: any digit, or `BLIND` `COVERAGE` `DENOMINATOR` `UNRESOLVED`
`SCANNED` `NOT-FOUND` `REFUSED`. Both limbs are bounded to the disposition's own line — the next
tool's line is not scored as this tool's evidence.

⛔ **A vintage dates the corpus; it cannot tell you the lens was BLIND on your subject.** Specimen:
`comp-dataflow` on the file at the centre of the 09-01 incident returned *2 reads scanned, 2
unresolved-dynamic (blind)* — a vintage alone would have shown two rows and read like an answer.

⛔ **TWO SETS, NOT ONE -- corrected 2026-09-02 (CVO~A @`0d272d257c` R2; RC6).** The prior text listed one
"admitted" set and merely bounded `comp-adversary`, while `.tools/to-pipeline-gate.py:45`
`PREFLIGHT_TOOLS` already made `comp-adversary` one of THREE tools every new TO **must** disposition. Law
said seven-and-a-bound; the gate enforced three-and-different. **Distinguish what is LAWFUL TO SELECT from
what is REQUIRED OF EVERY TO, and do not call the admitted catalog mandatory unless the gate enforces it:**

```
  MANDATORY CORE (3)   comp-schedule · comp-iam · comp-adversary
                       = to-pipeline-gate.py PREFLIGHT_TOOLS. Every new TO carries a disposition for
                       each (RUN + denominator/blindness word on its own line, or
                       DECLARED-NOT-APPLICABLE + reason). This is what the gate REFUSES on.

  ADMITTED CATALOG (9) the core, plus: comp-blast · comp-dataflow · comp-trigger · comp-pipescript ·
                       comp-denytest · comp-similar
                       = tools LAWFUL to select for a decomp. Not every one is required of every TO.
                       comp-similar READMITTED 2026-09-02 on CVO~A's own exercise (self-test 9/9;
                       vintage + denominator on its disposition line; a failed resolution returns
                       an explicit non-answer). Admission is bounded to a version that prints both.

  ⛔ comp-adversary     SUBSTANTIVELY FIT, EFFECTIVE ADMISSION HELD (CVO~A) until its battery is
                       collectible by the standard runner (`sys.exit()` at module scope kills pytest
                       collection while the module battery prints 7/7). It is IN THE MANDATORY CORE
                       BY THE GATE AND HELD BY THE REVIEW AT THE SAME TIME -- and there is no truthful
                       disposition for an applicable-but-held tool (DECLARED-NOT-APPLICABLE is the
                       wrong grain; RUN erases the hold). CONSEQUENCE, stated rather than papered:
                       NO NEW CANONICAL TO PASSES STEP 6 ANYWHERE until the battery repair lands
                       (placed with 0.8.0_AE_CloudComp, gate 1.0.0_SA_CTO). That is the fabric-wide
                       critical path as of 2026-09-02.
```

>> **A gate's mandatory list and a spec's admitted list are two carriers of one quantity, and this file
   let them drift for a day.** When the gate changes `PREFLIGHT_TOOLS`, this block changes in the same
   commit, or the spec is describing a gate that does not exist. <<
**Two bounds to carry when using them, not footnotes:**
- **`comp-iam` cannot answer "is this denied?"** — unparsed deny statements include NEVER#1's
  cross-firm belts. **Silence from it must not be read as allowed.**
- **`comp-adversary` expands from CITED paths.** A thin decomp yields "0 uncited siblings" over a
  directory holding six live files. **Record the cited-path denominator: a 0-over-0 is an unrun
  check, not a clean bill.**

### Step 6 — TASK-ORDER ISSUANCE · **THE ONLY GATE**

Mechanism: `.tools/to-pipeline-gate.py` @`40bf270dec`. Three requirements refuse a non-conformant new
task order: the third admissibility limb, the step-3 fabric declaration, and the per-lens preflight
evidence. Override `# pipeline-override: <reason>`, audited.

>> **THE CHOKE-POINT PRINCIPLE — gate the NECK of the funnel, not every stage.** Nothing executes
   without a task order. A conformant TO requires a decomp reference, which requires the decomp,
   which requires the PRD, which requires registration. **One gate at issuance enforces the entire
   upstream funnel without taxing any other act.** Steps 1–5 are enforced BY IMPLICATION. <<

---

## THE SURPRISE / INVESTIGATION FLOW — steps 7 to 10

### Step 7 — the worker

**This line goes VERBATIM into every task order**, so a worker never has to judge:

> **"Did I have to do something the TO did not say to do, or could I not do something the TO said to
> do?"** If yes, append a row. If it is *"I noticed something interesting elsewhere"* or *"this could
> be better"* — **that is NOT a surprise and you must keep working.**

⛔ **THE WORKER JUDGES FORM. NEVER SIGNIFICANCE.** That is the load-bearing decision: significance is
the judgment a worker is worst placed to make mid-task and most likely to resolve as "not worth
interrupting." Validated against all **17 rows already filed on `ADVI_PERFRP`: zero exceptions.**

A row carries **`spec_asserts` + `world_is`** — both halves required.

### Step 8 — compilation (CVO)

`org/surprise_channel/surprise-watch.sh <serial> stream|once|status|reset`. Baseline seeded on the
real channel: **18 files, 190 rows, 17 projects.** Pre-existing rows are not notified — that is a
flood, not a signal.

⛔ **IT IS A NOTIFIER. It never gates, never blocks, never closes anything.** Local only: no SNS, no
SES, no email, no alarm, no freshness-checker.

⭐ **THE DESIGN POINT WORTH COPYING ELSEWHERE.** `inbox-watch.sh` achieves exactly-once delivery by
**moving** the message before echoing it — **and that move is what makes an orphaned inbox watcher a
THIEF.** This watcher is a **read-only watermark**: it never mutates what it watches, so **an orphan
of it cannot steal** — the worst it does is advance a state file nobody reads. Delivery is
at-least-once rather than exactly-once, **and that is the correct trade for a notifier: a duplicate
ping costs a glance, a stolen row costs the finding.** It also cannot race workers appending
concurrently.
⚠ **The state file is NOT an oracle for "CVO read it."** It records what the PROCESS emitted.
**SENT ≠ EMITTED ≠ READ**; only an agent-side ack is sound.

### Steps 9 and 10 — disposition, then route

`route` and `loop_target` are REQUIRED fields on a remediation row. **This is where the loop closes:**

```
  spec-error            ->  back to step 6
  decomp-invalidating   ->  back to step 5
  SCOPE CHANGE          ->  back to step 2
```

⛔ **The scope-change limb is decided by "does the PRD name this OUTCOME?"** With no named endpoint
that question has **no answer**, and the scope-change route **silently collapses into the spec-error
route** — every misrouted scope change then lands on COO as a task-order amendment instead of on CTO
as a PRD revision. **The loop degrades quietly rather than failing loudly**, which is the worst
available failure mode. That is why step 2's output must land in the step-4 document.

---

## ⛔ WHAT IS NOT MECHANICAL — stated plainly

**The loop is gated at exactly ONE hop of ten.** Steps 1–5 and 7–10 bind by reading.

⚠ **The upstream half is enforced by implication through step 6. THE DOWNSTREAM HALF IS ENFORCED BY
NOTHING** — and steps 7–10 are exactly where surprises are raised, compiled, dispositioned and
routed. A worker who never appends a row, a disposition never made, a remediation row with no route:
none of that refuses anything today.

**CVO's own summary, quoted rather than softened:**
> *"A loop with one gate is not a deterministic loop. It is a well-documented convention with a
> checkpoint in it."*

**The next build** is row validators on the investigation and remediation rows, landing the step
7/9/10 fields as mandatory. That is what gives the downstream half its first teeth.

---

## POINTERS

- `org/tier1_exec/3.0.0_SA_CVO/deliverables/SPEC_CANONICAL_LOOP_INCORPORATION_20260901.md` — the
  incorporation spec this document summarises. Names steps 1,2,3,5,6,7,8,9,10; **step 4 was defined
  by Andrew afterwards and is recorded here.**
- `.claude/skills/endpoint/SKILL.md` — Phase 0 `--forward` (step 2), Phase 1/2 (projection, reorient).
- `.tools/to-pipeline-gate.py` — the step-6 gate.
- `org/surprise_channel/surprise-watch.sh` — the step-8 notifier.
- `org/ref/DIRECTIVE_EXECUTION_PIPELINE.md` — **the five-stage framing. UNRECONCILED with this one.**
