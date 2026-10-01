# ANDREW-DIRECT 2026-10-01 ~02:0xZ -- gateway Terraform isolates to site Z; Tax SMA finishes on the laptop; CRO checkpoints and pauses; reboot

**Channel:** the `0.0.0_AB_MSTR` Claude Code terminal (laptop). **Recorded by:** `0.0.0_AB_MSTR`, same turn.

## Verbatim, in order

Andrew's framing (~01:5xZ):

> what i want to figure out is how to manage this scenario with the terraform applies. im trying to think of who is
> really using the opalgateway. on sitez, they have a LOT of opalgateway work between opal_ai and all the nfra projects,
> oplgtw, mcpindex, and so on. Here however there is MDPF_TAXSMA, but I feel like CRO can drive that to a close shortly,
> there isnt that much to do on there. The only other one I can think of is NFRA_TRNSPT, but i dont know if that is
> really writing or changing resources as much as simply using them. what id prefer is to generally isolate all
> gateway-tf specfic work over to sitez, but really want TAXSMA done because that feels like its such a simple thing we
> should just bang it out and stop fucking around. what do you suggest with all of this in mind?

MSTR's three suggestions (same turn): (1) the gateway Terraform folder (`infra/aws/terraform/opal-gateway`) and gateway
releases are applied from site Z only; laptop seats never plan or apply it; the laptop CTO lands the rule. (2) Tax SMA
keeps being driven on the laptop by `4.0.0_SA_CRO` on the laptop-only roots, with ONE small order to site Z for the
gateway release carrying the workbook route with the Tax capability off. (3) a standing word that an applied
infrastructure commit is pushed right after its ledger closes, without asking.

Andrew's answer (~02:0xZ):

> yeah i agree. you and cro are the only agents left on this device. i think what id like to do is as soon as CRO is
> done with moving whatever they need to move around, or even get to a checkpoint, they need to pause work, because i
> want to reboot this device.

## Scope (relayed, not adjudicated)

- "yeah i agree" answers the three suggestions as written above. Whether item (3) is a standing push authorization for
  both MSTRs is read back to Andrew before either MSTR acts on it; until he confirms, every push still takes his word.
- `4.0.0_SA_CRO`: finish moving its resources or reach a checkpoint, then PAUSE. No apply left half-landed.
- Andrew reboots the laptop after the CRO's checkpoint. `0.0.0_AB_MSTR` and `4.0.0_SA_CRO` are the only seats live.

## Parked items and their owners

- Landing rule (1) in law or doctrine: owner `1.0.0_SA_CTO`; un-parks when the laptop CTO is relaunched.
- The gateway release order for Tax SMA (TX-r-2): owner site Z NFRA_OPLGTW (`1.0.0_SA_CTO~O` / `2.0.0_SA_COO~O`);
  the request file is the CRO's, relayed by `0.0.0_AB_MSTR` over the bus.
- MDPF_TAXSMA-S10 (ARMED): disarms when site Z pushes ac0290cdf7 and the laptop pulls.
- Measurements behind the suggestions (21 days, non-merge commits): gateway Terraform root touched by NFRA_OPLGTW 14,
  NFRA_MCPORTAL 10, ETFS_RIVALS 4, NFRA_MCPMSP 2, NFRA_MCPINDEX 2; MDPF_TAXSMA 0; NFRA_TRNSPT 0. Gateway application
  code: MDPF_TAXSMA 5, NFRA_TRNSPT 0.
