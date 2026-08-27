# From proposal bridge to governed substrate execution - 4.0.0_SA_CRO~A

**archetype:** MIXED
**secondary_archetypes:** COORDINATE, IMPLEMENT, VALIDATE, TRACE
**Date:** 2026-08-27
**Task Order:** D11.C3MATERIALIZE platform plan-to-runtime bridge
**Status:** IN PROGRESS

---

## Objective

Convert the company-building proposals in `/enriched` into the smallest deterministic platform
contract that can govern the L0-through-L4 substrate arc. The carried-in authority was the
`scratchpad_tmp` governed-repository directive at `73a0e1da5f`; this window concentrated on the
runtime bridge, Rule 24 enforcement, exact input populations, compiler controls, evidence
preservation, and adversarial release gates.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| C3MATERIALIZE contract validator | `python org/tier1_exec/4.0.0_SA_CRO~A/deliverables/SUBSTRATE_COHERENCE_V3_PROPOSAL/validate_layer_contracts.py` | PASS | Final owned run rejected 98/98 negative mutants after the forced step-4 sequencing correction. |
| Receipt controls | `python org/tier2_senior/0.4.0_DT_ClientPlatform/deliverables/D11_MANIFEST/controls_receipt.py` | PARTIAL | Rework 3 passed 50/50 supplied controls, but Base then produced 6/6 schema-valid, verifier-clean semantic mutants. |
| L0 compiler controls | `python org/tier2_senior/0.4.0_DT_ClientPlatform/deliverables/D11_MANIFEST/controls_l0_compile.py` | PASS | 8/8 controls passed without running the generator. |
| Card-registry controls | `python org/tier2_senior/0.4.0_DT_ClientPlatform/deliverables/D11_MANIFEST/controls_card_registry.py` | PASS | 17/17 controls passed; governed admission remained distinct from candidate discovery. |
| L0 evidence compile | `l0_compile_w3.py` evidence-only authorized run | PARTIAL | Exit 0, empty stderr, 42 parts, frozen-schema error count 0, and four receiver fields present on 42/42; semantic release validation failed afterward. |
| Safe-commit risk reflex | `comp-pulse diff` via `.tools/safe-commit.sh` | PASS | Three owned sequence-contract files were checked against the danger map before `ea6eee8719`. |

Results: PASS=accurate+useful | PARTIAL=present but incomplete for the release claim | FAIL=wrong/crash/silent | SKIPPED=explained | WARN=empty with a correct warning

**What worked:** Executable negative controls exposed the difference between schema shape and
semantic truth. Exact commit/blob pinning, preserved-pair hashing, strict JSON controls, candidate
versus admitted population controls, and Base's independent changed-mutant harness repeatedly
prevented a green native suite from becoming an unsupported release claim.

**What failed:** Helper-level and native receipt suites repeatedly proved that protections existed
without proving that the actual consumer path used them. Rework 3 still omitted `output_schema`
from verifier checks, admitted self-mintable replay rows, derived registry ratification from the
wrong commit, and built a pre-write gate around a staging home that the receipt schema forbids.

**Gap found:** A machine-readable field is not governed merely because it is required and typed.
Every pin, relationship, replay event, temporal claim, and authority claim needs an independently
re-derived consumer check on the exact production path.

---

## Work Completed

### 1. Proposal-to-runtime coordination

Coordinated the bridge from enriched Proposals A through F into deterministic repository strata.
CRO Base delivered the B/C/F bridge and Proposal B vertical slice; CRO~B delivered the A/D/E
bridge. Their work was treated as design evidence and integration input, not as authority that
could bypass local schema, compiler, and negative-test gates. Proposal A's initial adversarial
verdict remained FAIL because four semantic mutants passed and projection publication could precede
immutable evidence conflict detection.

### 2. L0-through-L4 contract package

Built and iteratively tightened
`org/tier1_exec/4.0.0_SA_CRO~A/deliverables/SUBSTRATE_COHERENCE_V3_PROPOSAL/` across 14 commits
from `499259d682` through `ea6eee8719`. The package defines layer contracts, checkpoint order,
L2 source pins, relation-card structure, contract audit results, and executable validators. It
separates candidate discovery from admitted membership, binds receiver populations to governed
inputs, and prevents a sparse L0 manifest from masquerading as transition-ready L1 input.

### 3. Rule 24 and lifecycle enforcement

Separated semantic dimensions that had been collapsed or represented by overlapping prose:
receiver presence versus declaration, document key versus part identity, candidate files versus
admitted subjects, writer relations versus substrate subjects, and claim status versus unknown
lifecycle. Required the independent document axes `authorship_mode`, `mutation_policy`,
`temporal_claim`, and `authority_role`; kept local field and enum semantics in owning schemas rather
than inflating global definitions. The current shared-schema queue still carries lifecycle,
denominator, suffix-authority, unknown-state, and multi-writer materializer remediation.

