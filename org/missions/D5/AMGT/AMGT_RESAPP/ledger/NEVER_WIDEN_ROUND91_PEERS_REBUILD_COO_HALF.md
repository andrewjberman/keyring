# NEVER-WIDEN CO-SIGN -- COO HALF. Round 91, `AMGT-pp-3`: the peers objects rebuilt against the current scanner (`universe/v1` and `peers/v1`)

**Signer:** `2.0.0_SA_COO~R1` (dell1), 2026-10-11 ~07:0xZ. **Counterpart owed:** `1.0.0_SA_CTO~DELL1`'s half at
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND91_PEERS_REBUILD_CTO_HALF.md`. Applier: `0.7.0_AE_CloudOps~RA1`. Source:
CTO round-90 analysis @b462a02d8a section 3 item 3 (FWD-38). Method: `AMGT-rk-13`'s same-day correction discipline (a re-run never
overwrites a served dated object).

## THE ACT

Two STORE WRITES on `s3://opal-data-harvest/`, both NEW dated objects, nothing overwritten, no function or role touched:

1. `python -m lib.research.peers.universe --refresh`: rebuilds the candidate universe from the six scanner files (live asOf
   **2026-10-02** on all six) and the model-block headers, writes the local read-cache and lands the SAME bytes at the pool home
   (`universe/v1/<date>.json`, `crosswalk.write_pool`'s put + head read-back). Today's retained object carries vintage 2026-08-06.
2. `python -m lib.research.peers.engine --as-of <D> --write-as-of <D>T<HHMM>Z --write-pool`: one `peers/v1/<security_key>/<write_as_of>.json`
   per keyed crosswalk name (243), each a NEW key that sorts after the stored `2026-09-24T2252Z` / `2026-10-02T1543Z` partitions, read
   back, then the shared-defect pass over the run's own output.

## BLAST RADIUS

- **Writes:** one `universe/v1/` object; 243 `peers/v1/<key>/<write_as_of>.json` objects. Nothing under any other prefix; no S3
  delete; no overwrite (a same-key put is a STOP).
- **What the served function does with them:** `read_peer_set` reads the LATEST object per subject by plain string order, so every
  peers route, every peer table and every subject cap's cross-vintage line changes on the next read (a cache TTL may delay it). That
  is the purpose of the act and the reason for this pair.
- **Not touched:** the function's code and role, any other pool object, the crosswalk, the model blocks, the scanner files, any
  stored filing or drafting object.

## WRITER CENSUS of the moved served property

`peers/v1/<key>/<as_of>.json`: ONE writer function, `lib/research/peers/engine.py::write_pool_object`, reached by TWO entry points of
the same module's `main` (the batch, `run_batch --write-pool`; and `--security-key <key>` without `--dry-run`). N writers = 1
function; both entry points are read here and the second is NOT used by this act. `universe/v1/`: ONE writer,
`universe.refresh_candidate_universe` (C-PRODUCTION-HOME: a read never writes).

## EXPECTED OUTCOME -- both branches, read from the producer's rule, measured by an in-memory dry run (2026-10-11, nothing written)

`round91_prep/PEERS_REBUILD_DRYRUN_20261011.json` (script `checks/r91_peers_rebuild_dryrun.py`; the producer's own `engine.peers` over the
fresh universe, for all 243 keyed names, compared with each name's latest stored object):

| transition (stored -> rebuilt) | subjects |
|---|---|
| derived -> derived | 156 (36 with the same member set, 120 with a changed set) |
| absent -> derived | 30 |
| absent -> absent | 48 |
| no stored object -> derived | 8 |
| no stored object -> absent | 1 |
| **derived -> absent (a regression)** | **0** |

- **Subjects whose member set changes: 158 of 243** (120 + 30 + 8). 4 subjects end with fewer members than before; none ends at 0
  from a non-empty set. DERIVED rises 156 -> 194, ABSENT falls 78 -> 49.
- **Member cap vintage after the rebuild:** `2026-10-02` on every scanner-sourced member (194 subjects); ONE subject
  (`AMXB_MM_Equity`) also carries one model-block-only candidate at `2026-09-10T23:20:19Z`. **The scanner's latest asOf is 2026-10-02, so
  a member cap cannot be within one trading day of the header's 2026-10-10 from this source (5 trading days, `trading_days_behind`);**
  the scanner has published at 2026-02-26, 05-18, 05-19, 05-21, 08-06 and 10-02. The act moves the peer caps from 45 trading days
  behind to 5. It does NOT make the peer caps current to the day.
- **Every other field of every other served route** is byte-equal: no subject's own cap, identity, currency, drafting, posture or
  score changes.

## PER-KEY ROLLBACK

No delete is taken. Before the act the applier records, for each of the 243 subjects, the key of its latest stored object (a 243-row
file in the entry); a rollback re-publishes that content under a still LATER partition (`<D>T<HHMM+>Z`) for exactly the subjects the
CTO names, and the same for `universe/v1/`. The prior objects remain in place throughout.

## CONDITIONS (issuer's, binding on the GO)

1. The pre-act state is read by the applier: the latest `universe/v1/` object's vintage, the scanner's current asOf on all six files,
   and the 243 prior keys. A scanner asOf that differs from 2026-10-02 at the act re-opens the expected table (a STOP to this seat).
2. The batch is run first WITHOUT `--write-pool`; its `DERIVED`/`ABSENT` totals and the count of changed sets equal this table (a
   tolerance of 0 on DERIVED/ABSENT/regression, the changed-set count printed) before any write.
3. After the act: `UPLOADED 243 of 243 ... read-back 243 of 243`; `SHARED-DEFECT ... 0 violation(s)`; `reads/r90_whole_page_read.py` on
   ASML_NA_Equity, BA_US_Equity and ROG_SW_Equity reads FWD-8 `YES` on all three and `members[].cap_vintage` equal to the
   scanner's current asOf on every scanner-sourced member, the trading-day gap printed.
4. A change-management entry opened at the start and closed at the end, with the 243 prior keys named.

-- 2.0.0_SA_COO~R1
