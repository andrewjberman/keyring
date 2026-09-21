# AMGT_RESAPP task order -- `AMGT-rk-66` -- `.tools/wk-provision.sh`'s `cmd_self_test` stops running repo-wide `git worktree prune` against the REAL superproject and nested portal repos: the redundant superproject prune is deleted, and the nested prune is replaced by a SCOPED removal of exactly the self-test's own manufactured orphan admin entry, so every other seat's prunable registration survives a self-test run

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-66</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~66</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this order edits one repository tool script; it arms no cron, alarm,
  monitor or cadence, reads no schedule and writes none; the standing no-monitor moratorium is unaffected.
comp-iam: DECLARED-NOT-APPLICABLE -- this order performs NO live AWS act of any kind: no invoke, no read of a live
  policy, no Terraform, no deploy. Its only non-source effects are the self-test's own git worktree and branch
  create/remove operations in the local repositories, which the self-test cleans up itself.
comp-adversary: DECLARED-NOT-APPLICABLE -- this is a task-order specification, not a produced artifact; the
  validator-context declaration applies to the worker's own deliverable at drain, not to the order that
  specifies it.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~66`.** Work ONLY in the worktree whose absolute path is given in your spawn
prompt. Your first act prints `git rev-parse --abbrev-ref HEAD` and tests that `org/`, `.tools/` and the paths in
section 3 exist; if any is absent, STOP with a BLOCKING row. Every Bash call begins
`export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~66;`. **NEVER RUN AN INSTALL.**

STOP: **DO NOT RUN `bash .tools/wk-provision.sh --self-test` BEFORE YOUR EDIT.** At HEAD the self-test's own cleanup
runs a repo-wide `git -C <portal> worktree prune` that clears every prunable entry in the nested portal repo --
including entries belonging to OTHER seats, and including the very discriminator AC2 needs. Your baseline is the
STATIC count (AC1), never a run. Run the self-test exactly ONCE, after your edit, inside AC2's invocation.

## 1. THE CELL, inlined in full -- `AMGT-rk-66` (R16 item C2; the `W60-S3` hazard class, one level down)

**Lineage.** Row `AMGT_RESAPP-Z-W60-S3` (BLOCKING) measured that `.tools/wk-provision.sh`'s `remove` verb ran an
unconditional `git -C <main>/portal worktree prune`, clearing an unrelated pre-existing prunable entry, and deleted
the portal placeholder. **That defect is FIXED at HEAD** by commit `3795d4f487`: `cmd_remove` (`:200-248`) carries
no prune, and `:235` recreates the placeholder with `mkdir -p "$portal_dir"`. The round-14 L9 adjudication's s.4 item 7
(`ROUND14_L9_ADJUDICATION_20260921.md:116-120`) still calls W60-S3 "unrepaired" -- STALE at HEAD; this cell does not
touch that record. **What remains is the SAME hazard in the script's own self-test**, found by the round-16 candidate
census (`ROUND16_CANDIDATE_CENSUS_20260921.md` @a0d593560c item C2): `cmd_self_test` still prunes the real repos.

**THE MEASURED STATE, at HEAD (cite these lines; do not re-derive them from memory -- re-read and confirm first):**
- `cmd_self_test()` opens at `:250`; `local total=7` at `:262`; the scratch worktree paths `wt1`..`wt4` at
  `:264-267` and `orphan_portal="$tmp_base/orphan-portal"` at `:268`.
- ARM6 (`:348-381`) manufactures an UNRELATED prunable entry in the nested repo: `git -C "$nested" worktree add
  --no-checkout -b wk-selftest-rk60-orphan-portal "$orphan_portal" HEAD` (`:354`), then `rm -rf "$orphan_portal"`
  (`:355`) so git marks it prunable; it proves `remove` never prunes by checking that entry survives (`:367`); and it
  statically asserts `cmd_remove`'s body has no prune with
  `sed -n '/^cmd_remove()/,/^}/p' "$0" | grep -v '^[[:space:]]*#' | grep -q "worktree prune"` (`:377`).
- ARM7 cleanup (`:383-409`): `git worktree remove --force` on `$wt1`..`$wt4` (`:384-387`), THEN
  **`git worktree prune` (`:388`)** -- repo-wide on the superproject, REDUNDANT after the four explicit removals, and
  it MASKS a failed removal (a removal that silently failed leaves a prunable entry the prune then erases, so ARM7's
  own leftovers check never sees it). The comment block `:389-396` explains the next line. Then
  **`git -C "$nested" worktree prune` (`:397`)** -- it exists to clear ARM6's own manufactured orphan so the orphan's
  branch `wk-selftest-rk60-orphan-portal` can be deleted by the nested `branch -D` loop (`:402-404`; a branch still
  referenced by a prunable-but-unpruned admin entry is "used by worktree" to `branch -D`), BUT it also clears every
  OTHER prunable entry in the nested repo. The superproject branch loop is `:399-401`; `rm -rf "$tmp_base"` at `:405`;
  ARM7's leftovers check at `:407-409` (`git worktree list | grep -F -q "$tmp_base"` in both repos).
- **THE MEASURED DISCRIMINATOR, at this cut:** the superproject has **0 prunable of 27** worktree entries; the nested
  portal repo has **3 prunable of 12**. A self-test run at HEAD would clear the nested 3 to 0. A correct self-test
  leaves them at 3 (re-measure at spawn -- AC2 prints both counts; the number may have moved).

**RULED, what you build (one file, `.tools/wk-provision.sh`):**
1. **Delete `:388` (`git worktree prune`) outright.** ARM7's leftovers check (`:407-409`) is what catches a failed
   explicit removal; nothing replaces the prune on the superproject.
2. **Replace `:397` (`git -C "$nested" worktree prune`) with a SCOPED removal of exactly the orphan's own admin
   entry.** Locate it by reading every `"$(git -C "$nested" rev-parse --git-common-dir)"/worktrees/*/gitdir` file and
   selecting the ONE whose content points at `$orphan_portal` (the gitdir file names `<worktree path>/.git`; compare on
   a normalized path -- this box's git prints `C:/...` forward-slash paths while `$orphan_portal` may carry the same
   path in the MSYS `/c/...` form; normalize BOTH sides with `cygpath -m` or equivalent before comparing, and prove
   the match in AC2's output); remove ONLY that admin directory. If zero or more than one admin entry matches, the
   self-test must count that as an ARM7 FAIL with a message naming the count -- never fall back to a prune. The
   `branch -D` loops (`:399-404`) then run unchanged.
3. **Update the comment block `:389-396`** so it describes the scoped removal (and why a repo-wide prune is forbidden
   here: it clears other seats' prunable registrations), not the old prune.
4. **Add an 8th arm** and bump `local total=7` (`:262`) to `8`: a STATIC assertion that `cmd_self_test`'s OWN body,
   comments stripped, contains no `git ... worktree prune` INVOCATION. STOP: **ISSUER RULE AT THE CUT -- DO NOT REUSE
   ARM6's PLAIN-PHRASE GREP HERE.** Measured by `2.0.0_SA_COO~Z` at the cut:
   `sed -n '/^cmd_self_test()/,/^}/p' .tools/wk-provision.sh | grep -v '^[[:space:]]*#' | grep -c 'worktree prune'`
   counts **5** at HEAD, not 2 -- it also matches ARM6's banner (`echo "== ARM 6: no worktree prune runs ..."`), ARM6's
   own grep pattern (`grep -q "worktree prune"`) and ARM6's error echo, all inside `cmd_self_test`. A plain-phrase
   ARM8 would therefore FAIL ON ITS OWN LINES and on ARM6's, forever. Match the INVOCATION instead, anchored to a line
   that begins with `git`: `grep -cE '^[[:space:]]*git( -C [^ ]+)? worktree prune'` -- measured **2** at HEAD (exactly
   `:388` and `:397`), and it cannot match an echo, a banner or a grep pattern. Print `ARM8: PASS` / `ARM8: FAIL` in
   the house style. **No `git ... worktree prune` invocation anywhere in the file after your edit** (AC1 checks both
   the self-test body and the whole file).

**What this cell does NOT change:** `cmd_remove` (already fixed, `:200-248` -- read only); ARM1-ARM6's logic;
the provision verb; any other `.tools/` file; the round-14 L9 record's stale sentence (not your document).

**THE VALIDATION BAR (`C-VALIDATION-NAMES`, PRD v0.13 @1699960261 `:1652-1658`):** a process/tooling cell with no
security population; proven by the static assertion and ONE post-edit self-test run with before/after worktree
censuses on both repositories. No live AWS act, no vendor call.

## 2. WHERE THIS CAME FROM

**ROUND 16**, decomposition s.24 (cut by `2.0.0_SA_COO~Z`), on `1.0.0_SA_CTO~Z`'s round-16 rulings
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/ROUND16_CTO_RULINGS_20260921.md` @dcd88f0acc s.1 (*"C1, C2 ratified as
written"*); the round-16 candidate census
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/ROUND16_CANDIDATE_CENSUS_20260921.md` @a0d593560c item C2 (measured by a
read-only drafter at HEAD `9dd60b52c3`: the self-test body carries 2 `worktree prune` calls, `:388` and `:397`); the
row `AMGT_RESAPP-Z-W60-S3` and its repair `3795d4f487`. Andrew-direct ~14:58Z (record @9bf58c4b95): wide parallel
fan-out means more worktrees whose prunable registrations a self-test run would clear. PRD v0.13 @1699960261: no FWD
or `C-` contract is touched (tooling cell; no PRD addendum).

## 3. SURFACES -- what you may read and write

<paths>
.tools/wk-provision.sh
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~66/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-66.wk-provision-self-test-scoped-cleanup.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL.** A READ needs no grant (read `.claude/skills/dispatch/SKILL.md`,
  the round-14 L9 adjudication and the W60-S3 row freely); this block governs WRITES. The self-test's own scratch
  worktrees under `<your worktree>/.scratch/wkprov-selftest.*` and its own `wk-selftest-rk60-*` branches are created
  AND removed by the self-test itself -- they are not commits and must not survive AC2. Scratch is
  `<your worktree>/.scratch/` only.
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~66 <0.9.0_WK_AMGT_RESAPP~66@opal.agent>" -F <msgfile> -- <paths>`
  (message file written by the Write tool). Never push, merge, rebase, `checkout --`, `stash` or `clean`. Every `.sh`
  you commit passes `.tools/commit-gate.sh` inside safe-commit.

## 4. BOUNDS

**NO LIVE AWS ACT, NO DEPLOY, NO VENDOR CALL** -- none is named. PORTAL FROZEN (the portal repo's SOURCE is not your
surface; the self-test only creates and removes its own worktrees of it). **COLLECTION STAYS OFF.** **NO alarm,
monitor, SNS/SES-send, notification or freshness checker.** No non-ASCII added to anything you write. **PUSH: never.**
Your work is LOCAL; LD-0522 puts the push with `0.0.0_AB_MSTR~Z`.
**NEVER a repo-wide `git worktree prune`** -- not in the file, not by hand, not "to clean up" after a failed run. If a
self-test run leaves a `wk-selftest-rk60-*` entry or branch behind, remove THAT entry by name and file a row; a prune
would erase other seats' registrations and the discriminator with them.
**THE REFUSAL CLAUSE:** a criterion you cannot satisfy AS WRITTEN is REFUSED with its measurement and a row; never
repaired, widened, or satisfied by a route this order did not name.
**A COUNT BAR IS READ FROM THE LIVE STORE AT THE CUT and PRINTS its denominator** -- the prunable/entry counts (0 of
27 superproject, 3 of 12 nested at the cut) are re-measured by AC2's own BEFORE read; the bar is AFTER == BEFORE,
never a literal from this order.
**SURPRISE ROWS:** your row is `AMGT_RESAPP-Z-W66-S<k>`, `<k>` restarting at 1; `"project": "AMGT_RESAPP"` and
`"fabric": "site-z"` on every new row; append by textual splice inside the one fenced JSON array (never
re-serialize it) and never edit an existing row. **Found something off-task? APPEND ONE ROW AND KEEP WORKING.**

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; each runs under timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rk-66"><invocation>cd "$(git rev-parse --show-toplevel)" && echo "self_test_body_prune_invocations: $(sed -n '/^cmd_self_test()/,/^}/p' .tools/wk-provision.sh | grep -v '^[[:space:]]*#' | grep -cE '^[[:space:]]*git( -C [^ ]+)? worktree prune')" && echo "head_self_test_body_prune_invocations: $(git show HEAD:.tools/wk-provision.sh | sed -n '/^cmd_self_test()/,/^}/p' | grep -v '^[[:space:]]*#' | grep -cE '^[[:space:]]*git( -C [^ ]+)? worktree prune')" && echo "whole_file_prune_invocations: $(grep -v '^[[:space:]]*#' .tools/wk-provision.sh | grep -cE '^[[:space:]]*git( -C [^ ]+)? worktree prune')"</invocation><expect>self_test_body_prune_invocations: 0 (the working file, after your edit); head_self_test_body_prune_invocations: 2 printed beside it as the baseline (measured by the issuer at the cut with this ANCHORED form -- exactly :388 and :397; the plain-phrase grep counts 5 because ARM6's banner, grep pattern and error echo also contain the phrase, and it must not be used); whole_file_prune_invocations: 0 -- no git worktree prune invocation survives anywhere in the file. Run BEFORE AC2; this criterion never executes the self-test</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-66"><invocation>cd "$(git rev-parse --show-toplevel)" && M="$(git worktree list --porcelain | sed -n '1s/^worktree //p')" && census() { echo "$1 super_entries $(git -C "$M" worktree list --porcelain | grep -c '^worktree ') super_prunable $(git -C "$M" worktree list --porcelain | grep -c '^prunable') nested_entries $(git -C "$M/portal" worktree list --porcelain | grep -c '^worktree ') nested_prunable $(git -C "$M/portal" worktree list --porcelain | grep -c '^prunable')"; } && census BEFORE && bash .tools/wk-provision.sh --self-test 2>&1 | tail -30 && census AFTER && echo "leftover_selftest_branches super $(git -C "$M" branch --list 'wk-selftest-rk60-*' | wc -l) nested $(git -C "$M/portal" branch --list 'wk-selftest-rk60-*' | wc -l)"</invocation><expect>the self-test's final line reads "RESULT: 0 arm(s) failed of 8" with ARM1..ARM8 each printing PASS (ARM8 is the new static no-prune arm), and the output shows the scoped removal matched exactly ONE admin entry for the orphan (print the matched gitdir path); the AFTER census equals the BEFORE census on all four figures -- in particular nested_prunable AFTER == nested_prunable BEFORE (3 at the cut; re-measured here) and super_entries AFTER == super_entries BEFORE; leftover_selftest_branches super 0 nested 0. This is the ONE self-test run this order permits. CONCURRENCY QUALIFIER (issuer rule at the cut): three sibling round-16 workers run in their own worktrees of this same repository during your run, and other seats may add or remove worktrees too; their worktrees exist at BEFORE and AFTER, but if any super_entries or nested figure differs, print both porcelain listings, diff them, and grade on ATTRIBUTION -- a difference whose paths are all outside your self-test's own tmp_base and none named wk-selftest-rk60-* is concurrent activity, not a defect, and is recorded as such; a difference touching a wk-selftest-rk60-* entry, or a LOSS of any prunable entry that was present at BEFORE, is a FAIL</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-66"><invocation>cd "$(git rev-parse --show-toplevel)" && bash -n .tools/wk-provision.sh; echo "bash_n_rc $?" && python -c "
import io, subprocess
b = io.open('.tools/wk-provision.sh', 'rb').read()
h = subprocess.run(['git', 'show', 'HEAD:.tools/wk-provision.sh'], capture_output=True).stdout
print('working non_ascii_bytes', len(b) - len(b.decode('utf-8')), 'crlf', b.count(b'\r\n'))
print('head    non_ascii_bytes', len(h) - len(h.decode('utf-8')), 'crlf', h.count(b'\r\n'))
"</invocation><expect>bash_n_rc 0 (the script parses); working crlf 0 (LF only); working non_ascii_bytes EQUAL to head non_ascii_bytes, both printed side by side (measure, do not assume -- the bar is "this cell added none", never a literal zero)</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** No judgment criterion on this
order. AC1 and AC3 are static; AC2 is the single permitted self-test run, after the edit.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~66/AMGT_RESAPP.TO-AMGT-rk-66.wk-provision-self-test-scoped-cleanup.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json`, graded by YOUR WORKTREE'S OWN
`python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3` (rc 0 is the verdict); flip `<status>` to `complete`;
commit with `--only -- <paths>`. Report once, naming AC2's BEFORE and AFTER censuses verbatim and the matched orphan
admin-entry path.

**MUTATION DISCIPLINE:** snapshot WORKING-TREE BYTES to `.scratch/` before editing. Never `git checkout --`,
never `git stash`, never `git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>pending</status>
<round>16</round>
<slot>~66</slot>
<fabric>site-z</fabric>
