# NEVER-WIDEN CO-SIGN -- COO HALF. Round 97, `AMGT-bd-2`: the ONE redeploy of `opal-amgt-scoped-api` serving a withheld listing's sector BY LISTING KEY, with its source and as-of date

**Signer:** `2.0.0_SA_COO~R1` (dell1), 2026-10-11 ~20:2xZ. **Counterpart owed:** `1.0.0_SA_CTO~DELL1`'s half at
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND97_LISTING_SECTOR_REDEPLOY_CTO_HALF.md`. Model: `NEVER_WIDEN_ROUND95_CLASSIFICATION_REDEPLOY_COO_HALF.md` (+ its CTO half, msg 4042).
Applier: `0.7.0_AE_CloudOps~RA1`. Source: CTO round-96 analysis `ledger/ROUND_ANALYSIS.round96.md` section 2 item 1 (msg 4084; the round-95 ADDENDUM 1 fallback fired); order
`task-orders/AMGT_RESAPP.TO-AMGT-bd-2.redeploy-the-scoped-api-carrying-the-listing-sector-on-the-scratch-pin.md`.
**Written from a ROUTE-BY-ROUTE MEASUREMENT taken from the pin's OWN worktree** (a detached checkout of `08d5ea2920`, so the measuring tree IS the built tree, unlike round 95), against
the live function; instruments `deliverables/2.0.0_SA_COO~R1/round94_prep/checks/`, `round95_prep/checks/`, `round97_prep/checks/`.

## THE ACT

One CODE leg on us-east-1 `opal-amgt-scoped-api`, built from a DETACHED worktree at **`08d5ea2920`** on the scratch branch `scratch/r97-bd2-pin` (never merged): PARENTED on `b3512d18fb`
(the live package's own build input) plus exactly `lib/research/api/scoped_amgt.py` (`9b13bf0371d4`) and `lib/research/api/monthly_chatter.py` (`38e9511ccc9c`) as `box/dell1` carries
them at `fa5caf93dc` (`AMGT-bd-1` merged @fa5caf93dc). Live pre-act: `TmeKvn83XnePF4RrJUQKIpbzYdH4VnCmvyXePbs3KB8=` (apply 2026-10-11T18:03:15Z, built at `b3512d18fb`).
`box/dell1` HEAD is NOT the pin (it carries AMGT_CORPUS's unpaired round-47 corpus files), and a pin from `15b7af1601` is refused (CTO, msg 4080). **Every changed line of the two api files
between `b3512d18fb` and `fa5caf93dc` was read: each is an `AMGT_RESAPP-bd-1` hunk.**

The rule (read at the cut): where the classifications-table row is WITHHELD (round 95: the row's name disagrees with the registered name), the entry also carries the listing's own
sector, read from ITS stored model block by KEY: `_listing_sector(security_key)` takes the key's newest `derived/model_block/<key>/<stamp>/model_block.json` through the existing
`_read_model_block_pool`, the `figures[]` record whose `mnemonic` is `GICS_SECTOR_NAME`, and returns `{sector, sector_source: 'Bloomberg, listing', sector_as_of: YYYY-MM-DD of the object
folder's stamp}`; absent, empty, a non-string key or ANY exception returns None and the entry stays withheld with no sector. **The `classification` object stays withheld** (null with
'classification not available for this listing'); a ranked row's `sector_reason` becomes null where its sector is served. It never serves "a matching value" from any row: the CVO's
point (C-S90) is that the LISTING KEY discriminates, since the collided `SAN` row also reads Health Care.

## THE MEASUREMENT (the expected outcome is its reading)

Instrument: the LIVE function's response (Lambda invoke, GET) against the checkout-at-the-pin's own `scoped_amgt.handler` on the same live pool; every JSON path compared.

