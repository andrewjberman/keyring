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

⛔ **CARD 8 UPDATE (RULED ~18:15Z): D8 SITS FIRST.** This spec originally recorded card 8 as still
open, because a blanket approval of a declared non-recommendation authorizes nothing. Andrew has
since ruled it explicitly. **D8 precedes D3 in `/self-drive`.**

---

## 0 · AMENDMENT ~19:0xZ -- STEP 4 IS THE PRD, AND THE THREE FRAMINGS ARE RECONCILED

**ANDREW-DIRECT, relayed verbatim by `1.0.0_SA_CTO` (msg 92454), filling a gap that seat flagged in
this document before he answered:**

> *"Step 4 is the PRD, you need to write it, that's what gets decomposed by COO. The premise is that
> we basically read the briefing from CRO and align on the endpoint, and the PRD is the document
> that takes a briefing and converts it into a project arc with a defined outcome."*

⛔ **THIS IS A RE-MAP, NOT JUST A FILL, AND THIS DOCUMENT HAD THE OLD NUMBERING.** The original
transcript put the PRD at step 2 and made step 4 *"the handoff of the endpointed PRD to COO."*
Andrew has moved it: **step 2 is ENDPOINT ALIGNMENT, step 4 is THE PRD ITSELF**, and the handoff is
what step 4 produces rather than a step of its own.

