# SPEC: incorporating the canonical loop -- what CTO and COO must change, exactly

**AUTHORITY:** Andrew-direct 2026-09-01, `/open-calls` (9 cards) answered **"All recs approved"**,
followed by *"get it done and spec whatever needs to be spec'd so CTO and COO can get it
incorporated."*

**READ THIS FIRST -- WHAT IS ALREADY MECHANICAL.** Three of the nine are BUILT and ENFORCING as of
this document. You do not need to agree with them; you need to satisfy them, because a commit that
does not will be REFUSED.

```
  BUILT + ENFORCING   the third admissibility limb        .tools/to-pipeline-gate.py   @40bf270dec
  BUILT + ENFORCING   the step-3 fabric declaration       .tools/to-pipeline-gate.py   @40bf270dec
  BUILT (notifier)    the step-8 investigations monitor   org/surprise_channel/surprise-watch.sh
```

⛔ **ONE CALL WAS NOT ANSWERED AND IS NOT IN THIS SPEC.** Card 8 (D3-vs-D8 ordering in
`/self-drive`) carried the explicit non-recommendation *"no recommendation with confidence -- this
turns on your business priority, which I do not hold."* **A blanket approval of a
non-recommendation authorizes nothing.** That call is still OPEN at Andrew. Do not sequence D3
against D8 on the strength of "All recs approved."

---

## 1 · AT `1.0.0_SA_CTO`

### 1.1 STEP 3 -- every project you register now needs a `fabric` key. **ENFORCING.**

```json
{
  "project_code": "EXAMPLE_CODE",
  "dep_stage": "REGISTERED",
  "fabric": "laptop"
}
```
`fabric` enum: **`laptop` | `site-z`** (case-insensitive on read; write it lowercase).

**What refuses:** a NEW `org/**/task_orders/*.md` committed against a project whose JSON has no
`fabric`, or a `fabric` outside the enum. The message names the enum. Override remains
`# pipeline-override: <reason>`, audited.

**Why it is at step 3 and not later:** Andrew named it there -- *"when it is listed to
directives.yaml, we need to discuss at that point if this is going to be a laptop fabric project or
a site Z fabric project."* MEASURED before building: **0 of 349 project JSONs carried any
fabric/device/host/site key.** The fork was being decided implicitly, by whoever picked up the TO.

⭐ **CORROBORATION you should know about:** the surprise-channel schema ALREADY carries a fabric
coordinate in its id pattern (`{PROJECT}-S{n}` laptop, `{PROJECT}-Z-S{n}` site Z), and it is LIVE --
`ETFS_POSITIONING` currently holds BOTH an `INVESTIGATION_v1.md` (14 rows) and an
`INVESTIGATION_v1.Z.md` (16 rows). The schema comment records the reason: **7 colliding ids, 14
distinct findings, zero identical**, measured 2026-08-21. So the fabric axis is not new -- it was
load-bearing downstream and undeclared upstream.

**PROSPECTIVE ONLY.** 349 projects lack the key. Nothing is back-filled; a project acquires it the
first time someone cuts a new TO against it. Per Andrew-direct: *"Dont get caught up on historical
TOs, this is a relatively new system and something we need to maintain now and prospectively."*

### 1.2 STEP 2 -- build the FORWARD form of `/endpoint`. **YOURS TO BUILD.**

**Do not write a new skill.** `.claude/skills/endpoint/` exists, is yours, and was Andrew-commissioned
2026-09-01 at your own terminal. Add a mode.

**The gap, stated precisely.** Phase 1 today asks *"if every active task order completes exactly as
written, what do we have?"* -- it **reads TOs in flight**. At step 2 there are no TOs; there is not
even a project yet. So the existing skill cannot serve the step-2 ask, which is *"before even
writing the PRD, we need to define where we need to go."*

**REQUIRED BEHAVIOUR of `/endpoint --forward <topic-or-brief-path>`:**
1. Reads the CRO brief (step 1), not the TO register.
2. Emits numbered **capability outcomes** in the same shape Phase 1 emits, each tagged
   `DESIRED | APPLIED | EXERCISED` and carrying its acceptance test.
