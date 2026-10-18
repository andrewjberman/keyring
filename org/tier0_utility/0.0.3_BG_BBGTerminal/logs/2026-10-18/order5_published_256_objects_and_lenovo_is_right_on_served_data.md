# ORDER 5: 256 objects PUBLISHED to live G4, and Lenovo now reads correctly on SERVED data

**archetype:** TRACE
**Recorded by:** `0.0.3_BG_BBGTerminal`, 2026-10-18 ~01:2xZ.
**Order:** crossbox `XB-20261018T005221Z-7343` from `2.0.0_SA_COO~RV`, acked 01:04:55Z. This is ORDER 3
act 3, released under BOTH signed never-widen halves: COO @859e4e8799, CTO
`NEVER_WIDEN_ORDER3_HELDTR_PUBLISH_CTO_HALF.md` @98d4271685.
**Deploy ledger:** `etfs-rivalfunds-heldtr-publish-20261018`, L1+L2 closed by me at 01:20:08Z, committed
@986adec61e. **L3 remains OPEN and is not mine.**

## Preconditions, measured before touching anything

Both halves in HEAD (`is-ancestor` true, bogus-hash control rejected). The order required a script "at
or after the commit carrying this file" because it ADDS the `readers` act -- so I checked the dispatch
existed rather than assuming: `heldtr_stage.py:258` maps `"readers": readers`, and the publish
byte-compare prints at `:238`. Layer 256 objects. CTO condition 3's ledger entry present on site Z's
ledger and genuinely OPEN with 3 legs.

## ACT 1 -- readers (CTO condition 1): CLEAN

```
day 2026-10-16 | window 2025-10-15..2026-10-16 | layer dates 254
dramatic_move candidates A 1 B 0 | new in B 0 | gone in B 1 | NEW ON A LAYER DATE (STOP) 0
VERDICT: no new dramatic_move candidate on a held-tr date
```

The condition was that a held-tr close must not MANUFACTURE a dramatic move. It manufactured none, and
it REMOVED one (`gone in B 1`). `bigmove` falls 1 -> 0 in BASG, GQGU, IDVZ, PCLG, PFOE and TSEL --
corroborating the root finding from the other direction: the shifted closes were generating false
move flags, and correcting them clears those flags.

### An exit code I had to go back and measure properly

My first readers run piped to `tail`, so the harness's "exit code 0" was **tail's**, not the python's --
and the order names **exit 3** as its gate. A pipeline exit code is not the gate's verdict, which is the
same class as reading a verdict from a positional slice. I re-ran it UNPIPED: **true python exit 0**, and
the second run reproduced the first line for line. Cost: a few minutes. Justified because the act it
gates is an irreversible served write.

## ACT 2 -- the SERVED write

```
dry   : objects in layer 256 | new 256 | present-and-equal 0 | present-and-different 0   (exit 0)
        256 PLAN lines, ALL on s3://.../rivalfunds/etfs/gold/security_market/date=
        no DIFF / REFUSED / ERROR / Traceback in 258 lines
apply : objects in layer 256 | written 256 | skipped (exist) 0 | apply True              (exit 0)
```

I swept the WHOLE dry-run file by token rather than reading the summary line alone: a single DIFF row
among 256 PLAN lines would have been invisible in a preview, and the order says a DIFF means stop. I
also counted that all 256 targets sit on the intended prefix -- that is the blast-radius check, and it
matches the CTO half's "256 objects, NEW only, a present uri skipped never overwritten".

## THE VERIFICATION THAT MATTERS, independent of the producer

`NEVER trust a producer's self-report or rc=0.` The script's own read-back is its self-report, so:

- **Live G4 object count 266 -> 522, exactly +256.**
- **992 HK Equity read through `hc.g4_rows` on LIVE S3**, the real merge a consumer uses:

| date | served now | BDH truth | the shifted value it replaced |
|---|---|---|---|
| 2026-10-12 | **32.34** | 32.34 | 31.10 |
| 2026-10-13 | **31.10** | 31.10 | 30.40 |
| 2026-10-14 | **30.40** | 30.40 | 25.98 |
| 2026-10-15 | **25.98** | 25.98 | 28.06 |

Every row `as_of_source` **held-tr**, and `drop_backfill` KEEPS them, so **the rankings see the price**
(rows=1 per date). That last clause resolves the coverage worry I raised at 35393: where a BACKFILL row
won the merge the rankings lost the price entirely, but held-tr is a non-backfill past-date writer, so
it both outranks the snapshot AND survives the rankings filter.

**Andrew's request is now satisfied in SERVED data, not just a local layer.** The chain from his one
line: Lenovo looks stale -> a one-day shift -> venue-wide -> my own correction that it is capture-TIME
not venue -> RV extends the remediation to 653 securities -> RIV-zb-1 fixes the producer -> 256 objects
published -> the served merge reads true closes.

## What I did NOT do

- **No delete.** The order and both halves are explicit: there is no per-key rollback by any seat;
  removing an object is an S3 delete and Andrew's act alone.
- **L3 not closed.** It is the next page build's verify leg (`holding_contribution` implied days falling
  as act 2 measured, read from the next publish's `price_source` counts). The entry therefore stays OPEN
  legitimately -- that is the manifest's design, not a half-landed deploy. Its 72h window will go RED if
  nobody claims it, so I said so explicitly to the issuer rather than leaving an open entry to be
  misread as my unfinished work.
- **GQGU not diagnosed by me.** I flagged it as an outlier after ORDER 4; the CTO half already carried
  the cause -- its issuer-file keys mostly lack a Bloomberg ticker, so DQ-t-63 excluded them from
  TR-HELD -- and records it as a row for the next round. My flag was worth raising and the answer was
  already theirs.
