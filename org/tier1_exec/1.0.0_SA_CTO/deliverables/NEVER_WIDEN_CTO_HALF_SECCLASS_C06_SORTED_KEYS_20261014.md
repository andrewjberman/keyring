# NEVER-WIDEN -- CTO half: C_06 writes `mix_daily_summary.json` with sorted keys (MDPF_SECCLASS cell SC-e-102) (`1.0.0_SA_CTO~DELL1`, 2026-10-14 ~12:5xZ)

**Pairs with:** `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_C06_SORTED_KEYS_20261014.md` (`2.0.0_SA_COO~M1`, msg 5531;
the COO half is signed after the 23:00Z re-base read). **Authority:** XA-20261014T113939Z-a304 (the follow-up the laptop CTO named) and this seat's round-24 analysis,
section 4 item 3 (@94da0b08da).

## Read by this seat at signing

- **The code delta:** `git show 717405d44e` changes ONE line in `C_06.client_mix_timeseries.py`, from `json.dumps(payload, separators=(',', ':'))` to
  `json.dumps(payload, sort_keys=True, separators=(',', ':'))`, plus a new test file. No other line of C_06 changes.
- **The served object = the issuance base:** `head-object s3://opal-data-bd/code/gold/C_06.client_mix_timeseries.py` reads ETag `f847d8d105025ffbee94b1aa5092faf6`,
  VersionId `jGO15I3AZTATLbGxE3_36dKm86wuggDK`, 66,473 bytes, LastModified 2026-10-13T06:22:23Z. The md5 of `git show 3e1365fdaa:<the file>` is `f847d8d1...`, so the deploy
  delta is exactly the one line.

## Signed for, exactly as the request states

- **The act:** one code object, `safe-deploy.sh` of that one file, outside any BD gold run, with the ledger opened before and closed after. Nothing from `lib/`, D_03, D_04,
  a table, a watermark or a data key rides it. D1-S39 is satisfied: the served classifier is not in the act.
- **Blast radius:** BYTES move once, CONTENT does not, on four families:
  - the mix daily summary;
  - `firm_mix_views_daily.json` and its alias;
  - the 56 advisor `mix_daily.json` files and their aliases;
  - `platinum/firm/mix_summary.json`, whose total moves by at most $0.000001 (measured max 2.4e-7). That is below every display precision, and this seat accepts it as a
    no-content move.
- **Writers N = 1 per family,** as counted. **Both branches and the STOP state as written.** **Rollback per key as written:** the code by VersionId, and the data by the
  VersionIds leg P enumerates at the ship.

## Conditions (this half's own)

- **C1 -- the order of served causes.** No two served causes share a fire: the ship follows the 23:00Z fire and the re-base read (the issuer's order, adopted here). Branch 1's
  unchanged-input run is C_06 ALONE (no D_03 or D_04), outside any scheduled fire window. Its restore target is the mix-summary VersionId read IMMEDIATELY before that
  run, not today's `sB5iD9...`, which the 23:00Z fire will supersede.
- **C2 -- the dell1 restart at 21:00Z** (Andrew's word, msg 5483). The ship and Branch 1 run after the restart. A ledger opened before 21:00Z and not closed is read
  across every live worktree before any re-execution (CLAUDE.md NEVER-2).

**CTO HALF: SIGNED** by `1.0.0_SA_CTO~DELL1`, with C1 and C2. The commit carrying this file is the signature's vintage.

-- 1.0.0_SA_CTO~DELL1
