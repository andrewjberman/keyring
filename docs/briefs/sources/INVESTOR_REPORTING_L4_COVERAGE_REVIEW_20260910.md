# Investor Reporting L4 coverage review

Author: 4.0.0_SA_CRO. Review date: 2026-09-10. Requested by CTO message 95562.

**Initial result at `d555a33482`: heading coverage is complete; six concrete mapping or detail-carriage corrections remain.** This is a bounded source review, not a hold on decomposition, a replacement PRD, or implementation certification. CTO owns the corrections. The source requirements below already existed; this review introduces no product scope.

**Follow-up at `bde174b126` (v0.3): R2 and R5 are closed, and the coverage pointer is repaired. R1, R3, R4 and R6 have the smaller residual edits listed at the end of this review.** Their principal corrections landed; this is not a claim that all six findings are fully closed.

**Current result at `62301f71e0` (v0.4): all six named review findings, their four residual edits, and the coverage pointer are closed at the document level.** The earlier results above remain the dated review history.

## Compared artifacts and method

- Frontend PRD: `org/missions/D9/IRPT/IRPT_FNTEND/prd/IRPT_FNTEND_PRD.md` at `d555a33482`.
- Backend PRD: `org/missions/D9/IRPT/IRPT_BCKEND/prd/IRPT_BCKEND_PRD.md` at `d555a33482`.
- Source briefs: `docs/briefs/investor-reporting-ir-fe-brief-20260910.md` and `docs/briefs/investor-reporting-ir-bk-brief-20260910.md`, both at `2acf23d8fd`.
- Companion evidence: [split manifest](INVESTOR_REPORTING_FE_BK_SPLIT_EVIDENCE_20260910.json), including pinned hashes and coverage rows for this review.

Read all eight PRD sections, counted actual coverage rows, matched the ordered brief-section inventory and S1-S9 source rows, and compared the mapped candidate/contract/path text with the detailed source requirements. Targeted whole-document searches corroborated the missing controls named below; a literal-search absence alone was not treated as proof of a semantic omission. Line references in this review are to the pinned versions, not later worktree edits.

| Check | Frontend | Backend |
|---|---:|---:|
| Brief sections | 25 | 28 |
| Supporting documents | 9 | 9 |
| Actual coverage rows / required rows | 34 / 34 | 37 / 37 |
| Source IDs S1-S9 represented once | 9 / 9 | 9 / 9 |
| Explicit NOT CONSUMED rows, with reasons | 3 | 3 |
| Candidate cells | 14 | 18 |

The skipped display numbers 26 and 29 do not represent missing rows. Structural headings have structural dispositions. These counts establish inventory coverage only. They do not establish that a reference to a paragraph carries its operational detail into a worker's execution instructions; FE IV.5 and BK IV.8 expressly require that detail.

## Corrections for CTO

### R1 — B6 names the wrong reuse path for mailbox authentication

BK PRD line 113 labels `infra/aws/lambda/ycharts-session-capture/index.mjs` a Graph/certificate pattern reference. Reading that complete file establishes a Chromium/Puppeteer login and Secrets Manager cookie-capture implementation; it contains no Graph mailbox or application-certificate authentication implementation. Its YCharts-session reference is appropriate to B8, not evidence of B6 mail access.

Remove the incorrect B6 reuse claim and attach a verified mailbox application/certificate implementation when identified; otherwise mark that exact reuse source unresolved. Carry BK IV.4's effective mailbox-only read grant, folder delta/pagination, immutable message identity, durable completed checkpoint, initial cutoff and overnight catch-up into B6. Do not imply that a cookie-capture Lambda establishes mail permissions. This review does not nominate an uninspected replacement path.

### R2 — ExportBundle's consumer declarations disagree

FE PRD lines 99 and 119 explicitly consume `ExportBundle` for F8 preview. BK PRD line 140 names only B14 render as its consumer. The frozen preview/render contract must agree on both sides.

Name FE F8 preview as a consumer alongside B14 render and carry the matching producer/consumer fixtures. Expose the authorized preview contract; internal artifact locations, credentials and raw vendor routing remain server-side. This correction does not make the browser a storage or authorization owner.

### R3 — FWD-4 export is present in the endpoint but missing from the render-cell mapping

The Analysis endpoint requires a matching branded PDF. FE endpoint line 66 correctly preserves Analysis-specific certified layouts without the performance narrative. However, FE F9 at line 100 serves FWD-8/3/12 and describes the landscape-letter performance template; BK B14 at line 121 serves FWD-8/3. Neither render candidate names FWD-4. FE's S8 mapping reaches F5 without identifying the Analysis render-package consumer.

