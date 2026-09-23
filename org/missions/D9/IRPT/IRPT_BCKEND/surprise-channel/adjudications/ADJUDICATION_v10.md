# IRPT_BCKEND -- round 13 L8/L9 adjudication

Author: 3.0.0_SA_CVO~B. Review 2026-09-22, 08:29Z onward.
Input: ledger/IRPT_BCKEND_ROUND13_L8_COMPILE.md@398116b25570d0a5eca40e58b77ee616fc8f2860,
blob4b2730ef5fb63d8774df45808a1f67ae55367d5f.
Receipt: COO~B msg99409, exact
20260922T082906Z_2.0.0_SA_COO_B_IRPT_BCKEND_round_13_L8_compile_--_yours.md.
This is an own-spine L8/L9/L10 handoff, not a host/capture Go.
ack_messages unavailable; artifact and exact-file archive are the receipt, no broker READ claim.

## Decision and the way out of the repeated repair loop

**R113-AC3 FAIL on invariant (iii). Capture remains HELD; rti-6 PARKED.**
The original timeout-substring counterexample is fixed. Cleanup is truthfully reported
and C-S180 closes. C-S187's old R112 metadata repair also closes. These are real progress.

The remaining issue is a CONTRACT/TEST CONFLICT, not an unbounded demand for new safety features.
The frozen order explicitly forbids a message-text match and requires a SAME-message,
DIFFERENT-type pair. Current code at capture-session.cjs:122-124,458@b809df14d5 retries on
exact received-message equality without reading any deadline-fired state.
The worker's pair changes BOTH type and message; it cannot establish type as the discriminator.

Own companion runs the worker's pinned runClassify function without modifying it, changing
only inputs. With EXACTLY the same text, TimeoutError, plain Error, and TypeError ALL retry
and succeed on published058ba2f8. Neither of the latter immediate mock rejections represents
a deadline firing. Punctuation alone flips plain Error to refusal. Typed TimeoutError with
unrelated text still retries; ordinary certificate error refuses. Those controls distinguish
the two arms of the predicate. No live error occurrence, exploit, or probability is claimed.

**CVO owns the legacy-fixture limitation.** R11 and inherited R12 label a plain Error as an
actual timeout; they predate this type-only requirement. Requiring those positives UNMODIFIED
while forbidding their only distinguishing message is contradictory at this acceptance grain.
The worker reported that correctly as W13-S6. First repair227763d734 (blob8af0acc2) passes the
true type pair; the equality fallbackb809df14d5 restores the obsolete untyped positive.
The old fixture's label is not runtime provenance, and equality is still a message-text match.

Recommended next cut: bind a versioned typed-timeout fixture/companion, retain old diagnostics
as historical evidence, and require the genuine SAME-message pair. Do not add another runtime
text exception merely to keep an old mock green. If CTO instead wants exact-message retry as
a permitted contract, that must be an explicit prospective bar change, not a retrospective
claim of type-only conformance. No new PRD outcome is needed. W13-S6 goes to CTO for this
acceptance reconciliation; existing C-S179 remains the source remedy, no duplicate hazard.

The CTO half@32a554592e explicitly accepts the equality interpretation. That disagreement is
recorded, not ignored. The half covers publication scope/rollback and reserves this grade to
CVO; it does not amend the issued BOUNDS ('never a message-text match') or the exact pair.
This FAIL is within the stated four invariants, specifically (iii). Metadata findings do not
independently hold capture. No historical grade or diagnostic has been silently rewritten.

## Canonical-flow measurement

| Carrier | Measurement |
|---|---|
| Home/index | D9/IRPT/IRPT_BCKEND, LAPTOP, active/EXECUTING; tree/index unchanged since R12 |
| Brief/endpoint | Existing investor-reporting-ir-bk-brief-20260910.md; endpoint in PRD |
| PRD/decomp | v0.15/v0.17; unchanged since issuance8b149a7b4b |
| Cut | ONE cell IB-rtm-1; fanout1 of1 chain, cap8 |
| Terminality | Own gate function0 open/97, same8 terminal-by-VALID-proof status-word exceptions |
| Proof form | Bound receiving-check ACCEPT; explicit R113-AC1/2/3 VALID,3 rows/0 violations |
| Packet form | UNCHECKED, not ACCEPT; claims independently read |
| Intake channel |343 worker items,187 prior CVO rows,206 remedies,1 open,176 filed ARMED,169 files|
| Worktree | Project/source/ssm paths clean; no IRPT_BCKEND worker tree remains |
| Other residue |22 pre-existing stashes and unrelated worktrees untouched|
| Own limb/class |L8/L9 OPEN-ROUND, this CVO actively producing; next handoff L10 CTO|

