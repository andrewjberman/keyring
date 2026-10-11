# NEVER-WIDEN CO-SIGN -- COO HALF. Round 91, `AMGT-pp-6`: the ONE redeploy of `opal-amgt-scoped-api` carrying the round's served cells

**Signer:** `2.0.0_SA_COO~R1` (dell1), 2026-10-11 ~07:0xZ. **Counterpart owed:** `1.0.0_SA_CTO~DELL1`'s half at
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND91_REDEPLOY_CTO_HALF.md`. Model: round 89's nn-7 pair (COO half
`NEVER_WIDEN_ROUND89_NN7_COO_HALF.md`). Applier: `0.7.0_AE_CloudOps~RA1`. Source: CTO round-90 analysis @b462a02d8a section 3 item 6.

## THE ACT

One CODE leg on us-east-1 `opal-amgt-scoped-api`, built from a DETACHED worktree at the build pin the GO names (a box/dell1 commit
carrying the cells below that are then merged). Live pre-act: `l8egBo/rfEH4ddCEFyWnUOb9BvN3bGu/azarul5Ho0g=` (pin a943b1b412,
LastModified 2026-10-11T04:56:11Z, dossier /11).

## BLAST RADIUS -- the CONTENT-DIFF the build may print against the live package, each member admitted by BLOB at the GO

| member | admitted for | blob at the cut (2026-10-11, box/dell1 HEAD) | the only change admitted |
|---|---|---|---|
| `lib/research/peers/numeric_tickers.py` | `AMGT-pp-1` | `85db6ab86b6f` (moves with pp-1) | one added pure function, `name_match_fields`; `numeric_fields`, `name_token`, `japan_forms` unchanged |
| `lib/research/api/scoped_amgt.py` | `AMGT-pp-1`; `AMGT-pp-4` only if its answer has landed and it is merged | `cbccb2d08b3f` (moves) | pp-1: the one extension of `_with_numeric_tickers` ONLY; pp-4: the answer's reader and its call at the currency decorator ONLY |
| `lib/research/peers/price_currency.py` | `AMGT-oo-5` (round 90, merged @a423f1d667) | `ba913ab145d4` | the `answered` parameter and `answered_currency`; nothing is served until pp-4's reader calls it |
| `lib/research/identity/crosswalk.py` | `AMGT-nn-5` (round 89, merged @04ecb2d528), by blob | `3603be4be89a` | `write_pool` guard and `main` early refusal: producer-CLI paths the function never calls |
| other projects | only if the build's closure carries them, each with its closure reason printed | -- | -- |

Any other member is a STOP. NOT admitted: `lib/research/identity/add_security.py` (producer CLI), `lib/research/filings/analyze.py`
(`AMGT-pp-2` is producer-side; the function's closure does not import `lib/research/filings`), `.tools/git-hooks/mass-deletion-check.sh`
(`AMGT-oo-3`). NO IAM, route, memory, schedule, store write or S3 delete.

## WRITER CENSUS of the moved served properties

`/security/<key>/peers` `members[].security_key` and `members[].identity`: THREE writers in `read_peer_set`, disjoint by ticker form:
`_with_listed_identity` (a United States alphabetic ticker, nn-2), `_with_numeric_tickers` (an all-digit ticker: Japan code, then exact
name), and the new exact-name arm inside `_with_numeric_tickers` (any other non-US ticker). N = 3 rules read. `members[].price_currency*`:
`_with_price_currency` (one writer; pp-4 adds its answered input, and only when merged).

## EXPECTED OUTCOME -- both branches, read from the producer's rule

- **A non-digit member that is not a United States alphabetic ticker whose name token names exactly one held company:** serves
  `security_key` and `identity.resolution` MEASURED with `matched_as` `company_name`. Measured 2026-10-11 against the 243 subjects'
  latest stored peers objects: 18 such members, 0 served today (`checks/r91_name_match_deployed.py`). **Any other member** (no held
  name, a name two held companies share, numeric, United States alphabetic, already MEASURED): byte-equal to today.
- **Currency:** byte-equal to today unless pp-4 is in the pin; with pp-4, only a United States alphabetic member the answer covers with
  a three-letter code and no record key (or a record stating none) gains `price_currency`, `price_currency_claim` `measured` and
  `price_currency_source`; a failed or absent answer read serves no currency and a plain reason.
- **Everything else** (subject cap, dossier /11, the withhold, the listing, every figure) is byte-equal: the no-regression arm below.

## PER-KEY ROLLBACK

The kept live package (downloaded and hash-checked as `l8egBo/rf..`), one `safe-apply`, same hour. No store object is written.

## CONDITIONS (issuer's, binding on the GO)

1. The pin carries `AMGT-pp-1` merged; `AMGT-pp-4` only if its answer has landed and its cell is merged (ancestry read by the applier
   at the pin, not taken on the issuer's word); `AMGT-oo-5` and `AMGT-nn-5` are already ancestors.
2. The blob of every admitted member at the pin is printed beside this table's column and any difference beyond the admitted change is
   a STOP; the content diff of the built package against the kept live package is printed WHOLE before any upload.
3. After the act: `r89_peers_deployed.sh` reads `R89 PEERS DEPLOYED: YES`, `r89_deployed_close.sh --want amgt-corpus-dossier/11` reads
   `R89 DEPLOYED CLOSE: YES` (the no-regression arm), and `r91_name_match_deployed.py` reads `R91 NAME MATCH DEPLOYED: YES`, each with
   the function's CodeSha256 re-read in the same output.
4. The source map records the deploy (`record-terraform-deploy.sh`, entry before and after).
5. AMGT_CORPUS (`2.0.0_SA_COO~C1`) is asked in the GO whether a leg rides; a leg that rides brings its own pair and blobs.

-- 2.0.0_SA_COO~R1
