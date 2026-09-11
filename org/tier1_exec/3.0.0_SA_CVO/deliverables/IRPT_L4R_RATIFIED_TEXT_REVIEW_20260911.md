# IRPT L4-R ratified-text review: backend v0.11 and frontend v0.5

Reviewer: `3.0.0_SA_CVO`. Date: 2026-09-11 UTC. Archetype: VALIDATE.

**REFUSED for both exact versions below.** BK needs amendment provenance moved outside ENDPOINT; FE needs its consumed contract to preserve BK's explicit server-only `resolved` boundary. These are separate, bounded findings. The 54 original DONE WHEN, ACCEPT and PROOF fields pass comparison.

| PRD | Version | Reviewed PRD commit | Verdict | Finding |
|---|---|---|---|---|
| `org/missions/D9/IRPT/IRPT_BCKEND/prd/IRPT_BCKEND_PRD.md` | v0.11 | `737cd1670546b106bb12b489e1fe5d1c0f1bfa90` | REFUSED | C1 |
| `org/missions/D9/IRPT/IRPT_FNTEND/prd/IRPT_FNTEND_PRD.md` | v0.5 | `fb5bb6e8b7dfeee031bf7c2850804079eb46516d` | REFUSED | C2 |

## Authority and review boundary

CTO message 95788 requested the CVO L4-R decision on BK v0.10 and FE v0.5 and relayed Andrew's direction to nudge the reviewers. Message 95801, `20260911T043156Z_1.0.0_SA_CTO_L4-R__IRPT_BCKEND_is_at_v0.11__737cd1670.md`, supersedes the backend request with v0.11 at the exact commit above; frontend remains v0.5. This is the spine-assigned ratified-text review, which precedes COO receipt and does not require a COO task order.

The governing rule is `org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md@f8337502a983e33549a78b9c606d933802282b75`, lines 144-178, specifically 156-158: preserve the ratified fields and operative constraints, exclude annotation/history/seat names from ENDPOINT, and agree with the counterpart's CONTRACTS. This record supplies the CVO half only. The prior v0.4 signatures do not sign these amended versions.

## C1: backend ENDPOINT contains amendment history

**Pinned location:** `IRPT_BCKEND_PRD.md@737cd1670546b106bb12b489e1fe5d1c0f1bfa90`, lines 51-52, inside FWD-4's ENDPOINT block.

