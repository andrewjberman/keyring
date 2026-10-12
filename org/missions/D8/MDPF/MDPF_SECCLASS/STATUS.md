# MDPF_SECCLASS -- one canonical security classification -- status

Seat `2.0.0_SA_COO~M1` (dell1), successor to `2.0.0_SA_COO~M`. Contract `org/standards/MDPF_SECCLASS_CONTRACT.json`. Lease **FULL**
(`drive-mode.py read`); `/canonical-drive` armed at 60m (Andrew-direct 2026-10-10 ~23:3xZ). As of **2026-10-12 ~09:4xZ** (each table row carries its own measure time).
History is in git and the drive logs (`org/tier1_exec/2.0.0_SA_COO~M1/drive_log_*Z_*.md`).

Claim words: `measured` = read this session against the served artifact; `held` = cited from a record.

## Live thread (FWD-1)

| Surface | State | Claim |
|---|---|---|
| Investor Reporting Holdings | live since 2026-09-30 | held |
| Black Diamond firm Mix (Advisor Intelligence) | six classes + one `Unclassified` line; Unclassified 972,621.40 (0.048 pct) at data_as_of 2026-10-08; the 23 ticker-no-row securities ($966,285) still sit in it (row D1-S26) | measured 02:4xZ |
| Cottonwood firm / clients | four clients' latest point sums to 1; no multi_asset class served; firm_composition gap $0.01 | measured 02:5xZ |
| Cottonwood NAME:: placement (e84) | 1,061 positions ($17.32M) placed, none outside the six; firm unclassified 65.2M vs the 84.3M baseline | measured 02:4xZ |

## Deploy ledgers

All MDPF_SECCLASS ledgers are CLOSED except one (HELD):

| Ledger | State |
|---|---|
| e87b BD three-file ship (SC1) | CLOSED 2026-10-12 06:4xZ, leg G NOT MET: shipped as signed (06:20Z, `E87-SHIPPED ok=True`, ETags = signed digests) but D_04's served `mix_summary.json` Unclassified is unchanged at the same as-of (2026-10-09, identical firm total): $1,846,332.73 before the ship, after the 00:18Z `bd-gold-trigger` run and after the 04:00:46Z nightly fire, equal to the cent. D_03's `firm_composition.json` did move (92 / $3,325,002.64 -> 66 / $2,760,199.32). Cause (code at HEAD): C_06 is incremental and `reclassify_retained` (:274-311) skips retained `unclassified` holdings; D_04 reads C_06's snapshot (:486). Row D1-S30 |
| e57e61 FWD-10 apply (~S) | HELD on the first scheduled new-security run that plans US stocks |
| e60 D_04 Unclassified line | CLOSED (SC1): AC1 ok, arm 2 closed as non-e60 drift by the CTO (ADDENDUM 1 @4cac828d3c) |
| e79 BD lib ship | CLOSED, leg G NOT MET: the lib is inert on the served path (row D1-S26) |
| e84 COT NAME:: port | CLOSED, leg G PASS |
| remap-b (33 multi_asset rows) | CLOSED, leg G PASS |

## Open findings

- **D1-S26:** the three BD classify sites (D_04, C_06, D_03) called `classify_with_identity` with an empty ticker only, so e79's
  ticker-no-row branch never ran. FIXED IN CODE by round 20's SC-e-87 (23 of 23 placed, $966,285.46 on the live table, CVO's own
  run, ADJUDICATION_v16 D1-C-S2); SHIPPED 06:20Z by `TO-SC-e87b`; leg G NOT MET at D_04 (row D1-S30): the fix reaches D_04 only on a date C_06 builds new.
- **D1-S27:** C_06's firm-daily `total` differs from its class sum by about $128 with a flipping sign; e60's `Unclassified` carries
  it. EXPLAINED by SC-e-88 as 6-decimal share rounding (2026-10-08 reproduces to the cent). Only the owner's acceptability ruling
  is open (remediation owner `1.0.0_SA_CTO~DELL1`).
- **D1-W78-S1** (INERT): the served firm totals for 2026-10-06 and 2026-10-07 do not reproduce from the current partitions
  (partitions rewritten 2026-10-10 23:15Z, after the 05:26Z snapshot); cause not traced.

## Next, in order

1. **Round 21 is EXECUTING** (one issuance `2f215ca75a`, 2026-10-12 ~09:4xZ, on the CTO's round-20 analysis @e5adc667e2, msg 4321; `dep_stage` EXECUTING; fanout 5 of 5, cap 8). Round 20 stays graded MAY-CLOSE (CVO L9 @eb33d5d466; `TO-SC-e87b` terminal, leg G NOT MET). DECOMP `decompositions/MDPF_SECCLASS_DECOMP_R21.md`.
   | cell | what | risk | slot | state |
   |---|---|---|---|---|
   | `SC-e-91` | C_06 retained pass revisits retained `unclassified` holdings on every fire (also with no new partition); firm and advisor snapshots follow; never-widen half request, both halves unsigned (row D1-S30) | SERVED | ~80 `worker` | built, AC1-AC3 re-run by me; reopened by amendment 1: the half request must state its REACH (row D1-W80-S4: the revisit only sees each date's stored top-10 holdings) |
   | `SC-e-92` | cross-box deploy check: trunk-first sentinel status; a vanished worktree is not a hit; a branch-only sentinel still hits (row D1-S28) | LOCAL | ~81 `worker` | DRAINED 8d755a8491 after amendment 1 (row D1-W81-S2: a vanished worktree is read through its branch ref); AC1-AC4 re-run by me |
   | `SC-e-93` | read: served BD positions with the literal ticker NAN / NONE, denominator printed (row D1-W77-S1) | LOCAL | ~82 `worker-light` | DRAINED 97ca96b08f: NOT_EXPOSED (0 NAN/NONE of 114,554 positions at 2026-10-09; 225 null market values) |
   | `SC-e-94` | read: the writer of the 2026-10-06/07 holdings partition rewrite at 2026-10-10T23:15Z, writer count, whether C_06 re-serves those dates (row D1-W78-S1) | LOCAL | ~83 `worker-light` | DRAINED 81cfb83df2: writer `B_00.canonical_holdings` (run 608de09d26a6), writer_count 1; the 23:15Z rewrite re-put identical bytes, the content moved 10-11T04:16:35Z and 10-12T00:33:48Z; the next default C_06 fire re-serves none of 10-06/07/08 |
   | `SC-e-90` | portal test `iv-e-46.class-readers.test.ts` locates each named reader by content, plus a negative arm (CTO msg 4167); direct act, portal worktree at origin/DEV `62507dae67` | LOCAL | ~84 `worker-light` | DRAINED 4ff03e1393; portal test commit 64d8c6de38 on origin/DEV (ls-remote, fast-forward from 62507dae67, test file only; AC1 3 pass, AC2 1 pass, re-run by me) |
   - **Carried, not a cell:** leg G of SC-e-87 and D1-S30, read on the first post-ship as_of (Tuesday 2026-10-13's fire or later), the expected
     figure stated at THAT as-of, never at 10-08. SC-e-91 must also ship (a pair-gated act by a CloudOps lane) before that read can pass.
   - Drain per chain end (`/dispatch` Step 5), then the real run of each outcome, the L8 packet to the CVO, the `round-close-check`.
2. **e57e61:** release when a scheduled new-security run plans US stocks.
3. **p1 residue** (11 keys outside FWD-15's plan): waits on a ruling.
4. **IB-pr-417:** the COO half on the e56 member is SIGNED (@ced2704270, due Mon 2026-10-12 13:00Z at dell2); push of that commit
   is the box-sync's.
