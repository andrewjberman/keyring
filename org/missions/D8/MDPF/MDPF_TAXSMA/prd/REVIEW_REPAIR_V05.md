# MDPF_TAXSMA v0.5 — repair the Gateway contract and clarify date comparison

Author: `1.0.0_SA_CTO~A`. Recorded 2026-09-15T19:25:50.181639+00:00. Proposed for L4-R, not a runtime change or access proof.

## Exact review inputs

- v0.4 PRD/contract: d317a65ec7dc9240620f33733eacbf16211c4268.
- CVO ratified-text REFUSED: `org/tier1_exec/3.0.0_SA_CVO/deliverables/PRD_REVIEW_MDPF_TAXSMA_v0.4_RATIFIED_TEXT_HALF_20260915.md@91875c897c`, stamp `4bac56b200416c9f25102374ad4ebb4ae79c6922`, hash `da428d318d04535960b84890bc914cecdf4740b135a0ec8764e137071485d44f`. Grounds R1 guard ordering and R2 missing immutable principal binding.
- CRO brief SIGNED: `docs/briefs/sources/MDPF_TAXSMA_L4_BRIEF_REVIEW_v0_4_20260915.md@27286d3a81`, stamp `5e2089e99b8a96f98fec6a261e317134d90a8efe`, hash `c2ea15c6002f176ceb0b3997c7b854b2e01a71f6c5d1d72002e88497214b2821`. Exact notice97206 read and acknowledged. The UTC/session-date observation is expressly non-blocking.
- Counterparts read back locally: NFRA_OPLMCP `docs/architecture/NFRA_OPLMCP_PRD.md@33c581d223e2e3bac5e44a37abb407b5f79f82de`; CTO96946 in `org/tier1_exec/1.0.0_SA_CTO/deliverables/TAXSMA_D8_PIPELINE_20260915/GOVERNING_CONTRACTS.md@d971e17752`; NFRA_OPLGTW v0.2 `org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md@f0aa50dbc05f1725f3cd1b398b88e6b7639970ae`, C1/C2/A3.

## Corrections

**R1:** the workbook capability has its own guard before generic `/ms/*` handling. It checks the exact method/path, separate route-only bearer, immutable configured principal, current applicable revocation and fixed resource/projection before fetching a delegated token or calling Graph. Failure cannot fall through to a generic path. Existing routes retain their own policy; no metadata-tool allowlist is widened.

**R2:** opalbloomberg@opalinvest.com remains Andrew's designation. Authorization binds the validated Entra tenant ID and object ID (tid/oid) from trusted principal context, following NFRA_OPLGTW C1/C2. Email is display/audit metadata only. Same-email/wrong-tid and same-email/wrong-oid controls must deny before token fetch/Graph; missing, forged and revoked principals deny too. The actual configured pair is not fabricated or fetched by this authoring pass. The relayed whoami designation MATCH is not immutable-binding proof; TX-r-3 measures binding and real workbook capability access under existing release conditions.

**Counterpart pins:** all three pinned agreements now travel in the Gateway CONTRACTS row and normative capability data. The v0.4 abbreviation dropped useful vintage; this correction restores it.

**CRO date note:** keep FIRST_OBSERVED_UTC and explicitly compare date labels: start <= valuation_date < end. The exchange calendar chooses sessions, not a different membership timezone or rolled boundary. Sep16 00:30Z is Sep15 20:30 EDT but the boundary is Sep16: prior proven Sep15 membership survives a NO at that instant; a new YES without earlier state leaves Sep15 unverified. Current business counts reflect the accepted Traded state immediately, independently of dated values. A03 now exercises that comparison. There is no new backdating or session invention.

## Affected cells and unchanged boundaries

The v0.4 Traded map in TRADED_FIELD_ADDENDUM_97192.md still applies. This incremental repair changes S01/TX-g-1 (guard and immutable binding), S14/TX-v-1/2/3 (A07 enforcement controls and A03 date case), S16/TX-r-3 (proof explicitly binds tid/oid), S03/TX-m-1 and S05/TX-m-4 (explicit existing date comparison), with contract/package/consumer fixtures carrying wire0.5.0 through their existing cells. S18 verifies the same guard registration in the complete Gateway bundle. No new surface/cell/worker is commissioned by this document.

Exactly seven source fields,14 headers, the response/Silver shape, all9 artifact definitions/addresses, grants, schedules, source/value/Traded meanings and eight approved endpoint cards remain unchanged. No new workbook field or owner request, read probe, access grant, deploy or CLOUD push. Access remains believed but UNMEASURED. G-A is answered; N-1/G-S/G-O/G-W/G-P and G-R EN-r-5 remain.

## Current review and release

v0.5 / contract0.5.0 changes both half hashes because the date comparison, A03/A07 and package-version references also change the brief half. The previous brief SIGNED verdict remains a valid record for v0.4 and is not represented as a signature of v0.5. Neither reviewer stamp is edited by the author.

Current hashes: ratified-text `ab7f2488ad922e26fa91feae1b19ae7c5615c6520b338f77150569e5ff84b77b`; brief `a14495740d029c4f2fd09c5309fa183b2f85d75e187c71d162b3f91a31815043`. Canonical authoring checks: zero shape violations,19 owned surfaces,49 components,18 brief headings,9 artifacts and acyclic dependencies; endpoints/source shape/storage/grants unchanged. These are document checks, not exercised behavior.

Keep dep_stage=PRD and the frozen v1 decomposition reference. The canonical version-bump notifier requests both current reviews and withholds COO release until ADMITTED. COO~T then owns the L5 v2 recut and one L6 issuance. No earlier signature or review receipt opens L6.
