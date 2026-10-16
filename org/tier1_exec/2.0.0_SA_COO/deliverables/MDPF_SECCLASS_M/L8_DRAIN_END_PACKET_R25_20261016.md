# L8 drain-end packet -- MDPF_SECCLASS round 25 (2.0.0_SA_COO~M1, dell1, 2026-10-16 ~03:2xZ)

**For:** 3.0.0_SA_CVO (and the record for 1.0.0_SA_CTO~DELL1). **Decomposition:** `org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R25.md`.
**Issuance:** @3e1365fdaa (`fanout: 2 of 2 chains, cap 8`), on the CTO round-24 analysis (msg 5506, `94da0b08da`). **Round-close check:**
`round-close-check.py --project MDPF_SECCLASS --round 25`: `orders=19 judgment=0 verdict=MAY-CLOSE` (15 complete, proofs 15/15; one not complete and outside the verdict:
TO-DEPLOY-e57e61, hold stated below). Claim words: `measured` = read this session against the served artifact; `held` = cited from a record.

| cell | order | slot | risk | drained | criteria (issuer re-run at trunk) |
|---|---|---|---|---|---|
| SC-e-101 | TO-SC-e101 | ~91 | LOCAL, direct act | @b5f6b816a4 | `R25_CHECKS/r25_rebase_read.py` capture/read/selftest; baseline captured 2026-10-14T12:33Z (15 dates, 56 advisors, 5 bars) |
| SC-e-102 | TO-SC-e102 (ship `TO-SC-e102b`, SC1) | ~92 | SERVED | @ee2cbf1023 | C_06 `_write_mix_summary` `sort_keys=True` plus a test (AC1 7 passed, AC2 30 passed) |

## What the round established (measured unless marked)

- **FWD-1 REALIZED WHOLE** (CVO `ADJUDICATION_v24.md`, row D1-C-S25, @72faa70f49, 2026-10-14 12:58Z): the Positioning limb read (`POSITIONING_LIMB_READ_20261014.md`) and the BD page half. The first FWD to grade REALIZED.
- **Re-base read after the 23:00Z fire of 10-14** (`FIRE_READ_20261014_2300Z.md`): raw `R25-REBASE ok=False` on classes and bars because that fire was the first run of DB-b-183's FDRXX -> cash classifier ($18.2M-$20.6M `fixed_income` -> `cash` on all 15 dates, equal and opposite within $110, AUA conserved); netted read 15 of 15 dates and 5 of 5 bars; totals, advisors, s27 (max $165.09) and restated pass raw. The transfer's identity is DB-b-183's L3, not graded here.
- **SC-e-102 SHIPPED 2026-10-15 06:47:09Z; Branch 1 MET** (`E102_BRANCH1_READ_20261015.md`): C_06 `f884f28d` = repo md5; `mix_daily_summary.json` ETag `6e8ac834` -> `10d0a665` with canonical-JSON equality, body equals its own sorted dump (negative control: the pre body does not), run 2 ETag unchanged. Ledger `secclass-e102-c06-sorted-keys-sc1-20261015` CLOSED. Leg P counts 59 advisor files, not the 56 the request wrote.
- **Leg G MET on the first scheduled fire after the ship** (launch 2026-10-15T23:00:11Z; `LEGG_E102_READ_20261016.md`, instrument `R25_CHECKS/r25_legg_read.py`, commit @7ea7734eaf): canonical-JSON equality on 2,293 of 2,297 firm dates in `mix_daily_summary.json` and `firm_mix_views_daily.json` and on 49 of 56 moved advisor files; the rest differ only on 10-10..10-13, inside the 09-29..10-13 re-derive window; sorted bytes on `mix_daily_summary`, `firm_mix_views_daily` (+ alias) and 56 of 56 moved advisor files; D_04's composition total equals its same-order recompute pre and post (`2024173838.39`, `2024164661.27`, diff 0.000000). Rows: D1-W92-S2 DISARMED (D1-S40), D1-W92-S3 INERT and not realised.
- **D1-S27 accepted as rounding** with a $1,000-per-firm-date bound (max read $165.09).

## Not shown

The cause of the 10-10..10-13 content move in the 10-15 fire (a data change on re-derived dates, not graded); the chain's launch-to-stop runtime for that fire (stop instant unmeasured); production-fire idempotence beyond this fire; that no consumer keys on `mix_daily_summary.json`'s ETag. The 3 advisor files with no D_03 write since the ship (`abby_horton`, `erick_webb`, `sydney_cobb`) carry no entry in the served summary and are stale, not live.

## e57e61 (held, restated)

`TO-DEPLOY-e57e61` (FWD-10 producer apply) was APPLIED and proven 2026-10-08; its L3 verification waits on a scheduled new-security run that plans US stocks. The 10-14 14:00Z run planned 0. If no scheduled run plans one by the 10-20 14:00Z run, it is cut as a round-26 seeded exercise (CTO msg 5510). Outside the verdict.

## The 17-FWD board (denominator 17 of 17)

FWD-1 REALIZED (above, CVO). The other 16 are exactly as printed in `L8_DRAIN_END_PACKET_R24_20261014.md` section "The 17-FWD board": every state word `held` from a record older than round 20; this round did not re-exercise them and claims none REALIZED. Under the PIVOT DIRECTION no seat is added to the non-BD FWDs this week.

## Owed at the round-26 recut (on the CTO's round-25 analysis)

The 4 seed rows HPI, CUBE, GLPI, PCEF under a never-widen pair (this project is the list's writer, PRD C-WRITER; CTO msg 5510); the DEMQUE<->SECCLASS sync cell (classify the 23 of 131 landed DEMQUE fund names with no `etf-classifications` row on the scheduled path and prove one end to end; state how a CUSIP-only security keys into a ticker-hashed table, C-DEMQUE-SECCLASS-SYNC); e57e61's run date. Open at Andrew: the client-facing Black Diamond Mix restated-history PROD push (approval for e97's served BD Mix data consumed, `BD_MIX_PROD_PUSH_APPROVAL_CONSUMED_20261015.md`).
