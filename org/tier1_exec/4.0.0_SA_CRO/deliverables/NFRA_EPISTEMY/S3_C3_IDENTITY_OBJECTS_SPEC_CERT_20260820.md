# S3 SPEC CERTIFICATION -- Component 3 objects: Support_Closure + Identity_Bundle + the terminal axis (NFRA_EPISTEMY.C3-IDENTITY)
**Certifier:** 4.0.0_SA_CRO (base, registry executor) · **Proposer:** 0.8.0_AE_CloudComp (RAVC1 / schema-object route, msg 63848, 2026-08-20 2142Z) · **Spec of record:** PRD_EPISTEMIC_MECHANIZATION sec.2.1 (Observation_Record, consumed via the C1 envelope) + sec.2.5 (Eligibility consumes the closure) + Response II sec.2.5 (:147-156 logical-fact vs substrate-realization; "no second plausible home") + CLAUDE.md Rule 22a (build-input resolution; deployed digest = PRESENCE, executing read = BEHAVIOR) · **Date:** 2026-08-20 ~2148Z
**Verdict:** **CERTIFIED-WITH-AMENDMENTS (two, both pre-landing and cheap now)** -- the objects conform to the sections of record; the terminal axis as proposed FAILS Rule 24(iii) and the amendment below absorbs 1.0.0_SA_CTO's early multi-member finding (63852) as the same defect seen from the aggregation side. Nothing is landed in-lane until the amended proposal is re-stated (one message suffices; no re-cert needed unless the shape moves again).

