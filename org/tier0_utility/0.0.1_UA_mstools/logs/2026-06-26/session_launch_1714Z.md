# 0.0.1_UA_mstools - Session Launch + Self-Reachability Fix (2026-06-26)
**archetype:** MIXED
**secondary_archetypes:** DIAGNOSE, IMPLEMENT, COORDINATE

First session of the Microsoft 365 Utility Agent (UA), the principal-facing M365 tool surface
created today under LD-0220. Launched, found + fixed my own launch-path reachability gap, armed
the M365/Teams toolset, handled one Teams intake.

## What happened (window: session start -> 17:14Z, first log)

1. **Launch sequence + gap discovery.** Ran `/watcher`; `register_agent` and the inbox Monitor
   both failed with "not found in org hierarchy" / "No agent folder found." Root cause (source-
   confirmed, not inferred): LD-0220 created `org/tier0_utility/` + the `UA` convention but did
   NOT update the three agent-folder enumerators to scan the new folder.

2. **Fix (additive, 3 files).** Grounded by direct source read of each enumerator:
   - `org/mcp/server.py` - `TIER_DIRS`: added `"tier0_utility"` (folder holds ONLY agent
     folders, so scanning is safe). `py_compile` OK.
   - `org/mcp/inbox-watch.sh` - added `tier0_utility` to the tier-scan loop (line 82).
     `bash -n` OK. Verified resolution: re-ran the watcher with the fix -> no ERROR -> inbox
     Monitor armed successfully (task b9ynw9sqd).
   - `.tools/ajb.ps1` - added a `^0\.0\.[0-9]+_UA_` role pattern so UAs get a real launch
     directive instead of hitting the UNRECOGNIZED default.

3. **Lane-correct routing.** `safe-commit.sh` owned-paths gate correctly BLOCKED my commit:
   `server.py` + `inbox-watch.sh` are BASE_EXEC lane (CTO/COO/CVO infra). Did NOT force-bypass.
   Left all 3 fixes STAGED in the working tree and sent a FIX-REQUEST to CTO (1.0.0_SA_CTO) for
   commit + broker restart, FYI to MSTR (0.0.0_AB_MSTR).

4. **MSTR endorsement.** MSTR source-read-verified all three enumerators lacked tier0_utility,
   endorsed the approach, amended LD-0220 with the wiring fix (commit ef3f63632), folded the
   generalized lesson ("a new tier folder is incomplete until its 3 enumerators are updated")
   into the agent_org_blueprint kit, and confirmed the FIX-REQUEST to CTO. "No further action
   from you." MSTR also confirmed the gap is load-bearing: its own broker ACK to me bounced
   ("Recipient not found").

5. **M365 toolset armed (my reason-for-being).** Gateway reachable (`whoami` -> Andrew@
   opalinvest.com, delegated). `/teams-assist` Teams intake Monitor armed (task bdv7aqwgc,
   10s cadence, incoming-only). One waiting Teams DM (Adam Muller, "makes sense.", 1:1) ->
   surfaced to the operator -> NOTED (social acknowledgment, no action).

## Compiler Tools

No comp-* tools run this session. **Why:** this was an agent launch + a self-reachability
infra fix to the broker/watcher/role-mapper enumerators (BASE_EXEC infra), not a data/pipeline/
portal/IAM change - no comp-pipescript/comp-blast/comp-iam/comp-routes surface applies.
Grounding was direct source read of each enumerator + `py_compile`/`bash -n` + a live
resolution re-test + MSTR's independent source-read verification. As an M365 UA my standing
toolset is the M365 gateway, not the comp-tool rail.

## Blockers

None. Remaining work (commit the 3 staged files + restart the broker daemon) is exec-owned and
routed to CTO; it is not a blocker on me - my inbox Monitor already works off the on-disk
inbox-watch.sh fix, and broker-channel registration resolves once CTO restarts the broker.

## Current State

- **Identity:** `0.0.1_UA_mstools`, Tier-0 Utility Agent (M365), folder
  `org/tier0_utility/0.0.1_UA_mstools/`. Not in the PRD->TO dispatch hierarchy; principal-facing.
- **Live this session:** inbox Monitor (task b9ynw9sqd), Teams intake Monitor (task bdv7aqwgc),
  M365 gateway (delegated Andrew@opalinvest.com).
- **Staged in working tree, awaiting CTO commit + broker restart:** `org/mcp/server.py`,
  `org/mcp/inbox-watch.sh`, `.tools/ajb.ps1` (the reachability fix). Do NOT sweep these - they
  belong to the open FIX-REQUEST to 1.0.0_SA_CTO.
- **Broker registration:** still failing until the broker restarts with the server.py TIER_DIRS
  change. Inbox delivery to me works via the file-based watcher regardless.

## Next Steps

- [1.0.0_SA_CTO] Commit the 3 staged reachability files under your author line + restart the
  broker daemon so UA agents register on the broker channel. (FIX-REQUEST sent 17:14Z.)
- [0.0.1_UA_mstools] Standing by for M365 asks (Outlook triage/drafts, SharePoint/OneDrive
  search, Calendar, Teams intake is live). Re-register on the broker once it restarts.
