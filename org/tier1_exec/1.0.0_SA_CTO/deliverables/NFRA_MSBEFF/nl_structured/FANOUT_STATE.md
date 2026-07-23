# NL-corpus fanout — FINAL STATE (2026-07-23)

**STOPPED by operator (Andrew): the parallel fanout repeatedly exhausted account spend limits.**
Do NOT relaunch as a 10-wide Opus fleet. **If resumed: cap subagent model to Sonnet/Haiku and run
in small serial batches (2-3 at a time), not 10 parallel.**

## Harvested (banked, verified, sufficient to rank Phase 3)
- COMPLETE: chunk_01 (192), chunk_03 (142), chunk_04 (198)
- PARTIAL:  chunk_08 (63), chunk_09 (54)
- MERGED: `findings_merged.jsonl` = 649 findings, 0 unverifiable quotes dropped (610 exact / 39
  transliterated). Structured log: `../STRUCTURED_LOG_working_vs_not.md`.

## Pending (NOT harvested — optional refinement, not required for Phase 3)
chunk_02, chunk_05, chunk_06, chunk_07, chunk_10 (~5 chunks / ~1,100 sections).
Relaunch prompt is per-chunk identical to RUBRIC.md; merge/verify procedure unchanged.
The partial is representative — the remaining chunks refine FREQUENCIES, not the DIRECTION of the
findings (coverage + triggers, not correctness).
