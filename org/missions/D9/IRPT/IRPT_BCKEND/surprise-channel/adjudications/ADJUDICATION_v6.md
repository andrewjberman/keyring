# IRPT_BCKEND -- round 10 early L9 judgment: R101-AC3 FAIL

Author: `3.0.0_SA_CVO~B`. Read 2026-09-22 01:57-02:04 UTC. Evidence snapshot
`1b62c69ca445594278b8a9af244d506104f8587b`; graded proof vintage `4a65336eb44dc4cf908888a590dbb5acb92a29a4`.
File v6 is a rollover counter, not round 6. This is a bounded early grade of IB-rtj-1,
NOT the round-10 drain compilation, remediation slug, round close, or capture authorization.

## Receipt, authority, and boundary

Exact unread messages read: COO~B `20260922T015635Z_2.0.0_SA_COO_B__URGENT__out_of_band__Please_grade_R101-.md`
(99367), and CTO `20260922T015722Z_1.0.0_SA_CTO_Concur_with__ii___R101-AC3_is_3.0.0_SA_C.md`
(99370). COO requests the early grade and retracts attribution of its rerun as CVO closure.
CTO agrees that only this seat grades R101-AC3 and says the ask to Andrew stays HELD until
the verdict. Neither sender's rerun is adopted as the grade. The CVO's L9 ownership permits
this artifact; urgency does not authorize a capture, repair, publish, or premature L10.

Canonical-flow receiving check, bound to the issued task order: ACCEPT by
`proof-of-spec-check.py`, 3 acceptance rows, zero violations. The separate explicit
`R101-AC1,R101-AC2,R101-AC3` coverage invocation also returns VALID/0. These are form checks.
The checker reports 18 bare blobs UNRESOLVED-HERE and one commit-resolved ledger row.
CVO independently resolves all 18 blobs: 17 equal current artifact blobs; the result.md
pin is stale (C-S160). The ledger commit resolves normally; a commit hash is not a blob hash.
Source and project adjudication paths were clean before this act. No other's files edited.

## Judgment against the issued bar

**R101-AC3 FAIL.** Its three limbs are conjunctive. The exact initial-navigation
counterexample in C-S153 is repaired, but that narrower result does not establish the
issued requirement that EVERY navigation/interactive-interval response be checked and a
foreign hop at ANY point refuse before further action. Two independently exercised residuals
below defeat that requirement. These are pre-existing uncovered behaviors, not a claim that
the new initial-chain check introduced them. Repair occurred, so NOT_EVALUATED is inapplicable.

1. **Lifecycle (i): FAIL.** At `capture-session.cjs@bfe67b1eab`, :144-169 walks a supplied
   response and :228-229 applies it to the initial goto. :249 waits for human interaction
   without a page/context navigation observer; only the NEXT goto response at :250-255 is
   read. A main-frame foreign hop and return during that wait is invisible. Separately,
   :186 detects a foreign verification hop but :255-259 treats it as retryable; a subsequent
   clean navigation writes at :267-270. The cell's arm (b) expressly requires refusal before
   further action for a foreign hop anywhere, not eventual success after an origin violation.
2. **Runbook (ii): satisfied at documented-procedure grain.** `README.md@7f5c2dad5a:118`
   says NOT optional, NOT one-time, EVERY time. :135-136 copies exactly the two keys;
   :137 prints both hashes; :142-143 gives the packet's exact expected hashes; :144 says
   STOP on either mismatch, before :149 invokes the wrapper. A real operator's compliance
   and host bytes are UNMEASURED. No requirement for a host experiment is silently invented.
3. **Regression (iii): not a blanket PASS.** CVO reran the UNCHANGED R91 battery:
   command/readiness/origin/diagnostic each exit 0 with its original token. Its packet arm
   exits 1: the old packet still names `ea60b932...`/`5b26be91...`, whereas the repair is
   `c5a18898...`/`defcb585...`. This is an expected vintage mismatch, not proof the NEW
   packet is invalid. The issued phrase "SAME battery shape" is not discharged by skipping
   that arm. No publish arm was replayed: it contains real S3 writes. The worker's new packet,
   signed halves, and closed ledger support a separate, inherited publish event, not a
   claim that all six original invocations were rerun successfully. Limb (i) independently
   decides FAIL even if CTO accepts a properly rebound new-packet comparison for limb (iii).

## Independent exercises and exact byte grain

`capture-session.cjs` blob `c5a18898985158abc1679241b95e822a1b75799d`, SHA256 of LF git bytes
`defcb58572276f36036d610d296f53df32f86477ffb3e6b17aab00c6f6c2d95a`.
Worktree SHA256 `72c796968cd8ea7d42f5be8c2dd0326c6b313ffe01541cf89b40061225b365cb`.
CVO ran the diagnostic against BOTH grains with identical case results; line endings do not
alter this verdict. The unchanged .sh blob is `d704adfb7b6a3ee904c3ba7173eb81533679c97b`.

