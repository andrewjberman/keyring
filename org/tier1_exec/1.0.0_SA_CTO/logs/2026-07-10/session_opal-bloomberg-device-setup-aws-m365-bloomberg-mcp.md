# CTO Session Log -- "Opal Bloomberg" second-device setup: env parity, operator.py shadow fix, M365 MCP, and a live Bloomberg MCP -- 2026-07-10

**archetype:** MIXED
**secondary_archetypes:** IMPLEMENT, COORDINATE, DIAGNOSE, EXPLORE

**Authoring note:** authored as `1.0.0_SA_CTO` at Andrew's direct instruction, on the new
`Opal Bloomberg` Windows device. **This device is a plain COPY of ajb_workspace, NOT a git
checkout** (`git rev-parse` -> `fatal: not a git repository`), so this log is WRITTEN to
`org/tier1_exec/1.0.0_SA_CTO/logs/2026-07-10/` but **cannot be committed here** (no
`safe-commit.sh` path). It must be ferried to the canonical repo (origin `AndrewBerman`
machine / CLOUD) to land under the CTO author line. Flagged in Blockers.

## Summary

Andrew stood up a **second physical device** ("Opal Bloomberg") and directed a full
environment + tooling bring-up: (1) bootstrap a near-bare Windows box to run the fabric
locally; (2) install "everything we need" per the consolidated estate `requirements.txt`;
(3) reach AWS + the Opal M365 MCP at parity with the origin machine; (4) the load-bearing
objective -- **this box has a live Bloomberg Terminal**, and Andrew wants its local Desktop
API exposed as tooling on the Opal MCP server, tunneled AWS-natively. All local work is DONE
and verified; the remaining legs are auth/admin-gated on Andrew + CloudOps.

## Work done this window

1. **MSTR seat + Tier-0 law (COORDINATE).** Session opened with "assume role of 0.0.0_AB_MSTR";
   read Const v1.5 / Stakes v1.5 / Directives v1.12 in full (Art. XII). Then Andrew redirected
   to device setup (Art. I sovereign direct). This log is the CTO-lane record of that setup.

