# 2.0.0_SA_COO~T -- session close, managed wind-down

**Seat:** `2.0.0_SA_COO~T` (Tier-2 COO lane, laptop box, branch `CLOUD`)
**Seated:** Andrew seat order ~12:5xZ 2026-09-15 (LD-0569, msg 97080), by `0.0.0_AB_MSTR`
**Held:** ONE project -- `MDPF_TAXSMA` (D8/MDPF)
**Closed:** 2026-09-16 ~00:1xZ, on Andrew's MANAGED WIND-DOWN of the laptop fabric (~23:3xZ, msg 97269,
"we need a managed winddown, computer is moving too slow"). Goals and loops are PAUSED, not cancelled.

---

## 1. RESUME POINT -- one line

**Drain branch `wk-mdpf_taxsma-1-1` (TX-g-1, complete at 23 of 23 PASS, HEAD `f2cac74c60`) into `CLOUD`
via `.tools/safe-merge.sh`, then spawn the remaining 24 task orders of round 1.**

Expect a conflict on `org/missions/D8/MDPF/MDPF_TAXSMA/surprise-channel/investigations/INVESTIGATION_v1.md`
(NFRA_CLDGRPH-S36 shape: both sides append at the same offset and restate the header). Resolve by union --
assert the shared rows are byte-identical, append the branch's three new rows `MDPF_TAXSMA-W1-S1..S3` exactly
as the branch wrote them, verify the final id list, `git add` that one path, then `safe-merge.sh --continue`.

---

## 2. STATE AT CLOSE (measured, not claimed)

| what | value | vintage |
|---|---|---|
| `dep_stage` | `EXECUTING` | `project.json` at HEAD |
| `status` | `scoping` | sequence-check, stage 0 of SEQUENCE.yaml |
| PRD | v0.5 `@671925aecc` **ADMITTED** -- ratified-text SIGNED (`3.0.0_SA_CVO`), brief SIGNED (`4.0.0_SA_CRO`), both `current` | `prd-signoff.py status` |
| decomposition | v2 `@7f65001ab3` -- 27 cells, 39 edges, 1 component, 4 heads, M=21 maximal paths, FROZEN | header JSON |
| issuance | ONE, `@955b8c6cbe` -- 27 orders, every cell covered | issuance commit |
| orders at HEAD | **25 open** (4 ACTIVE, 21 PENDING), **2 complete** | `to-check.py --project MDPF_TAXSMA` |
| shared-tree HEAD | `3dcb249826` | this seat's last commit |
| push state | **LOCAL on `CLOUD`** -- this seat pushes nothing (shared branches are `0.0.0_AB_MSTR`'s on Andrew's word) | -- |

### Worker slots

| slot | order | outcome | branch | worktree |
|---|---|---|---|---|
| `~5` | TX-v-1 expected-cases | drained `@a481dfa6a1` | removed | removed |
| `~6` | TX-p-1 baseline | **10 of 10 PASS**, drained `@3dcb249826` (16 of 16 branch paths verified landed by first-parent diff) | `wk-mdpf_taxsma-1-6` KEPT | removed at close |
| `~1` | TX-g-1 workbook-capability | **23 of 23 PASS**, complete on its branch, **NOT DRAINED** | `wk-mdpf_taxsma-1-1` `@f2cac74c60` KEPT | **KEPT** (1.4 GB) |

`~1` was not drained because the shared tree carried **another seat's open `MERGE_HEAD`** (a
`NFRA_OPLGTW` worker drain, 6 staged files) at the moment the wind-down reached this step. A drain would
have been refused on the foreign merge, correctly. Its three commits are durable on the branch; nothing is
lost and nothing is half-landed.

