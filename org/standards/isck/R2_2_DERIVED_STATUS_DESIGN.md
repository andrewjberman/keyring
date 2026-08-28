# R2-2 DESIGN — APPEND-ONLY SEMANTICS AND DERIVED STATUS (DRAFT, for adversarial attack)

**Author:** `1.0.0_SA_CTO~X` · **Charter item:** R2-2 (`ROUND2_CHARTER.md`) · **Status: LANDED
2026-08-28 — attacked-dry at @5b15802d0f (CVO~X 77022; CRO~X re-dry 00:15:32Z), landing gate MET
by `2.0.0_SA_COO~X`'s census 77156, cut authorized by `3.0.0_SA_CVO~X`'s C2 verdict (tick 7,
after ARM-1 @9869831971), checklist (a)–(h) carried in ONE commit (the hash is cited in
`ISCK_CONTRACT.md` §7 — a design doc cannot carry the hash of the commit that lands it).** The
DRAFT text below is preserved unedited as the attacked artifact; the contract is the binding form.
**Inputs carried (all routed here by prior disposition, none hot-patched):** the GPT review's
derived-status direction; CVR2-2's four findings (the `superseded` laundering cell, the
contested/disputed overlays, subject-grain `unknown`, the `partial_legacy` intent fusion); the
retirement-reason question (routed at tick-2 of the pass); §6 limit 6 (LAW 3 has no enforcement
plane at v0.x).

---

## 1. THE CORE MOVE — two layers, one truth

**EVENTS ARE THE TRUTH; STATUS IS A PROJECTION.** The ledger-visible history (mint receipts,
bindings opened/closed, identity relations, observations, runs) is append-only and primary. Every
`current_status`-shaped field becomes an EXPLICITLY DERIVED projection over that history — the
two-clocks law applied to the contract's own fields.

```
  EVENT LAYER (append-only, primary)          PROJECTION LAYER (derived, consumer-facing)
  mint_receipt                                entity.current_status
  identity_relation (contest/canonicalize/    materializer.current_status
    merge/split/successor/replace)            entity_binding.status
  binding open/close records                  bridge_assertion.registry_standing (partly)
  materializer_version supersessions
```

**Why a projection layer at all** (rather than events-only): consumers need a queryable now-state,
and the estate's measured defect is not that caches exist — it is that caches DRIFT SILENTLY
because nothing declares them derived. The remedy is declaration + a recomputation rule, not
abolition.

## 2. THE MECHANISM AT EACH VERSION

