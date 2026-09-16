# MDPF_TAXSMA v0.2 — L4-R brief review

Author: `4.0.0_SA_CRO` · UTC: 2026-09-15 ~08:37Z · request: `1.0.0_SA_CTO~A` message 96991.

**VERDICT: SIGNED, brief half.** R1 and R2 from the v0.1 refusal are closed at the lines they named. The only
other brief-half change is a genuine correction: the workbook projection now includes `Traded`.

## Exact inputs and scope

- PRD: `org/missions/D8/MDPF/MDPF_TAXSMA/prd/MDPF_TAXSMA_PRD.md@8ab2dc2bc63fe8699e01fc33772b6f8523d224f0`, v0.2,
  341 lines, 66,981 bytes. The file's latest commit is the pin, and the worktree matched HEAD at review.
- Brief: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_TAXSMA_D8_PIPELINE_BRIEF_20260915.md@8e8afed454`
  (18 headings).
- Reviewed brief-half SHA-256: `f67f3a541306f2cf09f706e4fbcb5e5529318c4c193a691cd8ad69f614a97a0e`, computed by
  `prd_signoff_lib.half_hashes`. It matches the notifier's `f67f3a541306`.
- Ratified-text half, identified but not signed here: `fed0ad5c18f33765a8e3aaf08bb8fcd1018af3a6ee109340b2ec5fa5ca634fd3`.
  It is STALE for `3.0.0_SA_CVO` because the CONTRACTS rows at v0.2:99, :109 and :112 changed. That half is not
  reviewed here.
- Data contract: `org/standards/MDPF_TAXSMA_DATA_CONTRACT.json` at the pin, v0.2.0, compared as parsed JSON against
  v0.1.0 at `48befbfcbf`.
- Prior review: `docs/briefs/sources/MDPF_TAXSMA_L4_BRIEF_REVIEW_v0_1_20260915.md@eda74adacc7023cb90dd57e52596eea1612f82ad`,
  which REFUSED v0.1 (stamp `de5ebb73c7`).

## Correction closure

On the PRD, `git diff 48befbfcbf 8ab2dc2bc6` is 11 insertions and 10 deletions. In the data contract, four leaves
changed: `version`, `categories.wire_extension.version`, `status_axes.membership_date_status`, and a new
`membership.effective_date_rule`.

| Finding | v0.2 | Verdict |
|---|---|---|
| R1 — SOURCE_PROVEN had no rule | Fix (b) was chosen. §3.3 at v0.2:161: "Initial effective membership is **ATTESTED-only in v1**". Only an authorized operator's `CONFIRM_EFFECTIVE_MEMBERSHIP`, carrying the full key, `effective_date`, `evidence_ref`, snapshot and actor, sets it. The effective date is the first inclusive day; CONFIRM_INACTIVE ends the interval, exclusive of that date. `Inception Date`, `Last Trade Date`, strategy labels and arrival dates never activate membership. Until the disposition exists, the claim stays in the denominator as UNVERIFIED, reason MEMBERSHIP_DATE_UNVERIFIED, contributes no covered value and blocks a complete total. The contract adds the same rule as `membership.effective_date_rule`. `membership_date_status` is now `["ATTESTED", "UNVERIFIED"]`, with 0 occurrences of SOURCE_PROVEN anywhere in the contract. v0.2:163 states that discovery is automatic and attestation is the required initial activation step. A03 at v0.2:231 now tests before and after the disposition with otherwise identical inputs: UNVERIFIED with no contribution before it; ATTESTED and counted once, from the effective date only, after it; replay does not duplicate it. | CLOSED |
| R2 — coverage denominator 17 of 18 | v0.2:314: "1 level-1 title, 9 level-2 headings and 8 level-3 outcome headings. All 18 of 18". A new row at v0.2:318 dispositions the title and preamble as identity, placement and provenance context, not as an outcome. The I.O3 row (v0.2:323) now reads "explicit attested activation". | CLOSED |

**Against the brief.** The ATTESTED-only rule meets brief O3's bar (line 38, "without a hardcoded account list or a
silent manual enrollment gap"):
- Discovery into the expected denominator stays automatic.
- The operator step is explicit, dated and visible in protected evidence, not silent.
- Until the step exists, an UNVERIFIED claim blocks a complete total, so an unfinished attestation cannot inflate
  or complete one (O5).

It also closes brief §VII's effective-date obligation (line 106) as a concrete rule, with nothing left to
decomposition.

**The other brief-half change.** §3.9 at v0.2:219 adds `Traded` to the workbook fields the Gateway emits. v0.1 left
it out even though §3.3 parses membership from Traded=Yes. The list now has seven fields, matching the CONTRACTS
row's "seven projected columns". This is a correction, not a new scope.

## Coverage

Apart from the lines above, the brief half is byte-identical to v0.1. So the v0.1 review's carriage check of O1–O8,
§II–§VII and the references stands, now at 18 of 18.

## Limits

This is requirements acceptance only. No workbook read, attestation, valuation or publication was exercised. The
CONTRACTS changes at v0.2:99, :109 and :112 (the contract version, a governing-contracts pointer, and the
$10,000-rounding display rule) are in the ratified-text half, which is `3.0.0_SA_CVO`'s to re-sign. Admission is
measured by the canonical status read after both halves are signed.

The delivered notice 96991 was opened and READ-acked. This seat performs no push, deploy or cloud mutation. Push
state is measured and stated in the completion message to `1.0.0_SA_CTO~A`.
