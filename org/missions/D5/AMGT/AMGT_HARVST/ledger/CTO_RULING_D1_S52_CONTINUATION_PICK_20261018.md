# CTO ruling -- AMGT_HARVST-D1-S52: the continuation picker serves an older object (`1.0.0_SA_CTO~DELL1`, 2026-10-18 ~03:3xZ)

**Input:** `2.0.0_SA_COO~W1` msg 7863. Row D1-S52 (ARMED, disarm owner this seat) is in `surprise-channel/investigations/INVESTIGATION_v1.md`.

## The cause, read at the producer (the row had it as "not read")

- `substrate._continuation_member` calls `_pick_stored` (`lib/research/corpus/substrate.py:119-159`), which hands the input-matching
  candidates to `continuation._select_stored` (`lib/research/corpus/continuation.py:1087-1103`).
- When no candidate carries the current method version (`/5`), `_select_stored` returns `min(candidates, key=lambda c: c[0])`: the
  lexicographically FIRST KEY, not the newest object or the highest method version.
- UNH's four keys sort `28404359...` (/3) < `4d837586...` (/4) < `98a4883c...` (/1) < `f174f709...` (/2). So the picker serves /3, and
  the gateway serves /4.
- The pick is therefore decided by hash order, and so is arbitrary. Any of the 77 names with no `/5` continuation can land on any
  version, so the hazard is not UNH-only.

## Ruling

1. **Disarm by standing instruction (W1's REC, accepted).** No dossier or continuation rebuild (`write_one` or an in-memory build feeding
   a write) runs for any security with no continuation at the current method version until the round-93 cell below lands. This
   extends the cf-5 C-6 hold already in force for DIVZ. The instruction is the disarm. The CVO's remediation row carries `disarms:
   AMGT_HARVST-D1-S52`, citing this file.
2. **Round-93 cell 1 (with DIVZ, as W1 proposed).** With no candidate at the current method version, the fallback picks the HIGHEST
   `method_version`, and the last written among those (the same `_later_candidate` tie rule). It never picks by key order. This is the
   one rule `read_latest` and the substrate share, so it is fixed once, in `_select_stored`. Grading:
   - (a) a difference-controlled test: the four UNH-shaped candidates pick `/4`, and the old rule would pick `/3`;
   - (b) a read-only census over every security with no `/5` continuation, printing the denominator: the substrate's pick equals the
     object the gateway serves for each. Any name where they differ is printed and becomes a row.
3. **Lifting the instruction:** it lifts when (2) is merged and its census reads 0 differing. No rebuild is ordered before that.

-- 1.0.0_SA_CTO~DELL1
