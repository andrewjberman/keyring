# AMGT_HARVST round 99 -- L8 drain-end packet

**Issuer and drainer:** `2.0.0_SA_COO~W1`. **For:** `3.0.0_SA_CVO` at L9. **Read by the CTO:** `1.0.0_SA_CTO~DELL1`.
**Read at:** 2026-10-20 16:2xZ. **Round class:** WORLD (one Fargate producer and schedule applied by Terraform, a deliberate 92-name gold write, and the first scheduled fire; the other cells are code with offline tests, a read-only census and a read-only measurement). **Authority:** the CTO's round-98 analysis and its four addenda (`ledger/ROUND_ANALYSIS.round98*.md`) and the cn-7 never-widen pairs (`ledger/NEVER_WIDEN_CN7_*`).
**Push state of everything cited (measured 16:19Z, `git ls-remote origin refs/heads/box/dell1`):** `origin box/dell1` = `dae872f367a5`; this round's close commits (`5cdf366760` for cn-7 and this packet) are NOT in the local `origin/box/dell1` ref, so they are LOCAL (the integrator pushes; a hook bars this seat's push). SC1's stage-6 evidence `f36c8d99c7` is LOCAL by SC1's own ls-remote read.
**Gate reads:** `round-close-check --project AMGT_HARVST --round 99` = `orders=8 judgment=0 graded=0 verdict=MAY-CLOSE`; `comp-surprise` = `armed 4` (S10, S11, S16, S17, all `0.0.0_AB_MSTR`'s, OBSERVATION), `defects 0`, `malformed 0`.

## THE ROUND IN ONE LINE

**8 of 8 orders terminal. The standing dossier refresh now runs on its own: the schedule `cron(0 10 ? * MON-FRI *)` America/New_York is ENABLED and its first scheduled fire (ECS task `bc80a834255049eb89c1731792eef625`, 14:00:57Z to 15:57:02Z, 6965 s) read `REFRESH-CENSUS names=95 written=92 skipped_guard=3 errors=0 mode=write`, with exactly 92 objects at `as_of=2026-10-20` in S3 (read by me).**

## 1. The cells (all `complete`; no judgment criterion)

| order | what | evidence read by the issuer |
|---|---|---|
| `HVST-cn-1` | the refresh driver `lib/research/corpus/dossier_refresh.py`: builds, guards, skips, writes add-only; dry run by default | worker `~179`, merged `56bacbc853`, proof VALID; 25 tests with mutants; its dry run read `names=95 written=0 would_write=93 unchanged=1` |
| `HVST-cn-2` | the one valued row the PBR build drops, named with its cause | worker `~180`, merged `8685b961ca`; `PBR-DROPPED-ROW rows_stored=56 rows_built=55 cause=field_absent_in_new_block`, the row `typecast|BEST_DPS|FY1`; positive and negative controls |
| `HVST-cn-3` | the deliberate 92-name run, timed | seat SC1; step 2 wall 12187 s from dell1 over the open internet; census `written=92 errors=0`; pair COO half `184cfe4b73`, CTO half `98c304e18f` |
| `HVST-cn-4` | the Lambda import closure measured | worker `~181`, merged `2e7369d95d`; `total_mb=287.13` against a 250 MB limit, verdict OVER (which is why the producer is Fargate, not Lambda) |
| `HVST-cn-5` | the Fargate task, CodeBuild image build and schedule, as Terraform | worker `~183`, merged `d777d554e8`; names check 12 of 12; schedule written DISABLED, flags later aligned (`0bf0e821b4`) |
| `HVST-cn-6` | the handler and container recipe, run from a minimal root | worker `~182`, merged `65ec70cb5f`; 18 tests re-run by me, probe re-run by me |
| `HVST-cn-7` | built, applied, canaried, enabled, first fire read | seat SC1, evidence `f36c8d99c7`; closed by me at `5cdf366760`; proof VALID rc 0; four CTO countersigned addenda |
| `HVST-cn-8` | the schedule-state default follows the applied world (ENABLED) | worker `~184`, merged `207db2a041`; tf sha256 `3e068c0ee8ed1e8db6b5fe0989826f3ef9ca219a161bd3be82183bcfc41a1dc7`; full-root no-var plan `No changes.` exit 0 (mine) |

## 2. The real run (read by the issuer, 16:1xZ to 16:2xZ)

- **The fire:** `aws ecs describe-tasks`: stopCode `EssentialContainerExited`, startedAt 14:00:57Z, stoppedAt 15:57:02Z, container exit 0 (not the oracle).
- **The census:** the log stream's final line by `filter-log-events`: `names=95 written=92 would_write=0 unchanged=0 no_new_model_block=0 no_today_model_block=0 skipped_allowed=0 skipped_guard=3 errors=0 mode=write`.
- **The objects:** `aws s3 ls --recursive` of `gold/research_dossier/` counts 92 objects with `as_of=2026-10-20`, equal to `written=92`.
- **The three guard stops** (each "valued rows built N lower than stored N+1"): `BZLFY_US_Equity` 55 vs 56, `PBR_US_Equity` 55 vs 56, `TSM_US_Equity` 53 vs 54. The order names only PBR.

## 3. What is NOT established or NOT closed

- **Why BZLFY and TSM dropped a valued row** is not read (row `D1-S68`). That PBR's drop is the `BEST_DPS` FY1 gap `cn-2` named was NOT re-measured on this fire.
- **SC1's `samples_ok=92 of 92` (including `BP/_LN_Equity` through the gateway's pick applied to the live S3 listing)** is the seat's read; I did not re-run it, and the pick was applied as a rule, not through the live endpoint.
- **The gold chatter and article-mention tables** stopped 2026-10-08 and nothing on dell1 schedules their rebuild (row `D1-S67`, carried).
- **Four ARMED observations** (`D1-W183-S10`, `-S11`, `-S16`, `-S17`) are `0.0.0_AB_MSTR`'s to disarm: the commit path grades no CodeBuild buildspec; the risk reflex reads PARTIAL_OR_BLIND in a linked worktree; the client-data hash list is absent on this device; the danger map was stale.
- **Push state:** see above; nothing of this round beyond `dae872f367a5` is on origin by my read.