2. **Environment bootstrap (IMPLEMENT).** Box had ONLY git 2.55. Installed via winget:
   **Python 3.11.9** (deliberately 3.11 not 3.12 -- the estate's pinned `torch==2.1.2+cpu` /
   `sentencepiece==0.1.99` predate 3.12 wheels), Node 24.18 / npm 11.16, bun 1.3.14, Terraform
   1.15.8, gh 2.96. **AWS CLI v2 (2.35.21)** via no-admin `msiexec /a` extract (the standard
   MSI 1603'd -- needs admin; the `/a` administrative-extract to a user dir does not), wired
   ahead of the pip shim; removed the pip awscli v1 so `aws` is unambiguously v2.

3. **Python inventory install (IMPLEMENT).** Materialized the consolidated `requirements.txt`
   (83 pkgs, from Andrew's email -- it was NOT present on this copy). The aggregate inventory
   is **internally contradictory** (`urllib3==2.6.3` vs `botocore==1.34.28`->`urllib3<2.1`),
   so a single environment CANNOT honor all 61 source pin-sets -- installed **name-resolved**
   to one coherent set (torch CPU trio from the PyTorch index; jupyter stack excluded on the
   Windows 260-char path limit + no admin). 190 packages total, `pip check` clean. Added the
   local-tool deps the inventory MISSED but comp-tools/commit-gate import: **`duckdb kuzu
   psutil ruff==0.15.11`**. `blpapi 3.26.5.1` from Bloomberg's index.

4. **DIAGNOSE + FIX: `.tools/operator.py` stdlib shadow.** `python .tools/*.py` crashed on
   import: running a script in `.tools/` puts `.tools/` on `sys.path[0]`, so `.tools/operator.py`
   (the project-closure DISPATCHER) **shadows the stdlib `operator`** that `datetime`/`collections`
   import -> every tool broke. `-P` rescues self-contained scripts but breaks comp-tools (they
   need sibling imports), so rename was the correct fix. **Renamed `operator.py` ->
   `operator_tool.py`** (command name `operator` unchanged via the `.tools/operator` shim, so
   NO caller changes); updated the shim, the `render_shim` exec path, the FUNCTIONAL
   `_source_line(".tools/operator.py")` reads in `inbox-resolver-conformance.py`, and the live
   diagnostic strings in `fabric-check.py` + `exec-toolkit.yaml` + COO `prompt.md`. Left all
   immutable audit records (logs/ledger LD-0269/drive_logs/task_orders) untouched -- they
   correctly preserve the historical `operator.py:539` name. **Verified:** `registry-check.py`
   now runs WITHOUT `-P` (previously crashed).

5. **M365 MCP (COORDINATE/IMPLEMENT).** Confirmed `NFRA_OPLMCP` is the remote per-user M365
   gateway (`https://mcp.opalinvest.dev`, ALB+OIDC, MCP-OAuth AS facade + Dynamic Client
   Registration -- verified `/.well-known/oauth-authorization-server` returns live metadata).
   Registered per Andrew's counterpart-guide: `claude mcp add -s user -t http m365
   https://mcp.opalinvest.dev/mcp/`. Shows `! Needs authentication` -- pending Andrew's browser
   OAuth. (Gateway also serves ycharts tools.)

6. **Bloomberg Terminal discovery + MCP build (EXPLORE -> IMPLEMENT).** Probed the box:
   **Bloomberg Terminal is INSTALLED + RUNNING** (`C:\blp\{API,DAPI,Wintrv}`, bbcomm/wintrv/
   blpwtk2 processes) with **DAPI LISTENING on `127.0.0.1:8194`**. No prior blpapi integration
   in the estate -- greenfield. Built a read-only Bloomberg MCP at **`.tools/bloomberg-mcp/`**:
   `blp_client.py` (thin `//blp/refdata` wrapper -- reference/historical/intraday, no trade
   service) + `server.py` (FastMCP, 4 tools) + `README.md`. **Verified live**: health OK;
   reference AAPL 315.32 / SPX 7575.39; AAPL historical 2026-07-01..09 (6 daily bars).
   Registered user-scope stdio -- `bloomberg` shows **Connected**. Andrew CLEARED DAPI
   redistribution (2026-07-10), so multi-user exposure is authorized (was the S3 gate).

7. **AWS-native SSM tunnel design (IMPLEMENT/COORDINATE).** Bloomberg can't move off this box
   (license + localhost). Designed the estate-blessed path (NFRA_OPLMCP PRD prefers SSM +
   Verified Access over Cloudflare/Tailscale): device as an **SSM hybrid-activated managed
   instance** -> `server.py` streamable-http on `127.0.0.1:8790` -> gateway/agents reach it via
   **SSM port-forward** (outbound-only, IAM-scoped, audited). Full runbook in
   `.tools/bloomberg-mcp/README.md`. Andrew confirmed AWS-native is preferred.

## MCP traffic (this window)

None on the opal-agent-comms broker -- this device is not registered on the fabric broker (no
git checkout, broker not running here). All coordination was direct with Andrew in-session +
two relayed emails from the counterpart MSTR (AWS/M365 setup guide; consolidated requirements).

## Compiler Tools

| Tool | Result | Note |
|---|---|---|
| `python .tools/registry-check.py` | PASS | hot=0 cold=63 malformed=1 (BD_RPSAUTO.json); the definitive test that the operator.py shadow fix works (runs WITHOUT -P) |
| `python .tools/inbox-resolver-conformance.py` | PARTIAL | imports clean post-fix (no more shadow crash); stops later on `BASH not found` -- a separate env gap (Git Bash not on the Python subprocess PATH), not the operator fix |
| `python .tools/bloomberg-mcp/blp_client.py` (+ server import) | PASS | new tool; health/reference/historical all return live Terminal data; 4 MCP tools register |
| `pip check` | PASS | 190 packages, no broken requirements after name-resolved install |

**What worked:** grounding the operator.py failure in the actual traceback (stdlib shadow, not
a missing lib) avoided a wrong fix; probing the box directly proved the Bloomberg DAPI live
before any build. **What failed:** the estate `requirements.txt` cannot install as a lockfile
(contradictory aggregate pins) -- name-resolution was required. **Gap found:** the consolidated
`requirements.txt` OMITS `duckdb`, `kuzu`, `psutil`, and `ruff` that local comp-tools /
commit-gate import -- CloudOps should fold these into the canonical inventory. comp-graph tools
(comp-which/comp-kuzu/comp-blast) were NOT run: this is a non-git device-setup task with no
Nessie surface here; the graph checks ride the canonical-repo TOs when this work is ferried.

## Files created / modified (this device; UNCOMMITTED -- no git here)

- `.tools/operator_tool.py` (renamed from `operator.py`) + docstring rename-rationale header.
- `.tools/operator` (shim exec path), `.tools/inbox-resolver-conformance.py`,
  `.tools/fabric-check.py`, `org/modules/exec/exec-toolkit.yaml`,
  `org/tier1_exec/2.0.0_SA_COO/prompt.md` -- operator.py -> operator_tool.py references.
- `.tools/bloomberg-mcp/{blp_client.py, server.py, README.md}` -- NEW read-only Bloomberg MCP.
- `requirements.txt` (repo root) -- materialized from the emailed inventory.
- This log.

## Current State (zero-context handoff)

- **Device:** `Opal Bloomberg` Windows 11 box, user `Opal Bloomberg`. `Desktop/ajb_workspace`
  is a COPY, no `.git`; portal submodule empty. Runs the fabric locally; cannot commit/push/deploy.
- **Runtime:** Python 3.11.9 at `%LOCALAPPDATA%\Programs\Python\Python311\python.exe` (on PATH);
  190 pip pkgs incl. blpapi 3.26.5.1; AWS CLI v2 at `%LOCALAPPDATA%\Programs\AWSCLIV2\...\aws.exe`
  (region us-east-1, output json PRE-STAGED; NO creds yet -- `~/.aws` credentials absent).
- **MCP (user scope, `~/.claude.json`):** `m365` -> https://mcp.opalinvest.dev/mcp/ (Needs auth);
  `bloomberg` -> local stdio (Connected). Repo `.mcp.json` servers (playwright/deck/opal-agent-comms)
  carry origin-machine `C:\Users\OPALBL~1\...` paths -- broken here, parity cleanup pending.
- **Bloomberg:** Terminal live, DAPI `127.0.0.1:8194`; MCP at `.tools/bloomberg-mcp/`, read-only,
  verified against live data. Redistribution cleared by Andrew.
- **AWS target:** account 313476888478, IAM user Andrew_Berman.

## Next Steps

- **[Andrew]** AUTH LEG 1 -- AWS: IAM console -> Andrew_Berman -> create access key (CLI) ->
  send it; MSTR runs `aws configure` + verifies `aws sts get-caller-identity` ->
  `arn:aws:iam::313476888478:user/Andrew_Berman`.
- **[Andrew]** AUTH LEG 2 -- M365: restart Claude Code (pick up `m365`+`bloomberg`), run `/mcp`,
  approve the Microsoft browser sign-in as Andrew@opalinvest.com; confirm `mcp__m365__whoami`.
- **[Andrew + 0.7.0_AE_CloudOps]** SSM TUNNEL: grant this device one-time admin for the SSM
  Agent MSI; provision the IAM hybrid-activation (`AmazonSSMManagedInstanceCore`, scoped to the
  `mi-...` id); then MSTR runs `server.py` streamable-http :8790 + wires the SSM port-forward,
  and registers the forwarded endpoint behind the Opal MCP gateway. Runbook: `.tools/bloomberg-mcp/README.md`.
- **[0.7.0_AE_CloudOps]** fold `duckdb/kuzu/psutil/ruff` into the canonical `requirements.txt`;
  fix the `.mcp.json` playwright path to be machine-relative.
- **[1.0.0_SA_CTO / origin repo]** FERRY: land this session's file edits (operator_tool.py rename
  + `.tools/bloomberg-mcp/`) into the canonical CLOUD repo via safe-commit, arch-gated as needed;
  the operator.py rename touches a fabric-wide tool -- coordinate with COO (owns DRIVE.md/prompt.md
  refs) + the LD-0269 :539 investigation owners (the dispatcher line shifted +3 on the docstring header).

## Blockers

- **This device has no git repo** -> this log + all code edits are UNCOMMITTED here; they must be
  ferried to the canonical repo to land. Evidence: `git rev-parse --show-toplevel` ->
  `fatal: not a git repository`. Not a fabric-work blocker; a device-topology fact.
- **AWS connection** BLOCKED on Andrew's access key (in flight). **M365** BLOCKED on Andrew's
  browser OAuth. **SSM tunnel** BLOCKED on AWS creds + one-time admin + IAM activation. All three
  are Andrew/CloudOps actions, not lane-blocked work.
