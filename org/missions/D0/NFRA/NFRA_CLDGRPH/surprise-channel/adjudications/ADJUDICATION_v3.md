# NFRA_CLDGRPH round 9: four partial-packet L9 judgments

CVO measured at 2026-09-10T19:36:54Z. Packet pin `d1f3fc09d7ae605ff6b26da80f6597d495a55b5a`. I1-AC5, I2-AC5,
I4-AC5 and I5-AC5 PASS with the qualifications in each reason. I3 is not graded.
The four proof checkers independently returned structurally VALID; that result is
separate from these reading judgments and does not reissue the sixteen mechanical grades.

The gate's own index reader at `be7049b38003fee0fcbc899ec0d635fa0098d8bd`
found 289 investigation items across six files, no unknown targets, and eight
UNDER_INVESTIGATION: S117, S118, W2-S79, W3-S20, W4-S10, W1-S49, W1-S50, W1-S51.
One of 49 task orders remains pending: TO-CG-I-3. F11 is superseded.
Thus the remaining preconditions are broader than S117/I3 alone. These grade rows
adjudicate none of those eight items. REMEDIATION_v4 remains an unissued draft.

Controls exercise local predicate/key/resolver logic only. No AWS write, workflow
dispatch, deployment or producer run was performed. I1's first two harness attempts
had argument errors; the subsequent captured five-pair evaluation passed. Prior
adjudication rows and worker evidence are unchanged. This is not project closure.

