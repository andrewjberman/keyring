# IRPT completion — CTO session rulings

Authority: AUTHORITY.md, Andrew's direct session open-call/fork delegation recorded at `ecf350639a`. These rulings apply to this completion effort. They do not restart held canonical rounds or replace independent acceptance evidence.

## IRPT-S7-01 — conditional private reporting placement

Date: 2026-09-22. Decider and condition owner: `1.0.0_SA_CTO`, acting under Andrew's explicit session delegation. Raised by COO~M at 21:16:01Z.

**Decision: approve the proposed A2 bucket-placement exception conditionally.** Register the exact exception through `infra/logic/06_CONFORMANCE_LEDGER.md` section 6 before the destination policy becomes writable. CRO owns the existing register carrier. This ruling is the decision record, not a second exception register. The canonical entry identifier and committed carrier must be returned to M/P/Y and their reviewers.

Basis read: `infra/logic/02_DOCTRINE.md` R20, R21 and section 4; conformance ledger section 6 (including its delegated-CTO decider precedent); CONTRACT.md S7; COO~M's 73-line proposal at `C:/Users/AndrewBerman/Desktop/ajb_irpt_m/org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/STORAGE_POLICY_PROPOSAL.md`, SHA256 `23375afbb74ded78d0c2b2c12ec8058067fac0faeadaa9f55b952e138a5c8413` as read. M must preserve a committed proposal before candidate handoff.

The current user delegation authorizes CTO to adjudicate this session fork. Record acknowledgement accurately as **CTO under Andrew's explicit delegation**, linking AUTHORITY.md at `ecf350639a`; do not invent a quote saying Andrew personally approved this particular bucket. No additional user round trip is required for this bounded decision.

### Exact allowed departure

Private reporting artifacts for `49financial`, `cottonwood`, and `inflection` may reside in registered product bucket `opal-data-irpt`, with canonical firm identity retained in every key. This is an A2 placement departure from the normal firm home, not permission to label private data global, change naming grammar, or waive required upstream custody processing.

Exactly these eleven families are in scope: ORIGINAL_CSV, NORMALIZED_PORTFOLIO, REQUEST_COMPOSITION, ORIGINAL_VENDOR_PDF, EXTRACTION_EVIDENCE, PERFORMANCE, ANALYSIS, EXPORT_BUNDLE, EXPORT_PDF, EXPORT_RECEIPT, SELECTED_ACCOUNTS. PERFORMANCE and ANALYSIS are bounded JSON report payloads under platinum; the other nine are per-request/input/export state families. Canonical custody, directory, holdings and model Gold/Platinum remain in their existing long-form firm destinations. DynamoDB remains the process-state authority under the shared contract; this placement does not create a second state machine.

### Conditions and implementation responsibilities

- M implements the closed family/firm policy through the canonical registry and naming builder, with server-only validated IDs, digest and key construction. Existing default destinations remain unchanged. No browser-supplied bucket/key or fallback destination is admitted.
- P implements owner/firm isolation, current selected-account or prospect authorization before and after retrieval, least-privilege producer access, immutable accepted versions, and exact object-version/hash verification. Inaccessible interrupted objects cannot become visible reports.
- P supplies a concrete family-by-family retention/expiry policy and IAM/IaC plan before provisioning or live writes. This decision approves placement only; it does not waive R21 expiry requirements or approve indefinite storage. Preserve existing evidence while that policy is prepared; no cleanup/deletion is authorized by this ruling.
- Every affected reader/writer consumes the same registered policy revision. Cutover is coordinated and bounded; no standing dual-write fallback, estate-wide migration, or deletion. Naming owners review the registry/builder change; CVOs independently verify it with actual reader/writer evidence.
- Until the canonical entry is recorded and the implementation enforces these conditions, policy remains pending and cannot yield a writable destination. If a condition ceases to hold, disable affected publication/retrieval as appropriate and route the failure to CTO; do not silently revert or broaden access.
- End condition: this conditional exception ceases when CTO supersedes it through the same canonical register, the named product placement is retired, or required conditions no longer hold. CTO owns condition review upon owner/reviewer reports.

M can complete the candidate builder, tests and interfaces now. P can complete repository composition, least-privilege plans and retention specification now. Existing live/vendor, production, and R18-e render gates remain separate and unchanged. No product criterion receives PASS from this policy decision alone.
