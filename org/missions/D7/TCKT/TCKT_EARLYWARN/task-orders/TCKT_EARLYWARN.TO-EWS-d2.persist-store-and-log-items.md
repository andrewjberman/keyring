# TO TCKT_EARLYWARN.TO-EWS-d2 -- the container logs items opened per rule each pass and keeps its open-items store on ONE S3 prefix (fast-path)
<to_id>TCKT_EARLYWARN.TO-EWS-d2</to_id>
<project>TCKT_EARLYWARN</project>
<issued_to>0.7.0_AE_CloudOps~TM1</issued_to>
<issued_by>2.0.0_SA_COO~Q1</issued_by>
<issued_date>2026-10-17</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
**AMENDED by the issuer 2.0.0_SA_COO~Q1, 2026-10-17 ~09:3xZ (row TCKT_EARLYWARN-D1-S7, `0.7.0_AE_CloudOps~TM1`):** the builder's address for the store is in `opal-data-49financial`, whose `DenyForeignFirmPrincipals` fence does not admit the role. The issuer recommends option (A), the fence admission, and the COO half is signed conditionally at `org/missions/D7/TCKT/TCKT_EARLYWARN/ledger/NEVER_WIDEN_EWS_D2_STORE_FENCE_COO_HALF.md`. **You apply NOTHING until `ledger/NEVER_WIDEN_EWS_D2_STORE_FENCE_CTO_HALF.md` exists at HEAD** (the CTO's half; if he rules (B) instead, it is an R20 deviation for Andrew and the order is re-cut). When it exists: append ONE row to `infra/logic/registry/exemptions.json` under `opal-data-49financial` exactly as the COO half names it (principal, arn, actions GetObject/ListBucket/PutObject, `prefix` `schwab/49financial/state/ews_store/current/`, `signoff_ref` the two halves), run the shared-infra plan (it must show ONLY that one added principal in the generated fence), then `safe-apply`. No file of `infra/aws/terraform/shared-infra/` is yours to edit; the fence is generated from the row. AC1 simulates the identity policy and ignores the bucket policy, so AC3 (the object exists) is the real grade. Keep building the launcher work, which is independent of the bucket.
**Directive:** D7 | **Fabric:** dell1 (placement dell1) | **Decomp cell:** `EWS-d-2` (`decompositions/TCKT_EARLYWARN_DECOMP.md`; FAST-PATH) |
**outcome_ref:** the CTO's exercised read of `TO-EWS-d1`, `1.0.0_SA_CTO~DELL1` msg 7455 (PARTIAL): "NOT READ: any rule's output. The log carries no items-opened line, and the store is SQLite inside the container ... RISK: a restart loses the store and replays for 3.5 hours. Next cell: log items opened per rule each run, and persist the store to one S3 prefix (role widened to that prefix only)." | **depends_on:** `TO-EWS-d1` (complete)

---

## WORKER FACE

### THE CELL

`TO-EWS-d1` deployed the always-on container (`opal-clientops-ews-task`, taskdef :2). It runs the Schwab daily rules from a launcher written inside `infra/aws/ec2/client-ops-early-warning/Dockerfile`. Its first pass processed 573 dates in 3h32m (log line `ews-launcher: run_pending dates_processed=573 last_processed=2026-10-15` at 08:56:40Z). Two gaps remain, and **this cell closes both, in the launcher and the role only; the `ews/` package is not yours to change.**

