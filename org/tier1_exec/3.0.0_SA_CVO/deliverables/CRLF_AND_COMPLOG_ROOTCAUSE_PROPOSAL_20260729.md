# The CRLF churn + compiler-tools-log contention — root causes MEASURED, staged fix proposed

**Author:** 3.0.0_SA_CVO · 2026-07-29 ~14:40Z · **archetype:** DIAGNOSE
**Trigger:** Andrew-direct at my terminal: *"two things that seem to persistently cause cruft and
nonsense... this CRLF renormalization and LF issues, as well as the compiler-tools-log.md always
seeming to get caught on commits... look into these and see if there is a solution."*
**Status:** findings + proposal. Implementation routes to CTO (repo-mechanism gate; verifier does
not land the fix it will verify).

## PART 1 — the CRLF class: three stacked causes, all measured this session

**1a. `core.autocrlf=true` at SYSTEM scope** (`C:/Program Files/Git/etc/gitconfig`, the
Git-for-Windows default) with **no repo-level override and no `*.md` attribute** — so every
markdown/text file's line-ending behavior depends on each machine's config. Site Z is a second
clone with its own config; nothing pins the two sites to one convention.

**1b. The hot file's committed blob is itself MIXED** — `git ls-files --eol` reads
`i/mixed w/mixed` for `org/compiler-tools-log.md` (and `w/crlf` vs `i/lf` for CLAUDE.md). Once
CRLF entered the blob, git's renormalization-suppression stops converting on re-stage, and any
path that DOES renormalize (a different git config, an interrupted stage) produces the whole-file
phantom diff — **measured today: a 27,699-line staged rewrite with zero real content under
`--ignore-cr-at-eol`, left by an index.lock race, which then blocked every subsequent merge.**

**1c. The two writer classes disagree.** `comp_log_auto.py:267` appends with
`open(..., "a", encoding="utf-8")` — Windows Python default newline translation writes **CRLF**.
Bash `echo >>` appends (the /log skill line) write **LF**. Byte census of the live file:
**27,715 CRLF lines + 1 LF line** — the writers manufacture mixed endings continuously, so any
one-time cleanup decays immediately.

### Fix (staged, smallest-reversible-first)

| stage | change | owner/lane | risk |
|---|---|---|---|
| F-1 | `comp_log_auto.py`: add `newline="\n"` to BOTH sinks (:267 md, :286 jsonl) | rail-tool lane (CTO routes) | nil — 1-line x2; stops new CRLF at the source |
| F-2 | `.gitattributes`: `*.md text eol=lf` + `*.json text eol=lf` + `*.yaml/*.yml text eol=lf` (shell/py/Dockerfile already covered) | BASE_EXEC (CTO lands, same as the union line) | attributes travel with the repo — pins BOTH sites regardless of local autocrlf |
| F-3 | one-time `git add --renormalize` of the newly-attributed set, ONE dedicated commit, landed in a quiet window (NOT during a deploy wave) | CTO word on timing | the last whole-file diff this class ever produces; blame noise on md files, accepted once |
| F-4 | repo-local `git config core.autocrlf false` (shared `.git` = one setting binds every agent on this box) + the same line in site-Z's clone | CTO | after F-2 it is belt-and-suspenders; without F-2 it would NOT protect site Z |

F-2 without F-3 leaves existing mixed blobs churning; F-3 without F-1 re-mixes within a day.
**Land F-1 -> F-2 -> F-3 in that order, ideally same session.**

## PART 2 — compiler-tools-log.md: the contention is STRUCTURAL, not a discipline failure

**Measured today alone:** 546 rows auto-appended by the HUD (`comp_log_auto.py`, called by every
comp-* wrapper, every agent), **38 commits touching the file by 10+ authors**, one 27,716-line
ever-growing file in a SHARED worktree. The mechanics of the "always caught" experience:

- **It is dirty again seconds after any commit** (next comp-tool run anywhere re-appends) — which
  is exactly the *"it is committed but the log itself isn't"* observation: the commit DID take;
  the file was re-dirtied by a peer's (or your own) next tool run before you looked.
- **`git pull` refuses to merge onto ANY dirty tracked file it touches** — and since every pull
  brings peers' rows to this file AND the local copy always has fresh rows, **every pull collides
  by construction.** merge=union (landed @f989e47ee7) fixed the committed-side conflicts; it
  cannot help the dirty-worktree check. Today's fabric-wide block (AE~A 142427Z) was this.
- The CRLF phantom (1b) stacks on top: interrupted stages leave 27k-line index rewrites that read
  as "it recompiled the whole log."

### Fix: follow the estate's own ratified precedent — per-writer live files, single-writer shared view

The `.agent_context` race was fixed by `comp-to` writing a **race-free per-session file** instead
of one repo-global last-writer-wins file. Same shape here:

| stage | change | effect |
|---|---|---|
| L-1 | `comp_log_auto.py` appends to **`org/mcp/comp-log/{serial}.md`** (per-serial live shard; jsonl sink unchanged — it already carries every row with richer fields) | zero cross-agent contention on the hot path; a pull can only collide with YOUR OWN rows (same serial, sequential — rare and trivially union-merged) |
| L-2 | `org/compiler-tools-log.md` becomes a **COMPILED VIEW with ONE writer**: a `comp-log-fold` step (ride the existing audit-archive-invoker cadence, or /log's Step-3) folds per-serial shards into the canonical file and commits under the folding agent's line | the shared file changes hands once per fold, not 546 times/day; "the log" stays exactly where every doc points |
| L-3 | date-bound the canonical file (`org/compiler-tools-log/2026-07.md` monthly shard, current month symref/pointer at the old path) | bounds the 27k-line growth; ends 55k-line diffs; old months become immutable |
| L-4 | retire merge=union on the hot path once L-1/L-2 land (the compiled view is single-writer; union becomes unnecessary, and its known hazard — silently keeping a stale line beside its correction — goes away with it) | one less special case |

**What this deliberately does NOT do:** no gitignoring of the canonical record (MSTR's
untracked-oracle lesson stands — the compiled view remains tracked and committed); no new
daemon/cron (the fold rides an existing invoker or /log); no format change to the rows (the
/log requirement "append one line" is unchanged — it just lands in your shard).

## Sequencing note

F-1 + L-1 are the same file (`comp_log_auto.py`) — **one edit, one owner, both fixes.** That
single change (newline + per-serial target) removes ~all of tomorrow's churn even before
F-2/F-3/L-2 land. Recommend it as the first move; CTO to route the owner (rail lane).

**Denominators:** EOL census = full byte scan of the live file; contention = today's git log
`--since` author count + `grep -c 2026-07-29` row count; config = `--show-origin` all scopes;
attr state = `git ls-files --eol` on 4 files (hot file + 3 controls). Site-Z config NOT measured
(no access) — F-2's whole point is that it doesn't need to be.

— 3.0.0_SA_CVO
