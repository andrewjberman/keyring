# ETFS_GUARDRAIL round 2 -- L8 PACKET (PARTIAL: 1 of 5 orders terminal; the filename keeps the history of its versions in place)

**Compiled by** `2.0.0_SA_COO` 2026-09-10 ~00:4xZ on the `/drive` obligation "terminal orders -> L8 compile NOW", at the first drain of round 2.
**For** `3.0.0_SA_CVO` at L9, as a FILE (the spine's three tracks share files, never messages; the one message names this path and its hash). **This is NOT the L10 slug** -- the slug is the CVO's, after L9, once every order of the round is terminal. Four orders are open on two live worker slots; this packet will be REVISED in place at each drain.

---

## 1. THE ROUND, AS IT STANDS AT L7

Round 2 is the manual-trigger round: PRD v0.4 @`a830ea1cc0` (the addendum on Andrew's 21:4xZ no-waiting word) placed five cells; ONE issuance @`4155c85a1f` cut all five on three worker slots (`fanout: 3 of 3 chains, cap 8`): slot `~1` holds EG-s-14 -> EG-s-15 -> EG-s-16 by continuation, slot `~2` held EG-s-17, slot `~3` holds EG-s-18. All five faces were AMENDED @`5507841f04` the tick the first two worker reports landed (rows W1-S11..S16, W2-S7..S9), and EG-s-18 again @ this packet's sibling commit on row W2-S10; every re-cut is judged on EFFECT in the AMENDMENT paragraph before each face's `<expected_criteria>`, told to `1.0.0_SA_CTO` and `3.0.0_SA_CVO` (94793, 94795, 94803).

**Two findings the CVO should read first, because they shape every grade in this round:**

1. **The August re-render FIRED and FAILED on the box (row W1-S11).** The deployed `render_month_end.py`, byte-equal to repo HEAD, raises `ModuleNotFoundError: _orion_vendor_asof` at `:72/:75`: its fallback resolves `/opt/coverage` while the vendored copy lives at `/opt/etfs-reports/coverage`, pulled by a bootstrap that runs AFTER the import. Nothing rendered, published or sent; the 5 served objects unchanged; the priors archived byte-equal; the ledger entry HELD on the row. **The 10-01 scheduled fire would have failed identically.** The fix, its box-layout rehearsal, its deploy as a new leg of the same held NEVER-2 entry, and the re-invoke are ordered on EG-s-14 (the CTO: inside the grant, no new half, 94795). NOT YET ASSERTED by anyone: whether the 09-01 scheduled render ran a renderer without this import (the alignment landed in EG-s-13 after 09-01).
2. **Every CloudTrail `Invoke` arm on the five faces read an instrument no trail covers (rows W1-S13, W2-S7):** `lambda:Invoke` is a data event and 0 of 2 trails select `AWS::Lambda::Function`. The arms could neither pass nor fail. Re-cut onto the log group's `START RequestId` read by time (a manual fire), the SCHEDULER role's `AssumeRole` (the monthly, which has a `RoleArn`), and -- corrected on row W2-S10 -- the cron-instant `START` lines plus the execution role's cold-start `AssumeRole` as corroboration for the two daily EventBridge RULES (which carry no `RoleArn`). The issuer's cut defect, twice tonight in one family with NFRA_OUTSET-S29 (an instrument named without its coverage fact); the substrate-card coverage question is now asked at every cut that names a trail.

## 2. THE TERMINAL ORDERS, each with the instance the checker graded AT THE ISSUER'S SEAT

Re-validated at this seat on the merged tree after the drain, with the expected criterion ids taken from the ORDER at HEAD and passed as the checker's third argument.

| order | cell | instance (under `deliverables/`) | checker at HEAD `d1b8945948` | worker commits | drained at |
|---|---|---|---|---|---|
| TO-EG-s-17 | EG-s-17 | `0.9.0_WK_ETFS_GUARDRAIL~2/ETFS_GUARDRAIL.TO-EG-s-17.the-filled-in-day.proof_of_spec.json` | VALID rc 0; alignment 2/2 criteria, 1/1 cell; artifact-resolution 2 resolved at pin / 5 PENDING co-committed / 1 s3_object skipped (denominator 8); surprises 4 of 4 resolve | `73e6cd94dc` (pass 1: FAIL by output on the instrument, rows W2-S7..S9), `1e995e83b5` (pass 2 on the amended face: PASS by output, the flip, row W2-S10) | `d1b8945948` (clean merge, 8 paths; the channel's 4 branch rows united) |

**EG-s-17, what the output says.** `S17-AC1` PASS by output on the amended face: `arms holding: 7 of 7`, `EGS17-FILLED-IN-DAY` printed WITH `CATCHUP-BRANCH-NOT-EXERCISED` beside it, rc 0; determinism STABLE (two consecutive runs, SUMMARY blocks diff-empty); the mutant FIRED-AS-EXPECTED (carried from pass 1). The one real class-C hole in the estate -- cottonwood `2026-09-08`, the newest priced partition (`partition=true, priced=12016, output_exists=false`; bd 0 of 20 absent, cot 1 of 20) -- was filled by the producer's OWN fire with the rule's byte-equal payload (EventBridge's default scheduled envelope; `Target.Input` ABSENT on 2 of 2 daily rules): request id `0840a0d3-15aa-4884-a12e-20e75cfa6136`, `START` 23:15:50.560Z, ONE write `s3://opal-data-etfs/daily/cottonwood/2026-09-08.json` (4 ETF slices, total_ownership 53,641,351.75, `source_as_of=2026-09-08`), the served object byte-identical after three battery runs (ETag `5da999e2fbfadfe302df35ef24407372`, 1345 B, 23:15:52Z). No second fire, no served delete or overwrite. The schedules' own firing from history: cot 30 of 30 days at 10:30:24Z, bd 30 of 30 at 10:45:05Z (cold-start `AssumeRole` at the cron instants), the manual invoke the negative control (warm, 0 `AssumeRole` in its own window, exactly 1 client `START RequestId`).

## 3. THE JUDGMENT CRITERIA -- THIS IS THE L9 WORK

- **`S17-AC2`** (judgment, recorded in `the-filled-in-day.result.md` ss.0-2, 6-9): the recovered date as a person reads it (cottonwood 2026-09-08, four ETFs, 330/331/320/319 accounts); WHY it was missing -- the 10:30Z daily fire runs ~76 minutes before the D+1 ~11:46Z partition landing, so the newest trading day is sliceless ~11.5 h every day (a measured race, the CTO has TAKEN it for the L10 addendum, 94795); that the port respected the reporting-obligation window (terminus = the shipped 2026-08 signal, no day-count); and **what the token does NOT claim: the catch-up branch (class B/C recovery by `_catchup_missing_dates`) was NOT exercised** -- it is structurally unreachable for a head-of-window hole (`skip_date`), 0 CATCHUP lines in 152 cot / 103 bd log events over 30 days, and exercising it needs a hole older than the newest partition, which the estate does not have. A manufactured hole is a served S3 DELETE: **at Andrew** (this seat's card, 00:0xZ; the CTO concurs, 94795). The CVO grades whether the FWD this cell serves is REALIZED by the main-path recovery or waits on that branch.
- The rows the CVO dispositions at L9: **W2-S7** (BLOCKING/INERT -- the instrument absence; ruled by the re-cut), **W2-S8** (BLOCKING/ARMED -> disarm record **S9** in this commit), **W2-S9** (OBSERVATION/INERT -- the stale `2026-07-31` docstring; for the L10), **W2-S10** (OBSERVATION/INERT -- the daily rules carry no `RoleArn`; the issuer's premise corrected on EG-s-18 in this packet's sibling commit).

## 4. THE OPEN ORDERS (no grade here; stated so the CVO sees the round's shape)

| order | slot | state at HEAD `d1b8945948` | what is in flight |
|---|---|---|---|
| TO-EG-s-14 | `~1` | pending; FAILED BY OUTPUT on the world at the first fire (S14-AC1 arms d, e, f) @`aadcbc7694`; the renderer fix committed on the branch @`0c8bdbe5a5` | the box-layout rehearsal, the deploy leg to `s3://opal-313476888478-lambda-artifacts/ec2/etfs-reports/render_month_end.py` under the held entry, the re-invoke with `--cli-read-timeout 0`, arms (a)-(g) re-read; the ISSUER's gateway read of aj@/andrew@ delivery cited on the face by amendment when the send lands |
| TO-EG-s-15 | `~1` (after S14) | pending | the one line at `lambda_function.py:383`, the targeted plan, the deploy under NEVER-2, the September refusal ladder on real data, the ONE terminal send to andrew@ (the carve-out) |
| TO-EG-s-16 | `~1` (after S15) | pending | the Labor Day read on S15's run |
| TO-EG-s-18 | `~3` | pending; 0 commits at 00:33Z, nudged twice (00:00Z the re-cut, 00:35Z commit-what-stands), corrected on W2-S10 at 00:4xZ | the schedules from history on the re-cut instruments |

## 5. ROWS AND THEIR STANDING AT THIS SEAT (the disarm records are in this commit: S5..S9)

| row | class / standing | disarm owner | standing at this seat |
|---|---|---|---|
| W1-S11 | BLOCKING / ARMED | 2.0.0_SA_COO | DISARMED by the EG-s-14 amendment (the fix + deploy leg + re-invoke); record **S5** |
| W1-S12 | OBSERVATION / ARMED | 2.0.0_SA_COO | DISARMED by the archive-location clause; record **S6** |
| W1-S13 | OBSERVATION / INERT | -- | ruled: the shared-instrument re-cut on all five faces |
| W1-S14 | OBSERVATION / ARMED | 2.0.0_SA_COO | DISARMED by the synchronous bound + the flags; record **S7** |
| W1-S15 | OBSERVATION / INERT | -- | `ARTIFACT-CARRIES-NO-TRIGGER-FIELD`, anticipated by the face; for the L10 (the OUTSET carrier's shape) |
| W1-S16 | OBSERVATION / ARMED | 2.0.0_SA_COO | DISARMED for these faces by the ordering clause; the tool defect to the CVO for a remediation row against `0.2.0_DT_PortfolioAnalytics`; record **S8** |
| W2-S7 | BLOCKING / INERT | -- | ruled: the re-cut |
| W2-S8 | BLOCKING / ARMED | 2.0.0_SA_COO | DISARMED by arm (d)'s re-cut + the call carried to Andrew; record **S9** |
| W2-S9 | OBSERVATION / INERT | -- | for the L10 |
| W2-S10 | OBSERVATION / INERT | -- | the issuer's premise corrected on EG-s-18 |

## 6. WHAT THE ISSUER DID NOT DO

No served object was deleted or rewritten by this seat; no deploy by this seat; no push (origin/CLOUD @`c6bcb7b12b`, ls-remote read 00:09:52Z by `~W` and 23:48:07Z by this seat; every commit named here is LOCAL). The worktree `/c/tmp/wk-etfs-2-2` and branch `wk-etfs_guardrail-2-2` were removed after the drain (`git branch -d`, merged). `dep_stage` stays `EXECUTING` until the CTO's receipt of the CVO's slug.
