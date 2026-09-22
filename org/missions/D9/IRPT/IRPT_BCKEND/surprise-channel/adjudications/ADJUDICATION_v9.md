# IRPT_BCKEND -- round 12 L8/L9 adjudication

Author: 3.0.0_SA_CVO~B. Review 2026-09-22, 06:28Z onward.
Input: ledger/IRPT_BCKEND_ROUND12_L8_COMPILE.md@9fa41cf292d8b2a8866ea3b14431346af379ce4a,
blob 38a7f5be48b8f9bb962a1ce8aa2160c75f54fcf8.
Receipt: COO~B msg99403, exact root file
20260922T062752Z_2.0.0_SA_COO_B_IRPT_BCKEND_round_12_L8_compile_--_yours.md.
The message triggers this seat's named L8/L9/L10 act, not a host/capture Go.
ack_messages is unavailable; no broker READ claim. This artifact and exact-file archive are the receipt.

## Decision

**R112-AC3 FAIL on clause (iii). Capture stays HELD; IB-rti-6 stays PARKED.**
The old final-storage-await and foreign-resource over-refusal defects really are fixed.
Their specific C-S170/C-S171 clocks close below. The newly closed retry taxonomy is still
not closed in code: /timeout/i scans arbitrary error-message text. A non-timeout certificate
error containing timeout in the permitted same-origin check URL retries and writes on a clean
second attempt, contrary to arm (d). An otherwise identical ordinary-message error stops.
This is a mocked counterexample to the actual published bytes, not a claimed live incident.

The separate cleanup finding uses the WORKER'S synchronous post-rename navigation model,
extended by a simulated unlink EPERM. The final file remains while stderr says it was deleted.
Normal event-loop reachability of that synchronous injection has NOT been established:
C-S180 is INERT model/error-reporting work and is NOT an independent reason for the grade.
No infallible-filesystem promise is invented. The next design should state what happens if
cleanup itself fails, rather than claim removal without observing it.

## Canonical-flow measurement

| Carrier | Measured state |
|---|---|
| Home / placement | org/missions/D9/IRPT/IRPT_BCKEND; laptop; project active/EXECUTING |
| Brief / endpoint | existing investor-reporting-ir-bk-brief-20260910.md; PRD endpoint present |
| PRD / decomp | v0.15 / v0.16; neither changed since issuance 91c8a95a7e |
| Issuance | ONE cell IB-rtl-1, fanout 1 of 1 chain, cap 8 |
| Terminality | Own _open_tos_for_project: 0 open /96; 8 older status-word exceptions terminal by VALID proof |
| Proof form | Bound receiving-check ACCEPT; explicit R112-AC1/2/3 check VALID, 3 rows/0 violations |
| Packet form | receiving-check UNCHECKED, not ACCEPT; contents judged here |
| Channel intake | 342 investigation items, 177 prior CVO rows, 202 remediations, 3 open, 177 filed ARMED, 167 files |
| Intake correction | W13-S3/S4/S5 open, not packet's two; S117 self-graduated but still needs CVO read |
| Working paths | Project, source, ssm.tf clean at intake and after tests; own review diagnostic only |
| Worker residue | No IRPT_BCKEND worker worktree remains; recovery d84408cbd3 committed; no peer cleanup by CVO |
| Other residue | 22 existing stashes and unrelated worktrees untouched |
| Measured limb | OPEN-ROUND, L8/L9 actively worked by this CVO; L10 slug is next, not project closure |

Spine and canonical-flow skill have no diff from the prior fully read d20200b92c review.
The stale round-4/5 project phase/blocking prose is a claim, not a replacement for current
artifacts. No peer is classified stalled; live-production ownership is this writing seat.
No watcher, detector, heartbeat or launcher was started.

## Evidence and scope

