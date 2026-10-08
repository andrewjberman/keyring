# Pre-write refusal patterns -- every check in this workspace that refuses before a write lands

**Author:** 4.0.0_SA_CRO. **Date:** 2026-10-08. **For:** 2.0.0_SA_COO~G, re msg 106953 (LGIC_BLANKFIX round 6, item E5).
**Question:** what past patterns exist for a check that refuses BEFORE a name is written: where each lives, what it
refuses, how it is bypassed, and how it has failed.
**Method:** read on the laptop's shared tree at CLOUD HEAD 20832e4476. Installed hooks were read in `.git/hooks/`
(core.hooksPath points there), harness hooks in `.claude/settings.json`, `.claude/settings.local.json` and the user
`~/.claude/settings.json`. Failures are cited from the gates' own incident comments, from git, and from the audit logs.
[READ] = read in a file or counted. [INFER] = reasoning. A row says ABSENT where no failure record was found; ABSENT
does not mean none happened.

**Audit-log counts used below** [READ], from `org/git-author-override-audit.log` (41,996 rows, every writer combined):
PASS 38,770; BLOCK 1,169; OVERRIDE 848 (300 since 2026-09-08); MERGE-REFUSED 313; FORCE-BYPASS 241;
SYSTEM-CURRENT-OVERRIDE 167; WARN 127; NEVER-OVERRIDE 41. From `org/mcp/naming-gate-verdicts.log` (since 2026-09-15):
NAMING REFUSE lines 9,487 (5,837 under ENFORCE, 3,422 under WARN); gate-level `NAMING-GATE: REFUSE` under ENFORCE: 82.

---

## Census

Mode: BLOCK = the write stops; WARN = it prints and the write goes on; BY-READING = no mechanism; UNWIRED = the script
exists but nothing calls it on this box.

