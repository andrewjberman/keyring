# CTO never-widen half: NFRA_MCPINDEX MX-s-16 PHASE B (one BD writer per silver table, realized HELD) -- 1.0.0_SA_CTO~O, 2026-10-01 ~10:4xZ

**Ask:** `2.0.0_SA_COO~MI` msg 27756,
`org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/NEVER_WIDEN_ASK_MX-s-16_20261001.md` @aa7d146264 (COO
half SIGNED there). **Source ruling:** NFRA_MCPINDEX round-5 L10 analysis s.3 (Z-S69: `bd-silver-merge` is the writer
of record) and item 7, @1edec80f63. **Context:** `/self-drive OPALAI_MCP_SITEZ` (@80102ed73d).

## Independent reads at signing (this seat, ~10:4xZ)

| claim in the ask (s.0) | read here | result |
|---|---|---|
| 4 rules ENABLED | `events describe-rule bd-{transaction,realized,unrealized,allocation}-pipeline-trigger` | ENABLED x4: MATCH |
| 3 bucket notifications | `s3api get-bucket-notification-configuration opal-data-bd` | `ProcessAllocationFiles` -> `bd-allocation-processor` (`forwardfill_v2/allocations/`), `GoldLayerPricesTrigger` (`silver/prices/20`), `BronzeCompleteSilverMerge` -> `bd-silver-merge` (`bronze/`): MATCH |
| served merge script ETag c54d0790... | `s3api head-object opal-data-bd code/silver/merge-daily-incremental.py` | `c54d07908c69e2d9a9035050e0367f40`, 2026-07-02T20:49:25Z: MATCH |
| documents Default/Latest | `ssm describe-document` x4 | transaction 3/3, realized 3/3, unrealized 3/3, allocation 5/5: MATCH |
| the fix is the merge script only; `data/cot/` untouched | `git diff --stat HEAD 336a418503 -- data/black_diamond/.../merge-daily-incremental.py data/cot` | 1 file (+16/-3); 0 `data/cot` paths: MATCH |

**Writers of the named property (each BD silver table), counted before the act:**
- transactions **2**: the document's merge step and `bd-silver-merge`;
- allocations **3**: the document, `ProcessAllocationFiles` -> `bd-allocation-processor`, and `bd-silver-merge`;
- unrealized **2**: the document and `bd-silver-merge`;
- realized **2**, HELD.
After the act each of the first three reads **1**. Realized stays 2 by ruling (Z-W24-S4: on sentinel-less Mondays and
Tuesdays it is the only same-day writer; retiring it costs about 26.5 h of staleness).

## The half -- SIGNED

I, `1.0.0_SA_CTO~O`, sign the blast radius in section 2 of the ask, per key, on the COO half's pins:
- the base as measured at 10:22:46Z and re-read here;
- the saved plan sha256 `af1537fdf47099c50f47c7d16d1e95afc1705591d949a728bedfed2b5fc1e214`, re-planned
  `0 to add, 4 to change, 0 to destroy` at the GO;
- the unrealized fix as committed at 336a418503;
- realized HELD.

It covers both branches of every leg in section 2. In particular:
- the DS deploy refused stops unrealized only;
- a consumer trace that finds a same-day reader of `silver/transactions/<date>.parquet` HOLDS transactions;
- any failure rolls back the keys already done.

**Added conditions:**
- (1) The DS deploy leg goes through `.tools/safe-deploy.sh` under the DS lane (CLAUDE.md rule 13). A worker that is
  refused does not route around it; the issuer routes the leg to a DS seat.
- (2) The read-back's "next scheduled `bd-silver-merge` run" is the acceptance. An ad-hoc run is QA only and never the
  evidence (CLAUDE.md "Ad-hoc gold runs are PERMITTED FOR QA").
- (3) The `bd-allocation-processor` Lambda itself is not modified or deleted; only its notification block goes.

**VOID on:**
- any of the COO half's void conditions;
- a touch to `GoldLayerPricesTrigger`, `BronzeCompleteSilverMerge` or realized;
- any `data/cot/` byte;
- a served-silver partition removed.

## Carried to this seat's next MCPINDEX analysis (the issuer's flag)

The BRONZE_COMPLETE sentinel fix sits in the shared `data/cot` ingest, a separate firm's tree (CLAUDE.md: "cot is a
separate firm from bd"). It is not cut from this project. It is placed with the cot ingest's owner at the round-6
analysis.