1. **Items opened per rule.** After each `run_pending()` pass the launcher logs, for each of the three Schwab rules, one line `ews-launcher: items_opened rule=<name> n=<int>`: the number of items that rule OPENED during that pass (count the store's OPENED events of the pass per rule; `SqliteStore.events()` and `.open_items()` in `ews/store.py`), plus the rule's open count is allowed on the same line as `open=<int>`. Counts only: no client row, id, amount or account number in any log line. A pass that processed no dates still logs the three lines with `n=0`. The latest pass line must be followed by the three rule lines before the next pass line.
2. **The store survives a restart.** Keep the store on ONE S3 prefix: at launch, before the `SqliteStore` opens, fetch the object if it exists into `EWS_STORE_PATH`; after every pass that processed at least one date, write a consistent copy (the `sqlite3` backup API into a temp file, never a copy of a live file) and `put_object` it to the same key; log `ews-launcher: store_persisted bytes=<int>` or, on failure, `ews-launcher: store_persist failed type=<ExceptionName>` (a failed persist is retried next tick and never stops the loop). A restart then resumes at `last_processed`, not at the first complete date.

### Requirements (each is a rule)

1. **The prefix comes from the builder.** The bucket, prefix and key are `lib/opal_naming.py address()` output (CLAUDE.md rule 30); a builder REFUSAL is a missing registry row to add under `infra/logic/registry/`, never a hand-typed address. Print the address you used in the report. The bucket is one of the account's private buckets, and nothing under the prefix is public.
2. **The role widens to that prefix and nothing else:** `s3:GetObject` and `s3:PutObject` on the one object key (or the one prefix), `s3:ListBucket` on the bucket conditioned on that prefix. NO `s3:DeleteObject`, no other S3 write, and the existing grants stay exactly as `TO-EWS-d1` left them (the cert secret, the two Schwab silver read prefixes). Nothing sends.
3. **Apply** through `safe-apply`; open a NEVER-2 ledger entry first and close it at completion (sentinel committed). Rebuild the image through the existing CodeBuild project; the new task replaces the old by the existing service.
4. **State the one-time cost before you apply.** The replacement task starts with no persisted store, so its first pass replays all 573 dates again (about 3.5 hours at 0.25 vCPU); the store is uploaded when that pass ends. Do NOT resize the task (CTO msg 7416: Andrew approved about $10-15 a month). The old task keeps running until the new one is up.
5. **Extend the manifest** `org/tier1_exec/0.7.0_AE_CloudOps~TM1/deliverables/EWS_DEPLOY.json` with `persist_bucket` and `persist_key`; keep the six existing keys.
6. Do not widen the secret scope, add a mail poller, or send anything.

### ACCEPTANCE

<criterion id="EWS-d2-AC1" cell_refs="EWS-d-2"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/TCKT_EARLYWARN_Q1/EWS_CHECKS/ews_check.py persist-iam</invocation><expect>EWS-PIAM-OK</expect></criterion>
<criterion id="EWS-d2-AC2" cell_refs="EWS-d-2"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/TCKT_EARLYWARN_Q1/EWS_CHECKS/ews_check.py counts</invocation><expect>EWS-CNT-OK</expect></criterion>
<criterion id="EWS-d2-AC3" cell_refs="EWS-d-2"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/TCKT_EARLYWARN_Q1/EWS_CHECKS/ews_check.py persist-object</invocation><expect>EWS-POBJ-OK</expect></criterion>

<expected_criteria>EWS-d2-AC1,EWS-d2-AC2,EWS-d2-AC3</expected_criteria>

`EWS-d2-AC1` -- the role, SIMULATED, may Get and Put the manifest's store key, and may not Delete it nor Put on a sibling prefix of the same bucket. `EWS-d2-AC2` -- in the container log the latest `run_pending` pass line is followed by an `items_opened rule=<name> n=<int>` line for each of three distinct rules. `EWS-d2-AC3` -- the store object exists and is non-empty; this arm is DATE-GATED to the end of the replacement task's first pass (about 3.5 hours after the apply), and the order stays open until it reads EWS-POBJ-OK. Run each from the repository root. The three earlier arms of `ews_check.py` (`running`, `iam`, `ledger`) must still read OK after your apply; run them too and report. At the base: `EWS-BAD the deploy manifest lacks the key 'persist_bucket'` (AC1, AC3) and `EWS-BAD after the latest pass line, 0 distinct items_opened rule line(s), wanted 3` (AC2).

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- Reads: the two Schwab silver prefixes (unchanged). Writes: the one store prefix. No other S3 write, no delete, no send, no change to `ews/`, no resize, no `terraform apply` outside `safe-apply`, no rebase of a shared branch.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id `TCKT_EARLYWARN-D2-W1-S<k>`, `surfaced_at` = `date -u +%FT%TZ`, class `OBSERVATION` or `BLOCKING`) appended to the investigation file below, and do not weaken a check. Rows are APPEND-ONLY.

<paths>
infra/aws/terraform/client-ops-early-warning/
infra/aws/ec2/client-ops-early-warning/Dockerfile
infra/logic/registry/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/tier1_exec/0.7.0_AE_CloudOps~TM1/deliverables/
org/missions/D7/TCKT/TCKT_EARLYWARN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D7/TCKT/TCKT_EARLYWARN/decompositions/TCKT_EARLYWARN_DECOMP.md</decomp_doc> (FAST-PATH: the declaration file), cell `EWS-d-2`.
<owned_cells>EWS-d-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: EWS-d2-AC1, EWS-d2-AC2, EWS-d2-AC3. Instance at `org/missions/D7/TCKT/TCKT_EARLYWARN/deliverables/0.7.0_AE_CloudOps~TM1/TCKT_EARLYWARN.TO-EWS-d2.persist-store-and-log-items.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> EWS-d2-AC1,EWS-d2-AC2,EWS-d2-AC3` BEFORE the flip. Write it in your own deliverables folder (lane TREE_DELIVERABLES admits only the serial named by the sub-folder).
</proof_of_spec>

**REPORT:** the address you used, the one-time replay cost and when you applied, the three criteria's output (AC3 after the first pass of the new task), the four arms of the earlier checks, the ledger entry, the manifest, commits and push state.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE the loop keeps its own 15-minute clock; no EventBridge or Windows schedule is created.
comp-iam: RUN the role gains one S3 prefix; AC1 simulates it, and the lane runs comp-iam on the role after the apply.
comp-adversary: DECLARED-NOT-APPLICABLE graded by a read-only policy simulation, a log read and an object head.
risk: WORLD -- the container gains a write grant (one S3 prefix) on an account bucket; the object holds the open-items store of client-ops findings, no mail content.
direct_act: false -- a seat order to the TCKT CloudOps lane, rule 34.
</preflight>

Source: `1.0.0_SA_CTO~DELL1` exercised read of `TO-EWS-d1` (msg 7455) and its no-resize ruling (msg 7416); the replay evidence is the log line quoted above.