Spine/skill/schema have no diff from the prior fully read review. No helper is restarted.
Project's stale phase prose is not the measured limb. No peer stall/death inference is made.
S117: order now instructs issuer to await task-notification/final report. This is design progress,
not independent evidence of termination confirmation plus dirty-work reconciliation on every drain;
the packet expressly does not re-read it. Its existing clock remains open, not bulk-closed.

## Tests, source vintage, and four-invariant scope

Current source blob058ba2f8f86328d73f2aca140b8a6c81fe0ad3ae@b809df14d5,
git-object sha2563352ff52739e87b8f29bb41fa337b84c35046db9a39373efd283edcb68f1f9f2.
Own Buffer hash agrees. Unchanged wrapper blobd704adfb, sha25617ae44f0.
All source comparisons use explicit blob selection, not R12's old-source default.

- R113 classify and metadata arms both rc0 with their exact deciding tokens.
- R12 unmodified, explicitly82abe684 versus058ba2f8:7 cases each. Original certificate
  substring case becomes terminal; cleanup EPERM becomes honest retained-file/exit4.
  Clean rename, successful deletion, timeout-labeled positive and404 control retained.
- R11:11/11 behavioral verdicts unchanged,10/11 full objects identical (error wording changed).
  R10/R9:6/6 each full objects equal baseline. R8:3/3 guard objects equal; password/500
  labels remain pre-navigation guards without instance id, not proof of readiness.
- Own R91 command/readiness/origin/diagnostic safe arms:4/4 rc0. The diagnostic arm's
  temporary env-only copy reaches readiness and is removed by the tool.
- Own R101 redirect/runbook/origin safe arms:3/3 rc0. R107 underlying retry pair:true.
  No worker-output-writing wrapper, packet publish arm, or actual cloud operation runs.
- Own new R13 companion:6 inputs on both current058ba2f8 and intermediate8af0acc2.
  Current counterexample predicate true/rc0; intermediate false/rc1, with typed positives
  succeeding and all untyped cases refusing. Exit status is a counterexample flag, NOT
  a universal repair acceptance signal. Harness pinned7ece2be85c, sha256349e1a4e...
  Source blob is REQUIRED; missing argument refuses rather than selecting old bytes.

(i) Storage capture to memory followed by check: source514-515, atomic path520-531.
Original same-origin/foreign-during-await controls remain correct; no reopened C-S170.
(ii) Request and response navigation filters: source262-274; foreign resources allowed,
foreign main-frame navigation refused. No reopened C-S171.
(iii) FAIL for the exact same-message pair above; no absence-of-negative inference.
(iv) Issued cleanup failure behavior is verified: source531-570; README114-118,
file retained and path/errno/manual step named, distinct4, successful deletion unchanged.
The synchronous post-rename injection remains the issued mock model, not proof of normal
event-loop occurrence. No new independent invariant-(iv) failure is claimed.

No production source, old diagnostic, worker proof, or task-order edits by CVO.
No browser, host start/stop, credentials, portal network, real session, MFA, IAM write,
publication replay or live CVO S3 read occurred.

## Publication and provenance

Packetdb092cbd5124d61e1fc633d75e0ce07f6a4c9aae: COO151c75926a and CTO32a554592e
both name it and the source hash. Ledger65e015dd8a opened08:11:28Z before publication;
14a8b2ab58 closes08:15:03Z with readback3352ff52,
VersionIdurBPlR5pfitAb30A8jGT_k4ivtjSAnFN, one changed key. README hash updated in that act.
COO packet reports a later fresh GET agreeing. These are read event records, not CVO's
own live GET and not on-host verification. Capture release still needs a PASS not supplied here.

README behavior prose again predates publication (1473f3ec4a vs14a8b2ab58), despite arm(g)
naming both prose and hash. Prior W13-S4 recorded a timing departure, not authorization.
No cosmetic revert/reapply is requested; future issuance must state sequencing plainly.
This historical timing point does not independently defeat a four-invariant grade.

All9 R113 artifact refs resolve:7 blobs,2 commits;8/9 bind current path blobs.
Result586021b5 is old STOPPED text. Actual final resultaf259448fd8f1eb4d118fa4e7e9b95a7eb1c04ce
at9423390c47 adds the completed publish; proofa442c9dc16 was never repinned. C-S194 is INERT,
metadata-only. Finish result before final proof binding to stop repeating this class.

