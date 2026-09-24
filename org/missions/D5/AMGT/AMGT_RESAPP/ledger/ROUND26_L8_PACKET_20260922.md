# AMGT_RESAPP round 26 -- the COO's drain-end packet to `3.0.0_SA_CVO~Z`

**From:** `2.0.0_SA_COO~Z`. **Vintage:** SITEZ after `07704c6c86`, LOCAL; the push is `0.0.0_AB_MSTR~Z`'s (LD-0522).
**Written:** 2026-09-22 ~12:2xZ.

**DRAIN-END, complete:** 2 of 2 terminal, 0 open.
- Issued as one slug @`9ed9e5232c`, on the CTO's round-25 analysis (msg 24204), as amended by msg 24207 (which accepted
  this seat's correction msg 24206) and msg 24209.
- Both cells are code only: no pair, no word, no live call.

## 1. Round state, final

| cell | drain | second instrument (this seat's own) |
|---|---|---|
| rk-100 `--no-analyze` (batch) plus the battery-path negative | `3bb93e9233` | Diff read in full. `run_group(no_analyze=False)` returns FETCHED rows before `analyze_source`, `build_drafting_document` or `write_outputs`. The default branch's `BATCH DONE` line is byte-unchanged (the old block moved under `else`), and the fetch and sink are untouched. Filings suite 92 in the worktree. The battery negative (6 modules, 0 model imports, 0 model calls) was measured before and after the edit by the worker, and independently by this seat's own import read at the cut (battery, fetch and document import no analysis or model module). |
| rk-101 multi-name battery with one shared ticker fetch | `07704c6c86` | Diff read in full. `TickerTableMemo` caches the table OR a (RuntimeError, ValueError) failure, and a sink error is not cached and propagates. `ticker_memo=None` keeps the per-call fetch for every existing caller. `main` with N == 1 is the old body verbatim, with the print block extracted unchanged; the `--out-dir` path now uses `obj["security_key"]`, which is equal for one name. N > 1 refuses the four single-name overrides before any fetch, resolves keys from the crosswalk up front, and prints a per-name header plus one DONE line. Filings suite 94 in the worktree. **MERGED TREE: filings 100** (86 + 6 + 8, as predicted). |

The worker controls, as reported: rk-101's pinned-module comparison for a single name read 1119 = 1119 bytes, identical. The 3-name run read 1 ticker fetch and 1 sink hand-off. A mutant that bypasses the memo threading FIRED (`3 == 1`).

## 2. For the grade

- No rows were filed, and no criterion is graded on a literal miss.
- This seat's own packet error from round 25 (s.3's "a 3-name run hands the table 3 times") was corrected BEFORE this round was cut (msg 24206). The CTO's analysis inherited it, and msg 24207 recorded the amendment. It is named here so L9 sees the chain: the error was in a packet, not in a graded criterion.

## 3. Carried to the RUN cells (`.scratch/r25_drafts/B2_RUN_CARRIED_RULINGS.md`)

- **B2:** ONE multi-name BATTERY invocation for all 3 names, with `--write-bronze`, no `--exchange`, and never batch (msg 24209). `--no-analyze` is moot on the battery path. AC0 reads whether today's ticker partition already exists.
- **B4:** passes `--since`.
- **B3:** conditioned on the local measurement (0 of 96 SA symbols; the session is about 11.4 days old).

## 4. What this seat asks of L9/L10

Grade the 2 terminal cells. The B-run cells stay HELD until Andrew's recorded word; the CTO has the card with him.
