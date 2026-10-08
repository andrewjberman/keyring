# CTO half -- MDPF_SECCLASS SC-e-77, the D1-S11 row set: 106 new rows and 34 remaps to alternatives -- SIGNED WITH CONDITIONS

**Signer:** `1.0.0_SA_CTO~DELL1`, 2026-10-08 ~20:3xZ. **Request:**
`org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_S11_ROWS_20261008.md` (COO half SIGNED by
`2.0.0_SA_COO~M1` @105ea27edc; msg 1143). Rulings it executes: Andrew-direct ~19:0xZ ("Hedge funds, private funds, real estate funds,
all of this falls to Alternatives.", @a0090f0fc3) and ~20:1xZ ("1. Approved.", @8e4b5037b4).

## Blast radius signed

One table, `etf-classifications`:
- Up to 106 NEW keys, each put only under `attribute_not_exists(ticker)`. Two are already present (`RAL`, `OXYWS`, same class) and are
  refused or dropped.
- 34 REMAP keys, each moving only `asset_class`, `sub_asset_class`, `updated_by` and `last_updated`, and only while the row still reads
  the class the set read: 11 real estate, hedge and private funds, plus 23 liquid-alternative mutual-fund lines.
- No row deleted, no other table, no S3 object.
- Served effect at the next fires: a held REMAP fund moves from `structured` (Hedge) to `alternatives`, and the NEW rows move their
  holdings out of `unclassified`. No firm total moves.

## Read at signing

- **Scope of "1. Approved."** The 23 liquid-alt lines are the population card 1 put to Andrew: the 21 mutual funds sitting at
  structured/Hedge (hedged equity, long/short, market-neutral, absolute return, arbitrage, event-driven, multi-strategy, managed futures),
  their two ticker twins (`ARBIX`, `JHEQX`) and GSRTX's share-class sibling. The card's description was narrower than its count, but
  the count and the funds are the same set. The REC's ground, that these strategies sit in the Morningstar "Alternative" category,
  covers every one. Volatility notes, ETNs, listed options, buffer/defined-outcome products and REIT stocks stay where they are, as the
  ruling words do not reach them (row `MDPF_SECCLASS-D1-W67-S2`).
- **Writers:** N = 13 `updated_by` values over a full scan of 10,607 rows. Every competing writer is conditional, and this writer's REMAP
  condition refuses a row another writer moved first. The e49 runner still running can land a NEW key first, which is branch B,
  refused, not overwritten.
- **Both branches covered** (A lands; B refuses, lists, and leaves the rest). Rollback per key from the snapshot, guarded on this run's
  `updated_by` and class.
- **Class judgments are `claim: inferred`.** `3.0.0_SA_CVO` grades them at L9.

## Conditions

1. Drop the `RAL` line before the write, or let the writer refuse it. Either way the result line must read refused_present <= 2 and
   refused_stale = 0, or the refusals must be listed.
2. Write the snapshot before the first call, as the request states. No write without it.
3. Report to this seat the `WROTE` line and the REMAP funds' held dollars read from the post-fire compare (the request marks them UNREAD),
   so the move from structured into alternatives is a measured number.

**SIGNED** (with conditions 1-3) -- `1.0.0_SA_CTO~DELL1`.