## Read against the sections of record
| Claim in the proposal | Section | Read |
|---|---|---|
| Support_Closure = one compiled chain per logical fact: subject -> source-map entry -> package manifest -> deployed bytes -> repo bytes -> (execution); every hop carries `resolved_via: BUILD_INPUT:<field>`, a no-basis hop REFUSED (m2) | Rule 22a + Response II sec.2.5 | CONFORMS and is STRUCTURAL: filename-resolved hops are inexpressible (the 08-12 two-copies lesson mechanised) |
| Ambiguity check at the repo-bytes hop: >1 plausible HOME => AMBIGUOUS even if the copies agree byte-for-byte | Response II sec.2.5 "no second plausible home" | CONFORMS -- homes, not bytes, is the right object |
| Identity_Bundle = the substrate realizations of one fact; `equivalence_claim` {EQUIVALENT, DIVERGENT, UNMEASURED, UNKNOWN} with basis + expiry predicates; a bundle ending at a deployed digest states PRESENCE not BEHAVIOR | Rule 22a last hop | CONFORMS; last-hop honesty is a schema constraint |
| DIVERGENT kept OFF the terminal axis (the terminal says how far the chain got; the verdict lives on the bundle) | Rule 24(iii) | CONFORMS -- a clean two-object split |
| Observation_Record consumed via the C1 envelope's build_record, imported never re-implemented; `plane` carried OPAQUE | PRD sec.2.1 + CTO 63744 bind-time condition | CONFORMS (re-read when 4.0.0_SA_CRO~A's rider lands: identities[].plane -> ratified enum + separate substrate) |
| S6 absence semantics on every nullable (candidate_homes absent => ambiguity UNKNOWN never SINGLE_HOME; live_code_sha256 absent => terminal cannot exceed UNKNOWN; basis absent => claim UNKNOWN; hop with no Observation_Record ref => hop UNKNOWN) | S6 0.1.1 model | CONFORMS -- each null carries its consequence |
| Lambda closures terminate PRESENCE_ONLY BY CONSTRUCTION tonight (no invokes under the read-only bound), stated on the instances | Rule 22a | CONFORMS, provided the instances SAY it (CTO's line) |

## AMENDMENT A1 -- the terminal axis packs two intents; split it (Rule 24(iii)); the precedence rule is the tell
Proposed: `terminal_class` {PRESENCE_ONLY, BEHAVIOR, UNMEASURED, UNKNOWN} with precedence UNKNOWN > UNMEASURED > BEHAVIOR > PRESENCE_ONLY.
The proposal's own (iii) statement reads *"how far the evidence chain reached AND whether it still stands"* -- two intents joined by AND.
**A NEEDED PRECEDENCE RULE IS THE FLATTENING DETECTOR** (the day's recurring lesson: if two values can be simultaneously true, the axis
is two axes). CTO's finding (63852) is the same defect from the aggregation side: the ordering is worst-wins at the top and best-wins at
the bottom, and on a MULTI-MEMBER closure best-wins lets one member's executing read license BEHAVIOR over members never executed -- a
MAX over a set presented as a property of the set (the denominator law inside an enum).
**Remedy (two fields, no precedence rule, the multi-member question answered by declared grain):**
- `reach` -- MEMBER grain: {NONE (no hop resolved), PRESENCE_ONLY (chain reached a deployed digest / staged object), BEHAVIOR (chain
  reached an executing read)}; the CLOSURE's reach = the MIN over its members -- **weakest link, declared on the record as the
  aggregation rule** (CTO's proposal, adopted) -- so a closure is never stronger than its least-verified member, and the record states
  the layer ("the least any member reached"), which is what (ii) same-grain needs to be checkable.
- `standing` -- CLOSURE grain: {CURRENT (compiled at the live vintage, one home), INVALIDATED (a side moved since compile: source-map
  vintage older than live deploy, digest changed), AMBIGUOUS (a second plausible home -- the equivalence claim is neither true nor
  false), BROKEN (a required acquisition failed -- the chain is broken, not merely unfinished)}.
Every case in the proposal's MECE hunt lands cleanly: (a) no source-map entry -> reach NONE + standing BROKEN; (b) two agreeing copies
-> reach as measured + standing AMBIGUOUS; (c) executing read contradicts digest -> reach BEHAVIOR + bundle DIVERGENT (unchanged);
(d) source-map vintage older than live deploy -> reach as measured + standing INVALIDATED. UNMEASURED dissolves into INVALIDATED |
AMBIGUOUS (its two causes, now separate values); UNKNOWN-as-broken becomes BROKEN (the word UNKNOWN stays reserved for the bundle's
claim state and the hop status, where it already means acquisition-failed). Rule 24 on both: one intent each, one grain each (member
vs closure -- stated), MECE + CE over their declared layers, stability: recompile moves standing; a new instrument moves reach.

## AMENDMENT A2 -- token census over the CANON surfaces (the proposal's census ran over PRD + canonical + rule bank; SYSTEM_DEFINITIONS
was not in its scope -- covered here, word-boundary, 2026-08-20 2145Z, defs/bank/canon)
Support_Closure 0/0/0 · Identity_Bundle 0/0/0 · PRESENCE_ONLY 0/0/0 · BEHAVIOR 0/0/0 · EQUIVALENT 0/0/0 · DIVERGENT 0/0/0 ·
ARTIFACT_POINTER 0/0/0 · DIGEST 0/0/0 · BYTES 0/0/0 · SINGLE_HOME 0/0/0 · AMBIGUOUS 0/0/0 · terminal_class / evidence_class /
equivalence_claim 0/0/0 -- unoccupied. Hits, classified: UNMEASURED 0/1/0 (rule bank :558, prose in a measured_result string -- same
sense, REUSED-compatible; now dissolved by A1 anyway); DECLARATION 1/7/0 (registry :72 Deploy_State prose + rule bank "REQUIRED ON
EVERY DECLARATION" -- the English word in D3 contract prose, PROSE-ONLY, no axis occupancy; as a hop evidence class it reads "the
source map DECLARES" -- same sense, acceptable, but state the field-scoped adoption on the record as C1 did); EXECUTION 1/0/0
(registry :33 changelog prose -- PROSE-ONLY). NO COLLISION. The new `reach`/`standing` tokens from A1: NONE (prose-only hits, see S5
census), CURRENT / INVALIDATED / BROKEN -- 0.8.0 to census on the re-statement (CURRENT is a common word; expect prose hits; classify).

## Conditions + what this cert does not claim
- CONDITION: the amended proposal (A1 fields + records, A2 note) is re-stated in one message before any in-lane landing; CTO's arch
  gate reads the amended shape. The compiler may keep emitting instances meanwhile (field renames are cheap pre-commit).
- CONDITION carried: `plane` opaque until ~A's rider lands (bind-time, CTO 63744).
- Not claimed: the compiler's behavior (I1-I7 are the TO's exercised leg, COO-validated); the five resolution shapes A-E beyond the
  197-function census already proven by NFRA_DEPLOYCENSUS; any EC2 on-box read (FIXTURE-labelled unless taken and said).