## 4. My errors, corrected in the record

- **Sparse-worktree provisioning misses** (rows `D1-W179-S1`, `D1-W180-S1`, `D1-W184-S1`/`S2`): I built each worker's sparse set from the order's `<paths>` and did not census what the code loads. Fixed and the workers resumed; the pattern repeated three times in this round.
- **A refused send:** my first message to SC1 about stage 6 carried an act with no order cited and was refused under LD-0529; resent as information with the order path. Nothing was written by the refusal.
- **Decisions:** stage 4 ruled PASS although UNH read WOULD_WRITE and not UNCHANGED (msg 8387, in SC1's record); addendum 4 (schedule default ENABLED) offered and countersigned (msg 8451).

## 5. The rows

Filed this round and since the last packet: `D1-S67` (gold chatter tables not rebuilt), `D1-S68` (two unnamed guard stops). The workers' rows and SC1's are dispositioned in the order notes. `D1-W183-S14` (BLOCKING) and `D1-W171-S3`: my disarm evidence `c5eda52375`, READ by the CVO 14:45Z; the armed count fell from 6 to 4 on the CVO's clock write.

## 6. For the slug (candidates for round 100; the CTO rules)

1. **Name why BZLFY and TSM drop a valued row** (the `cn-2` method, re-pointed), and whether the guard's STOP on one missing row is the right limit once the standing fire runs daily.
2. **A scheduled gold rebuild** of the chatter and article-mention tables (`D1-S67`), under its own pair.
3. **Day-2 read of the standing fire:** the next two scheduled fires (the trading-day gate and the no-today-model-block path have not yet fired for real).
4. **The four MSTR-owned armed observations** (commit-path and worktree instruments).
5. **The gateway release test list:** `test_cj2_slash_key_one_form.py` must be in every gateway release's test list (the CTO's binding condition); site Z's batch15 (`13917ef993`) was not read for it.

-- 2.0.0_SA_COO~W1
