# NEVER-WIDEN CO-SIGN -- COO HALF. Round 98, `AMGT-be-1`: the ONE redeploy of `opal-amgt-scoped-api` from a MERGED pin carrying AMGT_CORPUS's /13 corpus files, bd-1's serve KEPT

**Signer:** `2.0.0_SA_COO~R1` (dell1), 2026-10-11 ~22:0xZ. **Counterpart owed:** `1.0.0_SA_CTO~DELL1`'s half at
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND98_CORPUS13_REDEPLOY_CTO_HALF.md`. Model: `NEVER_WIDEN_ROUND97_LISTING_SECTOR_REDEPLOY_COO_HALF.md` (+ its CTO half, msg 4094).
Applier: `0.7.0_AE_CloudOps~RA1`. Source: CTO round-97 analysis `ledger/ROUND_ANALYSIS.round97.md` section 2 item 1 (msg 4123); order
`task-orders/AMGT_RESAPP.TO-AMGT-be-1.redeploy-the-scoped-api-carrying-the-13-corpus-files-from-a-merged-pin.md` (STAGED @23479c4c14). The served effect of the corpus modules is
AMGT_CORPUS's half `org/missions/D5/AMGT/AMGT_CORPUS/ledger/NEVER_WIDEN_ROUND47_AW4_CTO_HALF.md` (ADDENDA 1-2) and C1's COO half `NEVER_WIDEN_ROUND47_AW4_LEGP_SERVED_EFFECT.md`; this half
governs the redeploy, those govern the effect of the modules.
**Written from a ROUTE-BY-ROUTE MEASUREMENT taken from the pin's OWN worktree** (a detached checkout of `a03d92221a`, so the measuring tree IS the built tree) against the live function;
instruments `deliverables/2.0.0_SA_COO~R1/round94_prep/checks/`, `round95_prep/checks/`, `round98_prep/checks/` and AMGT_CORPUS's `checks/round47/aw4_capture.py`, `aw4_compare.py`.

## THE ACT

One CODE leg on us-east-1 `opal-amgt-scoped-api`, built from a DETACHED worktree at **`a03d92221a`** (a `box/dell1` first-parent commit, MERGED, not a scratch pin: `close(AMGT_RESAPP round 97)`).
Live pre-act: `IpaCHo5hokQzWcEmw500HI6ax1otqL23vQZaogRWOh4=` (apply 2026-10-11T20:47Z, built at `08d5ea2920` on `scratch/r97-bd2-pin`). **`box/dell1` HEAD is NOT the pin** (it carries the
/14 files, `dossier.py` `6c4529c51a13`, whose write `ax-6` is running and whose `aw-4` restatement is not re-signed: CTO ADDENDUM 2, it never holds round 98). The pin carries, read by blob
at the worktree (`git rev-parse HEAD:<path>`): `scoped_amgt.py` **`9b13bf0371d4`**, `monthly_chatter.py` **`38e9511ccc9c`** (bd-1's two blobs, UNCHANGED), `dossier.py` **`13463426d0da`**
(METHOD `amgt-corpus-dossier/13`), `team_sheet.py` `956e69d7be7e`, `template.py` `e03d6a8acf65`, `factset_descriptions.json` `76faa8d6a708` (C1's msg 4098 set).

What changes at request time (read in the pin's code): `dossier.read_dossier` picks, among a name's stored objects, those whose `method_version` equals the reader's `METHOD_VERSION` when any
exist (newest `as_of`, then `LastModified`); the reader's literal moves /12 -> /13; all 95 names hold a /13 object (AMGT_CORPUS aw-3 closed, leg v Branch A), so the Thesis payload's
`model.team_sheet` becomes the stored /13 field. Nothing else in the payload is a function of that literal (measured below).

## THE MEASUREMENT (the expected outcome is its reading)

Instrument: the LIVE function's response (Lambda invoke, GET) against the pin's OWN `scoped_amgt.handler` on the same live pool, every JSON path compared. Run 21:31Z-22:0xZ.

| route (instrument) | reads | paths changed | where |
|---|---|---|---|
| overlay + peers, all MEASURED subjects (`r94_name_table.py`) | **243 subjects x 2 routes** | **0** | none |
| ranked lists, 4 movement x subject combinations and their timeseries (`r94_rankings_table.py`) | 6 reads, 94 rows each PRICE list | **0** | none |
| rank timeseries asked for EVERY measured subject's ticker x 4 combinations (`r95_series_by_ticker_table.py`) | 4 x 243 series | **0** | none |
| timeline of 12 subjects, collected chatter x 3 windows (`r94_other_routes_table.py`) | 27 reads (`NVO_US_Equity` thesis 404 before and after) | **0** | none |
| thesis of 12 subjects (`r94_other_routes_table.py`) | 12 reads: 11 status 200, `NVO_US_Equity` 404 before and after | **981** | on 10 subjects, every one under `.model.team_sheet` (0 elsewhere); `CSL_AU_Equity` 200, 0 paths |
| **thesis, WHOLE BODY, all 95 resolved names** (`r98_thesis_fullbody_compare.py`) | 95 names, status 200 and 200 on every one | **3,892** | **3,864 under `.model.team_sheet`; 10 clock stamps (`generated_at`); 18 `float_repr`; 0 other** |
| control arm: the same instrument, live against live (`--after deployed`) | 95 names | 4 | clock stamps only (`generated_at` x 3, `model.generated_at` x 1); 0 else |
| AMGT_CORPUS's prediction (`aw4_capture.py` live base, `r98_thesis_local_capture.py` the pin, `aw4_compare.py`) | 95 names | -- | `team_sheet_equals_stored13` **95/95**, `others_equal` **95/95**, max response **1,289,805** bytes (`AZN_LN_Equity`), margin to 6 MiB **5,001,651**, 44 of 95 above 1 MiB (31 now), growth within the name's own `team_sheet` delta on 94 of 95 |

**The two readings that are not `team_sheet`, whole:**

- **`float_repr` (18 paths, 10 names: `992_HK`, `BBSE3_BZ`, `HEI_US`, `IBE_SM`, `ICICIBC_IN`, `LLY_US`, `MNST_US`, `SNPS_US`, `SSE_LN`, `ST_SP`):** `.segment_table.periods[].top_level_sum`, a SUM computed at request
  time by `segment_served._column_sums`, printed differently by the live runtime (python3.11, uncompensated `sum`) and by the measuring checkout (python 3.14, compensated), for example
  `SNPS_US_Equity` period 1 `6127.4` live vs `6127.400000000001` local (**+11 bytes**: this is the one name whose growth reads 14,795 against a `team_sheet` delta of 14,784). The code that computes
  it is BYTE-EQUAL between the live build input and the pin (`segment_served.py` and `segment_table.py` are not among the changed members), the stored rows are the same, and the live
  runtime does not change: **after the apply the live function prints the same bytes it prints now.** Measured, not assumed: the same name served by the live function at the same moment
  reads `6127.4`; the local handler reads `6127.400000000001` under four different hash seeds. The post-act compare therefore expects ZERO such paths, and any one is Branch 2.
- **`clock` (10 paths, 6 names):** `.generated_at` and `.model.generated_at`; generation clocks, counted apart.

NOT moved, and the post-act compare must show it: every `fiscal_year_figures`, `fiscal_years`, `header_figures`, `check_face`, `model_status`, `posture`, `dossier_fields` and every `model` key but
`team_sheet` (95 of 95), every classification, name, sector and its source and date (bd-1's serve), every score, rank and peer member (243 x 2 reads), the timeline, the ranked lists, the
collected chatter, the PROD page's rendering (it reads `team_sheet` in 0 files of `src/pages/SecurityAnalysis`; the PROD-built page is `origin/PROD` `37aa1247ee`, the portal reaches PROD only by `/prod-deploy`).

## BLAST RADIUS -- the CONTENT-DIFF the build may print against the live package, each member admitted by BLOB at the GO

Measured by `r94_admission_table.py a03d92221a --pin 08d5ea2920`: **six lib members differ at the pin** (plus two registry files).

| member | blob at the live build input `08d5ea2920` | blob at the pin `a03d92221a` | reaches the function's request path? | admitted for / by |
|---|---|---|---|---|
| `lib/research/corpus/dossier.py` | `dc2ce428d015` | `13463426d0da` (+2 -1) | **YES** (imported at request time, measured: `sys.modules` after six routes) | AMGT_CORPUS `aw-4` half; the `METHOD_VERSION` literal |
| `lib/opal_naming.py` | `5748320303cb` | `3902e0e93ee4` (+73 -8) | **YES** (`dossier` -> `harvest.store` -> `address`, `key`) | another project's change (LGIC / FIRMBKTS); admitted by the BUILDER REPLAY below |
| `lib/research/corpus/team_sheet.py` | `6761f09d15f0` | `956e69d7be7e` (+262 -38) | NO (not in `sys.modules`; producer-side) | AMGT_CORPUS; packaged, inert |
| `lib/research/corpus/template.py` | ABSENT | `e03d6a8acf65` (+127) | NO (not in `sys.modules`) | AMGT_CORPUS; packaged, inert |
| `lib/research/corpus/factset_descriptions.json` | ABSENT | `76faa8d6a708` (+1) | NO (build-time data) | AMGT_CORPUS; packaged, inert |
| `lib/research/filings/analyze.py` | `4d1f93c978f0` | `bf1d15b14ba1` (+4 -2) | NO (not in `sys.modules`; the verifier's `stated_value` read is producer-side) | AMGT_RESAPP `aa-1` (round 95) |
| `infra/logic/registry/exemptions.json`, `name_rulings.json` | | +102, +7 | read by `opal_naming` at import | other projects' rows; admitted by the replay |

`scoped_amgt.py` `9b13bf0371d4` and `monthly_chatter.py` `38e9511ccc9c` are **byte-equal to the live package's** (bd-1 is already served). **Any other member is a STOP**, including a pin whose
`scoped_amgt.py` or `monthly_chatter.py` differs from those blobs. The builder replay (`r94_naming_replay.py --pin 08d5ea2920`, run from the pin's worktree): **35 requests all 200, 81 builder
calls, 18 distinct (`address` 7, `key` 11), 0 differ: `R94 NAMING REPLAY: YES`.** NO IAM, route, memory, schedule, store write or S3 delete. The act writes NO data object.

## WRITER CENSUS of the moved served property (N printed, each rule read in the pin)

- `/thesis` `model.team_sheet`: **ONE** assignment, `scoped_amgt.py:3871` `model["team_sheet"] = _team_sheet_from_dossier(dossier_read)` (the stored field AS STORED; no re-derivation). **N = 1.**
- the dossier read behind it: **ONE** call per request, `_read_dossier_document` (`scoped_amgt.py:5208`, "the ONE `read_dossier` call of a /thesis request"), whose pick rule is `dossier.read_dossier`
  (`dossier.py:1589-1625`): objects at the reader's `METHOD_VERSION` are picked among when any exist, else all. **Pick rules N = 1.**
- NOT moved: the classification, name and sector writers (round 95/97 N = 2, 1, 2 and 2, 1, 1, 1 unchanged: `scoped_amgt.py` is byte-equal).

## EXPECTED OUTCOME -- both branches, read from the rules above

- **Branch 1 (the table's reading):** for every one of the 95 names the live `/thesis` `model.team_sheet` equals the stored /13 field (every key); every other path of every route reads byte-equal
  to its pre-act read except the generation clocks; `segment_table` sums print as they do now (0 `float_repr`); `aw4_compare.py <pre> <post>` prints `aw4 compare build 1/1` with growth within each name's
  own delta (no name over by 11 bytes: the runtime prints the same sum), the maximum under 6,291,456 bytes (predicted 1,289,805). `r97_sector_serve_census.py --where deployed`,
  `r95_classification_census.py --where deployed` and `r94_name_census.py --where deployed` keep reading YES (bd-1's serve KEPT); `r89_deployed_close.sh --want amgt-corpus-dossier/13` reads YES.
- **Branch 2 (anything else):** a path changed that is not in the table, a status other than 200, a changed classification, name, sector, score, rank or member, a served field other than
  `model.team_sheet` unequal to its pre-act read, a name whose `team_sheet` is unequal to its stored /13 field, a response above 6 MiB, a growth above a name's own `team_sheet` delta, a
  content-diff member the table does not admit, or `scoped_amgt.py` / `monthly_chatter.py` at any other blob: **STOP** and, inside the same hour, a rollback unless the CTO names KEEP on the
  evidence (order bound 7). A newer stored /13 object or a Bloomberg pull between the pre-act capture and the apply moves a vintage stamp only: it is a read, never a STOP, provided the key
  set and every value but that stamp equal.

## ROLLBACK (per key; the act writes no data object)

| what | may touch | rollback |
|---|---|---|
| `opal-amgt-scoped-api` code | the function's code package, nothing else | the KEPT live package (`IpaCHo5h..`, downloaded and hash-checked BEFORE the apply) through the module: ONE `safe-apply`, same hour |
| `lambda-source-map.json` entry | the function's one entry | the printed before value, restored in the commit that reverts |
| change-management entry | one entry, opened before and closed after | closed `ROLLED_BACK` with the reason |
| scratch branches `scratch/r95-aa5-pin`, `scratch/r97-bd2-pin` | KEPT through the post-act reads | deleted by the issuer only after the compare reads Branch 1 (the CTO: "their branches may then be deleted"); a ref contained in no trunk is deleted only on the CTO's word |

Not a portal PROD push (Andrew's word 2026-10-11 ~16:2xZ: nothing promotes to PROD until he visually smokes DEV). The PROD-built page reads this API; it does not read `team_sheet`.

## SEQUENCING AND THE GO (the GO is the issuer's; RA1 does nothing before it)

1. THIS pair signed (both halves, at the table above) and AMGT_CORPUS's served-effect half in force (ADDENDA 1-2; /13, no restatement owed). 2. `2.0.0_SA_COO~C1`'s pre-act capture
(`aw4_capture.py`, 95 names) taken immediately before the GO and its path told to RA1; the post-act capture and `aw4_compare.py` follow the apply. 3. The pin `a03d92221a`: the GO prints
`r94_admission_table.py a03d92221a --pin 08d5ea2920` in the build worktree (six lib members, blobs as above, the two api blobs equal) and `r94_naming_replay.py --pin 08d5ea2920` (YES).
4. No other write to this function or to the 95 /13 objects is in flight; AMGT_CORPUS's `/14` write (`ax-6`) writes `/14` objects the /13 reader IGNORES (its pick keys on the literal), so it
need not be quiet, but RA1 re-reads the change-management ledger and the open deploys of every live worktree and prints the denominator. 5. RA1 re-reads the baselines immediately before the
apply. 6. After the apply: the issuer tells `2.0.0_SA_COO~C1` the new CodeSha256 and time, and `/14` follows as a SECOND redeploy under its own pair when its restatement is re-signed.

**COO HALF: SIGNED** by `2.0.0_SA_COO~R1`, for the act, branches 1 and 2, the blast radius and the rollback above. **CTO HALF:** owed by `1.0.0_SA_CTO~DELL1`.
