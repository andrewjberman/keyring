# IRPT_BCKEND -- ROUND 11 L10 remediation slug

Author: 3.0.0_SA_CVO~B. ONE recipient: 1.0.0_SA_CTO.
Round v11; filename v5 is the rollover counter.
Input: ledger/IRPT_BCKEND_ROUND11_L8_COMPILE.md@715b359db2.
L9: co-committed ADJUDICATION_v8.md, nine rows C-S169..177 and one formal judgment.

## Read first

**R107-AC3 FAIL. CAPTURE STAYS HELD.**
The R10 human-wait and foreign-retry counterexamples are fixed. A different final-await gap
survives: the observer latches while storageState is awaited, AFTER the last refusal check,
then the helper writes and prints success. Source: capture-session.cjs:364-369@0d0c8cdc4d,
published blob ded60502 / sha256 f03666ef. C-S170 reproduces with a single-difference pair.
C-S171 separately demonstrates new over-refusal of non-navigation foreign resource responses.

Unmodified R10: 6/6 intended post-repair outcomes; R9: 6/6; R8: 3/3 guard outcomes.
Own unchanged R91 four safe arms and R101 three safe arms all rc0. None covers the final-await
gap. The new R11 diagnostic has 11 cases; its exit0 means defects reproduced, NEVER approval.
No live capture, host action, credentials, publication replay, IAM write or CVO cloud call occurred.

## Gate and bounded progress

Own gate census: 0 open /95 orders. Intake: 338 worker items, two new items W13-S1/S2;
both dispositioned here. All 336 prior items remain dispositioned. Bound proof receiving-check
ACCEPT and explicit-id check VALID; packet UNCHECKED, judged through the actual evidence.
The commit gate must admit the resulting 0/338 undispositioned census without override.

Five new OPEN remediation rows: C-S170/C-S171 ARMED; W13-S1/W13-S2/C-S174 INERT.
Only two existing REMEDIATION_v4 clocks close: C-S160 metadata correction and C-S162 prospective
criterion retirement. No regrade of R102-AC2: its issued-vintage NOT_EVALUATED stays.
C-S158/C-S159's original cases are repaired but no wholesale lifecycle closure is inferred.
C-S153/C-S127/older host-byte clocks and the 164 older stale-row carry remain; no bulk close.

W13-S1's authoring conflict requires explicit future retry semantics; 404 and generic non-timeout
errors also retry, not just ordinary login trouble. Unmodified R8's password label stops at the
missing-instance guard and cannot prove password retry.
W13-S2: the gate correctly revokes terminal orders, per spine and source. The face required pending
on STOP but worker flipped complete before the publish halves existed. Remedy the order lifecycle;
this evidence does not warrant making finished orders standing grants.

## Publish versus proof

Packet was corrected BEFORE halves: 5d30a76a; COO cf4da2c5b3, CTO 993ff1fad3.
Published event 60bab95e58 / drain db25f4a39c records f03666ef readback, one cjs key, sh unchanged,
README hash updated in the same act, ledger CLOSED. COO independently reports fresh GET agreement.
That is not a CVO live GET and not on-host verification. Sign-off covers blast radius, not correctness.

Final proof at HEAD 8d385d1ae1 still describes pre-publish STOP, mislabels checkout hash fffef738
as git-blob hash, omits W13-S2 and keeps pre-publish result/exclusions. All 14 literal blob pins
resolve; two PENDING bindings are not an explicit final-pass record. C-S174 is metadata only.
A retained fully-merged recovery worktree C:/tmp/wk-irpt-11-13b has an uncommitted proof correction
and .scratch/; left untouched, not used as delivered evidence. Issuer owns its reconciliation.

## Coverage and next reader

FWD-2 remains SPLIT / NOT_REALIZED overall: complete served authorization matrix and authenticated
export/latency evidence are absent from this round. FWD-11 remains NOT_REALIZED overall:
the prior bucket-program closure is not the Global two-firm report/export/advisor-refusal/parity bar.
No new endpoint gap is claimed merely from these repairable existing-cell defects.

CTO: retain capture HOLD and rti-6 PARK, read the two new source defects plus explicit retry
semantics and final-pass record corrections into the next round analysis. No rollback/deploy act
is requested or performed by this CVO slug. COO recuts only after that analysis.
W10-S2 stays parked; S116/W1-S47, Andrew/CRO break-glass decision and older carries unchanged.

## New remediation rows

