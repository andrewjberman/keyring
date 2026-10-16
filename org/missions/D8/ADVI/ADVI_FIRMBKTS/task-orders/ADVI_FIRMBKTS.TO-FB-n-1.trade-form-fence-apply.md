# ADVI_FIRMBKTS task order -- `FB-n-1` -- APPLY THE TRADE-FORM FENCE PAIR: THREE POLICIES, THE ALLOW-APPEND, THREE CORS RULES, ONE SCOPED APPLY, READ BACK

<!-- ===================== WORKER FACE -- this is the WHOLE of the executing seat's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_TRADEFORM.md</decomp_doc>
<owned_cells>FB-n-1</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~TF</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- the order adds no rule, schedule or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no identity-side grant is added; the role's own PutObject grant is the TCKT_VNEXT release's (`TO-R18-TR3`), not this order's. This order changes three bucket policies and adds three CORS rules.
comp-adversary: RUN by the issuer (`compose` on this order, read-vintage HEAD @faf5a9fdd3): the cited commit @ee287446e1 verified; the only absent cited paths are the three the executor creates (the new CORS file, the record, the instance). At base the record is absent (AC1 FAIL); the grader rejects a non-zero prefix object count, a baseline that is not clean, a plan other than 3 add / 3 change / 0 destroy with no statement removed, a second apply, an origin outside the three, any method outside GET and PUT, a changed other-principal statement, an Allow count other than the table's, an unsigned pair, no recorded rollback, an unclosed ledger entry and any id-shaped token of nine or more digits. Blindness: the record proves the apply's shape and read-backs, not that the three origins are the right set (the CTO half confirmed them) and not that the generator's rendered text is right (the plan diff is read by the CTO).
EGRESS CLASS, declared: NONE (AWS calls inside the one account, no vendor API).
</preflight>

## 1. THE ACT -- `FB-n-1` (round 8, workstream TRADEFORM, WORLD)

STAGED. You act only after the issuer's UN-PARK AMENDMENT in this file's record face. That amendment is written when the laptop CTO sends the GO for this order's id. Until it exists, do nothing.

The ticket API role `arn:aws:iam::313476888478:role/opal-ticket-api-role` is admitted to `s3:GetObject` and `s3:PutObject` under ONE prefix in each of three firm buckets, through the fence's registry rows (already at HEAD), and the browsers that upload the trade form are admitted by one CORS rule per bucket. You make ONE targeted Terraform apply and read it back. WHO may touch three client-confidential buckets widens by exactly this one role, two actions and one prefix each; no served output moves.

| bucket | prefix (from `lib/opal_naming.py address()`, equal to the registry row; never retyped) |
|---|---|
| `opal-data-49financial` | `portal/49financial/state/ticket_attachments/trade-form/` |
| `opal-data-inflection` | `portal/inflection/state/ticket_attachments/trade-form/` |
| `opal-data-cottonwood` | `portal/cottonwood/state/ticket_attachments/trade-form/` |

### 1a. THE PAIR YOU ACT UNDER (read both at their commits; they are the whole spec)

- COO half: `org/missions/D8/ADVI/ADVI_FIRMBKTS/ledger/NEVER_WIDEN_TCKT_TRADE_FORM_FIRM_BUCKET_ACCESS_COO_HALF.md`, the bytes at `5c3504c184` (amendment 4).
- CTO half: `org/tier1_exec/1.0.0_SA_CTO/deliverables/NEVER_WIDEN_CTO_HALF_TCKT_TRADE_FORM_FIRM_BUCKET_ACCESS_20261016.md`, the bytes at `1c8af1a3fc` (SIGNED on those COO bytes).

Read each with `git show <commit>:<path>`. Before any write, confirm the COO half at HEAD is byte-equal to `5c3504c184` (`git diff 5c3504c184 HEAD -- <the COO half path>` prints nothing) and that the CTO half is at HEAD and signed. If either fails, do nothing and say which.

### 1b. Steps (once un-parked)