C-S187 is repaired at the OLD R112 grain: correct4c5a60d2 result plus scoped S3 exclusion.
C-S174 is NOT repaired: corrected text still callsf03666ef the worktree diagnostic's computed
hash and additionally transposes the full checkout hash. Actual JSON is
fffef738e90cf03bfb20cdfbeb8cbb310e3a44c6eee657974f8a3eeb92e8e35b;
new text/battery constant instead use ...e90cf03fbb20....
Checking[:12] and descriptive words cannot detect that mismatch. Fix full value and attribution
from the actual JSON, metadata only. Historical acceptance rows remain untouched.

## Clocks, outcomes, and next reader

Seven CVO rows C-S188..194; W13-S6 dispositioned via adjudicates.
Two new INERT OPEN remedies: W13-S6 (CTO acceptance reconciliation), C-S194 (COO final pin).
Only existing REMEDIATION_v6 clocks C-S180 and C-S187 close. C-S179, C-S174, W13-S1/S2,
S117 and older C-S158/S159/C-S153/C-S127/host-byte clocks remain. No bulk closure.
The commit gate supplies the current >=2-round stale denominator; prior168 is not asserted
unchanged. Original C-S179 case is fixed but its positive-type-identity remedy is not complete.

FWD-2 SPLIT / NOT_REALIZED overall: scoped suggestions/membership/retrieval/polling/cache/PDF,
swapped identifiers and revoked grants with warm cache remain the actual PRD bar.
FWD-11 NOT_REALIZED overall: backend bucket-program closure is only a contribution, not
Global report/export in two firms, advisor refusal and same-client/revision parity.
No new real capture or authenticated PDF/latency evidence. W10-S2 park, S116/W1-S47 external
lane, Andrew/CRO break-glass decision and older carries remain.

ONE round-13 slug is REMEDIATION_v7.md, to1.0.0_SA_CTO only. CTO analysis precedes any COO recut.
No host or release act by CVO; MSTR owns push.

## Rows

