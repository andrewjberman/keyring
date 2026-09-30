# NEVER-WIDEN -- CTO HALF -- AMGT_HARVST round 30, `HVST-ac-3` (the paired `chatter_daily` rebuild carrying ab-2's pairs) -- `1.0.0_SA_CTO~Z`, 2026-09-30 ~17:5xZ

**Against:** `deliverables/2.0.0_SA_COO_H/round30/NEVER_WIDEN_HALF_COO_AC3.md` @`f406a6106b` (msg 27302, READ-acked; read to EOF,
4,974 B).
**Ruling it serves:** round-29 analysis ruling 4 and section 4 item 3 (@`d0bc0a79f0`).

## VERDICT: SIGNED

## 1. RE-MEASURED BY THIS SEAT (own instrument)

- **Script:** `ctoz_ac3_pairs.py`, in this seat's scratchpad. It reads both gold mention parts under
  `amgt/harvest/gold/article_security_mention/date=2026-09-30/` from S3 (the listing is paged, 2 parts) and diffs the
  (`article_key`, `security_key`) pairs.
  - It found **21 added pairs on 11 articles**, which equals the CVO's v38.
  - **The added pairs dated inside the page window are exactly five:**

    | security | day | story |
    |---|---|---|
    | 992_HK | 2026-08-13 | bbg `TJP0ADKJH6V500` |
    | AAPL | 2026-08-13 | bbg `TJP0ADKJH6V500` |
    | C | 2026-08-13 | bbg `TJP0ADKJH6V500` |
    | MU | 2026-08-13 | bbg `TJP0ADKJH6V500` |
    | 992_HK | 2026-09-01 | bbg `TKPBVYKK3NY800` |

  - The other 16 pairs are dated 2015-2019, before any page day.
- **This seat's "the 992_HK days ... and nothing else" (round-29 analysis s.4 cell 3) was WRONG.** It predicted the outcome from the
  input's shape, which a half forbids (CLAUDE.md NEVER-1: the outcome is read from the producer's rule). The 08-13 story names three
  more covered companies.
  - **The COO half's widening is CORRECT and ACCEPTED.** Its 5 expected rows equal this read.
  - This seat's analysis line is superseded by the half.
- **Code:** `git diff --stat 0814b408e4 HEAD -- lib/research lib/opal_naming.py` is **empty**. The code at this signing is the code
  the COO half signed. The COO half's predecessor diff runs from `717cbb0a14`, which built the served part `121049Z`. That is the
  right predecessor.
- **The move ledger is coherent:**
  - 53 moves on the 5 rows;
  - 486 rolling-field consequences, which only move on later days of those 4 securities;
  - OTHER 0;
  - 52,143 rows with 0 new keys.

## 2. CONDITIONS

1. **Act-start gate:** as the COO half.
   - The newest part is `121049Z`.
   - The dry-run digest `a71ca3f966e89965` and 49,679 bytes are reproduced.
   - The `lib/research/harvest` diff is re-printed empty.
   - `--as-of 2026-09-30`, and the act starts before 00:00Z. A later as-of adds keys, so STOP.
2. **The positive arm before the act** (RESAPP round-53 ruling 1): run `ac-3.AC1.py` and `ac-3.AC2.py` against the CAPTURED dry-run
   part, as the simulated post-state. Both must PASS: exactly the 539 signed moves; `bbg` in the 5 rows' found codes in the in-process
   route read. This is beside the base FAIL the half already shows. A check that cannot pass on the intended part is not a check:
   STOP.
3. **After the act:** AC1 and AC2 PASS on the written part. Any move outside the 539: STOP and name it.

## 3. ROLLBACK

Forward only. Readers take the newest part, and the prior 10 parts stay. A delete is Andrew's act.

## 4. NOT COVERED

- the deployed scoped-API build's carriage of `q-5` (the found codes on the served route);
- the chatter producer's gold branch, which HOLDs `NO_DECLARED_PUBLISHER`;
- every other date partition.
