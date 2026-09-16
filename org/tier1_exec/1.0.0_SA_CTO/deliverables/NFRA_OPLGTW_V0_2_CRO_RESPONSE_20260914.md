# NFRA_OPLGTW v0.2 response to CRO brief refusal

Author: 1.0.0_SA_CTO~A. Date: 2026-09-14.
Input: exact unread message 96736 from 4.0.0_SA_CRO, citing review docs/briefs/sources/NFRA_OPLGTW_L4_BRIEF_REVIEW_v0_1_20260914.md@51c7fc7f51 and REFUSED stamp @f348c0a537.
Authority: Andrew's existing project/PRD commission and eight-bar approval. This is the author's correction of the review; it does not self-sign the brief.

PRD: org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md, v0.2.
Content SHA256: 96f42e0caf8dfed8af63c967f359912de423b632244f458234803962424b4598.
Ratified-text half: 908c9e9460c1cdbb3cf4fa111d5946461c1dfc074963022b3b5e43d6c00233f9 (UNCHANGED from the signed v0.1).
Brief half: 04461a4925dc40dcbe06c85962f6cd200dd819bacdf1a6c2251885281c798dc1 (changed; CRO re-review owed).

## Disposition of all three grounds

| Ground | Correction and consuming evidence |
| --- | --- |
| R1: network/front door | S9 at line 209, the coverage row at line 239, A16/A19 and the deployment-operator paragraph carry actual Claude IPv4 DNS/global routing/no-cross-host redirect; WAF/proxy headers and streaming; the SPEC-recorded 160.79.104.0/21 egress conditional on filters and reverified at rollout; work-browser reachability; Host/Origin validation; clientInfo as telemetry only; and the recorded 60-second ALB idle timeout constraining preparation and streaming. |
| R2: acceptance | A6 at line 258 proves filtering before query/aggregate/cache/export, including warmed-cache scope changes and revocation. A16 at line 268 carries the network checks. A19 at line 271 deliberately exercises ALB idle/slow preparation/streaming/cancellation with the 30-second internal deadlines. The matrix preamble and A20 at line 272 restore tool, UTC timestamp, public connector URL and sanitized server correlation/ofid_ fields. Public connector URL excludes credential/ticket material. |
| R3: disclosures/preservation | Downloads coverage and onboarding state that returned results enter organization Claude chats/retention and commercial training defaults do not mean zero transfer. Observations coverage and the S9 operator/A15 before-after checks preserve versioning enabled, AES256, all four public-access blocks enabled and non-public bucket policy through rollout/rollback. |

All eight approved outcome cards and all 32 DONE WHEN/ACCEPT/PROOF/SOURCE lines remain verbatim. The ten surface IDs and twenty acceptance IDs do not change. Contract JSON and ENDPOINT/CONTRACTS section bytes are unchanged. No new scope or outcome is inferred from the reviewer.

## Validation actually performed

- Canonical half_hashes equals the current CVO sign-off's ratified-text hash; the brief hash differs from v0.1.
- Canonical prd-manifest-gate passed all key surfaces on v0.2.
- The existing authoring validator passed header schema, three identity carriers, eight cards/32 approved text lines, ten brief headings, ten surfaces, twenty acceptance rows, eighteen evidence cells and fifteen component units.
- git diff reviewed against v0.1 and git diff --check passed.
- L4 author stamp refreshed by prd-stamp.py for v0.2 and the current content pin.
- Bare comp-adversary compose ran for this correction; declaration: NFRA_OPLGTW_V0_2_VALIDATION_CONTEXT_20260914.md beside this record. Its directory-adjacency limits and deferred sources remain declared; the external RFC URL's local-path GONE is not a missing repository dependency.

The 60-second ALB value and source-bucket baseline are carried from the supplied pinned SPEC, not remeasured. No cloud changes, network probes, entitlement changes, or new execution results are asserted. The authoring run remains OPEN pending the separate CVO ground-truth requirement, so the PRD remains DRAFT. This correction is local and is returned to CRO for the scoped brief re-review. No push.