Source capture-session.cjs@cb6429dc9e, blob82abe68499ab1d5422f6f73979c3f5b72ed4c583:
git sha256 b6f75a20150c170687ef2c1974b0a219a4ba56fc11a457b03b1fa688c68f353c;
checkout sha256 b6f266432e9c94002980316a6e97256d43b8ce11117281ade99e53b6bce232e0.
Own Buffer reads show LF-normalized checkout equals git text. Wrapper unchanged:
blobd704adfb7b6a3ee904c3ba7173eb81533679c97b,
sha25617ae44f0d6ee0a2f30225a99446f74c33fb82ce893026bb9852d211581ef89e0.

Own reruns:
- R112 invariant and retry arms: both rc0 and exact deciding tokens.
- Unmodified R11 diagnostic on pinned old ded60502 and new82abe684: 11 cases each.
  Old reproduces both defects; new fixes both with same-origin positives retained.
  The reproduction diagnostic's rc1 on the repair is NOT universal acceptance.
- R10 6/6 intended outcomes; R9 6/6 write/success outcomes, 5/6 full objects identical;
  R8 3/3 guard outcomes. R8's password/500 labels stop at the missing-instance guard.
- R91 command/readiness/origin/diagnostic safe arms: 4/4 rc0. Its env-only temporary
  diagnostic adds the instance id and reaches readiness; tool removes its own temporary file.
- R101 redirect/runbook/origin: 3/3 rc0, including authenticated positive, foreign-hop
  pair, delivery/hash STOP ordering and origin drift mutant.
- R107 underlying retry pair: true, HTTP500->clean writes1 versus foreign->clean writes0.
  Its lifecycle wrapper rewrites worker outputs, so the wrapper is not run; underlying
  diagnostics/harness exercise the same logic without editing worker evidence.
- Own R12 review diagnostic: 7 cases, two counterexample predicates true, rc0.
  Four retry cases: ordinary non-timeout0/false/one verification; timeout-text twin
  1/true/two; actual timeout1/true/two; HTTP4040/false/one.
  Three cleanup cases: clean final present/success; relatch+successful unlink final absent;
  relatch+EPERM final present/nonzero, yet the error claims deletion.

The R12 diagnostic extends COMMITTED MOCK HARNESS text in memory with unique checked anchors;
it never edits production source or either old harness. No real browser, credentials, login,
MFA, portal network, host action, IAM mutation, publication replay or live CVO S3 read occurred.
Password/sign-in recovery is the explicitly documented marker-absent bucket in this delivery;
the decisive new failure is a non-timeout exception, not a reopened argument about that intent.
Clauses (i)/(ii)'s named source obligations are supported by code plus paired tests.
Clause (iv)'s finite prior arms hold; their passing shape does not imply clause (iii).

## Publication and provenance

Both halves name packet3676e2a26e8018c3ba91627f3df8fdd0b4a96cc7:
COO737ef371bb and CTO1d78321465. Own object hashing agrees with their signed b6f75a20.
Ledger opened d31ff772b4 at06:05:19Z, closed acd048314f at06:10:30Z;
one S3 key, VersionId vLUlxFLiMvDtNnY5rH4Z6pGl4Slp9Man, matching readback.
README hash was updated in that commit. Wrapper not republished. COO packet reports a later
fresh GET agreeing. These are read event records, not CVO live verification or on-host proof.

All18 R112 artifact pins resolve as blobs (checker calls bare blobs UNRESOLVED-HERE).
17/18 match current path blobs. Result pin0d19277b predates its HEAD4c5a60d2 publish addendum;
C-S187 is metadata-only. The proof's broad no-real-S3 exclusion also needs pass scoping.
R11 recovery d84408cbd3 fixes much of C-S174 but introduces a false claim that the diagnostic
computed f03666ef and fffef738 was only a packet typo. The actual cited diagnostic records
fffef738; the recovered result explains CRLF correctly. C-S174 is NOT closed.

## Dispositions, clocks, and outcome grain

