# H03 2a -- PRE-APPLY POINTER PINS (the corrected control's BEFORE arm)

**`3.0.0_SA_CVO~Z`, 2026-09-24 ~04:0xZ.** Captured **BEFORE the AE apply**, on the CTO half's amended
condition 3 (`41616c8789`). **NOT a grade.** This is the arm of the control that cannot be measured
after the act.

## WHY

The corrected control has two arms: **(a)** the 09-23 pointers stay **byte-identical**, and **(b)** a
fresh `#2026-09-24 _CURRENT` appears with `row_count 2` and `names_with_links 3 of 250`. **Arm (a)
requires a before-state.** Without one, "byte-identical" can only be asserted by the applying party
after the fact.

**INSTRUMENT:** `dynamodb get-item` on `opal-harvest-security-metrics`
(key schema `axis_date` HASH / `ticker` RANGE, read from `describe-table`).

## THE PINS

| item | value |
|---|---|
| **`TRENDING_CHATTER#2026-09-23` / `_CURRENT`** | |
| canonical sha256 | **`64e3bddba86d3b2515994fd792375cbb31d04710c234d9fb4ac3eb4617d367f9`** |
| `generation_id` | `20260923T100026Z-d09ee37a8f3b` |
| `row_count` / `state` | **2 / COMPLETE** |
| `payload_hash` | `d09ee37a8f3b52bd5133a407a0d8e0362f1f0d596feef0258c1b4539a7bde6c5` |
| **`BREAKOUT_CHATTER#2026-09-23` / `_CURRENT`** | |
| canonical sha256 | **`887bd7c308bd99994f3d8603d778cd46f7fd07fb21aa9cd86903c19b3451116d`** |
| `generation_id` | `20260923T100028Z-25147d66b259` |
| `row_count` / `state` | **0 / EMPTY** |
| `payload_hash` | `25147d66b2597ea8438fd0519ad9881907b93975d98edd1fd5fcc2fe3401f34e` |

⭐ **Both `generation_id`s match the CTO amendment's cited values exactly**, measured here by a seat that
did not author them. **And each `generation_id` embeds its own `payload_hash` prefix** (`-d09ee37a8f3b`
against `d09ee37a8f3b52bd...`), so the id is self-checking against the payload it names.

**`canonical sha256`** is over the whole DynamoDB item, keys sorted, separators tight -- so **arm (a) is
now falsifiable on one comparison** rather than on a field-by-field reading.

## ONE OBSERVATION FOR THE GRADE

`BREAKOUT_CHATTER#2026-09-23` is **`state: EMPTY`, `row_count: 0`** -- it **has** a terminal pointer.
That is consistent with, and sharper than, "Breakout has no **COMPLETE** pointer in any window and reads
ABSENT at every hour": **EMPTY is not COMPLETE, and the reader's window rule distinguishes them.** A
grader reading "no pointer" rather than "no COMPLETE pointer" would look for an absent item and find a
present one.

## WHAT THIS DOES NOT ESTABLISH

- **Not a grade of the 2a candidate.** The apply has not run; deployed `CodeSha256` is still
  `I6eitcaItzqRTlVUaUSF+GGzrpNDHnn71ILk1vIGjHY=` at 128 MB / 60 s, so **nothing is applied**.
- **Arm (b) is unmeasurable until the 10:00Z fire.** A fresh `#2026-09-24 _CURRENT` cannot be verified
  before it is written.
- **Nothing is rendered**, and the edge is not exercised.
- These are **pointer items only** -- the gold parquet, the artifact bytes and the Terraform plan are
  measured elsewhere and not re-derived here.
