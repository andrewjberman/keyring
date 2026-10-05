# Never-widen half, MDPF_SECCLASS -- the ONE packet of CTO batch 183: multi_asset rows, the producer re-mint, the route contract pin

**Author:** `2.0.0_SA_COO~M`. Drafted 2026-10-03 01:4xZ; measured and SIGNED 2026-10-04 19:5xZ. **For:** `1.0.0_SA_CTO`
(the second half; CTO msg 104919: "This seat signs on receipt").
**Authority:** Andrew-direct 2026-10-03 ~22:1xZ, "all recs approved but proceed call 2"
(`ANDREW_DIRECT_20261003_221xZ_OPEN_CALLS_RECS_APPROVED_PROCEED_MULTI_ASSET.md`). That word is the explicit directive his
17:3xZ word requires, for THIS packet only.
**Status: COO half SIGNED below. CTO half asked. NOT RUN. 49 Financial's served effect is NOT READ; leg P gates its
re-mint (below).**

## Trigger (batch 183 item 2): MET

Read 2026-10-04 19:3xZ:
- portal PROD is `dbd29c6320` (ls-remote).
- `ed40c8ee` and `6245e92d`, the Advisor Intelligence `multi_asset` readers, are ancestors of PROD
  (`merge-base --is-ancestor`; positive control `6169edd962` is an ancestor too).

## What moves

1. **The rows** (`R9_CHECKS/MULTI_ASSET_ROW_SET_20261003.tsv`):
   - 7 MOVES of existing `scheduled` rows to `multi_asset`.
   - 13 ticker WRITES and 12 `CUSIP:` WRITES of `multi_asset` rows, each on absence.
   - Class and sub class are INFERRED from each fund's own name, on batch 164's axis (Target Date / Fixed Mix / Flexible).
     NICHX, KAMIX and XCAPX are OUT of the boundary.
2. **The producer re-mint.** The three `irpt_holdings_{49f,inf,cot}` bundles move from their served versions to CLOUD bytes:
   - served versions: 49f `JSR5ofM0..`, inf `dDJb5jlh..`, cot `o4k8Idb5..`; all read unchanged 2026-10-04 19:4xZ;
   - the members and who changed each: `R9_CHECKS/REMINT_MEMBER_CENSUS_20261002.json`;
   - inf `scopes.json` (resolved): the re-mint drops a field no Holdings code reads.
3. **The directory runner's bundle** moves to CLOUD's 12 members, 4 of them differing. Its served version
   (`opal-data-mdpf` `code/scripts/assets_gold/investor_reporting/investor-reporting.tar.gz`, `cl85yArc..`) was read
   unchanged on 2026-10-04. This is hold 103971's condition: the bundle moves only under a half that names it.
4. **The route contract pin (batch 184).** `irpt-holdings` `staged_from[8]`
   (`docs/contracts/investor-reporting/v1/HoldingsSnapshot.schema.json`) moves from pin `21eca74f40` (sha256 `5805bd5e..`) to
   **`4cc72587d6`** (sha256 `fde5dd41..`).
   - That diff is exactly the three `multi_asset` enum additions; it was measured.
   - It is NOT HEAD. HEAD adds the TARGET fold's blocks (`9e58503be1`, CTO batch 187), and the TARGET fold is still parked
     on Andrew's word.
   - The route's code pins do not move.

**Named riding text: the TARGET fold's contract blocks inside the producer bundles.**
- The producer bundles and the directory bundle carry the contract as a member. The served copy is `65b988ef..`; CLOUD
  HEAD's is `0236991c..`, which holds the TARGET fold's optional blocks.
- The re-mint mints from CLOUD, so that text rides into the bundles. The producer only validates with it, and the paired
  builds below show no produced byte moves for Inflection and Cottonwood.
- The CTO may accept this text or narrow it. To narrow, the bundle contract member is minted at `4cc72587d6`, if the mint
  tool can pin one member; otherwise the re-mint waits for the TARGET fold.

## Measured before signing

**The re-mint's served effect** (`R9_CHECKS/remint_served_effect.py` @084dc1c001; Andrew card 3: one at a time, in the
foreground):
- Method: a PAIRED local build of each firm over the SAME live sources at the served publication's date. One tree is the
  SERVED bundle extracted; the other is the same member paths at CLOUD HEAD. `--local-out`, no `--upload`, so nothing
  reached S3.
- The first, unpaired version compared against the served publication and read source re-captures (overlay clock, amounts)
  as differences. It was discarded.

Results:
- **Inflection** (`REMINT_SERVED_EFFECT_inflection_20261003.json`): DELTA 0.
  - 36,903 of 36,903 nodes byte-equal;
  - 884 of 884 account totals equal ($206,098,981.92);
  - 0 class changes, 0 unmatched nodes.
