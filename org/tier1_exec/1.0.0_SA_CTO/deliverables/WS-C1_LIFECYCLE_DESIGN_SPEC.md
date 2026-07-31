# WS-C1 LIFECYCLE AXIS -- DESIGN SPEC (the D3 lifecycle/supersession vocabulary)

**Program:** NFRA_VELOCITY / CORE. **PRD:** `docs/architecture/NFRA_VELOCITY_CORE_PRD.md` WS-C1.
**Author + design owner + gate:** `1.0.0_SA_CTO~Z`. **Builds into the rule bank:** `0.8.0_AE_CloudComp~C`.
**Verify:** `3.0.0_SA_CVO~Z`. **Written:** 2026-07-31, site Z.
**Target artifact:** `org/modules/graph/NFRA_ONTOLOGY_RULE_BANK.yaml`, ADDITIVE section inside
`dynamic_rails.D3_contract_obligation`. Rule bank head at authorship: `meta.version: "1.7"`.

**STATUS: DESIGN, not built.** This document is the specification `~C` builds from. Nothing here is
landed in the rule bank yet, and no claim below is a claim about live rule-bank content.

---

## S.0 THE SHAPING CORPUS (declared FIRST, per the sovereign fence)

The WS-C2 held-out fence (MSTR~Z relay 20260729T233721Z, Andrew verbatim 2325Z: *"this is setting up
the framework... the real test will be running ADVI_PERFORMANCE MDPF_GLOBAL and others"*) requires that
a rail author publish the corpus they drew from, because **a breached held-out set looks exactly like a
well-fitting rail and nothing reports it.** An unnamed shaping corpus is indistinguishable from a
breached one. So, exhaustively, what shaped this spec:

1. The `gold/trigger-pending.json` trigger-marker class -- the specimen named in the PRD itself
   (landed in a kill list's top tier on "no object found").
2. The `comp-legacywriter` TRANSIENT-MARKER name-pattern stopgap (@d51f6b38a0) -- as the thing being
   REPLACED, per the PRD.
3. `0.7.0_AE_CloudOps~Z`'s never-yet specimen: `org/surface-check-ack-audit.log`,
   `org/mcp/comp-detect-gate-override.log`, `org/mcp/log-open-ok-override.log` (msgs 20260731T024616Z
   and 20260731T024950Z).
4. `audit-archive-invoker.py`'s own output on THIS device, my startup run 20260731T024700Z (rc=1,
   11 findings) -- an independent second observation of specimen 3 taken before I read their framing.
5. The existing `D3_contract_obligation` section of the rule bank at v1.7 (its four obligation types,
   its `intent_denominator_binding`, and its `coverage_boundary` law that an absent contract is an
   UNDECLARED obligation, never an absent one -- S.4 below is that law extended to lifecycle).

**NOT drawn on, and deliberately not opened while writing this:** `ADVI_PERFORMANCE`, `MDPF_GLOBAL`.
No surface of either is used as a vocabulary example here, and no contract has been authored to make
this rail look expressive. The fence holds as of this document.

**Honest boundary on my own corpus:** the PRD's WS-C2 corpora (MSBEFF's 718 findings, the 210-incident
INCIDENT_TAXONOMY, the DEBTLOOPS shapes) have NOT yet been walked item-by-item against this vocabulary.
That walk IS WS-C2 and it is the acceptance test for this enum, not a formality. **This spec is
therefore PROPOSED, not validated -- it is fitted to five specimens and must survive three corpora.**
Expect the enum to change at WS-C2. If it does not change at all, be suspicious of the walk.

---

## S.1 THE PROBLEM, STATED PRECISELY

**An existence check is being asked a question about lifecycle that existence cannot answer.**

A 404 / `head-object` miss / `test -f` false is ONE symbol standing for at least four distinct states
(partition contributed by `0.7.0_AE_CloudOps~Z`, 20260731T024950Z, and adopted here verbatim in
substance):

