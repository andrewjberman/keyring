# /self-drive ~O fabric -- ticks 49-50 (04:49Z-05:20Z), 1.0.0_SA_CTO~O

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260926_03xxZ_SELF_DRIVE_O_FABRIC.md` @56050d290d
**Why written:** driver acts -- two defect assignments, and the MX-r-3 condition-2 acceptance.

## MX-r-3

- `2.0.0_SA_COO~O` (file 20260927T043118Z) holds condition 2 as the issuer, since a worker cannot be messaged mid-act.
  - Measured `/c/tmp/mx-rel/mcportal` = `a3bff71ffa`, 0 dirty paths, at 04:2xZ and 04:29:29Z.
  - `deploy-to-ec2.sh:84-86` only READS that HEAD and prints it.
  - The COO~O grades the printed line in the L1 proof; any other commit is a rollback to `df724ef284`.
  - **ACCEPTED:** a pre-upload measurement, an act that cannot move it, and a named rollback. That is what the condition
    asks for.
- The ledger `nfra-mcpindex-r2-gateway-release` was OPENED at 04:38:49Z on the worker branch (@68d061ce5f), with 4 legs.
  At 05:18Z no leg is proven yet. That is inside its 4.0h window, and COO~O owns it.

## Assignments

- **Z-S3 + Z-S6/Z-S11** (COO~O file 20260927T051043Z) go to `0.4.0_DS_ClientPlatform~D`, after Z-S18.
  - Z-S3's `dtype == object` guard is in FIVE copies (measured). The source is `data/assets/scripts/silver/mirror_conversion.py:330`.
    Four vendored Lambda copies sit under `infra/aws/lambda/opal-assets/opal-assets-silver-{blackdiamond,etf,eclipse,orion}`;
    eclipse is at :275 and orion at :277.
  - DS fixes the source, with a test that fails first. AE vendors it and deploys through Terraform, under a never-widen
    sign-off, because the served silver dtype metadata moves.
  - Z-S6/Z-S11 (4 missing pathfinder fact_dailynav partitions, 2026-08-29/30): read the cause first, no backfill until
    it is known.

## Z-S18 landed on 56 of 59

- @219e930eec, drained @f1830f38da: the future import AND the ruff half restored; 0 new violations.
- 3 files are REFUSED by a rule that is not lint: `coerce_silver_ids()` is missing in `bd_price_update.py`,
  `build_bd_assets_dim.py` and `build_interpolated_prices.py`. It was already there at base.
  - Satisfying it is a functional change to 3 silver producers, so under this seat's ruling (lint-only, no redeploy) it
    rides each file's next functional change.
  - Consequence to note: any seat that next edits one of those 3 will be refused until it adds the call.
    `build_bd_assets_dim.py` is MX-s-4/MX-s-6 territory.

## Calls, verdicts

/open-calls re-carded at ~04:45Z: 2 calls at Andrew, unchanged (call 1 BLOCKING: the OPLGTW re-seat; call 2 CARRIED:
the D9 device), plus the switchover sitting (his act, not a call). 0 self-drive verdicts.

## Completion test

NOT DONE -- 0 of 4 projects `complete`. All REACHABLE.

state: ARMED

## Compiler Tools

git show per commit; the rev-parse and ledger read in the worker's worktree; native Glob for the 5 copies.
