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

## v0.3 amendment -- PRESERVE FIFO reconstruction as an independent custodian-latency sanity check (Andrew-direct 2026-06-25)

Andrew-direct: do NOT fully retire FIFO reconstruction. We have no visibility into custodian-side ETL latency/errors, so an independent FIFO-from-our-own-transactions check on the custodian-direct lots is worth its (small) cost. This REVISES the earlier "retires B_01 FIFO" framing: B_01 is **repositioned from the serving path to a VALIDATION lane**, not deleted.

**Design change -- a SECOND hash on `fact_lot_unrealized`:**
- `lot_uid` (per-snapshot, +occurrence-index) -- the SERVING row key (unchanged; serves the custodian-direct ULN lots).
- **`lot_lineage_id`** = deterministic hash over the lot's natural identity `(account_id, cusip, acquired_date, cost_per_share)` -- a PERSISTENT comparison key. This is the "additional hash." It is the grain at which the FIFO-reconstructed lots and the custodian ULN lots are compared (sum qty/cost within the key; the key is not row-unique -- 289 collisions on 06-18 -- so the comparison aggregates to it, which is fine for a parity check).

**The validation lane:** the FIFO reconstruction (B_01 logic, rebuilt on `fact_transaction`) produces reconstructed lots keyed on the SAME `lot_lineage_id` -> compare vs custodian ULN at that grain -> divergence beyond tolerance = a **custodian-latency / error flag** (the sanity check). Serving stays custodian-direct (lean); FIFO is the cross-check.

**Honest cost (it is slightly more than "just a hash"):** = the `lot_lineage_id` hash (trivial) + RETAINING the FIFO reconstruction compute (the B_01 logic) + RUNNING it to compare. Mitigation: run the FIFO check **sampled / periodic** (e.g. a daily sample of accounts, or a full weekly pass), NOT a nightly full-recompute -- so it's a cheap watchdog, not a return to the heavy nightly FIFO. The transactions raw material (`fact_transaction`) is already required, so the marginal cost is the retained logic + a bounded check run.

**Patch-register update:** B_01 / `is_ghost` move from "EXCISE (retire)" to "REPOSITION (validation lane)". The bd_stale/is_ghost flag becomes meaningful again ONLY inside the validation lane (a FIFO-reconstructed position the custodian doesn't confirm = a divergence signal), not in the served path.
