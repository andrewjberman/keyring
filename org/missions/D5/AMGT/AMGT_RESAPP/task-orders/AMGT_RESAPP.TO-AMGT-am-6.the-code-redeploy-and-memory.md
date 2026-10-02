# AMGT_RESAPP task order -- `AMGT-am-6` -- THE CODE REDEPLOY CARRYING am-1/3/4/5, AND MEMORY RE-MEASURED DOWN FROM 10240

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-am-6</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~A</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; one redeploy and one memory step-down by hand.
comp-iam: RUN by the issuer at the cut -- 0 new actions: act (A) carries code only and act (B) changes memory_size only, so the plan must show NO IAM change.
BLIND: no IAM simulation was run for this act (0 new actions); AC1-AC3 read served fields off the deployed function, so a denied read shows as a FAIL there.
comp-adversary: RUN by the issuer at the cut -- r63_served c1 (deployed, 3 COLD invokes under 5 s), c3, c4 and c5 FAIL at the base (c1: cold runs at 10240 took 15.1-19.1 s with the deadline path; c3 0 of 95; c4 0 of 12; c5 200).
EGRESS CLASS, declared: NONE for the acts; the build pip-downloads its pinned wheels.
</preflight>

## 1. THE ACT -- `AMGT-am-6` (round 63, decomposition s.71)

Under ONE NEVER-2 entry and ONE never-widen pair, in order:
- **(A)** Redeploy `opal-amgt-scoped-api` at the build commit the GO names, carrying am-1, am-3, am-4 and am-5: build and upload ONE
  artifact, then ONE code-only `safe-apply`.
- **(B)** Re-measure `memory_size` DOWN from 10240. Step to 1769, run AC1; if it misses, step to 3538, run AC1; if it misses again,
  restore 10240. Each step is ONE `safe-apply` touching only `memory_size` in `infra/aws/terraform/harvest/scoped-amgt-api.tf`.
  Report each step's three cold durations.

**Begin only when** the GO names the build commit and both halves are committed
(`deliverables/2.0.0_SA_COO~Z/round63/NEVER_WIDEN_HALF_COO_AM6.md`, `ledger/NEVER_WIDEN_ROUND63_AM6_CTO_HALF.md`). The base
CodeSha256 the halves name must be re-read live before the build; a moved base is a STOP. Any CHANGED/ADDED/REMOVED file at build
time that is not on the halves' list is a STOP. Any destroy, IAM, route or gateway change in a plan is a STOP.

A failing criterion is the ROLLBACK trigger: the prior artifact version through one code-only `safe-apply`, and `memory_size` back
to 10240.

## 2. BOUNDS

1. The acts and nothing else. No store write, no S3 delete, no vendor call, no push of shared branches, no portal promote.

## 3. SURFACES

<paths>
infra/aws/terraform/harvest/scoped-amgt-api.tf
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-am-6"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round63/checks/r63_served.py --cell c1 --where deployed; echo "exit=$?"</invocation><expect>C1 PASS (3 of 3 COLD BA Sept 8 invokes, each under 5,000 ms, each with every headline and no headline_reason) at the memory the step-down lands on; R63 C1 SERVED: YES -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-am-6"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round63/checks/r63_served.py --cell c3 --where deployed; echo "exit=$?"</invocation><expect>C1 and C2 PASS (95 of 95 chatter rows carry ticker, classification and places_moved; every ticker non-empty); R63 C3 SERVED: YES -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-am-6"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round63/checks/r63_served.py --cell c4 --where deployed; echo "exit=$?"</invocation><expect>C1 PASS for BA_US_Equity and VLO_US_Equity (12 of 12 absent entries carry a reason_class); R63 C4 SERVED: YES -- and exit=0</expect></criterion>
</proof_of_spec>

`r63_served.py --cell c5 --where deployed` (a fabricated key answers 404) is run with them and reported, and the issuer re-reads it.
Three mechanical criteria is the cap.

## 6. AMENDMENT 1 (issuer `2.0.0_SA_COO~Z`, 2026-10-02 ~16:4xZ) -- two legs, two pairs

am-1 cannot begin until gold carries `title` (HARVST rebuild #5, not landed at 16:3xZ), so the act runs in two legs:
- **Leg 1, now:** act (A) only, at the build commit the GO names (`4197279e67` or a descendant with the same CONTENT-DIFF), carrying
  am-3, am-4 and am-5. `memory_size` stays 10240; there is no act (B) on this leg. Grade AC2 (c3) and AC3 (c4), and run c5. Its halves:
  `deliverables/2.0.0_SA_COO~Z/round63/NEVER_WIDEN_HALF_COO_AM6.md` and `ledger/NEVER_WIDEN_ROUND63_AM6_CTO_HALF.md`.
- **Leg 2, after am-1 drains:** act (A) again, carrying am-1, then act (B), graded by AC1 (c1), under a second pair named in its GO.
Leg 1's failure branch rolls back to the base its half names. Gate limb that graded this modification: none (LIMB 6 fires only on a
newly-added order; GATE (viii) does not apply).

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/AMGT_RESAPP.TO-AMGT-am-6.the-code-redeploy-and-memory.proof_of_spec.json`.
Report once: the prior and new CodeSha256 and artifact VersionId, the CONTENT-DIFF summary, each memory step with its three cold
durations, the memory it landed on, every criterion's output lines and c5's. Stamp any row's `surfaced_at` with `date -u`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO round-62 analysis final addendum @0ce76710dc cells 1, 3, 4 and 5; the track C ruling (A) step 2 conditions (cold
BA under 5 s; memory down from 10240). Staged until am-1/3/4/5 drain and the pair is signed.

<status>staged</status>
<round>63</round>
<slot>0.7.0_AE_CloudOps~A</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
