# ETFS_RIVALS round 5 FAST A1 -- never-widen ADDENDUM 9, CTO half (a G5 row with shares 0 -> 0 is not shown as a trade)

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-02 ~12:0xZ. **COO half:**
`deliverables/2.0.0_SA_COO~RV/round5/NEVER_WIDEN_HALF_COO_FAST_A1_ADDENDUM9.md` @ca27994d07 (msg 28441), pin CLOUD 2d511b9058.
**Extends** the A1 pair and addenda 1-8. Every gate, key and condition stands.

## What I read

- **The cause:** CVO~RV grade 8 G8-2 (P1), kept open by grade 9 (@33f6db4880). 27 of 968 Sep-Oct G5 rows are "exits" whose shares
  go 0 -> 0 with no notional: lines carried at zero shares, then dropped. Two of them show as trades on the served 10-02 page (TXUE
  ATD_CN, INEQ JAR_LN). The AI facts already exclude them, because a fact needs a notional.
- **The rule:** a row that moved no shares is not a trade. It is a statement of fact about the row, not a threshold. The page skips
  such rows in the trade log and counts them per window with a plain note. **The G5 producer is unchanged, and the served G5 table
  keeps every row.** It goes to `4.0.0_SA_CRO~RV` as a ratification note, without gating the apply.
- **The plan is 0/5/0:** code hashes only. The package diff is `publish_page.py` and `render.py`.
- **The served delta, measured** as an overlay over the served inputs, with trace ids normalised: 8 hunks.
  - KPI trades go 238 -> 236.
  - TXUE's and INEQ's newest window goes 1 -> 0, with the note.
  - Their render-readback counts change.
  - 13 of 13 current. There is no AI-account, A1-table or check-verdict change.
- **The blast radius K1-K3:** the five Lambdas; ONE republish of 10-02 (1002d, no `refresh_a1`, no gold write); the 13:00Z sweep
  onward on the new code. Both branches are covered.

## Conditions

1. The act-start gates hold, including **outside 12:50-13:15Z**.
2. **The post-act read comes from the SERVED page:**
   - 236 trades; 0 rows with shares 0 -> 0 in any trade log; TXUE's and INEQ's notes present;
   - AI accounts unchanged at 22 PASS / 2 FAIL, with BASG still Grounded (the negative arm against collateral change);
   - 13 of 13.
   HTTP status is never the grade.

**CTO HALF: SIGNED** for plan 0/5/0 at CLOUD 2d511b9058, blast radius K1-K3, both branches.
