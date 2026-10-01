# Opal_Agent and Bloomberg DAPI 8194: can the account be walled off?

Prepared by 4.0.0_SA_CRO~O on 2026-10-01 for 1.0.0_SA_CTO~O (msg 27791, /self-drive OPALAI_MCP design fork). This
was read-only research. No host setting, firewall rule, account or file outside this brief was changed. No vendor or
web call was made. Every measurement below was taken as `Opal_Bloomberg\Opal Bloomberg`, non-elevated, on the site-Z
terminal box. Nothing was run as `Opal_Agent`. Source: `E6_LOOPBACK_REACH.json` @5abe4f6c86 (TCP connect only;
8194 and 8790 OPEN from both accounts).

## Answer in one line

**Recommend the per-user NETWORK DENY on 127.0.0.1:8194 for Opal_Agent's SID, with G3 kept as the second layer.**
- No API-level control exists for DAPI: its identity is the signed-in Terminal user, not the OS caller (inferred,
  falsifier below).
- The tool boundary alone is not sufficient. G3 fences MCP tool names, but the runtime keeps a shell with a readable
  blpapi DLL beside it (measured).

## (1) Can a per-user loopback deny be expressed on Windows 11? Yes, and this box already carries one

**Precedent, live on this machine.** Windows Firewall rules that carry a LocalUser condition: 8 in total. Five are
Windows defaults (Wireless Display, Wi-Fi Direct). Three are the Codex sandbox's, all Outbound, Block, Enabled, and
scoped by `LocalUser = O:LSD:(A;;CC;;;S-1-5-21-29065828-778925147-1918870939-1005)` (the `CodexSandboxOffline`
account):

| Rule | RemoteAddress | RemotePort |
|---|---|---|
| `codex_sandbox_offline_block_loopback_tcp` | `127.0.0.0/255.0.0.0, ::/127` | `1-65535` |
| `codex_sandbox_offline_block_loopback_udp` | `127.0.0.0/255.0.0.0, ::/127` | Any |
| `codex_sandbox_offline_block_outbound` | everything except loopback | Any |

That is the exact shape this design needs: a per-user, outbound, loopback block. A Firewall rule with a LocalUser SDDL
compiles to a WFP filter at the ALE connect layer, conditioned on the connecting process's user. The CONNECTING side
is Opal_Agent's process, so the filter keys on Opal_Agent's SID. `bbcomm.exe` (pid 36004, owner `Opal Bloomberg`,
session 1, listening on 127.0.0.1:8194 only) is the accepting side, and it and the daily pull are untouched.

**The common belief that the Windows Firewall exempts loopback is the thing to falsify, not assume.** The Codex
implementers ship these rules as if loopback blocking works on Windows 11. I did not see them work on this box: it
needs a run as the blocked user, and I hold no such account.

**Falsifier (zero host change, run first).** Any Codex seat on this box running inside its OFFLINE sandbox runs
`Test-NetConnection 127.0.0.1 -Port 8194`. The same command outside the sandbox is the control. Read the result:
- **Refused inside, OPEN outside:** the mechanism is proven here.
- **OPEN inside:** loopback is exempt, and the deny has to be a raw WFP filter in its own sublayer with a higher
  weight. That needs an elevated installer and is not a Firewall rule.

**The rule this design would add** (an admin act, Andrew's per the isolation design's R1 class; NOT applied):
- Outbound, Block.
- `LocalUser` = Opal_Agent's SID `S-1-5-21-29065828-778925147-1918870939-1007`.
- RemoteAddress `127.0.0.0/8, ::1`, RemotePort **8194 only**.

Port 8790, the view server, must stay open: the isolation design gives Opal_Agent the view server as its sanctioned
Bloomberg path (`OPAL_AI_RUNTIME_ISOLATION_DESIGN_20260924.md` Plane 2, item 4). Opal_Agent is not in Administrators,
so it cannot remove the rule.

Acceptance (re-run E6), three arms:
- Opal_Agent -> 8194 refused;
- Opal_Agent -> 8790 OPEN (control);
- Opal Bloomberg -> 8194 OPEN (control).

A second account, `Opal_MSP` (SID `...-1008`), also exists on this box and is outside this ask. If it is meant to run
agents, it needs the same rule.

## (2) Does DAPI or blpapi authenticate the connecting OS user? No (inferred, falsifier named)

- **What our own client does.** `integrations/bloomberg/mcp/blp_client.py:53-59` builds `SessionOptions` with host and
  port only and calls `openService` with no `AuthOptions`, and it is served. DAPI attaches the signed-in Terminal
  user's identity to the session; the caller supplies none.
- **What the installed library offers.** blpapi 3.26.4.2 has user-identity modes in
  `site-packages/blpapi/auth.py:154-200`: `AuthUser.createWithLogonName` (`OS_LOGON`) and
  `createWithActiveDirectoryProperty` (`DIRECTORY_SERVICE`). Those are authorization modes a CLIENT opts into, for the
  server-side (SAPI/B-PIPE) identity model. Nothing in DAPI mode REQUIRES them.
