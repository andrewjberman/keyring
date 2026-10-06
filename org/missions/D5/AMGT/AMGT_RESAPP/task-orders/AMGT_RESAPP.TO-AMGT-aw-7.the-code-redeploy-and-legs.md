# AMGT_RESAPP task order -- `AMGT-aw-7` -- THE CODE REDEPLOY CARRYING aw-1/aw-2/aw-3/aw-5, AND ITS LEGS: ANY GRANT aw-1 NEEDS, THE KEEP-PRIOR POOL WRITE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-aw-7</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~A</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; one redeploy and its hand-run legs.
comp-iam: RUN by the issuer at the cut -- aw-1 reads `raw/bloomberg/<KEY>/.../refdata.json`; every new read path carries a simulate-principal-policy arm reading allowed before the code leg is LANDED.
comp-adversary: RUN by the issuer at the cut -- on deployed 2lUlZomo, r73 c48/c49/c50 FAIL; c51/c52 FAIL locally.
EGRESS CLASS, declared: NONE for the act; the build pip-downloads its pinned wheels.
</preflight>

## 1. THE ACT -- `AMGT-aw-7` (round 73, decomposition s.81)

Under ONE NEVER-2 entry and ONE never-widen pair, redeploy `opal-amgt-scoped-api` at the build commit the GO names, carrying aw-1,
aw-2, aw-3 and aw-5. `memory_size` stays 1769. **The GO names every leg, its keys and its order**: a grant if aw-1's read path needs
one (before the code), the code, then the keep-prior pool universe write (`build_universe --as-of <date> --write-pool`, aw-6's key).

**Begin only when** the GO names the build commit and every leg, and both halves are committed.
- Re-read the base CodeSha256 live (`2lUlZomoyb2ttLBaQTg6l3ysfw2aEjZGD7mInm8J/WQ=` unless a newer closed entry records another); any
  other value is a STOP.
- Read every live worktree's `.open_deploys/`.
- Any CONTENT-DIFF file not on the halves' list is a STOP; over 262,144,000 B is a STOP.
- Any destroy, route or gateway change is a STOP.
- Measure the BEFORE state of every key written.

**Right after the code leg,** run `round71/checks/leadpanel_cold_warm.py --label after`, and read the `AMGT_PHASE` lines of the cold
invokes from the function's log tail, into your deliverables.

A failing criterion is the ROLLBACK trigger: the prior artifact version through one code-only `safe-apply`, and each written key
restored from its BEFORE version.

## 2. BOUNDS

1. The act and nothing else. No memory change, no IAM change beyond the GO's grant, no store write outside the GO's keys, no S3
   delete, no vendor or SEC call, no push of shared branches, no portal promote.

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
  <criterion id="AC1" cell_refs="AMGT-aw-7"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; for c in c48 c49 c50; do PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round73/checks/r73_served.py" --cell $c --where deployed || exit 1; done; echo "exit=$?"</invocation><expect>R73 C48, C49 and C50 SERVED: YES on the deployed function; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-aw-7"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round73/checks/r73_served.py" --cell c52 --where local; echo "exit=$?"</invocation><expect>after the pool write leg the dry-run against the new pool still reads C1 and C2 PASS (0 regressions); R73 C52 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-aw-7"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; for c in c39 c41 c42 c43 c44 c45; do PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round72/checks/r72_served.py" --cell $c --where deployed || exit 1; done &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round71/checks/r71_latency.py" --where deployed; echo "exit=$?"</invocation><expect>R72 C39-C45 and R71 C38 SERVED: YES on the deployed function (no regression); and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

The instance is genre DEPLOY, with a NAMED rollback and base-vs-new CodeSha256 as the discriminating control, at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/AMGT_RESAPP.TO-AMGT-aw-7.the-code-redeploy-and-legs.proof_of_spec.json`.
`proof-of-spec-check` must read VALID on the committed bytes.
Report once:
- the prior and new CodeSha256 and the VersionId;
- the CONTENT-DIFF and size;
- each leg's keys with BEFORE and AFTER;
- the simulate arms;
- every criterion's output lines;
- the leadpanel AFTER output and the `AMGT_PHASE` lines of the cold invokes.

Stamp any row's `surfaced_at` with `date -u`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** s.81; staged until aw-1/2/3/5/6 drain and the pair is signed. The GO names the legs from the workers' reports.

<status>staged</status>
<round>73</round>
<slot>0.7.0_AE_CloudOps~A</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<proof_genre>DEPLOY</proof_genre>
<worker_class>worker</worker_class>
