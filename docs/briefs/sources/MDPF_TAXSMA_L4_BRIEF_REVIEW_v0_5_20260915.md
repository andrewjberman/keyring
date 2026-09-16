# MDPF_TAXSMA v0.5 — L4-R brief review

Author: `4.0.0_SA_CRO` · UTC: 2026-09-15, after 19:27Z · request: `1.0.0_SA_CTO~A` message 97209 (completion receipt
"97206 acted").

**VERDICT: SIGNED, brief half.** v0.5 repairs the two points in `3.0.0_SA_CVO`'s v0.4 refusal and closes this seat's
v0.4 date note. In this half:
- §3.9 binds the named account by its validated Entra tid/oid, with email as designation only, and puts the route's
  own guard ahead of generic `/ms/*` handling.
- A07 tests both of those.
- §3.3 and A03 state how a UTC effective date compares with an exchange-session valuation date.

Nothing else in the half moved, and Andrew's two records are still read no wider and no narrower.

## Exact inputs and scope

- PRD: `org/missions/D8/MDPF/MDPF_TAXSMA/prd/MDPF_TAXSMA_PRD.md@5061a43a46230b6d188886f8b19846f5445b0b0c`, v0.5,
  383 lines, in CLOUD.
- Brief: `…/ANDREW_DIRECT_TAXSMA_D8_PIPELINE_BRIEF_20260915.md@8e8afed454` (18 headings).
- Reviewed brief-half SHA-256: `a14495740d029c4f2fd09c5309fa183b2f85d75e187c71d162b3f91a31815043`, computed by
  `prd_signoff_lib.half_hashes` at the pin. It matches the notifier's `a14495740d02`.
- Ratified-text half: `ab7f2488ad922e26fa91feae1b19ae7c5615c6520b338f77150569e5ff84b77b`, changed, `3.0.0_SA_CVO`'s.
  The "v0.5 Gateway counterpart repair and date comparison" subsection (v0.5:134–138) sits under `## CONTRACTS`, so it
  is in that half and is not graded here.
- Counterpart: `org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md@f0aa50dbc0`, v0.2, the version this seat reviewed
  on 2026-09-14.
- Prior review: `docs/briefs/sources/MDPF_TAXSMA_L4_BRIEF_REVIEW_v0_4_20260915.md@27286d3a81` (SIGNED v0.4, stamp
  `5e2089e99b`).

## What changed in this half, v0.4 (`d317a65ec7`) to v0.5

| Where | Change | Check |
|---|---|---|
| §3.3 (v0.5:195) | A new paragraph, "UTC versus session comparison": effective_date is the UTC calendar date of source_observed_at, compared directly with the exchange-session valuation_date as ISO dates (start <= valuation_date < end). There is no local-time reinterpretation and no roll to a session. The exchange calendar chooses valid sessions only. | This closes the v0.4 note by stating the comparison, with the UTC choice kept. The worked case is right: `2026-09-16T00:30:00Z` is 20:30 EDT on September 15, and the boundary is September 16. A YES with no earlier state leaves September 15 unverified, never zero (brief O5). An explicit NO keeps proven September 15 membership and excludes September 16 onward. The live count moves at once, separate from the dated value. Nothing counts an account before its first observation. |
| §3.9 (v0.5:257, :259) | The designated email identifies Andrew's chosen account. Authorization binds its validated Entra tid/oid under NFRA_OPLGTW v0.2 C1/C2/A3, and a mismatch fails even with the same email. The route-specific guard runs before generic `/ms/*` handling, and every identity, resource and revocation check completes before the delegated-token fetch or Graph. TX-r-3 verifies the configured tid/oid. | **Counterpart read at `f0aa50dbc0`:** :131 "Carry validated `tid` and `oid` in signed principal context; email is display/audit metadata only"; :145 "Key grants by tid/oid, not email"; :255 A3 "tid/oid mismatch denied even with same email". The binding is the counterpart's own rule. It is the same account Andrew named at `f95470f384`, so his word is neither widened nor narrowed. Brief O7 is served: controlled, auditable access with no generic caller identity. |
| A03 (v0.5:271) | Adds the 2026-09-16T00:30Z boundary arm: a NO with retained prior state keeps September 15 and excludes September 16; a YES with no prior history leaves September 15 unverified; the live count changes at once; no local-time shift and no invented weekend session. | This is a deliberate, observable arm of the §3.3 rule, not a wait (Rule 27). |
| A07 (v0.5:275) | Proves the capability guard runs before generic `/ms/*` dispatch. With the same email and otherwise valid inputs, a wrong tid, a wrong oid, missing claims or a revoked principal fail before the token fetch; only the configured pair succeeds; generic MCP, ms-ingest and OTP credentials cannot open the capability. | Each arm discriminates: the same email with a different principal must fail. This matches the counterpart's A3. |
| §9 (v0.5:381) | The package now lists REVIEW_REPAIR_V05.md and contract 0.5.0. | Process text only. |
| Every other part of the half | Byte-identical to v0.4: §3.3's Traded rules, dates and events, S16, coverage and the manifest. | The v0.4 checks against Andrew `1729cef85e` and `f95470f384` and brief O1, O3, II, III and VII stand. 18 of 18 headings. |

## Limits

This is requirements acceptance only. No capability, guard or principal binding was exercised. The relayed whoami
MATCH still proves neither the immutable binding nor workbook access; TX-r-3 measures both. The CONTRACTS rows,
subsection and data contract 0.5.0 are `3.0.0_SA_CVO`'s.

Message 97209 was opened and READ-acked. This seat performs no push, deploy or cloud mutation. Push state is measured
and stated in the completion message to `1.0.0_SA_CTO~A`.
