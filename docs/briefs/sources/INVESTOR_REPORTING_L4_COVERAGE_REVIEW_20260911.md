# Investor Reporting L4-R: current-version brief review

Reviewer: **4.0.0_SA_CRO**, BRIEF half. Trigger: CTO message 95787, exact inbox delivery `20260911T042014Z_1.0.0_SA_CTO_L4-R_REVIEW_IS_DUE_NOW__on_Andrew_s_word.md`. Date: 2026-09-11 UTC.

| Project / reviewed version | Committed PRD pin | CRO verdict |
|---|---|---|
| IRPT_FNTEND v0.5 | `fb5bb6e8b7dfeee031bf7c2850804079eb46516d` | **SIGNED** |
| IRPT_BCKEND v0.10 | `3624e60defa7dab02fdb9f218a05b6bf87d598ee` | **REFUSED**, for R1 and R2 below |

The backend corrections concern source-to-consumer routing and the current evidence available to extraction/export work. They require document edits by CTO, not another vendor experiment. This review neither changes an endpoint nor certifies implementation. CVO owns the separate ratified-text verdict.

## Pins, method and measured coverage

Compared all committed changes from the previously signed v0.4 pin `62301f71e03a0725a7f4bebf0770a438dfc8b371`, using the completed review at `docs/briefs/sources/INVESTOR_REPORTING_L4_COVERAGE_REVIEW_20260910.md@b6bd03bdca567fa3b78ad761c88625e0cbe2fd14` as the unchanged baseline. Re-read the affected candidate, contract, source/path, fixture and coverage rows at the current pins, together with their source requirements and the counterpart's consumers. Verified that neither PRD had changed after its named pin during the review.

Source briefs remain `investor-reporting-ir-fe-brief-20260910.md` and `investor-reporting-ir-bk-brief-20260910.md` at `2acf23d8fd`. The added source is `investor-reporting-ycharts-session-recovery-brief-20260910.md` through VI.6 at `72acd16e66`, plus `docs/research/investor_reporting_ycharts_variants_20260911/UI_CONTRACT.md`, its manifest, implementation and results at that same pin. Machine-read source hashes and row counts are in [INVESTOR_REPORTING_L4_REVIEW_EVIDENCE_20260911.json](INVESTOR_REPORTING_L4_REVIEW_EVIDENCE_20260911.json).

| Inventory | Actual | Required |
|---|---:|---:|
| FE main brief headings, including title | 25 | 25 |
| FE coverage rows: main brief + S1-S10 | 35 | 35 |
| BK main brief headings, including title | 28 | 28 |
| BK original coverage rows: main brief + S1-S9 | 37 | 37 |
| BK supplement coverage rows | 32 | 32 |
| FE / BK candidate cells | 14 / 18 | 14 / 18 |

The supplement has 33 Markdown headings including its document title; its explicitly enumerated denominator excludes that title and correctly counts 32 sections. Skipped display numbers are not missing entries. Counts verify inventory, not semantic carriage.

## R1: BK sends the Generate UI source to the Holdings cell

**Pinned locations:** BK `IRPT_BCKEND_PRD.md@3624e60defa7dab02fdb9f218a05b6bf87d598ee`, lines **178** and **294**. The new PATHS row assigns `UI_CONTRACT.md` to `FNTEND F6`; the VI.6 coverage row repeats `counterpart F6 consumes UI_CONTRACT.md`.

The source contract at `72acd16e66`, line 3, explicitly names the Analysis tab. The counterpart at `fb5bb6e8b7dfeee031bf7c2850804079eb46516d` makes **F5 Analysis** the consumer at line 96; **F6 is Holdings** at line 97. This is a wrong consuming-cell reference, not a missing source heading.

**Required correction:** change both current Generate-source references to **FNTEND F5**. In the supplement boundary row at BK line 273, assign progress/lifecycle to **F7**, export options to **F8**, and rendering to **F9** where those roles are enumerated; remove F6 from YCharts ownership. Preserve Holdings F6's separate `HoldingsSnapshot` boundary. No frontend product change is requested.

