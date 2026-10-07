# Never-widen half, MDPF_HEALGAP round 1 -- the one real run of FWD-1: one morning's Cottonwood Rebalancer pull made to fail, healed the same day

**Author:** `2.0.0_SA_COO~G1` (dell1), 2026-10-07 ~14:3xZ. **For:** `1.0.0_SA_CTO~DELL1`, the CTO half. **Status: BOTH HALVES SIGNED** -- CTO half
`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_HALF_MDPF_HEALGAP_FWD1_EXERCISE_20261008.md` @b05cdf04c1, conditions (1) GO only after HG-d2 completes with its SKIP probe and WIRED-OK, (2) each put-targets timed and read back, RESTORED-OK by 06:20Z, (3) a targeted plan reads no change after the restore, (4) whether the 13:30Z floor was met is recorded, (5) one date only -- all carried into `MDPF_HEALGAP.TO-HG-d3`. The exercise runs only after `MDPF_HEALGAP.TO-HG-d2` is complete (the re-attempt target live, `WIRED-OK`) and both halves
are signed. Order: `MDPF_HEALGAP.TO-HG-d3`. **Andrew's word:** ACT 1 @e5fb41862f ("1.) Yes, rec approved."), which names this exercise
as covered (the same call on the same runner).

## The act (exercise date 2026-10-08, or the first date after HG-d2 completes)

1. Before 05:50Z: `aws events put-targets --rule cot-rebalancer-runner-daily` re-putting its ONE existing target (same `Id`, same
   `Arn`) with input `{"mode":"pull","induce":"auth-lapse"}`. Read it back.
2. 06:00Z: the scheduled fire runs the live runner (HG-t-1 build). No stamp exists for the date, so the guard passes and the induced
   branch raises `BD GET /auth/token -> HTTP 401: INDUCED auth-lapse ...` before any secret read or vendor call. Lambda's async
   retries (2, within minutes) raise the same. `on_success` does not fire. Nothing is written.
3. By 06:20Z: re-put the same target with input `{"mode":"pull"}`, read it back (`hg_fwd1_exercise.py --restored`). Terraform state
   then matches the declared input again (the act changes the input only. CORRECTED 2026-10-07 ~20:2xZ, row MDPF_HEALGAP-S11: since amendment @7a61248f77 lets step 1
   run the evening before, the induced input is live from 17:40:36Z to the 06:05-06:20Z restore, ~12.5 hours, not ~25 minutes; during
   that window an untargeted apply of opal-assets would restore it and void the test -- held off by laptop 1.0.0_SA_CTO msg 106554's
   CROSS-BOX DEPLOY NOTICE until 06:20Z).
4. ~11:32Z: the session chain's sentinel fires `cot-bronze-complete`; its new target invokes the runner with `{"mode":"pull"}`. No
   stamp exists, so the runner pulls (ONE Black Diamond pull, under ACT 1), lands the three feeds, writes the stamp, and `on_success`
   drives silver, then gold.
5. The issuer's read: `--failed`, `--healed`, then the reader's served Cottonwood figures for the date by end of day.

## What changes, read from the producers' own rules

**Writers counted:** the date's bronze keys and stamp, N = 1 rule (`ingest`); silver, N = 1 (the converter on `on_success`).
**Both branches:**
- (A) The re-run at ~11:32Z succeeds: the date's three feeds and stamp land ~5.5 hours later than on a normal day; silver and gold
  follow through the existing chain. The served Cottonwood point for the date appears that day. Whether it is in place by the
  13:30Z floor (MDPF_TRGALN) is NOT predicted here: the bronze lands ~2 hours before the floor and the silver/gold chain's duration on
  this feed is unmeasured. The outcome only claims "by the end of the same day".
- (B) The re-run fails (session chain dead that day, or any raise): the date has no Rebalancer data, as on any failed day today.
  Remedy the same day, still under ACT 1: one manual invoke of the runner with `{"mode":"pull"}` for the date, by the deploying seat,
  recorded in the ledger. The FWD-1 run is then graded NOT REALIZED for this date, and the cause gets a row.
- The 2026-10-08 fire is the ONLY one changed. Every other day keeps `{"mode":"pull"}`.

## Blast radius

The `cot-rebalancer-runner-daily` target's input for one fire. On branch (A), the bronze keys, stamp and silver/gold partitions of
that ONE date are written ~5.5 hours later than usual. The served Cottonwood figures for that date are late by the same amount, or on
branch (B) absent until the manual remedy. No other date, feed, firm, function or rule.

## Rollback

Re-put the target with `{"mode":"pull"}` (step 3; also the rollback at any point). If step 3 is missed and the next scheduled fire
(2026-10-09 06:00Z) would read the induce input, `--restored` reads BAD and the seat re-puts before 05:59Z. Data: nothing to undo.

## Acceptance

1. HG1-d3-AC1 `hg_fwd1_exercise.py --failed <date>` -> `FAILED-OK`.
2. HG1-d3-AC2 `hg_fwd1_exercise.py --healed <date>` -> `HEALED-OK`.
3. HG1-d3-AC3 `hg_fwd1_exercise.py --restored` -> `RESTORED-OK`.
Base reads 2026-10-07 ~14:3xZ: AC1 and AC2 BAD for 2026-10-08 (not run); AC3 OK. Controls on 2026-10-07, a normal day: AC1 BAD (never
induced), AC2 BAD (stamp written 06:00:58Z, before 11:00Z): the checks distinguish a healed day from a normal one.

## COO half -- SIGNED

`2.0.0_SA_COO~G1`, 2026-10-07, after reading the live runner (HG-t-1 build, the induce branch's position after the guard), the daily
target, the 10-01..10-06 sentinel times, the stamp census and the checks' base and control runs.
- **Blast radius, writers counted, rollback:** as above.
- **Not signed here:** FWD-2..FWD-6 (enrichment); the 13:30Z floor for the exercise date (not predicted, stated above).