3. **The outcome list is QUALITATIVE and that is deliberate** -- Andrew: *"This does not have to be
   a deliverable contract. It can be qualitative because we will not know enough about the
   quantitative mechanics at this point."* Do not force a contract here; forcing one is what makes
   the endpoint a guess wearing a schema.
4. Its output is written INTO the PRD as a named section, so step 10 can read it back.

⛔ **WHY THIS IS THE KEYSTONE AND NOT A NICE-TO-HAVE.** Step 10's routing fork has three limbs, and
the third -- SCOPE CHANGE -- is decided by *"does the PRD name this OUTCOME?"* **With no named
endpoint that question has no answer, and the scope-change route silently collapses into the
spec-error route.** Every misrouted scope change then lands on COO as a TO amendment instead of on
you as a PRD revision. **The loop degrades quietly rather than failing loudly**, which is the worst
available failure mode.

### 1.3 `/self-drive` stays scoped to OPEN CALLS ONLY

Ratified in the fork adjudication and unchanged. Andrew's protocol for a fork you hit: **one pass
with CVO, CVO adjudicates, you go or you pivot.** Today is the argument for the scoping -- a driver
that also investigates becomes a fifth debugger.

---

## 2 · AT `2.0.0_SA_COO`

### 2.1 STEP 5/6 -- the `<preflight>` block now needs EVIDENCE per lens. **ENFORCING.**

**Old form (still refused for a different reason -- bare not-applicable):**
```
<preflight>
comp-schedule: RUN
comp-iam: RUN
comp-adversary: RUN
</preflight>
```
**REQUIRED form -- every `RUN` carries a denominator or an explicit blindness statement, ON ITS OWN
LINE:**
```
<preflight>
comp-schedule: RUN -- 19 gates armed across 5 carriers; C5 NOT-DECIDABLE (334 project blocking keys)
comp-iam: RUN -- 395 .tf files / 3 trees; BLIND on 24 unattached policy blocks + 2 unparsed denies
comp-adversary: RUN -- 12 cited paths, 41 uncited siblings
</preflight>
```
Accepted evidence tokens: any **digit**, or any of `BLIND` `COVERAGE` `DENOMINATOR` `UNRESOLVED`
`SCANNED` `NOT-FOUND` `REFUSED`.

`DECLARED-NOT-APPLICABLE` still requires its reason on the same line. **Both limbs are bounded to
the disposition's own line** -- the next tool's line will NOT be scored as this tool's evidence
(that was a live bug, caught by its own control).

**Why:** measured across all 8 candidate lenses, runtime-OR-vintage admits 7 of 8 and is not what
separated the strong lenses from the weak ones. **A vintage dates the corpus; it cannot tell you the
lens was blind on YOUR subject.** Specimen: `comp-dataflow origin perfrp_emit_core.py` -- the file at
the centre of the 09-01 incident -- returned `2 reads scanned, 2 unresolved-dynamic (blind)`. A
vintage alone would have shown two rows and read like an answer.

### 2.2 STEP 5 -- the ADMITTED battery, and the one that is OUT

```
  ADMITTED (7)     comp-blast · comp-dataflow · comp-schedule · comp-iam · comp-trigger
                   comp-pipescript · comp-denytest
  REFUSED (1)      comp-similar -- emits NO vintage and NO denominator on either carrier
                   (--json top-level keys are exactly ['arn','neighbors']). Its self-test is 7/7:
                   the tool is not weak, it is UNDISCLOSED. Do not cite it in a preflight until
                   0.8.0_AE_CloudComp adds the provenance header its sibling already prints.
```
**Two bounds to carry when you USE them, not footnotes:**
- **`comp-iam` CANNOT answer "is this denied?"** -- 2 deny statements are unparsed and among them
  are NEVER#1's cross-firm Deny belts. **Silence from this tool must not be read as allowed.**
- **`comp-adversary` expands from CITED paths.** A thin decomp yields "0 uncited siblings" over a
  directory holding six live files. **Record the cited-path denominator: a 0-over-0 is an unrun
  check, not a clean bill.**

### 2.3 `comp-adversary` runs at STEP 5, and it is CHEAPER than Andrew thought

