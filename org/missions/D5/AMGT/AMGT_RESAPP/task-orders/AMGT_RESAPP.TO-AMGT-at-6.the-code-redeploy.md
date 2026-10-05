# AMGT_RESAPP task order -- `AMGT-at-6` -- THE CODE REDEPLOY CARRYING at-1..at-4 (HEADER FIGURES, EXEC ROSTER, PEER PRICE CURRENCY, DAY-ROUTE ORIGIN)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-at-6</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~A</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; one code-only redeploy by hand.
comp-iam: RUN by the issuer at the cut -- at-1..at-4 declare no write; each reports any new S3 read path it adds. The halves list every S3 read path the content diff adds, and each one carries a simulate-principal-policy arm reading allowed before the code leg is called LANDED (CTO round-67 ruling 4).
comp-adversary: RUN by the issuer at the cut -- on deployed OcKZF34X, r70_served c30-c33 FAIL (43 headers, 84 rosters, 676 peer members, 8 day rows).
EGRESS CLASS, declared: NONE for the act; the build pip-downloads its pinned wheels.
</preflight>

## 1. THE ACT -- `AMGT-at-6` (round 70, decomposition s.78)

Under ONE NEVER-2 entry and ONE never-widen pair, redeploy `opal-amgt-scoped-api` at the build commit the GO names, carrying at-1..at-4.
Build and upload ONE artifact, then ONE code-only `safe-apply`. `memory_size` stays 1769.

**Begin only when** the GO names the build commit and both halves are committed. Then:
- **Re-read the base CodeSha256 live.** It is the one the halves name, `OcKZF34X9liuVKg9ZnpaqBcbSxwcDl6JlW+PlxWyF4k=` (round 69's redeploy),
  unless another project's closed NEVER-2 entry since then records a newer one. Any other value is a STOP.
- **Two projects deploy this function.** Read `org/critical_paths/.open_deploys/` first. If another entry on this function is open,
  wait for it to close.
- **Build from a detached checkout at the build commit.** The CONTENT-DIFF runs against the DEPLOYED build. Any CHANGED, ADDED or
  REMOVED file not on the halves' list is a STOP. The list may include HARVST's shared `store.py` (CTO msg 29511); the halves name
  it if so.
- **For every new S3 read path the halves list,** a `simulate-principal-policy` on the function's role must read `allowed`. If one
  does not, it is a STOP.
- **Any destroy, IAM, route or gateway change in the plan is a STOP.** Print the build's size; a build over 262,144,000 B is a STOP.

A failing criterion is the ROLLBACK trigger: the prior artifact version through one code-only `safe-apply`.

## 2. BOUNDS

1. The act and nothing else. No memory change, no IAM change, no store write, no S3 delete, no vendor call, no push of shared
   branches, no portal promote.

## 3. SURFACES

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 2400)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-at-6"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; for c in c30 c31; do PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round70/checks/r70_served.py" --cell $c --where deployed || exit 1; done; echo "exit=$?"</invocation><expect>R70 C30 and C31 SERVED: YES on the deployed function (95 names, 0 failing); and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-at-6"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; for c in c32 c33; do PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round70/checks/r70_served.py" --cell $c --where deployed || exit 1; done; echo "exit=$?"</invocation><expect>R70 C32 and C33 SERVED: YES on the deployed function; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-at-6"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round69/checks/r69_served.py" --cell c29 --where deployed &amp;&amp; for c in c27 c28; do PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round68/checks/r68_served.py" --cell $c --where deployed || exit 1; done &amp;&amp; for c in c23 c24 c25 c26; do PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round67/checks/r67_served.py" --cell $c --where deployed || exit 1; done; echo "exit=$?"</invocation><expect>R69 C29, R68 C27/C28 and R67 C23-C26 SERVED: YES on the deployed function (no regression); and exit=0</expect></criterion>
</proof_of_spec>

These are run with them and reported (no regression), and the issuer re-reads them:
- `r64_served.py --cell c9 / c10 (30-day clauses) / c11 / c12 / c13 / c14`, `r65_served.py --cell c17` and
  `r66_served.py --cell c18 / c19 / c22`, all `--where deployed`;
- `r64_served.py --cell c15 --where deployed`, cold, on the day route.

## 5. WHEN YOU ARE DONE

The instance is genre DEPLOY, with a NAMED rollback and base-vs-new CodeSha256 as the discriminating control. It goes at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/AMGT_RESAPP.TO-AMGT-at-6.the-code-redeploy.proof_of_spec.json`, and
`proof-of-spec-check` must read VALID on the committed bytes.
Report once:
- the prior and new CodeSha256 and the artifact VersionId;
- the CONTENT-DIFF summary and the package size;
- every criterion's output lines;
- the regression reads.

Stamp any row's `surfaced_at` with `date -u`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** s.78; staged until at-1..at-4 drain and the pair is signed. CTO round-69 ruling 3; CTO msg 29511 (store.py may ride).

<status>staged</status>
<round>70</round>
<slot>0.7.0_AE_CloudOps~A</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<proof_genre>DEPLOY</proof_genre>
<worker_class>worker</worker_class>
