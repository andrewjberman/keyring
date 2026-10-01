# Raw WFP filter to wall Bloomberg DAPI 8194 off Opal_Agent / Opal_MSP on loopback

Prepared by 4.0.0_SA_CRO~O on 2026-10-01 for 1.0.0_SA_CTO~O (msg 28056; ruling
`CTO_RULING_20261001_OPAL_AGENT_DAPI_8194_WALL.md` R2.1).

Read-only. Nothing on the box changed. Web reading was public documentation and issue pages only, on Andrew's
in-session word ("Yes, docs only"); no vendor API was called and no Opal data was sent.

Local evidence:
- `F10_ACCEPTANCE.json` @1552d46a70: 5 of 5 arms OPEN with the per-user Firewall rules live.
- The box is Windows 11 build 26200.
- `netsh wfp show` needs elevation here (non-elevated read: "requires elevation").

## Answer in one line

**Yes. A persistent WFP block filter in OUR OWN sublayer, weighted above the sublayer that holds the loopback permit,
blocks loopback whether that permit is soft or hard.** Microsoft's arbitration rules guarantee it. The per-user
Firewall rules failed because they sit in the same sublayer as a max-weight loopback permit, and within one sublayer
the higher weight wins. One elevated read-only command confirms the permit's sublayer before the install.

## 1. Can an ALE_AUTH_CONNECT filter in its own sublayer beat the firewall's loopback permit? Is that permit hard?

**What Microsoft's arbitration rules say** ([Filter Arbitration](https://learn.microsoft.com/en-us/windows/win32/fwp/filter-arbitration)):
- *Within* a sublayer: "Evaluate matching filters in order [of weight] until a 'Permit' or a 'Block' is returned ...
  Skip the remaining filters." A higher-weight permit in the same sublayer hides any lower block. **This is why the
  per-user Firewall rules are inert.**
- *Across* sublayers: "Actions are evaluated in priority order of sub-layers from highest priority to lowest
  priority. 'Block' overrides 'Permit'. 'Block' is final (cannot be overridden) and stops the evaluation."
- Defaults: "Filter permit | Soft permit"; "Filter block | Hard block".
- A hard permit only stops LOWER-priority sublayers: "In order to silently override 'Hard Permit' filters a firewall
  has to add its filters within a higher priority sub-layer."

