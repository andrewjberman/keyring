# NFRA_MCPORTAL -- C17 round 2 L8 compile + the backlog since v3 (site Z) -- 39 of 39 undispositioned rows dispositioned

Author: 3.0.0_SA_CVO~Z. Round: v4. Fabric: site-z. Recorded: 2026-10-14 ~02:4xZ.
**Input:** `2.0.0_SA_COO~MP` `deliverables/2.0.0_SA_COO~MP/c17r2/C17R2_DRAIN_PACKET.md` @f9f9f3c4b0, read to EOF (msg 33938,
acked). C17 round 2 has 4 of 4 orders terminal (MP-n-2, MP-n-3, MP-n-5, MP-n-4). This seat re-ran round-close-check and
it reads MAY-CLOSE. There are no judgment criteria.

**The backlog.** No CVO compile had been written for this project since v3 (2026-10-09), so 39 investigation rows were
undispositioned, four of them ARMED since 2026-09-25. All 39 are dispositioned here. The REMEDIATION_v1 states that
Z-S20 said were "the CVO's act" are flipped in place in this commit:
- Z-W3-S3: REMEDIATED, DISARMED;
- Z-C-S10: REMEDIATED, DISARMED;
- Z-W3-S2: REMEDIATED.
Their basis is Z-S20's measured acts (the staged build, E1's header read, the sub-branch apply, and the deployed
writer's live refusal). This seat did not re-read those acts; they are 09-25 premises that many later releases of the
same writer have overtaken.

## The one real run, read again by this seat (~02:4xZ)

- `EC2_MANIFEST.json` `services.opal-gateway`: `deployed_commit` b0c75d24f1 (2026-10-14T01:21:24Z), previous 7eff14b2e6.
- One `head-object` per box on `s3://opal-313476888478-globgrph/fabric/activity/v1/gitstate/box=<B>/last_integrate.json`:
  - laptop present, LastModified 2026-10-14T02:37:22Z;
  - sitez, dell1 and dell2 return 404.
  - This matches the packet's table.
- `app/admin_fabric_gitstate.py:173-182` (`_refused`): `rc != 0` gives {at, note}; otherwise it returns
  `_NOT_RECORDED`, and that includes a pointer that exists with `rc == 0`.

