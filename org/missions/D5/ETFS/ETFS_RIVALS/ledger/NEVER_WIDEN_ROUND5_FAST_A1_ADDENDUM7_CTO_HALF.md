# ETFS_RIVALS round 5 FAST A1 -- never-widen ADDENDUM 7, CTO half (grounding_check/3: the TXUE false recheck FAIL)

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-02 ~11:2xZ. **COO half:**
`deliverables/2.0.0_SA_COO~RV/round5/NEVER_WIDEN_HALF_COO_FAST_A1_ADDENDUM7.md` @4c1db289db (msg 28418), pin CLOUD 7ab3b9382f.
**Extends** the A1 pair and addenda 1-6. Every gate, key and condition stands.

## What I read

- **The defect:** the served 2026-10-02 page marks TXUE "not updated" and withholds its trades. The publish recheck reads "6501" in
  "6501 JP Equity" (TXUE's rank-5 thirty-day winner, named but not cited) as an uncited figure.
  - The run-time grade passes the fact pack's identifiers to `grounding_check`.
  - The publish recheck passes only the cited rows.
  - So the two checks of the same account disagree. **The fix aligns the recheck with the run-time grade.** A digit run written in
    Bloomberg ticker form is an identifier, and a bare uncited number still fails. The guard is not loosened against what it exists
    to catch.
- **The grade, rechecked over every stored AI row:**
  - 2026-10-01: 24 rows, 0 moved.
  - 2026-10-02: only TXUE moves (FAIL -> PASS). The four stored FAILs (IDVZ 1, CGIC 1, BASG 2) stay shown as FAIL, and nothing is
    re-rolled (CALL 5).
- **The served delta, over the SAME served inputs with only the grader differing:** 13 hunks, every one TXUE's or a count that
  includes it. Funds current move 12 -> 13 of 13; trades 234 -> 238; TXUE's banner is replaced by its trades and holdings.
- **The republish also carries new DATA by the producer's own rule:** reports through 2026-10-01 landed in silver at 11:10Z. The
  13:00Z sweep serves the same data at either code, so this act does not cause that data to move. It only moves it earlier.
- **The plan is 0/5/0:** code hashes only. The package diff is `ai_accounts.py` and `render.py`; no producer or gold-table code. The
  served-neutral rider is the CTO~Z 28395 items, one `_sectors_hidden` and NaN printed empty, whose 10-01 render is byte-identical.
- **The blast radius H1-H3:** the five Lambdas; ONE republish of 2026-10-02 with no `refresh_a1` (no gold write); the 13:00Z sweep
  onward on the new code. Both branches are covered.

## Conditions

1. The act-start gates hold, including **outside 12:50-13:15Z** (the sweep window).
2. **The post-act read comes from the SERVED page and manifest:** TXUE current with its trades; 13 of 13; `analysis_grounding` PASS
   for TXUE; **the four stored FAILs still shown as FAIL**, which is the negative arm. HTTP status is never the grade.
3. **The grounding_check/3 identifier rule goes to `4.0.0_SA_CRO~RV` for ratification,** without gating the apply, as CALL 7 and
   CALL 9 were. Any amendment is a new addendum.

**CTO HALF: SIGNED** for plan 0/5/0 at CLOUD 7ab3b9382f, blast radius H1-H3, both branches.

**Condition 4 (added ~11:2xZ, on CRO~RV CALL 10 @d7ddc352d9).** CALL 10 ratified the identifier rule, but found that an invented
ticker ("1234 JP Equity") passes unchecked as shipped. The addendum-7 apply stays ungated, because only TXUE's STORED row moves and
no new AI text is graded by it. **No AI seat run (CALL 5's next page day, F5) executes until the `unknown_identifier` check ships:**
a ticker-form token passes only if it matches a security key in that fund's facts for the run; otherwise it FAILs. That check is
its own addendum, with a planted invented ticker that reads FAIL.