`~1`'s worktree is KEPT because it holds an uncommitted tracked modification --
`infra/aws/ec2/opal-gateway/audit.jsonl`, the append the Gateway suite makes when run from its own
directory (the worker's own row `MDPF_TAXSMA-W1-S2`). Removing it would need `git worktree remove --force`,
a destructive git act that takes Andrew's word. It is 1.4 GB and can be removed on that word; the branch
carries every artifact.

### Amendments and rulings this session

- TX-g-1 `@50b8910af4` -- granted `infra/aws/ec2/opal-gateway/tests/test_principal_cutover.py` in `<paths>`
  for ONE `ROUTE_CLASS` entry. Defect found by `2.0.0_SA_COO~O` (msg 97236), verified at HEAD before spawn.
  Row `MDPF_TAXSMA-S3`.
- TX-p-1 AC10 `@6be05d277f` -- admits AC7's one read-only `ssm send-command` by name, under
  `1.0.0_SA_CTO` ruling 97255 option (A), four conditions. The worker had correctly REFUSED to reword and
  filed BLOCKING row `MDPF_TAXSMA-W6-S1`; the contradiction was this seat's cut defect, not the worker's.
- `1.0.0_SA_CTO` ruling **97272/97273**: `>/dev/null` is NOT a write to a path, so condition (2) is met --
  **AC10 PASS and TX-p-1's `complete` flip STAND, no second amendment.** Canonical wording for any sibling
  criterion is in that message and is quoted in row `MDPF_TAXSMA-W6-S4`.

### Surprise channel

At HEAD: `S1`, `S2`, `S3`, `W5-S1`, `W6-S1`, `W6-S2`, `W6-S3`, `W6-S4` (8 rows).
On the undrained `~1` branch: `W1-S1`, `W1-S2`, `W1-S3` -- they reach the shared channel only at that drain.

### Three carries `~1` recorded for later cells

1. `TAXSMA_WORKBOOK_IDENTITY` is `<tid>/<oid>` and binds through the token broker's principal-keyed cache,
   which only `verify_upstream_id_token` writes -- that shape is what makes AC8/AC9 checkable with zero
   token fetches. TX-i-3's secret and TX-r-3's activation depend on it.
2. The projection ships cell values as Graph returns them, so an Excel date cell arrives as a serial number
   with no number format beside it; S02/S19/S03 decode downstream. The contract's `response_fields` are
   closed, so the response was not widened.
3. Running the Gateway suite from its own directory appends to the TRACKED `audit.jsonl` (row `W1-S2`).

---

## 3. WIND-DOWN DISPOSITION (Andrew's order, step by step)

1. **STOP STARTING** -- honored. No new spawn, task order, round, worktree or apply after 97269.
2. **WORKERS PARKED** -- `~1` had already reported complete before the wind-down reached it, so it is parked
   as a finished-but-undrained branch, not mid-flight. Nothing is mid-criterion.
3. **APPLIES** -- none were mid-flight. No Terraform apply and no deploy was open at any point in this
   session, so NEVER-2 has nothing to finish or roll back.
4. **COMMITTED** -- the `~6` drain finished through its guards at `3dcb249826` and this log is committed.
5. **LOOPS STOPPED** -- goal cron `8484df75` deleted; the inbox Monitor expired on its own 30-minute timeout
   and its bash child was killed.
6. **WORKTREES** -- `~5` and `~6` removed and pruned; `~1` kept with its reason above. Every branch kept.
7. **REPORTED** to `0.0.0_AB_MSTR`, one message, before exit.

---

## 4. WHAT THE NEXT SEAT SHOULD NOT REDO

- The decomposition is FROZEN for round 1. A cell that looks wrong is a surprise ROW, never an edit.
- Both PRD halves are SIGNED at the current bytes. A re-cut does not re-open them; `prd-signoff.py status`
  is the one read of what is owed.
- The L6 coverage limb reads `dep_stage` at HEAD (`to-pipeline-gate.py:537-540`), so a re-cut staged while
  the row already reads `EXECUTING` has coverage NOTED, not GRADED. A dropped cell is the human's to catch
  there.
- A worker subagent is TERMINAL once it reports and cannot be resumed; slot `~1`'s next order is a cold
  start carrying its own continuation note.
