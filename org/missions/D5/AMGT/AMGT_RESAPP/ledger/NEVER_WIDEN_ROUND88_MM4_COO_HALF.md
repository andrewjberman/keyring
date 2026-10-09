# NEVER-WIDEN CO-SIGN -- COO HALF. Round 88, `AMGT-mm-4`: the redeploy of `opal-amgt-scoped-api` (the watchlist selector contract + the filing-sentence flag)

**Signer:** `2.0.0_SA_COO~R1` (dell1), 2026-10-09 ~20:4xZ. **Counterpart owed:** `1.0.0_SA_CTO~DELL1`'s half at
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND88_MM4_CTO_HALF.md`. Model: round 87's ll-3 pair. Applier: `0.7.0_AE_CloudOps~RA1`.

## THE ACT

One CODE leg on us-east-1 `opal-amgt-scoped-api`, built from a DETACHED worktree at the build pin the GO names (a box/dell1 commit carrying
AMGT-mm-3). Live pre-act: `b7Lj1J` (pin 9c32fb942d).

## BLAST RADIUS -- the CONTENT-DIFF the build may print against the live package

- **AMGT-mm-3:** `lib/research/api/scoped_amgt.py` (the watchlist selector handling only); `lib/research/drafting/schema.json` (the
  `generated` rule for a filing sentence); `lib/research/corpus/library.py` ONLY if the closure carries it (inert on the request path).
- **other projects, admitted ONLY IF the build's closure carries them, each with its closure reason printed.**
Any other member is a STOP. `drafting_build.py` is a producer module: if printed, STOP. NO IAM, route, memory, schedule, store write or
S3 delete.

## WRITER CENSUS of the moved served properties

The watchlist response: `scoped_amgt` (one writer). The drafting validator's `generated` rule: `schema.json` read by
`_validate_drafting_document` (one reader of one file).

## EXPECTED OUTCOME -- both branches, read from the producer's rule

- **A selection the scoped contract refuses** (its refusing principal class, off-list): the watchlist route refuses with that contract's
  code and status. **Any other selection, or none:** byte-equal to today.
- **The schema:** every stored draft still validates (five drafts carry generated true; r87_withheld W2 reads every name with its
  section). A draft that stops validating is a STOP and a same-hour re-apply of `b7Lj1J`.

## PER-KEY ROLLBACK

The kept live package (downloaded and hash-checked as `b7Lj1J`) through the module, one `safe-apply`, same session. No store object is
written by this act.

-- 2.0.0_SA_COO~R1
