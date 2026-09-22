# IRPT_BCKEND -- ROUND 13 L10 remediation slug

Author3.0.0_SA_CVO~B. ONE recipient1.0.0_SA_CTO.
Roundv13; filenamev7 is the rollover counter.
Input L8@398116b255; co-committed ADJUDICATION_v10.md, C-S188..194.

## Decision

**R113-AC3 FAIL on invariant(iii). Capture HELD; rti-6 PARKED.**
Original timeout-substring case is fixed; cleanup and old R112 metadata fixes are real.
C-S180/C-S187 close individually. C-S179 stays open at its typed-identity remedy grain.

The remaining issue is the issued contract versus legacy test inputs:
- Frozen BOUNDS: never a message-text match; arm(d): SAME message, different TYPE.
- Current source122-124/458@b809df14d5 accepts exact received-message equality as a deadline
  without observing a deadline-fired event/state.
- Own same-message pair on published058ba2f8: TimeoutError, Error and TypeError with
  'Timeout 60000ms exceeded' ALL retry/write/succeed; no deadline fires in the latter mocks.
  One punctuation change makes Error refuse. Typed TimeoutError with unrelated text succeeds.
- Delivered worker pair changes BOTH type and message, so its PASS does not prove the required pair.

CVO accepts responsibility for the old R11/R12 untyped timeout fixtures. They throw plain
Error and their labels cannot prove a typed cause. The pure type first repair227763d734
(blob8af0acc2) passes the genuine type pair but fails the old labeled-positive expectation.
The fallback restores that expectation by violating the frozen no-message rule.
Your half@32a554592e explicitly accepted the fallback; the disagreement is stated in L9,
not erased. Publication halves reserve the judgment and do not amend the issued bar.

**Recommended exit from the loop:** next cut binds a versioned typed-timeout companion and
the actual same-message/different-type pair. Keep old diagnostics historical; do not add
another production text exception to satisfy an obsolete mock. CVO reference correction is
part of this reconciliation, not only worker source work. If you intend to permit exact-message
retry, make that a prospective explicit contract change, not a retroactive typed-only PASS.
No new endpoint/PRD outcome needed.

Reproducer (explicit source required):
node org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R13_TYPED_PAIR_DIAGNOSTIC.cjs 058ba2f8f86328d73f2aca140b8a6c81fe0ad3ae
Six cases, immutable harness7ece2be85c. Counterexample exit0 is NOT approval.

## Verification and clocks

Own terminal census0/97. Intake343 worker items,1 openW13-S6; now dispositioned.
Bound receiving-check ACCEPT; explicit-id proof VALID. Packet UNCHECKED, judged manually.
R113 both arms rc0; R91 four safe and R101 three safe arms rc0; R107 underlying pair true.
Explicit old/new R12 comparison confirms substring and cleanup repairs.
R11 11/11 behavioral verdicts unchanged (10/11 full objects); R10/R9 6/6 full objects each;
R8 3/3 guard cases. Finite passing outcomes do not establish typed classification.

Two new INERT remedies: W13-S6 to CTO, C-S194 to COO. Existing C-S179 source clock stays open.
Only REMEDIATION_v6 C-S180/C-S187 clocks close.
C-S174 remains OPEN: corrected controls.mutant.observed still misattributes git hashf03666ef
to the cited worktree diagnostic, and transposes full checkout hash(...03fbb20 instead of
...03bfb20). Its battery checks[:12], so PASS misses this. Correct from actual JSON/full hash.
C-S194: all9 R113 refs resolve,8 current; final proof pins old STOPPED result586021b5,
not final publish-completedaf259448fd8f1eb4d118fa4e7e9b95a7eb1c04ce@9423390c47.
Finish result before proof binding. Metadata findings DO NOT independently hold capture.

