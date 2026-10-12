# TO IRPT_BCKEND.TO-IB-pr-465 -- READ ONLY: whether the holdings-performance producer function's network reaches the vendor, read from configuration

<to_id>IRPT_BCKEND.TO-IB-pr-465</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~320</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-12</issued_date>
<status>complete</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>160</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** `1.0.0_SA_CTO~DELL2` msg 6245 (PRD v0.46 @3f577ef37f: "three reads before any cell, no build") | **Decomp cell:** `IB-pr-465` (decomposition section 152) | **outcome_ref:** FWD-13

---

## WORKER FACE

Root: `C:/dev/wk-irpt-bckend-320/` (bash `/c/dev/wk-irpt-bckend-320`). Work only there; `git rev-parse HEAD` before your first
commit is `base_commit` (state it). **A READ, NOT A BUILD.** You edit no product file and propose no build or fix.

**Why.** Read PRD ADDENDUM v0.46 (the last section of `org/missions/D9/IRPT/IRPT_BCKEND/prd/IRPT_BCKEND_PRD.md`), item 10: "Packaging
is not ruled until egress is measured. The bars producer needs to reach the vendor from where it runs; whether the existing
function's network allows it is not established." The second witness's bars come from Yahoo Finance; v0.46 rules them a
landed, scheduled source, so something on a schedule must fetch them. This read says whether the existing producer function
could, by its NETWORK as configured.

**HARD BOUNDS.** READ ONLY, CONFIGURATION ONLY. You do NOT invoke any function, you make NO call to the vendor from anywhere
(not from the function, not from this box), nobody signs in, nothing is written. AWS reads allowed, through `.tools/aws`:
`lambda get-function-configuration` with a `--query` selecting `VpcConfig`, `Runtime`, `Layers`, `Timeout`, `MemorySize` and the
environment's KEY NAMES only (never a value); and, only if the function is in a VPC, `ec2 describe-subnets`,
`ec2 describe-route-tables` (filtered to those subnets), `ec2 describe-security-groups` (the function's groups),
`ec2 describe-nat-gateways` and `ec2 describe-vpc-endpoints` for that one VPC. Read Terraform first; the AWS reads confirm it.

**Read and state:**
1. Which function: the holdings-performance producer (find its Terraform root under
   `infra/aws/terraform/investor-reporting/holdings-performance/` and its entry in `infra/aws/lambda/ci/lambda-source-map.json`;
   `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~313/IB153-1_PRODUCER_DESIGN_READ.md` names the call site).
   `function`, `terraform_file` (file:line), `read_at_utc`. Also `other_candidate_functions`: any other IRPT gold function a
   bars producer could be packaged with or modelled on (the reporting-gold producer), each with `in_a_vpc`.
2. `network`: `in_a_vpc` (true/false). If false: a Lambda outside a VPC has public egress by the platform; say so with the
   configuration reading. If true: `subnets` (each: its id class only, e.g. private/public by its route, and
   `default_route_target_class`: nat-gateway, internet-gateway, none, or other), `security_group_egress` (each rule's protocol,
   port range and destination class: all, a prefix list, a security group), `vpc_endpoints` (service names), and whether a
   NAT exists and is available.
3. `reach`: ONE of `REACHES` (configuration gives a route to the public internet on the port a fetch uses),
   `DOES_NOT_REACH`, `REACHES_ONLY_THROUGH_A_NAMED_PATH` (say which, e.g. an egress proxy), `CANNOT_BE_TOLD_FROM_CONFIGURATION`;
   with `claim` (`measured` means read from live configuration, and that is a statement about CONFIGURATION, not a call) and
   `reason`. `a_call_was_made_from_the_function: false`.
4. `a_run_time_fetch_would_use`: from the reader's code (`fetch_yahoo` in
   `data/assets/scripts/silver/commonwealth_price_basis_census.py`, about line 200): the `library`, the `hosts` it calls as the
   library's code or documentation in the environment names them (read the installed package's source for its base URLs if it
   is installed on this box; say where you read them, or that they are not established), `code_line`.
   `package_carries_the_library`: does the producer function's package or any layer it uses carry that library (read the map
   entry's files and layers, and `requirements` files; true, false or null with the reason).
5. `not_established`: at least: whether the vendor answers a datacentre address at all, its rate limits from a fixed address,
   and anything the configuration cannot show.

**Outputs** in `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~320/`: `IB160-2_producer_network_reach.json` with
the members named above plus `base_commit`, `functions_invoked:0`, `aws_writes_made:0`, `vendor_calls_made:0`, `sign_ins_made:0`;
and a one-page `IB160-2_PRODUCER_NETWORK_REACH_READ.md` leading with the one word.

<criterion id="IB160-2-AC1" cell_refs="IB-pr-465"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r160/p160_cells.py" . IB160-2-AC1</invocation><expect>IB160-2-AC1 PASS</expect></criterion>
<criterion id="IB160-2-AC2" cell_refs="IB-pr-465"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r160/p160_cells.py" . IB160-2-AC2</invocation><expect>IB160-2-AC2 PASS</expect></criterion>

<expected_criteria>IB160-2-AC1, IB160-2-AC2</expected_criteria>

The checks grade the shape, the sums and the bounds. Every count and answer is UNMEASURED by the issuer; "none found" and
"cannot be told" pass where true.

## BOUNDS

- **Grant:** the `<paths>` block and nothing else. No product file is edited.
- **Refusal clause:** an AWS read refused (record it as a reading; never retry another way; seek no grant) or a criterion that
  cannot be met as written: file a row and report. Never weaken a check; do not edit `p160_cells.py`.
- **Row ids** are `IRPT_BCKEND-D2-W320-S<k>`; `surfaced_at` is `date -u +%FT%TZ` at filing; `grounding.status` is `GROUNDED` or
  `INFERRED`; append only, keeping the channel file's line endings byte for byte; check the id is free before you commit.
- **Scratch** in `C:/dev/_scratch320/`, outside the worktree, removed at the very end by a short bounded python script; if the
  cleanup hangs or errors, stop cleaning, say so, and still report.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~320" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~320@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~320 <0.9.0_WK_IRPT_BCKEND~320@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool, OUTSIDE the worktree; do NOT pre-`git add`. ASCII only. Do not push.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~320/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-465.producer-function-network-reach.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 152 (round 160, workstream ~P), cell `IB-pr-465`.
<owned_cells>IB-pr-465</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB160-2-AC1, IB160-2-AC2. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~320/IRPT_BCKEND.TO-IB-pr-465.producer-function-network-reach.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message: the base; the function and its Terraform; in a VPC or not, with the routes, groups and endpoints read; the one word with its claim and reason; what a fetch would use and whether the package carries it; the other candidate functions; what is not established; each criterion's last line; the proof checker's result; commit hashes; row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: the tool was not run by the issuer; a read written to the worker's own deliverables folder; nothing is edited, built, invoked or served.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change; reads only; a refused read is a reading.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change; no deployed route is called.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p160_cells.py dry-run at base box/dell2 on dell2 2026-10-12 ~01:4xZ: every criterion of this order FAIL (no file); commit-gate clean. The issuer read PRD v0.46 item 10 and names the call site from IB-pr-457's merged record; it read no network configuration. The account-id text test is not in this check (three false failures of that pattern on 2026-10-11); the bounds keep values out.
lane: the <paths> block IS the grant. DIRECT-ACT (one read-only cell, LOCAL: records only).
</preflight>
