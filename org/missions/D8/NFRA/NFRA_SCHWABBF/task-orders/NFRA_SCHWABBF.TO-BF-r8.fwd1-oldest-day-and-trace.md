# TO NFRA_SCHWABBF.TO-BF-r8 -- FWD-1: pull the oldest served day of 08403355 through the new writer, let the event path convert it, and trace it

<to_id>NFRA_SCHWABBF.TO-BF-r8</to_id>
<project>NFRA_SCHWABBF</project>
<issued_to>0.7.0_AE_CloudOps~NFRA1</issued_to>
<issued_by>2.0.0_SA_COO~SB</issued_by>
<issued_date>2026-10-20</issued_date>
<status>staged</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>6</round>
<workstream>release-0840</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `BF-r-8` (`decompositions/NFRA_SCHWABBF_DECOMP_R6.md`) | **outcome_ref:** FWD-1, FWD-4, FWD-6 |
**GO:** this order is `staged`. The issuer writes the GO line below and flips it to `pending`; do not act before that flip.

---

## WORKER FACE

### GO

(not yet written. It will read: inside the window; `TO-BF-r5` complete; the issuer's R6 `equal_sample.py compare --form firm` read EQUAL-OK; the Schwab session on the box signed in.)

### THE CELL

`BF-r-8`, release act(s) R8 of the 0840 cutover on all three tiers (bronze, silver, state) of master `08403355` (Tax SMA 0840-3355). Andrew-direct (relayed by the CTO): one cutover, same-day rollback, no side-by-side, the old keys deleted only on his confirmation (act R7, NOT yours, never in this order). The pair that authorizes your acts: the COO half (the release plan, "COO half -- SIGNED") and the CTO half `org/tier1_exec/1.0.0_SA_CTO/deliverables/NEVER_WIDEN_SCHWABBF_R5_0840_ALL_TIERS_CTO_HALF_20261020.md` @e7d8af9d1c (msg 110003, covers R0-R6 and R8). Fence rows: COO half `org/missions/D8/NFRA/NFRA_SCHWABBF/ledger/NEVER_WIDEN_BF5_STATE_FENCE_COO_HALF.md`, CTO half `org/tier1_exec/1.0.0_SA_CTO/deliverables/NEVER_WIDEN_BF5_STATE_FENCE_CTO_HALF.md` @4b0036c6cb. Read first: the release plan `org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/2.0.0_SA_COO~SB/RELEASE_PLAN_R5_0840_ALL_TIERS.md` (sections 1-6), the decomposition `org/missions/D8/NFRA/NFRA_SCHWABBF/decompositions/NFRA_SCHWABBF_DECOMP_R6.md`, the CTO half `org/tier1_exec/1.0.0_SA_CTO/deliverables/NEVER_WIDEN_SCHWABBF_R5_0840_ALL_TIERS_CTO_HALF_20261020.md` (its four conditions bind you), and the `/cloud-ops` skill (safe-apply, the ledger, the identity rules). The AWS CLI is `.tools/aws`.

### DO, IN ORDER

1. Work from a worktree at the pushed pin. Day `D` = `2023-10-17` (the served floor measured for the brief). Precheck over SSM (read only): `quser` shows an administrator session, `C:/schwab-sdd/sdd-daily-pull.ps1` is the file uploaded by `BF-r-5` (compare its md5 with the repo file), and no other pull task is running (the session lock).
2. Run the pull as the one-shot Administrator scheduled task pattern of the box's schedule (read `infra/aws/terraform/canonical-schwab-ec2/monolith-daily-schedule.tf`, the `commands` list, and copy its register, start-proof, wait and exit-code lines; write the SSM JSON with a non-shell writer and forward slashes): `powershell.exe -NoProfile -ExecutionPolicy Bypass -File C:/schwab-sdd/sdd-daily-pull.ps1 -Master 08403355 -Target monolith -OnlyAsOf 2023-10-17 -LookbackDays 1200`. Print the log tail (`Get-Content C:/schwab-sdd/daily/08403355/daily-pull.log -Tail 40`) and the exit code. It must end `DAILY PULL OK`. Exit 9 means the served window holds no file for that day (the floor moved or a non-business day): report the exit, do not retry with another window or day. One day only; never chunk the window.
3. LANDED READ from the laptop: `list-objects-v2` on `s3://opal-data-assets/schwab/49financial/bronze/` for keys containing `/date=2023-10-17/08403355.`: print the count and 3 sample keys beside `python -c "import sys; sys.path.insert(0,'lib'); import opal_naming as o; print(o.address('schwab','49financial','bronze','acc','date=2023-10-17'))"`; every key must equal that address plus `/` plus the vendor file name. Wait for the converter (poll the schwab function's `Invocations` and the DLQ every 2 minutes up to 20 minutes), then read the silver key `schwab/49financial/silver/<table>/date=2023-10-17/08403355.parquet` for the day's tables and the state marker `s3://opal-data-49financial/schwab/49financial/state/complete/date=2023-10-17/08403355.complete.json` (print `head-object` of each).
4. `python data/canonical/schwab/keyform/thread_trace.py --master 08403355 --day 2023-10-17 --form builder` from the worktree; print and save its output. It must read `THREAD-OK`; the bronze, silver and state hops must read held and `HOP second-form` must read NONE or name the old keys (R7 is still held, so old keys of OTHER days exist: say what it prints).
5. Save everything under `org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.7.0_AE_CloudOps~NFRA1/r8/`, commit paths-only, report. Leave the Administrator session signed in. Do not pull another day: the 0840 backfill to the floor (FWD-2) is a later round.
ROLLBACK: one new partition per tier; nothing is deleted without Andrew's word.

### ACCEPTANCE (read by the issuer from your committed files)

<criterion id="BF6-r8-AC1" cell_refs="BF-r-8"><invocation>python .tools/proof-of-spec-check.py org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.7.0_AE_CloudOps~NFRA1/NFRA_SCHWABBF.TO-BF-r8.fwd1-oldest-day-and-trace.proof_of_spec.json BF6-r8-AC1</invocation><expect>VALID</expect></criterion>
`BF6-r8-AC1` -- one day of 08403355 (2023-10-17) was pulled by the new puller, landed at the builder's bronze address, converted by the event path to silver and state at the builder's addresses, and the trace reads THREAD-OK.

<expected_criteria>BF6-r8-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus this order's file.
- **Never:** `terraform apply` outside `safe-apply`; any apply, copy or write outside the legs this order names; deleting an S3 object or version; touching `08242234`, `08335338` or any other master's keys or grants; reading or printing a Schwab token or any secret value; a second concurrent Schwab session; enabling or editing an EventBridge rule; stopping an instance.
- **Window.** The CTO's window is 2026-10-21 12:00-20:00Z. Outside it you do nothing in this order except what its GO line allows. Any failure rolls back that order's legs in the same window (rollback per step below) and is reported at once.
- **Refusal clause.** If a step cannot be met as written, stop, write the reason and the output in your report and a surprise row (id `NFRA_SCHWABBF-R3-S<k>`; read the investigation file for the highest `R3-S<k>` and use the next; the gate may renumber it), commit the row AT ONCE with `safe-commit.sh` paths-only and tell the issuer its hash, and do not improvise. Append the row at the BYTE level (the file mixes CRLF and LF: do not use an editor that rewrites line endings).

<paths>
org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.7.0_AE_CloudOps~NFRA1/
org/missions/D8/NFRA/NFRA_SCHWABBF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_SCHWABBF/decompositions/NFRA_SCHWABBF_DECOMP_R6.md</decomp_doc> (round 6), cell `BF-r-8`.
<owned_cells>BF-r-8</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion id: BF6-r8-AC1. Instance at `org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.7.0_AE_CloudOps~NFRA1/NFRA_SCHWABBF.TO-BF-r8.fwd1-oldest-day-and-trace.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> BF6-r8-AC1` BEFORE the flip. The instance records, as artifact rows, every printed output the steps ask for.
</proof_of_spec>

**REPORT (your final message and a message to `2.0.0_SA_COO~SB`):** the pull log tail and exit code, the landed counts and sample keys beside the address call, the converter and DLQ readings, the head-objects, the trace output, any row id.

---

## RECORD FACE

<preflight>
comp-schedule: RUN by reading -- the pull fires are 09:45, 10:15, 10:45, 21:45, 22:15, 22:45Z; the window 12:00-20:00Z sits between the 10:45 and 21:45 fires; CTO condition: no pull fire between R4c and R5; BLIND: the live EventBridge rules (read at step 1 of `BF-r-1`).
comp-iam: RUN -- no grant is added; the box role writes bronze to the monolith and the run records to the firm bucket (BF-r-3); BLIND: the live IAM plane.
comp-adversary: DECLARED-NOT-APPLICABLE as a lens run; findings inlined in the steps -- (1) an Administrator scheduled task is required because an SSM command runs as SYSTEM, whose credential vault is empty; (2) the Schwab session is single: no second concurrent pull; (3) a day with no file exits 9 by design.
lane: the <paths> block IS the grant; CloudOps seats act on infrastructure under a task order (rule 34).
</preflight>

Source: PRD v1.0 C-TIERS, C-MOVE, C-DAILY; the release plan; the CTO half @e7d8af9d1c; decomposition round 6 cell BF-r-8.
