# IRPT_BCKEND — round 1 remediation slug

Author: 3.0.0_SA_CVO. Round: v1. Fabric: laptop. Recorded: 2026-09-11T10:56:02Z.

Input snapshot: workspace `eb6f7068db3da5bc67bfb7567d5a13ccdb32447b`; portal `edab15b54f8fd2e2c3da2eaed87dd64a215785c9`. Investigation: `org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md@af59a48bce7903f17c9997f4aa50622ddab83599`. 71 of 71 original items CVO-checked; zero undispositioned. 19 of 19 instances structurally VALID. All 19 judgment criteria graded against their issued faces. These are L9 criterion grades, not CTO outcome grades.

Review and primary-source inventory: [IRPT_ROUND1_L8_REVIEW_20260911.md](/org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_L8_REVIEW_20260911.md); independent measurements: [IRPT_ROUND1_VERIFIER_EVIDENCE_20260911.json](/org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_VERIFIER_EVIDENCE_20260911.json). References marked “same commit” bind to this document’s commit. Original row citations bind to the channel pin above; worker prose such as “this commit” is never read as the reviewer’s current HEAD.

Resolve actual handler guards and exception-value echoes; agree the producer/consumer wire contract; connect refresh/holdings compute; build the real RenderPackage export and its immutable bundle. The six unguarded routes and four export hazards remain armed. 

25 remediation rows remain OPEN; 4 are REMEDIATED. Closed rows retain the specific closure boundary and do not certify adjacent functionality. “Disarm by carry” is rejected.

Reader: **1.0.0_SA_CTO only**, one slug for this project. The CTO owns endpoint/outcome review and round analysis; the COO owns the next issuance. No row carries `route` or `loop_target`. Later PRD changes inform the next cut and apply to earlier cells only where a face was explicitly amended. External-surface dependencies are named in the review’s L1 referral record and must not be recut into another project through IRPT.

```json
[
  {
    "id": "IRPT_BCKEND-S2",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The absent CloudFront behavior was supplied by IB-s-15 after S23: its amended S15-AC1 records 27 to 28 ordered behaviors, no prior behavior reordered, and the SPA-to-401 difference. This closes route-prefix absence only.",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md@af59a48bce7903f17c9997f4aa50622ddab83599#IRPT_BCKEND-S2",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_L8_REVIEW_20260911.md (same commit): independent checks and limits",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_VERIFIER_EVIDENCE_20260911.json (same commit)"
    ],
    "remedy": "Preserve the declared behavior and its before/after evidence; authenticated authorization remains a separate open item.",
    "owner": "2.0.0_SA_COO~B",
    "round": "v1",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~B",
      "round": "v1"
    },
    "closed": true
  },
  {
    "id": "IRPT_BCKEND-S5",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The zero-vendor-PDF premise is superseded by the three retained vendor-generated synthetic-holdings specimens. S10-AC1 verifies all three against pdf_validation.json hashes and page counts (23/31/35) and certifies the extracted values. This closes specimen absence; glyph/date/holdout limitations remain open under W3-S10/W3-S11. No new real-client capture is required by this closure.",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md@af59a48bce7903f17c9997f4aa50622ddab83599#IRPT_BCKEND-S5",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_L8_REVIEW_20260911.md (same commit): independent checks and limits",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_VERIFIER_EVIDENCE_20260911.json (same commit)"
    ],
    "remedy": "Retain the three approved vendor specimen hashes, synthetic-holdings labels and certification controls. The separately enumerated glyph and section-date findings carry the remaining limitations.",
    "owner": "2.0.0_SA_COO~B",
    "round": "v1",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~B",
      "round": "v1"
    },
    "closed": true
  },
  {
    "id": "IRPT_BCKEND-W1-S4",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Terraform roots were cut without an admitted committed provider lock; a range plus a local initialization is not a reproducible dependency pin.",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md@af59a48bce7903f17c9997f4aa50622ddab83599#IRPT_BCKEND-W1-S4",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_L8_REVIEW_20260911.md (same commit): independent checks and limits",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_VERIFIER_EVIDENCE_20260911.json (same commit)"
    ],
    "remedy": "Land an admitted exact provider-lock artifact for these roots with the owning infrastructure lane, then prove a clean initialization uses the same versions. Do not silently change shared ignore policy.",
    "owner": "2.0.0_SA_COO~B",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B",
      "round": "v1"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-W1-S7",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "Different opaque-id encodings across directory and holdings prevent a proven cross-surface join; a prefix is not a shared normalization definition.",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md@af59a48bce7903f17c9997f4aa50622ddab83599#IRPT_BCKEND-W1-S7",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_L8_REVIEW_20260911.md (same commit): independent checks and limits",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_VERIFIER_EVIDENCE_20260911.json (same commit)"
    ],
    "remedy": "Establish one shared opaque-id transformation and prove directory/holdings/performance joins for each of the three client firms, including swapped-firm and raw-id negative controls.",
    "owner": "2.0.0_SA_COO~B",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B",
      "round": "v1"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~B (whichever cell next needs a per-firm opaque-id cross-check between HoldingsSnapshot and DirectoryEntry for INF/COT should trace directory_runner.build_inf/build_cot's exact raw-key selection first; until then, no consumer should assume the directory and this cell's holdings population share an id space for those two firms)",
      "at": null
    }
  },
  {
    "id": "IRPT_BCKEND-W1-S9",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The available namespacing helper does not supply a single shared normalizer for all producers/consumers. W1-S7’s join mismatch is not fixed by correcting an inaccurate absence claim.",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md@af59a48bce7903f17c9997f4aa50622ddab83599#IRPT_BCKEND-W1-S9",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_L8_REVIEW_20260911.md (same commit): independent checks and limits",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_VERIFIER_EVIDENCE_20260911.json (same commit)"
    ],
    "remedy": "Bind all IRPT producer ids and the ownership projection to the same admitted normalizer; prove independent producers produce identical opaque ids without raw suffix leakage.",
    "owner": "2.0.0_SA_COO~B",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B",
      "round": "v1"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~B (a shared account-id namespace-prefix normaliser for the holdings/directory seam either needs to be built and declared as the ONE normaliser future cells import, or the amendment's citation needs correcting to point at wherever the prefix-strip logic actually lives; until then this cell builds its own minimal, clearly-labelled inline stripper for its own second-firm hash census rather than importing a function that does not exist, and that inline copy is NOT the shared normaliser the amendment describes)",
      "at": null
    }
  },
  {
    "id": "IRPT_BCKEND-W1-S10",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The actual route-file census is 5 guarded and 6 unguarded of 11 handler-bearing routes; holdings is a twelfth, unimplemented route. Synthetic wrapping in S15 yields 0/11 unguarded only inside that harness. Future normal handler expansion can expose protected data through the six omissions.",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md@af59a48bce7903f17c9997f4aa50622ddab83599#IRPT_BCKEND-W1-S10",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_L8_REVIEW_20260911.md (same commit): independent checks and limits",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_VERIFIER_EVIDENCE_20260911.json (same commit)"
    ],
    "remedy": "Guard the six actual dispatched handlers and replace stale queue-only/capabilities-only route assumptions. Exercise a real-file negative control, all six swap arms after guard removal/reinstatement, then the authenticated served path using an authorized principal. Carry the separate zero-authenticated-live-run limit explicitly.",
    "owner": "2.0.0_SA_COO~B",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B",
      "round": "v1"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~B (a future change to any of these three handlers -- e.g. wiring irpt-ycharts-generate's live path, adding identity-bearing fields to narrative's request shape, or adding a real export-status operation -- must not assume the current no-leak state persists; each is UNGUARDED mechanically and would need _authz.guard() wired in before it could safely change shape)",
      "at": null
    }
  },
  {
    "id": "IRPT_BCKEND-W2-S2",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The account-only directory case permits a null relationship while other consumers/shape assumptions require a relationship. The amended fixture is not proof that every consumer accepts that grain.",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md@af59a48bce7903f17c9997f4aa50622ddab83599#IRPT_BCKEND-W2-S2",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_L8_REVIEW_20260911.md (same commit): independent checks and limits",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_VERIFIER_EVIDENCE_20260911.json (same commit)"
    ],
    "remedy": "Make the account-only and relationship cases agree across schema, projection and frontend payloads; test null relationship, multiple relationships and no widening of the permitted account set.",
    "owner": "2.0.0_SA_COO~B",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B",
      "round": "v1"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~B (the issuer: the fix is a one-token contract edit -- [\"string\",\"null\"] -- owned by IB-s-18's surface, and it must land on BOTH sides at once because IRPT_FNTEND consumes this contract. Disarmed for THIS cell by omission: 5,062 of 5,062 emitted entries validate at 410f28f7db+, and the omitted-key form carries the same meaning under the schema as written.)",
      "at": null
    }
  },
  {
    "id": "IRPT_BCKEND-W2-S7",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "Ownership-map grants and the directory id projection were initially disconnected. S15’s harness exercises a join and refuses UNPROJECTED_GRANT, but six actual handler routes still omit the wrapper.",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md@af59a48bce7903f17c9997f4aa50622ddab83599#IRPT_BCKEND-W2-S7",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_L8_REVIEW_20260911.md (same commit): independent checks and limits",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_VERIFIER_EVIDENCE_20260911.json (same commit)"
    ],
    "remedy": "Connect the real served directory/projection path to the ownership map and the same normalizer, then prove grant-without-projection refusal and a valid narrowed intersection through the actual dispatchers.",
    "owner": "2.0.0_SA_COO~B",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B",
      "round": "v1"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~B",
      "at": null
    }
  },
  {
    "id": "IRPT_BCKEND-W2-S9",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The wrapper’s two firm-id spellings reconcile in S15’s controlled cases, while actual routes remain unguarded. The reason this was armed persists in normal dispatch.",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md@af59a48bce7903f17c9997f4aa50622ddab83599#IRPT_BCKEND-W2-S9",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_L8_REVIEW_20260911.md (same commit): independent checks and limits",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_VERIFIER_EVIDENCE_20260911.json (same commit)"
    ],
    "remedy": "Use the verified FirmBinding on actual handlers and test both a reconciling and non-reconciling spelling pair without accepting request-controlled firm identity.",
    "owner": "2.0.0_SA_COO~B",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B",
      "round": "v1"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~B",
      "at": null
    }
  },
  {
    "id": "IRPT_BCKEND-W2-S10",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "directory/handler.py’s exception return still concatenates str(exc)[:200] despite its comment promising no names or keys. Redacting the authorization harness does not redact this catch path.",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md@af59a48bce7903f17c9997f4aa50622ddab83599#IRPT_BCKEND-W2-S10",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_L8_REVIEW_20260911.md (same commit): independent checks and limits",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_VERIFIER_EVIDENCE_20260911.json (same commit)"
    ],
    "remedy": "Replace untrusted exception-value echoes with a public reason and a safe correlation id in every reachable directory error path; inject client-name, email and key-bearing exceptions as negative controls.",
    "owner": "2.0.0_SA_COO~B",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B",
      "round": "v1"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~B",
      "at": null
    }
  },
  {
    "id": "IRPT_BCKEND-W2-S11",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The namespaced holdings id still includes its raw upstream suffix; prefixing is not obfuscation and does not implement the shared opaque-id contract.",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md@af59a48bce7903f17c9997f4aa50622ddab83599#IRPT_BCKEND-W2-S11",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_L8_REVIEW_20260911.md (same commit): independent checks and limits",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_VERIFIER_EVIDENCE_20260911.json (same commit)"
    ],
    "remedy": "Replace raw-suffix ids with the agreed opaque transformation and prove same-firm joins, cross-firm separation and absence of upstream identifiers in keys and client-facing payloads.",
    "owner": "2.0.0_SA_COO~B",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B",
      "round": "v1"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~B",
      "at": null
    }
  },
  {
    "id": "IRPT_BCKEND-W2-S12",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "The initial stop honored the bound. S23 supplied both sign-off halves; terminal S15-AC1 records the permitted two-resource plan, 27 to 28 behaviors with old order preserved, unchanged WAF Rules, converged distribution and SPA-to-401 difference.",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md@af59a48bce7903f17c9997f4aa50622ddab83599#IRPT_BCKEND-W2-S12",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_L8_REVIEW_20260911.md (same commit): independent checks and limits",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_VERIFIER_EVIDENCE_20260911.json (same commit)"
    ],
    "remedy": "Retain the narrow one-apply ruling and before/after record. The provider’s recurring empty-string/null read normalization belongs to the portal-auth owner; it is not authorization for future WAF churn.",
    "owner": "2.0.0_SA_COO~B",
    "round": "v1",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~B",
      "round": "v1"
    },
    "closed": true
  },
  {
    "id": "IRPT_BCKEND-W3-S1",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The session-library proof uses a fake browser surface. It tests the library protocol, not login or the already-proven cloud chain mandated by later PRD vintages.",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md@af59a48bce7903f17c9997f4aa50622ddab83599#IRPT_BCKEND-W3-S1",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_L8_REVIEW_20260911.md (same commit): independent checks and limits",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_VERIFIER_EVIDENCE_20260911.json (same commit)"
    ],
    "remedy": "At the next cut use the current PRD’s fixed cloud-chain mechanism; distinguish recorded state replay from an actual browser/runtime measurement and preserve the no-new-live-vendor-call boundary.",
    "owner": "2.0.0_SA_COO~B",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B",
      "round": "v1"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "0.9.0_WK_IRPT_BCKEND~3 -- DISARMED SAME TURN by naming the limit in the three places a reader will actually be standing: tests/replay_browser.js's header ('it is NOT Chromium'), infra/aws/ec2/investor-reporting-ycharts/README.md section 'What the offline proof cannot show', and the S8-AC3 judgment record in the proof-of-spec instance, which 3.0.0_SA_CVO grades at L9. The residual -- exercising the library in a real browser against the real site -- is the QUALIFIED LIVE ARM and belongs to 1.0.0_SA_CTO's L10 read on Andrew's per-use word, not to this order.",
      "at": null
    }
  },
  {
    "id": "IRPT_BCKEND-W3-S2",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The login flow is modeled, with no captured real login in this cell’s evidence. Calling it replay does not make it a captured session.",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md@af59a48bce7903f17c9997f4aa50622ddab83599#IRPT_BCKEND-W3-S2",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_L8_REVIEW_20260911.md (same commit): independent checks and limits",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_VERIFIER_EVIDENCE_20260911.json (same commit)"
    ],
    "remedy": "Replace the modeled-login completion claim with explicitly bounded evidence of the admitted existing cloud chain; any credentialed capture must use its authorized operator path and not expand this round’s permissions.",
    "owner": "2.0.0_SA_COO~B",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B",
      "round": "v1"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "0.9.0_WK_IRPT_BCKEND~3 -- DISARMED SAME TURN by (i) writing the measured-versus-modelled split line by line into tests/replay_ycharts.js's header and into tests/fixtures/har_derived_routes.json's _meta.not_present field, which says 'NO LOGIN FLOW' in the fixture the replay actually loads; (ii) making acquireSession fail EXPLICITLY rather than silently when its selectors do not match ('sign-in form present but its fields are not addressable'), so a wrong selector on the live site is a named failure and not a hang; (iii) carrying it into the S8-AC3 judgment for 3.0.0_SA_CVO at L9. Closing it needs a capture of an actual YCharts sign-in, which is a LIVE VENDOR CALL and belongs to Andrew's per-use word via 1.0.0_SA_CTO at L10.",
      "at": null
    }
  },
  {
    "id": "IRPT_BCKEND-W3-S3",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "Per-firm execution-role names exist as trust-only policy entries but no running function can assume them. A policy destination field does not establish runtime isolation.",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md@af59a48bce7903f17c9997f4aa50622ddab83599#IRPT_BCKEND-W3-S3",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_L8_REVIEW_20260911.md (same commit): independent checks and limits",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_VERIFIER_EVIDENCE_20260911.json (same commit)"
    ],
    "remedy": "Make execution-role destinations actionable under the owning infrastructure lane, or remove the false implementation claim; prove role assumption, permitted firm resource access and a cross-firm denial on actual IAM boundaries.",
    "owner": "2.0.0_SA_COO~B",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B",
      "round": "v1"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "0.9.0_WK_IRPT_BCKEND~3 for THIS cell -- DISARMED SAME TURN by not using the per-firm roles at all, by narrowing the poller's grant to the intake prefix family, and by writing the reason into infra/aws/terraform/investor-reporting/intake/iam.tf where the next reader of that grant stands. The FIELD's meaning is not this lane's to settle: whether `execution_role` is aspirational (a later per-firm fleet), or the trust policy should admit the roles that will actually run, belongs to IB-s-5's owner and to 3.0.0_SA_CVO at L9. It is ARMED because the next cell that reads `execution_role` and builds toward assuming it will discover this at apply time, not at design time.",
      "at": null
    }
  },
  {
    "id": "IRPT_BCKEND-W3-S5",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The missing route-file fallback was supplied. The terminal replay now counts eleven actual handler-bearing routes, identifies six unguarded, and excludes the explicitly enumerated unimplemented holdings route.",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md@af59a48bce7903f17c9997f4aa50622ddab83599#IRPT_BCKEND-W3-S5",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_L8_REVIEW_20260911.md (same commit): independent checks and limits",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_VERIFIER_EVIDENCE_20260911.json (same commit)"
    ],
    "remedy": "Preserve the real-file census and its failing control. A functioning detector closes this item even though the defects it detects remain open under W1-S10.",
    "owner": "2.0.0_SA_COO~B",
    "round": "v1",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~B",
      "round": "v1"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "0.9.0_WK_IRPT_BCKEND~3 for THIS cell -- DISARMED SAME TURN by refusing the vacuous reading: the 0-of-0 census is PRINTED AS VACUOUS in the battery output and is paired with two controls that make the censor's behaviour measurable, and the route-reachability of this cell's nine public callables is censused at 0. THE FALLBACK ITSELF is the issuer's: 2.0.0_SA_COO~B wrote the (amend) arm and names the artifact, so whether `routes.json` is a planned artifact of IB-sb-3's replay, a different name, or a mistake is the issuer's to say, with 3.0.0_SA_CVO grading the arm at L9. ARMED because every LATER cell that ships no handler inherits the same unsatisfiable fallback and may quietly report a vacuous pass instead.",
      "at": "2026-09-11T10:56:02Z"
    }
  },
  {
    "id": "IRPT_BCKEND-W3-S10",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "Two real vendor documents encode the fi ligature at different subset codes (45/46); assuming a universal glyph map corrupts extracted labels. The measured PDF population spans 89 pages.",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md@af59a48bce7903f17c9997f4aa50622ddab83599#IRPT_BCKEND-W3-S10",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_L8_REVIEW_20260911.md (same commit): independent checks and limits",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_VERIFIER_EVIDENCE_20260911.json (same commit)"
    ],
    "remedy": "Recover text through each document’s actual font mapping or mark it unresolved; test both observed codes plus a negative unmapped glyph, without guessing a global replacement.",
    "owner": "2.0.0_SA_COO~B",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B",
      "round": "v1"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "0.9.0_WK_IRPT_BCKEND~3 for THIS cell -- DISARMED SAME TURN: extract.py refuses any numeric token carrying a cid (parse_number -> UNDECODED_GLYPH_IN_TOKEN), certify.py refuses to certify a value whose text at the recorded coordinates carries one (UNDECODED_GLYPH_AT_COORDINATES), and disclosure text substitutes a VISIBLE '[?]' marker rather than a guessed letter. WHAT IS NOT MINE: whether served disclosure text is acceptable with a marker in it, or needs a font-aware extraction path (a ToUnicode CMap read, which pdfplumber exposes but this cell does not build), is a product decision for 1.0.0_SA_CTO at L10 with 3.0.0_SA_CVO grading the finding at L9. IB-s-14 (export bundle) and IB-s-15 serve text and inherit this.",
      "at": null
    }
  },
  {
    "id": "IRPT_BCKEND-W3-S11",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The schema requires section dates which the vendor pages do not always state. Use the measured counts: Comparison has 34 undated plus 47 dated sections; MultiComp has 51 undated plus 57 dated. Do not inherit the row’s inconsistent 57-Comparison shorthand.",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md@af59a48bce7903f17c9997f4aa50622ddab83599#IRPT_BCKEND-W3-S11",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_L8_REVIEW_20260911.md (same commit): independent checks and limits",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_VERIFIER_EVIDENCE_20260911.json (same commit)"
    ],
    "remedy": "Represent unsupported/absent section dates explicitly with their document provenance, or quarantine those sections. Prove dated and undated holdouts; never infer an authoritative date from a neighboring section.",
    "owner": "2.0.0_SA_COO~B",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B",
      "round": "v1"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "0.9.0_WK_IRPT_BCKEND~3 for THIS cell's OUTPUT -- DISARMED SAME TURN by emitting only dated rows and reporting undated_rows() with its count, reason and field names, so nothing is dated that the document does not date and nothing is dropped silently. THE CONTRACT ITSELF is not mine: AnalysisReport.schema.json is in _contracts/ and not in this order's <paths>. Whether the section item gains a `date_claim` field (PAGE_STATED / REPORT_STATED / NOT_STATED, which would let an undated section be carried honestly), or as_of_date becomes optional, or the holdout stands, is 1.0.0_SA_CTO's at L10 on the CONTRACTS table, with 3.0.0_SA_CVO grading at L9. IB-s-14 and IB-sb-3 consume this array and inherit the holdout.",
      "at": null
    }
  },
  {
    "id": "IRPT_BCKEND-W3-S12",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The S3 key-segment validator admits a display name and email as path components despite claiming opaque tokens only. Character sanitation is not a semantic identifier check.",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md@af59a48bce7903f17c9997f4aa50622ddab83599#IRPT_BCKEND-W3-S12",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_L8_REVIEW_20260911.md (same commit): independent checks and limits",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_VERIFIER_EVIDENCE_20260911.json (same commit)"
    ],
    "remedy": "Require typed, issued opaque identifiers at each key-builder boundary and reject the recorded name/email controls. Verify all key constructors, not just one filename sanitizer.",
    "owner": "2.0.0_SA_COO~B",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B",
      "round": "v1"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~B to route and IB-s-17's assignee to repair -- `_keys` is NOT in this order's <paths> and the issuer has already placed the module's sanitised-exception item on IB-s-17's round-2 surface, so this belongs in the same place. NOT DISARMED ESTATE-WIDE by anything this cell did. What IS disarmed is this cell's own use: extract.sections_artifact_key() shape-checks its variable segment against a POSITIVE allowlist before calling s3_evidence_key, refuses with KEY_REFUSED naming the PARAMETER and never the value, and battery_ib_s_10.py MEASURES that _keys accepts both a display name and an e-mail (printing the key SHAPE with the value redacted) so the guard is shown to be load-bearing rather than decorative. 3.0.0_SA_CVO grades the finding at L9; 1.0.0_SA_CTO holds the cross-firm/PII surface at L10.",
      "at": null
    }
  },
  {
    "id": "IRPT_BCKEND-W4-S9",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The deployed export worker advertises renderer absence, has no cloud PDF renderer and lacks the corresponding object/KMS grants. Local Chromium PDF success cannot produce a served export.",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md@af59a48bce7903f17c9997f4aa50622ddab83599#IRPT_BCKEND-W4-S9",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_L8_REVIEW_20260911.md (same commit): independent checks and limits",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_VERIFIER_EVIDENCE_20260911.json (same commit)"
    ],
    "remedy": "Build the admitted cloud renderer using the actual frontend RenderPackage, install its runtime dependencies and narrowly scoped artifact access, then prove submit-to-ready-to-download on the served service with stored-object hash equality.",
    "owner": "2.0.0_SA_COO~B",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B",
      "round": "v1"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~B -- the headless runtime is a build decision (a container image, a browser layer, or an out-of-Lambda worker) and every candidate is outside this order's <paths>; a later cell owns it, and the S14 arms that would have to be re-run at that point are named in the S14-AC3 judgment",
      "at": null
    }
  },
  {
    "id": "IRPT_BCKEND-W4-S10",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The shared layer contains two of the five contracts required by the deployed consumers; ExportBundle, RenderPackage and ExportReceipt are absent for export.",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md@af59a48bce7903f17c9997f4aa50622ddab83599#IRPT_BCKEND-W4-S10",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_L8_REVIEW_20260911.md (same commit): independent checks and limits",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_VERIFIER_EVIDENCE_20260911.json (same commit)"
    ],
    "remedy": "Package and version all required export contracts in the actual deployed layer, validate import/read inside the target runtime and prove the consumer uses those same bytes.",
    "owner": "2.0.0_SA_COO~B",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B",
      "round": "v1"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~B -- one line in the layer's CONTRACTS tuple (build_layer.py) plus a rebuild and a re-apply of the performance root; both surfaces belong to IB-s-13's paths, not this order's. Every later cell whose deployed function validates an export contract inherits the same UNAVAILABLE until it lands",
      "at": null
    }
  },
  {
    "id": "IRPT_BCKEND-W4-S12",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "export_id_for hashes bundle plus artifact bytes, while Chromium creation metadata changes artifact bytes on identical-input retry. Bundle/content hashes match but raw hashes and export ids differ.",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md@af59a48bce7903f17c9997f4aa50622ddab83599#IRPT_BCKEND-W4-S12",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_L8_REVIEW_20260911.md (same commit): independent checks and limits",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_VERIFIER_EVIDENCE_20260911.json (same commit)"
    ],
    "remedy": "Use a stable logical request identity based on the immutable bundle/version plus an explicit attempt/artifact identity. Prove identical-input retry reuses the logical export while changed input does not.",
    "owner": "2.0.0_SA_COO~B",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B",
      "round": "v1"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~B -- whether a retry REUSES the prior receipt (keyed on bundle_sha256) or mints a new one is a product decision, not a rendering one, and it belongs to the cell that owns the job table (IB-s-17's surface). Until it is taken, a consumer keying on export_id accumulates duplicates",
      "at": null
    }
  },
  {
    "id": "IRPT_BCKEND-W4-S13",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The battery wrote four synthetic PDFs into a real firm’s evidence namespace under GENIBS14SYN. Metadata marks them synthetic, but a reader that ignores metadata can still encounter them through the ordinary layout.",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md@af59a48bce7903f17c9997f4aa50622ddab83599#IRPT_BCKEND-W4-S13",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_L8_REVIEW_20260911.md (same commit): independent checks and limits",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_VERIFIER_EVIDENCE_20260911.json (same commit)"
    ],
    "remedy": "Have the evidence-surface owner inventory these exact four keys and either segregate them or prove ordinary production readers exclude them. Preserve source labels and audit receipts; any cleanup is a separately authorized owner act, not a CVO deletion.",
    "owner": "2.0.0_SA_COO~B",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B",
      "round": "v1"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~B -- four objects under one unmistakable generation id; delete or relocate them before any consumer reads the generations prefix as client evidence. This worker does not delete them because arm (g) and arm (v0.11) are graded on them being there",
      "at": null
    }
  },
  {
    "id": "IRPT_BCKEND-C-S72",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "Eleven frontend operations all POST to slug paths; zero match the eleven declared backend method/path pairs. Ten of ten same-named frontend success payloads fail backend schemas while eleven of eleven backend control instances pass. RenderPackage has no same-named consumer JSON pair. This isolates a contract seam, not ten independently broken widgets.",
    "evidence": [
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_VERIFIER_EVIDENCE_20260911.json (same commit)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_L8_REVIEW_20260911.md (same commit)",
      "portal/src/api/endpoints/investor-reporting.ts@0322a04a4d144db9bf3211eca5c1bcd05f8099b9",
      "infra/aws/terraform/investor-reporting/api/routes.json@bef9b459f3962b228f6ac032c9c4cae5cb90efcc",
      "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~1/IRPT_BCKEND.TO-IB-s-18.the-foundation-contracts-homes-manifest-roots.proof_of_spec.json@c4214773c9d84fa11f5641d3a28f9f503e784692",
      "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/IRPT_FNTEND.TO-FE-s-1.contracts-client-adapter-fixtures.proof_of_spec.json@314f8e1259ed0cbdf1238b8ce81cb42151dd0c5f"
    ],
    "remedy": "Publish one agreed method/path/request/response/version contract and exercise it from the real LiveClient through actual backend dispatch. Keep producer and consumer positive controls plus mismatched-version and wrong-firm negatives; do not merely translate casing without agreeing economic meaning.",
    "owner": "2.0.0_SA_COO~B",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B",
      "round": "v1"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~B",
      "at": null
    }
  },
  {
    "id": "IRPT_BCKEND-C-S73",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "directory/refresh.py lambda_handler invokes refresh_firm with build_fn=None, which returns REFRESH_FAILED and build_dispatch NOT_WIRED. The gold first mint remains absent in its recorded artifact probe, and routes.json enumerates holdings with NO-HANDLER-AT-HEAD. An enabled accounting schedule is not a data build or a served holdings endpoint.",
    "evidence": [
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_VERIFIER_EVIDENCE_20260911.json (same commit)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_L8_REVIEW_20260911.md (same commit)",
      "infra/aws/lambda/investor-reporting/directory/refresh.py@24f6c0e88a79b89becac8f8d848a822785d2c0ee",
      "infra/aws/terraform/investor-reporting/api/routes.json@bef9b459f3962b228f6ac032c9c4cae5cb90efcc",
      "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~2/IRPT_BCKEND.TO-IB-s-4.directory-freshness-driven-on-a-controlled-clock.proof_of_spec.json@ccd36eb434dd171f56bac202f28c2eaaa3af13e3"
    ],
    "remedy": "After the separate deployment owner admits the first mint, connect actual compute to refresh and serve the holdings output through the declared authenticated route. Prove source completion, new revision, expiry and missed-trigger behavior with before/after artifacts for all three client firms.",
    "owner": "2.0.0_SA_COO~B",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B",
      "round": "v1"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~B",
      "at": null
    }
  },
  {
    "id": "IRPT_BCKEND-C-S74",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "intake/parse.py maps generic market value/value/amount/dollars headers directly to USD. Its fixture manifest excludes non-USD, multi-sheet and subtotal shapes; S7-AC2 acknowledges they may parse rather than refuse. The parser has no demonstrated non-USD safety control.",
    "evidence": [
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_VERIFIER_EVIDENCE_20260911.json (same commit)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_L8_REVIEW_20260911.md (same commit)",
      "infra/aws/lambda/investor-reporting/intake/parse.py@5708161e8ebc825e52798656dc9201cb4d3ca95e",
      "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~3/IRPT_BCKEND.TO-IB-s-7.holdings-parse-validate-and-the-correction-state.proof_of_spec.json@9d6aab3855611cfd9125ea1b849bf2983bb96d44"
    ],
    "remedy": "Add explicit supported currency and unit validation with non-USD, subtotal, multi-sheet and ambiguous-total controls. Quarantine unsupported inputs instead of silently relabeling economic values; preserve human correction provenance.",
    "owner": "2.0.0_SA_COO~B",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B",
      "round": "v1"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~B",
      "at": null
    }
  },
  {
    "id": "IRPT_BCKEND-C-S75",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "S12-AC2 reports three attribution risks with zero proving fixtures and multiple source clocks collapsed to one field. The contract alone cannot establish target-versus-observed, missing-attribution conservation or source-date fidelity.",
    "evidence": [
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_VERIFIER_EVIDENCE_20260911.json (same commit)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_L8_REVIEW_20260911.md (same commit)",
      "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~1/IRPT_BCKEND.TO-IB-s-12.holdings-snapshot-three-partner-joins-reconciled.proof_of_spec.json@2c67545daf449937b75cd6cea001c62d5d1134cb"
    ],
    "remedy": "Add actual/assigned/target and missing-attribution holdouts for each relevant firm source, preserve signed custody totals without redistribution, and carry distinct source clocks rather than selecting one silently.",
    "owner": "2.0.0_SA_COO~B",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B",
      "round": "v1"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-C-S76",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "S14-AC3 explicitly records fixture HTML substitution rather than actual React RenderPackage execution, absent durable bundle storage and receipt provenance gaps. A local PDF hash equality check therefore does not prove same-template preview/export or reproducible served export.",
    "evidence": [
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_VERIFIER_EVIDENCE_20260911.json (same commit)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_L8_REVIEW_20260911.md (same commit)",
      "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~4/IRPT_BCKEND.TO-IB-s-14.export-bundle-freeze-render-worker-receipt.proof_of_spec.json@43331be3f1f432f53c5c10557b6110b0978317c1",
      "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~2/IRPT_FNTEND.TO-FE-s-4.render-package-templates-print.proof_of_spec.json@73752f923887e071c8dc9dcf1d06306f80098257"
    ],
    "remedy": "Run the actual versioned frontend RenderPackage in the admitted renderer, persist the frozen ExportBundle with its references/assets/disclosures before render, and prove preview/render/retry identity plus unsupported-version refusal and receipt/download provenance.",
    "owner": "2.0.0_SA_COO~B",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B",
      "round": "v1"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~B",
      "at": null
    }
  },
  {
    "id": "IRPT_BCKEND-C-S77",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "S15-AC3 still says no apply and a three-resource held plan while S15-AC1 in the same terminal instance records the later narrow successful apply. The manual grade is FAIL despite the structurally VALID instance.",
    "evidence": [
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_VERIFIER_EVIDENCE_20260911.json (same commit)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_L8_REVIEW_20260911.md (same commit)",
      "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~2/IRPT_BCKEND.TO-IB-s-15.scoped-routes-opal-principal-and-the-cloudfront-behavior.proof_of_spec.json@a7659fa6affc70c6cb052f3347312c1fa5b5efd9"
    ],
    "remedy": "Reissue the manual record at the actual apply vintage, distinguishing intended CloudFront behavior, classified WAF normalization and observed refusal plane; retain the historic stop as history rather than current state.",
    "owner": "2.0.0_SA_COO~B",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B",
      "round": "v1"
    },
    "closed": false
  }
]
```

