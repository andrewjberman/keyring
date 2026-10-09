# 0.7.0_AE_CloudOps~TRL -- NFRA_TRNSPT s21 applied, a18 VERIFY leg worked to its device limit

**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE, COORDINATE

**Session:** 2026-10-09 12:53Z -> 15:00Z | **Device:** laptop | **Branch:** box/laptop
**Serial:** `0.7.0_AE_CloudOps~TRL` (new lane, first session; no prior log)

---

## Summary

Seated as the laptop CloudOps lane for NFRA_TRNSPT. Two GOs arrived and were acted on the same
turn each. `TO-APPLY-s21` is COMPLETE: FWD-5's silver-only reader role and its one key-policy
statement are live, proven by three real reads through the role, and its ledger is closed with a
VALID proof-of-spec instance. `TO-APPLY-a18`'s open VERIFY leg was worked to the limit this
device allows -- role read-back and key-policy diff DONE on a stronger instrument than the leg
asked for -- and LEFT OPEN, because both of its real reads need credentials that do not exist on
the laptop. One decision is owed by the issuer.

---

## Startup

`/watcher`: lane `~TRL` was NOT REGISTERED; registered LIVE (PID 20908). Watcher armed, census
exactly 1 row every time, re-armed on each of the four `[WATCHER-EXPIRED]` notices in one call,
same turn, no skill load. Final arm: task `bega4wuta`, script pid 11536. Zero crons.

`org/XXX.md` A-F all run. Identity cross-check clean (`liveness.json` shows `~TRL` at PID 20908,
no other serial at that PID). PATH: 102 of 102 comp-tools resolve bare and a forwarder RAN.
`audit-archive-invoker` printed ONE finding -- a non-append edit of
`org/mcp/agent-spawn-audit.log` at line 12991 -- which the invoker itself defers to a
GOVERNANCE_AUDIT-permitted exec startup; owned elsewhere, not re-filed. `/cloud-ops` loaded.

TOs held: ONE at start (`s21`, by `<issued_to>`), a second (`a18`) re-addressed mid-session. The
7 rows `get_agent_status` printed are BASE-scoped and exact-string-matched, not this lane's --
rule 22a.

---

## Deployment Sequence -- NFRA_TRNSPT.TO-APPLY-s21 (WORLD, DEPLOY)

Pin `32d09cc6ad06beb379ddd344f0f551dcced8077b` on `box/laptop`, carrying `365a08577e` and
`dc5032abde` (both `merge-base --is-ancestor` YES; the reverse direction run as the negative
control, NO). Order amendment `124e65440e`. Both never-widen halves read in full first: COO
`@23251db022` blob `74b8779dba`, CTO `@91e314b74e` verdict GIVEN.

1. Change ledger OPENED with 3 legs; live key-policy Sids printed (4 statements, no
   `SilverReaderDecryptOnly`, `DellAgentUsersGenerateDataKey` present with both conditions).
2. `terraform init -reconfigure` -- the shared tree's `.terraform` was written by another
   terraform version and refused the plan ("Backend configuration block has changed"). The
   backend `bucket`/`key`/`region` were compared against `main.tf` and are IDENTICAL, so
   `-reconfigure` migrated no state; `-migrate-state` was not used.
3. `terraform plan -target` x4 `-out=s21.tfplan`. **3 to add, 1 to change, 0 to destroy.**
4. Plan GRADED from `terraform show -json`, not the human diff: 4 non-no-op over a denominator of
   6 `resource_changes`. The two no-ops (`aws_iam_role.second_reader`, `aws_s3_bucket.transcripts`)
   confirm the `-var` matches live; the four Lambda files produced zero changes, so the shared-zip
   drift named as a STOP in the a18 preflight did not happen.
5. `safe-apply` from the SAVED plan. Gates: APPLY-WHO ADMITTED; CROSSBOX-DEPLOY verdict STOP in
   **WARN** mode, both limbs read rather than waved through (see Blockers/Findings); HALT-GATE
   surfaced 3 base-serial messages, all read, none STOP-class, none naming this root -> re-run
   with `HALT_ACK=1`.
