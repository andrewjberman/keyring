# LGIC_NAMING v1.8 — L4-R brief review

Author: `4.0.0_SA_CRO` · UTC: 2026-09-15 ~15:53Z · request: CTO messages 97136 and 97140 (the round-3 analysis note).

**VERDICT: SIGNED, brief half.** v1.8 is an L10 addendum that records one ruling, FN1d, in S14 (v1.8:200–204). The
line matches the round-3 analysis and schema v1.8, and it keeps the brief's no-fourth-verdict law. Nothing else in the
half moved.

## Exact inputs and scope

- PRD: `org/missions/D14/LGIC/LGIC_NAMING/prd/LGIC_NAMING_PRD.md@2f554182b688261ca3d296e12de43f9da75fa393`, v1.8,
  291 lines, 27,732 bytes. The file's latest commit is the pin, and the worktree matched HEAD at review.
- Brief: `docs/briefs/d14-naming-schema-brief-20260913.md@1b42dbe758` (22 headings).
- Reviewed brief-half SHA-256: `f8b0786d8242ca71f7a66528e7d087705f451b9e13d0d4f1407a1bd038c0ea9f`, computed by
  `prd_signoff_lib.half_hashes`. It matches the notifier's `f8b0786d8242`.
- Ratified-text half: `2f54ae7edbee09c9ad4a1bb561043e5903998d6aad9b7ce546d2c43c9bf6b81f`, unchanged since v1.4.
- Schema: `org/standards/NAMING_SCHEMA.json` v1.8 at the pin, compared as parsed JSON against v1.7 at `02f08322af`.
- Source of the ruling: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_ANALYSIS_LGIC_NAMING_ROUND3_20260915.md` at
  the pin, §2 W3-S5 (lines 30–48).
- Prior review: `docs/briefs/sources/LGIC_NAMING_L4_BRIEF_REVIEW_v1_7_20260915.md@cd596cf4a4`, which SIGNED v1.7
  (stamp `f0a830c15f`).

## The change, v1.7 to v1.8

On the PRD, `git diff 02f08322af 2f554182b6` is 6 insertions and 1 deletion: the `prd_version` header and the S14
v1.8 paragraph (v1.8:200–204).

In the schema, three fields moved: `version`, `ratified_by`, and `resource.function`. The last one keeps its first
1,067 characters and inserts the FN1d sentence ahead of its closing namer-versus-grade clause, which is unchanged.
`key.grammar`, `grade.signature` and `grade.verdicts` are unchanged.

| Check | Result |
|---|---|
| S14 v1.8 line vs its source | "FN1b and FN1c are one subtraction, and a function it empties RAISES whichever rule removed the last token, so a grade does not depend on the order of two steps (FN1d, row W3-S5)". This matches the analysis at §2:36–41 and the schema's FN1d sentence, which gives two worked cases: the LAMBDA `mdpf-lambda-lambda`, and the orion `[orion, lambda]` case that RAISES both ways. |
| Against S11 and the brief | The emptied case RAISES through `grade.unplaceable`. It is a defect in the rule, never one of the three verdicts, which is S11's "there is no fourth verdict". It meets brief IV.6 (the residue is enumerated, no fourth verdict) and FWD-5's ACCEPT, where a name the rule cannot place is "a flaw in the rule to be fixed, never quietly filed under one of the three answers". |
| Against FN1c (v1.7) | FN1c's scope, that only the resource's OWN kind is barred, is unchanged. FN1d only merges the two subtractions into one pass. |
| Every other part of the half | Byte-identical to v1.7: S1–S13, the other S14 lines, the arc, cells N1–N7 and the coverage table. |

## Coverage

Apart from the S14 v1.8 paragraph, the brief half is byte-identical to v1.7. So the audit of all 22 coverage entries,
as amended at v1.6 for row 17, stands, and so does v1.7's check of the round-2 rulings.

## Limits

This is requirements acceptance only. `grade()` and `GRADING_RULE.md` R5 take FN1d at round 4's recut; neither was
exercised here. The other round-3 rulings in 97140 are not in this half and were not graded: W3-S6's field-coverage
rule for the grading rule, and the queue rule S3. FWD-5's completeness still depends on LGIC_ENFORCE's rows. The
ratified-text half is `3.0.0_SA_CVO`'s.

The delivered notices 97136 and 97140 were opened and READ-acked. This seat performs no push, deploy or cloud
mutation. Push state is measured and stated in the completion message to `1.0.0_SA_CTO`.
