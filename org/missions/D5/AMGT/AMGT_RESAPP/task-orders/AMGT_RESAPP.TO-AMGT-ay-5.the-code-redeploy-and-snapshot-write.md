# AMGT_RESAPP task order -- `AMGT-ay-5` -- THE CODE REDEPLOY CARRYING ay-1..ay-4, AND THE FIRST /freshness SNAPSHOT WRITE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ay-5</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~A</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; one redeploy and one snapshot write by hand.
comp-iam: RUN by the issuer at the cut -- denominator: 4 build cells; ay-2 adds ONE new key (the snapshot), read and written by the function. The pair lists it with a simulate-principal-policy arm, and a grant leg if the role lacks it. ay-1, ay-3 and ay-4 add no read path.
comp-iam coverage: BLIND to an IAM change outside the plan; the plan STOPs on any IAM resource the pair does not list.
comp-adversary: RUN by the issuer at the cut -- on deployed 0MZWPl7n, r75 c57, c58 and c61 FAIL; c59 and c60 FAIL locally.
EGRESS CLASS, declared: NONE for the act; the build pip-downloads its pinned wheels.
</preflight>

## 1. THE ACT -- `AMGT-ay-5` (round 75, decomposition s.83)

Under ONE NEVER-2 entry and ONE never-widen pair:
1. **Code leg** at the build commit the GO names, carrying ay-1..ay-4. `memory_size` stays 1769. The CONTENT-DIFF the pair lists is
   measured at that commit's CONTENT. A file not on the list is a STOP. Then run `round71/checks/leadpanel_cold_warm.py --label
   after` and read the cold invokes' `AMGT_PHASE` lines.
2. **Grant leg,** only if the pair names one: the function's read and write of the snapshot key.
3. **Snapshot write leg:** the first snapshot, written by the refresh step's own writer, at the NEW key the pair names (absent at
   signing). **Rollback:** a re-put of a computed view, or the route's fallback. Never an S3 delete.

**Begin only when** the GO names the build commit and both halves are committed. Read every live worktree's `.open_deploys/`. Grade
the plan UNTARGETED.

A failing criterion is the ROLLBACK trigger.

**Pins:** r74 c55 (the slash keys) runs on this redeploy.

## 2. BOUNDS

1. The act and nothing else. No memory change, no unlisted IAM change, no S3 delete, no vendor or SEC call, no push of shared
   branches, no portal promote.

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
  <criterion id="AC1" cell_refs="AMGT-ay-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; for c in c57 c58 c59 c61; do PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round75/checks/r75_served.py" --cell $c --where deployed || exit 1; done; echo "exit=$?"</invocation><expect>R75 C57, C58, C59 (C1-C3) and C61 SERVED: YES on the deployed function; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ay-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; for c in c53 c55 c56; do PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round74/checks/r74_served.py" --cell $c --where deployed || exit 1; done &amp;&amp; for c in c48 c49 c50; do PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round73/checks/r73_served.py" --cell $c --where deployed || exit 1; done &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round71/checks/r71_latency.py" --where deployed; echo "exit=$?"</invocation><expect>R74 C53/C55/C56, R73 C48-C50 and R71 C38 SERVED: YES on the deployed function (no regression); and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

The instance is genre DEPLOY, with a NAMED rollback and base-vs-new CodeSha256 as the discriminating control, at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/AMGT_RESAPP.TO-AMGT-ay-5.the-code-redeploy-and-snapshot-write.proof_of_spec.json`.
`proof-of-spec-check` must read VALID on the committed bytes.
Report once:
- the prior and new CodeSha256;
- the CONTENT-DIFF and size;
- the snapshot object written and its ETag;
- every criterion's output lines;
- the leadpanel AFTER output and the `AMGT_PHASE` lines.

Stamp any row's `surfaced_at` with `date -u`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** s.83; staged until ay-1..ay-4 drain and the pair is signed.

<status>staged</status>
<round>75</round>
<slot>0.7.0_AE_CloudOps~A</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<proof_genre>DEPLOY</proof_genre>
<worker_class>worker</worker_class>
