# CVO~X attack on the R2-2 derived-status design draft

**archetype:** VALIDATE
**Target:** `org/standards/isck/R2_2_DERIVED_STATUS_DESIGN.md` @1061546c63 (the claimed attack slot,
76930). Round 2 is NON-BLIND by declaration; sequence disclosed: this attack was formed from the
draft alone, then 4.0.0_SA_CRO~X's inputs (76931-class, four holes) were read and diffed —
convergent items are tagged as shared-context convergence, never as corroboration.

**Overall read first, because it is earned: the core move is RIGHT.** Events-primary,
status-as-declared-projection, staged honestly with `derived` illegal pre-ledger — this resolves
all four of my routed CVR2-2 findings in the correct direction, and 3a's design (supersession
carried by `superseded_by` presence; epistemic history survives the temporal event) kills the
laundering cell exactly as my finding asked. The attacks below are on the SPECIFICATION, not the
direction.

---

## AT-1 — THE 3a MIGRATION LAUNDERS THE VICTIMS OF THE LAUNDERING CELL (P0 for the landing)

"Rewrite to pre-supersession standing WHERE RECOVERABLE, else `unverified`" has three defects:

(a) **Recoverability is near-zero BY CONSTRUCTION** — the pre-supersession standing was overwritten
by the very defect being fixed; there is no event history to recover from. So the floor is the
common path, and a record that was `contradicted`-then-superseded migrates to `unverified` —
**the migration erases the contradiction the design exists to make ineradicable.** Unavoidable
information loss — but it must be MARKED, not silent: a migrated standing is a `rule_derived`
claim and the contract's OWN doctrine (§3.1: legacy-import → rule_derived, migration map cited in
evidence) already prescribes the shape. Every rewritten record carries the migration-map ref in
`evidence_refs`; without it, **a migrated `unverified` is byte-identical to a virgin `unverified`**
— the substrate-unavailable-vs-absent collapse rebuilt at migration grain.
CONVERGENT (shared-context) with 4.0.0_SA_CRO~X's append-only migration-receipt input; the receipt
is the stronger form of the same marker and I endorse it — receipt preserving source value +
recoverability decision, ref'd from `evidence_refs`.

(b) **The rewrite is itself a status change with no event** — executed by a migration in a kernel
whose thesis is "a change is an observation." The migration receipt in (a) is also the cure here:
the migration becomes an event with a record, eating its own cooking.

(c) **"`superseded_by` present → no further standing changes on THIS record" is a LAW-3-class
promise with no enforcement plane pre-WP-3** — a stateless validator cannot see a change. Declare
it in §6 beside limit 6, or it reads as coverage (the CV-2 entry-1 class, third instance).

## AT-2 — `status_basis: authored` PRE-LEDGER IS A CONSTANT, AND A CONSTANT CARRIES NO CLAIM (the named question, answered)

With `derived` illegal until WP-3, the field has exactly ONE legal value. It fails DISCRIMINATION
by construction — the evidence could not differ if the claim were false, because no record can say
anything else. It is therefore NOT an honesty label pre-ledger; it is a RESERVED DISCRIMINATOR,
constant until WP-3, informative only after — and the doc should name it that, or reviewers will
read "certifications must read status_basis" as a working control (a protection that exists only
as a description). The one bit it DOES carry pre-ledger: **vintage** — a record WITHOUT the field
is pre-R2-2. Bind the certification bridge on ABSENCE (absent = old shape, state it in scope),
which is checkable today.

**Rule 24 on the new enum:** `authored | derived` — uncovered-member hunt finds **MIGRATED** (the
3a rewrites: no author asserted the value, no ledger derived it). Either the four-postulate record
declares migrated ⊂ authored-with-migration-evidence (legal iff AT-1's marker lands), or the enum
has an uncovered member on day one. The record must say which.

## AT-3 — 3b MOVES THE STATUS BUT NOT ITS OBLIGATIONS, AND ONE CARRIER RECORD DOES NOT EXIST

(a) **The adjudicator arm dies in the move as drafted:** `contested → adjudicated_by REQUIRED`
(batch-2/3.4 arm) binds the VALUE being retired into a projection. The obligation must travel to
the CONTEST EVENT (open-event: who may adjudicate named or namable; close-event: adjudicated_by
REQUIRED), else the projection era loses a warrant the enum era had — conditioning-mints-uncovered
in reverse (de-conditioning un-mints a warrant).
(b) **"a binding-dispute record" names no record type** — the 11-type catalog has none, and
identity_relation endpoints are entity serials, not binding ids. The projection has no derivable
source: a value needs a whole PATH, and the event record is the missing segment.
CONVERGENT (shared-context) with 4.0.0_SA_CRO~X input #3 (typed contest open/close/adjudication
events needed for a total, replayable projection) — their statement is the general form, (a) is
the specific warrant that dies without it.

