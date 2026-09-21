# AMGT_RESAPP task order -- `AMGT-rk-80` -- two Exec Management tab text fixes: the CEO line ends in exactly ONE period (it prints "was not run.." today), and the panel subtitle names the Bloomberg fallback when the served roster is the fallback; a RESOLVED roster's subtitle and every other element render byte-for-byte as today

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-80</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~80</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this order edits one portal tab, amends one check in one existing
  static-render harness and adds one new harness; it arms no cron, alarm, monitor or cadence, reads no schedule and
  writes none, and opens no deploy-ledger entry (it deploys nothing: no push, no DEV or PROD move).
comp-iam: DECLARED-NOT-APPLICABLE -- this order makes NO AWS call of any kind (its fixtures are AMGT-rk-78's
  committed captures, read-only); no role, policy or grant is read or changed, and no S3 object is read or written.
comp-adversary: DECLARED-NOT-APPLICABLE -- this is a task-order specification, not a produced artifact; the
  validator-context declaration applies to the worker's own deliverable at drain, not to the order that
  specifies it.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~80`.** Work ONLY in the worktree whose absolute path is given in your spawn prompt
(call it `<wt>`). Your first act prints `git rev-parse --abbrev-ref HEAD`, `git rev-parse --show-toplevel` and
`git -C portal rev-parse --abbrev-ref HEAD` from `<wt>`, and tests that `org/`, `.tools/`,
`portal/src/pages/SecurityAnalysis/tabs/ExecManagementTab.tsx`,
`portal/src/pages/SecurityAnalysis/__harness__/execFallback.harness.cjs` and `portal/node_modules/typescript` exist;
if any is absent, STOP with a BLOCKING row. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~80;`.
**NEVER RUN AN INSTALL.** Never read, show, diff or check out branch `wk-amgt-14-50` or `C:/tmp/wk-amgt-14-50` -- it
holds an exposed credential.

**YOUR PORTAL CHECKOUT, provisioned by the issuer before your spawn.** `<wt>/portal` is a PORTAL-REPO worktree on
branch `wk-amgt-20-80-portal`, checked out WITH `core.autocrlf=false` (so its files are LF, as the committed blobs
are -- row `AMGT_RESAPP-Z-W78-S1` is the CRLF checkout this prevents). Its base is chosen by the rule AC0 checks: portal
`origin/DEV` if DEV contains AMGT-rk-78's commit `95d96edb8f0a448c187b23d5d3e274a4fa01d0d2`, else that commit itself.
`<wt>/portal/node_modules` is a DIRECTORY JUNCTION to the main tree's installed packages. **The junction writes
through into a directory other seats depend on: it is NOT a write surface, and a package that reads ABSENT is a row,
never an install.** The superproject's `portal` gitlink NEVER moves (AC5).

## 1. THE CELL, inlined in full -- `AMGT-rk-80` (R20-C; row `AMGT_RESAPP-Z-S201`)

**The ruling, verbatim (CTO pre-ruling msg 24055, `1.0.0_SA_CTO~Z`, 2026-09-21 20:13:30Z, the S201 part):**
*"S201 (INERT), RULED -> R20-C, a portal cell:
- the double period "was not run.." (fix at whichever side appends the second ".");
- the "from the filing" subtitle over a Bloomberg-fallback roster must read as the fallback.
It is a DEV push; its PROD promote is under the standing word."*

