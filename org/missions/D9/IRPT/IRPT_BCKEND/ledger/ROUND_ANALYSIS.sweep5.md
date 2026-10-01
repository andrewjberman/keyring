# IRPT_BCKEND sweep 5 -- the CTO's L10 analysis

**Author:** 1.0.0_SA_CTO, 2026-10-01 ~03:4xZ (first session after the reboot). **Input:** `3.0.0_SA_CVO`'s slug 103404 and
`org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_SWEEP5_REVIEW_20260930.md` @0592ab79d8 (ADJUDICATION_v19, REMEDIATION_v15).
**Read with:** `ROUND_ANALYSIS.round26P.md` @7c9ed807bb, which ruled six of these rows conditionally before the slug arrived, and
`2.0.0_SA_COO~P`'s round-27 results (drains 934c157f17, 690409234b, cc20caf7b8; session log @accb783b6d), which measured the
conditions. This file closes those conditions; it does not repeat the round-26 text. Channel row: `IRPT_BCKEND-S242`.

## 1. Rows this seat owns, ruled

| row | ruling | state after |
|---|---|---|
| W86-S1 | **DISARMED stands; the compile's objection is answered, not overruled.** 103088 tied W86-S1 and S216 to one per-account read. Round 26 split them on new evidence: run `chain_full_20260930_145412` passes step 3 and landed raw for 09-30, which is W86-S1's own mechanism (the missing `silver_ids` import). The per-account read past 09-27 is S216's condition alone. This sentence is the amendment to 103088 that REMEDIATION_v14 did not have. | W86-S1 closed; S216 ARMED |
| W97-S3 | **Branch A is measured** (pr-272: one client, household 63; Orion re-typed four transaction ids to internal journals). The round-26 ruling applies as written: a never-widen packet of the three literal keys (866, 769, 1096; partition 2026-09-24), before and after values, rollback by re-emitting the prior values; this seat signs on read. The packet is NOT written (~P log, next step 3). The guard is never disabled. | ARMED; next act ~P |
| S237, S239 | **Placed:** ADVI_PERFRP, cut by base `2.0.0_SA_COO`, under both halves. Record `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_DECISION_20261001_034xZ_S237_PERFRP_REMEDY_ROUTE.md` @8729d9792c. pr-273 measured that the error does NOT reach the IRPT adapter (it reads the holdings gold only) and DOES reach the ADVI perfrp account leaf, which is served (row W100-S2: 200 three times, two clients). S239's period reader has no separate owner: the same cell names the leaf and `parity_period_returns.py`. | ARMED; parked on Andrew's D2 hold |
| S235 | **DISARMED on this seat's read (~03:40Z):** `opal-data-assets` `schwab/08335338/silver/dim_position/date=2026-09-29/data.parquet` exists, LastModified 2026-09-30T21:46:40Z -- 12 hours past the feed's hour, and after the compile's 19:1xZ read. The late landing's CAUSE is unread and stays with TO-IB-pr-274 (parked on `0.6.2_AE_PartnerETL~C`, dark). What remains is a different defect, ruled in section 2 item 3. | S235 closed; pr-274 parked |
| S236 | **No new status value.** The 4,074 rows of date=2024-07-08 keep `REFUSED-NO-BMV`: it is true (no BMV exists) and it refuses, so no figure is served. `NO-PRIOR-TRADING-DAY` is a new enum member on an engine retired for serving; it arrives with a rule-24 record or not at all. TO-IB-pr-263 stays superseded. | S236 closed |
| S232 | Unchanged: disarms when the first job accepted under `svc-irpt-analysis` reaches a terminal state. That job waits on W27, which waits on IB-pr-275. | ARMED |
| S233 | **Ruled as far as the estate can answer.** The Analysis capture keeps its own web-app session: its deliverable is a rendered export and no REST equivalent is known. Everything with a REST endpoint stays on the gateway's shared session. Two facts decide whether the layers can merge -- whether YCharts publishes a report or export endpoint, and whether one account holds two sessions without eviction -- and both are vendor probes that need Andrew's per-use word. Until then ~Y names S230's 03:36Z cause from the ordinary job path only. | ARMED; the probe is listed for Andrew |
| W97-S2 | **No gate change.** `halt-gate-check.sh` already admits a worker and scans its ISSUER's inbox (`:157-198`, `:342-349`). `HALT_ACK=1` is the gate's own routine-ack path (`:463-466`), not an override; `HALT_OVERRIDE` is the override and stays outside every worker grant. Issuer rule: a worker face whose cell runs `safe-deploy` or `safe-apply` writes the invocation with `HALT_ACK=1` allowed when the print holds zero `[STOP]` lines, and never writes a raw `aws s3 cp` fallback, which skips the per-file SHA check and the S3-membership guard. | W97-S2 closed |
| S238 (disarm owner) | Unchanged: disarms on this seat's read of both prints (a foreign firm refused, the own firm 200) after the served move. pr-271 is on CLOUD and is NOT served; IB-pr-275 is prepped on `coo-p-pr275` @b217896d65, unmerged. See section 2 item 1. | ARMED |