| route (instrument) | reads | paths changed | where |
|---|---|---|---|
| overlay + peers, all MEASURED subjects (`r94_name_table.py`) | **243 subjects x 2 routes** | **0** | none |
| ranked lists (`r94_rankings_table.py`) | 4 lists, 188 rows | **8** | row 67 of TRENDING/PRICE and BREAKOUT/PRICE (`SAN_FP_Equity`): `sector`, `sector_source`, `sector_as_of`, `sector_reason` |
| rank timeseries asked for EVERY measured subject's ticker x 4 combinations (`r95_series_by_ticker_table.py`) | 4 x 243 series | **24** | `SAN_FP_Equity` and `CSL_AU_Equity`: `sector`, `sector_source`, `sector_as_of` x 4 combinations each (the 4 listed SAN series of `r94_rankings_table.py` are a subset) |
| collected chatter list x 3 windows (`r94_other_routes_table.py`) | days 30, 90, 365 | **9** | row 73 (SAN FP): `sector`, `sector_source`, `sector_as_of` x 3 |
| timeline of 12 subjects, thesis of 12 subjects (`r94_other_routes_table.py`) | 24 reads (`NVO_US_Equity` thesis 404 before and after) | **0** | none |

**41 sector paths in all, on two subjects; 0 paths of any other kind.** The sector census (`r97_sector_serve_census.py --where local`, merged tree) reads 6 of 6: K1 2 ranked
rows, K2 2 rank series, K3 3 chatter rows serve 'Health Care' with source 'Bloomberg, listing' and the block's date; K4 each withheld ticker asked for by ticker serves it and not
the table row's name; K5 the other 186 ranked rows and 186 series carry no new key and equal their table row's classification; K6 no per-security route carries a classification.
The round-95 census (`r95_classification_census.py`, K1 changed by the issuer, row W393-S1) reads 6 of 6 and `r94_display_name.py` 12 of 12 against the same tree.

### The changed values, whole

| subject / entry | key | live serves | pin serves |
|---|---|---|---|
| `SAN_FP_Equity` ranked row 67, both PRICE lists | `sector` | null | 'Health Care' |
| | `sector_source`, `sector_as_of` | (absent) | 'Bloomberg, listing'; '2026-10-11' |
| | `sector_reason` | 'classification not available for this listing' | null |
| `SAN_FP_Equity` rank series, 4 combinations; chatter row 73, 3 windows | `sector`, `sector_source`, `sector_as_of` | (absent) | 'Health Care'; 'Bloomberg, listing'; '2026-10-11' |
| `CSL_AU_Equity` rank series asked by ticker, 4 combinations | `sector`, `sector_source`, `sector_as_of` | (absent) | 'Health Care'; 'Bloomberg, listing'; **'2026-09-30'** (its newest stored block) |

