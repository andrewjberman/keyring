# NEVER-WIDEN CO-SIGN -- COO HALF. Round 89, `AMGT-nn-7`: the ONE redeploy of `opal-amgt-scoped-api` (peer identity + subject cap vintage + AMGT_CORPUS dossier /11)

**Signer:** `2.0.0_SA_COO~R1` (dell1), 2026-10-11 ~03:4xZ. **Counterpart owed:** `1.0.0_SA_CTO~DELL1`'s half at
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND89_NN7_CTO_HALF.md`. Model: round 88's mm-4 pair. Applier:
`0.7.0_AE_CloudOps~RA1`. CTO round-88 analysis item 8: this is the one redeploy that carries the dossier at /11 (or /12 if
AMGT_CORPUS `CRPS-at-4` finds the master template); it is not cut a second time in round 90.

## THE ACT

One CODE leg on us-east-1 `opal-amgt-scoped-api`, built from a DETACHED worktree at the build pin the GO names (a box/dell1 commit
carrying `AMGT-nn-2` and `AMGT-nn-3` merged AND AMGT_CORPUS's dossier method). Live pre-act: `KlosR/ap8O3tYrjDfNkUofT/vTQ5pTt32EvYL8mCqs8=`
(pin 4d006edc74, round 88 mm-4, LastModified 2026-10-09T22:55:03Z, dossier /10).

## BLAST RADIUS -- the CONTENT-DIFF the build may print against the live package

- **`AMGT-nn-2`:** `lib/research/api/scoped_amgt.py` (the `_with_listed_identity` decorator and its one call site in `read_peer_set`
  ONLY); `lib/research/peers/listed_identity.py` (new, pure).
- **`AMGT-nn-3`:** `lib/research/api/scoped_amgt.py` (the `_with_subject_cap` decorator and its one call site ONLY);
  `lib/research/peers/subject_cap.py` (new, pure).
- **AMGT_CORPUS leg p:** the dossier-method modules the CTO's half names by path and hash (`lib/research/corpus/dossier.py` at the
  /11 or /12 METHOD_VERSION and any module AMGT_CORPUS's own served-act half admits). Their halves bind them; this half only
  admits that they may ride the same package.
- **other projects, admitted ONLY IF the build's closure carries them, each with its closure reason printed.**

Any other member, and any scoped_amgt.py line outside the two decorators and their two call sites that is not AMGT_CORPUS's
admitted dossier reader change, is a STOP. NO IAM, route, memory, schedule, store write or S3 delete. `crosswalk.py`,
`add_security.py` and `mass-deletion-check.sh` (nn-4, nn-5) are producer or hook modules: if the closure prints one, STOP.

## WRITER CENSUS of the moved served properties

`/security/<key>/peers` `members[].security_key` and `members[].identity`: `read_peer_set` (one writer; `_with_numeric_tickers` writes
the same two fields for an all-digit ticker and `_with_listed_identity` is disjoint from it by construction: a numeric ticker is not an
alphabetic one). `peers.subject.{market_cap_musd, market_cap_raw, market_cap_vintage, cap_vintage, cap_source, cap_stored_vintage,
cap_refresh}`: `read_peer_set` (one writer after nn-3). The dossier: AMGT_CORPUS's own census in its half.

## EXPECTED OUTCOME -- both branches, read from the producer's rule

- **A United States alphabetic-ticker member the crosswalk holds under `<TICKER> US`:** serves `security_key` and
  `identity.resolution` MEASURED with `matched_as` `us_listed_ticker`. **Any other member** (not held, non-US, numeric, already
  MEASURED): byte-equal to today.
- **The subject cap:** when the subject's current model block states CUR_MKT_CAP, the five cap fields move to it and
  `cap_refresh.status` reads REFRESHED with the stored vintage kept in `cap_stored_vintage`; when it does not, or the read fails,
  the stored cap is served unchanged with `cap_refresh.status` ABSENT or UNREADABLE and a plain reason. **Every other subject field
  and every member field** is byte-equal to the stored object's. No stored object is rewritten.
- **Currency (item 2, D1-S14) does NOT move:** a member's `price_currency` / `price_currency_reason` is byte-equal to today. A
  resolved key with no model block yields the same reason text; if a text changes it is a STOP, because no cell moves it.

## PER-KEY ROLLBACK

The kept live package (downloaded and hash-checked as `KlosR/ap8O..`) through the module, one `safe-apply`, same hour. It serves dossier
/10, so a rollback is also a dossier-version rollback. No store object is written by this act.

## CONDITIONS (issuer's, binding on the GO)

1. The pin carries `AMGT-nn-2` and `AMGT-nn-3` merged (ancestry read by the applier at the pin, not taken on the issuer's word).
2. The content diff of the built package against the kept live package is printed WHOLE before any upload.
3. After the act: `r89_peers_deployed.sh` reads `R89 PEERS DEPLOYED: YES`, and `r89_deployed_close.sh --want <the GO's method>` reads
   `R89 DEPLOYED CLOSE: YES` (dossier method, the withhold, the listing no-regression pair), each with the function's CodeSha256
   re-read in the same output.
4. The source map records the deploy (`record-terraform-deploy.sh`, entry before and after), as mm-4's AMENDMENT 1 did.

-- 2.0.0_SA_COO~R1
