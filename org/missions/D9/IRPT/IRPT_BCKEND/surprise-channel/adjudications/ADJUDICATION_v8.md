# IRPT_BCKEND -- round 11 L8/L9 adjudication

Author: 3.0.0_SA_CVO~B. Review 2026-09-22, 04:28Z onward.
Input: ledger/IRPT_BCKEND_ROUND11_L8_COMPILE.md@715b359db271e6df0d0e6ceaeb04cd5097a5100b,
blob cc97ee7a72efe80efcf7212dd6cd397f6170fa2d. Receipt: COO~B msg99393, exact
20260922T042709Z_2.0.0_SA_COO_B__L8__IRPT_BCKEND_round_11_drain-end_pack.md.
ack_messages is unavailable in this tool context; no broker READ stamp is claimed.
The committed adjudication and exact-file archive are the receipt.

## Decision

**R107-AC3 FAIL. Capture stays HELD; IB-rti-6 stays PARKED.**
The two R10 residual cases are genuinely fixed, but complete-lifecycle safety is not.
A foreign navigation during storageState's awaited response latches AFTER the last check,
and the helper still writes and prints success. The proof is against the published git bytes,
not just a differently rendered checkout. Separately, ordinary foreign resource responses
are misclassified as main-frame navigation. No real browser, host, credential, portal network,
IAM mutation, publication replay or live S3 read was performed by this CVO review.

## Measured canonical-flow state

| Carrier | Measurement |
|---|---|
| Home / index | D9/IRPT/IRPT_BCKEND, laptop; index points to tree; active/EXECUTING |
| Brief / endpoint | PRD names investor-reporting-ir-bk-brief-20260910.md@2acf23d8fd; endpoint present in PRD |
| PRD / decomp | v0.15 / v0.15; neither changed from issuance 2bebd4a93c to review |
| Issuance | ONE cell IB-rtk-1, fanout 1 of 1 chain, cap 8; C-S162 issuer-discharge at same cut |
| Terminality | Own _open_tos_for_project run: 0 open /95; eight older pending-word orders terminal by valid proof |
| Proof form | Bound receiving-check ACCEPT; explicit R107-AC1/2/3 proof check VALID, 3 rows /0 violations |
| Packet | Receiving-check UNCHECKED, not ACCEPT; claims judged individually here |
| Channel intake | comp-surprise: 338 worker items, 168 prior adjudications, 197 remediations, 2 open, 175 filed ARMED, 164 files |
| Worktree | Shared project/source paths initially clean; own diagnostic is the only new source under this review |
| Worker residue | wk-irpt_bckend-11-13b-recovery has 0 commits ahead of HEAD, but one uncommitted proof edit and untracked .scratch/ in C:/tmp/wk-irpt-11-13b |
| Other residue | 22 pre-existing stashes and unrelated worktrees untouched; no stall/dead-seat inference |
| Limb / class | OPEN-ROUND, L8/L9 owned by this actively producing CVO; slug hands to CTO L10, not project CLOSED |

The worker recovery proof edit is NOT consumed as delivered truth. It is reported here to the
CTO for the issuer's handling, consistent with the one-slug message boundary; no grant or recovery
work is done by CVO. The historical phase prose says round 4 and is not the measured limb.
Only the two new worker rows require new dispositions; prior rounds' 336 remain carried.
This document adds nine rows C-S169..177. No new watcher/detector is started.

## Independent evidence, not diagnostic exit-code shorthand

Source blob ded605028b2210b589735927868aacf92ceb852d@0d0c8cdc4d hashes
f03666ef827e7c6a169214c83b2a4fe593d7f1cbf181f728f1febb0235eacd0d.
The CRLF worktree hashes fffef738e90cf03bfb20cdfbeb8cbb310e3a44c6eee657974f8a3eeb92e8e35b;
normalizing CRLF to LF equals the git text. The packet's formerly wrong hash was the checkout
hash, not the claimed git-blob hash. The corrected packet and README name the git-byte value.

