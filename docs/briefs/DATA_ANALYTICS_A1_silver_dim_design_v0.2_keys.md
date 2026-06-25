# DATA_ANALYTICS A1 -- Silver dim design v0.2: LOCKED join keys + key-type resolution

**Supersedes** the key/grain section of `..._full_flow_AtoD_and_silver_dim_design_v0.1.md` (the A->D flow + table list stand). This locks the join keys, EMPIRICALLY VERIFIED against the latest Schwab silver partitions (06-18), and resolves the two open subtleties. **Author:** 0.4.0_DS_ClientPlatform, 2026-06-25.

## Universal join keys (verified 100%)
- **`account_id`** = 10-digit zero-padded Schwab id (`'0010023253'`). IDENTICAL across ACC/RPS/ULN/RLD; = TRN `account_id_padded` (NOT `account_id_schwab`, which is unpadded). RPS-in-ACC 100%, TRN-in-RPS 100% (modulo closed/cash-only accts). The spine of every join. xref bridges to BD legacy via `schwab_padded_id = account_id`.
- **`cusip`** = security key, 100% populated (ticker 99.7% + drifts on rebrand). Join securities on cusip; ticker is a `dim_security` display label.

## Locked per-table keys (PK verified against 06-18 data)

| Table | Grain / PRIMARY KEY | Key type | FKs | Verified |
|---|---|---|---|---|
| **`dim_account`** | `account_id` | **NATURAL** (clean) | relationship_id (household, self-ref); xref→bd | ACC account_id UNIQUE (0 dups) |
| **`dim_security`** | `cusip` | **NATURAL** | -- | (confirm cusip->1 name/asset_class in v1.0) |
| **`fact_position`** | (`date`,`account_id`,`cusip`,**`position_type`**) | **NATURAL composite** | account_id, cusip | (date,acct,cusip) NOT unique (7 collide, max 4) -- splits across **cash/margin/short**; unique only with the qty_cash/margin/short discriminator. See note A. |
| **`fact_lot_unrealized`** | **SURROGATE `lot_uid`** | **SURROGATE REQUIRED** | account_id, cusip | NO natural key exists -- (acct,cusip,acquired_date,cost_per_share,current_quantity) STILL collides on rows identical in ALL columns. See note B. |
| **`fact_lot_realized`** | (`close_event_id`,`open_event_id`) | **NATURAL composite** (clean) | account_id, cusip | UNIQUE (0 dups). close_event_id alone is the parent sell-event (1 close : many open lots, max 85). |
| **`fact_transaction`** | **HASH `txn_uid`** over the natural cols | **HASH SURROGATE prudent** | account_id (←account_id_padded), cusip | TRN has NO stable id; rows are distinct but the natural key is ~8 fragile cols (acct,trade_date,cusip,tran_code,qty,net,gross,price,transaction_detail). 0 fully-identical rows. See note C. |
| **`dim_fee`** | (`account_id`,`effective_date`) | **NATURAL** (SCD) | account_id | (fee feed = the non-custodian gap) |

## Resolved subtleties

**Note A -- fact_position grain (cash/margin/short split):** RPS carries `quantity_cash` / `quantity_margin` / `quantity_short` -- a single (account,cusip) can be held across these sub-positions (up to 4 rows). So the RAW grain is (date, account_id, cusip, position_type∈{cash,margin,short}). DECISION: store fact_position at this natural grain (preserves the cash/margin/short truth), and the **holdings/AUA view AGGREGATES to (date, account_id, cusip)** summing market_value (the AUA grain gold wants). Don't collapse at silver -- collapse at the holdings view, so margin/short detail isn't lost.

**Note B -- fact_lot_unrealized has NO natural key:** even (account_id, cusip, acquired_date, cost_per_share, current_quantity) collides on rows that are IDENTICAL in every column (6 truly-dup rows + 12 indistinguishable-collision rows on 06-18). Two genuinely indistinguishable open lots cannot be told apart by ANY natural combination. RESOLUTION: dedup the fully-identical rows (keep one), then assign a **deterministic surrogate `lot_uid`** = a within-(account_id, cusip) ordered sequence (sorted by acquired_date, cost_per_share, current_quantity) OR a content-hash + occurrence-index. Deterministic ordering required (the ADHC_GLDINC oracle-fix lesson) so the surrogate is stable run-to-run.

**Note C -- fact_transaction needs a hash:** rows are genuinely distinct (the 6-col-key collisions differ in transaction_detail/gross_amount), so no dedup-collapse -- but there is no stable custodian txn id and the full natural key is ~8 columns. RESOLUTION: a **content-hash `txn_uid`** over the deterministic natural-column tuple. This doubles as the **dedup + aberration-excision control point** (the curated-list/rule-based excision keys off txn identity here -- the $4B-withdrawal class is identified + excised at this surrogate).

## Surrogate-key landscape (the discussion input)
- **Clean NATURAL keys (no surrogate):** `dim_account` (account_id), `dim_security` (cusip), `fact_lot_realized` (close_event_id, open_event_id), `dim_fee` (account_id, effective_date).
- **NATURAL composite, ugly but valid:** `fact_position` (date, account_id, cusip, position_type) -- natural works; surrogate optional for join-ergonomics.
- **SURROGATE/HASH genuinely PRUDENT (no/fragile natural key):** `fact_lot_unrealized` (`lot_uid` -- no natural key exists at all) and `fact_transaction` (`txn_uid` hash -- fragile 8-col natural key + it's the dedup/aberration anchor).

These two are exactly where the custodian data gives us no stable row identity -- so a deterministic surrogate is not gold-plating, it's required for stable joins, idempotent incremental loads, and (for txn) the aberration-excision hook.
