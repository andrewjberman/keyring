# AMGT_RESAPP round 25 -- the COO's drain-end packet to `3.0.0_SA_CVO~Z`

**From:** `2.0.0_SA_COO~Z`. **Vintage:** SITEZ after `8dd72465b6`, LOCAL; the push is `0.0.0_AB_MSTR~Z`'s (LD-0522).
**Written:** 2026-09-22 ~12:0xZ.

**DRAIN-END, complete:** 2 of 2 terminal, 0 open.
- Issued as one slug @`83d7edfe7d`, on the CTO's ruling msg 24189 (which supersedes the round-24 analysis's "no round
  25"), after PRD v0.21 read ADMITTED.
- Both cells are code only: no pair, no Andrew word, no live call.
- The CTO kept all five L5 choices (msg 24200).

## 1. Round state, final

| cell | drain | second instrument (this seat's own) |
|---|---|---|
| rk-99 B4 Lusha wiring | `0c5dcc7c06` | Diff read in full: `enrich.lusha_client` wraps `_lusha_client` (0 lines removed), and `lusha.harvest_company` refuses an empty roster, dedupes only when `since` is given, and runs the guard before any write. Suites: harvest 72, management 95/13. **Probe, with the key env var UNSET:** a stubbed Lusha page result carrying an `email` key gave a row WITHOUT `email` and 1 silver put. A MUTANT that adds `email` to `KEPT_FIELDS` RAISED `LushaExceptionError` with 0 puts. So the second guard catches an allow-list edit. |
| rk-98 B2 filings bronze wiring | `8dd72465b6` | Diff read in full: `BronzeSink` (lazy import) is threaded into battery steps 1, 2 and 4 and into `fetch.build_source_object`, all `None` by default, with `--write-bronze` and `--security-key` on the CLIs. **The narrowed `except (RuntimeError, ValueError)` at step 1 does not change the network-failure behaviour:** `_call_http_get` still catches every exception from the HTTP call itself, so the narrowing only lets a SINK exception propagate, as ruled. Suites: filings 86, harvest 64 in the worktree; on the MERGED tree, harvest 72 and filings 86. |

## 2. For the grade

- No criterion was graded on a literal miss this round. Neither worker filed a row.
- rk-98's worker ran a mutant control on the narrowed except clause. With the clause reverted, `test_writer_error_propagates` fails, so the guard discriminates.

## 3. Carried to the RUN cells (recorded at `.scratch/r25_drafts/B2_RUN_CARRIED_RULINGS.md`; applied at their cut)

- **B2 run:**
  - `--no-analyze` (CTO msg 24200 (a)). `batch.py` has no such flag today, so the run cell or a code-only precursor adds it.
  - One ticker-table fetch per UTC day (msg 24200 (b)). Also, battery step 1 fetches the ticker table ONCE PER NAME, so with `--write-bronze` a 3-name run hands the same table to the writer 3 times. Whether `bronze_put` treats equal bytes as already present, and different bytes as a refusal, is read at the run cell's AC0.
- **B4 run:** the `lusha` CLI defaults `--since` to None, which means NO dedupe-skip, so a re-run spends credits again. The run cell passes `--since`.
- **B3:** measured read-only and local only (msg to the CTO at 10:48Z). 0 of 96 crosswalk records carry an SA symbol, and the SA session is about 11.4 days old.

## 4. What this seat asks of L9/L10

- Grade the 2 terminal cells. Neither carries a judgment criterion.
- The CTO then re-issues Andrew's card: B2, then B4, then B3 conditioned on the local measurement. The run cells are cut the moment his word is recorded.
