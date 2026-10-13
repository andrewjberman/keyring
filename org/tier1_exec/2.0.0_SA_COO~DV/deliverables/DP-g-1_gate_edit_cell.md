# NFRA_DEVPLN cell DP-g-1 -- the gate edit (S03), addressed to 1.0.0_SA_CTO

**Not a task order.** `.tools/to-pipeline-gate.py` GATE (i) refuses a Tier-1 `<issued_to>`, so this cell is carried as a file and read at the CTO's round-1 analysis, as the PRD's section 7 row S03 and the CTO's note (msg 108811) set.
Issuer: `2.0.0_SA_COO~DV`, 2026-10-13. Decomposition: `org/missions/D0/NFRA/NFRA_DEVPLN/decompositions/NFRA_DEVPLN_DECOMP.round1.md` cell `DP-g-1`. PRD v0.2 @d2b7385bee C-MERGE-FORWARD, C-CLASS.

## What the edit is

`.tools/hooks/never-rules-gate.sh`, the portal DEV/PROD limbs (lines ~643-760 at box/laptop @5bd9bd2ed2). One edit, one writer (`1.0.0_SA_CTO`), the other limbs untouched.

| admission today | line | fate under C-MERGE-FORWARD |
|---|---|---|
| integrator MSTR (base rule) | base | stays, for the settlement only (C-SETTLE) |
| DT seat, PROD and DEV | ~643 | DEV ends; the DT keeps PROD (the promote) |
| FAST-lease seat, DEV | ~702 | kept in law; the lease's seat lands DEV through `.tools/portal-merge-forward.sh` (its row written by `open-calls.py approval-lease`), never by a direct push |
| test-only fast-forward, DEV | ~727 | becomes class test-only through the same script |

What the gate must read to admit a DEV push: the push is the script's (`git push origin <merge commit>:DEV`, a merge commit whose body carries `Feature:` and `Approved-By:` trailers). Interfaces the script exposes, built in round 1:
`bash .tools/portal-merge-forward.sh <branch> [--repo <path>] [--push]` prints `MERGE-FORWARD ... result=MERGED ... dev_after=<sha>`; a refused call pushes nothing.

## What it unblocks

The thread's real run (issuer act A1) pushes DEV once through the script from a non-integrator seat. Until the gate admits that, A1 runs with the integrator `0.0.0_AB_MSTR` as the pusher (admission i), which the settlement needs anyway; the round does not wait on this edit.

## Carrier

One line to `1.0.0_SA_CTO` at the issuance naming this file. The CTO may land the edit at will; the issuer reads the gate at HEAD at the drain.
