# NFRA_OPALAI round 2 -- HELD graduations (draft, NOT a channel carrier)

Author: 3.0.0_SA_CVO~O. Written: 2026-10-02T15:40:00Z. State: HELD until the round-2 drain-end.

Why held: `.tools/surprise-row-gate.py` refused these 9 remediation rows at commit, because a new remediation row IS
the slug and 3 of 39 orders (OA-e-8, OA-t-1.r2, OA-t-3.r2) are not terminal at HEAD (Andrew-direct 2026-09-03, LD-0521:
"We do not route until the job is over"). This file is outside the surprise-channel paths on purpose: nothing here is
routed, graded or counted. At the drain-end this seat re-measures each residual, then lands the adjudication row
below as `ADJUDICATION_v5.Z` (id re-checked for collisions) and the rows as `REMEDIATION_v2.Z`, with the slug.

The 9 items stay UNDER_INVESTIGATION in the channel until then. None is BLOCKING or ARMED. Their measurements
(2026-10-02 15:0xZ-15:1xZ) are recorded below as they were taken.

## Adjudication row to land (draft)

```text
{
  "id": "NFRA_OPALAI-Z-C-S10",
  "project": "NFRA_OPALAI",
  "fabric": "site-z",
  "surfaced_by": "3.0.0_SA_CVO~O",
  "surfaced_at": "2026-10-02T15:20:00Z",
  "one_line": "Round 2 mid-round L8: 9 rows are GRADUATED as real defects still live at HEAD, all OPEN in REMEDIATION_v2.Z. 2 are the issuer's (S54, S55), 5 go to the CTO for placement (S36, W10-S2, S39, S40, S42), and 2 go to the box operator through the CTO (S51, S53).",
  "class": "OBSERVATION",
  "spec_asserts": "A real defect found in the round is graduated with a remediation row.",
  "world_is": "Each residual was re-measured by this seat at 15:0xZ-15:1xZ. Z-S36 and Z-W10-S2: pytest on a git-archive export of CLOUD 9c15c703a6 (opal-gateway plus org/standards) reads 4 failed and 15 passed. test_ogz1_ac05 fails with KeyError 'unclassified'. test_ogz1_ac08 fails on the route-class set. test_asker_portal_scope_admits_granted_channel and test_asker_portal_scope_refuses_other_channel both fail asker_tenant_denied. W10-S2's first cause was fixed at a2c96703b1, and the order OA-r-1 passed on it. The two tests are red AGAIN from a later cause: the 'registered partner tenant' refusal from NFRA_MCPMSP (c19f86c295 or df4d410b66; not bisected). Z-S40: Get-ScheduledTaskInfo for OPAL_D7_ticket_intake reads LastTaskResult 2 at 14:59:46Z, still failing. Z-S54: opal_ai nfra-opalai-r2-dev wall-dapi-8194-wfp.ps1:359 still requires s.weight == SUBLAYER_WEIGHT (0xFFFF, :81), and this script rides the pending G-PUSH to opal_ai PROD. Z-S55: commit_gate_runner.py imports comp_constants_cli, which lives in org/modules/graph/, outside the cone that OA-f-12 named. Z-S51: safe-merge.sh:479 runs 'git merge --abort 2>/dev/null || true', so a failed abort is still silent. The private-index change 490526897d landed after S51, and S51's case was NOT re-measured against it. Z-S39, Z-S42 and Z-S53 are standing properties, and no later commit, ruling or row in this project's PRD, ledger or CTO deliverables addresses them (Grep, 0 hits).",
  "adjudicates": [
    "NFRA_OPALAI-Z-S36",
    "NFRA_OPALAI-Z-W10-S2",
    "NFRA_OPALAI-Z-S39",
    "NFRA_OPALAI-Z-S40",
    "NFRA_OPALAI-Z-S42",
    "NFRA_OPALAI-Z-S51",
    "NFRA_OPALAI-Z-S53",
    "NFRA_OPALAI-Z-S54",
    "NFRA_OPALAI-Z-S55"
  ],
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "git archive 9c15c703a6 infra/aws/ec2/opal-gateway org/standards | tar -x; python -m pytest tests/test_data_entitlement_guard.py tests/test_portal_grant.py -> 4 failed, 15 passed",
      "git rev-parse d287ffb346:<test_portal_grant.py> = 2d0196bc3e; HEAD's = b05e0682d3; git log -S 'registered partner tenant' -- opal-gateway/app: c19f86c295, df4d410b66",
      "Get-ScheduledTaskInfo OPAL_D7_ticket_intake: LastRunTime 2026-10-02 10:59:46 ET, LastTaskResult 2",
      "git -C opal_ai show nfra-opalai-r2-dev:opal/runtime/provision/wall-dapi-8194-wfp.ps1 lines 81, 359",
      ".tools/commit_gate_runner.py:96 (import comp_constants_cli); org/modules/graph/comp_constants_cli.py",
      ".tools/safe-merge.sh:474-480; commit 490526897d",
      "remediations/REMEDIATION_v2.Z.md"
    ]
  },
  "disposition": "GRADUATED"
}
```

