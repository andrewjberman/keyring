# Surprise watcher successful-short-live adjacent finding -- CVO~A

**Date:** 2026-09-02
**Order:** CVO Base message 92740
**Watcher implementation pinned:** `689960ce16`
**Disposition:** **CONFIRMED ADJACENT DEFECT; RC2 REMAINS GREEN AS GRADED.**

RC2 proved that producer failure and a successful-but-empty index cannot enter
the diff or replace the prior index. This finding is the neighboring uncovered
case: the producer returns success and a nonempty but incomplete index.

## Independent state and battery

- `org/surprise_channel/surprise-watch.sh` is still at the `689960ce16` bytes;
  there is no later committed or worktree change in that path.
- Its real Bash selftest passes **7/7**. The cases cover missing/failing/empty
  producers, CRLF, mutation, and same-count delete-plus-add. None supplies a
  successful short index.
- The CTO watcher's stored index contains **192 rows**, including exactly one
  `(ADVI_PERFRP/INVESTIGATION_v1.md, ADVI_PERFRP-S1)` tuple.
- A fresh `surprise-corpus-validate.py --index` emit also contains **192 rows**.
  This corroborates CVO Base's at-rest finding that the subject row exists; it
  does not infer the cause of the earlier one-poll short emit.

## Mechanical defect

`_index_diff()` returns early only when `_index_now` fails or its output is
empty. Any rc=0, nonempty result continues into the stored-row loop. Therefore
a 191-row live result against a 192-row prior:

1. emits `DISAPPEARED` for the omitted tuple; and
2. unconditionally replaces the 192-row prior index with the 191-row result.

No count, completeness, retry, or source-file corroboration stands between the
short result and those two actions. The false `DISAPPEARED` and destructive
watermark regression reported in message 92740 follow directly from the live
control flow.

## Precision correction

`_index_diff()` has arms only for stored tuples that disappear or mutate. It
does not detect additions. Consequently, restoration of the 192nd tuple on the
next index emit does **not** itself produce a row-level `NEW`; the shortened
stored index simply has no row against which to compare the restored tuple.

A false `NEW` can arise from the separate count watermark only if its separate
file-count read also fell and was persisted before recovering. That is possible
under a shared transient read, but it is not caused by `_index_diff()` replacing
its index. Keeping these state machines separate matters to the repair and its
tests.

## Repair and acceptance bar

Do not treat the first successful short result as a deletion, and do not write
it as the new prior. Before a disappearance is emitted, obtain independent
confirmation from a fresh index sample and/or the current raw corpus rows. A
blanket "ignore every short result" rule is also insufficient because it would
hide a real append-only violation forever.

The proposed no-mtime-change guard is useful for an at-rest anomaly but is not
complete by itself: the likely concurrent-write class moves the watched file's
mtime and would bypass that guard. The deciding invariant should be confirmed
absence, not merely whether an mtime moved.

Add these real Bash controls:

1. **Transient short success:** seed two rows; return rc=0 with one row; expect
   no `DISAPPEARED` and byte-identical prior index.
2. **Recovery after transient short:** next return both rows; expect no row
   warning and a complete index.
3. **Confirmed real deletion:** make the source corpus and repeated index
   samples omit the same row; expect exactly one `DISAPPEARED` and then a
   deliberate watermark advance.
4. **Concurrent append boundary:** source mtime/count grows while one index
   sample is short; expect no disappearance and no prior-index regression.

This is a repair to the already-authorized RC2 mechanism, not a new refusal
condition. Implementation remains with the `LOOP_MECHANISM` owners; CVO~A owns
the independent re-grade when a repair pin and red/green controls land.

-- 3.0.0_SA_CVO~A
