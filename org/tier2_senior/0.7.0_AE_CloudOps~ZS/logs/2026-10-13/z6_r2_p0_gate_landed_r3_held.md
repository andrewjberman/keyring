# OPAL_BBGTML Z6-R2 landed and proven; Z-S17 filed; R3 held by the issuer -- 2050-2155Z

**archetype:** DEPLOY
**secondary_archetypes:** DIAGNOSE, SCRIBE

**Seat** `0.7.0_AE_CloudOps~ZS` (first session of this lane; it was NOT REGISTERED at launch)
**Window** 2026-10-13 ~20:50Z (session start) -> 21:55Z. First log, so the window is the whole session.
**Issuer** `2.0.0_SA_COO~ZB` | **ruling** `1.0.0_SA_CTO~Z` @`61e3067f5c` | **risk** WORLD on both orders

## What happened

Seated for OPAL_BBGTML with two queued orders. **R2 is complete and proven. R3 was never started and is now formally
held by the issuer** on a row this session surfaced.

### TO-Z6-R2 -- COMPLETE, all three criteria PASS

The P0 cheap-remedy gate in `integrations/bloomberg/auth/bbg_fallback.ps1` now branches on `$absent`: on `0` (8194
listening 3 of 3) it classifies "listener up, not entitled" and proceeds toward sign-in, because STEP 1's real
`dapi_check.py` had already failed. `1`/`2` (flicker escalation) and `3` (sustained-down) are unchanged. Before this,
`$absent -eq 0` fell into `if ($absent -lt 3)` and escalated `8194 not sustained-absent (0/3)`, exit 2 -- so a Terminal
whose 8194 is held by the BG seat's `bbcomm.exe` never got a sign-in and the pull exited 50.

Saving the file IS the deploy (shared working tree, Scheduled Task `OPAL_BBGTML_daily_pull`, next fire 2026-10-14
07:00 ET = 11:00Z). Landed 21:08Z, proven by 21:14Z, against a 10:00Z deadline.

- **AC1 PASS exit=0** -- `r2_p0_listener_check.sh`, listeners 1, the classification line present, `STUB: would now fill`
  reached, no `not sustained-absent` line, `R2: PASS`.
- **AC2 PASS exit=0** -- un-forced run took the **DAPI UP** branch, the first of its two accepted branches.
- **AC3 PASS** -- 1 file changed, `bbg_fallback.ps1` only.

### Two instrument traps that each nearly produced a wrong act

1. **The file is CRLF, and the instrument that said otherwise was `sed`.** `sed -n '58p' | od -c` showed no `\r`, because
   Git Bash `sed` strips it; the binary read showed `\r` at every line end. An LF-only replacement block was already
   written; the `count == 1` assertion caught it at **0 matches** and nothing was saved. The `grep -c $'\r'` reading of
   111/111 was **correct here** -- I initially dismissed it as the known every-line false positive and was wrong to.
   **The tell that resolves the two:** when a per-line predicate reads true on every line, do not conclude "broken
   predicate" -- read ONE line's bytes in binary. `od` after a text-mode filter is not a binary read.
2. **`commit-gate.sh` reported `checked 0 of 1 file(s)`** -- it reads only `.py`/`.sh`/`.tf`/`org/projects/*.json`, so a
   `.ps1` falls through unexamined. Ran the language-appropriate instrument instead:
   `[Parser]::ParseFile` = 0 errors, against a planted-syntax-error control that read 1. A parse error here breaks the
   07:00 ET pull.

### Three surprise rows -- @`ee4040615e`, gate read 3 new of 17, 0 malformed

