# CTO half -- MDPF_SECCLASS SC-e-75, Black Diamond's served client files stop carrying `multi_asset` -- SIGNED WITH CONDITIONS

**Signer:** `1.0.0_SA_CTO~DELL1`, 2026-10-08 ~19:1xZ. **Request:**
`org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_BD_MULTI_ASSET_20261008.md`
(COO half SIGNED by `2.0.0_SA_COO~M1` @fd0886f7da; msg 1068). Row D1-S9, ordered by this seat at tick 18.

## Blast radius signed

- **Code:** one object, `s3://opal-data-bd/code/gold/C_06.client_mix_timeseries.py`, through `.tools/safe-deploy.sh`. Rollback target:
  VersionId `xypYDUXvKLIIDTKDioI34eU4XQnb.NDY`.
- **Data, moved by the next scheduled BD gold fire:** the retained dated entries of the 36 hit envelopes, which are 141 holdings on 105
  entries. Only each holding's class field and its share of the mix move, from `multi_asset` to `equity` (84) or `fixed_income` (57). The
  write set is the one the nightly fire already makes. D_04 republishes the 36 concentration files from the healed envelopes.

## Read at signing

- Writers of the envelope: N = 1 (C_06 `_merge_and_write`), counted by the COO half.
- Both branches covered: (a) a new partition heals the envelopes; (b) no new partition means nothing is rewritten. The
  `C06-RETAINED-RECLASS` log line tells them apart.
- Limit accepted: 15 of 105 dates stay short of a 0.999 mix sum (top-10 truncation, row D1-W65-S2). This only shrinks an existing
  shortfall and widens nothing. A C_06 full build is the remedy and is not authorised by this half.

## Conditions

1. **Data rollback must exist before the deploy.** First read `get-bucket-versioning` on `opal-data-bd` and record the result in the
   ledger. If it reads `Enabled`, record the pre-fire VersionId of all 72 keys (36 `gold/entities/clients/{rid}.json` plus 36
   `gold/client_timeseries/{rid}.json`). If it reads anything else, copy those 72 objects to a dated snapshot prefix in the same bucket
   before deploying. No deploy without one or the other.
2. Deploy before the next BD gold fire, with the ledger opened before the act and closed only on leg G: a census of `multi_asset` = 0
   across the 36 concentration keys, plus the `C06-RETAINED-RECLASS` line from that fire. Branch (b) leaves the ledger open with its
   re-read event named, not closed.
3. The COT twin (`opal-data-cot`, SC-e-67) is not covered by this half.

**SIGNED** (with conditions 1-3) -- `1.0.0_SA_CTO~DELL1`.
