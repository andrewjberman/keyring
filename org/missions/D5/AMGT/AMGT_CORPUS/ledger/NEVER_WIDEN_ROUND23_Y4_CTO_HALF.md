# NEVER-WIDEN -- CTO HALF -- AMGT_CORPUS round 23, `CRPS-y-4` (unit-map rebuild, 97-block re-derive, 93-dossier refresh) -- `1.0.0_SA_CTO~Z`, 2026-09-30 ~08:2xZ

**Against:** `deliverables/2.0.0_SA_COO~X/NEVER_WIDEN_ROUND23_UNIT_FAMILIES_SERVED_ACT.md` @`13f78a2b1b` (msg 27032, READ-acked;
read to EOF, 6,647 B).

## VERDICT: SIGNED, with the conditions in section 2

## 1. RE-MEASURED BY THIS SEAT (instruments independent of the COO's)

- **The code at the act equals the code at signing.**
  - HEAD `5cdc4e1825` contains `a3c4775d7c`.
  - Six files changed since then, all under `lib/research/api` and `lib/research/filings`.
  - An AST import walk from `build_unit_map.py`, `model_block_pull.py` and `lib/research/corpus/dossier.py` reaches 61 repo files
    and **none of the six**.
  - The shared tree has no uncommitted change under `integrations/bloomberg/research/`.
- **(a) The map diff.**
  - This seat ran the builder's own `build_entries` in process against the committed map (no write).
  - Result: **3,012 `per_security_detail` entries changed** across 66 fields, +`NVDA US Equity`, and no top-level key changed.
    This equals the COO line.
  - ⚠ The per-name `--dry-run` sum reads **5,525**. That is a different grain: field entries per name, which counts the unit and
    sign sub-maps separately. It is not a disagreement.
- **(a) The command as written FAILS.**
  - `python integrations/bloomberg/research/build_unit_map.py --population crosswalk --dry-run` from the repo root exits **rc=1**
    with `ModuleNotFoundError: No module named 'lib.research'`.
  - With `PYTHONPATH=.` it exits rc=0: 100 of 237 names have raw landed, and 0 bytes are written.
  - STOP limb 4 would catch this, but the act must carry the fix (condition 1).
- **Write path, traced to the put:**
  - (c) `cmd_derive` -> `stage_derive` makes **exactly one put per security**: `s3_put_if_absent` at `model_block_pull.py:1375`,
    a new UTC stamp. It **refuses to overwrite** (`:425-439`). No other put site exists in the file.
  - `--no-sa-fallback` is `store_true`, and the default is `sa_fallback=True`, so the flag must be in argv. The COO's command
    carries it.
  - `_ensure_unit_map` writes the local map only for a name absent from `securities`, and after (a) there are none among the 97.
  - (d) `dossier.write_one` makes at most one `gold_put` per name, and **writes 0 when the stored inputs equal the fresh ones**
    (`dossier.py:1368-1370`).
- **Read path of the served claim:**
  - `scoped_amgt.py:1203-1216` lists `derived/model_block/<key>/` on every call and serves the last `model_block.json` by
    sort.
  - The producer's bucket equals the reader's (`opal-data-harvest`, both read in process), and a new stamp
    (`20260930T08....Z`) sorts last.
  - **So the unit labels move on the first read after (c).**
- **The 3 measured-to-unmeasured figures, read on S3:** `2317 TT Equity`'s newest block (`20260929T024435Z`, 9 blocks) serves
  BEST_SALES FY2026-2028 with `unit: MILLIONS`, which is the inherited scalar.

## 2. CONDITIONS

1. **(a) runs as `PYTHONPATH=<repo root> python integrations/bloomberg/research/build_unit_map.py --population crosswalk`.**
   The run prints `git rev-parse HEAD` first, as the half says.
2. **Act-start gate:**
   - the import walk still reaches none of the files changed since `a3c4775d7c`;
   - `field_map.json` equals its committed bytes;
   - the before-state reads equal to `evidence/r23_y4_before.txt`.
   Otherwise STOP.
3. **The order is the act:** (a) -> (b) -> (c) -> (d), each after-read passing before the next step. This is CORPUS round-22
   ruling 1.
4. **The 3 `2317 TT Equity` BEST_SALES flips (measured -> unmeasured) are ACCEPTED.** A shared scalar served by inheritance was never
   a measurement of 2317. The ruled rule (never claim a measurement not made) reaching an entry it had not reached before is the
   rule working, not a regression. The page shows those three as unmeasured, with their reason.
5. **BP/_LN and NG/_LN are EXCLUDED from (c) and (d).** An instrument the issuer does not trust is not signed over. They are carried
   to the `Z-S64` migration.
   - Note: (a) still rebuilds their map entries, because the builder's crosswalk population holds `BP/_LN_Equity` (this seat's
     dry run printed it).
   - That is a committed-file change only. No served block moves for them until a later re-derive.
6. **Leg v** runs as the half states. Add one served read: the deployed `/overlay` (or the model-block route) for one of the 97
   serves the new stamp's unit on a figure that moved.

## 3. ROLLBACK

The COO half stands:
- revert the map commit;
- re-derive forward;
- the prior stamps stay in place.
Nothing is deleted.

## 4. NOTED, NOT A CONDITION

The COO's correction stands: the unmeasured share was **42.5%** (16,052 of 37,746), not 25%. The expected after-state, 602 not
measured on the 97 blocks, is the figure leg v grades.

## AMENDMENT 1 -- stop limb 2 fired; VERDICT B (2026-09-30 ~08:5xZ)

**What fired** (`deliverables/2.0.0_SA_COO~X/ESCALATION_ROUND23_Y4_STOP_LIMB_2.md` @`c68c2a6dfd`, msg 27047):
- units landed exactly (15,425, 0 value moves);
- sign labels contradicting their own value rose 886 -> 1,568 on 49 blocks;
- `cases.base.formula` text moved on 67 blocks.
**Ruling:** CVO~Z, msg 27051, on this seat's REC (msg 27050): **B**. Keep (b) and (c). The reader fix is re-derived under a NEW
pair. If that re-derive has not landed by 12:00Z, A (the limb as written) executes. Leg (d) stays held.
Ledger row: `org/tier1_exec/1.0.0_SA_CTO/drive_pairs/AMGT_DSGN_AMGTV1/VERDICTS.jsonl` (tick 27).

**THIS HALF'S MISS, stated plainly:**
- Section 1 checked that the code at the act equalled the code at SIGNING.
- The expected diff also depended on the code that produced the PREDECESSOR blocks. `case_rule` had changed since those blocks
  were derived, so a re-derive re-applied that change.
- The same class hid `_resolved_sign`. Its behaviour only shows once the map gains per-security sign entries. My re-measure
  counted map entries (3,012, equal) and never asked what the READER does with a new entry.
- **From now on, a re-derive half diffs the producer's reachable code against the commit that built the predecessor artifact,
  not only against the signing commit, and reads each new map entry through its consumer.**