Line 52 prefixes CONSTRAINT++ with the v0.9 history, an Andrew-direct timestamp and a quotation describing why the amendment was requested. That is amendment provenance inside ENDPOINT, forbidden by the L4-R rule. The source carrier already separates the quotation at line 568 from the operative CONSTRAINT++ at line 571: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ENDPOINT_FWD_IRPT_BCKEND_20260910.md@86bde3ea26ff9ca75b15e3c1810836f48cd038d5`. After the added provenance prefix, the PRD's operative mechanism text equals that source clause.

Line 51 also contains the v0.5 provenance prefix and an attribution parenthesis. These were copied from source line 558; the finding does not allege the PRD invented them. Their placement still needs to satisfy the endpoint-cleanliness rule.

**Required correction:** move the version/timestamp/quotation/attribution history from lines 51-52 to a provenance paragraph outside ENDPOINT. Preserve the source references in PIN and preserve every operative constraint: report-capable identity verification, same request/revision recovery, accepted shared-login displacement with bounded retries, one automation owner, protection of the legacy credential contract, and the fixed EC2 K3 capture -> fenced versioned session -> browserless Lambda replay -> report/PDF chain. Retain all five named unproven boundary arms. No change to DONE WHEN, ACCEPT or PROOF is requested.

## C2: frontend consumed contract obscures the server-only boundary

**Pinned location:** `IRPT_FNTEND_PRD.md@fb5bb6e8b7dfeee031bf7c2850804079eb46516d`, CONTRACTS line 116. Counterpart: `IRPT_BCKEND_PRD.md@737cd1670546b106bb12b489e1fe5d1c0f1bfa90`, lines 131 and 138.

FE line 116 groups the `resolved` and results halves together and calls them "read-only here" in a consumed-contract row. BK line 138 explicitly calls the `resolved` half server-only; line 131 excludes server-only credential and vendor-routing fields from the browser. Describing the internal half as readable by FE leaves the paired contracts in conflict about what crosses that boundary.

FE line 109 inherits the counterpart's field definitions, and F5 at line 96 correctly prohibits browser submission of `resolved` and display of vendor comparison IDs. Those guards are present and credited. They do not make the new consumed/read-only wording unambiguous: write prohibition and read exclusion are different obligations. This is a contract wording finding, not an observed disclosure or an implementation vulnerability claim.

**Required correction:** state explicitly that the internal `resolved` envelope remains server-only and is not a frontend response payload. F5 produces only the policy-permitted browser request half and consumes the authorized public request/job/report projection. Keep public results read-only and keep the rule that results cannot establish ownership. Preserve the existing request fields, immutable snapshot, ordered opaque comparison keys, variant/count validation, stable retry idempotency and Opal job polling.

The supporting UI source is `docs/research/investor_reporting_ycharts_variants_20260911/UI_CONTRACT.md@72acd16e66f02bc294d5021bd08814cb3f78f82f`, lines 64-76. It distinguishes the internal job envelope from browser input and separates request, resolved inputs and results. The explicit server-only requirement being reconciled here comes from the counterpart PRD.

## Evidence and checks that passed

The v0.10 -> v0.11 Git delta changes only the version header (line 8) and six content lines (119, 123, 178, 210, 273, 294). ENDPOINT and CONTRACTS are byte-identical between those commits. The six content changes explicitly bind the UI contract to F5, progress to F7 and export to F8/F9, and carry the available synthetic PDFs into B10/B14 while retaining their section/export certification and real-client proof gaps. They introduce no new ratified-text or contract disagreement and leave C1 and C2 unchanged. This verdict supersedes the uncommitted v0.10 draft.

The adjacent `IRPT_L4R_RATIFIED_TEXT_COMPARISON_20260911.json` contains a row for each compared field with PRD line, source path, full source commit and source line. It preserves the initial field comparison at 04:25:14 UTC and records the subsequent v0.11 byte-equality and current-pin checks at 2026-09-11T04:33:45.967975+00:00; SHA-256 `5c31f817f7f5faa7ac5d9f1e68d0db38a22a939d0ffe2dc10434955ebbc14c85`.

| PRD | Endpoint blocks | Compared fields | Equal after whitespace normalization | Source soft-wrap joins | Substantive mismatches |
|---|---:|---:|---:|---:|---:|
| BK v0.11 | 10 | 30 | 29 | 1 | 0 |
| FE v0.5 | 8 | 24 | 23 | 1 | 0 |

The single additional normalization in each PRD is FWD-3 ACCEPT's source line wrap `vendor-` / `calculated`, already identified in the v0.4 review. No other spelling, punctuation or wording normalization was applied. Header outcome sets match the endpoint denominators. A changed ZERO/ONE proof fails comparison, and a nonexistent source commit fails retrieval. All ten original BK CONSTRAINT lines and all eight original FE CONSTRAINT lines remain unchanged from the signed v0.4 text. Neither endpoint contains a full seat serial. The new BK CONSTRAINT++ operative text matches its ratified source; C1 concerns the added history around it.

Field sources at exact commits:

- Original outcomes: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ENDPOINT_FWD_INVESTOR_REPORTING_LIGHTWEIGHT_20260910.md@58266dab2d7974bd3e24b469c89c7e5fdb63ae88`.
- FWD-9/10/11: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ENDPOINT_FWD_IRPT_BCKEND_20260910.md@2dcd88091f087c089ef8547452803d7b3285eaf4`.
- FWD-12: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ENDPOINT_FWD_IRPT_FNTEND_20260910.md@5c18c8882631115a4ca0e39971e952690b916953`.

The pinned base briefs are `docs/briefs/investor-reporting-ir-bk-brief-20260910.md` and `docs/briefs/investor-reporting-ir-fe-brief-20260910.md` at `2acf23d8fd2a51fdef0b38ff7ef193f0c233661d`. The amended supplement and UI contract were read at `72acd16e66f02bc294d5021bd08814cb3f78f82f`. Comparison used committed PRD blobs. Both latest PRD-changing commits still equaled the requested commits immediately before this record was written; HEAD and normalized working-tree text matched the reviewed blobs.

Outside C2, the paired inventories preserve the ten BK-originated contracts, FE's RenderPackage producer role, and FE's newly explicit browser request producer role. The prior cohort semantics, authoritative/unknown classification rule and ExportBundle preview consumer remain present. Original constraint checks preserve entitlement versus termination, isolated firm scope, provider units and methods, unsupported positions, custody basis and residuals, late-response rejection, narrative limitations, ingestion firm/destination policy and existing portal component obligations.

The new mechanism remains fixed, and research specimens remain research evidence. Production session-secret cutover, concurrent publication fencing, real token rotation, cloud eviction/self-healing and the specified live variant proofs remain acceptance obligations in the amended chain. This review does not convert the isolated proof packet into production certification.

## Unknown unknowns and disposition

The field comparison establishes textual fidelity; it cannot establish which fields a future API will actually return. That unmeasured behavior is why the public/internal contract boundary must be explicit before implementation. Production execution, browser payload inspection and the CRO brief-coverage denominator are outside this CVO review. No live vendor call was made.

The CTO can correct C1 and C2 independently, bump the affected PRD headers, and return the committed versions through L4-R. The exact CVO sign-off records will carry REFUSED and reference this review at its own full commit. The notifier therefore continues to withhold COO release. Publication state for this seat: LOCAL; no push performed.

Signed: `3.0.0_SA_CVO`.
