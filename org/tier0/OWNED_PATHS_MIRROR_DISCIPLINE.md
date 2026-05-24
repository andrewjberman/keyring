# Owned-Paths Mirror Discipline — Cross-Fabric Maintenance Doctrine

**Status:** v1.0 — 2026-05-24 (LD-0046 establishment; Andrew Option A+ ratification 2026-05-24T20:23Z)
**Authority:** Canonical reference doc, **NOT TIER0_LAW lock**. Operational tuning surface; amendable via successor LD-NNNN.
**Fabric scope:** `[ajb_workspace, feature_clb]` per CONSTITUTION Art. XV.
**Tier-0 commit hash at establishment:** `2d5fdc03f`

---

## §1 — Purpose

Both `ajb_workspace` and `feature_clb` maintain their own `.owned-paths.yaml` files since 2026-04-24. The files declare path-to-agent-lane mappings used by each fabric's pre-commit hook (`.tools/git-hooks/owned-paths-check.sh`) to validate commits against agent serial.

Under CONSTITUTION Art. XV fabric-fungible governance + LD-0031 Path B canonicalization, **lane-class definitions are fabric-shared canon** while **path-to-lane mappings remain fabric-local**. This doctrine codifies the Mirror Discipline required to prevent drift between the two fabrics' shared canon.

Andrew sovereign ratification 2026-05-24T20:23Z verbatim: *"I concur on Q-A. Its far betteer to keep ownedpaths separate in mirrored format."* Option A+ chosen over Option B (Tier-0 canonical lanes file) for operational simplicity + locally-self-sufficient hook behavior.

---

## §2 — The Mirror Discipline

### §2.1 — What MUST mirror across both fabrics

For each lane class (BASE_EXEC, COMP_LEARNS, ANY_CTO, TIER0_LAW, INTER_FABRIC, etc.), the following fields MUST be identical across both fabrics' `.owned-paths.yaml` files:

