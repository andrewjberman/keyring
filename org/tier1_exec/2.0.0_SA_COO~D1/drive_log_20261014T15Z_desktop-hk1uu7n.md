# 2.0.0_SA_COO~D1 -- /canonical-drive log, hours 2026-10-14T11Z-T15Z (host desktop-hk1uu7n)

Project MDPF_CANON, cron `34eb9ad0` hourly at :23, lease FULL, empty_tick=on. Preceding: `drive_log_20261014T05Z_desktop-hk1uu7n.md`.

## 11Z-13Z: the dated wait on the fold's first scheduled fire
Seat re-seated after the reboot (watcher armed, cron re-armed). Ticks 11:06Z, 11:29Z and 12:29Z were empty ticks recorded as a dated wait on the 2026-10-14 13:30Z fire (`WAITING DATED`, empty=0).
Mail acted on: msg 5488 (the CLAUDE.md Portal law edit, `fcdfc34843`: portal DEV only through `portal-merge-forward.sh` on an approved row), acked; no Tier-2 seat under this lane to tell.

## 13:41Z: the fold's first fire read, and the round-6 packet
`r6_fold_readback.py` 9 of 9 arms, `r4_daily.py` 4 of 4 (global 2026-10-13, manifest `20261014T133149Z.json`, code `51cfc93ea8`). Packet `round6/ROUND6_DRAIN_END.md` (`e647498179`) to the CVO and `1.0.0_SA_CTO~DELL1`.
One defect of mine, recorded in decomposition v7: the packet's `/portfolios` line "Total Holdings 8,607 -> 8,607" was a wrong-date read (the account-distribution is keyed by the run date, 2026-10-14; I passed the frontier date). The CTO's -177 (8,430) stands; row D1-S24, repaired by CN-k-1.

## 13:54Z: the round-6 analysis in hand -> ONE issuance, round 7
CTO analysis `65bf603a7a` (msg 5589; AC4 MET, FWD-3 REALIZED). Four forks drafted the cells with no staged draft (CN-k-1, CN-l-1, CN-m-1, CN-n-1) and a fifth CN-l-2; decomposition v7 and eight orders: `879feb7e99`, merged `7df957722b`; `fanout: 7 of 7 chains, cap 8`; every check dry-run at the base. The first commit attempts were refused while another seat held a merge open in the shared tree, so the issuance went through a linked worktree and `safe-merge.sh`; two lint findings in the forks' check files were fixed first.

## 14:34Z-15:35Z: the drain
Merged: CN-l-1 `72ef4f8a3a`, CN-k-1 `be1fb86ee4`, CN-j-1 `1c8ebf3e5d`, CN-i-1 outer `0da4e7a7df`, CN-m-1 `6ad2e97350`, CN-l-2 `cb9836f2c1`, CN-n-1 `edd4f4f2f6`, CN-h-1 `9592daf75c`; each instance graded VALID by `proof-of-spec-check.py` and the cell's checks re-run on the merged tree.
- CN-n-1 took four seats. The cause each time was the issuer's instrument, not the guard: the plant edited artifacts in place (S1), blanked a value beside a count the Global builder re-sets (S4, S5), then sat inside the builder where the composition gate runs first (S6). Amendments `8237f981c8`, `25f5cecb74`, `2a6c586f88`; the fourth run refuses Global whole with the `GLOBAL MIN-FIRMS FOLD REFUSED:` prefix, writes 0, 2886 served object-versions identical.
- CN-h-1 was blocked by the naming gate (row W17-S3): call f6f8 to the CTO, cross-box XA-c328, route a `legacy_addresses.json` row (`81453d51cf`); amendment `7c5fff2765` also adds the package-list line, because `legacy_address` raises when the registry file is absent from the gold package; seams arm S5 corrected for the docstring (`fix` commit).
- Worker `~20` reported that it had seen the issuer's pre-read; it sat in the order's record face and was seen only by opening the order to flip its status; its counts differ from the pre-read.
- Hygiene: gold and canon suites 163 passed, 3 failed; the same 3 fail on a detached checkout of `7df957722b` (row D1-S1).
- The real run of the portal cells: `/ui-walk` on the candidate (Snapshot and Trend); screenshots local only.

## 15:36Z-15:40Z: L8 and the approval
`round-close-check.py --round 7`: 8 of 8 complete, 5 JUDGMENT ungraded, REFUSED. Packet `round7/ROUND7_DRAIN_END.md` (`238fa48e78`) READ by the CVO (msg 5631). All round-7 commits are on origin `box/dell1` (read with ls-remote, `e4f3097ae4`).
Portal candidate `cand/dell1/mdpf-canon-aua-trend-groups-and-as-of` @34cd12d2 registered as a client-facing approval call (check-only OK; scope OWN-BOX); not landed.
In progress at the time of this log: two forks drafting the never-widen pairs and CloudOps orders (gold package for CN-h-1 and CN-l-1; publisher for CN-j-1).

## Compiler Tools
Run: `comp-find` (script locations), `comp-surprise --armed` (5 ARMED rows read), `to-check`-class reads via `round-close-check.py`, `proof-of-spec-check.py`, `unblock.py tick`, `open-calls.py add --kind approval`, `drive-mode.py read`. Worked: all; the comp rail denied four blind searches and each was rerun as the tool it named. Failed: none. Gaps: `comp-surprise` offers no per-row disarm view, so the disarm standing of W16-S5 is read from the rows themselves.
