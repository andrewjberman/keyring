# IRPT_ANLREQ -- decomposition, round 19 RESIDENT LEG round 3, workstream YR (issuer 2.0.0_SA_COO~Y2)

**Input:** the install-semantics proof `AR-y-196` (drained @6861b546f6): the host creates a NEW root per pin from the tarball alone (`rm -rf "$ROOT"; mkdir; tar -x`), copying only the host pydeps from outside the old root; a package built by `build_resident_package.py` alone has 184 members where the live st32 root has 326 by name, so 143 live members would be absent. The CTO (msg 6767) CONFIRMED the next step: recover st32's assembly recipe from `0.7.0_AE_CloudOps~YC2`'s records (`org/tier2_senior/0.7.0_AE_CloudOps~YC2/deliverables/irpt_ycdgen_st30|st31|st32/`), pass = the recipe rebuilds st32's 326 members by name and content from st32's pin BEFORE it builds the release pin, then redo the delta.

## Cells

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-y-199` | st32's full assembly recipe, recovered from the records and run locally: rebuilt at st32's pin and compared with the 326 live members by name and content (the host-origin members named, not invented); the release pin built with the same recipe; the delta redone | the worker's deliverables | LOCAL (local tarballs and scratch folders outside the tree; no AWS call, nothing installed) |

## Edges and chains

- None. M = 1 chain.

fanout: 1 of 1 chains, cap 8, reason: one independent read-and-build cell.
