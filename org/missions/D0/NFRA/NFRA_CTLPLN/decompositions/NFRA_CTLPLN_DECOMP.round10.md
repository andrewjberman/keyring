# NFRA_CTLPLN decomposition -- round 10: realize FWD-28 on the landed portal carrier, the thread read for ONE order (E1), and a stated carry for every other item (issuer 2.0.0_SA_COO~C; cut 2026-10-12)

**Status: ISSUED in one issuance (one worker order plus the issuer acts below). FROZEN at the cut.**

**Input.** `org/missions/D0/NFRA/NFRA_CTLPLN/ledger/ROUND_ANALYSIS.round9.md` (1.0.0_SA_CTO msg 108536), section 3. Round 9 closed first (`round-close-check --round 9` MAY-CLOSE, proof_bad 0, 2 of 2 judgments graded, 66 gating items dispositioned). The v0.25 ratified half is SIGNED current; nothing is owed on the PRD half (struck from the issuer's list).

## The analysis's items, each with its disposition (denominator: 8)

| # | item | disposition |
|---|---|---|
| 1 | Confirm MSTR's DEV push of portal `53506d49` landed | DONE at the cut, read: `git ls-remote origin refs/heads/DEV` in the portal repository reads `53506d4903ae...`; `git show origin/DEV:src/lib/firmAccess.ts` carries the generated block (msg 108519 from `0.0.0_AB_MSTR`). |
| 2 | Move the gitlink; re-run the 10 checkout tests (FWD-28 REALIZED reads on it) | ISSUER ACT A10. The 10 tests read `portal/src/lib/firmAccess.ts` from the workspace's portal checkout, which is 355 commits behind and carries other seats' uncommitted edits, so they cannot be re-run in place. A10 provisions a workspace worktree whose nested portal is `origin/DEV` (`wk-provision.sh ... --portal-ref`), runs the three test files there and records the counts; then the gitlink in the index is set to `53506d4903ae...` and committed on `box/laptop` (the pointer only; the checkout is not touched). |
| 3 | E1 end to end: the whole thread | CUT: `CT-z-1` (the instrument: an order filter, so a round that mixes boxes can be traced for the dell1 order alone), then ISSUER ACT A1: `thread-trace.py --project NFRA_CTLPLN --round 9 --order TO-CT-y-2` printed whole. |
| 4 | E4: the 12-message matrix | PARTIAL, stated: `crossbox-matrix.py` now reads `acked=10`: laptop->dell2 `XB-20261012T070501Z-cb95` is ACKED (dell2's manager came back at 12:27Z). Two pairs stay OPEN, each on another project's seat: dell1->dell2 `XB-20261012T082300Z-d5e7` (the dell2 seats) and dell2->laptop `XB-20261012T024226Z-0dce` (addressed to the stood-down `0.7.0_AE_CloudOps~ANL`; the file is dell2's to close or withdraw). Asked through `0.0.0_AB_MSTR` this tick; re-read at the close. |
| 5 | E2, E3, E5-E8 carried | E2 DONE (`TO-CT-x-1`); E3 DONE on dell1 (`CT-v-1`, `CT-v-3`, `CT-w-5`; the read-aloud to Andrew is his act); E5 DONE (`TO-CT-t-3`); E6 an ask to the CVO and Andrew; E7 an ask to each box's manager and MSTR; E8 DONE (census + the design, `CT-w-6` and `CT-y-1`). Reasons stated; no cell is owed. |
| 6 | E9 FWD-27 | GATED on Andrew's public keys and elevated lines; no cell runs without them. |
| 7 | S9112 purge and refresh-token invalidation | ANDREW'S (asked by the CTO 11:5xZ); retention 14 d, the pre-fix lines age out by about 2026-10-26. |
| 8 | S9111 (partner `/api/scoped/partners` calls reaching the proxy's `$default`) | A ONE-LINE ROW, no cell: the owner is the shared portal API root, `infra/aws/terraform/shared-infra/apigateway-portal` (API `7k3ed8px20`); its latest authors are `0.7.0_AE_CloudOps~Z` under NFRA_OPSEC202609 (the jwt authorizer onto the data routes) and `0.7.0_AE_CloudOps` (the route consolidation). |

## Cells

| cell | what | serves | risk | issued to |
|---|---|---|---|---|
| `CT-z-1` | `.tools/thread-trace.py` gains `--order <TO id>` (repeatable): only the named orders are traced (their issuance, their `<issued_to>` serial's work, publish, integrate, grade), so the thread of the dell1 order `CT-y-2` can be read without the laptop worker order `CT-y-1` of the same round; the selftest gains cases; the behaviour with no `--order` is unchanged. | FWD-1, FWD-4 | LOCAL | `0.9.0_WK_NFRA_CTLPLN~73` |

## Rule 24

**Domain:** the eight items above. Each has a disposition naming its act, cell or owner. **Same grain; one intent.** **State coherence:** `CT-z-1` changes one tool and its selftest; A10 changes one gitlink record and nothing in the checkout.

## Dependency chains and fan-out

One chain: `CT-z-1`, then A1. `fanout: 1 of 1 chain, cap 8, reason: the instrument fix is the only cell; everything else is an issuer act or Andrew's`

## Issuer acts (the COO's one real run of each outcome, at the close)

- **A10:** as row 2; the three test files' counts, the DEV sha read, the gitlink commit.
- **A1:** as row 3, after `CT-z-1` merges: the trace for `CT-y-2` alone, and for the whole round, both printed.
- **A4:** the matrix re-read at the close; the ask to MSTR about the two OPEN files.
