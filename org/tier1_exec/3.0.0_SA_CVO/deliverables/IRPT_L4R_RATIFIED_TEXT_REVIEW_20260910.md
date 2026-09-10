# IRPT v0.4 L4-R ratified-text review

Reviewer: `3.0.0_SA_CVO`. Review completed: 2026-09-10 22:04 UTC.

**Verdict: SIGNED for both PRDs at the exact pin below.** This is the CVO ratified-text half of L4-R.

| PRD | Version | Reviewed PRD pin | Verdict |
|---|---|---|---|
| `org/missions/D9/IRPT/IRPT_FNTEND/prd/IRPT_FNTEND_PRD.md` | v0.4 | `62301f71e03a0725a7f4bebf0770a438dfc8b371` | SIGNED |
| `org/missions/D9/IRPT/IRPT_BCKEND/prd/IRPT_BCKEND_PRD.md` | v0.4 | `62301f71e03a0725a7f4bebf0770a438dfc8b371` | SIGNED |

## Authority and inputs

CTO message 95632, dated 2026-09-10 21:56:15 UTC, names these exact PRDs and pin and requests the spine-owned CVO act. The governing carrier is `org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md@648a820408`, L4-R lines 144-171 and owner row 510. The repository load skill's corrected Step 8 explicitly excludes spine-owned L4-R sign-off from COO-order gating; a COO order cannot precede this gate. No COO order was fabricated or requested to authorize this act.

The message relays Andrew's direction at approximately 21:2x UTC: "I dont want to ask shit this should be entirely automatic and gated, CRO and CVO should have to sign off on PRD before COO gets it." This is a CTO-relayed quotation, not a direct user message received by this seat.

Read the two complete pinned PRDs, their counterpart contract sections, the pinned brief ownership/contract/scope and dependency sections, and the operative endpoint qualifications. Brief inputs are `docs/briefs/investor-reporting-ir-fe-brief-20260910.md` and `docs/briefs/investor-reporting-ir-bk-brief-20260910.md`, both at `2acf23d8fd2a51fdef0b38ff7ef193f0c233661d`. Endpoint inputs are:

- `org/tier1_exec/1.0.0_SA_CTO/deliverables/ENDPOINT_FWD_INVESTOR_REPORTING_LIGHTWEIGHT_20260910.md@58266dab2d` for original outcomes.
- `org/tier1_exec/1.0.0_SA_CTO/deliverables/ENDPOINT_FWD_IRPT_BCKEND_20260910.md@2dcd88091f` for FWD-9/10/11.
- `org/tier1_exec/1.0.0_SA_CTO/deliverables/ENDPOINT_FWD_IRPT_FNTEND_20260910.md@5c18c88826` for FWD-12.

The earlier bounded review, `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_PRD_COVERAGE_REVIEW_20260910.md`, was recorded at `d0e72ccd56` and closed its C1-C3 findings at `b0def16c13`. This review independently checks the current v0.4 text; the earlier closure alone is not the sign-off.

## Ratified fields and endpoint cleanliness

An inline Python comparison read Git blobs at the pins above, matched each PRD's endpoint header denominator, and compared each DONE WHEN, ACCEPT and PROOF with its cited source. It made no network or vendor calls.

| PRD | Endpoint blocks | Fields | Equal after whitespace normalization | Only additional difference | Substantive differences |
|---|---:|---:|---:|---|---:|
| FNTEND | 8 | 24 | 23 | FWD-3 ACCEPT joins source line wrap `vendor-` / `calculated` | 0 |
| BCKEND | 10 | 30 | 29 | Same FWD-3 ACCEPT line-wrap join | 0 |

The text is verbatim modulo presentation whitespace and that single source soft wrap appearing in both PRDs. No other spelling, punctuation or wording normalization was used. The endpoint sections contain only the FWD headings and DONE WHEN, ACCEPT, PROOF, OWNER, CONSTRAINT and PIN fields: zero unrecognized nonempty lines and zero full seat names. No amendment history or annotation blocks were copied into them. Controls confirmed that a changed ZERO/ONE proof differs and an unresolved source pin fails retrieval.

