# TO-F2 default-flip CERT — GRANTED, one condition (orphan-lock steal rides the flip commit)
**archetype:** VALIDATE

Trigger: AE 0.7.0 cert request 144005Z (engine edaa8d410 committed, flip held). Independent code-read +
artifact check done before cert (doctrine): _canonical.py full read, kuzu_cli wiring diff, artifact shape.

## Verified
1. **Engine mechanics sound** (_canonical.py): mkdir-mutex (atomic, Rule-16 — no flock) + double-checked
   locking (L142-144) + losers wait/recheck/reuse (L130-138) + MUTEX_WAIT_S timeout fail-safe; build-to-temp
   + os.replace swap with manifest-second ordering (reader's worst case = complete fresh DB with old
   manifest — correct reasoning, L81-85); EVERY failure path (rebuild exception, swap block, mutex timeout)
   fail-safes to the existing TO-F1-LABELED-stale DB — never corrupt, never silent. Subprocess rebuild
   isolation. needs_refresh falls through to age-check on unreachable warehouse (no rebuild storm).
2. **Artifact shape**: kuzu_nessie_db is a single FILE (8.8MB) — os.replace is valid + atomic on same
   volume (the os.replace-on-directory Windows failure mode does not apply).
3. **CLI wiring**: ensure_fresh gated on _canonical.is_canonical (scratch DBs via --db-path never
   auto-refresh) and wrapped in try/except — an auto-refresh failure can never kill a query; stderr-only.
   DEFAULT_DB_PATH confirmed still kuzu_db pre-cert (zero fabric impact to date).
4. **AC10b/c evidence accepted**: deliberately-BEHIND rebuild-on-query demonstrated; 4-way concurrency =
   exactly 1 rebuild, all 4 procs at oracle 1157, no corruption/leak, pin restored. Oracle 1157 consistent
   with the F4 phantom-collapse figure (24831->1157).
5. **Dependencies**: Item-2b delete-propagation deployed (globgrph-v0.1.10) + drift revert landed
   (c3d9b3349, 0/0/0) — the freshness the canonical surface rides on is in place. F5 honored (no code
   change required; auto-refresh does not promote the graph to a verification surface).

## CERT: GRANTED — flip DEFAULT_DB_PATH to _canonical.CANONICAL_DB_PATH — with ONE CONDITION
**Orphan-lock steal must ride the SAME flip commit.** Gap: if a rebuild winner dies between mkdir(lock)
and the finally-rmdir (SIGKILL/machine crash — and this fabric hard-kills agents routinely), the
.rebuild.lock dir persists forever. Post-flip effect: EVERY default comp-kuzu query fabric-wide pays the
180s mutex wait then serves stale, until a human notices and rmdirs. Pre-flip this only bit explicit
--db-path users; the flip is what makes it a fabric-wide availability footgun, so the fix gates the flip.
Spec (~6 lines): on FileExistsError, stat the lock dir mtime; if older than a steal threshold (15 min —
generously above any legitimate rebuild), log WARN ("stealing orphaned rebuild lock, age Xs"), rmdir it,
retry the acquire ONCE; if the re-acquire also hits FileExistsError, proceed with the normal wait loop
(a live winner re-created it).

OPTIONAL (not a condition): the loser wait-loop rechecks needs_refresh every 0.5s, each hitting the S3
metadata list — consider backing the recheck interval off to ~2-3s to avoid hammering during long
rebuilds. AE's judgment.

Phase-3 docs as planned: comp-tools.yaml in AE's lane; graph-call-manifest.yaml patch routes to COO
(exec-owned) — the manifest entry must note the default now auto-refreshes (QUERY stays the default
posture per Rule 20; the rebuild is engine-internal, not a comp-build invocation).

## Compiler Tools
| Tool | Run? | Why / result |
|---|---|---|
| comp-* (any) | NO | Cert = line-level engine review (direct Read of _canonical.py + wiring diff + ls artifact-shape check) + acceptance of AE's demonstrated AC10b/c transcript. No change by me; the flip commit carries AE's TO mandate (comp-kuzu smoke post-flip per TO-F2). |
