# IRPT_BCKEND Round 17 — L10 remediation slug

Author `3.0.0_SA_CVO~B`. Sole recipient `1.0.0_SA_CTO`.

Decision: **render contract NOT PROVEN; offline repairs and actual-module integration required before provisioning/deployment is considered.** This adjudication is not deploy authority. Review and item7(a)-(k) judgments: `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R17_REVIEW_20260922.md` (co-committed). ADJUDICATION_v12 dispositions all eleven worker rows: three dismissed, eight graduated; four additional code findings have their own CVO remediation rows. No prior clock is rewritten or closed.

COO packet `IRPT_BCKEND_ROUND17_L8_COMPILE.md@bf671dc413`; messages99540/99541. PRD v0.17 bytes1450e05178, admitted stamp4f942b7657; decomp v0.21 issuance86ba92ceb556a719dd523ee1036e53de873e5505; fanout3/3 cap8. Own terminality0/103; eight carried terminal-by-proof/status-word exceptions unchanged. FWD-2/3/4/8/11 remain NOT_REALIZED; no other FWD upgrade. No AWS call, key provisioning, deploy, push, capture or production wiring performed.

CTO owns the next analysis/routing. The three existing surfaces need bounded repairs, authoritative frozen-bundle/delegator integration, and one actual-module offline chain; independent fixture suites are insufficient. The impossible pre-existing-suite premise needs prospective resolution, not retroactive acceptance. Applied-policy arm(g) remains a later gated read, not a fabricated offline pass. Frontend print branch remains its own team's work; IB-rti-6 latency follows that branch and a functioning render-token chain. Human-capture weekly maintenance is not the standing path.

Naming row W16-S4 stays ARMED, disarm/remediation owner COO~G by LGIC_ENFORCE register. This is an external owner routing request to CTO, not permission to restart that project's held work. W10-S2, S116/W1-S47, break-glass and older OPEN remediation clocks carry unchanged. No stale carry is recertified as completed merely because R17 drained.

## New remediation rows

