# NFRA_MCPMSP task order -- `MS-t-3` -- ROUND 1, hop 4 files: the partner Analyst's harness, on the shared scripts

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPMSP/decompositions/NFRA_MCPMSP_DECOMP.md</decomp_doc>
<owned_cells>MS-t-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_MCPMSP~4</issued_to>
<issued_by>2.0.0_SA_COO~MS</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- nothing reaches AWS.
comp-adversary: DECLARED-NOT-APPLICABLE -- thread round; AC2's default-config arm is the difference control.
EGRESS CLASS, declared: none.
</preflight>

## 1. THE CELL -- `MS-t-3` (decomposition section 2)

The partner pilot runs as ONE supervised Claude Code session under its OWN dedicated non-admin Windows account on this
box, provisioned with the SAME scripts as the internal Analyst `Opal_Agent` but a separate account and credential;
partner traffic never runs as the internal Analyst's identity (PRD C8). Its one MCP server is the Opal gateway (C1).

The scripts live in the nested repo `opal_ai` (branch DEV), under `opal/runtime/`: `provision/provision-account.ps1`,
`provision/verify-boundary.ps1`, `launcher.ps1`, `launch-gate.ps1`, each configured by a JSON file
(`provision/runtime.config.example.json`: `checkout_dir`, `state_dir`, `workspace_probe_file`, `prod_ref`). Measured at
opal_ai DEV `fd8ab8a57f`: all four HARD-CODE `$AccountName = 'Opal_Agent'`, and the operator-side credential file is
hard-coded `opal_agent_cred.xml` (`provision-account.ps1:160`, `verify-boundary.ps1:30`).

Build, in your nested `opal_ai` worktree:
1. **An `account_name` config key** read by all four scripts. ABSENT = `Opal_Agent`, and every behaviour with the
   existing example config stays byte-for-byte what it is today (the internal Analyst must not move). Every
   account-derived path follows the name: the credential file becomes `<account_name lowercased>_cred.xml`, so the
   default stays `opal_agent_cred.xml`. Validate the name (a Windows local-user name; refuse anything else loudly).
