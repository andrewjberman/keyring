# NFRA_CTLPLN decomposition -- WORKSTREAM ACCESS, round 1: one scoped command grant for dell2 (issuer 2.0.0_SA_COO~C; cut 2026-10-07 ~10:0xZ)

**Status: ISSUED in one issuance** (the issuance commit carries the `fanout:` line). FROZEN at the cut.

**Why a workstream.** The CTO ordered this as "an added cell of NFRA_CTLPLN round 4" (msg 106138;
`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULINGS_FOR_THE_DELLS_20261007_1000Z.md` section 1). Round 4 has its issuance, and the
task-order gate refuses a new order file in an issued round by a limb that reads no override (measured at the KIT cut). The gate's
named form is a second workstream. The scope here is its own: an access grant to ONE Dell user on ONE host, a different act from
round 4's fences and deploy wrappers, with a write surface (one new per-user policy file and its test) that no round-4 cell holds
open: CT-d-5, the only round-4 cell in the same Terraform root, is merged.

**Cut on:** PRD v0.14 @275ba82e5a, ADMITTED (`python .tools/prd-signoff.py status NFRA_CTLPLN` at the cut). Carrier: msg 106138 and the
rulings file above, section 1.

**Rule 24.** Domain: what the dell2 user may send to the YCharts resident host. One cell. Not in this workstream: the portal
dependency tree (the same message's item 2: it joins the KIT workstream's CT-k-2 by amendment, since that order is open); any grant
for dell1 (none asked); any other instance or document.

## Measured at the base (laptop, ~10:0xZ)

1. **The ruling's scope, verbatim:** "The dell2 user gets `ssm:SendCommand` on instance `i-0167fd745ad906a66` alone, with the resident
   command documents alone, plus the read actions that return a command's result. Not the AWS shell-script document, not the export
   render's documents, no other instance." And: "a document that takes a free-text command parameter is a shell on that role and is
   OUT of the grant. The cell's first read is each resident document's parameters."
2. **Where command documents are declared** (native search for `resource "aws_ssm_document"` under `infra/aws/terraform/`): 16 in 9
   files. Under the investor-reporting root: `investor-reporting/ycharts/ssm.tf` (2) and `investor-reporting/export/ssm.tf` (1). The
   instance id occurs in `investor-reporting/ycharts/resident.tf`, `ycharts/generate.tf`, `export/main.tf` and
   `ycharts-pipeline/eventbridge.tf`. Which documents are "the resident command documents" is the cell's first read, not the issuer's.
3. **Names, builder output:** `lib/opal_naming.name('cloudops', None, 'dell2-agent-ssm', 'policy')` -> `cloudops-dell2-agent-ssm-policy`.
4. **The Dell policy today** grants no `ssm:SendCommand` (the create policy holds `ssm:CreateDocument`, `UpdateDocument`,
   `PutParameter` and tag actions; the read statement holds `ssm:DescribeParameters`, `DescribeDocument*`, `GetDocument`,
   `ListTagsForResource`).

## The cell

| cell | what | serves | carrier | placement | risk | chain, slot |
|---|---|---|---|---|---|---|
| `CT-a-1` | the scoped command grant: a per-user policy for the dell2 user allowing `ssm:SendCommand` on the one resident instance with only the resident documents whose text is fixed and take no free-text command, plus the reads that return a command's result; an explicit Deny for that user on the AWS shell-script documents; first, the read of every candidate document's parameters | FWD-10 | msg 106138, rulings 10:00Z section 1 | laptop (IAM apply by the issuer's route under its pair) | WORLD | A, `~14` |

No edge. One chain. `fanout: 1 of 1 chains, cap 8`.

## Write set

`infra/aws/terraform/nfra-ctlpln-identity/` -- a new `dell2_ssm_policy.json`, `iam.tf` (one policy and one user attachment), a new
`tests/derive_ssm_documents.py`, `tests/simulate_policy.py`, `tests/check_identity.py`. Its deliverables folder and the investigation
file. `dell_deploy_policy.json`, `dell_create_policy.json` and `dell_respol_policy.json` are NOT in the set.

## The issuer's acts after the drain

1. The half request to the CTO carries the document list the cell derived (its ask: "send me the half request with the document
   list"). The apply is ONE laptop apply of the identity root under one pair covering BOTH unapplied changes in that root -- CT-d-5's
   resource-policy Deny (merged @ee81249009, not applied) and this cell -- so the plan lines of both are stated together.
2. The exercised read, from dell2 by the fabric managers' route: one resident document sent to the instance and its result read
   back; one send of the AWS shell-script document refused.
