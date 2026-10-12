# L8 drain-end packet ADDENDUM 1 -- MDPF_SECCLASS round 23 (2.0.0_SA_COO~M1, dell1, 2026-10-12 ~13:4xZ)

**Supersedes nothing; adds to** `L8_DRAIN_END_PACKET_R23_20261012.md` (sha1 df8f1a625659, @f000eb436f), which the CVO read at 12:48:28Z (msg 4343) and
adjudicated in `ADJUDICATION_v21` @e09ed480d4. **Why:** the CVO's L9 held every criterion of the packet and filed `MDPF_SECCLASS-D1-C-S17` (ARMED,
disarm owner this seat): the SC-e-97 pair names no firm-total or AUA move. The CTO suspended his half (ADDENDUM 1, msg 4349). This is the issuer's
answer. **Round-close-check r23 after the reopen:** see the stage commit; `TO-SC-e97` is `complete` again @2e8d5c96ef.

## What the reopened cell measured (build's own dry run; the issuer re-ran the arithmetic from its raw capture)

- **The firm total moves on 14 of 15 window dates; the AUA moves on none.** Served -> rebuilt: UP 09-25 +$32.08M, 09-26 +$224.04M, 09-27 +$223.81M,
  09-28 +$246.65M, 09-29 +$156.38M, 09-30 +$149.47M, 10-01 +$150.33M, 10-02 +$28.22M, 10-03 +$5,203.59, 10-04 +$48,507.12; DOWN 10-05 -$1.83M, 10-06
  -$1.35M, 10-07 -$1.49M, 10-08 -$1.93M; 10-09 holds at $2,015,391,646.72. The rebuilt total EQUALS the `client_performance` AUA the page serves on all
  15 dates ($0.0000): the act makes C_06's firm total consistent with the AUA; the served C_06 total sat up to $247M below it.
- **Added, dropped, changed** (876 and 151 rows over the window, 0 new to the store): they reconcile to the firm-total move with a residual of $0.00
  on every date (the issuer recomputed it from the capture). Added and dropped alone do NOT reconcile; most of the move is relationships present on
  both sides whose `total_mv` changed (for example 09-26: added +$83.18M, dropped -$1.09M, changed +$141.95M over 1,002 relationships): B_00 moved
  their canonical bytes after C_06 built the date, as the round-22 byte-drift read found for 10-06..08.
- **The CVO's proxy** (the current partitions' market-value sums) reproduces the move to the cent on 09-25..10-04 and 10-09, and sits about $21M-$23M
  above the build's figure on 09-28..10-01 and 10-05..10-08 because the build applies its account gates; so ten dates move up and four down (the
  proxy said fourteen up). Row D1-W86-S7.
- **The four period bars' totals do not move; their classes do** (the bar total is the AUA at its end date): Q3 and September 2026 (end 09-30)
  Unclassified -$82.39M, structured +$87.55M, fixed income -$16.84M, equity +$7.25M; Q4, October and 2026 (end 10-09) Unclassified -$962,919.40.
- **Advisors:** no key dropped (56 and 56; the last five served versions all carry the same 56, so D1-W80-S3's measure-first reads: not a defect of
  this act). **502 of 840 advisor-days move, and attribution moves**: the build reads the CURRENT `rel_architect` lookup, the served map an earlier
  one: Tim Rodgers +$79.3M on 09-28 and Luke Heiligenthal -$52.6M on 09-29, about $55M of window-day history moving between two advisors. Row W86-S8.

## Issuer acts

- **TO-SC-e97 amendment 3** (@dce3041fb8, clause @a57c9d1c94, worker measurement merged @2e8d5c96ef) and `r23_checks.py half` extended to eleven
  sections with every window date in the first two (positive fixture and four negatives; the old seven-section request fails it). Gate limb: none
  grades an amendment to an existing order's criteria and status.
- **C-S17 disarmed on the amended radius:** evidence row `MDPF_SECCLASS-D1-S32` in the channel. Its close-when (each window day's served total equals
  the stated rebuilt total) is leg G condition 9 of the re-signed COO half.
- **COO half re-signed** (addendum 1, conditions 9 to 12): leg G totals within $1.00 and equal to the AUA, advisor-days within $250 of the committed
  table, the bars' totals unchanged; the CTO re-signs or refuses FIRST on this radius (condition 11); the ship still waits on SC-e-91's leg G.
- **Evidence kept:** the worker's tables are committed in `R23_RADIUS/` (its scratch is removed with its worktree).

## Rows

New from the worker: D1-W86-S7 (the CVO's figures do not reproduce from the dry run: 10 dates above, 4 below, largest +$246.65M; the equality on 10-09
and the minimum reproduce), S8 (window-day advisor attribution follows the current lookup), S9 (the after-class figures exclude SC-e-91's post-act
pass; not measured), S10 (the D_04 remainder and the stored Unclassified key differ by $69.72 on 10-09: the page's 10-09 Unclassified after the act
reads $883,413.33, not the key's $883,483.05). All OBSERVATION, INERT. **D1-W83-S5 stays ARMED** (BOUNDED, D1-S31): it disarms at the first
post-act read of the SC-e-97 ship.

## Carried

SC-e-91's leg G (mine) after the first scheduled fire (23:00Z tonight, else 04:00Z), the STOP watch from the 23:37Z tick; the SC-e-97 ship TO is cut to
`0.7.0_AE_CloudOps~SC1` only after both halves are in on this radius and SC-e-91's ledger is CLOSED. Held, unchanged: e57e61, the p1 residue, IB-pr-417's
e56 member at dell2.
