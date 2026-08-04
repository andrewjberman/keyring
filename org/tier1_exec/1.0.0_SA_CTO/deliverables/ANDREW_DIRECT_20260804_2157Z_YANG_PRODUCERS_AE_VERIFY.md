# ANDREW-DIRECT — yang producer fixes: designated-AE verify/deploy/test (0.2.0_DS occupied on cochange)

**Channel:** Andrew-direct, CTO terminal, 2026-08-04 ~21:57Z (~17:57 ET).
**VERBATIM:** > "also 0.2.0_DS base is very occupied with cochange work, which they took on
> before we realized the scope of the issue with the lambdas. I believe however that they
> already addressed the changes in the code, which means that a designated AE should just check
> their commits, see if its done, and make sure its terraform applied properly/deployed. and
> then run a test"

**Scope as surfaced:** the three-producer LT/ULT batch (positioning / factor-tilts / attribution
label-map fixes, routed to 0.2.0_DS at 212500Z) re-shapes: 0.2.0_DS stays on comp-cochange; a
**designated AE** instead (1) checks 0.2.0_DS's commits for the label-map changes, (2) verdicts
done/not-done per producer, (3) verifies Terraform-applied/deployed state on the live functions,
(4) runs a test — the regen + LT/ULT-rows-present verify per artifact (DE 0.2.0's diagnosis +
S3 measurement = the test criteria; bound predictions per the benchmarks template). If the code
changes are NOT complete, the gap report comes back before anyone writes code — no AE improvises
DS-lane edits.

**Routing:** COO designates the AE seat (recommendation: 0.7.0_AE_CloudOps~B — live, fresh,
light-loaded; base 0.7.0 is mid-swap; ~D is stopped by Andrew's word). Broadcast same turn.

**ADDENDUM ~22:0xZ, VERBATIM (the test's cross-device leg + the strict ordering):**
> "Also, for that test, I would like to try having MSTR send an agentbus message to
> 0.0.0_AB_MSTR~Z on the sitez machine (the terminal machine, not local device) to run
> /terminal-upload. I actually am curious if we have the capacity to do so from this device,
> but we can establish that next. In essence, what needs to happen here is that some 0.7.0_AE
> (of which we have 3 active right now) needs to check on this terraform for the relevant
> lambdas that 0.2.0_DS worked on, make sure the changes are there, get the terraform deployed
> canonically, and then and only then do we have MSTR issue the inter-device command for a
> terminal upload to test the refresh with the new lambdas."

**Ordering as ruled (strict):** (1) a 0.7.0_AE seat verifies the DS commits + TF state and
deploys canonically (full TF law); (2) **THEN AND ONLY THEN** MSTR sends the agentbus message to
`0.0.0_AB_MSTR~Z` (sitez terminal machine) to run `/terminal-upload` — the refresh test against
the new lambdas rides the terminal upload. Contingencies surfaced, not improvised: MSTR base is
currently dark (the staged ask sits in their inbox for return); sitez was reported hung this
morning (SQS is durable — the bus message waits if sitez is still down; the test completes when
both seats are live). The from-this-device capacity question is Andrew's own follow-up, not
tonight's task.