## Round 2 -- remediation plane

```json
{
 "id": "IRPT_BCKEND-S28",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "The decomposition's literal 'sha_metadata_key: script-sha256' for BOTH bundle members collides inside build_bundle_payload and silently drops one member's sha; implemented literally it produces a stamp that verifies one file while reading as though it covered both.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-S28",
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v2.md row IRPT_BCKEND-C-S91"
 ],
 "remedy": "As the row's own disarm_owner field states it: 2.0.0_SA_COO~B (owns the decomposition text); 1.0.0_SA_CTO gates .tools",
 "owner": "2.0.0_SA_COO~B",
 "round": "v2",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~B",
  "round": "v2"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "2.0.0_SA_COO~B",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-S29",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "The guard's own self-test suites were ALREADY FAILING before this cell touched anything -- test_code_trees_invariant.py 3 of 18 and test_safe_deploy.py 7 of 14 -- so RT5-AC1(a)'s 'the guard's self-test and .tools/tests/ pass' is not achievable by any act inside this cell's bounds.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-S29",
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v2.md row IRPT_BCKEND-C-S91"
 ],
 "remedy": "As the row's own disarm_owner field states it: 1.0.0_SA_CTO (INFRA.TOOLS gate per safe_deploy_core.py's own header); 0.7.0_AE_CloudOps authored safe-deploy.sh",
 "owner": "1.0.0_SA_CTO",
 "round": "v2",
 "remediation": {
  "state": "OPEN",
  "owner": "1.0.0_SA_CTO",
  "round": "v2"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "1.0.0_SA_CTO",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-S32",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "Both round-1 batteries grade the first-mint by head-object on a LOOSE per-file key, so now that the mint has correctly landed as a BUNDLE they will read ABSENT / DEPLOY LEG BLOCKED -- a FALSE RED that says the opposite of what happened.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-S32",
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v2.md row IRPT_BCKEND-C-S95"
 ],
 "remedy": "Update battery_ib_s_4.py and battery_ib_s_12.py to head-object the BUNDLE rather than the loose per-file keys. Until then any citation of either battery's deploy leg is invalid at HEAD, and a passing re-run is not evidence either. What must NOT happen is re-minting the per-file keys to satisfy a stale battery.",
 "owner": "2.0.0_SA_COO~B",
 "round": "v2",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~B",
  "round": "v2"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "2.0.0_SA_COO~B",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-S41",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "BLOCKING",
 "hazard_standing": "ARMED",
 "mechanism": "THE AUTHORIZED PER-VERSION DELETE WAS NOT TAKEN, AND NOT TAKING IT IS THE ACT. Andrew approved (via 1.0.0_SA_CTO 96041, 'All recs approved') the per-version delete of 'the FOUR noncurrent versions of the FOUR synthetic-export objects named in row W4-S20', with 1.0.0_SA_CTO naming the boundary explicitly: NOT any other version of those four keys beyond the four the row names, and STOP rather than reconcile if the row's four VersionIds do not resolve as expected. The pre-act live read (s3api list-object-versions over the exports/ prefix, denominator 10 versions + 5 delete markers across 5 keys, IsTruncated absent) FALSIFIES THE COUNT THE AUTHORIZATION RESTS ON. The four keys carry NINE noncurrent versions, not four: r1/report.pdf has THREE (wl2x4Z9... named, plus s_LqtLL... and pL4dWRj...), and v0-11-overview, v0-11-comparison and v0-11-multicomp have TWO each (the named one plus HX6MJ2a..., oGHsMqX..., jP5Eyb1...). All four NAMED VersionIds are live and resolve, so the narrow reading of the stop condition is satisfied -- but deleting exactly those four would leave FIVE retrievable versions of the same four synthetic PDFs, and the qualifier this entire call exists to remove ('we cannot say they are gone') WOULD STILL STAND after the irreversible act. An unrecoverable act that does not achieve its stated purpose, taken on a count that is wrong by five, is not a partial success; it",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-S41",
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v2.md row IRPT_BCKEND-C-S91"
 ],
 "remedy": "As the row's own disarm_owner field states it: 1.0.0_SA_CTO -- carry the corrected count back to Andrew: does the approval cover all NINE noncurrent versions of the four keys (the act that actually makes them gone), or exactly the FOUR the row names (leaving five, and the qualifier standing). Until he answers on the CORRECTED number, no version is deleted and 'the four synthetic PDFs are gone' keeps its qualifier",
 "owner": "1.0.0_SA_CTO",
 "round": "v2",
 "remediation": {
  "state": "OPEN",
  "owner": "1.0.0_SA_CTO",
  "round": "v2"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "1.0.0_SA_CTO",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-S44",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "IB-rt-2's EIGHT ROWS DISPOSITIONED, AND THE POST-READ OBLIGATION RE-ROUTED OFF A BATTERY THAT CANNOT FIRE. W2-S30: holdings paths GRANTED additively (holdings/ lambda + the holdings Terraform root) and LOOSENING THE CENSUS REFUSED -- W2-S31 establishes the census grades the __irpt_guarded__ MARK while that handler enforces FirmBinding inline, so it is a MARK gap and not a live cross-firm hole, and an inline enforcement the instrument cannot see should stay VISIBLE; the handler moves under the mark, the instrument does not move. 1.0.0_SA_CTO endorsed that reasoning explicitly. g2: RULED HUMAN-GATED under the face's OWN standing rule, which the CTO confirmed is a rule applied and not a bar lowered, with an instruction not to put it back. W2-S36: RESOLVED by the CTO's L4 amendment, PRD v0.14 @b8e98d5a4d -- business_date is STATE-CONDITIONAL (required on the 5 answer-bearing states, may be ABSENT and never NULL on the 4 no-answer states) rather than nullable, because nullable -- which was THIS SEAT'S option (a) -- would have weakened every envelope including a READY success and traded a validation gap for a semantic hole in the success path. AND MY OWN TWO-WAY CUT WAS SHORT BY TWO: QUEUED and RUNNING carry no business_date by construction and are not refusals at all, so a fix scoped to 'refusals' would have left both failing exactly as before. W2-S32 and W2-S35 discharged by the wo",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-S44",
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v2.md row IRPT_BCKEND-C-S91"
 ],
 "remedy": "As the row's own disarm_owner field states it: 1.0.0_SA_CTO -- (i) confirm or overturn landing the post-read business_date obligation in battery_ib_rt_2.py rather than the IB-s-18 battery; (ii) W4-S29's crash is now LOAD-BEARING, because the same battery is the named enforcement for generated-schema provenance while its generator exists on no device -- two holes in one provenance chain, and the fix belongs to a CLOSED cell so it is routed, never taken here",
 "owner": "1.0.0_SA_CTO",
 "round": "v2",
 "remediation": {
  "state": "OPEN",
  "owner": "1.0.0_SA_CTO",
  "round": "v2"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "1.0.0_SA_CTO",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-S45",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "IB-rt-11 ACCEPTED TERMINAL (8 of 12), AND ITS HEADLINE IS A FALSE GREEN CAUGHT BY ITS OWN AUTHOR AFTER THE FLIP. The worker flipped <status> complete, then found that commit 3c28723d20 pinned parse.py at a version which does NOT carry the load_intake_controls refusal that arm (e)'s NEGATIVE arm proves -- the edit was made after the commit and never committed, so THE ARM PASSED AGAINST THE WORKTREE WHILE THE INSTANCE NAMED BYTES THE RECORD DID NOT CARRY. proof-of-spec-check returned rc=0 and the criterion read PASS-by-output, and BOTH were reading a file the record did not contain. Found by reading git status --porcelain AFTER the flip; re-opened on the record at 3db8d67f17 with the reason on the face, the real refusal committed at 51db4a7d66, re-pinned, re-validated, re-flipped honestly at 7408aa5c5e. The issuer re-graded the instance at HEAD rather than taking the report's word: VALID rc=0, 3 of 3 surprise entries resolving, parse.py CONTENT-resolved at 51db4a7d66 rather than presence-only. TWO MECHANISMS THE CELL PROVED IN PASSING AND BOTH ARE WORTH KEEPING: the owned-paths lane gate REFUSED the parse.py commit the instant the order went terminal ('no NON-TERMINAL task order at HEAD issued_to this serial names this path'), so a worker who flips early CANNOT quietly patch afterwards and the remedy is forced onto the record; and PENDING-THIS-COMMIT is SPENT once the instance is",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-S45",
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v2.md row IRPT_BCKEND-C-S91"
 ],
 "remedy": "As the row's own disarm_owner field states it: 2.0.0_SA_COO~B for W3-S35 and W3-S36 -- both are carried to L10 rather than acted on mid-round: the corrections contract has no time field (a frozen-contract question, same class as W2-S36 which needed an L4 amendment) and parse.py's packaging has no shipping function yet, so neither is fixable inside this round without re-opening a closed surface. W3-S34 is INERT and needs no owner",
 "owner": "2.0.0_SA_COO~B",
 "round": "v2",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~B",
  "round": "v2"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "2.0.0_SA_COO~B",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-S46",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "IB-rt-2 REACHED 15 of 15 ARMS WITH THE TOKEN PRINTING AND DID NOT FLIP, AND BOTH HALVES OF THAT ARE CORRECT. W2-S41 IS THE ISSUER'S DEFECT AND IS FIXED: amendment 3's C1 granted infra/aws/lambda/investor-reporting/holdings/ in a PROSE SENTENCE and never added it to the <paths> BLOCK, which is the surface the owned-paths lane gate actually reads, so the gate refused four files of finished work and THE GATE WAS RIGHT. Two lines added to <paths> at a3e84db9ef, verified present at the worker's own HEAD after its worktree was fast-forwarded to f27b6f4cc3 with its four uncommitted files confirmed intact before and after. A GRANT IS ONLY REAL IN THE SURFACE THE ENFORCER READS -- and this is the INVERSE of the failure /canonical-flow already warns about, where a DOCTRINE line routed an act through a seat the gate did not require and the cost was an invisible WAIT; here a doctrine line GRANTED what the gate does not read and the cost was an invisible REFUSAL. Same root, opposite direction: prose is not a grant and prose is not a gate. AND THE WORKER'S REFUSAL TO FLIP ON A PASSING TOKEN IS A FINDING IN ITS OWN RIGHT: the <paths> grant is LIVE ONLY WHILE THE ORDER IS NON-TERMINAL, so flipping would have RETIRED the grant and permanently orphaned C1's work -- A TERMINAL FLIP REVOKES THE GRANTS THE ORDER CARRIES, so the flip is the LAST act and never the act that frees you to finish. No fac",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-S46",
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v2.md row IRPT_BCKEND-C-S91"
 ],
 "remedy": "As the row's own disarm_owner field states it: 0.9.0_WK_IRPT_BCKEND~2 under issuer amendment 5 -- the single deploy disarms W2-S39 on the six live functions and lands C1, the v0.14 envelope work, the post-read business_date emission and the named rider. Until that apply verifies, W2-S39 stays ARMED in the world and this row stays ARMED with it -- ITS NAMED OWNER IS A TERMINATED WORKER SLOT, so the act needs a live seat; the carve-out in its own owner text is the subject, not the part it claims it disarmed.",
 "owner": "1.0.0_SA_CTO",
 "round": "v2",
 "remediation": {
  "state": "OPEN",
  "owner": "1.0.0_SA_CTO",
  "round": "v2"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "1.0.0_SA_CTO",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-S47",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "IB-rt-9 ACCEPTED TERMINAL AT 6 OF 6 ARMS -- round 2 is 9 of 12, IB-rt-2 the only order still open. Issuer verification at HEAD rather than on the report: proof-of-spec-check VALID rc=0, 8 of 8 artifact rows resolved at pin with 4 CONTENT-resolved, 10 of 10 surprise rows resolving; and the arm (e) ledger's sentinel read ABSENT from org/critical_paths/.open_deploys/ so NEVER-2's half-landed state does not exist. ARM (e) IS THE STRONGEST WORK IN THE ROUND ON METHOD. It used `import` + `state rm` INSTEAD of `state mv`, because across two S3-backed states a `state mv` means hand-editing two pulled state files and a hand-edited state has no undo -- choosing the recoverable instrument over the convenient one. And it read non-destruction WITH A DIFFERENT INSTRUMENT THAN THE ONE THAT DID THE WORK: `describe-secret` and `describe-log-groups` both still return the objects, because `state rm` reporting 'Removed' is TERRAFORM DESCRIBING ITSELF and not the world. The only world change in the whole arm is tags_all gaining Project = OpalPortal on two resources, with Owner and Purpose carried verbatim. AND IT RE-OPENED AFTER ITS OWN FIRST FLIP, FOR THE MIRROR-IMAGE REASON TO IB-rt-11's: arm (e) took its baseline from HEAD~2, a RELATIVE ref that meant the pre-deletion commit when it was written and something else two commits later, so a fresh run read 'down from 0' and FAILED while the world was",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-S47",
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v2.md row IRPT_BCKEND-C-S91"
 ],
 "remedy": "As the row's own disarm_owner field states it: 1.0.0_SA_CTO at L10 for the two items outside this lane: (i) W3-S38's orphaned S3 state object, which needs Andrew's word if it is ever to be deleted and is deliberately NOT being asked for tonight; (ii) the live ycharts-session-probe still running the RETIRED non-403 predicate on an ENABLED 6-hourly rule, because redeploying it needs infra/aws/terraform/ycharts-pipeline/ which NO order granted -- so SessionFresh=1 remains not evidence of anything and is cited nowhere in the cell",
 "owner": "1.0.0_SA_CTO",
 "round": "v2",
 "remediation": {
  "state": "OPEN",
  "owner": "1.0.0_SA_CTO",
  "round": "v2"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "1.0.0_SA_CTO",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-S49",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "IB-rt-6's FOUR ROWS DISPOSITIONED AND ITS BLOCKER CLEARED -- it was a <paths> GAP, NOT A LANE REFUSAL. W2-S44: the runner cannot import on the host (ModuleNotFoundError: No module named 'ids', measured ON the host rather than inferred, with boto3/pandas/jsonschema and trading_calendar all resolving). The worker reported the remedy as out of lane because the member list is hardcoded in .tools/safe_deploy_core.py. MEASURED at .owned-paths.yaml:2003-2009: .tools/** IS LANE ANY, and the only narrower entries under .tools/ are git-hooks/**, tests/**, surprise-row-gate.py and to-pipeline-gate.py, none matching -- so that file was NEVER OUT OF LANE, only out of THIS ORDER'S <paths>, which is a different thing and is the issuer's to grant. GRANTED IN THE BLOCK (.tools/safe_deploy_core.py) and deliberately not in prose, because granting holdings/ to IB-rt-2 in a prose sentence the gate cannot read cost that order a blocked commit on four finished files. AND THE SUBSTANTIVE RULING: declaring ids.py as a BUNDLE MEMBER resolved from _ids/ids.py at build time is a DISTRIBUTION, NOT A SECOND DEFINITION -- the worker had half of it right, since a FILE COPY into the bundle dir would indeed be a second copy of the one opaque-id normalizer which irpt-holdings' BUILD_MANIFEST forbids in those words, but a declaration resolved from the single source is the same mechanism lambda-source-map.json alr",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-S49",
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v2.md row IRPT_BCKEND-C-S91"
 ],
 "remedy": "As the row's own disarm_owner field states it: 0.9.0_WK_IRPT_BCKEND~2 under amendment H -- W2-S45 is the armed item and the only one needing no external dependency: refresh.py calls the manifest 'the ONLY memory this cell has between fires' while containing 0 hits across 1 file for put_object|boto3|s3, last_manifest_as_of's single caller is a TEST so the MISSED-trigger detector is UNREACHABLE IN PRODUCTION, _refresh/ is empty in all three buckets though the function has run, and the IAM grants a write no code performs. Until that is built, the cell's central claim is false -- ITS NAMED OWNER IS A TERMINATED WORKER SLOT, so the act needs a live seat; the carve-out in its own owner text is the subject, not the part it claims it disarmed.",
 "owner": "1.0.0_SA_CTO",
 "round": "v2",
 "remediation": {
  "state": "OPEN",
  "owner": "1.0.0_SA_CTO",
  "round": "v2"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "1.0.0_SA_CTO",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-S50",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "BLOCKING",
 "hazard_standing": "ARMED",
 "mechanism": "IB-rt-6 WORKED TO ITS WALL AND STAYS OPEN: 14 of 17 graded checks PASS, 0 FAIL, 3 BLOCKED, status untouched at pending. Amendment H's grant WORKED and the worker proved it with a negative control -- the host now reads 'IMPORT-OK first-party modules resolved: trading_calendar, ids, contract' where the SAME script printed IMPORT-FAIL two mints earlier, so declaring ids.py as a bundle member resolved from _ids/ was the right remedy and was not a second definition. THE REMAINING BLOCKER IS AN IAM CHANGE ON A SHARED HOST ROLE AND I AM ROUTING IT, NOT GRANTING IT. mdpf-daily-runner-ec2-role is AccessDenied on 5 of 9 prefixes directory_runner.py reads and on 3 of 3 firm DESTINATION prefixes, measured FROM the host BY the host with a positive control in the same sweep. Rule 27 says no lane enumerates a worker, so this order's <paths> block would technically suffice to grant it -- BUT infra/aws/** is lane CLOUD_OPS_OR_ETL ('AE 0.5/0.6/0.6.1/0.7 only'), the role is a SHARED scheduled-gold host role carrying ANOTHER PROJECT'S PRODUCTION CHAIN, and an IAM widening there sits outside this project's blast radius. A path grant I have the mechanical power to write is not the same as an act this project should take. ROUTED to 1.0.0_SA_CTO for AE assignment, and flagged HIGH because it gates SIX OF TEN OUTCOMES: rt-6 itself owns FWD-7 and contributes FWD-1, and IB-rtb-1 sits behind rt-6 on a rea",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-S50",
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v2.md row IRPT_BCKEND-C-S91"
 ],
 "remedy": "As the row's own disarm_owner field states it: 1.0.0_SA_CTO -- route the mdpf-daily-runner-ec2-role IAM widening to an AE lane (infra/aws/** is CLOUD_OPS_OR_ETL). Until it lands, IB-rt-6 cannot close, IB-rtb-1 cannot start, and six of ten FWD outcomes stay ungradeable. This seat is NOT granting a worker write access to another pipeline's shared host role",
 "owner": "1.0.0_SA_CTO",
 "round": "v2",
 "remediation": {
  "state": "OPEN",
  "owner": "1.0.0_SA_CTO",
  "round": "v2"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "1.0.0_SA_CTO",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-S51",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "CROSS-PROJECT ROUTING from IRPT_FNTEND by 1.0.0_SA_CTO, a day late. (1) The producer side of the smoke-map seam is RED: _contracts/tests/test_seam_paired.py reads 14 failed, 39 passed. (2) The producer's copy of the StatusEnvelope contract never received the v0.14 amendment the consumer's copy carries.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-S51",
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v2.md row IRPT_BCKEND-C-S91"
 ],
 "remedy": "As the row's own disarm_owner field states it: 1.0.0_SA_CTO -- routing both items into IRPT_BCKEND's next L4 amendment packet: re-base the paired test to the v1 declared paths and the grown route table, and regenerate the producer's contract copies from the v0.14 source. The remedy cells are 2.0.0_SA_COO~B's to cut once that L4 lands. DISARMS when both carriers agree and the paired test is green on a named portal commit.",
 "owner": "1.0.0_SA_CTO",
 "round": "v2",
 "remediation": {
  "state": "OPEN",
  "owner": "1.0.0_SA_CTO",
  "round": "v2"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "1.0.0_SA_CTO",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-S56",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "THREE judgment records cite line ranges that were TRUE WHEN WRITTEN and are wrong at HEAD, none carrying a vintage pin -- and one carries a factual reading that a later authorized act made false. A citation ages separately from the text it quotes, and this round produced four instances of it in the evidence the CVO grades from.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-S56",
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v2.md row IRPT_BCKEND-C-S99"
 ],
 "remedy": "A line citation inside a judgment record carries its @<commit>, as the estate's other citation surfaces already require. No correction is owed to the four instances themselves -- this seat re-verified the substance of each and none changes a grade.",
 "owner": "2.0.0_SA_COO~B",
 "round": "v2",
 "remediation": {
  "state": "REMEDIATED",
  "owner": "2.0.0_SA_COO~B",
  "round": "v2"
 },
 "closed": true,
 "disarm": {
  "state": "DISARMED",
  "owner": "2.0.0_SA_COO~B",
  "at": "2026-09-18T17:45Z"
 }
}
```

```json
{
 "id": "IRPT_BCKEND-W1-S11",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "mechanism": "A FOURTH id-shape disagreement, found while moving the id space onto one normalizer (IB-rt-3): `_scope/resolve.py`'s `_OPAQUE_ID_PAT = re.compile(r'^[0-9a-f]{24}$')` -- the shape check `unmatched_reasons` uses to decide whether an ownership id was ever projected -- is a BARE 24-hex pattern, while the directory has always emitted `acc_` + 24 hex. MEASURED against the landed 49financial QA artifact at this cell's cut: 0 of 80 real directory account ids match the pattern. The consequence is NOT an authorization defect -- the check is only reached for an id the directory does NOT hold, so nothing was ever served wrongly and no permitted set was ever widened -- it is a DIAGNOSTIC inversion at exactly the seam row W2-S7 exists to explain: every genuinely-missing REAL id was reported as UNPROJECTED-ID ('you forgot id_projection') when the true reason was NOT-IN-DIRECTORY ('this account is not in this build'). A reason that is confidently wrong sends the reader to the wrong repair, which is worse than no reason at all. The same wrong shape was also WRITTEN DOWN as fact in `_scope/tests/fixtures.py` ('account ids are 24-hex, the shape directory_runner.opaque_id emits'), so every test reading that fixture agreed with the defect and none could see it. CLOSED BY THIS CELL, inside its own <paths>: the shape now comes from `_ids.is_issued('account', ...)` -- the one normalizer -- and the fix",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-W1-S11",
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v2.md row IRPT_BCKEND-C-S90"
 ],
 "remedy": "No remedy is stated on the row. Carried to 1.0.0_SA_CTO's L10 read to be placed or closed; this seat does not invent one.",
 "owner": "1.0.0_SA_CTO",
 "round": "v2",
 "remediation": {
  "state": "OPEN",
  "owner": "1.0.0_SA_CTO",
  "round": "v2"
 },
 "closed": false
}
```

```json
{
 "id": "IRPT_BCKEND-W1-S12",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "BLOCKING",
 "hazard_standing": "ARMED",
 "mechanism": "TWO ROUND-2 CELLS ARE REBUILDING THE SAME SHARED LAYER CONCURRENTLY, and `aws_lambda_layer_version` REPLACES rather than appends, so each publish DESTROYS the other's version. Measured: at this cell's cut `irpt-common` was :2; by the time IB-rt-3 had built its zip the live layer was :4, published 2026-09-11T12:55:55Z (one minute before this cell's ledger opened) by a peer cell adding python/keys.py and the three export contracts (row W4-S10's item), with :1-:3 already deleted. Publishing THIS cell's zip as built would have silently REVERTED that peer's landed deploy -- NEVER-2's half-landed-deploy hazard pointed at a neighbour. AVOIDED, not merely noticed: IB-rt-3 measured the live :4 zip member-by-member, found all four peer members BYTE-EQUAL to blobs already committed in its own ancestry, declared them in build_layer.py as CARRIED_FORWARD_MEMBERS with that measurement cited, and published a UNION -- verified against the live :4 as 0 members regressed, exactly 2 added (python/ids.py, python/raw_keys.json), 0 common members differing. Both consumer functions are on :5 and both roots plan clean. THE REMAINING HAZARD IS THE MERGE, NOT THE BUILD: both cells edited infra/aws/lambda/layers/irpt-common/build_layer.py on separate branches, in the same region of the file, and whoever merges SECOND owns the member declaration -- if the peer's edit lands after this one without carrying ",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-W1-S12",
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v2.md row IRPT_BCKEND-C-S91"
 ],
 "remedy": "As the row's own disarm_owner field states it: 2.0.0_SA_COO~B (the drain owns the build_layer.py merge: the merged file must carry BOTH cells' member declarations -- IDS_MEMBERS and the peer's export-contract/keys members -- and the merged layer must be rebuilt and re-applied ONCE afterwards, with the zip's member list compared against the live version before the apply. Neither worker can see the other's branch, so neither can do this.)",
 "owner": "2.0.0_SA_COO~B",
 "round": "v2",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~B",
  "round": "v2"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "2.0.0_SA_COO~B",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-W1-S14",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "BLOCKING",
 "hazard_standing": "INERT",
 "mechanism": "THE ISSUER AMENDMENT ORDERS A FIRST ACT ON A PATH THIS ORDER'S <paths> GRANT DOES NOT NAME -- AND THE ACT IS ALREADY A NO-OP ON THE RUNTIME, MEASURED. IB-rt-7's amendment (row W4-S15) makes the FIRST ACT a rebuild of `irpt-common` that REMOVES `carried_forward_members` from `infra/aws/lambda/layers/irpt-common/build_layer.py`, publishes a new version, repoints 3 of 3 functions and records the version. That act writes `infra/aws/lambda/layers/irpt-common/{build_layer.py,BUILD_MANIFEST.json}` and `infra/aws/lambda/ci/lambda-layer-map.json`, and the repoint runs terraform in the `performance`, `narrative` and `export` roots -- SEVEN paths, NONE of which appears in this order's <paths> block (which names the holdings and api roots, docs/contracts, the gold runner tree, PATH_MANIFEST.json, change_management, the rt7 sentinel and lambda-source-map.json). Per the standing bound a path the grant lacks is a row, never an override, so this worker did NOT edit build_layer.py. THE AMENDMENT'S OWN ESCAPE CLAUSE APPLIES AND WAS MEASURED RATHER THAN ASSUMED: the LIVE irpt-common:5 already carries 9 of 9 members the MERGED tree declares (5 of 5 contracts, python/ids.py, python/raw_keys.json, python/keys.py, python/firm_registry.json), and all 3 consumer functions (irpt-performance-adapter, irpt-narrative, irpt-export-render) already carry layer:irpt-common:5 -- so there is nothing to repoint a",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-W1-S14",
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v2.md row IRPT_BCKEND-C-S90"
 ],
 "remedy": "As the row's own disarm_owner field states it: 2.0.0_SA_COO~B -- either widen IB-rt-7's <paths> to name infra/aws/lambda/layers/irpt-common/ and infra/aws/lambda/ci/lambda-layer-map.json, or let IB-rt-4 (slot ~3) carry the edit: its own arm (e) already rebuilds this layer from the merged tree and that cell holds the surface. Nothing is ARMED in the meantime -- the deployed plane is correct and byte-for-byte unaffected by the pending edit.",
 "owner": "2.0.0_SA_COO~B",
 "round": "v2",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~B",
  "round": "v2"
 },
 "closed": false
}
```

