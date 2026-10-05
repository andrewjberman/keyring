# AMGT_RESAPP task order -- `AMGT-as-2` -- THE CODE REDEPLOY CARRYING as-1 (THE /ledger DEDUPE AND THE ARTICLE NIT)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-as-2</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~A</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; one code-only redeploy by hand.
comp-iam: RUN by the issuer at the cut -- as-1 declares no new read or write. The halves list every S3 read path the content diff adds, and each one carries a simulate-principal-policy arm reading allowed before the code leg is called LANDED (CTO round-67 ruling 4).
comp-adversary: RUN by the issuer at the cut -- on deployed 6wwEU3Sw, r69_served c29 FAILS (C1 95 repeating filings reasons; C2 "for driver chart").
EGRESS CLASS, declared: NONE for the act; the build pip-downloads its pinned wheels.
</preflight>

## 1. THE ACT -- `AMGT-as-2` (round 69, decomposition s.77)

Under ONE NEVER-2 entry and ONE never-widen pair, redeploy `opal-amgt-scoped-api` at the build commit the GO names, carrying as-1.
Build and upload ONE artifact, then ONE code-only `safe-apply`. `memory_size` stays 1769.

**Begin only when** the GO names the build commit and both halves are committed. Then:
- **Re-read the base CodeSha256 live.** It is the one the halves name, `6wwEU3Sw+zFE66qfpFMXKL07e5QobD35LsRm2GsOZws=` (round 68's ar-3),
  unless another project's closed NEVER-2 entry since then records a newer one. Any other value is a STOP.
- **Two projects deploy this function.** Read `org/critical_paths/.open_deploys/` first. If another entry on this function is open,
  wait for it to close.
- **Build from a detached checkout at the build commit.** The CONTENT-DIFF runs against the DEPLOYED build. Any CHANGED, ADDED or
  REMOVED file not on the halves' list is a STOP.
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
  <criterion id="AC1" cell_refs="AMGT-as-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round69/checks/r69_served.py" --cell c29 --where deployed; echo "exit=$?"</invocation><expect>run from a checkout at the build commit: population 95 names with 0 non-200; C1 and C2 PASS; R69 C29 SERVED: YES on the deployed function; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-as-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; for c in c27 c28; do PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round68/checks/r68_served.py" --cell $c --where deployed || exit 1; done; echo "exit=$?"</invocation><expect>R68 C27 and C28 SERVED: YES on the deployed function (the round-68 repairs hold); and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-as-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; for c in c23 c24 c25 c26; do PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round67/checks/r67_served.py" --cell $c --where deployed || exit 1; done; echo "exit=$?"</invocation><expect>R67 C23, C24, C25 and C26 SERVED: YES on the deployed function (no regression); and exit=0</expect></criterion>
</proof_of_spec>

These are run with them and reported (no regression), and the issuer re-reads them:
- `r64_served.py --cell c9 / c10 (30-day clauses) / c11 / c12 / c13 / c14`, `r65_served.py --cell c17` and
  `r66_served.py --cell c18 / c19 / c22`, all `--where deployed`;
- `r64_served.py --cell c15 --where deployed`, cold, on the day route.

## 5. WHEN YOU ARE DONE

The instance is genre DEPLOY, with a NAMED rollback and base-vs-new CodeSha256 as the discriminating control. It goes at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/AMGT_RESAPP.TO-AMGT-as-2.the-code-redeploy.proof_of_spec.json`, and
`proof-of-spec-check` must read VALID on the committed bytes.
Report once:
- the prior and new CodeSha256 and the artifact VersionId;
- the CONTENT-DIFF summary and the package size;
- every criterion's output lines;
- the regression reads.

Stamp any row's `surfaced_at` with `date -u`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** s.77; staged until as-1 drains and the pair is signed. CTO round-68 ruling 3.

<status>staged</status>
<round>69</round>
<slot>0.7.0_AE_CloudOps~A</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<proof_genre>DEPLOY</proof_genre>
<worker_class>worker</worker_class>