**Correction to the transcript's premise, measured at source.** Andrew weighed it as possibly *"too
operationally heavy"* because he understood it to spawn a parallel subagent (*"so that there's a
sub-agent that's effectively running at the same time"*). **It does not.** In `.tools/comp-adversary`:
`anthropic` 0 · `Agent(` 0 · `subagent` 0 · `api_key` 0 · `requests.post` 0. It shells only to `git`
and to local comp-tools. **It is deterministic, read-only and static.** The operational-weight
objection to putting it at step 5 does not survive the measurement.

### 2.4 STEP 7 -- give workers the trigger VERBATIM in every TO

One line, and it goes in the TO so a worker never has to judge significance:

> **"Did I have to do something the TO did not say to do, or could I not do something the TO said to do?"**
> If yes, append a row. If it is *"I noticed something interesting elsewhere"* or *"this could be
> better" -- that is NOT a surprise and you must keep working.**

**The worker judges FORM. Never SIGNIFICANCE.** Validated against all 17 rows already filed on
`ADVI_PERFRP`: zero exceptions.

### 2.5 STEP 7 -- the flow-ingestion defect gets its OWN carrier

Card 7, approved. Do not fold it into D2. The "22 D2 TOs" scoping frame weakened on 2026-09-01: a
mechanical open-count is now measured unsound on this corpus (**30 of 62 D2 status blocks carry BOTH
open and closed words; HEAD and TAIL disagree on 39 of 62**). Inheriting that bar inherits its
unreliability.

### 2.6 The drive cadence stays a KNOB

20 minutes default, changeable by Andrew. **Not a gate, and nothing should refuse on it.**

---

## 3 · AT `3.0.0_SA_CVO` (mine -- recorded so you can hold me to it)

### 3.1 The step-8 monitor is BUILT. `org/surprise_channel/surprise-watch.sh`

```
  surprise-watch.sh <serial> stream     persistent; run under the Monitor tool
  surprise-watch.sh <serial> once       one pass
  surprise-watch.sh <serial> status     the watermark table
  surprise-watch.sh <serial> reset      clear the watermark; next run re-baselines
```
**Baseline seeded on the real channel: 18 files, 190 rows, 17 projects.** Pre-existing rows are not
notified -- that is a flood, not a signal.

⛔ **IT IS A NOTIFIER. It never gates, never blocks, never closes anything.** Scope is exactly what
Andrew approved: local only. No SNS, no SES, no email, no alarm, no freshness-checker.

⭐ **THE DESIGN POINT WORTH COPYING.** `inbox-watch.sh` gets exactly-once delivery by MOVING the
message before echoing -- and that mv is what makes ITS orphan a **thief**. This watcher is a
**read-only watermark** watcher: it never mutates what it watches. **An orphan of this watcher
cannot steal** -- the worst it does is advance a state file nobody reads. Delivery is therefore
at-least-once, never exactly-once, and that is the correct trade for a notifier: a duplicate ping
costs a glance, a stolen row costs the finding. It also means it cannot race the workers who are
concurrently appending.

⛔ **The state file is NOT an oracle for "CVO read it."** It records what the PROCESS emitted.
SENT != EMITTED != READ; only an agent-side ack is sound.

### 3.2 Steps 7/9/10 -- the fields I will mandate next

Approved in card 2: mandate the three that are ALREADY schema-backed, and **defer the
markdown-to-JSON container swap** until I census the readers of the 17 existing INVESTIGATION docs.
The ROWS are already JSON against real schemas; only the CONTAINER is markdown, so the swap is cheap
but not yet SAFE, and I will not break 17 live documents to win a format argument.

```
  step 7   spec_asserts + world_is        both halves required on a row
  step 9   disposition                    enum EXISTS, unchanged
  step 10  route + loop_target            REQUIRED fields on a remediation row
                                          spec-error -> 6 | decomp-invalidating -> 5 | scope -> 2
```

---

## 4 · WHAT IS STILL NOT MECHANICAL, STATED PLAINLY

**The loop is gated at exactly ONE hop of ten** -- step 6. Steps 1-5 and 7-10 bind by reading. This
spec moves two more requirements INTO that one gate (fabric, preflight evidence) and adds a notifier
at step 8. **It does not make steps 7-10 refuse anything.** Card 2's mandate is the next build, and
it lands on the investigation/remediation ROW validators, not on this gate.

**A loop with one gate is not a deterministic loop. It is a well-documented convention with a
checkpoint in it.** That is the honest state, and it is better than it was this morning.
