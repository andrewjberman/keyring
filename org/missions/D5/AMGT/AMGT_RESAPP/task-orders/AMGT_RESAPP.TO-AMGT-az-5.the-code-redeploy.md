# AMGT_RESAPP task order -- `AMGT-az-5` -- THE CODE REDEPLOY CARRYING az-2 AND az-4

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-az-5</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~A</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no new cron, alarm, monitor or cadence; one redeploy by hand. The daily snapshot schedule is unchanged.
comp-iam: RUN by the issuer at the cut -- denominator: 2 build cells; az-2 and az-4 add no read path (the same objects). No IAM leg.
comp-iam coverage: BLIND to an IAM change outside the plan; the plan STOPs on any IAM resource.
comp-adversary: RUN by the issuer at the cut -- on deployed D29LJCXh, r76 c62 and c63 FAIL; c65 FAILS locally.
EGRESS CLASS, declared: NONE for the act; the build pip-downloads its pinned wheels.
</preflight>

## 1. THE ACT -- `AMGT-az-5` (round 76, decomposition s.84)

Under ONE NEVER-2 entry and ONE never-widen pair:
1. **Code leg.** Build from a DETACHED worktree at EXACTLY the commit the GO names, never "at or after" it. `memory_size` stays 1769.
   - The CONTENT-DIFF the pair lists is measured at that commit. A file not on the list is a STOP.
   - Then run `round71/checks/leadpanel_cold_warm.py --label after` and read the cold invokes' `AMGT_PHASE` lines.
2. **After the code leg,** invoke the snapshot's scheduled event once (`{"amgt_scheduled_action": "refresh_freshness_snapshot"}`), so
   the snapshot is written by the new code. Read the stamp.

**Begin only when** the GO names the build commit and both halves are committed. Read every live worktree's `.open_deploys/`. Grade
the plan UNTARGETED.

A failing criterion is the ROLLBACK trigger. **Pins:** r74 c55 and r75 c59 run on this redeploy.

## 2. BOUNDS

1. The act and nothing else. No memory change, no IAM change, no S3 delete, no vendor or SEC call, no push of shared branches,
   no portal promote.

## 3. SURFACES

<paths>
infra/aws/terraform/harvest/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 3600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-az-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; for c in c62 c63; do PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round76/checks/r76_served.py" --cell $c --where deployed || exit 1; done &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round75/checks/r75_served.py" --cell c59 --where deployed; echo "exit=$?"</invocation><expect>R76 C62 and C63 and R75 C59 SERVED: YES on the deployed function; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-az-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; for c in c57 c58 c61; do PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round75/checks/r75_served.py" --cell $c --where deployed || exit 1; done &amp;&amp; for c in c53 c55 c56; do PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round74/checks/r74_served.py" --cell $c --where deployed || exit 1; done &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round71/checks/r71_latency.py" --where deployed; echo "exit=$?"</invocation><expect>R75 C57/C58/C61, R74 C53/C55/C56 and R71 C38 SERVED: YES on the deployed function (no regression); and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

The instance is genre DEPLOY, with a NAMED rollback and base-vs-new CodeSha256 as the discriminating control, at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/AMGT_RESAPP.TO-AMGT-az-5.the-code-redeploy.proof_of_spec.json`.
`proof-of-spec-check` must read VALID on the committed bytes.
Report once:
- the prior and new CodeSha256;
- the CONTENT-DIFF and size;
- every criterion's output lines;
- the leadpanel AFTER output and the cold `AMGT_PHASE` table;
- the snapshot stamp after the event.

Stamp any row's `surfaced_at` with `date -u`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** s.84; staged until az-2 and az-4 drain and the pair is signed.

<status>staged</status>
<round>76</round>
<slot>0.7.0_AE_CloudOps~A</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<proof_genre>DEPLOY</proof_genre>
<worker_class>worker</worker_class>
