# NEVER-WIDEN -- CTO HALF -- AMGT_HARVST round 27, `HVST-q-1` (= `p-3` part (b): the span-bearing Lenovo bbg/wsj run, its upload, the `chatter_daily` rebuild) -- `1.0.0_SA_CTO~Z`, 2026-09-30 ~08:3xZ

**Against:** `deliverables/2.0.0_SA_COO_H/round26/NEVER_WIDEN_HALF_COO_P5.md` @`dadba8badd` (read to EOF, 4,665 B). The issuer
re-measured it at the round-27 cut @`0cfb340` (msg 27035, READ-acked).
**Ruling it serves:** `ledger/ROUND_ANALYSIS.round26.md` rulings 6 and 4-list cell 1 (@`ff4405d3d5`).
**Vendor authority:** R-21 @`b390c36444`, Andrew's word *"you have all the egress you want for vendors"* on its mechanism
(*"deterministic/scripted"*). The collector is that script; no agent turn calls a publisher.

## VERDICT: SIGNED

## 1. RE-MEASURED BY THIS SEAT

- **Before-state, every root re-listed on S3 by this seat against the signing snapshot `round26/p5_signing_before.json`**
  (ETag and size, key by key):

  | root | signed | now | equal |
  |---|---|---|---|
  | bbg | 1006 | 1006 | yes |
  | wsj | 84 | 84 | yes |
  | barrons | 30 | 30 | yes |
  | ft | 28 | 28 | yes |
  | sa | 106 | 106 | yes |
  | `run_record` | 0 | 0 (0 keys containing `run_record` under `amgt/harvest/`) | yes |
  | `chatter_daily` | 9 | 9 | yes |

  Both outboxes read 0 pending.
- **The code at the act equals the code at signing:** `git diff --stat 2023d17e46 HEAD -- lib/opal_data_harvest lib/research/harvest`
  is empty at this read.
- **Write path:**
  - `worker._persist_run_record` (`worker.py:592-604`) makes one `store.bronze_put("amgt", "run_record", ...)`.
  - Article and listing bronze go through `harvest_grammar.py:90` and `:113` at upload, never at collection.
  - The listing ceiling is read from config per publisher (`worker.py:309-314`).
  - This matches the COO half's put table.
- **The page count is printed before the run:** `__main__.py:119-131` emits `planned_listing_pages` per publisher. This is the
  `C-HV-EGRESS` "printed BEFORE the run" clause.
- **Read path:** unchanged from this seat's `p-3(a)` half (`scoped_amgt.py:4292-4299`: `/timeline` serves the newest
  `chatter_daily` part on every call). The CVO's round-26 served read is the baseline: 992_HK covered codes `[bbg]` on 265
  days and `[bbg, wsj]` on 8.

## 2. CONDITIONS

1. **The act-start gate** (`p-5.before.py`) reads equal to section 1 and the code diff reads empty, or STOP.
2. **The planned listing pages per publisher are printed and recorded BEFORE the first request** (`C-HV-EGRESS`).
3. **Order:**
   - the run, then the upload, then `build-daily`, each after-read passing before the next;
   - **no round-27 code cell (`q-2`, `q-4`, `q-5`, `q-6`) merges until `q-1` drains** (analysis ruling 6).
4. **After-state the verify reads:**
   - `run_record` is 1 object;
   - new objects exist only under `bloomberg/harvest/` and `wsj/harvest/`, and barrons, ft and sa are equal to section 1;
   - `chatter_daily` is 10 parts;
   - `run_records_read >= 1`;
   - RESOLVED is 0 of 191.
5. **One served read after the rebuild:** `/timeline` for 992_HK_Equity prints the covered-code distribution beside the baseline
   (265 / 8).
   - On a successful wsj job, the days in its `reached_span` gain `wsj`.
   - On a refusal, the distribution is unchanged and the run record names the refusal. **Both branches are acceptable; a silent
     one is not.**
6. **The run record is the FWD-3 exercise:** each fetched key's outcome (stored / rejected / not stored) and `keys_stored_join`
   are present in the persisted record. This is read, not assumed.

## 3. ROLLBACK

The COO half stands: forward only, every put never-overwrite, and readers take the newest part. A delete is Andrew's act.

## 4. NOT COVERED

- any publisher but bbg and wsj;
- any security but Lenovo;
- the mention snapshot;
- the bbg silver repair (`Z-S44`, round 28);
- the `gold` flip (`q-7`).
