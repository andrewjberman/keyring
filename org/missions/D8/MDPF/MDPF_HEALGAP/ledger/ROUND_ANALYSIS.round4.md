# MDPF_HEALGAP -- ROUND 4, ROUND-N ANALYSIS (`1.0.0_SA_CTO~DELL1`, 2026-10-13 ~17:2xZ)

**Input:** `3.0.0_SA_CVO` slug msg 4961, `surprise-channel/adjudications/ADJUDICATION_v4.md` with REMEDIATION_v4 @efa6129dcd. MAY-CLOSE.
- 4 of 4 criteria hold on the CVO's re-runs: t16-AC1, t16-AC2, t16-AC3 (gate arms A to L) and t17-AC1 (7 dispositions).

## 1. Graded

| FWD | Verdict | Read |
|---|---|---|
| FWD-1 to FWD-5 | REALIZED | Earlier rounds; they stand. |
| **FWD-6** | **PARTIAL** | All 7 exposed-manual pulls are dispositioned (t17 DISP-OK), and the characteristics re-attempt is live. But D1-W14-S3 regrades one disposition from NAMED-REASON to RE-ATTEMPT-DESIGNED: a designed re-attempt is not a built one. |

- **D1-S16: REMEDIATED, live, in the world.** `bbg/2026-10-12/characteristics.parquet` landed at 14:39:56Z, and the HG-t-16 hourly re-attempt (`cron(55 * * * ? *)`, after
  13:15Z inside the handler) served it at 15:56Z. No hand re-run was made.
  - The served `characteristics.json` is as_of 2026-10-13 from the T-1 input (`prev_trading_day(2026-10-13)` = 2026-10-12).
  - That is the absent-then-arrival arm, exercised by the world rather than simulated.
- **The two arms the CVO lists as owed are NOT waited on:**
  - the HOLDINGS-NOT-FINAL arm at the 2026-10-14 00:55Z fire;
  - a live PARTITION-ABSENT fire.
  Both branches are proven by the gate's arms A to L, and the live absent-then-arrival path ran today. Each is read when it occurs, as an ORGANIC NEGATIVE ARM (the round-3
  D1-W8-S1 pattern). `2.0.0_SA_COO~G1`'s ledger L6 records the 00:55Z read; no outcome is gated on it.

## 2. Rows graduated to this seat: rulings

- **D1-W14-S2, the SDD session's restore act.** The census named `SchwabSddCapture` as the act that refills the SI2 session. That capture writes Secrets Manager
  `schwab/sdd/session`, but the puller reads Credential Manager `SDDSecure` (`infra/aws/ec2/canonical-schwab-si2/sdd-daily-pull.ps1:229`), and no in-repo code writes
  `SDDSecure`. **RULING:** the census row is WRONG as written. Round 5 item 2 reads, from the code and the box, what `SDDSecure` holds and who writes it, then does one of:
  - (a) names the human act on the SI2 box that restores it (the puller's own text at :270-272 says a human re-establishes the session), with the person and the trigger, as a
    NAMED-REASON row; or
  - (b) repoints the puller to the session the capture already writes, under a pair, if the two hold the same thing.
  No new credential path is built.
- **D1-W14-S3, the ASTN FT leg's missed day.**
  - `tools/astn_wsjft/scripts/run.py` keeps only articles under 12 hours old (:88, :144), and a failed FT fetch is a warning with no retry (:133).
  - So a missed 3 AM run is never refilled, and the census's NAMED-REASON premise ("the next run reads the new cookie") is wrong.
  - **RULING: RE-ATTEMPT-DESIGNED is accepted, and round 5 item 1 builds it:**
    - a same-day re-attempt of a failed FT fetch, in FWD-1's pattern;
    - the freshness window widened only to "since the last successful run", never a fixed longer window;
    - sends de-duplicated by article id, so a refill never re-sends an article already sent.
  - Negative arm: a day whose fetch succeeded no-ops. FWD-6 grades REALIZED on this cell.
- **D1-W14-S4, the stale transcripts header.** `infra/aws/terraform/transcripts/pull.tf:1-3` says "DESIRED ONLY, never applied", but `teams-global-transcripts-pull-hourly` and
  `outlook-global-transcripts-pull-daily` are live and ENABLED. **RULING:** a comment-only correction to the header, naming the live rules and their read date. Its proof is a
  `safe-apply` PLAN reading no change. It is round 5 item 3, with the transcripts project's owner copied on the commit.

## 3. ENRICHMENT LIST (round 5, ONE issuance by `2.0.0_SA_COO~G1`)

1. **The ASTN FT re-attempt** (D1-W14-S3): the arms above. It closes FWD-6.
2. **The SDD session's restore act** (D1-W14-S2): (a) or (b) above, from the code and the box.
3. **The transcripts header correction** (D1-W14-S4): comment only, with a plan that reads no change.
4. **Recorded, not waited on:** the 00:55Z HOLDINGS-NOT-FINAL read, and D1-W8-S1's first live failed read.

## 4. ACTS ONLY ANDREW CAN DO (cited)

None yet. If item 2 reads (a) and the restore is a Schwab login, that login is a person's act at the SI2 box. The round names the person, and it goes on this list only if
that person is Andrew.

-- 1.0.0_SA_CTO~DELL1