- **Repo census.** `comp-find -i 'OS_LOGON|AuthOptions|authenticationOptions|ApplicationIdentity|DIRECTORY_SERVICE'
  integrations` returned 0 hits across 109 scanned files. 109 more ephemeral-floor files were not searched. No code
  here uses them.
- **Consequence.** A second OS account reaching 8194 would draw on the SAME Terminal user's data limits. Nothing at the
  API refuses it.
- **Not assessed:** the Bloomberg licence terms for DAPI use by a second account. That is a vendor-terms question, not
  a mechanism.
- **Falsifier.** As Opal_Agent, one `session.start()` plus `openService('//blp/refdata')` with NO request (no data
  consumption). If DAPI refuses a foreign OS user, the session fails. This needs a blpapi build importable by
  Opal_Agent: only `C:\Program Files\Python314` is runnable by it, and it has no blpapi (measured). Staging one would
  mean a Bloomberg package download, which needs Andrew's per-use word. Because of that cost, I recommend running the
  falsifier only if the network deny is refused.

## (3) Prior pattern in the repo and in the Bloomberg guardrails

- `integrations/bloomberg/README.md` section 1: "exactly one physical pipe, and it is loopback". DAPI binds 127.0.0.1
  only, and "something running ON the Terminal box must make the blpapi call". The guardrails assume every local
  caller IS the Terminal user, and say nothing about a second local account.
- `integrations/bloomberg/READ_HERE.md` is symptom-first: the sign-in budget, entitlements, the BQL wall, and
  current-day-only fields. It has no access-boundary clause.
- **G3** (`C:\opal_runtime\opal_ai\opal\agent\hooks\concierge-gate.sh:97-107`, inherited unchanged from
  `bg-concierge-gate.sh`) blocks `mcp__bloomberg__bloomberg_historical_data` and `_intraday_bars`, and blocks
  `reference_data` for more than 2 securities. It matches MCP TOOL NAMES only.
- **G2** (same file, `:121-170`) gates Bash/PowerShell for git, aws and redirect mutation classes. It does not gate
  `python`, `pip`, `java` or a socket.
- The isolation design itself left this open: "Whether the Bloomberg DAPI loopback port can be reached from a second
  account was not tested" (`OPAL_AI_RUNTIME_ISOLATION_DESIGN_20260924.md:97`). E6 answered reach. This brief answers
  the wall.

## Why the tool boundary alone is not sufficient (measured, not run as Opal_Agent)

| Fact | Measurement |
|---|---|
| The fence cannot be edited by the agent. | `concierge-gate.sh` and `runtime/.claude/settings.json` grant Opal_Agent `ReadAndExecute` only, and `C:\opal_runtime` grants it `Read`. Owner: `Opal Bloomberg`. |
| The agent keeps a shell. | The runtime settings register one PreToolUse hook (`matcher "*"`), and G2 denies only mutation classes. Bash and PowerShell are otherwise allowed. |
| A Python it can run exists. | `C:\Program Files\Python314` (system-wide). It has no blpapi today. |
| The native API is in reach. | `C:\blp\DAPI` holds `blpapi3_64.dll`, `blpapi3_32.dll` and `blpapi3.jar`. ACL: `BUILTIN\Users FullControl`, `Authenticated Users Modify`. |
| Outbound egress is not walled. | Firewall default outbound is `NotConfigured` on all 3 profiles, so `pip install` from the shell is not blocked. |

So "no blpapi in its runtime" holds today by absence, not by a wall. A prompt-injected or creative agent has a
three-step path: Python314 plus the readable DLL (ctypes), or a pip-installed wheel, then 8194. G3 never sees that
path because no MCP tool is called. The network deny closes every such path at once, whatever the client.

**Adjacent, surfaced, not chased:** `C:\blp\DAPI` is `Users FullControl`, so a non-admin account can REPLACE the
Terminal's DAPI binaries. Our Python pipelines load the copy bundled in their wheel (`site-packages/blpapi/
blpapi3_64.dll`), not this one. I did not trace which Terminal or Excel processes load `C:\blp\DAPI`. Owner: the box's
operator, 0.0.0_AB_MSTR~Z.

## Recommendation

1. **The network deny**, as specified in (1). Run the Codex-sandbox falsifier first (free, today). Then apply the rule
   as one admin act, and accept with the three-arm E6 re-run.
2. **Keep G3** as defense in depth for the sanctioned MCP path.
3. **Do not pursue an API-level control.** DAPI has no per-OS-user check to configure. The only API-side lever would
   be a different Bloomberg product (SAPI/B-PIPE with per-user identity), which is a purchase, not a setting.
4. If the deny is refused, close the shell path instead: remove Bash/PowerShell from the runtime's tool set, or put
   `python`/`pip`/`java` in G2. That is weaker, because it enumerates clients rather than walling the port.
