# AMGT_RESAPP task order -- `AMGT-an-7` -- THE CODE REDEPLOY CARRYING an-1..an-6 (FWD-36/37/38, THE COLD READ, THE REPAIRS)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-an-7</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~A</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; one code-only redeploy by hand.
comp-iam: RUN by the issuer at the cut -- 0 new actions: the act carries code only, so the plan must show NO IAM change.
BLIND: no IAM simulation was run for this act (0 new actions); the criteria read served fields off the deployed function, so a denied read shows as a FAIL there.
comp-adversary: RUN by the issuer at the cut -- r64_served c9-c14 FAIL at the base (local, ~20:4xZ); c15 deployed cold 11.5-12.8 s (round 63).
EGRESS CLASS, declared: NONE for the act; the build pip-downloads its pinned wheels.
</preflight>

## 1. THE ACT -- `AMGT-an-7` (round 64, decomposition s.72)

Under ONE NEVER-2 entry and ONE never-widen pair: redeploy `opal-amgt-scoped-api` at the build commit the GO names, carrying an-1 to
an-6. Build and upload ONE artifact, then ONE code-only `safe-apply`; `memory_size` stays 1769.

**Begin only when** the GO names the build commit and both halves are committed
(`deliverables/2.0.0_SA_COO~Z/round64/NEVER_WIDEN_HALF_COO_AN7.md`, `ledger/NEVER_WIDEN_ROUND64_AN7_CTO_HALF.md`). Re-read the base
CodeSha256 the halves name live before the build; a moved base is a STOP. Any CHANGED/ADDED/REMOVED file at build time that is not on
the halves' list is a STOP. Any destroy, IAM, route or gateway change in a plan is a STOP. The package is at 96.8% of the 262,144,000 B
ceiling: print the build's size, and a build over the ceiling is a STOP.

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
  <criterion id="AC1" cell_refs="AMGT-an-7"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; for c in c9 c10 c11; do PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round64/checks/r64_served.py --cell $c --where deployed || exit 1; done; echo "exit=$?"</invocation><expect>R64 C9, C10 and C11 SERVED: YES on the deployed function -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-an-7"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; for c in c12 c13 c14; do PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round64/checks/r64_served.py --cell $c --where deployed || exit 1; done; echo "exit=$?"</invocation><expect>R64 C12, C13 and C14 SERVED: YES on the deployed function -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-an-7"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round64/checks/r64_served.py --cell c15 --where deployed; echo "exit=$?"</invocation><expect>C1 3 of 3 COLD BA Sept 8 invokes under 5,000 ms with every headline (Init Duration present); C2 AMGT_SEGMENT lines in every log; R64 C15 SERVED: YES -- and exit=0</expect></criterion>
</proof_of_spec>

`r63_served.py --cell c3 / c4 / c5 / c7 / c8 --where deployed` are run with them and reported (no regression), and the issuer re-reads
them. Three mechanical criteria is the cap.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/AMGT_RESAPP.TO-AMGT-an-7.the-code-redeploy.proof_of_spec.json`.
Report once: the prior and new CodeSha256 and artifact VersionId, the CONTENT-DIFF summary and the package size, every criterion's
output lines, and the regression reads. Stamp any row's `surfaced_at` with `date -u`.

## 6. AMENDMENT 1 (issuer `2.0.0_SA_COO~Z`, 2026-10-02 ~22:0xZ) -- the round-63 analysis @8642d76ceb

The redeploy also carries `AMGT-an-8` (the 500 attribution, analysis ruling 3). After the act, run an-8's census script
(`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~216/census_500.py --days 7`) and report its output with its
denominator, beside the criteria. A 500 the census cannot attribute is reported, not alarmed. Gate limb that graded this modification: none (LIMB 6 fires only on a newly-added order; GATE (viii) does not apply, `<placeholders>NONE</placeholders>`).

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** s.72; staged until an-1..an-6 drain and the pair is signed. If c15 misses the 5 s bound again, record it with the
segment timings and route it to the CTO; do not raise memory (the round-63 curve is flat).

<status>staged</status>
<round>64</round>
<slot>0.7.0_AE_CloudOps~A</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