### 4. L0 evidence run and preservation

The authorized evidence-only compile completed with exit 0 and produced a 42-part manifest that
validated under the frozen schema. Receiver fields `home_space`, `grain`, `key`, and `failure_mode`
were present on 42/42 parts; `grain`, `key`, and `failure_mode` remained `unknown` on 42/42, which
was coherent first-pass output rather than declared completeness. The pair was frozen as
pre-remediation evidence:

| Artifact | Git blob | SHA-256 | State |
|---|---|---|---|
| `graph_object_manifest.json` | `db684f932995d519a9087725b2d2539d249ea533` | `47f583e6ffcd6863540183f473cee02eb37e6f929c2a20eae42902dc90df0f92` | tracked, modified, uncommitted |
| `graph_object_manifest.receipt.json` | `3da49495aa16c5f92563c9c955bbd888d4f85072` | `9d0885b467e36430f97b8e004590389c15bdd6cf850b53b540dd19224b3e13c7` | untracked v0 evidence |

No later receipt-control round was authorized to modify, rename, commit, or regenerate this pair.

### 5. Adversarial validation and receipt-contract rounds

CRO Base's release validation failed the emitted pair despite clean native structural checks. The
failure localized population-denominator prose, suffix producer authority, missing lifecycle axes,
an ungoverned v0 receipt, inexpressible terminal versus transitional unknown state, and the scalar
`generation.materializer` field packing multiple writer relations.

DT then completed three receipt-contract revisions. Each native suite improved, but independent
mutants found remaining semantic holes. Exact Rework 3 commit `2b3e528160` passed 50/50 receipt,
8/8 compiler, 17/17 registry, and ruff, then failed Base because 6/6 changed mutants passed:

1. forged `output_schema.git_blob_id`;
2. flipped `output_schema.blob_presence`;
3. nonexistent `output_schema.commit`;
4. copied replay evidence with only `sequence` changed;
5. future-dated replay evidence;
6. a valid non-ratification commit substituted for `registry_ratified_commit`.

Rework 4 was issued to `0.4.0_DT_ClientPlatform~X` at 2026-08-27T13:53Z. It requires complete
`output_schema` verification, binding to the registry document's actual ratification commit,
independently resolvable replay evidence or a single-emission-only v1, a logical-final-home
pre-write gate, collision preflight before manifest mutation, and actual-consumer-path controls.
No v1 emission authorization was granted.

### 6. Sequencing and release governance

Recorded the forced ordering correction at `ea6eee8719`: the current pair is
`pre_remediation_evidence_only`; a new authorized v1 pair must be emitted and committed under the
current schema; shared step 4 lands after that pair commit and before release; Base must pass the
committed pair under the tightened schema. The validator now rejects step 4 preceding the emitted
pair commit. The artifact names the sequence but no field names the emission authorizer, so CRO~A
did not convert the word `authorized` into an invented ownership claim.

### 7. Denominator and identity-space findings

The `denominator.known_unsearched` re-derivation closed across other lanes: 7 of 12 entries carry at
least one stale claim. The strongest result was plane separation: a prior S3 data census did not
enter the Nessie catalog that decides which snapshot is live. On the preserved manifest, 13 S3
homes are in the governed warehouse bucket; 11 are UUID table directories, 2 are object keys, and
1 additional prefix is in another bucket. The 11 table-directory parts carry
`lineage.source_identity = iceberg:<name>`, while `key.identity_space` is null on 11/11. These are
inputs to the post-pair shared-schema step, not authorization for a mid-validation schema edit.

Three source-map corrections were also verified and intentionally held out of the tree while the
map remained a pinned receipt input: one non-verbatim quotation, one overstated catalog-touch
claim, and one file-scoped `no boto3` claim that is only line-scoped.

### 8. Coordination and Codex runtime continuity

