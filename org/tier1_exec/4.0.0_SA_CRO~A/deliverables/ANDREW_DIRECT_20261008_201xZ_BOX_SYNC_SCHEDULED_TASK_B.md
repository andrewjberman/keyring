# ANDREW_DIRECT 2026-10-08 ~20:1xZ -- box-sync runs from a Windows scheduled task on each box (call 1, option b)

**Channel:** laptop terminal, to `4.0.0_SA_CRO~A`, answering /open-calls CALL 1 of 2: "What runs box-sync on schedule: (a) each
MSTR's /govern at its slot, as now, or (b) a Windows scheduled task on each box, with no agent involved?" REC was (a) now,
(b) after a day of clean BOX-SYNC rows.
**Recorded by:** `4.0.0_SA_CRO~A`, same turn.

## Andrew's words, verbatim

> "I think B is the stable long-term solution."

## Reading

Option (b) is chosen as the solution. This seat builds it now and does not wait the day its REC proposed. Each box
gets a scheduled task that runs `.tools/box-sync.sh` at that box's slot under that box's MSTR serial, with no agent
in the loop: laptop `:00`/`:30` integrate then box pass; site Z `:06`/`:36`; dell1 `:12`/`:42`; dell2 `:18`/`:48`.
Once a box's task runs, that MSTR's `/govern` stops invoking box-sync. 
## CALL 2, same channel, minutes later, VERBATIM

> "THen yes to your call 2"

Call 2: "Delete the leftover org/tier1_exec/2.1.0_SA_COO folder (8 tracked files) under your 2026-08-25 order to
'delete categorically'?" Done the same turn. The folder held 9 files: 8 tracked, plus 1 untracked CL task order
(`COMP_LEARNS.271`, issued by 2.1.0_SA_COO to 1.1.0_DS_CompLearns, 2026-05-27). The `/allocation` skill's CL-fabric
section and the `2.[01].0` COO pattern in `.tools/ajb.ps1` were cut with it.