| Field | Mirror requirement |
|---|---|
| Lane name | Identical string (case-sensitive) |
| `permitted_agents` list | Identical agent-serial list (order-insensitive); cross-fabric agents (e.g., ws CTO listed in CL fabric's BASE_EXEC) are explicitly canonical |
| `description` field | Substantively identical; minor formatting drift acceptable (e.g., line-wrap differences) |

### §2.2 — What stays fabric-local

| Field | Locality |
|---|---|
| `paths:` mappings (path-glob to lane-name) | Each fabric maps own paths; path classes need not exist in both fabrics |
| `rollout_phase` (warn vs fail-closed) | Independent per-fabric operational choice |
| File header comments + dating | Fabric-local |

### §2.3 — Why this split

- **Lane-class definitions describe WHO** — cross-fabric (an agent like `1.0.0_SA_CTO` exists across both fabrics from each fabric's POV)
- **Path-mappings describe WHAT** — fabric-local (an ajb path doesn't exist in feature_clb and vice versa)

Mirror the WHO; keep the WHAT local.

---

## §3 — Maintenance protocol

### §3.1 — Lane-class updates require paired commits

When a lane class is amended in either fabric:

1. Author the change in one fabric (e.g., add a new agent to BASE_EXEC in ajb)
2. **Within the same operational cycle**, author the mirror commit in the other fabric
3. Both commits cite each other in their commit messages for cross-fabric audit trail
4. Routed via ws COO + CL COO coordination (each COO authors own fabric's commit)

### §3.2 — Path-mapping updates are fabric-local

Adding a new `paths:` entry that maps a fabric-local path to a lane class is normal owned-paths maintenance — no cross-fabric coordination needed. Example: ajb adds `infra/aws/new-pipeline/**` → ANY_AE; CL doesn't need to know about it.

### §3.3 — New lane class introduction requires both fabrics

When introducing a brand-new lane class (e.g., `INTER_FABRIC`):

1. MSTR or sovereign-directed CTO proposes the lane class shape
2. Andrew ratifies (cross-fabric operational lane = mandate_distance > 1 territory; warrants sovereign call)
3. ws COO + CL COO commit paired adds to both fabrics' owned-paths.yaml
4. Path-mappings to the new lane class added per-fabric as needed (still fabric-local)

### §3.4 — Lane removal requires both fabrics

Same paired-commit pattern as introduction; never remove a lane in one fabric while it persists in the other.

---

## §4 — MSTR drift-detection at /govern Step 1(b)

MSTR runs cross-fabric owned-paths drift-detection each /govern cycle. Implementation lands paired with D-003 v1.11 amendment via /govern SKILL.md amendment per LD-0034 ship-paired precedent.

### §4.1 — Drift-detection scan logic

```
# Pseudocode
ajb_lanes = parse_yaml("ajb_workspace/.owned-paths.yaml")["lanes"]
cl_lanes  = parse_yaml("feature_clb/.owned-paths.yaml")["lanes"]

for lane_name in (ajb_lanes.keys() | cl_lanes.keys()):
    if lane_name not in ajb_lanes:
        SURFACE_DRIFT(lane_name, "exists in CL only")
    elif lane_name not in cl_lanes:
        SURFACE_DRIFT(lane_name, "exists in ajb only")
    elif set(ajb_lanes[lane_name].permitted_agents) != set(cl_lanes[lane_name].permitted_agents):
        SURFACE_DRIFT(lane_name, "permitted_agents differ")
    # description difference is informational (logged but not flagged as actionable)
```

### §4.2 — Drift surfacing

Drift items surface in MSTR's cycle record under a `## Owned-paths drift` section (new). Each item routed as:

- **Lane membership drift** (e.g., agent in ajb but not CL): operational fix via paired ws COO + CL COO commit
- **Lane existence drift** (e.g., lane in one fabric only): operational fix per §3.3 or §3.4
- **Description drift** (substantive wording divergence): informational; addressed in next paired update opportunistically

### §4.3 — Drift threshold response

| Drift count per cycle | Action |
|---|---|
| 0 items | clean — no action |
| 1-3 items | log in cycle record + surface to ws COO via MCP; route paired-commit fix |
| 4+ items | escalate to Andrew with "owned-paths sync attention needed" framing — likely indicates protocol failure in one fabric |

---

## §5 — Current drift items (as of 2026-05-24)

Three items observable from initial probe:

1. **CL BASE_EXEC missing ws CVO (`3.0.0_SA_CVO`)** — ajb added 2026-05-23 per CVO-as-Tier-1-Claude-agent ruling; CL didn't mirror. **Paired-commit fix needed; ws COO routes.**

2. **rollout_phase mismatch** — ajb phase 2 (fail-closed); CL phase 1 (warn-only). **NOT a Mirror Discipline drift** (rollout_phase is fabric-local per §2.2). Listed for Andrew Q-B operational decision on whether CL promotes to phase 2.

3. **`INTER_FABRIC` lane needed for `org/inter_fabric/`** — neither fabric has it; first needed at first Input 1 brief fire post-archetype-cutover. **Awaits Andrew Q-C decision** on new lane (proposed: `0.0.0_AB_MSTR + 1.0.0_SA_CTO + 1.1.0_SA_CTO` permitted) vs map to existing TIER0 lane.

---

## §6 — Override mechanism preservation

The existing `git commit --author-override LANE ...` escape hatch (logged to `org/git-author-override-audit.log`) is **unchanged** by this doctrine. It remains the per-instance Andrew-directed channel for legitimate cross-lane commits (e.g., TIER0_LAW commits per Directive Authoring Protocol).

Mirror Discipline operates on the canonical lane definitions, not on override mechanics.

---

## §7 — Reference

- **Establishing LD:** `org/tier0/ledger/LD-0046.md`
- **Existing PRD on owned-paths:** `docs/architecture/ADHC_OWNPTH.md` (PRD §6.1 schema reference cited by both fabrics' .owned-paths.yaml headers)
- **Tier-0 law context:** CONSTITUTION v1.1 Art. XV (fabric scope); STAKES_MATRIX v1.3; DIRECTIVES v1.10 (canonical at `2d5fdc03f`)
- **Cross-fabric governance origin:** LD-0031 Path B + LD-0032 ratification + LD-0033 cross-fabric coordination protocol
- **Both fabrics' owned-paths files:**
  - `ajb_workspace/.owned-paths.yaml` (rollout_phase 2; AUTHORED_BY 1.0.0_SA_CTO 2026-04-24)
  - `feature_clb/.owned-paths.yaml` (rollout_phase 1; AUTHORED_BY 1.0.0_SA_CTO 2026-04-24)
- **MSTR /govern Step 1(b) extension (forthcoming):** rides paired with D-003 v1.11 amendment per LD-0034 ship-paired precedent

---

*Established 2026-05-24 under LD-0046. Mirror Discipline canonical for cross-fabric owned-paths maintenance. Lane-class mirror obligation enforced via paired commits + MSTR /govern Step 1(b) drift-detection scan.*
