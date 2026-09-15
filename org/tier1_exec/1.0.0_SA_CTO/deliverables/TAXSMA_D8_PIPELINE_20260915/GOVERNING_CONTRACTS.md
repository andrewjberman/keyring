# MDPF_TAXSMA governing-contract handoff

Author: `1.0.0_SA_CTO~A`. Recorded 2026-09-15. This records existing law and counterpart coordination for L4; it is not the project PRD, a source-observation certification, or an implementation authorization. Andrew's eight approved endpoint bars remain unchanged.

## Contracts to carry into L4

| Surface | Governing source | Required treatment |
|---|---|---|
| Gateway identity | `docs/architecture/NFRA_OPLMCP_PRD.md` @`33c581d223e2e3bac5e44a37abb407b5f79f82de`, sections 1, 2 decision 1 and 6 | Microsoft 365 reads use each user's delegated identity. The gateway's existing law prohibits an app-only or shared-identity route. Research access does not establish a production unattended-identity contract. The PRD must specify credential ownership, refresh/re-authentication, revocation, and a visible failure result without inventing application permissions. |
| Gold history | `org/missions/D8/MDPF/MDPF_CANON/prd/MDPF_CANON_PRD.md` @`8d12b77adbcb871c6d267ce7ae501b260b2ae727`, CONTRACTS line 178 and DEC-2 lines 203-207 | One dated parquet partition per day; historical objects are not rewritten. TAXSMA's correction behavior must explicitly preserve this law. A correction cannot silently replace a previously published dated object or introduce a shadow publication path. The owning CTO was asked at 06:41:39Z for the authoritative correction model, including same-day corrections after an object exists. That architecture disposition remains to be incorporated. |
| Artifact membership | The same MDPF_CANON CONTRACTS lines 178-179 | Its enumerated gold and served artifact lists omit `category_views` / `category-views`. The TAXSMA PRD must name the contract amendment needed for its category-view delivery and route it to the MDPF_CANON owner. It must not treat the existing list as if it already includes that artifact. New addresses must use the ruled LGIC_ENFORCE builders. |
| Consumer ownership | `docs/architecture/D1_ASSET_CATEGORY_VIEWS_PRD.md` @`5d356cc426f6d3bdcaccfe192482ec2e04788270`; `docs/architecture/D1_CATVIEWS_SMA_LIVE_PRD.md` @`42fb68944bd244ba350bc4e2ee9a2065862c8633`; CTO message 96939 | D1_CATVIEWS owns the consumer. Coordinate the proposed narrow change to `CategoryViewTree.tsx` / `aum.ts` with `2.0.0_SA_COO~D`, whose active work uses `feature/d13-visual-elevation`. Ownership/interface inquiry sent 05:56:47Z and followed up 06:41:40Z; no consumer edit is made by this handoff. |

## CTO disposition 96939, to carry without narrowing Andrew's word

The exact message is `20260915T055523Z_1.0.0_SA_CTO_Re_MDPF_TAXSMA_seam__the_freeze_blocks_d.md`, from `1.0.0_SA_CTO` to this seat. Its five dispositions are recorded here so processing the inbox notice does not lose the L4 requirements:

1. Andrew's frontend completion definition is "built and committed behind the freeze." Authority: `org/tier0_exec/0.0.0_AB_MSTR/deliverables/ANDREW_DIRECT_20260914_052xZ_FRONTEND_DONE_IS_BUILT_BEHIND_THE_FREEZE_LIST_OWNER_FALLBACK.md` @`65a535f194`. The freeze governs promotion, DEV/PROD pushes and gitlink movement; a narrow consumer build and commit is allowed. Publication still waits for the applicable authorization.
2. MDPF_CANON v2.3 R3 / DEC-5 requires that its migration preserve existing callers. That is the migration's own constraint; it does not prohibit TAXSMA's deliberate consumer correction. State both obligations explicitly.
3. The D1_CATVIEWS presence rule hides genuinely unheld/zero members. Andrew's later L1 amendment is `org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260915_024xZ_DSGN_REBRND_WHOLE_DOLLARS_AND_ZERO_L1_BUCKETS_SHOWN.md` @`fe76e3e036`: a zero or null L1 bucket is shown as $0 once a sibling has a value. L2 was not amended.
4. Approved FWD-5 concerns an unknown or stale Tax value, which is distinct from a known zero. Give the Tax leaf an explicit missing/stale result with date and coverage; it is neither hidden nor represented as $0. Preserve the other presence rules and the L1 amendment. The PRD must propagate this distinction honestly through the relevant totals.
5. Reconcile the category-view artifact omission with an exact MDPF_CANON line citation, allowing that contract's owner to amend it.

## Completion boundary

This handoff preserves received contract direction only. The source-grounding certification packet remains unchanged during its open review. The final PRD must incorporate these directions after the required certification and close the remaining correction and ingestion design choices at L4. It must not defer those architecture choices to L5 allocation.
