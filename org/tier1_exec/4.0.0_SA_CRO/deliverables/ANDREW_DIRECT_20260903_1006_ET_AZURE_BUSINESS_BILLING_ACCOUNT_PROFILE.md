# Andrew-direct — Azure business billing account and AJ payment profile

**Author:** `4.0.0_SA_CRO` (Chief Research Officer)  
**Channel:** Andrew direct to the `4.0.0_SA_CRO` Codex terminal  
**Received:** 2026-09-03 10:06 ET  
**Recorded:** 2026-09-03 10:06 ET

## Andrew's words — verbatim and entire

> Finish your startup, what we are going to be working on is the Azure billing issue. I just added aj@opalinvest.com as an owner in the Azure portal. we need to create a new billing profile with his card information and a "business" account rather than an "individual".

## Grounded state at receipt

- Azure CLI identity: `Andrew@opalinvest.com`; tenant `6810043e-d171-4adc-9975-068b35e179da`; subscription `1e594a38-9247-4744-a33d-eb2b29dd64e6` (`Opal Capital`) enabled.
- Billing account `42bd2b5d-9666-563c-3d49-025dfe081418:63786753-3e0c-40f4-86e7-161dbe446070_2019-05-31` reads `agreementType=MicrosoftCustomerAgreement`, `accountType=Individual`, `displayName=Opal Capital LLC`, status `Active`.
- The billing account's only profile is `I6HW-JUCK-BG7-PGB`; its bill-to identity remains Andrew Berman at the prior personal address.
- Billing-role read-back confirms `AJ@opalinvest.com` / principal `a0b6b272-3188-49a5-8fc6-9ea871b61080` now holds Billing account owner (`50000000-aaaa-bbbb-cccc-100000000000`) on the full billing-account scope. This is a Microsoft Billing role, not Azure subscription RBAC; an Azure RBAC query correctly returned no assignment.
- No payment-card data was requested, received, printed, or stored by this seat. Card entry remains inside Microsoft's authenticated payment form.

## Operational reading — surfaced, not substituted for Andrew's words

`Business` / `Individual` is a billing-account property, not a billing-profile property. Microsoft's current Billing Account Update contract permits only the MCA display name and address to be changed; creating another profile under the current account would leave the parent account `Individual`. The supported completion path must therefore establish a new Business billing account first (or obtain Microsoft's billing-support action), then create its billing profile with AJ entering the card inside the portal. Moving the existing subscription's billing ownership is a separate follow-on act and is not silently inferred from this instruction.

