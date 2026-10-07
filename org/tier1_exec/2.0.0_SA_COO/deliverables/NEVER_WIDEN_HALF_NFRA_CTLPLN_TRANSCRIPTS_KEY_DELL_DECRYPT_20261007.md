# COO never-widen half -- NFRA_CTLPLN: the transcripts key admits the two Dell agent users to DECRYPT (one targeted apply, one key policy)

**Author:** `2.0.0_SA_COO~C`, 2026-10-07 ~18:3xZ. **Read at:** trunk `5d321bfc0a` (the merge of cell CT-a-1 AMENDMENT 3). Root
`infra/aws/terraform/transcripts/`. **Counterpart owed:** a CTO half for this same act. **Authority:** `1.0.0_SA_CTO` msg 106391:
"the transcripts key policy admits the Dell agent users to decrypt. A widening: measure the plan, send one half request", on
Andrew's word as recorded by `4.0.0_SA_CRO`
(`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261007_161xZ_SIX_OPEN_CALLS_ANSWERED_TICKET_CENTER_AND_TRNSPT_ON_DELL2.md`
@a3e5396e1e, item 5, verbatim: "Yes Dell boxes can read all of that."). This seat read that record's item 5 and did not hear
the word itself.

## The act

One `safe-apply` of the root TARGETED at exactly `aws_kms_key.transcripts`, at the laptop.

## The plan, MEASURED -- and why it must be targeted

Targeted at the key, 2026-10-07 ~18:2xZ, read-only, exit 2:

```
  # aws_kms_key.transcripts will be updated in-place
Plan: 0 to add, 1 to change, 0 to destroy.
```

11 added lines, 0 removed: one statement `DellAgentUsersDecryptOnly` with the two Dell users' ARNs.

**UNTARGETED, the same root reads `9 to add, 4 to change, 0 to destroy`:** the key, plus another project's unapplied work
(a pull function with its role, policy, rule, target, log group, permission and a KMS grant; two function updates; two updates
inside the `ldo_001` module). None of that is this cell's, none is covered here, and an untargeted apply would land all of it.

**A second state fact about this root, measured:** in the shared tree `terraform init` fails with "Backend configuration
changed": the root's local `.terraform` directory holds a backend record that differs from the backend block in `main.tf`. This
seat did not reconfigure it (it is another project's root and may be mid-migration); both plans above were made with
`TF_DATA_DIR` set to a scratch directory, which leaves the root's own `.terraform` untouched. The applier needs the same care
or the owner's word on the backend before applying.

**Writers of the property (who may use the key): N = 1 key policy + 3 grants, read.** The key policy (this act changes it) and
three KMS grants declared in the root for the pull role, the mail-pull role and the chat-assist function's role (unchanged; LIVE
grants were not listed).

## Blast radius

One KMS key policy. It changes what two principals may do with one key and nothing else.

**What the two Dell users gain (the widening):** `kms:Decrypt` and `kms:DescribeKey` on the transcripts key. Their own identity
policies ALREADY allow `s3:GetObject`, `s3:ListBucket` and `s3:PutObject` on the transcripts bucket (the estate's bucket
pattern), and the bucket policy has no reader list; today a read fails only at the key. So after this act both Dell box users can
read EVERY object in the transcripts store: the raw tier included, every meeting, every participant. That is what the recorded
word says; `4.0.0_SA_CRO`'s own recommendation had been the wiped tier only, and the record says the answer goes beyond it.

**What they do not gain:** `kms:Encrypt`, `kms:GenerateDataKey`, `kms:ReEncrypt*` (so a write to the bucket still fails at the
key, although S3 itself would allow the put), and no key administration.

**What stays as it is:** the existing reader statement is byte-identical (the owner's user: decrypt AND encrypt).

**Evidence, issuer's own re-run in the worker's tree:** `TRANSCRIPTS-DELL-DECRYPT dell_decrypt=2/2 dell_write_refused=10/10 reader_unchanged=True unlisted_refused=True statements_added=1 ok=True`; proof VALID.
**What that evidence is, exactly:** the policy simulator reads a named principal in a key policy correctly, but it does not
model the KMS rule that the account-root statement only delegates to IAM. Read raw, it shows two administration actions as
allowed for a Dell user on TODAY's policy as well; the check applies the KMS rule itself (a statement naming the user, or the
root statement naming the action AND the user's own policy allowing it) and prints both readings: 10 of 10 under the rule, 6 of
10 raw (row `NFRA_CTLPLN-W14-S6`). A mutant with `kms:Encrypt` added to the new statement fails the check. No decrypt was made.

## Expected outcome, BOTH branches

- **A:** the applier's targeted plan reads exactly one in-place update of `aws_kms_key.transcripts`; the diff is one added
  statement, Sid `DellAgentUsersDecryptOnly`, actions exactly `kms:Decrypt` and `kms:DescribeKey`, principals exactly the two
  Dell agent users; zero removed lines -> apply.
- **B:** any other resource in the plan, any other action or principal in the statement, any removed line, or an `init` that
  asks to migrate or reconfigure state -> apply NOTHING and report.

## Rollback

Revert the statement (the commit `74320c91b2`'s edit to `main.tf`) and the same targeted apply; or, same window, put the saved
prior key policy back with the key's policy API. Do NOT set the variable to an empty list: an empty principal list is a
malformed policy. Content a Dell has already read is not recalled.

## Conditions

1. The targeted plan shape of branch A, read immediately before the apply. NEVER an untargeted apply of this root under this
   half.
2. The live key policy saved before the apply (the rollback reference); a NEVER-2 ledger entry opened and closed.
3. `python infra/aws/terraform/transcripts/tests/check_transcripts_dell_decrypt.py` reads `ok=True` immediately before the plan.
4. Read-back LIVE: the live key policy (`kms get-key-policy`) equals the saved one plus exactly the one statement (parsed, with
   a planted-mutant control); the simulator arms against the LIVE policy, with both readings printed; a re-plan of the one
   target reads no changes.
5. The applier reads NO transcript object, lists NO key in the bucket and makes NO decrypt call. The exercised read is a Dell's
   own, by another route, and is owed after the apply: one object decrypted and read from one Dell; one put from a Dell refused
   at the key. Until it runs the grant is APPLIED, not EXERCISED.
6. Both Dells are told before the apply, in one line, what they may now read and that the raw tier holds meeting content: a
   seat that reads it handles it as the firm's most sensitive text, and prints or saves none of it in a row, a log or a message.

**SIGNED** -- `2.0.0_SA_COO~C`
