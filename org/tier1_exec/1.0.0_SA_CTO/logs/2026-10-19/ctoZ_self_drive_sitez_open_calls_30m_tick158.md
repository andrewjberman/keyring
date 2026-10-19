# 1.0.0_SA_CTO~Z -- /self-drive 30m sitez open calls, ticks 157-158 (2026-10-19 05:58Z to 06:57Z)

**archetype:** COORDINATE

Arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261016_024xZ_SELF_DRIVE_30M_SITEZ_BOX_OPEN_CALLS.md` @b155c4c03a.
Session cron e6b088c9. **state: ARMED**

## Signed

- **OG-ap-48, the twelfth release (the CTO half)** @2f57a5ef26. Bound to ask 942e7f6a3f0d (re-hashed) and release 6b1a9bd292 on live
  e09c30c3f0.
- **Own reads:**
  - the release's parent is e09c30c3f0;
  - 2 files, +106/-3: `app/audit.py` (exactly round-44 item 2, OG-pr-6) and `tests/test_og_pr6.py`;
  - the 4 harvest blobs and `graph.py` are equal to live;
  - the put call itself is unchanged.
- **Discrepancy accepted:** `retries={"max_attempts": 1}` gives TWO sends (measured `total_max_attempts` 2).
  - The worst case is about 10 s on the loop, against the default 120 s over 5 attempts.
  - The comment fix, or `total_max_attempts: 1`, is carried to the next `audit.py` release.
- **Conditions:**
  - CT1: the base.
  - CT2: the carried md5s.
  - CT3: three counts. Journal `POST /mcp`, lake records, and the journal's `audit-lake WARN` lines, expected 0. A non-zero WARN
    count is reported, not rolled back.
  - CT4: tools/list 103; 27 of 27; unarmed.
- **The CVO half was SIGNED @c57a121b47** (msg 35910).
  - Its finding 2: an immediate rollback on WARN would re-hide a lake failure. This agrees with my CT3.
  - Relayed to 2.0.0_SA_COO~O, with the ask to align the ask's triggers. **Three halves are in hand.**

## Box state

- Commit free 31,572 MB (06:27Z) and 33,864 MB (06:57Z). 8 claude.exe alive.
- **Bloomberg sign-in:** the 09:00Z cutoff stands (ruled 04:10Z).

## Open calls

- 0 forks.
- 4 open `act` rows, which only Andrew can do: f0d2, 8ed7, def4 (postponed by Andrew) and 5b35.
- Plus the Bloomberg Terminal sign-in, which has the 09:00Z cutoff.

## Compiler Tools

| tool | used for | result |
|---|---|---|
| sha256sum / git diff / rev-parse | OG-ap-48 half | parent, 2 files, carried blobs equal |
| grep (the ask) | process-wide line, retry measurement | present, 2 sends measured |
| grep (CVO half) | binding | 2 hits |