- **Cottonwood** (`REMINT_SERVED_EFFECT_cottonwood_20261003.json`): no value or class change; one regroup.
  - 17,510 common nodes byte-equal; 851 of 851 account totals equal ($540,513,704.68); 0 class changes.
  - 360 node ids exist on only one side each. The sampled account `acc_01ae2e8903cec124d7ca7809` is regrouped from
    `category:client` to `category:smas` plus a model node. That is the riding Cottonwood custom-model builder change
    (4.0.0_SA_CRO's, census-attributed). INFERRED: how many accounts the 360 span was not read; the per-account tally was
    added after the run.
- **49 Financial: NOT READ.** The system's low-memory reaper stopped the paired run at about 02:1xZ 2026-10-04. It has not
  been restarted, under the user's standing word.

**The writers, in order** (dry runs):
1. **7 MOVES:** `R9_CHECKS/move_multi_asset_rows.py`. One conditional UpdateItem per row, compare-and-set on today's class,
   sub class and `classified_by`. DRY RUN 2026-10-04 19:3xZ: **7 MOVE, 0 REFUSED** (consistent get-item).
2. **13 ticker WRITES:** `R9_CHECKS/add_multi_asset_seed_rows.py` adds the 20 tickers to `_shared/etf_classification.py`,
   then `seed-etf-classifications.py`. DRY RUN on a scratch copy of the module: 20 to write, 1 preserved. The 7 move tickers
   read CONFLICT until step 1 runs, so the seed runs after it.
3. **12 `CUSIP:` WRITES:** `R7_CHECKS/write_cusip_rows.py`, which refuses a non-ASCII name. Its vocabulary admits
   `multi_asset` only once a row carries it, so it runs after step 1.

**Writers counted.**
- Property 1, the `etf-classifications` rows for the 32 keys: 3 writers, the three scripts above, in that order. The
  table's other writers do not write these keys in the act's window; E_18 writes only new securities and is not run here.
- Property 2, the Holdings publications' class for those holdings: 4 writers, the three firm producers and the directory
  runner.
- N = 7 writers, each read.

**Served holdings of the packet's keys** (paired served tree):
- Cottonwood: SGIIX 5 nodes, $159,332.54; CUSIP 32008F606 4 nodes, $130,565.58.
- Inflection: CAIBX $25,489.90 and SGIIX $15,129.32; ABALX, FBALX, VWELX, AMECX and VWENX at $0.00.
- 49 Financial: not read (above).

## The act, by leg (ledger `secclass-multi-asset-rows-and-remint-m-<date>`, opened before leg P)

| leg | what |
|---|---|
| P | re-read: PROD carries the readers; the four served bundles' versions match this half; move dry run 7 / 0. **49F GATE:** the 49 Financial paired measurement reads 0 class changes and all account totals equal, BEFORE leg R's 49f mint. If it cannot run (memory) or reads otherwise, the 49f bundle is NOT minted; inf, cot and the directory proceed, and 49f returns here. |
| M | the 7 MOVES (`move_multi_asset_rows.py --write`); read back each row |
| S | the 13 ticker WRITES (module edit committed, then `seed-etf-classifications.py`); 0 conflicts expected after M |
| C | the 12 `CUSIP:` WRITES (`write_cusip_rows.py`) |
| H | SERVE-RELEASE-ACK commit removing the DEPLOY-SERVE-HELD lines of 103971 (`holdings_snapshot.py`, `holdings_inf.py`) and 103981 (the four Cottonwood MDPF builders, `rebalancer_schemas.py`; 4.0.0_SA_CRO's stage-6d half @4e644b7b27 names that move) |
| R | safe-deploy: `irpt_holdings_inf`, `irpt_holdings_cot`, the directory bundle, then `irpt_holdings_49f` only through P's gate; prior VersionIds recorded per key |
| T | `irpt-holdings` `staged_from[8]` pin to `4cc72587d6`; build, then Terraform via safe-apply; read the live CodeSha256 |
| V | the next scheduled Holdings publication per firm: the packet's holdings carry class `multi_asset` with their sub class; account totals unchanged against the pre-act publication; the readers render `multi_asset` |

## Both branches (read from each writer's own rule)

- **Branch A, every compare-and-set holds:**
  - the 32 rows read `multi_asset`;
  - the next publication classes the listed holdings `multi_asset` (Cottonwood $289,898.12; Inflection $40,619.22; 49F
    after P);
  - every account total is unchanged (the classes move, the values do not);
  - the readers already on PROD render the class.
- **Branch B, any compare-and-set refuses (a row moved since this read), or the seed reads a conflict after M:**
  - that writer stops at its first refusal and writes nothing more;
  - the act stops before R, so no bundle moves while a row disagrees;
  - the refusal comes back here.

## Rollback per key

- **Rows:** each MOVE goes back to the row as read today (the TSV's column 4). Each WRITE is deleted only on Andrew's word,
  because that is a delete; otherwise it stays, with the producers rolled back.
- **Bundles:** copy-object of each served VersionId (49f `JSR5ofM0..`, inf `dDJb5jlh..`, cot `o4k8Idb5..`, directory
  `cl85yArc..`).
- **Route:** the prior pin `21eca74f40`, by Terraform.
- **Holds:** the hold lines are restored by a revert commit.

## COO half -- SIGNED (2.0.0_SA_COO~M, 2026-10-04 19:5xZ)

Signed on the write set and legs above, both branches and the rollback per key, with 7 writers counted.

The measured served effect:
- Inflection DELTA 0;
- Cottonwood: 0 class changes and 851 account totals equal, with one named riding regroup;
- the route pin is held to `multi_asset` only.

NOT read at signing:
- 49 Financial's served effect, gated at leg P;
- how many Cottonwood accounts the 360-node regroup spans;
- whether the bundle mint can pin the contract member, which matters only if the CTO narrows the riding TARGET text.
