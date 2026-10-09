# NEVER-WIDEN HALF (COO) -- NFRA_CTLPLN: dell1 and dell2 hold identical permissions (AMENDMENT 26 to TO-CT-a-1)

**Signer:** 2.0.0_SA_COO~C. **Date:** 2026-10-09 ~04:0xZ.

**Pair:** the CTO half in
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261009_035xZ_DELL1_DELL2_IDENTICAL_PERMISSIONS_AND_LAYOUT.md` @910951a1e0 (SIGNED),
which was relayed to this seat by 1.0.0_SA_CTO msg 107701.

**Source:** Andrew-direct ~03:5xZ, verbatim in that record: "DELL1 and DELL2 should have the exact same permissions and layout."

## The act

One apply per Terraform root that holds a per-user Dell grant: `infra/aws/terraform/nfra-ctlpln-identity/`, and
`infra/aws/terraform/transcripts/` for the key. The cell's census names every per-user grant. Each one either moves to the
`dell_agents` group or is mirrored to the other user. Known:

- `aws_iam_policy.dell2_ssm`, which carries the resident-host documents and AMENDMENT 24's standing shell document;
- the transcripts key's `kms:GenerateDataKey`, now for both users (this widens AMENDMENT 25, which was dell2 only);
- any other per-user statement the census finds.

Writers: the cell prints the writer count of each property it moves. One writer per property is expected.

## Blast radius

dell1 gains what dell2 has:

- shell scripts and the resident-host documents on `i-0167fd745ad906a66` and on the route hosts;
- writing encrypted transcript objects;
- any other dell2-only grant the census names.

Nothing either user holds today is removed except by mirroring a deny; a deny that reached one user alone reaches both afterwards.
Unchanged:

- the denies on IAM users, access keys, login and MFA;
- the step-C before-rule;
- the after-the-fact reports of every send and IAM change.

## Both branches

- **A:** each plan changes only the policies and attachments the cell named, and the two-user simulation over one census prints
  identical results. Apply.
- **B:** anything else, or any inequality. Apply nothing and report the inequality first.

## Rollback

Re-apply each root at the amendment merge's first parent.

**SIGNED (COO half)** -- `2.0.0_SA_COO~C`
