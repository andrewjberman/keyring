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

---

## DISPOSITION (CTO 143807Z + 144114Z; Andrew follow-up question folded) — supersedes L-1..L-4

**Accepted with amendments; the design got sharper twice after commit:**

1. **CTO independently reproduced BOTH classes within the hour** (cite): @741d336281 — a 2-row
   append stat'd as 178/174 (set-difference proved TRULY LOST = 0; *"a real-loss detector
   permanently saturated by noise"*), and the ~1428Z pull collision (three agents wrote the
   identical unblock-chore commit today: fe3c4e4c93 / 9c95f0f485 / d73b6bc4cd).
2. **Andrew's question ("don't the session logs already carry Compiler Tools?") produced the
   reader census:** ZERO runtime consumers parse the central md as data; the charter-2 join
   already migrated to the jsonl (no_signal 6,508/6,509 against the md's midnight-ET clock).
   **L-1..L-4 SUPERSEDED by delete-the-write:** comp_log_auto stops appending per-run rows to the
   md; the md keeps only the /log one-liners (~15/day). ~97% contention cut, negative machinery.
3. **CTO's blocker, measured (144114Z) — the correction that governs:** `comp-tool-runs.jsonl` is
   **UNTRACKED + GITIGNORED (.gitignore:447), 2.7MB, THIS HOST ONLY.** Deleting the md append
   before the jsonl has durable off-host custody would recreate the morning's audit-log defect
   (sole per-run record one `>` from gone) in the act of cleaning up. *"The lesson lands on
   whichever file carries the record, not on whichever file we were already thinking about."*
   **PRECONDITION: custody first, then delete — never the reverse.** CTO's candidate (0.8.0 free
   to beat): daily tracked shards `org/mcp/comp-tool-runs/YYYY-MM-DD.jsonl`, immutable at day-roll
   (zero contention by construction, custody complete, and a real per-day join boundary).
4. **Census-widening made binding:** my denominator covered `.tools/` + `org/modules/graph/` +
   `.claude/skills/` — NOT site Z. Site-Z consumer check (via MSTR~Z / agentbus) is required
   before any write is deleted.

**Final sequence (CTO routing, nothing tonight):** 0.8.0_AE_CloudComp tomorrow — (1) site-Z census
→ (2) jsonl custody design → (3) delete the md auto-append → (4) F-1 newline on surviving sinks.
F-2/F-3/F-4 land as ONE atomic quiet-window operation, CTO's hand (the piecemeal-attribute failure
mode — each file renormalizing whenever next touched — is CTO's 741d336281 instance redistributed
fabric-wide). CVO recused from build; verifies the build against these denominators.

## ANDREW-DIRECT RULING (my terminal, 2026-07-29 ~14:48Z) — VERBATIM, binds the design

> *"yeah id like to keep that file because it would be interesting to parse through, but i dont
> want commits tied to it. i dont mind the mcp/comp-tool-runs.jsonl either, would be curious to
> check that out."*

Recorded per the record-verbatim/broadcast-same-turn protocol; scope adjudication is CTO's, not
mine. Plain reading surfaced to CTO with the relay: **keep `compiler-tools-log.md` as a live
parse-target, but decouple it from the COMMIT path** (the churn, not the data, is the objection) —
i.e., the md's disposition moves from "tracked, low-frequency" toward "kept, commit-free," which
INTERSECTS the custody precondition: if the md goes commit-free AND the jsonl is host-local, BOTH
per-run records are single-copy. The custody design (CTO's daily-tracked-shard candidate or better)
becomes the sole durability carrier and its precondition-ordering becomes even more load-bearing.
CTO holds the reconciliation; Andrew's phrasing is the ruling, this paragraph is only a relay.

## ANDREW-DIRECT CLARIFICATION (my terminal, ~14:50Z) — VERBATIM, answers CTO's open question

> *"the agent handwritten one in /log is the only one i really care about, the mcp jsonl is fine i
> dont want to touch that, i just dont want a gate on commits to the monolith md"*

Surfaced reading (CTO adjudicates): (1) **the valued record is the HANDWRITTEN /log content** —
session-log Compiler Tools sections + the /log one-liners; (2) **the jsonl stays AS-IS, untouched**
— which reads as: no shard/tracking build for it; and by ranking the handwritten record as "the
only one I really care about," the sovereign has DEVALUED the per-run machine telemetry as a
durable record — the custody-carrier mandate rested on that record being worth off-host custody,
and that premise is now his to have removed (this is the answer to MSTR's surfaced question, not
just CTO's); (3) **the md's only constraint is: never a gate/coupling on commits** — which
"quiet-but-tracked" satisfies (CTO's simpler reading confirmed): delete the auto-append, md keeps
its history and its ~15 handwritten lines/day, nothing else changes. Net brief for 0.8.0 shrinks
to: site-Z consumer census (CTO's call whether it survives this ruling) → delete the md
auto-append → F-1 newline on the /log echo path. No custody build, no shards, no gitignore.

**TWIN RULING at the CTO terminal ~14:46:30Z (verbatim in CTO 144702Z), CONSISTENT and stronger:**
*"I think we dont log to the monolith md file anymore, just not necessary. the mcp jsonl sounds
like its gitignored anyway and ive never seen any issues attached to that so i dont mind it. the
only one i really care about is the one that is attached to /log which is unobtrusive."* CTO's
FINAL disposition (144702Z, closes the thread): md auto-append DELETED not redirected; /log
one-liner stays, tracked; jsonl stays gitignored as-is; **the custody blocker dissolved BY
SCOPING, not waiver** — git-author-override-audit.log is an SoD-relevant GOVERNANCE record
(single-copy custody still forbidden, that ruling untouched), comp-tool-runs.jsonl is OPERATIONAL
TELEMETRY whose durability the sovereign has dispositioned. *"The durability question is decided
by WHAT THE RECORD IS FOR, not by how it is written."* Brief for 0.8.0 = one deletion + F-1
newline + a courtesy (non-gating) site-Z line. L-1..L-4 and both custody designs: UNBUILT — the
best outcome available. Bonus: the deleted append WAS the CRLF writer on the hot file, so the
mixed-writer condition dies in the same edit; F-3's one-time renormalize is still needed for the
existing i/mixed blob, and F-2/F-3/F-4 remain CTO's separate atomic quiet-window operation.

**SCOPE GUARD (Andrew ~144900Z, verbatim in CTO 144928Z): "we just want the auto-append deleted,
dont delete the md itself."** THE FILE IS PRESERVED — tracked, full history, still receiving /log
one-liners; only the WRITER code path is removed. CTO's acceptance criterion binds the implementer:
proving the machine rows stopped is HALF the check — prove the file and its history survived too.
Pattern banked (2nd occurrence in one day, after leg-(d)): when an instruction names a FILE and an
ACTION, state whether the action targets the file or its CONTENTS, every time.

— 3.0.0_SA_CVO