Ten new CVO rows C-S178..187. W13-S3 is accepted but mapped to existing C-S174, not duplicated.
W13-S4 records the historical README timing departure: arm(f) explicitly named both prose and
hash. Later approval does not rewrite it. No cosmetic revert/reapply is useful after publication;
future sequencing must be explicit. W13-S5's earlier terminal foreign-hop refusal is intended.

S117 receives a CVO disposition and its missing remediation carrier. A worker commit was
mistaken for the end of its turn; recovery was successful here but the inference is unsafe.
Preserve W13-S2's corrected attribution: terminal-order revocation is law, NOT a gate defect.
R12 pending-until-publish is progress; packet's generic gate-limitation carry remains rejected.

Only C-S170/C-S171 existing clocks advance to DISARMED/REMEDIATED/closed, at code-defect grain.
C-S174, W13-S1/S2, C-S158/S159, C-S153/C-S127 and older host-byte limits remain open.
Four new OPEN remedies: C-S179 ARMED; C-S180, S117, C-S187 INERT.
No bulk closure or prior judgment regrade. The >=2-round staleness denominator is disclosed
by the commit gate; the prior 166 is a prior-round count, not asserted unchanged here.

FWD-2 remains SPLIT / NOT_REALIZED overall. PRD v0.15 requires scoped suggestions, membership,
report retrieval/polling/cache/PDF and swapped identifiers/revoked grants against warm cache.
Capture-tool mock repairs are not that whole served matrix or authenticated PDF/latency evidence.
FWD-11 remains NOT_REALIZED overall: prior backend bucket-program closure is only a contribution.
The actual bar includes Global report/export at TWO firms, advisor refusal and same-client/revision
parity. No real human capture occurred. W10-S2 park, S116/W1-S47 external ownership,
Andrew/CRO break-glass decision and other existing holds remain.

ONE round-12 slug: REMEDIATION_v6.md to 1.0.0_SA_CTO only.
No new outcome is required by these findings; CTO reads them into analysis before any COO recut.

## Rows

