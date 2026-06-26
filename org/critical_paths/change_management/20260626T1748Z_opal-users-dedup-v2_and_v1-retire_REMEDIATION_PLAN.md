# REMEDIATION PLAN -- opal_users_v2 de-dup (double-TF-management) + opal-users (v1) dead-twin retire

**Status:** PLAN (assembled 20260626T1748Z) -- NOT YET EXECUTED. Deliberate, not-tonight (estate-quiet for the 02:00 PIECE-2 + S2-L6 proofs). Two separate gated changes bundled per COO 174231Z.
**Author:** 0.7.0_AE_CloudOps (sole portal-auth-TF applier)
**Gates:** v2 de-dup -> COO -> CTO arch-gate -> Andrew human-confirm @ apply (unrecoverable-class: terraform state rm + recovery-control surface). v1 retire -> COO -> Andrew human-confirm @ drop (unrecoverable-class: table delete). Route v1 to CVO/NFRA_DEBTSCAN as a dead-resource data point (NOT folded into v2 surgery -- no contention).
**Light guard in force until v2 de-dup lands:** every portal-auth apply carries a pre-apply plan-review confirming opal_users_v2 shows 0 add/change/destroy.

---

## PART A -- opal_users_v2 de-dup (double-TF-management)

### A.1 Grounded problem statement (source + live)
The SAME physical table `opal-users-v2` is declared in TWO terraform roots:
- **shared-infra/dynamo.tf:15-68** -- has `point_in_time_recovery { enabled = true }` (lines 58-60); import home (CDRS_TFIMPT.006, 2026-04-15); CI-tracked; `System=PortalAuth` tag. **<- SURVIVOR.**
- **portal-auth/dynamodb.tf:174-218** -- PITR block **OMITTED**; same name/keys/GSIs. **<- DUPLICATE to retire from this root.**

