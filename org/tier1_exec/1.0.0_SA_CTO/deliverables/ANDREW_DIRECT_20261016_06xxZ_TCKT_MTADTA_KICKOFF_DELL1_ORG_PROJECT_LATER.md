# ANDREW_DIRECT 2026-10-16 ~06:0xZ -- TCKT_MTADTA: refactor the spine brief and kick it off on dell1; the AWS Organization is a separate project later

Channel: the laptop `1.0.0_SA_CTO` terminal. Recorded by 1.0.0_SA_CTO, same turn.

## His words, VERBATIM

> We will have a separate project to set up the organization, for now just set it up in opal-data-trino as described. let's get
> that brief refactored into this tckt center metadata project and kicked off on dell1

## What it settles

1. **Box:** dell1. This answers the open placement in
   `ANDREW_DIRECT_20261016_054xZ_SPINE_BECOMES_TCKT_MTADTA_OPS_EIGHT_DROP_AT_OUTSET_GLOBGRPH_ROLE_ONLY.md` @0092da40fe, item 2.
2. **Project:** the M365 spine brief (`docs/briefs/m365-workflow-activity-spine-brief-20261016.md`) is refactored into the
   Ticket Center metadata project, TCKT_MTADTA, under the TCKT macro. It carries every term of @0092da40fe:
   - Ticket Center analytics purpose;
   - the eight ops accounts;
   - every other account dropped at collection and never stored, which is his acknowledgement of the R9 departure for the R20
     entry;
   - `opal-data-trino`, folder `m365-metadata`: bronze, then silver parquet, then gold analytics tables decided later;
   - readable only by a globgrph-group IAM role, reached by calling a Lambda that holds it.
   NFRA_WFSPINE is superseded by it, not run beside it.
3. **Storage now:** in the existing AWS account, in `opal-data-trino`, "as described". The dedicated AWS Organization and data
   account discussed in session are OUT of this project's scope; they are a separate project to be briefed later. The PRD names
   that project as the planned hardening and claims nothing it does not deliver. Inside one account, root and IAM admins can
   still reach the data (answered in session).
4. **Who acts (the canonical workflow, on dell1):**
   - L1 brief: `4.0.0_SA_CRO~XXX`, the brief's author, refactors it as `--midstream`.
   - L2 endpoint, L3 register (supersede NFRA_WFSPINE; register TCKT_MTADTA) and L4 PRD: `1.0.0_SA_CTO~DELL1`.
   - L4-R: the CVO signs.
   - L5-L6: a dell1 COO lane seated by `0.0.0_AB_MSTR~DELL1`.
   - Every new address and name is `lib/opal_naming` output; a builder refusal becomes a registry row, never a typed name.