2. **`opal/runtime-msp/` (new)**, the partner runtime beside `opal/runtime/`:
   - `CLAUDE.md`: names the agent the Opal MSP Analyst; it answers partner advisors ONLY through the gateway tool
     `opal_asker_query` (citing the chat and message ids of the question it answers), states the data's date on every
     figure, and sends NOTHING at all when the tool refuses (no apology, no reply -- PRD C3, "the agent should not
     even respond"). Import the shared guardrails the way `opal/runtime/CLAUDE.md` does only where they apply to a
     partner; no Bloomberg, no internal-only tool.
   - `.claude/settings.json`: the same fence as `opal/runtime/.claude/settings.json` (the concierge-gate hook), pointed
     at the same hook file.
   - `mcp.json.example`: `mcpServers` with EXACTLY ONE server, the gateway at `https://mcp.opalinvest.dev/mcp`, signed in
     through the gateway's own OAuth as the Opal Analyst Microsoft 365 user (G-USER, not yet created); nothing else.
   - `provision/runtime.msp.config.example.json`: the four existing keys for an `Opal_MSP` layout
     (`C:\opal_runtime_msp\opal_ai`, `C:\opal_runtime_msp\state`, the same workspace probe file, `PROD`) plus
     `"account_name": "Opal_MSP"`.

**AMENDMENT 1 (issuer, 2026-09-30, on the CTO's release ruling msg 27126).** The four shared scripts are NFRA_OPALAI's;
its `OA-t-3` round-2 order (`NFRA_OPALAI.TO-OA-t-3.r2-runtime-setup-launch-gate-fence.md`) will edit them later and
is held on Andrew's acts, unstarted. The CTO released this cell to edit them now, on two conditions you must meet:
- an ABSENT `account_name` key means `Opal_Agent` with BYTE-IDENTICAL behaviour (AC2's default-config arm is that
  proof);
- your nested `opal_ai` commit message NAMES `OA-t-3` (e.g. "additive account_name key, default Opal_Agent -- read by
  NFRA_OPALAI OA-t-3 r2") so that order's issuer sees it.

## 2. BOUNDS

1. Write surface: the four scripts and `opal/runtime-msp/**` EXCEPT `opal/runtime-msp/record/` (the next order in your
   queue owns that). `opal/agent/**` and `opal/runtime/CLAUDE.md`/`.claude/`/`mcp.json.example` are read-only.
2. Nothing is provisioned here (no account, no directory, no credential): `-Plan` only. The account is `MS-a-3`'s.
3. Commit in the nested `opal_ai` repo on your branch; no push (opal_ai DEV/PROD pushes are `0.0.0_AB_MSTR~Z`'s on
   Andrew's word). REFUSE a criterion you cannot meet as written, with its measurement.

## 3. SURFACES

<paths>
opal_ai/opal/runtime/provision/provision-account.ps1
opal_ai/opal/runtime/provision/verify-boundary.ps1
opal_ai/opal/runtime/launcher.ps1
opal_ai/opal/runtime/launch-gate.ps1
opal_ai/opal/runtime-msp/CLAUDE.md
opal_ai/opal/runtime-msp/.claude/settings.json
opal_ai/opal/runtime-msp/mcp.json.example
opal_ai/opal/runtime-msp/provision/runtime.msp.config.example.json
org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/0.9.0_WK_NFRA_MCPMSP~4/**
org/missions/D6/NFRA/NFRA_MCPMSP/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

Read, never write: `opal_ai/opal/runtime/**` (other than the four scripts), `opal_ai/opal/agent/**`,
`org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/2.0.0_SA_COO~MS/round1/checks/`.

Your worktree carries a nested `opal_ai` checkout at DEV (provisioned with `wk-provision.sh --nested opal_ai=<DEV ref>`);
the checks read `opal_ai/` inside your parent worktree. Rows: `INVESTIGATION_v1.Z.md`, id `NFRA_MCPMSP-Z-W4-S<k>`,
`disarm_owner` `2.0.0_SA_COO~MS`.

## 4. PROOF OF SPEC (literal; run from your parent worktree root after your nested commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MS-t-3"><invocation>bash org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/2.0.0_SA_COO~MS/round1/checks/t3.AC1.sh; echo "exit=$?"</invocation><expect>claude_md=y settings=y one_server=y msp_account=y provision-account.ps1=y verify-boundary.ps1=y launcher.ps1=y launch-gate.ps1=y verdict=OK -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MS-t-3"><invocation>bash org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/2.0.0_SA_COO~MS/round1/checks/t3.AC2.sh; echo "exit=$?"</invocation><expect>default config -> PLAN: CREATE-USER Opal_Agent; msp config -> PLAN: CREATE-USER Opal_MSP -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/0.9.0_WK_NFRA_MCPMSP~4/NFRA_MCPMSP.TO-MS-t-3.msp-harness-files.proof_of_spec.json`.
Report once, with: every account-derived path you keyed by name; the two check lines; the nested opal_ai commit hash
and your parent branch's commit hash; any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-1 issuance (CTO msg 26985). HELD at issuance: slot `~4` spawns only after NFRA_OPALAI's
`OA-t-3` round-2 order (`NFRA_OPALAI.TO-OA-t-3.r2-runtime-setup-launch-gate-fence.md`, `pending` at the cut) is
terminal, because it writes `launcher.ps1` / `launch-gate.ps1` (decomposition sequencing (a)); the nested ref at spawn
is opal_ai DEV HEAD at that time. Checks dry-run at base: AC1 FAIL as expected (all eight n: the parent tree's
`opal_ai` gitlink is the README-only `90ca424fc7`); AC2 FAIL as expected (script absent at the gitlink). AC2's
default arm controlled against opal_ai DEV `fd8ab8a57f` bytes: `-Plan` prints `PLAN: CREATE-USER Opal_Agent` and eight
plan lines, no act. Slot `~4` continues to MS-t-4, then MS-a-3.

**AMENDMENT 1 (issuer):** the hold on sequencing (a) is RELEASED by the CTO (msg 27126: "released. MS-t-3 may edit
opal_ai/opal/runtime/{launcher,launch-gate}.ps1 and provision/*.ps1 now"; OA-t-3 r2 is held on Andrew's G-ACCT/G-AUTH,
unstarted). Conditions carried onto the face: byte-identical no-key behaviour; the commit names OA-t-3. Spawn at
opal_ai DEV `fd8ab8a57f`. No criterion changes. Graded by: no gate limb grades a modification's criteria.

<status>staged</status>
<round>1</round>
<slot>~4</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