## Operative constraint review

| Ratified constraint | Current carrier and finding |
|---|---|
| FWD-1/7: terminated clients remain visible when entitled; eligibility freshness is separate from revocation | Both endpoint constraints, FE F2/F7 and BK B1/B3/B4 preserve the separation and actual availability dates. |
| FWD-2: cross-firm server/storage isolation is independently graded | BK FWD-2 retains both storage shapes and the separation from ingestion FWD-10 and the explicitly entitled Global principal. |
| FWD-3: provider meaning, units and exact selected-scope calculation | Both ACCEPT/PROOF fields remain intact. BK retains Orion summary-decimal versus daily-percentage conversion and factor-product-minus-one normalization; FE consumes that certified contract and cannot recalculate or relabel methods. |
| FWD-4: email intake, unsupported positions preserved, programmatic clear-input path, no universal analyst gate or live-call permission | Both endpoint constraints and their analysis cells preserve these rules. The historical qualification already discharged in the source is not reinstated as a new gate. |
| FWD-4/8: missing actual three-variant PDFs and multipart evidence | The gap remains explicit in BK B9/B10 and FE rendering evidence, including export parity; captured routes are not presented as native-section certification. |
| FWD-5: actual custody basis, target/observed distinction, residuals and denominators | Both constraints and HoldingsSnapshot retain these distinctions; FE F6 and BK B12 preserve unknown and signed/zero states without silently reallocating residuals. |
| FWD-6: asynchronous selection safety and honest partial/stale states | FE constraint and StatusEnvelope preserve immediate scope clearing, late-response checks, warm-cache revocation and incomplete-not-zero behavior. |
| FWD-8: context rather than causation, missing history, bounded narrative, pending logos | Both endpoint constraints retain all four; preview/PDF use frozen revisions, missing logos do not block, and Analysis keeps its own certified layout. |
| FWD-9: immutable sender-derived firm and cadence still proposed | BK constraint and AnalysisRequest preserve firm bounds, correction revisions and the distinction between driven proof and an unratified poll proposal. |
| FWD-10: maintained destination policy, named owner, new-firm gate edit | BK constraint and B5 retain the policy artifact and independent failure/recovery proof without confusing who may see with where a request may land. |
| FWD-11: existing scoped route and Global selector pattern | Both constraints and Global cells preserve explicit entitlement, firm attribution, reset/refusal behavior and no email-firm rebinding or blended result. |
| FWD-12: existing component and brand conformity | FE-only endpoint remains ratified and clean; existing path references and component, accessibility and brand obligations remain in the PRD. |

## Contract agreement and prior fixes

Both PRDs agree with the pinned BK brief II.3 inventory: ten BK-produced contracts are consumed by FE, and FE produces RenderPackage for BK B14. FE CONTRACTS lines 107-123 and BK CONTRACTS lines 127-145 agree on identity, scope, units, dates, revision, availability and producer/consumer ownership. Canonical server-only routing/credential fields stay out of browser contracts. Rendering uses an immutable ExportBundle and matching RenderPackage; preview and retries do not fetch the vendor again.

All three prior corrections remain present: C1 carries independent supervision/billing semantics and hierarchy in DirectoryEntry and HoldingsSnapshot, with authoritative classifications and explicit unknowns; C2 names FE F8 preview as an ExportBundle consumer; C3 distinguishes ten consumed contracts from the one FE-produced RenderPackage. The handoff does not conflate Holdings' alternative Client partitions with the independent supervision/billing axes.

## Scope and publication

This signs the ratified-text and counterpart-contract fidelity of the named PRDs. It does not certify implementation, fixtures not yet acquired, production access, deployment, or the CRO brief-completeness half. Missing vendor artifacts remain implementation proof obligations. No live vendor call or push is authorized by this review.

Immediately before writing the review, both PRDs' latest path-changing commit was the exact reviewed pin; HEAD and working-tree text matched the pinned blobs after line-ending normalization. The two CVO sign-off files were absent. Each new sign-off will reference this review at its committed pin, so later PRD versions must reopen their own L4-R decision.
