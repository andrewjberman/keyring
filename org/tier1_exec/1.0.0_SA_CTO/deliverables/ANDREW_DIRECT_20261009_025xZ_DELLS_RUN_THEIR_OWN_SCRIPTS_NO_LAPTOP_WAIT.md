# ANDREW_DIRECT 2026-10-09 ~02:5xZ -- the Dells run their own scripts; they never wait on the laptop for it

**Channel:** laptop terminal, to 1.0.0_SA_CTO. **Recorded by:** 1.0.0_SA_CTO, same turn. He pasted another seat's exchange with him
about dell2 waiting on the laptop (the F1 shell window, and two NFRA_TRNSPT transcript jobs routed to the laptop's CloudOps), in which he
said: "they should have the ability to run thoise scripts, its on the AWS closed-end environment right? what is the problem with that?"

## Andrew's words, verbatim

> "We need to fix the below, the DELLS should not be waiting on us for this function, let's adjust their permissions accordingly"

## The CTO's ruling (this seat's own "standing rule" is withdrawn)

The per-ledger F1 shell window and dell2's standing `DenyShellDocuments` on `AWS-RunShellScript` were this seat's rule (msgs 106138,
107120; step D2 half). On his word they are withdrawn. **Measured** (`infra/aws/terraform/nfra-ctlpln-identity/`, box/laptop HEAD): the
group Allow `cloudops-dell-agent-ssm-send-policy` (`iam.tf:231`, `modules/routes_policy/main.tf:117`), attached to the `dell_agents` group,
already grants both Dells `ssm:SendCommand` with `AWS-RunShellScript` on the privileged hosts of the routes. dell1 has had that since step D2.
The only thing refusing dell2 is its own per-user `DenyShellDocuments` (`dell2_ssm_policy.json`). So the change is **parity: dell2 gets
what dell1 has, plus its own resident host**.

## The change (AMENDMENT to NFRA_CTLPLN.TO-CT-a-1, cut and applied by 2.0.0_SA_COO~C / 0.7.0_AE_CloudOps)

1. `dell2_ssm_policy.json`: `arn:aws:ssm:*::document/AWS-RunShellScript` leaves `DenyShellDocuments`; the shell-script document joins
   `SendResidentDocumentsToResidentHost`, so dell2 may run it on `i-0167fd745ad906a66` (the F1/resident host) standing. Every other
   shell and session document (`AWS-RunPowerShellScript`, `AWS-RunRemoteScript`, `AWS-StartInteractiveCommand`, `AWS-StartSSHSession`,
   port forwarding, `irpt-export-render-run`) and `ssm:StartSession` on the shell-script document stay denied: they were not asked for.
2. The window variable `open_dell2_f1_shell_window` and its module output are retired, so no later apply re-closes the access; the
   generator (`tests/derive_ssm_documents.py`) and the checks (`tests/check_identity.py`, `tests/simulate_policy.py`) move with it.
3. **The transcript jobs:** dell2 runs NFRA_TRNSPT's jobs on `s3://opal-data-transcripts` through its own `0.7.0_AE_CloudOps~DELL2`. The cell
   measures dell2's write on the prefixes those jobs write (a simulation, positive control beside it). If refused, the same amendment
   grants exactly those prefixes. The two queued jobs go back to dell2.

## Blast radius (the CTO half), in plain words

A dell2 seat can run any shell command on the resident host and on the privileged hosts of the routes, as dell1 already can. That command
runs with the host's role, so it can change a live service or read what that host can read, outside Terraform. What keeps a trail:
every send is reported after the fact by bus (command id, host, purpose), as the step D2 half's condition 2 already says; a send that
writes a firm data bucket or the state bucket stays under the step-C before-rule. **Both branches:** A, the plan reads `0/1/0` on
`aws_iam_policy.dell2_ssm` (plus any transcript grant the measurement needs, named) -> apply. B, anything else -> apply nothing, report.
**Rollback:** re-apply the policy file at the amendment's parent commit.

## Supersedes

The step D2 half's per-ledger window and tonight's standing-window addendum (@5c2d9da8b2) are superseded once the amendment applies.
The window open now (TO-APPLY-25, st27, opened 02:37:46Z) stays open until then; the amendment's apply replaces it, never re-closes it.

**SIGNED (CTO half)** -- `1.0.0_SA_CTO`

## Addendum ~03:4xZ -- the transcripts key (row NFRA_CTLPLN-W14-S44, 2.0.0_SA_COO~C msg 107694)

AMENDMENT 24 merged @7dfcfb686a; TO-APPLY-26 (0/1/0 on `dell2_ssm`) GO'd. Measured by the issuer: dell2's `s3:PutObject` is already allowed on
every prefix the two transcript jobs write, but the transcripts KMS key grants the Dell users only `kms:Decrypt` and `kms:DescribeKey`, so a
real write fails at the key. **RULED (b): dell2 only, `kms:GenerateDataKey` on the transcripts key** (AMENDMENT 25), because NFRA_TRNSPT is
placed on dell2, and this is exactly the "same amendment grants exactly those" case above. dell1 is not asked. Plain words: dell2 can write
encrypted transcript files; it could already read them. CTa1-AC5's write-refused control moves for dell2 alone, and its expected count is
re-stated in the amendment. **SIGNED (addendum)** -- `1.0.0_SA_CTO`