Unmodified R10 diagnostic@33c5b593ef ran on BOTH pinned sources: old c5a18898 has the two residual
acceptances; new ded60502 refuses both. Other four case outcomes hold. Old exit0 means defect
reproduction; new exit1 means those reproduction assertions no longer all hold, NOT universal safety.
R9@a62b69f6d3: all six intended outcomes hold. R8: all three guard outcomes remain, but the
password/500 labels stop at missing-instance validation, not at readiness. That blindness was
already known and is not evidence for retry eligibility.

Own unchanged R91 battery: command/readiness/origin/diagnostic all rc0 (4/4 safe arms).
Command covers 7 invalid ids + valid + alternate port; readiness 1 positive +6 negatives;
origin checks include vendor equality and scoped-state positives. The diagnostic arm's temporary
env-only copy adds an instance id and reaches the old readiness cases; the tool removed its own
temporary file. No publish arm ran. Old packet is an old-vintage contract, not a current repair test.
Own unchanged R101 battery: redirect/runbook/origin all rc0 (3/3), including initial-hop
single-difference pair, authenticated positive, mandatory delivery/hash ordering and drift mutant.
Own worker retry harness: good HTTP500-then-clean 1 write/true/two verifications; foreign-then-clean
0/false/one verification. R107 lifecycle battery itself rewrites worker output files, so it was
not rerun; its underlying diagnostics/pair were run independently without those writes.
C160 battery rc0; actual parent diff independently confirms all acceptance bytes unchanged.

The co-committed R11 diagnostic uses an independent event-capable VM, no production-source edits.
Its eleven cases on published blob and worktree agree:
- Storage wait pair: same-origin 1/true, foreign-then-portal 1/true -- defect.
- Resource response pair (isNavigationRequest=false, same main frame): same-origin 1/true,
  foreign 0/false/exit1 -- over-refusal; page never leaves the portal.
- Interval foreign navigation control: 0/false/exit1 -- instrument sees a working latch path.
- Same-origin 500, timeout and missing marker, each followed by clean: 1/true, two verifications.
- Same-origin 404, non-timeout error and password-present, each followed by clean: also 1/true,
  two verifications. The first two fall outside even the stated ordinary-login clarification.
The old c5a18898 source still has the storage-wait acceptance but allows both resource responses:
the missing final check is pre-existing/unclosed; resource over-refusal is newly introduced.
R11 exit0 means TWO DEFECTS REPRODUCED, never a green repair test. No live-resource occurrence
rate is asserted. The same-origin twins and repaired-interval control bound harness blindness.

## Publication and proof provenance

Read both signed halves against corrected packet 5d30a76a4e851064e9f5ff0e4a3b742fdd740e6b:
COO cf4da2c5b3, CTO 993ff1fad3, both preceding arm (g). Ledger at 60bab95e58 records open
04:05:19Z and closed 04:08:27Z; one key, VersionId Angbnvkw2YIyOfdMmVGo11vs3dVfJxBM;
readback f03666ef. README updated in that commit; sh unchanged at blob d704adfb, hash 17ae44f0.
COO's pinned packet independently reports a later fresh GET agreeing. These are event records
read by CVO, not a fresh CVO S3 verification. No on-host readback is claimed.

The actual proof at 8d385d1ae1 remains first-pass: 16 artifact rows, 14 literal blobs all resolve
and match HEAD, two PENDING entries resolve through co-commit semantics. The latter packet has
since been corrected; no explicit final-pass binding is present. Publish exclusion, no-halves
claims, wrong hash grain, missing W13-S2 and pre-publish result are stale. C-S174 carries this,
separate from C-S160's correctly repaired OLD rtj-1 proof. No claim the publication did not occur.

## Dispositions, clocks and outcomes

W13-S1 graduates: issued retry predicate and retained retry behavior differ. A prospective explicit
taxonomy and matching tests are owed; later intent messages do not silently rewrite this grade.
W13-S2 graduates with corrected attribution: terminal grant refusal is required by law; an order
that explicitly required pending-on-STOP was prematurely completed. No blanket worker grant expansion.

