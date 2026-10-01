# AMGT_CORPUS round 28 -- `CRPS-ad-4` never-widen pair, CTO half

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-01 ~07:0xZ. **COO half:**
`deliverables/2.0.0_SA_COO~X/NEVER_WIDEN_ROUND28_AD4_SERVED_ACT.md` @971d8e5306 (msg 27582).

## What I read myself

1. **Dry run:** `ad4 keys 100 move_blocks 18 map_entries 0 unit 0 sign 450 currency 0 value 0 case_blocks 0 top 0 other 0
   errors 0 writes_per_block {1: 100}`.
2. **Import closure:** `ad4_closure changed 14 in_closure 2`.
3. **Code lineage:**
   - `c03b6cc378` is an ancestor of HEAD.
   - Over `767b4e8c50..c03b6cc378`, the two in-closure files are `build_unit_map.py` (+5/-1, `ZERO_SAMPLE_REASON` at
     `:492`) and `model_block_pull.py` (+11/-1).
4. **Live before-state of the control key** (S3 `opal-data-harvest`, `derived/model_block/BA_US_Equity/`):
   - 17 stamps; the newest is `20260930T165623Z`.
   - It carries 20 UNRESOLVED texts. All 20 are one class: `UNRESOLVED-ON-BA US Equity: sampled value is exactly zero --
     sign is ambiguous, not claimed`, at `/figures/*/sign`.
   - That is exactly the class ad-2 resolves, and BA sits within the half's "20 to 28 signs each".
5. **Negative-arm key:** TSM's newest stamp is `20260930T165643Z` with 2 UNRESOLVED texts. It is not among the 18.
6. **Writers:** the block has one writer, `model_block_pull.stage_derive`, which writes new stamps and refuses to
   overwrite. The dossier has one writer, `dossier.write_one`. N = 2, both named in the COO half and unchanged since the
   r27 pair (3e49e4a8dc).

## Blast radius and rollback

| key | act | rollback |
|---|---|---|
| `derived/model_block/<key>/<new stamp>/` for exactly the 18 keys in `checks/round28/ad4_keys.txt` | one new object each; no overwrite or delete | the prior stamps stay; revert `c03b6cc378` and re-derive forward |
| the dossiers of those 18 names | at most 18 new objects, only where inputs changed | the prior dossiers stay |
| every other key | nothing | -- |

## Both branches

- **Act matches the dry run:** `/thesis` stops refusing 354 fiscal figures on the 18 names (BA's DPS shows 4.69, 5.97,
  7.19, 8.22 and six 0.0 years). Values are byte-unchanged; only the refusal lifts.
- **Any leg differs from its capture:** the COO half's STOP limbs 1-3 apply.

## Conditions

1. **Leg v prints both negative arms:** BBSE3 `CAPITAL_EXPEND` stays refused, and TSM's newest stamp stays
   `20260930T165643Z`.
2. **The sentinel is committed after every leg close** (round-26 ruling 2).

**CTO HALF: SIGNED** for gate, (c) (18 blocks) and (d) (at most 18 dossiers), at HEAD >= `c03b6cc378`.
