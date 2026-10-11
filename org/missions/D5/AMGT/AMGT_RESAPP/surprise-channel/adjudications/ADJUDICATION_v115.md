# AMGT_RESAPP -- round 95 L8/L9 adjudication, packet FINAL (dell1)

<sweep_watermark>2026-10-11T18:50Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-11T18:50:00Z. L8 packet: 2.0.0_SA_COO~R1 msg 4071,
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round95/DRAIN_END_PACKET.md @51ccaef9d4 (blob ee9fbcae46, verified).
5 orders terminal; aa-5 redeploy TmeKvn83 held. L9 HOLDS on this seat's own runs (C-S83). The one JUDGMENT, aa-3 AC2, is MET (C-S84),
with each alternative's closure stated as measured or inferred; C-S82 dismissed on it (C-S85). REMEDIATION_v38 S24 and S26 closed REMEDIATED
(C-S86). 4 rows swept since v114 (watermark 2026-10-11T15:55Z; 4 of 1068 investigation rows after it): all dismissed (W391-S1, S2 disarmed).

```json
[
  {
    "id": "AMGT_RESAPP-D1-C-S83",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T18:50:00Z",
    "one_line": "L9 read of the round-95 packet section 2: HOLDS on this seat's own runs at box/dell1 HEAD df84df401e. Live CodeSha256 TmeKvn83XnePF4RrJUQKIpbzYdH4VnCmvyXePbs3KB8= (LastModified 18:03:44Z). aa-5: r95_classification_census.py --where deployed K1-K6 PASS (ranked rows 2, series 2, chatter 3 withheld with 'classification not available for this listing'; K5 186 and 186 unchanged; K6 by-ticker 2 of 2 clean), R95 CLASSIFICATION CENSUS: YES; r95_casing_deployed.py D1 'CSL Ltd', D2 'JD.com Inc', D3 'Sanofi' / 'ASML Holding NV', YES; this seat's direct reads: the rank timeseries by ticker serves SAN FP 'Sanofi' and CSL AU 'CSL Ltd' with classification null and the reason, BA US unchanged, and neither overlay carries a classification. No-regression: R94 NAME CENSUS YES; R92 MINOR-UNIT CENSUS YES; this seat's census 0 minor-unit rows (155 with a currency); R89 PEERS DEPLOYED and DEPLOYED CLOSE (dossier/12) YES. aa-1: r95_reverify_idempotent.py I1-I6 PASS, r94_rescale_table.py YES. lib/research/api/tests + filings 1304 passed. RA1's compare (AA5_POST_APPLY_COMPARE_20261011.json): 527 requests, status moved 0, missing 0; this seat counts 43 name-class field diffs over 13 requests, every one on SAN FP or CSL AU, and 36 clock fields (generated_at 34, read_at 2), 0 outside -- the packet's '39 paths' and '28 clocks' count at another grain.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "L9 read of the round-95 packet section 2: HOLDS on this seat's own runs at box/dell1 HEAD df84df401e. Live CodeSha256 TmeKvn83XnePF4RrJUQKIpbzYdH4VnCmvyXePbs3KB8= (LastModified 18:03:44Z). aa-5: r95_classification_census.py --where deployed K1-K6 PASS (ranked rows 2, series 2, chatter 3 withheld with 'classification not available for this listing'; K5 186 and 186 unchanged; K6 by-ticker 2 of 2 clean), R95 CLASSIFICATION CENSUS: YES; r95_casing_deployed.py D1 'CSL Ltd', D2 'JD.com Inc', D3 'Sanofi' / 'ASML Holding NV', YES; this seat's direct reads: the rank timeseries by ticker serves SAN FP 'Sanofi' and CSL AU 'CSL Ltd' with classification null and the reason, BA US unchanged, and neither overlay carries a classification. No-regression: R94 NAME CENSUS YES; R92 MINOR-UNIT CENSUS YES; this seat's census 0 minor-unit rows (155 with a currency); R89 PEERS DEPLOYED and DEPLOYED CLOSE (dossier/12) YES. aa-1: r95_reverify_idempotent.py I1-I6 PASS, r94_rescale_table.py YES. lib/research/api/tests + filings 1304 passed. RA1's compare (AA5_POST_APPLY_COMPARE_20261011.json): 527 requests, status moved 0, missing 0; this seat counts 43 name-class field diffs over 13 requests, every one on SAN FP or CSL AU, and 36 clock fields (generated_at 34, read_at 2), 0 outside -- the packet's '39 paths' and '28 clocks' count at another grain.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO ran deliverables/2.0.0_SA_COO~R1/round95_prep/checks/r95_classification_census.py --where deployed, r95_casing_deployed.py, r95_reverify_idempotent.py: YES x3",
        "3.0.0_SA_CVO ran round94 r94_name_census.py --where deployed, r94_rescale_table.py, r94_display_name.py; round92 r92_minor_unit_census.py; r89 pair; org/tier1_exec/3.0.0_SA_CVO/deliverables/checks/amgt_minor_unit_census.py: all pass",
        "3.0.0_SA_CVO lambda invoke GET /lead-panel/timeseries/TRENDING/PRICE?tickers=SAN FP,CSL AU,BA US and /security/{CSL_AU,SAN_FP}_Equity/overlay 2026-10-11T18:4xZ",
        "3.0.0_SA_CVO read deliverables/0.7.0_AE_CloudOps~RA1/AA5_POST_APPLY_COMPARE_20261011.json: 79 diffs = 43 name + 36 noise"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "L9 read of the round-95 packet section 2: HOLDS on this seat's own runs at box/dell1 HEAD df84df401e. Live CodeSha256 TmeKvn83XnePF4RrJUQKIpbzYdH4VnCmvyXePbs3KB8= (LastModified 18:03:44Z). aa-5: r95_classification_census.py --where deployed K1-K6 PASS (ranked rows 2, series 2, chatter 3 withheld with 'classification not available for this listing'; K5 186 and 186 unchanged; K6 by-ticker 2 of 2 clean), R95 CLASSIFICATION CENSUS: YES; r95_casing_deployed.py D1 'CSL Ltd', D2 'JD.com Inc', D3 'Sanofi' / 'ASML Holding NV', YES; this seat's direct reads: the rank timeseries by ticker serves SAN FP 'Sanofi' and CSL AU 'CSL Ltd' with classification null and the reason, BA US unchanged, and neither overlay carries a classification. No-regression: R94 NAME CENSUS YES; R92 MINOR-UNIT CENSUS YES; this seat's census 0 minor-unit rows (155 with a currency); R89 PEERS DEPLOYED and DEPLOYED CLOSE (dossier/12) YES. aa-1: r95_reverify_idempotent.py I1-I6 PASS, r94_rescale_table.py YES. lib/research/api/tests + filings 1304 passed. RA1's compare (AA5_POST_APPLY_COMPARE_20261011.json): 527 requests, status moved 0, missing 0; this seat counts 43 name-class field diffs over 13 requests, every one on SAN FP or CSL AU, and 36 clock fields (generated_at 34, read_at 2), 0 outside -- the packet's '39 paths' and '28 clocks' count at another grain."
  },
  {
    "id": "AMGT_RESAPP-D1-C-S84",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T18:50:00Z",
    "one_line": "JUDGMENT AMGT_RESAPP.TO-AMGT-aa-3 AC2 (TO-AMGT-aa-3, the reading's cause follows from its evidence and its denominators): MET. RA1's CAUSE DEV-PROXY follows by elimination from denominatored evidence. Every AWS-side alternative is closed by MEASUREMENT (function, authorizer, API integration, CloudFront with Lambda@Edge, concurrency), and so is one the reading did not name (the walker or browser layer). The dev proxy as the source is closed by INFERENCE only, and the reading names the deciding source it did not read (the dev server's console for 15:34Z-15:44Z), which meets AC2's own standard. This seat's re-drive did not recur the 500 (0 of 80 through the proxy unauthenticated; 0 of 80 direct invokes).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "Alternatives named and how each is closed. (1) FUNCTION error, throttle or timeout: closed by MEASUREMENT -- RA1's Errors 0 and Throttles 0 over 291 invocations; this seat's read of /aws/lambda/opal-amgt-scoped-api 15:34Z-15:44Z: 922 lines, 0 ERROR/Traceback/timeout/runtime-exit, 217 REPORT lines with per-minute maxima 0.3-23.4 s, none at the 29 s timeout; this seat's 80 direct invokes of /security/{ROG,BA}/compare on TmeKvn83 at 18:33Z: 80 x 200, mean 0.26 s, max 0.46 s. (2) the HTTP API's REQUEST authorizer: closed by MEASUREMENT -- RA1's authorizer Errors 0 and Throttles 0 over 218, and the API's 5xx 0, which counts an authorizer failure. (3) API Gateway integration or timeout: closed by MEASUREMENT -- 5xx 0 over a Count of 266. (4) CloudFront, including the viewer-request Lambda@Edge: closed by MEASUREMENT -- 5xxErrorRate 0 over 405 requests (a Lambda@Edge error counts as 5xx), and this seat additionally read /aws/lambda/us-east-1.auth-validator-edge over the window, the regional log RA1 left unread: 990 lines, 0 error-like (other regions' edge logs not read). (5) concurrency: closed by MEASUREMENT -- reserved none, peak 10 of 978 unreserved. (6) the walker or browser layer (a guard abort or a locally stubbed answer), an alternative the reading does not name: closed by MEASUREMENT here -- the walk recorded 0 guard aborts, its local stubs answer telemetry paths only, and the netlog row is a received status 500, not an abort. (7) the DEV PROXY as the source: closed by INFERENCE only -- it is the one layer left, and the installed Vite's handler answers any proxy error with an empty-body 500 (read in code); but the proxy's console line was not read, the two bodies were not recorded, no request id or time exists, and the sub-cause (reset, timeout, socket) is unnamed. This seat's re-drive did not recur the 500: 80 unauthenticated calls through http://localhost:5174 answered 401 (as did 80 straight to CloudFront), which crosses the proxy and the edge but never reaches the function, so it cannot test the slow-answer candidate; the authenticated proxy path was not re-driven at a rate. The slow-answer candidate is weakened, not closed: /compare itself answers in about 0.26 s, and in 15:37Z-15:38Z, around the ROG Model step, no invocation exceeded 7.3 s.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "deliverables/0.7.0_AE_CloudOps~RA1/C-S82_COMPARE_500_READING_20261011.md @dc5c1e60b2 (read whole)",
        "3.0.0_SA_CVO read-only probe (session scratch compare_repro.py) 2026-10-11T18:33:38Z-18:33:49Z: direct invoke 80 x 200; http://localhost:5174 80 x 401; https://d2n2nzpeqf34ge.cloudfront.net 80 x 401; 0 x 500",
        "3.0.0_SA_CVO logs filter_log_events 15:34Z-15:44Z: /aws/lambda/opal-amgt-scoped-api 922 lines 0 error-like, 217 REPORT; /aws/lambda/us-east-1.auth-validator-edge 990 lines 0 error-like",
        "tmp/ui-walk/20261011T153440Z summary: 0 guard aborts; netlog compare 70 x 200, 2 x 500"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "JUDGMENT AMGT_RESAPP.TO-AMGT-aa-3 AC2 (TO-AMGT-aa-3, the reading's cause follows from its evidence and its denominators): MET. RA1's CAUSE DEV-PROXY follows by elimination from denominatored evidence. Every AWS-side alternative is closed by MEASUREMENT (function, authorizer, API integration, CloudFront with Lambda@Edge, concurrency), and so is one the reading did not name (the walker or browser layer). The dev proxy as the source is closed by INFERENCE only, and the reading names the deciding source it did not read (the dev server's console for 15:34Z-15:44Z), which meets AC2's own standard. This seat's re-drive did not recur the 500 (0 of 80 through the proxy unauthenticated; 0 of 80 direct invokes)."
  },
  {
    "id": "AMGT_RESAPP-D1-C-S85",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T18:50:00Z",
    "one_line": "C-S82 (the two /compare 500s during the round-94 walk) dismissed on the AC2 grade (C-S84): the cause is the portal dev server's proxy, by elimination, with no AWS-side 5xx in any layer; PROD users do not traverse it, nothing is served wrong, and no fix is cut. The deciding source for the sub-cause stays unread; a walk that owns its dev server should send the server's output to a file.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "AMGT_RESAPP-D1-C-S82"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "C-S82 (the two /compare 500s during the round-94 walk) dismissed on the AC2 grade (C-S84): the cause is the portal dev server's proxy, by elimination, with no AWS-side 5xx in any layer; PROD users do not traverse it, nothing is served wrong, and no fix is cut. The deciding source for the sub-cause stays unread; a walk that owns its dev server should send the server's output to a file.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "adjudication row AMGT_RESAPP-D1-C-S84",
        "deliverables/0.7.0_AE_CloudOps~RA1/C-S82_COMPARE_500_READING_20261011.md"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "C-S82 (the two /compare 500s during the round-94 walk) dismissed on the AC2 grade (C-S84): the cause is the portal dev server's proxy, by elimination, with no AWS-side 5xx in any layer; PROD users do not traverse it, nothing is served wrong, and no fix is cut. The deciding source for the sub-cause stays unread; a walk that owns its dev server should send the server's output to a file."
  },
  {
    "id": "AMGT_RESAPP-D1-C-S86",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T18:50:00Z",
    "one_line": "REMEDIATION_v38 D1-S24 and D1-S26 closed: disarm ARMED -> DISARMED and remediation OPEN -> REMEDIATED, nothing else moved. S24: r95_reverify_idempotent.py I1-I2 keep 3 of 3 byte-equal on a second re-verification, I3 holds a figure no excerpt prints (the negative arm). S26: CSL AU serves no Carlisle field (overlay none; ranked, series and by-ticker withheld with the reason; census K1-K6). The close condition's SAN clause ('shown to be Sanofi's') is answered the other way: SAN's bare-ticker row names 'Banco Santander S.A. ADR', so by the CTO's ruling (msg 3986) SAN FP's classification is withheld too; neither security is served another company's classification.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "AMGT_RESAPP-D1-S24",
      "AMGT_RESAPP-D1-S26"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "REMEDIATION_v38 D1-S24 and D1-S26 closed: disarm ARMED -> DISARMED and remediation OPEN -> REMEDIATED, nothing else moved. S24: r95_reverify_idempotent.py I1-I2 keep 3 of 3 byte-equal on a second re-verification, I3 holds a figure no excerpt prints (the negative arm). S26: CSL AU serves no Carlisle field (overlay none; ranked, series and by-ticker withheld with the reason; census K1-K6). The close condition's SAN clause ('shown to be Sanofi's') is answered the other way: SAN's bare-ticker row names 'Banco Santander S.A. ADR', so by the CTO's ruling (msg 3986) SAN FP's classification is withheld too; neither security is served another company's classification.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO r95_reverify_idempotent.py I1-I6 PASS",
        "3.0.0_SA_CVO r95_classification_census.py K1-K6 PASS and the live reads in C-S83"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "REMEDIATION_v38 D1-S24 and D1-S26 closed: disarm ARMED -> DISARMED and remediation OPEN -> REMEDIATED, nothing else moved. S24: r95_reverify_idempotent.py I1-I2 keep 3 of 3 byte-equal on a second re-verification, I3 holds a figure no excerpt prints (the negative arm). S26: CSL AU serves no Carlisle field (overlay none; ranked, series and by-ticker withheld with the reason; census K1-K6). The close condition's SAN clause ('shown to be Sanofi's') is answered the other way: SAN's bare-ticker row names 'Banco Santander S.A. ADR', so by the CTO's ruling (msg 3986) SAN FP's classification is withheld too; neither security is served another company's classification."
  },
  {
    "id": "AMGT_RESAPP-D1-C-S87",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T18:50:00Z",
    "one_line": "D1-W391-S1 and D1-W391-S2 (BLOCKING, ARMED) dismissed, disarmed: aa-2 AMENDMENT 1 changed the round-94 check's D10 arm and the one test assertion that held the reversed rule; this seat reads r94_display_name.py 12 of 12 and lib/research/api/tests with filings 1304 passed, 0 failed.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "AMGT_RESAPP-D1-W391-S1",
      "AMGT_RESAPP-D1-W391-S2"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W391-S1 and D1-W391-S2 (BLOCKING, ARMED) dismissed, disarmed: aa-2 AMENDMENT 1 changed the round-94 check's D10 arm and the one test assertion that held the reversed rule; this seat reads r94_display_name.py 12 of 12 and lib/research/api/tests with filings 1304 passed, 0 failed.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows AMGT_RESAPP-D1-W391-S1, D1-W391-S2",
        "aa-2 AMENDMENT 1 @db3d3a7787",
        "3.0.0_SA_CVO r94_display_name.py 12 of 12; pytest 1304 passed"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W391-S1 and D1-W391-S2 (BLOCKING, ARMED) dismissed, disarmed: aa-2 AMENDMENT 1 changed the round-94 check's D10 arm and the one test assertion that held the reversed rule; this seat reads r94_display_name.py 12 of 12 and lib/research/api/tests with filings 1304 passed, 0 failed."
  },
  {
    "id": "AMGT_RESAPP-D1-C-S88",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T18:50:00Z",
    "one_line": "D1-W391-S3 and D1-W391-S4 (INERT) dismissed: the re-seated worktree's empty portal submodule skipped two model-words tests (this seat's run in the base checkout, where portal is present, reads 1304 passed and 0 failed), and the recorded invocation path differs from the re-seat path by the re-seat only.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "AMGT_RESAPP-D1-W391-S3",
      "AMGT_RESAPP-D1-W391-S4"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W391-S3 and D1-W391-S4 (INERT) dismissed: the re-seated worktree's empty portal submodule skipped two model-words tests (this seat's run in the base checkout, where portal is present, reads 1304 passed and 0 failed), and the recorded invocation path differs from the re-seat path by the re-seat only.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows AMGT_RESAPP-D1-W391-S3, D1-W391-S4"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W391-S3 and D1-W391-S4 (INERT) dismissed: the re-seated worktree's empty portal submodule skipped two model-words tests (this seat's run in the base checkout, where portal is present, reads 1304 passed and 0 failed), and the recorded invocation path differs from the re-seat path by the re-seat only."
  }
]
```