| row | class / standing | substance |
|---|---|---|
| Z-S15 | OBSERVATION / INERT | `bbg_fallback.ps1:66` still prints "transport sustained-down" two lines after "8194 listening (3/3)". The one-line guard was written and **discarded** to stay inside the order's bounds mid-round. **Now folded into R3 as the issuer's AMENDMENT 1** -- owned and scheduled, not merely filed. |
| Z-S16 | OBSERVATION / INERT | **`wintrv.exe` absence is not a signed-out oracle.** `dapi_check.py` read `entitled session live` at 21:14:16Z and again 21:43:37Z with `Get-Process wintrv` = 0 and only `bbcomm` + `blpcrashmon` alive since 19:07:29Z. The order's 20:36Z context read used that same unsound instrument, so there is **no sound before-measurement** to compare against. Andrew's sign-in open call may already be satisfied. |
| **Z-S17** | **BLOCKING / ARMED** | The no-modify record says **at HEAD** the order "still stands for ... the vehicle and the sign-in scripts"; `bbg_fallback.ps1` line 2 calls itself a sign-in fallback; the Z6 ruling has **0 hits** for `no-modify`. |

**Evidence limit stated, not hidden:** AC1 reaches the new branch only under `-ForceDown`, which short-circuits `Dapi-Up`
before `dapi_check` is ever called, and AC2's real state was UP. So the classification is proven against a **forced**
STEP-1 failure and **never** against a genuinely un-entitled session. ABSENT is not EXERCISED-AGAINST. The repair is still
correct and needed; it must not be reported as proven against the live un-entitled state.

### The division of labour on Z-S17, which is the judgement call of the session

Finding it was a side effect of reading the channel header before appending to it. Having found it, the temptation was to
hold R3 myself. **That would have been this seat adjudicating a sovereign order as the wider reading** -- CLAUDE.md bars
reading Andrew's word wider or narrower, `org/XXX.md` makes stopping mid-sequence to ask for a new GO a violation, and
section 2 says file the row and keep working. So: filed the row, sent ONE ask, did not revert, did not widen, and opened
R3's step-0 worktree. The issuer then held R3 on its own authority (msg 33803, acked) -- which is where that call belongs.
I had briefly written the opposite into the report ("a block this seat is naming") and corrected it in the addendum.

Two secondary findings inside Z-S17: the clause's phrase **wraps a line break**, so a single-line `grep 'sign-in scripts'`
returns 0 against a file containing it; and the basis it cites,
`ANDREW_DIRECT_20261006_1818Z_ALL_RECS_APPROVED_MSTRZ_OPEN_CALLS.md`, is **absent at HEAD** (43
`ANDREW_DIRECT_20261006_*` records exist under `org/tier1_exec/`, that name is not among them, no deletion in the log).

### TO-Z6-R3 -- HELD, nothing run under it

Status appends `held` @`31ac9b5255`: "DO NOTHING UNDER THIS ORDER until a later status line names that reading." Read the
**last** `<status>` line; the original `pending` line is still above it. No revert of R2 was ruled. Independently, R3's
step-2 exercise precondition is unmet -- `dapi_check` read UP twice, and the order forbids any fill on UP because `-Fresh`
would close a signed-in Terminal.

## Current State

- **Live in the world:** the five-line STEP 2 branch is deployed in the shared working tree and is what the 11:00Z fire
  will run. `integrations/bloomberg/auth/bbg_fallback.ps1` @`f6cc68d6bf`, 114 lines, CRLF throughout, 0 non-ASCII,
  `sha256 f717d111e21f30fd759c7d6cc45d9306feaf7da6b909541c42bbde18cd758bc5`.
- **Rollback, per key:** `git checkout f6cc68d6bf~1 -- integrations/bloomberg/auth/bbg_fallback.ps1`, commit, reopen/close
  the ledger as rolled back. Target bytes `sha256 5aeb770858cead537dd8106754324a3428a580260cb259a2855f3c89395d9193`.
  One file, one command, no infra.
- **Deploy ledger** `opal-bbgtml-z6-r2-p0-gate-20261013`: **CLOSED**, both legs proven, sentinel removed (verified with
  `ls -a`, not `ls -1`). Entry
  `org/critical_paths/change_management/20261013T2103Z_opal-bbgtml-z6-r2-p0-gate-20261013_deploy_completion.md`.
- **Held tree KEPT and LOCKED:** branch `zs-bbgtml-z6-r3` @`897a0f65eb` with **no R3 edits**; worktree `C:/tmp/zs-z6-r3`
  under `git worktree lock` with the hold as its reason, so an idle GC pass cannot take a tree a released R3 will want.
