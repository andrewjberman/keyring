# NFRA_CTLPLN -- ROUND-27 ANALYSIS (1.0.0_SA_CTO, 2026-10-16 ~10:1xZ)

**On:**
- the issuer's `L8_PACKET_ROUND27.md`, `ROUND27_INPUTS_FOR_ROUND_ANALYSIS.md` and `ROUND27_ADVANCED_FWD_SHORT_ACTS.md` @7f8eee22dc;
- the CVO's `ADJUDICATION_v31.md` @e401bbec00 (msg 109660).

**PRD:** v0.31 (ADMITTED).

## 1. FWD coverage (CVO v31)

| grade | count | FWDs |
|---|---|---|
| REALIZED | 10 | 1, 3, 5, 15, 16, 17, 18, 19, 24, 28 |
| ADVANCED | 14 | 2, 4, 6, 7, 8, 10, 11, 12, 14, 21, 22, 23, 25, 27 |
| PARKED | 1 | 9 |
| MOVED | 3 | 13, 20, 26 |

The package route served its first organic consumer. dell2's resident host received the yfinance==1.2.0 Linux closure: 17
wheels, 52 of 52 files equal to the manifest (record 40b21e0a58).

## 2. Rulings

1. **FWD-11: neither (a) nor (b) first. A real whole-box restart already happened mid-round, and the CVO reads it.**
   - The laptop rebooted overnight on 2026-10-16 while NFRA_CTLPLN round 24 was ISSUED and its worker `~126` was in flight.
     The worker died with the session after committing code and tests.
   - After the reboot, the next COO re-seated the slot on the same branch, wrote the proof instance, and the round drained to
     MAY-CLOSE (`L8_PACKET_ROUND24.md` @52567a1a41, header paragraph).
   - The CVO reads that record against FWD-11's DONE WHEN ("one box restarted mid-round, and the round finished") and ACCEPT
     ("the next person to look can say which round was where ... without work being redone or lost").
   - If the CVO grades it short, this seat takes (a): a deliberate whole-box reboot of one box, with a round in flight and no
     worker in flight. That waits on Andrew's confirmation that his 2026-10-14 hold on a whole-box reboot is spent; it is his
     word. (b), narrowing the ENDPOINT, is NOT taken: the outcome he ratified is box-level.
2. **The intake README page: YES.** The issuer cuts one page in the intake folder: "what the tools demand of the approval file
   and the signed file". It covers:
   - the exact `name==version` line;
   - every wheel's file name in the signed file;
   - the `CHECK 8 SIGNED` line;
   - the `WAIVE <file> check <N>: <reason>` form (never checks 1-2);
   - the dry-run command each tool offers.
   The issuer also dry-runs every gate on every line before a cut (its own stated miss).
3. **Check 6 becomes platform-aware, so the waiver stays exceptional: YES, one cell.**
   - When `compared_across_platforms` is true, check 6 compares after CRLF normalisation and after removing a
     `# start delvewheel patch ... # end delvewheel patch` block.
   - It passes when the only residual is a file on a named, short build-metadata list (`numpy/__config__.py` and the like),
     each one listed in the record.
   - Any other residual FAILS as today.
   - Tests: the four yfinance wheels pass on the new rule with no waiver; a planted edited line still fails.
   - The four existing waivers stay on their records as issued.
4. **FWD-7 (the 58 cross-box write overlaps).**
   - The ACCEPT clause ("two on different boxes change different files") is read over PROJECT write surfaces.
   - Shared append-only carriers (deploy-ledger sentinels, audit logs, surprise channels, the open-calls lists) are excluded;
     every box writes them by design and box-sync resolves them.
   - The issuer classifies the 58 into shared-carrier and project paths and reports the project-path overlaps alone. Zero
     project overlaps is the evidence for the CVO; any non-zero count becomes a cell.
5. **No act needed, CVO reads:** FWD-4 (pair one round-close commit with its integrate commit, for two boxes), FWD-12
   (`XB-20261008T203134Z-a3f0`) and FWD-22 (one closed own-box call and one XA file from both sides).
6. **Andrew's acts, carried:**
   - FWD-2 (a real new machine; a register-copy stand-in is NOT accepted, because the DONE WHEN names a seat started on it);
   - FWD-6 (a client-facing PROD push held until his word);
   - FWD-14 (`b87f`);
   - FWD-27 (logins from rc and muse, and from off the tailnet).
7. **Issuer's item 6:** both scratch-folder pairs are already deleted on his word. dell1 read them back absent (msg 109627) and
   site Z closed `ae72`. Nothing is owed.

## 3. ENRICHMENT LIST for round 28 (one issuance)

1. Check 6 platform-aware (ruling 3), with its tests.
2. The intake README page (ruling 2).
3. FWD-7: classify the 58 overlaps (ruling 4).
4. FWD-8: the E8 conflict read over a window in which two boxes each close a full round.
5. FWD-23: dell1, dell2 and site Z each write `seats.json`. These are cross-box calls to their MSTRs.
6. FWD-25: one real spawn of each seat kind on one box, each asked what it is, recorded. This is `0.0.0_AB_MSTR` via
   `/mstr-spawn`.
7. **Held for a later round:** FWD-10 (a deliberate Dell deploy, plus a real refused delete and a refused audit-trail write)
   and FWD-21(a) (a deliberately hung seat on an unwatched box). Each needs its box CTO's word and a quiet window.
8. **CVO:** FWD-11 (ruling 1), FWD-4, FWD-12 and FWD-22 (ruling 5).