C-S160 and C-S162 existing clocks alone advance to REMEDIATED/closed. C-S158/C-S159's concrete
counterexamples are repaired, but their armed capture clocks are conservatively carried until
the successor whole-lifecycle proof passes. C-S153/C-S127 and C-S125/C-S126 host-byte limits stay
unchanged. No older rows bulk-close; the prior 164 stale-row carry is not re-certified individually.

FWD-2: SPLIT / NOT_REALIZED overall. The actual bar covers suggestions, selected-account
membership, report retrieval, polling, cached results and PDF, with swapped identifiers and
revoked grant against warm cache. This round is capture tooling, not that complete served matrix
or authenticated PDF/latency evidence. Its positive and refusal sides remain separate.
FWD-11: backend bucket-program contribution previously EXERCISED/closed, unchanged this round;
overall NOT_REALIZED. PRD lines 94-100 require an Opal Global user to report/export at two firms,
advisor refusal and same-client/revision parity. Bucket-program closure does not satisfy that
frontend-owned outcome. The packet's phrase 'fully closed' is read at bucket-program grain only.

rti-6@82ef626c10 explicitly says S3 half met, judgment half open, condition (1) not fully met.
This FAIL leaves the capture ask HELD. W10-S2 park, S116/W1-S47 external lane, Andrew/CRO
break-glass decision and all older carries remain. No new human request is sent.
REMEDIATION_v5.md is the ONE round-11 slug, to CTO only.

## Rows

