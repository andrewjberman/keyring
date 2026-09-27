# /self-drive ~O fabric -- ticks 47-48 (03:47Z-04:25Z), 1.0.0_SA_CTO~O

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260926_03xxZ_SELF_DRIVE_O_FABRIC.md` @56050d290d
**Why written:** a second sign-off condition, a gap between it and the GO, and a ruling.

## MX-r-3: a second condition, and a GO that fired carrying only the first

- `3.0.0_SA_CVO~O` added a second pre-upload condition (@12fff6fc33, row NFRA_MCPINDEX-Z-C-S18). The artifact also ships the
  dashboard bundle, built from the nested `mcportal` checkout (`deploy-to-ec2.sh:80-92`). Neither half named it.
  - Live `mcportal_commit` = `a3bff71ffa` (EC2_MANIFEST).
  - Condition: `/c/tmp/mx-rel/mcportal` HEAD = `a3bff71ffa` before the upload, else STOP.
  - Re-read and adopted on the CTO half @c129941cdc; relayed to `2.0.0_SA_COO~O` (file 20260927T041300Z).
- **The gap:** COO~O's 04Z log (@6b289affea) says the GO fired at ~04:07Z "with the pre-upload ENABLED_INTEGRATIONS read as
  the one condition". My relay landed at 04:13Z, AFTER the GO, and was still unread at 04:22Z.
  - Measured at 04:22Z: `/c/tmp/mx-rel/mcportal` reads `a3bff71ffa`, clean tree, so the condition HOLDS at that moment.
  - An URGENT file to COO~O asks it to hand the GO worker condition 2 before the upload.
- Lesson for this seat, twice tonight: both of CVO~O's catches were DEPLOY INPUTS I did not trace (the `.env` render, the
  bundle build). A release sign-off reads the deploy script's inputs, not just the code diff.

## Ruling: Z-S18 sweep (DS~D msg 26139)

`0.4.0_DS_ClientPlatform~D` made the 59 edits (set-equal to this seat's list, +1/-0 each). But 48 files fail commit-gate on 324
ruff violations that were already there at base. They are the ruff half of a5ac27a275, which 64b6b9d65a also reverted.
- **(1) YES, restore the ruff half:** safe fixes only, plus noqa. An F401 fix that would drop a LOCAL-module import keeps it
  with a noqa (side effects). py_compile and commit-gate pass.
- **(2) NO redeploy for a lint-only change.** Record the divergence (a read-only S3 compare of the 48 against the pre-sweep
  bytes). Each script reaches S3 with its next functional change, through safe-deploy.

Why no redeploy: moving 48 production pipeline scripts gains no behaviour, and it is a served-code act.

## Calls, verdicts

No new call. At Andrew, unchanged: call 1 BLOCKING (the OPLGTW re-seat); call 2 CARRIED (D9 device); the switchover
sitting. 0 self-drive verdicts.

## Completion test

NOT DONE -- 0 of 4 projects `complete`. All REACHABLE.

state: ARMED

## Compiler Tools

git show at pinned commits; rev-parse on the release tree's nested checkout; the COO log read by line.
