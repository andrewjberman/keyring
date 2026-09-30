# 1.0.0_SA_CTO~Z -- /self-drive "AMGT fabric ops", ticks 34-35 (12:0xZ-13:06Z), 2026-09-30

**archetype:** COORDINATE
**secondary_archetypes:** VALIDATE

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260929_183xZ_SELF_DRIVE_AMGT_FABRIC_OPS.md` @`64a6172e7b`.
**state: ARMED**

## Scope

- **4 projects:** each `active`, `EXECUTING`. Sequence flags: 0.
- **Inbox:** empty at both tick starts. Read-acked in the window: 27133, 27134, 27138, 27141, 27142, 27148, 27151 and 27154.

## Andrew-direct in this window (record @`e1b5fd6d8c`, verbatim)

*"recs approved for all + we have credentials for everything in AWS Secrets. ... use existing trust tokens secured from past runs.
Crawling is only necessary if existing trust tokens are not working. Important to not confuse rate limit for trust token expiry.
Also recommend a retry backoff for the REST API hits ..."*

- **Executed:** HARVST PRD v0.9 `C-HV-TRUST-TOKEN`.
- **Routed:**
  - the portal DEV push after DSGN round-13 cell 1 -> MSTR~Z (QUEUED: no live session; parked on the record with its condition);
  - the worktree removals -> COO~D and COO~H, only the listed trees, branches kept;
  - the schedule re-arm after batch 1, and barrons/ft under his mechanism -> COO~H.
- **The NEVER-2 edit** was NOT approved as an edit. He asked to see the text, and it was shown to him verbatim. It waits on his word.

## Acts

| act | receipt |
|---|---|
| CORPUS z-1 CTO half | @`4acf8806ce` (map 84 / 10 fields re-derived equal; 8 of 19 changed files reached, the 2 extra move nothing) |
| HARVST round-28 analysis | @`c907537920`. The run-record path is a coverage SOURCE. Round 29: 3 cells, with the backfill measured-first per his quota word. The COO~H `worktree --force` is recorded as a fact for Andrew. |
| RESAPP round-52 analysis + v0.30 | @`5d3052d8d7`. The ASML chart is SERVED. FWD-27's line is amended per L9 (CVO signed @`7bec5ba4a5`). **The next scoped-API build IS the slash-key window:** one pair, copy then deploy. |
| DSGN round-12 analysis | @`81907cfe5f`. **The live no-dossier regression** (ab-2's per-field shape vs `ThesisTab` keyed on a top-level status) is ruled DSGN's: the page reads the served reason. Round 13 is 6 cells, cell 1 leading. |
| Slash-key object count, 40 not 30 (27154) | ruled: all 40, after the 10 extra classes' readers are shown routed through `slash_safe_key` (msgs 27159/27160) |
| 5174 moved to DSGN DEV `2c01af6a` | HEAD `a7dd4ccb`, 200 (27134) |

## Completion test

**NOT DONE:** 0 of 4 complete, 4 of 4 REACHABLE.

## Acts only Andrew can do (cited)

- The CLAUDE.md NEVER-2 edit, text shown [locked to his order].
- The portal PROD promotion [CLAUDE.md Portal].

## Watch items

- The 13:00Z CORPUS `r-1` fire (round-24 cell 3 reads it).
- RESAPP round 53 (issued @`cb37037d95`, 4 orders).
- HARVST round 29 (issued @`201bc76e9b`).
- DSGN round-13 issuance.
- The CVO's v0.9 half.

## Compiler Tools

| tool | result | note |
|---|---|---|
| `build_unit_map.build_entries` vs the committed map | PASS | 84 / 10, equal |
| AST closure intersected with `94301d5a9c..04b89561ce` | PASS | 8 of 19 reached, each traced |
| `git -C portal show ba62e945:.../ThesisTab.tsx` | PASS (finding) | the reader keys on a top-level `dossier.status` |
| `git -C portal rev-list` origin/DEV vs DEV | PASS | 67 ahead, 16 behind, for card 1 |
