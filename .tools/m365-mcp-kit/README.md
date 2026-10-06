# Opal Gateway reconnect (replaces the old local M365 kit)

This kit used to set up a local server. It is retired. Colleagues now use the HOSTED gateway.

1. Remove the old MCP entry (the local one the earlier kit added; also any old "m365" entry):

       claude mcp remove <old-entry-name> -s user

   Run `claude mcp list` to see the name.

2. Add the hosted gateway:

       claude mcp add --transport http -s user opalgateway https://mcp.opalinvest.dev/mcp

3. Authenticate with your work account (opalinvest.com) when the sign-in prompt appears.

An idle client registration expires after 30 days; if the connection is refused, repeat steps 1-3.
