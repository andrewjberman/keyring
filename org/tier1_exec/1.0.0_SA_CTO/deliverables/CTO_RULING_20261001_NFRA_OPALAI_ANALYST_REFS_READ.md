# CTO RULING 2026-10-01 ~04:0xZ -- NFRA_OPALAI: the Analyst reads `opal/agent/refs`, read-only

**Seat:** `1.0.0_SA_CTO~O`. **Asked by:** `2.0.0_SA_COO~O` msg 27471. **Authority:** Andrew-direct
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261001_035xZ_NEXT_CALLS_GO_NO_TAXSMA_CRO_O_RESOURCE.md`
(OPTION 2). **Cut by:** `2.0.0_SA_COO~AI`, the NFRA_OPALAI issuer, in the same order as the row NFRA_OPALAI-Z-S50
launcher fix.

## The defect

At ~01:45Z the Analyst (Opal_Agent, launched by `launch-v2.ps1`) passed the identity gate and stopped at launch step 2.
Its session working directory is `opal/runtime`, so it cannot read `opal/agent/refs/` (TEAMS_DUTY.md, THREAD_MEMORY.md,
REQUEST_CATALOG.md and the other four refs). `opal/agent/prompt.md` names those files as its operating references.

## The ruling

1. **Widen the session's READ set to exactly `opal/agent/refs/`.** The launcher adds the directory to the Claude
   session (`--add-dir`). The path is DERIVED from the launcher's own location (`$PSScriptRoot\..\agent\refs`) and is
   never typed as a device path.
2. **The write set does not change.** `opal/agent/hooks/concierge-gate.sh` G1 (lines 65-92 at opal_ai fd8ab8a) denies
   every write outside the configured `state_dir` and the tmp roots, for every directory the session can see. Thread
   memory is written under `state_dir/threads/`; `refs/THREAD_MEMORY.md` is its spec and is only read.
3. **The refs do not move.** `opal/agent/` holds the agent's product files, and `opal/runtime/` holds the launch
   mechanism. Moving the refs under `runtime/` would mix the two.
4. **Nothing wider.** The rest of `opal/agent/` (hooks, tools, skills, teams_watch) is not added by this ruling. A need
   for any of it comes back here.

## Acceptance (the cut's criteria, one clause each)

- POSITIVE: the launched Analyst reads `agent/refs/TEAMS_DUTY.md` and passes launch step 2.
- NEGATIVE (write): a Write to `agent/refs/` from the session is denied by concierge-gate G1.
- NEGATIVE (scope): a Read of `agent/hooks/concierge-gate.sh` from the session is outside its directories (refused or
  prompted, never silently read).
