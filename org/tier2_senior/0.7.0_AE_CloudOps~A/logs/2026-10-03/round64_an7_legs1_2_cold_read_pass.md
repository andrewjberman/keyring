# AMGT_RESAPP round 64 -- an-7 legs 1 and 2, and the first cold-read pass -- 0.7.0_AE_CloudOps~A

**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE

**Date:** 2026-10-03
**Task Order:** AMGT_RESAPP.TO-AMGT-an-7 sections 1, 6 (AMENDMENT 1) and 7 (AMENDMENT 2, leg 2)
**Status:** COMPLETE -- AC1, AC2, AC3 and leg 2's c10 all PASS; no regression; neither rollback taken.

Delta since `3eeb9490f4` and `4f59f32000`, which covered round 63.

## Objective

Two code-only redeploys of `opal-amgt-scoped-api`. Leg 1 carried an-1..an-6 -- FWD-36/37/38, the cold
read, the repairs and the 500 attribution. Leg 2 carried a one-word widening so the price-window branch
matches `trending` as well as `breakout`. Memory stayed 1769 throughout.

## Compiler Tools

| Tool | Result |
|------|--------|
| `build-and-upload-scoped-amgt.sh --build-only` x2 | PASS. The pre-upload STOP gate: leg 1 `355/349/4/2/0`, leg 2 `355/352/3/0/0`, plus the size line each time. |
| `build-and-upload-scoped-amgt.sh` x2 | PASS. Each real build reproduced its build-only diff AND size exactly. |
| `terraform plan` / `show -json` / `safe-apply` / `-detailed-exitcode` x2 | PASS. 49 `resource_changes`, 1 non-no-op, 3 attributes, `memory_size` 1769 -> 1769 both times; 0-diff after each. |
| `r64_served.py` c9-c15 | PASS. AC1, AC2, AC3 all exit=0; c10 re-graded on both movements at leg 2. |
| `r63_served.py` c3/c4/c5/c7/c8 x2 | PASS, all five YES after both legs. |
| a static import-graph census over the BUILT ZIP (this seat's own) | PASS on both arms with negative controls, run TWICE -- once per leg. |
| a read-only planted-fault invoke + log read (this seat's own) | PASS. One `AMGT_500` line, all four fields. Found a defect in MY predicate. |
| `census_500.py --days 7` | PASS. 6 of 21724 in 7 days, 2 signatures. |
| `.tools/deploy_ledger.py` x2 | PASS. Both entries opened AND COMMITTED before their upload, so both sentinels landed. |

**What worked:** writing the two reads the conditions needed but the cells did not provide. `c8` and `c2`
both satisfy their criterion with COUNTS while their CTO conditions ask for NAMES, and `c16` is local-only
while condition 3 asks for the deployed logs. Reading each check's source before grading it is what caught
that -- three times across the session now.

**What failed:** nothing in the acts. Two process notes. First, a long `--proof` string broke the shell on
embedded quotes; I moved to writing proofs to a file and passing them through a small Python runner, which
also removes the quoting class entirely. Second, my own planted-fault predicate was wrong (below).

**Gap found:** none new.

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | leg 1 base re-read | `31UL+7/s...`, 1769 -- round 63 leg 3's output |
| 2 | leg 1 `--build-only` | `355/349/4/2/0`; 8422589 B spare, equal to the half's figure to the byte |
| 3 | leg 1 import proof, both arms | 0 of 20 module-scope; 0 of 8 routes name `build_mention` |
| 4 | leg 1 entry opened + COMMITTED | `5ddb2d4808` |
| 5 | leg 1 build + upload | VersionId `40smkxDeOsBar9woKz_p5ICvkoUonv9y` |
| 6 | leg 1 `safe-apply` | 0/1/0; `kSeyeO0v...`; re-plan 0 |
| 7 | AC1, AC2 graded | both exit=0 |
| 8 | r63 set, planted fault, census | done BEFORE the idle, so none would warm an environment |
| 9 | 780 s idle, then AC3 | c15 3 of 3 COLD -- **the project's first pass** |
| 10 | leg 1 entry CLOSED | `bf4b04b120` |
| 11 | leg 2 base + `--build-only` + c10 base | `355/352/3/0/0`; c10 base 6 of 8 with 2 trending failures |
| 12 | leg 2 import proof RE-RUN | both arms PASS again on the leg-2 bytes |
| 13 | leg 2 entry opened + COMMITTED | `8b01f68bba` |
| 14 | leg 2 build, upload, apply | `KQSA62c3...`; memory 1769; re-plan 0 |
| 15 | c10 both movements + full regression | 8 of 8; r64 and r63 sets YES; covered keys 8 of 8 at 200 |
| 16 | leg 2 entry CLOSED | `9b94636a21` |

## Verification

c15, the first pass of the project:
```
run 1: 200, 1893.8 ms, cold=True, init 193.49, headlines 6 of 6
run 2: 200, 2307.13 ms, cold=True, init 170.70, headlines 6 of 6
run 3: 200, 2294.41 ms, cold=True, init 171.56, headlines 6 of 6
PASS C1 3 of 3 COLD ... under 5 s with every headline 3 of 3
PASS C2 every run's log carries AMGT_SEGMENT timings 3 of 3
R64 C15 SERVED: YES
```
Segments: identity 504-649, import 761-1027, gold_chatter_daily 366-419 (list 43-59, get 28-69,
decode 185-256), and NO `article_security_mention` segment on any cold run -- against a base profile of
3.55 s of 4.4 s in two WHOLE gold snapshot reads for one security-day.

c10 at leg 2, both movements, 8 of 8 -- against a base where exactly the two trending clauses failed:
```
base   FAIL C2 trending price days=90  status 200 rows 94 reason '  '
       FAIL C2 trending price days=365 status 200 rows 94 reason '  '
after  PASS C2 trending price days=90  status 200 rows 0 reason 'the 90- and 365-day price windows are not produced yet...'
       PASS C2 trending price days=365 status 200 rows 0  (same reason)
```

The planted fault, read off the function's own log:
```
AMGT_500 {"request_id": "d8737bd9-9df3-454b-9fc1-dba6cc1af44c",
          "route": "/security/{security_key}/overlay",
          "security_key": "BA_US_Equity",
          "exception_class": "AttributeError",
          "message": "'list' object has no attribute 'get'"}
statusCode 500, FunctionError None, 0 alarm/notify lines
```

## Decisions Made

1. **Re-ran c15 twice, and reported all nine runs rather than only the pass.** Attempt 1 failed on the
   COLDNESS COUNT, not on speed -- its cold runs were already 2.0 and 2.3 s. Attempt 2 read 0 of 3 cold
   because an apply recycles environments and an immediate re-run reuses them. Attempt 3 followed 780 s of
   idleness and read 3 of 3. Across 9 runs, 5 of 5 cold runs were under 5,000 ms with no exception, so the
   latency never varied and only coldness did. The re-runs were obtaining a VALID sample, not a fast one,
   and saying so required showing every run.
2. **Sequenced the r63 set, the planted fault and the census BEFORE the idle wait.** Each of them invokes
   the function, which would have warmed an environment inside the wait and destroyed the discriminator
   c15 needs. The wait was the discriminator here, not a stall.
3. **Re-ran the import-graph proof at leg 2 instead of inheriting it.** The half says it carries over
   because leg 2 ships the same file, but BOTH ends of the reachability claim changed in that diff:
   `finbert_sentiment.py` is the target and `publication_gold.py` is the importer holding `build_mention`,
   whose keyword the half itself records changing. A reachability proof is not transitive across a change
   to the importer. It still passed; the point is that it is now measured.
4. **Proved condition 3 on the REQUEST-TIME arm, not just module scope.** A module-scope census shows
   finbert is not loaded at cold start, but routes DO reach `publication_gold` at request time, so that
   alone does not settle it. The decisive measure is that 0 of 8 route modules name `build_mention` at any
   scope, with the contrast printed: routes name 2 of `publication_gold`'s 62 functions.
5. **Corrected my own predicate rather than the function.** My planted-fault check read NOT SATISFIED
   because it required the log's `request_id` to equal the `requestContext.requestId` I supplied. The
   function attributes by the LAMBDA request id, which is more traceable, and the join that matters holds:
   the 500 body's `request_id` equals the log line's. My assertion was wrong.
6. **Named the one r63 count that moved, twice.** After leg 1, c8 went 92 served / 2 null -> 93 / 1
   because c14 resolved BP's sector. Reporting "unchanged" flatly would have left a reader to find 93
   against 92 and wonder.
7. **Did not apply round 63's byte-identity standard to leg 2.** Body sizes grew (BA overlay 101996 ->
   127348) because an-1..an-6 add served fields. Leg 2's limb is 200, not byte-identity -- byte-identity
   was right for the memory-only act, where no served value should have moved. Carrying it over would have
   manufactured a failure.

## Files Modified

See commit messages: `5ddb2d4808`, `bf4b04b120`, `8b01f68bba`, `9b94636a21`. No terraform file changed --
both legs are code-only and `memory_size = 1769` stands as round 63 committed it.

## Blockers

**None owed by this seat.**

## Current State

`opal-amgt-scoped-api` runs `CodeSha256 KQSA62c3Diw5XqjBeKKZc0ZTZuTnaaRBbhuEQHfOdXQ=` at `MemorySize 1769`,
artifact VersionId `.xFOZLD1X0znp_5COtZvp3UgWTBrw19p`. Eight NEVER-2 entries opened and closed across the
session, every leg proven, none left open.

Round 64 served state: c9, c10 (both movements), c11, c12, c13, c14 and **c15** all YES. Round 63's c3, c4,
c5, c7 and c8 unchanged and YES. **c1/c15's under-5-s bound is met for the first time** -- the cold read is
1.9-2.3 s where round 63 measured 11.5-12.8 s at three memory values on a flat curve.

Package headroom: 8,419,691 B spare at 96.8%. Any later cell adding to this artifact measures at cut time;
crossing 262,144,000 B is a deploy STOP.

## Next Steps

1. **[`3.0.0_SA_CVO~Z`]** FWD-2, FWD-7 and now FWD-36/37/38 are re-gradeable on PROD. Routing is
   `2.0.0_SA_COO~Z`'s. For the sector grade the two null names are `BP/_LN_Equity` (now resolved to Energy)
   and `NG/_LN_Equity` (null with a TRUE reason, by design).
2. **[`2.0.0_SA_COO~D`]** Per the leg-2 half's condition 5, FWD-26's price presets now read a served window
   on BOTH movements, so `?days` can stop being treated as ignored.
3. **[`1.0.0_SA_CTO~Z`]** The 5 unattributed 500s in the census are TIMEOUTS and structurally
   unattributable -- the process dies before the handler's except arm runs. They belong to the pre-an-7 slow
   cold path this act cut by 5-6x, so the class should stop recurring. The next census can falsify that.
4. **[`0.0.0_AB_MSTR~Z`]** The push. All sixteen commits from this seat are LOCAL on this device.