6. Live readback, key diff, three-read proof, targeted re-plan. Ledger CLOSED, 3 of 3 legs proven.

### Verification -- actual output

```
aws iam get-role --role-name teams-global-transcripts-silver-reader-role --query "Role.RoleName"
  "teams-global-transcripts-silver-reader-role"
aws iam list-attached-role-policies --role-name teams-global-transcripts-silver-reader-role
  ["teams-global-transcripts-silver-reader-policy"]

live key policy Sids, AFTER (5):
  RootAdministersTheKeyAndCannotUseIt
  NamedReadersUseTheKey
  DellAgentUsersDecryptOnly
  SilverReaderDecryptOnly        <- added by this act
  DellAgentUsersGenerateDataKey  <- survives, both conditions intact

THE THREE READS (statuses only; 1-byte ranged GET, byte file deleted in the same call)
identity: arn:aws:sts::313476888478:assumed-role/teams-global-transcripts-silver-reader-role/s21-silver-reader-proof
silver/monday_meeting  expect=200          rc=0   verdict=200 OK   bytes_fetched=1
bronze/asset_mgmt_ic   expect=AccessDenied rc=255 verdict=REFUSED  error_code=AccessDenied
silver/research_mtg    expect=AccessDenied rc=255 verdict=REFUSED  error_code=AccessDenied

CONTROL, separate arm, session unset (so a denial cannot be a missing object):
MM-20260608-0855.parquet ContentLength 29000; ICA-20260609-0958.vtt 52063;
RT-20260407-1027.parquet 41922  -- 3 of 3 exist

targeted re-plan -detailed-exitcode -> rc=0, "No changes."
```

### The one judgment this act turned on

The pair's condition is "ONE in-place key-policy update whose ONLY difference is the added
`SilverReaderDecryptOnly` statement; anything else = STOP". **The plan cannot show that.** The new
statement's `Principal` is the role ARN created in the same plan, so `policy` is `after_unknown`
and terraform renders the whole before-policy as removed. That is an instrument limit, not a wide
blast radius.

Resolved the way the never-widen law asks: the after-image was read from the PRODUCER'S OWN RULE
(`main.tf`'s `jsonencode`; writers of the key policy counted, **N = 1**, because a18's leg had
already landed), written into the ledger BEFORE the apply, and then MEASURED against live.
Realized diff: 4 -> 5 statements, ADDED `SilverReaderDecryptOnly`, REMOVED none, 0 of 33
before-leaf-values gone after, and the realized after-image equals the prediction statement for
statement and in `main.tf`'s own Sid order.

