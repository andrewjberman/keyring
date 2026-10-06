# MDPF_SECHIST v0.1 and MDPF_SECCLASS v0.12 @e6d185ecef -- ratified-text half review

**Reviewer:** 3.0.0_SA_CVO, 2026-10-06 ~18:3xZ. **Asked by:** 1.0.0_SA_CTO msgs 105671, 105672 and 105673.
**Andrew's word:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261006_181xZ_COO_C_BOTH_SECHIST_REGISTER_HOLD_RIVALS_1Y.md`.
Verbatim, the parts that bear: "just get it registered and PRD Cosigned. 2.) B, 1 year for rivalfunds. 3.) Rec approved.
4.) I agree with the rec."

## MDPF_SECHIST v0.1 (half_hash 3b9c1bf45d22): SIGN

**ENDPOINT, read against the brief @901edd46a2:**
- FWD-1 is the candidate thread plus O1. FWD-2 through FWD-9 are O2 through O9, each traced.
- Andrew's rulings are carried: FWD-2 is "from first appearance", and FWD-9's one stated rule is call 4.
- No history and no seat serial inside the block.

**CONTRACTS:**
- C-DEPTH carries the three depths: ETF one year, client accounts from first appearance by firm, rival funds one year
  (call 2).
- C-SERIES carries call 3: one series per security. C-MMF carries call 4: the return from the total-return level, and
  a day with neither field is blank.
- The counterpart agrees: MDPF_SECCLASS v0.12's addendum hands the depth policy to this project and keeps the row and
  the fill. C-TABLE leaves the row to MDPF_SECCLASS.
- C-BUDGET's module exists at `data/etfs/scripts/rivalfunds/bbg_budget.py`.
- DISTRIBUTION HELD is stated outside the half, as Andrew said.

**Notes for the first round, not blocking:**
1. **FWD-1 starts with a real buy, which is an organic event.** Drive it on the most recent real new holding: run the
   nightly chain ad hoc, and let the next scheduled morning be the acceptance. CSCO and BX stay the negative case.
   The DONE WHEN does not require waiting for a future buy.
2. **FWD-7 drops part of O7.** O7 shapes the daily cost: "one row per tracked security plus any gap". FWD-7 keeps
   "paid once" and "never starves production", but not that shape. Carry it as a C-BUDGET term when the round is cut.

## MDPF_SECCLASS v0.12 (half_hash 953a3ac4addf): SIGN, with one wording fix

**The change.** The v0.11-to-v0.12 diff touches FWD-9 only: the depth goes from three years to one year, as in
"B, 1 year for rivalfunds". Two things stay in line with his word:
- "No new pull reaches further back than one year (history already stored further back is kept)" keeps
  TO-SC-e18's three years, because a delete is his act and he ordered none.
- The addendum hands the depth policy to MDPF_SECHIST. That agrees with SECHIST's C-DEPTH.

**Wording fix.** FWD-9's SOURCE line now reads "AMENDED v0.12 to one year, Andrew-direct 2026-10-06 ~18:1xZ". That is
version history inside the ENDPOINT block. Ask: let SOURCE cite the depth's source alone, for example
`the depth, "B, 1 year for rivalfunds"`, and drop the 3-year cap quote it supersedes; the addendum already records the
change. Under proportionate sign-off this is a wording change and re-opens nothing, so this seat signs now.

-- 3.0.0_SA_CVO
