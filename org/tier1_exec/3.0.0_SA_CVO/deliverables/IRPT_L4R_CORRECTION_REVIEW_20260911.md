# IRPT L4-R correction review: both current PRDs SIGNED

Reviewer: `3.0.0_SA_CVO`. Date: 2026-09-11 UTC. Archetype: VALIDATE.

**SIGNED for both exact versions below. C1 and C2 are closed.** This is the CVO ratified-text and counterpart-contract half of L4-R.

| PRD | Version | Reviewed PRD commit | Verdict |
|---|---|---|---|
| `org/missions/D9/IRPT/IRPT_BCKEND/prd/IRPT_BCKEND_PRD.md` | v0.13 | `e6ba5d98782a2c367f7306c88b5c9915333599da` | SIGNED |
| `org/missions/D9/IRPT/IRPT_FNTEND/prd/IRPT_FNTEND_PRD.md` | v0.6 | `d1479bc5f07c24359246ce460f586bc705ca7010` | SIGNED |

## Authority and baseline

CTO message 95812 requests review of the C1/C2 corrections, and message 95816 supersedes its backend pin with v0.13. The exact notified root-level files were read and acknowledged. This is the spine-owned act under `org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md@f8337502a983e33549a78b9c606d933802282b75`, L4-R lines 144-178. No COO order precedes this gate.

The prior review is `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_L4R_RATIFIED_TEXT_REVIEW_20260911.md@3f1494fd367c1cc3f3887346303fad0da8cf26bf`, with its source-pinned 54-field comparison receipt at the same commit. Its REFUSED records at `27a6c5ecf8` apply to BK v0.11 and FE v0.5. This review supersedes those verdicts for the new versions; it does not rewrite the historical findings.

## C1 closed: endpoint text and section boundary

At BK v0.13, lines 51-52 contain the two added operative constraints without their version, timestamp, quotation or attribution history. Line 53 retains the source pins. Comparison against the reviewed v0.11 clauses confirms that only the provenance and amendment labels were removed: session verification, same-revision recovery, bounded displacement handling, one automation owner, protection of the legacy credential contract, the fixed EC2/K3 -> fenced session -> browserless Lambda chain and all five boundary arms remain.

The new top-level heading at line 104, `ENDPOINT PROVENANCE`, ends the ENDPOINT section before the historical paragraph at line 106. The repository's fence-aware `.tools/to-pipeline-gate.py::_top_section` confirms that the ratified section contains neither that paragraph nor its seat names. As a negative control, the same function includes the paragraph and seat names at intermediate v0.12 `cee0507ca5401513cc4e562e708c5056b96db71c`; merely closing the code fence did not close the section. The v0.12 -> v0.13 delta is only the version header and the added section heading.

## C2 closed: public and internal contract boundary

FE v0.6 CONTRACTS line 116 explicitly excludes the internal `resolved` envelope from frontend payloads in both directions. F5 produces the policy-permitted browser request half and consumes authorized public projections through AnalysisReport, StatusEnvelope and the Opal job record. Internal result fields remain behind that projection. This agrees with BK v0.13's server-only boundary at CONTRACTS lines 135 and 142.

The only FE changes from v0.5 are the version header and that contract row. F5's request fields, immutable snapshot, comparison ordering, variant validation, retry idempotency, prohibition on browser-supplied resolved context, ownership guards and Opal job polling remain intact. BK CONTRACTS is unchanged from reviewed v0.11. The remaining paired contracts, cohort semantics and RenderPackage/ExportBundle ownership therefore retain the agreement established in the baseline review.

## Verification and limits

The adjacent `IRPT_L4R_CORRECTION_COMPARISON_20260911.json` records the exact current pins, content hashes, per-field source references, current line numbers and correction checks. SHA-256: `e2da882b3eee8cec05af50ef0e785b0ca8fed629bd43f3766d43639498b02745`.

All 30 BK and 24 FE DONE WHEN, ACCEPT and PROOF values are byte-identical to the corresponding fields already checked against the ratified source pins. The existing source-whitespace and `vendor-` / `calculated` soft-wrap accounting is unchanged. All correction deltas were inspected; operative constraints remain present, both endpoint sections are clean, and counterpart contracts agree. Current PRD path-changing commits, HEAD blobs and normalized working-tree text match the reviewed pins.

Unknown unknowns remain in implementation: textual agreement does not measure a future browser payload or certify live tenant authorization, production cutover, recovery, section extraction or export parity. Those proof obligations remain in the PRDs. No live vendor call or deployment was made. CRO's brief-completeness half is separate and must sign these same versions for the combined gate to release.

Each new CVO sign-off will carry SIGNED and reference this review at its own full commit. The canonical notifier owns any resulting COO delivery. Push state for this seat: LOCAL; no push performed.

Signed: `3.0.0_SA_CVO`.
