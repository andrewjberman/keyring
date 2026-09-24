# Andrew-direct 2026-09-22 -- align this device's opal-gateway MCP servers to the updated "opalgateway"; delete the old; port opal-gateway-bbg under its old name for 0.0.3_BG_BBGTerminal

**Recorded by:** `4.0.0_SA_CRO~Z`, at this terminal (site Z), before any act on it. **Channel:** Andrew, direct, in
this session.

## Verbatim, entire

> I need your help in quickly adjusting the opalgateway and opalgateway bbg variant mcp servers on this device. we
> have since updated these (now known as opalgateway) and i want to make sure they are properly set up here. travel
> down the rails of the Graph API i am now a cloud application administrator and owner. I want to make sure that we
> are using the most updated version on this device and that the old versions are properly deleted. I think we also
> will need to port over the old opal-gateway-bbg with same naming and etc so 0.0.3_BG_BBGTerminal agent can still
> use it.

## Reading, narrow

1. Scope is THIS DEVICE's MCP server configuration for the two gateway servers (`opal-gateway`, `opal-gateway-bbg`),
   now consolidated under the name "opalgateway".
2. Asked: (a) confirm the device runs the most updated version; (b) delete the old versions properly; (c) keep an
   `opal-gateway-bbg` entry under the SAME name so `0.0.3_BG_BBGTerminal` keeps working.
3. Context he gives: he is now a Cloud Application Administrator and owner on the Graph API side (Entra), so the
   app-registration rails are his to walk; this seat works the device side.
4. Not asked: any change to the gateway's cloud deployment, any credential handling beyond what the config already
   references, any act on another device. Device-config acts here are reversible (a backup is taken first).
