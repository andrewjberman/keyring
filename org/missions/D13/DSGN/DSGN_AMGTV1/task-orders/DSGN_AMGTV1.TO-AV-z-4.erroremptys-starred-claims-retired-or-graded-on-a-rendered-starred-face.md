# DSGN_AMGTV1 task order -- `AV-z-4` -- ERROREMPTY'S STARRED CLAIMS: RETIRED, OR GRADED ON A RENDERED STARRED FACE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-z-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~70</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the harness renders page sources statically.
comp-adversary: RUN by the issuer at the cut on portal DEV 24646bca -- starredclaims.cjs 2 of 3 (FAIL as expected: the starred cases remain with no starred-face anchor; arms 2-3 PASS by design); bound ALL 14 of 14 (control PASS).
EGRESS CLASS, declared: NONE. No fetch off this machine.
</preflight>

## 1. THE CELL -- `AV-z-4` (round 22, decomposition v22; an instrument repair, row DSGN_AMGTV1-Z-W56-S4)

DIRECT ACT. The CTO's round-21 analysis (`org/missions/D13/DSGN/DSGN_AMGTV1/ledger/ROUND_ANALYSIS.round21.md` @e14de1769c, ruling 4 and
section 3A row A4): `portal/src/pages/SecurityAnalysis/__harness__/errorEmpty.harness.cjs` still renders two STARRED cases
(`starred_successful_empty`, `starred_failed_request`) through `LeadPanel` with `starredOnly`, but StarredList left the Lead Panel, so
the claim `starred_error_differs_from_starred_empty` is met by the differing ranking footers, not by any starred face. It grades
nothing. Do ONE of:
- (a) RETIRE the two starred cases and the claim that reads them (with a one-line comment in the harness naming this order and why);
- (b) RE-POINT them at the price face's starred state: `portal/src/pages/SecurityAnalysis/components/PriceBars.tsx` with
  `starredOnly` true prints "No starred names in this list." on a successful empty read; a failed read prints its read-failure
  state. The re-pointed claim must anchor on that rendered text (for example `includes('No starred names')`), so it fails if the
  starred face stops rendering.
**Keep** `ranked_row_click_handlers_found`, `unresolved_row_navigates`, `a_click_sent_a_ticker` and `error_claims_no_daily_row`
exactly as they are: they read the RankedList click tree and the failed-request render, so they ARE exercised. The harness stays
green. Change no page source.

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only the file in `<paths>` changes (plus your deliverables and the channel).
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.
4. Write code with the Edit/Write tools, never through a shell heredoc or `python -c`.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/__harness__/errorEmpty.harness.cjs
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~70/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular the issuer's checks under `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round22/` and
`org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round15/` (never edit them).

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-z-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round22/checks/starredclaims.cjs"; echo "exit=$?"</invocation><expect>ERROREMPTY'S STARRED CLAIMS GRADE A RENDERED FACE: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-z-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round15/checks/bound.cjs" ALL leadPanelPattern.harness.cjs errorEmpty.harness.cjs tabs.harness.cjs shell.harness.cjs drafting.harness.cjs execFallback.harness.cjs execPattern.harness.cjs execText.harness.cjs peersCarry.harness.cjs peersPattern.harness.cjs peersReadFailed.harness.cjs modelPattern.harness.cjs posturePattern.harness.cjs thesisLadder.harness.cjs; echo "exit=$?"</invocation><expect>ALL BOUND: 14 of 14 harnesses green -- and exit=0</expect></criterion>
</proof_of_spec>

AC1: arm 1 the harness is green and its starred cases are retired or anchored on "No starred names"; arm 2 the base harness is the
vacuous form; arm 3 the four exercised RankedList checks still print at their values. AC2 all 14 page harnesses.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~70/DSGN_AMGTV1.TO-AV-z-4.erroremptys-starred-claims-retired-or-graded-on-a-rendered-starred-face.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance.**
Report once: what changed and where, the output line of every criterion, the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** DIRECT ACT (LOCAL), instrument repair. CTO round-21 analysis @e14de1769c ruling 4 / row A4 (Z-W56-S4). Chain ~70
alone. Base starredclaims 2 of 3 on DEV 24646bca.

<status>pending</status>
<round>22</round>
<slot>~70</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<direct_act>true</direct_act>
<worker_class>worker-light</worker_class>