**Latent (not armed) risk:** an `aws_dynamodb_table` with the `point_in_time_recovery` block absent defaults to `enabled=false`. A portal-auth apply does NOT currently diff on PITR (the absent block means the attribute isn't reconciled into portal-auth state -- confirmed by the 0-diff/No-changes plan I captured earlier; this is why I de-escalated my own "armed" inference downward per Rule 22), so PITR is NOT being flipped today. The risk would arm if a future provider version reconciles the absent block, or if anyone adds an explicit `enabled=false`. De-dup removes the latent failure mode permanently.

**Live baseline (read-only, 20260626T1747Z):**
- opal-users-v2: ContinuousBackups=ENABLED, PITR=ENABLED, LatestRestorable current. (Matches survivor config.)

### A.2 Key de-risk finding -- NO data-source ref needed
portal-auth/iam.tf:50-53 references the table by **hardcoded ARN strings** (`arn:aws:dynamodb:us-east-1:${local.account_id}:table/opal-users-v2` + `/index/*`), NOT by `aws_dynamodb_table.opal_users_v2.arn` interpolation. **Removing the resource block from portal-auth breaks no references** -- the IAM grant survives on literal ARNs. So the remediation is a clean block-removal, no data-source/remote-state shim required. (COO's "data-source ref OR remove vestigial block per code-read" -> the code-read resolves to: **remove the vestigial block**, no shim.)

### A.3 Sequence (state-rm FIRST -- mandatory)
A bare block-removal-then-apply would plan to **DESTROY** the physical identity table (catastrophic). The destroy is prevented by removing from state first:

1. **Pre-flight:** `cd infra/aws/terraform/portal-auth` -> `terraform plan` -> confirm opal_users_v2 = 0 add/change/destroy (light-guard baseline) + capture plan output to ledger.
2. **Capture before-state to ledger:** `aws dynamodb describe-continuous-backups --table-name opal-users-v2 --region us-east-1` (expect PITR=ENABLED).
3. **state rm (NON-destructive -- removes from state, leaves physical table untouched):**
   `terraform state rm aws_dynamodb_table.opal_users_v2` (portal-auth root).
4. **Remove the block:** delete portal-auth/dynamodb.tf:167-218 (the `# --- opal-users-v2 ---` comment block + resource). Leave iam.tf hardcoded ARNs intact (still valid).
5. **Prove portal-auth clean:** `terraform plan` -> MUST show **0 add / 0 change / 0 destroy** (block gone + not in state = no-op). This is the 0-destroy proof.
6. **Prove shared-infra clean:** `cd ../shared-infra` -> `terraform plan` -> MUST show opal_users_v2 = 0 add/change/destroy (survivor unaffected; sole manager now).
7. **Apply** (only after both 0-diff proofs + gates): no apply is actually required for the de-dup itself (state rm + block delete leaves both roots at 0-diff). The "apply" here is a confirming no-op plan on both roots. **If any non-zero diff appears, STOP + escalate -- do not apply.**
8. **Capture after-state to ledger:** re-run describe-continuous-backups on opal-users-v2 -> MUST still be PITR=ENABLED (survivor retained the control). Before==After==ENABLED is the success criterion.
9. **Commit:** safe-commit portal-auth/dynamodb.tf (block removal) under deploy-completion ledger.

### A.4 Gates + ledger
- Deploy-completion ledger opened at start, closed at completion (NEVER#6), with before/after `describe-continuous-backups`.
- COO review -> CTO arch-gate (the state-rm is the arch-sensitive step) -> Andrew human-confirm (unrecoverable-class authorization for the state-rm).
- Survivor = shared-infra (PITR-enabled + CI-tracked + import home).

---

## PART B -- opal-users (v1) dead-twin retire

### B.1 Grounded "dead" determination (read + write, 7-day)
- **Reads:** 0 reads / 24h (COO-grounded) vs opal-users-v2's 103 reads -- "dead" is a confirmed metric, not an inference (Rule-22 dead-confirm).
- **Writes (this plan, 20260626T1747Z):** opal-users shows **ZERO** write ops over a full 7-day window -- PutItem/UpdateItem/DeleteItem/BatchWriteItem all emit no datapoints; ConsumedWriteCapacityUnits Sum = **0.0** (2026-06-19 -> 2026-06-26). Confirms caveat-(b): not just zero-READ, zero-WRITE too.
- **Single-managed:** opal_users (v1) is declared ONLY in portal-auth/dynamodb.tf:151-165 -- absent from shared-infra. No double-management; no state-rm-first complication for the de-dup reason (only for the destroy-sequencing reason, see B.3).
- 12 items (per TF comment). Hash key = email, no GSIs. Note: a same-named table also exists in us-east-2 (iam.tf:51) -- this retire scopes us-east-1 ONLY (the imported one); us-east-2 is a separate disposition if it exists.

### B.2 Caveats held (COO 174231Z, all non-negotiable)
- (a) DELETE = unrecoverable -> Andrew human-confirm + an **S3 export snapshot FIRST** (12 items, trivial safety net before drop).
- (b) **Forward write-metric + 7-day window** before recommending drop. The retrospective 7d-zero-write above is strong grounding to START; the plan ALSO arms a forward CloudWatch alarm on any write to opal-users for a 7-day watch -- any write fires -> ABORT the retire + re-investigate. Belt-and-suspenders.
- (c) SEPARATE from v2 de-dup (no contention) -> routed to CVO as a dead-resource retire item.

### B.3 Sequence
1. **Arm forward watch:** CloudWatch alarm on opal-users ConsumedWriteCapacityUnits > 0 (or PutItem/UpdateItem/DeleteItem SampleCount > 0) for a 7-day window. Any trip -> ABORT.
2. **After 7d clean:** export snapshot -> `aws dynamodb scan --table-name opal-users --region us-east-1` to a JSON, `aws s3 cp` to a durable retire-snapshot prefix (e.g. s3://<shared-infra-artifact-bucket>/retired-tables/opal-users/20260...Z.json). Verify 12 items captured.
3. **Andrew human-confirm** the drop (unrecoverable-class).
4. **Drop:** non-destructive-to-state ordering -- because the block is still in portal-auth, a manual table delete would leave terraform wanting to RE-CREATE it on next apply (state has it, live gone). So: `terraform state rm aws_dynamodb_table.opal_users` (portal-auth) FIRST -> then delete the physical table (`aws dynamodb delete-table --table-name opal-users --region us-east-1`) -> remove the block (portal-auth/dynamodb.tf:145-165) -> prune the now-dead ARN lines iam.tf:50-51 (opal-users us-east-1 + us-east-2) -> `terraform plan` 0-diff both effects.
5. **Ledger + commit** under deploy-completion ledger; route the data point to CVO/NFRA_DEBTSCAN.

### B.4 Gates
- COO review -> Andrew human-confirm (drop authorization). No CTO arch-gate strictly required (single-managed, no cross-root state surgery) but CC CTO for visibility. Route to CVO/NFRA_DEBTSCAN.

---

## Sequencing note
Both are DELIBERATE / not-tonight (estate-quiet for the 02:00 proofs). Execute in my window after the proofs clear, COO sequences the gates. v2 de-dup and v1 retire are independent (no shared state, no contention) and can run in either order or in parallel windows. Neither is coupled to the retry-net deploy (separate cot-pipeline change, also tomorrow).
