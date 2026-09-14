# LGIC_NAMING v1.5 — L4-R brief review

Author: `4.0.0_SA_CRO` · UTC: 2026-09-14 ~19:25Z · request: CTO messages 96704 (delivery) and 96706 (change note).

**VERDICT: REFUSED, brief half.** v1.5 is an L10 addendum. It adds S14, which summarises the round-1 rulings; the
rulings themselves are data in `NAMING_SCHEMA.json` v1.5. S14 faithfully summarises the round-1 analysis, and the
rulings are in the schema. But three of them change a rule that another line of this half still states the old way:
- **R1:** AW1 against N2 and the coverage table.
- **R2:** PH1 against the arc and N6.
- **R3:** SC1 against S1 and doctrine R3.

A task order's worker face inlines cell text and L9 grades against it, so each is a second, contradictory bar inside
one half. Each fix is one or two lines. This is the same class of defect as LGIC_CANON v1.2's C2, found earlier today.

## Exact inputs and scope

- PRD: `org/missions/D14/LGIC/LGIC_NAMING/prd/LGIC_NAMING_PRD.md@de52d3db04d3ee97b12f92aea4047f4d5bf69b04`, v1.5,
  264 lines, 24,500 bytes. At review, HEAD and worktree both matched the pinned bytes (`cmp` against `git show`, and
  `git diff --quiet`).
- Brief: `docs/briefs/d14-naming-schema-brief-20260913.md@1b42dbe7582bc455fee225f663f5ef2566f8d68c`, 237 lines. Heading
  denominator: **22**, the same as at v1.4.
- Reviewed brief-half SHA-256: `be7cb62cffccee990cf6f0f5d421b6f3204f63e118735e3934620fdb79a4619b`, computed by
  `prd_signoff_lib.half_hashes` on the pinned bytes. It matches the notifier's `be7cb62cffcc`.
- Ratified-text half, identified but not signed here: `2f54ae7edbee09c9ad4a1bb561043e5903998d6aad9b7ce546d2c43c9bf6b81f`.
  It is unchanged from v1.4, so ENDPOINT and CONTRACTS are byte-unchanged.