## 2. Rulings for the next issuances

1. **IB-pr-275, order inside the window: the five `opal-users-v2` read grants apply and are simulated BEFORE any function's code
   moves.** ~P measured that six of seven roles cannot read the profile table and that the new boundary fails closed without it, so
   code-first refuses every service principal, its allowed firm included. The packet names six functions, five grants, `irpt-narrative`
   excluded, and both branches of the fail-closed read; each grant goes through `safe-apply`.
2. **The NNA Branch A packet (W97-S3)** is ~P's, as above. While the guard holds, INF_C_02..INF_D_11 do not run.
3. **49 Financial holdings gold for 2026-09-29: one catch-up fire.** The producer computes one day per fire and never revisits a
   missed day; the 09-30 fire refused ABSENT and the silver landed ten hours later, so the 09-29 partition is absent unless it is run
   (inferred from the schedule; the gold prefix was not re-read here). Cell for ~P: first read whether the producer accepts an as-of
   date; if it does, one fire for 2026-09-29 through the producer's own path. It mints a partition the adapter serves and it runs the
   producer off its own clock, so it carries both halves naming that one key and that manual state. If no date input exists, the gap is
   declared on the page under PRD ruling 18 and the input is its own cell.
4. **The five ~M Holdings orders still `pending` at HEAD (Q3): RE-CUT, not drained and not retired.** Read at HEAD: m22-222 is
   already `superseded` (@3412dc5bbe); m25-251, m26-261, m27-271, m27-272, m28-281 read `pending` on CLOUD and `complete` only on
   `wk-IRPT_BCKEND-84` (12 commits ahead of CLOUD, built before IB-mr-291 changed the same files). ~M flips all five to `superseded`
   with a pointer each: m25-251 to IB-mr-291 (@9fef6a7e9c, the served class source); m28-281 to the narrowed release half; m26-261,
   m27-271, m27-272 to the round-30 cells that port their content onto the 291 base. The branch ref `wk-IRPT_BCKEND-84` is kept
   until those cells drain (it is their source); the worktree may go. HOLD 103137 is unchanged for a table-only class source.
5. **A pass count is not a handler count (Q4).** W91-S2's cell is graded on two prints of `pytest -s test_seam_paired.py`: zero
   `ROUTE_NO_HANDLER` lines, and 12 of 12 operations reaching a handler. Any later cell that cites the seam suite cites both.
6. **W93-S1:** no contract addendum; `class_source` stays in the producer's census (C-S263 accepted).

## 3. Outcome read

No FWD is REALIZED by sweep 5. Round 27 (~P) is drained and NOT closed: IB-pr-275 is open, pr-274 is parked, and no drain-end record
or slug exists. At 03:30Z none of `2.0.0_SA_COO~P`, `~M`, `~Y` has a live session (live seats: 4, none a COO), so every act below
waits on a relaunch; the LIVE_ARMS RELAUNCH row is the authority and the arm is operator-initiated.

## 4. Enrichment

- **~P, round 27 close then round 28:** IB-pr-275 with the grant-first order (item 1); the NNA packet (item 2); the 09-29 catch-up
  cell (item 3); the W99-S3 and mirror re-time routing this seat has not yet received; carried S216, S132, W86-S2's observation.
- **~M, round 30:** the five flips and the three port cells (item 4); the one-window release's H5 read at the 2026-10-01 14:15Z
  `irpt-holdings-snapshot` fire; MDPF_SECCLASS BD_THREAD_R3 is signed (@8769ffe8d5) and waits on a gap that meets its invariants.
- **~Y, round 30:** REMEDIATION_v15's six graduated rows as owned there, W91-S2 graded per item 5, S229-S231 unchanged.

## 5. Waiting on Andrew (three, none new except the last)

1. The D2 hold on ADVI_PERFRP: lift it for the perfrp-leaf remedy cell, yes or no (recommended: yes, scoped to that cell).
2. The DB-b-1 method review he is running with `0.4.0_DS_ClientPlatform~S` (IRPT_DASHBD; not this project's).
3. A per-use word for one YCharts probe (does a report or export endpoint exist; does one account hold two sessions), or a no.

-- 1.0.0_SA_CTO
