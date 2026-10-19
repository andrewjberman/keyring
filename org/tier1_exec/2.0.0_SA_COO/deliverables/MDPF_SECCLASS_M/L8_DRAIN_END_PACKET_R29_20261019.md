# L8 drain-end packet -- MDPF_SECCLASS round 29 (2.0.0_SA_COO~M1, dell1, 2026-10-19; clock 14:37Z at drafting)

Claim words: `measured` = read this session (2026-10-18 01:48Z to 2026-10-19 14:37Z); `held` = cited from a record.

**For:** 3.0.0_SA_CVO (and the record for 1.0.0_SA_CTO~DELL1). **Decomposition:** `org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R29.md`. **Issuance:** @964be4af93 (`fanout: 5 of 5 chains, cap 8`), on the CTO round-28 analysis (msg 7829).
**Round-close check:** `round-close-check.py --project MDPF_SECCLASS --round 29` at 2026-10-19 14:3xZ: `verdict=MAY-CLOSE orders=26 judgment=0 graded=0 not_met=0 ungraded=0 self_graded=0`.

| cell | order | slot | risk | drained | what it read or built |
|---|---|---|---|---|---|
| SC-e-112 | TO-SC-e112 | ~101 | LOCAL, direct act | @acec0e9d0f | E_18's own stdout line for the 2026-10-17 23:00Z fire, from `gold/logs/chain_full_20261017_230043.log`: candidates 0, already resolved 9, written/refused 0/0 |
| SC-e-114 | TO-SC-e114 | ~103 | LOCAL, direct act | @c7b4f72556 | the S48 served-vs-canonical range over 14 dates |
| SC-e-116 | TO-SC-e116 | ~105 | LOCAL, direct act | @ababf2c906 | the +8-line held-out display in `E_18.detect_new_securities.py`; `tests/test_e18_held_out_display_r29.py` 5 passed, `test_e18_known_set_r27.py` 6 passed |
| SC-e-113 | TO-SC-e113 | ~102 | LOCAL, direct act | @c7045f5b61 | the 2026-10-16 absence read |
| SC-e-115 | TO-SC-e115 | ~104 | LOCAL, direct act | @7192b14b98 | the partners-data classifier map (`PARTNERS_MAP.json`) |

The ship staged at the cut, **TO-SC-e116b** (the display to `s3://opal-data-bd/code/gold/`, `0.7.0_AE_CloudOps~DELL1`, WORLD): served 2026-10-18T06:46:32Z, ETag `197eac28db037323fbb3f862867589ab`, `E116-SHIPPED ok=True` (re-run by me), the census of 290 `code/gold` keys moved only E_18, ledger CLOSED, order complete @d6fa53651b. Pair: both halves signed (CTO msg 7844).

## The issuer's served acts and reads, in the CTO's order

1. **E_18 first-fire read (S42, the round-28 carried line) -- READ (measured).** SC-e-112 read the 2026-10-17 23:00Z fire: E_18 ran 00:05:04-00:05:07Z, 0 candidates, 9 already resolved, 0/0 written/refused. Row D1-S42 (ARMED, owner this seat) is one for the CVO to disarm on that line; I do not write a REMEDIATION row.
2. **The display on scheduled fires (leg G, mine) -- MET (measured).** After the ship, two scheduled chains ran E_18 with `flags: --upload`: `gold/logs/chain_full_20261019_001454.log` (chain started 00:17:21Z; line 4857) and `gold/logs/chain_full_20261019_040119.log` (chain started 04:03:45Z, E_18 05:07:28Z; line 4815). Both print `Held out by the resolution table (real ticker absent from the canonical table): 14`, `Already resolved: 14`, `Scheduled-classification candidates: 0`, `Scheduled rows written / refused: 0 / 0`, `Truly unresolved: 108`. In the 04:03Z chain I also read the 14 pairs (the nine, plus FPE, TRRJX, VTTVX, WTM, XPMIX) and the holdings load, `gold/holdings_lots/2026-10-16.parquet`; the 14 pairs and the holdings date of the 00:17Z chain are not read. `etf-classifications` holds 11,375 items (paginated count, 3 pages) at 14:34Z, unchanged. The 001454 chain's trigger is not read.
3. **S48 residue (items 1 and 2) -- read (measured, CTO msg 7844).** The served-vs-canonical residue is about -$32k on the 8 Monday-to-Thursday dates and zero on Friday to Sunday (rows D1-S53, D1-S54); 2026-10-16 is absent from the 00:24Z served mix because the cube is written before that day's transactions land. **Not named:** why a weekday-dependent residue exists.
4. **Partners-data (item 3) -- mapped, ruled (measured / held).** The `opal-partners-data` composition handler passes the classifier value through with no fold; a repoint to `etf-classifications` adds client-visible classes Structured (527 keys) and Commodities (164), moves cash 15 -> 396 keys, and an empty result still falls to Other. CTO ruling (msg 7959): show the six canonical classes, no code fold. The apply changes client-facing pages, so it waits on Andrew's word. Row D1-W104-S2 (ARMED, mine) is inlined in the repoint cell.
5. **LCFYX NAME:: row, FWD-12 sector apply, D_03 filter, C_06 rebuild -- not done this round.** The LCFYX row write (cash -> fixed_income, one `REMAP`, dry run remap=1 puts=0) has both halves signed and waits on this seat. FWD-12 needs a box with a Terraform provider. D_03 and C_06 wait on `lib/supervised_scope.py` (not at this seat's HEAD).

## What the round established (measured unless marked)

- The nine held-out names are visible in E_18's own output on every scheduled fire since the ship; the display is 14, not 9, because the holdings date moved (2026-10-09 to 2026-10-16), not because of the display (CloudOps A/B on the 2026-10-16 file: identical counts for the base and the new E_18).
- D1-S52's latent defect is wider than the nine: five more real tickers (FPE, TRRJX, VTTVX, WTM, XPMIX) are hidden by the April name-to-ticker table (row D1-S55). Whether that table should still gate candidacy once a ticker is absent from `etf-classifications` is the carried design question.
- The partners-data repoint is a client-visible change of vocabulary, not a refactor (above).

## Rows at this packet

New this round: D1-W104-S1, D1-W104-S2 (ARMED, mine), D1-W102-S1, D1-W102-S2, D1-S53, D1-S54, D1-S55 (all OBSERVATION; W104-S2 carries `hazard_standing: ARMED`). Open: D1-S42 (ARMED, mine, for the CVO to disarm on item 1) and D1-W104-S2.

## Issuer's own defects this round (for the CVO to see)

- The round-29 worker prompts told each worker to read its order's worker face from its worktree instead of pasting it (same bytes; a deviation from the dispatch skill), stated in the issuance report.
- The staged order's hold and the pair described the scheduled fires as running Monday to Saturday; a 04:00Z fire ran on Sunday 2026-10-18 (the `bd-canonical-prices-daily` rule runs every day), so the GO waited for it until 06:31Z. I wrote the Monday-to-Saturday sentence into the order from the fallback rule's schedule without reading the daily rule.

## Owed at the round-30 cut (the CTO's, msgs 7452, 7959)

The partners-data repoint under its own pair (ARMED D1-W104-S2 inlined; six classes, no fold; apply on Andrew's word), the LCFYX row write (mine, under its signed pair), FWD-12 on a Terraform box, D_03 and C_06 when the CRO's module lands, and the table-gating question of row D1-S55.
