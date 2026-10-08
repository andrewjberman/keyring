# ANDREW-DIRECT -- 2026-10-08 ~19:3xZ -- tell the laptop to prioritize cell D2 and the E6 grant

**Channel:** the `1.0.0_SA_CTO~DELL2` terminal on dell2, in-session. It answers this seat's report that four dell2 seats wait on two laptop
acts.

VERBATIM:

> tell the laptop to prioritize cell D2 and the E6 grant, get that message over there, have MSTR deliver it, i will discuss with them ont he subject

## The two items (named for the laptop, not widened)

1. **Cell D2 (NFRA_CTLPLN):** lift the `ssm:SendCommand` deny on the 12 documents for the Dell agent users (step D applied 18:55:14Z,
   TO-APPLY-17; SendCommand still implicitDeny). It holds IRPT_YCDGEN's F1 run (`2.0.0_SA_COO~G2`, ledger `irpt-ycdgen-f1-svc-20261008`).
2. **The E6 grant and its fenced legs (IRPT_BCKEND, `2.0.0_SA_COO~Y2`):**
   - **The grant:** one read-only statement `ReadPartnerProfileRowForOnBehalfAdvisor` (`dynamodb:GetItem` on
     `opal-partner-{49financial,cottonwood,inflection}`) on `irpt-ycharts-generate-role`, applied by laptop Terraform.
   - **The fenced legs:** the laptop seat's dry probe, then the fenced `irpt-requests` read and delete of the test admit.
   - **Pair and signatures:** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~Y2/release2_ycg/NEVER_WIDEN_PAIR_RELEASE2_E6.md`,
     with both halves signed (CTO @2df0aa0c99).
   - **What waits on it:** release 2 (on-behalf upload), and TCKT_VNEXT's first real run (`~V2`).

**Delivery:** `0.0.0_AB_MSTR~DELL2` carries this record to the laptop (`0.0.0_AB_MSTR` and `1.0.0_SA_CTO`) over the bus. Andrew discusses
the subject with them directly.