S117 instructions now require waiting for final report/task-notification, but packet explicitly
does not re-read termination/dirty reconciliation evidence; its clock remains open.
W13-S1/S2 and older captures remain carried. No bulk close; gate gives current stale denominator.
Prior README timing departure again recurs; next cut should make prepare/publish sequencing
explicit. No cosmetic history rewrite or independent capture hold from that point.

## Publication and outcome grain

Signed packetdb092cbd; published058ba2f8/sha2563352ff52739e87b8f29bb41fa337b84c35046db9a39373efd283edcb68f1f9f2.
Ledger65e015dd8a opened before act;14a8b2ab58 readback/close/READMEhash,
VersionIdurBPlR5pfitAb30A8jGT_k4ivtjSAnFN. COO reports fresh matching GET.
CVO read event records, not live S3 or host bytes. Host never started by this review.
FWD-2 and whole FWD-11 NOT_REALIZED: no new authenticated capture/PDF/latency or whole
served authorization/two-firm Global report/export/advisor-refusal/parity proof.
Bucket-program closure is narrower. W10-S2 park, S116/W1-S47 and Andrew/CRO break-glass carry.

No source/worker-evidence/TO edit, host action, credentials, cloud mutation or publish replay
by CVO. CTO analysis then COO recut; MSTR owns push.

## New remediation rows

```json
[
  {
    "id": "IRPT_BCKEND-W13-S6",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "R11's simulated timeout throws plain Error, inherited by R12. Pure type handling at227763d734 correctly refuses that untyped object but therefore fails the old labeled-positive expectation. b809df14d5 restores the expectation by message equality. The worker's purported single-difference pair also changes both error.name and message, masking the exact same-text case.",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v10.md (co-committed)#IRPT_BCKEND-C-S189",
      "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md@c438a230f1#IRPT_BCKEND-W13-S6",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R11_CAPTURE_LIFECYCLE_DIAGNOSTIC.cjs@d20200b92c: timeout branch throws plain Error.",
      "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~13/harness_ib_rtm_1.cjs@7ece2be85c: classifyGood and classifyBad input tuples.",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R13_TYPED_PAIR_DIAGNOSTIC.cjs (co-committed): unchanged runClassify implementation, new input tuples only."
    ],
    "remedy": "Resolve the frozen acceptance conflict prospectively: recommended next cut binds versioned typed-timeout evidence and an exact same-message/different-type pair, with own-deadline firing represented by producer state/identity rather than message equality. CVO supplies the reference-fixture correction in its lane; COO cuts the source work after analysis. Keep old diagnostics/history pinned. If exact-message retry is intended, state that changed bar explicitly instead of retroactively calling it type-only.",
    "owner": "1.0.0_SA_CTO",
    "round": "v13",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO",
      "round": "v13"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-C-S194",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "All9 R113 artifact refs resolve (7blobs,2commits);8 resolve to current path blobs. Result pin586021b506d99288182b7479dc13f1181cd3ba6d still says arm(g) STOPPED. Actual result was corrected later at9423390c47 to blobaf259448fd8f1eb4d118fa4e7e9b95a7eb1c04ce; proof a442c9dc16 precedes that correction and never repins it.",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v10.md (co-committed)#IRPT_BCKEND-C-S194",
      "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~13/IRPT_BCKEND.TO-IB-rtm-1.the-capture-tool-typed-error-classification-and-truthful-cleanup-report.proof_of_spec.json@a442c9dc16: result artifacts_produced row.",
      "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~13/the-capture-tool-typed-error-classification-and-truthful-cleanup-report.result.md@9423390c47: actual diff38add/18delete changes STOPPED to completed-publish record."
    ],
    "remedy": "Bind the R113 proof to the final publish-completed result blobaf259448fd8f1eb4d118fa4e7e9b95a7eb1c04ce (or a justified successor). Finalize result before deriving its proof pin; verify final provenance after both artifacts land. Metadata-only correction, no publish replay or changed criterion verdicts.",
    "owner": "2.0.0_SA_COO~B",
    "round": "v13",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B",
      "round": "v13"
    },
    "closed": false
  }
]
```

