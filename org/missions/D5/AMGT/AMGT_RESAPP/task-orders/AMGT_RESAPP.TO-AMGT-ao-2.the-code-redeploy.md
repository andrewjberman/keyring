# AMGT_RESAPP task order -- `AMGT-ao-2` -- THE CODE REDEPLOY CARRYING ao-1 (FWD-38 (b) TITLE CASE)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ao-2</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~A</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; one code-only redeploy by hand.
comp-iam: RUN by the issuer at the cut -- 0 new actions: the act carries code only, so the plan must show NO IAM change.
BLIND: no IAM simulation was run for this act (0 new actions); the criteria read served fields off the deployed function, so a denied read shows as a FAIL there.
comp-adversary: RUN by the issuer at the cut -- r65_served c17 FAILS on deployed KQSA62c3: 60 of 94 price and 61 of 95 chatter names all-caps.
EGRESS CLASS, declared: NONE for the act; the build pip-downloads its pinned wheels.
</preflight>

## 1. THE ACT -- `AMGT-ao-2` (round 65, decomposition s.73)

Under ONE NEVER-2 entry and ONE never-widen pair: redeploy `opal-amgt-scoped-api` at the build commit the GO names, carrying ao-1. Build
and upload ONE artifact, then ONE code-only `safe-apply`; `memory_size` stays 1769.

**Begin only when** the GO names the build commit and both halves are committed
(`deliverables/2.0.0_SA_COO~Z/round65/NEVER_WIDEN_HALF_COO_AO2.md` and the CTO half the GO cites). Re-read the base CodeSha256 the
halves name live before the build; a moved base is a STOP. Any CHANGED/ADDED/REMOVED file at build time that is not on the halves'
list is a STOP. Any destroy, IAM, route or gateway change in a plan is a STOP. The package is at 96.8% of the 262,144,000 B ceiling:
print the build's size, and a build over the ceiling is a STOP.

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
  <criterion id="AC1" cell_refs="AMGT-ao-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round65/checks/r65_served.py --cell c17 --where deployed; echo "exit=$?"</invocation><expect>C1 PASS on both routes (0 all-caps names, acronym-only excepted); C2 PASS on both routes; R65 C17 SERVED: YES on the deployed function; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ao-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round64/checks/r64_served.py --cell c12 --where deployed; echo "exit=$?"</invocation><expect>R64 C12 SERVED: YES on the deployed function (one display name per security, unchanged); and exit=0</expect></criterion>
</proof_of_spec>

`r64_served.py --cell c9 / c10 / c11 / c13 / c14 --where deployed` are run with them and reported (no regression), and the issuer
re-reads them.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/AMGT_RESAPP.TO-AMGT-ao-2.the-code-redeploy.proof_of_spec.json`.
Report once:
- the prior and new CodeSha256 and artifact VersionId
- the CONTENT-DIFF summary and the package size
- every criterion's output lines
- the regression reads

Stamp any row's `surfaced_at` with `date -u`.

## 6. AMENDMENT 1 (issuer `2.0.0_SA_COO~Z`, 2026-10-03 ~19:1xZ) -- THE PIN IS `19cb3df089`

Your STOP (msg 28947) was right. The build commit is now `19cb3df089`, or a descendant whose CONTENT-DIFF equals CHANGED 3:
`scoped_amgt.py`, `publication_gold.py` and `finbert_sentiment.py`. That commit carries ao-1 and COO~H's `fc5a0bf42d` (the
ANDREW-DIRECT ~18:xxZ deletion of the quarantine mechanism). The original pin `9a8cbd2c97` is withdrawn.

Halves:
- COO: `deliverables/2.0.0_SA_COO~Z/round65/NEVER_WIDEN_HALF_COO_AO2.md`, AMENDMENT 1.
- CTO: the re-sign the GO cites.

Criteria are unchanged. Gate limb that graded this modification: none (LIMB 6 fires only on a newly-added order; GATE (viii)
does not apply, `<placeholders>NONE</placeholders>`).

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** s.73; staged until ao-1 drains and the pair is signed. c15 is not re-run as a criterion: ao-1 adds no read.

<status>staged</status>
<round>65</round>
<slot>0.7.0_AE_CloudOps~A</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<proof_genre>DEPLOY</proof_genre>
<worker_class>worker</worker_class>

**ISSUER CLOSE (2.0.0_SA_COO~Z, 2026-10-03 ~20:0xZ):** CLOSED. AE~A `76c5170831` built at pin `19cb3df089` (355 / 352 / 3, 96.8%). CodeSha256 `KQSA62c3` -> `lPTMo20T` (VersionId `5xO0vR9UWlx.XI59G0KNLJyAsjMKOes4`), memory 1769. AC1 c17 + AC2 c12 PASS; c9, c10, c11, c13 and c14 unchanged; NEVER-2 entry opened `4922fbb96f` and closed. Issuer re-read on deployed from a checkout at the pin: c17 YES (0 of 94, 0 of 95; MUFG whole), c12 YES, c9-c14 YES; the 5 cut names are served whole on both routes (`round65/served_names_lPTMo20T.json`). The pin moved once on AE~A's STOP (AMENDMENT 1). Not carried: `c20fd8cc98` (after the pin).

<status>complete</status>