NOT moved, and the compare must show it: every `classification` object (the two listings' stay null with the reason), every `name`, `name_state`, score, rank, peer member (0 of 2,230),
the thesis, the timeline, every other subject's row, series and chatter entry (K5: 372 judged, 0 carry a new key), the PROD page. **CSL AU's sector reads as of 2026-09-30**: its newest
stored block is that old (the `sector_as_of` says so; withholding by age is not this cell).

## BLAST RADIUS -- the CONTENT-DIFF the build may print against the live package, each member admitted by BLOB at the GO

Measured by `r94_admission_table.py 08d5ea2920 --pin b3512d18fb`: **two members differ at the pin**.

| member | blob at the live build input `b3512d18fb` | blob at the pin `08d5ea2920` | admitted for | the only change admitted |
|---|---|---|---|---|
| `lib/research/api/scoped_amgt.py` | `ec7c8fde988b` | `9b13bf0371d4` (+44 -0) | `AMGT-bd-1` | `LISTING_SECTOR_MNEMONIC`, `LISTING_SECTOR_SOURCE`, `_listing_sector`; its call in `_drop_disagreeing_table_names` (ranked rows) and in `_rank_series_names`; the series copy of the three keys in `read_rank_series` |
| `lib/research/api/monthly_chatter.py` | `5243b870cac5` | `38e9511ccc9c` (+2 -0) | `AMGT-bd-1` | the withheld chatter row also carries the three keys from `scoped_amgt._listing_sector(key)` |

Every other member is BYTE-EQUAL to the live package, **including `lib/opal_naming.py` (`5748320303cb`), `lib/research/corpus/dossier.py` (`dc2ce428d015`)**, `team_sheet.py`,
`names_read.py`, `engine.py` and `analyze.py` (`4d1f93c978f0`): the pin is the live package's tree with two files. **Any other member is a STOP**, including any corpus file at a blob other
than the live package's. NO IAM, route, memory, schedule, store write or S3 delete. The act writes NO data object. The one new read at request time is the withheld listing's own
model block through the reader `_with_subject_cap` already uses (at most the two listings per request; an S3 failure leaves the entry withheld).

## WRITER CENSUS of the moved served properties (N printed, each rule read)

- ranked `rows[].sector`, `rows[].sector_reason`: **TWO** rules in order: `_join_classification` (the table; a row with no classification) then `_drop_disagreeing_table_names` (round 95 nulls
  them, this act sets them from the listing). **N = 2.** `rows[].sector_source`, `rows[].sector_as_of`: **ONE**, `_drop_disagreeing_table_names`. **N = 1.**
- rank `series[].sector`, `sector_source`, `sector_as_of`: **ONE**, `_rank_series_names` (the merge) with its copy in `read_rank_series`. **N = 1.**
- collected-chatter `rows[].sector`, `sector_source`, `sector_as_of`: **ONE**, the row builder in `monthly_chatter.read_monthly_chatter`. **N = 1.**
- the value itself: **ONE** reader, `_listing_sector` (the model block's `GICS_SECTOR_NAME` figure of the listing's own key).
- NOT moved: `classification`, `name`, `name_state`, `classification_reason` (round 95's writers N = 2, 1, 2 unchanged).

## EXPECTED OUTCOME -- both branches, read from the rules above

- **Branch 1 (the table's reading):** exactly the 41 paths above, each from the value shown to the value shown. Every other path of every route read byte-equal, every status the same.
  The post-act compare re-runs the four table scripts against the recorded pre-apply baseline plus the census (AC1) and the NOT-moved set (AC2, AC3).
- **Branch 2 (anything else):** a path changed that is not in the table, a status other than 200, a changed `classification` or `name` or score or rank or member, a sector served for a row
  whose table name AGREES, a sector from any source other than the listing's own block, a changed dossier field, or a content-diff member the table does not admit: **STOP** and, inside
  the same hour, a rollback unless the CTO names KEEP on the evidence (order bound 7).

## ROLLBACK (per key; the act writes no data object)

| what | may touch | rollback |
|---|---|---|
| `opal-amgt-scoped-api` code | the function's code package, nothing else | the KEPT live package (`TmeKvn83..`, downloaded and hash-checked BEFORE the apply) through the module: ONE `safe-apply`, same hour |
| `lambda-source-map.json` entry | the function's one entry | the printed before value, restored in the commit that reverts |
| change-management entry | one entry, opened before and closed after | closed `ROLLED_BACK` with the reason |

Not a portal PROD push (Andrew's word 2026-10-11 ~16:2xZ: nothing promotes to PROD until he visually smokes DEV). The PROD-built page reads this API, so the two subjects' list sector appears
there as the API serves it (the reading ruled by the CTO at msg 3948).

## SEQUENCING AND THE GO (the GO is the issuer's; RA1 does nothing before it)

1. THIS pair signed (both halves, at the table above). 2. AMGT_CORPUS: this act carries NO AMGT_CORPUS blob; their /13 redeploy (waiting on its template put) re-measures at its own GO
against the function this act leaves, and retires both scratch pins. `2.0.0_SA_COO~C1` is told the CodeSha256 and apply time. 3. The pin: `08d5ea2920`; the GO prints
`r94_admission_table.py 08d5ea2920 --pin b3512d18fb` in the build worktree (2 members, blobs equal) and `r94_naming_replay.py --pin b3512d18fb` (YES). 4. `AMGT-aa-5` and
`AMGT-ff-4` are closed; no other write to this function or the stored objects is in flight (RA1 reads the change-management ledger and the open deploys of every live worktree and prints
the denominator). 5. The scratch branches `scratch/r95-aa5-pin` and `scratch/r97-bd2-pin` are KEPT. 6. RA1 re-reads the baselines immediately before the apply; a Bloomberg pull between
them moves a model block's vintage, and with it a `sector_as_of`: the prediction and the compare read the as-of from the same block, so a newer block is a read, not a STOP, provided the
sector VALUE and the key set equal the table's.

**COO HALF: SIGNED** by `2.0.0_SA_COO~R1`, for the act, branches 1 and 2, the blast radius and the rollback above. **CTO HALF:** owed by `1.0.0_SA_CTO~DELL1`.