A byte comparator said 3 of 4 shared statements had changed. Every one resolved to
`Principal.AWS` ARRAY REORDERING by KMS's own renderer -- identical membership, no value change.
That was measured, not asserted: the same comparator was run against a PLANTED MUTANT
(`DellAgentUsersGenerateDataKey`'s `kms:ViaService` set to `sqs.us-east-1.amazonaws.com`) and it
reported drift, so a real one-value narrowing could not have passed here as reordering.

---

## NFRA_TRNSPT.TO-APPLY-a18 -- VERIFY leg (GO msg 107993, nothing applied)

- **Role read-back DONE.** `teams-global-transcripts-second-reader-role`, CreateDate
  `2026-10-09T09:55:13Z`, its policy attached, trust = `user/Opal_Terminal` alone.
- **Key-policy diff DONE, on a better instrument than the leg asked for.** The APPLY leg's proof
  was a `safe-apply` receipt, i.e. the producer's self-report. The diff was taken instead from the
  `PutKeyPolicy` REQUEST DOCUMENTS in CloudTrail -- the bytes AWS was asked to store.
  `lookup-events` returned **11** events for 2026-10-09 (denominator printed); **3** carry a
  `keyId` and no `errorCode`: 05:40:10Z (pre-a18, 4 statements), 09:55:22Z (a18, 4), 14:07:33Z
  (s21, 5). a18's diff: 4 -> 4, ADDED Sids none, REMOVED none, **exactly ONE principal differs**
  -- the second-reader role added to `NamedReadersUseTheKey`. CTO half condition 1 SATISFIED.
  The remaining 8 events are `MalformedPolicyDocumentException` in the seconds before each
  successful put, the same shape at both applies: the provider retrying while a just-created role
  ARN is not yet resolvable to IAM. Named rather than left as an unexplained 8.
- **The ADMITTED/REFUSED proof NOT EXERCISED, and not exercisable here.** Measured both arms:
  `sts:AssumeRole` on the second-reader role returns `AccessDenied` for `user/Andrew_Berman`
  (its trust admits `Opal_Terminal` alone -- correct behaviour), and `irpt-ycharts-runner-role`'s
  trust is `Principal {"Service": "ec2.amazonaws.com"}` only, so no IAM user can assume it and
  that read must run ON a dell2 EC2 host. No principal was minted to manufacture either arm.
- **Leg LEFT OPEN.** `deploy_ledger.py list` reads the entry HELD-SOVEREIGN-GATED,
  `open-verify=['VERIFY']`, **tracked-not-stranded**, and its own `gate.reread` already names the
  same two probes. ONE decision owed by `2.0.0_SA_COO~T2`.

---

## Compiler Tools

| Tool | Invocation | Result |
|---|---|---|
| comp-adversary | `compose <s21 order> --max-neighbors 6 --digest-budget 6` | PASS. 4/4 cited commits VERIFIED; flagged `NFRA_TRNSPT_DECOMP_R21.md` MOVED-SINCE-AUTHORING (09:07:16Z vs the order's 09:00:11Z vintage) -- read at HEAD, AMENDMENT 1's TR-a-21 row matches and AMENDMENT 2 concerns TR-d-20 only; flagged `dc5032abde` as a hex run `COMMIT_RE` did not parse, verified by hand |
| comp-iam | `comp-iam role teams-global-transcripts-silver-reader-role` | FAIL (instrument). "No role matching" -- the name is `jsondecode(file(NAMES.json))` output, not a literal in the `.tf`. Recorded in the instance's `declared_exclusions` |
| comp-schedule | DECLARED-NOT-APPLICABLE per the order's preflight | n/a -- an identity grant, no schedule |
| comp-find / comp-rail | two denials, both answered | PARTIAL. One answered with the printed RUN NEXT; two reads re-run under an audited `# rail-checked:` marker (the proof OBJECT-KEY listing, and the live assume-role access proof) |
| proof-of-spec-check | `<instance> AC1 --governing-order <order>` | PASS. VALID rc=0, 0 violations, 4 of 4 controls discriminate, 1 of 1 git artifact row resolved at pin |
| deploy_ledger.py | `open` / `close-leg` x3 / `close` / `list` | PASS. s21 CLOSED, sentinel removed; a18 correctly classified tracked-not-stranded |

**What worked:** grading the plan from `show -json` rather than the rendered diff -- it is what
turned an unreadable `(known after apply)` key diff into a precise 4-non-no-op-over-6 statement.
CloudTrail's `PutKeyPolicy` request documents are a far better key-policy oracle than a
`safe-apply` receipt, and they are immune to the KMS array-reordering artifact.

**What failed:** `comp-iam role` cannot see a role whose name comes from
`jsondecode(file(...))`. Also `python ... <<'PY'` heredocs break in this Git Bash for long
bodies ("unexpected EOF while looking for matching `''`"); writing the script to the scratchpad
with the Write tool and running `python -I <file>` is the reliable shape.

**Gap found:** two, both in Findings below.

---

## Findings (routed, not blocking this lane)

1. **A simulate is anti-correlated with what a18 proves, not merely weaker.** `Opal_Terminal`
   holds `AdministratorAccess` through its group, so `simulate-principal-policy` reads `allowed`
   for both `s3:GetObject` on a bronze object and `kms:Decrypt` on the transcripts key -- and
   would have read the same BEFORE a18 landed, when the real read was denied by the key policy.
   `main.tf`'s own note says why (root gets administration, never the use actions, so an IAM
   `kms:Decrypt` on `"*"` does not reach this key). Quoting it as ADMITTED would be a false pass
   of exactly the class a18's refusal proof exists to catch. Recorded in the a18 ledger; routed to
   `2.0.0_SA_COO~T2` in the report.
2. **A relocation amendment that moves an order between seat folders must move `<paths>` with
   it.** AMENDMENT 1 moved s21 into `~TRL/task_orders/` but left `<paths>` naming the BASE
   deliverables dir. `to-pipeline-gate.py`'s `_proof_instance_candidates` derives its search dir
   from the ORDER'S OWN directory and ignores a `<proof_of_spec>` tag naming a path outside it,
   and NFRA_TRNSPT reads `dep_stage=EXECUTING`, so the gate was in scope: the instance in the base
   dir would have refused the issuer's complete flip with "NO proof-of-spec instance was found
   beside it" -- the same failure `2.0.0_SA_COO~C` hit on IRPT_BCKEND.TO-APPLY-Y75 (msg 107927).
   Found by checking the CONSUMER rather than assuming the `<paths>` block was the authority.
   Instance moved, re-validated, and the pattern routed to T2 for future amendments.
3. **Not a finding after measurement:** the HALT gate's 3 pending base-serial messages
   (107927/107939/107942) looked like a deaf-base-inbox hole; `get_live_agents` then showed
   `0.7.0_AE_CloudOps` LIVE (a codex seat) and `~CTL` reporting the NFRA_CTLPLN orders terminal.
   So the work was done by the lane and the messages are stale duplicates in the unread root,
   where they keep tripping the HALT gate for every apply from this box. Named to
   `2.0.0_SA_COO~C` as a one-liner, no action asked.

---

## Blockers

**One, evidence-cited, owned elsewhere:** a18's VERIFY leg condition 2 needs two real reads this
device cannot make -- `Opal_Terminal`'s (site Z's Bloomberg terminal identity, via
`0.0.0_AB_MSTR`) and an unnamed dell2 service role's from a dell2 EC2 host (via
`2.0.0_SA_COO~T2`). Both measured, quoted above. **ABSENT is not EXERCISED-AGAINST:** nothing
here says either read would fail.

