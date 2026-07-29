# FINDING: git-author-override-audit.log DELETED + RECREATED 03:36:35Z — and the archive answers the "unanswerable" hook-identity question

**Author:** 3.0.0_SA_CVO · 2026-07-29 ~05:20Z · **archetype:** DIAGNOSE
**Trigger:** `audit-archive-invoker` INTEGRITY/NON-APPEND-EDIT at my 050639Z startup run (clause-3: snapshot WITHHELD, needs human authority ruling).

## 1. The integrity event (MEASURED, this host)

| Fact | Evidence |
|---|---|
| Live `org/git-author-override-audit.log` **birth time 2026-07-29T03:36:35Z** | NTFS CreationTime (PowerShell `Get-Item`) — the file was **DELETED and recreated**, not edited in place |
| First surviving line 03:36:34Z (`PASS 0.4.0_DE_ClientPlatform 2`) | hook re-created it on DE's commit a6ab652c85 (03:36:32Z) |
| Baseline snapshot holds **17,172 lines through 2026-07-28T12:57:51Z** | `org/audit/archive/2026-07-28T125858Z/org_git-author-override-audit.log` (1,696,149 B, local, intact) |
| **Lost window: 07-28 12:58Z → 07-29 03:36Z (~14.6h)** | not in baseline, not live. Partially reconstructable: every commit in the window implies a PASS/OVERRIDE line (git history survives); **BLOCK lines (refused commits) are the unrecoverable class** |
| Exactly ONE log was deleted on this host | invoker heartbeat 050639Z: all other guarded logs passed append-check (comp-which-rail 22,682 lines, spawn-audit 1,206, ledger-hook 13,509 — intact supersets) |
| Deleter: **UNKNOWN — INFERRED nothing** | no rotation sibling, no mass-deletion-audit entry (last 07-09), gitignored so no git actor. Not a broad `git clean` (other ignored logs intact). Single-file targeting is the odd part. |

**Disambiguation from tonight's site-Z findings:** the 015053Z FINDINGS.md entries (multi-MB logs
"missing"/tiny) were emitted from `C:\Users\Opal Bloomberg\...` — **site Z's clone, where gitignored
logs structurally do not travel.** Those are instrument-vs-topology artifacts, NOT deletions. The
03:36:35Z deletion is THIS host's, real, and separate.

## 2. LD-0343's "no history to consult" is FALSE — correction needed

LD-0343 (§ owned-paths log table) records: *"19 lines, earliest 03:36:34Z today … There is no
history to consult."* Written in good faith over the post-deletion file. **The archive snapshot IS
the history**: 17,172 lines / 15,558 PASS / 674 BLOCK / 335 OVERRIDE / 241 FORCE-BYPASS / 113 WARN /
21 SYSTEM-CURRENT-OVERRIDE / 8 FORCE-HEADMOVE. MSTR owns the record; I surface, not edit.

> **AMENDED ~12:45Z (MSTR 053040Z refinement, independently re-verified by me):** the 36 below
> AGGREGATES THREE SIGNATURES — signature-anchored counts are **FORCE-BYPASS UNKNOWN = 18 · WARN
> UNKNOWN = 13 · PASS UNKNOWN = 5**; **the fail-open proper (`GIT_AUTHOR_NAME unset`) = 14 events
> across 7 days** (04-28, 05-28, 06-11, 07-02, 07-09, 07-17, 07-24), latest 07-24T18:44:45Z. My
> word-count over-reported 2.6x. Verification trap worth banking: a naive `grep "PASS  UNKNOWN"`
> returns 23, because **`PASS  UNKNOWN` is a SUBSTRING of `FORCE-BYPASS  UNKNOWN`** (23 = 5 + 18) —
> anchor the signature, never the word. MSTR's bound carries: the 14 cannot be sorted into
> designed-Andrew vs lost-identity-agent BY CONSTRUCTION; exploitation is undemonstrated.

## 3. The hook-identity question IS answerable — 36 UNKNOWN-identity events in the archive

HEAD (ce39a6095a) records Z's fail-open question as "UNANSWERABLE FROM BASE TOO." That verdict was
manufactured by the deletion — the 48-minute live window supported nothing. Over the archived
population (2026-04-28 → 07-24):

- `grep -c "UNKNOWN"` → **36 events on 13 distinct days**, two shapes:
  - `WARN UNKNOWN N (GIT_AUTHOR_NAME unset)` — the exact fail-open-with-no-identity shape Z reported,
    **most recent 2026-07-24T18:44:45Z**
  - `FORCE-BYPASS UNKNOWN` — bypasses with no resolvable identity (mostly May-era)
- Distribution: 04-28×2 · 05-04×4 · 05-12×1 · 05-14×2 · 05-18×1 · 05-21×4 · 05-22×1 · 05-26×6 ·
  05-28×4 · 06-11×1 · 07-02×5 · 07-09×4 · **07-24×1**

So: the fail-open is REAL, DELIBERATE-AND-DOCUMENTED per CTO's ruling — and now also **measured in
the wild at ~36 occurrences over 3 months, still occurring as recently as 5 days ago.** Whether that
incidence changes the ruling is CTO/MSTR's call, not mine.

## 4. Dispositions requested

1. **Clause-3 authority ruling** (invoker design: human rules on whether the edit was authorized):
   was the 03:36:35Z deletion authorized by anyone? If not — an unattributed deletion of an
   append-only audit log during an active investigation OF that log deserves a name.
2. **LD-0343 correction** (MSTR): replace "no history to consult" with the archive pointer.
3. **Re-baseline decision**: the invoker withholds snapshots until ruled. History through 12:58Z is
   safe in the existing snapshot; the live log is healthy and appending. Recommend: rule, then let
   the invoker re-baseline so the withhold doesn't run indefinitely.

**Coverage denominators:** UNKNOWN grep ran over the full 17,172-line archive (positive control: the
verdict-distribution awk on the same file sums to the same population). Creation-time read is NTFS
birth time, one file, this host only. I did not measure site Z.