R101 battery arms redirect, runbook, origin each exit 0. Redirect prints 6/6 intended R9
shapes, 3/3 unchanged R8 results, the single-difference initial-hop pair, and fresh positive.
Runbook finds 7/7 required lines, all delivery/verification lines before wrapper (144 < 149).
CVO independently checks those seven requirements against the actual git-blob hashes:
current runbook true; a memory-only copy with the delivery block removed false; a copy
with the EVERY-time instruction replaced by optional wording false (3/3 expected results).
Origin compares the typed origin with the renderer's Terraform root and catches a mutated
allowlist. The R8 no-instance-id limitation remains explicit; R91 diagnostic's id-supplied
copy exercises the actual readiness refusals. Neither original CVO diagnostic was edited.

New CVO diagnostic, co-committed:
`org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R10_CAPTURE_LIFECYCLE_DIAGNOSTIC.cjs`.
Run from repository root with `node <path>` or `node <path> c5a18898985158abc1679241b95e822a1b75799d`.
All Playwright, prompt and write operations are stubbed. The interval model emits main-frame
request/response/navigation events during the documented human wait, before ENTER. The bad/good
interval pair differs ONLY in its middle hop. It is not a real-browser observation or a claim
that a foreign server, credential leak, or portal redirect was actually encountered.

| Case | Writes | Success | Deciding observation |
|---|---:|---|---|
| Same-origin interval positive | 1 | yes | Positive control, one interval navigation |
| Interactive portal -> foreign -> portal | 1 | yes | Zero interval chain reads; zero installed observers |
| Initial foreign hop control | 0 | no | Refuses before first prompt: the R9 fix works |
| Foreign verification on every attempt | 0 | no | Five warnings, then exhausted attempts |
| Foreign verification once, then clean | 1 | yes | Two verification calls; violation did not latch refusal |
| HTTP500 control | 0 | no | Readiness still refuses |

The same six cases against old blob `ea60b932bd4fd8af1f08548ce51022c2740af8b2` change exactly
ONE write/success pair: the initial-hop control becomes 1/yes. The two residuals occur on
both sources; the same-origin positive succeeds on both. This independently corroborates
CTO's narrow repair observation without extending it to complete lifecycle correctness.
**Diagnostic exit 0 means both residual defects REPRODUCED, NEVER repair acceptance.**
Old blob exits 1 because the initial-hop refusal control is intentionally not satisfied.

New packet `2450320a688a4740af81d3a72f281b2a06f05b23` carries one changed S3 key, the cjs;
the .sh is unchanged and not republished. CVO read both exact signed halves (COO `5b67db0397`,
CTO `088669b331`) naming that packet. Ledger
`org/critical_paths/change_management/20260922T0137Z_irpt-rtj-1-capture-tool-publish_deploy_completion.md@ef15e1bd45`
records open-before-act at `8ff0ffc1af`, one closed leg, S3 VersionId
`llAMqS_QPopRTb3T9KWyHLX8jJvoQWS4`, and readback SHA256 equal to the cjs blob. These are
inherited event records. CTO's latest message reports a further GET, not a fresh CVO GET.
No on-host measurement, host action, portal network, real browser, credential, or MFA act here.

## L9 rows (rolling; no L10 slug)

The existing C-S153/C-S156 remediation clocks are NOT edited in this mid-round judgment.
C-S153's narrow counterexample and C-S156's runbook omission have source remedies; universal
capture safety and host delivery remain unproved. Existing capture HOLD remains unchanged.
The following grounded findings are carried for the round's single remediation slug; no
mid-round peer message is sent under the spine L8/L10 send rule. This artifact is the receipt.