Map FWD-4 to the FE render package and BK export worker, and map the relevant YCharts source detail to those consumers. Carry certified Analysis section/layout and orientation handling plus native-preview/PDF parity at the same input/configuration/artifact revision. Preserve the actual three-variant PDF proof gap. The Analysis export requirement has not vanished globally; its execution-cell assignment is incomplete.

### R4 — B12's IV.5 reference does not carry critical join and classification guards

BK PRD line 119 maps IV.5 but reduces its controls to join counts, unique custody totals, basis separation and reconciliation. The following requirements from source brief lines 226-243 are not spelled out elsewhere in this PRD:

- COT duplicates use an explicit equal-value/null policy with units/date checks; incompatible duplicates remain exceptions.
- Recursive model expansion applies relative/absolute weights exactly once, detects cycles and missing nodes, and retains unresolved mass. Empty-list cycle handling is invalid. Never renormalize only surviving Opal children; preserve wrapper/leaf attribution.
- SmartX roster, valuation and position rows are different grains. Missing positions are not zero; do not sum equity/cash/fees/accruals across incompatible grains or union parallel custody facts.
- Opal Supervised/Unsupervised and Advised/Residual are alternative Client partitions, not four additive children. Vendor AccountSupervised is not Opal fee-taking status. An older insurance-view exclusion cannot remove holdings from this product.
- Eclipse numeric identifiers require a declared canonicalization and `targetPercent` units remain uncertified. Preserve source-date differences, managed/excluded meaning and actual-sleeve versus assigned-account bases.

Carry these into B12's executable requirements and adversarial fixtures before issuing its work. A total can reconcile while a wrong recursive or classification allocation remains economically incorrect; the existing top-level reconciliation sentence is insufficient to test these cases.

### R5 — B13 omits the historical-evidence selection controls

BK PRD line 120 carries deterministic events, timezone, missing history and non-causal prose. Source IV.6 lines 247-249 additionally requires event detection before downsampling; no MWR/annualized/cash-flow-value substitution or zero-filled missing days; exclusion of future information; syndicated-context deduplication; and proof that a prefilter archive represents the final historical Topic Cloud before using it as such. Secondary signals need historical date/universe evidence; current neutral/fallback values cannot become historical observations.

Carry these controls and their failure fixtures into B13. A deterministic replay can still produce the same incorrect historical story twice if its input-selection policy admits future articles or current fallback values. Existing date/cutoff and missing-history fields do not specify all these exclusions.

### R6 — B9 points at the retrieval recipe while omitting material body/settings semantics

BK PRD line 116 lists endpoints and the 34-key/33-key census, but source IV.4 lines 192 and 206-212 also requires effective-settings readback, typed security identities, the real upload record/units, and the actual template/body distinctions. Carry:

- The recorded quarterly/dividends-false/oldest/prior-close/non-qualified/`^SPXTR` configuration, with current fee `0.003`; verify actual effective settings. A default tax configuration is not client tax status, and No Benchmark presentation does not remove the calculation benchmark.
- Overview primary/portrait, Comparison primary plus one/portrait, and Multi primary plus two-five/landscape; the captured Multi evidence contains two comparisons only.
- Single `secondarySecurity` versus Multi array, asymmetric null/empty fields and consistent duplicate cover fields; no PUT of global preferences. Preserve the S8 detailed body authority.
- Slow synchronous vendor 201 with `report_url`/`zip_url`, wrapped in an Opal asynchronous job; do not invent a vendor background-job identifier.

The observed-browser upload, uncertain-create reconciliation, intent checkpoint and retained PDF hash are already carried and should remain. The missing multipart body and actual PDFs remain proof gaps, not fields to invent.

## Small pointer repair and retained requirements

Both coverage tables refer to every cell's `CROSSES column` (FE line 169; BK line 209), but neither candidate table has that column. Point to the actual endpoint OWNER/CROSSES lines and contract handoffs, or add the intended cell crossing field. This is a traceability pointer defect, separate from the six content corrections above.

The reviewed PRDs do preserve the fixed BDAPI/Kimi runner style with no OTP branch, immutable sender-derived firm binding, Global/scoped routing, optional advisor logos, no causal narrative, current-only Holdings, distinct target/observed bases, and the frontend-only design census. FE FWD-8 explicitly retains the separate Analysis layout and optional Holdings appendix; this review does not falsely report those requirements absent from the whole PRD.

## Routing and publication status

Andrew's direction at `2f13cdbaeb` (LD-0542), followed by CTO's Rule 27/spine correction at `08722e8b86`, assigns CTO every L3 carrier and the L2-through-L5-handoff work. MSTR is not a register gate. CRO retains L1; COO retains L5 decomposition. The two L1 briefs have been corrected accordingly and now link their actual PRDs. Their product requirements are unchanged from the reviewed pin.

No PRD, register, decomposition or task order was edited by CRO. No live vendor request, production deployment or implementation test is part of this review. Andrew's push hold was reported in message 95567; this work makes no publication request or origin claim.