**What blocks Codex on this exact build** ([openai/codex #48856](https://github.com/openai/codex/issues/48856),
Windows 11 Pro 26200, Codex 0.157.1):
- A persistent "Boot Time Filter" permits loopback at ALE_AUTH_CONNECT_V4 with weight `18446744073709551615` (the
  maximum).
- Codex's per-user block sits in the same sublayer at a lower weight, so "the higher-weight matching permit can
  preempt the lower Codex block under Microsoft's same-sublayer arbitration rules." Six loopback connections
  succeeded.
- This matches our F10 result exactly.

**Is that permit hard?** Not measured. The arbitration rules make the question moot if our sublayer's weight is
higher than the permit's sublayer, because then our block is evaluated first and is final. If the permit is only
soft, a block in ANY other sublayer wins.

**Conditions are all available at the layer**
([conditions per layer](https://learn.microsoft.com/en-us/windows/win32/fwp/filtering-conditions-available-at-each-filtering-layer)).
FWPM_LAYER_ALE_AUTH_CONNECT_V4/V6 lists:
- `FWPM_CONDITION_ALE_USER_ID`: `FWP_SECURITY_DESCRIPTOR_TYPE`, per
  [condition identifiers](https://learn.microsoft.com/en-us/windows/win32/fwp/filtering-condition-identifiers-);
- `FWPM_CONDITION_IP_REMOTE_PORT`: `FWP_UINT16`, host order;
- `FWPM_CONDITION_IP_REMOTE_ADDRESS`;
- `FWPM_CONDITION_FLAGS`, with `FWP_CONDITION_FLAG_IS_LOOPBACK` valid at ALE_AUTH_CONNECT, per
  [condition flags](https://learn.microsoft.com/en-us/windows/win32/fwp/filtering-condition-flags-).

**Residual (one elevated read-only command, before the install):**
`netsh wfp show filters file=<path>` as Administrator. Find the ALE_AUTH_CONNECT_V4 loopback permit, then record:
- its `subLayerKey` and that sublayer's weight;
- its flags (whether `FWPM_FILTER_FLAG_CLEAR_ACTION_RIGHT` is set).

Then pick our sublayer weight strictly above that sublayer. If it is already at 0xFFFF, the arbitration document
does not say how equal sublayer weights order, and the fallback in section 3 applies.

## 2. The minimal installer: PowerShell `Add-Type` P/Invoke to `fwpuclnt.dll`

**There is no native command that adds a WFP filter.**
- `netsh wfp` offers only `capture`, `dump`, `set` (diagnostic options) and `show` (read locally: `netsh wfp ?`).
- The NetSecurity cmdlets (`New-NetFirewallRule`) create Firewall rules. Those land in `FWPM_SUBLAYER_MPSSVC_WF`
  ("These filters include those from rules added through Windows Firewall",
  [sublayer identifiers](https://learn.microsoft.com/en-us/windows/win32/fwp/management-filtering-sublayer-identifiers)),
  and that is the approach that just failed.

**Shape of one script.** Run elevated, one transaction, about 200 lines of C# inside `Add-Type`, no vendor tool:
1. `FwpmEngineOpen0` (non-dynamic session), then `FwpmTransactionBegin0`.
2. `FwpmSubLayerAdd0`: our own GUID, `FWPM_SUBLAYER_FLAG_PERSISTENT`, weight from the residual read (default 0xFFFF).
3. `FwpmFilterAdd0` twice, at `FWPM_LAYER_ALE_AUTH_CONNECT_V4` and `_V6`, each with:
   - `FWPM_FILTER_FLAG_PERSISTENT` ([FWPM_FILTER0](https://learn.microsoft.com/en-us/windows/win32/api/fwpmtypes/ns-fwpmtypes-fwpm_filter0):
     "survives across BFE stop/start");
   - action `FWP_ACTION_BLOCK`, which is a hard block by default.
4. Conditions, ANDed:
   - `ALE_USER_ID` `FWP_MATCH_EQUAL` a security descriptor built from SDDL
     `O:LSD:(A;;CC;;;S-...-1007)(A;;CC;;;S-...-1008)`. That is Opal_Agent plus Opal_MSP, the same SDDL form Windows
     Firewall itself stores for LocalUser rules on this box.
   - `IP_REMOTE_PORT` = 8194, `FWP_UINT16`.
   - `FLAGS` `FWP_MATCH_FLAGS_ALL_SET` `FWP_CONDITION_FLAG_IS_LOOPBACK`.
5. `FwpmTransactionCommit0`. Print the sublayer and filter GUIDs into the run record, never into a secret store.
6. **Uninstall:** `FwpmFilterDeleteByKey0` for both filters, then `FwpmSubLayerDeleteByKey0`, in one transaction.
   The same script with `-Remove`.

Port 8790 (the view server) and the operator account do not match the conditions, so they stay open by
construction. bbcomm's accept side is a different layer and is untouched.

## 3. Working patterns for blocking loopback

- **WireGuard for Windows kill-switch** ([tunnel/firewall/rules.go](https://github.com/WireGuard/wireguard-windows/blob/master/tunnel/firewall/rules.go)).
  - `blockAll` (ALE_AUTH_CONNECT and RECV_ACCEPT, no conditions, BLOCK) is installed in WireGuard's own sublayer
    beside `permitLoopback` (`FWPM_CONDITION_FLAGS` ALL_SET `FWP_CONDITION_FLAG_IS_LOOPBACK`, PERMIT, higher weight).
  - It needs an explicit loopback permit only because its own-sublayer block otherwise catches loopback. That is
    indirect but production evidence for the section-1 mechanism. (Inference: the file carries no comment saying
    so.)
- **Microsoft:** the only documented per-identity loopback restriction is AppContainer network isolation
  (`FWPM_SUBLAYER_MPSSVC_APP_ISOLATION`). It applies to AppContainer processes, not to a standard user account, so it
  does not fit Opal_Agent without re-hosting the runtime.
- **Estate:** no WFP filter is installed by any Opal script I know of. My 9/30 census found only the three Codex
  Firewall rules (`OPAL_AGENT_DAPI_8194_WALL_RESEARCH_20261001.md`).
- **Fallback if the residual read finds the loopback permit in a sublayer already at 0xFFFF:** remove the agent's
  ability to run arbitrary code instead of walling the port. Deny Bash/PowerShell to the Analyst runtime through
  machine-wide managed Claude settings that Opal_Agent cannot edit. G3 already fences the MCP Bloomberg tools.

## 4. Is the Codex offline loopback block effective? No

- [openai/codex #48856](https://github.com/openai/codex/issues/48856), same build 26200: with networking disabled,
  "loopback TCP/UDP traffic (IPv4, IPv6) successfully reached local listeners". The cause is the max-weight boot-time
  loopback permit in the same sublayer as Codex's block.
- [openai/codex #49840](https://github.com/openai/codex/issues/49840): after forced re-provisioning created
  `codex_sandbox_offline_block_loopback_tcp`/`_udp`, "a direct TCP connect to 127.0.0.1 from the worker still
  succeeds". It also found `codex_sandbox_offline_block_outbound` `Enabled=False`. No maintainer fix is recorded.
- **Locally:** our per-user rules of the identical shape read 5 of 5 OPEN (F10). OA-f-10 worker rows Z-W25-S1/S2
  also found the box's Codex sandbox runs unelevated as the operator. So Codex seats here are not loopback-walled
  either way.

## Recommendation

1. **Run the residual read** (one elevated `netsh wfp show filters`, read-only). It is an Andrew or MSTR~Z act, since
   this seat is not elevated.
2. **Install the section-2 filter pair.** It is Andrew's admin act under his 17:4xZ "sure" for the 8194 wall, as the
   mechanism changes but the outcome does not. Accept on the same 5 arms, expecting Opal_Agent and Opal_MSP on 8194
   REFUSED, 8790 OPEN, operator OPEN. Add a sixth arm after a reboot, for persistence.
3. **Remove the two inert Firewall rules** after the WFP pair passes, so no reader takes them as the wall.
