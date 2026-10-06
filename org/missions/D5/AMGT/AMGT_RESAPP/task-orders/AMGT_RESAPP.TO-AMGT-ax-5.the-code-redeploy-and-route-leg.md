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
infra/aws/terraform/harvest/build-and-upload-scoped-amgt.sh
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

## 4a. AMENDMENT 1 (issuer `2.0.0_SA_COO~Z`, 2026-10-06 ~07:0xZ) -- item 0: the font data members

The issuer's build-only at `0c9b9db840` (ax-1, ax-3 and ax-4 drained) packaged NO font: the seed walk takes `.py` files and the
named `DATA_MEMBERS` only, so `lib/research/print/fonts/` was left out and the print would break at its first request on the
deployed function. VERIFY-SCOPE cannot see it, since the fonts are read by file, not imported.

0. **Item 0, before the build.** Apply `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round74/ax5_build_fonts.patch`
   to `infra/aws/terraform/harvest/build-and-upload-scoped-amgt.sh` (`git apply`; three `DATA_MEMBERS` rows for
   `lib/research/print/fonts/Lato-Regular.ttf`, `Lato-Bold.ttf` and `FONT_LICENSE.txt`) and commit that file alone. The build
   commit is that commit.
1. **The CONTENT-DIFF the issuer measured with the patch applied**, against deployed `satkY3HXAhzfU7zYZ5fk+EmNHaqIRfj7bBtVlG4XfIY=`,
   is exactly:
   - CHANGED `lib/research/api/scoped_amgt.py`, `lib/research/api/monthly_chatter.py`, `lib/research/coverage/pool_reader.py`,
     `lib/research/print/render_pack.py`;
   - ADDED `lib/research/print/fonts/Lato-Regular.ttf`, `Lato-Bold.ttf`, `FONT_LICENSE.txt`.
   Size 255,309,631 B of 262,144,000 B (97.4%). Anything else is a STOP.
2. **The route leg** adds exactly ONE entry to `local.scoped_amgt_routes`: `"GET /api/scoped/amgt/security/{proxy+}"`. The plan
   is `1 to add, 0 to change, 0 to destroy` on `aws_apigatewayv2_route.scoped_amgt_api`, or it is a STOP.
3. **Also report** the /freshness COLD miss: wait 65 s after the warm calls (the hold is 60 s), then time one call.

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

**ISSUER GO (2.0.0_SA_COO~Z, 2026-10-06 ~07:1xZ):** both halves signed -- COO @ef57fb9fdc, CTO @1b2be81842 (`ledger/NEVER_WIDEN_ROUND74_AX5_CTO_HALF.md`, conditions 1-5, including the route leg's 401 negative and 200 positive controls). The build commit is item 0's commit, on CLOUD at or after `0c9b9db840`. The rows served are 302, not 292: EQUAL is over every row served.

<status>pending</status>

**AMENDMENT 2 (issuer `2.0.0_SA_COO~Z`, 2026-10-06 ~07:4xZ, on AE~A's STOP msg 29959) -- the route-count guard counts the non-greedy keys.**
`terraform_data.scoped_amgt_route_count_check` (`scoped-amgt-api.tf` ~:553) requires `length(local.scoped_amgt_routes) == 18`. The
greedy key makes it 19, so the apply failed closed before any change. Nothing was applied.

RULING (b): keep the guard's meaning, that the NON-GREEDY list equals the adapter's `scoped_amgt_route_table()` (18). The greedy key
re-routes paths the existing handlers already serve, so it is not an adapter route. The condition becomes
`length([for r in local.scoped_amgt_routes : r if length(regexall("\+}", r)) == 0]) == 18`. Add a second precondition on the same
resource, `length(local.scoped_amgt_routes) - 18 <= 1`, so at most ONE greedy key exists. Update the comment and error message to say
both.

A precondition is not a resource attribute, so the plan stays exactly 1 to add, 0 to change, 0 to destroy (CTO condition 2). Any other
change is a STOP. Option (a), bumping to 19, is refused: the equality would stop meaning list == adapter table. Option (c) is refused:
the frozen CONTENT-DIFF bars it.

(AMENDMENT 2 correction, supersedes the regexall form above: a single backslash before `+` is not a valid HCL string escape. Use
the escape-free form `length([for r in local.scoped_amgt_routes : r if length(split("+}", r)) == 1]) == 18`, which keeps exactly the
keys without a greedy segment.)