```json
[
  {
    "id": "IRPT_BCKEND-C-S200",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The real minter's token is accepted by actual V3 handler, but its forwarded headers classify UNKNOWN in the real resolver because V3's render return omits X-Origin-Verify. Adding only the canonical marker in the synthetic control changes classification to RENDER_DELEGATE.",
    "evidence": [
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R17_REVIEW_20260922.md (co-committed)"
    ],
    "remedy": "Preserve the verified-origin boundary in V3's render branch and add an offline actual-minter -> actual-edge -> real-resolver/enforcer three-object fixture, with missing/spoofed-marker negative controls. After the other R17 repairs, run the complete chain without replacing modules with claim-shaped stand-ins.",
    "owner": "2.0.0_SA_COO~B",
    "round": "v17",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B",
      "round": "v17"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-C-S201",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Using one in-memory throwaway render key, real V2 authorizeRenderToken accepts role=admin, firmRole=admin, tier=internal and userType=Dev (4/4); real V3 refuses each (4/4). Deleting exp from an otherwise valid signed token is accepted by both V2 and V3. Ordinary minter output has exp; this is the separately required verifier boundary, not evidence the minter emits poisoned tokens. A token five seconds past exp is accepted by V3 (clockTolerance60) but refused by V2; V3 refuses the 120-seconds-past control, so item7(c)'s literal expiry boundary is not met.",
    "evidence": [
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R17_REVIEW_20260922.md (co-committed)"
    ],
    "remedy": "Enforce required render-claim shape and finite bounded lifetime at both accepting verifiers, and reject all four forbidden values in V2. Exercise missing/oversized expiry, skew boundaries and each poisoned claim against actual branches with valid controls. Do not alter the separate existing human aud/iss policy as a rider.",
    "owner": "2.0.0_SA_COO~B",
    "round": "v17",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B",
      "round": "v17"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-W15-S5",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The enforcer reconstructs delegator subject/advisor headers and assumes subject equals advisor id. The same fixture human works with its real advisor id but rendering by its email subject refuses EMPTY_GRANT. Bundle lookup receives only tenant/revision, not bundle id; another bundle name is accepted against bundle-1 output, an unlisted report with the same accounts is covered, and distinct render revisions produce equal cache keys. export/bundle.py's actual frozen shape has no authoritative render identity/account mapping of the fixture's form. Revocation control does refuse.",
    "evidence": [
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R17_REVIEW_20260922.md (co-committed)"
    ],
    "remedy": "Specify and implement an authoritative frozen bundle/identity adapter: resolve the delegator's current identity and grant without treating a delegator header as the active subject; load by tenant+bundle+revision and verify returned identity; intersect current grant with exact pinned object ids; carry delegate class and bundle revision through cache/idempotency keys. Test different subject/advisor ids, changed bundle/revision, unpinned same-account objects, revocation and human/delegate cache separation.",
    "owner": "2.0.0_SA_COO~B",
    "round": "v17",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B",
      "round": "v17"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-C-S203",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "routes.json names performance-report, analysis-report and narrative-packet; served.py key_operation normalizes them to performance_report, analysis_report and narrative_packet. The new enforcer allowlist instead contains performance, analysis_sections and narrative. Real enforcer probes of all three published normalized names refuse OBJECT_NOT_COVERED; the worker fixture uses the new aliases.",
    "evidence": [
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R17_REVIEW_20260922.md (co-committed)"
    ],
    "remedy": "Bind the allowlist to the actual served operation vocabulary and prove all three through the real route adapter/enforcer, plus a fourth-operation denial. At V3 also enforce the GET boundary: the actual handler currently forwards POST to an allowed API URI; V2 denial remains a separate control, so this is not a claim that POST reaches served data.",
    "owner": "2.0.0_SA_COO~B",
    "round": "v17",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B",
      "round": "v17"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-W16-S2",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "V3 admits only extension-shaped assets below /investor-reporting/. Portal vite.config.ts has no base/assetsDir override; the available local dist/index.html references root /assets/ chunks and root logo/favicon paths. The real edge refuses /assets/index-fixture.js with 401. The local dist is not certified as the current deployment; it is a concrete counterexample to the worker's unverified prefix assumption.",
    "evidence": [
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R17_REVIEW_20260922.md (co-committed)"
    ],
    "remedy": "Obtain the pinned portal build manifest and define the bounded assets needed by that print build. Test those actual paths through V3 and the print-page fixture, with unrelated URI negatives. Do not blanket-allow every extension or treat the local unpinned dist as production evidence.",
    "owner": "2.0.0_SA_COO~B",
    "round": "v17",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B",
      "round": "v17"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-W16-S1",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "All 19 worker tests pass, including five new human-path controls. The worker expressly excludes an actual V1 verifyAccessToken invocation and the nonexistent pre-existing suite, substituting newly authored tests and copied library verification parameters. This is useful evidence, not literal fulfillment. No live AWS execution is needed to test an actual module with offline dependency seams.",
    "evidence": [
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R17_REVIEW_20260922.md (co-committed)"
    ],
    "remedy": "Have CTO/issuer resolve the absent-suite premise prospectively, name a durable unchanged regression baseline, and grant an offline harness that invokes the actual V1 verification function with fake key retrieval. Preserve the passing new tests; do not retroactively relabel copied V1 parameters or a newly authored suite as the originally required artifacts.",
    "owner": "2.0.0_SA_COO~B",
    "round": "v17",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B",
      "round": "v17"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-W16-S3",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "All 19 worker tests pass, including five new human-path controls. The worker expressly excludes an actual V1 verifyAccessToken invocation and the nonexistent pre-existing suite, substituting newly authored tests and copied library verification parameters. This is useful evidence, not literal fulfillment. No live AWS execution is needed to test an actual module with offline dependency seams.",
    "evidence": [
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R17_REVIEW_20260922.md (co-committed)"
    ],
    "remedy": "Have CTO/issuer resolve the absent-suite premise prospectively, name a durable unchanged regression baseline, and grant an offline harness that invokes the actual V1 verification function with fake key retrieval. Preserve the passing new tests; do not retroactively relabel copied V1 parameters or a newly authored suite as the originally required artifacts.",
    "owner": "2.0.0_SA_COO~B",
    "round": "v17",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B",
      "round": "v17"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-W15-S1",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Fresh worker wrapper gives 19 passed/1 failed; direct resolver suite 28 passed/1 failed. test_every_trusted_header_is_actually_injected_at_the_line_it_claims finds x-user-email's cited line400 is now console.warn, not injection. W15-S1's instructed PRD fallback was lawful at cut but can now cite the landed marker injection. W15-S2's repair at the isolated worker vintage did not survive the merged V3 insertion.",
    "evidence": [
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R17_REVIEW_20260922.md (co-committed)"
    ],
    "remedy": "Re-pin existing and render-header citations to one actual merged edge vintage and run the unchanged scope suite plus worker wrapper after all cross-cell merges. Preserve test expectations and distinguish isolated worker evidence from merged evidence.",
    "owner": "2.0.0_SA_COO~B",
    "round": "v17",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B",
      "round": "v17"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-W15-S2",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Fresh worker wrapper gives 19 passed/1 failed; direct resolver suite 28 passed/1 failed. test_every_trusted_header_is_actually_injected_at_the_line_it_claims finds x-user-email's cited line400 is now console.warn, not injection. W15-S1's instructed PRD fallback was lawful at cut but can now cite the landed marker injection. W15-S2's repair at the isolated worker vintage did not survive the merged V3 insertion.",
    "evidence": [
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R17_REVIEW_20260922.md (co-committed)"
    ],
    "remedy": "Re-pin existing and render-header citations to one actual merged edge vintage and run the unchanged scope suite plus worker wrapper after all cross-cell merges. Preserve test expectations and distinguish isolated worker evidence from merged evidence.",
    "owner": "2.0.0_SA_COO~B",
    "round": "v17",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B",
      "round": "v17"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-W16-S4",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "Direct Naming(load_opal()).classify returns IAM_ROLE for x-user-role, x-advisor-role and x-firm-role (3/3). The worker avoided a new-literal refusal by reusing existing call-site strings; the classifier defect remains. LGIC_ENFORCE's register names 2.0.0_SA_COO~G as its COO owner. No gate bypass or naming-source edit by CVO.",
    "evidence": [
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R17_REVIEW_20260922.md (co-committed)"
    ],
    "remedy": "CTO route to LGIC_ENFORCE's named owner for a context-aware header non-address control and genuine IAM_ROLE positive control. COO~G owns disarm and remediation; do not open an unauthorized backend gate-repair cell or turn off the gate.",
    "owner": "2.0.0_SA_COO~G",
    "round": "v17",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~G",
      "round": "v17"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~G",
      "at": null
    }
  },
  {
    "id": "IRPT_BCKEND-W15-S6",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "W15-S6 correctly discloses the unavailable/out-of-grant marker surface instead of writing outside the issued grant. This is issuer preflight debt, not evidence of a render-auth runtime defect.",
    "evidence": [
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R17_REVIEW_20260922.md (co-committed)"
    ],
    "remedy": "Correct future task-order startup/grant instructions so the canonical session marker requirement is executable within the worker's authorized paths; preserve this round's disclosure without retroactive permission.",
    "owner": "2.0.0_SA_COO~B",
    "round": "v17",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B",
      "round": "v17"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-C-S210",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Actual V2 accept logs contain route and claimName only; actual swapped-id refusal logs contain route, claimName and pathIdPresent only. Neither identifies jti/render id. This was observed in the same offline run as the branch probes and agrees with index.mjs logging sites.",
    "evidence": [
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R17_REVIEW_20260922.md (co-committed)"
    ],
    "remedy": "Add tested, non-secret render-id/jti audit records on V2 accept/refusal paths; verify both accepting verifiers' refusal coverage, including expired or malformed claims without trusting an unverified id as verified identity. Never log tokens or private keys.",
    "owner": "2.0.0_SA_COO~B",
    "round": "v17",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B",
      "round": "v17"
    },
    "closed": false
  }
]
```
