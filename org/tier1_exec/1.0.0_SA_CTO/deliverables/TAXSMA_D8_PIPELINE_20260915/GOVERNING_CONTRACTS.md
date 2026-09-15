# MDPF_TAXSMA governing-contract handoff

Author: `1.0.0_SA_CTO~A`. Recorded 2026-09-15. This records existing law and counterpart coordination for L4; it is not the project PRD, a source-observation certification, or an implementation authorization. Andrew's eight approved endpoint bars remain unchanged.

## Contracts to carry into L4

| Surface | Governing source | Required treatment |
|---|---|---|
| Gateway identity | `docs/architecture/NFRA_OPLMCP_PRD.md` @`33c581d223e2e3bac5e44a37abb407b5f79f82de`, sections 1, 2 decision 1 and 6; CTO disposition 96946 below | Microsoft 365 reads use delegated identity. Reuse the Gateway-held token contract and define one separate, bounded capability route for the workbook. No new delegated-token holder or application permission. The named person's authorization for unattended content reads is an explicit activation prerequisite, not supplied by this seat's research access or the approved endpoint bars. |
| Gold history | `org/missions/D8/MDPF/MDPF_CANON/prd/MDPF_CANON_PRD.md` @`8d12b77adbcb871c6d267ce7ae501b260b2ae727`, CONTRACTS line 178 and DEC-2 lines 203-207; CTO disposition 96944 below | One dated parquet partition per day; historical objects are not rewritten. Corrections are new observations in later knowledge-date partitions, with a separate valuation date and superseded-observation identity. A correction cannot replace a previously published dated object or introduce a shadow publication path. |
| Artifact membership | The same MDPF_CANON CONTRACTS lines 178-179 | Its enumerated gold and served artifact lists omit `category_views` / `category-views`. The TAXSMA PRD must name the contract amendment needed for its category-view delivery and route it to the MDPF_CANON owner. It must not treat the existing list as if it already includes that artifact. New addresses must use the ruled LGIC_ENFORCE builders. |
| Consumer ownership | `docs/architecture/D1_ASSET_CATEGORY_VIEWS_PRD.md` @`5d356cc426f6d3bdcaccfe192482ec2e04788270`; `docs/architecture/D1_CATVIEWS_SMA_LIVE_PRD.md` @`42fb68944bd244ba350bc4e2ee9a2065862c8633`; CTO message 96939 | D1_CATVIEWS owns the consumer. Coordinate the proposed narrow change to `CategoryViewTree.tsx` / `aum.ts` with `2.0.0_SA_COO~D`, whose active work uses `feature/d13-visual-elevation`. Ownership/interface inquiry sent 05:56:47Z and followed up 06:41:40Z; no consumer edit is made by this handoff. |

## CTO disposition 96939, to carry without narrowing Andrew's word

The exact message is `20260915T055523Z_1.0.0_SA_CTO_Re_MDPF_TAXSMA_seam__the_freeze_blocks_d.md`, from `1.0.0_SA_CTO` to this seat. Its five dispositions are recorded here so processing the inbox notice does not lose the L4 requirements:

1. Andrew's frontend completion definition is "built and committed behind the freeze." Authority: `org/tier0_exec/0.0.0_AB_MSTR/deliverables/ANDREW_DIRECT_20260914_052xZ_FRONTEND_DONE_IS_BUILT_BEHIND_THE_FREEZE_LIST_OWNER_FALLBACK.md` @`65a535f194`. The freeze governs promotion, DEV/PROD pushes and gitlink movement; a narrow consumer build and commit is allowed. Publication still waits for the applicable authorization.
2. MDPF_CANON v2.3 R3 / DEC-5 requires that its migration preserve existing callers. That is the migration's own constraint; it does not prohibit TAXSMA's deliberate consumer correction. State both obligations explicitly.
3. The D1_CATVIEWS presence rule hides genuinely unheld/zero members. Andrew's later L1 amendment is `org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260915_024xZ_DSGN_REBRND_WHOLE_DOLLARS_AND_ZERO_L1_BUCKETS_SHOWN.md` @`fe76e3e036`: a zero or null L1 bucket is shown as $0 once a sibling has a value. L2 was not amended.
4. Approved FWD-5 concerns an unknown or stale Tax value, which is distinct from a known zero. Give the Tax leaf an explicit missing/stale result with date and coverage; it is neither hidden nor represented as $0. Preserve the other presence rules and the L1 amendment. The PRD must propagate this distinction honestly through the relevant totals.
5. Reconcile the category-view artifact omission with an exact MDPF_CANON line citation, allowing that contract's owner to amend it.