Nothing blocks s21, which is complete.

---

## Files Modified

See commit messages: `e7ce5f2700`, `ce04c2dee3`, `31ee4440a2`. Plus the ledger `open`/`close`
commits the `deploy_ledger.py` contract makes under its own hand.

| Path | Note |
|---|---|
| `org/critical_paths/change_management/20261009T1339Z_nfra-trnspt-s21-...md` | the s21 ledger: before-image, graded plan, pre-apply prediction, measured after-image, the three proof statuses. CLOSED |
| `org/critical_paths/change_management/20261009T0933Z_nfra-trnspt-a18-...md` | a18's VERIFY section appended; leg left OPEN with its two owners named |
| `org/tier2_senior/0.7.0_AE_CloudOps~TRL/deliverables/NFRA_TRNSPT.TO-APPLY-s21...proof_of_spec.json` | VALID rc=0; moved here from the base dir so the complete-flip gate can find it |

No `pipeline_inventory.xml` edit, stated as a decision rather than left as an omission: this act
was three IAM resources plus one key statement in ANOTHER project's terraform root, the core
document carries no transcripts section, a18's apply added none either, and round 21 already
assigns that root's registration to cells `TR-m-21` (source-map entries) and `TR-g-21` (the first
`transcripts-v1.0.0` tag, the ISSUER's after the drain). `git tag -l "transcripts-v*"` still
reads 0, so no tag was taken here either -- taking it would cut another seat's cell.

---

## MCP traffic

4 messages total. IN: `107966` GO on s21 (acked), `107993` GO on a18's VERIFY leg (acked).
OUT: 3 sends -- the s21+a18 report relayed to dell2 `2.0.0_SA_COO~T2` through `0.0.0_AB_MSTR`
with its one ask, a copy to `2.0.0_SA_COO~C`, and a path addendum for the complete flip.

---

## Current State

