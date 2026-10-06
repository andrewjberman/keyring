# AMGT_RESAPP task order -- `AMGT-ax-5` -- THE CODE REDEPLOY CARRYING ax-1/ax-3/ax-4, AND THE ROUTE LEG: SLASH-CAPABLE GATEWAY ROUTES FOR THE SECURITY ENDPOINTS

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ax-5</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~A</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; one redeploy and one route change by hand.
comp-iam: RUN by the issuer at the cut -- denominator: 3 build cells (ax-1, ax-3, ax-4), 0 of 3 add an S3 read prefix (ax-1 and ax-3 re-read the same pool objects; ax-4 adds package files only); the route leg adds API Gateway routes to an existing integration and authorizer and touches no IAM.
comp-iam coverage: BLIND to an IAM change outside the plan; the plan STOPs on any IAM resource, and any read path the halves list carries a simulate-principal-policy arm.
comp-adversary: RUN by the issuer at the cut -- on deployed satkY3HX, r74 c53/c55/c56 FAIL; c54 FAILS locally. The gateway's 10 security GET routes are single-segment, so a key with '/' 404s at the gateway while the function answers 200.
EGRESS CLASS, declared: NONE for the act; the build pip-downloads its pinned wheels.
</preflight>

## 1. THE ACT -- `AMGT-ax-5` (round 74, decomposition s.82)

Under ONE NEVER-2 entry and ONE never-widen pair:
1. **Route leg.** In `infra/aws/terraform/harvest/scoped-amgt-api.tf`, add a slash-capable route for the security endpoints of
   `opal-portal-data-proxy-api` (7k3ed8px20), e.g. `GET /api/scoped/amgt/security/{proxy+}` to the same integration and authorizer, so
   a key containing '/' reaches the function (which parses `rawPath` itself). Add routes only; remove none. The plan names exactly
   the route resources added, or it is a STOP.
2. **Code leg** at the build commit the GO names, carrying ax-1, ax-3 and ax-4. `memory_size` stays 1769. Right after it, run
   `round71/checks/leadpanel_cold_warm.py --label after` and read the cold invokes' `AMGT_PHASE` lines.

**Begin only when** the GO names the build commit and both halves are committed.
- Re-read the base CodeSha256 live (`satkY3HXAhzfU7zYZ5fk+EmNHaqIRfj7bBtVlG4XfIY=`).
- Read every live worktree's `.open_deploys/`.
- Any CONTENT-DIFF file not on the halves' list is a STOP; over 262,144,000 B is a STOP.
- Any destroy, IAM or unlisted route change is a STOP.

A failing criterion is the ROLLBACK trigger: the prior artifact version, and the added routes removed by the reverse plan.

**c55 is the PIN:** from this act on, every redeploy of this function runs r74 c55 (CTO ruling 4).

## 2. BOUNDS

1. The act and nothing else. No memory change, no IAM change, no store write, no S3 delete, no vendor call, no push of shared
   branches, no portal promote.

## 3. SURFACES

<paths>
infra/aws/terraform/harvest/scoped-amgt-api.tf
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 3600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ax-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; for c in c53 c55 c56; do PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round74/checks/r74_served.py" --cell $c --where deployed || exit 1; done; echo "exit=$?"</invocation><expect>R74 C53, C55 (C1 and C2) and C56 SERVED: YES on the deployed function and gateway; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ax-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; for c in c48 c49 c50; do PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round73/checks/r73_served.py" --cell $c --where deployed || exit 1; done &amp;&amp; for c in c39 c42 c43 c45; do PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round72/checks/r72_served.py" --cell $c --where deployed || exit 1; done &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round71/checks/r71_latency.py" --where deployed; echo "exit=$?"</invocation><expect>R73 C48-C50, R72 C39/C42/C43/C45 and R71 C38 SERVED: YES on the deployed function (no regression); and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

The instance is genre DEPLOY, with a NAMED rollback and base-vs-new CodeSha256 as the discriminating control, at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/AMGT_RESAPP.TO-AMGT-ax-5.the-code-redeploy-and-route-leg.proof_of_spec.json`.
`proof-of-spec-check` must read VALID on the committed bytes.
Report once:
- the prior and new CodeSha256;
- the CONTENT-DIFF and size;
- the route keys added;
- every criterion's output lines;
- the leadpanel AFTER output and the `AMGT_PHASE` lines.

Stamp any row's `surfaced_at` with `date -u`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** s.82; staged until ax-1/3/4 drain and the pair is signed. List item 4 (slash keys) is this act's route leg; c55 pins it on every later redeploy.

<status>staged</status>
<round>74</round>
<slot>0.7.0_AE_CloudOps~A</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<proof_genre>DEPLOY</proof_genre>
<worker_class>worker</worker_class>