**The row this cell answers, `AMGT_RESAPP-Z-S201`** (OBSERVATION, INERT, filed by `2.0.0_SA_COO~Z` from its
/frontend-dev screenshots of AMGT-rk-78's branch): the tab prints the CEO line with a DOUBLE full stop on every
NOT_SEARCHED name ("... so the CEO web search was not run.."), and the panel subtitle "Officers from the filing, with
tenure against the pool" is false over a Bloomberg-fallback roster (CSL, 6861).

**WHICH SIDE APPENDS THE SECOND PERIOD -- measured, and it is the PORTAL.** The served reason is AMGT-rk-75's
plain-English sentence and already ends in one period: every committed rk-78 fixture reads so --
`execFixture.CSL_AU_Equity.json` `ceo_profile_reading.reason` = "No verified company website was found, so the CEO
web search was not run."; `6861_JP_Equity` and `CAT_US_Equity` = "No officer on the roster has a chief-executive
title, so the CEO web search was not run.". The tab appends a literal "." after the reason UNCONDITIONALLY. **So the
fix is portal-side, and the served sentences are NOT changed by this cell** (they are PRD v0.16 C-EXEC-MANAGEMENT's
"readable reasons"; a sentence keeps its own period).

**THE MEASURED STATE, at portal `95d96edb` (= portal `origin/DEV` and the superproject gitlink at the cut; RE-READ every
line at your checkout before editing):**
- `src/pages/SecurityAnalysis/tabs/ExecManagementTab.tsx`, 234 lines, crlf 0, non-ASCII 0. `CeoProfile` `:82`. It
  appends "." after a reason at FOUR sites:
  - `:101` `not searched -- {reason}.`
  - `:108` `searched, nothing found -- {reason}.`
  - `:124` `search failed -- {reason}.`
  - `:130` `unreadable object -- {reading?.reading_basis ?? 'no reading basis recorded'}.`
  The CONFIRMED branch (`:88-96`) and SEARCHED_LINKS_UNREADABLE (`:113-120`) append nothing after a served value.
- The subtitle is a STATIC prop on the panel header, `:219`:
  `<PanelHeader title="Exec Management" subtitle="Officers from the filing, with tenure against the pool" />`, inside
  `ExecManagementTab`, where the served bundle is in scope as `data` (`data.management.roster_source`).
- `src/pages/SecurityAnalysis/__harness__/execFallback.harness.cjs` (AMGT-rk-78), 249 lines, crlf 0. Its check
  `resolved_unchanged` (`:161-176`) compares the sha256 of CAT's WHOLE rendered markup against the tab pinned at
  `db1c5f64`. **Measured in a probe: applying fix 1 makes it read `resolved_unchanged false` (CHECKS-WRONG-WAY), because
  CAT's CEO line legitimately loses its second period.** The same probe with the amendment in RULED item 3 reads
  `EXECFALLBACK CHECKS 5/5` with `ceo_lines_set_aside=2`. Its stub `PanelHeader` renders no props, so it cannot see the
  subtitle either way.
- `src/pages/SecurityAnalysis/__harness__/tabs.harness.cjs` reads IDENTICALLY before and after both fixes (probe: rc 1
  and the same `CHECKS-WRONG-WAY` line and `EXEC officers=48/48 pool_line=5/5` segment either way -- only the tab's own
  hash moves). Its baseline depends on the workspace root around the portal, so YOURS is measured at spawn (AC4).
- The tab sits in `Panel variant="mixed"` (the dark band); add no colour, no class, no component, no dependency.

**RULED, what you build (portal files only):**
1. **`ExecManagementTab.tsx` -- the period.** Add ONE helper directly above `CeoProfile`:
   `function endSentence(text: string): string { return /[.!?]$/.test(text) ? text : \`${text}.\` }`
   (with a two-line comment citing PRD v0.16 readable reasons), and at the FOUR sites above replace `{X}.` with
   `{endSentence(X)}`. A reason that ends in `.`, `!` or `?` renders once; one that does not gets exactly one period, as
   today. Nothing else in `CeoProfile` moves.
2. **`ExecManagementTab.tsx` -- the subtitle.** At `:219`, the subtitle becomes
   `data?.management?.roster_source === 'BLOOMBERG_FALLBACK' ? 'Officers from the Bloomberg fallback list -- the
   filing roster did not resolve' : 'Officers from the filing, with tenure against the pool'` (this exact fallback
   text is `2.0.0_SA_COO~Z`'s L5 wording, named for the CTO at issuance; ASCII `--`). Every other roster_source
   (FILING, null, absent, no data) keeps today's string byte-for-byte.
3. **`execFallback.harness.cjs` -- amend ONE check, nothing else.** In `resolved_unchanged`, set aside every
   `<p data-ceo-profile="...">...</p>` element on BOTH the edited and the pinned render before hashing
   (`html.replace(/<p data-ceo-profile="[^"]*"[^>]*>[\s\S]*?<\/p>/g, '')`), count the elements set aside
   (`countOf(..., 'data-ceo-profile=')` over both sides) and print `ceo_lines_set_aside=<n>` in the check's note, with a
   comment naming AMGT-rk-80 and row Z-S201 as the reason. Every other byte of that file, every other check, the pin
   `db1c5f64...` and the fixtures stay as they are. **This is the Z-S193 class, handled at the cut:** a later cell
   changed one element of a pinned comparison on purpose, so the comparison excludes exactly that element and the new
   harness grades it.
4. **A NEW harness `src/pages/SecurityAnalysis/__harness__/execText.harness.cjs`**, in rk-78's idiom
   (`ts.transpileModule` + `vm` + `react-dom/server` `renderToStaticMarkup`; the ACTUAL `ExecManagementTab`; stubs for
   `@/ui/components/panels`, `../hooks/useLeadPanelApi` (`useThesisBundle` hands back the fixture),
   `../components/IdentityLine`), whose `PanelHeader` stub RENDERS its `subtitle` prop into the markup. It reads rk-78's
   COMMITTED `execFixture.{CSL_AU_Equity,6861_JP_Equity,CAT_US_Equity}.json` READ-ONLY (never re-captured, never
   edited), writes NO file, and exits rc 0 only if every check holds. Checks, each printing its denominator:
   - `ceo_line_single_period` -- CSL, 6861, CAT: the CEO line ends in "." and not "..", and carries the fixture's
     reason (minus its final period) verbatim; "3 of 3 names";
   - `period_added_when_missing` -- the CAT fixture with its reason's final "." stripped IN MEMORY still renders exactly
     one closing "." (the other branch of the rule);
   - `subtitle_fallback` -- CSL and 6861 (fixture `roster_source` BLOOMBERG_FALLBACK): the subtitle names the Bloomberg
     fallback and differs from the old string;
   - `subtitle_resolved_unchanged` -- CAT (`roster_source` FILING): the subtitle equals the pinned tab's and the old
     string, byte-for-byte;
   - **`pinned_copy_discriminates`** -- the DISCRIMINATING ARM: load the tab from
     `git show 95d96edb8f0a448c187b23d5d3e274a4fa01d0d2:src/pages/SecurityAnalysis/tabs/ExecManagementTab.tsx` (PINNED BY
     HASH -- never HEAD, never a merge-base: a HEAD read names this cell's own code once it merges, row
     `AMGT_RESAPP-Z-S193`) and show that on the CSL fixture it renders ".." and the old subtitle;
   - a final `EXECTEXT CHECKS n/n` and, on any failure, `CHECKS-WRONG-WAY <names>`.
   **Measured in the issuer's probe:** the patched tab reads `EXECTEXT CHECKS 5/5`; the SAME harness against the
   UNPATCHED tab reads 3/5 with `CHECKS-WRONG-WAY ceo_line_single_period subtitle_fallback` -- so it discriminates.

**What this cell does NOT change:** anything under `lib/` or any served sentence (the reasons keep their own period;
another round-20 cell, AMGT-rk-79, owns the producer and the management objects); any S3 object; `types.ts`; the
committed fixtures; `tabs.harness.cjs`; any other check in `execFallback.harness.cjs`; the CONFIRMED and
SEARCHED_LINKS_UNREADABLE lines; `package.json` and every dependency. **No push, no DEV or PROD move, no gitlink move.**
If you find a served field this tab would need to render for the round-20 producer change (for example a new
roster-completeness field), do NOT render it: record it in your report as an open question for the issuer.

**THE VALIDATION BAR:** on the three names a manager opens first, the CEO line reads as one sentence with one period,
and the panel subtitle says where the officers came from -- the Bloomberg fallback for CSL and 6861, the filing
(unchanged) for CAT.

## 2. WHERE THIS CAME FROM

**ROUND 20**, decomposition s.28 (cut by `2.0.0_SA_COO~Z`), on `1.0.0_SA_CTO~Z`'s pre-ruling msg 24055 (confirmed in
its round-19 analysis). Row `AMGT_RESAPP-Z-S201`, surfaced from the round-19 screenshots of AMGT-rk-78's branch. PRD
v0.16 @2d0da569e7 C-EXEC-MANAGEMENT "readable reasons". Andrew-direct ~16:5xZ (record @c5532df80a): a functional
product ready for the managers' review; ~15:12Z: one slug per round.

## 3. SURFACES -- what you may read and write

<paths>
portal/src/pages/SecurityAnalysis/tabs/ExecManagementTab.tsx
portal/src/pages/SecurityAnalysis/__harness__/execFallback.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/execText.harness.cjs
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~80/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-80.exec-tab-text-fixes.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL.** Reads need no grant. `portal/node_modules` is a junction and NOT a
  write surface; `portal/.tsbuild/` (gitignored, written by `tsc -b`) is tolerated. Scratch is `<wt>/.scratch/r80/`
  only (never committed). The one exception to the walls is the typecheck control file in AC1, which the criterion
  itself creates and deletes; it must not exist at your completion.
- **Collision check, at the cut:** the other round-20 cells write `lib/research/management/` and management objects in
  S3 (AMGT-rk-79) -- **no round-20 cell but this one writes a portal path.** The held branch `wk-amgt-14-50` touches no
  portal path (names only). The only shared file is `INVESTIGATION_v1.md` (append-only; do not isolate it).
- **COMMITTING PORTAL WORK:** inside `<wt>/portal`, on branch `wk-amgt-20-80-portal`, with
  `git add -- <the portal files you changed> && git commit --author "0.9.0_WK_AMGT_RESAPP~80 <0.9.0_WK_AMGT_RESAPP~80@opal.agent>" -F <msgfile> -- <those files>`
  (paths relative to `<wt>/portal`, message file written by the Write tool). **NEVER PUSH. Never touch the portal
  remote, DEV or PROD.** The integrator pushes your branch to portal DEV at the drain.
- **COMMITTING SUPERPROJECT WORK** (your instance, rows, the status flip):
  `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~80 <0.9.0_WK_AMGT_RESAPP~80@opal.agent>" -F <msgfile> -- <paths>`,
  never staging `portal`. Never merge, rebase, `checkout --`, `stash` or `clean`.

## 4. BOUNDS

**PORTAL: COMMIT YES, PUSH NO.** No push, no gitlink move, no DEV/PROD merge, no deployment, no `/prod-deploy`. A
local commit on a worker branch is not a publish. **No AWS call of any kind, no S3 read or write, no Terraform, no
Lambda change, no vendor call, no network fetch.** **COLLECTION STAYS OFF.** **NO alarm, monitor, SNS/SES-send,
notification or freshness checker.** No secrets are needed. **No non-ASCII** in anything you write (AC6 counts it).
**LINE ENDINGS:** your checkout is LF by provisioning; write LF only (AC0 and AC6 count CRLF). **PUSH: never**
(LD-0522).
**THE REFUSAL CLAUSE:** a criterion you cannot satisfy AS WRITTEN is REFUSED with its measurement and a row; never
repaired, widened, or satisfied by a route this order did not name -- never by an install, never by editing a WALL
(the served sentences and `lib/` included), never by editing a fixture, never by relaxing a pinned comparison beyond
the ONE set-aside RULED item 3 names.
**A COUNT BAR IS READ AT SPAWN AND PRINTS its denominator.**
**SURPRISE ROWS:** `AMGT_RESAPP-Z-W80-S<k>`, `<k>` from 1; `"project": "AMGT_RESAPP"`, `"fabric": "site-z"`; append by
textual splice inside the one fenced JSON array; never edit an existing row. A pure disarm sets
`DISMISSED_WITH_REASON`, never `GRADUATED`; the disposition of `Z-S201` is the CVO's L9 act, not yours.
**MUTATION DISCIPLINE:** snapshot WORKING-TREE BYTES to `<wt>/.scratch/r80/` before editing. Never `git checkout --`,
never `git stash`, never `git show :path`.

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; each runs under timeout 300; run AC0 and AC4's baseline BEFORE any edit)

<proof_of_spec>
  <criterion id="AC0" cell_refs="AMGT-rk-80"><invocation>cd "$(git rev-parse --show-toplevel)" && mkdir -p .scratch/r80 && git -C portal fetch --quiet origin DEV && python -c 'import io, subprocess
def g(*a):
    r = subprocess.run(["git", "-C", "portal"] + list(a), capture_output=True, text=True)
    return r.returncode, r.stdout.strip()
PIN = "95d96edb8f0a448c187b23d5d3e274a4fa01d0d2"
_, dev = g("rev-parse", "origin/DEV")
dev_has_pin = g("merge-base", "--is-ancestor", PIN, "origin/DEV")[0] == 0
pin_reachable = g("cat-file", "-e", PIN + "^{commit}")[0] == 0
base = dev if dev_has_pin else (PIN if pin_reachable else None)
_, head = g("rev-parse", "HEAD")
_, br = g("rev-parse", "--abbrev-ref", "HEAD")
print("origin_DEV", dev, "dev_contains_rk78", dev_has_pin, "pin_reachable", pin_reachable)
print("base", base, "head", head, "head_is_base", head == base, "branch", br)
io.open(".scratch/r80/base.sha", "w", encoding="ascii", newline="\n").write((base or "NONE") + "\n")
for f in ("src/pages/SecurityAnalysis/tabs/ExecManagementTab.tsx", "src/pages/SecurityAnalysis/__harness__/execFallback.harness.cjs"):
    b = io.open("portal/" + f, "rb").read()
    print(f.split("/")[-1], "crlf", b.count(b"\r\n"), "lines", b.count(b"\n"))'</invocation><expect>"dev_contains_rk78 True" (measured True at the cut: origin/DEV = 95d96edb8f0a448c187b23d5d3e274a4fa01d0d2) and so "base" = the printed origin_DEV sha, OR "dev_contains_rk78 False pin_reachable True" and "base 95d96edb8f0a448c187b23d5d3e274a4fa01d0d2"; "head_is_base True"; "branch wk-amgt-20-80-portal"; "ExecManagementTab.tsx crlf 0 lines 234" and "execFallback.harness.cjs crlf 0 lines 249" if base is 95d96edb (other line counts are legitimate only when DEV has moved past it -- record them and RE-READ section 1's line numbers at your base before editing). "base None" (neither reachable), "head_is_base False" or any crlf above 0: STOP with a BLOCKING row (disarm_owner 2.0.0_SA_COO~Z) and edit nothing. The base sha is written to .scratch/r80/base.sha and every later criterion diffs against it</expect></criterion>
  <criterion id="AC1" cell_refs="AMGT-rk-80"><invocation>cd "$(git rev-parse --show-toplevel)/portal" && ./node_modules/.bin/tsc -b --noEmit > ../.scratch/r80/tsc_clean.out 2>&1; echo "clean_rc $? errors $(grep -c 'error TS' ../.scratch/r80/tsc_clean.out)"; printf 'export const typecheckControl: number = "not a number"\n' > src/pages/SecurityAnalysis/__typecheck_control__.ts; ./node_modules/.bin/tsc -b --noEmit > ../.scratch/r80/tsc_control.out 2>&1; echo "control_rc $? errors $(grep -c 'error TS' ../.scratch/r80/tsc_control.out) naming $(grep -c '__typecheck_control__.ts' ../.scratch/r80/tsc_control.out)"; rm -f src/pages/SecurityAnalysis/__typecheck_control__.ts; ./node_modules/.bin/tsc -b --noEmit > ../.scratch/r80/tsc_after.out 2>&1; echo "after_rc $? errors $(grep -c 'error TS' ../.scratch/r80/tsc_after.out) control_file_present $(test -f src/pages/SecurityAnalysis/__typecheck_control__.ts && echo yes || echo no)"</invocation><expect>three lines: "clean_rc 0 errors 0" (measured so on the patched tab in the issuer's probe); "control_rc 2 errors 1 naming 1" (the planted error is caught, so the clean pass can fail); "after_rc 0 errors 0 control_file_present no". Run AFTER your edits. The form is `tsc -b --noEmit`, never bare `tsc --noEmit` (portal CLAUDE.md: the bare form checks an empty file set and passes on anything)</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-80"><invocation>cd "$(git rev-parse --show-toplevel)/portal" && node src/pages/SecurityAnalysis/__harness__/execText.harness.cjs; echo "rc $?"</invocation><expect>rc 0; CHECK lines for ceo_line_single_period ("3 of 3 names", each "ends_single_period=true carries_reason=true" with a tail ending "was not run."), period_added_when_missing, subtitle_fallback (CSL and 6861 roster_source=BLOOMBERG_FALLBACK, subtitle naming the Bloomberg fallback), subtitle_resolved_unchanged (CAT roster_source=FILING, edited = pinned = "Officers from the filing, with tenure against the pool") and pinned_copy_discriminates (pin=95d96edb8f0a448c187b23d5d3e274a4fa01d0d2, csl_tail ending "was not run..", csl_subtitle the old string), each "true (expected true)"; a final "EXECTEXT CHECKS 5/5"; no CHECKS-WRONG-WAY line -- measured exactly so in the issuer's probe, where the same harness against the UNPATCHED tab read 3/5 with "CHECKS-WRONG-WAY ceo_line_single_period subtitle_fallback". Also run it once against a scratch copy of the unpatched tab (restore after) and record that it reads 3/5 -- the negative control</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-80"><invocation>cd "$(git rev-parse --show-toplevel)/portal" && node src/pages/SecurityAnalysis/__harness__/execFallback.harness.cjs > ../.scratch/r80/fallback_after.out 2>&1; echo "rc $?"; grep -E "^CHECK |^EXECFALLBACK|^CHECKS-WRONG-WAY" ../.scratch/r80/fallback_after.out; grep -o "ceo_lines_set_aside=[0-9]*" ../.scratch/r80/fallback_after.out</invocation><expect>rc 0; five "CHECK ... true (expected true)" lines (fallback_source_rendered, fallback_not_confirmed_from_filing, resolved_unchanged, absent_unchanged, pinned_copy_discriminates); "EXECFALLBACK CHECKS 5/5"; no CHECKS-WRONG-WAY; "ceo_lines_set_aside=2" (CAT's CEO line on the edited and the pinned side) -- measured exactly so in the issuer's probe; WITHOUT the RULED item 3 amendment the same run reads "resolved_unchanged false" and "CHECKS-WRONG-WAY resolved_unchanged" (measured), which is why the amendment is part of this cell</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rk-80"><invocation>cd "$(git rev-parse --show-toplevel)/portal" && node src/pages/SecurityAnalysis/__harness__/tabs.harness.cjs > ../.scratch/r80/tabs_after.out 2>&1; echo "rc $?"; grep -E "^CHECKS-WRONG-WAY|EXEC officers=" ../.scratch/r80/tabs_after.out; cat ../.scratch/r80/tabs_spawn.summary</invocation><expect>the rc, the CHECKS-WRONG-WAY line (if any) and the line carrying "EXEC officers=" after your edits are IDENTICAL to the spawn baseline you recorded BEFORE editing into .scratch/r80/tabs_spawn.summary with the same command (rc, the grep lines). Measured in the issuer's probe (a bare portal worktree at 95d96edb): rc 1 with the same CHECKS-WRONG-WAY line and "EXEC officers=48/48 pool_line=5/5" both before and after the two fixes; AMGT-rk-78 measured rc 1 with "CHECKS-WRONG-WAY exec_officers_rendered" in the main tree -- the set depends on the workspace root around the portal, so record YOURS; a moved line FAILS this criterion</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-rk-80"><invocation>cd "$(git rev-parse --show-toplevel)" && B=$(cat .scratch/r80/base.sha) && git -C portal diff --name-only "$B"..HEAD | sort && echo "--- portal branch $(git -C portal rev-parse --abbrev-ref HEAD) status_porcelain $(git -C portal status --porcelain | grep -v '^?? .tsbuild' | wc -l)" && echo "--- gitlink $(git ls-tree HEAD portal | awk '{print $3}')" && git -C portal log --format='%an | %s' "$B"..HEAD</invocation><expect>exactly 3 paths, sorted: src/pages/SecurityAnalysis/__harness__/execFallback.harness.cjs, src/pages/SecurityAnalysis/__harness__/execText.harness.cjs, src/pages/SecurityAnalysis/tabs/ExecManagementTab.tsx; "portal branch wk-amgt-20-80-portal status_porcelain 0"; the gitlink line printing the SAME sha your workspace worktree carried at spawn (95d96edb8f0a448c187b23d5d3e274a4fa01d0d2 at the cut -- the superproject pointer never moved); every portal commit authored 0.9.0_WK_AMGT_RESAPP~80</expect></criterion>
  <criterion id="AC6" cell_refs="AMGT-rk-80"><invocation>cd "$(git rev-parse --show-toplevel)/portal" && python -c 'import io, subprocess; b = io.open("../.scratch/r80/base.sha", encoding="ascii").read().strip(); fs = subprocess.run(["git", "diff", "--name-only", b + "..HEAD"], capture_output=True, text=True).stdout.split(); [print(f, "crlf", io.open(f, "rb").read().count(b"\r\n"), "non_ascii_bytes", len(io.open(f, "rb").read()) - len(io.open(f, "rb").read().decode("utf-8")), "blob_crlf", subprocess.run(["git", "show", "HEAD:" + f], capture_output=True).stdout.count(b"\r\n")) for f in fs]; print("files", len(fs))'</invocation><expect>"files 3" and every file printing crlf 0, non_ascii_bytes 0 and blob_crlf 0 (the two edited files measured 0 and 0 at 95d96edb; the prototype execText harness measured crlf 0 non_ascii 0 in the issuer's probe)</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** No judgment criterion on this
order. Also record in your deliverable the CSL and CAT CEO lines and subtitles exactly as `execText.harness.cjs`
prints them, so the CVO can read what a manager will see.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~80/AMGT_RESAPP.TO-AMGT-rk-80.exec-tab-text-fixes.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json`, graded by YOUR WORKTREE'S OWN
`python .tools/proof-of-spec-check.py <instance> AC0,AC1,AC2,AC3,AC4,AC5,AC6` (rc 0 is the verdict); flip this order's
status tag (the record-face line at the end) from pending to complete; commit the superproject files with safe-commit
(never staging `portal`). Report once: the AC0 base line, the portal commit hash(es) on `wk-amgt-20-80-portal` (LOCAL,
unpushed), the typecheck and the three harness results, the tabs-harness spawn baseline and its after-edit reading,
and the CSL and CAT CEO lines and subtitles a manager will now read.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER PROVISIONING, before spawn** (measured feasible at the cut in a probe: `git -C portal -c core.autocrlf=false
worktree add` checks out LF -- crlf 0 on the tab, the harness and `types.ts`, where the plain form checked out CRLF
234/249 lines; `mklink /J` junction; `tsc -b` rc 0; probe removed, main `portal/` untouched, porcelain 0):
```
BASE=$(git -C portal merge-base --is-ancestor 95d96edb8f0a448c187b23d5d3e274a4fa01d0d2 origin/DEV && git -C portal rev-parse origin/DEV || echo 95d96edb8f0a448c187b23d5d3e274a4fa01d0d2)
git worktree add C:/tmp/wk-amgt-20-80 -b wk-amgt-20-80 <issuance-or-later SITEZ sha>
git -C portal -c core.autocrlf=false worktree add C:/tmp/wk-amgt-20-80/portal -b wk-amgt-20-80-portal $BASE
cmd //c mklink //J "C:\tmp\wk-amgt-20-80\portal\node_modules" "<workspace>\portal\node_modules"
```
Verify `C:/tmp/wk-amgt-20-80/portal/node_modules/typescript` resolves and crlf 0 on the tab. Teardown at the drain:
`cmd //c rmdir` the junction FIRST (never a recursive delete through it), then `git -C portal worktree remove`, then
the workspace worktree; keep branch `wk-amgt-20-80-portal` for the integrator.

**DRAIN:** the integrator pushes `wk-amgt-20-80-portal` to portal DEV and moves the superproject gitlink in its own
commit (LD-0522); the issuer runs `/frontend-dev` on the Exec Management tab for CSL and CAT (screenshot = acceptance;
a static harness is not a screenshot) before calling the page ready. **PROD promote: STANDING for AMGT page features
while PROD stays gated to Andrew** (CTO adjudication @c7bbb53f2a item 1; msg 24055: "its PROD promote is under the
standing word"), executed by the DT owner.

**L5 wording to name for the CTO at issuance:** the fallback subtitle "Officers from the Bloomberg fallback list -- the
filing roster did not resolve".

<status>pending</status>
<round>20</round>
<slot>~80</slot>
<fabric>site-z</fabric>
