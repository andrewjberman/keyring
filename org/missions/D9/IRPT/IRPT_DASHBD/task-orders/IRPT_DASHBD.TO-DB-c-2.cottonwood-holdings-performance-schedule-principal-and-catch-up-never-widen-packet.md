# TO IRPT_DASHBD.TO-DB-c-2 -- the NEVER-WIDEN PACKET for the Cottonwood `holdings_performance_daily` SCHEDULE, its PRINCIPAL and the CATCH-UP run: builder names, the catch-up keys counted, both branches, rollback per key, the CTO's questions; a packet; nothing is applied

<to_id>IRPT_DASHBD.TO-DB-c-2</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~401</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>114</round>
<workstream>B-CW</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** `1.0.0_SA_CTO~DELL2`, ruling `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_DELL2_IRPT_DASHBD_FOUR_WORKSTREAMS_AT_ROUND_114_20261015.md` (B-CW is this workstream) | **Rows:** IRPT_DASHBD-D2-W401-S<k> | **Decomp cell:** `DB-c-2` (`org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_B-CW.md` section 1) | **outcome_ref:** FWD-2, FWD-11 | **depends_on:** `DB-c-1` (this worker's previous order; its record `LANDING_AND_FRONTIER_R114.json` is your input, and the order is handed to you only after it is terminal).

---

## WORKER FACE

Your workspace worktree and folder are those of your previous order (`deliverables/0.9.0_WK_IRPT_DASHBD~401/`). Never push. Counts, dates, names, keys and words only in the repo, a row or your report; an account number, a client or household id, a name or a figure is never recorded. Every S3 read is from a short Python script (boto3, LIST and HEAD only) kept in your private folder.

**Why.** The Cottonwood `holdings_performance_daily` producer has no schedule, no principal, and a backlog of dates with an input and no gold (`DB-c-1`). A fire writes served gold that the portal path reads, so creating the schedule and running the catch-up are LATER acts under a never-widen pair (CLAUDE.md section 5; `deliverables/0.9.0_WK_IRPT_DASHBD~178/RD_COTTONWOOD_PRODUCER_R110.json`, `scheduled_fire_needs`). This cell writes the packet the CTO's half and the issuer's half sign; it applies nothing.

**The cell (`DB-c-2`).**
1. **Inputs.** Read your `LANDING_AND_FRONTIER_R114.json` (the catch-up dates, the proposed fire time and its basis) and `deliverables/0.9.0_WK_IRPT_DASHBD~178/RD_COTTONWOOD_PRODUCER_R110.json`. Read the 49 Financial model: `infra/aws/terraform/investor-reporting/holdings-performance/schedule.tf` and `iam.tf`, the handler `infra/aws/lambda/investor-reporting/holdings-performance/handler.py`, the declaration `data/assets/scripts/gold/irpt_holdings_performance/sources.json`, and the model packet `deliverables/0.9.0_WK_IRPT_DASHBD~166/COTTONWOOD_RESUME_PACKET.md` (its shape is the model).
2. **Names.** The schedule's name is `lib/opal_naming.py name("irpt","cottonwood","holdings-performance","daily")`; the principal's name comes from `name(...)` with the kind you judge right for a role (try the kinds the schema lists; the builder refuses a wrong kind). Record the exact arguments you used (`schedule_builder_args`, `principal_builder_args`) and the builder's output. A builder REFUSAL is recorded as the refusal text (`<key>_builder_refusal`) with the name `null` and is a missing registry row to add (`infra/logic/registry/`), never a hand-typed name.
3. **Keys.** The catch-up run writes, per catch-up date `D`: `address("irpt","cottonwood","gold","holdings_performance_daily","date=D","data.parquet")`, and `address("irpt","cottonwood","gold","holdings_performance_manifest","date=D","data.parquet")` and `...,"manifest.json")`. Record all of them in order in `keys_written.keys` (3 per date), `keys_written.dates` (the catch-up dates), `keys_written.count`.
4. **Packet** `NEVER_WIDEN_PACKET_DB-c-2_R114.md` (4,000 characters or more) with these `## ` headings, in this order: `## Change set` (the schedule's Terraform entry in words and a code block of the desired entry modelled on the 49 Financial one, the trigger input naming source `blackdiamond_z09`, the proposed time from `DB-c-1`, the principal with the exact prefixes it reads and writes, the catch-up run's command; every name from the builder); `## Keys written` (the count, the dates, the three objects per date, the keys that move and the statement that no other key moves, and whether any key already exists, from a fresh LIST); `## Both branches` (what is served and what the portal path reads if the run succeeds; what it reads if the run fails midway: which dates exist, which do not); `## Rollback` (per key: what deletes it and what that restores; the rollback of the schedule and the principal); `## Questions for the CTO's half` (at least: the proposed time against the 6 AM ET fold and `~P2`; the principal's identity and grants; whether the early silver date with no gold is expected; who applies, which AE instance; that the pair is signed before any apply); `## Not in this packet` (what you did not establish). The packet states it is UNSIGNED and carries no signature.
5. **Facts record** `PACKET_FACTS_R114.json` with exactly: `claim` ("measured"); `schedule_name`, `schedule_builder_args`, `schedule_builder_refusal` (empty string when the builder returned); `principal_name`, `principal_builder_args`, `principal_builder_refusal`; `keys_written` {`dates`, `keys`, `count`}; `reads` {`vendor_calls` 0, `s3_writes` 0, `dynamodb_writes` 0, `secret_reads` 0, `aws_writes` 0, `terraform_apply` 0}; `pushed` false; `deployed` false.

<criterion id="DBC114-2-AC1" cell_refs="DB-c-2"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~C2/checks/r114/p114_bcw.py" . DBC114-2-AC1</invocation><expect>DBC114-2-AC1 PASS</expect></criterion>
`DBC114-2-AC1` -- the facts record is complete; the schedule and principal names equal a fresh call of the builder with the recorded arguments (or the recorded refusal equals the builder's); the key dates equal `DB-c-1`'s catch-up set and the keys equal the builder's addresses, three per date; no catch-up date already has a gold partition; the packet holds all six headings, is 4,000 characters or more and claims no signature; no write is recorded. Base: FAIL (no record).

<expected_criteria>DBC114-2-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited, including the checker, every contract, every Terraform file and every IAM file: the desired entry is TEXT in the packet.
- **Reads and writes.** Reads: repo files; S3 LIST and HEAD under the Cottonwood gold prefixes in `opal-data-cottonwood` and the Black Diamond silver prefix named in `DB-c-1`. Writes: the packet and the facts record in your folder. No write to AWS, no Terraform plan or apply, no deploy, no push, no vendor call, no secret read.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. A section you cannot fill is written as "not established" with the reason.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W401-S<k>`, with the real current UTC time; append as BYTES. Commit with `.tools/safe-commit.sh`. ASCII only.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~401/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-c-2.cottonwood-holdings-performance-schedule-principal-and-catch-up-never-widen-packet.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_B-CW.md</decomp_doc> section 1, cell `DB-c-2`.
<owned_cells>DB-c-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBC114-2-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~401/IRPT_DASHBD.TO-DB-c-2.cottonwood-holdings-performance-schedule-principal-and-catch-up-never-widen-packet.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DBC114-2-AC1` BEFORE the flip; pin each artifact row to the commit that carried it.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; the two names (or refusals); the catch-up count and keys; whether any key already exists; the packet's length; the number of S3 reads; row ids. No account number, client or household id, name or figure.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a packet; no resource is changed, wired or deleted.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: the principal is described in text; no grant is created. The CTO's half reads the described grants.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: the order DESCRIBES a schedule; none is created or changed.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; DBC114-2-AC1 FAILS at base (no record) and its builder-recompute arms are exercised on the worker's record.
</preflight>