`0.7.0_AE_CloudOps~TRL` LIVE on the laptop, PID 20908, branch `box/laptop`, workspace root
`C:/Users/AndrewBerman/Desktop/ajb_workspace`. One inbox watcher, census exactly 1 row, task
`bega4wuta`, script pid 11536. Zero crons. Inbox empty, both messages ever delivered to this
lane acked.

**Live in the world because of this session**, all in account 313476888478:
- `arn:aws:iam::313476888478:role/teams-global-transcripts-silver-reader-role` -- trust
  `TrustTheRawTierReaders` admitting `user/Andrew_Berman`, `user/cloudops-dell1-agent-user`,
  `user/cloudops-dell2-agent-user`.
- `arn:aws:iam::313476888478:policy/teams-global-transcripts-silver-reader-policy`, default
  version `v1`, attached to that role: GetObject on `teams/transcripts/silver/*` and
  `outlook/transcripts/silver/*`, ListBucket conditioned on those prefixes, explicit Deny on
  `teams/transcripts/silver/research_meeting/*` for GetObject and ListBucket. No bronze, no raw,
  no write.
- KMS key `44a2284f-1e14-4ea1-b6cb-f6121bfde35a` (`alias/opal-data-transcripts`): 5 statements,
  the new one being `SilverReaderDecryptOnly` (Decrypt + DescribeKey for that role,
  `kms:ViaService` = `s3.us-east-1.amazonaws.com`). Rollback is one `put-key-policy` of the
  before-image recorded verbatim in the s21 ledger's step 0.

Terraform: `infra/aws/terraform/transcripts` is initialized against
`s3://opal-313476888478-terraform-state` key `transcripts/tfstate`, aws provider v5.100.0,
terraform v1.15.8 on PATH (no `.tools/terraform.exe` on this device). Targeted re-plan is 0-diff.
A saved plan `s21.tfplan` is left in that directory, already applied and now stale.

Commits `e7ce5f2700` (on origin/box/laptop, `ls-remote` read), `ce04c2dee3` and `31ee4440a2`
(LOCAL at the time of writing, `ls-remote` read; the laptop's scheduled `box-sync` pushes them --
this seat does not push a shared branch).

Ledgers: s21 CLOSED with no sentinel. a18 HELD-SOVEREIGN-GATED with VERIFY open, classified
tracked-not-stranded by the tool.

---

## Next Steps

1. `[2.0.0_SA_COO~T2]` Flip `NFRA_TRNSPT.TO-APPLY-s21` to `complete`. The VALID instance is at
   `org/tier2_senior/0.7.0_AE_CloudOps~TRL/deliverables/NFRA_TRNSPT.TO-APPLY-s21.silver-reader-role-laptop.proof_of_spec.json`;
   the flip is refused if the gate is pointed anywhere else.
2. `[2.0.0_SA_COO~T2]` ONE decision on a18's VERIFY leg: close it on the CloudTrail key-policy
   diff plus the trust documents, or hold it for the two real probes. If holding, the two reads
   are one each for the site-Z terminal seat (`Opal_Terminal` assumes the role, GETs one object,
   expect ADMITTED) and a dell2 seat (an unnamed dell2 service role GETs the same key from a
   dell2 EC2 host, expect REFUSED). Statuses only, no content.
3. `[2.0.0_SA_COO~T2]` Consider moving `<paths>` with the order in any future relocation
   amendment (Finding 2).
4. `[0.7.0_AE_CloudOps~TRL]` Event-driven hold: act on the next `[INBOX]` event the same turn,
   and re-arm the Monitor on each `[WATCHER-EXPIRED]` line in one call, same turn, no skill load.
5. `[1.0.0_SA_CTO]` or `[0.0.0_AB_MSTR]` -- unowned only if nobody else holds it: the
   `audit-archive-invoker` non-append finding on `org/mcp/agent-spawn-audit.log` (line 12991,
   baseline 6161037B vs live-head 6003052B). The invoker defers it to a GOVERNANCE_AUDIT-permitted
   exec startup; this lane did not re-file it.
