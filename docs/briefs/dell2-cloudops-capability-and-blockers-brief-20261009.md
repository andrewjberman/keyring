# Brief: what `0.7.0_AE_CloudOps~DELL2` can and cannot do, and what is actually blocking it

**Author:** `0.7.0_AE_CloudOps~DELL2` | **Date:** 2026-10-09 ~05:2xZ | **For:** Andrew-direct ask
**Claim on every number here:** `measured` this session, by the call named beside it. Nothing is inherited.

---

## 1. The short answer

**Deploys are not blocked.** This seat applied three Lambda releases tonight, autonomously, end to end:
`irpt-directory-refresh`, `irpt-ycharts-generate` (release 5b) and `opal-ticket-api` (SA1). Each one
built, uploaded, planned, `safe-apply`-ed, read back by content and closed under a NEVER-2 ledger.

**Two things are blocked, and neither is an approval gate.** Both are AWS permissions that live in
another box's Terraform:

| blocked work | the missing permission | state |
|---|---|---|
| `IRPT_BCKEND.TO-IB-pr-383` legs S1/S2/V1 (the per-firm seeding run) | `ssm:SendCommand` on `i-02448edb624a7a7cf` | laptop AMENDMENT 27 (`@349d6e9d91`) writes the grant; NOT yet applied |
| `NFRA_TRNSPT.TO-RUN-a17` and `b17` | `kms:GenerateDataKey` + `kms:Encrypt` on the transcripts key | key policy grants this identity `Decrypt` + `DescribeKey` only |

**The uncomfortable part, stated plainly: I hold the permissions to fix both myself, and I have not.**
See section 4. That is a decision for you, not a convenience for me.

---

## 2. What this seat CAN do -- demonstrated, not assumed

Each row was exercised tonight; the evidence is the cited commit.

- **Terraform Lambda deploys** via `.tools/safe-apply.sh` from a saved planfile, in three different
  roots (`investor-reporting/directory`, `investor-reporting/ycharts`, `ticket-center`).
  `@627f6fa99e`, `@8f677f9c3c`, `@f28a13d3ed`.
- **Artifact build + upload** to `opal-313476888478-lambda-artifacts`, with the uploaded object read
  back by `head-object` and, where a condition demanded it, downloaded by version id and hashed.
- **Bundle mint** through `.tools/safe-deploy.sh` (12-member investor-reporting bundle), ETag and
  sha256 both confirmed on the object.
- **SSM `AWS-RunShellScript`** to the ycharts resident host `i-0167fd745ad906a66` -- 7 commands tonight.
- **EC2 start** (`i-02448edb624a7a7cf`, `pending <- stopped`).
- **Lambda direct invoke** (the `irpt_import_census` gate), **DynamoDB read**, **Secrets Manager read**
  (token read into memory, never printed or written), **S3 read/write on Opal buckets**,
  **CloudFront-fronted HTTP probes** against `opalinvest.dev`.
- **Commits** under this seat's author line through `.tools/safe-commit.sh`, including surprise-channel
  rows and NEVER-2 ledger records.

**Permission source, measured:** the two policies attached to the *user* carry only `ssm:*` (4 statements)
and `sqs:*` (1 statement). Everything else arrives through group `cloudops-dell-agents-group` and its
**9** attached policies. A reader looking only at the user policies would badly under-read this seat.

---

## 3. What this seat CANNOT do

### 3a. Two live permission refusals (the real blockers)

**`ssm:SendCommand` on the mdpf-daily-runner host.** Re-probed at ~05:1xZ, still:

> `AccessDeniedException ... not authorized to perform: ssm:SendCommand on resource:
> .../instance/i-02448edb624a7a7cf because no identity-based policy allows the ssm:SendCommand action`

There are **two** SendCommand grants and the host is in neither:

- user policy `cloudops-dell2-agent-ssm-policy` v7, Sid `SendResidentDocumentsToResidentHost`:
  **one** instance, `i-0167fd745ad906a66`, plus 3 documents.
- group policy `cloudops-dell-agent-ssm-send-policy` v1, Sid
  `SendCommandDocumentsAndShellToPrivilegedHosts`: **six** instances
  (`i-0090b823a4a0997e3`, `i-00c7568bc510f7423`, `i-01003b035d2988dfb`, `i-0643a5bee8a8feabf`,
  `i-0800437d1dbb0b5cc`, `i-0ed5afded2ebd4ed4`) plus 13 documents.

> **Correction to my own earlier relay.** At 04:45Z I told MSTR and COO~P2 the fix was adding the ARN
> to the *user* policy's `SendResidentDocumentsToResidentHost`. Having now read the group policy, the
> better home is the group's privileged-hosts list -- AMENDMENT 27 grants the host "to both Dells",
> which is a group-shaped change, not a per-user one. The user-policy route would grant dell2 only.

It is an **absent ALLOW, not a DENY**: `AWS-RunShellScript` is already allowed in both statements and
appears in no Deny that reaches this instance. So nothing has to be unwound first.

`cloudops-dell2-agent-ssm-policy`'s `UpdateDate` is **03:52:22Z** -- exactly the AMENDMENT 26 apply.
So that apply did land on this very policy and still omitted the runner host; v7 is its newest version.

**`kms:Encrypt` / `kms:GenerateDataKey` on the transcripts key.** Key policy `default`, 3 statements,
Sid `DellAgentUsersDecryptOnly`, Effect Allow, Action **exactly** `[kms:Decrypt, kms:DescribeKey]` for
both Dell agent users. Re-read at ~05:1xZ, unchanged.

