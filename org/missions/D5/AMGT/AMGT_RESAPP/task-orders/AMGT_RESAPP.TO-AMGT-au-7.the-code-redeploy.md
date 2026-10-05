# AMGT_RESAPP task order -- `AMGT-au-7` -- THE CODE REDEPLOY CARRYING au-1, au-3, au-4, au-6, AND THE GOLD MENTION REBUILD au-3 NEEDS

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-au-7</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~A</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; one code-only redeploy and one gold rebuild by hand.
comp-iam: RUN by the issuer at the cut -- the builds declare no write; the halves list every S3 read path the content diff adds, each with a simulate-principal-policy arm reading allowed before the code leg is called LANDED (CTO round-67 ruling 4).
comp-adversary: RUN by the issuer at the cut -- on deployed GS//XHnV, r71_served c34/c35/c36 and r71_latency c38 FAIL (572 objects, 600 items, 42 names, 9 reads).
EGRESS CLASS, declared: NONE for the act; the build pip-downloads its pinned wheels.
</preflight>

## 1. THE ACT -- `AMGT-au-7` (round 71, decomposition s.79)

Under ONE NEVER-2 entry and ONE never-widen pair, redeploy `opal-amgt-scoped-api` at the build commit the GO names, carrying au-1, au-3,
au-4 and au-6, and rebuild the gold mention table with au-3's url column. `memory_size` stays 1769.

**Begin only when** the GO names the build commit, the gold rebuild's command and key list, and both halves are committed. Then:
- **Re-read the base CodeSha256 live.** It is `GS//XHnVd4+bBIg1VU++r1fp9v495pi6jKFat9KbEYE=` (round 70's redeploy), unless another
  project's closed NEVER-2 entry since then records a newer one. Any other value is a STOP.
- **Two projects deploy this function.** Read `org/critical_paths/.open_deploys/` first; if another entry on it is open, wait.
- **Build from a detached checkout at the build commit** with `infra/aws/terraform/harvest/build-and-upload-scoped-amgt.sh`. The
  CONTENT-DIFF runs against the DEPLOYED build; any file not on the halves' list is a STOP. Print the size; over 262,144,000 B is a STOP.
- **For every new S3 read path the halves list,** a `simulate-principal-policy` on the function's role reads `allowed`, or STOP.
- **Any destroy, IAM, route or gateway change in the plan is a STOP.**
- **Gold leg** (after the code leg): the rebuild the GO names, writing ONLY the keys it lists. Measure the BEFORE state of each key.

A failing criterion is the ROLLBACK trigger: the prior artifact version through one code-only `safe-apply`, and the gold keys restored
from their BEFORE versions.

## 2. BOUNDS

1. The act and nothing else. No memory change, no IAM change, no store write outside the GO's gold keys, no S3 delete, no vendor
   call, no push of shared branches, no portal promote.

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
  <criterion id="AC1" cell_refs="AMGT-au-7"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; for c in c34 c36 c35; do PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round71/checks/r71_served.py" --cell $c --where deployed || exit 1; done; echo "exit=$?"</invocation><expect>R71 C34, C36 and C35 SERVED: YES on the deployed function (C35 C1 and C2 PASS); and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-au-7"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round71/checks/r71_latency.py" --where deployed; echo "exit=$?"</invocation><expect>all 9 Lead Panel reads under 2000 ms warm with status [200]; R71 C38 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-au-7"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; for c in c30 c31 c32 c33; do PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round70/checks/r70_served.py" --cell $c --where deployed || exit 1; done &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round69/checks/r69_served.py" --cell c29 --where deployed &amp;&amp; for c in c23 c24 c25 c26; do PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round67/checks/r67_served.py" --cell $c --where deployed || exit 1; done; echo "exit=$?"</invocation><expect>R70 C30-C33, R69 C29 and R67 C23-C26 SERVED: YES on the deployed function (no regression); and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

The instance is genre DEPLOY, with a NAMED rollback and base-vs-new CodeSha256 as the discriminating control. It goes at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/AMGT_RESAPP.TO-AMGT-au-7.the-code-redeploy.proof_of_spec.json`, and
`proof-of-spec-check` must read VALID on the committed bytes.
Report once:
- the prior and new CodeSha256 and the artifact VersionId;
- the CONTENT-DIFF summary and the package size;
- the gold keys written, with BEFORE and AFTER versions;
- every criterion's output lines.

Stamp any row's `surfaced_at` with `date -u`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** s.79; staged until au-1, au-3, au-4 and au-6 drain and the pair is signed. The gold leg is au-3's url column (CTO ruling 5).

<status>staged</status>
<round>71</round>
<slot>0.7.0_AE_CloudOps~A</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<proof_genre>DEPLOY</proof_genre>
<worker_class>worker</worker_class>
