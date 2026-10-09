# TO IRPT_BCKEND.TO-IB-pr-395 -- the _authz served.py release (IB-pr-390: 385 + 387 + ALL never admits) applied on 6 of 8 hosts

<to_id>IRPT_BCKEND.TO-IB-pr-395</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.7.0_AE_CloudOps~IB2</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>100</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:**
- Andrew-direct, relayed by ~V2 msg 2536: release now, standalone, not behind IB-pr-383;
- the pair:
  - packet `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~201/NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-390.md` (blob be15b61188);
  - COO half `deliverables/2.0.0_SA_COO~P2/NEVER_WIDEN_IB_pr_390_AUTHZ_SERVED_RELEASE_COO_HALF.md` @567612e686;
  - CTO half `deliverables/1.0.0_SA_CTO~DELL2/NEVER_WIDEN_IB_pr_390_AUTHZ_SERVED_RELEASE_CTO_HALF.md` @b97ebb6b98 (msg 2726, with conditions);
- the lane: `0.7.0_AE_CloudOps~IB2`, seated by MSTR~DELL2 (msg 2725), IRPT_BCKEND only.

**Decomp cell:** `IB-pr-395` (decomposition section 93) | **outcome_ref:** FWD-2; it gates IRPT_ANLREQ FWD-1's one-firm seat run |
**depends_on:** IB-pr-390 (complete, drained).

---

## WORKER FACE

Work in your own worktree cut from `box/dell2`. The packet is your procedure. Read it IN FULL, then both halves; where the halves add
conditions, they win. In order:

1. **Re-run the packet's replay BEFORE the ledger** (CTO condition). The scripts are under
   `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~201/replay/`. Run them against the zips you will upload and the six
   LIVE zips, with scratch OUTSIDE every worktree, deleted after. Any arm that is not identical or expected-diff ends the order.
2. **Record the held hosts' live CodeSha256 BEFORE anything**: irpt-holdings and irpt-narrative. They stay held (CTO condition) and must
   read the same after.
3. **Open the ledger** (NEVER-2). It must STATE THE PIN, which the ccbe8b8be1 deploy gate requires:
   - packet blob be15b61188;
   - code pin 74a62fb46c;
   - census pin 71e9aacf27;
   - all six built sha256 (packet table).
4. **Land the six functions** through the build and Terraform path, from a clean tree at the census pin, never by console:
   irpt-49f-reporting-read-lambda, irpt-directory-search, irpt-export-render, irpt-performance-adapter, irpt-status and
   irpt-ycharts-generate. Read each live CodeSha256 back equal to its built value, and confirm a 0-diff re-plan.
5. **After-read.** Per the CTO, after-read 2 is satisfied by the step-1 replay; do NOT edit any profile row. Read the two held hosts again;
   they must be unchanged.
6. **Close the ledger.**
7. **After-reads file** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~IB2/IB100-1_authz_release_after_reads.json`:
   `{ledger: {state, pin, sha256: [six]}, rolled_back, replay_rerun_before_ledger: [{name, verdict, negative_control}],
   held_hosts_unchanged: {irpt-holdings: <CodeSha256>, irpt-narrative: <CodeSha256>}, live_after: {<fn>: <CodeSha256>}}`.

If any step fails, apply nothing more and run Branch B per the packet (each function's recorded S3 rollback version, through the same
path). File a row.

<criterion id="IB100-1-AC1" cell_refs="IB-pr-395"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r100/p100_apply_390.py" . IB100-1-AC1</invocation><expect>IB100-1-AC1 PASS</expect></criterion>
`IB100-1-AC1` -- all six live CodeSha256 equal their built values, and the ledger is CLOSED and states the pin and the six sha256. Base: FAIL.

<criterion id="IB100-1-AC2" cell_refs="IB-pr-395"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r100/p100_apply_390.py" . IB100-1-AC2</invocation><expect>IB100-1-AC2 PASS</expect></criterion>
`IB100-1-AC2` -- the replay ran before the ledger (at least 10 arms, with a negative control), and both held hosts are unchanged live.
Base: FAIL.

<expected_criteria>IB100-1-AC1, IB100-1-AC2</expected_criteria>

## BOUNDS

- **Grant:** the `<paths>` block below and nothing else.
- **The only served change:** the six functions' code. There is no IAM, route, schedule, env, profile-row or other function change, and
  irpt-holdings and irpt-narrative are NOT touched.
- **No vendor call**, no monitor, alarm, SNS or SES.
- **Refusal clause:** STOP, file a row, and apply nothing more (Branch B if already applied) on any of these:
  - a moved start sha;
  - a census other than the packet's;
  - a built sha other than the packet's;
  - a failed replay arm;
  - a plan touching anything else;
  - a failed read-back.
- **Row ids:** `IRPT_BCKEND-D2-S<n>`; take the next free number from the channel at HEAD, and check it is still free just before you
  commit. `surfaced_at` is the real time.
- **Commit** with your own author line via `bash .tools/safe-commit.sh -F <msgfile>`. ASCII only.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-395.authz-served-release-390-applied-6-hosts.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~IB2/
infra/aws/terraform/investor-reporting/
infra/aws/lambda/ci/CHANGELOG.md
infra/aws/lambda/ci/lambda-source-map.json
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 93 (round 100, workstream ~P), cell `IB-pr-395`.
<owned_cells>IB-pr-395</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB100-1-AC1, IB100-1-AC2. The instance goes at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~IB2/IRPT_BCKEND.TO-IB-pr-395.authz-served-release-390-applied-6-hosts.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message, give:
- live before and after for each function;
- the held hosts before and after;
- the replay verdicts;
- the ledger entry;
- each criterion's last line;
- any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- 8 functions package _authz/served.py; 6 released (restaged to 74a62fb46c, pins verified at HEAD), irpt-holdings and irpt-narrative held (IB-pr-394 in flight); no live profile row holds ALL (worker census), so no live caller's reach changes today; svc-custody-statement inert until its mint lands.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change; route behaviour changes only via the code (per-route table in the packet).
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p100_apply_390.py dry-run at base box/dell2 on dell2 2026-10-09 ~06:5xZ: AC1 FAIL (irpt-49f-reporting-read-lambda live cou/Td9y != built 8ySmTtYX), AC2 FAIL (no after-reads file); 0 control bytes; ruff clean.
lane: the <paths> block IS the grant; applied by 0.7.0_AE_CloudOps~IB2 (MSTR msg 2725), IRPT_BCKEND only.
</preflight>
