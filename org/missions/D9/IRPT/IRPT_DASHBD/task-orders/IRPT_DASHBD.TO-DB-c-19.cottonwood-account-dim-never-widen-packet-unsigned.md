# TO IRPT_DASHBD.TO-DB-c-19 -- the Cottonwood `account_dim` NEVER-WIDEN PACKET (unsigned): the change set, the catch-up first with its read-ABSENT, the one key written, both branches, the rollback per key, the questions for the CTO's half; read-only measurements; nothing is created, planned, applied, built, uploaded or written to S3

<to_id>IRPT_DASHBD.TO-DB-c-19</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~412</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>124</round>
<workstream>B-CW</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO's decision C (msg 8167: "The pair carries both branches. No delete. Cut the build cell and the packet; I sign the CTO half.") | **Rows:** IRPT_DASHBD-D2-W412-S<k> | **Decomp cell:** `DB-c-19` (`org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_B-CW.md` section 11) | **outcome_ref:** FWD-2 | **depends_on:** none (`DB-c-17` merged @f54c662ab0 and `DB-c-18` merged @a5929fb06e).

---

## WORKER FACE

Your workspace worktree is the absolute path your prompt names (branch `wk-IRPT_DASHBD-412`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~412/`. Never push. No client value is written anywhere (counts, dates, hashes and words only). **You make read-only AWS calls through python `boto3` and nothing else:** S3 `list_objects_v2` on the prefixes named below, `lambda.get_function`, `iam.get_role`, `scheduler.get_schedule`, `logs.describe_log_groups`. No put, delete, create, invoke, update, assume-role or secret read; no Terraform, no build, no upload. Region `us-east-1`. A read that is refused is recorded as refused (its words), never worked around.

**Why.** The Cottonwood `account_dim` producer is built in the repo (code `DB-c-16`, package entry `DB-c-17`, Terraform root `DB-c-18`) and nothing of it exists in AWS. Creating it and writing its first partition is a WORLD act that needs the never-widen pair: the CTO's half and the issuer's half signed over the SAME packet blob. You write the UNSIGNED packet that both halves will sign. Model its structure and rigor on the earlier packet `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~403/NEVER_WIDEN_PACKET_DB-c-5_R115.md` (read it first, whole); this packet is for a different table and function, so copy its section order and its discipline, not its content.

**The facts you build from (read them in the repo at your base; do not retype a name):**
- The Terraform root `infra/aws/terraform/investor-reporting/account-dim/` (read its five files): the function module, the execution role and its single inline policy, the scheduler role and policy, the schedule created `DISABLED` with `cron(45 8 ? * MON-FRI *)` in `America/New_York`.
- The source-map entry `irpt-cot-account-dim-lambda` in `infra/aws/lambda/ci/lambda-source-map.json` (15 files, 14 staged rows) and its test `infra/aws/lambda/investor-reporting/account-dim-cot/tests/test_package_resolves.py` (it accepts `ADCOT_ZIP_PATH=<built zip>` to run on the real artifact).
- The Lambda `infra/aws/lambda/investor-reporting/account-dim-cot/lambda_function.py` and the adapter `data/assets/scripts/gold/irpt_reporting/adapters/cottonwood_account_dim.py`: the handler reads the two Black Diamond silver partitions `fact_holdings` and `fact_allocations` for one day, lists its own gold partition, refuses to write when it is non-empty (returns `TARGET_ALREADY_LANDED`), and writes exactly ONE key: `data.parquet` under `address("irpt", <firm>, "gold", "account_dim", "date=<D>")`. An event `{"date": "<D>"}` names the day; with no date it computes the T-1 trading day itself.
- The names are builder output (`lib/opal_naming.py name()` with scope `cottonwood`, function `account-dim`): the function `irpt-cot-account-dim-lambda`, the role `irpt-cot-account-dim-role`, the policy `irpt-cot-account-dim-policy`, the scheduler role `irpt-cot-account-dim-scheduler-role`, the scheduler policy `irpt-cot-account-dim-scheduler-policy`, the schedule `irpt-cot-account-dim-daily`. Confirm each by calling the builder.

**The cell (`DB-c-19`).** Write ONE file, `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~412/NEVER_WIDEN_PACKET_DB-c-19_R123_ACCOUNT_DIM.md`, and ONE record `.../ACCOUNT_DIM_PACKET_READS_R123.json`.
1. **The reads (the record).** The JSON record carries, with the UTC time of each read: (a) `silver`: for each of `fact_holdings` and `fact_allocations` under the Black Diamond silver prefix (take the bucket and prefix the way `lambda_function.py` `silver_locations()` does, by calling it from the repo: it needs no AWS), the count of date partitions, the oldest and newest date, and the newest date present in BOTH (`common_newest`); (b) `gold_account_dim`: a fresh LIST of the whole `account_dim` gold prefix (the adapter's `gold_address` with the partition tail cut) with `object_count` (it must read 0 for the read to be ABSENT; if it is not 0 record every key's name and size and stop: the packet then says the catch-up is not a first write); (c) `exists`: for each of the function, the role, the scheduler role and the schedule, the result of the matching `get_*` call as `ABSENT` (the not-found error code is recorded) or `EXISTS` (then record only its name and state); a refused call is `REFUSED` with the error code; (d) `log_group`: `describe_log_groups` with the function's log-group prefix, count of matches; (e) `reads` counters: `s3_list_calls`, `get_calls`, and `writes` = 0; (f) `claim` = `measured` and `pushed` = false, `deployed` = false. No client value, no account id.
2. **The packet** has these sections, in this order, with exactly these headings: the title line, then a `Status: UNSIGNED.` paragraph (it applies nothing; both halves sign over the blob before any act), then `## Change set`, `## Function`, `## Catch-up first`, `## Keys written`, `## Both branches`, `## Rollback`, `## Questions for the CTO's half`, `## Not in this packet`. Content:
   - **Change set**: the names above (as output of the builder), the resources the Terraform root creates (each by its Terraform address and name, the role's closed set of actions and the exact prefixes they cover, derived from the files, not from this order), the schedule's expression, zone and the state at creation `DISABLED`, and that it is enabled only after the after-read by a one-line change; the package step: the artifact is built by `BUILD_ONLY=1 bash infra/aws/lambda/ci/build-and-upload.sh investor-reporting irpt-cot-account-dim-lambda` (no upload), the package test run on that zip with `ADCOT_ZIP_PATH`, and only then the real build-and-upload (which writes ONE new object, `investor-reporting/irpt-cot-account-dim-lambda.zip`, in the lambda-artifacts bucket, and records the sha256 in the source map); name that object as a write of the act.
   - **Function**: mode BUILD or ADOPT from the record (`exists`); what the handler does and refuses (above); the event.
   - **Catch-up first**: the ordered acts: both halves signed; the ledger entry opened (`deploy_ledger.py`, NEVER-2) before the first write; the build and package test; `safe-apply` of the new root creating the resources with the schedule DISABLED; ONE invoke with the event `{"date": "<D>"}` where `<D>` is the packet's pinned date; the AFTER-READ (a fresh LIST of the `account_dim` gold prefix shows exactly one key, `date=<D>/data.parquet`, and nothing else moved; the object's size and ETag recorded; the parquet read back for its row count and its schema hash against `org/standards/IRPT_DASHBD_ACCOUNT_DIM_CONTRACT.json`); only then the schedule is enabled by the one-line change and applied; the ledger left open for the first scheduled fire.
   - **Keys written**: the pinned date `<D>` = the `common_newest` of your read; the ONE key (its `address()` output, full URI); the pre-run state ABSENT with the fresh LIST (the record). State that the scheduled fires after enabling write one new key per trading day, each a new key under the same rule, and that a re-fire on a landed day writes nothing. State that NO other prefix is read or written beyond the two silver inputs, the function's own gold prefix, the artifact object and the Terraform state.
   - **Both branches**: success (the gold gains one partition; who reads it: say what you can establish from the repo about consumers of the `account_dim` table and mark the rest NOT ESTABLISHED); the invoke fails or the silver of `<D>` is absent (the handler raises, writes nothing, the resources stay, the schedule stays DISABLED); a partial state is impossible for the table (one key) but name the partial states of the ACT (resources created, no key; key written, schedule not enabled) and what the applier does in each.
   - **Rollback**: per key (an S3 delete of the one key restores absence; a delete needs Andrew's word and this packet does not authorise it), the schedule (set DISABLED or remove in a reviewed plan), the function and roles (remove in a reviewed plan), the artifact object (a delete, Andrew's word), the Terraform state (the root's own); no step reads or writes the silver.
   - **Questions for the CTO's half**: the applying seat and AE lane; the pinned date versus the history question (does any consumer need `account_dim` for earlier dates; the default of this packet is ONE partition now and none earlier); the bucket policy of the gold bucket (the deny fence admits `*-cot-*` roles: the new role matches; the packet did not read the bucket policy); the time of the schedule against the silver landing (08:45 New York against about 11:46 UTC) and against the other fires; the artifact upload as a write; the rollback deletes (Andrew's word); both halves sign over the same blob.
   - **Not in this packet**: what you did not read (bucket policies, the live state of IAM beyond the `get_role` result, consumers beyond the repo, whether the invoke would succeed: not run).
3. **Do NOT**: create, invoke, update, plan or apply anything; write to S3 or any AWS service; edit any file outside your folder, the channel and your order; sign either half; put a signature, an approval or the word `SIGNED` as a state anywhere in the packet.

<criterion id="DBC124-1-AC1" cell_refs="DB-c-19"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~C2/checks/r124/p124_bcw.py" . DBC124-1-AC1</invocation><expect>DBC124-1-AC1 PASS</expect></criterion>
`DBC124-1-AC1` -- the record and the packet agree with a FRESH read made by the checker: the record's `gold_account_dim.object_count` equals a fresh LIST (0), the pinned date is a partition of BOTH silver tables in a fresh LIST, the six names equal builder output, the key equals `address()` output, and the packet carries its title line and the eight `##` headings in order, the word `UNSIGNED`, no signature state and no write counter above 0. Base: FAIL.

<criterion id="DBC124-2-AC1" cell_refs="DB-c-19"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~C2/checks/r124/p124_bcw.py" . DBC124-2-AC1</invocation><expect>DBC124-2-AC1 PASS</expect></criterion>
`DBC124-2-AC1` -- the bounds: the only files changed since the base are the packet, the record, the worker's other records in its folder, the channel and the order; the packet blob hash (`git hash-object`) is printed; no `.tf`, source-map, Lambda or adapter file changed. Base: FAIL (no packet).

<expected_criteria>DBC124-1-AC1, DBC124-2-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited, including the checkers, every Terraform file, the source map, the Lambda and the adapter.
- **Reads and writes.** Reads: repo files, `git show`, and the read-only AWS calls named in the first paragraph. Writes: the files in `<paths>`. No AWS write of any kind, no Terraform, no invoke, no deploy, no push, no vendor call, no secret read.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. A silver partition that is absent, a gold prefix that is not empty or a refused read is a finding in the packet and a row, never a guess.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W412-S<k>`, with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~412/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-c-19.cottonwood-account-dim-never-widen-packet-unsigned.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_B-CW.md</decomp_doc> section 11, cell `DB-c-19`.
<owned_cells>DB-c-19</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBC124-1-AC1, DBC124-2-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~412/IRPT_DASHBD.TO-DB-c-19.cottonwood-account-dim-never-widen-packet-unsigned.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DBC124-1-AC1,DBC124-2-AC1` BEFORE the flip (set the order's status to complete only when both criteria PASS); pin each artifact row to the commit that carried it.
</proof_of_spec>

**REPORT:** your final message, once: the two criteria's last lines; the packet's blob hash; the record's `common_newest`, `object_count` and the four `exists` results; the eight headings present; row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: read-only measurements and a record; nothing is created, planned, applied or written to S3. The blast of the later act is what the packet bounds for the CTO's half.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: only read calls (list, get, describe); no grant is made or changed.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: the worker reads whether the schedule exists; none is created or changed.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; the checker re-reads the S3 plane itself and compares.
</preflight>
