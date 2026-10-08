# ANDREW-DIRECT 2026-10-08 ~17:0xZ -- graph coherence calls: hook on every box yes; engine goes to a new CRO

**Channel:** Andrew at the 4.0.0_SA_CRO terminal, laptop, 2026-10-08 ~17:0xZ (13:0x ET), answering this seat's
/open-calls cards of ~13:0x ET (call 1: install the commit hook on every box; call 2: graph engine).

## Verbatim

> Call 1, sure. Call 2, i will spawn another CRO agent to drive this, just write a handoff on it. You should proceed with your work in the interim past that and dont need to worry about it

## Placement (no scope adjudicated)

- Call 1, YES: every box installs the fabric-activity post-commit hook (`.tools/git-hooks/install-fabric-activity.sh`),
  each box's MSTR running the installer once the tool is on the trunk.
- Call 2: the engine decision passes to a CRO seat Andrew spawns. This seat writes a handoff
  (`GRAPH_ENGINE_HANDOFF_20261008.md`, same folder) and carries on with the activity build.
