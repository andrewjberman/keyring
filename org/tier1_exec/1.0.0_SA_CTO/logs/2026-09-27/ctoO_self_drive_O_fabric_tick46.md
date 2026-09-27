# /self-drive ~O fabric -- ticks 45-46 (02:47Z-03:25Z), 1.0.0_SA_CTO~O

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260926_03xxZ_SELF_DRIVE_O_FABRIC.md` @56050d290d
**Why written:** a correction on this seat's own signed bytes, plus an assignment.

## MX-r-3: both halves SIGNED, and my half corrected

- `3.0.0_SA_CVO~O` signed the second half @9ca9e44fea (row NFRA_MCPINDEX-Z-C-S17), and caught an error in mine.
  `deploy-to-ec2.sh:196` rewrites the host `.env` on every deploy with `ENABLED_INTEGRATIONS=ycharts opal_portal globgrph`.
  So the act DOES write the property. My half said "N = 1 ... the act does not touch it", which was false.
- Re-read at `df724ef284` and at HEAD: the same literal, and no MCPINDEX commit touches the script. Corrected on the
  signed bytes @c40292a57e: N = 2, and CVO~O's condition is adopted (SSM-read the live value before the upload; STOP on
  mismatch). The mismatch branch is not signed.
- The condition was relayed to `2.0.0_SA_COO~O` (file 20260927T0325xxZ), since CVO~O's send reaches only this seat.

## Assignment: the future-import sweep (row NFRA_MCPINDEX-Z-S18)

`2.0.0_SA_COO~O` routed it here (file 20260927T030935Z). Re-measured:
- 64b6b9d65a stripped `from __future__ import annotations` from 108 .py files;
- 59 still lack it;
- all 59 are under `data/black_diamond/scripts` (the DS lane, Rule 13);
- 0 of 59 use `get_type_hints`, pydantic, `__annotations__` or `@dataclass`.

Assigned to `0.4.0_DS_ClientPlatform~D`, with the list committed at
`org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/1.0.0_SA_CTO~O/S18_FUTURE_IMPORT_MISSING_59.txt`. It is repo hygiene only;
no script is to be redeployed for it.

## Calls, verdicts

No new call. At Andrew, unchanged: call 1 BLOCKING (the OPLGTW re-seat); call 2 CARRIED (D9 device); the switchover
sitting. 0 self-drive verdicts (the MX-r-3 half is a sign-off, not a pitched call).

## Completion test

NOT DONE -- 0 of 4 projects `complete`. All REACHABLE.

state: ARMED

## Compiler Tools

git show per file of 64b6b9d65a (108 stripped counted); grep over the 59 for runtime-annotation users.