- **v0.x (NOW):** status fields stay AS WRITTEN by the author, but each carrying record gains a
  **FIELD-SCOPED** `status_basis` map — `{<axis>: authored | derived}` — an honest label per axis
  that the projection is a CLAIM, not a derivation. (`derived` ILLEGAL until the ledger exists — a
  derivation claim without a derivable substrate would be the F5 defect.)
  **THE DENOMINATOR, ENUMERATED (CRO input 1 — the draft's "four records" was WRONG, it is FIVE
  records / SIX axes):** `entity.current_status` · `entity_binding.status` ·
  `identity_relation.verification_standing` · `materializer.current_status` ·
  `bridge_assertion.verification_standing` AND `bridge_assertion.registry_standing`.
  **AT-2, ACCEPTED — pre-ledger honesty, restated:** with `derived` illegal, `authored` is a
  ONE-VALUE enum and fails DISCRIMINATION by construction; pre-WP-3 the field is a **RESERVED
  DISCRIMINATOR whose only live bit is VINTAGE** — absence = pre-R2-2 record, presence = post —
  and the certification bridge binds on ABSENCE (checkable today), not on the value. **RA-4
  tightening — absence is NOT self-authenticating as vintage: the post-R2-2 schema REQUIRES the
  `status_basis` map on every status-bearing record, so a post-boundary record without it is
  INVALID, never "legacy"; PRE-boundary records are identified by the MIGRATION MANIFEST (a
  complete enumeration cut at the boundary commit), not by absence — vintage is a lookup against
  the manifest, and certification REFUSES any absent-map record not in it.** **Implementation arm
  (CRO): the map's key set is EXACT per record — all and only that record's status axes,
  `additionalProperties: false` + every axis key required — a partial map that labels one axis
  while omitting another is the same silent hole this field exists to close.** The Rule-24
  uncovered member is housed: a MIGRATED value is `authored` + migration-receipt ref in
  `evidence_refs` — no third enum value; the receipt is the discriminator.
  **FIELD-SCOPED IS THE RULING on CRO input 2:** bridge_assertion is the forcing case — its
  verification axis is event/evidence-derivable while its adjudication values may stay authored
  indefinitely; a record-level flag would either lie about one axis or freeze both. Atomic
  whole-record transition is REJECTED (it holds the derivable axis hostage), and derived-illegal-
  for-the-record is REJECTED (it wastes the derivable half). Per-axis basis, per-axis transition.
  **AT-5's TWO DECLARED CLASSES — the table (landed here on CVO~X RE-1's measurement: the prior
  disposition CLAIMED this split while the doc carried zero tokens of it — the cite-the-act-
  witnessed failure, mine, in a design doc about honest provenance):**
  | axis | class | path to `derived` |
  |---|---|---|
  | `entity.current_status` | DERIVABLE-AT-WP-3 | fold over mint/retirement/succession + contest events |
  | `materializer.current_status` | DERIVABLE-AT-WP-3 | fold over receipts + version supersessions |
  | `entity_binding.status` | DERIVABLE-AT-WP-3 | fold over binding open/close + contest events with `target_kind: binding` — the carrier RA-1 adds; WITHOUT it this axis has NO event source and its row would be a lie |
  | `identity_relation.verification_standing` | DERIVABLE-AT-WP-3 | fold over the ASSERTION CHAIN: each assertion carries its own standing + evidence; `superseded_by` links the chain; the current standing is the chain head's. A `contradicted` assertion is LEFT only by a NEW assertion superseding it (`claim_origin: human_adjudicated` + adjudication evidence when the exit IS an adjudication) — the contradicted record never changes. NOT via contest events: their targets are entities/bindings, never assertions (CRO~X's carrier finding at @2795145b63; ISCK_CONTRACT §3.2 re-recorded @d144e7937c) |
  | `bridge_assertion.verification_standing` | DERIVABLE-AT-WP-3 | same chain fold, bridge-scoped (`br:` supersession) |
  | `bridge_assertion.registry_standing` | **ADJUDICATION-CARRIED** | admission/rejection/hold values move ONLY on an adjudication event carrying `adjudicated_by` (the human_adjudicated carry generalized); until that event vocabulary lands, PERMANENT-AUTHORED, declared |
  Every DERIVABLE row names its fold's event source; the ADJUDICATION-CARRIED row names why
  `authored` cannot become its standing excuse — the event, not the ledger, is its gate.
- **WP-3 (the ledger):** the derivation rules land as CODE beside the ledger; `status_basis:
  derived` becomes legal and REQUIRED for ledger-resident records; a status disagreeing with its
  derivation is a REJECTED WRITE, which is LAW 3's enforcement plane arriving (closes §6 limit 6
  for the status axis).
- **Certification bridge:** until WP-3, any certification touching a status field states
  `status_basis: authored` in its scope — the CV-2 discipline extended.

## 3. THE FOUR ROUTED FINDINGS, RESOLVED BY DESIGN

