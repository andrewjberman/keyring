# Base-DS respawn: startup + acct-237 co-sign (grounded) + C6/C7/C10/C11/C12 reconciliation -> C12 closed

**archetype:** MIXED (VALIDATE, COORDINATE)
**serial:** 0.4.0_DS_ClientPlatform (base; PID 37836) | **window:** 2026-07-17 ~19:21Z -> ~19:40Z
**Session:** respawn per Andrew-direct launcher (COO note: "base-DS Andrew-incoming, reconciles own
C6/C7/C10/C12"). /watcher clean (no orphan -- fresh session, Monitor task b49jstmhz, LD-0290 serial file
written); XXX.md startup full. `~A` is a SEPARATE live session (PID 32136) on trn_nna -- not touched.

## 1. Co-sign RATIFIED: 778febc94 nna_coverage_excusals.json (acct-237), grounded end-to-end

CTO's non-blocking co-sign request (0.7.0 landed lib/nna_coverage_excusals.json in my POD4 gold-lib lane
under audited GIT_COMMIT_AUTHOR_OVERRIDE, executing CTO's acct-237 excusal ruling). Did NOT rubber-stamp --
verified 4 links vs the file (working-tree = @778febc94, 10-line add):
- SHAPE: `load_excusals` (nna_coverage_guard.py:147-170) reads `excused_accounts`, requires exactly
  {reason,decided_by,date} per acct (RAISEs on missing), `out[int(k)]=v`. File carries all three for "237"
  + a harmless top-level `_doc` the loader ignores. No ValueError path.
- TYPE PARITY (shape-only misses this): compare site :303 `a in excusals`; `lost` is int-keyed (:290;
  :296 `new={int(a)...}`), excusals int-keyed (:169) -> 237 matches 237, the excusal is LIVE not a silent
  no-op that would still block the chain.
- WIRED: INF_C_01.canonical_nna.py:919 `check_nna_partition_coverage(..., excusals=load_excusals(), ...)`.
- CONSUMER: :306-308 reads reason/decided_by/date, all present.
Ratified to CTO 192150Z. Nothing to flag.

## 2. Base-DS reconciliation of own C-cells -- one drift found+fixed, four confirmed at-frontier

Grounded each cell vs CTO's two ACKs (163535Z C12, 164045Z C10+C6/C7) + live roster + git since 16:45Z:
- **C12 pending -> COMPLETE** @e4fb9348f (pushed 6020a79c7..e4fb9348f). CTO 163535Z verbatim "you are done
  with it"; ruled additions executed @163d7027b (headline: orion legacy premise FALSIFIED -- orion-api +
  orion-api-v2 written THROUGH TODAY), orion carve-outs -> Andrew's board (CTO carries, NOT this TO's
  scope), zero deletions, ACs 1-3 met. Added a reconciliation `<state>` block; stale "Pending is correct"
  (COO 07-14, pre-addendum) preserved as history.
- **C10 HELD pending** -- cash honestly UNMEASURABLE pending the cot 07-09 zero-row freeze's OWN lane
  (not mine; close-nothing-on-it holds). $435.71M securities-only floor stated w/ refusal; nothing
  emitted, C11-gated. Concurs CTO 164045Z.
- **C6/C7 HELD pending** -- author-halves done; deploy legs ride V2-8 (0.7.0/0.6.2). Concurs CTO's
  comp-state protocol-rule-4 non-flip. No C3/C6 deploy landed since 16:45Z.
- **C11 HELD staged** -- Andrew hold LIFTED but staged BY GATE (C3+C6 deploys still closed; 0.6.2 on
  WP8-DECOM ASK-A prep, 0.7.0 idle post-INF). Author-half (C10 derivation + C6 silver-registry) already
  authored/tested per my 07-14 note, ready to fold on GO. "NO work begins -- staged only" respected.
RAVC-closed to CTO 193925Z.

## Blockers
None mine. All forward cells externally gated (stated plainly): C11 on C3+C6 deploys; C10 on the cot
zero-row freeze repair (other lane); WP8-DECOM cell 4 on 0.5.0's D2 redirect ruling. A4/trn_nna is `~A`'s
active lane. Not a coast-failure -- these are hard external gates, no ungated addressable work remains.

## Current State (handoff surface)
Base-DS lane at current-frontier. C12 TO = complete (e4fb9348f). C6/C7/C10 = pending true-status,
C11 = staged-by-gate; all four confirmed by CTO's ACKs as the correct reads. Nothing in flight, nothing
mis-recorded. Event-driven; zero crons; Monitor b49jstmhz live.

## Next Steps
- **[me]** On the C3+C6 deploy gate opening: fold the ready C11 author-half (C10 derivation + C6
  silver-registry) and execute C11 emitter one-bucket repoint per its ACs. On 0.5.0's D2 ruling:
  WP8-DECOM cell 4 (B_02.canonical_lots re-point). Both event-driven.
- **[1.0.0_SA_CTO]** Reads the reconciliation confirm (193925Z); carries the three orion Andrew-class
  carve-outs to Andrew's board.
- **[cot incident lane]** allocations zero-row freeze repair -> flips C10 cash to COMPLETE for free.

## Compiler Tools
| Tool | Result | Note |
|---|---|---|
| safe-commit surface-check + comp-pulse risk-reflex | CLEAN | 1 file vs 1,239 danger nodes; MEASURED (danger map 85.2h STALE, flagged) |
| raw git-log / grep / find (startup + co-sign grounding) | operational | located load_excusals + the excusal json; TO-status + commit-existence grounding |
No comp-pipescript io/deployed: no gold script edited this window (co-sign = read-only source-parity
verify; C12 = TO-record close only). **Gap (standing, re-noted):** the co-sign was a JSON-schema-vs-consumer
parity check done by raw grep/Read of the guard + json -- no comp-tool covers schema-vs-load_excusals
parity (same rail-checked class my `~A` lane logged 3x for parquet reads). comp-grep would have carried
dependency context on the file-location step; used raw find/grep instead -- minor rail miss, noted.
