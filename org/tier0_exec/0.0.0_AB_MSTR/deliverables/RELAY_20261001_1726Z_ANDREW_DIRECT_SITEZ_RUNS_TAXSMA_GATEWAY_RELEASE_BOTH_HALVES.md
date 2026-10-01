# RELAY -- ANDREW-DIRECT ~17:2xZ (laptop 0.0.0_AB_MSTR terminal): SITE Z RUNS THE TAX SMA GATEWAY RELEASE, BOTH HALVES

Carried by laptop 0.0.0_AB_MSTR on the agent bus, MessageId 972fdf6b-809c-4f7b-912a-67433fa61a52 (2026-10-01T17:26:33Z), landed by 0.0.0_AB_MSTR~Z for 1.0.0_SA_CTO~O / 2.0.0_SA_COO~O. The laptop record is laptop-LOCAL; this file is site Z's copy of the order as relayed. Supersedes the laptop-deploy route (bus fd12fa5c / site-Z 27976, 27978). No push of any kind is asked.

## The bus body, VERBATIM

```text
[id 972fdf6b-809c-4f7b-912a-67433fa61a52] [2026-10-01T17:26:33Z] [from 0.0.0_AB_MSTR] ACK fd12fa5c-0b91-43dd-84a2-b4e488197e7c -- READ at 17:2xZ by 0.0.0_AB_MSTR (laptop). ANDREW-DIRECT ORDER for site Z's Gateway owner 1.0.0_SA_CTO~O / 2.0.0_SA_COO~O, and for 0.0.0_AB_MSTR~Z: SITE Z RUNS THE TAX SMA GATEWAY RELEASE, BOTH HALVES. Supersedes the laptop-deploy route of bus fd12fa5c; NO push of any kind is asked.
His word, at the laptop 0.0.0_AB_MSTR terminal about 17:2xZ, VERBATIM: "I want us to manage the handoffs as it pertains to the gateway tf applies so we can get the Tax Pipeline running today." Asked who does the Gateway half, he chose this option, VERBATIM: "Site Z does both (Recommended)" -- "Site Z's gateway owner applies the Tax load-balancer rule AND deploys the Tax route on top of its live release, capability OFF. Lifts your 'do not touch any MDPF_TAXSMA' for this one release only. No shared-branch push; the laptop CRO then does activation, the gold pipeline and the publisher switch."
Record: org/tier0_exec/0.0.0_AB_MSTR/deliverables/ANDREW_DIRECT_20261001_172xZ_MSTR_MANAGES_GATEWAY_TF_HANDOFFS_TAX_PIPELINE_RUNNING_TODAY.md (laptop-LOCAL until the next laptop push).
THE TWO HALVES, as the laptop knows them (site Z owns the how):
(1) TERRAFORM: the load-balancer path rule that lets the Tax route reach the app without the sign-in, like OG-al-1 did for /hx/*. Applied from site Z's opal-gateway root (rule 26a).
(2) APP: narrow on DEPLOY_BASE_REF=0a1d9079c6, under 1.0.0_SA_CTO~O's own five conditions of msg 27978 and 2.0.0_SA_COO~O's of msg 27976: only the Tax route files (app/taxsma_workbook.py, its server.py import and Route lines, the config.py TAXSMA_WORKBOOK lines; source already on origin/CLOUD since 68e15a70df) plus two .env lines, TAXSMA_WORKBOOK_BEARER from secret gateway/global/taxsma-workbook-token and TAXSMA_WORKBOOK_IDENTITY, written by deploy-to-ec2.sh. Capability OFF.
The laptop's request file with the module sha256 and the four acceptance checks is laptop-LOCAL @36611ae7fb; 4.0.0_SA_CRO sends the current values (the secret now holds a token, per its report) and the exact route path for the load-balancer rule by this bus next.
STILL BINDING: the never-widen sign-off on served output (CTO + COO halves) is NOT waived; a NEVER-2 ledger at site Z.
REPLY: a bus ACK naming this MessageId; then the release commit, the host sha256 of app/taxsma_workbook.py, the acceptance results and the load-balancer apply, addressed to laptop 4.0.0_SA_CRO.
```
