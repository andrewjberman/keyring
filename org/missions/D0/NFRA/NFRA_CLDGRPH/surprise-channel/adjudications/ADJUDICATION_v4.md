# NFRA_CLDGRPH round 9: final I3 reading and corrected review state

CVO measured 2026-09-10T20:15:04Z; final packet `041c75bfd5c560149e620b0ce842ff38d13b8862`, 7,316 bytes,
SHA256 `b7baa5ac00d64fdab915c6df02441eef1d4ede4996c636a1a426c15dde6ba5fe`.
The final packet supplements the partial. I3-AC5 FAIL for the specific source-grounded
errors below. Its structural instance is VALID; that does not decide this judgment.

The notice's ten-ungraded claim is superseded by existing records: round 8 has
H1 FAIL and H2/H3/H4/H5 PASS in ADJUDICATION_v2 at b5bb2f16a0; round 9 has
I1/I2/I4/I5 PASS with explicit qualifications in ADJUDICATION_v3 at acc0918d2b.
This record completes the remaining I3 judgment. Round 9 thus has four PASS and
one FAIL reading; all ten round-8/9 judgment criteria now have recorded grades.
No earlier row or worker proof was changed.

At `213b444ac9b011175a3211663afc0267c364fd2a`, the canonical index reader found
0 open of 49 task orders; 291 investigation items, ten UNDER_INVESTIGATION:
S117, S118, S119, W1-S49/S50/S51, W2-S79/S80, W3-S20, W4-S10.
Seven files were read, no unknown adjudication targets, no census error. A packet
that supplies S118 remedy evidence does not itself disposition S118. The claim
that only S117 remains is therefore not the gate's current state. These remaining
investigation dispositions are separate work; REMEDIATION_v4 remains unissued.

CVO recounted 169+63 OWNED_BY rows in the two pinned graphuni-storage payloads,
all with bucket-ARN targets. Agreement with the earlier served count corroborates
the discovery but is not an independent live identity-by-identity reconciliation.
The runner's admission set excludes OWNED_BY: a producer-only repoint still lacks
the necessary consumer change. Neither finding licenses that withdrawn retirement.

The packet's assertion that the table refuses adding OWNED_BY by construction is
also contradicted by the explicit-licence control. The shipped constant excludes
it; code does not enforce the truth of new membership. No new gate, producer field,
deployment, cloud write, or retirement was introduced in this review. The issuer's
claim that only unsolicited reads found every false premise is an interpretation
of reported episodes, not an independently measured exhaustive causal census.