## Follow-up on CTO message 95585: PRDs v0.3

Read the committed changes from `d555a33482` through `bde174b126`, including the intervening v0.2 at `f58e9443e4`. Re-read the affected complete candidate, contract and source/path-map rows. Both endpoint sections are byte-for-byte unchanged after newline normalization; coverage remains FE 34/34 and BK 37/37. Candidate counts remain 14 and 18. This review verifies document carriage only.

| Finding | Verified in v0.3 | Remaining edit |
|---|---|---|
| R1 | BK B6, line 113, now states NONE VERIFIED for mailbox reuse and carries the mailbox grant/checkpoint details. | BK PATHS line 166 still maps the grouped YCharts client, cookie-capture Lambda and pipeline paths to **B6, B8**. Remove B6 from that reuse row; none of those paths was verified as a mailbox implementation. Retain them as B8 session/consumer references. |
| R2 | BK CONTRACTS line 140 now names FE F8 preview alongside B14 render as an ExportBundle consumer. | **Closed at the document level.** Producer/consumer fixtures remain implementation work. |
| R3 | FE F8/F9 and BK B14 now explicitly serve FWD-4, with the Analysis layout, orientation, revision parity and actual-PDF gap retained. | FE source-coverage rows S3/S8 at lines 187/192 still name only F5. Add the applicable F8/F9 export consumers, especially S8's certified section/orientation/PDF detail. The candidate assignment is repaired; the requested source-to-render map is incomplete. |
| R4 | B12 line 119 carries duplicate policy, one-time relative/absolute weights, cycles/missing nodes, unresolved mass, no surviving-child renormalization, grain separation, alternative partitions and uncertified Eclipse units. | Add the remaining source-IV.5 guard: preserve the proper attribution of an **Opal wrapper or Opal leaf**, with its fixture. Wrapper/leaf attribution is not stated in the complete v0.3 PRD; it is distinct from retaining unresolved mass or avoiding renormalization. |
| R5 | B13 line 120 carries all the named historical selection exclusions and their failure fixtures. | **Closed at the document level.** Historical coverage and replay fidelity remain unproved. |
| R6 | B9 line 116 carries effective settings, typed identities, template cardinality/orientation, body asymmetries, no global-preference PUT, and synchronous vendor 201 versus Opal async job. | Carry creation with the captured portfolio/items JSON multipart form using the **real `upload_record_id` and correct units**, per pinned BK IV.4 step 3, line 208. Parsing units in B7 does not specify how B9 uses the returned upload record and serializes those units. Preserve the missing-upload-field gap. |

The nonexistent CROSSES-column references are removed from both maps; the replacement references name actual ENDPOINT ownership/crossing lines and CONTRACTS columns. The additional v0.2 changes also correctly distinguish ten FE-consumed contracts from the FE-produced RenderPackage and name the cohort/classification contract carriers. No new broad review, outcome change or decomposition hold is introduced by these four residual edits.

## Closure on CTO message 95594: PRDs v0.4

Compared the complete v0.3-to-v0.4 diff and rechecked the affected committed rows at `62301f71e0`:

| Residual | Verified correction |
|---|---|
| R1 mailbox reuse path | BK PATHS line 166 assigns the grouped YCharts client/cookie-capture/pipeline paths to B8 alone; B6 still correctly states that no mailbox implementation has been verified. |
| R3 Analysis source-to-render mapping | FE S3/S8 coverage rows at lines 187/192 now name F8/F9 beside F5. F8/F9 and B14 retain their explicit FWD-4 assignments and Analysis-specific rendering constraints. |
| R4 wrapper/leaf attribution | BK B12 line 119 now preserves an Opal wrapper or leaf's proper attribution and requires both wrapper-over-non-Opal-children and leaf-under-non-Opal-wrapper fixtures. |
| R6 upload creation semantics | BK B9 line 116 now specifies the captured portfolio/items JSON multipart form, real upload_record_id, correct units and 201 model_portfolio_id response. Unknown upload field names remain a proof gap. |

R2's FE preview consumer and R5's historical-evidence controls remain intact; both CONTRACTS sections and the complete B13 row are unchanged from the already-reviewed v0.3. Both ENDPOINT sections remain unchanged from v0.1. Coverage remains 34/34 and 37/37, with 14 frontend and 18 backend candidates. The nonexistent coverage pointer remains removed.

**No named review finding remains open at this PRD revision.** This closes the bounded document review, not implementation acceptance or universal source-losslessness certification. Actual mailbox permissions, upload fields, three-variant PDF evidence, model-unit certification and the required execution fixtures still need the proof already assigned in the PRDs. The review adds no hold or further review gate to CTO's v0.4 handoff. Push remains held; no publication is claimed.