```json
[
  {
    "id": "IRPT_BCKEND-C-S169",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~B",
    "surfaced_at": "2026-09-22T04:34:17Z",
    "one_line": "R107-AC3 FAIL: a latched foreign navigation during storageState still permits a write and success.",
    "spec_asserts": "R107-AC3(ii) requires genuinely terminal sticky refusal; arm (d) forbids any write or success after the first foreign navigation. Clause (iii) also limits retry to three named causes.",
    "world_is": "On the published git blob ded60502, the storage-wait foreign-hop case writes 1, prints success, and exits without error. Its same-origin twin also writes 1; the interval foreign-navigation control correctly refuses. The latch is never reset, but the final await occurs after its last check.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rtk-1.the-capture-tool-complete-lifecycle-observer-and-sticky-refusal.md@2bebd4a93c: arm (d), R107-AC3(ii)-(iv).",
        "infra/aws/ec2/investor-reporting-export/capture-session.cjs:364 @0d0c8cdc4d checks before, not after, await storageState at :366; write :368 and success :369.",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R11_CAPTURE_LIFECYCLE_DIAGNOSTIC.cjs (co-committed): 11 cases on published blob and CRLF worktree; both reproduce the storage-wait and resource-response defects."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Evidence record only; no additional remedy opened by this row.",
    "grades": [
      {
        "criterion": "R107-AC3",
        "instance": "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~13/IRPT_BCKEND.TO-IB-rtk-1.the-capture-tool-complete-lifecycle-observer-and-sticky-refusal.proof_of_spec.json@8d385d1ae15a1bb8f8540bc5e6b67a087409cb62",
        "verdict": "FAIL",
        "reason": "Issued R107-AC3(ii), arm (d): zero writes/no success once any foreign main-frame hop latches. ded60502/f03666ef emits foreign navigation while awaiting storageState AFTER the last refuseIfLatched; then writes=1/success=true/exitCode=null. Single-difference same-origin twin writes=1; interval foreign control refuses=0/false/1. This is affirmative counterevidence, independent of the arm-(e) interpretation dispute. Clause (iii)'s literal three-cause restriction also does not hold: HTTP404 and a non-timeout navigation error retry to success. R91 four safe arms and R101 three safe arms rerun rc=0; finite regression passes do not cover the new case. No repair/publish/live capture performed by CVO."
      }
    ]
  },
  {
    "id": "IRPT_BCKEND-C-S170",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~B",
    "surfaced_at": "2026-09-22T04:34:17Z",
    "one_line": "A final await separates the latch check from the irreversible capture write.",
    "spec_asserts": "After any foreign main-frame navigation, arm (d) requires zero writes and no success for the rest of the run.",
    "world_is": "The final latch check runs before await context.storageState(); navigation events during that await can latch the observer, but the continuation proceeds directly to mkdir/write/success with no recheck.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/ec2/investor-reporting-export/capture-session.cjs:184-230,295-299,364-369 @0d0c8cdc4d: observer sets latched, final check precedes storageState await.",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R11_CAPTURE_LIFECYCLE_DIAGNOSTIC.cjs (co-committed): storage pair changes only the middle origin; both arms write 1 and succeed on ded60502; same result on prior c5a18898 (pre-existing unclosed window)."
      ]
    },
    "disposition": "GRADUATED",
    "disarm_owner": "2.0.0_SA_COO~B",
    "notes": "Preserve capture HOLD. Repair final asynchronous boundaries before irreversible write; prove foreign-during-storage refuses beside same-origin positive and retained interval/retry controls. New packet/halves/readback after any source change; no blanket claim of complete lifecycle from one added check."
  },
  {
    "id": "IRPT_BCKEND-C-S171",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~B",
    "surfaced_at": "2026-09-22T04:34:17Z",
    "one_line": "The response listener latches on a foreign subresource even when no navigation occurred.",
    "spec_asserts": "The new observer is a MAIN-FRAME NAVIGATION observer; request/response arms must discriminate navigation from ordinary resource traffic without changing existing authorized capture behavior.",
    "world_is": "onRequest excludes isNavigationRequest=false, but onResponse checks only frame and URL. A main-frame foreign fetch/image/script response sets the terminal latch despite the page remaining on the portal; same-origin response succeeds.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/ec2/investor-reporting-export/capture-session.cjs:198-213 @0d0c8cdc4d: response lacks the navigation-request filter present on request.",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R11_CAPTURE_LIFECYCLE_DIAGNOSTIC.cjs (co-committed): response pair changes only resource origin, request.isNavigationRequest=false in both; same-origin writes=1, foreign writes=0/exit1. On old c5a18898 both succeed; new regression. Interactive foreign navigation control still refuses on ded60502."
      ]
    },
    "disposition": "GRADUATED",
    "disarm_owner": "2.0.0_SA_COO~B",
    "notes": "Filter the response path at navigation grain, preserving main-frame foreign-hop refusal. Demonstrated with event mocks, not a live portal dependency census; no claim that a specific live resource fired."
  },
  {
    "id": "IRPT_BCKEND-C-S172",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~B",
    "surfaced_at": "2026-09-22T04:34:17Z",
    "one_line": "W13-S1 is a real issued-bar/implementation mismatch; unchanged R8 output does not prove password retry.",
    "spec_asserts": "Arm (e), BOUNDS, and R107-AC3(iii) explicitly allow ONLY timeout, 5xx, missing-marker retry; the same face requires existing checks unweakened.",
    "world_is": "Worker retains all prior retry reasons. Own R11 runs show the named three plus HTTP404, non-timeout navigation error, and password-present all retry then succeed. Unmodified R8 supplies no instance id and its password case never navigates, so its byte-identical output cannot adjudicate password retry.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md@897171eb53#IRPT_BCKEND-W13-S1.",
        "org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rtk-1.the-capture-tool-complete-lifecycle-observer-and-sticky-refusal.md@2bebd4a93c: arm (e), BOUNDS and R107-AC3(iii).",
        "infra/aws/ec2/investor-reporting-export/capture-session.cjs:235-258,333-355 @0d0c8cdc4d; generic goto catch and all readiness reasons continue.",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R11_CAPTURE_LIFECYCLE_DIAGNOSTIC.cjs (co-committed): six retry cases; three named positives plus three outside the literal list accept after a clean retry.",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R8_CAPTURE_DIAGNOSTIC.cjs: unchanged run has zero navigations for password case due to missing instance id."
      ]
    },
    "disposition": "GRADUATED",
    "adjudicates": [
      "IRPT_BCKEND-W13-S1"
    ],
    "notes": "Graduate the specification/coverage conflict to explicit prospective retry semantics and distinguishing tests, preserving the human login flow and foreign-origin terminal refusal. Issuer/CTO's intent clarification is recorded, not silently substituted for the issued bar. Do not manufacture a regression argument from a pre-navigation guard."
  },
  {
    "id": "IRPT_BCKEND-C-S173",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~B",
    "surfaced_at": "2026-09-22T04:34:17Z",
    "one_line": "W13-S2's refusal is real, but terminal orders intentionally grant nothing; premature completion is the proximate cause.",
    "spec_asserts": "Spine L7 and owned-paths worker_grant bind only non-terminal orders at HEAD. The order's own proof_of_spec says unmet sign-off STOP leaves it pending.",
    "world_is": "Worker marked complete before arm (g)'s halves existed, then a later README edit was refused as the law specifies. The source comment cited as permission describes the historical motivation for building this rule, not a new exemption for completed orders.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        ".tools/owned-paths-validate.py:113-122,175-202 @4e3142cfb3: NON-TERMINAL only, and terminal orders are not standing permission.",
        "org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rtk-1.the-capture-tool-complete-lifecycle-observer-and-sticky-refusal.md@2bebd4a93c: pending-on-STOP instruction; @8d385d1ae1: complete while explicitly saying arm (g) STOPPED.",
        "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md@897171eb53#IRPT_BCKEND-W13-S2; publish commit 60bab95e58 changes README and closes ledger."
      ]
    },
    "disposition": "GRADUATED",
    "adjudicates": [
      "IRPT_BCKEND-W13-S2"
    ],
    "notes": "Graduate procedural correction for held multi-pass work, not a demonstrated defect in the terminal-order grant rule. Preserve the grant boundary. Owner must reconcile pending/terminal state with actual remaining work before a later pass; any general exception is a separately authorized law change. Retained recovery worktree contains an uncommitted proof edit, left untouched."
  },
  {
    "id": "IRPT_BCKEND-C-S174",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~B",
    "surfaced_at": "2026-09-22T04:34:17Z",
    "one_line": "Round-11 proof/result at HEAD still describe pre-publish STOP and mislabel a CRLF worktree hash as the git-blob hash.",
    "spec_asserts": "Proof provenance must describe the delivered pass and distinguish source git bytes from checkout bytes; the final publish's event evidence belongs in the final record.",
    "world_is": "Proof at 8d385d1ae1 and result blob ef0e9734 still exclude publish, say no halves, and claim fffef738 as git-blob sha256; actual git blob hashes f03666ef and publish ledger/README at 60bab95e58 record delivery. Proof lists W13-S1 only although W13-S2 exists. Fourteen literal blob pins resolve and match HEAD; two PENDING entries include the subsequently corrected packet.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~13/IRPT_BCKEND.TO-IB-rtk-1.the-capture-tool-complete-lifecycle-observer-and-sticky-refusal.proof_of_spec.json@8d385d1ae1: artifacts_produced[0], declared_exclusions, surprises.",
        "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~13/the-capture-tool-complete-lifecycle-observer-and-sticky-refusal.result.md@0d0c8cdc4d (HEAD blob ef0e973405ad9672e3e31078c20805dd18309b12).",
        "org/critical_paths/change_management/20260922T0405Z_irpt-rtk-1-capture-tool-publish_deploy_completion.md@60bab95e58: closed readback event.",
        "CVO Buffer-based hash read: disk fffef738, git f03666ef; replacing CRLF with LF makes disk bytes equal git text. Packet corrected @2505e2c00a before both halves."
      ]
    },
    "disposition": "GRADUATED",
    "notes": "Metadata-only correction through owner; no publication replay or criterion truth changes. An uncommitted proof correction exists in C:/tmp/wk-irpt-11-13b (37 additions/7 deletions at read), not merged evidence and not touched by CVO. Do not confuse historical event pins with current final-pass proof."
  },
  {
    "id": "IRPT_BCKEND-C-S175",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~B",
    "surfaced_at": "2026-09-22T04:34:17Z",
    "one_line": "The C-S158/C-S159 original counterexamples are repaired; no complete-lifecycle clock closure is inferred.",
    "spec_asserts": "Original R10 diagnostic names human-wait foreign-hop and foreign-then-clean retry residuals. Source repair and publication alone do not imply whole-lifecycle acceptance.",
    "world_is": "CVO unmodified R10 run on old c5a18898 vs new ded60502 flips exactly those two acceptance outcomes to refusal; same-origin positive still captures and three other refusal controls remain. The worker retry pair preserves HTTP500 recovery. R107 still fails on the final await; retain existing armed capture clocks pending a complete successor proof.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R10_CAPTURE_LIFECYCLE_DIAGNOSTIC.cjs@33c5b593ef: own two pinned runs, old rc0 reproduction/new rc1 no reproduction; six case outputs interpreted explicitly.",
        "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~13/harness_ib_rtk_1.cjs@0d0c8cdc4d: own rerun pairOk=true, good 1/true/two verifications, foreign 0/false/one verification.",
        "infra/aws/ec2/investor-reporting-export/capture-session.cjs@0d0c8cdc4d."
      ]
    },
    "disposition": "GRADUATED",
    "adjudicates": [
      "IRPT_BCKEND-C-S158",
      "IRPT_BCKEND-C-S159"
    ],
    "notes": "Record of bounded progress, not dismissal of their remedies. C-S158/C-S159 REMEDIATION_v4 clocks remain OPEN/ARMED, as do C-S153/C-S127 and older host-byte limits."
  },
  {
    "id": "IRPT_BCKEND-C-S176",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~B",
    "surfaced_at": "2026-09-22T04:34:17Z",
    "one_line": "C-S160 metadata remedy verified and its existing clock closes.",
    "spec_asserts": "C-S160 requires the previous rtj-1 result pin corrected to the actual delivered second-pass blob, no other criterion changes and no republish.",
    "world_is": "Exact bdf01c0005 parent diff changes only commit_or_etag/deploy_evidence for the result row; all acceptance content unchanged. Actual HEAD result blob equals b7eea3ae and the old delivered commit; c160 arm and corrected proof recheck exit0.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git diff bdf01c0005^ bdf01c0005 -- org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~13/IRPT_BCKEND.TO-IB-rtj-1.the-capture-tool-navigation-lifecycle-and-host-delivery-runbook.proof_of_spec.json.",
        "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~13/battery_ib_rtk_1.py@0d0c8cdc4d --arm c160: own run IBR107-C160-METADATA-PIN-CORRECTED-PROOF-STILL-VALID, rc0."
      ]
    },
    "disposition": "GRADUATED",
    "adjudicates": [
      "IRPT_BCKEND-C-S160"
    ],
    "notes": "Advance only remediation.state=REMEDIATED and closed=true on existing REMEDIATION_v4 C-S160. Historical evidence/owner/round preserved. This does not close the separate new rtK proof defect."
  },
  {
    "id": "IRPT_BCKEND-C-S177",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~B",
    "surfaced_at": "2026-09-22T04:34:17Z",
    "one_line": "C-S162 remedy verified as prospective retirement, not a retroactive R102 grade.",
    "spec_asserts": "C-S162 requires resolving the undefined R102-AC2 bar without inventing a retrospective pass or recreating the role.",
    "world_is": "At issuance 2bebd4a93c the issuer removes AC2 from expected_criteria and explicitly preserves permanent NOT_EVALUATED at its original vintage; AC1 is retained and no new retrospective bar appears.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rtj-2.the-l4-bounded-test-principal-created-exercised-destroyed.md@2bebd4a93c: exact parent diff.",
        "org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_BCKEND_ROUND_10_20260922.md@703efac869: prospective-retirement ruling."
      ]
    },
    "disposition": "GRADUATED",
    "adjudicates": [
      "IRPT_BCKEND-C-S162"
    ],
    "notes": "Advance only remediation.state=REMEDIATED and closed=true on existing REMEDIATION_v4 C-S162. No change to the historical R102-AC2 NOT_EVALUATED record."
  }
]
```
