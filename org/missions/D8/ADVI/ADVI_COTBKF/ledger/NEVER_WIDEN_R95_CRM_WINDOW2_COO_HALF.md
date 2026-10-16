# NEVER-WIDEN co-sign, ROUND 95 -- the COO half: the SECOND one-job window on the restricted CRM zip (new key literal; round 88's limits unchanged)

**SUPERSEDED 2026-10-16 ~01:5xZ, NEVER SIGNED: the CTO ruled (msg 6389; record `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261016_013xZ_F086_9987_RELAYED.md` @dc3206a808) that round 95 is not cut: Andrew had the laptop read the local `Files.zip` in memory, which answered the question the second window would have asked (the CRM carries no account number; its TaxID has no partner on the account side; the only shared field is AdvisorID with 4 values). No key literal was ever filled in, no apply was planned, no role was created. This file is kept as the record of the draft.**

**DRAFT (superseded): the key literal `<KEY>` below is filled in, and the file hashed and committed, only when Andrew's exact key arrives from the CTO. Nothing here is signed until then.**

**Signer:** `2.0.0_SA_COO~C1` | **Date:** 2026-10-15/16 | **Acts covered:** (1) a targeted Terraform apply that adds ONE IAM role and ONE reader exception; (2) the matching job that assumes the role and reads ONE key in memory; (3) the withdrawal of both as the job's next act |
**Authority:** Andrew-direct 2026-10-15, call `d3cc` option (a), VERBATIM: "I agree with (a), let's see what we can do with that for now." (record `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261015_190xZ_D3CC_A_ONE_JOB_READS_RESTRICTED_CRM_ZIP.md`), and call `bccc`, VERBATIM: "Yes it was there to be super secret, i can break glass just let me know what to do for that." (record `ANDREW_DIRECT_20261015_205xZ_CALLS_BCCC_3ADB_BBD5.md` @cb7075dd11); the CTO's rulings: amendment 5 (`ledger/CTO_RULING_DELL1_UNPARK_ACCELERATE_20261015.md`), msg 6235 ("the second window is a new pair binding the new key literal") and msg 6334 ("open a new pair that reuses round 88's limits, with only the key literal changed. I sign the CTO half on it.") |
**The other half:** `1.0.0_SA_CTO~DELL1`, `ledger/NEVER_WIDEN_R95_CRM_WINDOW2_CTO_HALF.md` (not yet written) |
**Supersedes nothing:** round 88's pair (`NEVER_WIDEN_R88_CRM_MATCH_GRANT_COO_HALF.md`, sha256 `472df1c92c5927d6c714d1ab5bb3f13096d2456b0662f2524f388be17ed3bbc3`) covered a window now closed (the role was withdrawn 2026-10-15 ~20:07Z, verified `NoSuchEntity`); this pair is its own, on a different key literal. |
**Read against:** `infra/aws/terraform/shared-infra/s3-lgic-firm-buckets.tf` at HEAD (the three CRM Deny statements, `lgic_crm_readers`, `lgic_crm_writers`, the break-glass role); the round-88 records `deliverables/0.7.0_AE_CloudOps~CB1/GRANT_RECORD.json` and `WITHDRAWAL_RECORD.json`; the round-88 adjudication `surprise-channel/adjudications/ADJUDICATION_v62.md` (`CB88cj2-AC3` MET; `C-S3` answered by round 90) |

**Verdict:** to be SIGNED for the blast radius below, and ONLY it, once the key literal is in and the CTO half is signed. Until then no apply is planned and no job is staged.

## What changes in the world, and what is different from round 88

Same shape as round 88: for the length of ONE job, a new role can `GetObject` the ONE key
`s3://opal-data-cottonwood/<KEY>`
and the READ deny lets that role's ARN through; afterwards both are gone and a re-plan reads no changes. **Different:** (a) the key literal (`<KEY>`; Andrew read it from his console; the first window asked for `commonwealth/cottonwood/bronze/crm/date=2026-06-23/CRM_CottonwoodCapitalAdvisors.zip` and `head_object` returned 403); (b) the job is now parameterised: it reads its key and session name from the grant record (round 93) and the grant record's path from `--grant` (round 94); (c) the job's run record carries counts and role names only, never member text (round 90, `C-S3`); (d) the first window's 403 is read correctly: for a role without `ListBucket` a missing key and a refused read look the same, so a second 403 on a key Andrew has read in the console is a REFUSAL, not an absence.