```
  1  CRO brief                 4.0.0_SA_CRO
  2  endpoint alignment        1.0.0_SA_CTO      (/endpoint --forward, now BUILT)
  3  register + fabric         1.0.0_SA_CTO
  4  THE PRD                   1.0.0_SA_CTO      <- the handoff artifact to COO
  5  decomp + lens battery     2.0.0_SA_COO
  6  TO ISSUANCE               2.0.0_SA_COO      <- THE ONLY GATE
  7  worker + surprise rows    the worker
  8  compile                   3.0.0_SA_CVO
  9  disposition               3.0.0_SA_CVO
 10  route + loop_target       3.0.0_SA_CVO
```
⭐ **TWO WORDS IN HIS PHRASING ARE LOAD-BEARING** (`1.0.0_SA_CTO`'s reading, adopted): **"PROJECT
ARC"** -- a PRD listing requirements without an arc gives a decomp no shape to follow; and **"WITH A
DEFINED OUTCOME"** -- that is step 2's endpoint landing INSIDE the PRD, which is exactly what step
10's scope-change route reads back. **The endpoint section is the SEAM between steps 2 and 4.**

### THE 5-STAGE / 10-STEP / dep_stage DIVERGENCE -- RECONCILED, NOT SUPERSEDED

`1.0.0_SA_CTO` correctly named that `org/ref/DIRECTIVE_EXECUTION_PIPELINE.md` describes **FIVE
STAGES** while this spec describes **TEN STEPS**, and declined to assume which supersedes.
**Neither does. They are different GRAINS of one process and they nest cleanly:**
```
  steps 1-2   PRE-REGISTRATION inputs (feasibility + endpoint) -- they PRODUCE the decision to
              register, so they do not violate stage 1's "nothing else exists until this does",
              which is about the PROJECT, not about thinking
  STAGE 1  REGISTER        = step 3        dep_stage REGISTERED
  STAGE 2  PRD             = step 4        dep_stage PRD
  STAGE 3  DECOMP -> TOs   = steps 5-6     dep_stage DECOMP -> EXECUTING
  STAGE 4  EXECUTE         = step 7        dep_stage EXECUTING
  STAGE 5  CHANNEL         = steps 8-10    dep_stage ROUND_CLOSE -> CLOSED
```
**No document needs to be retired. The ten-step map is the FINE grain of the five-stage pipeline.**

⛔ **AND RECONCILING THEM CAUGHT A DEFECT IN MY OWN GATE.** See s.5.

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
  REFUSED (1)      comp-similar -- SUPERSEDED 2026-09-02. See the amendment below.
```

⛔ **AMENDMENT 2026-09-02 (`3.0.0_SA_CVO`) -- THE REFUSAL'S STATED GROUND WAS HALF FALSE WHEN I WROTE
IT, AND THE OTHER HALF IS NOW DISCHARGED. BOTH CORRECTIONS BELONG HERE BECAUSE THIS IS THE CARRIER
OTHER SEATS READ.**

**What the original text got WRONG (my error, propagated to two seats).** *"NO denominator on either
carrier"* was **FALSE**. `comp-similar` always printed a rich coverage denominator in `supersede` and
`cluster` -- `comp_similar.py:470` and `:494` print `cov["note"]`, and `coverage()` returns ten
fields. The parenthetical evidence (`--json` top-level keys `['arn','neighbors']`) was **correct but
scoped to the QUERY modes only**, and I generalised one mode's shape to "either carrier". CTO's
92486 and COO's manifest both inherited the wrong headline from this line.

**What was RIGHT: no VINTAGE, in any mode.** That was the whole true finding.

**DISCHARGED @`b8a73cc064` (`0.8.0_AE_CloudComp`), verified by this seat at source AND exercised:**
```
  D1  vintage rode comp-kuzu's STDERR; _kuzu_json read stdout only. Fixed in coverage() -- NOT at
      the comp-similar surface -- because coverage() has TWO consumers (comp_similar.py and
      0.7.0_AE_CloudOps' build_w1_cards.py:96). The defect was in what they SHARE.
  D2  all four modes now emit coverage, human and --json. Consumers censused first.
  D3  self-test 9/9, red-first, two planted mutants, byte-exact sha256 restore.
```
Exercised on THIS device 2026-09-02 ~15:0xZ, first line of `comp-similar cluster`:
`corpus built: 2026-09-02T14:20:11 (age: 0.8h), DB kuzu_nessie_db` over a 1,868-resource denominator.

**ALSO WITHDRAWN: my own claim that the corpus modes do not run on the laptop.** I measured a 180s
comp-kuzu timeout at ~13:53Z and reported it as a device condition. **The corpus was built at
14:20:11Z -- 27 minutes AFTER that run.** I had measured a cold DB building inside my own call.
There is no laptop-local retrieval defect; a cold kuzu build can exceed the 180s ceiling, which is a
cold-start property.

**TWO BOUNDS THAT TRAVEL WITH ANY USE, neither discharged:**
- **`b8a73cc064` is LOCAL** until an integrator runs. A seat pulling from `origin` still gets the
  undisclosed tool. **Check the vintage line renders before citing it.**
- **The vintage dates the KUZU DB, not the AWS estate behind it.** A fresh corpus is not a fresh
  estate.

**ADMISSION IS NOT RE-GRANTED BY THIS AMENDMENT, AND THAT IS DELIBERATE.** This line records that the
GROUND is gone; which lenses a given project's preflight admits is the ISSUING seat's call
(`1.0.0_SA_CTO` for ETFS_GUARDRAIL). **A spec that silently re-admitted a tool would be the same
stale-record-with-authority hazard in the other direction.**
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

## 5 · A DEFECT IN MY OWN GATE, FOUND BY RECONCILING THE FRAMINGS ABOVE

**`dep_stage` HAS SIX RATIFIED VALUES. MY GATE ACCEPTED SEVEN.**

```
  RATIFIED (COO Rule-24 record DEP_STAGE_ENUM_RULE24_RECORD_20260821.md:41-46):
    REGISTERED | PRD | DECOMP | EXECUTING | ROUND_CLOSE | CLOSED
  MY GATE CARRIED, until 2026-09-01 ~19:0xZ:
    REGISTERED | PRD | DECOMP | TOS_CUT | EXECUTING | ROUND_CLOSE | CLOSED
```
`TOS_CUT` **was never ratified.** The record transitions `DECOMP -> EXECUTING` directly on *"first
TO cut from a decomp cell"* -- there is no intermediate state, and the record's postulate work says
why. **I introduced it from the ten-step map's step 6 rather than from the enum's authority.**
Rule 24 binds any schema an agent **AUTHORS OR ADOPTS**, and this was a bad ADOPTION by the seat
that mandated the rule.

>> ⛔ **AND THE CONSEQUENCE IS THE SHARP PART: THE WRONG VOCABULARY SUPPRESSED A REAL FINDING.**
`--sweep` reported `BRIEF x2` as off-enum and said **nothing** about `TOS_CUT x2`, which is equally
off-enum -- because the tuple had been widened to admit it. **A GATE WHOSE VOCABULARY IS WRONG
CANNOT SEE THE VIOLATIONS THAT MATCH ITS OWN ERROR, AND IT REPORTS CLEAN ON EXACTLY THOSE.** <<

**MEASURED, before and after the one-line correction:**
```
  before   off-enum surfaced: BRIEF x2                    (2 of 33 populated)
  after    off-enum surfaced: BRIEF x2 + TOS_CUT x2       (4 of 33 populated)
```
**The correction DOUBLED the off-enum count** and it did so on a population that had been swept and
reported CLEAN on that axis twice today. Controls: 8, all pass -- `TOS_CUT` now refused, all six
ratified values pass, `BRIEF` still refused (regression guard).

⚠ **BLAST RADIUS, disclosed rather than quietly patched:** the bad value was printed back in every
refusal message this gate issued, and went out in **two fabric broadcasts** to 9 seats. A correcting
broadcast was sent. **Owner of the two `TOS_CUT` project JSONs: not me** -- surfaced, not chased.

---

## 4 · WHAT IS STILL NOT MECHANICAL, STATED PLAINLY

**The loop is gated at exactly ONE hop of ten** -- step 6. Steps 1-5 and 7-10 bind by reading. This
spec moves two more requirements INTO that one gate (fabric, preflight evidence) and adds a notifier
at step 8. **It does not make steps 7-10 refuse anything.** Card 2's mandate is the next build, and
it lands on the investigation/remediation ROW validators, not on this gate.

**A loop with one gate is not a deterministic loop. It is a well-documented convention with a
checkpoint in it.** That is the honest state, and it is better than it was this morning.
