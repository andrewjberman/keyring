# NEVER-WIDEN CO-SIGN -- COO HALF. Round 95, `AMGT-aa-5`: the ONE redeploy of `opal-amgt-scoped-api` carrying the withheld classification (D1-S26) and the initialism casing

**Signer:** `2.0.0_SA_COO~R1` (dell1), 2026-10-11 ~17:3xZ. **Counterpart owed:** `1.0.0_SA_CTO~DELL1`'s half at
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND95_CLASSIFICATION_REDEPLOY_CTO_HALF.md`. Model: `NEVER_WIDEN_ROUND94_NAME_REDEPLOY_COO_HALF.md` (+ CTO half
@c53a86ef41). Applier: `0.7.0_AE_CloudOps~RA1`. Source: CTO round-94 analysis `ledger/ROUND_ANALYSIS.round94.md` section 3 items 2 and 4 and ADDENDUM 1 (msg 3986: SAN FP's
classification is withheld too; no second source this round); order `task-orders/AMGT_RESAPP.TO-AMGT-aa-5.redeploy-the-scoped-api-carrying-the-withheld-classification-and-the-initialism-casing.md`.
**This half is written from a ROUTE-BY-ROUTE MEASUREMENT of the merged tree against the live function** (instruments at `deliverables/2.0.0_SA_COO~R1/round94_prep/checks/` and
`round95_prep/checks/`; named per row below), not from the cells' descriptions.

## THE ACT

One CODE leg on us-east-1 `opal-amgt-scoped-api`, built from a DETACHED worktree at the build pin the GO names: **`b3512d18fb`** on the scratch branch `scratch/r95-aa5-pin`
(never merged), which is the LIVE package's own build pin `15b7af1601` plus exactly `lib/research/api/scoped_amgt.py` (`ec7c8fde988b`) and `lib/research/api/monthly_chatter.py`
(`5243b870cac5`) as `box/dell1` carries them at `fe7175efde`. Live pre-act: `VNcX9ntm83qe07/eOOD16AYsDmoEp20eCzj9ljfGvGE=` (LastModified 2026-10-11T14:57:44Z, read 17:3xZ).
**Why a scratch pin and not `box/dell1` HEAD:** since `15b7af1601` AMGT_CORPUS's round 47 (`CRPS-aw-1`) landed `lib/research/corpus/dossier.py` (`13463426d0da`),
`team_sheet.py` (`0442f28ed1f6`), `template.py` and `factset_descriptions.json` on the shared branch; no pair of THIS act admits them and the dossier file moves the served dossier
pick. Every hunk of the two api files between the two commits was read line by line: each is an `AMGT_RESAPP-aa-2` or `aa-4` hunk.

The rules (read at the cut): (1) `AMGT-aa-2`, when a table row's name disagrees with the security's registered name (`names_read.names_disagree`, `AMGT-ff-1`), NO field of that row
is served: `classification` null, `sector` null with `sector_reason`, and `classification_reason`, all `classification not available for this listing`, on the ranked rows, the rank
series and the collected-chatter rows; the rank series also resolves a ticker through every MEASURED crosswalk record (`_measured_ticker_index`), not only the 95 covered names.
(2) `AMGT-aa-4`, `CSL` and `JD` join the declared initialisms of `DISPLAY_NAME_ACRONYMS`. **`analyze.py` (`AMGT-aa-1`, producer-side, never imported by the API) is NOT in the pin.**

## THE MEASUREMENT (the expected outcome is its reading)

Instrument: the LIVE function's response (Lambda invoke, GET) against the merged tree's own `scoped_amgt.handler` on the same live pool; every JSON path compared. The measurement tree
is `box/dell1` at `fe7175efde` or later; it differs from the pin only in the corpus files above, which none of these routes read (RA1's pre-apply step re-runs the three scripts
against the pin's own worktree and reports the local prediction against this half, as it did for ff-4).

| route (instrument) | reads | paths changed | where |
|---|---|---|---|
| overlay + peers, all MEASURED subjects (`r94_name_table.py`) | **243 subjects x 2 routes**, 2,230 peer members | **3** | `CSL_AU_Equity`: overlay `display_name`, overlay `peers.subject.display_name`, peers `subject.display_name`; **0 members changed** |
| ranked lists (`r94_rankings_table.py`) | 4 lists, 188 rows | **6** | row 67 of TRENDING/PRICE and BREAKOUT/PRICE (`SAN_FP_Equity`): `classification`, `sector`, `sector_reason` |
| rank timeseries asked for EVERY measured subject's ticker, 4 combinations (`r95_series_by_ticker_table.py`) | 4 x 243 series | **24** | `SAN_FP_Equity` (`classification`, `classification_reason` x 4); `CSL_AU_Equity` (`classification`, `classification_reason`, `name`, `name_state` x 4) |
| collected chatter list x 3 windows (`r94_other_routes_table.py`) | days 30, 90, 365 | **6** | row 73 (SAN FP): `classification`, `classification_reason` x 3 |
| timeline of 12 subjects (`r94_other_routes_table.py`) | 12 | **0** | (the SAN word cloud moved with ff-4 and does not move again) |
| thesis of 12 subjects (`r94_other_routes_table.py`) | 12 (11 served, `NVO_US_Equity` 404 before and after) | **0** | two generation clocks only; no name, classification or corpus field |

**39 name and classification paths in all, on two subjects (`SAN_FP_Equity`, `CSL_AU_Equity`).** The classification census (`r95_classification_census.py --where local`,
merged tree) reads 6 of 6: K1 2 ranked rows, K2 2 rank series, K3 3 chatter rows withheld with the reason; K4 no per-security route (overlay, thesis, peers, coverage, compare,
timeline) of a disagreeing subject carries a classification; K5 186 ranked rows and 186 series of the other subjects equal their table row's own; K6 each disagreeing ticker asked for
by ticker serves no table row's name or classification.

### The changed values, whole

| subject / row | path | live serves | merged serves |
|---|---|---|---|
| `SAN_FP_Equity` ranked row 67, both PRICE lists | `classification` | `{asset_class equity, sub_asset_class 'Health Care', sector 'Health Care', sector_source ...}` | null |
| | `sector` | 'Health Care' | null |
| | `sector_reason` | (absent) | 'classification not available for this listing' |
| `SAN_FP_Equity` rank series, all 4 combinations | `classification` | the same object | null |
| | `classification_reason` | (absent) | 'classification not available for this listing' |
| `SAN_FP_Equity` collected-chatter row 73, 3 windows | `classification`, `classification_reason` | the object; none | null; 'classification not available for this listing' |
| `CSL_AU_Equity` rank series asked by ticker, 4 combinations | `classification` | `{equity, sub_asset_class 'US Large Cap', sector null, sector_reason ...}` (Carlisle's) | null |
| | `classification_reason` | (absent) | 'classification not available for this listing' |
| | `name` | 'Carlisle Cos Inc' | 'CSL Ltd' |
| | `name_state` | `SERVED` | `ABSENT` (a crosswalk-filled row's existing reading) |
| `CSL_AU_Equity` overlay, peers | `display_name`, `peers.subject.display_name` | 'Csl Ltd' | 'CSL Ltd' |

Read as: the two securities whose table row names another company stop being served that row's classification on every route that serves one, and CSL's series name stops being
Carlisle's (round 94's stated limit, closed: the lookup widens). NOT moved, and the compare must show it: every `classification` object and `sector` of every other subject (K5:
372 judged, 0 differ), every score, rank, figure, date and peer member, every name other than CSL's series name and display casing, the thesis, the timeline, the PROD page.
**SAN FP loses its 'Health Care' sector on the list routes** (a legacy classification under a Santander-cleaned name; the CTO ruled it so, msg 3986): it is withheld, not wrong.

## BLAST RADIUS -- the CONTENT-DIFF the build may print against the live package, each member admitted by BLOB at the GO

Measured by `r94_admission_table.py b3512d18fb --pin 15b7af1601`: **two members differ at the pin**; the GO re-runs it in the build worktree and every blob below must match.

| member | blob at the live pin | blob at the build pin | admitted for | the only change admitted |
|---|---|---|---|---|
| `lib/research/api/scoped_amgt.py` | `9d7de3ba726f` | `ec7c8fde988b` (+32 -4) | `AMGT-aa-2`, `AMGT-aa-4` | `CLASSIFICATION_WITHHELD_REASON`; `_drop_disagreeing_table_names` also nulls `classification`/`sector` and sets `sector_reason`; `_rank_series_names` withholds and gives `classification_reason`, its lookup `{**_measured_ticker_index(), **_covered_bloomberg_index()}`; `_measured_ticker_index`; `read_rank_series` copies `classification_reason` onto the series; `CSL` and `JD` added to `DISPLAY_NAME_ACRONYMS` with their source comment |
| `lib/research/api/monthly_chatter.py` | `dc171ab6ce5f` | `5243b870cac5` (+8 -1) | `AMGT-aa-2` | a collected-chatter row whose table name disagrees with the registered name serves `classification` null and `classification_reason`; one `_crosswalk_names()` read per request |

Every other member is BYTE-EQUAL to the live package, **including `lib/opal_naming.py` (`5748320303cb`)**, `dossier.py` (`dc2ce428d015`), `team_sheet.py`, `names_read.py`,
`engine.py` and `analyze.py` (`4d1f93c978f0`): the pin is the live pin's tree with two files. **Any other member is a STOP**, including any corpus file at a blob other than the
live pin's. NO IAM, route, memory, schedule, store write or S3 delete. The act writes NO data object.

The builder replay (`r94_naming_replay.py --pin 15b7af1601`, run 17:3xZ against `box/dell1` HEAD's builder): 35 requests all 200, **88 builder calls, 18 distinct, 0 differ**
(`PASS P2`); at the pin itself the builder is the live package's own, so the replay is the identity.

## WRITER CENSUS of the moved served properties (N printed, each rule read)

- ranked `rows[].classification` and `sector`: **TWO** rules in order: `_join_classification` (the table's row) then `_drop_disagreeing_table_names` (this act: nulls them for a
  disagreeing row); `sector_reason` is also set by `_join_classification` (no classification) and by this rule. **N = 2.**
- rank `series[].classification`, `name`, `name_state`, `classification_reason`: **ONE**, `_rank_series_names` (table answer, then the disagreement replacement); the series object
  copies `classification_reason` in `read_rank_series`. **N = 1.**
- collected-chatter `rows[].classification`, `classification_reason`: **TWO** in order: `_classification_fields` then the disagreement override in the row builder. **N = 2.**
- `display_name` of a subject: `_overlay_name` (overlay), `_with_subject_display_name` (peers subject), `_with_display_name` (ranked row), `monthly_chatter` (chatter row): each
  through `_clean_display_name`, whose ONE casing rule reads `DISPLAY_NAME_ACRONYMS`. **N = 1 rule**, four callers. The declared set changes only an all-caps registered name that
  carries CSL or JD: of the 68 registered names exactly 'CSL LTD' and 'JD.COM INC-ADR' (`r95_casing.py` K3); `JD_US_Equity` is served from the table's mixed-case name and does not move.
- member `identity`, `security_key`, `price_currency` of a peers set: untouched (0 of 2,230 changed above).

## EXPECTED OUTCOME -- both branches, read from the rules above

- **Branch 1 (the table's reading):** exactly the 39 paths above, each from the value shown to the value shown. Every other path of every route read byte-equal, every status the
  same, the thesis and timeline unchanged. The post-act compare re-runs `r94_name_table.py`, `r94_rankings_table.py`, `r94_other_routes_table.py` and `r95_series_by_ticker_table.py`
  with the recorded pre-apply baseline (the scripts' `--after deployed` reads the live function twice, so the compare uses the baseline), plus the census (AC1) and the NOT-moved set.
- **Branch 2 (anything else):** a path changed that is not in the table, a status other than 200, a changed member or score or rank, a changed classification of a subject whose row
  AGREES, a changed dossier field, or a content-diff member the table does not admit: **STOP** and, inside the same hour, a rollback unless the CTO names KEEP on the evidence (order bound 7).

## ROLLBACK (per key; the act writes no data object)

| what | may touch | rollback |
|---|---|---|
| `opal-amgt-scoped-api` code | the function's code package, nothing else | the KEPT live package (`VNcX9ntm..`, downloaded and hash-checked BEFORE the apply) through the module: ONE `safe-apply`, same hour |
| `lambda-source-map.json` entry | the function's one entry | the printed before value, restored in the commit that reverts |
| change-management entry | one entry, opened before and closed after | closed `ROLLED_BACK` with the reason |

Not a portal PROD push (Andrew's word 2026-10-11 ~16:2xZ: nothing promotes to PROD until he visually smokes DEV). The PROD-built page reads this API, so the two subjects' names and
list classifications change there as the API serves them (the same reading as ff-4, ruled by the CTO at msg 3948).

## SEQUENCING AND THE GO (the GO is the issuer's; RA1 does nothing before it)

1. THIS pair signed (both halves, at the table above). 2. AMGT_CORPUS: this act carries NO AMGT_CORPUS blob (the pin holds the live package's `dossier.py`, `team_sheet.py`); their
round-47 files wait for their own pair and their own redeploy, which re-measures at its GO against the function this act leaves. `2.0.0_SA_COO~C1` is told the CodeSha256 and apply
time. 3. The pin: `b3512d18fb` on `scratch/r95-aa5-pin`; the GO prints `r94_admission_table.py b3512d18fb --pin 15b7af1601` (2 members, blobs equal) in the build worktree.
4. `AMGT-ff-4` is closed; no other write to this function or the stored objects is in flight (RA1 reads the change-management ledger and the open deploys of every live worktree and
prints the denominator). 5. RA1 re-reads the baselines immediately before the apply (a Bloomberg pull between them invalidates nothing in this table: no figure is moved).

**COO HALF: SIGNED** by `2.0.0_SA_COO~R1`, for the act, branches 1 and 2, the blast radius and the rollback above. **CTO HALF:** owed by `1.0.0_SA_CTO~DELL1`.
