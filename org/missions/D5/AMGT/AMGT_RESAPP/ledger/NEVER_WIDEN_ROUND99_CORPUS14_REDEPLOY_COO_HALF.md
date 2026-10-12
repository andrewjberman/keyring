# NEVER-WIDEN CO-SIGN -- COO HALF. Round 99, `AMGT-bf-1`: the SECOND redeploy of `opal-amgt-scoped-api` from a MERGED pin carrying AMGT_CORPUS's /14 corpus files, bd-1's serve KEPT

**Signer:** `2.0.0_SA_COO~R1` (dell1), 2026-10-12 ~00:0xZ. **Counterpart owed:** `1.0.0_SA_CTO~DELL1`'s half at
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND99_CORPUS14_REDEPLOY_CTO_HALF.md`. Model: `NEVER_WIDEN_ROUND98_CORPUS13_REDEPLOY_COO_HALF.md` (+ its CTO half, msg 4135, ADDENDUM 1).
Applier: `0.7.0_AE_CloudOps~RA1`. Source: CTO round-98 analysis `ledger/ROUND_ANALYSIS.round98.md` section 3 item 1 (msg 4161); order
`task-orders/AMGT_RESAPP.TO-AMGT-bf-1.redeploy-the-scoped-api-carrying-the-14-corpus-files-from-a-merged-pin.md` (STAGED @a5ca1e13ff). The served effect of the corpus modules is AMGT_CORPUS's
`NEVER_WIDEN_ROUND48_AX7_CTO_HALF.md` (signed, msg 4140) and C1's `NEVER_WIDEN_ROUND48_AX7_LEGP_14_SERVED_EFFECT.md`; this half governs the redeploy, those govern the effect of the modules.
**Written from a ROUTE-BY-ROUTE MEASUREMENT taken from the pin's OWN worktree** (a detached checkout of `b3d4856531`, the measuring tree IS the built tree) against the live /13 function;
instruments `deliverables/2.0.0_SA_COO~R1/round94_prep/checks/`, `round95_prep/checks/`, `round98_prep/checks/`, `round99_prep/checks/` and AMGT_CORPUS's `checks/round48/ax7_compare.py`.
**/15 is NOT carried:** its write (AMGT_CORPUS ay-3, signed msg 4177) was not ready before round 99 was cut (a5ca1e13ff); `/14` is the signed set and `/15` would be a THIRD redeploy.

## THE ACT

One CODE leg on us-east-1 `opal-amgt-scoped-api`, built from a DETACHED worktree at **`b3d4856531`** (a `box/dell1` first-parent commit, MERGED: `packet(AMGT_RESAPP round 98 L8)`; the GO names the final pin).
Live pre-act: `mbGRmy1Hnh7M6Gtt9LchHPmt17lYS/oyCl6s10lJO+w=` (apply 2026-10-11T22:14:54Z, built at `a03d92221a`). The pin carries, read by blob at the worktree: `scoped_amgt.py` **`9b13bf0371d4`**
and `monthly_chatter.py` **`38e9511ccc9c`** (bd-1's two blobs, byte-equal to the live package's), `dossier.py` **`6c4529c51a13`** (METHOD `amgt-corpus-dossier/14`), `team_sheet.py` `3ba68a99a22f`,
`factset_descriptions.json` `690950020aa5`, `template.py` `e03d6a8acf65`, `opal_naming.py` `3902e0e93ee4`, `analyze.py` `bf1d15b14ba1`.

What changes at request time (read in the pin's code): `dossier.read_dossier` picks, among a name's stored objects, those whose `method_version` equals the reader's `METHOD_VERSION` when any exist
(newest `as_of`, then `LastModified`); the reader's literal moves /13 -> /14; all 95 names hold a /14 object (AMGT_CORPUS ax-6 closed: 95 written, 0 failed, leg v Branch A), so the Thesis payload's
`model.team_sheet` becomes the stored /14 field: **83 names change, 12 are unchanged; 252 label rows move from `absent` to `held`, with the stored text and cite.**

## THE MEASUREMENT (the expected outcome is its reading)

Instrument: the LIVE /13 function's response (Lambda invoke, GET) against the pin's OWN `scoped_amgt.handler` on the same live pool, every JSON path compared. Run 23:37Z-23:59Z, sequential, no
other reader of mine on the function.

| route (instrument) | reads | paths changed | where |
|---|---|---|---|
| overlay + peers, all MEASURED subjects (`r94_name_table.py`) | **243 subjects x 2 routes** | **0** | none |
| ranked lists, 4 movement x subject combinations and their timeseries (`r94_rankings_table.py`) | 6 reads, 94 rows each PRICE list | **0** | none |
| rank timeseries asked for EVERY measured subject's ticker x 4 combinations (`r95_series_by_ticker_table.py`) | 4 x 243 series | **0** | none |
| timeline of 12 subjects, collected chatter x 3 windows (`r94_other_routes_table.py`) | 27 reads (`NVO_US_Equity` thesis 404 before and after) | **0** on timeline and chatter | none |
| thesis of 12 subjects (`r94_other_routes_table.py`) | 12 reads: 11 status 200 | **88** | on 7 subjects, every one under `.model.team_sheet` (0 elsewhere) |
| **thesis, WHOLE BODY, all 95 resolved names** (`r98_thesis_fullbody_compare.py`) | 95 names, status 200 and 200 on every one | **1,027** | **1,008 under `.model.team_sheet`; 1 generation clock (`.generated_at`); 18 `float_repr`; 0 other** |
| the 1,008 `team_sheet` paths | 83 names | 1,008 | exactly `row_labels[].text`, `.claim`, `.cite`, `.why` for **252 rows** (2 to 8 per name), every `claim` `absent` -> `held` |
| AMGT_CORPUS's prediction (`r98_thesis_local_capture.py` the pin, `ax7_compare.py <live pre> <pin>`) | 95 names | -- | `team_sheet_equals_stored14` **95/95**, `others_equal` **95/95**, max response **1,289,958** bytes (`AZN_LN_Equity`), margin to 6 MiB **5,001,498**, 44 of 95 above 1 MiB (as now) |

**The readings that are not `team_sheet`, whole:**

- **`float_repr` (18 paths, 10 names, the SAME 18 paths as round 98):** `.segment_table.periods[].top_level_sum`, a sum computed at request time by `segment_served._column_sums`, printed differently
  by the live runtime (python3.11, uncompensated `sum`) and by the measuring checkout (python 3.14, compensated). The computing code is byte-equal between the build input and the pin; round 98's
  apply left the live runtime printing the same bytes (0 `float_repr` in RA1's second replay). **Expected live: ZERO**; any one is Branch 2.
- **growth against the name's own delta, three names over by 21, 21 and 11 bytes in `ax7_compare.py` (`AZN_LN_Equity`, `BATS_LN_Equity`, `SNPS_US_Equity`): explained, not a pin effect.** The
  `SNPS_US_Equity` 11 bytes are its `float_repr`. For AZN and BATS the compare's "pre" is a live capture taken before the measurement; the LIVE body of each, read again at the end of the measurement,
  is 21 bytes longer than that capture (AZN 1,289,826 vs 1,289,805; BATS 1,162,875 vs 1,162,854) with no code change, and against that fresh live read the pin's growth is **132 bytes = the name's own
  `team_sheet` delta** (probe: 0 paths outside `team_sheet` for both). A stored value moved between the capture and the read. **Consequence for the act: the pre-act capture is taken by RA1
  IMMEDIATELY before the apply (the order says so), and the bound is graded live before vs live after, never against an older capture.**
- **`clock` (1 path):** `.generated_at`.

NOT moved, and the post-act compare must show it: every `fiscal_year_figures`, `fiscal_years`, `header_figures`, `check_face`, `model_status`, `posture`, `dossier_fields` and every `model` key but
`team_sheet` (95 of 95), every classification, name, sector and its source and date (bd-1's serve), every score, rank and peer member (243 x 2 reads), the timeline, the ranked lists, the collected
chatter, the PROD page's rendering (it reads `team_sheet` in 0 files of `src/pages/SecurityAnalysis`; the PROD-built page is `origin/PROD` `37aa1247ee`).

## BLAST RADIUS -- the CONTENT-DIFF the build may print against the live package, each member admitted by BLOB at the GO

Measured by `r94_admission_table.py b3d4856531 --pin a03d92221a`: **three lib members differ at the pin**, no registry file.

| member | blob at the live build input `a03d92221a` | blob at the pin `b3d4856531` | reaches the function's request path? | admitted for / by |
|---|---|---|---|---|
| `lib/research/corpus/dossier.py` | `13463426d0da` | `6c4529c51a13` (+2 -1) | **YES** (imported at request time, measured in round 98: `sys.modules` after six routes) | AMGT_CORPUS `ax-7` half; the `METHOD_VERSION` literal |
| `lib/research/corpus/team_sheet.py` | `956e69d7be7e` | `3ba68a99a22f` (+14 -10) | NO (producer-side) | AMGT_CORPUS; packaged, inert |
| `lib/research/corpus/factset_descriptions.json` | `76faa8d6a708` | `690950020aa5` (+40 -1) | NO (build-time data) | AMGT_CORPUS; packaged, inert |

Every other member is BYTE-EQUAL to the live package, **including `scoped_amgt.py` (`9b13bf0371d4`), `monthly_chatter.py` (`38e9511ccc9c`), `lib/opal_naming.py` (`3902e0e93ee4`) and `analyze.py`
(`bf1d15b14ba1`)**. **Any other member is a STOP**, including `scoped_amgt.py` or `monthly_chatter.py` at any other blob. The builder replay (`r94_naming_replay.py --pin a03d92221a`, from the
pin's worktree): **35 requests all 200, 88 builder calls, 18 distinct (`address` 7, `key` 11), 0 differ: `R94 NAMING REPLAY: YES`.** NO IAM, route, memory, schedule, store write or S3 delete.
The act writes NO data object.

## WRITER CENSUS of the moved served property (N printed, each rule read in the pin)

- `/thesis` `model.team_sheet`: **ONE** assignment, `scoped_amgt.py:3871` `model["team_sheet"] = _team_sheet_from_dossier(dossier_read)` (the stored field AS STORED). **N = 1.**
- the dossier read behind it: **ONE** call per request, `_read_dossier_document` (`scoped_amgt.py:5208`), whose pick rule is `dossier.read_dossier` (`dossier.py:1589-1625`): objects at the
  reader's `METHOD_VERSION` are picked among when any exist, else all. **Pick rules N = 1.**
- NOT moved: the classification, name and sector writers (`scoped_amgt.py` is byte-equal).

## EXPECTED OUTCOME -- both branches, read from the rules above

- **Branch 1 (the table's reading):** for every one of the 95 names the live `/thesis` `model.team_sheet` equals the stored /14 field (every key): 83 names carry their changed rows (252
  `absent` -> `held`), 12 are byte-equal to their pre-act read; every other path of every route reads byte-equal to its pre-act read except the generation clocks; `segment_table` sums print as they do
  now (0 `float_repr`); `ax7_compare.py <live pre> <live post>` prints `ax7 compare build 1/1` with `team_sheet_equals_stored14` 95/95, `others_equal` 95/95, growth within each name's own delta (live
  vs live, both python3.11), the maximum under 6,291,456 bytes (predicted 1,289,958). `r97_sector_serve_census.py`, `r95_classification_census.py` and `r94_name_census.py --where deployed` keep
  reading YES (bd-1's serve KEPT); `r89_deployed_close.sh --want amgt-corpus-dossier/14` reads YES.
- **Branch 2 (anything else):** a path changed that is not in the table, a status other than 200 for a name that read 200 before, a changed classification, name, sector, score, rank or member, a
  served field other than `model.team_sheet` unequal to its pre-act read, a name whose `team_sheet` is unequal to its stored /14 field, a response above 6 MiB, a growth above a name's own
  `team_sheet` delta (live vs live), a content-diff member the table does not admit, or `scoped_amgt.py` / `monthly_chatter.py` at any other blob: **STOP** and, inside the same hour, a rollback
  unless the CTO names KEEP on the evidence. A newer stored object or a Bloomberg pull between the pre-act capture and the apply moves a vintage stamp or a few bytes of a name's non-team_sheet
  content: it is a read, never a STOP, provided the key set and every value but that stamp equal and the growth over the name's `team_sheet` delta is accounted for by that moved input (printed).
- **Branch 2's slow-request clause (new, from rounds 98-99):** the function's own log reads 53 of 32,528 invocations over 20 s in a day, 47 of them BEFORE the round-98 apply, 49 with a
  'Connection pool is full' warning, none naming a route (`BF2_OVERLAY_TAIL_READING_20261011.md`). **One request over 20 s in RA1's replay is therefore read against that baseline, not as a STOP:
  RA1 re-invokes it three times; if every re-invoke is 200 with identical bytes it is recorded with its request id and duration; a re-invoke that is not 200, or bytes that differ, is Branch 2.**
  No other seat's reader runs on the function during the replay.

## ROLLBACK (per key; the act writes no data object)

| what | may touch | rollback |
|---|---|---|
| `opal-amgt-scoped-api` code | the function's code package, nothing else | the KEPT live package (`mbGRmy1H..`, downloaded and hash-checked BEFORE the apply) through the module: ONE `safe-apply`, same hour |
| `lambda-source-map.json` entry | the function's one entry | the printed before value, restored in the commit that reverts |
| change-management entry | one entry, opened before and closed after | closed `ROLLED_BACK` with the reason |

Not a portal PROD push. The PROD-built page reads this API; it does not read `team_sheet`.

## SEQUENCING AND THE GO (the GO is the issuer's; RA1 does nothing before it)

1. THIS pair signed (both halves, at the table above) and AMGT_CORPUS's served-effect half in force (the `ax-7` CTO half, msg 4140). 2. RA1 captures the 95 thesis payloads
(`aw4_capture.py`) IMMEDIATELY before the apply and tells the issuer; `2.0.0_SA_COO~C1` runs its own post-act read when the issuer relays the new CodeSha256. 3. The pin: the GO prints
`r94_admission_table.py <pin> --pin a03d92221a` in the build worktree (three lib members, blobs as above, the two api blobs equal) and `r94_naming_replay.py --pin a03d92221a` (YES). 4. No
other write to this function and no reader of any seat on it during the post-apply replay: the issuer and `2.0.0_SA_COO~C1` hold theirs until RA1 reports; RA1 reads the change-management ledger and
the open deploys of every live worktree and prints the denominator. 5. RA1 re-reads the baselines immediately before the apply. 6. After the apply: the issuer tells `2.0.0_SA_COO~C1` the new
CodeSha256 and time; `/15` follows as a THIRD redeploy under its own pair if it is ready.

**COO HALF: SIGNED** by `2.0.0_SA_COO~R1`, for the act, branches 1 and 2 (with the slow-request clause), the blast radius and the rollback above. **CTO HALF:** owed by `1.0.0_SA_CTO~DELL1`.
