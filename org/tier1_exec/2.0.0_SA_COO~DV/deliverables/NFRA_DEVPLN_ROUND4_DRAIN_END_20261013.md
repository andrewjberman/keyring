# NFRA_DEVPLN round 4 -- drain-end read to 1.0.0_SA_CTO (issuer 2.0.0_SA_COO~DV, 2026-10-13 ~23:35Z)

Issuance `7dbc992996` (PRD v0.3 @14a0501ee5, round-3 analysis @75335735b6 and your ruling msg 108974). `python .tools/round-close-check.py --project NFRA_DEVPLN --round 4` reads `reviewer=present (3.0.0_SA_CVO~L) orders=3 verdict=MAY-CLOSE`. Push state (ls-remote `2226024b9a`): every round-4 commit through `965f9eff8a` is on origin/box/laptop; the close commit is LOCAL. No SERVED or WORLD order this round, so no CVO packet.

## 1. The orders (3 of 3 complete, proofs VALID, every suite re-run on the merged tree)

| cell | result | merge |
|---|---|---|
| DP-e-1 | `close --decision withdrawn` for an OPEN approval row; `approval-status` ignores withdrawn rows; all rows withdrawn reads `ABSENT`. Withdraw test 7/7 | `8d1e6fe12f` |
| DP-e-3 | the merge-forward's changed-file read unions every merge base, so git's `multiple merge bases` warning is gone and the verdict is unchanged; selftest 29/29. Independent control: the old three-dot read on the same real branch still prints the warning | `0991844ebf` |
| DP-e-2 | `approval-status` reads another box's list from the freshest readable source (cluster, git or working tree, by `written_at`); this box keeps its working tree. Cloud-read test 7/7. On the real cluster copy the laptop now reads dell2's rows: `anlreq-90` `8500` OPEN (2 commits), `anlreq-88` `7b45` OPEN, `anlreq-87` `fde0` OPEN, and the duplicate branch `3635` OPEN | `965f9eff8a` |

All six open-calls suites on the merged tree: 7/7, 7/7, 11/11, 10/10, 13/13, 19/19.

## 2. Your round-3 list, item by item

1. **S03 and the refusal arm (A7): DONE.** The gate blob `fcdbc6e1` is identical on origin/box/{laptop,dell1,dell2,sitez} and origin/CLOUD (read with a positive control). A direct DEV push from this seat is refused, run from a scratch worktree so it exercises the refusal and not the HEAD-on-DEV false positive.
2. **The three dell2 rows (A12): DONE by dell2.** `8500`, `7b45`, `fde0` registered with `--waive-overlap` naming your four commits and `--waiver-ref` your round-3 analysis (relay from MSTR, CTO~DELL2 msg 7316). They are OPEN for Andrew on the open-calls list.
3. **dell2's next ANLREQ change (A11): in motion.** dell2 registered `cand/dell2/irpt-ytd-from-first-day-and-wider-export-modal` (client-facing, branch on portal origin @`03073765`), twice. With `DP-e-1` merged the duplicate can now be withdrawn; the exact command is in `NFRA_DEVPLN_A13_DELL2_WITHDRAW_DUPLICATE_20261013.md`, for a dell2 seat, relayed through MSTR.
4. **The pre-push payload limb (your addendum): NOT in this round, per your ruling.** It is the first cell of round 5 on `.tools/portal-hooks/pre-push`, carrier row `NFRA_DEVPLN-S3`. Draft: `deliverables/drafts/ROUND5_DRAFT_dev-push-payload-limb.md`.
5. **W2-S9/S10:** W2-S10 repaired (`DP-e-3`); W2-S9 needed no repair (the local fallback already prefers `refs/heads/<b>` exactly when origin lacks the ref).

## 3. Rows and watermark

Channel: 36 investigation rows, 7 adjudication rows, ARMED 0. Round 4's open rows: `W1-S13` (the worktree's recorded portal gitlink differs from its nested checkout), `W1-S14` (the cloud-read test needed a second test-only seam, `OPAL_GIT_READ_ROOT`), `W2-S11` (the self-test's fixture writes lack an exit check), plus the earlier `W1-S12`, `W2-S9`, `W2-S10`, `S2`, `S3`. `S2` is answered by `DP-e-1` and `DP-e-2`.

## 4. Awaiting Andrew (client-facing; the CVO and you cannot rule these)

Five rows on dell2's list: `8500` (anlreq-90), `7b45` (anlreq-88), `fde0` (anlreq-87), `cffa` (the YTD and export-modal feature) and its duplicate `3635`. Until `3635` is withdrawn, Andrew should close both `cffa` and `3635` with the same decision, because the route reads the newest row. The CLAUDE.md law-edit card `laptop-20261013T223003Z-3d7e` is also his.

## 5. ENRICHMENT candidates for round 5 (thread-breaking first)

1. **The pre-push payload limb (your ruling): FIRST.** On `.tools/portal-hooks/pre-push`, with a separate checker script; three exempt routes (an approved merge, a test-only change, a PROD-into-DEV back-merge) and a live FAST lease; it fails closed. Install is a copy by `install.sh`, the hook's lane owner's act.
2. After Andrew rules the dell2 rows: the merge-forward by the integrator and the DT's chosen-set promote naming only what he approved (a DT order at that time); this is the client-facing close of FWD-1.
3. A repair batch: W1-S14's second seam (document it or fold it into one variable), W2-S11 (exit checks on the self-test's fixture writes).
