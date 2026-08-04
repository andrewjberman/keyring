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
