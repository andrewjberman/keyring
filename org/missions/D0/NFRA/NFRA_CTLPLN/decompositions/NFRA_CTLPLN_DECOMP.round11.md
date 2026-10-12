# NFRA_CTLPLN decomposition -- round 11: the thread's grade hop, the order set read from git, the last two crossbox acks, and a stated reason for each carried item (issuer 2.0.0_SA_COO~C; cut 2026-10-12)

**Status: ISSUED in one issuance (two orders plus the issuer acts below). FROZEN at the cut.**

**Input.** `org/missions/D0/NFRA/NFRA_CTLPLN/ledger/ROUND_ANALYSIS.round10.md` (1.0.0_SA_CTO msg 108560), section 3. Round 10 closed first (`round-close-check --round 10` MAY-CLOSE, proof_bad 0, 2 of 2 judgments graded). FWD-28 is REALIZED; nothing is owed on it.

## The analysis's items, each with its disposition (denominator: 5, plus the section 4 owed list)

| # | item | disposition |
|---|---|---|
| 1 | A4: the last two acks (`0dce`, `d5e7`) now dell2's lanes are re-seated | ISSUER ACT A4. `crossbox-matrix.py` reads `acked=10` at the cut; both files are still OPEN. One message to `0.0.0_AB_MSTR` naming the two files and the lanes that owe the act (`2.0.0_SA_COO~Y2` closes or withdraws `0dce`; the `~Y` lane acks `d5e7`); the matrix is re-read at the close and FWD-3 / FWD-22 are graded on 12 of 12 only when it reads so. |
| 2 | W73-S2: `find_orders` reads refs, not the worktree | CUT: `CT-aa-1` (HYGIENE, round 2), worker `0.9.0_WK_NFRA_CTLPLN~74`. |
| 3 | E1 end to end | CUT: `CT-aa-2` (THREAD, round 11), a dell1 seat order for `0.7.0_AE_CloudOps~CT1` that carries ONE JUDGMENT criterion, so the thread's fifth hop (GRADE) has something to read. Round 9's thread read 4 of 5 hops because its order carried no judgment criterion (the CTO's reading of round 9); this round's thread is planned on the laptop, worked and committed on dell1, integrated by `0.0.0_AB_MSTR`, and graded by `3.0.0_SA_CVO~L` on the laptop. ISSUER ACT A1 reads it with `thread-trace.py --project NFRA_CTLPLN --round 11 --order TO-CT-aa-2` at the close. |
| 4 | E2, E3, E5-E8: at least one cut, or a reason each | NONE CUT, a reason each (read from the record at the cut): E2 (the deploy read-back and the refused IAM write) DONE under `TO-CT-x-1`; E3 (the dell1 click route) DONE under `TO-CT-v-1`, `TO-CT-v-3`, `TO-CT-w-5`, and `CT-aa-2` below rewrites its record in plain words for Andrew's read-aloud, the one part of E3 that was not done; E5 (no hand-carried step) DONE under `TO-CT-t-3`; E6 an ask to the CVO and Andrew (no cell can run it); E7 an ask to each box's manager and MSTR (no cell can run it); E8 DONE (the census and the design, `TO-CT-w-6`, `TO-CT-y-1`). |
| 5 | E9 FWD-27 | GATED on Andrew's public keys and elevated lines; no cell runs without them. |

Owed outside the project (analysis section 4): Andrew's W61-S1 elevated line, S9112's purge and refresh-token invalidation, FWD-27's keys, and the PROD push of the portal carrier. Not this round's cells.

## Cells

| cell | what | serves | risk | workstream / round | issued to |
|---|---|---|---|---|---|
| `CT-aa-1` | `.tools/thread-trace.py` `find_orders` reads the round's orders from git (`HEAD` and `origin/CLOUD`, by `git ls-tree` / `git show`), not from the reading checkout's files, and the THREAD line prints `orders_found=<n>`; the selftest gains two cases. | FWD-1 | LOCAL | HYGIENE / 2 | `0.9.0_WK_NFRA_CTLPLN~74` |
| `CT-aa-2` | On dell1, write one plain-language summary (at most 220 words) of what the three dell1 click-route records prove and what they do not, for Andrew to hear read aloud; commit it on `box/dell1`. One JUDGMENT criterion graded by the CVO. | FWD-1, FWD-4 | LOCAL | THREAD / 11 | `0.7.0_AE_CloudOps~CT1` |

## Rule 24

**Domain:** the five items above plus the owed list. Each has a disposition naming its act, cell or owner. **Same grain; one intent.** **State coherence:** `CT-aa-1` changes one tool and its selftest; `CT-aa-2` adds one record file; A4 moves two crossbox files on dell2's side and nothing on this box.

## Dependency chains and fan-out

Two independent chains: `CT-aa-1` (laptop worker) and `CT-aa-2` (dell1 seat); A1 follows `CT-aa-2`'s integration and reads with `CT-aa-1`'s tool. `fanout: 2 of 2 chains, cap 8, reason: the tool fix is a laptop worker and the grade-hop order is a dell1 seat; neither writes the other's files`

## Issuer acts (the COO's one real run of each outcome, at the close)

- **A4:** as row 1; the matrix printed whole before and after.
- **A1:** as row 3; the trace for `TO-CT-aa-2` alone and for the whole round, both printed.
- **After `CT-aa-1` merges:** re-run `thread-trace.py --project NFRA_CTLPLN --round 9 --order TO-CT-y-2` and print `orders_found`.

## Amendment 1 (issuer 2.0.0_SA_COO~C, 2026-10-12 ~14:3xZ; gate limb: none graded this modification) -- one cell added by the CTO's round-11 input

Input: `1.0.0_SA_CTO` msg 108579 (dell1 row D1-S9, measured 14:1xZ on `opal-users-v2`): 6 PROFILE rows carry `userType` Dev and 3 of them carry a tier other than `internal` (advisor or absent), all staff; the authorizer grants Dev everything whatever the tier, so the CT-u-6 helper `_require_route_access` (which tests `tier == internal` only) refuses those three staff logins on the 39 class-(ii) routes. Ruled by the CTO cluster-wide: the helper admits `tier == internal` OR `userType == Dev`; no user record is edited for a fence. This is the sixth analysis item of round 11 (denominator now 6); the CTO writes the PRD wording addendum to FWD-28's ACCEPT when this cell is cut.

| cell | what | serves | risk | workstream / round | issued to |
|---|---|---|---|---|---|
| `CT-aa-3` | `_require_route_access` admits `userType == Dev` beside `tier == internal`; a partner advisor token on a class-(ii) route still answers 403; a new test file. NOTHING IS DEPLOYED by this cell. | FWD-28 | WORLD (the floor of the infra path; no deploy) | DEVFENCE / 1 | `0.9.0_WK_NFRA_CTLPLN~75` |

The live apply is a SEPARATE order (`CT-aa-4`, a `0.7.0_AE_CloudOps~U7` seat order under a FOURTH signed never-widen pair in the shape of `CT-w-10`), cut as a recut when `CT-aa-3` has merged and its pin is known; the pair names the callers of its reads. Chain: `CT-aa-3`, then the pair, then `CT-aa-4`. Fan-out for the issuance of this amendment: `fanout: 3 of 3 chains, cap 8, reason: CT-aa-3 writes only the data proxy handler and its tests, disjoint from the thread-trace tool (CT-aa-1) and the dell1 record (CT-aa-2)`.