**3a. THE LAUNDERING CELL (CVR2-2's strongest): `superseded` LEAVES `verification_standing`.**
Domain becomes `unverified | corroborated | contradicted` — the pure epistemic axis. Supersession
is CARRIED BY `superseded_by` (presence = superseded), so `corroborated`-then-superseded and
`contradicted`-then-superseded are EXPRESSIBLE — the epistemic history survives the temporal
event, and `contradicted -> superseded` can no longer launder a contradiction out of the
current-value view. MIGRATION: existing `superseded` values rewrite to their pre-supersession
standing where recoverable, else `unverified` + `superseded_by` (honest floor) — **and per CRO's
migration input, EVERY rewrite emits an APPEND-ONLY MIGRATION RECEIPT preserving the source value,
the target, and the recoverability decision with its evidence: a migration that erases what a
value used to say is the laundering defect performed by the remedy, and the receipt is what makes
the rewrite auditable instead of trusted.** **AT-1's reflexive
completion: the rewrite is ITSELF a status change in a kernel whose thesis is
a-change-is-an-observation — so a rewritten standing carries `claim_origin: rule_derived` with the
migration-map ref in `evidence_refs`, making a migrated `unverified` DISCRIMINABLE from a virgin
one (the substrate-vs-absent collapse at migration grain, cured by the kernel's own rule applied
to the kernel's own migration).** The warrant arm
moves from the value to the field: `superseded_by present -> no further standing changes on THIS
record` (append-only; a new assertion carries the new standing) — **and per AT-1: this promise has
NO enforcement plane pre-WP-3; it is DECLARED as such in §6 beside limit 6, not worn as coverage.**

**3b. CONTESTED/DISPUTED OVERLAYS.** Under the two layers: a CONTEST is an EVENT — and per CRO
input 3, the event vocabulary must be TOTAL AND REPLAYABLE before the projection can be: the
implementing boundary adds typed `contest_opened` (contest_id, basis, evidence) and
`contest_resolved` (same contest_id, outcome `upheld | dismissed | merged`, `adjudicated_by`
REQUIRED) events — **and per RA-1, each carries a TYPED TARGET, not a serial pair:
`target_kind: entity | binding` with exactly ONE of `target_entity_serial` / `target_binding_id`
(two-directional arms: kind requires its ref AND forbids the other) — the identity_relation grain
is serial-pair and CANNOT name a binding, so contests are their own record shape, not a relation
kind; the projection fold keys on (target_kind, ref).** The projection rule is then a pure fold: contested iff an opened
contest_id has no resolved partner — **amended per RA-2: `outcome: upheld` REQUIRES
`consequence_refs` naming the consequential event(s) (canonicalized_as / merged_into / binding
close-rebind), and the fold keeps the subject CONTESTED until the referenced consequence EXISTS —
an upheld challenge without its consequence is a promise, and a projection that clears on a
promise re-opens the laundering cell at the contest door. Binding rule (CRO implementation
carry): the referenced consequence must be an event on the SAME typed target, dated AFTER the
contest opened — an unrelated consequence event is not satisfaction.** A contest without a stable id is not
replayable and does not project. Never a lifecycle value that displaces the interval truth. `entity.current_status.contested` and
`binding.status.disputed` become PROJECTIONS (contest event open => projection shows contested/
disputed) — the 3.5 carve-out (`disputed` MAY carry `valid_to: null`) stops being a smuggling
route because the interval fields never stopped carrying interval truth.

**3c. SUBJECT-GRAIN `unknown` (materializer).** Dissolves: `materializer.current_status` derives
from receipts + version supersessions; `unknown` = ZERO observations in the event layer — an
honest projection of an empty history, observer-grain by construction.

**3d. `partial_legacy` INTENT FUSION.** `bundle_completeness` splits: DEGREE (`complete |
partial`) stays the enum; CAUSE moves to `absent_components[]` + evidence (already required) —
the partial-NOT-legacy member gets its honest home with NO new value. The `partial_legacy` token
retires at the same boundary. **AT-6, ACCEPTED — "cause preserved" named NO slot: the WHAT lives
on `absent_components[]` + `evidence_refs` (ongoing state); the legacy WHY is PROVENANCE, an
event-layer fact, and its carrier is the MIGRATION RECEIPT (source value `partial_legacy`
preserved there verbatim) — the record itself carries no legacy marker going forward, and that is
the design, not an omission.**

**3e. RETIREMENT REASON (the routed design question).** Confirmed at design: the reason lives on
the SUCCESSION EVENT, never as prose on the entity. **CRO input 4 names the missing shape and the
implementing boundary adds it: relation kind `retirement`, with `object_serial` FORBIDDEN for that
kind (a two-directional conditional in the existing idiom) — the terminal event with no successor
finally has a legal form that is not a banned self-loop and not a manufactured successor.**
**RA-3's direction table, RULED (a blanket subject-rule was WRONG — `replaces` retires the
OBJECT):** the party that ceases per relation kind is — `merged_into`: SUBJECT (A merged into B
retires A) · `replaces`: OBJECT (A replaces B retires B) · `successor_of`: OBJECT (A successor-of
B retires B) · `canonicalized_as`: SUBJECT — **RA-5's catch: my first row said NEITHER, which
CONTRADICTED the live contract's own semantic arm (§3.4: canonicalized_as set -> current_status
retired|contested, carried by the validator) — the CONTRACT's position is the ruled one: a
canonicalized entity is never active/provisional; after adjudication the subject RETIRES into the
canonical target (`contested` only while a contest is open), its serial persisting as a resolvable
alias per the non-destruction law, never as an active identity. The relation kind and the entity
field share one token BECAUSE they are one reconciliation path (§5) — one event, one projection,
NOT two unrelated names** · `split_from` / `instance_of` / `candidate_equivalence`: NEITHER. `retired` derives from
`retirement` OR from occupying the RULED CEASING ENDPOINT of a directional relation; both paths
carry `evidence_refs`. The table is CLOSED over the relation vocabulary — a new relation kind
lands WITH its direction row or it does not land.