- Schema: `org/standards/NAMING_SCHEMA.json@de52d3db04`, v1.5, compared as parsed JSON against v1.4 at `e04b802fe9`.
- Source of S14: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_ANALYSIS_LGIC_NAMING_ROUND1_20260914.md` at HEAD (landed
  in `de52d3db04`).
- Doctrine and spine read at HEAD: `infra/logic/02_DOCTRINE.md` (R2, R3) and `infra/logic/05_IDENTITY_SPINE.md`.
- Prior review: `docs/briefs/sources/LGIC_NAMING_L4_BRIEF_REVIEW_v1_4_20260914.md@5454cfaa2d`, which SIGNED v1.4 at
  brief half `3cf0e30ac9c2…c7a4`.

## The change, v1.4 to v1.5

On the PRD, `git diff e04b802fe9 de52d3db04` is 14 insertions and 1 deletion: the `prd_version` header, plus S14 at
v1.5:169–180 under THE SCHEMA (a brief-half section). No cell, coverage row, arc line or manifest row changed.

**The schema, compared as parsed data between v1.4 and v1.5.**
- One key was added: `aws_fixed` (AW1).
- Changed: `resource.function` (FN1), `resource.qualifier` (FN2, FN3), `secret.purpose` and `iam_policy.purpose_slot`
  (FN4), `key.partition` (P1), `key.scope_rule` (SC1), `system.vendor_through_tiers` (SY1), `kind.closed_at_l4` (its
  note re-spelling `-trigger/-publisher/-scanner` under FN1), and `grade` (it gains `placeholder`, PH1).
- `key.grammar` is equal. `grade.signature` and `grade.verdicts` are unchanged; only `grade.placeholder` was added.

So S14's closing line (v1.5:180), "The five ruled key segments are unchanged, and the grade stays `(name, type)`",
holds as data.

**S14 against its source.** Each of the eight one-line summaries at v1.5:172–179 matches its ruling in the round-1
analysis (§2 and §5) and the corresponding schema field. Nothing in them overstates their source. I did not
re-derive the analysis's 18-item determinism table; its author labels it a text-consistency check, not FWD-1's grade.

## R1 — AW1 against N2 and the coverage table

| Where | Pinned text |
|---|---|
| Schema `aws_fixed.rule` / S14 at v1.5:179 | "names AWS fixes are OUTSIDE the grade's domain … excluded, never a fourth verdict". `by_name.SECURITY_GROUP: ["default"]`, plus AWS-managed policies by ARN and three LOG_GROUP forms. |
| **N2 at v1.5:201**, fixtures column | "the census residue classes (camel IAM, purpose-first policies, library-first layers, **`default` security groups**, workstream-coded schedules) **each graded**" |
| **Coverage row 17 at v1.5:245** | IV.6 is consumed by "S7, S11 (the residue enumerated; no fourth verdict); N2" |
| Brief IV.6, lines 167–170 | "the domain is the 1,912 nameable live names … the residue that fits no slot after the pass (…, `default` ×2) is enumerated, not omitted" |
| Brief Part III O5, lines 85–86 | "run over the 1,912 nameable live names, prints a verdict for every one" |

`SECURITY_GROUP` is a kind-graded type in the schema (`kind.by_type`), so AW1 does not fall under an existing
exclusion. It narrows the domain the brief declared. By AW1's own measurement the narrowing is SECURITY_GROUP 1 of 26,
IAM_POLICY 9 of 417 plus `ReadOnlyAccess`, and LOG_GROUP 4 of 264.

The narrowing may well be right: those names are fixed by AWS, not minted by Opal. But this half still asks N2's
worker to grade exactly what AW1 excludes, and the coverage table records no departure from the brief's domain.

**Fix, returned by pinned line:**
- v1.5:201, N2's fixtures: replace "`default` security groups … each graded" with a disposition under AW1. The
  AWS-fixed names are enumerated as excluded, with their measured set, not graded.
- v1.5:245, coverage row 17: record AW1 as a stated narrowing of the brief's declared 1,912-name domain (IV.6 and
  Part III O5), naming the excluded set as a denominator.

## R2 — PH1 against the arc and N6

| Where | Pinned text |
|---|---|
| Schema `grade.placeholder` / S14 at v1.5:178 | a canonical form may carry `{system}` … "filled from its source: `{system}` from the identity registry's resource-to-system rows (LGIC_ENFORCE) … FWD-5's correct name is complete for a name only when no placeholder remains" |
| Round-1 analysis §1 and §8 | FWD-5 "EXACT, NOT YET COMPLETE … Completeness is carried to LGIC_ENFORCE as a dependency"; 48 of 68 firm-first canonical forms carry `{system}` |
| **Arc at v1.5:189–192** | "… because the machine is `LGIC_ENFORCE`'s … **It closes when every FWD grades REALIZED.**" |
| **N6 at v1.5:205**, acceptance | "the two gradings agree on every name, verdict and canonical form" |
| Brief O5, lines 52–54, and Part III O5, lines 85–86 | "print the conformant form beside it … the printed conformant form is the remediation spec"; "a conformant form for every non-conformant one — no `UNDETERMINED`" |

With PH1, N6 can pass on agreed canonical forms that still hold `{system}`, and those are not a remediation spec.
FWD-5's completion now waits on another project's registry rows. That cross-project dependency governs when this
project can close, and it is stated only in the analysis and the schema, not where this PRD states closure. A successor
reading the arc would take N6 passing as FWD-5 done.

**Fix, returned by pinned line:**
- v1.5:192, the arc: state that FWD-5's canonical forms are complete only when no placeholder remains, and that for
  the firm-first roles this needs LGIC_ENFORCE's resource-to-system rows.
- v1.5:205, N6: say that agreement on forms still carrying a placeholder grades FWD-5 exact, not complete.

## R3 — SC1 against S1 and doctrine R3

| Where | Pinned text |
|---|---|
| Schema `key.scope_rule` / S14 at v1.5:176 | "the key's AUDIENCE: a FIRM when the data is one firm's; global when every firm shares it. A PRODUCT key is a scope only beneath a VENDOR source …" |
| **S1 at v1.5:124** | "`{scope}` is a FIRM, PRODUCT, MASTER or `global` … (doctrine R2; **a vendor MASTER is valid, R3**)" |
| Schema `key.scope_classes` | `["FIRM", "PRODUCT", "MASTER", "GLOBAL"]`. This is the only place MASTER appears in the schema; no rule says when it applies. |
| Doctrine R3, `02_DOCTRINE.md:118–119`; spine :44, :83, :106 | "A VENDOR MASTER IS A VALID SCOPE. **Two masters of one firm are two scopes, never commingled**"; Schwab masters `08242234` and `08335338` both map to `49financial`; `{VENDOR}/{FIRM|MASTER}/{tier}/` |

A Schwab master's data is one firm's. Read literally, SC1 gives it the scope `schwab/49financial/…` and commingles both
masters under it. S1 and R3 give `schwab/08242234/…`. So two namers who each follow a line of this half write
different keys, which is the FWD-1 failure the round-1 rulings exist to close. The analysis's 18 items contain no
master key, so its dry-run could not see this.

**Fix, returned by pinned line:**
- `key.scope_rule` in the schema, and S14's SC1 line at v1.5:176: state that a vendor MASTER keeps its own scope under
  R3, and that the audience rule decides FIRM versus `global` for everything else.

## What is unaffected

The rest of the brief half is byte-identical to v1.4. Apart from rows 7, 10 and 17 as they bear on R1 and R2, the
v1.4 review's 22-entry coverage audit stands. The brief denominator, 22 headings, matches the PRD's 22 coverage rows
(v1.5:228–249).

FN1–FN4, P1, SY1 and the rest of SC1 raise no brief-half issue. SC1's product-beneath-vendor clause agrees with brief
IV.2 line 108 ("a product scope (global)") and with the spine seed.

## Limits

This is requirements review only. No grader, exercise or live census was run. The `aws_fixed` measured set is cited
as the schema states it (row W1-S4), not re-measured. The clean-context seat in the analysis's Ruling B is surfaced to
Andrew there and is not a PRD change, so this review does not grade it. The ratified-text half is `3.0.0_SA_CVO`'s and
is not re-opened by this bump. FWD-5's ACCEPT text ("for every one, including the correct name") bears on R1 and R2,
but whether it needs reading anew is the CVO's question, not this review's.

Because round 2's issuance waits on this half (LIMB 6), a v1.6 that changes only the lines named above needs no
re-audit beyond them.

The delivered notices 96704 and 96706 were opened and READ-acked. This seat performs no push, deploy or cloud
mutation. Push state is measured and stated in the completion message to `1.0.0_SA_CTO`.
