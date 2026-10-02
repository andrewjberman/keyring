# DSGN_AMGTV1 task order -- `AV-zc-3` -- THE RE-ANCHORED POSTURE CHECK IS NAMED FOR WHAT IT GRADES; ITS ZERO PATH IS PLANTED

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-zc-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~76</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no role, policy or grant moves; the harness's existing read-only S3 get-object of the two posture objects (rl-7) runs under the machine's own credentials.
comp-adversary: RUN by the issuer at the cut on portal 41eeda55 -- posturezero.cjs 0 of 3 (FAIL as expected: the old name printed, no zero plant, no legacy predicate).
EGRESS CLASS, declared: NONE off Opal infrastructure. The harness's own read of s3://opal-data-harvest/posture/v1/ (Opal infra, read-only) is the one network act admitted.
</preflight>

## 1. THE CELL -- `AV-zc-3` (round 25, decomposition v25; an instrument cell, ADJUDICATION_v21 conditions)

DIRECT ACT. The CTO's round-23 analysis (`org/missions/D13/DSGN/DSGN_AMGTV1/ledger/ROUND_ANALYSIS.round23.md` @876dfcadb8, ruling 3):
round 23 (AV-zb-4) re-anchored `<KEY>:claims_with_resolved_cite_equal` in
`portal/src/pages/SecurityAnalysis/__harness__/posture.harness.cjs`. It now grades the page's STATED resolved count per claim (and counts
an all-unresolved claim only when every cite reads "Citation not resolved -- "). Two conditions, in that file only:
1. **Rename** the check to what it now grades (e.g. `<KEY>:claims_resolved_count_stated`). Keep it -- do not drop it; the clean run must
   still print 32 CHECKs, green.
2. **Plant the zero-resolved path, and keep the old predicate selectable:**
   - `POSTURE_HARNESS_PLANT=zero` forces EVERY cite of ONE served claim to fail resolution before rendering (the 0-resolved path) and
     prints one line beginning "PLANT ACTIVE:". Under the current (fixed) predicate the run stays GREEN (rc 0, `CHECKS-OK`).
   - `POSTURE_HARNESS_LEGACY_PREDICATE=1` selects the pre-AV-zb-4 predicate (a claim counts only with >= 1 resolved cite). With the zero
     plant it reads RED through the harness's own verdict path (rc != 0, at least one CHECK off its expectation, no uncaught exception).
   - The existing `POSTURE_HARNESS_PLANT=1` (blank every served claim) keeps working and keeps reading red.
Change no page source.

## 2. BOUNDS

1. No server, no install, no push, no deploy, no network except the harness's existing read-only S3 get-object named above.
   REFUSE, do not rescue.
2. Only the file in `<paths>` changes (plus your deliverables and the channel).
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.
4. Write code with the Edit/Write tools ONLY -- never a shell heredoc, `python -c` or a script that rewrites a file.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/__harness__/posture.harness.cjs
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~76/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular the issuer's checks under `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round24/`,
`round23/` and `round15/` (never edit them).

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-zc-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round24/checks/posturezero.cjs"; echo "exit=$?"</invocation><expect>THE ZERO-RESOLVED PATH IS NAMED AND PLANTED: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-zc-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round23/checks/postureharness.cjs" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round15/checks/bound.cjs" ALL leadPanelPattern.harness.cjs errorEmpty.harness.cjs tabs.harness.cjs shell.harness.cjs drafting.harness.cjs execFallback.harness.cjs execPattern.harness.cjs execText.harness.cjs peersCarry.harness.cjs peersPattern.harness.cjs peersReadFailed.harness.cjs modelPattern.harness.cjs posturePattern.harness.cjs thesisLadder.harness.cjs; echo "exit=$?"</invocation><expect>POSTURE.HARNESS RUNS GREEN AND GRADES SOMETHING: 3 of 3 arms, then ALL BOUND: 14 of 14 harnesses green -- and exit=0</expect></criterion>
</proof_of_spec>

AC1: arm 1 the clean run is green with 32 checks and the old name gone; arm 2 the zero plant stays green under the fixed predicate;
arm 3 the zero plant reads red under the legacy predicate. AC2 keeps round 23's harness outcome and all 14 page harnesses.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~76/DSGN_AMGTV1.TO-AV-zc-3.the-posture-check-is-named-and-its-zero-path-planted.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY).
A row id on this project carries the site-z infix: `DSGN_AMGTV1-Z-W76-S<k>`, and its `surfaced_at` is the real UTC time.
Report once: what changed and where, the output line of every criterion, the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** DIRECT ACT (LOCAL), instrument cell. CTO round-23 analysis @876dfcadb8 ruling 3. Chain ~76 alone. Base posturezero 0 of 3 on 41eeda55.

<status>pending</status>
<round>25</round>
<slot>~76</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<direct_act>true</direct_act>
<worker_class>worker-light</worker_class>