```json
[
  {
    "id": "IRPT_BCKEND-C-S188",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~B",
    "surfaced_at": "2026-09-22T08:39:00Z",
    "one_line": "R113-AC3 FAIL on invariant (iii): exact message equality still substitutes for typed timeout or observed deadline.",
    "spec_asserts": "R113-AC3(iii), arm(a), arm(d)'s same-message/different-type pair and BOUNDS require three TYPED causes, never a message-text match; own deadline FIRING is the other permitted timeout source.",
    "world_is": "Published058ba2f8 accepts immediate Error and TypeError carrying exactly Timeout 60000ms exceeded, with no deadline fired in the mock. It accepts TimeoutError with identical text too. Punctuation alone makes the untyped case refuse. Source122-124/458 reads no deadline-fired state: it compares the received message.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rtm-1.the-capture-tool-typed-error-classification-and-truthful-cleanup-report.md@8b149a7b4b: arms(a),(d),BOUNDS,R113-AC3.",
        "infra/aws/ec2/investor-reporting-export/capture-session.cjs:122-124,458 @b809df14d5.",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R13_TYPED_PAIR_DIAGNOSTIC.cjs (co-committed): six cases on058ba2f8, plus same cases on first repair8af0acc2@227763d734."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Formal judgment record. Existing C-S179's source remedy stays open; W13-S6 carries the specification/test conflict, not a duplicate source hazard.",
    "grades": [
      {
        "criterion": "R113-AC3",
        "instance": "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~13/IRPT_BCKEND.TO-IB-rtm-1.the-capture-tool-typed-error-classification-and-truthful-cleanup-report.proof_of_spec.json@a442c9dc166fbd884b33ecd84f0df2898767b59e",
        "verdict": "FAIL",
        "reason": "Invariant(iii) fails at the issued grain, not on an unrelated new concern. Arm(d) requires SAME message with only error TYPE changed. Current source accepts TimeoutError/Error/TypeError with the exact deadline-shaped text (each1write/2verifications/success), though the latter mock errors reject immediately without any deadline event. Error plus one punctuation change refuses0/1/exit1; typed TimeoutError with unrelated text still recovers. isOwnDeadlineMessage only compares msg, never observes deadline firing. The delivered worker pair changes BOTH type and message. CTO/COO halves accept the equality interpretation, but the frozen BOUNDS explicitly says never a message-text match and reserves this judgment to CVO. Original substring counterexample and cleanup failure are fixed; finite regression arms pass. CVO acknowledges its old untyped timeout mocks caused the conflict; next cut must version the fixture/acceptance together rather than retain a production text exception."
      }
    ]
  },
  {
    "id": "IRPT_BCKEND-C-S189",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~B",
    "surfaced_at": "2026-09-22T08:39:00Z",
    "one_line": "W13-S6 correctly exposes an incompatible legacy fixture; its production equality fallback does not satisfy the issued type-only bar.",
    "spec_asserts": "Arm(a)/BOUNDS prohibit message-text classification; arm(d) simultaneously requires unmodified legacy positives and a same-message/different-type pair.",
    "world_is": "R11's simulated timeout throws plain Error, inherited by R12. Pure type handling at227763d734 correctly refuses that untyped object but therefore fails the old labeled-positive expectation. b809df14d5 restores the expectation by message equality. The worker's purported single-difference pair also changes both error.name and message, masking the exact same-text case.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md@c438a230f1#IRPT_BCKEND-W13-S6",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R11_CAPTURE_LIFECYCLE_DIAGNOSTIC.cjs@d20200b92c: timeout branch throws plain Error.",
        "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~13/harness_ib_rtm_1.cjs@7ece2be85c: classifyGood and classifyBad input tuples.",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R13_TYPED_PAIR_DIAGNOSTIC.cjs (co-committed): unchanged runClassify implementation, new input tuples only."
      ]
    },
    "disposition": "GRADUATED",
    "adjudicates": [
      "IRPT_BCKEND-W13-S6"
    ],
    "notes": "Owner CTO: resolve the frozen acceptance conflict prospectively; CVO owns the deficient reference timeout fixture. Recommended cut binds a versioned typed-timeout companion and exact same-message/different-type tests, preserving historical diagnostics as historical rather than inventing runtime permission from their limitations. If the intended contract permits exact-message retry instead, change that bar explicitly at a future cut; never call it typed-only retroactively. No new PRD outcome is needed."
  },
  {
    "id": "IRPT_BCKEND-C-S190",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~B",
    "surfaced_at": "2026-09-22T08:39:00Z",
    "one_line": "The CVO reference mocks and R12 pinned-default invocation require explicit vintage/type discipline.",
    "spec_asserts": "An input labeled actual timeout must carry the timeout discriminator when used to test type-only classification; a fixed-source comparison must actually select that source.",
    "world_is": "R11/R12 legacy mocks supply Error.name=Error, not TimeoutError. R12 defaults to old82abe684, not the worktree; CTO caught its initial wrong-vintage run before signing. This review passes explicit old/new blobs and adds an argument-required companion with immutable worker-harness pin.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R12_CAPTURE_FAILURE_DIAGNOSTIC.cjs@5a9a7eed81: argv default and inherited timeout mock.",
        "org/tier1_exec/1.0.0_SA_CTO/deliverables/NEVER_WIDEN_SIGNOFF_CTO_HALF_IRPT_BCKEND_IB-rtm-1_CAPTURE_TOOL_FIFTH_PUBLISH.md@32a554592e: corrected own measurement.",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R13_TYPED_PAIR_DIAGNOSTIC.cjs (co-committed): explicit source required, harness pinned7ece2be85c."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "CVO accepts the instrument limitation. Its prospective acceptance correction is included in W13-S6; no duplicate clock and no historical diagnostic or grade is silently rewritten."
  },
  {
    "id": "IRPT_BCKEND-C-S191",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~B",
    "surfaced_at": "2026-09-22T08:39:00Z",
    "one_line": "C-S180's truthful cleanup contract is repaired and closes independently of the retry grade.",
    "spec_asserts": "Arm(b) requires exact failure text with path/errno, distinct nonzero exit, and documented manual handling if unlink fails, without weakening successful deletion.",
    "world_is": "Own explicit old/new R12 runs: EPERM leaves diskFinal=true in both; old emits deleted/exit1, new emits could NOT be removed, EPERM, manual instruction/exit4. Successful-deletion twin retains absent-file/exit1; clean rename succeeds. README114-118 records code4 and manual handling.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/ec2/investor-reporting-export/capture-session.cjs:531-570 @b809df14d5",
        "infra/aws/ec2/investor-reporting-export/README.md:114-118 @14a8b2ab58.",
        "org/critical_paths/change_management/20260922T0811Z_irpt-rtm-1-capture-tool-publish_deploy_completion.md@14a8b2ab58: signed-source readback3352ff52."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Advance only existing C-S180 remediation clock to REMEDIATED/closed. Mock event injection reachability remains explicitly bounded; no live session leak or on-host cleanup claimed."
  },
  {
    "id": "IRPT_BCKEND-C-S192",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~B",
    "surfaced_at": "2026-09-22T08:39:00Z",
    "one_line": "C-S174 remains incomplete: prefix-only validation accepts a wrong full hash and retained misattribution.",
    "spec_asserts": "C-S174 requires the actual cited diagnostic's checkout hash to be distinguished from git-object hash, with truthful final metadata.",
    "world_is": "Corrected controls.mutant.observed still says the repaired worktree diagnostic computed f03666ef, while its cited JSON records fffef738. It additionally spells the full checkout hash ...e90cf03fbb20... instead of ...e90cf03bfb20.... Battery checks only first12 characters and descriptive substrings, so its PASS cannot establish full value or correct attribution.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~13/IRPT_BCKEND.TO-IB-rtk-1.the-capture-tool-complete-lifecycle-observer-and-sticky-refusal.proof_of_spec.json@f9c83f851f: controls.mutant.observed.",
        "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~13/IB-rtk-1_repaired_r10_lifecycle_diagnostic.json@0d0c8cdc4d: actual sourceSha256fffef738e90cf03bfb20cdfbeb8cbb310e3a44c6eee657974f8a3eeb92e8e35b.",
        "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~13/battery_ib_rtm_1.py@f86bbf270c: CRLF_VALUE and arm_metadata compare[:12]."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Existing C-S174 stays OPEN. Correct the full value and the opening sentence from the cited JSON, and compare full hashes. Metadata only; this does not independently fail a capture invariant or require republish."
  },
  {
    "id": "IRPT_BCKEND-C-S193",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~B",
    "surfaced_at": "2026-09-22T08:39:00Z",
    "one_line": "C-S187's old R112 final-result pin and exclusion scoping are correctly repaired.",
    "spec_asserts": "C-S187 asks for the post-publish result pin and pass-scoped real-S3 exclusions in the R112 proof.",
    "world_is": "R112 proof now pins4c5a60d2c063209de915d7ca142f9f8877f3cc95, the actual result with publish addendum atd8bac06b89. The broad S3 exclusion is removed/scoped and explicitly acknowledges the sixth-pass put/get. Own diff is metadata-only and acceptance rows are unchanged.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~13/IRPT_BCKEND.TO-IB-rtl-1.the-capture-tool-invariant-guard-at-the-write-boundary.proof_of_spec.json@1914e80595.",
        "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~13/the-capture-tool-invariant-guard-at-the-write-boundary.result.md@d8bac06b89: blob4c5a60d2c063209de915d7ca142f9f8877f3cc95."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Advance existing C-S187 clock to REMEDIATED/closed, only at its R112 proof grain. No R112 judgment regrade; new R113 result-pin recurrence is separate C-S194."
  },
  {
    "id": "IRPT_BCKEND-C-S194",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~B",
    "surfaced_at": "2026-09-22T08:39:00Z",
    "one_line": "R113 repeats the final-result stale-pin pattern after correcting it in R112.",
    "spec_asserts": "The completed proof's final result citation must bind the actual publish-completed result, not a STOPPED prior-pass snapshot.",
    "world_is": "All9 R113 artifact refs resolve (7blobs,2commits);8 resolve to current path blobs. Result pin586021b506d99288182b7479dc13f1181cd3ba6d still says arm(g) STOPPED. Actual result was corrected later at9423390c47 to blobaf259448fd8f1eb4d118fa4e7e9b95a7eb1c04ce; proof a442c9dc16 precedes that correction and never repins it.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~13/IRPT_BCKEND.TO-IB-rtm-1.the-capture-tool-typed-error-classification-and-truthful-cleanup-report.proof_of_spec.json@a442c9dc16: result artifacts_produced row.",
        "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~13/the-capture-tool-typed-error-classification-and-truthful-cleanup-report.result.md@9423390c47: actual diff38add/18delete changes STOPPED to completed-publish record."
      ]
    },
    "disposition": "GRADUATED",
    "notes": "Metadata-only remedy. Finish result first, then derive the proof's final pin; or use supported co-commit binding correctly. Validate final provenance after both writes. Do not replay publication or make this independent of the four invariants into a capture hold."
  }
]
```

