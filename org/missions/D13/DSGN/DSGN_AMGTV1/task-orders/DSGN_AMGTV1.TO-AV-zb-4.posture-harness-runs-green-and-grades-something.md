# DSGN_AMGTV1 task order -- `AV-zb-4` -- POSTURE.HARNESS RUNS GREEN AND GRADES SOMETHING

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-zb-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~73</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no role, policy or grant moves; the harness's existing read-only S3 get-object of the two posture objects (rl-7) runs under the machine's own credentials.
comp-adversary: RUN by the issuer at the cut on portal DEV a730d8ce (= 419ef41d for this file) -- postureharness.cjs 0 of 3 (FAIL as expected: TypeError useCollectedChatter, no CHECK lines).
EGRESS CLASS, declared: NONE off Opal infrastructure. The harness's own read of s3://opal-data-harvest/posture/v1/ (Opal infra, read-only) is the one network act admitted.
</preflight>

## 1. THE CELL -- `AV-zb-4` (round 23, decomposition v23; an instrument repair, row DSGN_AMGTV1-Z-W69-S1)

DIRECT ACT. The CTO's round-22 analysis (`org/missions/D13/DSGN/DSGN_AMGTV1/ledger/ROUND_ANALYSIS.round22.md` @eee9380be7, ruling 6
and section 3 row 4): `portal/src/pages/SecurityAnalysis/__harness__/posture.harness.cjs` throws
`TypeError: (0 , useLeadPanelApi_1.useCollectedChatter) is not a function` (SecurityOverlay.tsx calls a hook its `SOURCE_STUBS` entry
for `src/pages/SecurityAnalysis/hooks/useLeadPanelApi.ts`, ~line 246, does not carry). Two changes, in that file only:
1. **Repair:** bring the hook stubs up to what the rendered components call today (at least `useCollectedChatter`; compare with the
   stub set `tabs.harness.cjs` carries, ~line 162-178 there) so the harness runs to its verdict: rc 0, `CHECKS-OK n of n`. If a check
   then reads a value other than its expectation because the PAGE changed since the harness was written (e.g. round-22's posture-claim
   guard), re-anchor that check to the page's current designed behaviour -- never delete it, never weaken it -- and say which in your
   report.
2. **The plant knob:** when `process.env.POSTURE_HARNESS_PLANT === '1'`, the harness corrupts ONE posture input it grades (for example
   blank every served basis claim, or flip a verdict) before rendering, so at least one CHECK reads a value other than its expectation
   and the harness exits non-zero through its own verdict path (no uncaught exception). Without the variable nothing changes. Print
   one line naming the plant when it is active.
The harness's own read-only S3 fetch of the two posture objects (into `<workspace>/.scratch/`) is admitted; nothing else leaves the
machine. Change no page source.

## 2. BOUNDS

1. No server, no install, no push, no deploy, no network except the harness's existing read-only S3 get-object named above.
   REFUSE, do not rescue.
2. Only the file in `<paths>` changes (plus your deliverables and the channel).
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.
4. Write code with the Edit/Write tools, never through a shell heredoc or `python -c`.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/__harness__/posture.harness.cjs
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~73/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular the issuer's checks under `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round23/`
and `round15/` (never edit them).

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-zb-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round23/checks/postureharness.cjs"; echo "exit=$?"</invocation><expect>POSTURE.HARNESS RUNS GREEN AND GRADES SOMETHING: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-zb-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round15/checks/bound.cjs" ALL leadPanelPattern.harness.cjs errorEmpty.harness.cjs tabs.harness.cjs shell.harness.cjs drafting.harness.cjs execFallback.harness.cjs execPattern.harness.cjs execText.harness.cjs peersCarry.harness.cjs peersPattern.harness.cjs peersReadFailed.harness.cjs modelPattern.harness.cjs posturePattern.harness.cjs thesisLadder.harness.cjs; echo "exit=$?"</invocation><expect>ALL BOUND: 14 of 14 harnesses green -- and exit=0</expect></criterion>
</proof_of_spec>

AC1: arm 1 the clean run exits 0 with `CHECKS-OK n of n`; arm 2 with `POSTURE_HARNESS_PLANT=1` it exits non-zero with at least one red
CHECK and no crash; arm 3 the planted run prints the clean run's CHECK names. AC2 the other 14 page harnesses stay green.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~73/DSGN_AMGTV1.TO-AV-zb-4.posture-harness-runs-green-and-grades-something.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY).
A row id on this project carries the site-z infix: `DSGN_AMGTV1-Z-W73-S<k>`.
Report once: what changed and where, the output line of every criterion, the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** DIRECT ACT (LOCAL), instrument repair. CTO round-22 analysis @eee9380be7 ruling 6 / row 4 (Z-W69-S1). Chain ~73
alone. Base postureharness 0 of 3 on DEV a730d8ce.

<status>complete</status>
<round>23</round>
<slot>~73</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<direct_act>true</direct_act>
<worker_class>worker-light</worker_class>
