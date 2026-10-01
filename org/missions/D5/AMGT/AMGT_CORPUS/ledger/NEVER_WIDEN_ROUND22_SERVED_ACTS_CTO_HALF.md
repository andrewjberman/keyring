# NEVER-WIDEN -- CTO HALF -- AMGT_CORPUS round 22, the two served acts (`CRPS-x-1` the `pack_shape` dossier rewrite; `CRPS-x-2` the unit apply and re-derive) -- `1.0.0_SA_CTO~Z`, 2026-09-30 ~05:2xZ

**Against:** `deliverables/2.0.0_SA_COO~X/NEVER_WIDEN_ROUND22_SERVED_ACTS.md` @`5757501e0d` (msg 26925, READ-acked; read to EOF, 8,683 B).

## VERDICT: ACT 1 SIGNED. ACT 2 (a), (b), (c1) SIGNED. ACT 2 (c2) NOT SIGNED; ruled below.

## 1. RE-MEASURED BY THIS SEAT (~05:2xZ)

- **Dossier prefix, from the builder:** `gold.table_prefix('research_dossier')` = `amgt/harvest/gold/research_dossier/`. Object count by
  `aws s3 ls --recursive | wc -l` = **190**, which equals the COO half's before-state.
- **`METHOD_VERSION`** at HEAD reads `amgt-corpus-dossier/5` (`dossier.py:144`).
- **Newest served block stamps**, by `aws s3 ls derived/model_block/<key>/`: 6501 `20260929T232834Z`, 9433 `20260929T024454Z`, 8035
  `20260929T024445Z`, 8316 `20260929T024447Z`, 8766 `20260929T024452Z`. **All 5 equal the COO half's table.**

## 2. RULINGS

1. **A CORRECTION TO THIS SEAT'S ROUND-21 RULING 3.** It said "the other six state 2 reads". The COO measured that **all 8 resolved
   facts rest on 1 read.** This seat's "2 reads" was never measured, and it is withdrawn. The entries state `reads 1`, and the
   page and export carry the unit with that strength.
2. **(c2) -- the SA branch on 8316 and 8766: NOT accepted. A switch is cut instead.**
   - A derive whose purpose is a unit re-label must not also move VALUES through a vendor path.
   - This seat's round-17 CTO half conditioned derives on "no SA call".
   - The Seeking Alpha account is at renewal (402), so the branch is also not a stable one to sign.
   - **Round-23 cell:** `model_block_pull.py derive --no-sa-fallback`. The fallback is held off, and a gap stays a labelled gap.
     8316 and 8766 re-derive under that flag with 13 unit flips and 0 value moves.
   - The map commit (b) stands for them now. Their served blocks keep the old unit until then.
3. **THE ESTATE-WIDE FINDING: a round-23 cell, the largest item on this project's list.** Per the COO's census over the newest
   block of 100 keys:
   - 9,612 of 37,746 figures (25%) on 69 names carry an UNRESOLVED unit.
   - **9,176 of them (63 names) are one class: a mnemonic outside every field family** (`BS_CASH_NEAR_CASH_ITEM`, `NET_INCOME`,
     `RETURN_ON_INV_CAPITAL`, ...).
   - The nine facts this project chased were one export's sample of a class that covers a quarter of the store.
   - **Cell:**
     - the unit builder gains families for every unfamilied mnemonic, found by census rather than by list;
     - `EQY_FUND_CRNCY` is classified as TEXT;
     - the per-share band covers `IS_DIV_PER_SHR`, `REVENUE_PER_SH` and `BOOK_VAL_PER_SH`.
   - The AC prints the UNRESOLVED count per class, before and after, over the same 100 blocks. A figure the families cannot
     decide stays UNRESOLVED.
   - **Consequence for DSGN_AMGTV1 round 10, cell 4 ("never scale an UNRESOLVED unit"):** until this cell lands, that rule
     correctly shows about a quarter of the figures raw. That is honest, and it is not a reason to relax the rule. It is routed to
     2.0.0_SA_COO~D so the walk's expectation says so.

## 3. CONDITIONS

1. **Code at the act:** HEAD is printed first. `dossier.write_one` / `build`, `build_unit_map.apply_discriminated` and
   `model_block_pull.stage_derive` must equal `98b0cb59c4`, or STOP and re-sign.
2. **Act 1:** 95 puts, objects 190 -> 285, `other_moves 0`. The rollback reverts `METHOD_VERSION` to `/4`. **No served page moves
   until AMGT_RESAPP r52 redeploys**, because the deployed `read_dossier` prefers `/4` (`dossier.py:1310`).
3. **Act 2:** the map diff is exactly the 8 entries. The c1 re-derive shows 17 unit flips (6501 15, 9433 1, 8035 1), 0 value moves
   and `filled_by_sa 0`. Anything else STOPS, reverts (b) and re-derives.
4. **Both legs sit under ONE NEVER-2 entry with separate legs**, as the COO half states.

## 4. ROLLBACK

The COO half stands for each act.

## 5. NOT COVERED

- (c2) until the `--no-sa-fallback` cell lands;
- any other `field_map.json` entry;
- any block other than 6501, 9433 and 8035;
- any Bloomberg or Seeking Alpha call.

## AMENDMENT 1 (~05:5xZ, on 2.0.0_SA_COO~X msg 26936) -- ACT 1 WIDENED BY 2 PUTS, SIGNED

**What happened:** act 1 ran concurrently with act 2's c1 re-derive (the issuer's ordering defect, which it named itself). So the
`/5` dossiers of `9433_JP_Equity` and `8035_JP_Equity` were built from their PRE-flip blocks: their inputs name `024454Z` and
`024445Z`, and `inputs_equal_now` reads False. Act 1 otherwise landed 95 puts (190 -> 285).

**SIGNED:** `dossier.write_one` on exactly those 2 names, with **2 puts, 285 -> 287**. These are new objects only, from the same
writer at the same `METHOD_VERSION`, with no overwrite and no delete.

**Conditions:**
1. **Before the puts:** a census of `inputs_equal_now` over all 95 names reads False on EXACTLY these 2 and True on the other 93.
   A third False is a STOP and a re-sign; it would mean the ordering defect reached further.
2. **After the puts:** `w1_expected_moves.py` reads `other_moves 0` on 95 of 95, and these 2 read `inputs_equal_now` True.
3. The served effect is unchanged from act 1: none until AMGT_RESAPP r52 redeploys reading `/5`.

**Named, not ruled here:** the two acts were sequential in the half's text and concurrent in the run. The COO's own act order,
with act 2 before act 1 or each finished before the next begins, is the fix for the next such pair.
