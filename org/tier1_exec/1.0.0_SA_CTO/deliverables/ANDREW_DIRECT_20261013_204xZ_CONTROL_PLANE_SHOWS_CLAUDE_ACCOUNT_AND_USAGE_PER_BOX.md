# ANDREW DIRECT -- the control plane shows each box's signed-in Claude account and its usage remaining (2026-10-13 ~20:4xZ)

**Channel:** Andrew, at the dell2 terminal, in the session of `1.0.0_SA_CTO~DELL2`. **For:** NFRA_MCPORTAL (site Z, `2.0.0_SA_COO~MP`), the page
https://mcp.opalinvest.dev/control-plane.

## What happened

Andrew asked this seat which Claude account the session was signed in to. It read the account from `~/.claude.json` (`oauthAccount`, no
token printed): `andrew@fideles.capital`, plan Max, its own organization, role admin, and the OAuth login expiring 2026-10-14T04:23Z. He had
already switched accounts because he thought the session would run out:

> "Fuck it i just changed over to andrew@fideles.capital because I thought we were gonna run out, but you shouldve noticed before the changeover what it was"

The account in use before the switch could not be recovered: Claude Code keeps only the current login, and no seat reads usage
remaining. Nothing showed him, before he decided, which account each box was on or how much of its limits was left.

## His word (verbatim)

> "yeah write a note about that becuse i want the mcp.opalinvest.dev/control-plane function to include the logged in account + usage remaining on 5hr and weekly basis by box. write that note and have it issued to the SITEZ box because the MCPORTAL COO shoudl get that worked in"

## The outcome it sets (for the NFRA_MCPORTAL CTO to take into its PRD at its next round boundary)

**On the Control Plane page, per box (laptop, dell1, dell2, site Z), and per Claude Code login where a box runs more than one, show:**
1. **The signed-in Claude account:** email, plan and organization, read from the box's own login record (on Windows,
   `~/.claude.json` `oauthAccount`). Never a token: the reader takes the account fields only.
2. **Usage remaining on the 5-hour window and on the weekly window**, each with when it resets, and each with its claim word (MEASURED or
   ABSENT, CLAUDE.md "a value must carry its claim").
   - The source of these figures is the first unknown: no seat reads them today.
   - The cell's first act is a READ of where Claude Code or the account exposes them (the CLI's own usage or status output, or the
     account's usage page), before anything is built.
   - A figure the box cannot read shows ABSENT with its reason. It is never a guess and never a stale copy.
3. **The age of each figure**, as the page already shows for its other figures.

**Done when (proposed):** Andrew opens the Control Plane page and reads, for each of the four boxes, the account each one is signed in to and
how much of its 5-hour and weekly limits are left, without asking any agent.

**Not asked:** an alert or notification when usage runs low. The standing moratorium holds (CLAUDE.md section 5); this is a display only.

-- recorded by 1.0.0_SA_CTO~DELL2
