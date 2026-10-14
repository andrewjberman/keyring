# ADVI_COTBKF round 85 -- L9 grade of one judgment criterion

**Grader:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-14 ~00:3xZ. **Asked by:** msg 7365, packet
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_85_DRAIN_END_20261014.md` @5e404034c4. The rounds
83-84 grades the message calls owed were already given at 23:52Z (`ADVI_COTBKF_ROUNDS_83_84_L9_GRADE_20261014.md`, @6b9f2b985d).
**Result: CB85cg1-AC3 PASS, with one finding that graduates.**

## CB85cg1-AC3 -- PASS

Record: `deliverables/0.9.0_WK_ADVI_COTBKF~168/ACTIVE_SET_V2_RECORD.json`. I also recounted the two committed files from @4d427d3bbb.
- **"Active" is the CTO's, defined before it is counted, and shown against both other sets.**
  - Open means non-null, non-zero units in the 2026-10-12 snapshot, cash included: 860 accounts.
  - Against round 82's 769: +91, the cash-only accounts.
  - Against the 90-day 875: -15 by count; as sets, 85 accounts are only in this set and 100 only in the 90-day set.
  - The 139 accounts with only zero or null units are counted separately.
- **Every window respects its bounds.** My recount of `ACTIVE_COTTONWOOD_SET_V2.csv`: 41,826 rows, earliest `held_from` 2013-04-08,
  0 clipped by the floor.
- **The reverse match drops no account, and every `none` row carries a list code.** My recount of `REVERSE_MATCH_V3.csv`:
  - 860 rows: 460 crosswalk-matched, 13 near, 387 `none`.
  - The 387 `none` rows: 168 NEW_CLIENT_AFTER_MIGRATION, 101 MISMATCH_NO_IDENTIFIER, 91 OTHER (sub-code NO_CANDIDATE_OVERLAP in the
    record), 27 AMBIGUOUS.
  - All 860 keys are 11 characters (raw ids, one key space).
  - The partition test now runs as the list defines it, on raw keys (W168-S5).
- **The invariants are printed with their results, and no DIFF is forced.**
  - 9 of 15 match. The 6 DIFFs were measured on the SAME 769 accounts, so the new definition does not explain them; the CTO's premise
    that it does is wrong.
  - The worker attributes the DIFFs to the round-82 side: its window script was never committed and its keys were tokens with a lost
    salt, so no committed rule reproduces its counts. That explains why the two cannot be reconciled, not where each row differs.
  - It is the honest answer available, and nothing was bent to match.
- **The four identifiers are answered.** One row each in the new set; 38150V6Q7 carries a zero-unit row in the latest snapshot.
- **No account number appears in the committed record.** The two committed CSVs carry raw ids under Andrew's 2026-10-09 word and the
  CTO's exemption, pinned by path and sha256.

## Which side of the 6 DIFFs I trust (the issuer's question, row W168-S2)

**Round 85's.** Its rule is written out in the record: held means non-zero units, plus the window open and close rules and the join rule.
Its keys are raw ids anyone can join. Its files are committed with checksums. Round 82's counts come from a script nobody can run and
keys nobody can join, so they cannot be checked. A figure that cannot be reproduced does not outrank one that can be. Retire round 82's
window counts as unreproducible.

**But round 85 has the same exposure.** Its build ran from `.scratch/cb/build.py, assemble.py, final.py, emit.py, record.py`, which is
gitignored and not committed (the proof of spec says so). That is exactly how round 82's method was lost. Before the park, commit those
five scripts and re-run them once to reproduce the two files' sha256. Otherwise the next comparison against round 85 meets the same wall
this one did. This is row W168-S2's remedy (REMEDIATION_v51).

## Worker deviations

The worker read the round-82 order whole, including its record face (a read). Two rail denials were not retried. No write, no `sts`,
and neither the private folder nor the salt was searched. No deviation changes the grade.

-- 3.0.0_SA_CVO
