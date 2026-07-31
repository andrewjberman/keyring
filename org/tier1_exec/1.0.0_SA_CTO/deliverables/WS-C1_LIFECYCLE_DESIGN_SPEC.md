# WS-C1 LIFECYCLE AXIS -- DESIGN SPEC (the D3 lifecycle/supersession vocabulary)

**Program:** NFRA_VELOCITY / CORE. **PRD:** `docs/architecture/NFRA_VELOCITY_CORE_PRD.md` WS-C1.
**Author + design owner + gate:** `1.0.0_SA_CTO~Z`. **Builds into the rule bank:** `0.8.0_AE_CloudComp~C`.
**Verify:** `3.0.0_SA_CVO~Z`. **Written:** 2026-07-31, site Z.
**Target artifact:** `org/modules/graph/NFRA_ONTOLOGY_RULE_BANK.yaml`, ADDITIVE section inside
`dynamic_rails.D3_contract_obligation`.

**REV 3 (~0325Z) -- THE AUTHORITATIVE REVISION. Rev 1 @bab75bba5, rev 2 @9d093cd94.**

**BUILD FROM THIS FILE, NOT FROM EITHER PRIOR COMMIT.** Rev 3 folds:
- **REV 2's content** -- `DORMANT` admitted, `revalidate_by` decay on every declaration, `EXPIRED`
  rejected (from `0.8.0_AE_CloudComp~C`'s disclosed divergent draft).
- **`3.0.0_SA_CVO~Z`'s commissioned DESIGN ATTACK -- 9 findings, 8 accepted, 1 BLOCKING.**
  Enum is now **7 values**: `ROLLING` collapsed to a derivation (F-8), `SUPERSEDED` renamed `LEGACY`
  and typed-violation `ZOMBIE/ORPHAN` renamed `SILENT-RESIDENT` (F-1/F-2, both tokens were already
  occupied on a ratified axis). Findings are marked F-n inline; none is paraphrased into anonymity.

> ### PROCESS FAILURE IN REV 2, DISCLOSED HERE BECAUSE IT CORRUPTED THE RECORD
>
> **Rev 2 only PARTIALLY landed, and its commit message overclaims what the file contained.**
> I issued parallel edits to this file in single tool calls; they raced against a shared base
> snapshot, **each reported SUCCESS, and the earlier edit's content was silently discarded.** So
> `9d093cd94` says *"DORMANT admitted as the 8th value"* while the committed S.2 table has **no
> `DORMANT` row** -- the S.5.1 gate exclusion landed, the enum row it referred to did not.
>
> **A commit message that describes changes its diff does not contain is a false record**, and it is
> the same shape this entire spec is pointed at: *an instrument reported success while the work did
> not land.* Rev 3 is written as ONE deterministic whole-file write for exactly that reason.
> **Operational rule taken from it: never issue parallel edits to a single file.**

> **VERSION-CLAIM CORRECTION (`3.0.0_SA_CVO~Z`, 030800Z).** Rev 1 said "rule bank head at authorship:
> v1.7". That was **true of the commit and already stale on disk** -- `~C` had begun editing the shared
> working tree to v1.8 in the same window. **THREE SEATS SHARE ONE CHECKOUT: "the rule bank is at
> v1.7" is only ever true of a REF, never of the file on disk, and my gate reads the disk.**
> Pinned pre-touch oracle for additivity: `8f8a63200`, md5 `37e16648dc965424b75c14677927a636`,
> 48217 bytes / 425 lines, `version "1.7"`. **Additivity is checkable only against a baseline pinned
> BEFORE the touch; they pinned it with minutes to spare, and the near-miss is the finding.**

**STATUS: DESIGN, not built.** Nothing here is landed in the rule bank, and no claim below is a claim
about live rule-bank content.

---

## S.0 THE SHAPING CORPUS (declared FIRST, per the sovereign fence)

The WS-C2 held-out fence (MSTR~Z relay 20260729T233721Z, Andrew verbatim 2325Z: *"this is setting up
the framework... the real test will be running ADVI_PERFORMANCE MDPF_GLOBAL and others"*) requires a
rail author to publish the corpus they drew from, because **a breached held-out set looks exactly like
a well-fitting rail and nothing reports it.** An unnamed shaping corpus is indistinguishable from a
breached one. Exhaustively:

1. The `gold/trigger-pending.json` trigger-marker class -- the specimen named in the PRD itself
   (landed in a kill list's top tier on "no object found").
2. The `comp-legacywriter` TRANSIENT-MARKER name-pattern stopgap (@d51f6b38a0) -- the thing REPLACED.
3. `0.7.0_AE_CloudOps~Z`'s never-yet specimen: `org/surface-check-ack-audit.log`,
   `org/mcp/comp-detect-gate-override.log`, `org/mcp/log-open-ok-override.log` (msgs 20260731T024616Z,
   024950Z) -- the source of the four-state partition in S.1 and of `EVENT_CREATED`.
4. ~~`audit-archive-invoker.py`'s output on THIS device, my startup run 024700Z -- an independent
   second observation of specimen 3.~~ **STRUCK AT REV 3 (F-5). THE INDEPENDENCE CLAIM IS FALSE AND IT
   IS MY OWN SPEC'S NAMED ERROR.** Specimen 3 came FROM audit-archive-invoker's output; item 4 IS that
   output. **Same instrument, same device, same declared MANIFEST, different clock -- a RE-RUN, not a
   second observation.** CVO~Z's own startup A.2 at 024851Z produced identical rc=1 / 11 findings and
   they declined to offer it as corroboration on the same grounds: **three agents, three runs, ONE
   instrument.** My own S.1(i) says *confirmation across correlated instruments is not independence*;
   this is the degenerate case -- one instrument -- and I wrote it into my corpus as a strength.
   **THE CORPUS IS FOUR SOURCES, NOT FIVE, and `EVENT_CREATED` rests substantially on a single
   instrument.** A stated weakness of that value, discharged at WS-C2 by a specimen from a DIFFERENT
   instrument.
5. The existing `D3_contract_obligation` section at v1.7 -- its four obligation types, its
   `intent_denominator_binding`, and its `coverage_boundary` law that an absent contract is an
   UNDECLARED obligation, never an absent one (S.4 is that law extended one axis).
6. **`org/modules/graph/keep-dormant.yaml`** -- the CANONICAL keep-dormant registry (CTO arch-gated
   RULING 1, `schema_version: 1`, **7 entries**, `revalidation_default_days: 180`) + its guard
   `org/modules/graph/comp_debt/dormant_guard.py`. Surfaced by `~C`; I then read the registry directly
   rather than accept the claim. **Its header states my own gap in the estate's words:** *"A deliberate
   belt and a corpse are IDENTICAL on every mechanical signal (both DISABLED, both 0-invocation, both
   0-consumer). Only the INTENT ANNOTATION separates them"* -- and *"a false-positive (decommission a
   deliberate belt) is THE named failure mode."* Produced `DORMANT` (S.2) and the decay rule (S.3.1).
7. **`~C`'s divergent draft enum**, disclosed unprompted before landing (msg 030718Z):
   `[ACTIVE, TRANSIENT, KEEP_DORMANT, SUPERSEDED, EXPIRED, RETIRED, UNDECLARED]`. One value was right
   (`DORMANT`), one a category error (S.2.3). **A second author deriving a different enum from the same
   PRD measures the vocabulary's underdetermination, and it was free.**
8. **`3.0.0_SA_CVO~Z`'s design attack** (msg 031515Z, 9 findings) and my source-confirmation of its
   token-collision claim at the pinned oracle.

**NOT drawn on, and deliberately not opened:** `ADVI_PERFORMANCE`, `MDPF_GLOBAL`. No surface of either
appears as a vocabulary example; no contract was authored to make a rail look expressive.
**CVO~Z falsified this rather than read it through and found NO unnamed source: THE FENCE HOLDS.**

> **FENCE-ADJACENT, OPEN (CVO~Z, from MSTR~Z 025421Z):** ESTATE WS-E1 has two unblock edges and edge 1
> is an ADVI_PERFORMANCE baseline confirmation -- **our held-out set is simultaneously the thing that
> must not inform the rails and the thing being actively worked estate-side. The separation today is
> two accidents, not a control.** CVO~Z is ruling; their ruling lands in this section. *A fence held by
> accident should say so, or a later reader will read intact and infer controlled.*

**Honest boundary:** the PRD's WS-C2 corpora (MSBEFF's 718 findings, the 210-incident
INCIDENT_TAXONOMY, the DEBTLOOPS shapes) have NOT been walked item-by-item against this vocabulary.
That walk IS WS-C2 and is the acceptance test, not a formality. **This spec is PROPOSED, not
validated.** Expect the enum to change there; **if it does not change at all, be suspicious of the
walk** -- and after F-1/F-3/F-4/F-6 that is now evidence about the BUILD, not about the enum.

---

## S.1 THE PROBLEM, STATED PRECISELY

**An existence check is being asked a question about lifecycle that existence cannot answer.**

A 404 / `head-object` miss / `test -f` false is ONE symbol standing for at least four distinct states
(partition contributed by `0.7.0_AE_CloudOps~Z`, adopted verbatim in substance):

| | state | shape of the absence over time |
|---|---|---|
| (a) | never existed and never will -- genuinely dead | flat |
| (b) | existed, was deleted -- dead, with history | terminal |
| (c) | exists as a lifecycle, absent RIGHT NOW -- **TRANSIENT** | **a TROUGH in a cycle** |
| (d) | will exist on first occurrence, which has not occurred -- **NEVER-YET** | **a PREFIX, monotonic** |

**Absence is not a state. It is a SET of states, and an existence check cannot partition it.**

**(i) The transient case is not fixable by re-observation.** Sample forever and you keep landing in
troughs; sampling harder makes you more confident and no more correct. This is why WS-E3's
>=2-CONFIRMED bar does not save it -- a transient key independently reads absent AND dormant AND
reader-less, so two confirmed signals agree and both are wrong. **Confirmation across correlated
instruments is not independence.**

**(ii) A two-value vocabulary is insufficient, and shipping one would be worse than shipping none.**
If CORE drafts `{TRANSIENT, DEAD}` and stops, state (d) has no home and every never-yet artifact is
misfiled -- most likely as DEAD, the default an existence check produces. We would fix the
trigger-marker class and *formalise* the audit-log class as a kill-list candidate, with the system now
more confident. **A neighbour bounds the vocabulary; a second instance only re-confirms a phenomenon
we already had.**

---

## S.2 THE ENUM: `lifecycle_class` (7 values)

Declared per contracted resource/process. Names the SHAPE of the thing's life, not its current phase.

| value | meaning | absent-at-rest | present-at-rest |
|---|---|---|---|
| `PERMANENT` | present from creation onward | **FINDING** (missing) | healthy; with a declared `cadence`, healthy iff vintage advances, else **FROZEN** |
| `TRANSIENT` | written -> consumed -> deleted; oscillates | **HEALTHY** | healthy iff dwell < `max_dwell`; **STRANDED** beyond |
| `EVENT_CREATED` | absent until a triggering occurrence; monotonic + append-only after | **HEALTHY** (zero occurrences) | healthy; a NON-APPEND edit is an INTEGRITY finding |
| `DORMANT` | deliberately inactive and deliberately RETAINED -- a rollback lever, a wired-not-armed path, an armed fallback | **FINDING** (a belt that vanished) | **healthy, AND zero traffic is ALSO healthy** |
| `LEGACY` | a live successor exists; the thing may still be READ | per successor | healthy to read; **a WRITE is LEGACY-WRITER** |
| `RETIRED` | decommissioned by ruling; absence is the correct terminal state | healthy (terminal) | **FINDING** (incomplete decommission) |
| `UNDECLARED` | no lifecycle declared | **UNKNOWN, LOUD** | **UNKNOWN, LOUD** |

### S.2.1 The polarity inversion -- the load-bearing consequence

**A detector cannot merely KNOW about `TRANSIENT` and skip it. It must run the OPPOSITE predicate.**

Absence is HEALTHY on two rows; presence is a FINDING on two rows. **A single-polarity existence
detector is wrong on four of seven rows** -- and wrong in the dangerous direction on `TRANSIENT`,
`EVENT_CREATED` and `DORMANT`, where it reports a healthy system as dead and proposes deleting a live
one.

**`DORMANT` needs a THIRD question the others do not: traffic-at-rest.** With a declared cadence, no
traffic is `FROZEN` (a finding); for `DORMANT`, no traffic is the DECLARED HEALTHY STATE -- a rollback
lever being exercised is not a lever. The estate's registry says it sharply: *"bare DISABLED / 0
CloudTrail / 0 invocations / no graph consumer / git-cold / un-queried"* are its
`tier_c_never_sufficient` signals -- **debt signals, never a keep on their own.** So an
existence-PLUS-traffic detector is STILL wrong here; only the declaration separates belt from corpse.

This is why the name-pattern stopgap is not a type system: **a skip-list SUPPRESSES; a type INVERTS.**
Suppression also loses `STRANDED` -- a transient marker written and never consumed is a dead pipeline
leg, and no current instrument can state it in either direction.

### S.2.2 Naming (`EVENT_CREATED`, not `NEVER_YET`)

`0.7.0_AE_CloudOps~Z` proposed `NEVER-YET` / `EXPECTED-ABSENT`. The class is named `EVENT_CREATED`
because **NEVER-YET names a PHASE, not a lifecycle shape** -- an enum mixing classes and phases will
not survive WS-C2. *They conceded with the sharper form of the argument: **their label EXPIRES.** The
moment an override fires, an audit log is no longer "never-yet" -- but its CLASS is unchanged and the
verdict a kill list needs is identical before and after. **A label that stops applying to an unchanged
artifact is describing the observation, not the object.*** The phase is not lost, it is unnecessary.

### S.2.3 `EXPIRED` and `ACTIVE` REJECTED (`~C`'s draft)

**`EXPIRED` fails the S.2.2 test: expiry is a STATE an obligation enters when its `expiry_condition`
evaluates TRUE, not a shape its life has.** The class is unchanged by the moment of expiry. It is
already carried as a derived state and is half of `debt` (S.5); promoting it would put one fact in two
places with no rule for which wins. **`ACTIVE`** is absorbed by `PERMANENT`, which says the same thing
while also stating what happens to the vintage.

### S.2.4 TOKEN COLLISION -- `SUPERSEDED` -> `LEGACY`, `ZOMBIE/ORPHAN` -> `SILENT-RESIDENT` (F-1/F-2)

**Source-confirmed by me at the pinned oracle `8f8a63200` (line 115 of 425; positive control run):**

```
variance.labels: [Canonical, Twin, Variant, Fork-Shadow, Superseded, Orphan]
  variance.Superseded := "same (position_key, dim_value); one supersedes the other"   <- a SIBLING verdict
  variance.Orphan     := "singleton, no sibling, no consumer"
```

Revs 1-2 proposed lifecycle `SUPERSEDED` and typed-violation `ZOMBIE/ORPHAN`. **Same rule bank, two
axes, the same two tokens, different definitions** -- against a settled prohibition here (v1.6
`@222b0c27c`, Andrew-ratified: never reuse a projection-language token; the C4 `terminology_law`
reserving `estate`). Renamed to `LEGACY` and `SILENT-RESIDENT`, **both verified ZERO occurrences at the
oracle before adoption.** `LEGACY` matches the violation it produces (LEGACY-WRITER); `SILENT-RESIDENT`
is the PRD's own phrase (*"a C-SILENT resident"*).

> **THE COLLISION WAS LOAD-BEARING -- F-2, BLOCKING.** S.5.1 gated the typed violation
> `ZOMBIE/ORPHAN`. It never gated **`variance.Orphan` -- a SEPARATE detector, already WIRED AND LIVE,
> which FLAGS on `"singleton, no sibling, no consumer"`.** That is precisely the at-rest signature of a
> `TRANSIENT` artifact. **So the exact danger S.5.1 exists to prevent -- a live transient reaching a
> kill list -- stayed reachable through a path my gate did not name, and the shared token is WHY it
> looked covered: a builder reading "ORPHAN is gated" reasonably believes both are.** A gate whose
> naming concealed its own bypass. *(CVO~Z weakened their own finding honestly: `variance` carries an
> `advisory:` clause, but it names Fork-Shadow explicitly and is SILENT on Orphan while `polarity:`
> says it FLAGS Orphan. I confirmed both lines at the oracle. The silence is the gap.)*

---

## S.3 EVERY DECLARATION MUST CARRY ITS OWN FALSIFIER (the anti-abuse gate)

**A lifecycle declaration SUPPRESSES findings. An unfalsifiable suppressor is a silencer, and a type
system that ships silencers is worse than no type system, because the silence now carries authority.**
Each value that flips a detector's polarity carries fields making the declaration itself CHECKABLE:

| value | required fields | what makes it falsifiable |
|---|---|---|
| `TRANSIENT` | `consumer` (**EXERCISED**, not merely resolvable), `max_dwell` (**BOUND to the consumer's D3 cadence**), `scope` | see S.3.2 -- both qualifiers are load-bearing and were added at rev 3 |
| `EVENT_CREATED` | `creating_event`, `event_observable` (where the occurrence is INDEPENDENTLY visible), `scope` | without an independent observable, "absence = zero events" is unverifiable and byte-identical to "the writer is broken" |
| `DORMANT` | `reason`, `rearm_condition`, `annotation_cite` (file:line), `revalidate_by` | **NOT INVENTED -- these are `keep-dormant.yaml`'s existing RULING-1 required fields, adopted verbatim.** `rearm_condition` is the one that matters: a belt nobody can state the re-arm for is not a belt |
| `LEGACY` | `successor` (live, EXERCISED), `intent_source` | makes debt computable; an unresolvable successor is not a supersession, it is a deletion |
| `RETIRED` | `retirement_ruling` (intent_source) | a retirement with no ruling is an outage with paperwork |
| `PERMANENT` | `intent_source`; optional `cadence` + `vintage_probe` | the default-looking value is still a claim from above, never the artifact's own config |

**`DORMANT`'s intent_source is `org/modules/graph/keep-dormant.yaml`, which already exists, is already
CTO arch-gated, and already enforces this discipline.** The axis does not replace that registry -- it
TYPES it. **Any build that copies the registry's entries into the rule bank has created a second copy
of a governed list: the frozen-enumeration defect.**

**Failure mode when a required field is missing or unresolvable: the declaration renders `UNKNOWN,
LOUD` -- it does NOT fall back to the declared value, and it does NOT fall back to `PERMANENT`.** A
half-declared lifecycle is the unfalsifiable case and must be noisier than no declaration, not quieter.

### S.3.1 EVERY DECLARATION DECAYS -- `revalidate_by` REQUIRED ON ALL VALUES

**The correction I most needed and did not find; the estate already had it.** `keep-dormant.yaml`
carries `revalidation_default_days: 180` and a per-entry `revalidate_by`, on RULING-1's reasoning:
*"A deliberate belt can DECAY into a true corpse... The registry is NOT write-once."*

Generalized: **`revalidate_by` is REQUIRED on EVERY declaration.** S.3's own logic, one step further:

> A falsifier verified ONCE and never again is a control that cannot fail. **A `TRANSIENT` declaration
> whose consumer was deleted last month is a perfectly-formed, fully-populated, permanently-silencing
> lie** -- it still names a consumer, the field is still present, and the detector it disarms will
> never fire again. **S.3 as originally written would have PASSED it.**

Past its window a declaration renders **STALE -- re-confirm or promote**, as the registry already does.
**STALE NEVER AUTO-PROMOTES TO A FINDING** -- that would make expiry a deletion warrant, the precise
failure this axis exists to prevent. Stale is loud and non-actionable, which is the correct pairing.

### S.3.2 THE `max_dwell` HOLE AND THE `RESOLVE`-vs-`EXERCISE` HOLE (F-3, F-4 -- the two I asked for)

**F-3 -- `max_dwell` was the only free scalar in the spec.** Every other required field is a POINTER
the graph must resolve (`consumer`, `successor`, `creating_event`, `event_observable`,
`retirement_ruling`, `cadence`, `vintage_probe`, `intent_source`). `max_dwell` was chosen by the
declarer. **ATTACK: declare `TRANSIENT`, name any resolvable consumer, set `max_dwell` absurdly large.
S.3 is satisfied to the letter, `SILENT-RESIDENT` is gated OFF, and `STRANDED` never fires -- a
permanent silencer wearing a falsifier.** That is S.3's opening sentence achieved *through* S.3. My own
`PERMANENT` row stated the cure and I did not apply it: *"never the artifact's own config."*
**FIX: `max_dwell` BINDS to the declared consumer's D3 `delivery_cadence` -- a transient key cannot
legitimately dwell longer than the cycle that consumes it.** D3 already carries `delivery_cadence`
(v1.7 :272), so the binding exists and costs nothing.

**F-4 -- the spec cited the rule and broke it one paragraph later.** S.3 required `consumer` be
"D2-RESOLVABLE" while also saying *"WS-C7's reachability limb must EXERCISE rather than RESOLVE."*
**A consumer that resolves in D2 but died six months ago still resolves.** Chained with F-3:
`TRANSIENT` declared -> `SILENT-RESIDENT` gated off -> `STRANDED` bounded by a declarer-chosen scalar
-> **a genuinely dead transient key is invisible to BOTH detectors. Strictly worse than today, which at
least reports it -- wrongly, but loudly.** **FIX: `consumer` and `successor` must be EXERCISED, not
resolved.** *This is `0.7.0_AE_CloudOps~Z`'s `aws.cmd` RESOLVED-BUT-CANNOT-RUN specimen, whose author
is item 3 of my own corpus. The lesson was in the room and I still wrote the weaker requirement.*

### S.3.3 PRODUCER-ASSERTED, NEVER OBSERVER-INFERRED

Binding on the build (`0.7.0_AE_CloudOps~Z`): the observer cannot distinguish (d) from (a) by looking
-- that is the entire problem -- **so a vocabulary requiring the OBSERVER to classify has MOVED the
impossible judgement rather than removed it.** Transience cannot be derived; it must be declared. Any
implementation inferring `lifecycle_class` from key names, directory position, or observed absence has
rebuilt the stopgap with more syntax.

### S.3.4 EVERY DECLARATION CARRIES AN EXPLICIT `scope` (F-6)

**The spec's flagship `EVENT_CREATED` specimen FAILED the spec's own S.3 requirement, and that is how
this was found.** The three override logs are gitignored (`.gitignore:68 *.log`) = **DEVICE-LOCAL**,
while `MANIFEST.txt` is a DECLARED path list (`audit-archive-invoker.py:115-123` -- plain lines, no
observation) carrying **no device qualifier.** So their lifecycle state DIFFERS PER DEVICE with no
shared oracle: absent here; on the primary laptop the override may well have occurred, and **neither
CVO~Z nor I can see it -- we are both on site Z.** By S.3's own `event_observable` rule that
declaration renders UNKNOWN, LOUD.

**The VALUE is right; the SPECIMEN cannot carry it.** `scope` already exists in the PRD's type tuple
`(rail, grain, plane, scope)` and the spec never said what scope a lifecycle declaration binds at.
**FIX: declarations carry an explicit `scope`; a device-local artifact is per-device or it is UNKNOWN.**
This is not a `type_tuple` amendment (S.6) -- it is a field on the declaration.

---

## S.4 `UNDECLARED` IS THE DEFAULT, AND ITS SCOPE IS BOUNDED

`UNDECLARED` renders UNKNOWN and LOUD -- never silently `PERMANENT`. D3's existing `coverage_boundary`
law extended one axis: *the ABSENCE of a declared contract is NOT the absence of an obligation.*

**Bounded, and the bound is part of the design.** Today essentially the whole estate is `UNDECLARED`;
if that made every detector render UNKNOWN, the axis would be unshippable and bypassed within a week.

> **`UNDECLARED` constrains what a tool may CLAIM; it does not disable what a tool may CHECK.**
> An existence check may still run and still report "absent." What it may NOT do is convert that into
> a lifecycle verdict -- dead, orphan, kill-list candidate -- without a resolvable `lifecycle_class`.
> It emits `ABSENT (lifecycle UNDECLARED)`: honest, actionable, cheap. Not `DEAD`.

**F-7 -- CVO~Z cleared the motive and found the real hole: STATING IS NOT ENFORCING.** They did not
find S.4 unmotivated (claim-vs-check is D3's law extended, as claimed). But S.6 said *"no detector is
rebuilt here"* and acceptance asked only that the bound be *"stated IN the rule bank."* **Ship that and
every consumer keeps emitting DEAD while a rule bank says they must not -- which makes the estate LOOK
governed. A DESIRED-only control reading as APPLIED: CLAUDE.md Rule 22a's exact class, and the one that
gets a real grant deleted as "unused."** **FIX: acceptance requires >=1 consumer ACTUALLY GATED**
(S.5.1 ranks which one); "stated in the rule bank" does not discharge it.

Ramp: announce-then-enforce. Declaration coverage is a printed denominator (`N of M contracted
resources carry a resolvable lifecycle_class`), never a boolean, and never prose here -- the gate owns
the count.

---

## S.5 DERIVATIONS LICENSED (definitional, never primitives)

- **debt** = `expired_obligation UNION legacy_with_live_successor`, where `expired_obligation` = a
  contract whose `expiry_condition` is TRUE and whose class is not `RETIRED`;
  `legacy_with_live_successor` = class `LEGACY` with an EXERCISED live `successor` AND a live writer
  still writing to it.
- **stranded** = class `TRANSIENT` AND observed dwell > `max_dwell` (itself cadence-bound per S.3.2).
  New -- not statable by any current instrument in either direction.
- **incomplete-decommission** = class `RETIRED` AND present at rest.
- **frozen-vs-stale** = a `PERMANENT` with a declared `cadence`: non-advancing vintage (frozen) vs a
  vintage advancing but behind cadence (stale).
- **ROLLING is a DERIVATION, not a class (F-8).** CVO~Z defended `ROLLING` as a genuine shape but
  charged it under the PRD's own law -- *every derived property defined as a derivation, never a
  primitive* -- since `ROLLING == PERMANENT + a declared D3 cadence`, with `FROZEN` falling straight
  out of its own required fields. **Collapsed on that reasoning.** They rated it medium confidence and
  would not have cut it on their confidence alone; I am cutting it on the PRD rule, which is mine to
  apply. *Flagged for WS-C2 re-test: if the walk finds a rolling artifact that is NOT expressible as
  PERMANENT+cadence, this collapse was wrong and the value returns.*

### S.5.1 The typed violations, and the gate

- **LEGACY-WRITER** = a D2 `WRITES` edge whose target carries `LEGACY` with a live successor, or whose
  obligation is expired.
- **CLOBBER** = two writers at one `(key, grain)` with no adjudicating `canonical_source` contract.
- **TRIGGER-MISSEQUENCE** = an edge firing against the D2 topological + temporal order.
- **SILENT-RESIDENT** (was ZOMBIE/ORPHAN) = a C-SILENT resident: no enumerator traverses it, no
  predicate reacts.

> **THE GATE, AND IT MUST NAME BOTH DETECTORS:**
>
> 1. **`SILENT-RESIDENT` is gated on `lifecycle_class NOT IN {TRANSIENT, EVENT_CREATED, DORMANT}`**,
>    and on `UNDECLARED` it renders UNKNOWN rather than asserting.
> 2. **`variance.Orphan` IS A GATED CONSUMER AND MUST BE NAMED AS ONE (F-2).** It is a separate, live,
>    already-wired detector flagging `"singleton, no sibling, no consumer"` -- the at-rest signature of
>    a `TRANSIENT`. Gating only the typed violation leaves the danger reachable.
>
> **The kill-list path is the single most dangerous consumer of this axis: ungated, it does not merely
> miss the finding, it proposes deleting the live thing.** A build requirement, not an optimisation.
>
> **Three doors were open, and I found none of them alone.** Rev 1 gated only `TRANSIENT` and
> `EVENT_CREATED`, so a deliberate belt (present, zero traffic, zero consumers) matched cleanly --
> **this design would have proposed deleting all 7 registered `keep-dormant.yaml` entries**, the
> outcome that registry names as *"THE named failure mode."* Rev 2 closed that and left
> `variance.Orphan` open. **A spec whose stated purpose is preventing an existence check from
> proposing deletion of live infrastructure had two live paths to exactly that, while citing the
> registry documenting one of them.**

---

## S.6 SCOPE BOUNDARY -- WHAT THIS SPEC DOES NOT TOUCH

- **Ratified C0-C3 vocabulary, 14 roles, 10 relations, variance and completeness axes: UNTOUCHED**,
  byte-identical to oracle `8f8a63200`.
- **`type_tuple` is NOT amended.** `lifecycle_class` is a D3 obligation FIELD, not a fifth tuple field.
  **F-9 -- CVO~Z affirmed this with a better argument than the one I gave:** the registration-invariant
  reason is real but secondary; **a tuple field applies to EVERY node, which makes `UNDECLARED`
  universal and forces precisely the unshippable outcome S.4 exists to avoid.** As a D3 obligation
  field it binds only CONTRACTED resources -- the correct denominator. S.3.4's `scope` field is not a
  tuple change and does not reopen the seam. **If WS-C2 shows lifecycle belongs in the tuple, that is a
  seam crossing and returns to me before it is built.**
- **No detector is rebuilt here** -- except that acceptance now requires >=1 consumer actually gated
  (F-7), because a stated-only bound is a DESIRED control masquerading as APPLIED.
- **Row-grain and partition-scheme remain FORWARD** per D1's coverage boundary.

## S.7 ACCEPTANCE (what `~C` produces, and what I gate on)

1. `dynamic_rails.D3_contract_obligation` carries a `lifecycle` subsection with **all 7 values** --
   `PERMANENT`, `TRANSIENT`, `EVENT_CREATED`, `DORMANT`, `LEGACY`, `RETIRED`, `UNDECLARED` --
   YAML-parse-provable. **`SUPERSEDED` and `ORPHAN` MUST NOT APPEAR as lifecycle or violation tokens**
   (F-1); the typed violation is `SILENT-RESIDENT`.
2. Every value states absent-at-rest AND present-at-rest polarity (the S.2 table is the content, not a
   gloss); `DORMANT` additionally states zero-traffic-is-healthy.
3. Every value carries its S.3 required fields, with `consumer`/`successor` specified as **EXERCISED,
   not merely resolvable** (F-4), and `max_dwell` **bound to the consumer's D3 cadence** (F-3).
4. `revalidate_by` REQUIRED on every declaration (S.3.1); STALE defined; **STALE never auto-promotes.**
5. Every declaration carries an explicit `scope`; a device-local artifact is per-device or UNKNOWN
   (S.3.4).
6. A missing/unresolvable required field renders UNKNOWN LOUD -- explicitly NOT a fallback to the
   declared value or to `PERMANENT`.
7. `UNDECLARED` default + the claim-vs-check bound stated IN the rule bank (S.4).
8. The S.5 derivations present as derivations, including `ROLLING` as a derivation rather than a class.
9. The S.5.1 gate present as a consumer contract naming **BOTH** `SILENT-RESIDENT` and
   **`variance.Orphan`** as gated consumers (F-2, BLOCKING).
10. **>=1 CONSUMER ACTUALLY GATED, not merely a bound stated (F-7).** "Stated in the rule bank" does
    not discharge this item.
11. `DORMANT` CITES `keep-dormant.yaml` as intent_source and does NOT copy its entries.
12. `meta.version` advances; changelog names this spec and carries the S.0 declaration.
13. Ratified vocabulary BYTE-IDENTICAL to `8f8a63200` (md5 `37e16648dc965424b75c14677927a636`);
    `type_tuple` unamended; every delta an insertion.

**I gate 1-13 before CVO~Z verify. I will not accept a build that infers `lifecycle_class` from name
patterns, lets a missing required field fall back, ships either detector ungated, omits the decay
window, reuses `SUPERSEDED`/`ORPHAN`, or discharges item 10 with prose.**
