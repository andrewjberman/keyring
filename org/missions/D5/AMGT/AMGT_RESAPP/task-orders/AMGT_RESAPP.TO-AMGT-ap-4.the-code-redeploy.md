# AMGT_RESAPP task order -- `AMGT-ap-4` -- THE CODE REDEPLOY CARRYING c20fd8cc98, ap-1 AND ap-2's ROUTE READ

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ap-4</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~A</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; one code-only redeploy by hand.
comp-iam: RUN by the issuer at the cut -- 0 new actions: the act carries code only, so the plan must show NO IAM change.
BLIND: no IAM simulation was run for this act (0 new actions); the criteria read served fields off the deployed function, so a denied read shows as a FAIL there.
comp-adversary: RUN by the issuer at the cut -- on deployed lPTMo20T, r66_served c18, c19 and c22 FAIL.
EGRESS CLASS, declared: NONE for the act; the build pip-downloads its pinned wheels.
</preflight>

## 1. THE ACT -- `AMGT-ap-4` (round 66, decomposition s.74)

Under ONE NEVER-2 entry and ONE never-widen pair, redeploy `opal-amgt-scoped-api` at the build commit the GO names. It carries:
- `c20fd8cc98` (the chatter `tone_reason` text);
- AMGT-ap-1 (FWD-39);
- AMGT-ap-2's route read (FWD-36 price 90/365).

Build and upload ONE artifact, then ONE code-only `safe-apply`. `memory_size` stays 1769.

**Begin only when** the GO names the build commit and both halves are committed. Then:
- Re-read the base CodeSha256 the halves name live before the build. A moved base is a STOP.
- Build from a detached checkout at the build commit. Any CHANGED/ADDED/REMOVED file not on the halves' list is a STOP.
- Any destroy, IAM, route or gateway change in a plan is a STOP.
- The package is at 96.8% of the 262,144,000 B ceiling: print the build's size, and a build over the ceiling is a STOP.

A failing criterion is the ROLLBACK trigger: the prior artifact version through one code-only `safe-apply`.

## 2. BOUNDS

1. The act and nothing else. No memory change, no store write, no S3 delete, no vendor call, no push of shared branches, no portal
   promote.

## 3. SURFACES

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ap-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round66/checks/r66_served.py --cell c19 --where deployed; echo "exit=$?"</invocation><expect>C1 PASS on all four chatter windows (no terms-card wording in tone_reason); R66 C19 SERVED: YES on the deployed function; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ap-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round66/checks/r66_served.py --cell c18 --where deployed; echo "exit=$?"</invocation><expect>run from a checkout at the build commit: C1 PASS for BA, AMD and VLO; C2 PASS; R66 C18 SERVED: YES on the deployed function; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-ap-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round66/checks/r66_served.py --cell c22 --where deployed; echo "exit=$?"</invocation><expect>C1 PASS on trending and breakout x 90 and 365; R66 C22 SERVED: YES on the deployed function; and exit=0</expect></criterion>
</proof_of_spec>

The following are run with them and reported (no regression), and the issuer re-reads them:
- `r64_served.py --cell c9 / c10 (30 only) / c11 / c12 / c13 / c14 --where deployed`;
- `r65_served.py --cell c17 --where deployed`;
- `r64_served.py --cell c15 --where deployed`: the cold read stays under 5 s with the word-cloud read added.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/AMGT_RESAPP.TO-AMGT-ap-4.the-code-redeploy.proof_of_spec.json`.
Report once:
- the prior and new CodeSha256 and artifact VersionId
- the CONTENT-DIFF summary and the package size
- every criterion's output lines
- the regression reads, c15 included

Stamp any row's `surfaced_at` with `date -u`.

## 6. AMENDMENT 1 (issuer `2.0.0_SA_COO~Z`, 2026-10-03 ~23:2xZ) -- the pin and one added read (CTO half @98c2b63401)

**The build commit is `b642e313f9`,** or a descendant whose CONTENT-DIFF equals these CHANGED 5:
- `rolling_windows.py`
- `scoped_amgt.py`
- `timeline_api.py`
- `lib/opal_naming.py`
- `infra/logic/registry/reporting_policies.json`

Halves:
- COO: `deliverables/2.0.0_SA_COO~Z/round66/NEVER_WIDEN_HALF_COO_AP4.md` @ffd60053d9.
- CTO: `ledger/NEVER_WIDEN_ROUND66_AP4_CTO_HALF.md` @98c2b63401.

**ADDED READ:** print the RANGE route's cold read on deployed (BA `/security/BA_US_Equity/timeline?from=2026-09-01&to=<today>`, COLD
invokes with Init Duration and AMGT_SEGMENT lines), beside c15, which grades the day route.
- A range read over 5 s is NOT a rollback trigger. It is reported, and the issuer files a row plus a round-67 cell.

Gate limb that graded this modification: none (LIMB 6 fires only on a newly-added order; GATE (viii) does not apply,
`<placeholders>NONE</placeholders>`).

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** s.74; staged until ap-1 and ap-2 drain, ap-3 lands, and the pair is signed. c10's 90/365 clauses now read
generation rows, not "not produced yet"; c22 grades them, and c10 is re-read for its 30-day clauses only.

<status>staged</status>
<round>66</round>
<slot>0.7.0_AE_CloudOps~A</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<proof_genre>DEPLOY</proof_genre>
<worker_class>worker</worker_class>

**ISSUER CLOSE (2.0.0_SA_COO~Z, 2026-10-04 ~00:5xZ):** CLOSED. AE~A `abb9bd85de` built at pin `b642e313f9` (355 / 350 / 5).
- CodeSha256 `lPTMo20T` -> `FcVBPafw`, VersionId `Pj6GLEdKjRnDFwBjZzOSR2gYAsQPHilG`; memory 1769.
- AC1 c19, AC2 c18 and AC3 c22 PASS.
- c15 cold 3 of 3 at 2.03-2.33 s. The ADDED range read was 9 of 12 cold at 2.03-2.55 s, 0 over 5 s, so no round-67 word-cloud cost cell.
- Regressions YES. c10's 90/365 clauses were retired at `6e1852e03f` (row Z-S344).
- NEVER-2 entry `c381a73995` closed.

Issuer re-read on deployed: c18 YES (BA, AMD and VLO 40 terms each; the empty window with its reason), c19 YES (4 windows), c22 YES (94/95 rows, `window_end` 2026-10-02 = the last trading day), c9-c14 YES, c17 YES. Correction: this half's 'VLO 22 terms' was an earlier local read; VLO serves 40 on deployed.

<status>complete</status>