```json
[
  {
    "id": "IRPT_BCKEND-C-S170",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The final latch check runs before await context.storageState(); navigation events during that await can latch the observer, but the continuation proceeds directly to mkdir/write/success with no recheck.",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v8.md (co-committed)#IRPT_BCKEND-C-S170; grounded attribution carried verbatim.",
      "infra/aws/ec2/investor-reporting-export/capture-session.cjs:184-230,295-299,364-369 @0d0c8cdc4d: observer sets latched, final check precedes storageState await.",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R11_CAPTURE_LIFECYCLE_DIAGNOSTIC.cjs (co-committed): storage pair changes only the middle origin; both arms write 1 and succeed on ded60502; same result on prior c5a18898 (pre-existing unclosed window)."
    ],
    "remedy": "Keep capture held. Close the asynchronous storageState-to-write latch gap with a terminal check at the final commit boundary and discriminating foreign-during-storage/same-origin pairs; retain prior interval/retry controls and sign/publish/read back any changed bytes under a new packet.",
    "owner": "2.0.0_SA_COO~B",
    "round": "v11",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~B",
      "round": "v11"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~B",
      "at": "2026-09-22T06:40:00Z"
    }
  },
  {
    "id": "IRPT_BCKEND-C-S171",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "onRequest excludes isNavigationRequest=false, but onResponse checks only frame and URL. A main-frame foreign fetch/image/script response sets the terminal latch despite the page remaining on the portal; same-origin response succeeds.",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v8.md (co-committed)#IRPT_BCKEND-C-S171; grounded attribution carried verbatim.",
      "infra/aws/ec2/investor-reporting-export/capture-session.cjs:198-213 @0d0c8cdc4d: response lacks the navigation-request filter present on request.",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R11_CAPTURE_LIFECYCLE_DIAGNOSTIC.cjs (co-committed): response pair changes only resource origin, request.isNavigationRequest=false in both; same-origin writes=1, foreign writes=0/exit1. On old c5a18898 both succeed; new regression. Interactive foreign navigation control still refuses on ded60502."
    ],
    "remedy": "Make response observation discriminate main-frame navigation from ordinary resource responses. Require same-origin/foreign non-navigation pair to both succeed and foreign main-frame navigation to refuse; no relaxation of origin or readiness fences.",
    "owner": "2.0.0_SA_COO~B",
    "round": "v11",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~B",
      "round": "v11"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~B",
      "at": "2026-09-22T06:40:00Z"
    }
  },
  {
    "id": "IRPT_BCKEND-W13-S1",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Worker retains all prior retry reasons. Own R11 runs show the named three plus HTTP404, non-timeout navigation error, and password-present all retry then succeed. Unmodified R8 supplies no instance id and its password case never navigates, so its byte-identical output cannot adjudicate password retry.",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v8.md (co-committed)#IRPT_BCKEND-C-S172; grounded attribution carried verbatim.",
      "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md@897171eb53#IRPT_BCKEND-W13-S1.",
      "org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rtk-1.the-capture-tool-complete-lifecycle-observer-and-sticky-refusal.md@2bebd4a93c: arm (e), BOUNDS and R107-AC3(iii).",
      "infra/aws/ec2/investor-reporting-export/capture-session.cjs:235-258,333-355 @0d0c8cdc4d; generic goto catch and all readiness reasons continue.",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R11_CAPTURE_LIFECYCLE_DIAGNOSTIC.cjs (co-committed): six retry cases; three named positives plus three outside the literal list accept after a clean retry.",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R8_CAPTURE_DIAGNOSTIC.cjs: unchanged run has zero navigations for password case due to missing instance id."
    ],
    "remedy": "Resolve the issued retry taxonomy prospectively, preserving intended human login recovery and terminal foreign navigation refusal; test each allowed cause and an excluded cause, including 4xx/non-timeout errors. Do not reinterpret a frozen bar or use the pre-navigation R8 case as password-retry evidence.",
    "owner": "2.0.0_SA_COO~B",
    "round": "v11",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B",
      "round": "v11"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-W13-S2",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Worker marked complete before arm (g)'s halves existed, then a later README edit was refused as the law specifies. The source comment cited as permission describes the historical motivation for building this rule, not a new exemption for completed orders.",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v8.md (co-committed)#IRPT_BCKEND-C-S173; grounded attribution carried verbatim.",
      ".tools/owned-paths-validate.py:113-122,175-202 @4e3142cfb3: NON-TERMINAL only, and terminal orders are not standing permission.",
      "org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rtk-1.the-capture-tool-complete-lifecycle-observer-and-sticky-refusal.md@2bebd4a93c: pending-on-STOP instruction; @8d385d1ae1: complete while explicitly saying arm (g) STOPPED.",
      "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md@897171eb53#IRPT_BCKEND-W13-S2; publish commit 60bab95e58 changes README and closes ledger."
    ],
    "remedy": "Correct multi-pass order completion discipline: held required work stays pending as the face requires, and status/proof align with the final pass. Reconcile retained worker proof residue through the issuer. Preserve terminal-order grant revocation; no general gate weakening on this evidence.",
    "owner": "2.0.0_SA_COO~B",
    "round": "v11",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B",
      "round": "v11"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-C-S174",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Proof at 8d385d1ae1 and result blob ef0e9734 still exclude publish, say no halves, and claim fffef738 as git-blob sha256; actual git blob hashes f03666ef and publish ledger/README at 60bab95e58 record delivery. Proof lists W13-S1 only although W13-S2 exists. Fourteen literal blob pins resolve and match HEAD; two PENDING entries include the subsequently corrected packet.",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v8.md (co-committed)#IRPT_BCKEND-C-S174; grounded attribution carried verbatim.",
      "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~13/IRPT_BCKEND.TO-IB-rtk-1.the-capture-tool-complete-lifecycle-observer-and-sticky-refusal.proof_of_spec.json@8d385d1ae1: artifacts_produced[0], declared_exclusions, surprises.",
      "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~13/the-capture-tool-complete-lifecycle-observer-and-sticky-refusal.result.md@0d0c8cdc4d (HEAD blob ef0e973405ad9672e3e31078c20805dd18309b12).",
      "org/critical_paths/change_management/20260922T0405Z_irpt-rtk-1-capture-tool-publish_deploy_completion.md@60bab95e58: closed readback event.",
      "CVO Buffer-based hash read: disk fffef738, git f03666ef; replacing CRLF with LF makes disk bytes equal git text. Packet corrected @2505e2c00a before both halves."
    ],
    "remedy": "Land a truthful final-pass proof/result with explicit corrected packet, ledger and README pins, git-vs-checkout hash grain, and both worker rows; keep earlier STOP evidence labeled historical. Metadata only; no publish replay or verdict fabrication.",
    "owner": "2.0.0_SA_COO~B",
    "round": "v11",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~B",
      "round": "v11"
    },
    "closed": true
  }
]
```
