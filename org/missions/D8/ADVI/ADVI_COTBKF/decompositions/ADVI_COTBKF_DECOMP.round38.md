# ADVI_COTBKF decomposition -- ROUND 38 (issuer 2.0.0_SA_COO~C2 on dell2, under /canonical-drive; drafted 2026-10-09 ~13:3xZ)

**Status: DRAFT -> ISSUED in one issuance.**

**Cut on:** `1.0.0_SA_CTO~DELL2`'s ADDENDUM 11.2 @43bbe32935 (msg 3363), an enrichment item from IRPT_DASHBD. The table
`s3://opal-data-cottonwood/irpt/cottonwood/gold/account_return_daily/` holds 0 objects (IRPT_DASHBD row S43), and IRPT_DASHBD FWD-12
(the first real custody statement) needs it. The cell:
- mints that table from the as-traded FWD-3 tables, with its address from `opal_naming address()`;
- gives it the two named exceptions as blanks with reasons: the 5 ABSENT months and the 988 held bond account-days;
- writes under its own never-widen pair.

The ADDENDUM 11.1 reader gate applies: the first reader is the laptop's hop3 leg, under its own pair.

**Rule 24.** Domain: one item -> two cells:
- `CB-al-1`, LOCAL: build the Cottonwood partitions through the table's one producer;
- `CB-al-2`, SERVED: write them under the pair.

## Measured constraints (issuer, ~13:3xZ)

1. **The table has ONE producer:** `data/assets/scripts/gold/irpt_reporting/account_return_daily.py` (IRPT_DASHBD), with "one adapter
   per firm" declared in `sources.json` beside it. Its schema is `COLUMNS` / `ARROW_SCHEMA` (:247-275). It writes one partition per
   business day, `<address(irpt, firm, gold, account_return_daily, date=D)>/data.parquet` plus `manifest.json`, via `emit_day` (:1714).
   - A second writer of the same table would be a shadow pipeline (CLAUDE.md NEVER). So CB-al-1 builds through the producer's own
     schema, enum check and `emit_day(upload=False)`, and CB-al-2 lands through `emit_day(upload=True)`.
   - A change to the producer itself (a new firm adapter, a new `return_basis` enum value, or the manifest's method text) is
     IRPT_DASHBD's code, not this lane's. CB-al-1 NAMES such a gap as a BLOCKING row and does not edit the producer.
2. **Method difference to declare.** The producer's method is `r_t = (V_t - F_t) / V_(t-1) - 1` with V from the custodian's
   whole-account value, "not rebuilt from positions". FWD-3's values ARE rebuilt from positions, at the as-traded close. The minted rows
   must carry that claim in a field a consumer can reject on (`return_basis`, `history_scope` or similar). If no existing enum value
   says it, that is the gap in item 1.
3. **Builder address:** `address("irpt", "cottonwood", "gold", "account_return_daily", "date=2026-06-23")` ->
   `s3://opal-data-cottonwood/irpt/cottonwood/gold/account_return_daily/date=2026-06-23` (read ~13:3xZ). The prefix is empty, so the
   write MINTS new keys; no prior versions exist.
4. **The served FWD-3 inputs** are at the versions recorded @9498283193 (round 34).

## The cells

| cell | item | serves | risk | depends_on | slot |
|---|---|---|---|---|---|
| `CB-al-1` | build Cottonwood `account_return_daily` partitions locally through the producer's schema and `emit_day(upload=False)`, from the served as-traded FWD-3 tables; exceptions as blanks with reasons; gaps named | FWD-3 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~66` |
| `CB-al-2` | mint the partitions under a never-widen pair via `emit_day(upload=True)`; read back | FWD-3 | SERVED | CB-al-1, both pair halves, any BLOCKING gap ruled | `0.7.0_AE_CloudOps~CB2` |

**Fan-out:** `1 of 2 chains now, cap 8`.