```json
[
  {
    "id": "NFRA_MCPORTAL-Z-C-S30",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-14T02:43Z",
    "one_line": "C17 round 2 grade: the bounded git-state read is REALIZED on the served host -- one pointer get per box, cold read 1.3 s / 136 fetches on the host (2.2 s from this box) against the 5 s bar, down from 9.7 s / 1,336 at the base.",
    "class": "OBSERVATION",
    "spec_asserts": "PRD v0.6 C17 (Z-S40 option c): integration_refused is read from one per-box pointer, so a cold read does not grow with history; the cold read is under its bar on the served host.",
    "world_is": "Served: deployed_commit b0c75d24f1 (manifest). The issuer's two cold reads, on the host under the instance role (1.3 s, 136 body fetches, recorded=4) and on this box (2.2 s), are on different planes and agree that the read is far inside 5 s. This seat's head-object census of the four pointers reads 1 present (laptop, 02:37:22Z) and 3 absent (404), which is the packet's own count. The refusal branch (rc != 0) was never exercised: no box records a refusal, and the packet says so. C17's bound holds. The DISPLAY of the non-refused states is a separate defect (Z-C-S31).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/ec2/EC2_MANIFEST.json services.opal-gateway deployed_commit b0c75d24f1 (this seat)",
        "aws s3api head-object x4 on box=<B>/last_integrate.json (this seat, ~02:4xZ): laptop 200, sitez/dell1/dell2 404",
        "deliverables/2.0.0_SA_COO~MP/c17r2/C17R2_DRAIN_PACKET.md @f9f9f3c4b0"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade, not a defect."
  },
  {
    "id": "NFRA_MCPORTAL-Z-C-S31",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-14T02:43Z",
    "one_line": "integration_refused shows ONE word, 'not recorded', for two different states: a box whose last integrate pass is RECORDED and clean (pointer present, rc 0 -- laptop today) and a box with NO pointer at all (sitez, dell1, dell2); and the basis text it shows ('no integrate pass has been recorded') is false for the first.",
    "class": "OBSERVATION",
    "spec_asserts": "A value carries its claim, and a measured negative is never displayed as an absence (A_VALUE_MUST_CARRY_ITS_CLAIM; taxonomy law, state coherence).",
    "world_is": "_refused (app/admin_fabric_gitstate.py:173-182) returns {at, note} for rc != 0 and _NOT_RECORDED for everything else. The module docstring (:15-16) and _REFUSED_BASIS (:59-61) explain 'not recorded' as 'no integrate pass has been recorded since the pointer began on 2026-10-13'. That is true for sitez, dell1 and dell2, which return 404. It is false for laptop: laptop's pointer exists (LastModified 02:37:22Z) and records a clean pass (rc 0, per the packet). Andrew therefore reads 'not recorded' for a box whose integration IS recorded and succeeded. Once every box writes a pointer, the column will read 'not recorded' on every healthy box forever, and only a refusal will ever show a value. The packet calls the 4-of-4 'designed reading', and it is the module's rule. The rule itself is the defect.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/ec2/opal-gateway/app/admin_fabric_gitstate.py:15-16, :56, :59-61, :173-182 (read at box/sitez HEAD; MP-n-4 released these bytes)",
        "head-object laptop last_integrate.json present 02:37:22Z; sitez/dell1/dell2 404 (this seat)",
        "C17R2_DRAIN_PACKET.md: laptop pointer rc 0, written 01:01:57Z, read 'not recorded' by the module's rule"
      ]
    },
    "disposition": "GRADUATED"
  },
  {
    "id": "NFRA_MCPORTAL-Z-C-S32",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-14T02:43Z",
    "one_line": "Backlog: 30 rows DISMISSED as resolved by a later row or a later measured act -- the 09-25 ARMED rows overtaken (W1-S3, W1-S4, W2-S7), the ruff and ledger-tool BLOCKING/ARMED rows disarmed by their own follow-ups (S24, S31, S34), the cold-read chain closed by C17 (S27..S30, S37..S40), deep links met (S41), and act-stop rows whose acts later completed (S21, S45, S48, S49/S50).",
    "class": "OBSERVATION",
    "spec_asserts": "The L8 compile dispositions every undispositioned BLOCKING or ARMED row, and every row in scope.",
    "world_is": "W1-S3 and W1-S4 (ARMED 09-25: the staged grant-writer zip and its check's interpreter) are overtaken by Z-S20's measured acts and by the writer serving through every later release. Z-S20 itself is accepted, and its three REMEDIATION_v1 flips are made in this commit. W2-S7 (BLOCKING ARMED 09-25: the narrow release failed on a .env printf shift and was rolled back) is overtaken by every later deploy-to-ec2.sh release serving. The newest, MP-n-4 at b0c75d24f1, passes AC2 on the host. Z-S24 (BLOCKING ARMED, deploy_ledger hold discarded prose) is disarmed by Z-S25 and fixed at source by 0.0.0_AB_MSTR~Z @a9d1b38f12 (Z-S26: a replay keeps 136 of 136 lines). Z-S31 (BLOCKING ARMED, ruff spawn refused) and Z-S34 (its corrected diagnosis) are disarmed by Z-S33, Z-S35 and Z-S36: the refusal is intermittent, the gate passed 20 of 20, nothing was bypassed, and the device fault is routed to 0.0.0_AB_MSTR~Z. Z-S32 and Z-S36 are measurement notes. The cold-read chain is closed: Z-S27 and Z-S29 by AMENDMENT 5 (overlap fell to 2.2 s, per Z-S38); Z-S30 answered by Z-S33; Z-S37, Z-S38, Z-S39 and Z-S40 by C17, whose round 2 serves 1.3 s (Z-C-S30). Z-S28 is fixed at the check by Z-S29. Z-S41 (deep links 404, this seat's row) is met: Z-S48's host probe reads /control-plane=401 and /open-calls=401 (routed and auth-gated) and an unlisted path 404, which is the W15 catch-all. Z-W15-S1, Z-W15-S2 and Z-W13-S1 are implementation and premise notes handled in their cells. Z-S21 (the naming gate refused the TO's policy name) is closed by MP-x-3 reading complete. Z-S45 (release-tree base failures) is handled by Amendment 1, the Z-S45 mechanism MP-n-4 used. Z-S48 (z5.AC2 probe not runnable) is a criterion defect, and the same probe with the import reads channels=8 tools=67. Z-S49 is corrected by Z-S50, and the stale release_note is fixed by its owner @642fe57f1d.",
    "adjudicates": [
      "NFRA_MCPORTAL-Z-W1-S3",
      "NFRA_MCPORTAL-Z-W1-S4",
      "NFRA_MCPORTAL-Z-W2-S7",
      "NFRA_MCPORTAL-Z-S20",
      "NFRA_MCPORTAL-Z-S21",
      "NFRA_MCPORTAL-Z-S24",
      "NFRA_MCPORTAL-Z-S25",
      "NFRA_MCPORTAL-Z-S26",
      "NFRA_MCPORTAL-Z-S27",
      "NFRA_MCPORTAL-Z-S28",
      "NFRA_MCPORTAL-Z-S29",
      "NFRA_MCPORTAL-Z-S30",
      "NFRA_MCPORTAL-Z-S31",
      "NFRA_MCPORTAL-Z-S32",
      "NFRA_MCPORTAL-Z-S33",
      "NFRA_MCPORTAL-Z-S34",
      "NFRA_MCPORTAL-Z-S35",
      "NFRA_MCPORTAL-Z-S36",
      "NFRA_MCPORTAL-Z-S37",
      "NFRA_MCPORTAL-Z-S38",
      "NFRA_MCPORTAL-Z-S39",
      "NFRA_MCPORTAL-Z-S40",
      "NFRA_MCPORTAL-Z-S41",
      "NFRA_MCPORTAL-Z-W15-S1",
      "NFRA_MCPORTAL-Z-W15-S2",
      "NFRA_MCPORTAL-Z-W13-S1",
      "NFRA_MCPORTAL-Z-S45",
      "NFRA_MCPORTAL-Z-S48",
      "NFRA_MCPORTAL-Z-S49",
      "NFRA_MCPORTAL-Z-S50"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows named, read in brief by this seat (one_line and world_is)",
        "task-orders/NFRA_MCPORTAL.TO-MP-x-3.gateway-fabric-read-grant.md last status complete",
        "EC2_MANIFEST deployed_commit b0c75d24f1; C17R2_DRAIN_PACKET.md (MP-n-4 AC2 PASS on the host)",
        "0.0.0_AB_MSTR~Z @a9d1b38f12 (deploy_ledger fix, per Z-S26)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Resolved by a later row or a later measured act, each named."
  },
  {
    "id": "NFRA_MCPORTAL-Z-C-S33",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-14T02:43Z",
    "one_line": "Backlog: 5 recipe rows DISMISSED as notes and carried to the cut template -- 'run the plan with safe-apply' is unsatisfiable (Z-S22, Z-S42), and the gateway's sparse cone needs infra/logic/registry and data/transcripts/scripts/teams/ and must be set via --stdin (Z-S43, Z-S44, Z-S46).",
    "class": "OBSERVATION",
    "spec_asserts": "A recurring order-wording or worktree-recipe defect is carried to its owner, not left as an open row.",
    "world_is": "Each row failed CLOSED and the cell recovered in-session. Z-S22 and Z-S42: safe-apply refuses any non-apply subcommand (rc 2), and the plan was run with terraform directly, as the wrapper's usage says. Z-S43, Z-S44 and Z-S46: the cone lists omit paths that the gates and deploy scripts read, and MSYS rewrites a leading-slash argv. Z-S46 enumerates the six paths the two deploy scripts read. These are the same class as NFRA_MCPINDEX Z-S92 (OPEN, the gateway deploy cone, owner 2.0.0_SA_COO~O), which recurred on three MCPINDEX releases. The fix is one shared cone list and order wording, not a per-project row.",
    "adjudicates": [
      "NFRA_MCPORTAL-Z-S22",
      "NFRA_MCPORTAL-Z-S42",
      "NFRA_MCPORTAL-Z-S43",
      "NFRA_MCPORTAL-Z-S44",
      "NFRA_MCPORTAL-Z-S46"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows Z-S22, Z-S42, Z-S43, Z-S44, Z-S46",
        "NFRA_MCPINDEX REMEDIATION_v6 row Z-S92 (OPEN)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Procedure notes, recovered in-session; the class is carried by NFRA_MCPINDEX Z-S92 and the cut template."
  },
  {
    "id": "NFRA_MCPORTAL-Z-C-S34",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-14T02:43Z",
    "one_line": "Backlog: 3 rows GRADUATE to REMEDIATION_v4 -- Z-W2-S8 (a triggered rollback is bounded by a 12-15 min halt-gate scan, not seconds; never re-measured), Z-S23 (the opal-gateway module does not plan clean untargeted), Z-S47 (Andrew-direct: the Control Plane shows each box's Claude account and 5-hour/weekly usage; no outcome carries it).",
    "class": "OBSERVATION",
    "spec_asserts": "A standing defect, or an unplaced word of Andrew's, leaves the compile as an owned remediation row.",
    "world_is": "Z-W2-S8 (ARMED since 09-25): the rollback's halt-gate scan took about 12 minutes before it reached the host, so the outage a triggered rollback bounds is 12-15 minutes. No later row re-measures it, and every release since has carried a rollback clause that assumes seconds. Z-S23: an untargeted plan of infra/aws/terraform/opal-gateway wanted an in-place update of aws_lambda_function.mcportal_grant_writer and errored on a data source for the absent secret gateway/mail/commassist-bearer. It was left as found, and it is the next actor's hazard. Not re-planned by this seat. Z-S47: Andrew's words at dell2 (~20:4xZ, cross-box ORDER XB-20261013T202846Z-111f; record ANDREW_DIRECT_20261013_204xZ_CONTROL_PLANE_SHOWS_CLAUDE_ACCOUNT_AND_USAGE...) ask for the logged-in account and 5-hour and weekly usage per box on /control-plane. The row says it lands at the GW round's analysis, which has not closed.",
    "adjudicates": [
      "NFRA_MCPORTAL-Z-W2-S8",
      "NFRA_MCPORTAL-Z-S23",
      "NFRA_MCPORTAL-Z-S47"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows Z-W2-S8, Z-S23, Z-S47, read in brief by this seat"
      ]
    },
    "disposition": "GRADUATED"
  }
]
```

-- 3.0.0_SA_CVO~Z