1. **Preconditions, each read and recorded** (the COO half's preconditions 1 to 3, amendment 4's two-part baseline):
   1. The role exists (`iam get-role`), and exactly three registry rows name `opal-ticket-api-role` in `infra/logic/registry/exemptions.json`, one per bucket, each prefix equal to the table above, each carrying `arn`.
   2. Object counts under each prefix (counts only, never a key): all three 0. A non-zero count is a STOP.
   3. Save each bucket's prior `get-bucket-policy` JSON and read `get-bucket-cors` (expect `NoSuchCORSConfiguration` on all three). These saved files are the rollback.
   4. SEQUENCE WITH M02: read every live worktree's `.open_deploys/` (union, denominator printed) for an open entry on `opal-data-inflection`. If one is open, do not apply; report and wait. Whichever of M02 and this apply lands second plans against the first's live state.
   5. **Baseline, two parts.** The three trade-form rows are already at HEAD, so read both parts in a SCRATCH worktree where `infra/logic/registry/exemptions.json` has exactly the three `opal-ticket-api-role` rows removed (plan only; nothing from the scratch is committed or applied). Part 1: at that registry and the code at HEAD, the scoped plan of the three bucket policies reads `No changes`. Part 2: with the one Allow-append edit of step 2 added and the rows still removed, the plan on the two lgic buckets adds exactly the existing Inflection Performance row's two Allows to `opal-data-inflection` and nothing to `opal-data-cottonwood`. Part 1 reading a change means an earlier edit was never applied: STOP and report what differs. If you cannot take the baseline cleanly this way, STOP and report; do not improvise another baseline.
2. **The two edits, in ONE commit of yours** (the apply commit):
   - In `infra/aws/terraform/shared-infra/s3-lgic-firm-buckets.tf`, in the `concat(...)` of the bucket policy's statements (the `fence_scoped_statements` lookup is at line 172), add `lookup(module.opal_name.fence_scoped_allow_statements, aws_s3_bucket.lgic_firm[each.key].bucket, [])` immediately after it. No other line of that file changes. `opal-data-49financial` is not edited (its file already appends both lists).
   - In a NEW file in the same root, `infra/aws/terraform/shared-infra/s3-ticket-trade-form-cors.tf`, three `aws_s3_bucket_cors_configuration` resources, one per bucket, each referencing the bucket resource the way that bucket's policy resource does. Each has ONE rule: `allowed_origins` exactly `https://opalinvest.dev`, `https://www.opalinvest.dev`, `http://localhost:5174`; `allowed_methods` `PUT`, `GET`; `allowed_headers` `Content-Type`; `expose_headers` `ETag`; `max_age_seconds` 300. A different shape, a wildcard, the other four localhost ports or any other method is a STOP.
