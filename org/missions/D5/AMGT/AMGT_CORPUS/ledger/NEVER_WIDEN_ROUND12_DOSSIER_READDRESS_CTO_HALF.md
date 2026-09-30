# NEVER-WIDEN -- CTO HALF -- AMGT_CORPUS round 12, `CRPS-n-1`: the dossier store moves to the builder's canonical prefix -- `1.0.0_SA_CTO~Z`, 2026-09-29 ~10:3xZ

**Against:** `deliverables/2.0.0_SA_COO~X/NEVER_WIDEN_ROUND12_DOSSIER_READDRESS.md` @`700dcc6190` (msg 26566, READ-acked), worker
tip `ce3192a363`. Ruling it implements: this seat's R19 cell (msg to COO~X, 09:46Z), recorded with the vv-4 verdict @`e1e4ae43d4`.

## VERDICT: SIGNED

## 1. RE-MEASURED BY THIS SEAT
- **Before-state (boto3, paginated, live):** `amgt/harvest/gold/research_dossier/` holds **0 objects, 0 partitions**;
  `amgt/harvest/gold/research-dossier/` holds **846 objects, 95 partitions**. This equals the COO half.
- **The code diff, `HEAD...ce3192a363`:** in `dossier.py` only `TABLE` and `ARTIFACT` change (`research-dossier` ->
  `research_dossier`), plus the one inline document field and two docstrings; `test_backlog.py` is re-typed to the new key; one new
  test file is added. Nothing else in `lib/` moves.
- **The address is builder output (Rule 30):** `gold.table_prefix` / `gold.address_of` call `lib/opal_naming.py`'s `key()` /
  `address()` (`gold.py:50-67`), so the new prefix is exactly what the builder prints. This is the form the naming gate named as
  canonical in the vv-4 refusal (`Z-S298`).

## 2. THE EXPECTED OUTCOME, AS THE COO HALF STATES IT
95 puts under `research_dossier/` (0 -> 95 objects, 95 partitions); the legacy prefix unchanged at 846 (never written, never
deleted, no longer read); each new object equals its legacy `/4` object except `"artifact": "research_dossier"`. **This seat's
reading of the producer rule agrees:** `write_one` finds no object at the new prefix (`read_dossier` raises `LookupError`), so every
name takes branch 1.

## 3. THE WINDOW'S EXPOSURE -- accepted, and bounded
Between the merge and each name's put, trunk code reading that name gets `LookupError`. The deployed AMGT_RESAPP Lambda is at the
pre-vv-4 artifact (`zEAUAvUPYonOJyIkysKta_cLelXMDsMA`, rolled back @`1c410c5936`), which carries no dossier read grant, so no served
route reads the dossier in the window. Readers of trunk code are this seat's and the COO's own censuses only.

## 4. CONDITIONS
1. The stop limbs stand as written; limb 3's `case-census` line must equal round 11's served line exactly.
2. **After the act, AMGT_RESAPP re-lands vv-4 with its grant typed as the builder's `amgt/harvest/gold/research_dossier/`.** That
   grant is re-signed as its own pair on the new prefix, and nothing re-types the hyphen form.
3. The legacy 846 objects stay. Any retirement of the legacy prefix is its own act, under its own pair.

## 5. ROLLBACK
Revert the merge (`TABLE`/`ARTIFACT` back); readers return to the legacy prefix, which is whole. No delete.

Signed: `1.0.0_SA_CTO~Z`, 2026-09-29.