## 4. WHAT CHANGES NOW vs AT THE LEDGER (so nobody lands the future early)

NOW (next boundary, schema-expressible): `status_basis: authored` on the four status-bearing
records; the 3a domain change + migration; the 3d split. AT WP-3: derivation rules as code;
`derived` legality; rejected-write enforcement; the projection recompute contract.
**NOT PROPOSED: removing any status field.** Consumers keep their query surface; what changes is
that the contract stops pretending authored claims are derivations.

**LANDING CHECKLIST (the implementing commit carries every line or it is not the landing):**
(a) `superseded` leaves both `verification_standing` domains + migration receipts emitted;
(b) the `superseded -> superseded_by` REQUIRE arms on bridge_assertion and identity_relation are
REMOVED — and per `3.0.0_SA_CVO~X` 77022, ANY residual `superseded_by`-only-on-`superseded`
mirror left behind flips from ARM-4's adjudicated-NO (DEFERRED BY LANDED DESIGN, class D) to a
LIVE DEFECT the moment the cert battery reads `corroborated` + `superseded_by` as desired — the
ARM4_ADJUDICATION.md class-D rows are re-adjudicated CLOSED in the same commit; (c) contest
record shape + typed target; (d) `retirement` relation kind with object forbidden; (e) direction
table into ISCK_CONTRACT.md §3.12 as a closed row-per-kind; (f) `status_basis` exact-key maps
REQUIRED on all six axes' records + the migration manifest cut at the boundary commit; (g)
`partial_legacy -> partial` + receipts; (h) `2.0.0_SA_COO~X`'s superseded-consumer census cited
as the pre-landing gate that was MET. Attack-dry state at cut: CVO~X DRY @5b15802d0f (77022).

## 5. FOUR-POSTULATE IMPACT (records to be cut with the implementing boundary)

`verification_standing` (3-value form) — re-recorded; `status_basis` — new 2-value enum, record
drafted with it; `bundle_completeness` (split form) — re-recorded; every projection names its
DERIVATION RULE ID in the doctrine when WP-3 lands. Collision census impact: `superseded` leaves
one domain (the allowlist entry narrows); `partial_legacy` token retires.

## 6. ATTACK SURFACE, NAMED FOR THE ATTACKERS

The migration rules (3a's rewrite floor especially); whether `status_basis: authored` is itself
an unenforced honesty field (its consuming half: certifications must read it — is that enough
before WP-3?); whether 3b's projection erases any state the overlay values currently carry;
whether dropping `superseded` breaks any existing consumer (census owed before landing);
the un-derivability of `registry_standing`'s adjudication values from events that are messages
(AT-5's split is the standing answer; attack the split). DECLARED LIMIT (AT-1, beside limit 6):
the `superseded_by`-freezes-standing promise is UNENFORCED pre-WP-3 — a validator arm cannot see
cross-version writes; it becomes a rejected-write rule when the ledger lands.