| # | Mechanism | Lives at | Fires when | Refuses what | Bypass / override | Known failure (cite) | Mode |
|---|---|---|---|---|---|---|---|
| 1 | pre-commit stage 1: COMP branch isolation | `.git/hooks/pre-commit:31-62` | every `git commit` with staged paths | a COMP-fabric author off branch COMP (except an all-`.claude/skills/**` commit); a non-COMP author on COMP | `--no-verify` (see row 23) | ABSENT | BLOCK [READ] |
| 2 | Missing-script sentinels in the pre-commit orchestrator | `.git/hooks/pre-commit:89-213` | the checker script for stages 5-12 is missing while a matching path is staged | the commit (FAIL-CLOSED) | none; stages 2-4 (owned-paths, mstr-ledger, branch-content-isolation) silently skip if their script is missing (`:73-87`) | ABSENT | BLOCK for 5-12; silent skip for 2-4 [READ] |
| 3 | Owned-paths lane check | `.tools/git-hooks/owned-paths-check.sh:116-268`, rules in `.tools/owned-paths-validate.py` + `.owned-paths.yaml` | every commit | a staged path outside the author's lane, or outside the `<paths>` of the worker's open task order | `GIT_COMMIT_AUTHOR_OVERRIDE=<LANE>` (audited, value not validated: CLAUDE.md 14a); `OWNED_PATHS_MODE=warn` env downgrades to WARN (`:116`); MERGE_HEAD exempts the whole commit (`:130-160`); unset author name = WARN and pass (`:222`) | (a) the merge exemption NEVER FIRED in production because a test-seam guard was the production condition, inverted (`:150-158`); (b) a linked worktree wrote its audit rows into its own gitignored copy, which died with the worktree (`:98-99`). Override use: 848 rows, 300 in the last 30 days | BLOCK [READ] |
| 4 | TO proof-of-spec issuance lint | `.git/hooks/pre-commit:130-135` -> `.tools/git-hooks/to-proof-of-spec-check.sh` | a NEW `task_orders/*.md` is staged | a new order with no `<proof_of_spec>` | `--no-verify`; checker body not read | ABSENT | BLOCK [READ wiring only] |
| 5 | Task-order pipeline gate, GATES (i)-(xii) and LIMB 6 | `.tools/to-pipeline-gate.py` (3,387 lines); called from `.git/hooks/pre-commit:155-165` AND from `.tools/safe-commit.sh` (TO limb after `:782`) | a staged task-order file | a NEW tree order missing issued_to / issued_by / non-empty `<paths>` / `<placeholders>` / risk class; a second issuer in a round; an order against a PRD with an unsigned half (LIMB 6) | `# pipeline-override: <reason>` in the order (`:63`), which does NOT lift LIMB 6 (`:738`); prospective only (a MODIFIED order is graded only by GATE viii); MERGE_HEAD exemption (`:836-851`) | THE ARGV CLIFF: past ~320 staged paths python failed to start (rc 126) on exactly the gates that carry the merge exemptions; fixed by passing STAGED by env (`.git/hooks/pre-commit:156-161`, 0.0.0_AB_MSTR msg 94338) | BLOCK [READ] |
| 6 | Surprise-channel row gate | `.tools/surprise-row-gate.py` (3,758 lines); `.git/hooks/pre-commit:174-181` | a staged surprise-channel row file | a NEW investigation row without `spec_asserts` + `world_is`; a remediation row without a valid route/loop_target; a foreign row the surfacer holds no order for | `# surprise-row-override: <reason>` (`:127`); PROSPECTIVE (only new row ids graded, so about 190 legacy rows never are: pre-commit `:171-172`); per-row MERGE exemption (`:289-326`) | same ARGV cliff as row 5 (pre-commit `:175-176`) | BLOCK [READ] |
| 7 | Project-tree validator and its round-close gate | `.tools/git-hooks/missions-tree-check.sh` | `org/missions/D<n>/**` or `org/projects/*.json` staged | validator: refusals R1-R5, ROW-*, INDEX-* (BLOCK on rc 1 or 2); close gate: a `dep_stage` change that fails its check | close gate is WARN unless `org/mcp/seat-gates.round-close.missions-tree-check.enforce` exists (absent on this box); `SEAT_GATES_OVERRIDE` audited (`:100-102`); `OPAL_SEAT_GATES_ENFORCE_DIR` env moves where the switch is looked for (`:74`) | ABSENT | validator BLOCK; close gate WARN [READ] |
| 8 | Law lock (CLAUDE.md, org/XXX.md) and byte budgets | `.tools/git-hooks/law-lock-check.sh` | either locked file staged | the commit unless `ANDREW_LAW_EDIT_ORDER` names a record; a file over budget that grows | the order check is FILENAME SHAPE plus EXISTENCE only: any `org/**/ANDREW_DIRECT_*.md` on disk, or staged in the same commit, passes (`:72-79`); whether it orders THIS edit is by reading | ABSENT | BLOCK on shape, BY-READING on content [READ] |
| 9 | One writer per append-only file | `.tools/git-hooks/one-writer-check.py` | a staged surprise-channel or `*-audit.log/.jsonl` file | a file whose `.<device>` suffix names another box | unsuffixed file from another box = WARN "until C-QUEUE" (`:12`); unresolved box = WARN (`:13`); MERGE exempt (`:14`) | ABSENT | BLOCK on foreign suffix, else WARN [READ] |
| 10 | Mass-deletion check (the installed commit-msg hook) | `.git/hooks/commit-msg` -> `.tools/git-hooks/mass-deletion-check.sh` | more than `MASS_DELETE_THRESHOLD` (25) tracked deletions | unattributed mass deletion | `FORCE_DELETE` override, audited as FORCE-BYPASS (`:189-191`); threshold is an env var | the WARN-ramp end epoch was 2 days in the past, so the gate went live BLOCKING while its message said WARN; the 10/10 test matrix forced the mode explicitly and never ran the default (`:68-82`) | BLOCK [READ] |
| 11 | Commit-message ASCII check | `.tools/git-hooks/commit-msg-ascii-check.sh`, installer `install-commit-msg-ascii-check.sh` | would fire on commit-msg | non-ASCII in a commit message | `ASCII_OVERRIDE="<reason>"` audited | NOT WIRED on this box: the installed `.git/hooks/commit-msg` runs only mass-deletion-check and carries no `commit-msg.chained-ascii` link | UNWIRED [READ] |
| 12 | pre-push -> safe-deploy | `.git/hooks/pre-push` -> `.tools/git-hooks/pre-push-safe-deploy.sh` -> `.tools/safe-deploy.sh` | a push carrying gold/silver/bronze scripts | a push whose scripts are not deployed and SHA-matched in S3 | `--allow-stale --reason`; FAILS OPEN with a WARN if the delegate script is missing (`pre-push:5-8`); fires only on push, which only MSTR does | ABSENT | BLOCK, fail-open on missing script [READ] |
| 13 | safe-commit refusals before staging | `.tools/safe-commit.sh:141-267, :478-620` | every commit made through the wrapper | no `-F/-m/-C` flag; a merge in progress (no override offered, `:233`); a sensitive file matched by a directory pathspec; contaminating staged files; a log commit that deletes non-log paths | `SAFE_COMMIT_ALLOW_SENSITIVE`, `--force` (contamination only), `SAFE_COMMIT_ALLOW_LOG_DELETIONS`, all audited | ABSENT (MERGE-REFUSED: 313 audited refusals) | BLOCK [READ] |
| 14 | Universal commit gate (py_compile, ruff, lints, ds-precommit) | `.tools/safe-commit.sh:696-731` -> `.tools/commit-gate.sh` -> `commit_gate_runner.py` | in-scope `.py/.sh/.tf/org/projects/*.json` | a file that fails compile, ruff or a lint; ZERO checks run on a declared file | none (`--force` does not bypass, `:709`) | before 2026-07-09 the gate blocked only on the queue-worker and pre-push paths; a ruff-F541 `.tools/*.py` landed through safe-commit (18c92b9ac) (`:696-703`) | BLOCK, wrapper path only [READ] |
| 15 | Cross-firm bucket and key-prefix lists | `.tools/ds-precommit-check.py:69-117` (GENERATED from `infra/logic/registry` by `lib/opal_naming.py generate`), checker `:633` | a `.py` under a home dir in the map, via row 14 | a string constant naming a foreign firm's bucket or key prefix | none named; the map has TWO home dirs only (`data/black_diamond/`, `data/cot/`), so a script anywhere else is not checked; only AST string constants are read, so a name built at run time is not seen [INFER] | THE GUARD BANNED ONE POPULATED PREFIX AND PERMITTED THE OTHER: `blackdiamond/49financial/` (8,862 objects) passed while `49f/` blocked, until 2026-08-27; also `opal-data-49financial` was missing from the cot bans (`:60-66, :79-104`) | BLOCK [READ] |
| 16 | LGIC naming limb at commit (LGIC_ENFORCE DEC-6) | `.tools/safe-commit.sh:740-780` -> `.tools/naming-gate.py` -> `lib/opal_naming.py grade()` | ADDED lines in staged `.py .js .mjs .ts .tf .json .yaml .yml` | a NEW out-of-pattern or alias literal, a new hand-kept firm token, an edit to a GENERATED file | ENFORCE is on while `org/mcp/naming-gate.enforce` exists (tracked; flipped @d181e0ac5a, 2026-09-17, by 2.0.0_SA_COO~G); no named override env; a deliberate departure is an R20 register row (`naming-gate.py:114-123`); runs only in safe-commit, so a bare `git commit` never reaches it | DRIFT: CLAUDE.md rule 30 still says "WARN today"; the live mode is ENFORCE (82 gate-level refusals since). A registry that fails `validate()` grades nothing and errors (`naming-gate.py:34-37`) | BLOCK on this box [READ] |
| 17 | Naming builders `address()` / `name()` | `lib/opal_naming.py:1849, :2033` | when code calls the builder | an unknown scope, tier with no home, non-systems.json system, refused token in function/qualifier, unknown kind (ValueError / KeyError / RegistryError) | the builder only refuses for a caller that uses it; a hand-typed literal never calls it, which is why row 16 exists | ABSENT | BLOCK at call [READ] |
| 18 | Terraform `opal_name` module | `infra/aws/terraform/modules/opal_name/variables.tf:22-46`, `main.tf:39-51, :192-209` | `terraform plan` of a root that calls the module (29 files reference it) | non-kebab function/kind/qualifier; partial name; fifo on a non-queue kind; a scope not in `scopes.json`; an unknown or half-scoped exemption row | a resource that does not use the module is never checked here | the module comment records that a Terraform `check` block only warns and the plan proceeds, so fences use output `precondition` instead (`main.tf:104-105`) | BLOCK at plan [READ] |
| 19 | safe-apply: halt checkpoint, named-commit check, seat gates, naming limb (apply side) | `.tools/safe-apply.sh:36-268` -> `.tools/naming-apply-gate.py` | `safe-apply` of a root | a named-commit failure (exit 8); seat-gate refusal (apply-who, overlap); a planned name the module would not produce (ENFORCE, same switch file as row 16) | `SEAT_GATES_OVERRIDE` audited (`:138-158`); `TAGAUTHZ_OVERRIDE` (`:36`); an UNSCOPED apply is graded only on the pre-plan literals | ABSENT | BLOCK [READ] |
| 20 | safe-deploy seat gates | `.tools/safe-deploy.sh:47-167` | a DS deploy | named-commit failure; seat-gate refusal (exit 9) | `SEAT_GATES_OVERRIDE`, audited to a DIFFERENT log (`org/safe-deploy-bypass-audit.log`, `:141`); `--allow-stale` | ABSENT | BLOCK [READ] |
| 21 | safe-merge, the drain's refuser | `.tools/safe-merge.sh` | a worker drain | a merge the gates refuse on the merged index; a branch not carried (exit 5); stale merged paths (exit 6); another seat's open merge | a conflict is deliberately NOT aborted (exit 4); it grades with MERGE_HEAD present, so every gate's merge exemption applies (`surprise-row-gate.py:303-304` states this) | ABSENT | BLOCK [READ] |
| 22 | never-rules-gate (harness PreToolUse, Bash and PowerShell) | `.tools/hooks/never-rules-gate.sh` (769 lines), wired `.claude/settings.json` | every shell call | rebase or `pull --rebase` on a shared branch; bare `terraform apply/destroy`; `commit -m` with a backtick or `$(`; `git stash`; `git clean`; push/pull on a shared branch by a non-integrator | `# never-override: <reason>` on the same simple command, audited (41 NEVER-OVERRIDE rows) | (a) RV-0048 F-019: the marker anywhere in the command waived EVERY rule (`:175-185`); (b) `git -c pull.rebase=...` evaded the gate until 2026-08-05 (`:425-437`); (c) the terraform PATH shim it was modeled on never existed (`:8-21`) | BLOCK [READ] |
| 23 | (gap) `git commit --no-verify` | not matched by row 22 (0 occurrences of `no-verify` in it or in safe-commit) | -- | nothing: it skips rows 1-11 | -- | ABSENT as a gate [READ] | none |
| 24 | Comp-tool rail | `.tools/hooks/comp-tool-hud.sh:79, :203` | Bash/Grep/Glob repo search | a raw recursive repo search (DENY while `org/mcp/comprail-gate1.enforce` exists, which it does) | `# rail-checked: <why>`; `/freeform`; pipe-receiver grep; native Grep/Glob | ABSENT | BLOCK [READ] |
| 25 | Memory write guard | `.tools/hooks/memory-write-guard.sh` -> `memory_write_guard.py` | Write/Edit naming a memory dir | any memory file but MEMORY.md; MEMORY.md over 3 KB and growing | a parse failure ADMITS; the shell wrapper always exits 0 with stderr discarded (`:12-13`); a write through Bash is not a Write/Edit call [INFER] | ABSENT | BLOCK, fail-open [READ] |
| 26 | MSTR cannot write a Tier-2 seat | `.tools/hooks/mstr-no-tier2-writes.sh` | `send_message` | an MSTR message to a serial starting `0.` that is not Tier 0 | not read | ABSENT | BLOCK [READ header] |
| 27 | Destructive HEAD-move guard | `.tools/git-hooks/headmove-guard.sh` (a `git()` shell function sourced from `~/.bashrc`) | `git reset` to a divergent ref, `rebase`, `commit --amend` | discarding local-only commits | FORCE-HEADMOVE audited | PowerShell never sources `~/.bashrc`, and CLAUDE.md says agent shell profiles never load, so the shadow does not reach agent calls (`never-rules-gate.sh:24-26`) | effectively UNWIRED for agents [READ + INFER] |
| 28 | Bare inbox-watch blocker | `.tools/hooks/block-bare-inbox-watch.sh` | would fire on a relative-path watcher launch | a relative `inbox-watch.sh` launch | -- | NOT WIRED in any of the three settings files read | UNWIRED [READ] |
| 29 | BG seat fence | `.tools/hooks/bg-concierge-gate.sh` | would fire for serial 0.0.3_BG_BBGTerminal | writes outside an allowlist, Bloomberg download, prompt changes | -- | unwired on Andrew's word @4c179f1826 (LD-0580); before F8 an unresolved identity passed silently on all four classes (`:15-20`) | UNWIRED [READ] |