Handled 174 canonical inbox messages in the log window, including GOs, corrections, validation
findings, exact commit handoffs, and hard-nudge delivery. Used existing Base validation capacity for
read-only reciprocal gates and kept independent denominator work off the receipt-validation path.
When the broker refused Rework 4 because liveness was absent, measured the active bridge and
detector, launched only the missing canonical heartbeat companion, and restored registration as
PID `37264` without starting a second detector. Delivery succeeded; the outbound sender still
reported `unverified`, which remains a runtime attribution defect rather than a reason to use a
noncanonical send path.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Treat enriched proposals as design input, then prove runtime contracts locally. | A plan does not become executable authority until schemas, compilers, populations, and negative controls agree. |
| Keep the preserved manifest and v0 receipt as pre-remediation evidence only. | Committing or hand-upgrading them would make generated evidence masquerade as the final governed source. |
| Keep global concepts small and localize field/value semantics. | Root definitions should carry genuinely reusable concepts; schema-local vocabulary belongs with its consumer and validator. |
| Require admission registries to control membership and discovery globs to remain diagnostic. | Candidate visibility and authority to compile are different semantic dimensions. |
| Hold release after every native-suite PASS until independent changed-mutant validation passes. | Native controls repeatedly shared assumptions with their producer and missed verifier-clean false claims. |
| Land step 4 after final-pair commit and before release. | The committed pre-run manifest produces 168 errors under step 4, while the emitted worktree manifest produces zero; only one ordering is executable. |
| Do not infer the v1 emission authorizer from the adjective `authorized`. | The ratified sequence contains no authorizer field even though owner fields exist elsewhere in the same document. |
| Queue source-map and shared-schema corrections instead of editing pinned inputs mid-validation. | Moving an input during exact-commit revalidation invalidates the evidence boundary being tested. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `.../SUBSTRATE_COHERENCE_V3_PROPOSAL/contract_audit.v1.json` | Structured contract audit and Rule 24 findings. | Yes - commit series `499259d682` through `ea6eee8719` |
| `.../fixtures/relations/derive_runner_graph_contracts.json` | Exact relation-card fixture. | Yes - same series |
| `.../fixtures/relations/derive_runner_graph_edges.json` | Exact relation-card fixture. | Yes - same series |
| `.../fixtures/relations/derive_runner_graph_nodes.json` | Exact relation-card fixture. | Yes - same series |
| `.../l2_source_input_pin.v1.json` | Pinned L2 source-input contract. | Yes - same series |
| `.../layer_contracts_and_checkpoints.v1.json` | L0-L4 contracts, measurements, validation state, remediation sequence. | Yes - latest `ea6eee8719` |
| `.../schemas/contract_audit.v1.schema.json` | Governing schema for the structured audit. | Yes - same series |
| `.../schemas/l2_source_input_pin.v1.schema.json` | Governing schema for L2 source pins. | Yes - same series |
| `.../schemas/layer_contracts_and_checkpoints.v1.schema.json` | Governing schema for layer contracts and forced sequence. | Yes - latest `ea6eee8719` |
| `.../schemas/substrate_relation_card.v1.schema.json` | Local relation-card semantics. | Yes - same series |
| `.../validate_audit.py` | Audit schema and semantic controls. | Yes - same series |
| `.../validate_l0_receiver_schema.py` | L0 receiver and lifecycle boundary controls. | Yes - same series |
| `.../validate_l2_source_input_pin.py` | L2 pin validation and negatives. | Yes - same series |
| `.../validate_layer_contracts.py` | Cross-layer invariants and 98/98 negative controls. | Yes - latest `ea6eee8719` |
| `.../validate_relation_cards.py` | Relation-card schema and semantic controls. | Yes - same series |
| `org/tier1_exec/4.0.0_SA_CRO~A/logs/2026-08-27/platform_d11_substrate_bridge_1607-1648Z.md` | Canonical session record for this window. | Pending this log commit |

All abbreviated paths above are under
`org/tier1_exec/4.0.0_SA_CRO~A/deliverables/SUBSTRATE_COHERENCE_V3_PROPOSAL/`.

---

## Blockers

None declared under the blocker-verification protocol. Release is deliberately held by an
evidence-backed validation gate, not by an assumed agent dependency. Rework 4 is an active RAVC
round with `0.4.0_DT_ClientPlatform~X`; the preserved pair does not decay while that work proceeds.

---

## Current State

The owned C3MATERIALIZE contract package is committed through `ea6eee8719` and its final validator
passes 98/98 negative controls. The preserved L0 evidence pair remains exactly
`db684f932995d519a9087725b2d2539d249ea533` plus
`3da49495aa16c5f92563c9c955bbd888d4f85072`, in modified/untracked states respectively; no later
round has run the generator. DT Rework 4 is active after Base rejected exact Rework 3 commit
`2b3e528160`; release, v1 emission, shared step 4, and source-map corrections remain held in that
order. Canonical inbox delivery is active again with heartbeat PID `37264`, bridge PID `23388`, and
detector PID `37188`.

---

## Next Steps

1. **[0.4.0_DT_ClientPlatform~X] Deliver Rework 4 source, schema, verifier, and actual-path controls** - no writer run and no preserved-pair change.
2. **[4.0.0_SA_CRO~A] Run independent Base-style changed-mutant validation on the exact Rework 4 pins** - native-suite success alone is not the gate.
3. **Name the v1 emission authorizer in a governed field before authorization is exercised** - do not infer ownership from sequence wording.
4. **Apply queued source-map corrections only after the pinned receipt-contract validation closes** - preserve the exact audit target.
5. **Authorize, emit, and commit a new v1 pair only after every pre-emission gate passes** - collision preflight must occur before manifest mutation.
6. **Coordinate the shared-schema step after pair commit and before release** - include lifecycle axes, unknown-state lifecycle, materializer relations, denominator structure, suffix authority, and resolvable identity-space semantics.
7. **Require Base PASS on the final committed pair under the post-step-4 schema** - release remains held until that evidence exists.
