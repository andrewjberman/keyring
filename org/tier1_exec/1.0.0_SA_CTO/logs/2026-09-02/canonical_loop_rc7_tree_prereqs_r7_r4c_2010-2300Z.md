# 1.0.0_SA_CTO -- 2026-09-02 20:10Z-23:00Z: the loop closed on real traffic, the tree's gates read both roots, and the design's last two items landed

**CONCLUSION.** The ETFS_GUARDRAIL RED/HOLD is LIFTED (CVO base verdict 21:26Z, RC1-RC7 + limb 5 GREEN on
CVO's own instrument). Andrew's mandatory start point -- the project-tree prerequisites -- is COMPLETE
from both halves and with `3.0.0_SA_CVO` for review (COO's ONE message 22:36Z). R3 (the PRD-commit
notifier) closed end to end on REAL traffic: two notifications sent, one re-offered, both READ-acked
by COO at 21:48:53Z. R7 (the step-10 router) and R4-c (the watcher's NEW-row arm) are built and
exercised. Push state, measured: everything through R7 @`b5302e192c` is on origin (MSTR pushed);
R4-c @`f2cbab30a1` is local.

## What landed, in order (all `safe-commit`, all gated)

| commit | what | evidence |
|---|---|---|
| `38f60078c4` | limb 5 pass 5 (CommonMark fence SCANNER; `brief_ref` no-whitespace) + RC7 files | harness v5 56 cases: RED 6 / GREEN 0; schema OLD 4 of 11 wrong / NEW 0; selftest probe QUEUED -> READ |
| `cf532d66c5` | ETFS_GUARDRAIL PRD v0.2 (`outcome` -> `outcome_ref`) -- the RC7 PRD-path exercise | hook fired; python FAILED (see below) |
| `451df0d61f` | notifier: explicit UTF-8; a read failure is an ERROR, never a header verdict; hook logs every firing | manual post-commit -> id 92762 to COO |
| `719e73ffd3` | notifier: re-offer sends as the row's ORIGINAL author | hook fired on CVO's commits twice in 5 min |
| `fafb009458` | PRD v0.3: the hold-lift line (CVO's verdict cited) | id 92781; re-offer of v0.2 as 92780 |
| `4d9e66d31b` | notifier: legacy rows read their sender off the ledger; refuse rather than borrow | 92780 had gone out from `3.0.0_SA_CVO` |
| `20d1c60866` | tree prereq 4: `org/missions/**` lanes by artifact type + validator clause 4 | 27/27 both directions; 68 lanes / 272 rules |
| `1655d87688` | tree prereq 5: both gates + corpus `--index` + watcher read BOTH roots; walk-back retired | TO gate RED 14 / GREEN 0 of 19; row gate RED 8 / 0 of 12; prior 56 + 34 still 0; watcher selftest 19/19 |
| `fa44d04e2c` | manifest rows 4-5 BUILT | COO closed the set @`1223c343fe` |
| `b5302e192c` | R7 router on the R3 machinery | selftest 7/7; dry-run on the only two real remediation commits |
| `f2cbab30a1` | R4-c NEW-row arm + 7-column `--index-rows` | selftest 22/22; real bytes: `WSE_COTMDL-S1 class=BLOCKING hazard=ARMED` named |

## Grades issued (certifier != author)

- `surprise-watch.sh` pass 2 @`1a4ce78782`: **PARTIAL 3/4** on a second instrument (the committed function
  block sourced; the REAL validator over the LIVE 192-row channel; wrappers dropping a REAL row).
  **F2 defect:** the guard triggered on COUNT, the hazard was a missing `(path,id)`; a real row dropped in the
  same sample as a genuine append kept the count equal, fired DISAPPEARED, and the row was FORGOTTEN.
  Repair bar (i)-(iv) sent. Pass 3 @`d413196285` implemented it: **GREEN 4/4**, E2 now holds a still-present
  row provisional. The bound sized: ~34 s at a 2 s sample + 15 s sleep; two independent races after pass 3.

## What I got wrong tonight, with the tell each time

1. **Three selftest runs failed on MY side before the transport was even reached.** (a) the temp body dir did
   not exist; (b) the receipt has no `id=`; (c) the message was DELIVERED and NOT ON THE LEDGER. (c) is the
   one that matters: `codex-send.py` delivers through the broker LIBRARY in-process; the HTTP ledger never
   sees it; **no READ-ack can ever exist for anything sent that way.** Memory written.
2. **The first real firing of the notifier reported a FALSE reason.** `git show` under the hook decoded as
   cp1252, died on the PRD's UTF-8, and the notifier printed *"no valid PRD_HEADER"* -- naming the step-6 gate
   as the refuser of a PRD that gate passes. A read failure reported as a content verdict. Memory written.
3. **The device-wide hook runs as whoever commits.** Measured: a re-offer went out from `3.0.0_SA_CVO`. Two
   fixes, the second because the first did not cover rows written before it.
4. **Harness defects, four of them, each caught by the harness contradicting itself:** the flip limb reads
   the STAGED index (my cases ran outside the patched reader -> both read FOUND); the fake blob reader
   returned ABSENT for the schema too; the borrowed corpus row had no trigger halves (0 of 191 corpus rows
   carry them); the pass-1 watcher harness died on an unset global under `set -u`. None reached a commit.
5. **A 0-byte hook log after the first firing could not say whether the hook fired.** Now one line per firing.

## Open, and where it sits

- R2 lens readmissions, R8-b `FWD-NONE` sentinel, F2 `disposition` enum gap -- at `3.0.0_SA_CVO` as routed.
- Grades owed by CVO: limb 5 pass 5 is GREEN; R7 and R4-c sent 22:5xZ; the tree set (COO's message).
- **NFRA_COMPEFFICACY as the tree test** (Andrew pre-notice via COO 22:4xZ, NOT A GO): when his word comes,
  this seat runs `/endpoint --forward` on the foundational artifact -- CVO's ANDREW_DIRECT record
  `org/tier1_exec/3.0.0_SA_CVO/deliverables/ANDREW_DIRECT_20260902_1715Z_COMPTOOL_EFFICACY_PROJECT.md`
  (the admitted `brief_ref` form) with CVO's PRD draft `NFRA_COMPEFFICACY_PRD_DRAFT_v0.1.md` @`0c7c172f57`
  beside it -- and the pipeline runs from step 2 under the tree, `org/missions/D11/NFRA/NFRA_COMPEFFICACY/`
  (D11's macro enum RATIFIED by Andrew at MSTR's terminal 22:3xZ). No register row exists: registration is
  `mkdir` + `project.json` in one commit (s.5), the index by COO's generator.
- Residuals on the manifest: investigations/ + cards/ lanes are ANY (Andrew's call); three flat TOs the
  retired walk-back had mis-resolved now refuse if re-touched; the watcher's per-row awk cost; both gate
  harnesses re-run against the generator's REAL output when the first tree project lands.
- `PRD_HEADER.status` enum: unadopted.
- CloudComp's ARMED item (pytest over `.tools/tests/` collects zero -- several files `SystemExit` at import):
  disarmed same-turn by its owner; remedy theirs; I am the lane's gate, cc'd.

Loop arming this session: ZERO crons; the inbox Monitor only. Wind-down on Andrew's word, not before.
