# ANDREW-DIRECT 2026-10-01 ~17:2xZ (1:2x PM Eastern) at the 0.0.0_AB_MSTR terminal -- manage the Gateway Terraform handoffs so the Tax pipeline runs today

**Channel:** Andrew typed at the laptop `0.0.0_AB_MSTR` terminal, pasting `4.0.0_SA_CRO`'s report that it stopped short of
the Gateway deploy (the live Gateway runs site Z's 0a1d9079c6, not on the laptop or origin; the Tax route also needs a new
load-balancer path rule in the Gateway's Terraform, which only site Z can plan cleanly). Recorded by `0.0.0_AB_MSTR` the
same turn.

## Verbatim

> "Have you already seen this: [the pasted 4.0.0_SA_CRO report]. I want us to manage the handoffs as it pertains to the
> gateway tf applies so we can get the Tax Pipeline running today."

## What the word gives this seat, read narrowly

- The handoffs between the laptop and site Z for the Gateway Terraform applies that the Tax pipeline needs are this seat's
  to manage, today.
- It names the goal: the Tax pipeline running today.

## His answer to the one question this seat put (same turn, ~17:2xZ)

Question: "Who does the Gateway half of the Tax release? The live Gateway runs site Z's code, and the load-balancer rule
lives in site Z's Terraform." His choice, VERBATIM, the option text he selected:

> "Site Z does both (Recommended)" -- "Site Z's gateway owner applies the Tax load-balancer rule AND deploys the Tax route on
> top of its live release, capability OFF. Lifts your 'do not touch any MDPF_TAXSMA' for this one release only. No
> shared-branch push; the laptop CRO then does activation, the gold pipeline and the publisher switch."

## What follows from it

- Site Z's Gateway owner (`1.0.0_SA_CTO~O` / `2.0.0_SA_COO~O`) runs the Tax Gateway release: the load-balancer rule in
  `opal-gateway` Terraform and the narrow app deploy on top of 0a1d9079c6, capability OFF. Rule 26a holds: the release is
  applied from site Z.
- His 04:00Z word to site Z, "do not touch any MDPF_TAXSMA", is lifted for THIS ONE release only.
- No push to a shared branch. The Tax route source is already on origin/CLOUD (68e15a70df is an ancestor).
- Laptop `4.0.0_SA_CRO` keeps the activation (TX-r-3), the gold pipeline and the publisher switch.

## What this record does NOT decide

- The never-widen sign-off on served output: not waived (CTO + COO halves).
- The portal PROD promote, and the timing question on the first Tax observation: put to Andrew by `4.0.0_SA_CRO`.
