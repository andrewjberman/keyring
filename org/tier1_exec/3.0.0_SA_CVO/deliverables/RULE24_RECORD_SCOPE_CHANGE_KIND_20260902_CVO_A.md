# Rule 24 record: `scope_change_kind`

**Date:** 2026-09-02  
**Author and axis owner:** `3.0.0_SA_CVO~A`  
**Proposal:** `CANONICAL_LOOP_ADVERSARIAL_REVIEW_20260902_CVO_A.md` @ `0d272d257c`  
**Implementation reviewed:** `cf70842564c20e52283042c68c726f0d70be4971`  
**Schema:** `org/surprise_channel/schemas/remediation_row.schema.json`  
**Consumer:** `.tools/surprise-row-gate.py`  

Rule 24 requires a value-enum proposal to carry its four-postulate record and a word-boundary token census. This record closes that debt for:

```text
scope_change_kind = CONTRADICTS_NAMED_OUTCOME | REQUIRES_UNNAMED_OUTCOME
```

## Four postulates

### (i) MECE over a declared domain

**Declared domain:** one remediation row already adjudicated as `route=SCOPE_CHANGE`, at the PRD version against which the finding was surfaced. The axis asks one question: **does the outcome-level scope defect attach to an outcome the PRD names, or does the required outcome have no named member in that PRD?**

- `CONTRADICTS_NAMED_OUTCOME`: the PRD names the outcome and the grounded world/remedy contradicts that named outcome. The row must carry its real permanent `FWD-n` reference.
- `REQUIRES_UNNAMED_OUTCOME`: no named outcome covers the required result. The row must carry the `outcome_ref` key with value `null` plus usable `proposed_outcome` text; step 2, not the filer, allocates the next permanent `FWD-n`.

The values are mutually exclusive on the existence of a named outcome and collectively exhaustive over the declared SCOPE_CHANGE domain: a matching named outcome either exists or does not. The uncovered-member hunt found no third valid state:

- an unresolved or malformed reference is invalid evidence and must be refused, not represented by a third value;
- a gap contained by an existing decomp cell or requiring a missing cell belongs to `SPEC_ERROR` or `DECOMP_INVALIDATING`, outside this domain;
- a false finding is dismissed on the investigation plane and never becomes a remediation route;
- a progress state belongs to `remediation.state`, not this axis.

### (ii) Same grain

Both values classify **one SCOPE_CHANGE remediation row's relationship to one PRD version's named-outcome set**. Neither value classifies the whole PRD, a decomp cell, a task order, an owner, a delivery event, or the remediation's progress.

### (iii) Intent coherence

The axis has one intent: select the outcome-level payload step 2 must receive.

- Named branch: an existing `FWD-n` to revisit.
- Unnamed branch: required-null plus proposed outcome text from which step 2 can mint a new `FWD-n`.

It does not encode destination (`route` and locked `loop_target` do that), ownership (`owner`), severity (`class`/`hazard_standing`), or completion (`remediation.state`/`closed`). `FWD-NONE` is forbidden because it would make the identifier field carry non-existence and collapse the axis into its payload.

### (iv) State coherence

This is a filing-time classification, not a progress state. **No remediation operation moves a row from one value to the other.**

- Revising a named outcome can resolve a `CONTRADICTS_NAMED_OUTCOME` row, but the immutable historical row remains classified by the PRD version it contradicted.
- Minting the proposed outcome can resolve a `REQUIRES_UNNAMED_OUTCOME` row, but the historical row does not mutate into `CONTRADICTS_NAMED_OUTCOME`; a later defect against the newly named outcome is a new row.
- Work progress moves `remediation.state`; PRD evolution may overtake the obligation; neither rewrites `scope_change_kind` in place.

Thus one remedy can close either branch, but it does not move both values together or convert one into the other. Corrections append a new identity under the channel's append-only law.

## Word-boundary token census

### Canonical channel population

Direct fenced-JSON enumeration over `org/surprise_channel/**/REMEDIATION_v*.md`:

```text
remediation documents = 1
remediation rows      = 1
malformed blocks      = 0
route=SCOPE_CHANGE    = 0

CONTRADICTS_NAMED_OUTCOME = 0 rows
REQUIRES_UNNAMED_OUTCOME   = 0 rows
```

The sole remediation row is `NFRA_PIPELINE-S1`; it is legacy and has no `route`. Therefore the correct declared-domain denominator is **0 SCOPE_CHANGE rows**, not one. This is truthful zero population, not non-execution of the census.

### Current repository token occupancy

`comp-find` word-boundary scans, `--corpus all --all`, at 2026-09-02 18:0xZ:

```text
CONTRADICTS_NAMED_OUTCOME
  24 hits / 144,963 files scanned
  SURFACED=9  CONFIG=2  DOC=13

REQUIRES_UNNAMED_OUTCOME
  31 hits / 144,963 files scanned
  SURFACED=13 CONFIG=3  DOC=15

shared scope boundary
  71,635 EPHEMERAL-FLOOR files not searched
  6 UNREADABLE files not searched
  4,181 BINARY files not searched
```

Every returned occurrence belongs to this proposal's gate implementation, schema, red/green controls, review artifacts, design incorporation, or message relays. No returned occurrence carries an independent pre-existing meaning.

### Pre-proposal collision control

Exact `git grep -w` against the parent of proposal commit `0d272d257c`, pin `1bb676905566ef64d964c14a9f475c85571bc27c`:

```text
tracked-file denominator             = 29,796
CONTRADICTS_NAMED_OUTCOME hits       = 0
REQUIRES_UNNAMED_OUTCOME hits        = 0
```

**Collision verdict:** both value tokens were unoccupied before this proposal. The current hits are propagation of this same axis, not semantic collisions.

## Cost and non-application

**Cost:** one two-value field on SCOPE_CHANGE remediation rows plus one conditional payload. The gate already consumes it and refuses an absent kind, false sentinel, invalid real reference, absent required-null key, or unusable proposed outcome.

**Non-application:** investigation rows and remediation rows routed `SPEC_ERROR` or `DECOMP_INVALIDATING` do not acquire a `scope_change_kind`. Legacy remediation rows are not backfilled. Zero current SCOPE_CHANGE population is a measured empty domain, not a reason to force the enum onto another route.

## Ruling

The two-value enum is **RATIFIED with this record**. Its effective implementation remains subject to the separate canonical-loop release hold and the RC1/RC2 end-to-end gate repairs recorded at `0dbf12ebb3`; this taxonomy ruling does not lift that hold.

-- 3.0.0_SA_CVO~A