**Rows: 29** (27 mechanisms, 1 gap row, 1 sentinel pattern row).

---

## Patterns across rows

1. **A merge is the widest unguarded door.** [READ] Rows 3, 5, 6, 9 each exempt a commit while MERGE_HEAD exists, and
   row 21 grades the drain with MERGE_HEAD present, so the drain runs under every exemption at once. [INFER] A name
   that arrives through a merge is graded only by row 16 if the integrator commits through safe-commit, and not at all
   by the pre-commit stages.
2. **Where a refusal lives decides who it reaches.** [READ] Rows 14, 15 and 16 (compile, cross-firm, naming) live only
   in the safe-commit wrapper; a bare `git commit` skips them, `--no-verify` skips every git hook (row 23), and three
   built gates are not wired on this box at all (rows 11, 28, 29), plus one wired into a profile agents never load
   (row 27). [INFER] A pre-write naming refusal should be measured as "fires on the act", not "exists on disk".
3. **Enumeration-bound guards fail by a missing member.** [READ] Row 15 is the clear case: the guard is only as wide as
   its list, and it missed a populated firm prefix and a firm bucket until 2026-08-27; the map still has two home dirs.
   Row 22 enumerates command shapes and missed `git -c pull.rebase` and `--no-verify`. The fix that held was
   generating the list from the registry (row 15's GENERATED block), not hand-keeping it.
4. **The mode lives in a switch file, and the docs drift from it.** [READ] ENFORCE/WARN is read at run time from a file
   (rows 7, 16, 19, 24) or an env var (rows 3, 7). CLAUDE.md rule 30 says the naming gate is WARN; it has been ENFORCE
   since 2026-09-17. `OWNED_PATHS_MODE` and `OPAL_SEAT_GATES_ENFORCE_DIR` let a caller change the mode without an
   audited override.
5. **Tests that drive the override, not the default, pass while production fails.** [READ] Row 10 (ramp epoch in the
   past, 10/10 tests forced the mode) and row 3 (merge exemption tested only on the direct-invocation path) both
   failed this way. Row 22's universal-disarm bug was the same family: the override was tested, its reach was not.
6. **Overrides are routine, and only some prove anything.** [READ] 848 owned-paths overrides (300 in 30 days) and 241
   force bypasses are audited; row 8's override accepts any existing ANDREW_DIRECT file, including one staged in the
   same commit, so its audit row proves a file existed, not that Andrew ordered the edit. [INFER] A pre-write naming
   refusal needs an override whose value a consumer can reject (the R20 register row id is that shape).

Item E2 (a key ruling keyed on a file path breaks on a move) has precedents here [INFER]: rows 3, 9 and 15 all key on
path strings (lane paths, a `.<device>` suffix, a home-dir substring), and none follows a rename.

---

## Not read

- Bodies of `mstr-ledger-check.sh`, `branch-content-isolation-check.sh`, `rcg-manifest-check.sh`,
  `rcg-sweep-check.sh`, `pipescript-suite-check.sh`, `jq-ban-check.sh`, `to-proof-of-spec-check.sh` (wiring read only).
- `memory_write_guard.py` and `mstr-no-tier2-writes.sh` beyond their headers; `naming-apply-gate.py` beyond its header.
- Which writer produced the 241 FORCE-BYPASS rows (safe-commit `--force` and mass-deletion `FORCE_DELETE` share the
  log and the label).
- Hooks on dell1, dell2 and site Z; any `.git/hooks` in linked worktrees or in the portal submodule.
- Codex seats, which run no Claude harness hooks (org/XXX.md step 1b).
- No gate was exercised; every BLOCK above is read from code, not driven.