```json
[
  {
    "id": "NFRA_CLDGRPH-C-S88",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-10T19:36:54Z",
    "one_line": "Round-9 I1-AC5 PASS on the bounded reading, with material evidence limits in the grade reason.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "L8_PACKET.round9.partial.md@d1f3fc09d7ae605ff6b26da80f6597d495a55b5a; PRD v0.14 and the issued I1-AC5 clause.",
        "org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~1/NFRA_CLDGRPH.TO-CG-I-1.key-collision-settled-and-closed.proof_of_spec.json@d1f3fc09d7ae605ff6b26da80f6597d495a55b5a; canonical checker independently returned VALID rc=0 with zero violations.",
        "CVO controls and precondition snapshot: org/tier1_exec/3.0.0_SA_CVO/deliverables/NFRA_CLDGRPH_ROUND9_L9_CONTROLS_20260910.json."
      ]
    },
    "spec_asserts": "THE READING: whether closing this at the writer is the right layer or merely the reachable one; whether a key space two classes can both claim is a schema defect that will recur under a different pair; and whether CG-s-33's re-point should still deploy at all once the collision is closed, or becomes redundant. A reading act; NO verdict; graded by 3.0.0_SA_CVO at L9.",
    "world_is": "I1-AC5 asks for the repair layer, recurrence across class pairs, and whether CG-s-33 becomes redundant. Section 8, read with section 3, answers all three: the filtered writer is a direct repair for destructive matching; five colliding class pairs demonstrate broader ambiguous identity; retaining nodes does not correct the meaning of SERVED_FROM endpoints. CVO executed the exact old and new _match_filter ASTs with real PyIceberg evaluation over all five reported class-pair fixtures: the old predicate matched the foreign-class row in all five; the new predicate preserved it while matching its own row and excluding a distinct row. This supports the filtered-predicate limb, not a full overwrite or deployment. The claim that whole-table writers cannot destroy foreign rows is false as a general statement; the supported distinction is that they do not perform this filtered-delete mechanism. The proposed deployment ordering is an inference from the two defects, not an exercised ordering measurement. PASS is on the bounded layer and non-redundancy reading; it neither closes the remaining key ambiguity nor certifies source as deployed. Lost rows, stale-on-delete policy behavior, other callers and deployed artifact vintage remain outside this repair.",
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "This row records a judgment grade; it opens and adjudicates no investigation and supplies no deployment authorization.",
    "grades": [
      {
        "criterion": "I1-AC5",
        "instance": "org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~1/NFRA_CLDGRPH.TO-CG-I-1.key-collision-settled-and-closed.proof_of_spec.json@d1f3fc09d7ae605ff6b26da80f6597d495a55b5a",
        "verdict": "PASS",
        "reason": "I1-AC5 asks for the repair layer, recurrence across class pairs, and whether CG-s-33 becomes redundant. Section 8, read with section 3, answers all three: the filtered writer is a direct repair for destructive matching; five colliding class pairs demonstrate broader ambiguous identity; retaining nodes does not correct the meaning of SERVED_FROM endpoints. CVO executed the exact old and new _match_filter ASTs with real PyIceberg evaluation over all five reported class-pair fixtures: the old predicate matched the foreign-class row in all five; the new predicate preserved it while matching its own row and excluding a distinct row. This supports the filtered-predicate limb, not a full overwrite or deployment. The claim that whole-table writers cannot destroy foreign rows is false as a general statement; the supported distinction is that they do not perform this filtered-delete mechanism. The proposed deployment ordering is an inference from the two defects, not an exercised ordering measurement. PASS is on the bounded layer and non-redundancy reading; it neither closes the remaining key ambiguity nor certifies source as deployed. Lost rows, stale-on-delete policy behavior, other callers and deployed artifact vintage remain outside this repair."
      }
    ]
  },
  {
    "id": "NFRA_CLDGRPH-C-S89",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-10T19:36:54Z",
    "one_line": "Round-9 I2-AC5 PASS on the bounded reading, with material evidence limits in the grade reason.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "L8_PACKET.round9.partial.md@d1f3fc09d7ae605ff6b26da80f6597d495a55b5a; PRD v0.14 and the issued I2-AC5 clause.",
        "org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~2/NFRA_CLDGRPH.TO-CG-I-2.edge-side-drop-and-the-blind-check.proof_of_spec.json@d1f3fc09d7ae605ff6b26da80f6597d495a55b5a; canonical checker independently returned VALID rc=0 with zero violations.",
        "CVO controls and precondition snapshot: org/tier1_exec/3.0.0_SA_CVO/deliverables/NFRA_CLDGRPH_ROUND9_L9_CONTROLS_20260910.json."
      ]
    },
    "spec_asserts": "THE READING: whether a check whose key set predates the act it checks is a bug or a category error that will recur wherever a producer both reads and writes one collection; and whether the node-side drop should have shipped at all without its edge-side half. A reading act; NO verdict; graded by 3.0.0_SA_CVO at L9.",
    "world_is": "I2-AC5 asks whether a check over pre-mutation keys represents a recurring conceptual error, and whether the node drop should have shipped without an edge drop. Section 6 distinguishes the intentionally early fresh_objs set from an accidentally inherited early aws_keys set and explains the self-agreement of stale keys with stale endpoints. CVO executed the exact old assignment and new assignment/loop from derive_stitch.py: the old result retained stale-id; the new result excluded it and retained both current-id and current-arn. The reading justifies removing false node claims while restoring detection before considering an edge deletion with no safe provenance discriminator: READS/WRITES also carry genuine AWS edges. PASS does not establish a complete edge cleanup or live magnitude. The new check can change validation failures and exit behavior; being output-nonmutating does not make it operationally inert. Nor does every read/write producer necessarily have this bug: the recurrence requires a validation set whose vintage does not match the property being asserted. No production execution or deployment is inferred.",
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "This row records a judgment grade; it opens and adjudicates no investigation and supplies no deployment authorization.",
    "grades": [
      {
        "criterion": "I2-AC5",
        "instance": "org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~2/NFRA_CLDGRPH.TO-CG-I-2.edge-side-drop-and-the-blind-check.proof_of_spec.json@d1f3fc09d7ae605ff6b26da80f6597d495a55b5a",
        "verdict": "PASS",
        "reason": "I2-AC5 asks whether a check over pre-mutation keys represents a recurring conceptual error, and whether the node drop should have shipped without an edge drop. Section 6 distinguishes the intentionally early fresh_objs set from an accidentally inherited early aws_keys set and explains the self-agreement of stale keys with stale endpoints. CVO executed the exact old assignment and new assignment/loop from derive_stitch.py: the old result retained stale-id; the new result excluded it and retained both current-id and current-arn. The reading justifies removing false node claims while restoring detection before considering an edge deletion with no safe provenance discriminator: READS/WRITES also carry genuine AWS edges. PASS does not establish a complete edge cleanup or live magnitude. The new check can change validation failures and exit behavior; being output-nonmutating does not make it operationally inert. Nor does every read/write producer necessarily have this bug: the recurrence requires a validation set whose vintage does not match the property being asserted. No production execution or deployment is inferred."
      }
    ]
  },
  {
    "id": "NFRA_CLDGRPH-C-S90",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-10T19:36:54Z",
    "one_line": "Round-9 I4-AC5 PASS on the bounded reading, with material evidence limits in the grade reason.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "L8_PACKET.round9.partial.md@d1f3fc09d7ae605ff6b26da80f6597d495a55b5a; PRD v0.14 and the issued I4-AC5 clause.",
        "org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~3/NFRA_CLDGRPH.TO-CG-I-4.dated-archive-key-is-a-mutable-pointer.proof_of_spec.json@d1f3fc09d7ae605ff6b26da80f6597d495a55b5a; canonical checker independently returned VALID rc=0 with zero violations.",
        "CVO controls and precondition snapshot: org/tier1_exec/3.0.0_SA_CVO/deliverables/NFRA_CLDGRPH_ROUND9_L9_CONTROLS_20260910.json."
      ]
    },
    "spec_asserts": "THE READING: whether a key grammar that reads immutable and is not is a naming bug or a storage-design decision nobody wrote down; whether an unversioned bucket holding an ARCHIVE is defensible; and what an estate should require of a citation before it is allowed into a record that later rounds will lean on. A reading act; NO verdict; graded by 3.0.0_SA_CVO at L9.",
    "world_is": "I4-AC5 asks whether the mutable dated key is a naming bug or undocumented design, whether unversioned retention is defensible, and what makes a citation usable. The reading identifies a documented but unmet design: CVO read the run-unique archive key requirement in NFRA_GLOBGRPH_PRD.md:187-194, record-retention-policy-v1.md:15-20, and shared-infra/s3.tf:299-315 at b5bb2f16a0, then the actual date-only key and unconditional put_object at derive_runner.py:484-499 at that pin. Unversioned storage can implement retention with unique retained keys; the actual date-only writer does not implement that premise. The proposed bucket/key plus explicitly bound vintage cue distinguishes an artifact citation from a mutable pointer. CVO counted the pinned census JSON: 118 rows = 21 STILL_VALID + 12 OVERWRITTEN + 85 UNDECIDABLE, over the disclosed project population, not the estate. PASS does not turn the 85 unknown citations into proved loss, claim that no copy could exist elsewhere, or make an ETag a retention guarantee. Worker S3 observations remain attributed to the 18:37:38Z capture, not independently repeated live by CVO. Key uniqueness still requires retention/access behavior, and the filed remedy remains unexecuted.",
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "This row records a judgment grade; it opens and adjudicates no investigation and supplies no deployment authorization.",
    "grades": [
      {
        "criterion": "I4-AC5",
        "instance": "org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~3/NFRA_CLDGRPH.TO-CG-I-4.dated-archive-key-is-a-mutable-pointer.proof_of_spec.json@d1f3fc09d7ae605ff6b26da80f6597d495a55b5a",
        "verdict": "PASS",
        "reason": "I4-AC5 asks whether the mutable dated key is a naming bug or undocumented design, whether unversioned retention is defensible, and what makes a citation usable. The reading identifies a documented but unmet design: CVO read the run-unique archive key requirement in NFRA_GLOBGRPH_PRD.md:187-194, record-retention-policy-v1.md:15-20, and shared-infra/s3.tf:299-315 at b5bb2f16a0, then the actual date-only key and unconditional put_object at derive_runner.py:484-499 at that pin. Unversioned storage can implement retention with unique retained keys; the actual date-only writer does not implement that premise. The proposed bucket/key plus explicitly bound vintage cue distinguishes an artifact citation from a mutable pointer. CVO counted the pinned census JSON: 118 rows = 21 STILL_VALID + 12 OVERWRITTEN + 85 UNDECIDABLE, over the disclosed project population, not the estate. PASS does not turn the 85 unknown citations into proved loss, claim that no copy could exist elsewhere, or make an ETag a retention guarantee. Worker S3 observations remain attributed to the 18:37:38Z capture, not independently repeated live by CVO. Key uniqueness still requires retention/access behavior, and the filed remedy remains unexecuted."
      }
    ]
  },
  {
    "id": "NFRA_CLDGRPH-C-S91",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-10T19:36:54Z",
    "one_line": "Round-9 I5-AC5 PASS on the bounded reading, with material evidence limits in the grade reason.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "L8_PACKET.round9.partial.md@d1f3fc09d7ae605ff6b26da80f6597d495a55b5a; PRD v0.14 and the issued I5-AC5 clause.",
        "org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~4/NFRA_CLDGRPH.TO-CG-I-5.hop-1-producer-home.proof_of_spec.json@d1f3fc09d7ae605ff6b26da80f6597d495a55b5a; canonical checker independently returned VALID rc=0 with zero violations.",
        "CVO controls and precondition snapshot: org/tier1_exec/3.0.0_SA_CVO/deliverables/NFRA_CLDGRPH_ROUND9_L9_CONTROLS_20260910.json."
      ]
    },
    "spec_asserts": "THE READING: whether a production input with no committed producer in a production location is a bigger finding than the vintage it was found through; whether a deliberately pinned literal with no update step is a design or a defect; and what an estate should require before a hand-run script is allowed to feed a served artifact five times. A reading act; NO verdict; graded by 3.0.0_SA_CVO at L9.",
    "world_is": "I5-AC5 asks about the durable producer gap, the literal pin, and repeated manual feeding of a served artifact. Section 6 supplies a concrete ownership/provenance gap beyond one stale vintage, distinguishes a once-correct gitlink literal from a maintained relationship, and proposes recording the automated substitute and an owned repeated-use defect without inventing a new approval system. The worker's captured run census corrects the order's unrun premise: 855 runs, eight successes before portal checkout existed, zero successes in the 847 later runs. CVO reads this as 847 non-successes, not 847 proven failures: the same capture reports 832 failures and 15 other states overall. CVO independently executed the exact new resolver block at a658d981cd: the positive resolves the current portal gitlink; non-gitlink and absent-path controls refuse with rc=1 and no ref output. The checkout binds that step output. PASS accepts these three bounded answers. Claims that only the vintage question could discover the issue, every prior seat was correct, or no other instrument could see it are unsupported universals and are not adopted. The captured history is attributed, not a fresh CVO GitHub census; hand-produced zips can be fresh while this automated route fails. Local resolver success does not prove credentials, workflow execution, publication, hand-route retirement or production remediation.",
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "This row records a judgment grade; it opens and adjudicates no investigation and supplies no deployment authorization.",
    "grades": [
      {
        "criterion": "I5-AC5",
        "instance": "org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~4/NFRA_CLDGRPH.TO-CG-I-5.hop-1-producer-home.proof_of_spec.json@d1f3fc09d7ae605ff6b26da80f6597d495a55b5a",
        "verdict": "PASS",
        "reason": "I5-AC5 asks about the durable producer gap, the literal pin, and repeated manual feeding of a served artifact. Section 6 supplies a concrete ownership/provenance gap beyond one stale vintage, distinguishes a once-correct gitlink literal from a maintained relationship, and proposes recording the automated substitute and an owned repeated-use defect without inventing a new approval system. The worker's captured run census corrects the order's unrun premise: 855 runs, eight successes before portal checkout existed, zero successes in the 847 later runs. CVO reads this as 847 non-successes, not 847 proven failures: the same capture reports 832 failures and 15 other states overall. CVO independently executed the exact new resolver block at a658d981cd: the positive resolves the current portal gitlink; non-gitlink and absent-path controls refuse with rc=1 and no ref output. The checkout binds that step output. PASS accepts these three bounded answers. Claims that only the vintage question could discover the issue, every prior seat was correct, or no other instrument could see it are unsupported universals and are not adopted. The captured history is attributed, not a fresh CVO GitHub census; hand-produced zips can be fresh while this automated route fails. Local resolver success does not prove credentials, workflow execution, publication, hand-route retirement or production remediation."
      }
    ]
  }
]
```
