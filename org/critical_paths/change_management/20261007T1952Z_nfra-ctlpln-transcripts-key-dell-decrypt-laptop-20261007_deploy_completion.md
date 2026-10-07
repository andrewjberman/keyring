# Deploy Completion Record
**Date opened:** 2026-10-07T19:52:46.040157+00:00
**Status:** OPEN
**Deploy:** NFRA_CTLPLN TO-APPLY-9: the transcripts KMS key admits the two Dell agent users to kms:Decrypt and kms:DescribeKey -- ONE targeted apply of ONE key policy, from a scratch TF_DATA_DIR
**Authored by:** 0.7.0_AE_CloudOps~E
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| A1 | activation | aws_kms_key.transcripts (targeted, scratch TF_DATA_DIR, lock taken) | the targeted plan shape of branch A read immediately before, the apply result, and the proof the root own .terraform is byte-unchanged |  | OPEN |
| V1 | verify | live key policy == saved prior + exactly the one statement | parsed comparison with a planted-mutant negative control; the two prior statements byte-identical |  | OPEN |
| V2 | verify | the cell check arms against the LIVE policy, BOTH readings printed | dell_decrypt=2/2 and dell_write_refused=10/10 under the KMS rule, with the raw simulator reading printed beside it |  | OPEN |
| V3 | verify | targeted re-plan of aws_kms_key.transcripts | no changes, exit 0 |  | OPEN |
| V4 | verify | the UNTARGETED plan counts, applied NOTHING | 9 to add and 3 to change after (4 before, of which exactly one was the key), filed as a row for NFRA_TRNSPT per CTO condition 8 |  | OPEN |
| V5 | verify | COO condition 6 and the backend discipline | both Dell managers acked the notice by MessageId before the apply; init took the backend main.tf declares from a scratch data dir with no migrate or reconfigure |  | OPEN |

## Log

- 20261007T195246Z OPENED by 0.7.0_AE_CloudOps~E with 6 leg(s)

---

## BOX

**THE LAPTOP.** Executor `0.7.0_AE_CloudOps~E`, seated by `2.0.0_SA_COO~C` under
`NFRA_CTLPLN.TO-APPLY-9.transcripts-key-dell-decrypt-apply-laptop` @`70eeb0005b` (GO msg 106508, acked READ). Applying
identity `arn:aws:iam::313476888478:user/Andrew_Berman`. Root `infra/aws/terraform/transcripts/`, resource
`aws_kms_key.transcripts`, key `44a2284f-1e14-4ea1-b6cb-f6121bfde35a`.

## THE WIDENING, STATED AT ITS FULL WIDTH

One statement on one key: `kms:Decrypt` and `kms:DescribeKey` for `cloudops-dell1-agent-user` and
`cloudops-dell2-agent-user`. **Both Dell box users can then read EVERY object in the meeting-transcripts store, the raw
tier included, every meeting and every participant** -- because their own identity policies already allow
`s3:GetObject`, `s3:ListBucket` and `s3:PutObject` on the bucket pattern and the bucket policy has no reader list.
**Today a read fails only at the key.** This act removes the only thing stopping it.

That width is wider than the recommendation Andrew was shown. `4.0.0_SA_CRO`'s card recommended "no for the raw tier,
yes for the wiped tier"; his answer, recorded at
`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261007_161xZ_SIX_OPEN_CALLS_ANSWERED_TICKET_CENTER_AND_TRNSPT_ON_DELL2.md`
@`a3e5396e1e` line 21, is **"5.) Yes Dell boxes can read all of that."** Both halves say plainly that this is wider
than the recommendation and that it is what he answered. The CTO half records that its own 14:13Z ruling (dell2's user
does not read the store) **is reversed by his word, not by that seat**. Neither half signs anything narrower, and
narrowing his word is not this seat's to do either.

**What the Dells do NOT gain:** `kms:Encrypt`, `kms:GenerateDataKey*`, `kms:ReEncrypt*` -- so a put to the bucket
still fails at the key although S3 itself would allow it -- and no key administration (their own policies carry an
`explicitDeny` on `kms:PutKeyPolicy`, measured).

