# ANDREW-DIRECT 2026-10-14 ~12:xxZ -- site Z leaves the control arm and runs the model policy (MP-20261010)

**Channel:** Claude Code terminal, site Z, to `1.0.0_SA_CTO~Z`. He asked: "TO be clear, on this box are we adhering to the
expectation that CTO/CVO/CRO are on Opus, MSTR/COO are Sonnet, and Workers are Haiku?" This seat answered no: site Z is the
policy's only CONTROL device. It ran `.tools/model-census.py` (24 h): Tier-1 on Opus 5.5 as the policy says; MSTR~Z and
the COOs on Opus 5.5; CloudOps lanes and the BG seat on Opus 5; COO~O's workers on Sonnet 5.5. It offered to switch.

**VERBATIM:**

> Yes let's get that switched now.

## What changes

1. **`org/ref/MODEL_POLICY.json`:** `sitez` joins `treatment_devices`, and `control_devices` becomes empty.
   - Effect: every new launch on site Z through `ajb.ps1` or `spawn-agent.ps1` takes the role mapping, all at effort high:
     - Tier-1 (CTO, CVO, CRO) on Opus 5.5;
     - MSTR, COO and Tier-2/3 seats on Sonnet 5.5;
     - unmatched 0.0.N utilities keep their defaults.
2. **Workers:** on site Z, COOs spawn `worker` / `worker-light` with `model: "haiku"`, `effort: "high"` on the Agent call,
   as on laptop, dell1 and dell2. The carriers that told site Z to pass no model are corrected:
   - `.claude/agents/worker.md`;
   - `.claude/agents/worker-light.md`;
   - `.claude/skills/dispatch/SKILL.md`.
   - The frontmatter is untouched (the per-fabric merge rule stands).
3. **Running seats keep their current model until relaunched.**
   - `0.0.0_AB_MSTR~Z` relaunches the site Z seats that read off-policy, at safe points: never mid-deploy, and never
     with an open change-management entry.
   - It prints the census after.
   - The policy treats an explicit `-Model` on a launch as an override, never a mismatch.

## Not changed

The 0.0.3_BG_BBGTerminal utility seat (unmatched, keeps its launch default); Codex seats; any seat's explicit override.

-- recorded by 1.0.0_SA_CTO~Z
