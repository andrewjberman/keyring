# AMGT_RESAPP task order -- `AMGT-rk-60` -- portal-cell worktrees are PROVISIONED with `portal/` checked out: `.tools/wk-provision.sh` adds the linked superproject worktree and, inside it, a linked worktree of the nested portal repository at the ref the issuance names, with a buildable `node_modules`; `/dispatch` Step 4 names it and the issuance says which ref

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-60</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~60</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this order builds one git-worktree provisioning script and names it in
  one skill step; it arms no cron, alarm, monitor or cadence, reads no schedule and writes none; the standing
  no-monitor moratorium is unaffected. (The round's gate ledger was read at the cut: comp-schedule 2026-09-18
  ~15:55Z scanned 5 of 5 carriers, C1=23 C2=6 C3=12 C4=21 C5=334, 25 gates armed -- none binds a .tools/ or
  .claude/ edit.)
comp-iam: DECLARED-NOT-APPLICABLE -- this order performs NO live AWS act: no invoke, no read, no Terraform, no
  deploy; every act is a local git operation on this device (worktree add/remove on the superproject and on the
  nested portal repository) plus a directory link. It grants no permission and provisions no cloud resource.
comp-adversary: DECLARED-NOT-APPLICABLE -- this is a task-order specification, not a produced artifact; the
  validator-context declaration applies to the worker's own deliverable at drain, not to the order that
  specifies it.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~60`.** Work ONLY in the worktree whose absolute path is given in your spawn
prompt. Your first act prints `git rev-parse --abbrev-ref HEAD` and tests that `org/`, `.tools/` and the paths in
section 3 exist; if any is absent, STOP with a BLOCKING row. Every Bash call begins
`export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~60;`. **NEVER RUN AN INSTALL** -- the script's default `link` mode
links the main tree's existing `portal/node_modules` and installs nothing; its `install` mode (`bun install
--frozen-lockfile` against the EXISTING `portal/bun.lock`) exists for a device with no main-tree `node_modules` and
is NOT exercised by this order.

## 1. THE CELL, inlined in full -- `AMGT-rk-60` (R14-T6; row `AMGT_RESAPP-Z-W31-S1`; process)

**The analysis row, verbatim (`ROUND_ANALYSIS.round13.md` s.4 @9c8e04cd9a, row R14-T6 `:146`):** *"W31-S1:
portal-cell worktrees provisioned with `portal/` checked out; the issuance says which"* -- serves process; co-sign
no. Chain T (tools). Carried by s.6 `:207` (*"W31-S1 -> T6"*).

**The row this cell closes, `AMGT_RESAPP-Z-W31-S1` (`INVESTIGATION_v1.md:8167-8191`, BLOCKING, ARMED, disarm owner
`2.0.0_SA_COO~Z`), verbatim in its two binding fields.** `spec_asserts` (`:8188`): *"The task order's first-act
instruction: 'tests that org/, .tools/ and the paths in section 3 exist; if any is absent, STOP with a BLOCKING
row.' Section 3's <paths> names portal/src/pages/SecurityAnalysis/ and portal/src/api/endpoints/amgt-lead-panel.ts
as surfaces this worker reads and writes, and AC1/AC2 both assume a real, buildable portal checkout under this
worktree."* `world_is` (`:8189`): *"Neither named portal path exists in this worktree -- portal/ is an unpopulated
gitlink (0 files, no package.json) because no .gitmodules URL mapping exists to init it and no supported mechanism in
.tools/ populates a portal checkout inside a linked worktree. This worker therefore STOPS per the order's own
first-act instruction rather than cloning/reconstructing portal content ... AC1 and AC2 are recorded FAIL against
their real expectation (their literal invocations return rc=0 but on an empty tree ...)."* The row's own disarm
shape (b) (`:8190`): *"the dispatching COO ensuring each portal-touching worker's linked worktree is created with
portal/ already checked out at the gitlink's recorded commit, before the next chain-A cell is issued."*

**THE MEASURED STATE, at HEAD (cite these lines; do not re-derive them from memory):**
- `.gitmodules` is 0 bytes; `git ls-tree HEAD portal` reads `160000 commit 2453a7b4c6b7ff91ea89db499890a9486265d1a0
  portal` (a gitlink with no URL mapping). The main tree's `portal/` is an independently-managed NESTED git
  repository (`git -C portal rev-parse --abbrev-ref HEAD` = `DEV`, HEAD `625a08887b` 2026-09-18 *"merge(portal DEV):
  pull-merge origin's admin-gate commit onto round 13's page work"*), `git -C portal status --short` empty,
  `package.json` and `bun.lock` present, `node_modules/` present. The gitlink's recorded commit is **6 commits
  behind** that HEAD (`git -C portal rev-list --count 2453a7b4c6..HEAD` = 6): round 13's page work is on `DEV`, not in
  the gitlink -- which is why *"the issuance says which"*: a worker provisioned at the GITLINK commit would edit a
  tree six commits stale.
- The nested repository ALREADY carries linked worktrees at exactly this shape (`git -C portal worktree list`, 12
  entries at the cut): `C:/tmp/wk-amgt-11-1/portal [wk-amgt_resapp-11-1-portal]`, `C:/tmp/wk-aggfix-1-3/portal
  [wk-aggfix-1-3-portal]`, and `C:/tmp/wk-amgt-10-1/portal ... prunable` -- the pattern is precedent, and the
  `prunable` entry is the failure mode this cell's `remove` verb retires (a superproject worktree torn down with its
  nested portal worktree left registered).
- A fresh linked superproject worktree (`git worktree add -b wk-<CODE>-<n> <path> HEAD`, `/dispatch` Step 4
  `.claude/skills/dispatch/SKILL.md:173-177`) creates `portal/` as an EMPTY directory (row `:8179`: *"`ls -laR
  portal` ... shows only '.' and '..'"*). `git worktree add` accepts an existing EMPTY directory as its path and
  refuses a non-empty one -- the nested worktree lands exactly where the gitlink sits.
- `.tools/` carries no worktree provisioner (`ls .tools` matches only `provision-path-shims.sh` and
  `sync-skills-to-worktree.sh`, the latter a retired LD-0088 skill mirror, `:40-45`). Step 4 of `/dispatch` is ONE
  bash line (`:176`) and says nothing about `portal/`.
- The estate's bun rule (`CLAUDE.md` Portal: *"resolve bun via profile, don't bake a path"*) and the banked lesson
  that `bun install` writes no npm shims so `npx tsc` runs a registry decoy (row `AMGT_RESAPP-Z-W31-S2` `:8193-8200`;
  `AMGT-rk-53` AC6 uses `./node_modules/.bin/tsc -b`): the provisioned `portal/` must resolve
  `./node_modules/.bin/tsc` by path.

**RULED, what you build (one script, one skill step):**
1. **`.tools/wk-provision.sh`** -- Git Bash 3.6.7-safe bash (`set -uo pipefail`, default utilities only, every
   path double-quoted: this device's checkout path carries a space). Verbs:
   - `provision <CODE> <n> --path <abs-path> [--portal-ref <commit-ish>] [--node-modules link|install|none]`:
     `git worktree add -b wk-<CODE>-<n> "<abs-path>" HEAD` (the base is HEAD, never a branch name -- Step 4
     `:179-183`), then the `portal` verb below into it. Prints `WORKTREE: <abs-path> branch=wk-<CODE>-<n> base=<sha>`.
   - `portal <worktree-path> [--portal-ref <commit-ish>] [--node-modules link|install|none]`: derives the MAIN
     worktree as the first entry of `git worktree list --porcelain` and the nested repository as `<main>/portal`
     (refuses if `<main>/portal/.git` is absent); reads the gitlink commit at the worktree's HEAD
     (`git -C <worktree> ls-tree HEAD portal`); resolves `--portal-ref` in the nested repository (default: the nested
     repository's own HEAD) and REFUSES (rc 2, nothing created) if it does not resolve; REFUSES (rc 2) if
     `<worktree>/portal` exists and is NOT empty (never overwrite); runs
     `git -C "<main>/portal" worktree add -b wk-<CODE>-<n>-portal "<worktree>/portal" <resolved-sha>` (the branch
     name derived from the superproject worktree's branch, `wk-<CODE>-<n>` + `-portal`); prints
     `PORTAL_REF: <ref> -> <sha>`, `GITLINK: <gitlink-sha> behind_ref=<git -C <main>/portal rev-list --count
     <gitlink>..<sha>>` and `PORTAL: <worktree>/portal branch=wk-<CODE>-<n>-portal`; then `node_modules` per mode:
     `link` (default when `<main>/portal/node_modules` exists) creates `<worktree>/portal/node_modules` as a directory
     link to the main tree's -- a junction via `cmd //c mklink /J` when `cmd.exe` is on PATH, `ln -s` otherwise (the
     one device-purpose branch, guarded by capability not by device name) -- and prints `NODE_MODULES: link -> <main>/portal/node_modules`;
     `install` runs `bun install --frozen-lockfile` inside `<worktree>/portal` with `bun` resolved from PATH and
     REFUSES if it is not (never a baked path); `none` does nothing. In every mode the verb ends by printing
     `TSC: <output of ./node_modules/.bin/tsc --version, or ABSENT>`.
   - `remove <worktree-path> [--portal-only]`: `git -C "<main>/portal" worktree remove --force "<worktree>/portal"`
     (the link is removed with the directory; a junction is unlinked, never recursed into), then
     then RECREATE the empty gitlink placeholder (`mkdir "<worktree>/portal"`, so the superproject's status reads clean,
     never `D portal`) and NEVER run `worktree prune` (a prune clears UNRELATED pre-existing prunable entries, which AC5
     forbids; `worktree remove` already drops its own entry) -- ISSUER REPAIR on row W60-S3, making section 1 agree with
     AC5's end-state; then -- unless `--portal-only` -- `git worktree remove --force "<worktree>"` (no prune). Prints `REMOVED: ...` lines and `PORTAL_WORKTREES_LISTING_PATH: 0 of N`
     (the nested repository's worktree list no longer carries the path).
   - `--self-test`: PURE and local arms with a printed denominator (`RESULT: <f> arm(s) failed of <n>`): (a) into a
     temp directory carrying an empty `portal/` subdirectory (a stand-in for a fresh superproject worktree, created
     with `mktemp -d` under the repository's `.scratch/`), `portal` provisions at the nested repository's HEAD:
     `portal/package.json` exists, `git -C <tmp>/portal rev-parse HEAD` equals the resolved ref, the branch is named
     as derived; (b) `--portal-ref no-such-ref-rk60` REFUSES rc 2 and creates nothing (the temp `portal/` stays
     empty); (c) a NON-EMPTY `portal/` REFUSES rc 2 (never overwrite); (d) `remove --portal-only` leaves the nested
     repository's `worktree list` without the path and the temp `portal/` empty; (e) `link` mode resolves
     `./node_modules/.bin/tsc --version` from inside the provisioned `portal/`. The self-test cleans up every
     worktree and branch it created (branches `wk-selftest-rk60-*-portal` deleted with `git -C <main>/portal branch
     -D`), and a self-test that cannot clean up FAILS its own last arm rather than leaving a `prunable` entry.
   Plain ASCII; `OK:`/`WARN:`/`ERROR:`/`REFUSED:` prefixes; never `2>/dev/null` on a read whose emptiness is a verdict.
2. **`.claude/skills/dispatch/SKILL.md` Step 4 (`:173-177`)** -- the one bash line becomes the script: *"Make the
   worktree yourself, from THE BRANCH YOU ARE ON, with `.tools/wk-provision.sh provision <CODE> <n> --path <path>`;
   for a PORTAL cell add `--portal-ref <ref>`, where `<ref>` is the value the issuance commit's `fanout:` data names
   as `portal_ref:` (the nested repository's `DEV` HEAD at the cut, never the gitlink commit, which is measured
   behind it -- row `AMGT_RESAPP-Z-W31-S1`, cell `AMGT-rk-60`); the drain tears a portal worktree down with
   `.tools/wk-provision.sh remove <path>` so the nested repository never carries a `prunable` entry."* The existing
   `git worktree add -b wk-<CODE>-<n> <path> HEAD` line stays in the text as what the script runs. Nothing else in
   the file moves (`AMGT-rk-58` appends one sentence to the grant paragraph `:208-224` of this same file -- a
   different hunk; do not touch that paragraph).

**What this cell does NOT change:** `.gitmodules` (stays empty; the row's disarm shape (a) is not taken -- the nested
repository is not a submodule and this order does not make it one); the superproject gitlink commit; the nested
repository's `DEV` branch or any of its existing worktrees; `worker.md`; any task order; `build_zip.py` (running it
in provisioning is `AMGT-rk-59`'s ruled alternative and is NOT taken). No live AWS act, no deploy, no vendor call.

**THE VALIDATION BAR (`C-VALIDATION-NAMES`, PRD v0.13 @1699960261 `:1652-1658`):** a process cell with no security
population; proven on a DRY RUN -- the self-test's temp directory and the `portal` verb run INTO THIS WORKER'S OWN
WORKTREE (whose `portal/` is the empty gitlink directory the row measured), then removed by the same script's
`remove --portal-only` so the COO's drain finds a clean worktree. Nothing is pushed, nothing is committed under
`portal/`. `C-PRODUCTION-HOME` (`:1643-1650`): the script reads no worker's folder; the nested repository and its
`node_modules` are the main tree's own.

## 2. WHERE THIS CAME FROM

**ROUND 14**, decomposition s.22 (cut by `2.0.0_SA_COO~Z`), on `1.0.0_SA_CTO~Z`'s L10 round-13 analysis
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/ROUND_ANALYSIS.round13.md` @9c8e04cd9a s.4 row R14-T6 (`:146`) and s.6
(`:207`); the row `AMGT_RESAPP-Z-W31-S1` (`surprise-channel/investigations/INVESTIGATION_v1.md:8167-8191`, filed
2026-09-17T20:30Z by `0.9.0_WK_AMGT_RESAPP~31`) and its sibling `AMGT_RESAPP-Z-W31-S2` (`:8193-8200`, the `npx tsc`
decoy, carried to `0.4.0_DT_ClientPlatform` by s.6 `:210` -- NOT this cell's). PRD v0.13 @1699960261:
`C-PRODUCTION-HOME` (`:1643-1650`), `C-VALIDATION-NAMES` (`:1652-1658`). `/dispatch` Step 4
(`.claude/skills/dispatch/SKILL.md:155-224`); `.claude/agents/worker.md:38-41` (the first-act bar the row obeyed).

## 3. SURFACES -- what you may read and write

<paths>
.tools/wk-provision.sh
.claude/skills/dispatch/SKILL.md
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~60/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-60.portal-worktree-provisioning.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL.** This block governs COMMITS. The `portal` and `remove` verbs write
  into YOUR OWN worktree's `portal/` directory (a nested-repository checkout, not a superproject file) and into the
  nested repository's `.git/worktrees/` bookkeeping; neither is committed by you, and nothing under `portal/` is
  granted for commit. A READ needs no grant (read `.claude/agents/worker.md`, `.tools/provision-path-shims.sh`,
  `.tools/sync-skills-to-worktree.sh`, the nested repository's `package.json` and `bun.lock` freely). Scratch is
  `<your worktree>/.scratch/` only; the self-test's temp directory lives there.
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~60 <0.9.0_WK_AMGT_RESAPP~60@opal.agent>" -F <msgfile> -- <paths>`
  (message file written by the Write tool). Never push, merge, rebase, `checkout --`, `stash` or `clean` -- in the
  superproject OR in the nested portal repository. The `.sh` passes `.tools/commit-gate.sh` inside safe-commit.
- **THE NESTED REPOSITORY IS SHARED.** Its `DEV` branch is checked out in the main tree; you never check `DEV` out
  elsewhere (a second checkout of one branch is refused by git and would be wrong anyway); every nested worktree you
  create is on its own `wk-...-portal` branch and is removed by you before you report.

## 4. BOUNDS

**NO LIVE AWS ACT, NO DEPLOY, NO VENDOR CALL, NO INSTALL** (link mode only). PORTAL: COMMIT NO for this order --
you edit nothing under `portal/`; the provisioned checkout is the ACT under test, not a surface. **THE PORTAL DEV
PUSH IS RESERVED.** **COLLECTION STAYS OFF.** **NO alarm, monitor, SNS/SES-send, notification or freshness
checker.** Secrets through `comp-secrets` only. No non-ASCII in anything you write. **PUSH: never.** Your work is
LOCAL; LD-0522 puts the push with `0.0.0_AB_MSTR~Z`.
**THE REFUSAL CLAUSE:** a criterion you cannot satisfy AS WRITTEN is REFUSED with its measurement and a row; never
repaired, widened, or satisfied by a route this order did not name -- in particular never by copying the main tree's
`portal/` files by hand and never by `git clone`.
**A COUNT BAR IS READ FROM THE LIVE STORE AT THE CUT and PRINTS its denominator** -- the nested repository's
worktree count (12 at the cut, one `prunable`) and the gitlink gap (6 at the cut) are re-measured at spawn; they may
have moved.
**LEAVE YOUR WORKTREE AS YOU FOUND IT:** AC5 removes the nested portal worktree you provisioned in AC2; a report
that leaves it registered is a FAIL of AC5.
**SURPRISE ROWS:** your row is `AMGT_RESAPP-Z-W60-S<k>`, `<k>` restarting at 1; `"project": "AMGT_RESAPP"` and
`"fabric": "site-z"` on every new row; append by textual splice inside the one fenced JSON array (never
re-serialize it) and never edit an existing row. **Found something off-task? APPEND ONE ROW AND KEEP WORKING.**

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; each runs under timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rk-60"><invocation>cd "$(git rev-parse --show-toplevel)" && bash .tools/wk-provision.sh --self-test 2>&1 | tail -25</invocation><expect>the final line reads "RESULT: 0 arm(s) failed of N" with N at least 6, the arms named above it covering: portal provisioned into a temp directory's empty portal/ at the nested repository's HEAD (package.json present, rev-parse HEAD equal to the resolved ref, branch named wk-selftest-rk60-<n>-portal); a bad --portal-ref refused rc 2 with the temp portal/ still empty; a non-empty portal/ refused rc 2; link mode resolving ./node_modules/.bin/tsc --version; remove --portal-only leaving the nested repository's worktree list without the temp path; and a final cleanup arm proving every branch and worktree the self-test created is gone</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-60"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import os, subprocess
wt = os.getcwd()
main = subprocess.run(['git', 'worktree', 'list', '--porcelain'], capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=30).stdout.splitlines()[0].replace('worktree ', '', 1)
print('main_tree', main, 'this_worktree', wt, 'distinct', os.path.normcase(main) != os.path.normcase(wt))
print('gitlink', subprocess.run(['git', 'ls-tree', 'HEAD', 'portal'], capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=30).stdout.strip())
print('portal_entries_before', len(os.listdir('portal')) if os.path.isdir('portal') else 'NO DIR', 'of 0 expected (the empty gitlink directory)')
r = subprocess.run(['bash', '.tools/wk-provision.sh', 'portal', wt], capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=110)
out = r.stdout + r.stderr
print(out.strip()[-1500:])
print('rc', r.returncode)
ref_lines = [l for l in out.splitlines() if l.startswith('PORTAL_REF: ')]
gl_lines = [l for l in out.splitlines() if l.startswith('GITLINK: ')]
print('portal_ref_line', len(ref_lines), 'of 1; gitlink_line', len(gl_lines), 'of 1')
print('package_json', os.path.exists('portal/package.json'), 'bun_lock', os.path.exists('portal/bun.lock'), 'security_analysis_dir', os.path.isdir('portal/src/pages/SecurityAnalysis'), 'lead_panel_endpoint', os.path.exists('portal/src/api/endpoints/amgt-lead-panel.ts'))
head_nested = subprocess.run(['git', '-C', 'portal', 'rev-parse', 'HEAD'], capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=30).stdout.strip()
head_main = subprocess.run(['git', '-C', os.path.join(main, 'portal'), 'rev-parse', 'HEAD'], capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=30).stdout.strip()
print('nested_head', head_nested, 'main_portal_head', head_main, 'equal', head_nested == head_main)
print('nested_branch', subprocess.run(['git', '-C', 'portal', 'rev-parse', '--abbrev-ref', 'HEAD'], capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=30).stdout.strip())
print('nested_status_lines', len(subprocess.run(['git', '-C', 'portal', 'status', '--short'], capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=60).stdout.splitlines()), 'of 0 expected')
"</invocation><expect>distinct True (this is a linked worktree, not the main tree); gitlink reads "160000 commit <sha> portal"; portal_entries_before 0 of 0 expected; rc 0 with portal_ref_line 1 of 1 and gitlink_line 1 of 1 (the GITLINK line prints behind_ref=N, 6 at the cut, re-measured); package_json True, bun_lock True, security_analysis_dir True, lead_panel_endpoint True -- the two paths row W31-S1 found absent now exist; nested_head equals main_portal_head (the default ref is the nested repository's own HEAD, never the gitlink commit); nested_branch wk-AMGT_RESAPP-60-portal; nested_status_lines 0 of 0 expected (a clean checkout)</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-60"><invocation>cd "$(git rev-parse --show-toplevel)/portal" && python -c "
import os, subprocess
print('node_modules_is_link_or_dir', os.path.isdir('node_modules'), 'bin_tsc', os.path.exists('node_modules/.bin/tsc'))
r = subprocess.run(['bash', '-c', './node_modules/.bin/tsc --version'], capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=60, shell=False)
print('tsc_rc', r.returncode, (r.stdout + r.stderr).strip()[-200:])
n = subprocess.run(['bash', '-c', './node_modules/.bin/tsc --version'], capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=60, cwd=os.path.join(subprocess.run(['git', 'worktree', 'list', '--porcelain'], capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=30).stdout.splitlines()[0].replace('worktree ', '', 1), 'portal'))
print('main_tree_tsc', (n.stdout + n.stderr).strip()[-200:], 'same_version', (r.stdout or '').strip() == (n.stdout or '').strip())
"</invocation><expect>node_modules_is_link_or_dir True and bin_tsc True (link mode reached the main tree's node_modules through the link); tsc_rc 0 printing "Version X.Y.Z" -- the compiler resolves BY PATH inside the provisioned portal, which is the resolution AMGT-rk-53 AC6 and every page cell use (never npx); same_version True against the main tree's own ./node_modules/.bin/tsc --version ISSUER REPAIR (2.0.0_SA_COO~Z, on row W60-S2): the shim at node_modules/.bin/tsc is a POSIX shebang script that native-Windows Python cannot CreateProcess (WinError 193), so both calls go through bash -c -- the resolution is still BY PATH inside the provisioned portal; a version printed through bash meets the criterion</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rk-60"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import io, subprocess
f = '.claude/skills/dispatch/SKILL.md'
now = io.open(f, 'rb').read()
head = subprocess.run(['git', 'show', 'HEAD:' + f], capture_output=True, timeout=30).stdout
print('mentions_wk_provision_now', now.count(b'wk-provision.sh'), 'at_head', head.count(b'wk-provision.sh'))
print('portal_ref_word_now', now.count(b'portal_ref:'), 'at_head', head.count(b'portal_ref:'))
print('worktree_add_line_kept', now.count(b'git worktree add -b wk-' + b'<CO' + b'DE>-<n> <path> HEAD'), 'of 1')
print('non_ascii_now', len(now) - len(now.decode('utf-8')), 'non_ascii_head', len(head) - len(head.decode('utf-8')))
s = io.open('.tools/wk-provision.sh', 'rb').read()
print('script_non_ascii', len(s) - len(s.decode('utf-8')), 'script_crlf', s.count(b'\r\n'), 'script_set_uo_pipefail', s.count(b'set -uo pipefail'))
d = subprocess.run(['git', 'diff', '--numstat', 'HEAD', '--', f], capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=30).stdout.strip()
print('skill_numstat', d)
"</invocation><expect>mentions_wk_provision_now at least 2 (provision and remove) with at_head 0; portal_ref_word_now at least 1 with at_head 0 ("the issuance says which"); worktree_add_line_kept 1 of 1; non_ascii_now equals non_ascii_head (the skill already carries non-ASCII glyphs and this order adds or removes none); script_non_ascii 0, script_crlf 0, script_set_uo_pipefail 1; skill_numstat shows the one file with added lines confined to Step 4</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-rk-60"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import os, subprocess
wt = os.getcwd()
main = subprocess.run(['git', 'worktree', 'list', '--porcelain'], capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=30).stdout.splitlines()[0].replace('worktree ', '', 1)
nested = os.path.join(main, 'portal')
before = subprocess.run(['git', '-C', nested, 'worktree', 'list'], capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=30).stdout
print('nested_worktrees_before', len(before.splitlines()), 'listing_this_path', sum(1 for l in before.splitlines() if os.path.normcase(os.path.join(wt, 'portal')).replace(os.sep, '/') in os.path.normcase(l).replace(os.sep, '/')), 'of 1')
r = subprocess.run(['bash', '.tools/wk-provision.sh', 'remove', wt, '--portal-only'], capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=110)
print((r.stdout + r.stderr).strip()[-800:])
print('rc', r.returncode)
after = subprocess.run(['git', '-C', nested, 'worktree', 'list'], capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=30).stdout
print('nested_worktrees_after', len(after.splitlines()), 'listing_this_path', sum(1 for l in after.splitlines() if os.path.normcase(os.path.join(wt, 'portal')).replace(os.sep, '/') in os.path.normcase(l).replace(os.sep, '/')), 'of 0', 'prunable_entries', after.count('prunable'))
print('portal_dir_exists', os.path.isdir('portal'), 'portal_entries', len(os.listdir('portal')) if os.path.isdir('portal') else 'NO DIR', 'of 0')
print('main_node_modules_intact', os.path.isdir(os.path.join(nested, 'node_modules')), 'main_package_json', os.path.exists(os.path.join(nested, 'package.json')))
print('superproject_status', subprocess.run(['git', 'status', '--short', '--', 'portal'], capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=30).stdout.strip() or '(clean)')
"</invocation><expect>nested_worktrees_before N with listing_this_path 1 of 1; rc 0; nested_worktrees_after N-1 with listing_this_path 0 of 0 and prunable_entries equal to the pre-existing count (the removal registers no new prunable entry; the pre-existing C:/tmp/wk-amgt-10-1/portal prunable entry, if still present at spawn, is reported, not pruned by you); portal_dir_exists True with portal_entries 0 of 0 -- the worktree is back to the empty gitlink directory the COO's drain expects; main_node_modules_intact True and main_package_json True (removing the link never touched the main tree's node_modules); superproject_status (clean)</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** No judgment criterion on this
order. Order of execution is fixed: AC1 (self-test, temp directory), AC2 (provision into YOUR worktree), AC3 (tsc by
path), AC4 (the skill and the script's bytes), AC5 (remove, last). Commit the script and the skill edit AFTER AC5.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~60/AMGT_RESAPP.TO-AMGT-rk-60.portal-worktree-provisioning.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json`, graded by YOUR WORKTREE'S OWN
`python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4,AC5` (rc 0 is the verdict); flip `<status>` to
`complete`; commit with `--only -- <paths>`. Report once, quoting AC2's `PORTAL_REF:` and `GITLINK:` lines so the COO
can name `portal_ref:` in the issuance data for the page cells.

**MUTATION DISCIPLINE:** snapshot WORKING-TREE BYTES to `.scratch/` before editing. Never `git checkout --`,
never `git stash`, never `git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>pending</status>
<round>14</round>
<slot>~60</slot>
<fabric>site-z</fabric>