**What stays as it is:** `NamedReadersUseTheKey` (the owner's user: decrypt AND encrypt) and
`RootAdministersTheKeyAndCannotUseIt` are untouched.

## BLAST RADIUS

**One KMS key policy.** It changes what two principals may do with one key and nothing else. No IAM object, no bucket
policy, no S3 object, no served output, no other resource of this root.

| | before | after |
|---|---|---|
| statements on the key policy | 2 | 3 |
| principals admitted to use the key | 1 (`Andrew_Berman`) | 3 (+ the two Dell agent users, decrypt-only) |

## WHY IT MUST BE TARGETED -- this root is not clean

**UNTARGETED, this root plans `9 to add, 4 to change, 0 to destroy`** (measured read-only at 19:4xZ, applying
nothing). The 9 creations and 3 of the 4 changes are **another project's unapplied work**: a pull function
(`aws_lambda_function.pull`) with its role, policy, event rule, event target, log group, permission and a KMS grant,
plus in-place updates to `aws_lambda_function.mail_pull`, `module.ldo_001.aws_lambda_function.handler` and
`module.ldo_001.aws_lambda_function.ingress[0]`. **None of it is covered by either half and an untargeted apply voids
both.** Exactly ONE of the four changes is this act's -- which is why the order predicts `9 to add, 3 to change`
afterwards: that number is derived, not guessed.

**THE BACKEND RECORD.** In the shared tree `terraform init` fails "Backend configuration changed", and this root is
another project's and may be mid-migration. **No `init -reconfigure` and no `init -migrate-state` was run and the
root's own `.terraform` was not written.** Instead `TF_DATA_DIR` was set to a scratch directory **outside every git
tree** (proven: `git rev-parse --show-toplevel` there returns `fatal: not a git repository`), and `init` there reported
`Successfully configured the backend "s3"!` with **no migrate prompt and no reconfigure prompt**.

**A PRECISION THE HALVES DO NOT CARRY:** the root's own `.terraform/terraform.tfstate` records
`bucket=opal-313476888478-terraform-state key=transcripts/tfstate region=us-east-1`, which **matches `main.tf`'s
backend block on all three fields**. So the "Backend configuration changed" refusal is NOT a bucket, key or region
mismatch; it is some other field of the record. The stale record is not repaired under either half and was not
touched; this is recorded as a row for the root's owner per CTO condition 8, not acted on.

## ROLLBACK -- named, with the empty-list trap called out

**The saved live key policy IS the rollback reference**, saved before the apply:

| | |
|---|---|
| path | `org/tier2_senior/0.7.0_AE_CloudOps~E/deliverables/PRIOR9_key_policy_transcripts_20261007.json` |
| bytes | 770 |
| sha256 | `118c5cd7a4afc085b85aeccab8ab02dc9fb9c5d464e4dc482e78986ffb0fac17` |
| content | 2 statements; `DellAgentUsersDecryptOnly` **absent** |

**PRIMARY ROUTE:** revert the statement (commit `74320c91b2`'s edit to `main.tf`) and run the same targeted apply.
**SAME-WINDOW FALLBACK:** `kms put-key-policy` with the saved document, whose bytes are the exact string KMS returned.

**DO NOT set `dell_agent_user_names` to an empty list.** Both halves name this: the statement renders
`Principal = { AWS = [for n in var.dell_agent_user_names : ...] }`, so an empty list renders an **empty principal
list, which is a malformed key policy**. The revert removes the statement; it does not empty it.

**TRIGGERS:** the targeted plan departing from branch A; an `init` offering to migrate or reconfigure; the live policy
ceasing to equal saved-plus-one-statement; and **CTO CONDITION 9 -- if the exercised read shows a Dell put
SUCCEEDING, the prior key policy goes back the same window.**

**NOT UNDONE BY ANY ROLLBACK:** content a Dell has already read. Both halves say so in those words.

## PRE-APPLY EVIDENCE IN HAND

- **THE COMMIT GATE PASSES WITH A WORKING CONTROL.** `git diff --stat 5d321bfc0a HEAD -- .../main.tf` prints nothing
  and the file is unmodified in the working tree; blob `c53caabb39b1` at both refs. **The instrument discriminates:**
  the same pathspec across `74320c91b2^..HEAD` prints 15 insertions.
- **THE CELL'S CHECK, run immediately before the plan:** `TRANSCRIPTS-DELL-DECRYPT dell_decrypt=2/2
  dell_write_refused=10/10 reader_unchanged=True unlisted_refused=True statements_added=1 ok=True` -- the order's
  expect exactly.
- **THE SCRATCH INIT** initialised against `bucket=opal-313476888478-terraform-state key=transcripts/tfstate
  region=us-east-1`, matching `main.tf`'s declaration on all three fields.
- **THE ROOT'S OWN `.terraform` IS BYTE-UNCHANGED:** `terraform.tfstate` 1818 B,
  sha256 `13b0ae8497536acf75c68d229041b22397cb43b1edabc1814a466ed328215383` **before and after** the init.
- **THE TARGETED PLAN IS BRANCH A, CLASSIFIED FIELD BY FIELD** -- `Plan: 0 to add, 1 to change, 0 to destroy`, one
  resource block, **11 added lines, 0 removed, 0 changed-value lines** (matching the COO half's own 11/0 measurement):

  | field | plan reads | signed shape | |
  |---|---|---|---|
  | `Sid` | `DellAgentUsersDecryptOnly` | same | OK |
  | `Effect` | `Allow` | same | OK |
  | `Action` | exactly `kms:Decrypt`, `kms:DescribeKey` | same | OK -- no encrypt, no data-key, no re-encrypt |
  | `Principal.AWS` | exactly the two Dell agent users' ARNs | same | OK |
  | `Resource` | `*` | same | OK |

  The plan's `id` is `44a2284f-1e14-4ea1-b6cb-f6121bfde35a`, **the same key independently resolved from
  `alias/opal-data-transcripts`** -- so the resource being changed is the key behind the bucket's alias, cross-checked
  by two routes. `NamedReadersUseTheKey` is printed **unchanged**, its five actions and `Andrew_Berman` intact, and
  `RootAdministersTheKeyAndCannotUseIt` is the `# (1 unchanged element hidden)`.
- **THE TARGET ARGUMENT WAS ECHOED BACK** before use (`[aws_kms_key.transcripts]`) and arrives intact through MSYS.
- **THE PLAN TOOK THE STATE LOCK** (no `-lock=false`), as both halves require. Only the read-only untargeted drift
  read used `-lock=false`.
- **COO CONDITION 6 IS SHOWN, from the primary record** --
  `org/tier0_exec/0.0.0_AB_MSTR/deliverables/DELL_NOTICE_TRANSCRIPTS_KEY_DECRYPT_SENT_20261007_1820Z.md` (2700 B, on
  disk and **UNTRACKED**, so anchored by content and not by a commit pin). Both Dell fabric managers **acked the line
  by MessageId before any apply**: dell2 sent `ac334558` ~18:19Z, **ACK `98cdd415` at 18:26:33Z** (12 DELIVERED / 0
  QUEUED); dell1 sent `c064c3d7` ~18:33Z, **ACK `c0781efc` at 18:38:55Z** (6 DELIVERED / 0 QUEUED / 0 REFUSED).
  **The record's own limit, carried rather than dropped:** those counts are each Dell's broker delivery as its manager
  reports it, **not each seat's own read**. This seat messaged no Dell.
  *Provenance note:* a census of `0.0.0_AB_MSTR`'s tree at ~19:30Z found no such record and this seat asked once, as
  the condition's second route allows; the record's mtime is 19:39:39Z, **nine minutes after that census**, so the
  absence read was correct when made and the record was written in answer to the ask. The SENDS, which are what the
  condition is about, are timestamped 18:19Z and 18:33Z -- before the apply either way.

## NOT EXERCISED, and the limits of this evidence

**This seat reads NO transcript object, lists NO key of the bucket and makes NO decrypt call** -- the order's bounds.
The simulator takes the UNION of identity and resource policies and does **not** model the KMS rule that a
customer-managed key needs its KEY POLICY to permit use, so the check supplies that rule itself and prints **both**
readings; a bare `Resource "*"` is refused by the simulator and is replaced by the key ARN for the call only. Key
GRANTS were not listed, SCPs were not evaluated, and no real decrypt happened. **The exercised read is a Dell's own,
by another route: until it runs the grant is APPLIED, NOT EXERCISED.**
