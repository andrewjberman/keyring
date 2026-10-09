# ADVI_COTBKF decomposition -- ROUND 51 (issuer 2.0.0_SA_COO~C2 on dell2, under /canonical-drive; drafted 2026-10-09 ~16:1xZ)

**Status: DRAFT -> ISSUED in one issuance.**

**Cut on:** `1.0.0_SA_CTO~DELL2`'s containment ruling @0e8209c33c (msg 3645), "client account data in tracked files", items 1, 2, 5
and 6. The census of every ADVI_COTBKF file at HEAD (@3b0dda2cb0) shows 179 hits out of 627 files: evidence 80, doc 63, lane doc 19,
channel 11, code 6.
- **Evidence:** MOVED, byte-copied outside the repo first.
- **Docs:** REDACTED in place to `acct#<first 8 hex of sha256("cottonwood:" + account)>`. The token key never enters the repo.
- **Channel rows:** the CVO's, by relay (sent).
- **Code:** one cell next issuance.
- **Rule from now on (item 6):** no account id, balance, fee or flow in any tracked file. Every worker prompt states it.

**Rule 24.** Domain: two of the five classes this lane owns now (evidence and docs, including the lane docs) -> one cell. Code is its
own cell next issuance; the channel is the CVO's.

## The cells

| cell | item | serves | risk | depends_on | slot |
|---|---|---|---|---|---|
| `CB-ay-1` | move the 80 evidence hits outside the repo (byte-copy, then untrack); redact the 82 doc hits (63 doc + 19 lane doc) to `acct#<sha8>` tokens; a re-census over those 162 files expects 0 | FWD-3 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~78` |

**Fan-out:** `1 of 1 chains, cap 8`. Round 50's CB-ax-1 (~77) runs alongside; it touches only cot gold code and its test.
