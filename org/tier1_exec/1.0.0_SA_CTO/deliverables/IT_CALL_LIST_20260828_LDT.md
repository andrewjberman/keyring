# IT (LDT) call list -- 2026-08-28

**Assembled at `1.0.0_SA_CTO~D` on Andrew's word** ("I'll call them up now, show me the three points that
were on that request list" + via 0.0.0_AB_MSTR msg 78699: "send this to CTO~D because they are assembling a
list of stuff to talk to IT about and i want to make sure we're properly wired into the Opal system with
the azure account"). LDT = Little Dog Tech, the MSP holding Global Admin on tenant
`6810043e-d171-4adc-9975-068b35e179da` (opalinvest.com). Opal staff hold no admin roles.

Every value below was READ from the artifact on 2026-08-28 (Azure CLI 2.89.1 as Andrew@opalinvest.com;
`az ad app show`, `az account show`, `az group show`, `az consumption budget list`, `az provider list`),
not copied from a message.

## A. Gateway browser sign-in (BLOCKING today -- `mcp.opalinvest.dev/sprint`)

1. **App registration "M365-MCP-Login"** (`53360468-0a38-4e56-a1ed-3db6914461cd`) -> Authentication -> Web
   -> Redirect URIs. The single entry is `https://mcp.opalinvest.dev/oauth2/idpresponse%60` -- a trailing
   BACKTICK was pasted in with the value. Replace with exactly `https://mcp.opalinvest.dev/oauth2/idpresponse`.
   Nothing else on the app changes. (The ALB builds this callback itself; nothing on the AWS side can add a
   character. The daily MCP path uses App 2's `/callback`, which is why this survived since June.)
   Symptom: `AADSTS50011` redirect-URI mismatch. Record: `infra/aws/ec2/opal-gateway/IT_REQUEST.md` Incident #3.
2. **Add `Andrew@opalinvest.com` as Owner** of BOTH "M365-MCP-Login" and "M365-MCP-Graph" (the apps have
   no owners; `az ad app update` from Andrew's account returns `Insufficient privileges`). Owners can edit
   redirect URIs; ownership grants no tenant role.
3. **Secret rotation date:** both app client secrets were minted June 2026 with 24-month expiry -> expire
   **June 2028**. Get the date on LDT's calendar and ours.

## B. Azure subscription -- make it properly Opal's (Global / Compliance Admin acts)

Measured state: subscription `1e594a38-9247-4744-a33d-eb2b29dd64e6` "Opal Capital", PayAsYouGo, Enabled,
home tenant == Opal tenant, Andrew = Owner; resource group `rg-opal-purview-billing` (eastus; tags
purpose=purview-payg-billing, owner=Andrew, created=2026-08-28); budget `opal-purview-payg-monthly-50`
USD 50/month; providers Microsoft.Purview / Consumption / CostManagement registered. Duplicate
`7a09b6bb-6bc1-473d-912c-9f5a13547ed5` cancelled 2026-08-28.

4. **Purview pay-as-you-go linkage:** Purview portal -> Settings -> Billing -> subscription `1e594a38...`,
   resource group `rg-opal-purview-billing`, region East US. Opal's prerequisites are done; without this
   step OCR scanning (PII detection on inbound PDFs/images for the DLP auto-encryption project) stays off.
5. **Billing ownership:** the billing account behind the subscription is a PERSONAL profile ("Andrew
   Berman"), not an Opal entity. Move billing ownership / invoice contact to AJ (COO/CFO) or an Opal
   billing profile BEFORE OCR charges begin. This is the item that makes the subscription Opal's.
6. **Roles:** Compliance Administrator (or at least Security Reader) for Andrew in Purview so DLP/OME state
   is readable from Opal's side; and a second subscription Owner (AJ) so a single account is not the
   only owner.
7. **Licence tier:** confirm the encrypt action is covered (Azure Information Protection P1 -- included in
   M365 Business Premium / E3 / E5) and whether Teams DLP needs an E5-class add-on. Andrew can read his
   own tier at myaccount.microsoft.com; IT owns the purchase.
8. **Azure Rights Management / Purview Message Encryption activated** on the tenant (usually on by default
   for newer tenants). Discriminator: an OME test message from an Opal mailbox.
9. **Tenant hygiene:** should non-admins be able to create Azure subscriptions? (Andrew could -- that is
   how the duplicate happened.)
10. **DLP design inputs Opal hands IT** (not the reverse): sensitive-info types incl. custom custodian
    account-number patterns; scope; Encrypt-Only vs Do-Not-Forward; override-with-justification; test mode
    first. Plus the exposure inventory: Opal's Graph-based mail automation (gateway read_email/send_email,
    the ticketing distro watcher, report ingestion) goes blind to encrypted inbound mail.

## Also worth a sentence on the call (App 2 consent, from IT_REQUEST.md)

App-2 "M365-MCP-Graph" consent carries only the ReadWrite forms for Files/Calendar/Chat/OneNote (no `.Read`
variants) -- a documented read-gap if a read-only identity ever needs those. Not blocking; note it while the
consent screen is open.

---
Sources: `infra/aws/ec2/opal-gateway/IT_REQUEST.md` (Apps 1+2, incidents 1-3) · MSTR msg 78699 (Azure
measured state, re-verified here) · memory `project_azure_subscription_and_cli_setup_20260828`.
