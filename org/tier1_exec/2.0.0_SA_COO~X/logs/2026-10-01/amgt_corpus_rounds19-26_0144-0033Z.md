# 2.0.0_SA_COO~X -- AMGT_CORPUS rounds 19-26 under /canonical-drive -- 2026-09-30 01:44Z to 2026-10-01 00:33Z

**archetype:** COORDINATE
**secondary_archetypes:** DEPLOY, VALIDATE

**Seat:** `2.0.0_SA_COO~X`, respawned ~01:44Z on 09-30. The drive authority is `org/ref/LIVE_ARMS.md` (`/canonical-drive AMGT_CORPUS`,
under `1.0.0_SA_CTO~Z`'s AMGT fabric-ops self-drive). Window: since the respawn. My last log was 2026-09-24. The hourly drive logs
`org/tier1_exec/2.0.0_SA_COO~X/drive_log_20260930T{02..23}Z_opal_bloomberg.md` carry the tick-level detail; this is the session
record over them.

## Summary
I drove AMGT_CORPUS from the round-19 drain through round 26, issuing every round as ONE issuance on the CTO's analysis in the tick
it landed. Every served act ran under a never-widen pair with a NEVER-2 ledger, and every ledger is CLOSED except round 26's ab-4,
which is at leg d's last check.

The served outcomes on the newest block of each key:
- **Units:** not-measured units went from 42.5% (16,052 of 37,746) to 11 UNRESOLVED over 100 keys.
- **Signs:** sign labels contradicting their own value went from 1,569 to 0.
- **Currency:** TSM's `CUR_MKT_CAP` (a USD value labelled TWD) serves USD. 41 header figures stop printing a currency they never
  measured; BP's market cap (GBP, unstated) stops printing USD.
- **BP and NG:** both moved to encoded keys (with RESAPP r53) and are now derived from trusted raw. Their dossiers read through a
  slash-safe reader (ab-1).

**Andrew's words in the window:**
- "if all the content has been committed, then we do not need them anymore" (drained worktrees removed, branches kept; record
  `8c4f79e531`);
- "delete the empty wk-crps-1 folder too" (done non-recursively; it held a junction to the live `portal/node_modules`);
- "Go with sequence" (the `/next-calls` options 1-3 on 09-30 ~17:47Z).

## Work Done (by round; hashes are the issuance / ledger / packet)

| round | issuance | served act(s) and ledger | packet |
|---|---|---|---|
| 22 | -- (drained) | `amgt-corpus-r22-served-acts` CLOSED `d8b48f4a9e` | `9d55db806d` |
| 23 | `bbf33b05b4` | y-4 units + y-5 sign fix (VERDICT B on stop limb 2) | `44b762332a` |
| 24 | `43fd463710` | z-1 units (553 to measured) | `97d992d947` |
| 25 | `6e3180360a` + AMENDMENT 1 `38ece555e3`/`9ab55e18ea` | aa-2 labels + units; aa-4 BP/NG on encoded keys | `5fe52a896a` |
| 26 | `65ed3968c1` | ab-4: the map, 18 blocks, dossiers through the fixed reader | in progress |

**Round 23:**
- y-4 units ran under the ledger `amgt-corpus-r23-unit-families` (CLOSED).
- Stop limb 2 fired, and VERDICT B followed.
- y-5 fixed the sign reader per figure (`94301d5a9c`).

**Round 24:** z-1, z-2 and z-4 merged. The z-1 act ran under `amgt-corpus-r24-unit-closures` (CLOSED). The slash-key supply for RESAPP
was 40 objects, not 30 (`7e569c4d1d`, `38702fe8e4`).

**Round 25:**
- aa-1 and aa-3 merged after AMENDMENT 1 (4 issuer defects).
- The aa-2 act ran under `amgt-corpus-r25-labels-units` (CLOSED): 22 blocks, TSM USD.
- The aa-4 act ran under `amgt-corpus-r25-bpng` (CLOSED on CTO AMENDMENT 2): leg d had 0 writes (`Z-S71`).

**Round 26:**
- ab-1, ab-2, ab-3 and ab-5 merged (`78842bba5e`, `6cfc6bab90`, `c50db70fb0`, `9753b57672`).
- The ab-4 act ran under `amgt-corpus-r26-ab4` (`9661eab7ad`): legs a, b and c CLOSED, and leg v's reads passed.

**Surprise rows filed this window:**
- `Z-S68`: the per-field sign reader.
- `Z-S69`: TSM's currency label.
- `Z-S70`: proof-of-spec-check accepts a pin to an older version.
- `Z-S71`: the dossier read the raw key.

**Rulings files:** `RULINGS_ROUND24.md`, `RULINGS_ROUND25.md`, `RULINGS_ROUND26.md`.

**MCP traffic (significant only):**
- the CTO round analyses: 26846 (r18), 27104 (r23), 27200 (r24), 27357 (r25);
- the CTO pair halves: 27053 (VERDICT B), 27136, 27276, 27297, 27343, 27422;
- the slash-key ruling: 27159;
- the packets to `3.0.0_SA_CVO~Z`: 27095, 27191, 27347;
- the RESAPP coordination with `2.0.0_SA_COO~Z`: 27152/27153, the leg-c notices.

## Compiler Tools

| tool / instrument | used for | result |
|---|---|---|
| `to-pipeline-gate.py` | each issuance | PASS (gate2 seating lint ANNOUNCE-mode misparse `0.9.0_WK_AMGT_CORPUS~n` -> `0.9.0_WK_AMGT`, not blocking) |
| `proof-of-spec-check.py` | every re-grade, with the order args | PASS. It accepted a pin to an older version (`Z-S70`); since then every pin is read by content |
| `deploy_ledger.py` | 6 served-act ledgers | PASS. A HOLD is refused while apply legs are open |
| serializing dry runs (`aa4_dryrun.py`, `m4_dryrun.py`, `c26.py`, `aa4_verify.py`) | the expected diff by the producer's own `stage_derive` with a write-capturing client | PASS; each real block equal to its capture |
| `m2/m3_measure.py`, `c_verify.py`, `c25_verify.py`, `d25.py` | per-figure units/signs/labels; leg-c and leg-d verifies | PASS |
| `safe-commit.sh` / `safe-merge.sh` | commits and drains | PASS. One commit loop hid a gate BLOCK (fixed in `commit_retry.sh`); peer merges waited out, never touched |

- **What worked:** capturing writes around the real producer (`stage_derive`) made every act's expected diff exact. The served blocks
  equalled the dry runs byte for byte, apart from `vintage`.
- **What failed:**
  - a harness-killed background job left its `python -` child writing (aa-4 leg d, round 24). It was caught by CreationDate, and all
    long writers now run as named scripts with `python -u`.
  - I twice wrote a stray file to `C:\OPALBL~1\` by mistake; both were removed.
- **Gap found:**
  - `proof-of-spec-check` pin drift (`Z-S70`; the CTO has since added the announce limb);
  - the seating lint's serial parse;
  - `/thesis` recomputes cases from the DEPLOYED `case_rule`, so a producer case fix reaches the page only with RESAPP's redeploy.

## Blockers
None on this seat.
- ab-4 leg d's `inputs_equal_now` check is running: 9 of 19 at the time of writing.
- The case fix on `/thesis` is RESAPP's redeploy, owned by `2.0.0_SA_COO~Z` and told at leg c.

## Current State
- **Project:** AMGT_CORPUS (`org/missions/D5/AMGT/AMGT_CORPUS/`), round 26.
  - The decomposition is `decompositions/AMGT_CORPUS_DECOMP.md` v26.0.
  - All 4 orders (`TO-CRPS-ab-1/2/3/5`) are complete and merged.
- **Open ledger:** `org/critical_paths/change_management/20260930T2301Z_amgt-corpus-r26-ab4_deploy_completion.md`.
  - Legs a, b and c are CLOSED. The map is `29d87a966a` (byte-identical to the dry run), and the 18 blocks equal their captures.
  - **Leg d:** 19 of 19 dossiers written, 0 errors. The S3 structure is exactly one new object each, with changed keys `model_rows`,
    `inputs` and `content_sha256` (plus `as_of` on 8 after midnight UTC). The `inputs_equal_now` check is running.
  - **Leg v:** reads done, not yet closed. The census reads 11 over 100 keys. `/thesis` BP serves `PE_RATIO` RATIO, `PROF_MARGIN`
    PERCENT, and `CUR_MKT_CAP` with no currency and its value byte-unchanged. BA stays USD.
- **Evidence:** `deliverables/2.0.0_SA_COO~X/evidence/r26_*`. The checks are `deliverables/2.0.0_SA_COO~X/checks/round26/`.
- **The round-26 packet** is not yet written. It follows the ledger close. Its draft items are in `RULINGS_ROUND26.md` and the
  20Z-23Z drive logs.
- **Push state:** LOCAL throughout (MSTR pushes); origin unread this window.

## Next Steps
1. [2.0.0_SA_COO~X] When `inputs_equal_now` reads 19 of 19: close legs d and v and ledger `amgt-corpus-r26-ab4`, write the
   round-26 packet, and send it to [3.0.0_SA_CVO~Z].
2. [2.0.0_SA_COO~Z] The scoped-API redeploy carries ab-3's case fix to `/thesis` (BP's 778.57 input), under its own pair.
3. [1.0.0_SA_CTO~Z] The round-26 analysis; the round-27 candidates are in `RULINGS_ROUND26.md`:
   - `Z-W5-S7`, the basis text;
   - `Z-W2-S19`, zeros in the median;
   - the `Z-S70` battery patch parked with [0.8.0_AE_CloudComp];
   - the 11 UNRESOLVED (BBSE3 10, TSM 1).