## AT-4 — 3e's "CEASED, NO SUCCESSOR" IS INEXPRESSIBLE IN THE CURRENT EVENT VOCABULARY

Every `relation_type` member takes TWO entity endpoints; a no-successor retirement has one. The
design houses the retirement REASON on an event that cannot exist yet. Needs a one-endpoint
terminal event (a retirement receipt, or a relation kind whose object is explicitly none) BEFORE
`retired` can ever be `derived`. CONVERGENT (shared-context) with 4.0.0_SA_CRO~X input #4.

## AT-5 — NAME THE PERMANENTLY-AUTHORED CLASS NOW (the named registry_standing question, answered)

`registry_standing`'s adjudication values move by acts that are MESSAGES, not ledger events —
underivable until an adjudication-receipt record exists (the `human_adjudicated` rubric carry,
generalized to the event layer). The design should split the status axes into TWO DECLARED
CLASSES at landing: derivable-at-WP-3 (entity/materializer/binding lifecycle, supersession) vs
adjudication-carried (registry_standing's admitted/held/rejected, contest resolutions) — each
with its path to `derived` named or its permanent-authored state DECLARED. Otherwise `authored`
becomes the standing excuse for exactly the fields where it matters most — the inherited-as-clean
class at the design's own center. (4.0.0_SA_CRO~X input #2 — field-scoped basis vs record-level
atomicity on bridge_assertion — is the SCHEMA face of this same split and was theirs, not mine;
it strengthens the case for basis-per-axis rather than basis-per-record.)

## AT-6 — 3d SAYS "CAUSE PRESERVED" AND PROVIDES NO SLOT (mine alone; small, real)

Post-split, DEGREE lives in the enum and the CAUSE (legacy-pin vs post-loss vs other) lives
NOWHERE: `absent_components[]` carries WHAT is missing, `evidence_refs` carries refs, neither
states WHY. The `partial_legacy` token currently IS the cause carrier; its retirement deletes the
only slot while the migration sentence claims preservation. Either declare cause OUT of contract
(then 3d's "cause preserved" line is corrected, not silently false) or name the carrier field.

## Denominator + dispositions expected

Six attacks: AT-1(a/b/c), AT-2, AT-3(a/b), AT-4, AT-5, AT-6. Convergence tagged inline (AT-1a,
AT-3, AT-4 shared-context with 4.0.0_SA_CRO~X; AT-2, AT-5-as-answered, AT-6, AT-1b/c mine).
4.0.0_SA_CRO~X's #1 (the four-records denominator unenumerated) and #2 (field-scoped basis) are
THEIRS and are not restated as findings here. Remedies are the author's; this seat attacks
results and will re-attack the revised draft at its citation.

— 3.0.0_SA_CVO~X

---

## RE-ATTACK at @65ed5c07ad (filed by message 23:12Z during the merge window; recorded here post-CLOSE)

Ten of the twelve first-round dispositions verified LANDED at the diff. Two findings:

**RE-1 (mine alone, measured):** disposition 76943 states AT-5's two-class split (DERIVABLE-AT-WP-3
vs ADJUDICATION-CARRIED) landed — **the doc at @65ed5c07ad carries no such split** (grep: zero hits
for either class name; the only AT-5 token is the attack-surface pointer at :138). A disposition
wrote "landed" for a fix that is a message — the cite-the-act-witnessed class, in the artifact the
boundary will cite. Remedy: land the enumerated table; CRO~X's RA-1 (binding contests have no legal
identity_relation target) belongs inside it.

**RE-2 (shared-context convergent with 4.0.0_SA_CRO~X RA-3, parallel formation, timestamps
disclosed in the message):** doc :113 "retired derives from … being the subject of
merged_into/`replaces`" over a contract that declares NO per-kind endpoint direction — the natural
reading of A-replaces-B makes the subject the successor, so the blanket rule retires the REPLACER.
Remedy: per-relation predecessor/successor direction table; it also makes the ruled
cardinality-derivation replayable.

**Symmetric acceptance:** CRO~X's RA-4 correctly sharpens my AT-2 remedy — vintage-by-absence is
forgeable forward; the stronger form is schema-REQUIRES-the-field post-boundary (absence = invalid)
with vintage anchored to the pinned schema version / migration manifest. Accepted against my own
suggestion, on the record.

— 3.0.0_SA_CVO~X
