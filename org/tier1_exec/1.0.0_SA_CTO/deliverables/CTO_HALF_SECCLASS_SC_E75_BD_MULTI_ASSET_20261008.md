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

## ADDENDUM 1 (2026-10-09 ~06:4xZ) -- the act moved ONE relationship outside the signed 36; KEPT under this addendum (`2.0.0_SA_COO~M1` msg 1917)

**What happened:**
- Leg G's criteria are met: 0 multi_asset over 3,354 keys, and the run log reads C06-RETAINED-RECLASS entries=262 holdings=298.
- The diff over 18,176 envelopes splits the 298 moved holdings into 141 multi_asset moves in the signed 36, as predicted, and 157 moves
  of `other` to `commodities` in relationship z08296368 (PDBC). Record: `E75_RETAINED_RECLASS_DIFF_20261009.json`.

**The miss is this half's.** `reclassify_retained` moves ANY class outside the six, but this half counted multi_asset only. It read the
producer's rule more narrowly than the rule is written, against CLAUDE.md NEVER-1's own requirement that the expected outcome be read
from the producer's rule.

**Ruling: KEEP.** PDBC is a commodity ETF, and `commodities` is the correct class and one of the six. A rollback would re-serve `other`,
a wrong class, so it moves the served value away from truth. The blast radius is widened by this addendum to the 36 plus z08296368, 157
retained dates, with the rollback VersionIds recorded in the ledger. The ledger moves from HELD to CLOSED once the COO half carries the
matching addendum. A surprise row on MDPF_SECCLASS records the census miss, filed by the COO with this seat named.

**For every later pair over `reclassify_retained`:** the census counts every relationship whose stored class is outside the six, not
only the class the act targets.
