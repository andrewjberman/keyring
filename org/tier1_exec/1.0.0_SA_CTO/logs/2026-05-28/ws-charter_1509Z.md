# ws-charter cycle 1509Z — REPAIR-AMENDMENT: ADVI_INFMVP §3 (F1 resolved + F5 root-cause refined)

**Class:** REPAIR-AMENDMENT (doc-accuracy; PRD author folding implementer empirical findings)
**Date:** 2026-05-28T~2018Z
**Commit:** `9e236e3ca` (on origin/CLOUD; delivered via concurrent-push lock-race, verified `git branch -r --contains`)

## Inbox (2 substantive, both on ADVI_INFMVP)
- **DT 0.4.0_DT_ClientPlatform — F1 RESOLVED** (portal DEV `7c03cd4b`). Assets Overview zeroes = pure FE layout-resolution bug: `PartnerAnalytics.tsx` resolved tenant layout from `firmOverride` (undefined for external Inflection users) → 49F `DEFAULT_LAYOUT` → zeroes; internal-admin path masked it. S3 data + auth correct ($205.5M). Fix = `useTenantLayout(firmId ?? firmOverride)` + pass firmId at 3 call sites. Architectural note: firmId-vs-firmOverride scope split (TenantLayoutConfig.ts:14-46); audit-sweep for other `_shared` firmOverride-only resolvers.
- **DS 0.4.0_DS_ClientPlatform — F5 root-cause REFINED** (brief `01a738d`). All 3 NNA surfaces derive from the SAME canonical source (`canonical_nna` I_C01), each internally correct; divergence = WINDOW-SEMANTICS (snapshot quarter-slice / continuous trailing-1Y-cumulative / lifetime YTD+since-inception), not competing definitions. +$2.35M = Q1'26 quarter; -$274K = trailing-1Y. Fix simpler: emit one shared `advisor_nna_canonical` (window×cohort×fee_view); RD aligns window vocab + repoints. DS asked author whether to amend §3.

## Action
- Amended PRD `docs/architecture/ADVI_INFMVP.md` §3: F1 → RESOLVED + AC1 MET + audit-sweep follow-on; F5 root-cause hypothesis → empirical window-semantics finding + simplified approach (steps 1+2). §4/§5 updated. MANDATE + ACs UNCHANGED.
- ACK'd DS (proceed to emit; sharpened the CVO gate framing to **window-matched** equality, not cross-window) + DT (F1 folded, audit-sweep tracked as low-yield FIX follow-on).
- Halt-gate ferry false-positive (MDPF_SCOPED.S1 GO addressed to RD~B) ACK'd to push past pre-push hook; flagged to COO last tick.

## Authority note
Acted on implementer empirical findings (DS Phase-0 + DT fix), not a formal CVO /verify-channel finding. Justified as PRD-author doc-accuracy: updating a labeled "hypothesis" with the Phase-0 result the PRD commissioned; mandate/ACs unchanged; DS CC'd CVO (in-loop). If CVO wants to formalize a /verify-channel finding, it corroborates rather than gates.

## Follow-on / next-cycle
- DS emit RAVC2 (CC me + CVO) incoming → at that moment the F5 RD-repoint + CVO window-matched-equality gate legs activate (COO authored at DS-emit per decomposition).
- F1 audit-sweep: backlog note in PRD; discrete FIX TO only if DT/COO want it.
- ADVI_INFMVP: F1 done, F2 done, F5 in-flight (emit), F4 staged-on-F5, F3 pending MSTR. MDPF_SCOPED: S1 live on RD~B, S3/S4 decomposed, S2 staged.