| | state | shape of the absence over time |
|---|---|---|
| (a) | never existed and never will -- genuinely dead | flat |
| (b) | existed, was deleted -- dead, with history | terminal |
| (c) | exists as a lifecycle, absent RIGHT NOW -- **TRANSIENT** | **a TROUGH in a cycle** |
| (d) | will exist on first occurrence, which has not occurred -- **NEVER-YET** | **a PREFIX, monotonic** |

**Absence is not a state. It is a SET of states, and an existence check cannot partition it.**

Two consequences that drive the whole design:

**(i) The transient case is not fixable by re-observation.** You can sample forever and keep landing in
troughs; sampling harder makes you more confident and no more correct. This is why WS-E3's
>=2-CONFIRMED bar does not save it -- a transient key independently reads absent AND dormant AND
reader-less, so two confirmed signals agree and both are wrong. **Confirmation across correlated
instruments is not independence.**

**(ii) A two-value vocabulary is insufficient, and shipping one would be worse than shipping none.**
If CORE drafts `{TRANSIENT, DEAD}` and stops, state (d) has no home and every never-yet artifact gets
misfiled -- most likely as DEAD, because DEAD is the default an existence check produces. We would
ship a vocabulary that fixes the trigger-marker class and *formalises* the audit-log class as a
kill-list candidate, with the system now more confident. The three override logs in specimen 3 would
be **correctly classified as dead by a better-typed system.** A neighbour bounds the vocabulary; a
second instance would only have re-confirmed the phenomenon we already had.

---

## S.2 THE ENUM: `lifecycle_class`

Declared per contracted resource/process. Names the SHAPE of the thing's life, not its current phase.

| value | meaning | absent-at-rest | present-at-rest |
|---|---|---|---|
| `PERMANENT` | present from creation onward | **FINDING** (missing) | healthy |
| `ROLLING` | present, instances replaced each cycle; identity persists, vintage advances | **FINDING** (missing) | healthy iff vintage advances; **FROZEN** if not |
| `TRANSIENT` | written -> consumed -> deleted; oscillates | **HEALTHY** | healthy iff dwell < `max_dwell`; **STRANDED** beyond |
| `EVENT_CREATED` | absent until a triggering occurrence; monotonic + append-only after | **HEALTHY** (zero occurrences) | healthy; a NON-APPEND edit is an INTEGRITY finding |
| `SUPERSEDED` | a live successor exists; the thing may still be READ | per successor | healthy to read; **a WRITE is LEGACY-WRITER** |
| `RETIRED` | decommissioned by ruling; absence is the correct terminal state | healthy (terminal) | **FINDING** (incomplete decommission) |
| `UNDECLARED` | no lifecycle declared | **UNKNOWN, LOUD** | **UNKNOWN, LOUD** |

### S.2.1 The polarity inversion -- the load-bearing consequence

**A detector cannot merely KNOW about `TRANSIENT` and skip it. It must run the OPPOSITE predicate.**

On the table above, absence is HEALTHY on two rows and presence is a FINDING on two rows. **A
single-polarity existence detector is wrong on three of seven rows** -- and wrong in the dangerous
direction on `TRANSIENT` and `EVENT_CREATED`, where it reports a healthy system as dead and proposes
deleting a live one.

This is precisely why the name-pattern stopgap is not a type system: **a skip-list SUPPRESSES; a type
INVERTS.** Suppression loses the finding that presence-beyond-dwell (`STRANDED`) is a real defect that
today has no name at all -- a transient marker that was written and never consumed is a dead pipeline
leg, and the current instrument set cannot state it in either direction.

### S.2.2 Naming note (`EVENT_CREATED`, not `NEVER_YET`)

`0.7.0_AE_CloudOps~Z` proposed `NEVER-YET` / `EXPECTED-ABSENT`. I am naming the class `EVENT_CREATED`
because **NEVER-YET names a PHASE, not a lifecycle shape** -- it is the pre-first-occurrence phase OF
this class, and an enum whose members mix classes and phases will not survive WS-C2's walk. The phase
vocabulary (`pre-first-occurrence` / `established`) hangs off the class. Their substantive point is
adopted in full and is what S.3 exists to enforce.

---