- **Box left as found:** nothing filled, submitted or clicked; the sign-in ledger
  (`%USERPROFILE%\.bbg_signin_attempts.json`, 35 attempts, last 2026-10-13T14:28:30Z) was never written; `bbcomm.exe`
  pid 17756 never touched. The pre-edit difference control was deliberately NOT re-run, to avoid appending another
  escalation line to the live `C:\opal-elev\bbg_fallback_ESCALATION.txt` a human may read -- it is already recorded in the
  issuance commit at 20:36:58Z.
- **Push state, MEASURED** (`git ls-remote origin box/sitez` = `2d57c41ac0` at 21:28Z; containment tested against that
  hash with a positive and a negative control, not against the local tracking ref): `ea7dd1c07e`, `f6cc68d6bf`,
  `ee4040615e` **on origin**; `4bba8e8432`, `461e8b5573`, `89e30883dd` **LOCAL**, pending this box's scheduled `box-sync`.
  This seat does not push a shared branch.

## Blockers

**None on this seat.** R3 is held by its ISSUER with an explicit do-nothing instruction, which is a gate held elsewhere
rather than a blocked act here. The reading that releases it is Andrew's, carried on his card by `0.0.0_AB_MSTR~Z` and
`1.0.0_SA_CTO~Z`. Nothing this seat can do brings it forward.

## Next Steps

1. `[2.0.0_SA_COO~ZB]` Drain R2 and flip its `<status>`; the assignee does not edit the order file.
2. `[2.0.0_SA_COO~ZB]` Disposition rows Z-S15, Z-S16, Z-S17 (`disarm_owner` is this issuer on all three). Z-S15 is
   already absorbed as R3 AMENDMENT 1.
3. `[0.0.0_AB_MSTR~Z]` / `[1.0.0_SA_CTO~Z]` Carry the no-modify reading to Andrew. **Time-boxed to the 11:00Z fire** --
   whichever way it falls, it should fall before then. If the order stands and he says revert, the command is in Z-S17.
4. `[1.0.0_SA_CTO~Z]` Worth folding into the record either way: `wintrv.exe` should stop being used as a signed-out
   oracle anywhere in this project (Z-S16). Disposition 1's own prescription -- `dapi_check.py`, a real data request --
   is the sound read, and it currently disagrees with the premise.
5. `[0.7.0_AE_CloudOps~ZS]` On a later R3 status line naming the reading: resume at step 1 in the locked worktree, with
   AMENDMENT 1 folded in. The step-2 exercise additionally needs `dapi_check` to read DOWN.

## MCP traffic

4 total. Significant: **sent** msg 33795 to `2.0.0_SA_COO~ZB` -- the one ask, disposition Z-S17 before R3. **Received and
ACKED** msg 33803 -- R3 held, R2 received, no revert ruled. Inbox was empty at load and `get_delivery_state` returned
0 rows (a fresh lane never addressed -- zero ROWS MATCHED, not zero delivered).

## Files Modified

See commit messages: `ea7dd1c07e`, `f6cc68d6bf`, `ee4040615e`, `4bba8e8432`, `461e8b5573`, `89e30883dd`. One row needs
context beyond them:

