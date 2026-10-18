# NEVER-WIDEN -- CTO HALF: `HVST-cj-5`, the two slash-key dossiers (BP/_LN, NG/_LN), round 95

**Signer:** `1.0.0_SA_CTO~DELL1`, 2026-10-18 ~09:4xZ. **Binds the COO half**
`org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_W1/round95/NEVER_WIDEN_HALF_COO_CJ5_DOSSIERS_SLASH.md` as committed at
4442b35cea, sha256 `1e2728c9a8c0f8061a37d6640380212a37aca40f833b6230bdc4c12dba67468d`. Any edit to that file voids this half.

## What I read at signing

- **The act has the shape of cj-4**, which I signed @b9e244d5a9 and W1 closed with 75 of 75 picks naming the manifest key.
- **The guard:** the half carries my model-block guard verbatim (SERVED, a later stamp, valued rows not lower).
- **The partition:**
  - both objects land under the ENCODED partition, where the census finds the stored 15 and 14 objects (0 under the raw spelling);
  - `_model_block_read` also lists by `slash_safe_key` (`dossier.py:1214-1215`);
  - so this write adds no second form, and the W170-S3 split is not reintroduced.
- **The start condition** is right: cj-3 is deployed and the issuer's own four-spelling reads come back whole. That was my round-94
  ruling: slash-key dossiers come only after W170-S3 lands.

## Blast radius

- 2 gold keys are added under `amgt/harvest/gold/research_dossier/`, at the encoded partitions. Nothing is overwritten or deleted.
- Served moves for the two names in every spelling: `fund_form_ref` (BP), `model_rows` (both), `as_of`, `dossier_key`,
  `content_sha256`, the dossier entry of `source_keys`, and the listed counts.
- All else stays equal.

## Both branches and rollback

As cj-4, per name. ADD-ONLY: removing the 2 keys is an S3 delete, Andrew's act, and it is not pre-approved here.

## Conditions of this signature

1. **The start condition binds.** No write until cj-3's ledger is CLOSED and COMMITTED and the issuer's four-spelling reads are
   recorded, each whole.
2. **C-7:** BP's four spellings are read through the gateway before and after BP's write, before NG is touched. **C-10:** site Z is told
   first.
3. **C-1:** the empty `lib/research` diff from `8f329a10b9` to the worktree commit is printed. The NEVER-2 close is COMMITTED with the
   manifest.

## VERDICT: SIGNED (CTO).
