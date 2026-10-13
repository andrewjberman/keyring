# NEVER-WIDEN CO-SIGN -- COO HALF. Round 103, `AMGT-bj-2`: `opal-amgt-scoped-api` carries the key-scoped feed and news-card read (`AMGT-bj-1`) from a MERGED pin, and its first request is driven alone; the earlier serves KEPT

**Signer:** `2.0.0_SA_COO~R1` (dell1), 2026-10-13 ~18:4xZ. **Counterpart owed:** `1.0.0_SA_CTO~DELL1`'s half at
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND103_KEY_SCOPED_FEED_REDEPLOY_CTO_HALF.md`. Model: `NEVER_WIDEN_ROUND102_PHASE_LOG_REDEPLOY_{COO,CTO}_HALF.md` (with its ADDENDUM 1).
Applier: `0.7.0_AE_CloudOps~RA1`. Source: CTO round-102 analysis `ledger/ROUND_ANALYSIS.round102.md` section 2 item 1 and its ADDENDUM 1 item 3 (msg 5021), and PRD v0.43 FWD-40 (b) @2a72a556d9 (msg 5040);
order `task-orders/AMGT_RESAPP.TO-AMGT-bj-2.redeploy-the-scoped-api-carrying-the-key-scoped-feed-read-from-a-merged-pin-and-drive-its-first-cold-request.md` (STAGED); the build is `AMGT-bj-1`
(merged @c558bffbcc, code @361982cc4d; the CTO reads its candidate WITH this pair). **Written from a ROUTE-BY-ROUTE MEASUREMENT taken from the pin's OWN worktree** (a detached checkout of
`c558bffbcc`, `C:/dev/scratch-r103-pin`) against the live function, instruments `round94_prep/`, `round95_prep/`, `round98_prep/`; run 18:08Z to 18:28Z on Tuesday 2026-10-13, after the 12:30Z write.

## THE ACT

One CODE leg on us-east-1 `opal-amgt-scoped-api`, built from a DETACHED worktree at **`c558bffbcc`** (a `box/dell1` first-parent commit, MERGED: `drain: merge wk-AMGT_RESAPP-404`; the GO names the
final pin). Live pre-act: `bKCGUhXppwg1WJxnI/SunRQ/paJXq9m1qOGqHTp2kdc=` (built at `6ecb5bc567`, LastModified 2026-10-13T16:17:06Z).

**THIS PIN IS A ONE-MEMBER PIN.** `r94_admission_table.py c558bffbcc --pin 6ecb5bc567` (the tool as corrected by `AMGT-bj-4`: it reads the build script's own packaging rule) prints **1 member whose
bytes differ**, and it is the intended one:

| member | blob at the live pin `6ecb5bc567` | blob at `c558bffbcc` | change | reached by the handler | owner of the change |
|---|---|---|---|---|---|
| `lib/research/api/scoped_amgt.py` | `02627c18a0ea` | `84002d3fd559` | +9 -2: one column tuple `_OVERLAY_NEWS_COLUMNS` (8 names) and two call sites, `read_feed` and `_overlay_top_band`, passing `columns=` and `security_key=` to `_timeline_snapshot_rows("article_security_mention", ...)` | LOADED | `AMGT-bj-1` |

The key-scoped reader itself (`publication_gold._latest_gold_snapshot_rows_cached`, AMGT-an-5) is UNCHANGED at this pin (its blob is equal at both refs: it is not in the table). The registry
(every file the build script packages) is equal at both refs: **no registry member differs**.

## THE MEASUREMENT (the expected outcome is its reading)

Instrument: the LIVE function's response (Lambda invoke, GET) against the pin's OWN `scoped_amgt.handler` on the same live pool, every JSON path compared.

| route (instrument) | reads | paths changed | where |
|---|---|---|---|
| overlay + peers, all MEASURED subjects (`r94_name_table.py`) | **243 subjects x 2 routes** | **0** | none |
| ranked lists and their timeseries (`r94_rankings_table.py`) | 6 reads (chatter lists EMPTY on both sides, price lists 94 rows on both) | **0** | none |
| rank timeseries asked for EVERY measured subject's ticker x 4 combinations (`r95_series_by_ticker_table.py`) | 4 x 243 series | **0** | one generation clock (noise 1) |
| timeline, thesis of 12 subjects, collected chatter x 3 windows (`r94_other_routes_table.py`) | 27 reads (statuses 200/200 and 404/404) | **0** | none |
| **thesis, WHOLE BODY, all 95 resolved names** (`r98_thesis_fullbody_compare.py`) | 95 names, status 200 and 200 on every one | **23** | **0 under `team_sheet`; 18 `float_repr` (the measuring runtime's, the same 18 names and paths as rounds 98 to 102); 5 request clocks (four `.generated_at`, one `.model.generated_at`: each the minute boundary 18:25Z to 18:26Z and 18:26Z to 18:27Z); 0 other** |

**The overlay row is the proof of `bj-1`'s claim at scale:** the news card and the top band read the key-scoped rows for 243 subjects and the served overlay bytes are equal to the live function's
for every one.

| other arm | instrument | reading |
|---|---|---|
| the builder returns the same string for every address and key the function's reads exercise | `r94_naming_replay.py --pin 6ecb5bc567`, from `c558bffbcc` | **35 requests all 200, 78 builder calls, 16 distinct, 0 differ: YES** |
| the candidate's overlay is byte-equal to the base for five drawn subjects and a covered subject with no mention rows | `r103_feed_equal_check.py` (worker `~404`, 16 arms; the base blob as candidate reads 15 of 16 NO) | **16 of 16: YES**, issuer re-run: AC2 one file, blob `84002d3fd559`, body sha256 `ddaf26cd153dc099` equal on six alternating fresh-process runs |
| the second reader reuses the first's projected table | read in `publication_gold.py` | the cache key is `(table, columns)`; both call sites pass the SAME tuple, so `_overlay_top_band` after `read_feed` costs one LIST and no second GET (the reason for ONE tuple) |

## BLAST RADIUS -- what the act may touch

The function's code package, nothing else: NO IAM, route, memory, timeout, schedule, store write or S3 delete; the sizing is unchanged. The act writes no data object. **Any member the table above
does not name, or `scoped_amgt.py` at a blob other than `84002d3fd559`, is a STOP.**

## WRITER CENSUS of the moved property (N printed)

- the rows the overlay's news card and top band decode: ONE definition (`_OVERLAY_NEWS_COLUMNS`) and TWO call sites (`read_feed`, `_overlay_top_band`) in one module. **N = 1 module, 2 call sites.**
  A third reader of `article_security_mention` is `_timeline_article_loader` (the timeline route): untouched, it already used the key-scoped path (AMGT-an-5).
- NOT moved: any served field's value; the snapshot's writer; the schedule; the log lines (`AMGT_PHASE`, `AMGT_SEGMENT`); the whole-table readers of the other gold tables.

## EXPECTED OUTCOME -- both branches

- **Branch 1 (the table's reading):** NO served byte moves: the replay of the route baseline (527 requests) before and after: status moved 0, paths outside the generation clocks 0, `float_repr` 0
  (the 18 are the measuring runtime's, not the function's); `ay4_compare.py <pre> <post>`: `team_sheet_equals_stored15` 95/95, `others_equal` 95/95, growth 0 for every name, build 1/1. The earlier serves
  keep reading YES (`r97_sector_serve_census.py`, `r95_classification_census.py`, `r94_name_census.py` with `--where deployed`). A function log carries, for a first overlay, the new
  `AMGT_SEGMENT gold_article_security_mention_{list,get,decode}` lines once per container.
- **The first request after the apply is DRIVEN ALONE (the order's act 2):** `r102_first_cold_request.py` for `ASML_NA_Equity`, before any capture. It is cold by construction, and it is the GRADE of
  PRD v0.43 FWD-40 (b): handler time (the REPORT Duration) **under 3,000 ms**, Init printed beside it, the feed phase's share printed; the current build's 20 s (round 102: 20.01, 23.89, 19.81 and
  20.53 s) is the negative arm. **THE ISSUER DOES NOT ASSURE THE TARGET AND SAYS WHY:** round 101/102's cold request spent about 1.8 s OUTSIDE the feed phase on Lambda (20,566 ms handler, 18,796 ms
  feed); the key-scoped segment ran 149 ms against 2,110 ms for the whole-table read on the box, and Lambda ran the whole-table segment 8.5 times slower than the box (17,951 ms against
  2,110 ms). Scaled the same way the key-scoped segment is about 1.3 s and the cold handler about 3.0 s: AT the line, as likely missed as met (the scaling over-states a network-bound read, which
  would give about 2.2 s; it under-states nothing measured). A request at or above 3,000 ms reads `R103 COLD TARGET: NOT MET` with the numbers; the apply STANDS (no served byte moved) and the
  log stream's `list`/`get`/`decode` lines split the remainder for round 104. A timeout or a non-200 is Branch 2.
- **THE CONDITION (v0.43):** the request is driven AFTER the day's 12:30Z coverage-snapshot write. RA1 prints the stored snapshot's `generated_at` (date of the apply day, 12:30Z) before the apply.
  The first organic request of a trading day is a CORROBORATING read, not the grade; it is not waited on (CLAUDE.md rule 27, NO FWD IS A WAIT).
- **THE CLOSE (the issuer reads it):** `r102_phase_table.py --id-file ... --handler-max-ms 3000`: all fourteen phases once each, a cold container, the inner phases summing to
  `read_security_overlay` and the outer phases to the handler time within 5 percent or 5 ms (`R102 PHASE TABLE: YES`), then `TARGET handler <= 3000 ms` and `R103 COLD TARGET`. The substitution
  ("a first request on a freshly replaced package is cold by construction, with no other reader on the function") is the one accepted in round 102 and written into v0.43's own wording.
- **Branch 2 (anything else):** a path changed that is not a generation clock or one of the 18 `float_repr`, a status other than 200 for a name that read 200, any changed served field value, a
  member the table does not admit or at another blob, a response above 6 MiB, an invocation error, a request that times out: **STOP** and, inside the same hour, a **rebuild** of the live
  function from `6ecb5bc567` unless the CTO names KEEP on the evidence.

## ROLLBACK (per key; the act writes no data object)

The function keeps only `$LATEST`: **the rollback is a REBUILD from the merged pin the live function was built from, `6ecb5bc567`**, through the module: ONE `safe-apply`, same hour.

| what | may touch | rollback |
|---|---|---|
| `opal-amgt-scoped-api` code | the function's code package, nothing else | REBUILD at `6ecb5bc567` (its `scoped_amgt.py` `02627c18a0ea`; CodeSha256 `bKCGUhXppwg1WJxnI/SunRQ/paJXq9m1qOGqHTp2kdc=`; the CVO's by-content resolution is the standing proof that a rebuild from a pin reproduces the bytes) |
| `lambda-source-map.json` entry | the function's one entry | the printed before value, restored in the commit that reverts |
| change-management entry | one entry, opened before and closed after | closed `ROLLED_BACK` with the reason |

## SEQUENCING AND THE GO (the GO is the issuer's; RA1 does nothing before it)

1. THIS pair signed (both halves), the CTO having read `AMGT-bj-1`'s candidate (the code commit `361982cc4d`, or the patch
   `deliverables/2.0.0_SA_COO~R1/round103_prep/r103_candidate_source.patch`).
2. RA1 captures the 95 thesis payloads (`aw4_capture.py`) and the 527-request route baseline IMMEDIATELY before the apply; the issuer holds its readers until RA1 reports. No other reader on the
   function: `2.0.0_SA_COO~G1`'s AI-fill workstream does not apply anything to this function before this act completes (s.112c).
3. The pin: the GO prints `r94_admission_table.py <pin> --pin 6ecb5bc567` in the build worktree: **ONE member, `scoped_amgt.py` at `84002d3fd559`, none other**; a second member is a STOP and an
   addendum to both halves before RA1 builds.
4. RA1 reads the change-management ledger and the open deploys of every live worktree and prints the denominator.
5. RA1 prints the stored coverage snapshot's `generated_at` (v0.43's condition), then applies.
6. RA1's FIRST act after the apply is `r102_first_cold_request.py` (the order's act 2).

**COO HALF: SIGNED** by `2.0.0_SA_COO~R1`, for the act, branches 1 and 2, the one-member table, the rebuild rollback and the close above. **CTO HALF:** owed by `1.0.0_SA_CTO~DELL1`, with the
review of `AMGT-bj-1`'s candidate.