> **Instrument note worth keeping.** `a17` step 1 names `simulate-principal-policy` as its oracle.
> That API evaluates **identity** policies only and cannot see a resource-based key policy, so it is
> structurally uninformative here: it returned `implicitDeny` for `kms:Decrypt`, which this identity
> demonstrably **holds**, and `implicitDeny` for a deliberately nonsensical action name. Its agreement
> with the truth about `Encrypt` was luck. The key-policy read is what proves the refusal.

### 3b. Reserved to a human by law, not by permission

Human confirmation, per CLAUDE.md Agent Autonomy: **stopping EC2**, **S3 object deletes / recursive
deletion**, **destructive git**, dropping tables, anything unrecoverable. One live consequence: I
started `i-02448edb624a7a7cf` to do the seeding and **cannot stop it again**; MSTR has ruled it stays
up until its own 13:30Z fire, and a stop is your call.

### 3c. Out of lane, not out of reach

`NFRA_CTLPLN` (the IAM/control-plane project) is the laptop's. The grants above are its Terraform.

---

## 4. The honest part: I could unblock myself, and chose not to

Measured, separating Allow from Deny statement by statement:

- `cloudops-dell-agent-iam-roles-policy` v1 **ALLOWS**, on resource `*`:
  `iam:CreatePolicy`, **`iam:CreatePolicyVersion`**, **`iam:SetDefaultPolicyVersion`**.
  Its Deny (`DenyIamUsersGroupsKeysAndAccount`) covers `iam:AttachGroupPolicy` and `iam:PutGroupPolicy`
  -- group **attachment**, which I do not need, because `cloudops-dell-agent-ssm-send-policy` is
  *already* attached to my group. A new version plus `SetDefaultPolicyVersion` would take effect.
- `cloudops-dell-agent-respol-allow-policy` v2 **ALLOWS** `kms:PutKeyPolicy` (and `kms:CreateGrant`).

So both blockers are, technically, one API call each from this seat. I did not make either call, for
two reasons I want on the record rather than inferred:

1. **Terraform drift.** Both resources are managed in the laptop's Terraform. A hand-edit diverges live
   state from state-file, and the next apply in that root silently reverts it -- possibly mid-run, which
   is the worst moment to lose a grant.
2. **It is self-granting privilege escalation.** Widening my own identity's reach is exactly the class of
   act that should carry a human's name, not an agent's convenience -- especially when AMENDMENT 27
   already writes this grant and is merely waiting on an apply.

**Your call, and either answer is workable:**

- **(a) Wait for the laptop's apply.** Zero drift. Cost: `383`'s seeding has a Friday-close deadline and
  cottonwood's `OVER_AGE` lands 2026-10-12; `a17`/`b17` hold round 17 open.
- **(b) Tell me to apply the two changes directly.** Both run in minutes. I would create a new version of
  `cloudops-dell-agent-ssm-send-policy` adding the one instance ARN, and `PutKeyPolicy` adding
  `kms:GenerateDataKey` + `kms:Encrypt` to the existing Dell statement -- each under its own ledger, each
  reported to MSTR, and each also sent to the laptop so AMENDMENT 27 and the key-policy change land in
  Terraform rather than staying as live-only drift.

I recommend **(b) with the Terraform follow-up**, because the grant is already written and ratified;
what is missing is only an apply, and the deadline is real.

---

## 5. Queue as it stands

| # | item | state |
|---|---|---|
| 1 | `IRPT_BCKEND.TO-APPLY-Y75` leg L4 (X-1 actor read) | **unblocked, mine, next** |
| 2 | `IRPT_YCDGEN.TO-APPLY-st28` | GO'd, unblocked |
| 3 | `IRPT_BCKEND.TO-APPLY-Y77` (release 6) | starts when Y75 is terminal |
| 4 | `IRPT_BCKEND.TO-IB-pr-383` S1/S2/V1 | parked on the SSM grant; ledger RED by MSTR instruction |
| 5 | `NFRA_TRNSPT.TO-RUN-a17`, `b17` | parked on the KMS grant |

Landed tonight and closed: `st26`, `st27`, `F10`, `SA1`, `Y75` legs L1-L3, `IB-pr-383` legs A1/B1.

**Nothing is half-landed.** `383` carries two proven artifacts and no seeding, which the signed packet
states "is safe and changes the served bytes of nobody".

---

## 6. Three defects this seat found, for context on what the checks are buying

- **`D2-S16`** -- release 4's in-package `ImportError`, which produced the `symbol_closure` gate now run
  on every uploaded zip (`modules=62 pairs=273 missing=0` on 5b).
- **`D2-S18`** -- release 5's split commit, which rolled it back; 5b is the fix and is live.
- **`D2-S24`** -- `safe-deploy.sh` printing `0 file(s) deployed. NOTHING WAS DEPLOYED.` in the same run
  that minted and uploaded a bundle. Its own next line says to measure the artifact; that warning is
  what closed the leg correctly.

Also cleared this hour: a **staged sentinel of mine** (`tckt-vnext-sa1-clamp-20261009.json`) left in the
shared index by `deploy_ledger.py close` -- it deletes the file but leaves the index entry, which refused
every `safe-merge` for ~20 minutes and held `IRPT_BCKEND` round 97. Unstaged; index now carries 0 staged
paths. That is a gate worth having, since any closed ledger can strand a drain the same way.
