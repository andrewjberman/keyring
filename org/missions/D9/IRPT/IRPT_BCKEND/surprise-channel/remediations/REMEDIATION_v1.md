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