## CTO disposition 96944: corrections preserve both dates

The exact message is `20260915T064603Z_1.0.0_SA_CTO_Re_MDPF_TAXSMA_corrections__no_amendment.md`, from `1.0.0_SA_CTO` to this seat, received and acknowledged. The CTO reports a bounded search of `infra/logic/02_DOCTRINE.md` and MDPF_CANON for an existing correction/amendment contract and issues the following new architecture disposition under R11, R18 and MDPF_CANON DEC-2:

The underlying doctrine was also read directly at `infra/logic/02_DOCTRINE.md` @`6dab0d76a7425ee2448b872790c3364acdf87b2e`: R11 lines 212-225 requires dated parquet history; R18 lines 295-301 prohibits shadow paths, dual writes and standing comparators. R12 lines 227-229 reserves parquet-to-JSON projection and serving shape for the publisher.

- A partition's key date is its **knowledge date**: what the estate knew on that date. It must not be confused with the date of the value being described.
- A correction is a new observation in a later daily partition. Each correction carries `valuation_date`, the corrected value, the corrected workbook identity and business status, and the identity of the observation it supersedes.
- For each valuation date, the consolidator and publisher use the observation with the latest knowledge date. Both the original and correction remain in immutable history, through the same canonical keys and publisher.
- Once a day's object exists, a same-day correction is admitted to the **next day's partition**. No second same-date object or replacement leaf is allowed. The stated nominal latency is at most one day; L4 must explicitly carry the schedule and visible pending-correction behavior needed to satisfy that promise, including non-trading days, and distinguish an operational delay from normal correction latency.
- This is the CTO's reading of the ruled history requirements, not a new sovereign ruling. MDPF_CANON's owner will add the same clause to its gold-artifact contract at its next bump; this seat must cite the disposition and its R11 / DEC-2 bases in TAXSMA's PRD.

## CTO disposition 96946: bounded unattended workbook capability

The exact message is `20260915T065013Z_1.0.0_SA_CTO_Re_TAXSMA_identity__reuse_the_gateway_s_.md`, from `1.0.0_SA_CTO` to this seat, received and acknowledged. It closes the architecture choice with **one new capability endpoint**, reusing the Gateway-held delegated-token contract. The CTO identifies `infra/aws/ec2/opal-gateway/app/ms_ingest.py` (NFRA_MSGRAPH S2, CTO arch-GO `20260626T162714Z`), its earlier `otp.py` precedent, and `token_broker.py` as the owning pattern. These are owner-supplied contract references here, not a new live-source validation claim or an assertion that the TAXSMA endpoint exists.

- The scheduled job holds a separate static capability bearer in Secrets Manager. It is accepted only on the new route and compared in constant time. The route must never accept that bearer as a general caller identity.
- The Gateway uses its server-held delegated token for one fixed, named Opal person. The job does not receive that token. There is no new delegated-token store, copied research credential, shared caller identity, or tenant-wide application permission.
- The server-side GET allowlist contains exactly the workbook driveItem. The response allowlist contains exactly the named sheet/range needed by TAXSMA. The predecessor returns structure; this endpoint returns **content**, which is the new access surface and must be explicit in L4 and its controlled tests.
- The person must already have delegated workbook access. **Which person, and permission to use that person's token for this unattended client-financial-content read, require Andrew's explicit word before activation.** Preserve this as a named sovereign prerequisite; no actual unattended read or deploy is authorized by this handoff. Prepare the concrete route, content boundary and traceability contract before presenting that decision.
- Every call is audited. Token revocation/expiry and `NeedsLogin` produce a fail-closed `auth-required` / stale result, never zero or silent success. L4 must state the source date and what remains unavailable.
- This requires a Gateway code change and its normal authorized deployment. The CTO requests naming the reusable pattern for IRPT_BCKEND's later mailbox intake; TAXSMA does not implement or grant that mailbox access.

## Completion boundary

This handoff preserves received contract direction only. The source-grounding certification packet remains unchanged during its open review. The final PRD must incorporate these directions after the required certification and close ingestion scheduling and the concrete correction/endpoint representation at L4. It must not defer architecture choices to L5 allocation. The architecture choices are disposed; the named delegated person's unattended-content authorization remains an explicit sovereign activation prerequisite. No production credential is established by the research session.
