# Drive log -- 2.0.0_SA_COO~D -- 2026-10-04 21:35Z to 23:4xZ (host opal_bloomberg)

| time (Z) | project | limb | round | TOs | act |
|---|---|---|---|---|---|
| 21:39-21:47 | DSGN_AMGTV1 | L10 | r35 | -- | The CTO APPROVED d60a0f90 under 4 conditions (@98209ce86a). Condition 1 met: re-merged onto DEV aa373a83 as 35a723bf, battery + 6 checks full (@42ecd20f61). |
| 21:4x-21:58 | DSGN_AMGTV1 | -- | r35 | -- | Andrew's word to MSTR~Z: DEV aa373a83 -> 35a723bf, CI 37237977735 green (msgs 29263/29269). Worktrees 94-96 deleted on Andrew's word: junctions removed first, main node_modules intact (258). |
| 21:5x-22:3x | DSGN_AMGTV1 | L5 | r36 | -- | instrument35 base 0/4 at 35a723bf (948 s); repairs36 authored, base 2/5, green 5/5 (issuer re-runs). CTO msg 29279 / COO~X msg 29293: ModelTab.tsx has a second writer; round 36 touches neither file (ack sent). |
| 22:3x | DSGN_AMGTV1 | L6 | r36 | 0/2 | ISSUED @70d41165c1: AV-zn-1 (~97), AV-zn-2 (~98); fanout 2 of 2, cap 8. |
| 23:0x-23:1x | DSGN_AMGTV1 | L7 | r36 | 2/2 | Drained bd396ef6b8 (after 120 s waiting on CRO~Z's staged deploy entry) and bef3b2d7a7. Candidate cb6772fd = DEV 75efe9d6 + r36: battery ALL PASS, 7 checks full. |
| 23:14-23:31 | DSGN_AMGTV1 | real runs | r36 | -- | FWD-20 instrument on cb6772fd: 4/4, 76 PASS / 0 FAIL; PNGs read. Close walk read-20261004T232007Z (ARMED 23:20:09Z, DISARMED 23:31:15Z): 21/1/1, the FWD-5 tooltip now PASS. |

**State:** candidate portal cb6772fd goes to the CTO's review (ROUND36_CLOSE.md). This close names no new page defect.