## What the act MAY touch (the whole permitted set)

Exactly round 88's table, with the key literal changed:

| object | what moves | bound | rollback |
|---|---|---|---|
| a new `aws_iam_role` (name from `lib/opal_naming name()` via the `opal_name` module; a builder refusal is a registry row to add, never a typed name) and its inline policy | created | trust: ONE principal, the agents' shell user, `sts:AssumeRole`, no wildcard, no service; max session 3600 s; policy: `s3:GetObject` on the one key above, NOTHING else (no `GetObjectVersion`, no `List`, no `Put`) | the withdrawal order: destroy of the same two addresses |
| the firm bucket policy, statement `DenyRestrictedReadExceptReaders` | the role's ARN is added to the readers list that statement reads (`lgic_crm_readers`) | the READ deny only; the LIST deny and the WRITE deny are byte-equal | remove the ARN; a re-plan then reads no changes |

**Exception width, as in round 88 and accepted by the CTO there (msg 6150):** an IAM Deny cannot be lifted per key; the exception is prefix-wide for the READ deny and the ONE-KEY bound is the role's own allow. **No other object moves**: not the break-glass role, not the console user, not `lgic_crm_writers`, not any other bucket policy statement or firm bucket. The plan before the apply must show exactly 2 to add and 1 to change; if another project's unapplied change rides the plan it is CARVED OUT in the worktree only (never committed), as in round 88 (CTO ruling amendment 6); the inflection bucket policy changing is a STOP.

## Writers of the named property, counted

Same as round 88: N = 1 writer file (`s3-lgic-firm-buckets.tf`), 1 rule (the Deny reads `local.lgic_crm_readers`); this act adds one entry. The population measured is the repository's Terraform.

## Branches named (round 88's, with (d) corrected)

- **The key exists and the role reads it:** the job reads the zip once, in memory, and writes only the four allow-listed columns.
- **`head_object` returns 403 or 404:** the job records the exact error class, reads nothing, writes nothing, and the withdrawal runs at once. A 403 is read as "refused or absent, not told apart"; it is NOT read as "not landed".
- **The role cannot be assumed, or the plan carries a change outside the permitted set:** nothing is applied or nothing is read; the withdrawal (or the stop) follows.

## What the job MAY emit, and may NOT do

Exactly round 88's (the CVO graded it MET at L9 on the first window): link rows with exactly the columns `commonwealth_account, bd_account_id, rule, tier`, plus counts; no CRM column value leaves the job; the run record is the log and holds counts and role names only. Links are DETERMINISTIC only on a direct stable-key pair (an old/new account-number pair, or an identifier Black Diamond also carries), otherwise CANDIDATE; nothing is applied to the served crosswalk; the zip is never written to disk or copied; Cottonwood is not contacted. The CTO's added conditions (round 88): C1, the run record lists every `AssumeRole` event on the role with session names; C2, the withdrawal is absolute at 23:30Z of the grant day (23:59Z is the stop), and runs as the job's NEXT act; the CRM-record rule (round 90): the run record carries no member text.

## Order of the act, and its stop

1. Both halves signed; the CVO's PRD sign-off still `ADMITTED` (the PRD's C-RESTRICTED text carries Andrew's one-job exception and its limits). 2. Ledger entry opened in `org/critical_paths/change_management/` (with the `.open_deploys/` sentinel) naming the removal as its rollback, BEFORE the plan. 3. The apply starts no earlier than 00:05Z and no later than 20:59Z of a UTC day (three hours must remain before 23:59Z for the job and the withdrawal). 4. Targeted plan read: 2 add, 1 change. 5. `bash .tools/safe-apply.sh` scoped to those addresses; live read-back. 6. The job (one run), then the withdrawal as its next act; a re-plan reads no changes; the ledger closes. **Stop:** a plan with any other change, an apply that leaves one half landed without the other, a job that writes a column outside the allow-list or a record that carries member text, or a job still unfinished at 23:30Z: the withdrawal runs regardless and the finding is the report.

-- `2.0.0_SA_COO~C1` (DRAFT)