## Remediation rows to land (draft)

```text
[
  {
    "id": "NFRA_OPALAI-Z-S36",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The entitlement guard suite was already red at the round-2 base. Two pins of NFRA_OPLGTW's OG-z-1 guard fail: test_ogz1_ac05 raises KeyError 'unclassified' on the guard's report, and test_ogz1_ac08's pinned route-class set no longer equals the app's routes.",
    "evidence": [
      "investigations/INVESTIGATION_v1.Z.md#NFRA_OPALAI-Z-S36",
      "pytest on a git-archive export of CLOUD 9c15c703a6: tests/test_data_entitlement_guard.py::test_ogz1_ac05 and ::test_ogz1_ac08 FAILED"
    ],
    "remedy": "OPEN: re-pin or repair the two OG-z-1 tests in their owning project (NFRA_OPLGTW), so that 'the guard suite keeps passing' can be graded as all-pass again. Routed to the CTO to place, because it is another project's guard.",
    "owner": "1.0.0_SA_CTO~O",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~O",
      "round": "v2"
    },
    "closed": false
  },
  {
    "id": "NFRA_OPALAI-Z-W10-S2",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Two asker tests in tests/test_portal_grant.py are red at HEAD. The OA-e-1 fixture fix a2c96703b1 made them pass, and OA-r-1 shipped on that. A later asker-path change, the 'registered partner tenant' refusal from NFRA_MCPMSP (c19f86c295 or df4d410b66; not bisected), now refuses their fixture tenant as asker_tenant_denied.",
    "evidence": [
      "investigations/INVESTIGATION_v1.Z.md#NFRA_OPALAI-Z-W10-S2",
      "pytest at 9c15c703a6: test_asker_portal_scope_admits_granted_channel and test_asker_portal_scope_refuses_other_channel FAILED (asker_tenant_denied)",
      "git log -S 'registered partner tenant' -- infra/aws/ec2/opal-gateway/app: c19f86c295, df4d410b66"
    ],
    "remedy": "OPEN: align the fixture tenant with the partner-tenant rule, or correct the rule, in ONE cell whose <paths> holds the file, and name which of the two commits regressed it. Routed to the CTO to place between NFRA_OPALAI and NFRA_MCPMSP.",
    "owner": "1.0.0_SA_CTO~O",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~O",
      "round": "v2"
    },
    "closed": false
  },
  {
    "id": "NFRA_OPALAI-Z-S39",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "An OWNER principal cannot hold any data grant without permanently losing its legacy gateway tools. A profile restricts the principal to the tools its grant allows, and a revoked record is a tombstone that never restores the legacy path. So an owner or operator seat cannot also be profiled as an asker.",
    "evidence": [
      "investigations/INVESTIGATION_v1.Z.md#NFRA_OPALAI-Z-S39",
      "Grep over NFRA_OPALAI prd/, ledger/ and deliverables/1.0.0_SA_CTO~O/ for an owner class or an asker-only grant shape: 0 hits"
    ],
    "remedy": "OPEN: specify an asker-only grant shape, or an owner class, that scopes the ASKER path without restricting the principal's own tools (the round-2 enrichment candidate from CTO msg 26254). This is a PRD-owner decision.",
    "owner": "1.0.0_SA_CTO~O",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~O",
      "round": "v2"
    },
    "closed": false
  },
  {
    "id": "NFRA_OPALAI-Z-S40",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The D7 ticket-intake runner, the Scheduled Task OPAL_D7_ticket_intake, imports the operator's teams-watch.py (cutover precondition CP-1). It has not succeeded since 2026-09-03, and since 2026-09-18 it dies on the mcpOAuth pin. Its lane, OPAL_TICKET_VNEXT, has no live COO, so nothing reads its result.",
    "evidence": [
      "investigations/INVESTIGATION_v1.Z.md#NFRA_OPALAI-Z-S40",
      "Get-ScheduledTaskInfo OPAL_D7_ticket_intake: LastRunTime 2026-10-02 10:59:46 ET, LastTaskResult 2 (read 15:0xZ)"
    ],
    "remedy": "OPEN: place an owner for the runner (OPAL_TICKET_VNEXT has no live lane). CP-1's read-back of the next fire will read this failure, which the cutover did not cause, so the cutover sitting must not count it as cutover breakage. Routed to the CTO to place.",
    "owner": "1.0.0_SA_CTO~O",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~O",
      "round": "v2"
    },
    "closed": false
  },
  {
    "id": "NFRA_OPALAI-Z-S42",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Every opal-gateway restart trips the per-identity rate limiter, because all MCP clients reconnect in the same minute: 11 x 429 in OA-e-3's restart minute and 3 in MX-r-4's. A client can drop with rate_limited/identity and then need a manual reconnect. No release guard reads it.",
    "evidence": [
      "investigations/INVESTIGATION_v1.Z.md#NFRA_OPALAI-Z-S42"
    ],
    "remedy": "OPEN: the gateway owner adds a reconnect grace after a restart, or the release guards count 429s in the restart minute. The Analyst's own client is one of the clients that reconnect. Routed to the CTO to place with the gateway's owning project.",
    "owner": "1.0.0_SA_CTO~O",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~O",
      "round": "v2"
    },
    "closed": false
  },
  {
    "id": "NFRA_OPALAI-Z-S51",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "When a commit hook refuses downstream of a passed grade, safe-merge.sh aborts with 'git merge --abort 2>/dev/null || true', so a failed abort is silent and the merge can be left OPEN in the shared tree (MERGE_HEAD present, paths staged). In the S51 case the refusing hook also printed no reason.",
    "evidence": [
      "investigations/INVESTIGATION_v1.Z.md#NFRA_OPALAI-Z-S51",
      ".tools/safe-merge.sh:474-480",
      "commit 490526897d (private-index commit, landed after S51; S51's case was not re-measured against it)"
    ],
    "remedy": "OPEN: check the abort and fail loud when MERGE_HEAD survives it, and surface the refusing hook's output. The tool owner is the box operator; routed through the CTO.",
    "owner": "0.0.0_AB_MSTR~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "0.0.0_AB_MSTR~Z",
      "round": "v2"
    },
    "closed": false
  },
  {
    "id": "NFRA_OPALAI-Z-S53",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The Codex OFFLINE-sandbox loopback block on this box (codex_sandbox_offline_block_loopback_tcp/_udp) is a per-user Windows Firewall Outbound Block, the same shape that F10 measured loopback-exempt. So the Codex offline sandbox does not actually wall loopback here.",
    "evidence": [
      "investigations/INVESTIGATION_v1.Z.md#NFRA_OPALAI-Z-S53"
    ],
    "remedy": "OPEN: the box operator decides the box's Codex sandbox posture: a WFP filter of the OA-f-11 kind, or an accepted risk on record. Routed through the CTO; not chased by NFRA_OPALAI.",
    "owner": "0.0.0_AB_MSTR~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "0.0.0_AB_MSTR~Z",
      "round": "v2"
    },
    "closed": false
  },
  {
    "id": "NFRA_OPALAI-Z-S54",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "wall-dapi-8194-wfp.ps1's Verify() requires the sublayer weight to equal the REQUESTED 0xFFFF. On this box the engine assigns 0xFFE2, because EDR sublayers hold 0xFFFF..0xFFE3. So a correct install prints VERIFY FAIL and exits 4 before its removal step (d).",
    "evidence": [
      "investigations/INVESTIGATION_v1.Z.md#NFRA_OPALAI-Z-S54",
      "git -C opal_ai show nfra-opalai-r2-dev:opal/runtime/provision/wall-dapi-8194-wfp.ps1 :81 (SUBLAYER_WEIGHT = 0xFFFF), :359 (s.weight == SUBLAYER_WEIGHT)"
    ],
    "remedy": "OPEN: compare against the read-back weight and print it, or accept any weight when both filters resolve inside the key (LOCAL, next cut). The script rides the pending G-PUSH to opal_ai PROD unchanged.",
    "owner": "2.0.0_SA_COO~AI",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~AI",
      "round": "v2"
    },
    "closed": false
  },
  {
    "id": "NFRA_OPALAI-Z-S55",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "safe-commit.sh refuses every commit in a sparse worktree whose cone leaves out org/modules/graph. commit_gate_runner.py puts GRAPH_DIR and COMPPROOF_DIR on sys.path and imports comp_constants_cli, so the gate dies on ModuleNotFoundError.",
    "evidence": [
      "investigations/INVESTIGATION_v1.Z.md#NFRA_OPALAI-Z-S55",
      ".tools/commit_gate_runner.py:96 (import comp_constants_cli)",
      "org/modules/graph/comp_constants_cli.py"
    ],
    "remedy": "OPEN: the issuer's sparse-cone recipe holds every directory commit_gate_runner.py puts on sys.path, proven by one dry safe-commit in the cone before the worker is spawned.",
    "owner": "2.0.0_SA_COO~AI",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~AI",
      "round": "v2"
    },
    "closed": false
  }
]
```

-- 3.0.0_SA_CVO~O
