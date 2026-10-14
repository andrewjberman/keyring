# NFRA_MCPORTAL task order -- `MP-pc-6` -- WORKSTREAM PC ROUND 1: the close run -- one real person's served view against the stores, and the three refusal states served

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPORTAL/decompositions/NFRA_MCPORTAL_DECOMP.md</decomp_doc>
<owned_cells>MP-pc-6</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPORTAL.TO-MP-pc-6</to_id>
<issued_to>0.9.0_WK_NFRA_MCPORTAL~24</issued_to>
<issued_by>2.0.0_SA_COO~MP</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a one-time close run.
comp-iam: DECLARED-NOT-APPLICABLE -- reads only: the served modules through SSM, the grant store through the existing operator read path, and the gitstate pointers through S3 head/get.
comp-adversary: DECLARED-NOT-APPLICABLE -- each equality is read against a source other than the page (the store, the breakdown, the pointer object itself).
EGRESS CLASS, declared: AWS reads (SSM send-command, DynamoDB GetItem/Query through the operator read, S3 head-object/get-object); no write.
</preflight>

## 1. THE CELL -- `MP-pc-6` (workstream PC round 1, decomposition sections PC.1 and PC.5)

Your worktree is `C:/tmp/mp-pc-24` (branch `wk-NFRA_MCPORTAL-pc-24`). Work and commit only there.

The release (MP-pc-5) is live. It serves `GET /api/admin/people`, the per-person view of what each person reaches
through the gateway, and the three-state `integration_refused` on `GET /api/admin/fabric/gitstate`. Both routes are
owner-gated, and you hold no owner identity. So read the SERVED modules on the host, the way the release check does:
over SSM on `i-07dccb1615503ac99`, from `/opt/opal-gateway` with the host's `.venv`, as `ec2-user`. Begin the probe with
`import app.server`, which registers the served integrations (row Z-S48). See
`org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/pc/checks/_pc5_probe.py` for the pattern.

1. **One real person against the grant store.** In `app.admin_people._compute()`, take the one real principal whose
   `how` reads "data grant revision <n>" (the grant store's profiled principal) -> `person` (its `who`, exactly as
   served). From its channels, list the data-grant tools it holds (`schwab_*` and `blackdiamond_list_fees`) ->
   `page_person_tools`. Then, independently, read that principal's ACTIVE grant from the store with the existing operator
   read: `infra/aws/ec2/opal-gateway/ops/schwab_entitlement_admin.py`, its read/show subcommand, under the operator role
   as its header describes. From the grant's `operations`, list the data-grant tools it admits, using the operation each
   tool needs in `app/data_entitlement.py` `SCHWAB_TOOLS` -> `store_tools`.
2. **One channel, per person, against the breakdown.** In the same probe run, also call
   `app.admin_gateway_breakdown._compute()`. Pick the channel with the most tools that is NOT `m365` -> `channel`. For
   ONE person who holds tools in it (prefer `opalbloomberg@opalinvest.com` if it holds any; otherwise the first such
   person), take the breakdown holder row's `tools` for that person -> `breakdown_holder_tools`, and the tools
   `admin_people` lists for that person under that channel -> `page_channel_tools`.
3. **The three refusal states.** For each box in `laptop sitez dell1 dell2`, read
   `s3://opal-313476888478-globgrph/fabric/activity/v1/gitstate/box=<B>/last_integrate.json` yourself, through
   `.tools/aws s3api head-object`, reading the RETURN CODE (a 404 is rc 254 with "(404)" on stderr; an empty output
   without that is NOT absence, so re-read). Where it is present, get the object and read its `rc`.
   - `box_no` = a box whose pointer is present with rc 0;
   - `box_not_recorded` = a box with no pointer.

   In the probe, call `app.admin_fabric_gitstate._compute()` and record those two boxes' served `integration_refused` ->
   `served_box_no` (expected `{"refused": false, "at": ...}`) and `served_box_not_recorded` (expected
   `"not recorded"`). If no box has rc 0, or no box lacks a pointer, write null for that box and say so; do not invent
   one.
4. **Write the run file** `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~24/pc6_run.json`:
   `{"person","store_tools","page_person_tools","channel","breakdown_holder_tools","page_channel_tools","box_no","box_not_recorded","served_box_no","served_box_not_recorded"}`.
   Commit it, then run AC1.

## 2. BOUNDS

1. Write surface: exactly the paths in section 3. No gateway file, no store write, no pointer write, no deploy.
2. Standing rules: no push and no vendor call. Commit via `.tools/safe-commit.sh` with your serial as author (CLAUDE.md
   14a). If you cannot meet a criterion as written, REFUSE it with its measurement. Never repair a criterion.

## 3. SURFACES

<paths>
org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~24/**
org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/**
</paths>

Read, never write: `infra/aws/ec2/opal-gateway/ops/schwab_entitlement_admin.py`, `infra/aws/ec2/opal-gateway/app/**`,
and `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/pc/checks/`.

Rows go to `org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, with id
`NFRA_MCPORTAL-Z-W24-S<k>` (the next free k for W24). `surfaced_at` = `date -u +%FT%TZ` at filing. `disarm_owner` on an
ARMED row is `2.0.0_SA_COO~MP`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MP-pc-6"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/pc/checks/pc6.AC1.sh; echo "exit=$?"</invocation><expect>run=read; store==page:yes; breakdown==page:yes; served_no:yes; served_not_recorded:yes -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~24/NFRA_MCPORTAL.TO-MP-pc-6.fwd21-read-close-run.proof_of_spec.json`.
Report once, with:
- the check output;
- the commit hash;
- the run file's values;
- each box's pointer read (rc and return code);
- the SSM command id;
- any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** cut STAGED at the PC issuance (decomposition v9). This is the read half of FWD-21's DONE WHEN ("the same
per-person view read for one real person and checked against the stores it reads") plus G1's closing condition (C17
round-2 analysis ruling 1: "the served page reads `no` for laptop and `not recorded` for a box with no pointer"). The
write half waits on F2. Check dry-run at base 9be88c9134: AC1 FAIL (run file absent). The checker's pass arm is the equality of
independently read lists, the MP-z-6 method. Spawned when MP-pc-5 drains.

<status>staged</status>
<round>1</round>
<workstream>PC</workstream>
<slot>~24</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
