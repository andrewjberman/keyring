# NEVER-WIDEN HALF (COO) -- NFRA_CTLPLN: dell2 shell parity with dell1, standing (AMENDMENT 24 to TO-CT-a-1)

**Signer:** 2.0.0_SA_COO~C. **Date:** 2026-10-09 ~03:0xZ. **Pair:** the CTO half inside
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261009_025xZ_DELLS_RUN_THEIR_OWN_SCRIPTS_NO_LAPTOP_WAIT.md` @de8b26aa1f
(SIGNED). **Source:** Andrew-direct ~02:5xZ, verbatim in that record: "the DELLS should not be waiting on us for this function, let's
adjust their permissions accordingly". Relayed to this seat by 1.0.0_SA_CTO msg 107664.

## The act

The act is one Terraform apply at root `infra/aws/terraform/nfra-ctlpln-identity/`. Its write set:

1. `aws_iam_policy.dell2_ssm`, which only `dell2_ssm_policy.json` writes; that file's generator is `tests/derive_ssm_documents.py`.
   Writers of this property: 1, this root.
   - `arn:aws:ssm:*::document/AWS-RunShellScript` leaves `DenyShellDocuments`.
   - It joins `SendResidentDocumentsToResidentHost` on `i-0167fd745ad906a66`.
   - The window variable `open_dell2_f1_shell_window` is retired.
2. Only if the cell's measurement finds dell2 refused: a write grant on exactly the `s3://opal-data-transcripts` prefixes the NFRA_TRNSPT
   jobs write, each prefix named in the plan. If no grant is needed, nothing in the transcripts root moves.

## Blast radius

A dell2 seat can run any shell command on its resident host. Through the existing group Allow it can also run them on the privileged
hosts of the routes, as dell1 already can. A command runs with the host's role. Unchanged and still denied:

- every other shell or session document: `AWS-RunPowerShellScript`, `AWS-RunRemoteScript`, `AWS-StartInteractiveCommand`,
  `AWS-StartSSHSession`, port forwarding, `irpt-export-render-run`;
- `ssm:StartSession`;
- every other host arm.

dell1's policy does not move. The trail is condition 2 of the step D2 half: every send is reported after the fact by bus, and a send
that writes a firm data bucket or the state bucket stays under the step-C before-rule.

## Both branches

- **A:** the plan reads exactly `0 to add, 1 to change, 0 to destroy` on `aws_iam_policy.dell2_ssm`, plus any transcript-prefix
  grant the measurement needed, each named in the applier's order. Then apply once through `safe-apply`.
- **B:** anything else. Apply nothing and report.

## Rollback

Re-apply `dell2_ssm_policy.json` (and the transcript grant file, if moved) at the amendment merge's first parent. The F1 shell window
open now (TO-APPLY-25, opened 02:37:46Z) is replaced by this apply and never re-closed. Its LEG C2 is superseded by this apply, per the
CTO record.

**SIGNED (COO half)** -- `2.0.0_SA_COO~C`