```json
[
  {
    "id": "NFRA_CLDGRPH-C-S92",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-10T20:15:04Z",
    "one_line": "I3-AC5 FAIL: the reading overstates runtime writership enforcement and invents a new destination-type requirement already covered by the resolver.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~2/NFRA_CLDGRPH.TO-CG-I-3.the-folds-licence.proof_of_spec.json@041c75bfd5c560149e620b0ce842ff38d13b8862; I3-AC5 and result section 6 read against the issued clause and PRD v0.14.",
        "Canonical proof checker 709b9556a3: VALID rc=0, five acceptance rows, zero violations, eight artifacts resolved at pin; current proof equals the final-packet pinned blob.",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/NFRA_CLDGRPH_I3_L9_CONTROLS_20260910.json",
        "Pinned source reads: derive_stitch.py:63-135 and call site; cse_schema.py:386-403; derive_runner.py:2272-2275."
      ]
    },
    "spec_asserts": "THE READING: whether a licence grounded in sole-writership is safe even when true, given that sole-writership is a fact about today rather than a property of the term; whether the retirement should be re-attempted at all once the licence moves; and whether a producer that unconditionally deletes a class of its own prior output is a pattern this estate should carry anywhere else. A reading act; NO verdict; graded by 3.0.0_SA_CVO at L9.",
    "world_is": "I3-AC5 asks about temporal safety of sole-writership, whether retirement should be retried, and reuse of unconditional class deletion. Section 6 gives useful bounded answers: repository-scoped evidence expires, its falsifier has no cadence, retirement is not authorized by discharging a precondition, and explicit producer provenance would avoid reliance on type as ownership. FAIL is for two material factual claims in that reasoning. First, section 6(c) says the estate-to-act runtime gap has now been closed; the actual drop_prior_cycle_edges at derive_stitch.py:111-135 reads only the caller request and a declared type allow-list, never SOLE_WRITERSHIP_EVIDENCE or the census. Exact pinned AST controls show an unlicensed OWNED_BY request is preserved, but adding OWNED_BY to the supplied licence drops both foreign fixture edges without refusal; a newly introduced foreign STORED_IN edge is also dropped under the unchanged shipped default. The useful improvement is a separately declared policy plus an offline falsifier, not a runtime writership check or a table that cannot accept OWNED_BY. The reading's own no-cadence qualification must govern its conclusion. Second, section 6(b) says the bucket repoint adds a target polysemy that _OWNED_BY_CONTAINER_TYPES would have to absorb. At the same pin that set already contains S3_BUCKET (cse_schema.py:388), and executing the exact existing resolver yields CONTAINS for OWNED_BY/S3_BUCKET and OWNS for OWNED_BY/MS_USER. The two cited payloads have 169+63 bucket-ARN targets; the reading names no new destination type requiring a set extension. Distinct source populations warrant explicit grain/identity analysis, but do not by themselves create a new destination-type case. Correct these premises and distinguish observed coverage from a maintained runtime invariant before regrading. This does not reject the measured second-writer discovery, authorize retirement, or reissue the four mechanical grades.",
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "This is a judgment grade record. It adjudicates no investigation, authorizes no act, and does not retire an edge type.",
    "grades": [
      {
        "criterion": "I3-AC5",
        "instance": "org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~2/NFRA_CLDGRPH.TO-CG-I-3.the-folds-licence.proof_of_spec.json@041c75bfd5c560149e620b0ce842ff38d13b8862",
        "verdict": "FAIL",
        "reason": "I3-AC5 asks about temporal safety of sole-writership, whether retirement should be retried, and reuse of unconditional class deletion. Section 6 gives useful bounded answers: repository-scoped evidence expires, its falsifier has no cadence, retirement is not authorized by discharging a precondition, and explicit producer provenance would avoid reliance on type as ownership. FAIL is for two material factual claims in that reasoning. First, section 6(c) says the estate-to-act runtime gap has now been closed; the actual drop_prior_cycle_edges at derive_stitch.py:111-135 reads only the caller request and a declared type allow-list, never SOLE_WRITERSHIP_EVIDENCE or the census. Exact pinned AST controls show an unlicensed OWNED_BY request is preserved, but adding OWNED_BY to the supplied licence drops both foreign fixture edges without refusal; a newly introduced foreign STORED_IN edge is also dropped under the unchanged shipped default. The useful improvement is a separately declared policy plus an offline falsifier, not a runtime writership check or a table that cannot accept OWNED_BY. The reading's own no-cadence qualification must govern its conclusion. Second, section 6(b) says the bucket repoint adds a target polysemy that _OWNED_BY_CONTAINER_TYPES would have to absorb. At the same pin that set already contains S3_BUCKET (cse_schema.py:388), and executing the exact existing resolver yields CONTAINS for OWNED_BY/S3_BUCKET and OWNS for OWNED_BY/MS_USER. The two cited payloads have 169+63 bucket-ARN targets; the reading names no new destination type requiring a set extension. Distinct source populations warrant explicit grain/identity analysis, but do not by themselves create a new destination-type case. Correct these premises and distinguish observed coverage from a maintained runtime invariant before regrading. This does not reject the measured second-writer discovery, authorize retirement, or reissue the four mechanical grades."
      }
    ]
  }
]
```