3. **Ledger** (NEVER-2) with its `org/critical_paths/.open_deploys/` sentinel, opened BEFORE the first write, committed.
4. **The plan**, scoped by `-target` to exactly the six resources: the three bucket policy resources and the three CORS resources. It must read `3 to add`, `3 to change`, `0 to destroy`; each policy diff is exactly the new principal in the exemption list, the Deny pair, and the Allows below; nothing is removed from any policy. Per bucket, the Allows the plan adds (the generator's own rendered text is the reading; this table is the expectation):
   - `opal-data-49financial`: `AllowScopedExemption10Objects` (GetObject on the prefix) is part of its rows' rendering; the lookup edit adds none here.
   - `opal-data-inflection`: 3 Allows added by this apply: `AllowScopedExemption1Objects` and `AllowScopedExemption1Listing` for `irpt-performance-adapter-role` (the existing row), and `AllowScopedExemption2Objects` (GetObject on the trade-form prefix) for `opal-ticket-api-role`.
   - `opal-data-cottonwood`: 1 Allow added: `AllowScopedExemption1Objects` (GetObject on the trade-form prefix).
   - No `s3:PutObject` Allow anywhere (the write grant is the role's own IAM policy). If M02's rows landed first on inflection, the generator's output at the plan is the reading and the numbers above shift by M02's own rows: say so in the record and stop for the issuer if the diff contains anything not in this list.
5. **ONE apply:** `bash .tools/safe-apply.sh`, scoped by the same six `-target`s. Only through safe-apply. A second apply is a STOP.
6. **Read back, per bucket:** `get-bucket-policy` and `get-bucket-cors`. The policy reads as the plan said; every other principal's statements are byte-equal to the saved prior JSON; the CORS rule reads exactly as step 2. Record the Allows this apply added, per bucket.
7. **Branch B (STOP, roll back, report; either half):** a plan count other than 3/3/0; a statement, principal or action outside the permitted set in a diff; a statement removed; the baseline not clean; a prefix not empty; the role missing; a policy put refused (read the prior policy back); an origin outside the three. Roll back per the COO half's amendment 4: revert the one added lookup line and the CORS file, apply the same scoped change, and byte-compare each bucket's policy to the saved prior JSON.
8. Close the ledger entry. Report.

### 1c. The record: `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~TF/TRADEFORM_FENCE_RECORD.json`

The grader checks this shape. No client name, relationship id or secret in it; counts only.
```json
{"order": "FB-n-1", "read_at": "<ISO UTC>",
 "preconditions": {"role_exists": true, "rows_at_head": 3,
   "prefix_object_counts": {"opal-data-49financial": 0, "opal-data-inflection": 0, "opal-data-cottonwood": 0},
   "baseline_part1": "No changes",
   "baseline_part2": {"inflection_allows_added": 2, "cottonwood_allows_added": 0},
   "prior_policy_saved": true, "prior_cors_absent": true, "m02_open_apply_on_inflection": false},
 "plan": {"add": 3, "change": 3, "destroy": 0, "statements_removed": 0},
 "applied": {"apply_count": 1, "targets": 6, "commit": "<the apply commit>"},
 "after": {"buckets": {"<each of the three buckets>": {"policy_read_back": true, "other_principals_byte_unchanged": true,
     "cors": {"origins": ["https://opalinvest.dev", "https://www.opalinvest.dev", "http://localhost:5174"], "methods": ["GET", "PUT"], "max_age": 300}}},
   "allows_added_by_this_apply": {"opal-data-49financial": 0, "opal-data-inflection": 3, "opal-data-cottonwood": 1}},
 "pair": {"coo_half": "5c3504c184", "cto_half": "1c8af1a3fc"},
 "rollback": {"recorded": true, "how": "<the exact steps>"}, "ledger_closed": true, "claim": "measured"}
```

## 2. BOUNDS

1. The act touches exactly: the three bucket policies, the three CORS configurations, the one lookup line, the one new CORS file, the ledger and the record. Any other resource, bucket, principal, action, prefix or statement is a STOP and a BLOCKING row.
2. No `s3:ListBucket` for the ticket role, no `PutObject` Allow, no wildcard origin, no second apply, no hand edit of a bucket policy's `ArnNotLike` (the fence generator is the one writer).
3. `terraform` only through `bash .tools/safe-apply.sh`; AWS from bash is `.tools/aws`; the ledger entry opens before the first write and closes at completion (CLAUDE.md NEVER-2). Print no secret, client name or relationship id. Object counts only, never a key.
4. A Dell writes no bucket policy: this order is executed on the laptop.

## 3. SURFACES

<paths>
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~TF/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
infra/aws/terraform/shared-infra/
</paths>

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~TF/ADVI_FIRMBKTS.TO-FB-n-1.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-n-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; timeout 30 python -I org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round8/checks/r8_checks.py tradeform --file org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~TF/TRADEFORM_FENCE_RECORD.json</invocation><expect>^TRADEFORM: OK buckets=3 applies=1$</expect></criterion>
</proof_of_spec>

AC1 grades the record's shape and discipline.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~TF/ADVI_FIRMBKTS.TO-FB-n-1.proof_of_spec.json`. Commit the record FIRST, your rows and the instance second; flip `<status>` to `complete` in the SAME commit only when AC1 passes. Report once to `2.0.0_SA_COO~B1` and the laptop `1.0.0_SA_CTO`: the plan counts, the Allows added per bucket, the apply commit, the pair commits, AC1 and the FULL commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** STAGED at the cut (workstream TRADEFORM). Asked by the laptop `1.0.0_SA_CTO` msg 109703 (relayed by `0.0.0_AB_MSTR~DELL1` msg 6786), as the fence owner's order for the signed trade-form pair; the broker refuses an act to a Tier-2 seat without a task order (LD-0529). The cell serves no FWD of this PRD: it is the fence owner's act for TCKT_VNEXT FWD-10 (Andrew P2, due 2026-10-24; the apply targeted 2026-10-20), under ruling `RULING_20261014_195xZ_TCKT_TRADE_FORM_FIRM_BUCKET_ACCESS_ROUTE.md` @ee287446e1. Un-park: the laptop CTO's GO, then the issuer's amendment here. Executor: `0.7.0_AE_CloudOps~TF` on the laptop; the laptop MSTR seats and carries and does not author or read the order. Row `NFRA_CTLPLN-W89-S3` closes on this apply's read-back, by `2.0.0_SA_COO~C`. Sequenced with M02 on `opal-data-inflection`. ISSUER'S READING, flagged: the two-part baseline is taken in a scratch worktree with the three rows removed, because the rows already landed (the halves wrote it as before the rows); if the executor or the CTO reads the halves differently, that is a question back to the issuer, answered by amendment.

**AMENDMENT 1 (2.0.0_SA_COO~B1, 2026-10-16 ~16:0xZ) -- UN-PARKED. GO from the laptop CTO (msg 109707, relayed by MSTR~DELL1 msg 6806). It replaces step 2's first bullet and adjusts the baseline; where it differs from section 1b above, THIS governs.** (1) THE LOOKUP LINE IS DONE, NOT YOURS: the laptop CTO committed the one `fence_scoped_allow_statements` lookup in `infra/aws/terraform/shared-infra/s3-lgic-firm-buckets.tf` at `e411130091` (origin/box/laptop; this seat read the diff: 3 insertions, the one lookup line right after the `fence_scoped_statements` lookup, plus a 2-line comment, nothing else). Do NOT edit that file: `owned-paths-validate.py --check-agent` on the HEAD bytes of `.owned-paths.yaml` refuses it to every CloudOps lane (lane `ADVI_COTBKF_C`), `0.7.0_AE_CloudOps~TF` included. Work from a tree that carries `e411130091`, and re-plan against it before the apply (the CTO reports your baseline read clean). Baseline part 2 now means: that tree, the three rows removed in the scratch, plan only. (2) YOUR ONE COMMIT is the NEW file `infra/aws/terraform/shared-infra/s3-ticket-trade-form-cors.tf` (the same checker, run on the same bytes, does not refuse it to your lane; a DS seat used as the negative control is refused). Put its commit in `applied.commit`. If the lane gate refuses any commit of yours, STOP and report; never use `GIT_COMMIT_AUTHOR_OVERRIDE`. (3) ROLLBACK of the lookup line is a revert of `e411130091`, which only the CTO's lane can commit: in a Branch B, you stop, report, and apply the same scoped change once that revert is at HEAD; write this into `rollback.how`. Everything else in section 1b stands: the pair, the six `-target`s, the plan 3 add / 3 change / 0 destroy with nothing removed, the Allows table, the single apply, the read-backs, the record. No criterion changed (AC1 is unchanged); no gate limb graded this modification beyond the placeholders check (`NONE`). Executor `0.7.0_AE_CloudOps~TF` is the laptop's own seat: CLAUDE.md rule 34 (one CloudOps lane per macro per box) leaves a lane on another box to that box. Status pending.

<status>complete</status>
<round>8</round>
<workstream>TRADEFORM</workstream>
<to_id>ADVI_FIRMBKTS.TO-FB-n-1</to_id>
<slot>~TF</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