```json
[
  {
    "id": "IRPT_BCKEND-C-S157",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~B",
    "surfaced_at": "2026-09-22T02:04:21Z",
    "one_line": "Early R101-AC3 judgment FAIL: initial-hop repair works, but the issued complete-lifecycle bar does not hold.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": { "status": "GROUNDED", "evidence": [
      "IRPT_BCKEND.TO-IB-rtj-1.the-capture-tool-navigation-lifecycle-and-host-delivery-runbook.md@0601daa7f6, arm (b), R101-AC3(i)-(iii).",
      "infra/aws/ec2/investor-reporting-export/capture-session.cjs@bfe67b1eab:249-269; co-committed IRPT_BCKEND_R10_CAPTURE_LIFECYCLE_DIAGNOSTIC.cjs, six cases, two residual counterexamples."
    ] },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Grade record only; substantive residual findings are C-S158/C-S159. Not a round close or capture Go.",
    "grades": [{
      "criterion": "R101-AC3",
      "instance": "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~13/IRPT_BCKEND.TO-IB-rtj-1.the-capture-tool-navigation-lifecycle-and-host-delivery-runbook.proof_of_spec.json@4a65336eb44dc4cf908888a590dbb5acb92a29a4",
      "verdict": "FAIL",
      "reason": "Issued arm (b) and AC3(i) require every navigation/interactive interval and refusal before further action on any foreign hop. An interval foreign hop is unseen (writes=1, success=true), and a detected foreign verification hop followed by a clean retry also writes=1/succeeds. Positive and refusal controls fire. README satisfies (ii) at procedure grain, not host execution. Four unchanged R91 arms pass; old packet arm fails its stale source pin, and live publish is not replayed. Failure of (i) independently defeats the conjunction; no urgency-based hold release."
    }],
    "spec_asserts": "R101-AC3 PASS iff lifecycle, unconditional pre-capture delivery/verification, and same-shape regression limbs all hold.",
    "world_is": "Repair occurred and initial-hop/runbook controls pass, but two exercised lifecycle counterexamples remain; FAIL, not NOT_EVALUATED."
  },
  {
    "id": "IRPT_BCKEND-C-S158",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~B",
    "surfaced_at": "2026-09-22T02:04:21Z",
    "one_line": "The human-interaction wait does not observe navigations: a foreign intermediate hop returns to portal and capture succeeds.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~B",
    "grounding": { "status": "GROUNDED", "evidence": [
      "infra/aws/ec2/investor-reporting-export/capture-session.cjs@bfe67b1eab:221-250 installs no navigation observer before asking the human to operate the same page.",
      "IRPT_BCKEND_R10_CAPTURE_LIFECYCLE_DIAGNOSTIC.cjs co-committed: same-origin and middle-hop-foreign interval pair both writes=1/success=true, intervalChainReads=0, intervalListeners=0. Reproduced on c5a18898985158abc1679241b95e822a1b75799d and worktree bytes."
    ] },
    "disposition": "GRADUATED",
    "spec_asserts": "IB-rtj-1 arm (b): EVERY verification/interactive-interval navigation and any foreign hop at ANY point must be checked and refuse before further action.",
    "world_is": "Only returned goto responses are checked; the human-wait navigation is unobserved and a later clean verification permits capture.",
    "notes": "Remedy holder COO~B via normal repair issuance. Retain the capture hold; require a lifecycle guard and discriminating interval pair plus positive control. ARMED describes future normal use of the published tool, not a measured live leak. No worker contact or source repair by CVO."
  },
  {
    "id": "IRPT_BCKEND-C-S159",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~B",
    "surfaced_at": "2026-09-22T02:04:21Z",
    "one_line": "A detected foreign verification hop is retryable, not a terminal refusal: the next clean attempt writes a session.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~B",
    "grounding": { "status": "GROUNDED", "evidence": [
      "infra/aws/ec2/investor-reporting-export/capture-session.cjs@bfe67b1eab:186 returns an origin-refusal string; :255-259 warns/continues; :267-270 captures after a clean retry.",
      "IRPT_BCKEND_R10_CAPTURE_LIFECYCLE_DIAGNOSTIC.cjs co-committed: foreign every attempt refuses after 5; foreign first attempt then clean writes=1/success=true after 2 verification calls. Initial foreign control refuses before any prompt."
    ] },
    "disposition": "GRADUATED",
    "spec_asserts": "IB-rtj-1 arm (b) requires a foreign hop anywhere in any navigation to refuse before any further action.",
    "world_is": "The violation is detected, but retry state forgets it. All-foreign attempts in older diagnostics concealed acceptance on a subsequent clean attempt.",
    "notes": "Remedy holder COO~B. Preserve retry for ordinary unauthenticated readiness if appropriate, but an origin violation must not be forgotten. Require mixed-attempt regression and positive control. This existed before the second repair; not a newly introduced regression. Hold unchanged."
  },
  {
    "id": "IRPT_BCKEND-C-S160",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~B",
    "surfaced_at": "2026-09-22T02:04:21Z",
    "one_line": "Second-pass proof still pins the first-pass result.md blob that says publish did not run.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": { "status": "GROUNDED", "evidence": [
      "IB-rtj-1 proof@4a65336eb44dc4cf908888a590dbb5acb92a29a4 artifacts_produced result.md pin 35aac8b8bc7025024926b1c2eb61910009718366, deploy_evidence at 7f5c2dad5a.",
      "git show 35aac8b8bc7025024926b1c2eb61910009718366: opening says arm (f) did NOT run. Result at proof commit 4a65336eb4 is b7eea3aeb2817e4e436ce536feb833a1d4a9ee37 and records the completed second pass. Of 18 bare-blob artifacts, 17 match HEAD and this one does not."
    ] },
    "disposition": "GRADUATED",
    "spec_asserts": "The proof's artifact row pins the delivered result supporting the second-pass completion record.",
    "world_is": "The narrative was updated but its artifact pointer still selects the earlier STOPPED report; the actual publish ledger is separately pinned and resolves.",
    "notes": "Remedy holder COO~B: metadata-only pin correction, not a publish replay. Does not negate the inherited ledger event or decide the lifecycle grade."
  }
]
```
