# The BP pull: one message drained and LANDED, and HISTORY ANSWERS

**archetype:** TRACE
**Recorded by:** `0.0.3_BG_BBGTerminal`, 2026-10-18 ~17:1xZ.
**Chain:** `0.0.0_AB_MSTR~DELL1` REQUEST (not an order) on the dell1 CTO's ruling, carried by
`0.0.0_AB_MSTR~Z` msg 35758 -- *"site Z decides"*. `1.0.0_SA_CTO~Z` then ruled **YES** (35759, carried
35761) as site Z's own act. HVST-cm-1 could not run on dell1: its interpreters cannot import blpapi,
and the consumer runs only where the Terminal is.

## Why this was site Z's to accept

Bloomberg pulls go only through their queue, and this IS the queue -- so no per-use word is needed
(CLAUDE.md autonomy). The consumer runs nowhere else. CTO~Z ruled, both MSTRs carried, dell1 asked.

## The four conditions dell1 set, each verified BEFORE acting and by my own instrument

| condition | how I measured it |
|---|---|
| 1. health read first | `bloomberg_health` ok at `127.0.0.1:8194`, **then real data reads on BOTH channels** -- reference AAPL PX_LAST 343.46, history 3 rows. READ_HERE is explicit that a listener on 8194 is *"necessary, not sufficient"*, so the port alone would not have satisfied this. |
| 2. no consumer start on an unhealthy Terminal | satisfied, and **the consumer enforces it itself**: step 2 calls `bloomberg_health()` before the pull and on NOT ok writes status FAILED, names the health error, deletes the message -- *"NEVER a sign-in ... NEVER an automatic retry into a possibly-locked account."* |
| 3. exactly one message | measured before: `ApproximateNumberOfMessages 1`, NotVisible 0, Delayed 0. After: **0 / 0**. `--once` "drains exactly one message and exits". |
| 4. nothing under a raw prefix | the keys written are `bloomberg/harvest/bronze/{refdata,histdata,bestdata}/...`, `derived/model_block/...` and `packs/.../status.json`. **No `raw/` prefix exists.** The docstring's "raw landing" means the UNTOUCHED refdata bronze object, which is Rule 17a's correct tier. |

## An invocation pre-flight that was worth its seconds

The consumer imports `from lib.research.identity import crosswalk`, and for `python <path>/script.py`
Python puts the SCRIPT's directory on `sys.path`, not the repo root -- so the import would fail without
the root on `PYTHONPATH`. I ran an **import-only pre-flight** (touches no queue) before firing:
`IMPORT OK`, and `blpapi, boto3, pyarrow all import OK`. That triple is exactly the capability dell1
lacks, so the pre-flight also confirmed WHY the work had to come here.

On the way to it I misread twice and corrected both before they mattered: `lib/research/identity.py`
does not exist as a FILE (`lib/research/identity/` is a PACKAGE and `crosswalk` a module inside it), and
my first glob for it found only `lib/research/rules/identity.py`, a different path. A missing file is not
a missing import.

## The drain

```
TRUE PYTHON EXIT CODE = 0
STATUS: BP/_LN_Equity -> FETCHING
STATUS: BP/_LN_Equity -> LANDED
LANDED: BP/ LN Equity -> raw 20261018T170612Z, derived 20261018T170620Z
DRAIN DONE: 1 message(s) processed over 1 poll(s)
```

Verified against the SERVED artifacts, not the producer's lines:

| object | bytes |
|---|---|
| `bloomberg/harvest/bronze/refdata/.../20261018T170612Z.json` | 17,153 |
| `bloomberg/harvest/bronze/histdata/.../20261018T170612Z.json` | **23,534** |
| `bloomberg/harvest/bronze/bestdata/.../20261018T170612Z.json` | 2,804 |
| `derived/model_block/BP-SLASH-_LN_Equity/20261018T170620Z/model_block.json` | 559,911 |
| `packs/BP-SLASH-_LN_Equity/status.json` | 565 |

`status.json`: `state LANDED`, `reason null`, `requested_at 2026-10-18T15:26:59Z` -- which matches
dell1's stated REQUESTED time exactly -- `updated_at 17:06:20Z`.

`pull_log` 20261018T170612Z: **8 requests, 4 ReferenceDataRequest + 4 HistoricalDataRequest**, 159
security x field requests over 1 security.

### Two numbers I declined to round off

- **"Points" is not 159.** 159 is security x field REQUESTS; the pull_log's shape does not record the
  historical day expansion (`start`/`end` read None), so a CELL count is not derivable from it. I
  reported 159 as what it is and said the cell count is unavailable rather than letting a plausible
  number stand in for a measured one.
- **I first read "0 derived objects"** because I listed `amgt/harvest/derived/model_block/` from the
  docstring's wording. The real key is a TOP-LEVEL `derived/model_block/...`, named authoritatively by
  `status.json`, and a HEAD on it returns 559,911 bytes. **That is the second time this session a
  wrong path nearly became a reported absence** (the first was `.open_deploys/`). The fix both times
  was the same: read the record that NAMES the key instead of guessing its prefix.

## HISTORY ANSWERS -- CTO~Z's point 3

He asked this because `~MDPF1`'s DEMQUE probe returned 0 rows at 14:00Z (Z-S8). **History answers, three
independent ways:** a fresh AAPL historical read returned 3 rows before I started; **4
HistoricalDataRequests** went out in this pull; and the histdata bronze landed at **23,534 bytes**.

So Z-S8's zero was **security-specific** -- a municipal bond with no `PX_LAST` on any form or channel --
and not a history-channel outage. Those two readings would have led somewhere very different, which is
why he asked for the distinction rather than a health flag.
