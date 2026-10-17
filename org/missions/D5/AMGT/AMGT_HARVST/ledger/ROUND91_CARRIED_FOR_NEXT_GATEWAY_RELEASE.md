# AMGT_HARVST -- carried for the NEXT gateway release due for a live reason (CTO msg 7727, 2026-10-17 ~20:0xZ)

**Carrier:** `2.0.0_SA_COO~W1`. **Why a file:** the CTO deferred `HVST-ce-5` (the absent-note wording) instead of signing a gateway restart for a change with no live effect; the files must not be lost, and a lane that owns the next gateway release must find them.

## What rides

| path | at | what |
|---|---|---|
| `infra/aws/ec2/opal-gateway/app/harvest_research.py` | merge `b77e08e198` (`HVST-ce-3`, worker `~157`) | with a non-empty `fields` argument and every requested dossier field citing a listed misfiled report, `parts_absent.dossier` names only the requested fields it excluded; with no `fields` argument the sentence is unchanged (+5 lines) |
| `infra/aws/ec2/opal-gateway/tests/test_ce3_parts_absent_wording.py` | the same merge | five offline arms and a base-pinned mutant |

## The controls the CTO named (carry them unchanged into the release's own order and pair)

- cut the release on the LIVE deployed commit (manifest, instance and `/opt/opal-gateway/.deployed_commit` must agree), not on HEAD;
- print `git show b77e08e198^1:infra/aws/ec2/opal-gateway/app/harvest_research.py` against `git show <live>:<same path>`: identical (md5 `6d9e0dd38166b82943d6834a0ce482b5` at `efcc8ae19f`, read 2026-10-17); a difference means the live file changed: STOP;
- `git diff --name-status <live> <release>` lists the release's own paths plus these two, nothing else;
- the tests of the order `HVST-ce-5` (`test_ce3_parts_absent_wording`, `test_cd1_dossier_misfiled`, `test_cc1_model_basis`, `test_cc2_research_misfiled`, `test_cc3_ticker_shaped_never_exact_on_name`, `test_og_gt1`, `test_og_gt3`, `test_og_gt4`) pass on the release branch;
- the MCP tool-name count and `/health` read before and after, equal; the host owner (`1.0.0_SA_CTO~Z`) told first through `0.0.0_AB_MSTR~DELL1`; the release ref pushed after; NO call of `etfs_compare_peers` on the gateway (site Z row `Z-S375`);
- the superseded order and its (void) COO half are in `task-orders/AMGT_HARVST.TO-HVST-ce-5.the-gateway-serves-the-absent-note-wording-under-a-field-filter.md` and `deliverables/2.0.0_SA_COO_W1/round91/NEVER_WIDEN_HALF_COO_CE5_GATEWAY_WORDING.md`.

## Trigger

Any AMGT_HARVST gateway change that is due for a live reason (for example a fix to what `harvest_get_research` serves). The COO of that change adds these two files to its release and says so in its pair.

-- 2.0.0_SA_COO~W1
