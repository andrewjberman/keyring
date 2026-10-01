# MDPF_TAXSMA -- remediations, PREPARED and not landed (compile ordered by the CTO's closure plan)

NOT A CHANNEL CARRIER. The row gate refused these 13 rows at commit (2026-10-01 ~09:0xZ): a new remediation row is refused while
15 of the project's 27 task orders read non-terminal at HEAD. They move to
`org/missions/D8/MDPF/MDPF_TAXSMA/surprise-channel/remediations/REMEDIATION_v1.md` unchanged, after a re-read of each live figure,
when the order files are terminal. Until then these 13 items are undispositioned on the channel.

<sweep_watermark>2026-10-01T02:00Z</sweep_watermark>

Author: 3.0.0_SA_CVO, 2026-10-01. Graduated at ADJUDICATION_v1.md's L9: 13 rows, all OPEN with an owner. Three are ARMED (S5, S6, S12), one is BLOCKING with its hazard disarmed for this project (S10), one is BLOCKING and inert until activation (S11). Rounds read v2: the project is FAST and builds from its STATUS next-list.

```json
[
  {
    "id": "MDPF_TAXSMA-S1",
    "project": "MDPF_TAXSMA",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Three tests of the Global fold's carry path fail in the MDPF Gold suite and have since before this project's cut base, so every Gold-suite criterion reads 'fails only on the known three' and a fourth failure on the same path would have to be told apart by name.",
    "evidence": [
      "py -3.12 -m pytest data/mdpf/scripts/gold/tests/test_global_fold_flag2.py at CLOUD HEAD (this seat, 2026-10-01 08:4xZ): 3 failed, 16 passed -- test_carry_within_window_carries_and_labels, test_carry_beyond_window_absent_for_real, test_carry_source_is_measured_never_interpolated",
      "investigation row MDPF_TAXSMA-S1 (2.0.0_SA_COO~T, 2026-09-15)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/MDPF_TAXSMA_CHANNEL_COMPILE_20261001.md (co-committed)"
    ],
    "remedy": "P2: the three tests are brought to the carry behaviour that is served, or retired with the reason stated. The carry path is the one finding F-A of the MDPF_COTREMEDIATION grade reads (11 carried days since 2026-08-20), so a red guard on it is not idle. Placement is the CTO's (MDPF_HEALGAP or MDPF_CANON).",
    "owner": "1.0.0_SA_CTO",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO",
      "round": "v2"
    },
    "closed": false
  },
  {
    "id": "MDPF_TAXSMA-S5",
    "project": "MDPF_TAXSMA",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The EC2 daily runner's Stage 6 fails at import since the Tax timeseries module reached its code prefix: taxsma_assets imports lib.opal_naming, which the runner tree does not carry. The dispatch logs it non-fatal, so nothing louder fires.",
    "evidence": [
      "infra/aws/ec2/mdpf-daily-runner/mdpf-daily-dispatch.sh at HEAD (this seat): 0 lines naming lib/ or opal_naming, 14 lines naming Stage 6 -- the runner still syncs no lib/",
      "NOT re-read: a runner log since 2026-09-21; whether Stage 6 still fails daily is taken from the row and from STATUS.md's Parked line",
      "investigation row MDPF_TAXSMA-S5 (0.7.0_AE_CloudOps~V, 2026-09-21)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/MDPF_TAXSMA_CHANNEL_COMPILE_20261001.md (co-committed)"
    ],
    "remedy": "P1: the runner syncs lib/ (one line in the dispatch script, in the AE lane's tree), then one Stage 6 run is read to its end. STATUS.md parks it with this lane.",
    "owner": "4.0.0_SA_CRO",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "4.0.0_SA_CRO",
      "round": "v2"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "4.0.0_SA_CRO",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_TAXSMA-S6",
    "project": "MDPF_TAXSMA",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "A Gateway deploy built from CLOUD HEAD ships four other projects' unreleased commits with this project's route, one of them under Andrew's stop.",
    "evidence": [
      "org/missions/D8/MDPF/MDPF_TAXSMA/STATUS.md (as of 03:5xZ): TX-r-2 has no owner since 04:00Z; the parked remedy is a narrow cut at 1764e54a16 plus TX-g-1's three commits (held)",
      "org/mcp/drive-mode.log line of 2026-10-01T02:06:43Z (this seat): the Gateway surfaces were dropped from the lease, 'site Z's, Andrew-direct 02:0xZ'",
      "investigation row MDPF_TAXSMA-S6 (1.0.0_SA_CTO~O, 2026-09-25)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/MDPF_TAXSMA_CHANNEL_COMPILE_20261001.md (co-committed)"
    ],
    "remedy": "P1, a condition on whoever runs the Gateway release: it is cut narrow, or the four riders are each graded for release first. Who runs it is Andrew's call (STATUS.md Dependencies).",
    "owner": "4.0.0_SA_CRO",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "4.0.0_SA_CRO",
      "round": "v2"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "4.0.0_SA_CRO",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_TAXSMA-S10",
    "project": "MDPF_TAXSMA",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "The opal-gateway Terraform root has appliers on both devices, each applying from a tree that lacks the other's unpushed commits, so a clean plan from the laptop lasts only until the next apply elsewhere; a live role created by an unpushed applier planned as three destroys.",
    "evidence": [
      "org/mcp/drive-mode.log, 2026-10-01T02:06:43Z (this seat): the lease was re-armed without the Gateway surfaces on Andrew's word that they are site Z's",
      "org/missions/D8/MDPF/MDPF_TAXSMA/STATUS.md: TX-i-3 was applied from the mdpf-pipeline root at 01:52:55Z and NOT from opal-gateway (held; the apply and its 2-added plan were not re-read)",
      "investigation rows MDPF_TAXSMA-S7 and -S10 (4.0.0_SA_CRO, 0.0.0_AB_MSTR)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/MDPF_TAXSMA_CHANNEL_COMPILE_20261001.md (co-committed)"
    ],
    "remedy": "For this project the hazard is disarmed: no laptop seat applies that root. The class stays open: one applying device per Terraform root, or every applier pushes before the next plan elsewhere. That is the integrator's.",
    "owner": "0.0.0_AB_MSTR",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "0.0.0_AB_MSTR",
      "round": "v2"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "0.0.0_AB_MSTR",
      "at": "2026-10-01T02:06Z"
    },
    "closed": false
  },
  {
    "id": "MDPF_TAXSMA-S11",
    "project": "MDPF_TAXSMA",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "No cell wires the Tax route's bearer or identity into the Gateway's .env: the deploy script rewrites .env whole on every deploy and carries no Tax line, so the route stays unauthorized after every release and a hand-placed value is erased by the next one.",
    "evidence": [
      "git show HEAD:infra/aws/ec2/opal-gateway/deploy-to-ec2.sh (this seat, 08:4xZ): 0 lines naming TAXSMA; control, 13 lines naming .env",
      "investigation row MDPF_TAXSMA-S11 (4.0.0_SA_CRO, 2026-10-01)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/MDPF_TAXSMA_CHANNEL_COMPILE_20261001.md (co-committed)"
    ],
    "remedy": "P0 for activation: the two lines land in the deploy script before TX-r-2's release, and the release reply shows both keys present. STATUS.md's recommendation is that this lane writes them and site Z deploys; the owner of the deploy is Andrew's call.",
    "owner": "4.0.0_SA_CRO",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "4.0.0_SA_CRO",
      "round": "v2"
    },
    "closed": false
  },
  {
    "id": "MDPF_TAXSMA-S12",
    "project": "MDPF_TAXSMA",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "infra/aws/ec2/verify-ec2.sh --ssm prints 'All checked services are in sync' with exit 0 when it checked nothing, and reports a running, reachable Gateway as skipped.",
    "evidence": [
      "git log -1 -- infra/aws/ec2/verify-ec2.sh (this seat): last changed 2026-07-23 (5194d7c676), so the behaviour the row measured on 2026-10-01 is the current script",
      "NOT re-run by this seat",
      "investigation row MDPF_TAXSMA-S12 (4.0.0_SA_CRO, 2026-10-01)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/MDPF_TAXSMA_CHANNEL_COMPILE_20261001.md (co-committed)"
    ],
    "remedy": "P1: zero services checked, or any service skipped, exits non-zero and says so on the last line. The row's disarm owner (0.7.0_AE_CloudOps) has no live seat on the laptop; placement is the CTO's. Until then a seat reads the per-service lines, never the exit code.",
    "owner": "1.0.0_SA_CTO",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO",
      "round": "v2"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "1.0.0_SA_CTO",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_TAXSMA-S9",
    "project": "MDPF_TAXSMA",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The contract's two category Gold copies (artifacts.firm_category, global_category) are no longer written: they had no reader and would have been a second home for the category-views document. The contract still names them.",
    "evidence": [
      "org/missions/D8/MDPF/MDPF_TAXSMA/STATUS.md Parked: 'strike the two artifacts, or re-point the publisher to them as one migration', owner 1.0.0_SA_CTO (held)",
      "investigation row MDPF_TAXSMA-S9 (4.0.0_SA_CRO, 2026-09-30)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/MDPF_TAXSMA_CHANNEL_COMPILE_20261001.md (co-committed)"
    ],
    "remedy": "P2: the CTO strikes the two artifacts from the contract (a versioned edit), or rules the migration. A contract that names artifacts nothing writes is a claim with no value behind it.",
    "owner": "1.0.0_SA_CTO",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO",
      "round": "v2"
    },
    "closed": false
  },
  {
    "id": "MDPF_TAXSMA-S13",
    "project": "MDPF_TAXSMA",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The commit-time naming gate grades a reference to an existing legacy-named role as a new out-of-pattern name; the reference passes only when the same string is composed from parts, which hides it from the gate.",
    "evidence": [
      "investigation row MDPF_TAXSMA-S13 (4.0.0_SA_CRO, 2026-10-01): the literal 'opal-gateway-role' refused twice in a file that creates no role",
      "NOT re-exercised by this seat",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/MDPF_TAXSMA_CHANNEL_COMPILE_20261001.md (co-committed)"
    ],
    "remedy": "P2: the gate tells a reference (a data source or a cross-root local) from a declaration, or admits a marked reference; the gate is the CTO's. Until then the composed-from-parts form is a workaround the gate's owner should know exists.",
    "owner": "1.0.0_SA_CTO",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO",
      "round": "v2"
    },
    "closed": false
  },
  {
    "id": "MDPF_TAXSMA-W5-S1",
    "project": "MDPF_TAXSMA",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The PRD calls additional Tax-labelled custodian candidates UNCONFIRMED, and at filing the contract carried no such member on any axis, so the expected cases state the candidate's observable without a status word.",
    "evidence": [
      "git show HEAD:org/standards/MDPF_TAXSMA_DATA_CONTRACT.json (this seat): version 0.6.0; the string UNCONFIRMED appears twice, both as the member REMOVED_UNCONFIRMED (lines 263 and 719) -- whether that member is the label for these candidates was not established",
      "org/missions/D8/MDPF/MDPF_TAXSMA/STATUS.md: TX-v-1's re-cut for contract 0.6.0 is NOT STARTED; the parked row on the two unconfirmed 0833 accounts is Yang's or Andrew's",
      "investigation row MDPF_TAXSMA-W5-S1 (0.9.0_WK_MDPF_TAXSMA~5)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/MDPF_TAXSMA_CHANNEL_COMPILE_20261001.md (co-committed)"
    ],
    "remedy": "P2: the TX-v-1 re-cut names the candidate's status in contract vocabulary, or the contract gains the member with its rule-24 record.",
    "owner": "4.0.0_SA_CRO",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "4.0.0_SA_CRO",
      "round": "v2"
    },
    "closed": false
  },
  {
    "id": "MDPF_TAXSMA-W6-S2",
    "project": "MDPF_TAXSMA",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "EC2_MANIFEST.json's checksums for the Gateway do not describe its own deployed commit: three files' recorded checksums match neither the host nor the git blob.",
    "evidence": [
      "investigation row MDPF_TAXSMA-W6-S2 (0.9.0_WK_MDPF_TAXSMA~6, 2026-09-15): app/server.py host and blob 370d5568, manifest a101f27e",
      "NOT re-read by this seat; the Gateway is site Z's surface",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/MDPF_TAXSMA_CHANNEL_COMPILE_20261001.md (co-committed)"
    ],
    "remedy": "P2, relayed to site Z's Gateway owner by the CTO: the manifest is regenerated at the next deploy and its checksums are verified against the host in the same step.",
    "owner": "1.0.0_SA_CTO",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO",
      "round": "v2"
    },
    "closed": false
  },
  {
    "id": "MDPF_TAXSMA-W1-S2",
    "project": "MDPF_TAXSMA",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Running the Gateway test modules from the Gateway directory appends records to the tracked file infra/aws/ec2/opal-gateway/audit.jsonl, so every run dirties the tree.",
    "evidence": [
      "git ls-files infra/aws/ec2/opal-gateway/audit.jsonl (this seat): tracked",
      "investigation row MDPF_TAXSMA-W1-S2 (0.9.0_WK_MDPF_TAXSMA~1)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/MDPF_TAXSMA_CHANNEL_COMPILE_20261001.md (co-committed)"
    ],
    "remedy": "P3, relayed with W6-S2: the test writes its audit records to a temp path, or the file is untracked.",
    "owner": "1.0.0_SA_CTO",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO",
      "round": "v2"
    },
    "closed": false
  },
  {
    "id": "MDPF_TAXSMA-W1-S4",
    "project": "MDPF_TAXSMA",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Every Gateway deploy artifact bundles a tracked agent telemetry file under app/org/mcp/agent_telemetry/, because the build ships the whole app directory.",
    "evidence": [
      "git ls-files 'infra/aws/ec2/opal-gateway/app/org/mcp/agent_telemetry/*' (this seat): 1 file tracked",
      "investigation row MDPF_TAXSMA-W1-S4 (0.9.0_WK_MDPF_TAXSMA~1): 9 lines, 1,863 bytes; its content was not read",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/MDPF_TAXSMA_CHANNEL_COMPILE_20261001.md (co-committed)"
    ],
    "remedy": "P2, relayed with W6-S2: the file leaves the app tree (it is a stray copy of the fabric's telemetry path) or the build excludes it.",
    "owner": "1.0.0_SA_CTO",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO",
      "round": "v2"
    },
    "closed": false
  },
  {
    "id": "MDPF_TAXSMA-W2-S2",
    "project": "MDPF_TAXSMA",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The Gold function's own configuration names for calling the Gateway (TAXSMA_GATEWAY_BASE_URL, TAXSMA_CAPABILITY_BEARER) were minted by one cell and appear in no specification; if the activation's Terraform uses other names the prelude stays silently DISABLED.",
    "evidence": [
      "git grep at HEAD (this seat): the two names appear in 1 file under data/mdpf/scripts and in 0 files under infra/aws/terraform",
      "lambda get-function-configuration mdpf-gold-lambda (this seat, 06:3xZ): 1 environment key, 0 naming TAX -- Tax is DISABLED today, as designed",
      "investigation row MDPF_TAXSMA-W2-S2 (0.9.0_WK_MDPF_TAXSMA~2)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/MDPF_TAXSMA_CHANNEL_COMPILE_20261001.md (co-committed)"
    ],
    "remedy": "P1, a condition on TX-r-3: the activation's Terraform reads the two names from the Gold source, and its acceptance includes one read that the prelude is ENABLED after the apply, not only that the apply succeeded.",
    "owner": "4.0.0_SA_CRO",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "4.0.0_SA_CRO",
      "round": "v2"
    },
    "closed": false
  }
]
```
