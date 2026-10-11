# NEVER-WIDEN CO-SIGN -- COO HALF. Round 94, `AMGT-ff-4`: the ONE redeploy of `opal-amgt-scoped-api` carrying the registered-name rule (Sanofi and CSL named as themselves)

**Signer:** `2.0.0_SA_COO~R1` (dell1), 2026-10-11 ~14:3xZ. **Counterpart owed:** `1.0.0_SA_CTO~DELL1`'s half at
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND94_NAME_REDEPLOY_CTO_HALF.md`. Model: `NEVER_WIDEN_ROUND92_REDEPLOY_COO_HALF.md`. Applier:
`0.7.0_AE_CloudOps~RA1`. Source: CTO round-93 analysis @bfa6b04c8c item 1 (row `D1-S23`, ARMED) and the issuer's rows `D1-S25`; order
`task-orders/AMGT_RESAPP.TO-AMGT-ff-4.redeploy-the-scoped-api-carrying-the-display-name-rule.md`. Sequencing: `AMGT-ff-5`'s write is CLOSED (ledger
`amgt-resapp-r94-ff5-sap-rescale-dell1`, 8 of 8, 13:24Z); this act opens its own window and re-measures at its own GO.
**This half is written from a ROUTE-BY-ROUTE MEASUREMENT of the merged tree against the live function, not from the cells' descriptions.** Instruments and evidence are
named per table below; every script is at `deliverables/2.0.0_SA_COO~R1/round94_prep/checks/`.

## THE ACT

One CODE leg on us-east-1 `opal-amgt-scoped-api`, built from a DETACHED worktree at the build pin the GO names (a box/dell1 commit carrying `AMGT-ff-1` merged @7e9d36c697 and
@7b54de1245, and AMGT_CORPUS leg p's `dossier.py` blob below). Live pre-act: `SOzAz9/gfKE++UOSB8qWSDJvhOsDQMoE+DDPzaFbeSI=` (LastModified 2026-10-11T09:26:42Z, 42,116,941
bytes, built at `6a6c5c49d0` by round 92's qq-5; read from `get-function-configuration` at 14:2xZ). The rule (`names_read.names_disagree`, `AMGT-ff-1`): when a security's
registered crosswalk name exists, is not the bare ticker, and shares no name token with the classifications table's name for the bare ticker, the REGISTERED name is served
(cleaned by the shared `_clean_display_name`), with source `crosswalk`. Cause (read): the table is keyed by the BARE Bloomberg ticker (`SAN FP` -> `SAN`, which is also Madrid's
Santander; `CSL AU` -> `CSL`, Carlisle).

## THE MEASUREMENT (the expected outcome is its reading)

Instrument: the LIVE function's response (Lambda invoke, GET) against the merged tree's own `scoped_amgt.handler` on the same live pool; every JSON path compared. Merged tree
= box/dell1 `7b54de1245` for the routes read after it, `7e9d36c697` for the 243-subject table (the later commit touches only `read_rank_series` and its new helper, which the
overlay and peers routes do not call).

| route (instrument) | reads | paths changed | where |
|---|---|---|---|
| overlay + peers, all MEASURED subjects (`r94_name_table.py`) | **243 subjects x 2 routes**, 2,230 peer members | **12** | `SAN_FP_Equity` and `CSL_AU_Equity` only; **0 members changed in any of the 243 peers sets** |
| ranked lists (`r94_rankings_table.py`) | 4 lists, 188 rows (94 + 94; the two CHATTER lists are EMPTY) | **8** | row 67 of TRENDING/PRICE and BREAKOUT/PRICE (`SAN_FP_Equity`) |
| rank timeseries of every listed ticker (`r94_rankings_table.py`) | 188 series | **4** | series 67 of both (SAN FP) |
| timeline word cloud (`r94_other_routes_table.py`) | 12 subjects | **49** | `SAN_FP_Equity` only (40 term, 9 count); 11 other subjects: 0 |
| collected chatter list (`r94_other_routes_table.py`) | days = 30, 90, 365 | **6** | row 73 (SAN FP), 2 paths x 3 windows |
| thesis (`r94_other_routes_table.py`) | 12 subjects (11 served, `NVO_US_Equity` 404 before and after) | 50 | **0 name fields**; 10 names x 5 new keys inside `model.team_sheet`: AMGT_CORPUS leg p's, not this act's |

### The changed values, whole

| subject / row | path | live serves | merged serves |
|---|---|---|---|
| `SAN_FP_Equity` | overlay `display_name` | 'Banco Santander S.A.' | 'Sanofi' |
| | overlay `name` | 'Banco Santander S.A. ADR' | 'SANOFI' |
| | overlay `display_name_source` and `name_source` | `etf-classifications` | `crosswalk` |
| | overlay `peers.subject.display_name`, peers `subject.display_name` | 'Banco Santander S.A.' | 'Sanofi' |
| `CSL_AU_Equity` | overlay `display_name`, `peers.subject.display_name`, peers `subject.display_name` | 'Carlisle Cos Inc' | 'Csl Ltd' |
| | overlay `name` | 'Carlisle Cos Inc' | 'CSL LTD' |
| | overlay `display_name_source` and `name_source` | `etf-classifications` | `crosswalk` |
| ranked row 67, both PRICE lists | `name`, `display_name` | 'Banco Santander S.A.' | 'Sanofi' |
| | `name_source` | `etf-classifications` | `crosswalk` |
| | `name_state` | `SERVED` | `ABSENT` (the table holds no agreeing name: a crosswalk-filled row's existing reading) |
| rank series 67, both PRICE lists | `name` | 'Banco Santander S.A. ADR' | 'Sanofi' |
| | `name_state` | `SERVED` | `ABSENT` (same reading) |
| collected chatter row 73, all 3 windows | `display_name` | 'Banco Santander S.A.' | 'Sanofi' |
| | `name_source` | `classification` | `crosswalk` |
| `SAN_FP_Equity` timeline `word_cloud.terms` | 40 `term`, 9 `count` | first term 'sanofi' (57 headlines), then 'drug' 25, 'ceo' 12 ... | 'sanofi' DROPPED as the security's own word (the cloud already drops a security's own name words); the list moves up one place: 'drug' 25, 'ceo' 12, 'vaccine' 10 ... |

Read as: every name of the two securities is now its own company's, on every route that serves one. NOT moved, and the compare must show it:
**the classification table's OTHER fields for these two tickers** (read live 14:2xZ: `SAN FP` serves asset class equity, sub-asset class and sector 'Health Care'; `CSL AU`
serves sub-asset class 'US Large Cap' with a null sector and its reason, which is Carlisle's classification, the same bare-ticker collision; this cell moves NO
`classification` object, and the table above shows none moves), the score and rank of every row, every member of every peers set, every figure and every date. `display_name` for CSL reads 'Csl Ltd': that is the shared casing rule `_clean_display_name`
applied to the registered 'CSL LTD' (a known cosmetic limit of the rule for a short all-capitals name, unchanged by this act; carried to the round-94 packet).

## BLAST RADIUS -- the CONTENT-DIFF the build may print against the live package, each member admitted by BLOB at the GO

Measured by `r94_admission_table.py` (`git diff` of every non-test `lib/` file and the two registry files, live pin `6a6c5c49d0` against the cut). Nine members differ at the
cut (box/dell1 `a9285f4a9d`); the GO re-runs it at its pin and every blob below must match its column, except where the row says otherwise.

| member | blob at the live pin | blob at the cut | admitted for | the only change admitted |
|---|---|---|---|---|
| `lib/research/api/scoped_amgt.py` | `0662ef5b08de` | `9d7de3ba726f` (+49 -4) | `AMGT-ff-1` | `_overlay_name` skips a disagreeing table name; `_drop_disagreeing_table_names` and its one call in `_join_ranked_rows`; `_rank_series_names` and its one call in `read_rank_series`; one import of `names_read` |
| `lib/research/api/names_read.py` | `7d8ee1be80bd` | `4dd1e67eca37` (+39 -4) | `AMGT-ff-1` | `names_agree`, `names_disagree`, and the rule inside `display_names` |
| `lib/research/corpus/dossier.py` | `1ad2fc824173` | `dc2ce428d015` (+2 -1) | AMGT_CORPUS leg p (`CRPS-av-4`) | `METHOD_VERSION` `amgt-corpus-dossier/11` -> `/12` (:149): the pick rule serves the /12 objects the leg-v read found for 95 of 95 names; its own pair governs the served effect |
| `lib/research/corpus/team_sheet.py` | `9a6bf6a19381` | `6761f09d15f0` (+146 -17) | AMGT_CORPUS leg p | packaged, NOT imported by the API (leg p's AC3 of av-1: 0 imports) |
| `lib/research/peers/engine.py` | `f8666b5a552a` | `15a70af793ec` (+44 -2) | round 93 `AMGT-ss-3` | producer side: `peers`, `batch_artifact_paths`, `run_batch`, `main`, one import. The one request-time use (`scoped_amgt._with_subject_cap` -> `engine._subject_from_model_block`) has NO hunk |
| `lib/research/api/peers_rebuild.py` | ABSENT | `4af49bd385f8` (+32) | `AMGT-ss-3` | the sanctioned peers-rebuild caller; not imported by the handler |
| `lib/research/filings/analyze.py` | `8620043fca4c` | `4d1f93c978f0` (+74 -6) | rounds 92-94 `AMGT-qq-3`, `AMGT-ff-3` | producer side (the thesis driver verifier and the scale rule); the API never imports `filings.analyze` |
| `lib/opal_naming.py` | `3fc88f348059` | `5748320303cb` (+230 -13; **moves with other projects' commits**) | ANOTHER project's (LGIC, ADVI_FIRMBKTS, IRPT) | admitted by the REPLAY, not by blob alone: see below |
| `infra/logic/registry/scopes.json` | `49208211301b` | `cb297c4faed9` | ANOTHER project's (ADVI_FIRMBKTS) | two rows added under the `49financial` scope (`tier_live`, `product_live`); no research scope row moves |

**The `opal_naming.py` replay (`r94_naming_replay.py`, run 14:1xZ):** the function reaches the builder at request time (`corpus.dossier` -> `harvest.store` ->
`naming.address` / `naming.key`). The handler served overlay, thesis and peers for ten subjects, the four ranked lists and a timeseries (35 requests, all 200); **87 builder
calls, 18 distinct**, each replayed against the PIN's own `lib/opal_naming.py` and `infra/logic/registry` (extracted by `git show` into a temp root): **0 differ**
(`PASS P2`). The store is also self-guarding (`address_of` refuses unless the builder prints `opal-data-harvest`). The member is admitted at ANY blob provided the GO's pin
re-runs `r94_naming_replay.py` to `R94 NAMING REPLAY: YES`; a `NO` is a STOP.

NOT admitted (if the content-diff names one, STOP): any other file under `lib/` or `infra/logic/registry/`; a change to `scoped_amgt.py` beyond the table's 49-4 (a different
blob is a STOP unless a committed pair names it); a second AMGT_CORPUS blob. NO IAM, route, memory, schedule, store write or S3 delete. The act writes NO data object.

## WRITER CENSUS of the moved served properties (N printed, each rule read)

- `overlay.name`, `name_source`, `display_name`, `display_name_source`: **ONE** writer, `_overlay_name` (the `**` spread at `scoped_amgt.py` :3611). **N = 1.**
- peers `subject.display_name` and the overlay's `peers.subject.display_name`: **ONE** writer, `_with_subject_display_name` -> `_display_name_for` -> `names_read.display_names`.
  **N = 1.**
- ranked `rows[].name`: FIVE rules in order, read: `_join_classification` (the table), `_drop_disagreeing_table_names` (this act), `_fill_names_from_crosswalk`,
  `_fill_names_from_model_block`, `_with_display_name` (casing). `rows[].display_name`: ONE (`_with_display_name`). **N = 5 and 1.**
- rank `series[].name`, `name_state`: **ONE**, `_rank_series_names` (this act). **N = 1.**
- collected-chatter `rows[].display_name`, `name_source`: **ONE**, `monthly_chatter._display_names` -> `names_read.display_names` (the shared chain). **N = 1.**
- timeline `word_cloud.terms`: **ONE** builder, `_word_cloud_block`, whose own-words set reads `_display_name_for` and `_overlay_name` (the two rules above). **N = 1.**
- member `identity` / `security_key` of a peers set (not moved, and the table shows it): THREE writers (round 92: `_with_listed_identity`, `_with_numeric_tickers` numeric
  arm and exact-name arm); the held-name index they read follows the chain, so the measurement above is the evidence that **0 of 2,230 members** changed.
- NOT moved: every `classification` object and `sector` (`CSL AU` still serves Carlisle's classification: carried to the round-94 packet), every score, rank, figure and date.

## EXPECTED OUTCOME -- both branches, read from the rules above

- **Branch 1 (the table's reading):** exactly the changed paths of the table, each from the value shown to the value shown: **12 + 8 + 4 + 49 + 6 = 79 name-related paths**
  and AMGT_CORPUS leg p's 50 `team_sheet` paths on the thesis route (their half's Branch A). Every other path of every route read (and every member, every row) byte-equal.
  The post-act compare re-runs the three table scripts with `--after deployed` and the census (AC1 C1, C3, C4).
- **Branch 2 (anything else):** a path changed that is not in the table, a changed member count or order, a changed `classification`, a status other than 200, a dossier field
  other than `model.team_sheet` changed (AMGT_CORPUS's Branch C), or a content-diff member the table does not admit: **STOP** and, inside the same hour, a rollback unless the
  CTO names KEEP on the evidence (order bound 7).

## ROLLBACK (per key; the act writes no data object)

| what | may touch | rollback |
|---|---|---|
| `opal-amgt-scoped-api` code | the function's code package, nothing else (no IAM, env, memory, route or schedule) | the KEPT live package (`SOzAz9/gfKE..`, downloaded and hash-checked BEFORE the apply) through the module: ONE `safe-apply`, same hour |
| `lambda-source-map.json` entry | the function's one entry | the printed before value, restored in the same commit that reverts |
| change-management entry | one entry, opened before and closed after | closed `ROLLED_BACK` with the reason |

Not a portal PROD push: the portal change (`AMGT-ff-2`, DEV @582ffe6eb8) is a separate act and PROD stays at 37aa1247 until `/prod-deploy`.

## SEQUENCING AND THE GO (the GO is the issuer's; RA1 does nothing before it)

1. THIS pair signed (both halves, at the table above). 2. AMGT_CORPUS's served-effect pair signed (their COO half `deliverables/2.0.0_SA_COO~C1/NEVER_WIDEN_ROUND46_AV4_LEGP_SERVED_EFFECT.md`,
CTO half `AMGT_CORPUS/ledger/NEVER_WIDEN_ROUND46_AV4_CTO_HALF.md`; where the two disagree THIS table governs the redeploy and theirs governs the served effect of the three modules).
3. The CTO half's two conditions on leg p: (a) leg v read Branch A on the written /12 objects (MET: msg 3908, 95 of 95, 0 failed, ledger `amgt-corpus-r46-av3` CLOSED); (b) the
post-act read covers one name per class (own_new, own_model, master_absent) on portal PROD's built page as well as DEV's, PROD unchanged in pixels; a PROD change is a STOP
with this pair's rollback. `2.0.0_SA_COO~C1` holds the pre-act snapshots (PROD-built 13:26Z, DEV-built 13:59Z) and reads after RA1's legs close. 4. The pin: a box/dell1
commit; the GO prints `r94_admission_table.py <pin>` and `r94_naming_replay.py` at it. 5. `AMGT-ff-5` is closed; no other write to this function or the stored objects is
in flight at the apply (RA1 reads the change-management ledger and the open deploys of every live worktree and prints the denominator). 6. A data refresh of the served blocks
before the apply invalidates `2.0.0_SA_COO~C1`'s baseline, not this table: RA1 re-reads the baseline immediately before the apply.

**COO HALF: SIGNED** by `2.0.0_SA_COO~R1`, for the act, branches 1 and 2, the blast radius and the rollback above. **CTO HALF:** owed by `1.0.0_SA_CTO~DELL1`.
