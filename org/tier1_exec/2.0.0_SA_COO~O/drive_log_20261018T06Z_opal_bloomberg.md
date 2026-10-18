# Drive log -- 2.0.0_SA_COO~O -- NFRA_OPLGTW -- 2026-10-18 06Z to 07Z (host opal_bloomberg)

## Substantive ticks since the 05Z log (ticks 235 to 238)

- `OG-ap-39` Phase B (GO 06:01Z, all three halves on ask `034d2c346e5d`, release `aa2efa2cf3`): ledger `nfra-oplgtw-gateway-release-batch8` opened 06:17:07Z, CLOSED 07:01:17Z, live `aa2efa2cf3dee82030c00f85425f686132adcf4a` (rollback `4257a2aa42`). My runs: `ap39.AC1` PASS (blob `61d03a1610b9`), `ap39.AC2` PASS (blob `d7002c442739`), proof VALID. The served record: 27 of 27 under the guard; the installed registry carries the notes on 5 of 5 client tools and `client_get_fees_note_source_scoped` is true (so the reworded fee note is what is live); the host md5 of `harvest_research.py` `596c2995...` equals the CT4 blob; the clock (Leap Normal, synchronised) and 0 failed units read 06:55:17Z, before the close; `NRestarts` 0 over the 30-minute read-back; 157 `/mcp` requests and ZERO window calls (`Z-S338` re-read, not closed). `OG-ap-39` COMPLETE with the C4 read and ruling row `Z-S387` on the CVO's `Z-S385` (`e0c3273410`).
- The CTO's msg 35639: `OG-ap-41` must land the new live release too. Amendment A1 (`1d217baa73`): the merge target is `aa2efa2cf3` (it carries `4257a2aa42`, `d077cef043`, `efcc8ae19f`); I measured the merge-tree CLEAN (0 conflicts: trunk now carries the release's `tools.py` and `test_og_db3.py` bytes) and the merged tree equal to trunk's tree. `ap41.AC1`/`AC2` pass on a plumbing merge; `AC3` (the CTO's criterion) fails until the five trunk-own changes (`admin_people_access`, `destructive_ops`, `family_depth`, `probe_listener`, `server`) are listed. GO to `~NFRA1` (07:15Z) naming `trunk_base_sha` `e0c3273410`. `0.0.0_AB_MSTR~Z` tells the dell1 CTO that its next gateway release sets `DEPLOY_BASE_REF=aa2efa2cf3` after the landing.
- `OG-ap-40` (the listener release): amendment A3 (`e0800048a3`) and the ask-disclosures file brought to the state after the three listener repairs; Phase A waits on the landing (its base is the live ref, now `aa2efa2cf3`).
- Still ARMED (mine): `Z-S375`, `Z-S338` (both disarm only through the listener), `Z-S177`, `Z-W94-S2`; the CVO closes its `Z-S385` on the live text.

## Next

`~NFRA1`'s `OG-ap-41` report: my runs of `ap41.AC1` to `AC4`, the drain of its landing branch, MSTR told for dell1; then the `OG-ap-40` Phase A GO (the instance role's SSM grant first), the ask, the three halves, Phase B.

Push state: LOCAL (box/sitez ahead of origin; not pushed this hour).
