# DESIGN -- opal_ai card 3: built in the workspace, run with no workspace access

**Author:** `1.0.0_SA_CTO~O` | **Written:** 2026-09-24 ~20:0xZ | **Asked by:** Andrew-direct, record
`ANDREW_DIRECT_20260924_195xZ_OPAL_AI_CARD3_DEV_IN_WORKSPACE_RUNTIME_WITHOUT_REPO_ACCESS.md` (this folder).
**Status:** design input to the program's L2 and L4. Nothing here has been built or changed on the box.

## 1. The two requirements, his words

- Development: *"I want to develop the opal_ai repo using the ajb_workspace tools, it really is an ajb_workspace
  project just like the portal"*.
- Runtime: *"I just don't want the actual team-facing agents, and ultimately external agents, being so close for
  comfort having ajb_workspace repo access."*

## 2. Why today's Analyst fails the runtime requirement (measured 2026-09-24)

| fact | measurement |
|---|---|
| The Analyst runs as the OS account `Opal Bloomberg`. | `whoami` in this session, same account |
| That account is a local Administrator. | `Get-LocalGroupMember Administrators`: `Administrator`, `Opal Bloomberg` |
| That account has Full control of the workspace. | `icacls ajb_workspace`: `Opal Bloomberg:(F)` |
| Its only barrier is a Claude hook, `bg-concierge-gate.sh`. | `prompt.md`; RCN-0014 finding 2 |
| It shares one Claude credential store and one MCP config with the dev seats, which include Andrew's proxy gateway `opal-gateway`. Its prompt forbids calling it. | `prompt.md` "YOUR IDENTITY BINDING" |
| It can read AWS secrets with the box's AWS profile. | `prompt.md`: `aws secretsmanager get-secret-value --secret-id opal/mcp/opalbloomberg-login` |
| It commits and deploys in the workspace. | commits 5e4e4b5ef0, a798477a11 (LEADPANEL_PRICE), 2026-09-24 |

A hook and a prompt are the whole boundary today. The runtime requirement asks for a boundary that holds even when
the prompt is talked around.

## 3. The design: two planes, split by the operating system

### Plane 1 -- DEVELOPMENT (unchanged from RCN-0015)

- `opal_ai` is a real submodule at `ajb_workspace/opal_ai/`, worked by fabric seats with every workspace gate.
- `DEV` is integration. `PROD` is what runs. Only `0.0.0_AB_MSTR` pushes either, on Andrew's word, as for the portal.
- The parent's pointer bump names the PROD commit that is running.

### Plane 2 -- RUNTIME (new)

1. **A separate, standard (non-admin) Windows account on the terminal box** runs every team-facing agent. It is not
   in `Administrators` and not in `CodexSandboxUsers`.
2. **The workspace is unreadable to it by construction.** Measured: the profile folder `C:\Users\Opal Bloomberg`
   grants only SYSTEM, Administrators and `Opal Bloomberg`. The Desktop and the workspace add `CodexSandboxUsers`
   and one unresolved SID ending `-3194460454`, both with Modify. A new standard account holds none of those, so it
   gets Access Denied.
3. **Its code is a read-only checkout of `opal_ai` PROD** in its own profile. It pulls with a GitHub credential scoped
   read-only to `Opal-Capital/opal_ai` alone. It holds no credential for `ajb_workspace`.
4. **Its Claude setup is its own and narrow:** its own Claude Code login, its own `CLAUDE.md` (the agent's guardrails
   only), its own `.claude/` (the fence hook and the Teams serve skills), and its own MCP config. That config lists
   `opal-gateway-bbg` and the Bloomberg view server only. Andrew's proxy gateway is never configured in that account,
   so the identity mistake cannot happen at all.
5. **No AWS profile in that account.** Anything the agent needs from AWS reaches it through the gateway's tools,
   which already carry the guard chain and the audit record. Its login re-mint moves to the operator.
6. **Its state lives in its own profile:** thread memory, logs and the Teams-watch cursor. Staff conversations stop
   being committed into the workspace's git. Backup of that state is a PRD item.
7. **A launch gate that fails closed.** Before the agent starts, the launcher tries to read one workspace file as the
   runtime account. If the read succeeds, it refuses to launch. That same read is the standing proof of the boundary.

### Release flow

```
seat edits opal_ai/ (submodule, workspace gates) -> DEV -> graded -> MSTR merges DEV->PROD on Andrew's word
  -> runtime account relaunch: git pull --ff-only PROD -> boundary read (must be DENIED) -> agent starts
  -> parent pointer bump names the PROD commit now running
```

### External agents later

These are the same runtime bundle, hosted OFF this box: one host or container per client, and never on a machine
that holds the workspace. The OS account on the terminal box is the V1 form of the same boundary.

## 4. What stays in the workspace

- The Bloomberg daily pull. It is programmatic and runs as OS scheduled tasks, per Andrew; its scripts and tasks do not
  move.
- Development work the Analyst's seat has been doing, such as the LEADPANEL_PRICE deploy this morning. After the split,
  that work belongs to ordinary workspace seats.
- The Bloomberg DAPI view. It is reached through an MCP server whose location is a PRD item, because the runtime
  account cannot run code that lives in the workspace.

## 5. What this design changes from earlier rulings

- **09-22 call 4** (launch inside the product repo) is superseded by this runtime plane.
- **09-22 call 2** (fabric adapter ON in the Opal instance) collides with the runtime requirement. The broker's code is
  `org/mcp/server.py` inside the workspace. It is put to Andrew as call R2.

## 6. Calls for Andrew

| # | call | recommendation |
|---|---|---|
| R1 | Is the V1 runtime boundary on this box a separate non-admin Windows account (creating it is an admin act on the box)? | Yes. It is the only boundary here that does not depend on the agent obeying its prompt. It also separates the credential store and removes Andrew's proxy identity from the agent's reach. |
| R2 | Does the Teams-facing agent keep a fabric connection (the broker), reversing 09-22 call 2? | No broker access. Operator hand-offs go through the gateway (a Teams message to the operator) or a one-way drop folder the workspace reads. Fabric mail into the agent is exactly the closeness he named. |

## 7. What this design does not claim

- The Access Denied result is inferred from the ACLs above. It becomes a measurement only when the account exists and
  the boundary read is run.
- Whether the Bloomberg DAPI loopback port can be reached from a second account was not tested.
- The cost of a second Claude Code login is not assessed.
