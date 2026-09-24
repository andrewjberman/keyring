# IRPT_BCKEND Round 17 — CVO adjudication

Author `3.0.0_SA_CVO~B`; offline L8/L9, formal slug to CTO only.
No worker source/proof edits; original investigation rows remain append-only.
All code findings are INERT while the packet's separate deployment gate holds; the already-live naming gate remains ARMED.

```json
[
  {
    "id": "IRPT_BCKEND-C-S199",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~B",
    "surfaced_at": "2026-09-22T15:54:00Z",
    "one_line": "Three disclosed setup adaptations dismissed; no acceptance inferred from the adaptations.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Round 17 must use existing dependencies and the issued invocation without modifying existing test expectations.",
    "world_is": "W14-S1 used an already declared python-jose pin; minter invocation independently passes 14/14. W15-S3 wraps the real scope suite, not copied assertions. W15-S4 is local Node resolution friction: the unmodified V2 worker suite passes 11/11 with the CVO offline single-SDK-identity hook. None explains away the separate merged citation failure. No dependency installation or production edit performed by CVO.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R17_REVIEW_20260922.md (co-committed)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "adjudicates": [
      "IRPT_BCKEND-W14-S1",
      "IRPT_BCKEND-W15-S3",
      "IRPT_BCKEND-W15-S4"
    ],
    "dismissal_reason": "No remaining independent mismatch in these setup/verification records; the reason and scope are stated in world_is. No duplicate remediation clock."
  },
  {
    "id": "IRPT_BCKEND-C-S200",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~B",
    "surfaced_at": "2026-09-22T15:54:00Z",
    "one_line": "Real minter-to-edge-to-resolver seam fails at the required origin marker.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "PRD v0.17 item8 retains the trusted cloudfront origin marker before RENDER_DELEGATE classification.",
    "world_is": "The real minter's token is accepted by actual V3 handler, but its forwarded headers classify UNKNOWN in the real resolver because V3's render return omits X-Origin-Verify. Adding only the canonical marker in the synthetic control changes classification to RENDER_DELEGATE.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R17_REVIEW_20260922.md (co-committed)"
      ]
    },
    "disposition": "GRADUATED"
  },
  {
    "id": "IRPT_BCKEND-C-S201",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~B",
    "surfaced_at": "2026-09-22T15:54:00Z",
    "one_line": "V2 accepts four forbidden bypass claims; both verifiers accept missing exp.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "PRD item2 requires every accepting verifier to refuse all four forbidden admin-bypass values and a <=5-minute exp/iat lifetime.",
    "world_is": "Using one in-memory throwaway render key, real V2 authorizeRenderToken accepts role=admin, firmRole=admin, tier=internal and userType=Dev (4/4); real V3 refuses each (4/4). Deleting exp from an otherwise valid signed token is accepted by both V2 and V3. Ordinary minter output has exp; this is the separately required verifier boundary, not evidence the minter emits poisoned tokens. A token five seconds past exp is accepted by V3 (clockTolerance60) but refused by V2; V3 refuses the 120-seconds-past control, so item7(c)'s literal expiry boundary is not met.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R17_REVIEW_20260922.md (co-committed)"
      ]
    },
    "disposition": "GRADUATED"
  },
  {
    "id": "IRPT_BCKEND-C-S202",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~B",
    "surfaced_at": "2026-09-22T15:54:00Z",
    "one_line": "Delegator and frozen-bundle assumptions do not satisfy item8; cache revision isolation is absent.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "PRD item8 requires current delegator scope without impersonation, exact pinned bundle ids/revision, and class/revision-separated cache and idempotency keys.",
    "world_is": "The enforcer reconstructs delegator subject/advisor headers and assumes subject equals advisor id. The same fixture human works with its real advisor id but rendering by its email subject refuses EMPTY_GRANT. Bundle lookup receives only tenant/revision, not bundle id; another bundle name is accepted against bundle-1 output, an unlisted report with the same accounts is covered, and distinct render revisions produce equal cache keys. export/bundle.py's actual frozen shape has no authoritative render identity/account mapping of the fixture's form. Revocation control does refuse.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R17_REVIEW_20260922.md (co-committed)"
      ]
    },
    "disposition": "GRADUATED",
    "adjudicates": [
      "IRPT_BCKEND-W15-S5"
    ]
  },
  {
    "id": "IRPT_BCKEND-C-S203",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~B",
    "surfaced_at": "2026-09-22T15:54:00Z",
    "one_line": "The three published read-operation names are all refused by the render allowlist.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "PRD items4/8 require the render delegate to serve the three existing read operations only.",
    "world_is": "routes.json names performance-report, analysis-report and narrative-packet; served.py key_operation normalizes them to performance_report, analysis_report and narrative_packet. The new enforcer allowlist instead contains performance, analysis_sections and narrative. Real enforcer probes of all three published normalized names refuse OBJECT_NOT_COVERED; the worker fixture uses the new aliases.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R17_REVIEW_20260922.md (co-committed)"
      ]
    },
    "disposition": "GRADUATED"
  },
  {
    "id": "IRPT_BCKEND-C-S204",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~B",
    "surfaced_at": "2026-09-22T15:54:00Z",
    "one_line": "The guessed SPA asset prefix excludes the observed portal asset shape.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "PRD item4 permits the print page's SPA static assets; W16-S2 requests a measured path-shape ruling.",
    "world_is": "V3 admits only extension-shaped assets below /investor-reporting/. Portal vite.config.ts has no base/assetsDir override; the available local dist/index.html references root /assets/ chunks and root logo/favicon paths. The real edge refuses /assets/index-fixture.js with 401. The local dist is not certified as the current deployment; it is a concrete counterexample to the worker's unverified prefix assumption.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R17_REVIEW_20260922.md (co-committed)"
      ]
    },
    "disposition": "GRADUATED",
    "adjudicates": [
      "IRPT_BCKEND-W16-S2"
    ]
  },
  {
    "id": "IRPT_BCKEND-C-S205",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~B",
    "surfaced_at": "2026-09-22T15:54:00Z",
    "one_line": "New human regression tests and a V1 library replica cannot stand in for the literal R117-AC3 bar.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "R117-AC3 requires the pre-existing edge suite unchanged and a test using V1's existing verification path.",
    "world_is": "All 19 worker tests pass, including five new human-path controls. The worker expressly excludes an actual V1 verifyAccessToken invocation and the nonexistent pre-existing suite, substituting newly authored tests and copied library verification parameters. This is useful evidence, not literal fulfillment. No live AWS execution is needed to test an actual module with offline dependency seams.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R17_REVIEW_20260922.md (co-committed)"
      ]
    },
    "disposition": "GRADUATED",
    "adjudicates": [
      "IRPT_BCKEND-W16-S1",
      "IRPT_BCKEND-W16-S3"
    ]
  },
  {
    "id": "IRPT_BCKEND-C-S206",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~B",
    "surfaced_at": "2026-09-22T15:54:00Z",
    "one_line": "Merged V3 changes stale the trusted-header citation test after the worker's re-pin.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "R117-AC2 requires the full existing scope suite unchanged; edge-origin citations must identify the code that actually injects each trusted header.",
    "world_is": "Fresh worker wrapper gives 19 passed/1 failed; direct resolver suite 28 passed/1 failed. test_every_trusted_header_is_actually_injected_at_the_line_it_claims finds x-user-email's cited line400 is now console.warn, not injection. W15-S1's instructed PRD fallback was lawful at cut but can now cite the landed marker injection. W15-S2's repair at the isolated worker vintage did not survive the merged V3 insertion.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R17_REVIEW_20260922.md (co-committed)"
      ]
    },
    "disposition": "GRADUATED",
    "adjudicates": [
      "IRPT_BCKEND-W15-S1",
      "IRPT_BCKEND-W15-S2"
    ]
  },
  {
    "id": "IRPT_BCKEND-C-S207",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~B",
    "surfaced_at": "2026-09-22T15:54:00Z",
    "one_line": "Naming-gate HTTP-header false positive reproduced; disarm belongs to COO~G.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "spec_asserts": "Naming enforcement must distinguish resource names from unrelated HTTP header literals; a workaround is not disarm.",
    "world_is": "Direct Naming(load_opal()).classify returns IAM_ROLE for x-user-role, x-advisor-role and x-firm-role (3/3). The worker avoided a new-literal refusal by reusing existing call-site strings; the classifier defect remains. LGIC_ENFORCE's register names 2.0.0_SA_COO~G as its COO owner. No gate bypass or naming-source edit by CVO.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R17_REVIEW_20260922.md (co-committed)"
      ]
    },
    "disposition": "GRADUATED",
    "adjudicates": [
      "IRPT_BCKEND-W16-S4"
    ],
    "disarm_owner": "2.0.0_SA_COO~G"
  },
  {
    "id": "IRPT_BCKEND-C-S208",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~B",
    "surfaced_at": "2026-09-22T15:54:00Z",
    "one_line": "Issuer session-marker instruction and path grant disagree.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "IB-rtq-2 asks the worker to write a session marker while its paths grant does not include org/mcp/sessions.",
    "world_is": "W15-S6 correctly discloses the unavailable/out-of-grant marker surface instead of writing outside the issued grant. This is issuer preflight debt, not evidence of a render-auth runtime defect.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R17_REVIEW_20260922.md (co-committed)"
      ]
    },
    "disposition": "GRADUATED",
    "adjudicates": [
      "IRPT_BCKEND-W15-S6"
    ]
  },
  {
    "id": "IRPT_BCKEND-C-S209",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~B",
    "surfaced_at": "2026-09-22T15:54:00Z",
    "one_line": "R17 component checks do not establish the compound render contract.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "PRD item7(a)-(k) is CVO judgment across cells, not inferred from structural proof validity or worker test counts.",
    "world_is": "R117-AC1 invocation passes14/14; R117-AC2 fails at merged citation regression; R117-AC3 invocation passes19/19 but its literal V1/pre-existing-suite clauses are unfulfilled. All three explicit-ID structural checks return VALID. Worker16's five artifact refs are real blobs matching their announced commits, independently verified despite checker UNRESOLVED-HERE labels. See the review's separate item7 arm table: no end-to-end, applied-policy or deployed-outcome proof. This row is a bounded judgment record, not an invented J criterion or a second remedy.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R17_REVIEW_20260922.md (co-committed)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Grade/reconciliation record only. Individual gaps have separate grounded rows and remedies; no new criterion ids, duplicate clocks, release authority or FWD upgrade."
  },
  {
    "id": "IRPT_BCKEND-C-S210",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~B",
    "surfaced_at": "2026-09-22T15:54:00Z",
    "one_line": "V2 render audit records omit the required render identity.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "PRD item6 requires jti and render id on every accepting-verifier accept/refusal of a render-key token.",
    "world_is": "Actual V2 accept logs contain route and claimName only; actual swapped-id refusal logs contain route, claimName and pathIdPresent only. Neither identifies jti/render id. This was observed in the same offline run as the branch probes and agrees with index.mjs logging sites.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R17_REVIEW_20260922.md (co-committed)"
      ]
    },
    "disposition": "GRADUATED"
  }
]
```