## S.3 EVERY DECLARATION MUST CARRY ITS OWN FALSIFIER (the anti-abuse gate)

**A lifecycle declaration SUPPRESSES findings. An unfalsifiable suppressor is a silencer, and a
type system that ships silencers is worse than no type system, because the silence now carries
authority.** Therefore each value that flips a detector's polarity must carry the fields that make the
declaration itself CHECKABLE. Required fields per value:

| value | required fields | what makes it falsifiable |
|---|---|---|
| `TRANSIENT` | `consumer` (D2-resolvable reader/deleter), `max_dwell` | you cannot declare TRANSIENT to silence a detector without naming a consumer the graph can resolve; and `max_dwell` creates the STRANDED finding that proves the declaration can still fail |
| `EVENT_CREATED` | `creating_event`, `event_observable` (where the occurrence is INDEPENDENTLY visible) | without an independent observable, "absence = zero events" is unverifiable and byte-identical to "the writer is broken" |
| `SUPERSEDED` | `successor` (live, D2-resolvable), `intent_source` | makes debt computable; an unresolvable successor is not a supersession, it is a deletion |
| `RETIRED` | `retirement_ruling` (intent_source) | a retirement with no ruling is an outage with paperwork |
| `ROLLING` | `cadence` (D3-sourced), `vintage_probe` | separates FROZEN from stale; the probe stays live per D2's coverage boundary |
| `PERMANENT` | `intent_source` | the default-looking value is still a claim from above, never the artifact's own config |

**Failure mode when a required field is missing or unresolvable: the declaration renders `UNKNOWN,
LOUD` -- it does NOT fall back to the declared value, and it does NOT fall back to `PERMANENT`.** A
half-declared lifecycle is the unfalsifiable case and must be noisier than no declaration, not quieter.

**PRODUCER-ASSERTED, NEVER OBSERVER-INFERRED** (constraint contributed by `0.7.0_AE_CloudOps~Z` and
binding on the build): the observer cannot distinguish (d) from (a) by looking -- that is the entire
problem -- so a vocabulary that requires the OBSERVER to classify has *moved* the impossible judgement
rather than removed it. Same structural reason WS-C7's reachability limb must EXERCISE rather than
RESOLVE. **Transience cannot be derived; it must be declared.** Any implementation that infers
`lifecycle_class` from key names, directory position, or observed absence has rebuilt the stopgap with
more syntax.

---

## S.4 `UNDECLARED` IS THE DEFAULT, AND ITS SCOPE IS BOUNDED

`UNDECLARED` renders UNKNOWN and LOUD -- never silently `PERMANENT`. This is D3's existing
`coverage_boundary` law extended one axis: *the ABSENCE of a declared contract is NOT the absence of an
obligation -- it is an UNDECLARED obligation, rendered UNKNOWN, never Complete.*

**Bounded scope, and this bound is part of the design, not a concession.** Today essentially the whole
estate is `UNDECLARED`. If `UNDECLARED` made every existing detector render UNKNOWN, the axis would be
unshippable and would be quietly bypassed within a week. So:

> **`UNDECLARED` constrains what a tool may CLAIM; it does not disable what a tool may CHECK.**
> An existence check may still run and still report "absent." What it may NOT do is convert that
> observation into a lifecycle verdict -- dead, orphan, zombie, kill-list candidate -- without a
> resolvable `lifecycle_class`. The finding it emits is `ABSENT (lifecycle UNDECLARED)`, which is
> honest, actionable, and cheap; it is not `DEAD`.

Ramp: announce-then-enforce, per the estate's standing gate convention. Declaration coverage is
reported as a printed denominator (`N of M contracted resources carry a resolvable lifecycle_class`),
never as a boolean, and never as prose in this file -- the gate owns the count.

---

## S.5 DERIVATIONS LICENSED (definitional, never primitives)

Per the PRD's requirement that every derived property be defined as a derivation:

- **debt** = `expired_obligation UNION superseded_with_live_successor`, where
  `expired_obligation` = a contract whose `expiry_condition` evaluates TRUE and whose `lifecycle_class`
  is not `RETIRED`; `superseded_with_live_successor` = `lifecycle_class == SUPERSEDED` with a
  D2-resolvable live `successor` AND a live writer still writing to the superseded target.
- **stranded** = `lifecycle_class == TRANSIENT` AND observed dwell > `max_dwell`. (New. Not statable
  by any current instrument in either direction.)
- **incomplete-decommission** = `lifecycle_class == RETIRED` AND present at rest.
- **frozen-vs-stale** = `ROLLING` with a non-advancing vintage (frozen) vs a vintage advancing but
  behind cadence (stale) -- the D2 derivation, now with the identity/instance split made explicit.

### S.5.1 The typed violations, and the one that must be lifecycle-GATED

- **LEGACY-WRITER** = a D2 `WRITES` edge whose target carries `SUPERSEDED` with a live successor, or
  whose obligation is expired.
- **CLOBBER** = two writers at one `(key, grain)` with no adjudicating `canonical_source` contract.
- **TRIGGER-MISSEQUENCE** = an edge firing against the D2 topological + temporal order.
- **ZOMBIE / ORPHAN** = a C-SILENT resident: no enumerator traverses it, no predicate reacts.

> **ZOMBIE/ORPHAN MUST BE GATED ON `lifecycle_class NOT IN {TRANSIENT, EVENT_CREATED}`, AND ON
> `UNDECLARED` IT MUST RENDER UNKNOWN RATHER THAN ASSERT.** A `TRANSIENT` artifact at rest matches
> the ZOMBIE/ORPHAN predicate EXACTLY -- absent, dormant, reader-less -- which is how a live pipeline
> trigger reached a kill list's top tier. **The kill-list detector is the single most dangerous
> consumer of this axis: ungated, it does not merely miss the finding, it proposes deleting the live
> thing.** This gate is a build requirement, not an optimisation.

---

## S.6 SCOPE BOUNDARY -- WHAT THIS SPEC DOES NOT TOUCH

- **The ratified C0-C3 vocabulary, 14 roles, 10 relations, variance and completeness axes: UNTOUCHED.**
  This is an additive section inside `D3_contract_obligation`.
- **`type_tuple` is NOT amended by this spec.** `lifecycle_class` is a D3 obligation FIELD, not a
  fifth tuple field. Adding a tuple field would change the canonical enum set that base 0.8.0's
  registration invariant validates every comp-tool against -- a comp-tool STANDARD change, which
  routes to main CTO under the standing carve. **If the WS-C2 walk shows lifecycle must be part of the
  tuple, that is a seam crossing and comes back to me before it is built.**
- **No detector is rebuilt here.** The gating requirement in S.5.1 is stated as a contract on
  consumers; migrating consumers is downstream work.
- **Row-grain and partition-scheme remain FORWARD** per D1's existing coverage boundary; nothing here
  assumes they arrived.

## S.7 ACCEPTANCE (what `~C` must produce, and what I gate on)

1. `dynamic_rails.D3_contract_obligation` carries a `lifecycle` subsection with the S.2 enum,
   **including an explicit `TRANSIENT` value**, each value carrying its S.3 required fields.
2. Each enum value states its absent-at-rest and present-at-rest polarity explicitly (the S.2 table is
   the content, not a gloss on it).
3. `UNDECLARED` present, defaulting, and scoped per S.4 -- with the claim-vs-check bound stated IN the
   rule bank, not only here.
4. The S.5 derivations present as derivations; the S.5.1 ZOMBIE/ORPHAN lifecycle gate stated as a
   consumer contract.
5. `meta.version` head advances, with the changelog comment naming this spec and the shaping corpus
   declaration (S.0) so a later reader can verify the held-out fence.
6. Ratified vocabulary byte-identical; `type_tuple` unamended.
7. `3.0.0_SA_CVO~Z` verify.

**I gate on 1-6 before CVO~Z verify. I will not accept a build that infers `lifecycle_class` from name
patterns, that lets a missing required field fall back to the declared value, or that ships
`ZOMBIE/ORPHAN` ungated.**
