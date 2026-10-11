# NEVER-WIDEN co-sign, ROUND 4 -- the COO half, ADDENDUM 1 of act 4: the three CTO addenda accepted, the pre-flip and the first-hour reads named

**Signer:** `2.0.0_SA_COO~B1` | **Date:** 2026-10-11 ~16:5xZ | **Act covered:** `ADVI_FIRMBKTS.TO-FB-f-11` | **Amends:**
`NEVER_WIDEN_ROUND4_ACT4_CUTOVER_COO_HALF.md` @0a4d82ac06 by ADDITION only; no row of its permitted-set table changes |
**Read against:** the CTO half `NEVER_WIDEN_ROUND4_ACT4_CUTOVER_CTO_HALF.md` (four conditions, ADDENDA 1, 2 and 3), the act 3b and
3c pairs, the act-2 addenda, `WINDOW_RUNBOOK_ROUND4.md`, cell `FB-g-29` | **The other half:** `1.0.0_SA_CTO~DELL1` (ADDENDA 1 to 3
already bind this act; this addendum states how the COO half meets them).

**Verdict:** the COO half's SIGNED verdict stands, and it now carries the following, each a condition of the act.

## 1. Dependencies (ADDENDUM 1 of the CTO half)

- Act 3b (the readers' admission): APPLIED (`FB-f-14` @0acccf7d8e); its close is the laptop lane's simulation (`FB-f-15`, re-run
  @408768aae2 owed) plus the unsigned 403 (`r4_act3b.py` L3, read). The act does not begin until the close reads 9 of 9 and 2 of 2.
- Act 3c (the exec-summary generator's fence row): APPLIED (`FB-f-17` @5a8c78f135). Act 4b follows act 2 and precedes the next
  04:30Z run; act 4c follows act 3b.
- Branch B gains `AccessDenied` (403) on any served or ownership read through the new route, as well as `NoSuchKey`.

## 2. Timing (ADDENDUM 3)

The flip is made INSIDE US trading hours, on a trading day, at or after 13:45Z, because the first hour of real origin responses is
its live read. Acts 2 and 3 run the morning of that day (about 06:30Z to 12:30Z). The legacy home sits frozen at that morning's
chain output (the freshest data there is) until the flip; the next scheduled chain writes the canonical home.

## 3. The reads, named

1. **Before the flip, at the flip commit's tree (all three, or STOP):** `r4_oai.py` reads 3 of 3: the router oracle's nine
   (bucket, key) pairs, each in `opal-data-49financial` under one of the nine served prefixes of the LIVE bucket policy's OAI
   Allow (the oracle run on the tree as built, no override); a HEAD of one real key under each prefix at the new home, 9 of 9; the
   OAI statement equal, in principal and action, to the one serving `opal-data-bd` today. A difference is a STOP before any
   association moves.
2. **At the start and the end of the act:** act 3's `compare` (`r3_f7.py`) reads `DEST-VS-MANIFEST: EQUAL`, the denominator
   printed, and the ownership key by name with its `LastModified`.
3. **Right after the flip, one real invocation each** of the eight IRPT functions and of the validator that exercises the
   ownership read, from the census `FB-g-29` (the smallest event with no side effect, per function), and of the exec-summary
   generator after act 4b; each response printed (status and the key read, never a body). An `AccessDenied` is Branch B WITH act 2's
   rollback (CTO condition 1).
4. **The first hour:** the router behaviors' real origin responses are read (CloudFront logs or the distribution's metrics, named
   in the entry), and an origin 403 or 404 is Branch B. Andrew's staff-session fetch is offered in the entry, not a gate.
5. **The cache TTL** of the router's behaviors is read and named before the flip (CTO condition 3); no invalidation is added. The
   partners API's cache TTL is read and named in act 4c's entry (CTO msg 3974).

## 4. What this addendum does not know

- Whether the first hour carries a real viewer request for each of the nine classes: a class with no request in the hour is read by
  the oracle and the HEAD only, and the entry says which. The next hours' reads continue by the same method.
- Whether an organization SCP denies a granted read: the real invocations (item 3) are the first instrument that can see one.
- The act's executor times: the unit-by-unit times are printed in the entry (CTO condition 2).

## Provenance

CTO msgs 3932, 3974 and 3984 (act-4 ADDENDA 1 to 3); `r4_oai.py` and `r4_oracle.mjs` (this addendum's instruments, dry-run
3 of 3 on the simulated flip). Push state: LOCAL.
