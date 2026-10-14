# NFRA_DEVPLN round 7 -- drain-end read to 1.0.0_SA_CTO (issuer 2.0.0_SA_COO~DV, 2026-10-14T02:17Z)

Issuance `684d9ba872` (PRD v0.3 @14a0501ee5, round-6 analysis, your msg 109029). `python .tools/round-close-check.py --project NFRA_DEVPLN --round 7` reads `reviewer=present (3.0.0_SA_CVO~L) orders=1 verdict=MAY-CLOSE`. Push state (ls-remote `6910f1c7a7`): the issuance, the DP-i-1 merge `ef2f11a541` and the rows are on origin/box/laptop; the close commit is LOCAL. No SERVED or WORLD order, so no CVO packet.

## 1. The order (1 of 1 complete, proof VALID; every project suite re-run on the merged tree)

| cell | result | merge |
|---|---|---|
| DP-i-1 | S4: `portal-release-build.sh --check <name>` prefers `refs/remotes/origin/<name>` for a trunk name and prints `ref=<full ref> sha=<12>` at the end of the `RELEASE-CHECK` and `RELEASE` lines; self-test 12/12. W1-S16: test case 9 runs under an empty temporary `GIT_DIR`, so no real ref is looked up; cloud-read test 10/10 | `ef2f11a541` |

The real seam: `--check PROD --prod-ref 63c4f9e3` now prints `RELEASE-CHECK features=2 first_parent_commits=2 unapproved=0 ref=refs/remotes/origin/PROD sha=7d5cb34daabc` (it read the stale local `PROD` and printed `features=1` before). All suites on the merged tree: 10/10, 7/7, 11/11, 10/10, 13/13, 19/19 (open-calls), payload limb 19/19, merge-forward 29/29, release builder 12/12, DEV read 7/7.
Consumer check, by the issuer: the only reader of those lines is `/prod-deploy` Step 4, which extracts the release branch with `sed -n 's/^RELEASE result=READY .* branch=\([^ ]*\) .*/\1/p'`. I ran it on a line with the new suffix (both ref forms) and on the old format: the branch is extracted unchanged.
Worker notes, recorded: cases 1 and 9 of the release self-test matched the whole line and now match the prefix (counts unchanged, row W1-S17); the cloud-read test's `run()` clears an inherited `GIT_DIR` for all ten cases, wider than the order (row W1-S18); build mode's lines carry the suffix too (declared in the proof).

## 2. State of the project (measured ~2026-10-14T02:17Z)

- Portal DEV `5e40e541`, PROD `7d5cb34d`. The pre-push limb is installed on all four boxes (MSTR's final state: hook `6dc8be3ced` on CLOUD; hook history LD-0646 gitlink path, LD-0647 your fail-closed ruling, LD-0648 workspace root from the hook's own location, LD-0649 refusal text). Not yet read anywhere: a real APPROVED merge-forward push through the hook on a submodule box; dell1 will report the first.
- Two features have reached PROD as chosen-set promotes (`10e7664d`, `7d5cb34d`); `unapproved=0`, none of the seven unapproved dell2 DEV commits shipped.
- Rows: 43 investigation, 7 adjudication, ARMED 0, 15 open observations. New: `W1-S17`, `W1-S18`, and `S5` (the unblock tick's `--owed-call` reads only this box's list, so a wait on Andrew's dell2 rows cannot be recorded; my attempt reached `empty=5`, no case opened, reset by a real work tick; options for you in the row).

## 3. What the project now waits on, all external

- **Andrew:** dell2 rows `3635`, `8500`, `7b45`, `fde0`, `7773` (all client-facing, all OPEN, read from dell2's cluster copy ~2026-10-14T02:17Z); the law-edit card `laptop-20261013T223003Z-3d7e`.
- **The DT:** the closed ledger file for TO-DP-x-1 is still uncommitted (asked; no reply), so other boxes read that deploy OPEN.
- **You:** the round-7 analysis; a ruling on row S5.

## 4. ENRICHMENT candidates for round 8

1. After Andrew rules: act A14, FWD-1's client-facing close (a DT order, SERVED, with the L8 packet). It is the only remaining work in this project's plan.
2. Nothing else is cut-ready: no open cell, no armed row. If Andrew's rulings are not in when you read this, the project's honest state is a dated wait on him, not a round.
