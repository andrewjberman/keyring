# NEVER-WIDEN CO-SIGN -- COO HALF. Round 100, `AMGT-bg-1`: the THIRD redeploy of `opal-amgt-scoped-api` from a MERGED pin carrying AMGT_CORPUS's /15 corpus files, bd-1's serve KEPT

**Signer:** `2.0.0_SA_COO~R1` (dell1), 2026-10-12 ~02:4xZ. **Counterpart owed:** `1.0.0_SA_CTO~DELL1`'s half at
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND100_CORPUS15_REDEPLOY_CTO_HALF.md`. Model: `NEVER_WIDEN_ROUND99_CORPUS14_REDEPLOY_COO_HALF.md` (+ its CTO half, msg 4184).
Applier: `0.7.0_AE_CloudOps~RA1`. Source: CTO round-99 analysis `ledger/ROUND_ANALYSIS.round99.md` section 2 item 1 (msg 4198); order
`task-orders/AMGT_RESAPP.TO-AMGT-bg-1.redeploy-the-scoped-api-carrying-the-15-corpus-files-from-a-merged-pin.md` (STAGED @aa58e5e113). The served effect of the corpus modules is AMGT_CORPUS's
`NEVER_WIDEN_ROUND49_AY4_CTO_HALF.md` (signed, msg 4191) and C1's `NEVER_WIDEN_ROUND49_AY4_LEGP_15_SERVED_EFFECT.md`; this half governs the redeploy, those govern the effect of the modules.
**Written from a ROUTE-BY-ROUTE MEASUREMENT taken from the pin's OWN worktree** (a detached checkout of `6e8dcaf414`, the measuring tree IS the built tree) against the live /14 function;
instruments `deliverables/2.0.0_SA_COO~R1/round94_prep/checks/`, `round95_prep/checks/`, `round98_prep/checks/` and AMGT_CORPUS's `checks/round49/ay4_compare.py`.
**This is FIRST of two applies.** `AMGT-bg-2`'s `scoped_amgt.py` (one S3 client per container; merged @703845dc6e) is NOT in this build: the pin carries bd-1's `scoped_amgt.py`, and the
S3-client change is `AMGT-bg-3`'s own pair and apply, never folded with this one (CTO, msg 4198).

## THE ACT

One CODE leg on us-east-1 `opal-amgt-scoped-api`, built from a DETACHED worktree at **`6e8dcaf414`** (a `box/dell1` first-parent commit, MERGED: `close(AMGT_RESAPP round 99)`; the GO names the
final pin). Live pre-act: `oEDHTRPqvrjYubJNqogLVKubI2UyQ8wZco0oa2Z6GVc=` (apply 2026-10-12T00:23:02Z, built at `b3d4856531`). The pin carries, read by blob at the worktree: `scoped_amgt.py`
**`9b13bf0371d4`** and `monthly_chatter.py` **`38e9511ccc9c`** (bd-1's two blobs, byte-equal to the live package's), `dossier.py` **`7b67bf62afdd`** (METHOD `amgt-corpus-dossier/15`),
`team_sheet.py` `ef4da7cdc85a`, `opal_naming.py` `3902e0e93ee4`, `analyze.py` `bf1d15b14ba1`.

What changes at request time (read in the pin's code): `dossier.read_dossier` picks, among a name's stored objects, those whose `method_version` equals the reader's `METHOD_VERSION` when any
exist (newest `as_of`, then `LastModified`); the reader's literal moves /14 -> /15; all 95 names hold a /15 object (AMGT_CORPUS ay-3 closed: 95 written, leg v Branch A; master names carry no value
in any block, 63 of 63; unread blocks no value, 12 of 12), so the Thesis payload's `model.team_sheet` becomes the stored /15 field: **its BLOCK rows (3,103 = period 401 + case 2,690 + unread
12)** and the `blocks` key.

## THE MEASUREMENT (the expected outcome is its reading)

Instrument: the LIVE /14 function's response (Lambda invoke, GET) against the pin's OWN `scoped_amgt.handler` on the same live pool, every JSON path compared. Run 02:11Z-02:34Z, sequential, no
other reader of mine on the function.

| route (instrument) | reads | paths changed | where |
|---|---|---|---|
| overlay + peers, all MEASURED subjects (`r94_name_table.py`) | **243 subjects x 2 routes** | **0** | none |
| ranked lists and their timeseries (`r94_rankings_table.py`) | 7 reads | **0** | none |
| rank timeseries asked for EVERY measured subject's ticker x 4 combinations (`r95_series_by_ticker_table.py`) | 4 x 243 series | **0** | one generation clock (noise) |
| timeline of 12 subjects, collected chatter x 3 windows (`r94_other_routes_table.py`) | 27 reads (`NVO_US_Equity` thesis 404 before and after) | **0** on timeline and chatter | none |
| thesis of 12 subjects (`r94_other_routes_table.py`) | 12 reads: 11 status 200 | **663** | on 10 subjects, every one under `.model.team_sheet` (0 elsewhere) |
| **thesis, WHOLE BODY, all 95 resolved names** (`r98_thesis_fullbody_compare.py`) | 95 names, status 200 and 200 on every one | **4,831** | **4,806 under `.model.team_sheet` (all 95 names); 7 generation clocks; 18 `float_repr`; 0 other** |
| AMGT_CORPUS's prediction (`r98_thesis_local_capture.py` the pin, `ay4_compare.py <live pre> <pin>`) | 95 names | -- | `team_sheet_equals_stored15` **95/95**, `others_equal` **95/95**, max response **1,303,205** bytes (`AZN_LN_Equity`), margin to 6 MiB **4,988,251**, 47 of 95 above 1 MiB (44 now), largest growth 13,247 bytes |

The 4,806 `team_sheet` paths by pattern: `.row_classes[]` **3,103** (the BLOCK rows: equals the ay-4 half's 3,103), `.row_formats[]` 709, `.row_values[]` 709, `.blocks` 95,
`.row_counts.BLOCK` 95, `.row_counts.FIGURE` 95. Nothing outside `model.team_sheet`.

**The readings that are not `team_sheet`, whole:**

- **`float_repr` (18 paths, 10 names, the SAME 18 paths as rounds 98 and 99):** `.segment_table.periods[].top_level_sum`, printed differently by the live runtime (python3.11, uncompensated
  `sum`) and the measuring checkout (python 3.14, compensated); the computing code is byte-equal. **Expected live: ZERO**; any one is Branch 2.
- **growth against the name's own delta, ONE name over by 11 bytes in `ay4_compare.py`: `SNPS_US_Equity`** (growth 10,170 against a `team_sheet` delta of 10,159): its `float_repr` (+11), the same
  11 bytes as in round 99. Every other name's growth is within its own delta (the largest 13,247 bytes). The compare's "pre" here is a capture taken at the start of this measurement window,
  not an older one.
- **`clock` (7 paths):** `.generated_at`, `.model.generated_at`.

NOT moved, and the post-act compare must show it: every `fiscal_year_figures`, `fiscal_years`, `header_figures`, `check_face`, `model_status`, `posture`, `dossier_fields` and every `model` key but
`team_sheet` (95 of 95), every classification, name, sector and its source and date (bd-1's serve), every score, rank and peer member (243 x 2 reads), the timeline, the ranked lists, the collected
chatter, the PROD page's rendering (it reads `team_sheet` in 0 files of `src/pages/SecurityAnalysis`; the PROD-built page is `origin/PROD` `37aa1247ee`). **DEV renders blocks** (the ay-4 half read it at `46926677c1`; DEV is now `0a06280a40`, its fast-forward
descendant), so the post-act DEV census (FWD-20's last read, C1's) is the rendered close.

## BLAST RADIUS -- the CONTENT-DIFF the build may print against the live package, each member admitted by BLOB at the GO

Measured by `r94_admission_table.py 6e8dcaf414 --pin b3d4856531`: **two lib members differ at the pin**, no registry file.

| member | blob at the live build input `b3d4856531` | blob at the pin `6e8dcaf414` | reaches the function's request path? | admitted for / by |
|---|---|---|---|---|
| `lib/research/corpus/dossier.py` | `6c4529c51a13` | `7b67bf62afdd` (+1 -1) | **YES** (imported at request time: round 98 `sys.modules`) | AMGT_CORPUS `ay-4` half; the `METHOD_VERSION` literal |
| `lib/research/corpus/team_sheet.py` | `3ba68a99a22f` | `ef4da7cdc85a` (+253 -13) | NO (producer-side) | AMGT_CORPUS; packaged, inert |

Every other member is BYTE-EQUAL to the live package, **including `scoped_amgt.py` (`9b13bf0371d4`), `monthly_chatter.py` (`38e9511ccc9c`), `lib/opal_naming.py` (`3902e0e93ee4`) and `analyze.py`
(`bf1d15b14ba1`)**. **Any other member is a STOP**, including `scoped_amgt.py` at ANY other blob: a pin that carries `AMGT-bg-2`'s `scoped_amgt.py` (`9f72b58aa87e` at `703845dc6e`) is a STOP for
THIS act. The builder replay (`r94_naming_replay.py --pin b3d4856531`, from the pin's worktree): **35 requests all 200, 88 builder calls, 18 distinct (`address` 7, `key` 11), 0 differ:
`R94 NAMING REPLAY: YES`.** NO IAM, route, memory, schedule, store write or S3 delete. The act writes NO data object.

## WRITER CENSUS of the moved served property (N printed, each rule read in the pin)

- `/thesis` `model.team_sheet`: **ONE** assignment, `scoped_amgt.py:3871` `model["team_sheet"] = _team_sheet_from_dossier(dossier_read)` (the stored field AS STORED). **N = 1.**
- the dossier read behind it: **ONE** call per request, `_read_dossier_document` (`scoped_amgt.py:5208`), whose pick rule is `dossier.read_dossier` (`dossier.py:1589-1625`): objects at the
  reader's `METHOD_VERSION` are picked among when any exist, else all. **Pick rules N = 1.**
- NOT moved: the classification, name and sector writers (`scoped_amgt.py` is byte-equal).

## EXPECTED OUTCOME -- both branches, read from the rules above

- **Branch 1 (the table's reading):** for every one of the 95 names the live `/thesis` `model.team_sheet` equals the stored /15 field (every key): BLOCK rows present, `blocks` key present; every
  other path of every route reads byte-equal to its pre-act read except the generation clocks; `segment_table` sums print as they do now (0 `float_repr`); `ay4_compare.py <live pre> <live post>`
  prints `ay4 compare build 1/1` with `team_sheet_equals_stored15` 95/95, `others_equal` 95/95, growth within each name's own delta (live vs live, both python3.11; largest predicted 13 KB), the maximum
  under 6,291,456 bytes (predicted 1,303,205). `r97_sector_serve_census.py`, `r95_classification_census.py` and `r94_name_census.py --where deployed` keep reading YES (bd-1's serve KEPT);
  `r89_deployed_close.sh --want amgt-corpus-dossier/15` reads YES.
- **Branch 2 (anything else):** a path changed that is not in the table, a status other than 200 for a name that read 200 before, a changed classification, name, sector, score, rank or member, a
  served field other than `model.team_sheet` unequal to its pre-act read, a name whose `team_sheet` is unequal to its stored /15 field, a master name or an unread block carrying a value, a
  response above 6 MiB, a growth above a name's own `team_sheet` delta (live vs live) that no moved input accounts for, a content-diff member the table does not admit, or `scoped_amgt.py` /
  `monthly_chatter.py` at any other blob: **STOP** and, inside the same hour, a rollback unless the CTO names KEEP on the evidence. A newer stored object or a Bloomberg pull between the pre-act
  capture and the apply moves a vintage stamp or a few bytes of a name's non-team_sheet content: it is a read, never a STOP, provided the key set and every value but that stamp equal and the
  growth over the name's `team_sheet` delta is accounted for by that moved input (printed).
- **Slow-request clause (CTO msg 4184, carried):** one replay request over 20 s is read against the day's baseline (53 of 32,528 invocations, 47 before round 98's apply; round 99's replay met one,
  24.87 s, 200, three identical re-invokes). RA1 re-invokes it three times; 200 with identical bytes is recorded with its request id and duration; a non-200 or differing bytes is Branch 2. A
  rise of the over-20 s RATE above the baseline over the following day is Branch 2. No other seat's reader runs on the function during the replay.

## ROLLBACK (per key; the act writes no data object)

| what | may touch | rollback |
|---|---|---|
| `opal-amgt-scoped-api` code | the function's code package, nothing else | the KEPT live package (`oEDHTRPq..`, downloaded and hash-checked BEFORE the apply) through the module: ONE `safe-apply`, same hour |
| `lambda-source-map.json` entry | the function's one entry | the printed before value, restored in the commit that reverts |
| change-management entry | one entry, opened before and closed after | closed `ROLLED_BACK` with the reason |

Not a portal PROD push. The PROD-built page reads this API; it does not read `team_sheet`.

## SEQUENCING AND THE GO (the GO is the issuer's; RA1 does nothing before it)

1. THIS pair signed (both halves, at the table above) and AMGT_CORPUS's served-effect half in force (the `ay-4` CTO half, msg 4191). 2. RA1 captures the 95 thesis payloads (`aw4_capture.py`)
IMMEDIATELY before the apply and tells the issuer; `2.0.0_SA_COO~C1` runs its post-act read when the issuer relays the new CodeSha256. 3. The pin: the GO prints
`r94_admission_table.py <pin> --pin b3d4856531` in the build worktree (two lib members, blobs as above, the two api blobs equal) and `r94_naming_replay.py --pin b3d4856531` (YES). 4. No
other write to this function and no reader of any seat on it during RA1's capture and replay: the issuer and `2.0.0_SA_COO~C1` hold theirs until RA1 reports. 5. After the apply and its read:
`AMGT-bg-3` (the S3 client) is a SECOND apply under its own pair, never folded with this one.

**COO HALF: SIGNED** by `2.0.0_SA_COO~R1`, for the act, branches 1 and 2 (with the slow-request clause), the blast radius and the rollback above. **CTO HALF:** owed by `1.0.0_SA_CTO~DELL1`.
