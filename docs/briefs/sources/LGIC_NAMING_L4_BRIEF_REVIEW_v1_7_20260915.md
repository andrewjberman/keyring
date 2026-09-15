# LGIC_NAMING v1.7 — L4-R brief review

Author: `4.0.0_SA_CRO` · UTC: 2026-09-15 ~02:05Z · request: CTO messages 96816 (delivery) and 96817 (change note).

**VERDICT: SIGNED, brief half.** v1.7 is an L10 addendum. It adds five round-2 rulings to S14 (FN1b, FN1c, DM,
POS, EX1) and corrects N3's briefing. Each summary line matches the round-2 analysis and the schema, and none of them
contradicts the brief or another line of this half. The coverage table, the arc and every other cell are unchanged.

## Exact inputs and scope

- PRD: `org/missions/D14/LGIC/LGIC_NAMING/prd/LGIC_NAMING_PRD.md@02f08322af1fc9eb8b18117e6b187749fc4d15df`, v1.7,
  286 lines, 27,362 bytes. The file's latest commit is the pin, and the worktree matched HEAD at review.
- Brief: `docs/briefs/d14-naming-schema-brief-20260913.md@1b42dbe758`. Heading denominator: 22.
- Reviewed brief-half SHA-256: `3bc6d473ac3e26dcc605f45f09b8fce5e9e410ef5a49064a37472f9b206930a4`, computed by
  `prd_signoff_lib.half_hashes`. It matches the notifier's `3bc6d473ac3e`.
- Ratified-text half: `2f54ae7edbee09c9ad4a1bb561043e5903998d6aad9b7ce546d2c43c9bf6b81f`. It is unchanged since v1.4.
- Schema: `org/standards/NAMING_SCHEMA.json` v1.7 at the pin, compared as parsed JSON against v1.6 at `2706014705`.
- Source of the rulings: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_ANALYSIS_LGIC_NAMING_ROUND2_20260915.md` at
  the pin.
- Registry row: `infra/logic/registry/scopes.json` row `demo`, written by LGIC_ENFORCE EN-r-1 at `a925c8a642`.
- Prior review: `docs/briefs/sources/LGIC_NAMING_L4_BRIEF_REVIEW_v1_6_20260914.md@d60eefad00`, which SIGNED v1.6
  (stamp `8e08704fb0`).

## The change, v1.6 to v1.7

On the PRD, `git diff 2706014705 02f08322af` is 15 insertions and 2 deletions: the `prd_version` header, a v1.7
paragraph in S14 (v1.7:187–199), and the N3 cell (v1.7:224).

In the schema, seven fields moved: `changelog`, `version`, `ratified_by`, `rows_owner`, `resource.function`,
`firm_forms[demo].note` and `system.vendor_through_tiers`. `key.grammar`, `grade.signature` and `grade.verdicts` are
equal to v1.6. This agrees with the CTO's own field-by-field count in 96817.

| S14 v1.7 line | Source in the analysis | Check | Verdict |
|---|---|---|---|
| FN1b: a noun-phrase function drops every token already written in the system or scope slot | §2 RULING FN1b; `resource.function` | Read from the name alone, so it binds namer and grade. If nothing is left, the name RAISES (`grade.unplaceable`), so no fourth verdict appears. | faithful |
| FN1c: only the resource's OWN kind is barred from its function | §2 RULING FN1c; `resource.function` | It narrows v1.6's too-wide sentence (which named `host`, a word in no kind list). The 31 forms stand, as `GRADING_RULE.md` R6 already does. | faithful |
| FN1's word-choice clauses bind the namer; a grade keeps a function's words as written | §2 | Consistent with S11's signature `(name, type)`: the grade has no item description to apply word-choice rules with. Brief O5 still gets a verdict and canonical form for every name. | faithful |
| DM: `demo` reads as a firm in every naming slot, per the registry row | §3 RULING DM; `firm_forms[demo].note`; `rows_owner` | The registry row reads `class FIRM`, `tenancy FIRM`, tenant kind `demo`, read at HEAD. It agrees with the brief, which lists `demo` among the firms at IV.2 line 108, and with S4's form list. | faithful |
| POS: FWD-2's reader may be told what each position holds | §3 RULING POS | The reader gets the grammar's slot order and `firm_forms`, both from the schema, and never the item set or key. That is knowledge of the schema, not of the estate. So brief O2 and Part III O2 ("a reader who has never seen the estate") stand. | faithful |
| EX1: SY1's worked example lies outside every naming-exercise item set | §4 row S15; `system.vendor_through_tiers` | The example is now `blackdiamond-cot-build-silver-profile`. | faithful |

**N3 at v1.7:224** now consumes the identity registry, with the seed as history, and carries EX1 (no briefing spells
an item's answer) and POS (the reader is told what each position holds). This matches the analysis's §3 carrier
line. Its acceptance clause is unchanged.

**CONTRACTS row 109** ("seed … until it exists") is in the ratified-text half, and it is not returned. The clause is
conditional and now resolved. `rows_owner` states the registry governs, and no v1.7 ruling contradicts it.

## Coverage

The coverage table (v1.7:241–262), the arc and cells N1, N2 and N4–N7 are byte-identical to v1.6. So the audit of all
22 entries, as amended at v1.6 for row 17, stands. The brief denominator, 22 headings, still matches the 22 rows.

## Observation, not a ground (filed on LGIC_ENFORCE's channel)

The registry's `demo` row carries the note "a tenant class the doctrine does not define (05_IDENTITY_SPINE.md s.3,
tick-list row 17)". But the doctrine does define it:
- `02_DOCTRINE.md:60`: "`opal-data-demo`: a tenancy class that is neither firm nor general".
- `02_DOCTRINE.md:366–367`: RULED at card 8 and "KEPT as a DEMO-TENANT class".
- `06_CONFORMANCE_LEDGER.md:135`: exception X6, "a demo tenant, neither firm nor general".

So the registry's `tenancy: FIRM` and the doctrine's "neither firm nor general" disagree on the tenancy plane. For
naming this is immaterial: DM rules the naming slots from the registry's class, and the brief agrees. It is filed as
a row for the registry's owner. It is not a ground on this half.

## Limits

This is requirements acceptance only. No namer, reader, grader or `grade()` run was exercised. How many of the 68
forms change under FN1b and the own-kind bar is left, as the analysis says, to the cell that re-cuts
`GRADING_RULE.md`. The ratified-text half is `3.0.0_SA_CVO`'s.

This seat's row `LGIC_NAMING-S14` (the sign-off library reads the worktree) is recorded in the analysis's §4 as IN
PROGRESS at `1.0.0_SA_CTO`. Nothing here depends on it.

The delivered notices 96816 and 96817 were opened and READ-acked. This seat performs no push, deploy or cloud
mutation. Push state is measured and stated in the completion message to `1.0.0_SA_CTO`.
