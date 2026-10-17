# 1.0.0_SA_CTO~DELL1 -- self-drive dell1 box, tick 74 (covers ticks 73a to 73g, about 14:19Z to 14:48Z)
**archetype:** COORDINATE

Arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261016_024xZ_SELF_DRIVE_DELL1_BOX_30M.md` @fa59eb8dec. state: ARMED.

## Rulings and acts (message ids; hashes are LOCAL on box/dell1)

- **7-day carrier re-pull done (CRO~DDD 7569).** The ledger closed @e74f7ba67f.
  - Holdings: 0 of 7 landed, all REJECTED by the guard.
  - Allocations: 5 of 7 landed.
  - The after-print showed 0 of 21 Cottonwood fields moved, and Global equal.
  - The 07-27/07-29 fact_allocations force re-convert was ruled YES: half addendum 1 @db626beded. It ran 14:21:55Z (3 to 897 accounts and
    1 to 896), and its ledger closed @aca0ad3bf5 (msg 7604).
- **Breach: 14 stray bronze account_attributes (CRO~DDD 7579, C1 7582).** The re-pull's built-in `--backfill-holdings-net` sweep
  first-landed 14 files carrying today's attributes under July and August dates.
  - RULED: quarantine through FORWARDFILL_QUARANTINE, never merge, no S3 delete. Ruling @d398734b87.
  - DEPLOYED from the deployed bytes. My read of `s3://opal-data-cot/code/silver/cot_silver_merge.py`: 38,922 bytes, sha256 72dcb7e5a42f4afe,
    14 names, and :126 still dedups on asset_name, so S34 did not ride along. Its ledger is CLOSED.
  - Surprise row S35 @38ae58ddb9 records the sweep's reach.
  - C1 proves it on the 10-18 silver run.
- **Global gate (v) (D1 7593, 7598).**
  - My 7551 cure (B1's catch-up) was wrong: 10-13 to 10-16 are never filled (msg 6986). Gate (v) checks every date (:1791-1815), so 10-16
    would refuse every fire.
  - RULED (B): an enumerated GLOBAL_AXIS_DROP_DATES {2026-10-16} at :2368. It is not added to the exempt list, Cottonwood's axis is
    untouched, and D4's dry run is the go/no-go. It is built on pin d2f734fbac, as the 10-18 fire's one gold change.
  - PRD v2.29 @11ea6ef573, amended @96e3ef7de9.
- **Bloomberg empty window (Q1 7581):** YES to a 7-day cooldown, listed in the receipt. A fire stops if more than 5 windows return empty.
- **FB-p-2 B1 (B1 7578):** the organic 12:52Z run satisfies the catch-up. Accepted, with no dispatch.
- **RESAPP (R1 7584):** fa30 and d775 LANDED on portal DEV @cab233bfdf.
  - The chosen-set PROD promote was accepted.
  - ~H1 is encumbered by two pending ADHOC orders from 2.0.0_SA_COO~J1 (MSTR 7606), so RULED: seat ~H2. R1 re-addresses bq-2 to it.
- **Upstream (MSTR 7567):** S55 not_met is built at c6980f0686 and relayed to R1.

## Completion test

NOT DONE. This is the standing box drive, which ends on Andrew's word.

## Acts only Andrew can do (each with its citation)

1. ADVI_COTBOOKS: confirm the 6 DONE WHEN lines (row 0cf5). Canonical loop L2.
2. SOC2_MSLOGS round 2: run the 8-day re-derive with his MFA session (row 89c9). The access group holds Andrew_Berman alone (TO-R2-r2 :29).
3. SOC2_MSLOGS FWD-1: his read of the enriched block, through the same MFA door.
4. EWS delivery channel. Nothing sends until he names one.
5. FWD-10's portal source line to PROD, a client-facing push (CLAUDE.md PUSHES).

## Watch

- The 2026-10-18 ~11:30Z Cottonwood silver run (C1's quarantine proof, then R106 C-1).
- The 2026-10-18 13:30Z MDPF fire (D4's dry run first, then the Global axis drop, and CN-s-1's Global grade).
- 18:00Z dell2 reconcile, now moot because DEV landed early. ~H2's PROD promote, then R1's RIO LN read.
- SECCLASS 23:00Z. TR-HELD act 3 after the 10-18 00:00Z replay. zb-1 at 10-19 11:00Z.

## Compiler Tools

| tool | result | note |
|---|---|---|
| aws s3 cp (one object) + sha256sum | PASS | verified the quarantine deploy by content |
| aws s3api list-objects-v2 (one prefix) | PASS | `_aggregate_aua` holds 10-12 and 10-17, nothing between |
| native Read of cot_silver_merge.py and dim_mdpf_aggregate_aua_timeseries.py | PASS | confirmed the quarantine mechanism and gate (v) |

What worked: verifying each producer's claim against the deployed bytes or the code before signing. Gap: a seat's built-in sweep can widen
an act beyond its half. That is row S35; future pairs name every table such a sweep can land.

-- 1.0.0_SA_CTO~DELL1
