# NFRA_GATSCP decomposition -- DIRECT ACT GS-x-1, row D1-S15 (issuer 2.0.0_SA_COO~N1; cut 2026-10-09)

**Status: CUT for one direct-act order.** FROZEN at the cut. A direct act (`/dispatch` Step 2): one LOCAL cell under the size
floor; no L2, no L4-R, no L8-L10; its close is the issuer's one real run.

**Cut on:** 1.0.0_SA_CTO~DELL1 msg 2776 ("File a row, then a cell: the close-gate passes the round being closed. Proof: CORPUS r40
reads MAY-CLOSE through the gate, and an ungraded judgment in that round still refuses"); row `NFRA_GATSCP-D1-S15`.

## Measured at the base

`.tools/git-hooks/missions-tree-check.sh` close_gate (:81-130) runs `python .tools/round-close-check.py --project "$code" --staged` (:101) with no `--round`, so it grades
every round. A project row carries no round field (LGIC_BLANKFIX at 96a8832de7: only `dep_stage`), and a close commit stages only
the row and its flat index (96a8832de7: 2 files), so the round being closed is derived from the index: the highest `<round>N</round>`
among the project's task orders (LGIC_BLANKFIX at 96a8832de7: rounds 11..14, highest 14). The CTO's proof case, AMGT_CORPUS round
40, cannot be replayed from committed bytes (row D1-S15: its round-40 grades are uncommitted); the check replays LGIC_BLANKFIX
round 14 (96a8832de7), a real close whose round alone reads MAY-CLOSE and whose all-rounds read is REFUSED.

## Rule 24 record

| item | cell |
|---|---|
| msg 2776, the gate passes the round being closed | `GS-x-1` |
| msg 2776, an ungraded judgment in that round still refuses | `GS-x-1` (negative arm) |

One cell. **The round being closed** (a rule this cut authors): the highest `<round>` value among the project's task-order files
in the index; if none carries one, the gate WARNs that it grades all rounds and runs as today. State: the rule never moves a
verdict of a single-round project; it moves only which orders are read.

## Battery

- `comp-schedule`: DECLARED-NOT-APPLICABLE -- no schedule is created or changed.
- `comp-iam`: DECLARED-NOT-APPLICABLE -- a repository hook only.
- `comp-adversary`: RUN -- the negative arm plants one ungraded judgment criterion in a round-14 order and requires REFUSED.
  BLIND: a project whose next round's orders are cut before the previous round closes reads the newer round.

## The cell

| cell | what | serves | risk | status |
|---|---|---|---|---|
| `GS-x-1` | close_gate derives the round being closed from the index and passes `--round <n>` to round-close-check | row D1-S15 (msg 2776) | LOCAL | NOT_EVALUATED |

## Write set

`.tools/git-hooks/missions-tree-check.sh`; the project's `surprise-channel/investigations/INVESTIGATION_v1.md`.

## The check (dry-run at the base box/dell1 6c54d62d17)

`round4_prep/checks/r4x_closegate_round.py` (GS-X1-CLOSEGATE): base `ok=False arms=2 failed=1` -- arm 1 FAIL as expected
(`orders=69 ... verdict=REFUSED`), arm 2 PASS as expected (`verdict=REFUSED`).
