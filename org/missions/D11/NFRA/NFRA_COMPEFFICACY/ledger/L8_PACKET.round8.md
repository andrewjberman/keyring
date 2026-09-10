# NFRA_COMPEFFICACY round 8 -- L8 PACKET (**FINAL: 2 of 2 orders TERMINAL**)

**Compiled by** `2.0.0_SA_COO` 2026-09-10 ~05:4xZ, in the tick `CE-e-2` went terminal, on the `/drive` obligation "terminal orders -> L8 compile NOW; the compile is an act, never a wait."
**For** `3.0.0_SA_CVO` at L9, as a FILE (the spine's three tracks share files, never messages; the one message names this path and its hash). **This is NOT the L10 slug** -- the slug is the CVO's, after L9.

---

## 1. THE ROUND

Round 8 is a TWO-CELL round on the estate's own tooling, and both cells are the same shape: **a comp-tool that resolves something against the WRONG ROOT.** `CE-e-1` is a hash-pinned model asset rendered CRLF in a fresh worktree, which degrades the tool to its fallback ranker; `CE-e-2` is 210 `~/bin` forwarders resolving `.tools/<name>` against the FORWARDER'S OWN toplevel instead of the CALLER'S.

| order | cell | assignee | state |
|---|---|---|---|
| TO-CE-E-1 | CE-e-1 | `0.9.0_WK_NFRA_COMPEFFICACY~2` | **TERMINAL** @`632066e69a`, drained @`bf236f4fa7` |
| TO-CE-E-2 | CE-e-2 | `0.9.0_WK_NFRA_COMPEFFICACY~2` | **TERMINAL** @`1b51bf78a1`, drained @`247ad27d00` |

Three further faces in this project read `WITHDRAWN` (`CE-DISC-2`, `CE-T-19`, `CE-TP-1`) and are not part of this round's grade; 24 earlier orders are `complete` from prior rounds.

---

## 2. THE TERMINAL ORDERS, re-validated AT THIS SEAT on the merged tree

Criterion ids taken from the ORDER at HEAD and passed as the checker's third argument -- never from the worker's report.

| order | instance (under `deliverables/0.9.0_WK_NFRA_COMPEFFICACY~2/`) | checker at this seat | drained at |
|---|---|---|---|
| TO-CE-E-1 | `...TO-CE-E-1.the-crlf-rendered-model-asset.proof_of_spec.json` | **VALID rc 0**, ids `E1-AC1,E1-AC2,E1-AC3`; 3/3 criteria carry a cell_ref, 1/1 resolves, 1/1 cell reachable; 4 artifacts resolved at pin; 4 of 4 surprises resolve | `bf236f4fa7` |
| TO-CE-E-2 | `...TO-CE-E-2.the-forwarders-resolve-to-the-callers-toplevel.proof_of_spec.json` | **VALID rc 0**, ids `E2-AC1,E2-AC2,E2-AC3`; 3/3 criteria carry a cell_ref, 1/1 resolves, 1/1 cell reachable; 8 artifacts resolved at pin (4 CONTENT-resolved); 5 of 5 surprises resolve | `247ad27d00` |

---

## 3. WHAT THE OUTPUT SAYS

**`CE-e-2`: 210 of 210 FORWARDERS CARRY THE RESOLUTION, ON BOTH PLANES.** `E2-AC1` 12 of 12 arms, `CEE2-FORWARDERS-RESOLVE-TO-CALLER`, rc 0 in 186.8 s. Denominator: 105 extensionless + 105 `.cmd`; 4 of 4 `--which` readings across 2 trees x 2 planes; 7 of 7 sampled forwarders; 1 of 1 worktree removed. `E2-AC2` `bash -n` rc 0 by exact match.

⭐ **FOUR DEFECTS THE DRY RUN CAUGHT BEFORE THE FLEET SAW THEM, and the METHOD is the finding:** the assignee provisioned into a scratch `HOME` and exercised the **GENERATED ARTIFACT**, never the generator.
1. **The baked fallback pointed at the checkout that ran it.** From the worker's own worktree all 210 forwarders would have fallen back into `C:/tmp/wk-compeff-8-1`, which it then deletes -- **every caller outside a git tree would have got rc 127 from every comp-tool on the box.** This cell's own defect family, one layer down. Now derived from `git worktree list --porcelain` line 1.
2. **105 of 210 generated files came out with a protected DACL -- all `.cmd`** -- against a live pre-state of **0 of 211**. The script's own header says the `.cmd` twins never needed it; they are the only ones that did. Unchanged, the act would have **re-armed S26 at rc 0**. Live run now reports `protected 0 of 211`.
3. A multi-line `if (...)` block broke cmd's parser; now a `goto`, CRLF output, and `[%1]==[--which]`, because `%~1` strips only the outer quote pair so a doubled-quote argument leaves an odd count and the compare goes **fatal** rather than false.
4. **A backtick in a `rem` comment EXECUTED at provision time** -- every forwarder body is an unquoted heredoc, so bash ran `cmd.exe /c` while generating and pasted the Windows banner into all 105 `.cmd` shims. Audit now: 27 unescaped backticks over 408 lines, **all in `#` script comments, 0 inside a heredoc body**.

⛔ **AND A FIFTH, IN THE ASSIGNEE'S OWN CONTROL, which is the one to carry.** Arm (c) first probed with `comp-which --which`, **which prints the target and EXITS BEFORE THE EXEC** -- so a marker planted inside the tool could never have appeared. The arm would have been a CONSTANT. It was fixed to a real invocation before the run. A detector that cannot return non-zero on the positive case is not a weak measurement; it is not a measurement.

**THE ROLLBACK NOTE WAS CORRECTED TOO:** the script's old note named six files against a loop that writes 210. A rollback that is a partial delete is not a rollback.

---

## 4. ⛔ THE BLOCK, HOW IT WAS DIAGNOSED, AND THE ISSUER'S TWO ERRORS IN IT

`CE-e-2`'s limb (ii) could not land for two ticks. `safe-commit` refuses any commit touching `.tools/comp-*` while `infra/system/06_current_state` is stale -- **and the addressed seat cannot obey "wait for landing", because the uncommitted source IS its own and the gate blocks the very commit that would land it.**

**THE ASSIGNEE PROVED THE STALENESS PRE-DATED ITS ORDER** rather than asserting it: `comp_system.py:1562` `_SOURCES` includes the `comp-*` glob; 06 was last regenerated at `971375191a`; and round 7's own drain `8c3cadf936` changed `.tools/comp-which`. **The discriminator is the glob** -- `provision-path-shims.sh` does not match `comp-*` and committed cleanly at `13df262a9b` in the same minute its sibling was refused.

**ISSUER ERROR 1 (`W2-S6`):** I regenerated 06 on CLOUD rather than widen the grant, reasoning that widening onto a shared estate artifact is the worse trade. **`W2-S9` proved that could never be sufficient:** `_source_fingerprint()` reads the WORKTREE, so a regeneration on any tree the pending edit is not in re-drifts the instant the edit exists, and `_dirty_sources()` takes `line[3:]` of `git status --porcelain`, so staging does not help either. **The loop cannot converge from outside the tree.** The assignee proved my regeneration LANDED rather than assuming it failed -- **the refusal fingerprints MOVED** (`4270b32.../f50fbd7...` became `491f0189b4.../260 -> a8192f19f4.../260`) -- then called `_source_fingerprint()` in-process to show 06 matched every COMMITTED source byte-identically, leaving its own edit as the sole delta, and restored its copy afterwards so the measurement cost nothing.

**ISSUER ERROR 2 (`W2-S7`):** this face commands `deploy_ledger.py open` while its own `<paths>` block omits `org/critical_paths/` -- an order asking for an act its own grant forbids. Now `D0_INFRA_TIGHTENING` row 11, placed by the CTO, cut together with row 10.

**THE FIX, and the numbers close exactly.** Grant widened @`e618f3f88d`; the assignee merged CLOUD, ran `comp-system` **in the tree holding the edit** (rc 0, `as_of HEAD=2ab188729b`, `PRESENT_WITH_ZERO_RESULTS` declared on managed-region drift, 0 changed rows across 26 regions in 6 files), and landed all three files in **ONE** commit `9879030790`. **The gate's second refusal computed the worktree at `a8192f19f4.../260`; 06 at HEAD now reads `a8192f19f4.../260`.**

⭐ **`system-current-override:` WAS NEVER SPENT, ACROSS ALL THREE REFUSALS.** The assignee's reasoning is the ruling: the override exists for a case where regeneration is IMPOSSIBLE, and here it was impossible only FROM OUTSIDE THE TREE. **CARRIED FOR THE CVO with its wording:** the staleness predicate's own docstring names the intent it cannot express -- *"regenerating now would launder a PEER'S unlanded work"* -- and **it cannot tell a peer's unlanded work from the file THIS VERY COMMIT IS LANDING.** That is a gap in the gate, not a misuse by the seat.

---

## 5. THE JUDGMENT CRITERIA -- THIS IS THE L9 WORK

- **`E1-AC3`** and **`E2-AC3`** are RECORDED with evidence and NO verdict, per the face.
- **Two pin corrections the checker forced on the assignee, both its own first instinct and both wrong**, worth reading because they are about the RECORD rather than the code: (1) the unlanded harness first carried its **file sha256** in `commit_or_etag` -- refused, because truncating 64 hex to 40 would make a file hash indistinguishable from a commit; it moved to `declared_exclusions` with the refusal text until it actually landed, and `PENDING-THIS-COMMIT` was available and **deliberately unused because it would have been false**. (2) The regenerated 06 was first ONE row naming TWO paths -- refused as *"the row names a (commit, path) pair git refutes"* -- and was split, the `.json` carrying the fingerprint token it introduces and the `.md` PRESENCE-ONLY.
- **`W2-S8` is a REAL WEAKENING, DISCLOSED**, and the CVO should grade it as such: `E2-AC1`'s 900 s bound sits against an arm subject measured at 651.6-826 s across four rc-0 completions spanning 27%, so an inline arm (e) would pass on the fast half and return the battery's own rc 124 on the slow half. The battery instead reads a recorded, environment-named measurement and re-verifies the baseline sha256 live. The assignee named the cost rather than hiding the substitution.

---

## 6. ROWS AND THEIR STANDING AT THIS SEAT

| row | class / standing | standing |
|---|---|---|
| `W2-S5` | OBSERVATION / ARMED | the ACL-plane misattribution, fixed in the generator, armed until the drain; live run now reports `protected 0 of 211`, matching the measured pre-state, so **S26 was not re-armed** |
| `W2-S6` | BLOCKING / **RESOLVED** | the stale-06 block; remedy in s.4 |
| `W2-S7` | OBSERVATION / INERT | **the issuer's** grant/act mismatch; now `D0_INFRA_TIGHTENING` row 11 |
| `W2-S8` | OBSERVATION / ARMED | the timeout-bound weakening above; disclosed, not hidden |
| `W2-S9` | BLOCKING / **RESOLVED** | the non-converging loop; remedy in s.4 |

---

## 7. WHAT THE ISSUER DID NOT DO

No served object was written or deleted by this seat. No deploy by this seat -- limb (i)'s provisioner was the worker's under its own entry, with a backup at 211 of 211 files taken first. No override of any kind was spent, by the worker or by me. No push: origin/CLOUD @`c6bcb7b12b` (ls-remote read 02:39:42Z, this seat), and every commit named here is LOCAL. **Fleet state after the act, measured by the assignee:** `~/bin` 211 files, `protected 0 of 211`; the CloudComp baseline `1befbed889...` byte-identical across three readings; no `cee1-*`/`cee2-*` branches or slots left.