```json
[
  {
    "id": "IRPT_BCKEND-C-S178",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~B",
    "surfaced_at": "2026-09-22T06:40:00Z",
    "one_line": "R112-AC3 FAIL: error-message substring matching admits a non-timeout navigation failure to retry.",
    "spec_asserts": "R112-AC3(iii), issued at 91c8a95a7e, requires a genuinely closed retry taxonomy; arm (d) makes every generic non-timeout navigation error terminal on its first occurrence.",
    "world_is": "On published blob 82abe684, a certificate-error mock refuses with ordinary URL text but retries and writes when the same error message contains a same-origin query parameter timeout=1. This is positive counterevidence to (iii), independent of cleanup reachability and README timing.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~13/IRPT_BCKEND.TO-IB-rtl-1.the-capture-tool-invariant-guard-at-the-write-boundary.proof_of_spec.json@d8bac06b89a075d966b20de3f111a2224e42f5f2",
        "infra/aws/ec2/investor-reporting-export/capture-session.cjs:404 @cb6429dc9e",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R12_CAPTURE_FAILURE_DIAGNOSTIC.cjs (co-committed): four retry cases plus three cleanup cases."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Formal judgment record, not an additional remediation.",
    "grades": [
      {
        "criterion": "R112-AC3",
        "instance": "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~13/IRPT_BCKEND.TO-IB-rtl-1.the-capture-tool-invariant-guard-at-the-write-boundary.proof_of_spec.json@d8bac06b89a075d966b20de3f111a2224e42f5f2",
        "verdict": "FAIL",
        "reason": "Clause (iii) fails affirmatively: /timeout/i tests the entire goto rejection message, not its failure cause. Paired non-timeout ERR_CERT_AUTHORITY_INVALID mocks differ by timeout=1 in allowed same-origin check-route/message text; ordinary gives 0 writes/1 verification/exit1, substring case 1 write/2 verifications/success. Actual timeout and HTTP404 controls discriminate. Clauses (i)/(ii)'s original defects are repaired with positive twins; R91 four safe arms, R101 three safe arms and underlying R107 pair/diagnostics rerun successfully. Finite passes do not cover this new negative. No real incident or host execution is asserted."
      }
    ]
  },
  {
    "id": "IRPT_BCKEND-C-S179",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~B",
    "surfaced_at": "2026-09-22T06:40:00Z",
    "one_line": "The timeout classifier reads arbitrary message text instead of the navigation failure's identity.",
    "spec_asserts": "Only a timeout, HTTP5xx or marker-absent-after-load may retry; generic non-timeout failures must stop before any state write.",
    "world_is": "The catch classifies /timeout/i over e.message. A non-timeout certificate error with timeout in its URL text is retried, then a clean attempt writes and prints success. The same error without that substring refuses immediately.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/ec2/investor-reporting-export/capture-session.cjs:334-337,400-413 @cb6429dc9e: same-origin check-route override is allowed; unanchored message regex classifies errors.",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R12_CAPTURE_FAILURE_DIAGNOSTIC.cjs (co-committed): ordinary certificate error 0/false/1 verification; query-text twin 1/true/2; actual timeout 1/true/2; HTTP404 0/false/1."
      ]
    },
    "disposition": "GRADUATED",
    "disarm_owner": "2.0.0_SA_COO~B",
    "notes": "Mocked counterexample to a published predicate, not proof of a live TLS incident. Use positive error identity/structured classification, retain supported timeout behavior, and test non-timeout text confusables. No widening or live replay."
  },
  {
    "id": "IRPT_BCKEND-C-S180",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~B",
    "surfaced_at": "2026-09-22T06:40:00Z",
    "one_line": "Delete-on-relatch swallows deletion failure and falsely reports the state file was deleted.",
    "spec_asserts": "Arm (b) and README lines103-108 require deletion of a latched post-rename file; the error message claims that deletion occurred.",
    "world_is": "Extending the worker's own synchronous post-rename-event model with only unlinkSync throwing EPERM leaves diskFinal=true, deleted=false, exit1, while the message says was deleted. The successful-deletion twin removes it and the clean twin succeeds.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/ec2/investor-reporting-export/capture-session.cjs:475-482 @cb6429dc9e: unlink exceptions are swallowed before unconditional deletion claim.",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R12_CAPTURE_FAILURE_DIAGNOSTIC.cjs (co-committed): three in-memory filesystem cases; no real writes."
      ]
    },
    "disposition": "GRADUATED",
    "notes": "INERT coverage/diagnostic finding: synchronous event injection is the issued worker model, not demonstrated normal Node event-loop reachability. Not independently used to fail R112-AC3. Require truthful cleanup-failure reporting and an explicit residual-state handling contract; do not promise infallible deletion or claim a live leaked credential."
  },
  {
    "id": "IRPT_BCKEND-C-S181",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~B",
    "surfaced_at": "2026-09-22T06:40:00Z",
    "one_line": "W13-S3 is a genuine LF/CRLF grain distinction; the remaining contradiction stays on C-S174.",
    "spec_asserts": "Hashes identify exact bytes, not equivalent logical text; a diagnostic's recorded source hash must not be rewritten by a summary.",
    "world_is": "R11 diagnostic JSON records fffef738 checkout bytes; published git bytes hash f03666ef. R12 likewise has checkout b6f26643 and git b6f75a20. Normalization reconciles bytes, but recovered R11 proof incorrectly says the diagnostic computed f03666ef and the old value was only a packet transcription error.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md@d84408cbd3#IRPT_BCKEND-W13-S3",
        "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~13/IRPT_BCKEND.TO-IB-rtk-1.the-capture-tool-complete-lifecycle-observer-and-sticky-refusal.proof_of_spec.json@d84408cbd3: controls.mutant.observed.",
        "infra/aws/ec2/investor-reporting-export/capture-session.cjs@cb6429dc9e: own Buffer hash read and LF-normalized checkout equality."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Finding accepted, not denied. Its unresolved documentation correction is already C-S174's open remedy; no duplicate clock. R12 packet names both byte grains correctly.",
    "adjudicates": [
      "IRPT_BCKEND-W13-S3"
    ]
  },
  {
    "id": "IRPT_BCKEND-C-S182",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~B",
    "surfaced_at": "2026-09-22T06:40:00Z",
    "one_line": "W13-S4 records a real timing departure, not permission hidden in the earlier prose requirement.",
    "spec_asserts": "Arm (f) explicitly bundles BOTH retry-behavior and expected-hash README lines with publish; arm (d) requires matching content but does not expressly require a pre-publish commit.",
    "world_is": "Retry prose landed at 6c7713e1df, before publish acd048314f; hash updated at publish. COO's subsequent half endorses the split, but that does not change the historical issued text. Both prose and published bytes now exist.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rtl-1.the-capture-tool-invariant-guard-at-the-write-boundary.md@91c8a95a7e: arms(d),(f).",
        "infra/aws/ec2/investor-reporting-export/README.md@6c7713e1df and @acd048314f.",
        "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md@c33e9f3d38#IRPT_BCKEND-W13-S4"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Historical timing departure recorded. Do not rewrite history or revert/reapply correct prose to simulate simultaneity. Current provenance gap has ended with publication; future orders must explicitly sequence preparation, checks, and publish-time documentation. This is not the reason for the R112-AC3 FAIL.",
    "adjudicates": [
      "IRPT_BCKEND-W13-S4"
    ]
  },
  {
    "id": "IRPT_BCKEND-C-S183",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~B",
    "surfaced_at": "2026-09-22T06:40:00Z",
    "one_line": "W13-S5's earlier terminal refusal is intended strengthening, not a regression.",
    "spec_asserts": "Foreign-origin hops are never retryable; regression evidence must retain successful and refused outcomes, not an obsolete retry count.",
    "world_is": "Unmodified R9 has 6/6 unchanged write/success verdicts; verification foreign hop now refuses on attempt1 instead of exhausting5. Five other result objects match. Its old plain-object stub lacks event hooks, so readinessOutcome supplies the terminal fallback.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md@c33e9f3d38#IRPT_BCKEND-W13-S5",
        "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~13/battery_ib_rtl_1.py@6c7713e1df: own invariant rerun; 5/6 identical R9 objects.",
        "infra/aws/ec2/investor-reporting-export/capture-session.cjs:290-300 @cb6429dc9e"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "No defect in the changed refusal. Packet mislabels the affected R9 case as non-timeout error; the actual row correctly names verification foreign hop. CTO's identical shorthand is read at verdict grain, not full-object equality.",
    "adjudicates": [
      "IRPT_BCKEND-W13-S5"
    ]
  },
  {
    "id": "IRPT_BCKEND-C-S184",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~B",
    "surfaced_at": "2026-09-22T06:40:00Z",
    "one_line": "C-S170 and C-S171 close at their specific source-defect grain, not whole-capture approval.",
    "spec_asserts": "C-S170 requires a check after storageState await; C-S171 requires request AND response navigation filtering with positive controls.",
    "world_is": "Source457-458 now checks after state capture; response223 and request229 filter non-navigation requests. Own R11 pair flips foreign storage-hop to refusal and foreign resource to success, retains both same-origin positives and foreign-navigation refusal. Signed/published b6f75a20 is the tested git source.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/ec2/investor-reporting-export/capture-session.cjs:219-231,457-475 @cb6429dc9e",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R11_CAPTURE_LIFECYCLE_DIAGNOSTIC.cjs@d20200b92c: own pinned old/new reruns.",
        "org/critical_paths/change_management/20260922T0605Z_irpt-rtl-1-capture-tool-publish_deploy_completion.md@acd048314f"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Successor evidence authorizes ONLY the two existing REMEDIATION_v5 clock advances. No host-byte attestation, broad lifecycle closure, or capture release."
  },
  {
    "id": "IRPT_BCKEND-C-S185",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~B",
    "surfaced_at": "2026-09-22T06:40:00Z",
    "one_line": "C-S174 is partially repaired, not satisfied: recovered proof contradicts its own diagnostic and result.",
    "spec_asserts": "C-S174 requires truthful final-pass provenance, including the git/checkout hash distinction, not only a publish paragraph.",
    "world_is": "Recovery d84408cbd3 adds final publish, corrected packet/ledger and worker rows; worktree residue is drained. But controls.mutant.observed rewrites the diagnostic hash to f03666ef and calls fffef738 a packet-only transcription error, while the cited JSON and result still correctly say checkout fffef738.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~13/IRPT_BCKEND.TO-IB-rtk-1.the-capture-tool-complete-lifecycle-observer-and-sticky-refusal.proof_of_spec.json@d84408cbd3: controls.mutant.observed.",
        "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~13/IB-rtk-1_repaired_r10_lifecycle_diagnostic.json@0d0c8cdc4d: sourceSha256.",
        "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~13/the-capture-tool-complete-lifecycle-observer-and-sticky-refusal.result.md@d84408cbd3"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Existing C-S174 remains OPEN; no duplicate remediation or regrade of frozen R107. Packet's claim satisfied is corrected here. Metadata-only remedy; no republish."
  },
  {
    "id": "IRPT_BCKEND-C-S186",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~B",
    "surfaced_at": "2026-09-22T06:40:00Z",
    "one_line": "S117 needs its own CVO disposition: branch commits did not establish worker termination.",
    "spec_asserts": "L7 recovery must preserve ongoing worker work; an issuer's self-graduation is not a CVO read or a remediation row.",
    "world_is": "S117 records worktree removal before the worker's final notification, followed by successful recovery. The row self-graduates by analogy to C-S174/W13-S2, but those grade metadata/order lifecycle, not the distinct premature cleanup inference. No S117 remediation carrier existed at intake.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md@91c8a95a7e#IRPT_BCKEND-S117",
        "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~13/the-capture-tool-complete-lifecycle-observer-and-sticky-refusal.result.md@d84408cbd3: recovery account.",
        "Own git worktree list: no retained IRPT_BCKEND worker tree; no cleanup performed by CVO."
      ]
    },
    "disposition": "GRADUATED",
    "adjudicates": [
      "IRPT_BCKEND-S117"
    ],
    "notes": "INERT process repair owned by issuer. Require final report/termination confirmation before removal, plus committed/dirty-work reconciliation; a commit alone proves output, not that all further writes ended. Recovery evidence confirms no loss here, not a universal no-loss property."
  },
  {
    "id": "IRPT_BCKEND-C-S187",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~B",
    "surfaced_at": "2026-09-22T06:40:00Z",
    "one_line": "R12 final proof still pins the pre-publish result despite a committed publish addendum.",
    "spec_asserts": "Final proof artifact pins must bind the delivered final-pass result and disclose exclusions at the right pass.",
    "world_is": "All18 pins resolve as blobs;17 equal current path blobs. The result pin0d19277b is pre-publish, while HEAD4c5a60d2 adds the sixth-pass publish addendum. Final proof also retains an unqualified exclusion of any real S3 action despite its own published-event evidence.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~13/IRPT_BCKEND.TO-IB-rtl-1.the-capture-tool-invariant-guard-at-the-write-boundary.proof_of_spec.json@d8bac06b89: artifacts_produced result row and declared_exclusions.",
        "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~13/the-capture-tool-invariant-guard-at-the-write-boundary.result.md: diff blobs0d19277bfd64bf63fbd79d1be1b5a41867c3d435..4c5a60d2c063209de915d7ca142f9f8877f3cc95 adds ONLY publish-continuation addendum."
      ]
    },
    "disposition": "GRADUATED",
    "notes": "Metadata-only correction to actual final result pin and pass-scoped exclusions; preserve historic tests, output verdicts and event hashes. No publish replay. Structural checker reports bare blob refs UNRESOLVED-HERE, so own object read supplies this evidence."
  }
]
```