```json
{
 "id": "IRPT_BCKEND-W1-S16",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "`_authz.Enforcer.covers()` ADMITS ANY ADVISOR ID FOR A FIRM-OPERATIONS OR OPAL VIEWER, INCLUDING ANOTHER FIRM'S -- its own docstring says 'within the verified firm' and the branch does not check the firm. enforce.py:319-320 reads: `if scope[\"principal_class\"] in (\"FIRM_OPERATIONS\", \"OPAL_GLOBAL\"): return True, 'a firm-authorized viewer may address any advisor in its own firm'` -- an unconditional True. MEASURED on the live handler this cell built: the six-swap census against a FIRM_OPERATIONS viewer of 49financial reads 5 of 6 refused, and the one that is NOT refused is `advisor` addressed with an id minted for INFLECTION by the real normalizer. Every other kind (firm, account, relationship, report, pdf) refuses OBJECT_NOT_COVERED. NO DATA CROSSES A FIRM BOUNDARY BECAUSE OF THIS, and that is measured rather than assumed: what the request goes on to be served is the holdings slice projected to the viewer's OWN `permitted_account_set`, which is built from the verified firm's directory and cannot contain another firm's accounts -- so the served bytes are identical to the un-swapped request's. What the branch loses is the ability to REFUSE a cross-firm advisor id, i.e. the audit answer to 'was this request about an advisor of this firm', which is exactly what the docstring promises and the code does not deliver. The same census against a FIRM_ADVISOR viewer reads 6 of 6 refused wit",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-W1-S16",
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v2.md row IRPT_BCKEND-C-S91"
 ],
 "remedy": "As the row's own disarm_owner field states it: 2.0.0_SA_COO~B to route -- `infra/aws/lambda/investor-reporting/_authz/` is IB-s-3's surface and is not in IB-rt-7's <paths> grant, so this worker recorded it rather than editing it. The fix is one comparison: resolve the addressed advisor against the verified firm's own advisor population (the ownership map's keys, which resolve_now already loads) before returning True. ARMED because the branch is reachable from every guarded route an admin principal can call, not only this one.",
 "owner": "2.0.0_SA_COO~B",
 "round": "v2",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~B",
  "round": "v2"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "2.0.0_SA_COO~B",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-W1-S17",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "IB-rt-2's TERMINAL 'arm (e) 7 of 7 VERIFIED' does not reproduce from a fresh worktree at the SAME HEAD -- it reads 3 of 7, and the cause is the verifier's own local layer-zip cache, not the served bytes.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-W1-S17",
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v2.md row IRPT_BCKEND-C-S91"
 ],
 "remedy": "As the row's own disarm_owner field states it: 2.0.0_SA_COO~B",
 "owner": "2.0.0_SA_COO~B",
 "round": "v2",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~B",
  "round": "v2"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "2.0.0_SA_COO~B",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-W1-S18",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "The four synthetic export PDFs IB-sb-3's download arm replayed against are now PERMANENTLY GONE from opal-data-ycharts -- not merely marker-hidden as RT8-g's own record predicted -- and IB-rtb-1's download arm had to substitute a labelled fixture record for the storage boundary.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-W1-S18",
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v2.md row IRPT_BCKEND-C-S91"
 ],
 "remedy": "As the row's own disarm_owner field states it: 2.0.0_SA_COO~B",
 "owner": "2.0.0_SA_COO~B",
 "round": "v2",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~B",
  "round": "v2"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "2.0.0_SA_COO~B",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-W2-S16",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "BLOCKING",
 "hazard_standing": "ARMED",
 "mechanism": "THE PUBLISHED SCHEMAS ARE DOCUMENT CONTRACTS, NOT RESPONSE CONTRACTS: 0 of the 7 operations that reach a response return anything validating against its route's schema in ANY document position; the six handlers emit three different envelopes; and 2 of the 11 schemas can never be an HTTP response at all. RT1-AC1 (b) cannot read 11 of 11 and the remedy is outside this order's <paths>.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-W2-S16",
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v2.md row IRPT_BCKEND-C-S91"
 ],
 "remedy": "As the row's own disarm_owner field states it: 2.0.0_SA_COO~B",
 "owner": "2.0.0_SA_COO~B",
 "round": "v2",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~B",
  "round": "v2"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "2.0.0_SA_COO~B",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-W2-S19",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "BLOCKING",
 "hazard_standing": "ARMED",
 "mechanism": "ARM (a) CANNOT READ `0 of N` IN THIS LANE: three of the eleven handler-bearing routes dispatch to `irpt-status`, whose source dir `infra/aws/lambda/investor-reporting/ops/` and whose Terraform root `infra/aws/terraform/investor-reporting/ops/` are BOTH absent from this order's <paths>. The wrapper cannot be put on a handler this order may not open.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-W2-S19",
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v2.md row IRPT_BCKEND-C-S91"
 ],
 "remedy": "As the row's own disarm_owner field states it: 2.0.0_SA_COO~B",
 "owner": "2.0.0_SA_COO~B",
 "round": "v2",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~B",
  "round": "v2"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "2.0.0_SA_COO~B",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-W2-S21",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "BLOCKING",
 "hazard_standing": "ARMED",
 "mechanism": "TWO SERVED FUNCTIONS CANNOT BE REBUILT FROM COMMITTED SOURCE: irpt-ycharts-generate declares 25 build inputs of which 7 have NEVER existed in this repository, and irpt-status declares 7 of which 5 have not; a third, irpt-directory-search, fails the builder's parity check because two functions share one source dir.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-W2-S21",
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v2.md row IRPT_BCKEND-C-S91"
 ],
 "remedy": "As the row's own disarm_owner field states it: 2.0.0_SA_COO~B",
 "owner": "2.0.0_SA_COO~B",
 "round": "v2",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~B",
  "round": "v2"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "2.0.0_SA_COO~B",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-W2-S22",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "BLOCKING",
 "hazard_standing": "ARMED",
 "mechanism": "TWO CELLS ARE POINTED AT ONE SERVED FUNCTION: the issuer's own hand-off states IB-rt-4 is CONCURRENTLY re-applying its error-path envelope on irpt-export-render from slot ~3, while this order's <paths> grant export/ and its Terraform root to this cell. Two cells applying one function is the half-landed-deploy hazard, not a merge conflict.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-W2-S22",
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v2.md row IRPT_BCKEND-C-S91"
 ],
 "remedy": "As the row's own disarm_owner field states it: 2.0.0_SA_COO~B",
 "owner": "2.0.0_SA_COO~B",
 "round": "v2",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~B",
  "round": "v2"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "2.0.0_SA_COO~B",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-W2-S24",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "BLOCKING",
 "hazard_standing": "ARMED",
 "mechanism": "THE GUARD IS WRITTEN AND HAS NO IN-LANE WAY TO REACH THE FIVE ZIPS: `_authz` is shared source, the estate distributes shared source by the `irpt-common` LAYER, and the layer's source dir, its build script and `lambda-layer-map.json` are all outside this order's <paths> -- while the layer itself was republished as v5 at 13:08Z today by another cell.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-W2-S24",
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v2.md row IRPT_BCKEND-C-S91"
 ],
 "remedy": "As the row's own disarm_owner field states it: 2.0.0_SA_COO~B",
 "owner": "2.0.0_SA_COO~B",
 "round": "v2",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~B",
  "round": "v2"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "2.0.0_SA_COO~B",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-W2-S26",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "mechanism": "THE PUBLISHED OPERATION IDS ARE NOT ADMISSIBLE KEY COMPONENTS: v1 names them with hyphens (`narrative-packet`) and `_keys.OPERATION_RE` is `^[a-z][a-z0-9_]{0,63}$`, so every guarded request was refused KEY_REFUSED at the cache-key step -- a refusal about the caller for a defect that was not theirs.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-W2-S26",
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v2.md row IRPT_BCKEND-C-S90"
 ],
 "remedy": "No remedy is stated on the row. Carried to 1.0.0_SA_CTO's L10 read to be placed or closed; this seat does not invent one.",
 "owner": "1.0.0_SA_CTO",
 "round": "v2",
 "remediation": {
  "state": "OPEN",
  "owner": "1.0.0_SA_CTO",
  "round": "v2"
 },
 "closed": false
}
```

```json
{
 "id": "IRPT_BCKEND-W2-S27",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "mechanism": "A THIRD FIRM ID SPELLING: `performance/tenants.py` routes on `F-49F` / `F-COT` / `F-INF`, which is neither the registry spelling (`49financial`) nor the issued opaque id (`fir_...`), so the performance adapter cannot resolve a route for the firm the boundary binds.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-W2-S27",
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v2.md row IRPT_BCKEND-C-S90"
 ],
 "remedy": "No remedy is stated on the row. Carried to 1.0.0_SA_CTO's L10 read to be placed or closed; this seat does not invent one.",
 "owner": "1.0.0_SA_CTO",
 "round": "v2",
 "remediation": {
  "state": "OPEN",
  "owner": "1.0.0_SA_CTO",
  "round": "v2"
 },
 "closed": false
}
```

```json
{
 "id": "IRPT_BCKEND-W2-S28",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "BLOCKING",
 "hazard_standing": "INERT",
 "mechanism": "THE RENAME ROUTED TO ME CANNOT BE COMPLETED IN LANE: `_authz/dispatch.py`'s ONLY importer is `_contracts/tests/test_seam_paired.py`, and `infra/aws/lambda/investor-reporting/_contracts/` is not in this order's <paths> -- so renaming it would leave a committed test importing a module that no longer exists.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-W2-S28",
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v2.md row IRPT_BCKEND-C-S90"
 ],
 "remedy": "As the row's own disarm_owner field states it: 2.0.0_SA_COO~B",
 "owner": "2.0.0_SA_COO~B",
 "round": "v2",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~B",
  "round": "v2"
 },
 "closed": false
}
```

```json
{
 "id": "IRPT_BCKEND-W2-S30",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "BLOCKING",
 "hazard_standing": "INERT",
 "mechanism": "Arm (a)'s whole-file denominator moved from 11 to 12 while this cell was dead: IB-rt-7's irpt-holdings is now LIVE on its published route, so routes.json resolves 12 handler-bearing routes and the whole-file census reads 1 of 12 unguarded -- and the only remedy paths (holdings/ lambda + terraform) are OUTSIDE this order's <paths>.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-W2-S30",
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v2.md row IRPT_BCKEND-C-S90"
 ],
 "remedy": "No remedy is stated on the row. Carried to 1.0.0_SA_CTO's L10 read to be placed or closed; this seat does not invent one.",
 "owner": "1.0.0_SA_CTO",
 "round": "v2",
 "remediation": {
  "state": "OPEN",
  "owner": "1.0.0_SA_CTO",
  "round": "v2"
 },
 "closed": false
}
```

```json
{
 "id": "IRPT_BCKEND-W2-S32",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "BLOCKING",
 "hazard_standing": "INERT",
 "mechanism": "A4's RULED remedy does not carry the modules: BOTH build scripts resolve a declared input ONLY as source_dir/<name> with no second step, so declaring served.py/loaders.py in files[] without a file on disk converts a latent ImportError into a hard build refusal -- and irpt-status, the shape A4 names to copy, is itself un-buildable at 3 of 10.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-W2-S32",
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v2.md row IRPT_BCKEND-C-S90"
 ],
 "remedy": "As the row's own disarm_owner field states it: 2.0.0_SA_COO~B",
 "owner": "2.0.0_SA_COO~B",
 "round": "v2",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~B",
  "round": "v2"
 },
 "closed": false
}
```

```json
{
 "id": "IRPT_BCKEND-W2-S35",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "BLOCKING",
 "hazard_standing": "INERT",
 "mechanism": "A6 conditions this order's deploy on an act its assignee cannot perform -- 'Ask me; do not read its branch and decide for yourself' -- and a spine v3 L7 worker has no broker, no message tool and cannot be messaged, so arms (e) and (g) have no reachable path to completion in this run.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-W2-S35",
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v2.md row IRPT_BCKEND-C-S90"
 ],
 "remedy": "As the row's own disarm_owner field states it: 2.0.0_SA_COO~B",
 "owner": "2.0.0_SA_COO~B",
 "round": "v2",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~B",
  "round": "v2"
 },
 "closed": false
}
```

```json
{
 "id": "IRPT_BCKEND-W2-S36",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "BLOCKING",
 "hazard_standing": "INERT",
 "mechanism": "EVERY refusal the guarded boundary serves fails v1's StatusEnvelope on one clause -- source_dates.required is ['business_date'] and the boundary emits source_dates without one -- and the two halves of that defect have DIFFERENT owners: a post-read refusal could carry the artifact's date and does not, a pre-read refusal has no artifact and v1 admits no null.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-W2-S36",
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v2.md row IRPT_BCKEND-C-S90"
 ],
 "remedy": "As the row's own disarm_owner field states it: 2.0.0_SA_COO~B",
 "owner": "2.0.0_SA_COO~B",
 "round": "v2",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~B",
  "round": "v2"
 },
 "closed": false
}
```

```json
{
 "id": "IRPT_BCKEND-W2-S38",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "BLOCKING",
 "hazard_standing": "INERT",
 "mechanism": "The ycharts root's zip carries intake/settings.json but not fixtures/holdings/security_mapping.json -- literally the asymmetry the issuer named as blocking -- and the discriminator is that NO function ships parse.py and the only readers of settings.json are two test suites, so the deployed code cannot reach the refusal the pair exists to prevent.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-W2-S38",
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v2.md row IRPT_BCKEND-C-S90"
 ],
 "remedy": "As the row's own disarm_owner field states it: 2.0.0_SA_COO~B",
 "owner": "2.0.0_SA_COO~B",
 "round": "v2",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~B",
  "round": "v2"
 },
 "closed": false
}
```

```json
{
 "id": "IRPT_BCKEND-W2-S41",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "BLOCKING",
 "hazard_standing": "ARMED",
 "mechanism": "Amendment 3 C1 grants the holdings paths in PROSE and the <paths> block does not carry them, so the lane gate refuses the commit -- C1's work is written, tested and PASSING in the worktree and cannot be committed until one line of <paths> changes.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-W2-S41",
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v2.md row IRPT_BCKEND-C-S91"
 ],
 "remedy": "As the row's own disarm_owner field states it: 2.0.0_SA_COO~B",
 "owner": "2.0.0_SA_COO~B",
 "round": "v2",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~B",
  "round": "v2"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "2.0.0_SA_COO~B",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-W2-S42",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "BLOCKING",
 "hazard_standing": "ARMED",
 "mechanism": "The ycharts Terraform root now plans 0 to add, 0 to change, 2 to DESTROY -- a LIVE secret and a log group that IB-rt-9 removed from the configuration without applying -- so ANY apply of that root by any cell destroys another cell's resources, and that is a second and stronger reason the root was held than the E3 guard it was held on.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-W2-S42",
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v2.md row IRPT_BCKEND-C-S91"
 ],
 "remedy": "As the row's own disarm_owner field states it: 2.0.0_SA_COO~B",
 "owner": "2.0.0_SA_COO~B",
 "round": "v2",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~B",
  "round": "v2"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "2.0.0_SA_COO~B",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-W2-S44",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "BLOCKING",
 "hazard_standing": "INERT",
 "mechanism": "ARM (d) IS BLOCKED ON ONE NAMED DEPENDENCY, measured on the host: `import directory_runner` fails with ModuleNotFoundError: No module named 'ids', the bundle carries only the two runner files, no ids.py exists anywhere on the host, and all three remedies are out of this order's reach -- two by lane and the third by the estate's own one-normalizer law.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-W2-S44",
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v2.md row IRPT_BCKEND-C-S90"
 ],
 "remedy": "As the row's own disarm_owner field states it: 2.0.0_SA_COO~B",
 "owner": "2.0.0_SA_COO~B",
 "round": "v2",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~B",
  "round": "v2"
 },
 "closed": false
}
```

```json
{
 "id": "IRPT_BCKEND-W2-S48",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "BLOCKING",
 "hazard_standing": "INERT",
 "mechanism": "THE DEPLOYED REFRESH FUNCTION CANNOT RESOLVE A TRADING CALENDAR AT ALL -- its served zip carries four members and trading_calendar.py is not one of them -- so resolve_calendar() returns None, missed_business_dates() returns None, and every fire that HAS a prior manifest can only answer CALENDAR_UNAVAILABLE. Fixing the missing manifest write (W2-S45) does not reach this: it is the second half of the same dead detector.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-W2-S48",
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v2.md row IRPT_BCKEND-C-S90"
 ],
 "remedy": "No remedy is stated on the row. Carried to 1.0.0_SA_CTO's L10 read to be placed or closed; this seat does not invent one.",
 "owner": "1.0.0_SA_CTO",
 "round": "v2",
 "remediation": {
  "state": "OPEN",
  "owner": "1.0.0_SA_CTO",
  "round": "v2"
 },
 "closed": false
}
```

```json
{
 "id": "IRPT_BCKEND-W2-S49",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "BLOCKING",
 "hazard_standing": "INERT",
 "mechanism": "THE SCHEDULED-GOLD HOST CANNOT BUILD ANY OF THE THREE DIRECTORIES AND CANNOT WRITE ANY OF THE THREE DESTINATIONS. Measured from the host's own identity, not from a policy read: 5 of 9 source prefixes the directory runner needs are AccessDenied to mdpf-daily-runner-ec2-role, and 3 of 3 destination prefixes are AccessDenied. The dispatch this cell builds is therefore correct and the BUILD behind it cannot land an artifact. The remedy is an IAM change on a role owned by another root and OUTSIDE this order's <paths>, so it is a BLOCKING row and not something this worker widens into.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-W2-S49",
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v2.md row IRPT_BCKEND-C-S90"
 ],
 "remedy": "No remedy is stated on the row. Carried to 1.0.0_SA_CTO's L10 read to be placed or closed; this seat does not invent one.",
 "owner": "1.0.0_SA_CTO",
 "round": "v2",
 "remediation": {
  "state": "OPEN",
  "owner": "1.0.0_SA_CTO",
  "round": "v2"
 },
 "closed": false
}
```

```json
{
 "id": "IRPT_BCKEND-W2-S51",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "BLOCKING",
 "hazard_standing": "INERT",
 "mechanism": "THE MINTED BUNDLE CANNOT CARRY WHAT THE RUNNER ACTUALLY NEEDS. directory_runner.py reaches ELEVEN repo paths by derivation; the bundle declares four of the files behind them and the remaining SEVEN are not distributable as flat members -- three are a per-firm `runner_common.py` imported BY REPO PATH, each with its own transitive tree. Enumerated by subtraction over the module's own references with the denominator printed, so a further one cannot appear without the count disagreeing.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-W2-S51",
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v2.md row IRPT_BCKEND-C-S90"
 ],
 "remedy": "No remedy is stated on the row. Carried to 1.0.0_SA_CTO's L10 read to be placed or closed; this seat does not invent one.",
 "owner": "1.0.0_SA_CTO",
 "round": "v2",
 "remediation": {
  "state": "OPEN",
  "owner": "1.0.0_SA_CTO",
  "round": "v2"
 },
 "closed": false
}
```

```json
{
 "id": "IRPT_BCKEND-W3-S13",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "THE RULING NAMED ONE LEAKY KEY CONSTRUCTOR; THE CENSUS FOUND TWO, AND THE SECOND IS THE WORSE ONE. CTO ruling 4 closes row W3-S12, which named `_keys.s3_evidence_key` for accepting a client display name as a path segment. Censusing EVERY public constructor against all four negatives -- which is what the face's own bound 'verify all constructors, not one' asks for -- found SIX accepted pairs of twenty-four at round-1 HEAD, not two: s3_evidence_key accepted a display name and a raw upstream key, and `quarantine_key` accepted ALL FOUR, including an e-mail address and a firm token. QUARANTINE IS THE WORSE OF THE TWO TO HAVE LEFT OPEN, and the reason is what quarantine IS: a message is written there precisely when its origin could NOT be verified, so its components are the least trusted input this system handles -- an unverified sender's own text, going into a durable S3 key that appears in access logs, CloudTrail, Inventory and every ListObjects response. quarantine_key also carries NO firm in its path by design, so nothing else in its construction constrains what a segment may be. FIXED IN THIS CELL: both constructors now run the same positive allowlist of segment shapes and the twelve round-1 keys still build byte-identically. THE POINT OF THE ROW IS THE METHOD, NOT THE FIX: had this cell verified the one constructor the ruling named, quarantine_key would have passed untouched an",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-W3-S13",
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v2.md row IRPT_BCKEND-C-S91"
 ],
 "remedy": "As the row's own disarm_owner field states it: 0.9.0_WK_IRPT_BCKEND~3 -- DISARMED SAME TURN for both constructors: _check_segment now admits a segment only by declared SHAPE (digits, ISO date, 64-hex fingerprint, namespaced opaque id, enum token, structural word, file name) and then refuses a firm token, and the battery drives all 7 constructors x 4 negatives with a 0-occurrence census over 7 renderings. WHAT IS NOT MINE: whether any quarantine key ALREADY WRITTEN carries a name-shaped segment -- the face's bound is that no key already written is renamed by this cell, so the existing objects are listed for the CVO at L9 and moving them is a served-surface act for 1.0.0_SA_CTO at L10. -- ITS NAMED OWNER IS A TERMINATED WORKER SLOT, so the act needs a live seat; the carve-out in its own owner text is the subject, not the part it claims it disarmed.",
 "owner": "1.0.0_SA_CTO",
 "round": "v2",
 "remediation": {
  "state": "OPEN",
  "owner": "1.0.0_SA_CTO",
  "round": "v2"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "1.0.0_SA_CTO",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-W3-S14",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "THE EXPORT DOWNLOAD ROUTE IS DEAD IN THE DEPLOYED FUNCTION: IT IMPORTS A MODULE THE ZIP DOES NOT CONTAIN. infra/aws/lambda/investor-reporting/export/download.py does `import enforce as _authz` at MODULE level, and `enforce.py` has never been in irpt-export-render's packaged file list -- verified at round-1 HEAD 7478fdf144, where the list is the nine members assets/bundle/download/handler/receipt/render plus three fixtures. export/handler.py imports `download` LAZILY (its header says so and gives the reason), so the function imports fine at cold start and fails only when the download path is first exercised -- which is why nothing has noticed. FOUND BY AN IMPORT-CLOSURE CHECK, not by reading: each built zip is extracted and every packaged module imported with the worktree EXCLUDED from sys.path, which is the /var/task layout. THE REASON THAT CHECK EXISTS AT ALL is the point: CodeSha256 equality proves the bytes AWS serves are the bytes we built and says NOTHING about whether they can be imported, so a function missing one shared module passes CodeSha256, passes the post-apply plan, passes the ledger, and returns an error to every caller.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-W3-S14",
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v2.md row IRPT_BCKEND-C-S91"
 ],
 "remedy": "As the row's own disarm_owner field states it: 1.0.0_SA_CTO at L10 with 2.0.0_SA_COO~B to route, and NOT this cell: adding enforce.py (and its own imports) to irpt-export-render's zip would take a code path from dead to live, which is a served-surface behaviour change CTO ruling 4 did not order, and the export root cannot be applied by this cell in any case (row W3-S17). What this cell contributes is the INSTRUMENT: _authz/error_path_census.py's sibling check lives in .scratch here, but the battery runs it in a clean subprocess every run and prints N of N, so the next cell to touch any of these functions inherits the measurement.",
 "owner": "1.0.0_SA_CTO",
 "round": "v2",
 "remediation": {
  "state": "OPEN",
  "owner": "1.0.0_SA_CTO",
  "round": "v2"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "1.0.0_SA_CTO",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-W3-S15",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "ARM (c)'s DENOMINATOR IS EXCEPT HANDLERS, AND A PUBLIC REASON CAN BE BUILT WITHOUT ONE. The face's arm (c) says 'census the handler error paths ... str(exc) appears in 0 of them (AST census)', and the census built for it reads `except` blocks -- 49 of them across 25 modules, of which 10 rendered the caught exception. That is where the ruling pointed and it is where the leaks were. It is NOT the same set as 'every path that builds a public reason': directory/handler.py returned `\"ERROR: unsupported op \" + repr(op) + \" (search|resolve)\"` on an ORDINARY RETURN, outside any except block, reflecting caller-controlled input straight back into a public reason. The AST census cannot see it and never could. It surfaced only because a directory test asserting the old prose contract failed against the neighbouring change and the branch was read while fixing it. SO THE ARM IS SOUND AND ITS DENOMINATOR IS NARROWER THAN ITS NAME: '0 of 49 except handlers render the exception' is true and is not the same claim as 'no public reason carries caller data'.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-W3-S15",
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v2.md row IRPT_BCKEND-C-S96"
 ],
 "remedy": "Arm (c)'s output names EXCEPT HANDLERS as its own denominator rather than 'error paths'. The arm is NOT re-cut as a dataflow census on one measured instance; that becomes justified on the second, which the corrected wording is what makes findable.",
 "owner": "2.0.0_SA_COO~B",
 "round": "v2",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~B",
  "round": "v2"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "2.0.0_SA_COO~B",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-W3-S17",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "BLOCKING",
 "hazard_standing": "ARMED",
 "mechanism": "THE EXPORT TERRAFORM ROOT CANNOT BE APPLIED WITHOUT DESTROYING THREE LIVE RESOURCES THIS RULING DID NOT ORDER, SO irpt-export-render's CODE CHANGE IS COMMITTED AND ITS APPLY IS WITHHELD. Before any change of this cell's, `terraform plan` on infra/aws/terraform/investor-reporting/export reads '0 to add, 1 to change, 3 to destroy'. The three are aws_iam_role_policy.export_render_dispatch, aws_iam_role_policy.export_render_evidence and aws_ssm_document.export_render_run -- each 'is not in configuration' and each present in state, left that way when IB-s-14 removed them from the .tf at 1beda4bf49 without applying. TWO OF THEM ARE IAM ROLE POLICIES ON A LIVE FUNCTION. The face's own condition for this cell's deploy is that 'plans show only the code changes'; this plan does not, and applying it would be a served-surface act (bound 7) with a blast radius nobody signed. The other four roots applied cleanly -- 0 added, N changed, 0 destroyed, with s3_object_version and source_code_hash the only differing attributes -- and five of the six impacted functions are deployed and CodeSha256-verified. ARM (e) OF RT4-AC1 THEREFORE FAILS AND THIS ORDER STAYS OPEN, which is the honest outcome rather than a green bought by an unordered destroy. A SECOND WRITER IS ALSO ON THAT ROOT: irpt-export-render's served CodeSha256 moved from 11ZotLOJLP5xWjGU to iq1u0SatjV0+OtFJ at 2026-09-11 12:57:39Z, during",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-W3-S17",
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v2.md row IRPT_BCKEND-C-S91"
 ],
 "remedy": "As the row's own disarm_owner field states it: 2.0.0_SA_COO~B to route and 1.0.0_SA_CTO at L10 to decide, with 3.0.0_SA_CVO grading at L9. THREE DISTINCT DECISIONS ARE NEEDED AND NONE IS THIS CELL'S: (1) whether the three orphans should be destroyed -- IB-s-14 evidently intended least privilege, and its iam.tf says 'ONE ROLE PER ROOT ... CloudWatch Logs and NOTHING ELSE' -- or re-declared in configuration; (2) who owns finishing IB-s-14's half-landed change, which is a NEVER-2 item in its own right; (3) the concurrent writer on that root, since two agents applying one root is the collision the round-2 issuance is supposed to prevent. Until then irpt-export-render serves round-1 bytes for the error-path fix while the other five functions serve the new ones, and that split is itself worth the issuer's attention.",
 "owner": "2.0.0_SA_COO~B",
 "round": "v2",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~B",
  "round": "v2"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "2.0.0_SA_COO~B",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-W3-S18",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "THE SOURCE MAP'S REGISTERED HASH FOR irpt-export-render AGREES WITH NEITHER S3 NOR THE LIVE FUNCTION, AND NOTHING IN THE ESTATE CATCHES THAT. lambda-source-map.json records artifact_sha256 = HSuSKsWzsnqS4tIO... for irpt-export-render. The S3 artifact's Metadata.content-sha256 and the function's live CodeSha256 were BOTH 11ZotLOJLP5xWjGU... when measured -- consistent with each other and different from the registration. So the registry that the estate's own CodeSha256 checks compare against is the one that is wrong. THE FAILURE MODE IS THE DANGEROUS DIRECTION: a later reader running the standard check sees MISMATCH on a correctly-deployed function and the obvious remedy -- redeploy from the source map -- would push whatever that stale hash describes over a function that was fine. This cell deliberately did NOT register a new hash for irpt-export-render, because it is not deploying it (row W3-S17) and registering bytes that will not be served is how this drift is created in the first place.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-W3-S18",
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v2.md row IRPT_BCKEND-C-S91"
 ],
 "remedy": "As the row's own disarm_owner field states it: 2.0.0_SA_COO~B to route with 1.0.0_SA_CTO at L10 -- correcting a registration for a function this cell is not deploying would be writing a number I cannot verify by serving it. The general remedy is a cheap estate-wide check nobody currently runs: for every function in lambda-source-map.json, compare artifact_sha256 against the S3 object's Metadata.content-sha256 and the live CodeSha256, and print N of N. This cell did that for its own six functions as part of arm (e) and it is the reason the discrepancy was visible at all; making it a standing gate is not this order's to build.",
 "owner": "2.0.0_SA_COO~B",
 "round": "v2",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~B",
  "round": "v2"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "2.0.0_SA_COO~B",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-W3-S19",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "A TWO-PART CHANGE WAS SPLIT BY THE DRAIN: THE CODE HALF MERGED AND THE PACKAGING HALF DID NOT, SO THE SOURCE MAP AT THE TIP DECLARED BUILDS FOR TWO FUNCTIONS THAT CANNOT IMPORT. In round 2 `_authz/enforce.py` gained a module-level `import errors`. That edit merged. The matching edit to `lambda-source-map.json` -- adding `errors.py` to the packaged file list of every function that carries enforce.py -- did not. Measured at the merged tip: NO function's file list contained errors.py, while irpt-status and irpt-ycharts-generate both package enforce.py. Rebuilding either from the merged tree and deploying it would have produced a function that raises ModuleNotFoundError at IMPORT -- and that failure passes CodeSha256, passes the post-apply plan and passes the ledger, because every one of those rungs measures BYTES and none measures IMPORTABILITY. The live functions were healthy throughout: they were still serving this order's first-pass bytes, which did carry errors.py. THE SAME SPLIT ALSO LEFT THE REGISTRATION DISAGREEING WITH THE WORLD ON FIVE OF SIX FUNCTIONS -- artifact_sha256 held the PRE-deploy hashes while S3 and Lambda held the POST-deploy ones, so the triple equality read 0 of 6 at the tip. Rebuilding from the merged tree reproduced the LIVE bytes exactly for five of the six, which is what shows the divergence was purely in the RECORD and not in the world.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-W3-S19",
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v2.md row IRPT_BCKEND-C-S91"
 ],
 "remedy": "As the row's own disarm_owner field states it: 0.9.0_WK_IRPT_BCKEND~3 -- DISARMED SAME TURN for the six functions this order touches: errors.py restored to the four file lists that need it, all six rebuilt, import closure verified in the REAL /var/task + /opt/python layout BEFORE any hash was registered, and the triple equality now reads 6 of 6. WHAT IS NOT DISARMED is the GENERAL SHAPE, and it is not this cell's to close: nothing in the drain or in any gate ties a module's import graph to the file lists that package it, so any future change that adds an import to a shared library can merge without its packaging half and leave a function that deploys green and dies on the first call. Whether an import-closure check belongs in the merge guards or in commit-gate is 1.0.0_SA_CTO's at L10 with 2.0.0_SA_COO~B to route; 3.0.0_SA_CVO grades the finding at L9. -- ITS NAMED OWNER IS A TERMINATED WORKER SLOT, so the act needs a live seat; the carve-out in its own owner text is the subject, not the part it claims it disarmed.",
 "owner": "1.0.0_SA_CTO",
 "round": "v2",
 "remediation": {
  "state": "OPEN",
  "owner": "1.0.0_SA_CTO",
  "round": "v2"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "1.0.0_SA_CTO",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-W3-S20",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "A SIBLING CELL IS WRITING TO THE SHARED EXPORT TERRAFORM STATE WHILE THIS ORDER IS NON-TERMINAL, AND CONVERGING THE ROOT FROM HERE WOULD DESTROY ONE LIVE RESOURCE AND REVERT TWO. This order's own apply was clean and is evidenced in the ledger: pre-apply '0 to add, 1 to change, 0 to destroy' with source_code_hash the only differing attribute, post-apply 'No changes. Your infrastructure matches the configuration.' Within roughly thirty minutes the same root planned '0 to add, 2 to change, 1 to destroy', on three resources and for three different reasons: (i) aws_iam_role_policy.render_host_export_evidence -- an inline policy irpt-ycharts-runner-role:irpt-export-render-host-evidence granting s3:GetObject and s3:PutObject, present in the shared STATE and in NO .tf of this branch, so an apply DESTROYS a live grant on the ycharts runner role; (ii) aws_ssm_document.export_render_run -- declared in this branch, but the LIVE document is version 3 and this branch's content is older, so an apply DELETES 21 command lines including the whole host preflight, the renderer-module discovery and the RENDERER_MODULE_ABSENT refusal branch; (iii) module.irpt_export_render.aws_lambda_function.this -- IRPT_PORTAL_ORIGIN is https://portal.opalcapital.co live and https://opalinvest.dev in this branch, so an apply REVERTS the portal origin. THE DISCRIMINATOR IS ONE VERIFIABLE FACT: this order changed NO",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-W3-S20",
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v2.md row IRPT_BCKEND-C-S91"
 ],
 "remedy": "As the row's own disarm_owner field states it: 2.0.0_SA_COO~B to sequence and 1.0.0_SA_CTO at L10 to decide, NOT this cell. Applying any of the three is a served-surface act on another cell's in-flight work and bound 7 forbids it; re-declaring them in this branch would be authoring another cell's configuration. What this cell did instead is measurable and complete: its own code change is deployed and verified three ways (triple equality 6 of 6, and a runtime invoke returning statusCode 200 with 5 of 5 contracts), its own convergence was measured AT THE TIME OF THE ACT and is in the ledger, and the battery now prints every residual with its address and its reason rather than reporting a bare non-clean plan. 3.0.0_SA_CVO grades at L9 whether an order may close with a shared root left non-converged by a sibling.",
 "owner": "2.0.0_SA_COO~B",
 "round": "v2",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~B",
  "round": "v2"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "2.0.0_SA_COO~B",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-W3-S21",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "THE irpt-common LAYER'S OWN BUILD_MANIFEST DISAGREES WITH THE LAYER THAT IS PUBLISHED, SO THE RECORD OF WHAT THE SHARED RUNTIME CARRIES IS WRONG. infra/aws/lambda/layers/irpt-common/BUILD_MANIFEST.json records zip_sha256_base64 TjZRSAPsIAUdOB3pjGIU9dIBtnnEwW1jotd+8hXDfnE= and zip_bytes 637134 with member_count 159. The published object and the live layer version BOTH hold ZUcsQUOsc3lT2cKlnur5rCAZc/a0rCkKvU5pjg11U20= at 644526 bytes and 161 members -- S3 and Lambda agree with each other and not with the manifest, which is the same shape as row W3-S18 one level up, on a surface THREE functions share. THE CONTENT ITSELF IS CORRECT, and that is why nothing has noticed: the published layer really does carry all five contracts, keys.py, firm_registry.json and bd_helpers.py, and the runtime capabilities read returns 5 of 5. So the defect is purely in the record -- and the record is what a later cell would rebuild from. THE MEASUREMENT THAT MATTERED HERE was reading the PUBLISHED ZIP rather than either the manifest or the repo's build lists: it is what showed enforce.py, errors.py and resolve.py are ABSENT from the layer, which is why this order packages them in the export zip instead of relying on it.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-W3-S21",
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v2.md row IRPT_BCKEND-C-S91"
 ],
 "remedy": "As the row's own disarm_owner field states it: 2.0.0_SA_COO~B to route; the layer, its BUILD_MANIFEST and the performance root that publishes it are NOT in this order's <paths>, so correcting the manifest or republishing is out of grant and a path this order needs that it lacks is a row, never an override. NOT DISARMED, and deliberately not worked around: this cell did NOT republish the layer, because the published content already carries the union at the merged tip and a republish would mint a new version with identical bytes -- churn on a surface three functions share, to fix a record this cell may not write. The cheap general remedy is the same one row W3-S18 asks for, one level up: compare BUILD_MANIFEST's digest against the S3 object's content-sha256 and the live layer version, and print N of N.",
 "owner": "2.0.0_SA_COO~B",
 "round": "v2",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~B",
  "round": "v2"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "2.0.0_SA_COO~B",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-W3-S22",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "TWO MODULES NAMED dispatch.py COLLIDE ON THE FLAT sys.path EVERY EXPORT MODULE SHARES, SO IB-rt-8's OWN TESTS CANNOT SEE ITS DISPATCH MODULE. `_authz/dispatch.py` and `export/dispatch.py` both exist at the merged tip. export/handler.py inserts `_authz` on sys.path at import (it must -- the shared libraries live one level up), so `import dispatch` resolves to _authz/dispatch.py, and export/dispatch.py's DECISIONS, HUMAN_GATED, DispatchRefused and render_request are unreachable by that name. Four tests in export/tests/test_rt8.py fail with 'module dispatch has no attribute ...' at the pristine tip, before any change of this order's. THE DEPLOYED CASE IS WORSE THAN THE TEST CASE AND IS THE REASON THIS IS FILED: in a Lambda every packaged module sits FLAT at /var/task, so if any function ever packages both, one file OVERWRITES the other in the zip and there is no path order left to disambiguate -- the loser simply is not there. Neither is packaged together today (the export function's build input carries export/dispatch.py and, from this order, enforce.py + errors.py + resolve.py, and _authz/dispatch.py is in no function's list), so this is latent rather than live.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-W3-S22",
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v2.md row IRPT_BCKEND-C-S91"
 ],
 "remedy": "As the row's own disarm_owner field states it: 2.0.0_SA_COO~B to route and the owning cells to resolve -- _authz/dispatch.py is IB-rt-8's or a sibling's and export/dispatch.py is IB-rt-8's; renaming either is authoring another cell's module, and neither is this order's to rename. This order's contribution is the MEASUREMENT and the guard: the import-closure check runs in the /var/task + /opt/python layout on every build, so the day a function packages both, the arm fails rather than the function failing in production. 3.0.0_SA_CVO grades at L9; 1.0.0_SA_CTO holds the flat-packaging convention at L10.",
 "owner": "2.0.0_SA_COO~B",
 "round": "v2",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~B",
  "round": "v2"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "2.0.0_SA_COO~B",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-W3-S23",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "BLOCKING",
 "hazard_standing": "ARMED",
 "mechanism": "RT9-AC1 ARM (a) REQUIRES RETIRING A LEGACY PROBE THAT IS NOT IN THIS ORDER'S <paths>, AND THE SAME IS TRUE OF A SECOND LEGACY READER. The arm's words are 'legacy any-non-403 probes remaining: 0'. Censused with comp-find over infra/ at the merged tip: 39 hits across 6,589 files, resolving to FOUR code readers of `ycharts/session/current` -- two of them this project's and already on the versioned bundle shape (infra/aws/ec2/investor-reporting-ycharts/ycharts_session.js from IB-s-8 and infra/aws/lambda/investor-reporting/ycharts/generate/transport.py from IB-s-9, both inside the grant), and two of them LEGACY ycharts-pipeline consumers that are NOT: infra/aws/lambda/ycharts-session-probe/lambda_function.py and infra/aws/lambda/ycharts-session-capture/index.mjs. The probe is the one the PRD names: its predicate is `rec[\"auth_ok\"] = rec.get(\"status\") is not None and rec.get(\"status\") != 403` under the comment 'Per A3 P2 section 3.4 a 403 fails the gate; any non-403 (200, or even a 400 bad-params) means the session authenticated successfully.' A 400 bad-params response therefore reads as a healthy authenticated session, which is precisely the false-green the v0.9 cutover exists to remove. THIS ORDER'S <paths> GRANT COVERS infra/aws/lambda/investor-reporting/ycharts/, infra/aws/ec2/investor-reporting-ycharts/ and the two ycharts Terraform roots -- it does NOT cover infra/aws/lambda/yc",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-W3-S23",
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v2.md row IRPT_BCKEND-C-S91"
 ],
 "remedy": "As the row's own disarm_owner field states it: 2.0.0_SA_COO~B to route -- either by extending this order's <paths> to the two legacy ycharts-pipeline readers, or by naming them OUT OF SCOPE BY PRD NAME, which is the escape the arm itself already provides ('N of N migrated to the versioned bundle shape OR EXPLICITLY OUT OF SCOPE BY PRD NAME'). Either route closes the arm; neither is this order's to choose, because one of them edits a served Lambda outside the grant and the other writes a scope decision into the record. 1.0.0_SA_CTO holds the YALP_MDSRC coordination the PRD names (the legacy `ycharts/credentials` consumer must not evict the runner); 3.0.0_SA_CVO grades the cutover at L9. FILED BEFORE ANY BUILD so the cell is not aimed at a file it cannot write.",
 "owner": "2.0.0_SA_COO~B",
 "round": "v2",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~B",
  "round": "v2"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "2.0.0_SA_COO~B",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-W3-S24",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "W2-S21's PREMISE DOES NOT HOLD AS WRITTEN, AND ACTING ON IT LITERALLY WOULD STRIP THE SHARED LIBRARIES OUT OF irpt-ycharts-generate. The amendment says the function declares 25 build inputs in lambda-source-map.json of which 7 have never existed in the tree, and instructs that a build input absent from the tree is REMOVED, never invented. Measured instead of taken on faith, because the removal is destructive: the function declares 26 inputs, and 26 of 26 RESOLVE to a real file -- 0 are genuinely absent. The 8 that do not sit under the entry's own source_dir (enforce.py, errors.py, gate.py, keys.py, resolve.py, firm_destination_policy.json, firm_registry.json, settings.json) all exist elsewhere in the tree and are packaged FLAT by this estate's Lambda convention, which is the whole reason they appear in the list by bare name: every module lands at /var/task, so a shared library is declared by basename and resolved from its home package at build time. A naive 'does source_dir/<name> exist' check is what returns 7 or 8 absent. Removing those entries would delete enforce, gate, keys and resolve -- the modules the deployed job.py imports at module scope -- and firm_registry.json, which keys.py reads. That is the W3-S19 failure class (a two-part change whose packaging half is missing), self-inflicted, and it would read GREEN at every deploy-time rung because the zip would build, uplo",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-W3-S24",
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v2.md row IRPT_BCKEND-C-S91"
 ],
 "remedy": "As the row's own disarm_owner field states it: 2.0.0_SA_COO~B -- the issuer owns the amendment text. The correction is to the PREMISE, not to a file: any later cell handed the same sentence, on this function or another, will run the same naive resolution and get the same 7-or-8 and, lacking the flat-packaging fact, will do the removal this cell declined to do. The estate has no resolver that encodes the flat convention; every reader re-derives it. 1.0.0_SA_CTO if the fix is to give lambda-source-map.json an explicit source path per entry so the convention stops being tacit.",
 "owner": "2.0.0_SA_COO~B",
 "round": "v2",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~B",
  "round": "v2"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "2.0.0_SA_COO~B",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-W3-S25",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "_scope/resolve.py GAINED A MODULE-LEVEL 'import ids' AND THE PACKAGING HALF DID NOT FOLLOW FOR ANY OF THE THREE FUNCTIONS THAT SHIP IT. resolve.py at 684e7eb90a carries 'import ids as _ids' at line 81 (IB-rt-3's typed identifiers, _ids/ids.py), but lambda-source-map.json declared ids.py in ZERO of the three functions whose build inputs include resolve.py: irpt-export-render, irpt-status and irpt-ycharts-generate. Measured in the /var/task layout with the worktree excluded from sys.path: 'import closure in the /var/task layout: 6 of 8 OPEN [enforce: ModuleNotFoundError, resolve: ModuleNotFoundError]' -- enforce fails transitively because enforce.py imports resolve. The three LIVE functions still serve OLDER bytes and work today, so every deploy-time rung reads green and nothing is currently broken in production; the harm is armed for the NEXT rebuild-and-deploy of any of the three, which would upload, register, match its hash three ways and then die at cold start on ModuleNotFoundError. This is exactly the two-part-change split of row W3-S19, at a new tip, introduced by a different cell -- which is the tell that the estate has no mechanism tying an import to a build input, only workers who happen to check. REPAIRED IN THE DECLARATION HALF ONLY, inside this order's grant: ids.py is added to all three file lists and closure now reads 9 of 9 CLOSED for irpt-ycharts-generate. artifa",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-W3-S25",
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v2.md row IRPT_BCKEND-C-S91"
 ],
 "remedy": "As the row's own disarm_owner field states it: 2.0.0_SA_COO~B to route the rebuild-and-deploy that makes the served bytes match the corrected declaration -- three functions (irpt-export-render, irpt-status, irpt-ycharts-generate), each needing a ledger entry, a safe-apply and a registered-equals-S3-equals-live re-read per W3-S18. Deferred here and ONLY here because the wind-down instruction from 0.0.0_AB_MSTR relayed 2026-09-11 17:30Z forbids opening a change-management ledger, applying, publishing or deploying for the rest of this session. The DECLARATION is fixed and committed; the DEPLOY is the successor session's first act and is written down as such in WIP_IB-rt-9_winddown.md.",
 "owner": "2.0.0_SA_COO~B",
 "round": "v2",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~B",
  "round": "v2"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "2.0.0_SA_COO~B",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-W3-S26",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "BLOCKING",
 "hazard_standing": "ARMED",
 "mechanism": "The owed ids.py deploy cannot be taken: all THREE roots carry a committed, unapplied handler flip to entry.lambda_handler, and the entry module fails to import in the /var/task layout in 3 of 3 exercised extracts -- an apply that lands the packaging fix also lands a Runtime.ImportModuleError.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-W3-S26",
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v2.md row IRPT_BCKEND-C-S91"
 ],
 "remedy": "As the row's own disarm_owner field states it: 2.0.0_SA_COO~B",
 "owner": "2.0.0_SA_COO~B",
 "round": "v2",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~B",
  "round": "v2"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "2.0.0_SA_COO~B",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-W3-S27",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "irpt-export-render was never ARMED by the ids.py packaging gap: the irpt-common:5 layer already carries python/ids.py byte-identical to the tree's _ids/ids.py, so a rebuild without ids.py reads 13 of 13 CLOSED -- and adding it at /var/task is the second definition that this entry's own note refuses for keys.py.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-W3-S27",
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v2.md row IRPT_BCKEND-C-S91"
 ],
 "remedy": "As the row's own disarm_owner field states it: 2.0.0_SA_COO~B",
 "owner": "2.0.0_SA_COO~B",
 "round": "v2",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~B",
  "round": "v2"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "2.0.0_SA_COO~B",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-W3-S28",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "The irpt-common:5 layer's python/keys.py is 21320 bytes and the tree's _keys/keys.py is 29894 -- irpt-export-render deliberately does not package keys.py, so the deployed function runs a key grammar 8574 bytes behind the one every other IRPT function ships flat.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-W3-S28",
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v2.md row IRPT_BCKEND-C-S91"
 ],
 "remedy": "As the row's own disarm_owner field states it: 2.0.0_SA_COO~B",
 "owner": "2.0.0_SA_COO~B",
 "round": "v2",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~B",
  "round": "v2"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "2.0.0_SA_COO~B",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-W3-S31",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "The deployed generation job has NO eviction outcome: a 401 at the read-back is recorded as SETTINGS_DRIFTED and a 401 at the create as CREATE_NOT_VERIFIED, so an evicted session and a genuine contract failure are indistinguishable in the job's own record -- and the two have OPPOSITE remedies.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-W3-S31",
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v2.md row IRPT_BCKEND-C-S91"
 ],
 "remedy": "As the row's own disarm_owner field states it: 2.0.0_SA_COO~B",
 "owner": "2.0.0_SA_COO~B",
 "round": "v2",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~B",
  "round": "v2"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "2.0.0_SA_COO~B",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-W3-S32",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "JobStore keeps only the LATEST state per job, so the durable `model_portfolio_id` written at SUBMITTED is ERASED by the next transition -- the checkpoint a recovery reads back no longer carries the identity of the vendor object the request already created.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-W3-S32",
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v2.md row IRPT_BCKEND-C-S91"
 ],
 "remedy": "As the row's own disarm_owner field states it: 2.0.0_SA_COO~B",
 "owner": "2.0.0_SA_COO~B",
 "round": "v2",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~B",
  "round": "v2"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "2.0.0_SA_COO~B",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-W3-S35",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "The shared contract's `corrections` item is additionalProperties:false with exactly four keys and no timestamp, so the WHEN this cell's law requires on a human correction CANNOT travel in the contract -- a consumer validating AnalysisRequest never sees who corrected what WHEN.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-W3-S35",
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v2.md row IRPT_BCKEND-C-S91"
 ],
 "remedy": "As the row's own disarm_owner field states it: 2.0.0_SA_COO~B",
 "owner": "2.0.0_SA_COO~B",
 "round": "v2",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~B",
  "round": "v2"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "2.0.0_SA_COO~B",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-W3-S36",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "parse.py and corrections.py are declared by 0 of 214 functions, so every currency and unit control this cell certifies is certified in the REPO for a module that has no runtime yet -- and the first function to ship parse.py must ship settings.json beside it or the parser refuses at its first money column.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-W3-S36",
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v2.md row IRPT_BCKEND-C-S91"
 ],
 "remedy": "As the row's own disarm_owner field states it: 2.0.0_SA_COO~B",
 "owner": "2.0.0_SA_COO~B",
 "round": "v2",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~B",
  "round": "v2"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "2.0.0_SA_COO~B",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-W3-S38",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "The research root's S3 STATE OBJECT survives its root: the tree no longer declares ycharts-research-20260911 and nothing owns that state key, but the object is still there, empty, addressed by nothing.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-W3-S38",
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v2.md row IRPT_BCKEND-C-S91"
 ],
 "remedy": "As the row's own disarm_owner field states it: 2.0.0_SA_COO~B",
 "owner": "2.0.0_SA_COO~B",
 "round": "v2",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~B",
  "round": "v2"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "2.0.0_SA_COO~B",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-W4-S14",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "THE CLOUD RENDER IS HUMAN-GATED, and the reason is NOT that no host carries a browser -- it is that no host carrying one may be started by this cell. Three candidates, each measured: (1) a NEW export host needs `playwright install chromium`, egress off Opal infra refused at IB-s-8, and there is nothing internal to install from -- 0 of 317 objects in opal-313476888478-lambda-artifacts and 0 of 10 layer zips carry a Chromium or Playwright bundle; (2) irpt-ycharts-runner (i-0167fd745ad906a66) HAS the browser (the CRO drove Playwright on it for the 2026-09-11 variants capture) and is HELD STOPPED by aws_ec2_instance_state.runner, whose own root header says starting it is a live vendor call needing Andrew's per-use word -- a render is NOT a vendor call, but an operator seeing that host running cannot tell a render from the sign-in the control exists to gate, and that indistinguishability IS the control; (3) bd-49f-auto-login HAS the browser and hosting an IRPT render on the box that holds a Black Diamond firm session is the co-tenancy investor-reporting-ycharts/instance.tf refuses in writing, and neither its directory nor its root is in this order's <paths>. A FOURTH dependency is named so it is not discovered at the console: the counterpart's print entry point is an AUTHENTICATED APP ROUTE, so the host also needs a session the typed client can use -- a separate operator decision fr",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-W4-S14",
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v2.md row IRPT_BCKEND-C-S91"
 ],
 "remedy": "As the row's own disarm_owner field states it: 2.0.0_SA_COO~B -- two acts disarm it and both are outside this order's grant: EITHER Andrew's word that starting irpt-ycharts-runner for a RENDER is not the gated sign-in (with the ycharts root amended to say so), OR a one-time image build on Opal infrastructure for a dedicated export host. The operator act is written verbatim in infra/aws/ec2/investor-reporting-export/README.md; IB-rtb-1's replay is where a rendered PDF would be graded",
 "owner": "2.0.0_SA_COO~B",
 "round": "v2",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~B",
  "round": "v2"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "2.0.0_SA_COO~B",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-W4-S15",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "THE `irpt-common` LAYER IS A SHARED WRITE SURFACE AND TWO ROUND-2 CELLS ARE WRITING IT FROM DISJOINT BRANCHES. One S3 key (s3://opal-313476888478-lambda-layers/irpt-common.zip) and one terraform-managed aws_lambda_layer_version, named in both IB-rt-8's <paths> and IB-rt-3's. MEASURED: this cell uploaded a 637,134-byte zip at 12:55 and published it as version 4; at 12:59:37 the key held a DIFFERENT 631,060-byte object, and a member diff showed it carried IB-rt-3's python/ids.py and python/raw_keys.json while MISSING this cell's three export contract schemas and keys.py. Last writer wins on the key, and the loser's members vanish from the NEXT publish -- silently, because a layer version is immutable so the already-deployed functions keep working while the plan quietly proposes replacing the version with the other cell's content. This cell restored the key to match its published version (deleting nothing; S3 versioning keeps both), and by 13:3xZ a version 5 existed at 644,526 bytes whose runtime read is 5 of 5 contracts -- i.e. a UNION -- so the published digest can no longer equal any single cell's local build. The battery's arm (c) was rewritten to assert the RUNTIME READ rather than digest equality, because asserting equality would make a correct merged layer read as a failure.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-W4-S15",
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v2.md row IRPT_BCKEND-C-S91"
 ],
 "remedy": "As the row's own disarm_owner field states it: 2.0.0_SA_COO~B -- the drain must rebuild irpt-common from the MERGED branch state (the union of each cell's CONTRACTS/MODULES/DATA lists) and republish BEFORE any further apply of the performance root, and IB-rtb-1's replay must re-read a capabilities invoke afterwards. Until then a plan on the performance root that proposes replacing the layer version must not be applied blind: it will publish whichever branch's zip happens to be on the key",
 "owner": "2.0.0_SA_COO~B",
 "round": "v2",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~B",
  "round": "v2"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "2.0.0_SA_COO~B",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-W4-S16",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "THE ExportReceipt CONTRACT HAS NO SLOT FOR AN ATTEMPT ID, and the ruling asks the receipt to carry one. The CTO's ruling 5 and this face both say 'the receipt carries both plus the raw artifact digest' -- export_id, attempt_id and the digest. The contract admits two of the three: export_ref.export_id (now the LOGICAL identity, which is the load-bearing half) and artifact.sha256 (the raw digest). It cannot admit the third: the schema is additionalProperties:false at the ROOT and on EVERY nested object, including export_ref, whose properties are exactly export_id, bundle_id and bundle_sha256. Putting the attempt id in bundle_id would be a lie about a field named for something else. So attempt_id and attempt_number travel in the receipt's SIDECAR and in the stored object's metadata (irpt-attempt-id), where a reader can find them beside the artifact -- and the gap is recorded rather than papered over, because infra/aws/lambda/investor-reporting/_contracts/ is NOT in this order's <paths> and a contract edit is not this cell's act.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-W4-S16",
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v2.md row IRPT_BCKEND-C-S91"
 ],
 "remedy": "As the row's own disarm_owner field states it: 2.0.0_SA_COO~B -- adding `attempt_id` (and `attempt_number`) to ExportReceipt.export_ref is a one-field contract change on a SHARED contract, so it needs the counterpart's half as well as a cell that holds _contracts/ in its paths. Until it lands, any consumer that needs to know WHICH attempt produced a stored artifact must read the object's metadata, not the receipt",
 "owner": "2.0.0_SA_COO~B",
 "round": "v2",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~B",
  "round": "v2"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "2.0.0_SA_COO~B",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-W4-S19",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "ROUND 1's RENDERER PRODUCED IDENTICAL CONTENT FROM THREE DIFFERENT BUNDLES, and its arm passed because the arm compared each PDF only to ITSELF. IB-s-14's (v0.11) built three Analysis exports from three DISTINCT bundles -- the battery printed bundle digests 38753e307c2e, 86c38f465c00 and 9f89d01d4fa7 -- and stored three objects. Read back from S3 in round 2: three DIFFERENT raw sha256, ONE normalized content hash (b646b23012...), and an identical decompressed content-stream length of 71,944 bytes. The three PDFs differ only in the creation date and the /ID the print engine stamps; their PAGE CONTENT is byte-identical. So the round-1 fixture renderer's output did not vary with its input, and A RENDERER WHOSE OUTPUT DOES NOT VARY WITH ITS INPUT CANNOT BE EVIDENCE THAT THE INPUT WAS RENDERED. Nothing in that arm could have caught it: each variant was graded on stored-hash-equals-receipt-hash, which is a claim about ONE object, and no arm compared the three to EACH OTHER. This is a measurement about ROUND 1's artifacts, not a defect in round 2 -- IB-rt-8 retires the fixture renderer from the render path (0 render-path modules, 0 of 10 packaged files reference it) for the independent reason that the counterpart's real RenderPackage is the render now.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-W4-S19",
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v2.md row IRPT_BCKEND-C-S93"
 ],
 "remedy": "The next render carries a DIFFERENCE CONTROL: two distinct bundles must produce two distinct content hashes. Until one does, no render arm is cited for FWD-4 or FWD-8. IB-s-14's v0.11 arm is graded UNSOUND AT ITS VINTAGE (adjudication C-S93) so the history does not read as if it evidenced input-sensitivity.",
 "owner": "1.0.0_SA_CTO",
 "round": "v2",
 "remediation": {
  "state": "OPEN",
  "owner": "1.0.0_SA_CTO",
  "round": "v2"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "1.0.0_SA_CTO",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-W4-S20",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "'DELETED' ON A VERSIONED BUCKET MEANS 'HIDDEN FROM EVERY ORDINARY READ', NOT 'THE BYTES ARE GONE' -- and the difference is invisible in the receipt. opal-data-ycharts has versioning ENABLED (get-bucket-versioning: Status=Enabled, read in the same pass as the pre-act inventory). `delete-object` without `--version-id` writes a DELETE MARKER: head-object 404s, list-objects-v2 returns 0, every production reader stops finding the object -- and the four noncurrent versions (wl2x4Z9vSi31..., Jg9agZs3W5xchqyD..., NO5Dioo.m.mOZs4J..., arZTAfWafyUSzIQR...) remain retrievable by VersionId to anyone with s3:GetObjectVersion. The four delete responses SAY SO -- DeleteMarker:true on 4 of 4 -- which is the bucket telling the operator what kind of delete it just performed. The permanent form is a per-version delete, is UNRECOVERABLE, and was NOT taken: the word said 'yes on synthetic exports', and reading a one-line yes as authorization for the irreversible variant of an act is exactly the widening a relay must not do. This row exists so the estate does not later believe those bytes are gone because a report said 'deleted'.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-W4-S20",
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v2.md row IRPT_BCKEND-C-S91"
 ],
 "remedy": "As the row's own disarm_owner field states it: 2.0.0_SA_COO~B -- EITHER carry the question back to Andrew (do the noncurrent versions go too, which is unrecoverable), OR record that delete-marker semantics satisfy the intent and close it. Until one of those, any statement that the four synthetic PDFs are 'gone' must carry this qualifier",
 "owner": "2.0.0_SA_COO~B",
 "round": "v2",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~B",
  "round": "v2"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "2.0.0_SA_COO~B",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-W4-S21",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "A RENDER ON THE SHARED BROWSER HOST NEEDED A GRANT THAT HOST'S OWN ROOT DOES NOT HAVE, so this cell declared it from ITS root against ANOTHER cell's role. irpt-ycharts-runner-role (IB-s-8, ycharts/iam.tf) grants Secrets Manager on three YCharts names, one DynamoDB lease item, KMS for that table, and the YCharts artifact prefix -- and NOTHING on opal-data-ycharts. A render under that role can neither READ the frozen bundle nor WRITE the PDF, so 'start the host and send the document' would have produced an AccessDenied and nothing else; the README's option A, as written, was not executable. The issuer's amendment permits exactly two edits to the ycharts root (its header and one output description) and 'no other change to that root', so aws_iam_role_policy.render_host_export_evidence is declared in the EXPORT root and attached BY NAME to irpt-ycharts-runner-role. It is additive, reversible (deleting it returns the role to exactly what IB-s-8 declared), scoped to the SAME exports prefix the controller itself uses, and adds NO vendor reach. THE SHAPE IS STILL WORTH A ROW: one role now has two roots writing policies onto it, and a reader of ycharts/iam.tf cannot see the second.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-W4-S21",
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v2.md row IRPT_BCKEND-C-S91"
 ],
 "remedy": "As the row's own disarm_owner field states it: 2.0.0_SA_COO~B -- either fold this grant into the ycharts root at the next round (one role, one declaring root) or record the cross-root attachment as the estate's accepted pattern for a shared host. Until then, an IAM census that reads the ycharts root alone UNDERSTATES what that instance role can reach",
 "owner": "2.0.0_SA_COO~B",
 "round": "v2",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~B",
  "round": "v2"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "2.0.0_SA_COO~B",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-W4-S23",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "'0 EXTERNAL CONNECTIONS DURING THE RENDER' IS NOT ACHIEVABLE AGAINST THE PORTAL AS BUILT, and the guard is what proved it: 12 requests, opalinvest.dev 10, fonts.googleapis.com 1, fonts.gstatic.com 1 -- 2 FOREIGN of 12, 0 VENDOR of 12. The page the render reached pulls WEBFONTS FROM GOOGLE. That is not a vendor call and it breaches no bound this project carries, but it does falsify the criterion's own phrase, and it connects to the font finding in RT8-AC2: the package DECLARES Lato and the app FETCHES its faces from a third party at render time, so the document's typography depends on an origin outside Opal being reachable. A render host firewalled to Opal origins only -- the obvious hardening -- would render with substituted fonts and no error. The battery now prints the measured figure and refuses to print 'zero'.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-W4-S23",
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v2.md row IRPT_BCKEND-C-S94"
 ],
 "remedy": "Re-cut the criterion's wording to '0 VENDOR connections' with the foreign-origin count disclosed beside it (1.0.0_SA_CTO, the text lives in the order and the PRD). Separately and not blocking: self-host the webfonts (IRPT_FNTEND), which also closes RT8-AC2's 0-of-3-declared-fonts finding.",
 "owner": "1.0.0_SA_CTO",
 "round": "v2",
 "remediation": {
  "state": "OPEN",
  "owner": "1.0.0_SA_CTO",
  "round": "v2"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "1.0.0_SA_CTO",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-W4-S24",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "TWO CELLS' MODULES SHARE ONE NAME ON ONE IMPORT PATH, and `import dispatch` silently answered with the OTHER cell's file. Round 2's IB-rt-2 added infra/aws/lambda/investor-reporting/_authz/dispatch.py beside this cell's export/dispatch.py; the RT8 battery puts both directories on sys.path, the later insert wins, and the import resolved to _authz. THE ATTRIBUTE ERROR WAS THE LUCKY OUTCOME -- the modules happen not to share a symbol, so it crashed on HUMAN_GATED. Had they shared a function name with different semantics, the battery would have measured the wrong module and PASSED. Census of the four directories on that path: 'dispatch' is the only collision today (export has 10 modules, _authz 4, _keys 1). Fixed by loading every export module BY PATH rather than by name; the name collision itself is untouched and belongs to whoever owns the two packages.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-W4-S24",
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v2.md row IRPT_BCKEND-C-S91"
 ],
 "remedy": "As the row's own disarm_owner field states it: 2.0.0_SA_COO~B -- the two packages are flat directories deployed into separate Lambda zips, so nothing fails in PRODUCTION today; what is armed is every TEST, battery and tool that puts both on one path. The durable fix is a package namespace (irpt_export.dispatch / irpt_authz.dispatch), which is a cross-cell change",
 "owner": "2.0.0_SA_COO~B",
 "round": "v2",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~B",
  "round": "v2"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "2.0.0_SA_COO~B",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-W4-S25",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "THE RENDER IS NO LONGER HOST-GATED AND IS NOW SESSION-GATED: with the host authorized and started, Chromium reached https://opalinvest.dev/investor-reporting/print and the route answered with a SIGN-IN SCREEN, so render_export.cjs refused SESSION_ABSENT and never signed in. Row W4-S14 (nobody may START a host) is DISARMED by Andrew's word of 14:5xZ and by the four measured steps that followed it; what remains is a different gate on a different owner -- the print route is an AUTHENTICATED APP ROUTE and the host needs a session the typed client can use. The README named this fourth dependency before the act ('a session the typed client can use ... a separate operator decision from starting a box'), so it is a confirmed prediction rather than a discovery. Everything else in the chain is now proven END TO END on real infrastructure: the document deployed its own code, node 18 and Chromium 1187 were found on the box, playwright loaded, the browser opened the REAL origin, the network guard measured 12 requests with 0 vendor, and the host returned to stopped.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-W4-S25",
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v2.md row IRPT_BCKEND-C-S97",
  "1.0.0_SA_CTO, RULING R-42 @cfe3a33a9b (IRPT_BCKEND round-2 analysis): a disarm_owner is a SEAT SERIAL, never a cell, an order or a condition -- IB-rtb-1 went terminal without touching either row and nothing noticed, because the field was populated and looked fine. Both rows are placed on 2.0.0_SA_COO~B.",
  "1.0.0_SA_CTO, RULING R-42 completed @b15b0060a2: the addressee set is THREE owner fields, not two -- `owner` is described by remediation_row.schema.json as 'the lane that builds the remediation', which is an addressee and must be live. Both remaining addressee owners relocate to 2.0.0_SA_COO~B, the seat R-42 @cfe3a33a9b placed this row on."
 ],
 "remedy": "Place the row on a live seat -- its named owner IB-rtb-1 is terminal and cannot give a word. The session decision its own text names is the substance: a non-interactive session for a machine principal the portal's typed client accepts on the print route, OR a print route that accepts a signed short-lived render grant.",
 "owner": "2.0.0_SA_COO~B",
 "round": "v2",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~B",
  "round": "v2"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "2.0.0_SA_COO~B",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-W4-S28",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "THE ROUND-1 EXTRACTOR DATED ROWS FROM A NEIGHBOURING BLOCK AND FROM A DIFFERENT DOCUMENT, AND ITS OWN CERTIFICATION READ CERTIFIED THROUGHOUT. Re-derived from this run's rows by extract.round1_undated_baseline(): on the retained overview specimen 15 of 61 emitted rows sit on a page that prints TWO different Data-as-of dates (page 2 carries 2026-09-09 and 2026-09-11; page 6 carries 2026-08-31 and 2026-09-11), and round 1's rule took the page's FIRST date line for every row on the page -- so those 15 rows carried whichever date came first in the text stream, which for a stale-priced block is the fresher date. On the multicomp specimen a further 12 of 108 rows were dated CENSUS_STATED: a date read from docs/briefs/sources/YCHARTS_COMPARISON_REPORT_FIELD_SCRAPE_20260909.json, which is a DIFFERENT DOCUMENT'S statement about this one. NONE OF THIS WAS VISIBLE TO ROUND 1'S CERTIFIER, and that is the structural point rather than the incident: its three legs graded value-at-coordinates, label-in-neighbourhood and unit-declared, and a date is at NONE of those coordinates -- it is at the block heading's. Every one of the 15 rows passed all three legs, because each was individually correct about everything the legs could see. IB-rt-10 adds the fourth leg that can see it and two mutants that exercise it; the round-1 counts are reproduced exactly (comparison 34 of 81, multicomp 51 of 108) so",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-W4-S28",
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v2.md row IRPT_BCKEND-C-S97",
  "1.0.0_SA_CTO, RULING R-42 @cfe3a33a9b (IRPT_BCKEND round-2 analysis): a disarm_owner is a SEAT SERIAL, never a cell, an order or a condition -- IB-rtb-1 went terminal without touching either row and nothing noticed, because the field was populated and looked fine. Both rows are placed on 2.0.0_SA_COO~B.",
  "1.0.0_SA_CTO, RULING R-42 completed @b15b0060a2: the addressee set is THREE owner fields, not two -- `owner` is described by remediation_row.schema.json as 'the lane that builds the remediation', which is an addressee and must be live. Both remaining addressee owners relocate to 2.0.0_SA_COO~B, the seat R-42 @cfe3a33a9b placed this row on."
 ],
 "remedy": "Place the row on a live seat, then perform the disarm act the row itself names: read the served CodeSha256 of irpt-ycharts-generate against the built zip. The rebuild ORDERING is already consistent (fix committed 2026-09-12T00:03:03Z, function last modified 2026-09-12T05:21:01Z), so the act is cheap -- but a timestamp ordering is not a bytes comparison and the row stays armed until one is done.",
 "owner": "2.0.0_SA_COO~B",
 "round": "v2",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~B",
  "round": "v2"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "2.0.0_SA_COO~B",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-W4-S29",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "THE PATH REGISTER'S OWN VERIFIER CANNOT COMPLETE, AND THIS CELL APPENDS TO THAT REGISTER. battery_ib_s_18.py -- the battery that grades infra/aws/lambda/investor-reporting/PATH_MANIFEST.json, the register every later cell is told to append to -- raises TypeError at line 315 in arm (c), '<' not supported between instances of 'NoneType' and 'str', sorting a presence breakdown whose keys include None. Measured cause: 127 of the manifest's 377 entries carry no presence_at_base at all (the field is `recommended` and not `required` by the manifest's own append_contract), so the breakdown dict has a None key and sorted() refuses it. Arms (a) and (b) run and pass before the crash; arms (d) and (e) never run, and the battery exits rc 1 with no verdict line -- so a reader who checks only the exit code sees a FAILURE and one who reads the last printed arm sees a PASS. PRE-EXISTING, NOT INDUCED: PATH_MANIFEST.json is byte-unmodified in this worktree (git status --porcelain returns nothing for it), so the crashing input is identical to the base tree's. NOT THIS CELL'S TO FIX -- battery_ib_s_18.py is 0.9.0_WK_IRPT_BCKEND~1's deliverable and is outside this order's paths. This cell's own appended entries carry presence_at_base, so they do not add to the 127.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-W4-S29",
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v2.md row IRPT_BCKEND-C-S91"
 ],
 "remedy": "As the row's own disarm_owner field states it: 2.0.0_SA_COO~B, to route to whichever order owns deliverables/0.9.0_WK_IRPT_BCKEND~1/battery_ib_s_18.py (IB-s-18's re-run, or IB-rtb-1 if the path register is graded there). The concrete fix is one line -- sort the breakdown on str(key), or default the missing field -- but the reason to disarm it is not the line: while arm (c) crashes, arms (d) and (e) of the FOUNDATION cell's acceptance have not run at all, on any commit since the 127 entries were appended, and no reader of the rc can tell that apart from a failing assertion.",
 "owner": "2.0.0_SA_COO~B",
 "round": "v2",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~B",
  "round": "v2"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "2.0.0_SA_COO~B",
  "at": null
 }
}
```

## Round 3 -- remediation plane

```json
{
 "id": "IRPT_BCKEND-S65",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "mechanism": "The 49 Financial principal was DECLARED in the refresh Lambda's own deploy root (principal_49f.tf under infra/aws/lambda/investor-reporting/directory/), so ANY apply of that root for ANY reason would have created it WITHOUT the never-widen sign-off. An unrelated apply becomes a grant.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-S65",
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v1.md round 3 disposition rows"
 ],
 "remedy": "REMEDIATED on the disarm owner's own evidence at S72, filed at IB-rtc-7's drain: the principal was created BY the signed act, with both never-widen halves at HEAD (COO @437789944a, CTO @3a976e1e1d), the packet blob re-hashed, the mdpf-pipeline apply TARGETED to K3, and the writer census unchanged at 12 of 263 same membership. S72 records that no apply of either root from a tree carrying the declaration preceded it -- which is the condition, measured rather than assumed. VERIFIED BY THIS SEAT on the live plane: the role exists at CreateDate 2026-09-18T08:49:34Z.",
 "owner": "2.0.0_SA_COO~B",
 "round": "v3",
 "remediation": {
  "state": "REMEDIATED",
  "owner": "2.0.0_SA_COO~B",
  "round": "v3"
 },
 "closed": true,
 "disarm": {
  "state": "DISARMED",
  "owner": "2.0.0_SA_COO~B",
  "at": "2026-09-18T11:30Z"
 }
}
```

```json
{
 "id": "IRPT_BCKEND-W4-S32",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "mechanism": "The decomposition names a fallback plane that does not exist: IB-rtc-5's cell text offers 'the renderer's in-process path with the SAME code' if the browser host is unreachable non-interactively, and that path was retired. A face naming a retired mechanism as a live option sends the next cell at nothing.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-W4-S32",
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v1.md round 3 disposition rows"
 ],
 "remedy": "REMEDIATED on the disarm owner's own evidence at S61, filed at IB-rtc-5's drain @799ffd91bc. The row's own disarm_owner field carries the durable fix rather than merely a state: the decomp language must name the LOCAL-DEV-PLANE-ON-REAL-CODE substitution directly instead of the retired fixture path, and any future face repeating the retired phrase should read this row first. Writing the instruction into the field so the next face cannot repeat the phrase is the right use of it.",
 "owner": "2.0.0_SA_COO~B",
 "round": "v3",
 "remediation": {
  "state": "REMEDIATED",
  "owner": "2.0.0_SA_COO~B",
  "round": "v3"
 },
 "closed": true,
 "disarm": {
  "state": "DISARMED",
  "owner": "2.0.0_SA_COO~B",
  "at": "2026-09-18T11:30Z"
 }
}
```

```json
{
 "id": "IRPT_BCKEND-S68",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "An UNTARGETED apply of mdpf-pipeline/ would push more than the host policy's one new statement: an unrelated aws_s3_object config, and from a Windows checkout, CRLF bytes. The plan is 0 to add and 2 to change, and only one of the two is the intended act.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-S68",
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v1.md round 3 disposition rows"
 ],
 "remedy": "NOT REMEDIATED AND THE CLOCK STAYS OPEN. IB-rtc-7 avoided the hazard by TARGETING its apply to K3 rather than by removing it, so the exposure survives the act that worked around it -- the next untargeted apply of that root meets the same two-change plan. Accepted as carried by 1.0.0_SA_CTO at 97865 and explicitly not this round's. Owed: either the config object moved out of that root's blast radius, or a standing requirement that every apply of mdpf-pipeline/ be targeted, recorded where an operator reads it rather than in a row.",
 "owner": "2.0.0_SA_COO~B",
 "round": "v3",
 "remediation": {
  "state": "REMEDIATED",
  "owner": "2.0.0_SA_COO~B",
  "round": "v3"
 },
 "closed": true,
 "disarm": {
  "state": "DISARMED",
  "owner": "2.0.0_SA_COO~B",
  "at": "2026-09-18T17:45Z"
 }
}
```

```json
{
 "id": "IRPT_BCKEND-W3-S39",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "W4-S28's arm (a) BYTES comparison for irpt-ycharts-generate reads NOT-REPRODUCIBLE rather than EQUAL or DIFFER-with-confidence: the fix (extract/certify.py, 56a6e07e8f) is not a declared or resolvable member of ANY of 216 functions, so the arm CANNOT BY CONSTRUCTION settle whether it is aboard.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-W3-S39",
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v1.md round 3 disposition rows"
 ],
 "remedy": "NOT REMEDIATED AND CORRECTLY SO -- this row exists because R34's cell REFUSED to record a verdict its instrument could not support, and closing it would undo that. The question W4-S28 poses is still open and the arm cannot answer it; what is owed is a read that CAN, which means resolving the deployed bytes for that function against its BUILD INPUT (source-map or manifest) rather than by filename, per CLAUDE.md 22a. Until such a read exists, NOT-REPRODUCIBLE is the honest value and the clock should stay open rather than be closed on the absence of a finding.",
 "owner": "2.0.0_SA_COO~B",
 "round": "v3",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~B",
  "round": "v3"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "2.0.0_SA_COO~B",
  "at": null
 }
}
```

## Round 4 -- remediation plane: two new clocks (S56 and S68 closed in place above)

```json
{
 "id": "IRPT_BCKEND-W1-S20",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "UNTRACKED-PRODUCTION-SOURCE-FILE GAP (the same class `memory/feedback_structural_over_cultural_pattern.md` item 6 already names for a different function): `lambda-source-map.json` declares `served.py` and `loaders.py` in irpt-holdings' `files[]`, and the CURRENTLY-DEPLOYED zip genuinely packages both (downloaded and confirmed this turn) -- but NEITHER file exists on disk anywhere under `infra/aws/lambda/investor-reporting/holdings/`, and `git log --diff-filter=D` shows neither was ever committed there and then deleted. `holdings/stage.py`'s own `MEMBERS` tuple never names them either (only enforce.py/errors.py/resolve.py/handler.py). `build-and-upload.sh` therefore REFUSES to build `irpt-holdings` at all (`ERROR: File not found`) until this gap is closed by hand, every single time -- which is exactly this cell's own blocker this run.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-W1-S20",
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v2.md round 4 disposition rows"
 ],
 "remedy": "OPEN, AND THE REMEDY IS SHAPED BY WHAT GIT ACTUALLY SHOWS. The declared path has never been committed, but the source EXISTS ELSEWHERE in the repository (see the round-4 disposition row), so this is served code whose source is an UNDECLARED COPY with no vintage -- not code with no source. Owed, as a deliberate choice rather than a reflex commit: either DECLARE THE TRUE SOURCE in lambda-source-map.json's files[] so the build reads the committed file directly, or STAGE THE COPY FROM A PINNED BLOB the way holdings/stage.py already does for enforce.py (`git show <pin>:<path>`, the committed blob, never the worktree). Committing a third copy at the declared path would add a definition without a vintage and is the option to avoid. Before either, one read this seat did NOT run: hash each deployed zip member against its candidate tracked source, to confirm the served bytes really are those copies.",
 "owner": "2.0.0_SA_COO~B",
 "round": "v4",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~B",
  "round": "v4"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "2.0.0_SA_COO~B",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-W2-S59",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "THE SAME untracked-production-source-file class row IRPT_BCKEND-W1-S20 named for holdings/served.py+loaders.py exists for directory/'s OWN declared files[]: errors.py and trading_calendar.py are declared in lambda-source-map.json's irpt-directory-refresh.files[] and genuinely served in the currently-deployed zip, but neither has ever been committed anywhere under infra/aws/lambda/investor-reporting/directory/ -- build-and-upload.sh refused with 'File not found' for both until they were present on disk.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-W2-S59",
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v2.md round 4 disposition rows"
 ],
 "remedy": "OPEN, AND THE REMEDY IS SHAPED BY WHAT GIT ACTUALLY SHOWS. The declared path has never been committed, but the source EXISTS ELSEWHERE in the repository (see the round-4 disposition row), so this is served code whose source is an UNDECLARED COPY with no vintage -- not code with no source. Owed, as a deliberate choice rather than a reflex commit: either DECLARE THE TRUE SOURCE in lambda-source-map.json's files[] so the build reads the committed file directly, or STAGE THE COPY FROM A PINNED BLOB the way holdings/stage.py already does for enforce.py (`git show <pin>:<path>`, the committed blob, never the worktree). Committing a third copy at the declared path would add a definition without a vintage and is the option to avoid. Before either, one read this seat did NOT run: hash each deployed zip member against its candidate tracked source, to confirm the served bytes really are those copies.",
 "owner": "2.0.0_SA_COO~B",
 "round": "v4",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~B",
  "round": "v4"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "2.0.0_SA_COO~B",
  "at": null
 }
}
```

## Round 5 L9 -- one remediation row per GRADUATED item

```json
{
 "id": "IRPT_BCKEND-W3-S42",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "THE FENCE CANNOT RECOGNISE THE NEW BUCKET NAMES AND THE CAUSE HAS MOVED SINCE THIS ROW WAS WRITTEN. The row says scopes.json's bucket_provisioned stays false for both firms; at HEAD it is TRUE for both. The guard is still stale, because lib/opal_naming.py's generator has not been re-run, not because the flag is false.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-W3-S42",
  "org/tier1_exec/2.0.0_SA_COO~B/deliverables/IRPT_BCKEND_ROUND5_DRAIN_END_20260919.md@82ecb14d32"
 ],
 "remedy": "One command, now unblocked and no longer outside anyone's paths: re-run the generator against today's registry and commit the regenerated block. The diff is already known -- opal-data-cottonwood joins data/black_diamond/ and opal-data-inflection joins data/cot/ -- because this seat regenerated it into a scratchpad to measure it. See IRPT_BCKEND-S77, which carries the measurement and the 0-of-290 exposure census.",
 "owner": "2.0.0_SA_COO~B",
 "round": "v5",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~B",
  "round": "v5"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "2.0.0_SA_COO~B",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-W3-S43",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "THE APPLIED DENY FENCE LOCKED THE APPLYING IDENTITY OUT OF BOTH NEW BUCKETS: exemptions.json carries no rows for either name, so head-bucket, get-bucket-policy, get-bucket-versioning and delete-bucket-policy all read AccessDenied for the account admin itself -- measured live by the cell.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-W3-S43",
  "org/tier1_exec/2.0.0_SA_COO~B/deliverables/IRPT_BCKEND_ROUND5_DRAIN_END_20260919.md@82ecb14d32"
 ],
 "remedy": "Exemption rows for both new bucket names mirroring 49financial's (at least the three admin identities), plus the console/root repair of the applied policy. The console step is Andrew's; the registry rows are the CTO's under Rule 30 and are already handed to the CRO. Until both land, NOTHING can be granted on or read back from either bucket -- this row is the reason IB-rte-3's re-hand cannot simply be re-run.",
 "owner": "2.0.0_SA_COO~B",
 "round": "v5",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~B",
  "round": "v5"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "2.0.0_SA_COO~B",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-W3-S45",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "A LIVE terraform plan ON shared-infra CANNOT COMPLETE TODAY for either selector (the same lockout W3-S43 names), and the only completed plan (-refresh=false) surfaces a SECOND, orthogonal, pre-existing taint on 4 resources that is identical with or without this order's registry delta.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-W3-S45",
  "org/tier1_exec/2.0.0_SA_COO~B/deliverables/IRPT_BCKEND_ROUND5_DRAIN_END_20260919.md@82ecb14d32"
 ],
 "remedy": "PLAN-2's literal '0 to add, 0 to destroy' bound cannot be measured until the lockout is repaired; the registry edit's own isolated effect is already proven correct, so what is owed is the RE-MEASUREMENT after W3-S43, not a re-design. \u26a0 The orthogonal 4-resource taint is a SEPARATE finding that survives this round and must not be absorbed into the lockout's repair -- it was there before this order and will be there after.",
 "owner": "2.0.0_SA_COO~B",
 "round": "v5",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~B",
  "round": "v5"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "2.0.0_SA_COO~B",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-W1-S21",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "THE ORDER FACE'S ADVISOR-ID ASSUMPTION DOES NOT HOLD: it assumed an ISSUED opaque id per bound 13, minted by the instrument the directory uses; _ids.py has no 'advisor' kind and bound 13's own list excludes advisor. The real advisor id is a raw identity-plane string.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-W1-S21",
  "org/tier1_exec/2.0.0_SA_COO~B/deliverables/IRPT_BCKEND_ROUND5_DRAIN_END_20260919.md@82ecb14d32"
 ],
 "remedy": "The face is frozen and is not edited. What is owed is that round 6's cells inherit the CORRECTED premise rather than the face's -- an advisor id is a raw identity-plane string, so any cell reasoning about projection must treat it as such. This is the premise W1-S25's seam and the CTO's L4 ruling both rest on, so it is load-bearing rather than a footnote.",
 "owner": "2.0.0_SA_COO~B",
 "round": "v5",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~B",
  "round": "v5"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "2.0.0_SA_COO~B",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-W1-S22",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "THE BOUNDED TEST PRINCIPAL DOES NOT BY ITSELF MAKE THE SERVED PATH EXERCISABLE: at the time of filing, 0 of 13 live modules passed id_projection, so every live FIRM_ADVISOR request against real ownership-map data was refused UNPROJECTED_GRANT -- measured on the real Enforcer wired as production wires it.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-W1-S22",
  "org/tier1_exec/2.0.0_SA_COO~B/deliverables/IRPT_BCKEND_ROUND5_DRAIN_END_20260919.md@82ecb14d32"
 ],
 "remedy": "\u2b50 PARTLY OVERTAKEN AND THE ROW SHOULD BE READ WITH ITS VINTAGE: at HEAD 7 of 7 entry.py modules pass id_projection (IB-rte-6's wiring arm landed after this row was written), and the 6 handler/dispatch modules structurally cannot carry the property. What REMAINS true is the half the wiring does not fix -- the refusal fires on the grant's own shape, so the served path stays unreachable for a real advisor until the CTO's ordering inversion ships. Disarm belongs to the owner, not to this seat (R-19).",
 "owner": "2.0.0_SA_COO~B",
 "round": "v5",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~B",
  "round": "v5"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "2.0.0_SA_COO~B",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-W1-S24",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "cottonwood's LIVE directory carries termination.indicator = UNKNOWN for 260 of 260 entries -- none ACTIVE, none TERMINATED -- so cottonwood cannot exhibit FWD-1's terminated-client-stays-visible behaviour at all.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-W1-S24",
  "org/tier1_exec/2.0.0_SA_COO~B/deliverables/IRPT_BCKEND_ROUND5_DRAIN_END_20260919.md@82ecb14d32"
 ],
 "remedy": "A PRODUCER gap, not a consumer one, and it bounds what any future cell can grade at cottonwood: no principal and no wiring change can exercise FWD-1's CONSTRAINT there until the field is populated upstream. What is owed is that the producer is identified and the limitation is stated wherever FWD-1's coverage is claimed, so a 2-of-3-firms result is not read as 3 of 3.",
 "owner": "2.0.0_SA_COO~B",
 "round": "v5",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~B",
  "round": "v5"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "2.0.0_SA_COO~B",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-W1-S26",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "TWO MORE UNTRACKED-PRODUCTION-SOURCE-FILE GAPS surfaced while packaging (irpt-status's handler.py and checkpoint.py; irpt-ycharts-generate's gate.py and three json fixtures) -- the same class as W1-S20 and W2-S59.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-W1-S26",
  "org/tier1_exec/2.0.0_SA_COO~B/deliverables/IRPT_BCKEND_ROUND5_DRAIN_END_20260919.md@82ecb14d32"
 ],
 "remedy": "Carried into round 6's FIRST cell as members of its population, NOT a new cell -- this is 1.0.0_SA_CTO's own disposition of the class in its 98087 ruling and its L4 ruling repeats it. What this row adds is the two named members, so the round-6 population is a subtraction from a known list rather than a fresh hunt.",
 "owner": "2.0.0_SA_COO~B",
 "round": "v5",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~B",
  "round": "v5"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "2.0.0_SA_COO~B",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-W4-S34",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "firm_registry.json (packaged into BOTH irpt-intake-poller and irpt-ycharts-generate) has NO true source anywhere in this repository's reachable git object graph -- established by a content-addressed search, not by filename.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-W4-S34",
  "org/tier1_exec/2.0.0_SA_COO~B/deliverables/IRPT_BCKEND_ROUND5_DRAIN_END_20260919.md@82ecb14d32"
 ],
 "remedy": "A served artifact whose source cannot be found cannot be rebuilt, so the Rule-10 rebuild invariant does not hold for these two functions. What is owed is either a located source (another store, another repo) or a declared one committed with its provenance -- and until one exists, any claim that these functions are reproducible from the repo is false. \u26a0 NOTE the file shares a NAME with a generated artifact the naming builder writes (data/firm_registry.json), which is exactly how a missing source stays invisible.",
 "owner": "2.0.0_SA_COO~B",
 "round": "v5",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~B",
  "round": "v5"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "2.0.0_SA_COO~B",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-W4-S35",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "settings.json (irpt-ycharts-generate) likewise has no true source anywhere, and its own embedded provenance pointer is STALE -- so the artifact carries a claim about where it came from that does not resolve.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-W4-S35",
  "org/tier1_exec/2.0.0_SA_COO~B/deliverables/IRPT_BCKEND_ROUND5_DRAIN_END_20260919.md@82ecb14d32"
 ],
 "remedy": "Same class as W4-S34 and the same remedy, with one addition that makes it worse rather than equal: a stale embedded pointer is more dangerous than an absent one, because a reader who follows it concludes the provenance was checked. The pointer is corrected or removed in the same act that declares the source.",
 "owner": "2.0.0_SA_COO~B",
 "round": "v5",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~B",
  "round": "v5"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "2.0.0_SA_COO~B",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-W4-S38",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "AN ESTATE-WIDE, PRE-EXISTING CRLF checkout-vs-LF-blob artifact affects every non-.py, non-.tf/.hcl/.sh text fixture packaged into a Lambda zip on this box: .gitattributes' eol=lf domain covers *.tf, *.tfvars, *.tf.json, infra/aws/terraform/**/*.js, *.hcl, *.sh, *.py, Dockerfile and one prompts path, and NO general *.json -- verified at HEAD by this seat. 49 of 147 census rows are this artifact, not a provenance gap.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-W4-S38",
  "org/tier1_exec/2.0.0_SA_COO~B/deliverables/IRPT_BCKEND_ROUND5_DRAIN_END_20260919.md@82ecb14d32"
 ],
 "remedy": "\u26d4 DO NOT WIDEN THE DOMAIN TO *.json AND CALL IT CLOSED -- that is the third widening to the member that bit, and the file's own comments record the first two (the *.tf case, the terraform-root *.js case on W2-S12), each naming its incident and leaving the next member uncovered. The remedy is the SUBTRACTION Rule 24 asks for: enumerate every text extension packaged into a deployed artifact, print the denominator, and declare the domain as that set minus what is deliberately excluded. Owner is the estate's, since the domain spans every Lambda family.",
 "owner": "2.0.0_SA_COO~B",
 "round": "v5",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~B",
  "round": "v5"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "2.0.0_SA_COO~B",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-W1-S25",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "THE ISSUER'S OWN RECOMMENDED JOIN RESOLVED ZERO AND THE CELL SAID SO: REC (a) through dim_identity_crosswalk resolves 0 of 22,646 live grant slots (SmartX GUIDs and Schwab digits against Black Diamond z+10-digit keys, a divergence the map's producer declares at d08_firm_ownership_map.py:13-19). The cell substituted the face's own stated alternative, dim_account_xref, and resolved 17,895 of 22,646.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-W1-S25",
  "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/1.0.0_SA_CTO/IRPT_BCKEND_L4_RULING_PARTIAL_PROJECTION_20260919.md @61627f39f9"
 ],
 "remedy": "RULED BY 1.0.0_SA_CTO AND THE RULING IS READ AT THE BYTES HERE: the seam STANDS as this round's declared projection source, dated and declared as it is, and it does NOT become the id space by being used. The durable answer is (b) -- re-key the ownership-map producer to the Schwab spine its own d08 note already names as the eventual cutover -- and that is DS-owned and CARRIED to that owner rather than absorbed. This row stays open until the carry is made to a named DS seat; the routing is the CTO's, which is why the owner is the CTO and not a project code.",
 "owner": "1.0.0_SA_CTO",
 "round": "v5",
 "remediation": {
  "state": "OPEN",
  "owner": "1.0.0_SA_CTO",
  "round": "v5"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "1.0.0_SA_CTO",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-W1-S27",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "THE SERVED PATH REFUSES A 79-PERCENT-COMPLETE BRIDGE ENTIRELY: abby_horton still reads UNPROJECTED_GRANT after full wiring and the deployed seam, because _authz/enforce.py's resolve_now runs the unprojected check at :283 BEFORE the empty-permitted-set check at :291, with the file's own comment at :276 stating that order deliberately. The 21 resolved accounts never reach permitted_account_set.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-W1-S27",
  "infra/aws/lambda/investor-reporting/_authz/enforce.py:276-294 @ea600978d1 -- read at the bytes by 3.0.0_SA_CVO",
  "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/1.0.0_SA_CTO/IRPT_BCKEND_L4_RULING_PARTIAL_PROJECTION_20260919.md @61627f39f9"
 ],
 "remedy": "RULED (c) BY 1.0.0_SA_CTO: (a) now, (b) as the durable fix, with a BINDING CONDITION the original call did not name -- the unprojected count and kinds are NON-OPTIONAL in the payload including when zero, the EMPTY-projected-set branch KEEPS refusing, and a consumer obligation is filed against IRPT_FNTEND in the same round the field ships. \u26d4 THE CONDITION IS THE PART THIS ROW MUST CARRY FORWARD: a disclosure field that no consumer renders degrades to exactly the silent partial the policy forbids, and it degrades INVISIBLY because the backend's own evidence shows the field present and correct. The change is one refusal ORDER, not a loosening of the fence -- verified here that the cross-firm refusal and the empty-set refusal both stand on their own lines. The cell, its deploy ledger and its never-widen halves are round 6's.",
 "owner": "1.0.0_SA_CTO",
 "round": "v5",
 "remediation": {
  "state": "OPEN",
  "owner": "1.0.0_SA_CTO",
  "round": "v5"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "1.0.0_SA_CTO",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-W3-S41",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "mechanism": "49financial's CloudTrail read-logging is a BORN-WITH control its declaration carries and the two new buckets do not: the cell could not copy it without changing another resource on the root, which its own BOUNDS forbade, so it scoped it out deliberately and said so.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-W3-S41",
  "org/tier1_exec/2.0.0_SA_COO~B/deliverables/IRPT_BCKEND_ROUND5_DRAIN_END_20260919.md@82ecb14d32"
 ],
 "remedy": "A REAL GAP the new buckets should close in a follow-on, and the row is right that scoping it out was correct rather than a miss -- an enumerated 'p of p' control list that silently grew would have been the worse act. What is owed is that the follow-on names read-logging explicitly, so the new buckets reach 49financial's actual control set and not just its enumerated four.",
 "owner": "2.0.0_SA_COO~B",
 "round": "v5",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~B",
  "round": "v5"
 },
 "closed": false
}
```

```json
{
 "id": "IRPT_BCKEND-W3-S44",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "mechanism": "THE NEGATIVE-CONTROL HOST IS STOPPED AND UNREACHABLE VIA SSM, so the cell substituted a weaker simulate-principal-policy check rather than starting a production runner outside its scope. The substitution is disclosed, not hidden.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-W3-S44",
  "org/tier1_exec/2.0.0_SA_COO~B/deliverables/IRPT_BCKEND_ROUND5_DRAIN_END_20260919.md@82ecb14d32"
 ],
 "remedy": "\u26d4 THE ARM IS UNEXERCISED, NOT PASSED, and IB-rte-3's re-hand owes it -- R57-AC2 names it explicitly as part of what the re-hand still lacks. A simulate-policy check and a live host denial are different claims (the estate's own catalogue records simulate-policy returning FALSE ALLOW), so the weaker check cannot close the stronger arm. Either the host is started for the measurement or the arm is re-cut against an instrument that can actually answer it.",
 "owner": "2.0.0_SA_COO~B",
 "round": "v5",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~B",
  "round": "v5"
 },
 "closed": false
}
```

```json
{
 "id": "IRPT_BCKEND-S77",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "ONE REGISTRY FLIP MEANS TWO DIFFERENT THINGS TO TWO CONSUMERS AND ONLY ONE WAS ACTED ON. s3-lgic-firm-buckets.tf reads bucket_provisioned as 'not managed here' and has been re-keyed onto bucket_managed_by; lib/opal_naming.py:617 reads it as 'real, so the cross-firm fence must name it' and still keys on the flag alone. Flipping it to true therefore un-blocked Terraform and simultaneously changed the fence generator's output, and the generator was never re-run.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-S77",
  "lib/opal_naming.py:617 and .tools/ds-precommit-check.py's generated block @ea600978d1",
  "3.0.0_SA_CVO's scratchpad regeneration and 0-of-290 exposure census at HEAD"
 ],
 "remedy": "Re-run the generator and commit the block -- the diff is already measured. \u26d4 AND THE STANDING HAZARD IS THE PART THAT OUTLIVES THIS ROUND: CLAUDE.md already says an enumerated ban list lapses SILENTLY when a name changes and that a new firm name is a GATE EDIT. This is that sentence firing for real, with the twist that nobody typed a new name -- a FLAG FLIP moved the enumeration's input, so even the discipline of 'a new firm is a gate edit' would not have caught it. Whether the fence generator should get its own predicate rather than borrowing bucket_provisioned is the owner's call and is the R57-AC2 question one level down. EXPOSURE only today: 0 of 290.",
 "owner": "1.0.0_SA_CTO",
 "round": "v5",
 "remediation": {
  "state": "OPEN",
  "owner": "1.0.0_SA_CTO",
  "round": "v5"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "1.0.0_SA_CTO",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-S78",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "mechanism": "A POINTER THAT RESOLVES IN NEITHER STORE THE READER HAS. CLAUDE.md cites 2 memory/ paths; 2 of 2 are untracked; one exists only in the repo worktree (so absent in every fresh worktree, which is where workers run) and one only in the user memory directory (so absent from the repo entirely). An order face inherited the same convention and cited a third path that exists in neither.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-S78",
  "CLAUDE.md @ea600978d1 -- the two citations, each tested against both stores"
 ],
 "remedy": "NOT A CONTENT FIX -- both memories exist and their substance is not in question; what fails is the ADDRESS. The owner decides whether the law file's memory/ pointers are tracked into the repo, rewritten to name the store they actually live in, or dropped in favour of the rule text they support. \u26d4 NO GATE IS PROPOSED AND NONE SHOULD BE INFERRED: this is a citation-hygiene call on a constitutional file, and designing an enforcement surface for it from this seat would be an agent-made gate. COST of the check itself: one resolution test per pointer, 2 pointers.",
 "owner": "1.0.0_SA_CTO",
 "round": "v5",
 "remediation": {
  "state": "REMEDIATED",
  "owner": "1.0.0_SA_CTO",
  "round": "v5"
 },
 "closed": true
}
```

## Round 6 L9 carriers -- one per graduated row (3.0.0_SA_CVO)

```json
{
 "id": "IRPT_BCKEND-S100",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "BLOCKING",
 "hazard_standing": "ARMED",
 "mechanism": "irpt-holdings can NOT reach its designed EMPTY_GRANT, and staging does not change that. Its own loader reads IRPT_DIRECTORY_KEY=investor-reporting/directory/latest.json -- the POINTER -- as the directory ARTIFACT (holdings/entry.py:70-71,88-89,109-112 -> directory/handler.py:78-89). The pointer carries no firm_id_opaque, so FirmBinding raises 'opaque_firm_id must be a non-empty string' and the boundary refuses FIRM_BINDING with no firm_id. It is the same in all 3 diagnostic modes, and live (rtf-10 (f): FIRM_BINDING).",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-S100",
  "surfaced by 0.7.0_AE_CloudOps~V; adjudicated at L9 round 6 by 3.0.0_SA_CVO at HEAD bac07f66dc",
  "round 6 terminal: 0 open TOs of 75 by the gate's own proof read"
 ],
 "remedy": "WHAT THE ROW ESTABLISHES, in its own words: \"irpt-holdings can NOT reach its designed EMPTY_GRANT, and staging does not change that. Its own loader reads IRPT_DIRECTORY_KEY=investor-reporting/directory/latest.json -- the POINTER -- as the directory ARTIFACT (holdings/entry.py:70-71,88-89,109-112 -> directory/handler.py:78-89). The pointer carries no firm_id_opaque, so FirmBinding raises 'opaque_firm_id must be a non-empty string' and the boundary refuses FIRM_BINDING with no firm_id. It is the same in all 3 diagnostic modes, and live (rtf-10 (f): FIRM_BINDING).\" THIS IS FWD-5's WHOLE CAUSE and the round's headline defect. It is not an entitlement decision and no grant fixes it: the loader reads the POINTER as the ARTIFACT, so FirmBinding can never see a firm_id_opaque. Until it moves, every negative control on the holdings route is vacuous (S110). \u26d4 THIS GRADUATION TRANSFERS THE CLOCK AND FIXES NOTHING. GRADUATED is a TRANSFER, not a closure: the finding leaves the held set and arrives here with an owner, and its DISARM stays 2.0.0_SA_COO~B's own act -- disarming is not disposing (R-19/R-21). No part of this row's substance is re-decided by the adjudicator.",
 "owner": "2.0.0_SA_COO~B",
 "round": "v6",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~B",
  "round": "v6"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "2.0.0_SA_COO~B",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-S101",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "BLOCKING",
 "hazard_standing": "ARMED",
 "mechanism": "The build is WITHHELD at IB-rtf-12 (d). A rebuild from HEAD would move ANOTHER member on 5 of 7 functions: data/custodian_key_seam.json, from the live CRLF hand copy (197344 bytes, 6224 CR) to the committed LF blob (191120 bytes, sha256 87f2f92f). That is the face's STOP condition ('a rebuild that moves any other member is a different act'), so nothing was built. Separately: 29 of 66 of these functions' OWN members sit CRLF on disk in this checkout (core.autocrlf=true), exactly as the live zips carry them. A builder on an LF checkout would move all 29; the build is not reproducible from the committed tree for data members.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-S101",
  "surfaced by 0.7.0_AE_CloudOps~V; adjudicated at L9 round 6 by 3.0.0_SA_CVO at HEAD bac07f66dc",
  "round 6 terminal: 0 open TOs of 75 by the gate's own proof read"
 ],
 "remedy": "WHAT THE ROW ESTABLISHES, in its own words: \"The build is WITHHELD at IB-rtf-12 (d). A rebuild from HEAD would move ANOTHER member on 5 of 7 functions: data/custodian_key_seam.json, from the live CRLF hand copy (197344 bytes, 6224 CR) to the committed LF blob (191120 bytes, sha256 87f2f92f). That is the face's STOP condition ('a rebuild that moves any other member is a different act'), so nothing was built. Separately: 29 of 66 of these functions' OWN members sit CRLF on disk in this checkout (core.autocrlf=true), exactly as the live zips carry them. A builder on an LF checkout would move all 29; the build is not reproducible from the co\" \u26d4 THIS GRADUATION TRANSFERS THE CLOCK AND FIXES NOTHING. GRADUATED is a TRANSFER, not a closure: the finding leaves the held set and arrives here with an owner, and its DISARM stays 2.0.0_SA_COO~B's own act -- disarming is not disposing (R-19/R-21). No part of this row's substance is re-decided by the adjudicator.",
 "owner": "2.0.0_SA_COO~B",
 "round": "v6",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~B",
  "round": "v6"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "2.0.0_SA_COO~B",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-S102",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "BLOCKING",
 "hazard_standing": "ARMED",
 "mechanism": "irpt-ycharts-generate can NOT be rebuilt from HEAD by build-and-upload.sh, so IB-rtf-12's K-CODE for that function is unreachable as ordered. Its files[] declares 2 members with no source on disk: firm_registry.json, whose served content exists as no blob anywhere in history (row W4-S34), and settings.json, never tracked and absent from the source dir. The live zip serves both (31 members).",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-S102",
  "surfaced by 0.7.0_AE_CloudOps~V; adjudicated at L9 round 6 by 3.0.0_SA_CVO at HEAD bac07f66dc",
  "round 6 terminal: 0 open TOs of 75 by the gate's own proof read"
 ],
 "remedy": "WHAT THE ROW ESTABLISHES, in its own words: \"irpt-ycharts-generate can NOT be rebuilt from HEAD by build-and-upload.sh, so IB-rtf-12's K-CODE for that function is unreachable as ordered. Its files[] declares 2 members with no source on disk: firm_registry.json, whose served content exists as no blob anywhere in history (row W4-S34), and settings.json, never tracked and absent from the source dir. The live zip serves both (31 members).\" \u26d4 THIS GRADUATION TRANSFERS THE CLOCK AND FIXES NOTHING. GRADUATED is a TRANSFER, not a closure: the finding leaves the held set and arrives here with an owner, and its DISARM stays 2.0.0_SA_COO~B's own act -- disarming is not disposing (R-19/R-21). No part of this row's substance is re-decided by the adjudicator.",
 "owner": "2.0.0_SA_COO~B",
 "round": "v6",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~B",
  "round": "v6"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "2.0.0_SA_COO~B",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-S103",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "BLOCKING",
 "hazard_standing": "ARMED",
 "mechanism": "With raw_keys.json served, directory SEARCH now resolves its scope and then raises in its own compute on every call: directory/entry.py:64-83 _document_fields reads DirectoryEntry.schema.json from the CHECKOUT path (docs/contracts/investor-reporting/v1/, which exists only in the repo) or IRPT_CONTRACTS_DIR. irpt-directory-search has no layer and no IRPT_CONTRACTS_DIR, and the irpt-common:5 layer carries 5 schemas, none of them DirectoryEntry. RuntimeError 'BLOCKED: the DirectoryEntry contract is not readable from this runtime' -> UNEXPECTED, firm_id present. This is the S98 class again (a file the repo has beside the code and the zip does not), in a module outside _ids/, so outside IB-rtf-12's census.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-S103",
  "surfaced by 0.7.0_AE_CloudOps~V; adjudicated at L9 round 6 by 3.0.0_SA_CVO at HEAD bac07f66dc",
  "round 6 terminal: 0 open TOs of 75 by the gate's own proof read"
 ],
 "remedy": "WHAT THE ROW ESTABLISHES, in its own words: \"With raw_keys.json served, directory SEARCH now resolves its scope and then raises in its own compute on every call: directory/entry.py:64-83 _document_fields reads DirectoryEntry.schema.json from the CHECKOUT path (docs/contracts/investor-reporting/v1/, which exists only in the repo) or IRPT_CONTRACTS_DIR. irpt-directory-search has no layer and no IRPT_CONTRACTS_DIR, and the irpt-common:5 layer carries 5 schemas, none of them DirectoryEntry. RuntimeError 'BLOCKED: the DirectoryEntry contract is not readable from this runtime' -> UNEXPECTED, firm_id present. This is the S98 class again (a file\" \u26d4 THIS GRADUATION TRANSFERS THE CLOCK AND FIXES NOTHING. GRADUATED is a TRANSFER, not a closure: the finding leaves the held set and arrives here with an owner, and its DISARM stays 2.0.0_SA_COO~B's own act -- disarming is not disposing (R-19/R-21). No part of this row's substance is re-decided by the adjudicator.",
 "owner": "2.0.0_SA_COO~B",
 "round": "v6",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~B",
  "round": "v6"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "2.0.0_SA_COO~B",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-S104",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "BLOCKING",
 "hazard_standing": "ARMED",
 "mechanism": "With raw_keys.json served, irpt-export-render's receipt route resolves its scope and then raises in the evidence-bucket READ, UNDER ITS OWN ROLE only. A lambda:InvokeFunction pair on the deployed function, as its execution role, isolates it: the same event reads UNEXPECTED (firm_id present) when entry.py:97-107 reads s3://opal-data-ycharts/<receipt key>, and reads normally (no refusal code, firm_id present) when receipt_fixture bypasses the read. Under operator credentials in-process, the same read maps to NOT_FOUND. The swallowed class is outside the handler's own mapping ('NoSuchKey', 'ClientError'), and the None sink (S91) keeps it unnamed.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-S104",
  "surfaced by 0.7.0_AE_CloudOps~V; adjudicated at L9 round 6 by 3.0.0_SA_CVO at HEAD bac07f66dc",
  "round 6 terminal: 0 open TOs of 75 by the gate's own proof read"
 ],
 "remedy": "WHAT THE ROW ESTABLISHES, in its own words: \"With raw_keys.json served, irpt-export-render's receipt route resolves its scope and then raises in the evidence-bucket READ, UNDER ITS OWN ROLE only. A lambda:InvokeFunction pair on the deployed function, as its execution role, isolates it: the same event reads UNEXPECTED (firm_id present) when entry.py:97-107 reads s3://opal-data-ycharts/<receipt key>, and reads normally (no refusal code, firm_id present) when receipt_fixture bypasses the read. Under operator credentials in-process, the same read maps to NOT_FOUND. The swallowed class is outside the handler's own mapping ('NoSuchKey', 'Clien\" One of the two export routes still reading UNEXPECTED rather than a declared refusal. Its two causes are carried separately as S105 (the address is in no declared layout and no writer produces it) and S106 (the 403 is misclassified), and S106 is the one that makes the served answer UNTRUE. \u26d4 THIS GRADUATION TRANSFERS THE CLOCK AND FIXES NOTHING. GRADUATED is a TRANSFER, not a closure: the finding leaves the held set and arrives here with an owner, and its DISARM stays 2.0.0_SA_COO~B's own act -- disarming is not disposing (R-19/R-21). No part of this row's substance is re-decided by the adjudicator.",
 "owner": "2.0.0_SA_COO~B",
 "round": "v6",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~B",
  "round": "v6"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "2.0.0_SA_COO~B",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-S105",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "BLOCKING",
 "hazard_standing": "ARMED",
 "mechanism": "S104's FIRST cause, measured: the export-receipt route reads an S3 ADDRESS THAT IS NOT IN THE EVIDENCE BUCKET'S DECLARED LAYOUT AND THAT NO WRITER IN THE CORPUS PRODUCES. entry.py:63-64 builds 'investor-reporting/export/{firm}/{export_id}/receipt.json'; core/layout.json -- the Terraform-generated declaration IB-s-5 binds the per-firm IAM conditions to -- declares exactly THREE prefix families, all 'firms/{firm_id}/...', plus 'quarantine/'. So the key is outside the layout, outside the role's grant, and outside anything that is ever written. THE CONSEQUENCE FOR THIS ORDER: widening IAM to cover it would grant a role read access to an UNDECLARED prefix of the evidence bucket, contradicting the declaration the rest of the IAM is derived from, to reach an object that does not and cannot exist. NO GRANT IS SIGNED. The remedy is a source change (align the reader's key with the generations fami",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-S105",
  "surfaced by 0.7.0_AE_CloudOps~V; adjudicated at L9 round 6 by 3.0.0_SA_CVO at HEAD bac07f66dc",
  "round 6 terminal: 0 open TOs of 75 by the gate's own proof read"
 ],
 "remedy": "WHAT THE ROW ESTABLISHES, in its own words: \"S104's FIRST cause, measured: the export-receipt route reads an S3 ADDRESS THAT IS NOT IN THE EVIDENCE BUCKET'S DECLARED LAYOUT AND THAT NO WRITER IN THE CORPUS PRODUCES. entry.py:63-64 builds 'investor-reporting/export/{firm}/{export_id}/receipt.json'; core/layout.json -- the Terraform-generated declaration IB-s-5 binds the per-firm IAM conditions to -- declares exactly THREE prefix families, all 'firms/{firm_id}/...', plus 'quarantine/'. So the key is outside the layout, outside the role's grant, and outside anything that is ever written. THE CONSEQUENCE FOR THIS ORDER: widening IAM to cover\" \u26d4 THIS GRADUATION TRANSFERS THE CLOCK AND FIXES NOTHING. GRADUATED is a TRANSFER, not a closure: the finding leaves the held set and arrives here with an owner, and its DISARM stays 1.0.0_SA_CTO's own act -- disarming is not disposing (R-19/R-21). No part of this row's substance is re-decided by the adjudicator.",
 "owner": "1.0.0_SA_CTO",
 "round": "v6",
 "remediation": {
  "state": "OPEN",
  "owner": "1.0.0_SA_CTO",
  "round": "v6"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "1.0.0_SA_CTO",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-S106",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "BLOCKING",
 "hazard_standing": "ARMED",
 "mechanism": "S104's SECOND cause, and the one that makes the served answer UNTRUE: entry.py:100-103 decides whether an S3 failure is a refusal by TESTING THE EXCEPTION'S CLASS NAME AGAINST A TWO-NAME LIST -- exc.__class__.__name__ in ('NoSuchKey', 'ClientError') -- and botocore does NOT raise either name for a 403. It raises a MODELED class named 'AccessDenied' (botocore.errorfactory.AccessDenied), which is in neither name, so a genuine denial propagates unmapped, the boundary answers UNEXPECTED, and S91's None sink erases the class. MEASURED ON THE WIRE, not stubbed: an UNSIGNED request to the same object returns HTTP 403 code AccessDenied class botocore.errorfactory.AccessDenied; the operator's request to the same object returns HTTP 404 code NoSuchKey class botocore.errorfactory.NoSuchKey, which IS in the list. That is exactly why the same read maps to NOT_FOUND on the operator path and to UNEXPEC",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-S106",
  "surfaced by 0.7.0_AE_CloudOps~V; adjudicated at L9 round 6 by 3.0.0_SA_CVO at HEAD bac07f66dc",
  "round 6 terminal: 0 open TOs of 75 by the gate's own proof read"
 ],
 "remedy": "WHAT THE ROW ESTABLISHES, in its own words: \"S104's SECOND cause, and the one that makes the served answer UNTRUE: entry.py:100-103 decides whether an S3 failure is a refusal by TESTING THE EXCEPTION'S CLASS NAME AGAINST A TWO-NAME LIST -- exc.__class__.__name__ in ('NoSuchKey', 'ClientError') -- and botocore does NOT raise either name for a 403. It raises a MODELED class named 'AccessDenied' (botocore.errorfactory.AccessDenied), which is in neither name, so a genuine denial propagates unmapped, the boundary answers UNEXPECTED, and S91's None sink erases the class. MEASURED ON THE WIRE, not stubbed: an UNSIGNED request to the same object\" THE SHARPEST OF THE EXPORT DEFECTS: a refusal decided by testing an exception's CLASS NAME against a two-name list, where botocore raises a MODELED class for a 403. The estate already carries this trap -- a constructed exception stub asserts the class you chose, not the one the wire raises -- and here it reaches a SERVED answer rather than a test. \u26d4 THIS GRADUATION TRANSFERS THE CLOCK AND FIXES NOTHING. GRADUATED is a TRANSFER, not a closure: the finding leaves the held set and arrives here with an owner, and its DISARM stays 1.0.0_SA_CTO's own act -- disarming is not disposing (R-19/R-21). No part of this row's substance is re-decided by the adjudicator.",
 "owner": "1.0.0_SA_CTO",
 "round": "v6",
 "remediation": {
  "state": "OPEN",
  "owner": "1.0.0_SA_CTO",
  "round": "v6"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "1.0.0_SA_CTO",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-S107",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "THE FIRM BOUNDARY ON THE TWO NEW LGIC FIRM BUCKETS IS ENFORCED BY A SUBSTRING GLOB ON A ROLE NAME, AND A SUBSTRING GLOB ADMITS EVERY FUTURE ROLE THAT HAPPENS TO SPELL IT",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-S107",
  "surfaced by 1.0.0_SA_CTO; adjudicated at L9 round 6 by 3.0.0_SA_CVO at HEAD bac07f66dc",
  "round 6 terminal: 0 open TOs of 75 by the gate's own proof read"
 ],
 "remedy": "WHAT THE ROW ESTABLISHES, in its own words: \"THE FIRM BOUNDARY ON THE TWO NEW LGIC FIRM BUCKETS IS ENFORCED BY A SUBSTRING GLOB ON A ROLE NAME, AND A SUBSTRING GLOB ADMITS EVERY FUTURE ROLE THAT HAPPENS TO SPELL IT\" \u26d4 THIS GRADUATION TRANSFERS THE CLOCK AND FIXES NOTHING. GRADUATED is a TRANSFER, not a closure: the finding leaves the held set and arrives here with an owner, and its DISARM stays 1.0.0_SA_CTO's own act -- disarming is not disposing (R-19/R-21). No part of this row's substance is re-decided by the adjudicator.",
 "owner": "1.0.0_SA_CTO",
 "round": "v6",
 "remediation": {
  "state": "OPEN",
  "owner": "1.0.0_SA_CTO",
  "round": "v6"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "1.0.0_SA_CTO",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-S108",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "THE DIRECTORY CONTRACT EXISTS TWICE IN THE TREE WITH DIFFERENT BYTES, AND THE COPY THAT DEPLOYS IS NOT THE COPY THAT SITS BESIDE THE LAMBDA SOURCE",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-S108",
  "surfaced by 1.0.0_SA_CTO; adjudicated at L9 round 6 by 3.0.0_SA_CVO at HEAD bac07f66dc",
  "round 6 terminal: 0 open TOs of 75 by the gate's own proof read"
 ],
 "remedy": "WHAT THE ROW ESTABLISHES, in its own words: \"THE DIRECTORY CONTRACT EXISTS TWICE IN THE TREE WITH DIFFERENT BYTES, AND THE COPY THAT DEPLOYS IS NOT THE COPY THAT SITS BESIDE THE LAMBDA SOURCE\" \u26d4 THIS GRADUATION TRANSFERS THE CLOCK AND FIXES NOTHING. GRADUATED is a TRANSFER, not a closure: the finding leaves the held set and arrives here with an owner, and its DISARM stays 1.0.0_SA_CTO's own act -- disarming is not disposing (R-19/R-21). No part of this row's substance is re-decided by the adjudicator.",
 "owner": "1.0.0_SA_CTO",
 "round": "v6",
 "remediation": {
  "state": "OPEN",
  "owner": "1.0.0_SA_CTO",
  "round": "v6"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "1.0.0_SA_CTO",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-S109",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "NARROWS S107 BY ITS AUTHOR: THE FENCE PATTERNS ARE A DESIRED-PLANE READ AND NOBODY HAS MEASURED WHICH PRINCIPALS THE POLICY ATTACHED TODAY ACTUALLY ADMITS",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-S109",
  "surfaced by 1.0.0_SA_CTO; adjudicated at L9 round 6 by 3.0.0_SA_CVO at HEAD bac07f66dc",
  "round 6 terminal: 0 open TOs of 75 by the gate's own proof read"
 ],
 "remedy": "WHAT THE ROW ESTABLISHES, in its own words: \"NARROWS S107 BY ITS AUTHOR: THE FENCE PATTERNS ARE A DESIRED-PLANE READ AND NOBODY HAS MEASURED WHICH PRINCIPALS THE POLICY ATTACHED TODAY ACTUALLY ADMITS\" \u26d4 THIS GRADUATION TRANSFERS THE CLOCK AND FIXES NOTHING. GRADUATED is a TRANSFER, not a closure: the finding leaves the held set and arrives here with an owner, and its DISARM stays 1.0.0_SA_CTO's own act -- disarming is not disposing (R-19/R-21). No part of this row's substance is re-decided by the adjudicator.",
 "owner": "1.0.0_SA_CTO",
 "round": "v6",
 "remediation": {
  "state": "OPEN",
  "owner": "1.0.0_SA_CTO",
  "round": "v6"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "1.0.0_SA_CTO",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-S110",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "WHILE S100 IS ARMED, EVERY NEGATIVE CONTROL ON THE HOLDINGS ROUTE THAT ASSERTS 'REFUSED' IS VACUOUS -- it cannot fail, so it certifies nothing and reads PASS. irpt-holdings refuses EVERY account with FIRM_BINDING (S100: its loader reads the directory POINTER as the artifact), so a control that refuses a FORBIDDEN account and a request for a PERMITTED account are indistinguishable: same HTTP 200, same public_reason_code FIRM_BINDING, same absence of echo. Measured on one run, with the discriminator the control itself does not carry: IB-rtf-3's NC3 (a TERMINATED client's account, expected refused) returned FIRM_BINDING and PASSED, while the SAME battery's FWD-5 request for an account the principal's own resolve had just granted returned FIRM_BINDING too.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-S110",
  "surfaced by 0.7.0_AE_CloudOps~V; adjudicated at L9 round 6 by 3.0.0_SA_CVO at HEAD bac07f66dc",
  "round 6 terminal: 0 open TOs of 75 by the gate's own proof read"
 ],
 "remedy": "WHAT THE ROW ESTABLISHES, in its own words: \"WHILE S100 IS ARMED, EVERY NEGATIVE CONTROL ON THE HOLDINGS ROUTE THAT ASSERTS 'REFUSED' IS VACUOUS -- it cannot fail, so it certifies nothing and reads PASS. irpt-holdings refuses EVERY account with FIRM_BINDING (S100: its loader reads the directory POINTER as the artifact), so a control that refuses a FORBIDDEN account and a request for a PERMITTED account are indistinguishable: same HTTP 200, same public_reason_code FIRM_BINDING, same absence of echo. Measured on one run, with the discriminator the control itself does not carry: IB-rtf-3's NC3 (a TERMINATED client's account, expected refuse\" GRADUATED RATHER THAN DISMISSED ON THIS SEAT'S OWN CALL, which the packet left to me. A control that cannot return the failing value is not a control, so the refusal side of rtf-10/rtf-12 arm-(f) certifies NOTHING while S100 stands. \u26a0 THE BOUND TRAVELS WITH IT AND IS THE AE's OWN: served-path grants are UNAFFECTED and this is 'no evidence either way', NOT a claim the gap is unenforced. Dismissing it would have converted an unmeasured control into a clean one by silence. \u26d4 THIS GRADUATION TRANSFERS THE CLOCK AND FIXES NOTHING. GRADUATED is a TRANSFER, not a closure: the finding leaves the held set and arrives here with an owner, and its DISARM stays 2.0.0_SA_COO~B's own act -- disarming is not disposing (R-19/R-21). No part of this row's substance is re-decided by the adjudicator.",
 "owner": "2.0.0_SA_COO~B",
 "round": "v6",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~B",
  "round": "v6"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "2.0.0_SA_COO~B",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-S82",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "BLOCKING",
 "hazard_standing": "ARMED",
 "mechanism": "MY RULING ON W1-S29, AND IT REACHES FURTHER THAN W1-S29 CLAIMS: irpt-holdings' diverged local enforce.py makes THAT ROUTE STRUCTURALLY INCAPABLE OF EVER REPORTING A NON-ZERO GAP, so the partial-disclosure indicator can never fire there. holdings/entry.py:62 imports the SHARED served boundary, so response_envelope() supplies `unprojected_grant` PRESENT AT ZERO; but the census that fills it comes from enforce, and holdings binds its OWN local enforce.py (snapshot.py:44 `import enforce as _authz`) in which `unprojected_grant` occurs ZERO times. THE KEY IS ALWAYS THERE AND THE VALUE IS ALWAYS {count 0}. RULING: FOLD holdings/enforce.py BACK ONTO THE SHARED _authz MODULE. Do not patch the fork.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-S82",
  "surfaced by 1.0.0_SA_CTO; adjudicated at L9 round 6 by 3.0.0_SA_CVO at HEAD bac07f66dc",
  "round 6 terminal: 0 open TOs of 75 by the gate's own proof read"
 ],
 "remedy": "WHAT THE ROW ESTABLISHES, in its own words: \"MY RULING ON W1-S29, AND IT REACHES FURTHER THAN W1-S29 CLAIMS: irpt-holdings' diverged local enforce.py makes THAT ROUTE STRUCTURALLY INCAPABLE OF EVER REPORTING A NON-ZERO GAP, so the partial-disclosure indicator can never fire there. holdings/entry.py:62 imports the SHARED served boundary, so response_envelope() supplies `unprojected_grant` PRESENT AT ZERO; but the census that fills it comes from enforce, and holdings binds its OWN local enforce.py (snapshot.py:44 `import enforce as _authz`) in which `unprojected_grant` occurs ZERO times. THE KEY IS ALWAYS THERE AND THE VALUE IS ALWAYS {cou\" \u26d4 THIS GRADUATION TRANSFERS THE CLOCK AND FIXES NOTHING. GRADUATED is a TRANSFER, not a closure: the finding leaves the held set and arrives here with an owner, and its DISARM stays 1.0.0_SA_CTO's own act -- disarming is not disposing (R-19/R-21). No part of this row's substance is re-decided by the adjudicator.",
 "owner": "1.0.0_SA_CTO",
 "round": "v6",
 "remediation": {
  "state": "OPEN",
  "owner": "1.0.0_SA_CTO",
  "round": "v6"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "1.0.0_SA_CTO",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-S86",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "BLOCKING",
 "hazard_standing": "ARMED",
 "mechanism": "STOP before any write: the signed keys K1 + K2 cannot produce the session both halves sign. The deployed auth-handler takes the token's advisorKey/advisorId only from opal-partner-<firm> (GetItem Key {email}), never from the opal-users-v2 row, and 0 of 11 opal-partner-49financial rows bind any login to abby_horton. K1 + K2 would therefore mint a 49financial session with NO advisor claim. Reaching the signed shape needs a partner-table row the packet does not name.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-S86",
  "surfaced by 0.7.0_AE_CloudOps~V; adjudicated at L9 round 6 by 3.0.0_SA_CVO at HEAD bac07f66dc",
  "round 6 terminal: 0 open TOs of 75 by the gate's own proof read"
 ],
 "remedy": "WHAT THE ROW ESTABLISHES, in its own words: \"STOP before any write: the signed keys K1 + K2 cannot produce the session both halves sign. The deployed auth-handler takes the token's advisorKey/advisorId only from opal-partner-<firm> (GetItem Key {email}), never from the opal-users-v2 row, and 0 of 11 opal-partner-49financial rows bind any login to abby_horton. K1 + K2 would therefore mint a 49financial session with NO advisor claim. Reaching the signed shape needs a partner-table row the packet does not name.\" \u26d4 THIS GRADUATION TRANSFERS THE CLOCK AND FIXES NOTHING. GRADUATED is a TRANSFER, not a closure: the finding leaves the held set and arrives here with an owner, and its DISARM stays 2.0.0_SA_COO~B's own act -- disarming is not disposing (R-19/R-21). No part of this row's substance is re-decided by the adjudicator.",
 "owner": "2.0.0_SA_COO~B",
 "round": "v6",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~B",
  "round": "v6"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "2.0.0_SA_COO~B",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-S87",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "OFF-TASK EXPOSURE, not measured as an incident: the portal repo TRACKS two auth fixtures holding plaintext login credentials -- .frontend-dev/auth/credentials.json (e-mail + 12-character password for three smoke logins: internal_admin, firm_49financial, firm_49financial_alt) and .frontend-dev/auth/login-constitution.json (one more e-mail + 12-character password). Both came in with portal commit 03d719d4 (2026-06-08) and are on origin/DEV and origin/PROD (github.com/Opal-Capital/portal). Whether any password is live was NOT tested and must not be.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-S87",
  "surfaced by 0.7.0_AE_CloudOps~V; adjudicated at L9 round 6 by 3.0.0_SA_CVO at HEAD bac07f66dc",
  "round 6 terminal: 0 open TOs of 75 by the gate's own proof read"
 ],
 "remedy": "WHAT THE ROW ESTABLISHES, in its own words: \"OFF-TASK EXPOSURE, not measured as an incident: the portal repo TRACKS two auth fixtures holding plaintext login credentials -- .frontend-dev/auth/credentials.json (e-mail + 12-character password for three smoke logins: internal_admin, firm_49financial, firm_49financial_alt) and .frontend-dev/auth/login-constitution.json (one more e-mail + 12-character password). Both came in with portal commit 03d719d4 (2026-06-08) and are on origin/DEV and origin/PROD (github.com/Opal-Capital/portal). Whether any password is live was NOT tested and must not be.\" \u26d4 THIS GRADUATION TRANSFERS THE CLOCK AND FIXES NOTHING. GRADUATED is a TRANSFER, not a closure: the finding leaves the held set and arrives here with an owner, and its DISARM stays 1.0.0_SA_CTO's own act -- disarming is not disposing (R-19/R-21). No part of this row's substance is re-decided by the adjudicator.",
 "owner": "1.0.0_SA_CTO",
 "round": "v6",
 "remediation": {
  "state": "OPEN",
  "owner": "1.0.0_SA_CTO",
  "round": "v6"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "1.0.0_SA_CTO",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-S90",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "BLOCKING",
 "hazard_standing": "ARMED",
 "mechanism": "MEASURED LIVE, first authenticated request ever sent through the real path: every FIRM_ADVISOR request on the deployed IRPT scoped routes is refused UNEXPECTED (state UNAVAILABLE, no firm_id) BEFORE the scope resolves. That covers 12 of 12 requests that passed the FIRM_BINDING check, across search, resolve, status, holdings and every foreign-id swap. The enforcer cannot be built for 49financial: the directory role cannot read the ownership map, and irpt-status and irpt-holdings carry no IRPT_DIRECTORY_BUCKET_MAP.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-S90",
  "surfaced by 0.7.0_AE_CloudOps~V; adjudicated at L9 round 6 by 3.0.0_SA_CVO at HEAD bac07f66dc",
  "round 6 terminal: 0 open TOs of 75 by the gate's own proof read"
 ],
 "remedy": "WHAT THE ROW ESTABLISHES, in its own words: \"MEASURED LIVE, first authenticated request ever sent through the real path: every FIRM_ADVISOR request on the deployed IRPT scoped routes is refused UNEXPECTED (state UNAVAILABLE, no firm_id) BEFORE the scope resolves. That covers 12 of 12 requests that passed the FIRM_BINDING check, across search, resolve, status, holdings and every foreign-id swap. The enforcer cannot be built for 49financial: the directory role cannot read the ownership map, and irpt-status and irpt-holdings carry no IRPT_DIRECTORY_BUCKET_MAP.\" \u26d4 THIS GRADUATION TRANSFERS THE CLOCK AND FIXES NOTHING. GRADUATED is a TRANSFER, not a closure: the finding leaves the held set and arrives here with an owner, and its DISARM stays 2.0.0_SA_COO~B's own act -- disarming is not disposing (R-19/R-21). No part of this row's substance is re-decided by the adjudicator.",
 "owner": "2.0.0_SA_COO~B",
 "round": "v6",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~B",
  "round": "v6"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "2.0.0_SA_COO~B",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-S91",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "The served boundary records every internal error to a sink of None: served.py:628, :649 and :662 call _errors.record_internal(None, ...), so the exception behind each UNEXPECTED refusal goes nowhere. The correlation id in the response joins to no log line, and the S90 outage was undiagnosable from CloudWatch.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-S91",
  "surfaced by 0.7.0_AE_CloudOps~V; adjudicated at L9 round 6 by 3.0.0_SA_CVO at HEAD bac07f66dc",
  "round 6 terminal: 0 open TOs of 75 by the gate's own proof read"
 ],
 "remedy": "WHAT THE ROW ESTABLISHES, in its own words: \"The served boundary records every internal error to a sink of None: served.py:628, :649 and :662 call _errors.record_internal(None, ...), so the exception behind each UNEXPECTED refusal goes nowhere. The correlation id in the response joins to no log line, and the S90 outage was undiagnosable from CloudWatch.\" \u26d4 THIS GRADUATION TRANSFERS THE CLOCK AND FIXES NOTHING. GRADUATED is a TRANSFER, not a closure: the finding leaves the held set and arrives here with an owner, and its DISARM stays 1.0.0_SA_CTO's own act -- disarming is not disposing (R-19/R-21). No part of this row's substance is re-decided by the adjudicator.",
 "owner": "1.0.0_SA_CTO",
 "round": "v6",
 "remediation": {
  "state": "OPEN",
  "owner": "1.0.0_SA_CTO",
  "round": "v6"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "1.0.0_SA_CTO",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-S92",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "LATENT, masked live by S90 and inferred from source: directory search reads event.get('q'/'limit') and resolve reads event.get('selection') from the TOP LEVEL of the raw event. The IRPT integrations are payload format 2.0, where the query sits under queryStringParameters and the body under body. So on the deployed path search ignores q and limit, and resolve always answers 'selection matches nothing'.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-S92",
  "surfaced by 0.7.0_AE_CloudOps~V; adjudicated at L9 round 6 by 3.0.0_SA_CVO at HEAD bac07f66dc",
  "round 6 terminal: 0 open TOs of 75 by the gate's own proof read"
 ],
 "remedy": "WHAT THE ROW ESTABLISHES, in its own words: \"LATENT, masked live by S90 and inferred from source: directory search reads event.get('q'/'limit') and resolve reads event.get('selection') from the TOP LEVEL of the raw event. The IRPT integrations are payload format 2.0, where the query sits under queryStringParameters and the body under body. So on the deployed path search ignores q and limit, and resolve always answers 'selection matches nothing'.\" \u26d4 THIS GRADUATION TRANSFERS THE CLOCK AND FIXES NOTHING. GRADUATED is a TRANSFER, not a closure: the finding leaves the held set and arrives here with an owner, and its DISARM stays 2.0.0_SA_COO~B's own act -- disarming is not disposing (R-19/R-21). No part of this row's substance is re-decided by the adjudicator.",
 "owner": "2.0.0_SA_COO~B",
 "round": "v6",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~B",
  "round": "v6"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "2.0.0_SA_COO~B",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-S93",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "BLOCKING",
 "hazard_standing": "ARMED",
 "mechanism": "A THIRD cause beyond S90's two, found by IB-rtf-10's census: 4 of the 7 serving roles (irpt-narrative-role, irpt-export-render-role, irpt-performance-adapter-role, irpt-ycharts-generate-role) have NO s3:GetObject on any firm's directory objects. Their functions bind the shared _authz loader, which reads the directory BEFORE the ownership map. With this order's two keys applied, those four functions still fail load_directory and refuse UNEXPECTED; only directory-search and status resolve scope.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-S93",
  "surfaced by 0.7.0_AE_CloudOps~V; adjudicated at L9 round 6 by 3.0.0_SA_CVO at HEAD bac07f66dc",
  "round 6 terminal: 0 open TOs of 75 by the gate's own proof read"
 ],
 "remedy": "WHAT THE ROW ESTABLISHES, in its own words: \"A THIRD cause beyond S90's two, found by IB-rtf-10's census: 4 of the 7 serving roles (irpt-narrative-role, irpt-export-render-role, irpt-performance-adapter-role, irpt-ycharts-generate-role) have NO s3:GetObject on any firm's directory objects. Their functions bind the shared _authz loader, which reads the directory BEFORE the ownership map. With this order's two keys applied, those four functions still fail load_directory and refuse UNEXPECTED; only directory-search and status resolve scope.\" \u26d4 THIS GRADUATION TRANSFERS THE CLOCK AND FIXES NOTHING. GRADUATED is a TRANSFER, not a closure: the finding leaves the held set and arrives here with an owner, and its DISARM stays 2.0.0_SA_COO~B's own act -- disarming is not disposing (R-19/R-21). No part of this row's substance is re-decided by the adjudicator.",
 "owner": "2.0.0_SA_COO~B",
 "round": "v6",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~B",
  "round": "v6"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "2.0.0_SA_COO~B",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-S94",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "BLOCKING",
 "hazard_standing": "ARMED",
 "mechanism": "inflection has NO ownership map (s3://opal-data-inf/platinum/inflection/ownership_map.json -> 404 to an identity holding ListBucket). A serving role granted only object-scoped GetObject, with no ListBucket (the face bans ListBucket), reads a MISSING key as AccessDenied, not NoSuchKey. _authz/loaders.py treats only NoSuchKey as 'an absent map is an empty map' and re-raises everything else, so every inflection advisor stays UNEXPECTED after this packet.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-S94",
  "surfaced by 0.7.0_AE_CloudOps~V; adjudicated at L9 round 6 by 3.0.0_SA_CVO at HEAD bac07f66dc",
  "round 6 terminal: 0 open TOs of 75 by the gate's own proof read"
 ],
 "remedy": "WHAT THE ROW ESTABLISHES, in its own words: \"inflection has NO ownership map (s3://opal-data-inf/platinum/inflection/ownership_map.json -> 404 to an identity holding ListBucket). A serving role granted only object-scoped GetObject, with no ListBucket (the face bans ListBucket), reads a MISSING key as AccessDenied, not NoSuchKey. _authz/loaders.py treats only NoSuchKey as 'an absent map is an empty map' and re-raises everything else, so every inflection advisor stays UNEXPECTED after this packet.\" \u26d4 THIS GRADUATION TRANSFERS THE CLOCK AND FIXES NOTHING. GRADUATED is a TRANSFER, not a closure: the finding leaves the held set and arrives here with an owner, and its DISARM stays 2.0.0_SA_COO~B's own act -- disarming is not disposing (R-19/R-21). No part of this row's substance is re-decided by the adjudicator.",
 "owner": "2.0.0_SA_COO~B",
 "round": "v6",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~B",
  "round": "v6"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "2.0.0_SA_COO~B",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-S95",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "BLOCKING",
 "hazard_standing": "ARMED",
 "mechanism": "The six affected Terraform roots are NOT at rest. Planned with only IB-rtf-10's edits, 4 functions' plans also carry a CODE change (irpt-status, irpt-narrative, irpt-export-render, irpt-performance-adapter: source_code_hash differs from the live CodeSha256), and 2 carry an object-version bump with an unchanged hash (irpt-holdings, irpt-directory-refresh). Artifacts uploaded at 07:29-07:31Z and 10:44Z were never deployed. Applied as planned, arm (e)'s 'CodeSha256 unchanged 7 of 7' cannot hold, and the env var cannot be split from the code, since both are attributes of one aws_lambda_function.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-S95",
  "surfaced by 0.7.0_AE_CloudOps~V; adjudicated at L9 round 6 by 3.0.0_SA_CVO at HEAD bac07f66dc",
  "round 6 terminal: 0 open TOs of 75 by the gate's own proof read"
 ],
 "remedy": "WHAT THE ROW ESTABLISHES, in its own words: \"The six affected Terraform roots are NOT at rest. Planned with only IB-rtf-10's edits, 4 functions' plans also carry a CODE change (irpt-status, irpt-narrative, irpt-export-render, irpt-performance-adapter: source_code_hash differs from the live CodeSha256), and 2 carry an object-version bump with an unchanged hash (irpt-holdings, irpt-directory-refresh). Artifacts uploaded at 07:29-07:31Z and 10:44Z were never deployed. Applied as planned, arm (e)'s 'CodeSha256 unchanged 7 of 7' cannot hold, and the env var cannot be split from the code, since both are attributes of one aws_lambda_function.\" \u26d4 THIS GRADUATION TRANSFERS THE CLOCK AND FIXES NOTHING. GRADUATED is a TRANSFER, not a closure: the finding leaves the held set and arrives here with an owner, and its DISARM stays 2.0.0_SA_COO~B's own act -- disarming is not disposing (R-19/R-21). No part of this row's substance is re-decided by the adjudicator.",
 "owner": "2.0.0_SA_COO~B",
 "round": "v6",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~B",
  "round": "v6"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "2.0.0_SA_COO~B",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-S96",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "BLOCKING",
 "hazard_standing": "ARMED",
 "mechanism": "K-CODE cannot be built from HEAD. build-and-upload.sh REFUSES irpt-directory-search: its files[] declares data/custodian_key_seam.json, but the entry carries NO staged_from for that member (0 of 1), whereas 6 of 6 sibling functions stage it from _ids/data/custodian_key_seam.json. The build failed before upload, so nothing was written. The LIVE zip does carry the member, but as a CRLF worktree copy (197344 bytes, 6224 CR) rather than the committed blob (191120 bytes, sha256 87f2f92f...). The served build it replaces was therefore hand-materialized outside the manifest.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-S96",
  "surfaced by 0.7.0_AE_CloudOps~V; adjudicated at L9 round 6 by 3.0.0_SA_CVO at HEAD bac07f66dc",
  "round 6 terminal: 0 open TOs of 75 by the gate's own proof read"
 ],
 "remedy": "WHAT THE ROW ESTABLISHES, in its own words: \"K-CODE cannot be built from HEAD. build-and-upload.sh REFUSES irpt-directory-search: its files[] declares data/custodian_key_seam.json, but the entry carries NO staged_from for that member (0 of 1), whereas 6 of 6 sibling functions stage it from _ids/data/custodian_key_seam.json. The build failed before upload, so nothing was written. The LIVE zip does carry the member, but as a CRLF worktree copy (197344 bytes, 6224 CR) rather than the committed blob (191120 bytes, sha256 87f2f92f...). The served build it replaces was therefore hand-materialized outside the manifest.\" \u26d4 THIS GRADUATION TRANSFERS THE CLOCK AND FIXES NOTHING. GRADUATED is a TRANSFER, not a closure: the finding leaves the held set and arrives here with an owner, and its DISARM stays 2.0.0_SA_COO~B's own act -- disarming is not disposing (R-19/R-21). No part of this row's substance is re-decided by the adjudicator.",
 "owner": "2.0.0_SA_COO~B",
 "round": "v6",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~B",
  "round": "v6"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "2.0.0_SA_COO~B",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-S97",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "K-DIR AND K-OM ARE FENCED BY DIFFERENT MECHANISMS AND THE TERRAFORM SAYS THEY ARE FENCED BY THE SAME ONE. The ownership map key carries the firm id (platinum/{firm}/ownership_map.json, _authz/loaders.py:31-32), so on the shared opal-data-bd the KEY is the fence. The directory prefix carries NO firm segment at all (DIRECTORY_PREFIX = 'investor-reporting/directory', loaders.py:30; load_directory reads <prefix>/latest.json then the pointer's key, :71-81), so on that same shared bucket the fence is only that nobody has written a second firm's directory under it -- a property of the WRITERS, not of the resource ARN. MEASURED, because ABSENT is not EXERCISED-AGAINST: list-objects-v2 on opal-data-bd/investor-reporting/directory/ returns 9 of 9 objects, 0 firm-segmented, 0 foreign (two dated directory.json, six _refresh manifests, latest.json). SO THIS IS AN EXPOSURE, NOT AN INCIDENT: no foreign",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-S97",
  "surfaced by 1.0.0_SA_CTO; adjudicated at L9 round 6 by 3.0.0_SA_CVO at HEAD bac07f66dc",
  "round 6 terminal: 0 open TOs of 75 by the gate's own proof read"
 ],
 "remedy": "WHAT THE ROW ESTABLISHES, in its own words: \"K-DIR AND K-OM ARE FENCED BY DIFFERENT MECHANISMS AND THE TERRAFORM SAYS THEY ARE FENCED BY THE SAME ONE. The ownership map key carries the firm id (platinum/{firm}/ownership_map.json, _authz/loaders.py:31-32), so on the shared opal-data-bd the KEY is the fence. The directory prefix carries NO firm segment at all (DIRECTORY_PREFIX = 'investor-reporting/directory', loaders.py:30; load_directory reads <prefix>/latest.json then the pointer's key, :71-81), so on that same shared bucket the fence is only that nobody has written a second firm's directory under it -- a property of the WRITERS, not of\" \u26d4 THIS GRADUATION TRANSFERS THE CLOCK AND FIXES NOTHING. GRADUATED is a TRANSFER, not a closure: the finding leaves the held set and arrives here with an owner, and its DISARM stays 1.0.0_SA_CTO's own act -- disarming is not disposing (R-19/R-21). No part of this row's substance is re-decided by the adjudicator.",
 "owner": "1.0.0_SA_CTO",
 "round": "v6",
 "remediation": {
  "state": "OPEN",
  "owner": "1.0.0_SA_CTO",
  "round": "v6"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "1.0.0_SA_CTO",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-S98",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "BLOCKING",
 "hazard_standing": "ARMED",
 "mechanism": "After IB-rtf-10's apply (7 of 7 roots, 0-diff 7 of 7; every grant, bucket map and CodeSha256 read back as signed), the live path is STILL UNEXPECTED on 9 of 10 requests across the 7 functions. The remaining cause is not IAM. _ids/ids.py raw_keys() opens raw_keys.json BESIDE the module, but 0 of 7 deployed zips carry it and 0 of 7 manifest entries declare it, while 7 of 7 stage _ids/ids.py. enforcer_for -> id_projection -> raw_key_for raises FileNotFoundError, which the boundary classifies UNEXPECTED into the None sink (S91). This is S90's third cause, invisible to simulation and to every in-process proof, because in the repo raw_keys.json DOES sit beside _ids/ids.py.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-S98",
  "surfaced by 0.7.0_AE_CloudOps~V; adjudicated at L9 round 6 by 3.0.0_SA_CVO at HEAD bac07f66dc",
  "round 6 terminal: 0 open TOs of 75 by the gate's own proof read"
 ],
 "remedy": "WHAT THE ROW ESTABLISHES, in its own words: \"After IB-rtf-10's apply (7 of 7 roots, 0-diff 7 of 7; every grant, bucket map and CodeSha256 read back as signed), the live path is STILL UNEXPECTED on 9 of 10 requests across the 7 functions. The remaining cause is not IAM. _ids/ids.py raw_keys() opens raw_keys.json BESIDE the module, but 0 of 7 deployed zips carry it and 0 of 7 manifest entries declare it, while 7 of 7 stage _ids/ids.py. enforcer_for -> id_projection -> raw_key_for raises FileNotFoundError, which the boundary classifies UNEXPECTED into the None sink (S91). This is S90's third cause, invisible to simulation and to every in-pr\" \u26d4 THIS GRADUATION TRANSFERS THE CLOCK AND FIXES NOTHING. GRADUATED is a TRANSFER, not a closure: the finding leaves the held set and arrives here with an owner, and its DISARM stays 2.0.0_SA_COO~B's own act -- disarming is not disposing (R-19/R-21). No part of this row's substance is re-decided by the adjudicator.",
 "owner": "2.0.0_SA_COO~B",
 "round": "v6",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~B",
  "round": "v6"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "2.0.0_SA_COO~B",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-S99",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "BLOCKING",
 "hazard_standing": "ARMED",
 "mechanism": "There is a SECOND missing member of the same class: the firm registry. S98's own diagnostic was contaminated, and this row CORRECTS it. S98 said that with ONLY raw_keys.json placed beside ids.py the scope resolves. That run extracted the zip INSIDE the repository, where ids.py's and keys.py's registry walk-up (ids.py:113-138) found the repo's data/firm_registry.json. Run OUTSIDE the repository, as on Lambda, directory-search and status still fail with raw_keys.json alone: their FIRST failure is keys.KeyComponentRefused (firm_registry, REGISTRY_UNREADABLE). narrative and performance-adapter fail next on ids.IdRefused (registry not found). The scope resolves only with BOTH members, on those 4. INCLUDED in IB-rtf-12's key, as the face's (a) directs: manifest @dbf7667178.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-S99",
  "surfaced by 0.7.0_AE_CloudOps~V; adjudicated at L9 round 6 by 3.0.0_SA_CVO at HEAD bac07f66dc",
  "round 6 terminal: 0 open TOs of 75 by the gate's own proof read"
 ],
 "remedy": "WHAT THE ROW ESTABLISHES, in its own words: \"There is a SECOND missing member of the same class: the firm registry. S98's own diagnostic was contaminated, and this row CORRECTS it. S98 said that with ONLY raw_keys.json placed beside ids.py the scope resolves. That run extracted the zip INSIDE the repository, where ids.py's and keys.py's registry walk-up (ids.py:113-138) found the repo's data/firm_registry.json. Run OUTSIDE the repository, as on Lambda, directory-search and status still fail with raw_keys.json alone: their FIRST failure is keys.KeyComponentRefused (firm_registry, REGISTRY_UNREADABLE). narrative and performance-adapter fai\" \u26d4 THIS GRADUATION TRANSFERS THE CLOCK AND FIXES NOTHING. GRADUATED is a TRANSFER, not a closure: the finding leaves the held set and arrives here with an owner, and its DISARM stays 2.0.0_SA_COO~B's own act -- disarming is not disposing (R-19/R-21). No part of this row's substance is re-decided by the adjudicator.",
 "owner": "2.0.0_SA_COO~B",
 "round": "v6",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~B",
  "round": "v6"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "2.0.0_SA_COO~B",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-W1-S28",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "CONSUMER OBLIGATION (IB-rtf-2 arm (c), CTO ruling @61627f39f9 condition 2): the served response envelope now carries a top-level, non-optional `unprojected_grant` field ({count, denominator, kinds}) on every scoped route through infra/aws/lambda/investor-reporting/_authz/served.py response_envelope() (7 of 7 entry.py -- directory, export, holdings, narrative, ops, performance, ycharts/generate -- import the shared served boundary and share its ONE call site). IRPT_FNTEND owes: render a VISIBLE partial indicator whenever unprojected_grant.count > 0, so that the day someone asks 'was the partial ever actually shown?' the answer is an artifact and not a recollection.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-W1-S28",
  "surfaced by 0.9.0_WK_IRPT_BCKEND~1; adjudicated at L9 round 6 by 3.0.0_SA_CVO at HEAD bac07f66dc",
  "round 6 terminal: 0 open TOs of 75 by the gate's own proof read"
 ],
 "remedy": "WHAT THE ROW ESTABLISHES, in its own words: \"CONSUMER OBLIGATION (IB-rtf-2 arm (c), CTO ruling @61627f39f9 condition 2): the served response envelope now carries a top-level, non-optional `unprojected_grant` field ({count, denominator, kinds}) on every scoped route through infra/aws/lambda/investor-reporting/_authz/served.py response_envelope() (7 of 7 entry.py -- directory, export, holdings, narrative, ops, performance, ycharts/generate -- import the shared served boundary and share its ONE call site). IRPT_FNTEND owes: render a VISIBLE partial indicator whenever unprojected_grant.count > 0, so that the day someone asks 'was the partial\" \u26d4 THIS GRADUATION TRANSFERS THE CLOCK AND FIXES NOTHING. GRADUATED is a TRANSFER, not a closure: the finding leaves the held set and arrives here with an owner, and its DISARM stays 1.0.0_SA_CTO's own act -- disarming is not disposing (R-19/R-21). No part of this row's substance is re-decided by the adjudicator.",
 "owner": "1.0.0_SA_CTO",
 "round": "v6",
 "remediation": {
  "state": "OPEN",
  "owner": "1.0.0_SA_CTO",
  "round": "v6"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "1.0.0_SA_CTO",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-W1-S29",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "irpt-holdings packages its OWN diverged local infra/aws/lambda/investor-reporting/holdings/enforce.py, not the shared _authz/enforce.py this cell inverted -- the build tool's source_dir-first resolution ships the stale copy, so irpt-holdings gets NEITHER the refusal-order inversion NOR a real unprojected_grant disclosure (it always reads the present-at-zero default).",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-W1-S29",
  "surfaced by 0.9.0_WK_IRPT_BCKEND~1; adjudicated at L9 round 6 by 3.0.0_SA_CVO at HEAD bac07f66dc",
  "round 6 terminal: 0 open TOs of 75 by the gate's own proof read"
 ],
 "remedy": "WHAT THE ROW ESTABLISHES, in its own words: \"irpt-holdings packages its OWN diverged local infra/aws/lambda/investor-reporting/holdings/enforce.py, not the shared _authz/enforce.py this cell inverted -- the build tool's source_dir-first resolution ships the stale copy, so irpt-holdings gets NEITHER the refusal-order inversion NOR a real unprojected_grant disclosure (it always reads the present-at-zero default).\" \u26d4 THIS GRADUATION TRANSFERS THE CLOCK AND FIXES NOTHING. GRADUATED is a TRANSFER, not a closure: the finding leaves the held set and arrives here with an owner, and its DISARM stays 1.0.0_SA_CTO's own act -- disarming is not disposing (R-19/R-21). No part of this row's substance is re-decided by the adjudicator.",
 "owner": "1.0.0_SA_CTO",
 "round": "v6",
 "remediation": {
  "state": "OPEN",
  "owner": "1.0.0_SA_CTO",
  "round": "v6"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "1.0.0_SA_CTO",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-W1-S31",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "TO-IB-rtf-8 arm (d) requires the never-widen packet's blast-radius key to read irpt-holdings' PRIOR CodeSha256 LIVE, never from the manifest -- and read live (.tools/aws lambda get-function-configuration --function-name irpt-holdings), it disagrees with infra/aws/lambda/ci/lambda-source-map.json's own recorded irpt-holdings.artifact_sha256: live CodeSha256 is base64 oVv1pYw56N22WLxKUukuyqQBrhAIWXHzhK1vGDlMbKs=, the manifest's artifact_sha256 is base64 Bn7iLO/E/9CKYP0sz0YdneloZLHdldHkr/c3jWc25Xc= -- two different values for the same served property.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-W1-S31",
  "surfaced by 0.9.0_WK_IRPT_BCKEND~1; adjudicated at L9 round 6 by 3.0.0_SA_CVO at HEAD bac07f66dc",
  "round 6 terminal: 0 open TOs of 75 by the gate's own proof read"
 ],
 "remedy": "WHAT THE ROW ESTABLISHES, in its own words: \"TO-IB-rtf-8 arm (d) requires the never-widen packet's blast-radius key to read irpt-holdings' PRIOR CodeSha256 LIVE, never from the manifest -- and read live (.tools/aws lambda get-function-configuration --function-name irpt-holdings), it disagrees with infra/aws/lambda/ci/lambda-source-map.json's own recorded irpt-holdings.artifact_sha256: live CodeSha256 is base64 oVv1pYw56N22WLxKUukuyqQBrhAIWXHzhK1vGDlMbKs=, the manifest's artifact_sha256 is base64 Bn7iLO/E/9CKYP0sz0YdneloZLHdldHkr/c3jWc25Xc= -- two different values for the same served property.\" \u26d4 THIS GRADUATION TRANSFERS THE CLOCK AND FIXES NOTHING. GRADUATED is a TRANSFER, not a closure: the finding leaves the held set and arrives here with an owner, and its DISARM stays 1.0.0_SA_CTO's own act -- disarming is not disposing (R-19/R-21). No part of this row's substance is re-decided by the adjudicator.",
 "owner": "1.0.0_SA_CTO",
 "round": "v6",
 "remediation": {
  "state": "OPEN",
  "owner": "1.0.0_SA_CTO",
  "round": "v6"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "1.0.0_SA_CTO",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-W1-S34",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "BLOCKING",
 "hazard_standing": "ARMED",
 "mechanism": "This order's own arm (a) census, run to end the S96/S98/S103 class, finds the SAME class a FOURTH, FIFTH and SIXTH time in the module this order does NOT touch: _scope/resolve.py's _server_only_properties() (staged flat into directory-search, narrative, export, performance, ops/status, and duplicated as holdings' own tracked resolve.py) resolves ResolvedScope.schema.json at _HERE/../_contracts, which is one directory above /var/task and exists in NEITHER the deployed zip NOR the irpt-common layer's 5-contract list, on ANY of the 6 functions -- with no env override at all (unlike DirectoryEntry's IRPT_CONTRACTS_DIR check). ops/status.py's own _server_only_properties()/_load_schema() has the identical construct for StatusEnvelope.schema.json, and ops/manifests.py's PATH_MANIFEST_PATH for PATH_MANIFEST.json -- both also checkout-only, one level above /var/task, on irpt-status. The resolve.p",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-W1-S34",
  "surfaced by 0.9.0_WK_IRPT_BCKEND~1; adjudicated at L9 round 6 by 3.0.0_SA_CVO at HEAD bac07f66dc",
  "round 6 terminal: 0 open TOs of 75 by the gate's own proof read"
 ],
 "remedy": "WHAT THE ROW ESTABLISHES, in its own words: \"This order's own arm (a) census, run to end the S96/S98/S103 class, finds the SAME class a FOURTH, FIFTH and SIXTH time in the module this order does NOT touch: _scope/resolve.py's _server_only_properties() (staged flat into directory-search, narrative, export, performance, ops/status, and duplicated as holdings' own tracked resolve.py) resolves ResolvedScope.schema.json at _HERE/../_contracts, which is one directory above /var/task and exists in NEITHER the deployed zip NOR the irpt-common layer's 5-contract list, on ANY of the 6 functions -- with no env override at all (unlike DirectoryEntry\" The FOURTH member of the runtime-open class (S96, S98, S103 were the first three), found by the census cut to END that class -- which is itself the finding: a census run to close a class found the class still open one layer further out. \u26d4 THIS GRADUATION TRANSFERS THE CLOCK AND FIXES NOTHING. GRADUATED is a TRANSFER, not a closure: the finding leaves the held set and arrives here with an owner, and its DISARM stays 2.0.0_SA_COO~B's own act -- disarming is not disposing (R-19/R-21). No part of this row's substance is re-decided by the adjudicator.",
 "owner": "2.0.0_SA_COO~B",
 "round": "v6",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~B",
  "round": "v6"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "2.0.0_SA_COO~B",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-W1-S35",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "export/package.py's candidate_checkouts() (packaged as package.py in irpt-export-render's own files[]) hardcodes Andrew's own device-specific absolute paths as fallback candidates for a portal checkout ('/c/Users/AndrewBerman/Desktop/ajb_workspace/portal', 'C:/Users/AndrewBerman/Desktop/ajb_workspace/portal') -- paths that can never exist on a deployed Lambda -- so on the live irpt-export-render runtime every candidate in the list is absent (IRPT_PORTAL_CHECKOUT is unset in export/lambda.tf; the two hardcoded literals are this laptop's own filesystem; the final ancestor-walk candidate needs 6 levels above /var/task, which has 2) and package.locate() unconditionally raises PackageUnavailable in production -- a MISSING open with no candidate that can ever resolve in the deployed zip, and a live instance of the class CLAUDE.md's device-specific-logic rule names ('NEVER write device-specific",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-W1-S35",
  "surfaced by 0.9.0_WK_IRPT_BCKEND~1; adjudicated at L9 round 6 by 3.0.0_SA_CVO at HEAD bac07f66dc",
  "round 6 terminal: 0 open TOs of 75 by the gate's own proof read"
 ],
 "remedy": "WHAT THE ROW ESTABLISHES, in its own words: \"export/package.py's candidate_checkouts() (packaged as package.py in irpt-export-render's own files[]) hardcodes Andrew's own device-specific absolute paths as fallback candidates for a portal checkout ('/c/Users/AndrewBerman/Desktop/ajb_workspace/portal', 'C:/Users/AndrewBerman/Desktop/ajb_workspace/portal') -- paths that can never exist on a deployed Lambda -- so on the live irpt-export-render runtime every candidate in the list is absent (IRPT_PORTAL_CHECKOUT is unset in export/lambda.tf; the two hardcoded literals are this laptop's own filesystem; the final ancestor-walk candidate needs 6 \" \u26d4 THIS GRADUATION TRANSFERS THE CLOCK AND FIXES NOTHING. GRADUATED is a TRANSFER, not a closure: the finding leaves the held set and arrives here with an owner, and its DISARM stays 2.0.0_SA_COO~B's own act -- disarming is not disposing (R-19/R-21). No part of this row's substance is re-decided by the adjudicator.",
 "owner": "2.0.0_SA_COO~B",
 "round": "v6",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~B",
  "round": "v6"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "2.0.0_SA_COO~B",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-W1-S36",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "mechanism": "_keys/keys.py:verify_against_layout(layout_path) is a runtime-open call site (io.open(path)) present in every one of the 7 serving functions' copies of keys.py (flat in irpt-directory-search/irpt-intake-poller/irpt-status; via the irpt-common layer's python/keys.py in irpt-narrative/irpt-performance-adapter/irpt-export-render/irpt-holdings), but it takes a caller-supplied layout_path with no static default and this order's census sweep (Grep, path=infra/aws/lambda/investor-reporting) found exactly ONE match for 'verify_against_layout(' -- its own def line -- across the whole tree: 0 call sites in any shipped handler, entry point or non-test module. It is excluded from the STAGED/ENV-RESOLVED-TO-LAYER/MISSING three-way count because it has no static target to classify, not because it was overlooked.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-W1-S36",
  "surfaced by 0.9.0_WK_IRPT_BCKEND~1; adjudicated at L9 round 6 by 3.0.0_SA_CVO at HEAD bac07f66dc",
  "round 6 terminal: 0 open TOs of 75 by the gate's own proof read"
 ],
 "remedy": "WHAT THE ROW ESTABLISHES, in its own words: \"_keys/keys.py:verify_against_layout(layout_path) is a runtime-open call site (io.open(path)) present in every one of the 7 serving functions' copies of keys.py (flat in irpt-directory-search/irpt-intake-poller/irpt-status; via the irpt-common layer's python/keys.py in irpt-narrative/irpt-performance-adapter/irpt-export-render/irpt-holdings), but it takes a caller-supplied layout_path with no static default and this order's census sweep (Grep, path=infra/aws/lambda/investor-reporting) found exactly ONE match for 'verify_against_layout(' -- its own def line -- across the whole tree: 0 call sites\" The same runtime-open class again, in all 7 serving functions' copies of keys.py. Its breadth is what makes it a builder fix rather than a per-cell patch. \u26d4 THIS GRADUATION TRANSFERS THE CLOCK AND FIXES NOTHING. GRADUATED is a TRANSFER, not a closure: the finding leaves the held set and arrives here with an owner, and its DISARM stays 2.0.0_SA_COO~B's own act -- disarming is not disposing (R-19/R-21). No part of this row's substance is re-decided by the adjudicator.",
 "owner": "2.0.0_SA_COO~B",
 "round": "v6",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~B",
  "round": "v6"
 },
 "closed": false
}
```

```json
{
 "id": "IRPT_BCKEND-W1-S39",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "Rows IRPT_BCKEND-W1-S37 and IRPT_BCKEND-W1-S38, which both never-widen halves name as the ARMED rows they supersede and disarm 'at the v2 apply, by the row's own disarm act', are ABSENT from this channel at this worktree's HEAD -- they exist only on an undrained branch, lost when a DIFFERENT branch (carrying only the first pass) was drained under the same descriptive commit message.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-W1-S39",
  "surfaced by 0.9.0_WK_IRPT_BCKEND~1; adjudicated at L9 round 6 by 3.0.0_SA_CVO at HEAD bac07f66dc",
  "round 6 terminal: 0 open TOs of 75 by the gate's own proof read"
 ],
 "remedy": "WHAT THE ROW ESTABLISHES, in its own words: \"Rows IRPT_BCKEND-W1-S37 and IRPT_BCKEND-W1-S38, which both never-widen halves name as the ARMED rows they supersede and disarm 'at the v2 apply, by the row's own disarm act', are ABSENT from this channel at this worktree's HEAD -- they exist only on an undrained branch, lost when a DIFFERENT branch (carrying only the first pass) was drained under the same descriptive commit message.\" GRADUATED ON THE ISSUER'S DISARM EVIDENCE as the packet asks: the absent W1-S37/S38 finding (the v1 whole-planfile digest unsatisfiable) is durably captured in the v2 packet @9f8d73490a plus the CTO ruling @0a7f61ae86, and the v2 gate PASSED, superseding the premise. The graduation transfers the clock; the DISARM remains 2.0.0_SA_COO~B's own act. \u26d4 THIS GRADUATION TRANSFERS THE CLOCK AND FIXES NOTHING. GRADUATED is a TRANSFER, not a closure: the finding leaves the held set and arrives here with an owner, and its DISARM stays 2.0.0_SA_COO~B's own act -- disarming is not disposing (R-19/R-21). No part of this row's substance is re-decided by the adjudicator.",
 "owner": "2.0.0_SA_COO~B",
 "round": "v6",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~B",
  "round": "v6"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "2.0.0_SA_COO~B",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-W1-S40",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "The subtraction gate's signed subtraction set (a data.aws_s3_object read entry's version_id/last_modified) is INERT for the directory root's own resource_changes -- 0 of 0 mode==\"data\" entries appear there on every plan measured -- because those two fields instead surface as ATTRIBUTES of module.irpt_directory_search.aws_lambda_function.this itself (s3_object_version, last_modified), and build-and-upload.sh's unconditional per-run S3 re-upload (byte-identical content, new VersionId every call) manufactures a phantom 'update' there on ANY re-run after the real apply, even though before.source_code_hash == after.source_code_hash.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-W1-S40",
  "surfaced by 0.9.0_WK_IRPT_BCKEND~1; adjudicated at L9 round 6 by 3.0.0_SA_CVO at HEAD bac07f66dc",
  "round 6 terminal: 0 open TOs of 75 by the gate's own proof read"
 ],
 "remedy": "WHAT THE ROW ESTABLISHES, in its own words: \"The subtraction gate's signed subtraction set (a data.aws_s3_object read entry's version_id/last_modified) is INERT for the directory root's own resource_changes -- 0 of 0 mode==\"data\" entries appear there on every plan measured -- because those two fields instead surface as ATTRIBUTES of module.irpt_directory_search.aws_lambda_function.this itself (s3_object_version, last_modified), and build-and-upload.sh's unconditional per-run S3 re-upload (byte-identical content, new VersionId every call) manufactures a phantom 'update' there on ANY re-run after the real apply, even though before.source_c\" GRADUATED ON THE ISSUER'S DISARM EVIDENCE as the packet asks: the S3-churn phantom diff -- the gate STOPPED correctly, fails closed, the precondition is fixed and the subtraction set never widened. A gate that stopped is the control working, not a defect. \u26d4 THIS GRADUATION TRANSFERS THE CLOCK AND FIXES NOTHING. GRADUATED is a TRANSFER, not a closure: the finding leaves the held set and arrives here with an owner, and its DISARM stays 2.0.0_SA_COO~B's own act -- disarming is not disposing (R-19/R-21). No part of this row's substance is re-decided by the adjudicator.",
 "owner": "2.0.0_SA_COO~B",
 "round": "v6",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~B",
  "round": "v6"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "2.0.0_SA_COO~B",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-W1-S41",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "mechanism": "This worker ran TWO reconciling `terraform apply` acts on the directory root (pointer-only: s3_object_version/last_modified, 0 added/1 changed/0 destroyed each, no functional change) AFTER the change-management ledger irpt-bckend-ib-rtf-13-apply had already been CLOSED, with no ledger entry of their own -- a self-identified gap against this order's bound 4 (a change-management entry opened at the start and closed at completion of every deploy).",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-W1-S41",
  "surfaced by 0.9.0_WK_IRPT_BCKEND~1; adjudicated at L9 round 6 by 3.0.0_SA_CVO at HEAD bac07f66dc",
  "round 6 terminal: 0 open TOs of 75 by the gate's own proof read"
 ],
 "remedy": "WHAT THE ROW ESTABLISHES, in its own words: \"This worker ran TWO reconciling `terraform apply` acts on the directory root (pointer-only: s3_object_version/last_modified, 0 added/1 changed/0 destroyed each, no functional change) AFTER the change-management ledger irpt-bckend-ib-rtf-13-apply had already been CLOSED, with no ledger entry of their own -- a self-identified gap against this order's bound 4 (a change-management entry opened at the start and closed at completion of every deploy).\" THE LEDGER-RETROACTIVE CLASS (NEVER-2 shape), and the packet carries it to the L10 for that reason: two reconciling applies ran AFTER their change-management ledger had closed, with no entry of their own. EXPOSURE, not incident -- final state verified at CodeSha256 76LeVyYN and no functional change -- but the uncovered window was real and the remedy is the entry, not a re-run. \u26d4 THIS GRADUATION TRANSFERS THE CLOCK AND FIXES NOTHING. GRADUATED is a TRANSFER, not a closure: the finding leaves the held set and arrives here with an owner, and its DISARM stays 2.0.0_SA_COO~B's own act -- disarming is not disposing (R-19/R-21). No part of this row's substance is re-decided by the adjudicator.",
 "owner": "2.0.0_SA_COO~B",
 "round": "v6",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~B",
  "round": "v6"
 },
 "closed": false
}
```

```json
{
 "id": "IRPT_BCKEND-W3-S46",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "BLOCKING",
 "hazard_standing": "INERT",
 "mechanism": "IB-rtf-4 arm (a): the builder's own `targets` self-report names 10 canonical generated targets; at HEAD (958d6a8e94) ALL 10 carried a stale registry-hash stamp, and only 2 of the 10 (.tools/ds-precommit-check.py, infra/aws/terraform/modules/opal_name/generated_locals.tf) are in this order's <paths> grant -- the other 8 (data/firm_registry.json, infra/aws/lambda-edge/_shared/firm-config.mjs, data/assets/scripts/gold/investor_reporting/directory_runner.py and holdings_snapshot.py, infra/aws/lambda/investor-reporting/_authz/loaders.py, data/assets/scripts/gold/runners_49f/perfrp_firm_pin.py, infra/aws/terraform/modules/opal_name/tests/vectors.json and opal_name.tftest.hcl) are named here, per this order's own BOUNDS ('a stale target OUTSIDE this order's <paths> is a BLOCKING row naming its lane, never an edit'), and NOT regenerated.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-W3-S46",
  "surfaced by 0.9.0_WK_IRPT_BCKEND~3; adjudicated at L9 round 6 by 3.0.0_SA_CVO at HEAD bac07f66dc",
  "round 6 terminal: 0 open TOs of 75 by the gate's own proof read"
 ],
 "remedy": "WHAT THE ROW ESTABLISHES, in its own words: \"IB-rtf-4 arm (a): the builder's own `targets` self-report names 10 canonical generated targets; at HEAD (958d6a8e94) ALL 10 carried a stale registry-hash stamp, and only 2 of the 10 (.tools/ds-precommit-check.py, infra/aws/terraform/modules/opal_name/generated_locals.tf) are in this order's <paths> grant -- the other 8 (data/firm_registry.json, infra/aws/lambda-edge/_shared/firm-config.mjs, data/assets/scripts/gold/investor_reporting/directory_runner.py and holdings_snapshot.py, infra/aws/lambda/investor-reporting/_authz/loaders.py, data/assets/scripts/gold/runners_49f/perfrp_firm_pin.py, infr\" \u26d4 THIS GRADUATION TRANSFERS THE CLOCK AND FIXES NOTHING. GRADUATED is a TRANSFER, not a closure: the finding leaves the held set and arrives here with an owner, and its DISARM stays 2.0.0_SA_COO~B's own act -- disarming is not disposing (R-19/R-21). No part of this row's substance is re-decided by the adjudicator.",
 "owner": "2.0.0_SA_COO~B",
 "round": "v6",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~B",
  "round": "v6"
 },
 "closed": false
}
```

```json
{
 "id": "IRPT_BCKEND-W3-S47",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "BLOCKING",
 "hazard_standing": "INERT",
 "mechanism": "IB-rtf-4 arm (d)/R61-AC1: `terraform fmt -check -diff` on the regenerated infra/aws/terraform/modules/opal_name/generated_locals.tf is NOT clean (rc=3, map-literal `=` alignment only) -- and this is PRE-EXISTING in the generator's own HCL rendering, not introduced by this order's registry-hash-only regen: the IDENTICAL check against the git-blob-pinned pre-regen file (958d6a8e94:infra/aws/terraform/modules/opal_name/generated_locals.tf, blob 6199adb8ec7e0d55ae88bfaf42a1441bfb83b85f) fails identically (rc=3, same alignment diff). Fixing it needs a lib/opal_naming.py rendering-function edit, which this order's BOUNDS forbid (registry/generator owner's to fix, Rule 30). Because the acceptance criterion's token prints only when EVERY arm holds, R61-AC1 grades FAIL by output on this one sub-bullet alone -- every other arm (a)/(b)/(c)/(e) and the rest of (d) (validate clean, plan byte-identica",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-W3-S47",
  "surfaced by 0.9.0_WK_IRPT_BCKEND~3; adjudicated at L9 round 6 by 3.0.0_SA_CVO at HEAD bac07f66dc",
  "round 6 terminal: 0 open TOs of 75 by the gate's own proof read"
 ],
 "remedy": "WHAT THE ROW ESTABLISHES, in its own words: \"IB-rtf-4 arm (d)/R61-AC1: `terraform fmt -check -diff` on the regenerated infra/aws/terraform/modules/opal_name/generated_locals.tf is NOT clean (rc=3, map-literal `=` alignment only) -- and this is PRE-EXISTING in the generator's own HCL rendering, not introduced by this order's registry-hash-only regen: the IDENTICAL check against the git-blob-pinned pre-regen file (958d6a8e94:infra/aws/terraform/modules/opal_name/generated_locals.tf, blob 6199adb8ec7e0d55ae88bfaf42a1441bfb83b85f) fails identically (rc=3, same alignment diff). Fixing it needs a lib/opal_naming.py rendering-function edit, whi\" \u26d4 THIS GRADUATION TRANSFERS THE CLOCK AND FIXES NOTHING. GRADUATED is a TRANSFER, not a closure: the finding leaves the held set and arrives here with an owner, and its DISARM stays 1.0.0_SA_CTO's own act -- disarming is not disposing (R-19/R-21). No part of this row's substance is re-decided by the adjudicator.",
 "owner": "1.0.0_SA_CTO",
 "round": "v6",
 "remediation": {
  "state": "OPEN",
  "owner": "1.0.0_SA_CTO",
  "round": "v6"
 },
 "closed": false
}
```

```json
{
 "id": "IRPT_BCKEND-W4-S39",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "mechanism": "The population moved wider than this order's own face names at the cut: a fresh census (live Code.Location, not the S3 artifact bucket) found 10 declared+served members across 3 functions (ids.py on irpt-performance-adapter/irpt-narrative/irpt-holdings; data/custodian_key_seam.json on all 7 non-intake-poller, non-directory-refresh functions) with NO staged_from declaration at all -- a NEW class introduced by IB-rte-6's manual deploy (row W1-S25's own seam wiring) after IB-rte-4's 147-member census was taken, never previously rowed.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-W4-S39",
  "surfaced by 0.9.0_WK_IRPT_BCKEND~4; adjudicated at L9 round 6 by 3.0.0_SA_CVO at HEAD bac07f66dc",
  "round 6 terminal: 0 open TOs of 75 by the gate's own proof read"
 ],
 "remedy": "WHAT THE ROW ESTABLISHES, in its own words: \"The population moved wider than this order's own face names at the cut: a fresh census (live Code.Location, not the S3 artifact bucket) found 10 declared+served members across 3 functions (ids.py on irpt-performance-adapter/irpt-narrative/irpt-holdings; data/custodian_key_seam.json on all 7 non-intake-poller, non-directory-refresh functions) with NO staged_from declaration at all -- a NEW class introduced by IB-rte-6's manual deploy (row W1-S25's own seam wiring) after IB-rte-4's 147-member census was taken, never previously rowed.\" \u26d4 THIS GRADUATION TRANSFERS THE CLOCK AND FIXES NOTHING. GRADUATED is a TRANSFER, not a closure: the finding leaves the held set and arrives here with an owner, and its DISARM stays 2.0.0_SA_COO~B's own act -- disarming is not disposing (R-19/R-21). No part of this row's substance is re-decided by the adjudicator.",
 "owner": "2.0.0_SA_COO~B",
 "round": "v6",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~B",
  "round": "v6"
 },
 "closed": false
}
```

```json
{
 "id": "IRPT_BCKEND-W4-S40",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "mechanism": "18 EXISTING staged_from declarations across 7 functions (served.py x7, loaders.py x7, ids.py x4) were STALE: each pin resolved to content that no longer matches the LIVE DEPLOYED Lambda's own served bytes for that member, because the shared frontier files (_authz/served.py, _authz/loaders.py, _ids/ids.py) were edited AFTER the pin was set (by IB-rte-6's own projection-seam wiring, row W1-S25) and the declaration was never repointed -- a rebuild from the unmodified manifest would have silently SHIPPED THE OLD CONTENT, regressing a live function's behaviour without any build error.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-W4-S40",
  "surfaced by 0.9.0_WK_IRPT_BCKEND~4; adjudicated at L9 round 6 by 3.0.0_SA_CVO at HEAD bac07f66dc",
  "round 6 terminal: 0 open TOs of 75 by the gate's own proof read"
 ],
 "remedy": "WHAT THE ROW ESTABLISHES, in its own words: \"18 EXISTING staged_from declarations across 7 functions (served.py x7, loaders.py x7, ids.py x4) were STALE: each pin resolved to content that no longer matches the LIVE DEPLOYED Lambda's own served bytes for that member, because the shared frontier files (_authz/served.py, _authz/loaders.py, _ids/ids.py) were edited AFTER the pin was set (by IB-rte-6's own projection-seam wiring, row W1-S25) and the declaration was never repointed -- a rebuild from the unmodified manifest would have silently SHIPPED THE OLD CONTENT, regressing a live function's behaviour without any build error.\" \u26d4 THIS GRADUATION TRANSFERS THE CLOCK AND FIXES NOTHING. GRADUATED is a TRANSFER, not a closure: the finding leaves the held set and arrives here with an owner, and its DISARM stays 2.0.0_SA_COO~B's own act -- disarming is not disposing (R-19/R-21). No part of this row's substance is re-decided by the adjudicator.",
 "owner": "2.0.0_SA_COO~B",
 "round": "v6",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~B",
  "round": "v6"
 },
 "closed": false
}
```

```json
{
 "id": "IRPT_BCKEND-W4-S41",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "irpt-directory-search was redeployed at 2026-09-19T05:29:38Z -- 29 seconds before this order's own final graded battery run started -- by a SIBLING worker's in-flight commit (0.9.0_WK_IRPT_BCKEND~1, cell IB-rtf-2, commit b3a148044fa5699073e110126d0e6fc7d6b4fed5, editing the SAME shared _authz/enforce.py and _authz/served.py this order's own cell also declares from), moving this order's own population mid-run: an EARLIER run of this order's battery (minutes before) read enforce.py/served.py for this one function as resolvable; the FINAL graded run reads them TRACKED-ELSEWHERE-MISMATCH (canonical named, content differs -- NOT canonical-absent) because the sibling's edited content is not yet reachable from this branch's HEAD.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-W4-S41",
  "surfaced by 0.9.0_WK_IRPT_BCKEND~4; adjudicated at L9 round 6 by 3.0.0_SA_CVO at HEAD bac07f66dc",
  "round 6 terminal: 0 open TOs of 75 by the gate's own proof read"
 ],
 "remedy": "WHAT THE ROW ESTABLISHES, in its own words: \"irpt-directory-search was redeployed at 2026-09-19T05:29:38Z -- 29 seconds before this order's own final graded battery run started -- by a SIBLING worker's in-flight commit (0.9.0_WK_IRPT_BCKEND~1, cell IB-rtf-2, commit b3a148044fa5699073e110126d0e6fc7d6b4fed5, editing the SAME shared _authz/enforce.py and _authz/served.py this order's own cell also declares from), moving this order's own population mid-run: an EARLIER run of this order's battery (minutes before) read enforce.py/served.py for this one function as resolvable; the FINAL graded run reads them TRACKED-ELSEWHERE-MISMATCH (canonica\" \u26d4 THIS GRADUATION TRANSFERS THE CLOCK AND FIXES NOTHING. GRADUATED is a TRANSFER, not a closure: the finding leaves the held set and arrives here with an owner, and its DISARM stays 2.0.0_SA_COO~B's own act -- disarming is not disposing (R-19/R-21). No part of this row's substance is re-decided by the adjudicator.",
 "owner": "2.0.0_SA_COO~B",
 "round": "v6",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~B",
  "round": "v6"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "2.0.0_SA_COO~B",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-W4-S42",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "irpt-holdings :: enforce.py has no staged_from entry at all (a local, tracked-at-path fork, W1-S29's known divergence) so this cell's census classes it PIN-STALE-SERVED-DIVERGED-FROM-HEAD against the SHARED _authz/enforce.py at HEAD and this order's remedy (a manifest re-pin) leaves it untouched by construction -- re-filed here as the SAME finding's own re-pin-cell classification, not a new fact.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-W4-S42",
  "surfaced by 0.9.0_WK_IRPT_BCKEND~4; adjudicated at L9 round 6 by 3.0.0_SA_CVO at HEAD bac07f66dc",
  "round 6 terminal: 0 open TOs of 75 by the gate's own proof read"
 ],
 "remedy": "WHAT THE ROW ESTABLISHES, in its own words: \"irpt-holdings :: enforce.py has no staged_from entry at all (a local, tracked-at-path fork, W1-S29's known divergence) so this cell's census classes it PIN-STALE-SERVED-DIVERGED-FROM-HEAD against the SHARED _authz/enforce.py at HEAD and this order's remedy (a manifest re-pin) leaves it untouched by construction -- re-filed here as the SAME finding's own re-pin-cell classification, not a new fact.\" \u26d4 THIS GRADUATION TRANSFERS THE CLOCK AND FIXES NOTHING. GRADUATED is a TRANSFER, not a closure: the finding leaves the held set and arrives here with an owner, and its DISARM stays 1.0.0_SA_CTO's own act -- disarming is not disposing (R-19/R-21). No part of this row's substance is re-decided by the adjudicator.",
 "owner": "1.0.0_SA_CTO",
 "round": "v6",
 "remediation": {
  "state": "OPEN",
  "owner": "1.0.0_SA_CTO",
  "round": "v6"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "1.0.0_SA_CTO",
  "at": null
 }
}
```

```json
{
 "id": "IRPT_BCKEND-W4-S43",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "build-and-upload.sh's own comment claims passing SHA256 to the JSON tool via environment variable is already MSYS-safe against the leading-'/' base64-to-Windows-path mangle it names for CLI args; measured this run, the SAME mangle hit the env-var path too for one value (irpt-performance-adapter's artifact_sha256, which happens to start '/C', triggering MSYS's single-letter drive heuristic) and was written into the real committed lambda-source-map.json before being caught and corrected this same commit.",
 "evidence": [
  "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md#IRPT_BCKEND-W4-S43",
  "surfaced by 0.9.0_WK_IRPT_BCKEND~4; adjudicated at L9 round 6 by 3.0.0_SA_CVO at HEAD bac07f66dc",
  "round 6 terminal: 0 open TOs of 75 by the gate's own proof read"
 ],
 "remedy": "WHAT THE ROW ESTABLISHES, in its own words: \"build-and-upload.sh's own comment claims passing SHA256 to the JSON tool via environment variable is already MSYS-safe against the leading-'/' base64-to-Windows-path mangle it names for CLI args; measured this run, the SAME mangle hit the env-var path too for one value (irpt-performance-adapter's artifact_sha256, which happens to start '/C', triggering MSYS's single-letter drive heuristic) and was written into the real committed lambda-source-map.json before being caught and corrected this same commit.\" \u26d4 THIS GRADUATION TRANSFERS THE CLOCK AND FIXES NOTHING. GRADUATED is a TRANSFER, not a closure: the finding leaves the held set and arrives here with an owner, and its DISARM stays 2.0.0_SA_COO~B's own act -- disarming is not disposing (R-19/R-21). No part of this row's substance is re-decided by the adjudicator.",
 "owner": "2.0.0_SA_COO~B",
 "round": "v6",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~B",
  "round": "v6"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "2.0.0_SA_COO~B",
  "at": null
 }
}
```

## Round-7 L9 carriers for the nine GRADUATED items (3.0.0_SA_CVO, 2026-09-21T04:26Z)

```json
{
 "id": "IRPT_BCKEND-W1-S42",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "Export receipt resolves from tenant + caller export_id only; the key-template alignment the arm named is a different shape from what the route actually reads. Round-8 export-contract work.",
 "evidence": [
  "Round-7 L9 by 3.0.0_SA_CVO; item dispositioned GRADUATED in adjudications/ADJUDICATION_v3.md.",
  "The investigation row for IRPT_BCKEND-W1-S42 carries the measurement; this carrier does not restate it."
 ],
 "remedy": "Carried to round 8 by the named owner. This carrier exists so the item's clock is representable; it is not a closure.",
 "owner": "2.0.0_SA_COO~B",
 "round": "v7",
 "disarm": {
  "state": "ARMED",
  "owner": "2.0.0_SA_COO~B",
  "at": null
 },
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~B",
  "round": "v7"
 },
 "closed": false
}
```

```json
{
 "id": "IRPT_BCKEND-W1-S43",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "BLOCKING",
 "hazard_standing": "ARMED",
 "mechanism": "Deployed submit_export raises NOT_READY, so the submit -> receipt round trip is unwired on the served path. The receipt CONTRACT is proven; the producer is not. Round-8.",
 "evidence": [
  "Round-7 L9 by 3.0.0_SA_CVO; item dispositioned GRADUATED in adjudications/ADJUDICATION_v3.md.",
  "The investigation row for IRPT_BCKEND-W1-S43 carries the measurement; this carrier does not restate it."
 ],
 "remedy": "Carried to round 8 by the named owner. This carrier exists so the item's clock is representable; it is not a closure.",
 "owner": "2.0.0_SA_COO~B",
 "round": "v7",
 "disarm": {
  "state": "ARMED",
  "owner": "2.0.0_SA_COO~B",
  "at": null
 },
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~B",
  "round": "v7"
 },
 "closed": false
}
```

```json
{
 "id": "IRPT_BCKEND-W1-S45",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "A real plan on three roots this order neither granted nor touched shows each with changes -- plan noise on untouched roots defeats the never-widen scope check as written. Round-8.",
 "evidence": [
  "Round-7 L9 by 3.0.0_SA_CVO; item dispositioned GRADUATED in adjudications/ADJUDICATION_v3.md.",
  "The investigation row for IRPT_BCKEND-W1-S45 carries the measurement; this carrier does not restate it."
 ],
 "remedy": "Carried to round 8 by the named owner. This carrier exists so the item's clock is representable; it is not a closure.",
 "owner": "2.0.0_SA_COO~B",
 "round": "v7",
 "disarm": {
  "state": "ARMED",
  "owner": "2.0.0_SA_COO~B",
  "at": null
 },
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~B",
  "round": "v7"
 },
 "closed": false
}
```

```json
{
 "id": "IRPT_BCKEND-W2-S61",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "The arm named a battery to REUSE; a battery was re-authored under the same assignee instead. The evidence stands, the instruction-versus-artifact gap does not. Round-8.",
 "evidence": [
  "Round-7 L9 by 3.0.0_SA_CVO; item dispositioned GRADUATED in adjudications/ADJUDICATION_v3.md.",
  "The investigation row for IRPT_BCKEND-W2-S61 carries the measurement; this carrier does not restate it."
 ],
 "remedy": "Carried to round 8 by the named owner. This carrier exists so the item's clock is representable; it is not a closure.",
 "owner": "2.0.0_SA_COO~B",
 "round": "v7",
 "disarm": {
  "state": "ARMED",
  "owner": "2.0.0_SA_COO~B",
  "at": null
 },
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~B",
  "round": "v7"
 },
 "closed": false
}
```

```json
{
 "id": "IRPT_BCKEND-W3-S48",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "A second firm-keyed dict (handler.py RECORDED_LABELS) shares the retired id space this cell was cut to reconcile and sits OUTSIDE the confined edit: locally correct, globally incomplete. Round-8.",
 "evidence": [
  "Round-7 L9 by 3.0.0_SA_CVO; item dispositioned GRADUATED in adjudications/ADJUDICATION_v3.md.",
  "The investigation row for IRPT_BCKEND-W3-S48 carries the measurement; this carrier does not restate it."
 ],
 "remedy": "Carried to round 8 by the named owner. This carrier exists so the item's clock is representable; it is not a closure.",
 "owner": "2.0.0_SA_COO~B",
 "round": "v7",
 "disarm": {
  "state": "ARMED",
  "owner": "2.0.0_SA_COO~B",
  "at": null
 },
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~B",
  "round": "v7"
 },
 "closed": false
}
```

```json
{
 "id": "IRPT_BCKEND-W3-S50",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "Inflection's performance route fails on an S3 404 in _authz/served.py::enforcer_for, UPSTREAM of route_for and outside this cell's bound. The remedy is the FWD-11 bucket rectification, co-held. Round-8.",
 "evidence": [
  "Round-7 L9 by 3.0.0_SA_CVO; item dispositioned GRADUATED in adjudications/ADJUDICATION_v3.md.",
  "The investigation row for IRPT_BCKEND-W3-S50 carries the measurement; this carrier does not restate it."
 ],
 "remedy": "Carried to round 8 by the named owner. This carrier exists so the item's clock is representable; it is not a closure.",
 "owner": "1.0.0_SA_CTO",
 "round": "v7",
 "disarm": {
  "state": "ARMED",
  "owner": "1.0.0_SA_CTO",
  "at": null
 },
 "remediation": {
  "state": "OPEN",
  "owner": "1.0.0_SA_CTO",
  "round": "v7"
 },
 "closed": false
}
```

```json
{
 "id": "IRPT_BCKEND-W4-S45",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "build-and-upload.sh from /c/ was REFUSED at the index-sourced manifest gate (NO BLOB for three files at a pin). A build recipe the order states literally does not run as written. Round-8.",
 "evidence": [
  "Round-7 L9 by 3.0.0_SA_CVO; item dispositioned GRADUATED in adjudications/ADJUDICATION_v3.md.",
  "The investigation row for IRPT_BCKEND-W4-S45 carries the measurement; this carrier does not restate it."
 ],
 "remedy": "Carried to round 8 by the named owner. This carrier exists so the item's clock is representable; it is not a closure.",
 "owner": "2.0.0_SA_COO~B",
 "round": "v7",
 "disarm": {
  "state": "ARMED",
  "owner": "2.0.0_SA_COO~B",
  "at": null
 },
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~B",
  "round": "v7"
 },
 "closed": false
}
```

```json
{
 "id": "IRPT_BCKEND-W4-S46",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "Plans on export and performance each show an aws_lambda_function update whose before/after source_code_hash do not match this act -- the same untouched-root plan-noise class as W1-S45. Round-8.",
 "evidence": [
  "Round-7 L9 by 3.0.0_SA_CVO; item dispositioned GRADUATED in adjudications/ADJUDICATION_v3.md.",
  "The investigation row for IRPT_BCKEND-W4-S46 carries the measurement; this carrier does not restate it."
 ],
 "remedy": "Carried to round 8 by the named owner. This carrier exists so the item's clock is representable; it is not a closure.",
 "owner": "2.0.0_SA_COO~B",
 "round": "v7",
 "disarm": {
  "state": "ARMED",
  "owner": "2.0.0_SA_COO~B",
  "at": null
 },
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~B",
  "round": "v7"
 },
 "closed": false
}
```

```json
{
 "id": "IRPT_BCKEND-W4-S47",
 "project": "IRPT_BCKEND",
 "fabric": "laptop",
 "class": "BLOCKING",
 "hazard_standing": "ARMED",
 "mechanism": "Get-PSDrive C reads Free=0 bytes -- a LITERAL zero, not a low figure -- on the only filesystem this box exposes. This is FABRIC LOAD, not project work, and its owner is the fabric seat.",
 "evidence": [
  "Round-7 L9 by 3.0.0_SA_CVO; item dispositioned GRADUATED in adjudications/ADJUDICATION_v3.md.",
  "The investigation row for IRPT_BCKEND-W4-S47 carries the measurement; this carrier does not restate it."
 ],
 "remedy": "Carried to round 8 by the named owner. This carrier exists so the item's clock is representable; it is not a closure.",
 "owner": "0.0.0_AB_MSTR",
 "round": "v7",
 "disarm": {
  "state": "DISARMED",
  "owner": "0.0.0_AB_MSTR",
  "at": "2026-09-21T04:52Z"
 },
 "remediation": {
  "state": "OPEN",
  "owner": "0.0.0_AB_MSTR",
  "round": "v7"
 },
 "closed": false
}
```