| file | note |
|---|---|
| `integrations/bloomberg/auth/bbg_fallback.ps1` | the only production file touched this session. STEP 2 only, +4/-1. Edited in the SHARED tree deliberately: saving it IS the deploy, and the order directed it there. |

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `comp-find` | `-i --files 'bloomberg\|bbg\|BBGTML' org/critical_paths/.open_deploys --limit 20` | PASS -- 36 hits / 13 files; 3 files, all cleared by reading |
| `comp-find` | `-i 'no-modify\|no modify' org/tier1_exec org/tier0_utility org/tier0 --limit 25` | PASS -- 86 hits / 17494 files, HEAD band 2. **This is the read that found Z-S17** |
| `comp-find` | `--files 'ANDREW_DIRECT_20261006_1818Z' --limit 10` | PASS -- 54 hits / 199487 files, all log/archive; the record itself absent |
| `to-check.py` | `--all --assignee 0.7.0_AE_CloudOps~ZS` | PASS -- 2 PENDING, `scanned=6334` |
| `sequence-check.py` | `--project OPAL_BBGTML` | PASS -- UNPLACED, not sequenced; no block |
| `deploy_ledger.py` | `open` / `close-leg` x2 / `close` | PASS -- opened `ea7dd1c07e`, both legs proven, CLOSED, sentinel gone |
| `safe-commit.sh` | x5 under this lane's author | PASS -- surprise-row gate 3 new of 17, 0 malformed |
| `commit-gate.sh` | (rode the commits) | **WARN -- `checked 0 of 1 file(s)`; a `.ps1` is outside its suffix set** |
| `[Parser]::ParseFile` | on the edited file + a planted-error control | PASS -- 0 errors, control 1. Ran BECAUSE commit-gate read 0 of 1 |
| `audit-archive-invoker.py` | startup A.2 | **rc=1, 16 findings** -- device-level, owned elsewhere, not re-filed |

**What worked.** `comp-find`'s HEAD band put the no-modify scoping record at the top of an 86-hit census -- the finding
came out of a 2-line read, not a hunt. `deploy_ledger.py open` committing its own entry + sentinel meant the OPEN record
existed before the edit without a separate act.

**What failed.** Two `comp-find` denial round-trips before the right form ran: F1 on a plain `grep -ril` over
`.open_deploys/`, then F4 on piping a census into `tail`. Both denials named the correct next command.

**Gap found.** `commit-gate.sh` reads no `.ps1`, so **every PowerShell commit in this repo is syntactically unchecked by
the standard gate** -- and site Z runs production PowerShell from the working tree, where saving IS the deploy. The gate
says so honestly in its WARN, which is why it was caught; a reader who treats the WARN as noise ships an unparsed
production script. A `.ps1` limb calling `[Parser]::ParseFile` would be a few lines. Not filed as a surprise row: it is
fabric tooling, outside OPAL_BBGTML's channel, and belongs to whoever owns `commit-gate.sh`. Named here and in the cell
report.

Secondary: `client-data-check` WARNed ABSENT on all five commits (no hashed account-id list at
`C:\Users\Opal Bloomberg\.opal\account_id_hashes.txt`), so none was checked for client account ids. Absent is not empty.

## ADDENDUM, 22:55Z -- R2 flipped `complete`; and one false alarm I raised and retracted

**R2's `<status>` now reads `complete`**, drained by `2.0.0_SA_COO~ZB` ~21:4xZ citing AC1/AC2/AC3 PASS, the deploy on
origin and the closed ledger. The cell is closed. R3's last status line still reads `held`; nothing moved on the
no-modify reading.

**A probe of my own making read 1 unread message when there were none, and I reported it before resolving it.** The probe
was `ls -1 "$d" | grep -v '^read$' | wc -l`. On this device `ls` is indicator-style, so `ls -1` prints the subdirectory as
`read/` -- the anchored pattern never matches, and the directory itself is counted as mail. `check_inbox` had read empty
the whole time; the two instruments disagreed and the MCP probe was the correct one. Fix: filter `'^read/\?$'`, or count
`*.md` explicitly and test the byte count (a no-match glob leaves the literal pattern behind).

Same flag, two opposite failure modes, which is the part worth carrying: `ls -1` **adds** a character to directory names
and **drops** dotfiles entirely (the reason `.unindexed_red_state.json` needs `ls -a` or `ls-tree` in the NEVER-2 read).
Any count whose zero -- or whose one -- carries a verdict should use `ls -a` plus an explicit glob.

Also non-evidence: `org/mcp/inbox/0.7.0_AE_CloudOps/~ZS/.unread-deliveries` is a POINTER that keeps naming the last
delivery after it has been read and acked (it still names msg 33803). Its presence is not unread mail; only
`check_inbox` / `get_delivery_state` answer that question.

Not banked to memory: a seat does not write lessons there (Andrew-direct 2026-09-24, enforced by the Write hook). This log
entry in git history is the carrier, and the durable fix would be a one-character change in whoever owns that probe form.
