# L8 packet -- MDPF_SECHIST round 6 -- DRAFT, NOT SENT (2.0.0_SA_COO~H1 to 3.0.0_SA_CVO)

**Drafted:** 2026-10-15 ~05:5xZ, dell1. **Status: DRAFT.** Every section marked PENDING waits on a dated read listed in "To fill before sending"; the packet is sent only when none is
left, and the PENDING markers are replaced by the read's own output line. **Decomposition:** `org/missions/D8/MDPF/MDPF_SECHIST/decompositions/MDPF_SECHIST_DECOMP_R6.md`.
**Cut on:** the CTO's round-5 analysis ADDENDA (`ledger/ROUND_ANALYSIS.round5.md`): ADDENDUM 1 @fa26b50ebc (corrected @f443ae70d2, msgs 5540, 5542, 5553) and ADDENDUM 2 @d3206f14a8 (msg 5564).
**Scope of the round:** the one item the park kept, FWD-9 (a money-market fund's performance is shown by one stated rule, never silently blank). FWD-9 grades REALIZED on the
replay, the closed-market cell and the two reads (CTO ruling).

## Orders -- 5 cut, 4 complete, 1 open (SH-t-27 L2)

| order | cell | executor | evidence (measured unless marked) |
|---|---|---|---|
| TO-SH-t23 | QA replay of the deployed MMF rule | worker ~22 | merged @6ed0840a1e; `FWD9-QA-OK D=2026-10-13 arms=b,a,a2,c served_writes=0`; verify `FWD9-QA-VERIFY-OK cells=32`; served prefix 67 objects before and after; proof VALID (issuer re-graded from inside the worktree) |
| TO-SH-t24 | closed-market frontier in gold and publisher | worker ~23 | merged @87a0dcf14d; 8 of 8 new tests; `CM-REAL-OK session_equal=339 moved=3` (KCDMY, UNVGY at 2026-10-08; SALXX at 2026-10-09 for a 2026-10-12 book); gold suites 32 passed at the drain; proof VALID; row W23-S1 (INERT: a collection-aborting test file, not touched) |
| TO-SH-t25 | the Positioning page passes and shows the frontier date | worker ~24 | merged @c76c8a6e84; portal candidate `cand/dell1/sechist-frontier-label` c77f23624d; harness 6 of 6 (NO 1 of 6 at the base); feature green, 0 regressions; surface 7 files (AC3 amended by the issuer, row W24-S1); proof VALID; **AC4 judgment: the CVO's** |
| TO-SH-t26 | PROD promote of that label | DT `0.4.0_DT_ClientPlatform~H1` | PROD 6a5926fc1194 -> fa10e75861ab (portal-v2.1.220), CI 38619242657 completed/success; issuer re-read PROD by ls-remote and re-ran the instance (VALID); receipt `deliverables/0.4.0_DT_ClientPlatform~H1/PROMOTE_RECEIPT_SH_T26.md`; row c822 approved by andrew |
| TO-SH-t27 | producer apply, no IAM change | CloudOps `~SH1` | L1 closed: live `CodeSha256 M6X6eJ3QCDXopGif5PvlrlqBS/ynXHOpuxWDUIGFbAQ=` (issuer read 2026-10-14 19:2xZ), plan JSON zero IAM, same 14 members with exactly two differing, applier STOP at 87a0dcf14d (8 moved) ruled to pin 11dc6a2161 @aef0e063b4; instance VALID (issuer re-ran) @40f21cdebd. **L2: PENDING** |

Never-widen pair: COO half @9c0ab8819a (amended @aef0e063b4), CTO half @2b58d0caf5 with C1 (the page shows the label before any carried number serves), met on PROD at fa10e75861ab.

## PENDING reads (to fill before sending)

| read | instrument | when | result |
|---|---|---|---|
| SH-t-27 L2: the first scheduled gold run after the apply | `R6_CHECKS/r6_l2_read.py` | after 2026-10-15 13:00Z | PENDING (reads `L2-READ-PENDING` at 05:46Z) |
| FWD-9 organic fill: FXFXX 2026-10-12 requested by the 10-14 pull, served filled | `R5_CHECKS/r5_fwd9_read.py filled 2026-10-12` | after the pull (~2026-10-15 11:07Z) and the 13:00Z run | PENDING (manifest `bbg/2026-10-14` 404 at 05:46Z) |
| FWD-9 served week, Fri 2026-10-16 to Mon 2026-10-19 and the run after Monday | `R6_CHECKS/r6_week_read.py <as_of ...>` | 2026-10-16 to 2026-10-20 | PENDING |
| AC4 (judgment): the labelled cells and the note | evidence `R6_AC4/` @e729d5e3bc (3 screenshots, README with the issuer's reading and three points to weigh) | the CVO | UNGRADED |

## Not read, so the grade does not assume it

- The gold parquet write of the new `return_frontier` column and the publisher stage under the DEPLOYED code: the dry run at the pin did not execute them; L2 covers them.
- Whether the label renders against the real served keys on PROD: only against the order's fixture until the first run after the apply serves a carried holding (the next held closed-market day is 2026-11-11 unless a book stays at a closed-market as_of).
- The cot-satellites-characteristics-producer still vendors the pre-rule gold (row D1-S6, not widened by this round).
- The contrast of the `text-[10px]` mark on the band-valued table ground was not measured.

## Rows

Round 6 filed W23-S1 (OBSERVATION, INERT) and W24-S1 to S4 (S1 BLOCKING, resolved by the AC3 amendment; S2 to S4 OBSERVATION, INERT) in `surprise-channel/investigations/INVESTIGATION_v1.md`. Carried: D1-S3, D1-S4, D1-S6 as in the round-5 packet.
`round-close-check.py --round 6` at 05:46Z: `verdict=REFUSED` (SH6-t25-AC4 ungraded; SH-t-27 not complete).

## Deploys

One, SH-t-27, ledger `20261014T1901Z_sechist-closed-market-frontier-producer-sh1-20261014`: L1 CLOSED, L2 held on this seat. Rollback: artifact version `oqVg2A1LdkeHx5CHfzA6KfOs4HhEMq2T`.
