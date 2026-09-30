# HANDOFF -- G-ACCT step 6: sign the Opal_Agent Analyst in to the gateway (for an ELEVATED Claude session)

**From:** `1.0.0_SA_CTO~O` (site Z), 2026-09-30 ~18:2xZ, on Andrew's word: "just write yourself a text handoff, we
can do it now, ill spawn you in there and send you the handoff".
**You run in:** an ADMINISTRATOR PowerShell, as the operator user `Opal Bloomberg`.
**Your identity:**
- Do NOT register on the broker as `1.0.0_SA_CTO~O`; that serial is held by the live non-elevated session.
- Do not commit to the repo.
- Report to Andrew in your terminal.
- NEVER print, echo or log the Claude token or the Opal_Agent password.

## The goal (one outcome)

Opal_Agent's Claude Code is signed in to the MCP server `opal-gateway-bbg` as **Opal Bloomberg**. Proof: inside
Opal_Agent's Claude, the gateway's `whoami` tool answers Opal Bloomberg.
- The sign-in is a browser OAuth that ANDREW completes: he signs in as Opal Bloomberg and approves ONE MFA.
- Your job is to get Andrew an Opal_Agent Claude window that ACCEPTS HIS KEYBOARD, then walk him through `/mcp` ->
  `opal-gateway-bbg` -> Authenticate.
- If a second Microsoft sign-in is asked for, STOP and tell Andrew. Do not request a second MFA.

## Already done (do not redo)

- **Account:** `Opal_Agent` exists, and the boundary check passed (DENIED-OK). Its credential is DPAPI-protected at
  `C:\Users\Opal Bloomberg\.opal_runtime\opal_agent_cred.xml`, and `Import-Clixml` reads it as the operator.
- **Claude token:** Opal_Agent's user env var `CLAUDE_CODE_OAUTH_TOKEN` is SET (108 chars, verified as Opal_Agent at
  17:5xZ). A copy is in AWS Secrets Manager at `opal/opalai/analyst-claude-oauth-token`.
- **Opal_Agent's Claude:** `C:\Users\Opal_Agent\.local\bin\claude.exe`. It is NOT on PATH, so always use the full path.
  Its user-scope MCP server is `opal-gateway-bbg`, pointing at `https://mcp.opalinvest.dev/mcp/`. That is the SAME
  gateway as the operator's `opalgateway`; the separate name keeps the sign-ins separate.
- **Runtime:**
  - checkout `C:\opal_runtime\opal_ai` at PROD `fd8ab8a`, READ-ONLY, so do not edit it;
  - config `C:\opal_runtime\runtime.config.json` (it carries `claude_exe`);
  - state `C:\opal_runtime\state`, where Opal_Agent has Modify;
  - `git config --system safe.directory C:/opal_runtime/opal_ai` is set.
- **One-off launcher** `C:\Users\Opal Bloomberg\.opal_runtime\launch-now.ps1`, run from an ADMIN shell at ~18:0xZ,
  printed `GATE: PASS` and started claude.exe as Opal_Agent. The gate is the checkout's own `launch-gate.ps1`,
  unmodified.

## The blocker you are here to solve

- Windows launched as Opal_Agent FROM THE ADMIN SHELL do not accept Andrew's keyboard. This covers the Claude window
  the launcher opened and fresh `Start-Process powershell -Credential ...` windows.
- A blue Opal_Agent window opened earlier today (~17:06Z) DID accept his typing.
- Working hypothesis: UIPI. A console created from an elevated parent sits above Andrew's medium-integrity input.
- From a NON-elevated operator shell, `Start-Process -Credential` failed with "Access is denied". That was with
  `-NoNewWindow` in one attempt, and `-Wait -RedirectStandardOutput -WorkingDirectory` in another. A plain
  `Start-Process powershell -Credential (Import-Clixml <cred>) -LoadUserProfile` from a non-elevated shell has not
  been isolated.

## What to try, in order (stop at the first that gives a typeable window)

1. **From your admin shell, create a NON-elevated operator shell,** then launch Opal_Agent from it:
   `runas /trustlevel:0x20000 "powershell -NoExit"` gives a basic, non-elevated operator token. In that window, run:
   `Start-Process powershell -Credential (Import-Clixml "C:\Users\Opal Bloomberg\.opal_runtime\opal_agent_cred.xml") -LoadUserProfile`
   Ask Andrew to click into the new blue window and type `whoami`. It must print `opal_bloomberg\opal_agent`.
2. **If "Access is denied",** find which parameter causes it with one-variable tests: plain; then add
   `-WorkingDirectory C:\opal_runtime\state`; and so on. Check the Secondary Logon service (`seclogon`) is running.
3. **Once a window takes his typing,** have him type:
   `cd C:\opal_runtime\opal_ai\opal\runtime` then `C:\Users\Opal_Agent\.local\bin\claude.exe`
   - Trust the folder if asked.
   - `/mcp` -> `opal-gateway-bbg` -> Authenticate -> sign in as Opal Bloomberg -> one MFA.
   - Then ask Claude to "call the opal-gateway-bbg whoami tool". Expect Opal Bloomberg.
4. **Record** what worked (the exact launch command and integrity level) in your final terminal report.
   `1.0.0_SA_CTO~O` turns it into the NFRA_OPALAI launcher fix.

## Context you should not act on

- The gateway is mid-deploy: MX-r-6 v3, GO at ~18:07Z, owned by 2.0.0_SA_COO~MI.
- If the OAuth sign-in errors with a gateway or 5xx failure, wait 5 minutes and retry. Do not touch the gateway.
- Known NFRA_OPALAI launcher defects (for the record; fixing them is not your task):
  1. git stderr under `$ErrorActionPreference='Stop'` with `2>&1` aborts the fetch;
  2. `Start-Process -Credential -NoNewWindow` fails;
  3. the gate's `git status` is refused for "dubious ownership" without `safe.directory`;
  4. `claude.exe` is started by bare name instead of the config's `claude_exe`.