## R2: BK's extraction/export consumers do not receive the newly available PDF specimens

**Pinned locations:** BK at the same pin, **B10 line 119**, **B14 line 123**, and the new variant-packet fixture row at **line 210**.

B10 still declares the actual three-variant PDFs `STILL MISSING`. B14 retains the unqualified three-PDF gap. The v0.10 fixture row establishes all three actual vendor-generated synthetic PDFs but routes the packet only to **B9, B2 and B16**, omitting the cells that extract their sections and render their matching exports. The late B9 result clause proves that the files exist; it does not give B10/B14 a current fixture disposition.

VI.6 at `72acd16e66` and the packet's `pdf_validation.json` establish the available specimens: Overview 23 pages, Comparison 31, Multi-Comp 35, with immutable artifact keys and SHA-256 receipts. Their synthetic input does **not** establish real-client parity, section-extraction fidelity, complete financial-statistic correctness, public-ETF/mixed cases or maximum-cardinality fidelity.

**Required correction:** name the current packet/PDF receipts as research inputs to **B10 and B14** in the candidate/fixture mapping. State the remaining proof precisely: paired section/native/export certification and representative real-client/input cases remain required; the three synthetic vendor PDFs are available starting fixtures. Preserve every remaining certification arm. Do not mark extraction or custom Opal rendering complete merely because the generator succeeded, and do not ask Andrew to supply PDFs the experiment already retained.

## What passes in the changed design

- **FE v0.5:** F5 and the AnalysisRequest row carry the ordered client/account/snapshot/comparison/title/profile inputs, displayed variant by count, stable request ID, immutable snapshot, and server-only `resolved` boundary. Autosuggest does not authorize Generate. The source distinguishes the three research specimens from the real-client gap. F7 preserves per-tab failure isolation; F8/F9 preserve Analysis-specific orientation and same-revision preview/export. S10 is counted and mapped. No new brief-half finding remains in the frontend change. F9's older short phrase about the PDF gap should be read with F5's explicit current specimen/gap distinction and can be made equally explicit in a later text cleanup; it is not a new missing-input requirement.
- **BK resolver and tenancy:** B2 owns authenticated resolution, the authorized typed comparison catalog and permission checks at acceptance and release. B17 rechecks the request ledger before mutation and delivery. A shared login conveys no cross-firm grant. B1/B12's firm-bucket projection and B15's explicit scoped CloudFront route preserve the brief's access boundary; this review does not independently certify those live surfaces.
- **BK session/recovery:** B8 carries the dedicated EC2/SSM lifecycle, Kimi K3 2500/400 split, public-pixel limit, no OTP branch, verified identity/capability, one account-scoped lease, fencing at publication, candidate VersionId ownership and competing-consumer migration. B9/B16 carry response-specific recovery, bounded retries and unknown-mutation reconciliation.
- **BK generation:** B9 builds on the tested worker/recipe modules, preserves exact wire asymmetries, annual fee/settings and typed dollar units, and names the untested variants/units. It distinguishes operator-driven checkpoint resumes from automatic self-healing. The successful synthetic chain is carried without promoting it to production readiness.
- **Prior review protections:** the former mailbox-reuse defect remains corrected; ExportBundle preview remains a named consumer; B12 retains grain, recursion, wrapper/leaf and alternative-partition guards; B13 retains dated-history selection exclusions; Analysis rendering remains explicitly mapped to FWD-4.

The signature reviews document carriage only. Production cutover/fencing, real token rotation, autonomous eviction recovery, real directory entitlements, email/attachment handling, and native/export certification remain implementation proof. No PRD, endpoint, task order or peer signature is edited by this reviewer.

## Delivery

The canonical CRO records bind the verdicts above to these exact current versions, with this committed review as `review_ref`. CTO owns the two backend corrections and its version bump; that new pin reopens review normally. No intermediate v0.5-v0.9 backend signatures are needed.

Push state: **LOCAL**. Observed `origin/CLOUD` via `git ls-remote`: `ae0fcf29346b4a8fe7c598fe69189880c8da6d29`. No push is performed.
